# -*- coding: utf-8 -*-
#@+leo-ver=4-thin
#@+node:edream.110203113231.302:@thin __wx_gui.py
#@@first

"""A plugin to use wxPython as Leo's gui."""

__version__ = '0.5' # Start of development with Leo 4.4.2 code base and wxWidgets 2.6.3

#@<< known bugs & incompletions >>
#@+node:ekr.20070104114159:<< known bugs & incompletions >>
#@@nocolor
#@@color
#@+at
# 
# - Many unit tests presently fail.
# * The gui methods should return dummy values when unit testing is in effect.
# 
# First:
# * Eliminate s_ctrl from Leo's core find logic.
# * Make minibuffer functional.
# * Use stc for body text.
# - Fix focus-to-outline and other focus commands.
# 
# Later:
# 
# - Outline pane beeps on control-characters.
#     - I don't know how to fix this.
# - k.masterCommand is slow.
#     - Make default bindings when creating the widget.
#     - Only override those bindings when in a state.
#     - With some luck we should be able to avoid key-up/key-down bindings 
# (they are buggy).
# - Syntax coloring causes flash even when nothing is colored.
# 
# 
#@-at
#@-node:ekr.20070104114159:<< known bugs & incompletions >>
#@nl
#@<< version history >>
#@+node:ekr.20050719111045:<< version history >>
#@@nocolor
#@+at
# 
# 0.1 EKR: Initial version ca: 2003
# 0.2 EKR: Works with Leo 4.3.
# 0.3 EKR: Ran script to put 'g.' in front of all functions in leoGlobals.py.
# 0.4 EKR: Now starts without crashing with 4.4.1 code base.
# 0.5 EKR: The beginning of the new wx plugin.
# - Converted wx.wxWhatever to wx.Whatever.
#@-at
#@nonl
#@-node:ekr.20050719111045:<< version history >>
#@nl
#@<< imports >>
#@+node:edream.110203113231.303:<< imports >>
import leoGlobals as g
import leoPlugins

import leoColor
import leoCommands
import leoFind
import leoFrame
import leoGui
import leoKeys
import leoMenu
import leoNodes
import leoUndo

import os
import sys
import traceback

try:
    import wx
    # The RichTextCtrl does not exist on windows, but the plain TextCtrl widget can use native Windows RichText widgets.
    # for space,name in ((wx,'wx'),(wx.wx,'wx.wx')):
        # aList = list(dir(space))
        # aList.sort()
        # print '---- %s' % name
        # for s in aList:
            # if s.lower().find('rich') != -1: print s
    
except ImportError:
    g.es_print('wx_gui plugin: can not import wxPython')
    raise # Tell the plugins manager that we did not load properly.
#@nonl
#@-node:edream.110203113231.303:<< imports >>
#@nl
#@<< constants >>
#@+node:edream.110203113231.259:<< constants  >>
cSplitterWidth = 600

const_dict = {}
const_lastVal = 100 # Starting wx id.

def const(name):
    
    """Return the wx id associated with name"""
    
    # Should this canonicalize the label?  Just remove '&' ??
    id = const_dict.get(name)
    if id != None:
        return id
    else:
        global const_lastVal
        const_lastVal += 1
        const_dict[name] = const_lastVal
        # g.trace(name,const_lastVal)
        return const_lastVal
#@nonl
#@-node:edream.110203113231.259:<< constants  >>
#@nl

#@+others
#@+node:ekr.20050719111045.1: init
def init ():
    
    ok = wx and not g.app.gui and not g.app.unitTesting # Not Ok for unit testing!

    if ok:
        g.app.gui = wxGui()
        g.app.root = g.app.gui.createRootWindow()
        g.app.gui.finishCreate()
        g.plugin_signon(__name__)

    elif g.app.gui and not g.app.unitTesting:
        s = "Can't install wxPython gui: previous gui installed"
        g.es_print(s,color="red")
    
    return ok
#@nonl
#@-node:ekr.20050719111045.1: init
#@+node:edream.110203113231.560: Find classes
#@+node:edream.111503093140:wxSearchWidget
class wxSearchWidget:

    """A dummy widget class to pass to Leo's core find code."""

    #@    @+others
    #@+node:edream.111503094014:wxSearchWidget.__init__
    def __init__ (self):
        
        self.insertPoint = 0
        self.selection = 0,0
        self.bodyCtrl = self
        self.body = self
        self.text = None
    #@nonl
    #@-node:edream.111503094014:wxSearchWidget.__init__
    #@+node:edream.111503094322:Insert point (deleted)
    # Simulating wxWindows calls (upper case)
    # def GetInsertionPoint (self):
        # return self.insertPoint
    # 
    # def SetInsertionPoint (self,index):
        # self.insertPoint = index
        # 
    # def SetInsertionPointEND (self,index):
        # self.insertPoint = len(self.text)+1
    # 
    # # Returning indices...
    # def getBeforeInsertionPoint (self):
        # g.trace()
    # 
    # # Returning chars...
    # def getCharAtInsertPoint (self):
        # g.trace()
    # 
    # def getCharBeforeInsertPoint (self):
        # g.trace()
    # 
    # # Setting the insertion point...
    # def setInsertPointToEnd (self):
        # self.insertPoint = -1
        # 
    # def setInsertPointToStartOfLine (self,lineNumber):
        # g.trace()
    #@nonl
    #@-node:edream.111503094322:Insert point (deleted)
    #@+node:edream.111503094014.1:Selection (deleted)
    # Simulating wxWindows calls (upper case)
    # def SetSelection(self,n1,n2):
        # self.selection = n1,n2
        # 
    # # Others...
    # def deleteSelection (self):
        # self.selection = 0,0
    # 
    # def getSelectionRange (self):
        # return self.selection
        # 
    # def hasTextSelection (self):
        # start,end = self.selection
        # return start != end
    # 
    # def selectAllText (self):
        # self.selection = 0,-1
    # 
    # def setSelectionRange (self,sel):
        # try:
            # start,end = sel
            # self.selection = start,end
        # except:
            # self.selection = sel,sel
    #@nonl
    #@-node:edream.111503094014.1:Selection (deleted)
    #@-others
#@nonl
#@-node:edream.111503093140:wxSearchWidget
#@+node:edream.110203113231.561:wxFindFrame class
class wxFindFrame (wx.Frame,leoFind.leoFind):
    #@    @+others
    #@+node:edream.110203113231.563:FindFrame.__init__
    def __init__ (self,c):
    
        # Init the base classes
        wx.Frame.__init__(self,None,-1,"Leo Find/Change",
            wx.Point(50,50), wx.DefaultSize,
            wx.MINIMIZE_BOX | wx.THICK_FRAME | wx.SYSTEM_MENU | wx.CAPTION)
    
        # At present this is a global window, so the c param doesn't make sense.
        # This must be changed to match how Leo presently works.
        leoFind.leoFind.__init__(self,c)
        
        self.dict = {} # For communication between panel and frame.
        self.findPanel = wxFindPanel(self)
        
        self.s_text = wxSearchWidget() # Working text widget.
    
        #@    << resize the frame to fit the panel >>
        #@+node:edream.111503074302:<< resize the frame to fit the panel >>
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.findPanel)
        self.SetAutoLayout(True)# tell dialog to use sizer
        self.SetSizer(sizer) # actually set the sizer
        sizer.Fit(self)# set size to minimum size as calculated by the sizer
        sizer.SetSizeHints(self)# set size hints to honour mininum size
        #@nonl
        #@-node:edream.111503074302:<< resize the frame to fit the panel >>
        #@nl
    
        # Set the window icon.
        if wx.Platform == '__WXMSW__':
            pass ## self.SetIcon(wx.Icon("LeoIcon"))
    
        # Set the focus.
        self.findPanel.findText.SetFocus()
    
        #@    << define event handlers >>
        #@+node:edream.110203113231.564:<< define event handlers >>
        wx.EVT_CLOSE(self,self.onCloseFindFrame)
        
        #@<< create event handlers for buttons >>
        #@+node:edream.111503085739:<< create event handlers for buttons >>
        for name,command in (
            ("changeButton",self.changeButton),
            ("changeAllButton",self.changeAllButton),
            ("changeThenFindButton",self.changeThenFindButton),
            ("findButton",self.findButton),
            ("findAllButton",self.findAllButton)):
                
            def eventHandler(event,command=command):
                # g.trace(command)
                command()
        
            id = const_dict.get(name)
            assert(id)
            wx.EVT_BUTTON(self,id,eventHandler)
        #@nonl
        #@-node:edream.111503085739:<< create event handlers for buttons >>
        #@nl
        
        #@<< create event handlers for check boxes and text >>
        #@+node:edream.111503085739.1:<< create event handlers for check boxes and text >>
        textKeys = ["find_text","change_text"]
        keys = textKeys[:]
        for item in self.intKeys:
            keys.append(item)
        
        for name in keys:
        
            if name not in textKeys:
                name += "_flag"
        
            def eventHandler(event,self=self,name=name):
                box = event.GetEventObject()
                val = box.GetValue()
                # g.trace(name,val)
                setattr(self.c,name,val)
        
            id = const_dict.get(name)
            if id:
                if name in textKeys:
                    wx.EVT_TEXT(self,id,eventHandler)
                else:
                    wx.EVT_CHECKBOX(self,id,eventHandler)
        #@nonl
        #@-node:edream.111503085739.1:<< create event handlers for check boxes and text >>
        #@nl
        #@nonl
        #@-node:edream.110203113231.564:<< define event handlers >>
        #@nl
    #@-node:edream.110203113231.563:FindFrame.__init__
    #@+node:edream.111403151611.1:bringToFront
    def bringToFront (self):
        
        g.app.gui.bringToFront(self)
        self.init(self.c)
        self.findPanel.findText.SetFocus()
        self.findPanel.findText.SetSelection(-1,-1)
    #@nonl
    #@-node:edream.111403151611.1:bringToFront
    #@+node:edream.111503213733:destroySelf
    def destroySelf (self):
        
        self.Destroy()
    #@nonl
    #@-node:edream.111503213733:destroySelf
    #@+node:edream.111503211508:onCloseFindFrame
    def onCloseFindFrame (self,event):
    
        if event.CanVeto():
            event.Veto()
            self.Hide()
    #@nonl
    #@-node:edream.111503211508:onCloseFindFrame
    #@+node:edream.111403135745:set_ivars
    def set_ivars (self,c):
        
        """Init the commander ivars from the find panel."""
    
        # N.B.: separate c.ivars are much more convenient than a dict.
        for key in self.intKeys:
            key = key + "_flag"
            data = self.dict.get(key)
            if data:
                box,id = data
                val = box.GetValue()
                #g.trace(key,val)
                setattr(c,key,val)
            else:
                #g.trace("no data",key)
                setattr(c,key,False)
    
        fp = self.findPanel
        c.find_text = fp.findText.GetValue()
        c.change_text = fp.changeText.GetValue()
    #@nonl
    #@-node:edream.111403135745:set_ivars
    #@+node:edream.111503091617:init_s_ctrl
    def init_s_ctrl (self,s):
        
        c = self.c
        t = self.s_text # the dummy widget
    
        # Set the text for searching.
        t.text = s
        
        # Set the insertion point.
        if c.reverse_flag:
            t.SetInsertionPointEnd()
        else:
            t.SetInsertionPoint(0)
        return t
    #@nonl
    #@-node:edream.111503091617:init_s_ctrl
    #@+node:edream.111503093522:gui_search
    # def gui_search (self,t,find_text,index,
        # stopindex,backwards,regexp,nocase):
            
        # g.trace(index,stopindex,backwards,regexp,nocase)
        
        # s = t.text # t is the dummy text widget
        
        # if index is None:
            # index = 0
    
        # pos = s.find(find_text,index)
    
        # if pos == -1:
            # pos = None
        
        # return pos
    #@nonl
    #@-node:edream.111503093522:gui_search
    #@+node:edream.111503204508:init
    def init (self,c):
    
        """Init the find panel from c.
        
        (The opposite of set_ivars)."""
    
        # N.B.: separate c.ivars are much more convenient than a dict.
        for key in self.intKeys:
            key = key + "_flag"
            val = getattr(c,key)
            data = self.dict.get(key)
            if data:
                box,id = data
                box.SetValue(val)
                # g.trace(key,`val`)
    
        self.findPanel.findText.SetValue(c.find_text)
        self.findPanel.changeText.SetValue(c.change_text)
    #@nonl
    #@-node:edream.111503204508:init
    #@-others
#@nonl
#@-node:edream.110203113231.561:wxFindFrame class
#@+node:edream.110203113231.588:wxFindPanel class
class wxFindPanel (wx.Panel):
    #@    @+others
    #@+node:edream.110203113231.589:FindPanel.__init__
    def __init__(self,frame):
        
        g.trace('wxFindPanel not ready yet')
        return
         
        # Init the base class.
        wx.Panel.__init__(self,frame,-1)
        self.frame = frame
    
        topSizer = wx.BoxSizer(wx.VERTICAL)
        topSizer.Add(0,10)
    
        #@    << Create the find text box >>
        #@+node:edream.110203113231.590:<< Create the find text box >>
        findSizer = wx.BoxSizer(wx.HORIZONTAL)
        findSizer.Add(5,5)# Extra space.
        
        # Label.
        findSizer.Add(
            wx.StaticText(self,-1,"Find:",
                wx.Point(-1,10), wx.Size(50,25),0,""),
            0, wx.BORDER | wx.TOP,15) # Vertical offset.
        
        findSizer.Add(10,0) # Width.
        
        # Text.
        id = const("find_text")
        self.findText = self.leoTextWidgetClass (
            self,
            id,"",
            wx.DefaultPosition, wx.Size(500,60),
            wx.TE_PROCESS_TAB | wx.TE_MULTILINE,
            wx.DefaultValidator,"")
        
        findSizer.Add(self.findText)
        findSizer.Add(5,0)# Width.
        topSizer.Add(findSizer)
        topSizer.Add(0,10)
        
        self.frame.dict["find_text"] = self.findText,id
        #@nonl
        #@-node:edream.110203113231.590:<< Create the find text box >>
        #@nl
        #@    << Create the change text box >>
        #@+node:edream.110203113231.591:<< Create the change text box >>
        changeSizer = wx.BoxSizer(wx.HORIZONTAL)
        changeSizer.Add(5,5)# Extra space.
        
        # Label.
        changeSizer.Add(
            wx.StaticText(self,-1,"Change:",
                wx.Point(-1,10),wx.Size(50,25),0,""),
            0, wx.BORDER | wx.TOP,15)# Vertical offset.
        
        changeSizer.Add(10,0) # Width.
        
        # Text.
        id = const("change_text")
        self.changeText = self.leoTextWidgetClass (
            self,
            id,"",
            wx.DefaultPosition, wx.Size(500,60),
            wx.TE_PROCESS_TAB | wx.TE_MULTILINE,
            wx.DefaultValidator,"")
        
        changeSizer.Add(self.changeText)
        changeSizer.Add(5,0)# Width.
        topSizer.Add(changeSizer)
        topSizer.Add(0,10)
        
        self.frame.dict["change_text"] = self.findText,id
        #@nonl
        #@-node:edream.110203113231.591:<< Create the change text box >>
        #@nl
        #@    << Create all the find check boxes >>
        #@+node:edream.110203113231.592:<< Create all the find check boxes >>
        col1Sizer = wx.BoxSizer(wx.VERTICAL)
        #@<< Create the first column of widgets >>
        #@+node:edream.110203113231.593:<< Create the first column of widgets >>
        # The var names must match the names in leoFind class.
        table = (
            ("plain-search-flag","Plain Search",wx.RB_GROUP),
            ("pattern_match_flag","Pattern Match",0),
            ("script_search_flag","Script Search",0))
        
        for var,label,style in table:
            
            id = const(var)
            box = wx.RadioButton(self,id,label,
                wx.DefaultPosition,(100,25),
                style,wx.DefaultValidator,"group1")
                
            if style == wx.RB_GROUP:
                box.SetValue(True) # The default entry.
        
            col1Sizer.Add(box,0,wx.BORDER | wx.LEFT,60)
            self.frame.dict[var] = box,id
            
        table = (("script_change_flag","Script Change"),)
        
        for var,label in table:
            
            id = const(var)
            box = wx.CheckBox(self,id,label,
                wx.DefaultPosition,(100,25),
                0,wx.DefaultValidator,"")
        
            col1Sizer.Add(box,0,wx.BORDER | wx.LEFT,60)
            self.frame.dict[var] = box,id
        #@nonl
        #@-node:edream.110203113231.593:<< Create the first column of widgets >>
        #@nl
        
        col2Sizer = wx.BoxSizer(wx.VERTICAL)
        #@<< Create the second column of widgets >>
        #@+node:edream.110203113231.594:<< Create the second column of widgets >>
        # The var names must match the names in leoFind class.
        table = (
            ("whole_word_flag","Whole Word"),
            ("ignore_case_flag","Ignore Case"),
            ("wrap_flag","Wrap Around"),
            ("reverse_flag","Reverse"))
        
        for var,label in table:
        
            id = const(var)
            box = wx.CheckBox(self,id,label,
                wx.DefaultPosition,(100,25),
                0,wx.DefaultValidator,"")
        
            col2Sizer.Add(box,0,wx.BORDER | wx.LEFT,20)
            self.frame.dict[var] = box,id
        #@nonl
        #@-node:edream.110203113231.594:<< Create the second column of widgets >>
        #@nl
        
        col3Sizer = wx.BoxSizer(wx.VERTICAL)
        #@<< Create the third column of widgets >>
        #@+node:edream.111503133933.2:<< Create the third column of widgets >>
        # The var names must match the names in leoFind class.
        table = (
            ("Entire Outline","entire-outline",wx.RB_GROUP),
            ("Suboutline Only","suboutline_only_flag",0),  
            ("Node Only","node_only_flag",0),    
            ("Selection Only","selection-only",0))
            
        for label,var,group in table:
        
            if var: id = const(var)
            else:   id = const("entire-outline")
                
            box = wx.RadioButton(self,id,label,
                wx.DefaultPosition,(100,25),
                group,wx.DefaultValidator,"group2")
        
            col3Sizer.Add(box,0,wx.BORDER | wx.LEFT,20)
            
            self.frame.dict[var] = box,id
        #@nonl
        #@-node:edream.111503133933.2:<< Create the third column of widgets >>
        #@nl
        
        col4Sizer = wx.BoxSizer(wx.VERTICAL)
        #@<< Create the fourth column of widgets >>
        #@+node:edream.111503133933.3:<< Create the fourth column of widgets >>
        # The var names must match the names in leoFind class.
        table = (
            ("search_headline_flag","Search Headline Text"),
            ("search_body_flag","Search Body Text"),
            ("mark_finds_flag","Mark Finds"),
            ("mark_changes_flag","Mark Changes"))
        
        for var,label in table:
            
            id = const(var)
            box = wx.CheckBox(self,id,label,
                wx.DefaultPosition,(100,25),
                0,wx.DefaultValidator,"")
        
            col4Sizer.Add(box,0,wx.BORDER | wx.LEFT,20)
            self.frame.dict[var] = box,id
        #@nonl
        #@-node:edream.111503133933.3:<< Create the fourth column of widgets >>
        #@nl
        
        # Pack the columns
        columnSizer = wx.BoxSizer(wx.HORIZONTAL)
        columnSizer.Add(col1Sizer)
        columnSizer.Add(col2Sizer)
        columnSizer.Add(col3Sizer)
        columnSizer.Add(col4Sizer)
        
        topSizer.Add(columnSizer)
        topSizer.Add(0,10)
        #@nonl
        #@-node:edream.110203113231.592:<< Create all the find check boxes >>
        #@nl
        #@    << Create all the find buttons >>
        #@+node:edream.110203113231.595:<< Create all the find buttons >>
        # The row sizers are a bit dim:  they should distribute the buttons automatically.
        
        row1Sizer = wx.BoxSizer(wx.HORIZONTAL)
        #@<< Create the first row of buttons >>
        #@+node:edream.110203113231.596:<< Create the first row of buttons >>
        row1Sizer.Add(90,0)
        
        table = (
            ("findButton","Find",True),
            ("batch_flag","Show Context",False), # Old batch_flag now means Show Context.
            ("findAllButton","Find All",True))
        
        for var,label,isButton in table:
            
            id = const(var)
            if isButton:
                widget = button = wx.Button(self,id,label,
                    wx.DefaultPosition,(100,25),
                    0,wx.DefaultValidator,"")
            else:
                widget = box = wx.CheckBox(self,id,label,
                    wx.DefaultPosition,(100,25),
                    0,wx.DefaultValidator,"")
                
                self.frame.dict[var] = box,id
        
            row1Sizer.Add(widget)
            row1Sizer.Add((25,0),)
        #@nonl
        #@-node:edream.110203113231.596:<< Create the first row of buttons >>
        #@nl
        
        row2Sizer = wx.BoxSizer(wx.HORIZONTAL)
        #@<< Create the second row of buttons >>
        #@+node:edream.110203113231.597:<< Create the second row of buttons >>
        row2Sizer.Add(90,0)
        
        table = (
            ("changeButton","Change"),
            ("changeThenFindButton","Change,Then Find"),
            ("changeAllButton","Change All"))
        
        for var,label in table:
        
            id = const(var)
            button = wx.Button(self,id,label,
                wx.DefaultPosition,(100,25),
                0,wx.DefaultValidator,"")
            
            row2Sizer.Add(button)
            row2Sizer.Add((25,0),)
        #@nonl
        #@-node:edream.110203113231.597:<< Create the second row of buttons >>
        #@nl
        
        # Pack the two rows
        buttonSizer = wx.BoxSizer(wx.VERTICAL)
        buttonSizer.Add(row1Sizer)
        buttonSizer.Add(0,10)
        
        buttonSizer.Add(row2Sizer)
        topSizer.Add(buttonSizer)
        topSizer.Add(0,10)
        #@nonl
        #@-node:edream.110203113231.595:<< Create all the find buttons >>
        #@nl
    
        self.SetAutoLayout(True) # tell dialog to use sizer
        self.SetSizer(topSizer) # actually set the sizer
        topSizer.Fit(self)# set size to minimum size as calculated by the sizer
        topSizer.SetSizeHints(self)# set size hints to honour mininum size
    #@nonl
    #@-node:edream.110203113231.589:FindPanel.__init__
    #@-others
#@nonl
#@-node:edream.110203113231.588:wxFindPanel class
#@+node:ekr.20061212100034:wxFindTab class
class wxFindTab (leoFind.findTab):
    
    '''A subclass of the findTab class containing all wxGui code.'''

    #@    @+others
    #@+node:ekr.20061212100034.1:ctor
    if 0: # We can use the base-class ctor.
    
        def __init__ (self,c,parentFrame):
        
            leoFind.findTab.__init__(self,c,parentFrame)
                # Init the base class.
                # Calls initGui, createFrame, createBindings & init(c), in that order.
    #@-node:ekr.20061212100034.1:ctor
    #@+node:ekr.20070105114426:class svar
    class svar:
        '''A class like Tk's IntVar and StringVar classes.'''
        def __init__(self):
            self.val = None
        def get (self):
            return self.val
        def set (self,val):
            self.val = val
    #@-node:ekr.20070105114426:class svar
    #@+node:ekr.20061212100034.2:initGui
    def initGui (self):
        
        # g.trace('wxFindTab')
    
        self.svarDict = {} # Keys are ivar names, values are svar objects.
        
        for key in self.intKeys:
            self.svarDict[key] = self.svar() # Was Tk.IntVar.
        
        for key in self.newStringKeys:
            self.svarDict[key] = self.svar() # Was Tk.StringVar.
    #@-node:ekr.20061212100034.2:initGui
    #@+node:ekr.20061212100034.3:createFrame (wxFindTab)
    def createFrame (self,parentFrame):
    
        self.parentFrame = self.top = parentFrame
    
        self.createFindChangeAreas()
        self.createBoxes()
        self.createButtons()
        self.layout()
        self.createBindings()
    #@+node:ekr.20061212100034.5:createFindChangeAreas
    def createFindChangeAreas (self):
        
        f = self.top
        
        self.fLabel = wx.StaticText(f,label='Find',  style=wx.ALIGN_RIGHT)
        self.cLabel = wx.StaticText(f,label='Change',style=wx.ALIGN_RIGHT)
        
        self.find_ctrl   = g.app.gui.leoTextWidgetClass(f,name='find-text',  size=(300,-1))
        self.change_ctrl = g.app.gui.leoTextWidgetClass(f,name='change-text',size=(300,-1))
        
    #@-node:ekr.20061212100034.5:createFindChangeAreas
    #@+node:ekr.20061212120506:layout
    def layout (self):
        
        f = self.top
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddSpacer(10)
        
        sizer2 = wx.FlexGridSizer(2, 2, vgap=10,hgap=5)
    
        sizer2.Add(self.fLabel,0,wx.EXPAND)
        sizer2.Add(self.find_ctrl,1,wx.EXPAND,border=5)
        sizer2.Add(self.cLabel,0,wx.EXPAND)
        sizer2.Add(self.change_ctrl,1,wx.EXPAND,border=5)
        
        sizer.Add(sizer2,0,wx.EXPAND)
        sizer.AddSpacer(10)
        
        #label = wx.StaticBox(f,label='Find Options')
        #boxes = wx.StaticBoxSizer(label,wx.HORIZONTAL)
        
        boxes = wx.BoxSizer(wx.HORIZONTAL)
        lt_col = wx.BoxSizer(wx.VERTICAL)
        rt_col = wx.BoxSizer(wx.VERTICAL)
    
        for w in self.boxes [:6]:
            lt_col.Add(w,0,wx.EXPAND,border=5)
            lt_col.AddSpacer(5)
        for w in self.boxes [6:]:
            rt_col.Add(w,0,wx.EXPAND,border=5)
            rt_col.AddSpacer(5)
            
        boxes.Add(lt_col,0,wx.EXPAND)
        boxes.AddSpacer(20)
        boxes.Add(rt_col,0,wx.EXPAND)
        sizer.Add(boxes,0) #,wx.EXPAND)
    
        f.SetSizer(sizer)
    #@nonl
    #@-node:ekr.20061212120506:layout
    #@+node:ekr.20061212100034.7:createBoxes
    def createBoxes (self):
        
        '''Create two columns of radio buttons & check boxes.'''
        
        c = self.c ; f = self.parentFrame
        self.boxes = []
        self.widgetsDict = {} # Keys are ivars, values are checkboxes or radio buttons.
        
        data = ( # Leading star denotes a radio button.
            ('Whole &Word', 'whole_word',),
            ('&Ignore Case','ignore_case'),
            ('Wrap &Around','wrap'),
            ('&Reverse',    'reverse'),
            ('Rege&xp',     'pattern_match'),
            ('Mark &Finds', 'mark_finds'),
            ("*&Entire Outline","entire-outline"),
            ("*&Suboutline Only","suboutline-only"),  
            ("*&Node Only","node-only"),
            ('Search &Headline','search_headline'),
            ('Search &Body','search_body'),
            ('Mark &Changes','mark_changes'),
        )
    
        # Important: changing these controls merely changes entries in self.svarDict.
        # First, leoFind.update_ivars sets the find ivars from self.svarDict.
        # Second, self.init sets the values of widgets from the ivars.
        inGroup = False
        for label,ivar in data:
            if label.startswith('*'):
                label = label[1:]
                style = g.choose(inGroup,0,wx.RB_GROUP)
                inGroup = True
                w = wx.RadioButton(f,label=label,style=style)
                self.widgetsDict[ivar] = w
                def radioButtonCallback(event=None,ivar=ivar):
                    svar = self.svarDict["radio-search-scope"]
                    svar.set(ivar)
                w.Bind(wx.EVT_RADIOBUTTON,radioButtonCallback)
            else:
                w = wx.CheckBox(f,label=label)
                self.widgetsDict[ivar] = w
                def checkBoxCallback(event=None,ivar=ivar):
                    svar = self.svarDict.get(ivar)
                    val = svar.get()
                    svar.set(g.choose(val,False,True))
                    # g.trace(ivar,val)
                w.Bind(wx.EVT_CHECKBOX,checkBoxCallback)
            self.boxes.append(w)
    #@nonl
    #@-node:ekr.20061212100034.7:createBoxes
    #@+node:ekr.20061212121401:createBindings TO DO
    def createBindings (self):
        
        return ### not ready yet
        
        def setFocus(w):
            c = self.c
            c.widgetWantsFocusNow(w)
            w.setSelectionRange(0,0)
            return "break"
            
        def toFind(event,w=ftxt): return setFocus(w)
        def toChange(event,w=ctxt): return setFocus(w)
            
        def insertTab(w):
            data = w.getSelectionRange()
            if data: start,end = data
            else: start = end = w.getInsertPoint()
            w.replace(start,end,"\t")
            return "break"
        
        def insertFindTab(event,w=ftxt): return insertTab(w)
        def insertChangeTab(event,w=ctxt): return insertTab(w)
        
        ftxt.bind("<Tab>",toChange)
        ctxt.bind("<Tab>",toFind)
        ftxt.bind("<Control-Tab>",insertFindTab)
        ctxt.bind("<Control-Tab>",insertChangeTab)
    #@-node:ekr.20061212121401:createBindings TO DO
    #@+node:ekr.20061212100034.8:createButtons (does nothing)
    def createButtons (self):
        
        '''Create two columns of buttons.'''
    
        # # Create the alignment panes.
        # buttons  = Tk.Frame(outer,background=bg)
        # buttons1 = Tk.Frame(buttons,bd=1,background=bg)
        # buttons2 = Tk.Frame(buttons,bd=1,background=bg)
        # buttons.pack(side='top',expand=1)
        # buttons1.pack(side='left')
        # buttons2.pack(side='right')
        
        # width = 15 ; defaultText = 'Find' ; buttons = []
        
        # for text,boxKind,frame,callback in (
            # # Column 1...
            # ('Find','button',buttons1,self.findButtonCallback),
            # ('Find All','button',buttons1,self.findAllButton),
            # # Column 2...
            # ('Change','button',buttons2,self.changeButton),
            # ('Change, Then Find','button',buttons2,self.changeThenFindButton),
            # ('Change All','button',buttons2,self.changeAllButton),
        # ):
            # w = underlinedTkButton(boxKind,frame,
                # text=text,command=callback)
            # buttons.append(w)
            # if text == defaultText:
                # w.button.configure(width=width-1,bd=4)
            # elif boxKind != 'check':
                # w.button.configure(width=width)
            # w.button.pack(side='top',anchor='w',pady=2,padx=2)
    #@-node:ekr.20061212100034.8:createButtons (does nothing)
    #@-node:ekr.20061212100034.3:createFrame (wxFindTab)
    #@+node:ekr.20061212100034.9:createBindings (wsFindTab) TO DO
    def createBindings (self):
        
        return ### not ready yet.
    
        c = self.c ; k = c.k
        
        def resetWrapCallback(event,self=self,k=k):
            self.resetWrap(event)
            return k.masterKeyHandler(event)
            
        def findButtonBindingCallback(event=None,self=self):
            self.findButton()
            return 'break'
    
        table = (
            ('<Button-1>',  k.masterClickHandler),
            ('<Double-1>',  k.masterClickHandler),
            ('<Button-3>',  k.masterClickHandler),
            ('<Double-3>',  k.masterClickHandler),
            ('<Key>',       resetWrapCallback),
            ('<Return>',    findButtonBindingCallback),
            ("<Escape>",    self.hideTab),
        )
    
        for w in (self.find_ctrl,self.change_ctrl):
            for event, callback in table:
                w.bind(event,callback)
    #@-node:ekr.20061212100034.9:createBindings (wsFindTab) TO DO
    #@+node:ekr.20061212100034.10:init (wxFindTab)
    # Important: we can not use leoFind.init because we must init the checkboxes 'by hand' here. 
    
    def init (self,c):
    
        # Separate c.ivars are much more convenient than a svarDict.
        for key in self.intKeys:
            # Get ivars from @settings.
            val = c.config.getBool(key)
            setattr(self,key,val)
            val = g.choose(val,1,0)
            svar = self.svarDict.get(key)
            if svar: svar.set(val)
            #g.trace(key,val)
    
        #@    << set find/change widgets >>
        #@+node:ekr.20061212100034.11:<< set find/change widgets >>
        self.find_ctrl.delete(0,"end")
        self.change_ctrl.delete(0,"end")
        
        # Get setting from @settings.
        for w,setting,defaultText in (
            (self.find_ctrl,"find_text",'<find pattern here>'),
            (self.change_ctrl,"change_text",''),
        ):
            s = c.config.getString(setting)
            if not s: s = defaultText
            w.insert("end",s)
        #@-node:ekr.20061212100034.11:<< set find/change widgets >>
        #@nl
        #@    << set radio buttons from ivars >>
        #@+node:ekr.20061212100034.12:<< set radio buttons from ivars >>
        # In Tk, setting the var also sets the widget.
        # Here, we do so explicitly.
        d = self.widgetsDict
        for ivar,key in (
            ("pattern_match","pattern-search"),
            #("script_search","script-search")
        ):
            svar = self.svarDict[ivar].get()
            if svar:
                self.svarDict["radio-find-type"].set(key)
                w = d.get(key)
                if w: w.SetValue(True)
                break
        else:
            self.svarDict["radio-find-type"].set("plain-search")
            
        for ivar,key in (
            ("suboutline_only","suboutline-only"),
            ("node_only","node-only"),
            # ("selection_only","selection-only")
        ):
            svar = self.svarDict[ivar].get()
            if svar:
                self.svarDict["radio-search-scope"].set(key)
                break
        else:
            key = 'entire-outline'
            self.svarDict["radio-search-scope"].set(key)
            w = self.widgetsDict.get(key)
            if w: w.SetValue(True)
        #@-node:ekr.20061212100034.12:<< set radio buttons from ivars >>
        #@nl
        #@    << set checkboxes from ivars >>
        #@+node:ekr.20061213063636:<< set checkboxes from ivars >>
        for ivar in (
            'ignore_case',
            'mark_changes',
            'mark_finds',
            'pattern_match',
            'reverse',
            'search_body',
            'search_headline',
            'whole_word',
            'wrap',
        ):
            svar = self.svarDict[ivar].get()
            if svar:
                w = self.widgetsDict.get(ivar)
                if w: w.SetValue(True)
        #@-node:ekr.20061213063636:<< set checkboxes from ivars >>
        #@nl
    #@-node:ekr.20061212100034.10:init (wxFindTab)
    #@-others
#@nonl
#@-node:ekr.20061212100034:wxFindTab class
#@-node:edream.110203113231.560: Find classes
#@+node:ekr.20061116074003:wxKeyHandlerClass
class wxKeyHandlerClass (leoKeys.keyHandlerClass):
    
    '''wxWidgets overrides of base keyHandlerClass.'''

    #@    @+others
    #@+node:ekr.20061116074003.1:ctor (wxKey)
    def __init__(self,c,useGlobalKillbuffer=False,useGlobalRegisters=False):
        
        # g.trace('wxKeyHandlerClass',g.callers())
        
        self.widget = None # Set in finishCreate.
        
        # Init the base class.
        leoKeys.keyHandlerClass.__init__(self,c,useGlobalKillbuffer,useGlobalRegisters)
    #@-node:ekr.20061116074003.1:ctor (wxKey)
    #@+node:ekr.20070123101021:wx.defineSpecialKeys
    def defineSpecialKeys (self):
        
        k = self
        k.guiBindNamesDict = {}
        k.guiBindNamesInverseDict = {}
    
        # No translation.
        for s in k.tkNamesList:
            k.guiBindNamesDict[s] = s
            
        # Create the inverse dict.
        for key in k.guiBindNamesDict.keys():
            k.guiBindNamesInverseDict [k.guiBindNamesDict.get(key)] = key
            
            
        # Important: only the inverse dict is actually used in the new key binding scheme.
    
        # wxWidgets may return the *values* of this dict in event.keysym fields.
        # Leo will warn if it gets a event whose keysym not in values of this table.
        
        # wxWidgets Keypresses are represented by an enumerated type, wxKeyCode.
        # The possible values are the ASCII character codes, plus the following:
        
        # k.guiBindNamesDict = {
            # "!" : "exclam",
            # '"' : "quotedbl",
            # "#" : "numbersign",
            # "$" : "dollar",
            # "%" : "percent",
            # "&" : "ampersand",
            # "'" : "quoteright",
            # "(" : "parenleft",
            # ")" : "parenright",
            # "*" : "asterisk",
            # "+" : "plus",
            # "," : "comma",
            # "-" : "minus",
            # "." : "period",
            # "/" : "slash",
            # ":" : "colon",
            # ";" : "semicolon",
            # "<" : "less",
            # "=" : "equal",
            # ">" : "greater",
            # "?" : "question",
            # "@" : "at",
            # "[" : "bracketleft",
            # "\\": "backslash",
            # "]" : "bracketright",
            # "^" : "asciicircum",
            # "_" : "underscore",
            # "`" : "quoteleft",
            # "{" : "braceleft",
            # "|" : "bar",
            # "}" : "braceright",
            # "~" : "asciitilde",
        # }
    #@-node:ekr.20070123101021:wx.defineSpecialKeys
    #@+node:ekr.20061116080942:finishCreate (wxKey)
    def finishCreate (self):
        
        c = self.c
        
        leoKeys.keyHandlerClass.finishCreate(self) # Call the base class.
        
        # In the Tk version, this is done in the editor logic.
        c.frame.body.createBindings(w=c.frame.body.bodyCtrl)
        
        self.widget = c.frame.minibuffer.ctrl
        
        self.setLabelGrey()
    #@nonl
    #@-node:ekr.20061116080942:finishCreate (wxKey)
    #@+node:ekr.20061116074003.3:Label (wx keys) (test all)
    #@+node:ekr.20061116074003.8:extendLabel
    def extendLabel(self,s,select=False,protect=False):
        
        k = self ; c = k.c ; w = self.widget
        if not w or not s: return
    
        c.widgetWantsFocusNow(w)
        w.insert('end',s)
        if select:
            i,j = k.getEditableTextRange()
            w.setSelectionRange(i,j,insert=j)
        if protect:
            k.protectLabel()
    #@-node:ekr.20061116074003.8:extendLabel
    #@+node:ekr.20061116074003.12:getEditableTextRange
    def getEditableTextRange (self):
        
        k = self ; w = self.widget
        if not w: return 0,0
    
        s = w.getAllText()
    
        i = len(k.mb_prefix)
        while s.endswith('\n') or s.endswith('\r'):
            s = s[:-1]
        j = len(s)
    
        return i,j
    #@nonl
    #@-node:ekr.20061116074003.12:getEditableTextRange
    #@+node:ekr.20061116074003.4:getLabel
    def getLabel (self,ignorePrompt=False):
        
        k = self ; w = self.widget
        if not w: return ''
        
        s = w.getAllText()
    
        if ignorePrompt:
            return s[len(k.mb_prefix):]
        else:
            return s or ''
    #@-node:ekr.20061116074003.4:getLabel
    #@+node:ekr.20061116074003.5:protectLabel
    def protectLabel (self):
        
        k = self ; w = self.widget
        if not w: return
    
        k.mb_prefix = w.getAllText()
    #@nonl
    #@-node:ekr.20061116074003.5:protectLabel
    #@+node:ekr.20061116074003.6:resetLabel
    def resetLabel (self):
        
        k = self
        k.setLabelGrey('')
        k.mb_prefix = ''
    #@-node:ekr.20061116074003.6:resetLabel
    #@+node:ekr.20061116074003.7:setLabel
    def setLabel (self,s,protect=False):
    
        k = self ; c = k.c ; w = self.widget
        if not w: return
    
        w.delete(0,'end')
        w.insert(0,s)
        c.masterFocusHandler() # Restore to the previously requested focus.
    
        if protect:
            k.mb_prefix = s
    #@-node:ekr.20061116074003.7:setLabel
    #@+node:ekr.20061116074003.9:setLabelBlue
    def setLabelBlue (self,label=None,protect=False):
        
        k = self ; w = k.widget
        if not w: return
    
        w.SetBackgroundColour('sky blue')
    
        if label is not None:
            k.setLabel(label,protect)
    #@-node:ekr.20061116074003.9:setLabelBlue
    #@+node:ekr.20061116074003.10:setLabelGrey
    def setLabelGrey (self,label=None):
    
        k = self ; w = self.widget
        if not w: return
        
        w.SetBackgroundColour('light grey')
    
        if label is not None:
            k.setLabel(label)
    
    setLabelGray = setLabelGrey
    #@-node:ekr.20061116074003.10:setLabelGrey
    #@+node:ekr.20061116074003.11:updateLabel
    def updateLabel (self,event):
    
        '''Mimic what would happen with the keyboard and a Text editor
        instead of plain accumalation.'''
        
        k = self ; c = k.c ; w = self.widget
        if not w: return
    
        ch = (event and event.char) or ''
        keysym = (event and event.keysym) or ''
        # g.trace('ch',ch,'keysym',keysym,'k.stroke',k.stroke)
        
        if ch and ch not in ('\n','\r'):
            c.widgetWantsFocusNow(w)
            i,j = w.getSelectionRange()
            if i != j:
                w.delete(i,j)
            if ch == '\b':
                s = w.getAllText()
                if len(s) > len(k.mb_prefix):
                    w.delete(i+1)
            else:
                i = w.getInsertPoint()
                w.insert(i,ch)
    #@-node:ekr.20061116074003.11:updateLabel
    #@-node:ekr.20061116074003.3:Label (wx keys) (test all)
    #@-others
#@nonl
#@-node:ekr.20061116074003:wxKeyHandlerClass
#@+node:edream.110203113231.305:wxGui class
class wxGui(leoGui.leoGui):
    
    #@    @+others
    #@+node:edream.111303091300:app.gui.wx birth & death
    #@+node:edream.110203113231.307: wxGui.__init__
    def __init__ (self):
        
        # g.trace("wxGui")
        
        # Initialize the base class.
        if 1: # in plugin
            leoGui.leoGui.__init__(self,"wxPython")
        else:
            leoGui.__init__(self,"wxPython")
            
        self.bitmap_name = None
        self.bitmap = None
        self.leoTextWidgetClass = wxLeoTextWidget
        self.findTabHandler = None
    #@-node:edream.110203113231.307: wxGui.__init__
    #@+node:ekr.20061116074207:tkGui.createKeyHandlerClass
    def createKeyHandlerClass (self,c,useGlobalKillbuffer=True,useGlobalRegisters=True):
                
        return wxKeyHandlerClass(c,useGlobalKillbuffer,useGlobalRegisters)
    #@nonl
    #@-node:ekr.20061116074207:tkGui.createKeyHandlerClass
    #@+node:edream.110203113231.308:createRootWindow
    def createRootWindow(self):
    
        self.wxApp = wxLeoApp(None) # This redirects stdout & stderr to stupid console.
        self.wxFrame = None
    
        if 0: # Not ready yet.
            self.setDefaultIcon()
            self.getDefaultConfigFont(g.app.config)
            self.setEncoding()
            self.createGlobalWindows()
    
        return self.wxFrame
    #@nonl
    #@-node:edream.110203113231.308:createRootWindow
    #@+node:edream.111303085447.1:destroySelf
    def destroySelf(self):
        
        pass # Nothing more needs to be done once all windows have been destroyed.
    #@nonl
    #@-node:edream.111303085447.1:destroySelf
    #@+node:edream.110203113231.314:finishCreate
    def finishCreate (self):
    
       pass # g.trace('gui')
    #@-node:edream.110203113231.314:finishCreate
    #@+node:edream.110203113231.315:killGui
    def killGui(self,exitFlag=True):
        
        """Destroy a gui and terminate Leo if exitFlag is True."""
    
        pass # Not ready yet.
    
    #@-node:edream.110203113231.315:killGui
    #@+node:edream.110203113231.316:recreateRootWindow
    def recreateRootWindow(self):
    
        """A do-nothing base class to create the hidden root window of a gui
    
        after a previous gui has terminated with killGui(False)."""
    
        # g.trace('wx gui')
    #@-node:edream.110203113231.316:recreateRootWindow
    #@+node:edream.110203113231.317:runMainLoop
    def runMainLoop(self):
    
        """Run tkinter's main loop."""
        
        # g.trace("wxGui")
        self.wxApp.MainLoop()
        # g.trace("done")
    #@nonl
    #@-node:edream.110203113231.317:runMainLoop
    #@-node:edream.111303091300:app.gui.wx birth & death
    #@+node:edream.110203113231.321:app.gui wx dialogs
    #@+node:edream.110203113231.322:runAboutLeoDialog
    def runAboutLeoDialog(self,c,version,copyright,url,email):
        
        """Create and run a wxPython About Leo dialog."""
    
        message = "%s\n\n%s\n\n%s\n\n%s" % (
            version.strip(),copyright.strip(),url.strip(),email.strip())
        
        wx.MessageBox(message,"About Leo",wx.Center,self.root)
    #@nonl
    #@-node:edream.110203113231.322:runAboutLeoDialog
    #@+node:edream.110203113231.323:runAskOkDialog
    def runAskOkDialog(self,c,title,message=None,text="Ok"):
        
        """Create and run a wxPython askOK dialog ."""
        
        d = wx.MessageDialog(self.root,message,"Leo",wx.OK)
        d.ShowModal()
        return "ok"
    #@nonl
    #@-node:edream.110203113231.323:runAskOkDialog
    #@+node:ekr.20061106065606:runAskLeoIDDialog
    def runAskLeoIDDialog(self):
    
        """Create and run a dialog to get g.app.LeoID."""
        pass
    #@nonl
    #@-node:ekr.20061106065606:runAskLeoIDDialog
    #@+node:edream.110203113231.324:runAskOkCancelNumberDialog (to do)
    def runAskOkCancelNumberDialog(self,c,title,message):
    
        """Create and run a wxPython askOkCancelNumber dialog ."""
    
        g.trace()
        return 666
    #@nonl
    #@-node:edream.110203113231.324:runAskOkCancelNumberDialog (to do)
    #@+node:ekr.20070122103916:runAskOkCancelStringDialog (to do)
    def runAskOkCancelStringDialog(self,c,title,message):
    
        """Create and run a wxPython askOkCancelNumber dialog ."""
    
        g.trace()
        return 'Not ready yet'
    #@nonl
    #@-node:ekr.20070122103916:runAskOkCancelStringDialog (to do)
    #@+node:edream.110203113231.325:runAskYesNoDialog
    def runAskYesNoDialog(self,c,title,message=None):
    
        """Create and run a wxPython askYesNo dialog."""
        
        d = wx.MessageDialog(self.root,message,"Leo",wx.YES_NO)
        answer = d.ShowModal()
    
        return g.choose(answer==wx.YES,"yes","no")
    #@nonl
    #@-node:edream.110203113231.325:runAskYesNoDialog
    #@+node:edream.110203113231.326:runAskYesNoCancelDialog
    def runAskYesNoCancelDialog(self,c,title,
        message=None,yesMessage="Yes",noMessage="No",defaultButton="Yes"):
    
        """Create and run a wxPython askYesNoCancel dialog ."""
        
        d = wx.MessageDialog(self.root,message,"Leo",wx.YES_NO | wx.CANCEL)
        answer = d.ShowModal()
        
        if answer == wx.ID_YES:
            return "yes"
        elif answer == wx.ID_NO:
            return "no"
        else:
            assert(answer == wx.ID_CANCEL)
            return "cancel"
    #@nonl
    #@-node:edream.110203113231.326:runAskYesNoCancelDialog
    #@+node:edream.110203113231.327:runOpenFileDialog
    def runOpenFileDialog(self,title,filetypes,defaultextension):
    
        """Create and run a wxPython open file dialog ."""
        
        wildcard = self.getWildcardList(filetypes)
    
        d = wx.FileDialog(
            parent=None, message=title,
            defaultDir="", defaultFile="",
            wildcard=wildcard,
            style= wx.OPEN | wx.CHANGE_DIR | wx.HIDE_READONLY)
    
        val = d.ShowModal()
        if val == wx.ID_OK:
            file = d.GetFilename()
            return file
        else:
            return None 
    #@-node:edream.110203113231.327:runOpenFileDialog
    #@+node:edream.110203113231.328:runSaveFileDialog
    def runSaveFileDialog(self,initialfile,title,filetypes,defaultextension):
    
        """Create and run a wxPython save file dialog ."""
    
        wildcard = self.getWildcardList(filetypes)
    
        d = wx.FileDialog(
            parent=None, message=title,
            defaultDir="", defaultFile="",
            wildcard=wildcard,
            style= wx.SAVE | wx.CHANGE_DIR | wx.OVERWRITE_PROMPT)
    
        val = d.ShowModal()
        if val == wx.ID_OK:
            file = d.GetFilename()
            return file
        else:
            return None
    #@nonl
    #@-node:edream.110203113231.328:runSaveFileDialog
    #@+node:edream.111403104835:getWildcardList
    def getWildcardList (self,filetypes):
        
        """Create a wxWindows wildcard string for open/save dialogs."""
    
        if not filetypes:
            return "*.leo"
    
        if 1: # Too bad: this is sooo wimpy.
                a,b = filetypes[0] 
                return b
    
        else: # This _sometimes_ works: wxWindows is driving me crazy!
    
            # wildcards = ["%s (%s)" % (a,b) for a,b in filetypes]
            wildcards = ["%s" % (b) for a,b in filetypes]
            wildcard = "|".join(wildcards)
            g.trace(wildcard)
            return wildcard
    #@nonl
    #@-node:edream.111403104835:getWildcardList
    #@-node:edream.110203113231.321:app.gui wx dialogs
    #@+node:edream.111303091857:app.gui wx panels (to do)
    #@+node:edream.111303092328:createColorPanel
    def createColorPanel(self,c):
    
        """Create Color panel."""
    
        g.trace("not ready yet")
    #@nonl
    #@-node:edream.111303092328:createColorPanel
    #@+node:edream.111303092328.1:createComparePanel
    def createComparePanel(self,c):
    
        """Create Compare panel."""
    
        g.trace("not ready yet")
    #@nonl
    #@-node:edream.111303092328.1:createComparePanel
    #@+node:edream.111303092328.2:createFindPanel
    def createFindPanel(self):
    
        """Create a hidden Find panel."""
    
        return wxFindFrame()
    #@nonl
    #@-node:edream.111303092328.2:createFindPanel
    #@+node:ekr.20061212100014:createFindTab
    def createFindTab (self,c,parentFrame):
        
        '''Create a wxWidgets find tab in the indicated frame.'''
        
        # g.trace(self.findTabHandler)
        
        if not self.findTabHandler:
            self.findTabHandler = wxFindTab(c,parentFrame)
    
        return self.findTabHandler
    #@-node:ekr.20061212100014:createFindTab
    #@+node:edream.111303092328.3:createFontPanel
    def createFontPanel(self,c):
    
        """Create a Font panel."""
    
        g.trace("not ready yet")
    #@nonl
    #@-node:edream.111303092328.3:createFontPanel
    #@+node:edream.111303092328.4:createLeoFrame (wxGui panels)
    def createLeoFrame(self,title):
        
        """Create a new Leo frame."""
    
        return wxLeoFrame(title)
    #@nonl
    #@-node:edream.111303092328.4:createLeoFrame (wxGui panels)
    #@+node:edream.110203113231.333:destroyLeoFrame (used??)
    def destroyLeoFrame (self,frame):
    
        g.trace(frame.title)
        frame.Close()
    #@nonl
    #@-node:edream.110203113231.333:destroyLeoFrame (used??)
    #@-node:edream.111303091857:app.gui wx panels (to do)
    #@+node:edream.111303090930:app.gui.wx utils (must add several)
    #@+node:edream.110203113231.320:Clipboard
    def replaceClipboardWith (self,s):
    
        cb = wx.TheClipboard
        if cb.Open():
            cb.Clear()
            cb.SetData(s)
            cb.Flush()
            cb.Close()
        
    def getTextFromClipboard (self):
        
        return ''
        
        # This code doesn't work yet.
        
        cb = wx.TheClipboard ; data = None
        if cb.Open():
            data = wx.DataObject()
            cb.GetData(data)
            data = data.GetDataHere()
            cb.Close()
        return data
    #@nonl
    #@-node:edream.110203113231.320:Clipboard
    #@+node:ekr.20070123101505:Constants
    # g.es calls gui.color to do the translation,
    # so most code in Leo's core can simply use Tk color names.
    
    def color (self,color):
        '''Return the gui-specific color corresponding to the Tk color name.'''
        return color # Do not call oops: this method is essential for the config classes.
    #@-node:ekr.20070123101505:Constants
    #@+node:edream.110203113231.339:Dialog
    #@+node:edream.111403151611:bringToFront
    def bringToFront (self,window):
        
        if window.IsIconized():
            window.Maximize()
        window.Raise()
        window.Show(True)
    #@nonl
    #@-node:edream.111403151611:bringToFront
    #@+node:edream.110203113231.343:get_window_info
    def get_window_info(self,window):
    
        # Get the information about top and the screen.
        x,y = window.GetPosition()
        w,h = window.GetSize()
        
        return w,h,x,y
    #@nonl
    #@-node:edream.110203113231.343:get_window_info
    #@+node:edream.110203113231.344:center_dialog
    def center_dialog(window):
        
        window.Center()
    #@nonl
    #@-node:edream.110203113231.344:center_dialog
    #@-node:edream.110203113231.339:Dialog
    #@+node:ekr.20061116085729:Events (wxGui)
    def event_generate(self,w,kind,*args,**keys):
        '''Generate an event.'''
        return w.event_generate(kind,*args,**keys)
    #@+node:ekr.20061117204829:wxKeyDict
    wxKeyDict = {
        # Keys are wxWidgets key codes.  Values are the standard (Tk) names.
        wx.WXK_DECIMAL  : '.',
        wx.WXK_BACK     : '\b', # 'BackSpace',
        wx.WXK_TAB      : '\t', # 'Tab',
        wx.WXK_RETURN   : '\n', # 'Return',
        wx.WXK_ESCAPE   : 'Escape',
        wx.WXK_SPACE    : ' ',
        wx.WXK_DELETE   : 'Delete',
        wx.WXK_LEFT     : 'Left',
        wx.WXK_UP       : 'Up',
        wx.WXK_RIGHT    : 'Right',
        wx.WXK_DOWN     : 'Down',
        wx.WXK_F1       : 'F1',
        wx.WXK_F2       : 'F2',
        wx.WXK_F3       : 'F3',
        wx.WXK_F4       : 'F4',
        wx.WXK_F5       : 'F5',
        wx.WXK_F6       : 'F6',
        wx.WXK_F7       : 'F7',
        wx.WXK_F8       : 'F8',
        wx.WXK_F9       : 'F9',
        wx.WXK_F10      : 'F10',
        wx.WXK_F11      : 'F11',
        wx.WXK_F12      : 'F12',
        wx.WXK_END                  : 'End',
        wx.WXK_HOME                 : 'Home',
        wx.WXK_PAGEUP               : 'Prior',
        wx.WXK_PAGEDOWN             : 'Next',
        wx.WXK_NUMPAD_DELETE        : 'Delete',
        wx.WXK_NUMPAD_SPACE         : ' ',
        wx.WXK_NUMPAD_TAB           : '\t', # 'Tab',
        wx.WXK_NUMPAD_ENTER         : '\n', # 'Return',
        wx.WXK_NUMPAD_PAGEUP        : 'Prior',
        wx.WXK_NUMPAD_PAGEDOWN      : 'Next',
        wx.WXK_NUMPAD_END           : 'End',
        wx.WXK_NUMPAD_BEGIN         : 'Home',
    }
    
    #@+at 
    #@nonl
    # These are by design not compatible with unicode characters.
    # If you want to get a unicode character from a key event use
    # wxKeyEvent::GetUnicodeKey instead.
    # 
    # WXK_START   = 300
    # WXK_LBUTTON
    # WXK_RBUTTON
    # WXK_CANCEL
    # WXK_MBUTTON
    # WXK_CLEAR
    # WXK_SHIFT
    # WXK_ALT
    # WXK_CONTROL
    # WXK_MENU
    # WXK_PAUSE
    # WXK_CAPITAL
    # WXK_SELECT
    # WXK_PRINT
    # WXK_EXECUTE
    # WXK_SNAPSHOT
    # WXK_INSERT
    # WXK_HELP
    # WXK_NUMPAD0
    # WXK_NUMPAD1
    # WXK_NUMPAD2
    # WXK_NUMPAD3
    # WXK_NUMPAD4
    # WXK_NUMPAD5
    # WXK_NUMPAD6
    # WXK_NUMPAD7
    # WXK_NUMPAD8
    # WXK_NUMPAD9
    # WXK_MULTIPLY
    # WXK_ADD
    # WXK_SEPARATOR
    # WXK_SUBTRACT
    # WXK_DECIMAL
    # WXK_DIVIDE
    # WXK_F13
    # WXK_F14
    # WXK_F15
    # WXK_F16
    # WXK_F17
    # WXK_F18
    # WXK_F19
    # WXK_F20
    # WXK_F21
    # WXK_F22
    # WXK_F23
    # WXK_F24
    # WXK_NUMLOCK
    # WXK_SCROLL
    # WXK_NUMPAD_F1,
    # WXK_NUMPAD_F2,
    # WXK_NUMPAD_F3,
    # WXK_NUMPAD_F4,
    # WXK_NUMPAD_HOME,
    # WXK_NUMPAD_LEFT,
    # WXK_NUMPAD_UP,
    # WXK_NUMPAD_RIGHT,
    # WXK_NUMPAD_DOWN,
    # WXK_NUMPAD_INSERT,
    # WXK_NUMPAD_EQUAL,
    # WXK_NUMPAD_MULTIPLY,
    # WXK_NUMPAD_ADD,
    # WXK_NUMPAD_SEPARATOR,
    # WXK_NUMPAD_SUBTRACT,
    # WXK_NUMPAD_DECIMAL,
    # WXK_NUMPAD_DIVIDE,
    # 
    # // the following key codes are only generated under Windows currently
    # WXK_WINDOWS_LEFT,
    # WXK_WINDOWS_RIGHT,
    # WXK_WINDOWS_MENU,
    # WXK_COMMAND,
    # 
    # // Hardware-specific buttons
    # WXK_SPECIAL1 = 193,
    # WXK_SPECIAL2,
    # WXK_SPECIAL3,
    # WXK_SPECIAL4,
    # WXK_SPECIAL5,
    # WXK_SPECIAL6,
    # WXK_SPECIAL7,
    # WXK_SPECIAL8,
    # WXK_SPECIAL9,
    # WXK_SPECIAL10,
    # WXK_SPECIAL11,
    # WXK_SPECIAL12,
    # WXK_SPECIAL13,
    # WXK_SPECIAL14,
    # WXK_SPECIAL15,
    # WXK_SPECIAL16,
    # WXK_SPECIAL17,
    # WXK_SPECIAL18,
    # WXK_SPECIAL19,
    # WXK_SPECIAL20
    #@-at
    #@nonl
    #@-node:ekr.20061117204829:wxKeyDict
    #@+node:ekr.20061117155233:eventChar & eventKeysym & helper
    def eventChar (self,event,c=None):
    
        '''Return the char field of an event, either a wx event or a converted Leo event.'''
    
        if hasattr(event,'char'):
            return event.char # A leoKeyEvent.
        else:
            return self.keysymHelper(event,c=c,kind='char')
    
    def eventKeysym (self,event,c=None):
        
        if hasattr(event,'keysym'):
            return event.keysym # A leoKeyEvent: we have already computed the result.
        else:
            return self.keysymHelper(event,c=c,kind='keysym')
    #@+node:ekr.20061117203128:keysymHelper
    def keysymHelper (self,event,c,kind):
        
        gui = self
        
        keycode = event.GetKeyCode()
        
        # g.trace(repr(keycode),kind)
    
        if keycode in (wx.WXK_SHIFT,wx.WXK_ALT,wx.WXK_CONTROL):
            return ''
    
        keysym = gui.wxKeyDict.get(keycode) or ''
        keyDownModifiers = hasattr(event,'keyDownModifiers') and event.keyDownModifiers or None
        alt = event.AltDown()     or keyDownModifiers == wx.MOD_ALT
        cmd = event.CmdDown()     or keyDownModifiers == wx.MOD_CMD
        ctrl = event.ControlDown()or keyDownModifiers == wx.MOD_CONTROL
        meta = event.MetaDown()   or keyDownModifiers == wx.MOD_META
        shift = event.ShiftDown() or keyDownModifiers == wx.MOD_SHIFT
        
        # Set the char field.
        char = keysym or ''
        if not char:
            # Avoid GetUnicodeKey if possible.  It crashes on '.' (!)
            try:
                char = chr(keycode)
            except ValueError:
                char = ''
        if not char and hasattr(event,'GetUnicodeKey'):
            i = event.GetUnicodeKey()
            if i is None: char = ''
            else:
                try:
                    char = unichr(i)
                except Exception:
                    g.es('No translation for', repr(i))
                    char = repr(i)
       
        # Adjust the case, but only for plain ascii characters characters.
        if len(char) == 1:
            if char.isalpha():
                if shift: # Case is also important for ctrl keys. # or alt or cmd or ctrl or meta:
                    char = char.upper()
                else:
                    char = char.lower()
            elif shift:
                char = self.getShiftChar(char)
            else:
                char = self.getUnshiftChar(char)
    
        # Create a value compatible with Leo's core.
        val = (
            g.choose(alt,'Alt+','') +
            # g.choose(cmd,'Cmd+','') +
            g.choose(ctrl,'Ctrl+','') +
            g.choose(meta,'Meta+','') +
            g.choose((alt or cmd or ctrl or meta) and shift,'Shift+','') +
            (char or '')
        )
    
        # if kind == 'char':  g.trace(repr(keycode),repr(val)) # Tracing just val can crash!
        return val
    #@-node:ekr.20061117203128:keysymHelper
    #@+node:ekr.20061118055443:getShiftChar
    def getShiftChar (self,char):
        
        d = {
            '1': '!',
            '2': '@',
            '3': '#',
            '4': '$',
            '5': '%',
            '6': '^',
            '7': '&',
            '8': '*',
            '9': '(',
            '0': ')',
            '-': '_',
            '=': '+',
            '[': '{',
            ']': '}',
            '\\': '|',
            ';': ':',
            "'": '"',
            ',': '<',
            '.': '>',
            '/': '?',
        }
        return d.get(char,char) # There must be a better way.
    #@nonl
    #@-node:ekr.20061118055443:getShiftChar
    #@+node:ekr.20061118070150:getUnshiftChar
    def getUnshiftChar (self,char):
        
        d = {
            '+': '='
        }
        return d.get(char,char)
    #@nonl
    #@-node:ekr.20061118070150:getUnshiftChar
    #@-node:ekr.20061117155233:eventChar & eventKeysym & helper
    #@+node:ekr.20061117155233.1:eventWidget
    def eventWidget (self,event,c=None):
    
        '''Return the widget field of an event, either a wx event or a converted Leo event.'''
    
        if hasattr(event,'widget'):
            return event.widget # a leoKeyEvent.
        elif hasattr(event,'GetEventObject'):
            return event.GetEventObject()
        else:
            return None
    #@-node:ekr.20061117155233.1:eventWidget
    #@+node:ekr.20061117155233.2:eventXY
    def eventXY (self,event,c=None):
        
        if hasattr(event,'x') and hasattr(event,'y'):
            return event.x,event.y
        if hasattr(event,'GetX') and hasattr(event,'GetY'):
            return event.GetX(),event.GetY()
        else:
            return 0,0
    #@-node:ekr.20061117155233.2:eventXY
    #@-node:ekr.20061116085729:Events (wxGui)
    #@+node:edream.110203113231.335:Focus (wxGui) (to do)
    #@+node:edream.110203113231.336:get_focus
    def get_focus(self,top):
        
        """Returns the widget that has focus, or body if None."""
    
        return top
    #@nonl
    #@-node:edream.110203113231.336:get_focus
    #@+node:edream.110203113231.337:set_focus (wxGui)
    def set_focus(self,c,w):
        
        """Set the focus of the widget in the given commander if it needs to be changed."""
        
        c.frame.setFocus(w)
    #@-node:edream.110203113231.337:set_focus (wxGui)
    #@-node:edream.110203113231.335:Focus (wxGui) (to do)
    #@+node:edream.110203113231.318:Font (wxGui) (to do)
    #@+node:edream.110203113231.319:getFontFromParams
    def getFontFromParams(self,family,size,slant,weight):
        
        ## g.trace(g.app.config.defaultFont)
        
        return g.app.config.defaultFont ##
        
        family_name = family
        
        try:
            font = tkFont.Font(family=family,size=size,slant=slant,weight=weight)
            #print family_name,family,size,slant,weight
            #print "actual_name:",font.cget("family")
            return font
        except:
            g.es("exception setting font from " + `family_name`)
            g.es("family,size,slant,weight:"+
                `family`+':'+`size`+':'+`slant`+':'+`weight`)
            g.es_exception()
            return g.app.config.defaultFont
    #@nonl
    #@-node:edream.110203113231.319:getFontFromParams
    #@-node:edream.110203113231.318:Font (wxGui) (to do)
    #@+node:edream.111303092854:Icons (wxGui) (to do)
    #@+node:edream.110203113231.340:attachLeoIcon
    def attachLeoIcon (self,w):
        
        """Try to attach a Leo icon to the Leo Window.
        
        Use tk's wm_iconbitmap function if available (tk 8.3.4 or greater).
        Otherwise, try to use the Python Imaging Library and the tkIcon package."""
    
        if self.bitmap != None:
            # We don't need PIL or tkicon: this is tk 8.3.4 or greater.
            try:
                w.wm_iconbitmap(self.bitmap)
            except:
                self.bitmap = None
        
        if self.bitmap == None:
            try:
                #@            << try to use the PIL and tkIcon packages to draw the icon >>
                #@+node:edream.110203113231.341:<< try to use the PIL and tkIcon packages to draw the icon >>
                #@+at 
                #@nonl
                # This code requires Fredrik Lundh's PIL and tkIcon packages:
                # 
                # Download PIL    from 
                # http://www.pythonware.com/downloads/index.htm#pil
                # Download tkIcon from http://www.effbot.org/downloads/#tkIcon
                # 
                # Many thanks to Jonathan M. Gilligan for suggesting this 
                # code.
                #@-at
                #@@c
                
                import Image,tkIcon,_tkicon
                
                # Wait until the window has been drawn once before attaching the icon in OnVisiblity.
                def visibilityCallback(event,self=self,w=w):
                    try: self.leoIcon.attach(w.winfo_id())
                    except: pass
                w.bind("<Visibility>",visibilityCallback)
                if not self.leoIcon:
                    # Load a 16 by 16 gif.  Using .gif rather than an .ico allows us to specify transparency.
                    icon_file_name = os.path.join(g.app.loadDir,'..','Icons','LeoWin.gif')
                    icon_file_name = os.path.normpath(icon_file_name)
                    icon_image = Image.open(icon_file_name)
                    if 1: # Doesn't resize.
                        self.leoIcon = self.createLeoIcon(icon_image)
                    else: # Assumes 64x64
                        self.leoIcon = tkIcon.Icon(icon_image)
                #@nonl
                #@-node:edream.110203113231.341:<< try to use the PIL and tkIcon packages to draw the icon >>
                #@nl
            except:
                # traceback.print_exc()
                self.leoIcon = None
    #@nonl
    #@-node:edream.110203113231.340:attachLeoIcon
    #@+node:edream.110203113231.342:createLeoIcon
    # This code is adapted from tkIcon.__init__
    # Unlike the tkIcon code, this code does _not_ resize the icon file.
    
    def createLeoIcon (self,icon):
        
        try:
            import Image,tkIcon,_tkicon
            
            i = icon ; m = None
            # create transparency mask
            if i.mode == "P":
                try:
                    t = i.info["transparency"]
                    m = i.point(lambda i, t=t: i==t, "1")
                except KeyError: pass
            elif i.mode == "RGBA":
                # get transparency layer
                m = i.split()[3].point(lambda i: i == 0, "1")
            if not m:
                m = Image.new("1", i.size, 0) # opaque
            # clear unused parts of the original image
            i = i.convert("RGB")
            i.paste((0, 0, 0), (0, 0), m)
            # create icon
            m = m.tostring("raw", ("1", 0, 1))
            c = i.tostring("raw", ("BGRX", 0, -1))
            return _tkicon.new(i.size, c, m)
        except:
            return None
    #@nonl
    #@-node:edream.110203113231.342:createLeoIcon
    #@-node:edream.111303092854:Icons (wxGui) (to do)
    #@+node:edream.110203113231.329:Idle time (wxGui) (to do)
    #@+node:edream.111303093843:setIdleTimeHook
    def setIdleTimeHook (self,idleTimeHookHandler,*args,**keys):
        
        pass # g.trace(idleTimeHookHandler)
        
    #@-node:edream.111303093843:setIdleTimeHook
    #@+node:edream.111303093843.1:setIdleTimeHookAfterDelay
    def setIdleTimeHookAfterDelay (self,idleTimeHookHandler,*args,**keys):
        
        g.trace(idleTimeHookHandler)
    #@nonl
    #@-node:edream.111303093843.1:setIdleTimeHookAfterDelay
    #@-node:edream.110203113231.329:Idle time (wxGui) (to do)
    #@+node:ekr.20061116091006:isTextWidget (wxGui)
    def isTextWidget (self,w):
    
        return isinstance(w,wx.TextCtrl)
    #@nonl
    #@-node:ekr.20061116091006:isTextWidget (wxGui)
    #@+node:ekr.20061117162357:widget_name (tkGui)
    def widget_name (self,w):
        
        # First try the wxWindow.GetName.
        if hasattr(w,'GetName'):
            name = w.GetName()
        else:
            name = repr(w)
        return name
    #@-node:ekr.20061117162357:widget_name (tkGui)
    #@-node:edream.111303090930:app.gui.wx utils (must add several)
    #@+node:ekr.20061116093228:class leoKeyEvent (wxGui)
    class leoKeyEvent:
        
        '''A gui-independent wrapper for gui events.'''
        
        def __init__ (self,event,c):
            gui = g.app.gui
            self.c                  = c
            self.actualEvent        = event
            self.char               = gui.eventChar(event,c)
            self.keysym             = gui.eventKeysym(event,c)
            self.widget = self.w    = gui.eventWidget(event)
            self.x,self.y           = gui.eventXY(event)
    #@-node:ekr.20061116093228:class leoKeyEvent (wxGui)
    #@-others
#@nonl
#@-node:edream.110203113231.305:wxGui class
#@+node:edream.110203113231.346:wxLeoApp class
class wxLeoApp (wx.App):
    #@    @+others
    #@+node:edream.110203113231.347:OnInit  (wxLeoApp)
    def OnInit(self):
    
        self.SetAppName("Leo")
    
        return True
    #@nonl
    #@-node:edream.110203113231.347:OnInit  (wxLeoApp)
    #@+node:edream.110203113231.348:OnExit
    def OnExit(self):
    
        return True
    #@-node:edream.110203113231.348:OnExit
    #@-others
#@-node:edream.110203113231.346:wxLeoApp class
#@+node:edream.110203113231.539:wxLeoBody class
class wxLeoBody (leoFrame.leoBody):
    
    """A class to create a wxPython body pane."""
    
    #@    @+others
    #@+node:edream.110203113231.540:Birth & death (wxLeoBody)
    #@+node:edream.110203113231.541:wxBody.__init__
    def __init__ (self,frame,parentFrame):
    
        # Init the base class: calls createControl.
        leoFrame.leoBody.__init__(self,frame,parentFrame)
        
        self.bodyCtrl = self.createControl(frame,parentFrame)
    
        self.colorizer = leoColor.colorizer(self.c)
    
        ### self.styles = {} # For syntax coloring.
        
        self.keyDownModifiers = None
    #@nonl
    #@-node:edream.110203113231.541:wxBody.__init__
    #@+node:edream.110203113231.542:wxBody.createControl
    def createControl (self,frame,parentFrame):
        
        w = g.app.gui.leoTextWidgetClass(
            parentFrame,
            pos = wx.DefaultPosition,
            size = wx.DefaultSize,
            style = (wx.TE_RICH | wx.TE_RICH2 | wx.TE_MULTILINE),
            name = 'body', # Must be body for k.masterKeyHandler.
        )
    
        # wx.EVT_CHAR(w,self.onKey) # Provides translated keycodes.
        wx.EVT_KEY_DOWN(w,self.onKeyDown) # Provides raw key codes.
        wx.EVT_KEY_UP(w,self.onKeyUp) # Provides raw key codes.
    
        return w
    #@-node:edream.110203113231.542:wxBody.createControl
    #@+node:ekr.20061116072544:wxBody.createBindings
    def createBindings (self,w=None):
    
        '''(wxBody) Create gui-dependent bindings.
        These are *not* made in nullBody instances.'''
    
        frame = self.frame ; c = self.c ; k = c.k
        if not w: w = self.bodyCtrl
        
        # g.trace('wxBody')
        
        w.bind('<Key>', k.masterKeyHandler)
        
        for kind,func,handler in (
            #('<Button-1>',  frame.OnBodyClick,          k.masterClickHandler),
            #('<Button-3>',  frame.OnBodyRClick,         k.masterClick3Handler),
            #('<Double-1>',  frame.OnBodyDoubleClick,    k.masterDoubleClickHandler),
            #('<Double-3>',  None,                       k.masterDoubleClick3Handler),
            #('<Button-2>',  frame.OnPaste,              k.masterClickHandler),
        ):
            def bodyClickCallback(event,handler=handler,func=func):
                return handler(event,func)
    
            w.bind(kind,bodyClickCallback)
    #@nonl
    #@-node:ekr.20061116072544:wxBody.createBindings
    #@+node:ekr.20061111183138:wxBody.setEditorColors
    def setEditorColors (self,bg,fg):
        pass
    #@nonl
    #@-node:ekr.20061111183138:wxBody.setEditorColors
    #@-node:edream.110203113231.540:Birth & death (wxLeoBody)
    #@+node:edream.111303204836:Tk wrappers (wxBody)
    #@+node:edream.111303204517:Color tags (wxBody)
    #@+node:edream.111303205611:wxBody.tag_add
    def tag_add (self,tagName,index1,index2):
        
        return self.bodyCtrl.tag_add(tagName,index1,index2)
        
    #@nonl
    #@-node:edream.111303205611:wxBody.tag_add
    #@+node:edream.111303205611.1:wxBody.tag_bind
    def tag_bind (self,tagName,event,callback):
        
        pass ; g.trace(tagName,event,callback)
    #@-node:edream.111303205611.1:wxBody.tag_bind
    #@+node:edream.111303205611.2:wxBody.tag_configure
    def tag_configure (self,colorName,**keys):
        
        return self.bodyCtrl.tag_configure(colorName,**keys)
    #@-node:edream.111303205611.2:wxBody.tag_configure
    #@+node:edream.111303205611.3:wxBody.tag_delete
    def tag_delete(self,tagName):
    
        if tagName == "keyword": # A kludge.
    
            # g.trace(tagName)
            style = wx.TextAttr(wx.BLACK)
            last = self.bodyCtrl.GetLastPosition()
            
            if 1: # This may cause the screen flash.
                self.bodyCtrl.SetStyle(0,last,style)
    #@nonl
    #@-node:edream.111303205611.3:wxBody.tag_delete
    #@+node:edream.111303205611.4:wxBody.tag_remove
    def tag_remove (self,tagName,index1,index2):
        
        pass # g.trace(tagName,index1,index2)
    #@-node:edream.111303205611.4:wxBody.tag_remove
    #@-node:edream.111303204517:Color tags (wxBody)
    #@+node:edream.110203113231.544:Configuration (wxBody) (To do)
    def cget(self,*args,**keys):
        
        pass
        
        # val = self.bodyCtrl.cget(*args,**keys)
        # if g.app.trace:
            # g.trace(val,args,keys)
        # return val
        
    def configure (self,*args,**keys):
        
        if g.app.trace: g.trace(args,keys)
    
        # return self.bodyCtrl.configure(*args,**keys)
    #@nonl
    #@-node:edream.110203113231.544:Configuration (wxBody) (To do)
    #@+node:edream.110203113231.545:Focus...
    def hasFocus (self):
        
        return self.bodyCtrl == self.bodyCtrl.FindFocus()
    
    def setFocus (self):
        
        self.bodyCtrl.SetFocus()
    #@-node:edream.110203113231.545:Focus...
    #@+node:edream.110203113231.549:Height & width
    def getBodyPaneHeight (self):
    
        return self.bodyCtrl.GetCharHeight()
        
    def getBodyPaneWidth (self):
    
        return self.bodyCtrl.GetCharWidth()
    #@nonl
    #@-node:edream.110203113231.549:Height & width
    #@+node:edream.110203113231.548:Idle-time (wxBody) (to do)
    def scheduleIdleTimeRoutine (self,function,*args,**keys):
    
        g.trace()
    #@nonl
    #@-node:edream.110203113231.548:Idle-time (wxBody) (to do)
    #@-node:edream.111303204836:Tk wrappers (wxBody)
    #@+node:ekr.20061116083454:wxBody.onKeyUp/Down
    useWX = False # True, use native key handling.  False, call masterKeyHandler.
    
    def onKeyDown (self,event,*args,**keys):
        keycode = event.GetKeyCode()
        self.keyDownModifiers = event.GetModifiers()
        if keycode == wx.WXK_ALT:
            event.Skip() # Do default processing.
        elif self.useWX:
            event.Skip()
        else:
            pass # This is required to suppress wx event handling.
        
    def onKeyUp (self,event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_ALT:
            # g.trace('wxBody: alt')
            event.Skip() # Do default processing.
        elif self.useWX:
            event.Skip()
        else:
            event.keyDownModifiers = self.keyDownModifiers
            event = g.app.gui.leoKeyEvent(event,c=self.c) # Convert event to canonical form.
            # g.trace('wxBody',event.keysym)
            if event.keysym: # The key may have been a raw key.
                self.c.k.masterKeyHandler(event,stroke=event.keysym)
    #@-node:ekr.20061116083454:wxBody.onKeyUp/Down
    #@+node:ekr.20061116064914:onBodyChanged
    def onBodyChanged (self,undoType,oldSel=None,oldText=None,oldYview=None):
        
        # g.trace('undoType',undoType,'oldSel',oldSel,'len(oldText)',oldText and len(oldText) or 0)
        
        c = self.c ; w = c.frame.body.bodyCtrl
        if not c:  return g.trace('no c!')
        p = c.currentPosition()
        if not p: return g.trace('no p!')
        if self.frame.lockout > 0: return g.trace('lockout!',g.callers())
    
        self.frame.lockout += 1
        try:
            s = wx.TextCtrl.GetValue(w)
            changed = s != p.bodyString()
            # g.trace('changed',changed,len(s),p.headString(),g.callers())
            if changed:
                p.v.t.setTnodeText(s)
                p.v.t.insertSpot = w.getInsertPoint()
                if 0: # This causes flash even when nothing is actually colored!
                    self.frame.body.recolor_now(p)
                if not c.changed: c.setChanged(True)
                c.frame.tree.updateVisibleIcons(p)
        finally:
            self.frame.lockout -= 1
    #@nonl
    #@-node:ekr.20061116064914:onBodyChanged
    #@-others
#@nonl
#@-node:edream.110203113231.539:wxLeoBody class
#@+node:edream.110203113231.349:wxLeoFrame class (leoFrame)
class wxLeoFrame(leoFrame.leoFrame):
        
    """A class to create a wxPython from for the main Leo window."""

    #@    @+others
    #@+node:edream.110203113231.350:Birth & death (wxLeoFrame)
    #@+node:edream.110203113231.266:__init__ (wxLeoFrame)
    def __init__ (self,title):
        
        # Init the base classes.
        
        leoFrame.leoFrame.__init__(self,g.app.gui) # Clears self.title.
        
        self.title = title
        self.c = None # set in finishCreate.
        self.bodyCtrl = None # set in finishCreate
        
        # g.trace("wxLeoFrame",title)
        self.activeFrame = None
        self.focusWidget = None
        self.iconBar = None
        self.iconBarClass = wxLeoIconBar
        self.lockout = 0 # Suppress further events
        self.quitting = False
        self.updateCount = 0
        self.treeIniting = False
        self.drawing = False # Lockout recursive draws.
        self.menuIdDict = {}
        self.menuBar = None
        self.ratio = 0.5
        self.secondary_ratio = 0.5
        self.startupWindow=False
        self.statusLineClass = wxStatusLineClass
        self.use_coloring = False # set True to enable coloring
    #@-node:edream.110203113231.266:__init__ (wxLeoFrame)
    #@+node:edream.110203113231.351:__repr__
    def __repr__ (self):
        
        return "wxLeoFrame: " + self.title
    #@nonl
    #@-node:edream.110203113231.351:__repr__
    #@+node:edream.110203113231.260:finishCreate (wxLeoFrame)
    def finishCreate (self,c):
        
        # g.trace('wxLeoFrame')
        frame = self
        frame.c = c
        c.frame = frame
        
        self.topFrame = self.top = top = wx.Frame(
            parent=None, id=-1, title=self.title,
            pos = (200,50),size = (950, 720),
            style=wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)
            
        # Set the official ivars.
        self.topFrame = self.top = self.outerFrame = top
        
        # Create the icon area.
        self.iconBar = wxLeoIconBar(c,parentFrame=top)
        
        # Create the splitters.
        style = wx.CLIP_CHILDREN|wx.SP_LIVE_UPDATE|wx.SP_3D
        self.splitter1 = splitter1 = wx.SplitterWindow(top,-1,style=style) # Contains body & splitter2
        self.splitter2 = splitter2 = wx.SplitterWindow(splitter1,-1,style=style) # Contains tree and log.
        
        # Create the tree.
        self.tree = wxLeoTree(frame,parentFrame=splitter2)
        
        # Create the log pane and its wx.Noteboook.
        self.nb = nb = wx.Notebook(splitter2,-1,style=wx.CLIP_CHILDREN)
        self.log = wxLeoLog(c,nb)
        g.app.setLog(self.log) # writeWaitingLog hangs without this(!)
        
        # Create the body pane.
        self.body = wxLeoBody(frame,parentFrame=splitter1)
        self.bodyCtrl = frame.body.bodyCtrl
        
        # Add the panes to the splitters.
        splitter1.SplitHorizontally(splitter2,self.bodyCtrl,0)
        splitter2.SplitVertically(self.tree.treeCtrl,nb,0)
        
        # Create the minibuffer
        self.minibuffer = wxLeoMinibuffer(c,top)
        ctrl = self.minibuffer.ctrl
        box = wx.BoxSizer(wx.VERTICAL)
        box2 = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(splitter1,1,wx.EXPAND)
        label = wx.StaticText(top,label='Minibuffer')
        label.SetBackgroundColour('light grey')
        label.SetForegroundColour('red')
        box2.Add(label,0,wx.EXPAND)
        box2.Add(ctrl,1,wx.EXPAND)
        box.Add(box2,0,wx.EXPAND)
        self.top.SetSizer(box)
    
        # Create the menus & icon.
        self.menu = wxLeoMenu(frame)
        self.setWindowIcon()
        
        top.Show(True)
        
        self.setEventHandlers()
        self.colorizer = self.body.colorizer
        c.initVersion()
        self.signOnWithVersion()
        self.injectCallbacks()
        g.app.windowList.append(self)
        self.tree.redraw()
    
        self.setFocus(g.choose(
            c.config.getBool('outline_pane_has_initial_focus'),
            self.tree.treeCtrl,self.bodyCtrl))
    #@+node:edream.110203113231.261:createSplitters
    #@-node:edream.110203113231.261:createSplitters
    #@+node:edream.110203113231.265:setWindowIcon
    def setWindowIcon(self):
    
        if wx.Platform == "__WXMSW__":
        
            path = os.path.join(g.app.loadDir,"..","Icons","LeoApp16.ico")
            icon = wx.Icon(path,wx.BITMAP_TYPE_ICO,16,16)
            self.top.SetIcon(icon)
    #@-node:edream.110203113231.265:setWindowIcon
    #@+node:edream.110203113231.264:setEventHandlers
    def setEventHandlers (self):
        
        w = self.top
    
        # if wx.Platform == "__WXMSW__": # Activate events exist only on Windows.
            # wx.EVT_ACTIVATE(self.top,self.onActivate)
        # else:
            # wx.EVT_SET_FOCUS(self.top,self.OnSetFocus)
        
        # wx.EVT_CLOSE(self.top,self.onCloseLeoFrame)
        
        # wx.EVT_MENU_OPEN(self.top,self.updateAllMenus)
        
        if wx.Platform == "__WXMSW__": # Activate events exist only on Windows.
            w.Bind(wx.EVT_ACTIVATE,self.onActivate)
        else:
            w.Bind(wx.EVT_SET_FOCUS,self.OnSetFocus)
        
        w.Bind(wx.EVT_CLOSE,self.onCloseLeoFrame)
        
        w.Bind(wx.EVT_MENU_OPEN,self.updateAllMenus) 
    #@-node:edream.110203113231.264:setEventHandlers
    #@-node:edream.110203113231.260:finishCreate (wxLeoFrame)
    #@+node:edream.111403141810:initialRatios
    def initialRatios (self):
    
        config = g.app.config
        s = config.getWindowPref("initial_splitter_orientation")
        verticalFlag = s == None or (s != "h" and s != "horizontal")
        
        # Tweaked for tk.  Other tweaks may be best for wx.
        if verticalFlag:
            r = config.getFloatWindowPref("initial_vertical_ratio")
            if r == None or r < 0.0 or r > 1.0: r = 0.5
            r2 = config.getFloatWindowPref("initial_vertical_secondary_ratio")
            if r2 == None or r2 < 0.0 or r2 > 1.0: r2 = 0.8
        else:
            r = config.getFloatWindowPref("initial_horizontal_ratio")
            if r == None or r < 0.0 or r > 1.0: r = 0.3
            r2 = config.getFloatWindowPref("initial_horizontal_secondary_ratio")
            if r2 == None or r2 < 0.0 or r2 > 1.0: r2 = 0.8
    
        return verticalFlag,r,r2
    #@nonl
    #@-node:edream.111403141810:initialRatios
    #@+node:edream.111503105816:injectCallbacks
    def injectCallbacks(self):
        
        import leoNodes
        
        # Some callback is required.
        def doNothingCallback(*args,**keys):
            pass
    
        for name in (
            "OnBoxClick","OnDrag","OnEndDrag",
            "OnHeadlineClick","OnHeadlineRightClick","OnHeadlineKey",
            "OnHyperLinkControlClick","OnHyperLinkEnter","OnHyperLinkLeave",
            "OnIconClick","OnIconDoubleClick","OnIconRightClick"):
    
            # g.trace(f)
            g.funcToMethod(doNothingCallback,leoNodes.vnode,name=name)
    #@nonl
    #@-node:edream.111503105816:injectCallbacks
    #@+node:edream.111303141147:signOnWithVersion
    def signOnWithVersion (self):
    
        c = self.c
        color = c.config.getColor("log_error_color")
        signon = c.getSignOnLine()
        n1,n2,n3,junk,junk=sys.version_info
        
        g.es("Leo Log Window...",color=color)
        g.es(signon)
        g.es("Python %d.%d.%d wxWindows %s" % (n1,n2,n3,wx.VERSION_STRING))
        g.enl()
    #@nonl
    #@-node:edream.111303141147:signOnWithVersion
    #@+node:ekr.20061118122218:setMinibufferBindings
    def setMinibufferBindings(self):
        
        pass
        
        # g.trace('to do')
    #@nonl
    #@-node:ekr.20061118122218:setMinibufferBindings
    #@+node:edream.111503213533:destroySelf
    def destroySelf(self):
        
        self.top.Destroy()
    #@nonl
    #@-node:edream.111503213533:destroySelf
    #@-node:edream.110203113231.350:Birth & death (wxLeoFrame)
    #@+node:edream.110203113231.267:event handlers
    #@+node:edream.110203113231.268:Frame events
    #@+node:edream.110203113231.269:onActivate & OnSetFocus
    if wx.Platform == '__WXMSW__':
        
        def onActivate(self,event):
            if event.GetActive():
                self.activeFrame = self
                if self.c:
                    pass ## self.c.checkAllFileDates()
    else:
        
        def OnSetFocus(self,event):
            self.activeFrame = self
            if self.c:
                self.c.checkAllFileDates()
    #@-node:edream.110203113231.269:onActivate & OnSetFocus
    #@+node:edream.110203113231.270:onCloseLeoFrame
    def onCloseLeoFrame(self,event):
    
        frame = self
        
        # The g.app class does all the hard work now.
        if not g.app.closeLeoWindow(frame):
            if event.CanVeto():
                event.Veto()
    #@nonl
    #@-node:edream.110203113231.270:onCloseLeoFrame
    #@+node:edream.110203113231.273:onResize
    def onResize(self,event):
    
        if mIniting:
            return # Can be called during initialization.
    
        # Resize splitter1 with equal sized panes.
        size = self.splitter1.GetClientSize()
        self.splitter1.SetClientSize(size)
        w = size.GetWidth() ; h = size.GetHeight()
        if self.splitter1.GetSplitMode()== wx.SPLIT_VERTICAL:
            self.splitter1.SetSashPosition(w/2,True)
        else:
            self.splitter1.SetSashPosition(h/2,True)
    
        # Resize splitter2 with equal sized panes.
        size = self.splitter2.GetClientSize()
        w = size.GetWidth() ; h = size.GetHeight()
        if self.splitter2.GetSplitMode()== wx.SPLIT_VERTICAL:
            self.splitter2.SetSashPosition((3*w)/5,True)
        else:
            self.splitter2.SetSashPosition((3*h)/5,True)
    #@-node:edream.110203113231.273:onResize
    #@-node:edream.110203113231.268:Frame events
    #@-node:edream.110203113231.267:event handlers
    #@+node:edream.110203113231.379:wxFrame dummy routines: (to do: minor)
    def after_idle(*args):
        pass
        
    def bringToFront(self):
        pass
    
    def get_window_info (self):
        """Return the window information."""
        return g.app.gui.get_window_info(self.topFrame)
    
    def resizePanesToRatio(self,ratio1,ratio2):
        pass
    
    def setInitialWindowGeometry (self):
        pass
    
    def setTopGeometry (self,w,h,x,y,adjustSize=True):
        pass
    
    def lift (self):
        self.top.Raise()
    
    def update (self):
        pass
    #@nonl
    #@-node:edream.110203113231.379:wxFrame dummy routines: (to do: minor)
    #@+node:edream.110203113231.378:Externally visible routines...
    #@+node:edream.110203113231.380:deiconify
    def deiconify (self):
    
        self.top.Iconize(False)
    #@nonl
    #@-node:edream.110203113231.380:deiconify
    #@+node:edream.110203113231.381:getTitle
    def getTitle (self):
        
        return self.title
    #@-node:edream.110203113231.381:getTitle
    #@+node:edream.111303135410:setTitle
    def setTitle (self,title):
    
        self.title = title
        self.top.SetTitle(title) # Call the wx code.
    #@nonl
    #@-node:edream.111303135410:setTitle
    #@-node:edream.110203113231.378:Externally visible routines...
    #@+node:edream.111303100039:Gui-dependent commands (to do)
    #@+node:ekr.20061211083200:setFocus (wxFrame)
    def setFocus (self,w):
    
        # g.trace(w,g.app.gui.widget_name(w))
         
        w.SetFocus()
        self.focusWidget = w
    #@nonl
    #@-node:ekr.20061211083200:setFocus (wxFrame)
    #@+node:ekr.20061106070201:Minibuffer commands... (wxFrame)
    
    #@+node:ekr.20061106070201.1:contractPane
    def contractPane (self,event=None):
        
        '''Contract the selected pane.'''
        
        f = self ; c = f.c
        w = c.get_requested_focus()
        wname = c.widget_name(w)
    
        # g.trace(wname)
        if not w: return
        
        if wname.startswith('body'):
            f.contractBodyPane()
        elif wname.startswith('log'):
            f.contractLogPane()
        elif wname.startswith('head') or wname.startswith('canvas'):
            f.contractOutlinePane()
    #@-node:ekr.20061106070201.1:contractPane
    #@+node:ekr.20061106070201.2:expandPane
    def expandPane (self,event=None):
        
        '''Expand the selected pane.'''
    
        f = self ; c = f.c
            
        w = c.get_requested_focus()
        wname = c.widget_name(w)
    
        # g.trace(wname)
        if not w: return
        
        if wname.startswith('body'):
            f.expandBodyPane()
        elif wname.startswith('log'):
            f.expandLogPane()
        elif wname.startswith('head') or wname.startswith('canvas'):
            f.expandOutlinePane()
    #@-node:ekr.20061106070201.2:expandPane
    #@+node:ekr.20061106070201.3:fullyExpandPane
    def fullyExpandPane (self,event=None):
        
        '''Fully expand the selected pane.'''
    
        f = self ; c = f.c
            
        w = c.get_requested_focus()
        wname = c.widget_name(w)
    
        # g.trace(wname)
        if not w: return
        
        if wname.startswith('body'):
            f.fullyExpandBodyPane()
        elif wname.startswith('log'):
            f.fullyExpandLogPane()
        elif wname.startswith('head') or wname.startswith('canvas'):
            f.fullyExpandOutlinePane()
    #@-node:ekr.20061106070201.3:fullyExpandPane
    #@+node:ekr.20061106070201.4:hidePane
    def hidePane (self,event=None):
        
        '''Completely contract the selected pane.'''
    
        f = self ; c = f.c
            
        w = c.get_requested_focus()
        wname = c.widget_name(w)
    
        if not w: return
        
        if wname.startswith('body'):
            f.hideBodyPane()
            c.treeWantsFocusNow()
        elif wname.startswith('log'):
            f.hideLogPane()
            c.bodyWantsFocusNow()
        elif wname.startswith('head') or wname.startswith('canvas'):
            f.hideOutlinePane()
            c.bodyWantsFocusNow()
    #@-node:ekr.20061106070201.4:hidePane
    #@+node:ekr.20061106070201.5:expand/contract/hide...Pane
    #@+at 
    #@nonl
    # The first arg to divideLeoSplitter means the following:
    # 
    #     f.splitVerticalFlag: use the primary   (tree/body) ratio.
    # not f.splitVerticalFlag: use the secondary (tree/log) ratio.
    #@-at
    #@@c
    
    def contractBodyPane (self,event=None):
        '''Contract the body pane.'''
        f = self ; r = min(1.0,f.ratio+0.1)
        f.divideLeoSplitter(f.splitVerticalFlag,r)
    
    def contractLogPane (self,event=None):
        '''Contract the log pane.'''
        f = self ; r = min(1.0,f.ratio+0.1)
        f.divideLeoSplitter(not f.splitVerticalFlag,r)
    
    def contractOutlinePane (self,event=None):
        '''Contract the outline pane.'''
        f = self ; r = max(0.0,f.ratio-0.1)
        f.divideLeoSplitter(f.splitVerticalFlag,r)
        
    def expandBodyPane (self,event=None):
        '''Expand the body pane.'''
        self.contractOutlinePane()
    
    def expandLogPane(self,event=None):
        '''Expand the log pane.'''
        f = self ; r = max(0.0,f.ratio-0.1)
        f.divideLeoSplitter(not f.splitVerticalFlag,r)
        
    def expandOutlinePane (self,event=None):
        '''Expand the outline pane.'''
        self.contractBodyPane()
    #@-node:ekr.20061106070201.5:expand/contract/hide...Pane
    #@+node:ekr.20061106070201.6:fullyExpand/hide...Pane
    def fullyExpandBodyPane (self,event=None):
        '''Fully expand the body pane.'''
        f = self ; f.divideLeoSplitter(f.splitVerticalFlag,0.0)
    
    def fullyExpandLogPane (self,event=None):
        '''Fully expand the log pane.'''
        f = self ; f.divideLeoSplitter(not f.splitVerticalFlag,0.0)
    
    def fullyExpandOutlinePane (self,event=None):
        '''Fully expand the outline pane.'''
        f = self ; f.divideLeoSplitter(f.splitVerticalFlag,1.0)
        
    def hideBodyPane (self,event=None):
        '''Completely contract the body pane.'''
        f = self ; f.divideLeoSplitter(f.splitVerticalFlag,1.0)
    
    def hideLogPane (self,event=None):
        '''Completely contract the log pane.'''
        f = self ; f.divideLeoSplitter(not f.splitVerticalFlag,1.0)
    
    def hideOutlinePane (self,event=None):
        '''Completely contract the outline pane.'''
        f = self ; f.divideLeoSplitter(f.splitVerticalFlag,0.0)
    #@-node:ekr.20061106070201.6:fullyExpand/hide...Pane
    #@-node:ekr.20061106070201:Minibuffer commands... (wxFrame)
    #@+node:edream.111303100039.1:Edit Menu... (wxLeoFrame)
    #@+node:edream.111303101257:abortEditLabelCommand
    def abortEditLabelCommand (self,event=None):
    
        g.es("abortEditLabelCommand not ready yet")
        return
        
        c = self.c ; v = c.currentVnode ; tree = self.tree
        # g.trace(v)
        if self.revertHeadline and c.edit_widget(v) and v == self.editVnode:
            
            # g.trace(`self.revertHeadline`)
            c.edit_widget(v).delete("1.0","end")
            c.edit_widget(v).insert("end",self.revertHeadline)
            tree.idle_head_key(v) # Must be done immediately.
            tree.revertHeadline = None
            tree.select(v)
            if v and len(v.t.joinList) > 0:
                # 3/26/03: changed redraw_now to force_redraw.
                tree.force_redraw() # force a redraw of joined headlines.
    #@nonl
    #@-node:edream.111303101257:abortEditLabelCommand
    #@+node:edream.111303101257.1:endEditLabelCommand
    def endEditLabelCommand (self,event=None):
        
        g.es("endEditLabelCommand not ready yet")
        return
    
        c = self.c ; tree = self.tree ; v = self.editVnode
        w = c.frame.body.bodyCtrl
    
        if v and c.edit_widget(v):
            tree.select(v)
    
        if v: # Bug fix 10/9/02: also redraw ancestor headlines.
            # 3/26/03: changed redraw_now to force_redraw.
            tree.force_redraw() # force a redraw of joined headlines.
    
        g.app.gui.set_focus(c,w)
    #@nonl
    #@-node:edream.111303101257.1:endEditLabelCommand
    #@+node:edream.111303100039.6:insertHeadlineTime
    def insertHeadlineTime (self,event=None):
        
        g.es("insertHeadlineTime not ready yet")
        return
    
        frame = self ; c = frame.c
        w = c.edit_widget(v)
        v = c.currentVnode()
        h = v.headString() # Remember the old value.
    
        if w:
            stamp = c.getTime(body=False)
            sel1,sel2 = w.getSelectionRange()
            if sel1 and sel2 and sel1 != sel2:
                w.delete(sel1,sel2)
            i = w.getInsertPoint()
            w.insert(i,stamp)
            frame.idle_head_key(v)
    
        # A kludge to get around not knowing whether we are editing or not.
        if h.strip() == v.headString().strip():
            g.es("Edit headline to append date/time")
    #@nonl
    #@-node:edream.111303100039.6:insertHeadlineTime
    #@-node:edream.111303100039.1:Edit Menu... (wxLeoFrame)
    #@+node:edream.111303100039.7:Window Menu
    #@+node:edream.111303100039.8:cascade
    def cascade(self,event=None):
        
        g.es("cascade not ready yet")
        return
    
        x,y,delta = 10,10,10
        for frame in g.app.windowList:
            top = frame.top
            # Compute w,h
            top.update_idletasks() # Required to get proper info.
            geom = top.geometry() # geom = "WidthxHeight+XOffset+YOffset"
            dim,junkx,junky = string.split(geom,'+')
            w,h = string.split(dim,'x')
            w,h = int(w),int(h)
            # Set new x,y and old w,h
            frame.setTopGeometry(w,h,x,y)
            # Compute the new offsets.
            x += 30 ; y += 30
            if x > 200:
                x = 10 + delta ; y = 40 + delta
                delta += 10
    #@nonl
    #@-node:edream.111303100039.8:cascade
    #@+node:edream.111303100039.9:equalSizedPanes
    def equalSizedPanes(self,event=None):
        
        g.es("equalSizedPanes not ready yet")
        return
    
        frame = self
        frame.resizePanesToRatio(0.5,frame.secondary_ratio)
    #@-node:edream.111303100039.9:equalSizedPanes
    #@+node:edream.111303100039.10:hideLogWindow
    def hideLogWindow (self,event=None):
        
        g.es("hideLogWindow not ready yet")
        return
        
        frame = self
        frame.divideLeoSplitter2(0.99, not frame.splitVerticalFlag)
    #@nonl
    #@-node:edream.111303100039.10:hideLogWindow
    #@+node:edream.111303100039.11:minimizeAll
    def minimizeAll(self,event=None):
        
        g.es("minimizeAll not ready yet")
        return
    
        self.minimize(g.app.findFrame)
        self.minimize(g.app.pythonFrame)
        for frame in g.app.windowList:
            self.minimize(frame)
        
    def minimize(self, frame):
    
        if frame:
            frame.Show(False)
    #@nonl
    #@-node:edream.111303100039.11:minimizeAll
    #@+node:edream.111303101709:toggleActivePane
    def toggleActivePane(self,event=None): # wxFrame.
    
        w = self.focusWidget or self.body.bodyCtrl
        
        w = g.choose(w == self.bodyCtrl,self.tree.treeCtrl,self.bodyCtrl)
            
        w.SetFocus()
        self.focusWidget = w
    #@nonl
    #@-node:edream.111303101709:toggleActivePane
    #@+node:edream.111303100039.12:toggleSplitDirection
    # The key invariant: self.splitVerticalFlag tells the alignment of the main splitter.
    def toggleSplitDirection(self,event=None):
        
        g.es("toggleSplitDirection not ready yet")
        return
    
        # Abbreviations.
        frame = self
        bar1 = self.bar1 ; bar2 = self.bar2
        split1Pane1,split1Pane2 = self.split1Pane1,self.split1Pane2
        split2Pane1,split2Pane2 = self.split2Pane1,self.split2Pane2
        # Switch directions.
        verticalFlag = self.splitVerticalFlag = not self.splitVerticalFlag
        orientation = g.choose(verticalFlag,"vertical","horizontal")
        g.app.config.setWindowPref("initial_splitter_orientation",orientation)
        # Reconfigure the bars.
        bar1.place_forget()
        bar2.place_forget()
        self.configureBar(bar1,verticalFlag)
        self.configureBar(bar2,not verticalFlag)
        # Make the initial placements again.
        self.placeSplitter(bar1,split1Pane1,split1Pane2,verticalFlag)
        self.placeSplitter(bar2,split2Pane1,split2Pane2,not verticalFlag)
        # Adjust the log and body panes to give more room around the bars.
        self.reconfigurePanes()
        # Redraw with an appropriate ratio.
        vflag,ratio,secondary_ratio = frame.initialRatios()
        self.resizePanesToRatio(ratio,secondary_ratio)
    #@nonl
    #@-node:edream.111303100039.12:toggleSplitDirection
    #@-node:edream.111303100039.7:Window Menu
    #@+node:edream.111703103908:Help Menu...
    #@+node:edream.111703103908.2:leoHelp
    def leoHelp (self):
        
        g.es("leoHelp not ready yet")
        
        return ##
        
        file = os.path.join(g.app.loadDir,"..","doc","sbooks.chm")
        file = g.toUnicode(file,g.app.tkEncoding) # 10/20/03
    
        if os.path.exists(file):
            os.startfile(file)
        else:	
            answer = g.app.gui.runAskYesNoDialog(c,
                "Download Tutorial?",
                "Download tutorial (sbooks.chm) from SourceForge?")
    
            if answer == "yes":
                try:
                    if 0: # Download directly.  (showProgressBar needs a lot of work)
                        url = "http://umn.dl.sourceforge.net/sourceforge/leo/sbooks.chm"
                        import urllib
                        self.scale = None
                        urllib.urlretrieve(url,file,self.showProgressBar)
                        if self.scale:
                            self.scale.destroy()
                            self.scale = None
                    else:
                        url = "http://prdownloads.sourceforge.net/leo/sbooks.chm?download"
                        import webbrowser
                        os.chdir(g.app.loadDir)
                        webbrowser.open_new(url)
                except:
                    g.es("exception dowloading sbooks.chm")
                    g.es_exception()
    #@nonl
    #@+node:edream.111703103908.3:showProgressBar
    def showProgressBar (self,count,size,total):
    
        # g.trace("count,size,total:" + `count` + "," + `size` + "," + `total`)
        if self.scale == None:
            #@        << create the scale widget >>
            #@+node:edream.111703103908.4:<< create the scale widget >>
            top = Tk.Toplevel()
            top.title("Download progress")
            self.scale = scale = Tk.Scale(top,state="normal",orient="horizontal",from_=0,to=total)
            scale.pack()
            top.lift()
            #@nonl
            #@-node:edream.111703103908.4:<< create the scale widget >>
            #@nl
        self.scale.set(count*size)
        self.scale.update_idletasks()
    #@nonl
    #@-node:edream.111703103908.3:showProgressBar
    #@-node:edream.111703103908.2:leoHelp
    #@-node:edream.111703103908:Help Menu...
    #@-node:edream.111303100039:Gui-dependent commands (to do)
    #@+node:edream.110203113231.384:updateAllMenus (wxFrame)
    def updateAllMenus(self,event):
        
        """Called whenever any menu is pulled down."""
        
        # We define this routine to strip off the even param.
        
        self.menu.updateAllMenus()
    #@nonl
    #@-node:edream.110203113231.384:updateAllMenus (wxFrame)
    #@-others
#@nonl
#@-node:edream.110203113231.349:wxLeoFrame class (leoFrame)
#@+node:ekr.20061118090713:wxLeoIconBar class
class wxLeoIconBar:
    
    '''An adaptor class that uses a wx.ToolBar for Leo's icon area.'''
    
    #@    @+others
    #@+node:ekr.20061119105509.1:__init__ wxLeoIconBar
    def __init__(self,c,parentFrame): # wxLeoIconBar
    
        self.c = c
        self.widgets = []
        self.toolbar = self.iconFrame = parentFrame.CreateToolBar() # A wxFrame method
    
        # Set the official ivar.
        c.frame.iconFrame = self.iconFrame
    #@-node:ekr.20061119105509.1:__init__ wxLeoIconBar
    #@+node:ekr.20061119105509.2:add
    def add(self,*args,**keys):
        
        """Add a button containing text or a picture to the icon bar.
        
        Pictures take precedence over text"""
        
        toolbar = self.toolbar
        text = keys.get('text') or ''
        #imagefile = keys.get('imagefile')
        #image = keys.get('image')
        bg = keys.get('bg')
        command = keys.get('command')
        
        # Create the button with a unique id.
        id = wx.NewId()
        b = wx.Button(toolbar,id,label=text)
        self.widgets.append(b)
        
        # Right-clicks delete the button.
        def onRClickCallback(event,self=self,b=b):
            self.deleteButton(b)
        b.Bind(wx.EVT_RIGHT_UP,onRClickCallback)
    
        self.setCommandForButton(b,command)
        tool = toolbar.AddControl(b)
        toolbar.Realize()
        return b
        
        # if imagefile or image:
            # < < create a picture > >
        # elif text:
            # b = Tk.Button(f,text=text,relief="groove",bd=2,command=command)
    #@+node:ekr.20061119105509.3:create a picture
    # try:
        # if imagefile:
            # # Create the image.  Throws an exception if file not found
            # imagefile = g.os_path_join(g.app.loadDir,imagefile)
            # imagefile = g.os_path_normpath(imagefile)
            # image = Tk.PhotoImage(master=g.app.root,file=imagefile)
            
            # # Must keep a reference to the image!
            # try:
                # refs = g.app.iconImageRefs
            # except:
                # refs = g.app.iconImageRefs = []
        
            # refs.append((imagefile,image),)
        
        # if not bg:
            # bg = f.cget("bg")
    
        # b = Tk.Button(f,image=image,relief="flat",bd=0,command=command,bg=bg)
        # b.pack(side="left",fill="y")
        # return b
        
    # except:
        # g.es_exception()
        # return None
    #@-node:ekr.20061119105509.3:create a picture
    #@-node:ekr.20061119105509.2:add
    #@+node:ekr.20061119105509.4:clear
    def clear(self):
        
        """Destroy all the widgets in the icon bar"""
        
        for w in self.widgets:
            self.toolbar.RemoveTool(w.GetId())
        self.widgets = []
    #@-node:ekr.20061119105509.4:clear
    #@+node:ekr.20061213092323:deleteButton
    def deleteButton (self,w):
        
        self.toolbar.RemoveTool(w.GetId())
    #@-node:ekr.20061213092323:deleteButton
    #@+node:ekr.20061119105509.5:getFrame
    def getFrame (self):
    
        return self.iconFrame
    #@-node:ekr.20061119105509.5:getFrame
    #@+node:ekr.20061213092105:setCommandForButton
    def setCommandForButton(self,b,command):
        
        if command:
            def onClickCallback(event=None,command=command):
                command(event=event)
        
            self.toolbar.Bind(wx.EVT_BUTTON,onClickCallback,b)
    #@-node:ekr.20061213092105:setCommandForButton
    #@+node:ekr.20061213094526:show/hide (do nothings)
    def pack (self):    pass  
    def unpack (self):  pass 
    show = pack   
    hide = unpack
    #@-node:ekr.20061213094526:show/hide (do nothings)
    #@-others
#@-node:ekr.20061118090713:wxLeoIconBar class
#@+node:edream.110203113231.553:wxLeoLog class
class wxLeoLog (leoFrame.leoLog):
    
    """The base class for the log pane in Leo windows."""
    
    #@    @+others
    #@+node:edream.110203113231.554:leoLog.__init__
    def __init__ (self,c,nb):
    
        self.c = c
        self.nb = nb
        
        self.isNull = False
        self.logCtrl = None
        self.newlines = 0
        self.frameDict = {} # Keys are log names, values are None or wx.Frames.
        self.textDict = {}  # Keys are log names, values are None or Text controls.
    
        self.createInitialTabs()
        self.setFontFromConfig()
    #@+node:edream.110203113231.557:leoLog.createInitialTabs
    def createInitialTabs (self):
        
        c = self.c ;  nb = self.nb
    
        # Create the Log tab.
        self.logCtrl = self.selectTab('Log')
        
        # wx.TheColourDatabase.AddColour('leo blue',wx.Color(214,250,254))
        
        # Create the Find tab (Use gui.createFindTab so we won't create it twice.)
        win = self.createTab('Find',createText=False)
        win.SetBackgroundColour('light blue') # 'leo blue','wheat','orchid','sky blue'
        self.findTabHandler = g.app.gui.createFindTab(c,parentFrame=win)
        
        # Make sure the Log is selected.
        self.selectTab('Log')
    #@-node:edream.110203113231.557:leoLog.createInitialTabs
    #@+node:ekr.20061118122007:leoLog.setTabBindings
    def setTabBindings (self,tag=None):
        
        pass # g.trace('wxLeoLog')
        
    def bind (self,*args,**keys):
        
        # No need to do this: we can set the master binding by hand.
        pass # g.trace('wxLeoLog',args,keys)
    #@nonl
    #@-node:ekr.20061118122007:leoLog.setTabBindings
    #@-node:edream.110203113231.554:leoLog.__init__
    #@+node:ekr.20070104065742:Config
    #@+node:edream.110203113231.555:leoLog.configure
    def configure (self,*args,**keys):
        
        g.trace(args,keys)
    #@nonl
    #@-node:edream.110203113231.555:leoLog.configure
    #@+node:edream.110203113231.556:leoLog.configureBorder
    def configureBorder(self,border):
        
        g.trace(border)
    #@-node:edream.110203113231.556:leoLog.configureBorder
    #@+node:edream.110203113231.558:leoLog.setLogFontFromConfig
    def setFontFromConfig (self):
        
        pass # g.trace()
    #@nonl
    #@-node:edream.110203113231.558:leoLog.setLogFontFromConfig
    #@-node:ekr.20070104065742:Config
    #@+node:edream.110203113231.559:wxLog.put & putnl
    # All output to the log stream eventually comes here.
    
    def put (self,s,color=None,tabName=None):
        
        if tabName: self.selectTab(tabName)
    
        if self.logCtrl:
            self.logCtrl.AppendText(s)
    
    def putnl (self,tabName=None):
        
        if tabName: self.selectTab(tabName)
    
        if self.logCtrl:
            self.logCtrl.AppendText('\n')
            self.logCtrl.ScrollLines(1)
    #@nonl
    #@-node:edream.110203113231.559:wxLog.put & putnl
    #@+node:ekr.20061118123730:wx.Log.keyUp/Down
    useWX = False # True, use native key handling.  False, call masterKeyHandler.
    
    def onKeyDown (self,event,*args,**keys):
        keycode = event.GetKeyCode()
        self.keyDownModifiers = event.GetModifiers()
        if keycode == wx.WXK_ALT:
            event.Skip() # Do default processing.
        elif self.useWX:
            event.Skip()
        else:
            pass # This is required to suppress wx event handling.
        
    def onKeyUp (self,event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_ALT:
            event.Skip() # Do default processing.
        elif self.useWX:
            event.Skip()
        else:
            event.keyDownModifiers = self.keyDownModifiers
            event = g.app.gui.leoKeyEvent(event,c=self.c) # Convert event to canonical form.
            g.trace('wxLog',event.keysym)
            if event.keysym: # The key may have been a raw key.
                self.c.k.masterKeyHandler(event,stroke=event.keysym)
    #@-node:ekr.20061118123730:wx.Log.keyUp/Down
    #@+node:ekr.20061211122107:Tab (wxLog)
    #@+node:ekr.20061211122107.2:createTab
    def createTab (self,tabName,createText=True,wrap='none'): # wxLog.
    
        nb = self.nb
        # g.trace(tabName)
        
        if createText:
            win = logFrame = wx.Panel(nb)
            nb.AddPage(win,tabName)
        
            style = wx.TE_RICH | wx.TE_RICH2 | wx.TE_MULTILINE
            w = g.app.gui.leoTextWidgetClass(
                win,
                style=style,
                name='text tab:%s' % tabName
            )
            
            sizer = wx.BoxSizer(wx.HORIZONTAL)
            sizer.Add(w,1,wx.EXPAND)
            win.SetSizer(sizer)
            sizer.Fit(win)
    
            self.textDict [tabName] = w
            self.frameDict [tabName] = win
            
            w.defaultFont = font = wx.Font(pointSize=10,
                family = wx.FONTFAMILY_TELETYPE,
                style  = wx.FONTSTYLE_NORMAL,
                weight = wx.FONTWEIGHT_NORMAL,
            )
            w.defaultAttrib = wx.TextAttr(font=font)
            w.defaultStyle = w.SetDefaultStyle(w.defaultAttrib)
            w.allowSyntaxColoring = False
            wx.EVT_KEY_DOWN(w,self.onKeyDown) # Provides raw key codes.
            wx.EVT_KEY_UP(w,self.onKeyUp) # Provides raw key codes.
            
            # c.k doesn't exist when the log pane is created.
            # if tabName != 'Log':
                # # k.makeAllBindings will call setTabBindings('Log')
                # self.setTabBindings(tabName)
            return w
        else:
            win = wx.Panel(nb,name='tab:%s' % tabName)
            self.textDict [tabName] = None
            self.frameDict [tabName] = win
            nb.AddPage(win,tabName)
            return win
    #@-node:ekr.20061211122107.2:createTab
    #@+node:ekr.20061211122107.11:selectTab
    def selectTab (self,tabName,createText=True,wrap='none'):
    
        '''Create the tab if necessary and make it active.'''
    
        tabFrame = self.frameDict.get(tabName)
        
        if not tabFrame:
            self.createTab(tabName,createText=createText)
        
        # Update the status vars.
        self.tabName = tabName
        self.logCtrl = self.textDict.get(tabName)
        self.tabFrame = self.frameDict.get(tabName)
    
        nb = self.nb
        for i in xrange(nb.GetPageCount()):
            s = nb.GetPageText(i)
            if s == tabName:
                nb.SetSelection(i)
                assert nb.GetPage(i) == self.tabFrame
        
        return self.tabFrame
    #@-node:ekr.20061211122107.11:selectTab
    #@+node:ekr.20061211122107.1:clearTab
    def clearTab (self,tabName,wrap='none'):
        
        self.selectTab(tabName,wrap=wrap)
        w = self.logCtrl
        w and w.Clear()
    #@-node:ekr.20061211122107.1:clearTab
    #@+node:ekr.20061211122107.5:deleteTab
    def deleteTab (self,tabName):
        
        c = self.c ; nb = self.nb
    
        if tabName not in ('Log','Find','Spell'):
            for i in xrange(nb.GetPageCount()):
                s = nb.GetPageText(i)
                if s == tabName:
                    nb.DeletePage(i)
                    self.textDict [tabName] = None
                    self.frameDict [tabName] = False # A bit of a kludge.
                    self.tabName = None
                    break
                    
        self.selectTab('Log')
        c.invalidateFocus()
        c.bodyWantsFocus()
    #@-node:ekr.20061211122107.5:deleteTab
    #@+node:ekr.20061211122107.7:getSelectedTab
    def getSelectedTab (self):
        
        return self.tabName
    #@-node:ekr.20061211122107.7:getSelectedTab
    #@+node:ekr.20061211122107.6:hideTab
    def hideTab (self,tabName):
        
        __pychecker__ = '--no-argsused' # tabName
        
        self.selectTab('Log')
    #@-node:ekr.20061211122107.6:hideTab
    #@+node:ekr.20061211122107.9:numberOfVisibleTabs
    def numberOfVisibleTabs (self):
        
        return self.nb.GetPageCount()
    #@-node:ekr.20061211122107.9:numberOfVisibleTabs
    #@+node:ekr.20061211132355:Not used yet
    if 0:
        #@    @+others
        #@+node:ekr.20061211122107.4:cycleTabFocus
        def cycleTabFocus (self,event=None,stop_w = None):
        
            '''Cycle keyboard focus between the tabs in the log pane.'''
        
            c = self.c ; d = self.frameDict # Keys are page names. Values are Tk.Frames.
            w = d.get(self.tabName)
            # g.trace(self.tabName,w)
            values = d.values()
            if self.numberOfVisibleTabs() > 1:
                i = i2 = values.index(w) + 1
                if i == len(values): i = 0
                tabName = d.keys()[i]
                self.selectTab(tabName)
                return 
        #@nonl
        #@-node:ekr.20061211122107.4:cycleTabFocus
        #@+node:ekr.20061211122107.8:lower/raiseTab
        def lowerTab (self,tabName):
            
            if tabName:
                b = self.nb.tab(tabName) # b is a Tk.Button.
                b.config(bg='grey80')
            self.c.invalidateFocus()
            self.c.bodyWantsFocus()
        
        def raiseTab (self,tabName):
        
            if tabName:
                b = self.nb.tab(tabName) # b is a Tk.Button.
                b.config(bg='LightSteelBlue1')
            self.c.invalidateFocus()
            self.c.bodyWantsFocus()
        #@-node:ekr.20061211122107.8:lower/raiseTab
        #@+node:ekr.20061211122107.10:renameTab
        def renameTab (self,oldName,newName):
            
            label = self.nb.tab(oldName)
            label.configure(text=newName)
        #@-node:ekr.20061211122107.10:renameTab
        #@+node:ekr.20061211122107.12:setTabBindings
        def setTabBindings (self,tabName):
            
            c = self.c ; k = c.k
            tab = self.nb.tab(tabName)
            w = self.textDict.get(tabName)
            
            # Send all event in the text area to the master handlers.
            for kind,handler in (
                ('<Key>',       k.masterKeyHandler),
                ('<Button-1>',  k.masterClickHandler),
                ('<Button-3>',  k.masterClick3Handler),
            ):
                w.bind(kind,handler)
            
            # Clicks in the tab area are harmless: use the old code.
            def tabMenuRightClickCallback(event,menu=self.menu):
                return self.onRightClick(event,menu)
                
            def tabMenuClickCallback(event,tabName=tabName):
                return self.onClick(event,tabName)
            
            tab.bind('<Button-1>',tabMenuClickCallback)
            tab.bind('<Button-3>',tabMenuRightClickCallback)
            
            k.completeAllBindingsForWidget(w)
        #@-node:ekr.20061211122107.12:setTabBindings
        #@+node:ekr.20061211122107.13:Tab menu callbacks & helpers (not ready yet)
        if 0:
            #@    @+others
            #@+node:ekr.20061211122107.14:onRightClick & onClick
            def onRightClick (self,event,menu):
                
                c = self.c
                menu.post(event.x_root,event.y_root)
                
                
            def onClick (self,event,tabName):
            
                self.selectTab(tabName)
            #@-node:ekr.20061211122107.14:onRightClick & onClick
            #@+node:ekr.20061211122107.15:newTabFromMenu
            def newTabFromMenu (self,tabName='Log'):
            
                self.selectTab(tabName)
                
                # This is called by getTabName.
                def selectTabCallback (newName):
                    return self.selectTab(newName)
            
                self.getTabName(selectTabCallback)
            #@-node:ekr.20061211122107.15:newTabFromMenu
            #@+node:ekr.20061211122107.16:renameTabFromMenu
            def renameTabFromMenu (self,tabName):
            
                if tabName in ('Log','Completions'):
                    g.es('can not rename %s tab' % (tabName),color='blue')
                else:
                    def renameTabCallback (newName):
                        return self.renameTab(tabName,newName)
            
                    self.getTabName(renameTabCallback)
            #@-node:ekr.20061211122107.16:renameTabFromMenu
            #@+node:ekr.20061211122107.17:getTabName
            def getTabName (self,exitCallback):
                
                canvas = self.nb.component('hull')
            
                # Overlay what is there!
                f = Tk.Frame(canvas)
                f.pack(side='top',fill='both',expand=1)
                
                row1 = Tk.Frame(f)
                row1.pack(side='top',expand=0,fill='x',pady=10)
                row2 = Tk.Frame(f)
                row2.pack(side='top',expand=0,fill='x')
            
                Tk.Label(row1,text='Tab name').pack(side='left')
            
                e = Tk.Entry(row1,background='white')
                e.pack(side='left')
            
                def getNameCallback (event=None):
                    s = e.get().strip()
                    f.pack_forget()
                    if s: exitCallback(s)
                    
                def closeTabNameCallback (event=None):
                    f.pack_forget()
                    
                b = Tk.Button(row2,text='Ok',width=6,command=getNameCallback)
                b.pack(side='left',padx=10)
                
                b = Tk.Button(row2,text='Cancel',width=6,command=closeTabNameCallback)
                b.pack(side='left')
            
                e.focus_force()
                e.bind('<Return>',getNameCallback)
            #@-node:ekr.20061211122107.17:getTabName
            #@-others
        #@nonl
        #@-node:ekr.20061211122107.13:Tab menu callbacks & helpers (not ready yet)
        #@-others
    #@nonl
    #@-node:ekr.20061211132355:Not used yet
    #@-node:ekr.20061211122107:Tab (wxLog)
    #@-others
#@nonl
#@-node:edream.110203113231.553:wxLeoLog class
#@+node:edream.111303095242:wxLeoMenu class
class wxLeoMenu (leoMenu.leoMenu):
    
    """A class that represents a wxPython Leo window."""
    
    #@    @+others
    #@+node:edream.111303095242.3:  wxLeoMenu.__init__
    def __init__ (self,frame):
        
        # Init the base class.
        leoMenu.leoMenu.__init__(self,frame)
        
        # Init the ivars.
        self.c = frame.c
        self.frame = frame
        
        self.acceleratorDict = {}
            # Keys are menus, values are list of tuples used to create wx accelerator tables.
        self.menuDict = {}
    #@nonl
    #@-node:edream.111303095242.3:  wxLeoMenu.__init__
    #@+node:ekr.20061118203148:createAccelLabel
    def createAccelLabel (self,keys):
        
        '''Create the menu label by inserting '&' at the underline spot.'''
        
        label    = keys.get('label')
        underline = keys.get('underline')
        accel = keys.get('accelerator')
        ch = 0 <= underline < len(label) and label[underline] or ''
        if ch: label = label[:underline] + '&' + label[underline:]
        if accel: label = label + '\t' + accel 
        return ch,label
    #@-node:ekr.20061118203148:createAccelLabel
    #@+node:ekr.20061118203148.1:createAccelData
    def createAccelData (self,menu,ch,accel,id,label):
    
        d = self.acceleratorDict
        aList = d.get(menu,[])
        data = ch,accel,id,label
        aList.append(data)
        d [menu] = aList
    #@-node:ekr.20061118203148.1:createAccelData
    #@+node:ekr.20061118194416:createAcceleratorTables
    def createAcceleratorTables (self):
        
        d = self.acceleratorDict
        entries = []
        for menu in d.keys():
            aList = d.get(menu)
            for data in aList:
                ch,accel,id,label = data
                if ch:
                    entry = wx.AcceleratorEntry(wx.ACCEL_NORMAL,ord(ch),id)
                    entries.append(entry)
        table = wx.AcceleratorTable(entries)
        self.menuBar.SetAcceleratorTable(table)
    #@-node:ekr.20061118194416:createAcceleratorTables
    #@+node:edream.111303103457:wx menu bindings
    #@+node:ekr.20061106062514:Not called
    #@+node:edream.111303103141.1:bind (Not called)
    def bind (self,bind_shortcut,callback):
        
        g.trace(bind_shortcut,callback)
        
        pass
    #@nonl
    #@-node:edream.111303103141.1:bind (Not called)
    #@+node:edream.111303103141.2:delete (not called?)
    def delete (self,menu,readItemName):
        
        g.trace(menu,readItemName)
        
        ## return menu.delete(realItemName)
    #@-node:edream.111303103141.2:delete (not called?)
    #@+node:edream.111303103141.4:destroy (not called ?)
    def destroy (self,menu):
        
        g.trace()
    
        ## menu.destroy()
    #@nonl
    #@-node:edream.111303103141.4:destroy (not called ?)
    #@+node:ekr.20070124111252:insert (not called)
    def insert (self,*args,**keys):
    
        g.trace('wxMenu: to do',args,keys)
    #@nonl
    #@-node:ekr.20070124111252:insert (not called)
    #@-node:ekr.20061106062514:Not called
    #@+node:edream.111603104327:Menu methods (Tk names)
    #@+node:edream.111303111942.1:add_cascade
    def add_cascade (self,parent,label,menu,underline):
    
        """Create a menu with the given parent menu."""
    
        if parent:
            # Create a submenu of the parent menu.
            keys = {'label':label,'underline':underline}
            ch,label = self.createAccelLabel(keys)
            id = const(label)
            parent.AppendMenu(id,label,menu,label)
            accel = None
            if ch: self.createAccelData(menu,ch,accel,id,label)
        else:
            # Create a top-level menu.
            self.menuBar.Append(menu,label)
            
    #@-node:edream.111303111942.1:add_cascade
    #@+node:edream.111303103141:menu.add_command
    def add_command (self,menu,**keys):
        
        if not menu:
            return g.trace('Can not happen.  No menu')
        
        callback = keys.get('command')
        accel = keys.get('accelerator')
        ch,label = self.createAccelLabel(keys)
        
        def wxMenuCallback (event,callback=callback):
            return callback() # All args were bound when the callback was created.
    
        id = const(label)
        menu.Append(id,label,label)
        key = (menu,label),
        self.menuDict[key] = id # Remember id 
        wx.EVT_MENU(self.frame.top,id,wxMenuCallback)
        if ch or accel:
            self.createAccelData(menu,ch,accel,id,label)
        
    #@nonl
    #@-node:edream.111303103141:menu.add_command
    #@+node:edream.111303121150:add_separator
    def add_separator(self,menu):
        
        if menu:
            menu.AppendSeparator()
        else:
            g.trace("null menu")
    #@nonl
    #@-node:edream.111303121150:add_separator
    #@+node:edream.111303103141.3:delete_range (wxMenu) (does not work)
    # The wxWindows menu code has problems:  changes do not take effect immediately.
    
    def delete_range (self,menu,n1,n2):
        
        if not menu:
            g.trace("no menu")
            return
            
        # g.trace(n1,n2,menu.GetTitle())
        
        items = menu.GetMenuItems()
        
        if 0: # debugging
            for item in items:
                id = item.GetId()
                item = menu.FindItemById(id)
                g.trace(item.GetText())
                
        ## Doesn't work:  a problem with wxPython.
        
        if len(items) > n1 and len(items) > n2:
            i = n1
            while i <= n2:
                id = items[i].GetId()
                item = menu.FindItemById(id)
                g.trace("deleting:",item.GetText())
                menu.Delete(id)
                i += 1
    #@nonl
    #@-node:edream.111303103141.3:delete_range (wxMenu) (does not work)
    #@+node:edream.111303111942:insert_cascade
    def insert_cascade (self,parent,index,label,menu,underline):
    
        if not parent:
            keys = {'label':label,'underline':underline}
            ch,label = self.createAccelLabel(keys)
            self.menuBar.append(menu,label)
            id = const(label)
            accel = None
            if ch: self.createAccelData(menu,ch,accel,id,label)
    #@-node:edream.111303111942:insert_cascade
    #@+node:edream.111303110018:new_menu
    def new_menu(self,parent,tearoff=0):
        
        return wx.Menu()
    #@nonl
    #@-node:edream.111303110018:new_menu
    #@-node:edream.111603104327:Menu methods (Tk names)
    #@+node:edream.111603112846:Menu methods (non-Tk names)
    #@+node:edream.111303103457.2:createMenuBar
    def createMenuBar(self,frame):
        
        self.menuBar = menuBar = wx.MenuBar()
    
        self.createMenusFromTables()
        
        self.createAcceleratorTables()
    
        frame.top.SetMenuBar(menuBar)
    #@nonl
    #@-node:edream.111303103457.2:createMenuBar
    #@+node:edream.111603112846.1:createOpenWithMenuFromTable (not ready yet)
    #@+at 
    #@nonl
    # Entries in the table passed to createOpenWithMenuFromTable are
    # tuples of the form (commandName,shortcut,data).
    # 
    # - command is one of "os.system", "os.startfile", "os.spawnl", 
    # "os.spawnv" or "exec".
    # - shortcut is a string describing a shortcut, just as for 
    # createMenuItemsFromTable.
    # - data is a tuple of the form (command,arg,ext).
    # 
    # Leo executes command(arg+path) where path is the full path to the temp 
    # file.
    # If ext is not None, the temp file has the given extension.
    # Otherwise, Leo computes an extension based on the @language directive in 
    # effect.
    #@-at
    #@@c
    
    def createOpenWithMenuFromTable (self,table):
        
        g.trace("Not ready yet")
        
        return ### Not ready yet
    
        g.app.openWithTable = table # Override any previous table.
        # Delete the previous entry.
        parent = self.getMenu("File")
        label = self.getRealMenuName("Open &With...")
        amp_index = label.find("&")
        label = label.replace("&","")
        try:
            index = parent.index(label)
            parent.delete(index)
        except:
            try:
                index = parent.index("Open With...")
                parent.delete(index)
            except: return
        # Create the "Open With..." menu.
        openWithMenu = Tk.Menu(parent,tearoff=0)
        self.setMenu("Open With...",openWithMenu)
        parent.insert_cascade(index,label=label,menu=openWithMenu,underline=amp_index)
        # Populate the "Open With..." menu.
        shortcut_table = []
        for triple in table:
            if len(triple) == 3: # 6/22/03
                shortcut_table.append(triple)
            else:
                g.es("createOpenWithMenuFromTable: invalid data",color="red")
                return
                
        # for i in shortcut_table: print i
        self.createMenuItemsFromTable("Open &With...",shortcut_table,openWith=1)
    #@-node:edream.111603112846.1:createOpenWithMenuFromTable (not ready yet)
    #@+node:edream.111303103254:defineMenuCallback
    def defineMenuCallback(self,command,name):
            
        # The first parameter must be event, and it must default to None.
        def callback(event=None,self=self,command=command,label=name):
            self.c.doCommand(command,label,event)
    
        return callback
    #@nonl
    #@-node:edream.111303103254:defineMenuCallback
    #@+node:edream.111303095242.6:defineOpenWithMenuCallback
    def defineOpenWithMenuCallback (self,command):
            
        # The first parameter must be event, and it must default to None.
        def wxOpenWithMenuCallback(event=None,command=command):
            try: self.c.openWith(data=command)
            except: print traceback.print_exc()
    
        return wxOpenWithMenuCallback
    #@nonl
    #@-node:edream.111303095242.6:defineOpenWithMenuCallback
    #@+node:edream.111303163727.2:disableMenu
    def disableMenu (self,menu,name):
        
        if not menu:
            g.trace("no menu",name)
            return
        
        realName = self.getRealMenuName(name)
        realName = realName.replace("&","")
        id = menu.FindItem(realName)
        if id:
            item = menu.FindItemById(id)
            item.Enable(0)
        else:
            g.trace("no item",name,val)
    #@nonl
    #@-node:edream.111303163727.2:disableMenu
    #@+node:edream.111303163727.1:enableMenu
    def enableMenu (self,menu,name,val):
        
        if not menu:
            g.trace("no menu",name,val)
            return
        
        realName = self.getRealMenuName(name)
        realName = realName.replace("&","")
        id = menu.FindItem(realName)
        if id:
            item = menu.FindItemById(id)
            val = g.choose(val,1,0)
            item.Enable(val)
        else:
            g.trace("no item",name,val)
    #@nonl
    #@-node:edream.111303163727.1:enableMenu
    #@+node:edream.111303163727.3:setMenuLabel
    def setMenuLabel (self,menu,name,label,underline=-1):
    
        if not menu:
            g.trace("no menu",name)
            return
            
        if type(name) == type(0):
            # "name" is actually an index into the menu.
            items = menu.GetMenuItems() # GetItemByPosition does not exist.
            if items and len(items) > name :
                id = items[name].GetId()
            else: id = None
        else:
            realName = self.getRealMenuName(name)
            realName = realName.replace("&","")
            id = menu.FindItem(realName)
    
        if id:
            item = menu.FindItemById(id)
            label = self.getRealMenuName(label)
            label = label.replace("&","")
            # g.trace(name,label)
            item.SetText(label)
        else:
            g.trace("no item",name,label)
    #@nonl
    #@-node:edream.111303163727.3:setMenuLabel
    #@-node:edream.111603112846:Menu methods (non-Tk names)
    #@-node:edream.111303103457:wx menu bindings
    #@-others
#@nonl
#@-node:edream.111303095242:wxLeoMenu class
#@+node:ekr.20061211091215:wxLeoMinibuffer class
class wxLeoMinibuffer:
    
    #@    @+others
    #@+node:ekr.20061211091548:minibuffer.__init__
    def __init__ (self,c,parentFrame):
        
        self.c = c
        self.parentFrame = parentFrame
        self.ctrl = self.createControl(parentFrame)
    #@-node:ekr.20061211091548:minibuffer.__init__
    #@+node:ekr.20061211091216:minibuffer.createControl
    def createControl (self,parentFrame):
    
        self.ctrl = w = g.app.gui.leoTextWidgetClass(
            parentFrame,
            pos = wx.DefaultPosition,
            size = (1000,-1),
            name = 'minibuffer'
        )
            
        w.defaultFont = font = wx.Font(pointSize=10,
            family = wx.FONTFAMILY_TELETYPE, # wx.FONTFAMILY_ROMAN,
            style  = wx.FONTSTYLE_NORMAL,
            weight = wx.FONTWEIGHT_NORMAL,
        )
    
        w.defaultAttrib = wx.TextAttr(font=font)
        w.allowSyntaxColoring = False
            
        # wx.EVT_KEY_DOWN (w,self.onKeyDown) # Provides raw key codes.
        # wx.EVT_KEY_UP   (w,self.onKeyUp) # Provides raw key codes.
            
        return w
    #@nonl
    #@-node:ekr.20061211091216:minibuffer.createControl
    #@+node:ekr.20061211091548.1:minibuffer.onKeyUp/Down (not used)
    # def onKeyDown (self,event,*args,**keys):
    
        # keycode = event.GetKeyCode()
        # self.keyDownModifiers = event.GetModifiers()
        # event.Skip() # Always do default processing.
        
    # def onKeyUp (self,event):
        
        # keycode = event.GetKeyCode()
        # if keycode == wx.WXK_ALT:
            # event.Skip() # Do default processing.
        # else:
            # event.keyDownModifiers = self.keyDownModifiers
            # event = g.app.gui.leoKeyEvent(event,c=self.c) # Convert event to canonical form.
            # g.trace('wxMinibuffer',event.keysym)
            # if event.keysym: # The key may have been a raw key.
                # self.c.k.masterKeyHandler(event,stroke=event.keysym)
            # event.actualEvent.Skip() # Do default processing.
    #@-node:ekr.20061211091548.1:minibuffer.onKeyUp/Down (not used)
    #@-others
#@nonl
#@-node:ekr.20061211091215:wxLeoMinibuffer class
#@+node:ekr.20070112173627:class wxStatusLineClass
class wxStatusLineClass:
    
    '''A class representing the status line.'''
    
    #@    @+others
    #@+node:ekr.20070112173627.1: ctor
    def __init__ (self,c,top):
        
        self.c = c
        self.top = self.statusFrame = top
        
        self.enabled = False
        self.isVisible = True
        self.lastRow = self.lastCol = 0
        
        # Create the actual status line.
        self.w = top.CreateStatusBar(1,wx.ST_SIZEGRIP) # A wxFrame method.
    #@-node:ekr.20070112173627.1: ctor
    #@+node:ekr.20070112173627.2:clear
    def clear (self):
        
        self.w.SetStatusText('')
    #@-node:ekr.20070112173627.2:clear
    #@+node:ekr.20070112173627.3:enable, disable & isEnabled
    def disable (self,background=None):
        
        # c = self.c ; w = self.textWidget
        # if w:
            # if not background:
                # background = self.statusFrame.cget("background")
            # w.configure(state="disabled",background=background)
        self.enabled = False
        c.bodyWantsFocus()
        
    def enable (self,background="white"):
        
        # c = self.c ; w = self.textWidget
        # if w:
            # w.configure(state="normal",background=background)
            # c.widgetWantsFocus(w)
        self.enabled = True
            
    def isEnabled(self):
        return self.enabled
    #@nonl
    #@-node:ekr.20070112173627.3:enable, disable & isEnabled
    #@+node:ekr.20070112173627.4:get
    def get (self):
        
        return self.w.GetStatusText()
    #@-node:ekr.20070112173627.4:get
    #@+node:ekr.20070112173627.5:getFrame
    def getFrame (self):
        
        return self.statusFrame
    #@-node:ekr.20070112173627.5:getFrame
    #@+node:ekr.20070112173627.6:onActivate
    def onActivate (self,event=None):
        
        pass
    #@-node:ekr.20070112173627.6:onActivate
    #@+node:ekr.20070112173627.7:pack & show
    def pack (self):
        pass
            
    show = pack
    #@-node:ekr.20070112173627.7:pack & show
    #@+node:ekr.20070112173627.8:put (leoTkinterFrame:statusLineClass)
    def put(self,s,color=None):
        
        w = self.w
        w.SetStatusText(w.GetStatusText() + s)
    #@-node:ekr.20070112173627.8:put (leoTkinterFrame:statusLineClass)
    #@+node:ekr.20070112173627.9:unpack & hide
    def unpack (self):
        pass
    
    hide = unpack
    #@-node:ekr.20070112173627.9:unpack & hide
    #@+node:ekr.20070112173627.10:update (statusLine)
    def update (self):
        
        c = self.c ; bodyCtrl = c.frame.body.bodyCtrl
    
        if g.app.killed or not self.isVisible:
            return
    
        s = bodyCtrl.getAllText()    
        index = bodyCtrl.getInsertPoint()
        row,col = g.convertPythonIndexToRowCol(s,index)
        if col > 0:
            s2 = s[index-col:index]
            s2 = g.toUnicode(s2,g.app.tkEncoding)
            col = g.computeWidth (s2,c.tab_width)
    
        # Important: this does not change the focus because labels never get focus.
        
        self.w.SetStatusText(text="line %d, col %d" % (row,col))
        self.lastRow = row
        self.lastCol = col
    #@-node:ekr.20070112173627.10:update (statusLine)
    #@-others
#@-node:ekr.20070112173627:class wxStatusLineClass
#@+node:edream.111603213219:wxLeoTree class
class wxLeoTree (leoFrame.leoTree):

    #@    @+others
    #@+node:edream.111603213219.1:wxTree.__init__
    def __init__ (self,frame,parentFrame):
    
        # Init the base class.
        leoFrame.leoTree.__init__(self,frame)
        
        c = self.c
        self.canvas = self # A dummy ivar used in c.treeWantsFocus, etc.
        self.editWidgetDict = {} # Keys are tnodes, values are leoHeadlineTextWidgets.
        self.imageList = None
        self.keyDownModifiers = None
        self.stayInTree = c.config.getBool('stayInTreeAfterSelect')
        self.root_id = None
        self.updateCount = 0
    
        self.treeCtrl = self.createControl(parentFrame)
        self.createBindings()
    #@+node:edream.111603213329:wxTree.createBindings
    def createBindings (self): # wxLeoTree
    
        w = self.treeCtrl ; id = const("cTree")
    
        wx.EVT_KEY_DOWN         (w,self.onKeyDown)  # Provides raw key codes.
        wx.EVT_KEY_UP           (w,self.onKeyUp)    # Provides raw key codes.
        # wx.EVT_TREE_KEY_DOWN  (w,id,self.onTreeKeyDown) # Control keys do not fire this event.
    
        wx.EVT_TREE_SEL_CHANGING    (w,id,self.onTreeSelChanging)
    
        wx.EVT_TREE_BEGIN_DRAG      (w,id,self.onTreeBeginDrag)
        wx.EVT_TREE_END_DRAG        (w,id,self.onTreeEndDrag)
     
        wx.EVT_TREE_BEGIN_LABEL_EDIT(w,id,self.onTreeBeginLabelEdit)
        wx.EVT_TREE_END_LABEL_EDIT  (w,id,self.onTreeEndLabelEdit)
         
        wx.EVT_TREE_ITEM_COLLAPSED  (w,id,self.onTreeCollapsed)
        wx.EVT_TREE_ITEM_EXPANDED   (w,id,self.onTreeExpanded)
        
        wx.EVT_TREE_ITEM_COLLAPSING (w,id,self.onTreeCollapsing)
        wx.EVT_TREE_ITEM_EXPANDING  (w,id,self.onTreeExpanding)
        
        wx.EVT_RIGHT_DOWN           (w,self.onRightDown)
        wx.EVT_RIGHT_UP             (w,self.onRightUp)
    #@-node:edream.111603213329:wxTree.createBindings
    #@+node:ekr.20061118142055:wxTree.createControl
    def createControl (self,parentFrame):
        
        style = (
            wx.TR_SINGLE | # Only a single row may be selected.
            wx.TR_HAS_BUTTONS | # Draw +- buttons.
            wx.TR_EDIT_LABELS |
            wx.TR_HIDE_ROOT |
            wx.TR_LINES_AT_ROOT |
            wx.TR_HAS_VARIABLE_ROW_HEIGHT )
        
        w = wx.TreeCtrl(parentFrame,
            id = const("cTree"),
            pos = wx.DefaultPosition,
            size = wx.DefaultSize,
            style = style,
            validator = wx.DefaultValidator,
            name = "tree")
    
        self.defaultFont = font = wx.Font(pointSize=12,
            family = wx.FONTFAMILY_TELETYPE, # wx.FONTFAMILY_ROMAN,
            style  = wx.FONTSTYLE_NORMAL,
            weight = wx.FONTWEIGHT_NORMAL,
        )
        
        self.imageList = self.createImageList()
        w.AssignImageList(self.imageList)
    
        return w
    #@-node:ekr.20061118142055:wxTree.createControl
    #@+node:ekr.20061211050723:wxTree.createImageList
    def createImageList (self): # wxTree.
    
        self.imageList = imageList = wx.ImageList(21,11)
        theDir = g.os_path_abspath(g.os_path_join(g.app.loadDir,'..','Icons'))
        
        for i in xrange(16):
            
            # Get the original bitmap.
            fileName = g.os_path_join(theDir,'box%02d.bmp' % i)
            bitmap = wx.Bitmap(fileName,type=wx.BITMAP_TYPE_BMP)
            
            # Create a larger bitmap.
            image = wx.ImageFromBitmap(bitmap)
            # image.SetMask(False)
            image.Resize(size=(21,11),pos=(0,0),)
            bitmap = wx.BitmapFromImage(image)
            
            # And add the new bitmap to the list.
            imageList.Add(bitmap)
    
        return imageList
    #@-node:ekr.20061211050723:wxTree.createImageList
    #@+node:ekr.20061118122218.1:setBindings (does nothing)
    def setBindings(self):
        
        pass # g.trace('wxLeoTree: to do')
    
    def bind(self,*args,**keys):
        
        pass # g.trace('wxLeoTree',args,keys)
    #@nonl
    #@-node:ekr.20061118122218.1:setBindings (does nothing)
    #@-node:edream.111603213219.1:wxTree.__init__
    #@+node:edream.111303202917:Drawing
    #@+node:ekr.20061105114250:drawIcon TO DO
    #@-node:ekr.20061105114250:drawIcon TO DO
    #@+node:edream.110203113231.295:beginUpdate
    def beginUpdate (self):
    
        self.updateCount += 1
    #@nonl
    #@-node:edream.110203113231.295:beginUpdate
    #@+node:edream.110203113231.296:endUpdate
    def endUpdate (self,flag=True,scroll=False):
    
        assert(self.updateCount > 0)
    
        self.updateCount -= 1
        if flag and self.updateCount == 0:
            self.redraw()
    #@nonl
    #@-node:edream.110203113231.296:endUpdate
    #@+node:edream.110203113231.298:redraw & redraw_now & helpers
    def redraw (self):
        
        c = self.c ; tree = self.treeCtrl
        if c is None: return
        p = c.rootPosition()
        if not p: return
    
        self.drawing = True # Tell event handlers not to call us.
        try:
            tree.DeleteAllItems()
            self.root_id = root_id = tree.AddRoot('Root Node')
            ### tree.SetItemFont(root_id,self.defaultFont)
            while p:
                self.redraw_subtree(root_id,p)
                p.moveToNext()
            if 0: # Don't do this when wx.TR_HIDE_ROOT is true.
                tree.Expand(root_id)
        finally:
            self.drawing = False
            
    def redraw_now(self,scroll=True):
        self.redraw()
    #@nonl
    #@+node:edream.110203113231.299:redraw_node
    def redraw_node(self,parent_id,p):
        
        tree = self.treeCtrl
        data = wx.TreeItemData(p.copy())
        image = self.assignIcon(p)
    
        id = tree.AppendItem(
            parent_id,
            text=p.headString(),
            image=image,
            #selImage=image,
            data=data)
    
        ### tree.SetItemFont(id,self.defaultFont)
        
        if p == self.c.currentPosition():
            tree.SelectItem(id) # Generates call to onTreeChanged.
        
        p.tree_id = id
        self.setEditWidget(p)
        assert (p == tree.GetItemData(id).GetData())
        return id
    #@-node:edream.110203113231.299:redraw_node
    #@+node:edream.110203113231.300:redraw_subtree
    def redraw_subtree(self,parent_id,p):
    
        tree = self.treeCtrl
        id = self.redraw_node(parent_id,p)
        child = p.firstChild()
    
        while child:
            # We must redraw the entire tree, regardless of expansion state.
            self.redraw_subtree(id,child)
            child.moveToNext()
        
        # The calls to tree.Expand and tree.Collapse *will* generate events,
        # This is the reason the event handlers must be disabled while drawing.
        if p.isExpanded():
            tree.Expand(id)
        else:
            tree.Collapse(id)
    #@nonl
    #@-node:edream.110203113231.300:redraw_subtree
    #@-node:edream.110203113231.298:redraw & redraw_now & helpers
    #@+node:edream.110203113231.299:redraw_node
    def redraw_node(self,parent_id,p):
        
        tree = self.treeCtrl
        data = wx.TreeItemData(p.copy())
        image = self.assignIcon(p)
    
        id = tree.AppendItem(
            parent_id,
            text=p.headString(),
            image=image,
            #selImage=image,
            data=data)
    
        ### tree.SetItemFont(id,self.defaultFont)
        
        if p == self.c.currentPosition():
            tree.SelectItem(id) # Generates call to onTreeChanged.
        
        p.tree_id = id
        self.setEditWidget(p)
        assert (p == tree.GetItemData(id).GetData())
        return id
    #@-node:edream.110203113231.299:redraw_node
    #@+node:edream.110203113231.300:redraw_subtree
    def redraw_subtree(self,parent_id,p):
    
        tree = self.treeCtrl
        id = self.redraw_node(parent_id,p)
        child = p.firstChild()
    
        while child:
            # We must redraw the entire tree, regardless of expansion state.
            self.redraw_subtree(id,child)
            child.moveToNext()
        
        # The calls to tree.Expand and tree.Collapse *will* generate events,
        # This is the reason the event handlers must be disabled while drawing.
        if p.isExpanded():
            tree.Expand(id)
        else:
            tree.Collapse(id)
    #@nonl
    #@-node:edream.110203113231.300:redraw_subtree
    #@+node:ekr.20061211052926:assignIcon
    def assignIcon (self,p):
        
        val = p.v.computeIcon()
        assert(0 <= val <= 15)
        return val
    #@-node:ekr.20061211052926:assignIcon
    #@+node:ekr.20061211072604:edit_widget
    def edit_widget (self,p):
        
        '''Return a widget (compatible with leoTextWidget) used for editing the headline.'''
        
        w = self.editWidgetDict.get(p.v)
        
        return w
    #@-node:ekr.20061211072604:edit_widget
    #@+node:ekr.20061211115055:updateVisibleIcons
    def updateVisibleIcons (self,p):
    
        '''Update all visible icons joined to p.'''
    
        tree = self.treeCtrl
        val = p.v.computeIcon()
        id = tree.GetFirstVisibleItem()
        while id.IsOk():
            p2 = tree.GetItemData(id).GetData()
            if p2.v.t == p.v.t:
                tree.SetItemImage(id,val)
            id = tree.GetNextVisible(id)
    #@-node:ekr.20061211115055:updateVisibleIcons
    #@-node:edream.111303202917:Drawing
    #@+node:edream.110203113231.278:Event handlers (wxTree)
    #@+node:ekr.20061127075102:get_p
    def get_p (self,event):
        
        tree = self.treeCtrl
        id = event.GetItem()
        p = id.IsOk() and tree.GetItemData(id).GetData()
        
        if 0:
            g.trace(
                'lockout',self.frame.lockout,
                'drawing',self.drawing,
                'id.IsOk',id.IsOk(),
                'p',p and p.headString(),
                g.callers(9))
            
        if self.frame.lockout or self.drawing or not p:
            return None
        else:
            # g.trace(p.headString(),g.callers())
            return p
    
    #@-node:ekr.20061127075102:get_p
    #@+node:ekr.20061127081233:selectHelper
    def selectHelper (self,event):
        
        '''Scroll so the presently selected node is in view.'''
        
        p = self.get_p(event)
        if not p: return
    
        # We can make this assertion because get_p has done the check.
        id = event.GetItem()
        assert (id.IsOk() and not self.frame.lockout)
    
        # g.trace(p.headString(),g.callers())
        tree = self.treeCtrl
        self.frame.lockout = True
        tree.SelectItem(id)
        tree.ScrollTo(id)
        self.frame.lockout = False
    #@-node:ekr.20061127081233:selectHelper
    #@+node:ekr.20061118144918:Keys
    #@+node:ekr.20061118123730.1:wxTree.onKeyUp/Down
    useWX = False # True, use native key handling.  False, call masterKeyHandler.
    
    def onKeyDown (self,event,*args,**keys):
        keycode = event.GetKeyCode()
        self.keyDownModifiers = event.GetModifiers()
        event.Skip() # Prepare to handle the event later.
    
    def onKeyUp (self,event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_ALT:
            event.Skip() # Do default processing.
        elif self.useWX:
            event.Skip()
        else:
            event.keyDownModifiers = self.keyDownModifiers
            event = g.app.gui.leoKeyEvent(event,c=self.c) # Convert event to canonical form.
            # g.trace('wxTree',event.keysym,self.keyDownModifiers)
            if event.keysym: # The key may have been a raw key.
                if event.keysym.isalnum() and len(event.keysym) == 1:
                    event.actualEvent.Skip(True) # Let the widget handle it.
                else:
                    # g.trace(event.keysym)
                    self.c.k.masterKeyHandler(event,stroke=event.keysym)
                    event.actualEvent.Skip(False) # Does not work.
    #@-node:ekr.20061118123730.1:wxTree.onKeyUp/Down
    #@-node:ekr.20061118144918:Keys
    #@+node:edream.110203113231.282:Clicks
    #@+node:edream.110203113231.280:Collapse...
    def onTreeCollapsing(self,event):
        
        '''Handle a pre-collapse event due to a click in the +- box.'''
    
        p = self.get_p(event)
        if not p: return
        
        # p will be None while redrawing, so this is the outermost click event.
        # Set the selection before redrawing so the tree is drawn properly.
        c = self.c ; tree = self.treeCtrl
        c.beginUpdate()
        try:
            c.selectPosition(p)
            p.contract()
        finally:
            c.endUpdate(False)
    
    def onTreeCollapsed(self,event):
        
        '''Handle a post-collapse event due to a click in the +- box.'''
    
        self.selectHelper(event)
    #@-node:edream.110203113231.280:Collapse...
    #@+node:edream.110203113231.281:Expand...
    def onTreeExpanding (self,event):
        
        '''Handle a pre-expand event due to a click in the +- box.'''
    
        p = self.get_p(event)
        if not p: return
        
        # p will be None while redrawing, so this is the outermost click event.
        # Set the selection before redrawing so the tree is drawn properly.
        c = self.c ; tree = self.treeCtrl
        c.beginUpdate()
        try:
            c.selectPosition(p)
            p.expand()
        finally:
            c.endUpdate(False)
            
    def onTreeExpanded (self,event):
        
        '''Handle a post-collapse event due to a click in the +- box.'''
        
        self.selectHelper(event)
    #@-node:edream.110203113231.281:Expand...
    #@+node:edream.110203113231.283:Clicks
    def onTreeSelChanging(self,event):
        
        p = self.get_p(event)
        if not p: return
        
        # p will be None while redrawing, so this is the outermost click event.
        # Set the selection before redrawing so the tree is drawn properly.
        c = self.c
        c.beginUpdate()
        try:
            c.selectPosition(p)
        finally:
            c.endUpdate(False)
    #@-node:edream.110203113231.283:Clicks
    #@+node:ekr.20061211064516:onRightDown/Up
    def onRightDown (self,event):
        
        tree = self.treeCtrl
        pt = event.GetPosition()
        item, flags = tree.HitTest(pt)
        if item:
            tree.SelectItem(item)
    
    def onRightUp (self,event):
        
        tree = self.treeCtrl
        pt = event.GetPosition()
        item, flags = tree.HitTest(pt)
        if item:
            tree.EditLabel(item)
    #@-node:ekr.20061211064516:onRightDown/Up
    #@-node:edream.110203113231.282:Clicks
    #@+node:edream.110203113231.285:Editing labels
    #@+node:edream.110203113231.286:onTreeBeginLabelEdit
    # Editing is allowed only if this routine exists.
    
    def onTreeBeginLabelEdit(self,event):
    
        # Disallow editing of the dummy root node.
        id = event.GetItem()
        if id == self.root_id:
            event.Veto()
    #@nonl
    #@-node:edream.110203113231.286:onTreeBeginLabelEdit
    #@+node:edream.110203113231.287:onTreeEndLabelEdit
    # Editing will be allowed only if this routine exists.
    
    def onTreeEndLabelEdit(self,event):
    
        c = self.c ; tree = self.treeCtrl
        s = event.GetLabel()
        id = event.GetItem()
        p = tree.GetItemData(id).GetData()
        changed = s != p.headString()
        
        if not changed: return
        
        # Remember the string.
        c.setHeadString(p,s)
    
        # Update the labels as needed.
        id = tree.GetFirstVisibleItem()
        while id.IsOk():
            p2 = tree.GetItemData(id).GetData()
            if p2.v.t == p.v.t and p2 != p:
                tree.SetItemText(id,s)
            id = tree.GetNextVisible(id)
    #@-node:edream.110203113231.287:onTreeEndLabelEdit
    #@-node:edream.110203113231.285:Editing labels
    #@+node:ekr.20061105114250.1:Dragging
    #@+node:edream.110203113231.289:onTreeBeginDrag
    def onTreeBeginDrag(self,event):
    
        g.trace() ; return
    
        if event.GetItem() != self.treeCtrl.GetRootItem():
            mDraggedItem = event.GetItem()
            event.Allow()
    #@-node:edream.110203113231.289:onTreeBeginDrag
    #@+node:edream.110203113231.290:onTreeEndDrag (NOT READY YET)
    def onTreeEndDrag(self,event):
        
        g.trace() ; return
    
        #@    << Define onTreeEndDrag vars >>
        #@+node:edream.110203113231.291:<< Define onTreeEndDrag vars >>
        assert(self.tree)
        assert(self.c)
        
        dst = event.GetItem()
        src = mDraggedItem
        mDraggedItem = 0
        
        if not dst.IsOk() or not src.IsOk():
            return
        
        src_v = self.tree.GetItemData(src)
        if src_v == None:
            return
        
        dst_v =self.tree.GetItemData(dst)
        if dst_v == None:
            return
        
        parent = self.tree.GetParent(dst)
        parent_v = None
        #@nonl
        #@-node:edream.110203113231.291:<< Define onTreeEndDrag vars >>
        #@nl
        if  src == 0 or dst == 0:  return
        cookie = None
        if (
            # dst is the root
            not parent.IsOk()or
            # dst has visible children and dst isn't the first child.
            self.tree.ItemHasChildren(dst)and self.tree.IsExpanded(dst)and
            self.tree.GetFirstChild(dst,cookie) != src or
            # back(src)== dst(would otherwise be a do-nothing)
            self.tree.GetPrevSibling(src) == dst):
            #@        << Insert src as the first child of dst >>
            #@+node:edream.110203113231.292:<< Insert src as the first child of dst >>
            # Make sure the drag will be valid.
            parent_v = self.tree.GetItemData(dst)
            
            if not self.c.checkMoveWithParentWithWarning(src_v,parent_v,True):
                return
            
            src_v.moveToNthChildOf(dst_v,0)
            #@nonl
            #@-node:edream.110203113231.292:<< Insert src as the first child of dst >>
            #@nl
        else:
            # Not the root and no visible children.
            #@        << Insert src after dst >>
            #@+node:edream.110203113231.293:<< Insert src after dst >>
            # Do nothing if dst is a child of src.
            p = parent
            while p.IsOk():
                if p == src:
                    return
                p = self.tree.GetParent(p)
            
            # Do nothing if dst is joined to src.
            if dst_v.isJoinedTo(src_v):
                return
            
            # Make sure the drag will be valid.
            parent_v = self.tree.GetItemData(parent)
            if not self.c.checkMoveWithParentWithWarning(src_v,parent_v,True):
                return
            
            src_v.moveAfter(dst_v)
            #@nonl
            #@-node:edream.110203113231.293:<< Insert src after dst >>
            #@nl
        self.c.selectVnode(src_v)
        self.c.setChanged(True)
    #@-node:edream.110203113231.290:onTreeEndDrag (NOT READY YET)
    #@-node:ekr.20061105114250.1:Dragging
    #@+node:ekr.20061118123730.1:wxTree.onKeyUp/Down
    useWX = False # True, use native key handling.  False, call masterKeyHandler.
    
    def onKeyDown (self,event,*args,**keys):
        keycode = event.GetKeyCode()
        self.keyDownModifiers = event.GetModifiers()
        event.Skip() # Prepare to handle the event later.
    
    def onKeyUp (self,event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_ALT:
            event.Skip() # Do default processing.
        elif self.useWX:
            event.Skip()
        else:
            event.keyDownModifiers = self.keyDownModifiers
            event = g.app.gui.leoKeyEvent(event,c=self.c) # Convert event to canonical form.
            # g.trace('wxTree',event.keysym,self.keyDownModifiers)
            if event.keysym: # The key may have been a raw key.
                if event.keysym.isalnum() and len(event.keysym) == 1:
                    event.actualEvent.Skip(True) # Let the widget handle it.
                else:
                    # g.trace(event.keysym)
                    self.c.k.masterKeyHandler(event,stroke=event.keysym)
                    event.actualEvent.Skip(False) # Does not work.
    #@-node:ekr.20061118123730.1:wxTree.onKeyUp/Down
    #@-node:edream.110203113231.278:Event handlers (wxTree)
    #@+node:edream.111403093559:Focus (wxTree)
    def focus_get (self):
        
        return self.FindFocus()
        
    def SetFocus (self):
        
        self.treeCtrl.SetFocus()
    #@-node:edream.111403093559:Focus (wxTree)
    #@+node:ekr.20050719121701:Selection
    #@+node:ekr.20061115172306:tree.select
    #  Do **not** try to "optimize" this by returning if p==tree.currentPosition.
    
    def select (self,p,updateBeadList=True,scroll=True):
        
        '''Select a node.  Never redraws outline, but may change coloring of individual headlines.'''
        
        c = self.c ; frame = c.frame
        w = frame.body.bodyCtrl
        old_p = c.currentPosition()
        if not p or not c.positionExists(p):
            g.trace('does not exist',p.headString())
            return # Not an error.
        
        # g.trace(p.headString(),g.callers())
    
        if not g.doHook("unselect1",c=c,new_p=p,old_p=old_p,new_v=p,old_v=old_p):
            if old_p:
                #@            << unselect the old node >>
                #@+node:ekr.20061115172306.1:<< unselect the old node >>
                # Remember the position of the scrollbar before making any changes.
                
                if 0: ###
                    yview = 0 ### yview=w.yview()
                    insertSpot = w.getInsertPoint()
                    
                    if old_p != p:
                        self.endEditLabel() # sets editPosition = None
                        self.setUnselectedLabelState(old_p)
                    
                    if c.edit_widget(old_p):
                        old_p.v.t.scrollBarSpot = yview
                        old_p.v.t.insertSpot = insertSpot
                    
                #@nonl
                #@-node:ekr.20061115172306.1:<< unselect the old node >>
                #@nl
    
        g.doHook("unselect2",c=c,new_p=p,old_p=old_p,new_v=p,old_v=old_p)
        
        if not g.doHook("select1",c=c,new_p=p,old_p=old_p,new_v=p,old_v=old_p):
            #@        << select the new node >>
            #@+node:ekr.20061115172306.2:<< select the new node >>
            # Bug fix: we must always set this, even if we never edit the node.
            self.revertHeadline = p.headString()
            
            ###frame.setWrap(p)
                
            # Always do this.  Otherwise there can be problems with trailing hewlines.
            ###s = g.toUnicode(p.v.t.bodyString,"utf-8")
            ###self.setText(0,body,s)
            
            w.setAllText(p.bodyString())
            
            # We must do a full recoloring: we may be changing context!
            self.frame.body.recolor_now(p) # recolor now uses p.copy(), so this is safe.
            
            ###if p.v and p.v.t.scrollBarSpot != None:
                ###first,last = p.v.t.scrollBarSpot
                ### w.yview('moveto',first)
            
            ###if p.v and p.v.t.insertSpot != None:
                ###spot = p.v.t.insertSpot
                ###w.mark_set("insert",spot)
                ###w.setInsertPoint(spot)
                ###w.see(spot)
            ###else:
                ###w.mark_set("insert","1.0")
                ### w.setInsertPoint(0)
                
            # g.trace("select:",p.headString())
                    
            #@nonl
            #@-node:ekr.20061115172306.2:<< select the new node >>
            #@nl
            if 0: ### Not ready ###
                if p and p != old_p: # Suppress duplicate call.
                    try: # may fail during initialization.
                        # p is NOT c.currentPosition() here!
                        if 0: # Interferes with new colorizer.
                            self.canvas.update_idletasks()
                            self.scrollTo(p)
                        if scroll:
                            def scrollCallback(self=self,p=p):
                                self.scrollTo(p)
                            self.canvas.after(100,scrollCallback)
                    except Exception: pass
                #@            << update c.beadList or c.beadPointer >>
                #@+node:ekr.20061115172306.3:<< update c.beadList or c.beadPointer >>
                # c.beadList is the list of nodes for the back and forward commands.
                
                if updateBeadList:
                    
                    if c.beadPointer > -1:
                        present_p = c.beadList[c.beadPointer]
                    else:
                        present_p = c.nullPosition()
                    
                    if p != present_p:
                        # Replace the tail of c.beadList by p and make p the present node.
                        c.beadPointer += 1
                        c.beadList[c.beadPointer:] = []
                        c.beadList.append(p.copy())
                        
                        # New in Leo 4.4: limit this list to 100 items.
                        if 0: # Doesn't work yet.
                            c.beadList = c.beadList [-100:]
                            g.trace('len(c.beadList)',len(c.beadList))
                        
                    # g.trace(c.beadPointer,p,present_p)
                #@-node:ekr.20061115172306.3:<< update c.beadList or c.beadPointer >>
                #@nl
            #@        << update c.visitedList >>
            #@+node:ekr.20061115172306.4:<< update c.visitedList >>
            # The test 'p in c.visitedList' calls p.__cmp__, so this code *is* valid.
            
            # Make p the most recently visited position on the list.
            if p in c.visitedList:
                c.visitedList.remove(p)
            
            c.visitedList.insert(0,p.copy())
            
            # g.trace('len(c.visitedList)',len(c.visitedList))
            # g.trace([z.headString()[:10] for z in c.visitedList]) # don't assign to p!
            #@-node:ekr.20061115172306.4:<< update c.visitedList >>
            #@nl
    
        c.setCurrentPosition(p)
        #@    << set the current node >>
        #@+node:ekr.20061115172306.5:<< set the current node >>
        ### self.setSelectedLabelState(p)
        
        frame.scanForTabWidth(p) #GS I believe this should also get into the select1 hook
        
        if self.stayInTree:
            c.treeWantsFocus()
        else:
            c.bodyWantsFocus()
        #@-node:ekr.20061115172306.5:<< set the current node >>
        #@nl
        if 0: ### Not ready yet ###
            c.frame.body.selectMainEditor(p) # New in Leo 4.4.1.
            c.frame.updateStatusLine() # New in Leo 4.4.1.
        
        g.doHook("select2",c=c,new_p=p,old_p=old_p,new_v=p,old_v=old_p)
        g.doHook("select3",c=c,new_p=p,old_p=old_p,new_v=p,old_v=old_p)
        
        return 'break' # Supresses unwanted selection.
    #@-node:ekr.20061115172306:tree.select
    #@+node:ekr.20050719121701.2:endEditLabel
    def endEditLabel (self):
        
        self.c.frame.bodyWantsFocus()
    #@-node:ekr.20050719121701.2:endEditLabel
    #@+node:ekr.20050719121701.3:editLabel
    def editLabel (self,p,selectAll=False): # wxTree
        
        """Start editing p's headline."""
    
        tree = self.treeCtrl
        id = tree.GetFirstVisibleItem()
        while id.IsOk():
            p2 = tree.GetItemData(id).GetData()
            if p2 and p.equal(p2):
                tree.EditLabel(id)
                break
            id = tree.GetNextVisible(id)
    #@-node:ekr.20050719121701.3:editLabel
    #@+node:ekr.20070125091308:setEditWidget
    def setEditWidget (self,p):
        
        w = self.editWidgetDict.get(p.v)
    
        if w:
            w.init(id)
        else:
            # g.trace(p.headString())
            w = wxLeoHealineTextWidget(self.treeCtrl,id)
            self.editWidgetDict[p.v] = w
    
        p.edit_widget = w
    #@-node:ekr.20070125091308:setEditWidget
    #@-node:ekr.20050719121701:Selection
    #@+node:ekr.20070125093538:tree.setHeadline (new in 4.4b2)
    def setHeadline (self,p,s):
        
        '''Set the actual text of the headline widget.
        
        This is called from the undo/redo logic to change the text before redrawing.'''
        
        w = self.c.edit_widget(p)
        if w:
            w.setAllText(s)
            self.revertHeadline = s
        else:
            g.trace('-'*20,'oops')
    #@-node:ekr.20070125093538:tree.setHeadline (new in 4.4b2)
    #@+node:ekr.20070123145604:tree.set...LabelState
    def setEditLabelState (self,p,selectAll=False):     pass
    def setSelectedLabelState (self,p):                 pass
    def setUnselectedLabelState (self,p):               pass
    
    # For compatibility.
    setNormalLabelState = setEditLabelState 
    #@+node:ekr.20070123145604.4:setDisabledHeadlineColors
    def setDisabledHeadlineColors (self,p):
    
        c = self.c ; w = c.edit_widget(p)
    
        if self.trace and self.verbose:
            if not self.redrawing:
                g.trace("%10s %d %s" % ("disabled",id(w),p.headString()))
                # import traceback ; traceback.print_stack(limit=6)
    
        fg = c.config.getColor("headline_text_selected_foreground_color") or 'black'
        bg = c.config.getColor("headline_text_selected_background_color") or 'grey80'
        
        selfg = c.config.getColor("headline_text_editing_selection_foreground_color")
        selbg = c.config.getColor("headline_text_editing_selection_background_color")
    
        try:
            w.configure(state="disabled",highlightthickness=0,fg=fg,bg=bg,
                selectbackground=bg,selectforeground=fg,highlightbackground=bg)
        except:
            g.es_exception()
    #@-node:ekr.20070123145604.4:setDisabledHeadlineColors
    #@+node:ekr.20070123145604.5:setEditHeadlineColors
    def setEditHeadlineColors (self,p):
    
        c = self.c ; w = c.edit_widget(p)
        
        fg    = c.config.getColor("headline_text_editing_foreground_color") or 'black'
        bg    = c.config.getColor("headline_text_editing_background_color") or 'white'
        selfg = c.config.getColor("headline_text_editing_selection_foreground_color") or 'white'
        selbg = c.config.getColor("headline_text_editing_selection_background_color") or 'black'
        
        # try: # Use system defaults for selection foreground/background
            # w.configure(state="normal",highlightthickness=1,
            # fg=fg,bg=bg,selectforeground=selfg,selectbackground=selbg)
        # except:
            # g.es_exception()
    #@-node:ekr.20070123145604.5:setEditHeadlineColors
    #@+node:ekr.20070123145604.6:setUnselectedHeadlineColors
    def setUnselectedHeadlineColors (self,p):
        
        c = self.c ; w = c.edit_widget(p)
        
        fg = c.config.getColor("headline_text_unselected_foreground_color") or 'black'
        bg = c.config.getColor("headline_text_unselected_background_color") or 'white'
        
        # try:
            # w.configure(state="disabled",highlightthickness=0,fg=fg,bg=bg,
                # selectbackground=bg,selectforeground=fg,highlightbackground=bg)
        # except:
            # g.es_exception()
    #@-node:ekr.20070123145604.6:setUnselectedHeadlineColors
    #@-node:ekr.20070123145604:tree.set...LabelState
    #@+node:ekr.20050719121701.19:tree.expandAllAncestors
    def expandAllAncestors (self,p):
        
        redraw_flag = False
        
        # g.trace(p)
    
        for p in p.parents_iter():
            if not p.isExpanded():
                p.expand()
                redraw_flag = True
    
        return redraw_flag
    
    #@-node:ekr.20050719121701.19:tree.expandAllAncestors
    #@-others
#@nonl
#@-node:edream.111603213219:wxLeoTree class
#@+node:ekr.20061115122034:wxLeoTextWidget class
# For the ctors of these widgets, look for g.app.gui.leoTextWidgetClass

class wxLeoTextWidget (wx.TextCtrl):
    
    '''A class to wrap the Tk.Text widget.
    Translates Python (integer) indices to and from Tk (string) indices.
    
    This class inherits almost all tkText methods: you call use them as usual.'''
    
    # The signatures of tag_add and insert are different from the Tk.Text signatures.
    __pychecker__ = '--no-override' # suppress warning about changed signature.
        
    # Note: this widget inherits the GetName method from the wxWindow class.
        
    #@    @+others
    #@+node:ekr.20061118101058:Birth & special methods (wxLeoTextCtrl)
    def __init__ (self,parent,*args,**keys):
        
        w = self
    
        wx.TextCtrl.__init__(self,parent,id=-1,*args,**keys) # Init the base class.
        
        w.defaultFont = font = wx.Font(pointSize=10,
            family = wx.FONTFAMILY_TELETYPE, # wx.FONTFAMILY_ROMAN,
            style  = wx.FONTSTYLE_NORMAL,
            weight = wx.FONTWEIGHT_NORMAL,
        )
    
        w.defaultAttrib = wx.TextAttr(font=font)
        w.defaultStyle = w.SetDefaultStyle(w.defaultAttrib)
        w.allowSyntaxColoring = False
    
    def __repr__(self):
        return 'wxLeoTextWidget: %s' % (id(self))
    #@-node:ekr.20061118101058:Birth & special methods (wxLeoTextCtrl)
    #@+node:ekr.20061105125717:Index conversion
    #@+node:ekr.20061117150656:w.toGuiIndex & toPythonIndex
    # This plugin uses Python indices everywhere.
    
    def toPythonIndex (self,index):
        
        w = self
    
        if type(index) == type(99):
            return index
        elif index == '1.0':
            return 0
        elif index == 'end':
            return w.GetLastPosition()
        else:
            # g.trace(index)
            s = wx.TextCtrl.GetValue(w)
            row,col = index.split('.')
            row,col = int(row),int(col)
            row -= 1
            i = g.convertRowColToPythonIndex(s,row,col)
            return index
    
    toGuiIndex = toPythonIndex
    #@nonl
    #@-node:ekr.20061117150656:w.toGuiIndex & toPythonIndex
    #@+node:ekr.20061117150523:w.rowColToGuiIndex
    # This method is called only from the colorizer.
    # It provides a huge speedup over naive code.
    
    def rowColToGuiIndex (self,s,row,col):
    
        return g.convertRowColToPythonIndex(s,row,col)    
    #@-node:ekr.20061117150523:w.rowColToGuiIndex
    #@-node:ekr.20061105125717:Index conversion
    #@+node:ekr.20061115122034.2:Wrapper methods
    #@+node:ekr.20061116070156:bind
    def bind (self,kind,*args,**keys):
        
        pass # g.trace('wxLeoText',kind,args[0].__name__)
    #@nonl
    #@-node:ekr.20061116070156:bind
    #@+node:ekr.20061115122034.3:delete
    def delete(self,i,j=None):
    
        w = self
        i = w.toGuiIndex(i)
        if j is None: j = i+1
        j = w.toGuiIndex(j)
    
        # g.trace(i,j,len(s),repr(s[:20]))
        wx.TextCtrl.Replace(w,i,j,'')
    #@-node:ekr.20061115122034.3:delete
    #@+node:ekr.20061115122034.4:get
    def get(self,i,j=None):
    
        w = self
        i = w.toGuiIndex(i)
        if j is None: j = i+ 1
        j = w.toGuiIndex(j)
        
        s = wx.TextCtrl.GetRange(w,i,j)
        return g.toUnicode(s,g.app.tkEncoding)
    #@-node:ekr.20061115122034.4:get
    #@+node:ekr.20061115122034.5:insert
    # The signature is more restrictive than the Tk.Text.insert method.
    
    def insert(self,i,s):
        
        w = self
        i = w.toPythonIndex(i)
        
        # g.trace(i,s)
        wx.TextCtrl.SetInsertionPoint(w,i)
        wx.TextCtrl.WriteText(w,s)
    #@-node:ekr.20061115122034.5:insert
    #@+node:ekr.20061115122034.6:mark_set (do-nothing)
    def mark_set(self,markName,i):
    
        w = self
        i = w.toGuiIndex(i)
        
        ### Tk.Text.mark_set(w,markName,i)
    #@-node:ekr.20061115122034.6:mark_set (do-nothing)
    #@+node:ekr.20061115122034.7:tag_add
    # The signature is slightly different than the Tk.Text.insert method.
    
    def tag_add(self,tagName,i,j=None,*args):
        
        w = self
        i = w.toGuiIndex(i)
        if j is None: j = i + 1
        j = w.toGuiIndex(j)
    
        if not hasattr(w,'leo_styles'):
            w.leo_styles = {}
    
        style = w.leo_styles.get(tagName)
    
        if w.allowSyntaxColoring and style is not None:
            g.trace(i,j,tagName)
            wx.TextCtrl.SetStyle(w,i,j,style)
    #@nonl
    #@-node:ekr.20061115122034.7:tag_add
    #@+node:ekr.20070116073454:tag_remove
    def tag_remove(self,tagName,i,j=None,*args):
        
        w = self
        i = w.toGuiIndex(i)
        if j is None: j = i + 1
        j = w.toGuiIndex(j)
        
        return ### Not ready yet.
    
        if not hasattr(w,'leo_styles'):
            w.leo_styles = {}
    
        style = w.leo_styles.get(tagName)
    
        if w.allowSyntaxColoring and style is not None:
            g.trace(i,j,tagName)
            wx.TextCtrl.SetStyle(w,i,j,style)
    #@nonl
    #@-node:ekr.20070116073454:tag_remove
    #@+node:ekr.20061116055348:tag_delete (NEW)
    def tag_delete (self,tagName,*args,**keys):
        
        pass # g.trace(tagName,args,keys)
    #@nonl
    #@-node:ekr.20061116055348:tag_delete (NEW)
    #@+node:ekr.20061115135849:tag_configure & helper
    def tag_configure (self,colorName,**keys):
        
        # g.trace(colorName,keys)
        
        w = self
        foreground = keys.get("foreground")
        background = keys.get("background")
    
        fcolor = self.tkColorToWxColor (foreground) or wx.BLACK
        bcolor = self.tkColorToWxColor (background) or wx.WHITE
        # g.trace('%20s %10s %15s %10s %15s' % (colorName,foreground,fcolor,background,bcolor))
        style = wx.TextAttr(fcolor,bcolor,font=w.defaultFont)
        
        if not hasattr(w,'leo_styles'):
            w.leo_styles={}
    
        if style is not None:
            # g.trace(colorName,style)
            w.leo_styles[colorName] = style
            
    tag_config = tag_configure
    #@nonl
    #@+node:ekr.20061115135849.1:tkColorToWxColor
    def tkColorToWxColor (self, color):
        
        d = {
            'black':        wx.BLACK,
            "red":          wx.RED,
            "blue":         wx.BLUE,
            "#00aa00":      wx.GREEN,
            "firebrick3":   wx.RED,
            'white':        wx.WHITE,
        }
            
        return d.get(color)
    #@nonl
    #@-node:ekr.20061115135849.1:tkColorToWxColor
    #@-node:ekr.20061115135849:tag_configure & helper
    #@+node:ekr.20061115122034.8:tag_ranges 
    def tag_ranges(self,tagName):
        
        return tuple() ###
        
        w = self
        aList = Tk.Text.tag_ranges(w,tagName)
        aList = [w.toPythonIndex(z) for z in aList]
        return tuple(aList)
    #@-node:ekr.20061115122034.8:tag_ranges 
    #@-node:ekr.20061115122034.2:Wrapper methods
    #@+node:ekr.20061115122034.9:Convenience methods (tkTextWidget)
    # These have no direct Tk equivalents.  They used to be defined in the gui class.
    # These methods must take care not to call overridden methods.
    #@+node:ekr.20061115122034.10:deleteTextSelection (to do)
    def deleteTextSelection (self):
        
        w = self
    
        i,j = w.getSelectionRange()
        if i != j:
            s = w.getAllText()
            del s[i:j]
            # g.trace(len(s),repr(s[:20]))
            wx.TextCtrl.ChangeValue(w,s)
    #@-node:ekr.20061115122034.10:deleteTextSelection (to do)
    #@+node:ekr.20061115122034.11:flashCharacter (to do)
    def flashCharacter(self,i,bg='white',fg='red',flashes=3,delay=75): # tkTextWidget.
    
        w = self
        
        return ###
    
        def addFlashCallback(w,count,index):
            # g.trace(count,index)
            i,j = w.toGuiIndex(index),w.toGuiIndex(index+1)
            Tk.Text.tag_add(w,'flash',i,j)
            Tk.Text.after(w,delay,removeFlashCallback,w,count-1,index)
        
        def removeFlashCallback(w,count,index):
            # g.trace(count,index)
            Tk.Text.tag_remove(w,'flash','1.0','end')
            if count > 0:
                Tk.Text.after(w,delay,addFlashCallback,w,count,index)
    
        try:
            Tk.Text.tag_configure(w,'flash',foreground=fg,background=bg)
            addFlashCallback(w,flashes,i)
        except Exception:
            pass ; g.es_exception()
    #@nonl
    #@-node:ekr.20061115122034.11:flashCharacter (to do)
    #@+node:edream.111303093953.18:getAllText (test)
    def getAllText (self):
        
        w = self
        s =  wx.TextCtrl.GetValue(w)
        
        if s is None:
            return u""
        else:
            return g.toUnicode(s,g.app.tkEncoding)
    #@nonl
    #@-node:edream.111303093953.18:getAllText (test)
    #@+node:edream.111303093953.9:getInsertPoint (test)
    def getInsertPoint(self):
        
        w = self
    
        return  wx.TextCtrl.GetInsertionPoint(w)
    #@-node:edream.111303093953.9:getInsertPoint (test)
    #@+node:ekr.20061115122034.14:getSelectedText (test)
    def getSelectedText (self): # tkTextWidget.
    
        w = self
        
        s = wx.TextCtrl.GetStringSelection(w)
        return g.toUnicode(s,g.app.tkEncoding)
    #@-node:ekr.20061115122034.14:getSelectedText (test)
    #@+node:edream.111303093953.13:getSelectionRange (test)
    def getSelectionRange (self,sort=True):
        
        """Return a tuple representing the selected range of the widget.
        
        Return a tuple giving the insertion point if no range of text is selected."""
    
        # To get the current selection
        w = self
        sel =  wx.TextCtrl.GetSelection(w)
        if len(sel) == 2:
            i,j = sel
            if sort and i > j: i,j = j,i
            return sel
        else:
            # Return the insertion point if there is no selected text.
            i =  wx.TextCtrl.GetInsertionPoint(w)
            return i,i
    #@nonl
    #@-node:edream.111303093953.13:getSelectionRange (test)
    #@+node:ekr.20061115122034.16:hasSelection (test)
    def hasSelection (self):
        
        w = self
        i,j = w.getSelectionRange()
        return i != j
    #@-node:ekr.20061115122034.16:hasSelection (test)
    #@+node:ekr.20061115122034.17:replace (test) (could be in the base class)
    def replace (self,i,j,s):
        
        w = self
        w.delete(i,j)
        w.insert(i,s)
    #@-node:ekr.20061115122034.17:replace (test) (could be in the base class)
    #@+node:ekr.20061115122034.18:selectAllText (test) (could be in the base class)
    def selectAllText (self,insert=None):
        
        '''Select all text of the widget.'''
        
        w = self
        w.setSelectionRange(0,'end',insert=insert)
    #@-node:ekr.20061115122034.18:selectAllText (test) (could be in the base class)
    #@+node:ekr.20061115122034.19:setAllText (test)
    def setAllText (self,s):
    
        w = self
    
        # g.trace(len(s),repr(s[:20]),g.callers())
        wx.TextCtrl.Clear(w)
        wx.TextCtrl.WriteText(w,s) # Uses style.
    #@-node:ekr.20061115122034.19:setAllText (test)
    #@+node:edream.111303093953.25:see & seeInsertPoint (test)
    def see(self,index):
    
        w = self
        wx.TextCtrl.ShowPosition(w,w.toGuiIndex(index))
    
    def seeInsertPoint(self):
        
        w = self
        wx.TextCtrl.ShowPosition(w,w.GetInsertionPoint())
    #@-node:edream.111303093953.25:see & seeInsertPoint (test)
    #@+node:edream.111303093953.10:setInsertPoint (test)
    def setInsertPoint (self,pos):
    
        w = self
    
        wx.TextCtrl.SetInsertionPoint(w,w.toGuiIndex(pos))
    #@nonl
    #@-node:edream.111303093953.10:setInsertPoint (test)
    #@+node:edream.111303093953.16:setSelectionRange (test)
    def setSelectionRange (self,i,j,insert=None):
        
        w = self
        
        wx.TextCtrl.SetSelection(w,w.toGuiIndex(i),w.toGuiIndex(j))
    
        if insert is not None:
            wx.TextCtrl.SetInsertionPoint(w,w.toGuiIndex(insert))
    #@-node:edream.111303093953.16:setSelectionRange (test)
    #@+node:ekr.20061115122034.24:xyToGui/PythonIndex (passed)
    #@-node:ekr.20061115122034.24:xyToGui/PythonIndex (passed)
    #@-node:ekr.20061115122034.9:Convenience methods (tkTextWidget)
    #@-others
#@nonl
#@-node:ekr.20061115122034:wxLeoTextWidget class
#@+node:ekr.20070125074101:wxLeoHeadlineTextWidget class
class wxLeoHealineTextWidget:
    
    '''A class to make a wxWidgets headline look like a wxLeoTextWidget.'''
    
    #@    @+others
    #@+node:ekr.20070125074101.2:Birth & special methods
    def __init__ (self,treeCtrl,id):
    
        self.tree = treeCtrl
        self.init(id)
        
    def init (self,id):
        self.tree_id = id
        self.ins = 0
        self.sel = 0,0
    
    def __repr__(self):
        return 'wxLeoHeadlineTextWidget: %s' % (id(self))
    #@-node:ekr.20070125074101.2:Birth & special methods
    #@+node:ekr.20070125075903:Do-nothing methods
    def bind (self,kind,*args,**keys):              pass
    
    def cget (self,*args,**keys):                   pass
    def configure(self,*args,**keys):               pass
    
    def mark_set(self,markName,i):                  pass
    
    def see(self,index):                            pass
    def seeInsertPoint(self):                       pass
    
    def tag_add(self,tagName,i,j=None,*args):       pass
    def tag_configure (self,colorName,**keys):      pass
    def tag_delete (self,tagName,*args,**keys):     pass
    def tag_ranges(self,tagName):                   return (0,0)
    def tag_remove(self,tagName,i,j=None,*args):    pass
    #@-node:ekr.20070125075903:Do-nothing methods
    #@+node:ekr.20070125074101.3:Index conversion
    #@+node:ekr.20070125074101.4:w.toGuiIndex & toPythonIndex
    # This plugin uses Python indices everywhere.
    
    def toPythonIndex (self,index):
        
        w = self ; id = w.tree_id ; tree = w.tree
    
        if type(index) == type(99):
            return index
        elif index == '1.0':
            return 0
        elif index == 'end':
            s = tree.GetItemText(id)
            return len(s)
        else:
            s = tree.GetItemText(id)
            row,col = index.split('.')
            row,col = int(row),int(col)
            row -= 1
            i = g.convertRowColToPythonIndex(s,row,col)
            return index
    
    toGuiIndex = toPythonIndex
    #@nonl
    #@-node:ekr.20070125074101.4:w.toGuiIndex & toPythonIndex
    #@+node:ekr.20070125074101.5:w.rowColToGuiIndex
    # This method is called only from the colorizer.
    # It provides a huge speedup over naive code.
    
    def rowColToGuiIndex (self,s,row,col):
    
        return g.convertRowColToPythonIndex(s,row,col)    
    #@-node:ekr.20070125074101.5:w.rowColToGuiIndex
    #@-node:ekr.20070125074101.3:Index conversion
    #@+node:ekr.20070125074101.6:Wrapper methods
    #@+node:ekr.20070125074101.9:delete
    def delete (self,i,j=None):
    
        w = self
        s = w.getAllText()
        i = w.toPythonIndex(i)
        if j is None: j = i + 1
        j = w.toPythonIndex(j)
    
        w.setAllText(s[:i]+s[j:])
        w.ins = i
        w.sel = i,i
    #@-node:ekr.20070125074101.9:delete
    #@+node:ekr.20070125074101.20:deleteTextSelection
    def deleteTextSelection (self):
        
        w = self
        if w.hasSelection():
            i,j = w.sel
            s = w.getAllText()
            s = s[:i] + s[j:]
            w.setAllText(s)
            w.ins = i
            w.sel = i,i
    #@-node:ekr.20070125074101.20:deleteTextSelection
    #@+node:ekr.20070125074101.21:flashCharacter (to do)
    def flashCharacter(self,i,bg='white',fg='red',flashes=3,delay=75):
    
        w = self
    #@-node:ekr.20070125074101.21:flashCharacter (to do)
    #@+node:ekr.20070125074101.10:get
    def get(self,i,j=None):
        
        w = self
        s = w.getAllText()
        i = w.toPythonIndex(i)
        if j is None: j = i+1
        j = w.toPythonIndex(j)
    
        return g.toUnicode(s[i:j],g.app.tkEncoding)
    #@-node:ekr.20070125074101.10:get
    #@+node:ekr.20070125074101.22:getAllText
    def getAllText (self):
        
        w = self
    
        s = w.tree.GetItemText(w.tree_id)
    
        if s is None:
            return u""
        else:
            return g.toUnicode(s,g.app.tkEncoding)
    #@nonl
    #@-node:ekr.20070125074101.22:getAllText
    #@+node:ekr.20070125074101.23:getInsertPoint
    def getInsertPoint(self):
        
        w = self
        return w.ins
    #@nonl
    #@-node:ekr.20070125074101.23:getInsertPoint
    #@+node:ekr.20070125074101.24:getSelectedText
    def getSelectedText (self):
        
        w = self
    
        if w.hasSelection():
            i,j = w.sel
            s = w.getAllText()
            return s[i:j]
        else:
            return u''
    #@-node:ekr.20070125074101.24:getSelectedText
    #@+node:ekr.20070125074101.25:getSelectionRange
    def getSelectionRange (self,sort=True):
        
        """Return a tuple representing the selected range of the widget.
        
        Return a tuple giving the insertion point if no range of text is selected."""
        
        w = self
        i,j = w.sel ; ins = w.ins
    
        if i == j:
            return ins,ins
        else:
            return i,j
    #@-node:ekr.20070125074101.25:getSelectionRange
    #@+node:ekr.20070125074101.26:hasSelection
    def hasSelection (self):
        
        w = self
        i,j = w.sel
        return i != j
    #@-node:ekr.20070125074101.26:hasSelection
    #@+node:ekr.20070125074101.11:insert
    # The signature is more restrictive than the Tk.Text.insert method.
    
    def insert(self,i,s2):
        
        w = self
        s = w.getAllText()
        i = w.toPythonIndex(i)
    
        w.setAllText(s[:i] + s2 + s[i:])
        j = i + len(s2)
        w.ins = j
        w.sel = j,j
    #@-node:ekr.20070125074101.11:insert
    #@+node:ekr.20070125074101.27:replace
    def replace (self,i,j,s):
        
        w = self
        w.delete(i,j)
        w.insert(i,s)
    #@-node:ekr.20070125074101.27:replace
    #@+node:ekr.20070125074101.28:selectAllText
    def selectAllText (self,insert=None):
        
        '''Select all text of the widget.'''
    
        w = self
        s = w.getAllText()
        w.sel = 0,len(s)
    #@nonl
    #@-node:ekr.20070125074101.28:selectAllText
    #@+node:ekr.20070125074101.29:setAllText
    def setAllText (self,s):
    
        w = self
        g.trace(repr(w.tree_id))
        w.tree.SetItemText(w.tree_id,s)
    #@-node:ekr.20070125074101.29:setAllText
    #@+node:ekr.20070125074101.31:setInsertPoint
    def setInsertPoint (self,pos):
        
        w = self
        w.ins = w.toPythonIndex(pos)
    #@-node:ekr.20070125074101.31:setInsertPoint
    #@+node:ekr.20070125074101.32:setSelectionRange
    def setSelectionRange (self,i,j,insert=None):
        
        w = self
        w.sel = w.toPythonIndex(i),w.toPythonIndex(j)
        if insert is not None:
            w.ins = w.toPythonIndex(insert)
    #@-node:ekr.20070125074101.32:setSelectionRange
    #@-node:ekr.20070125074101.6:Wrapper methods
    #@-others
    

    
#@nonl
#@-node:ekr.20070125074101:wxLeoHeadlineTextWidget class
#@-others
#@nonl
#@-node:edream.110203113231.302:@thin __wx_gui.py
#@-leo
