# -*- coding: utf-8 -*-
#@+leo-ver=4-thin
#@+node:edream.110203113231.302:@thin __wx_gui.py
#@@first

"""A plugin to use wxWidgets as Leo's gui."""

__version__ = '0.6'

#@<< version history >>
#@+node:ekr.20050719111045:<< version history >>
#@@nocolor
#@+at
# 
# 0.5 EKR: Released with Leo 4.4.3 a1.
# 0.6 EKR: Released with Leo 4.4.3 a2.
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
    import wx.richtext
    import wx.stc
except ImportError:
    g.es_print('wx_gui plugin: can not import wxWidgets')
#@nonl
#@-node:edream.110203113231.303:<< imports >>
#@nl

# Constants and globals.

### textBaseClass = wx.richtext.RichTextCtrl # wx.TextCtrl
cSplitterWidth = 600
const_dict = {}
const_lastVal = 100 # Starting wx id.

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
#@-node:ekr.20050719111045.1: init
#@+node:ekr.20070130115253:const
def const(name):
    
    """Return the wx id associated with name"""
    
    # Should this canonicalize the label?  Just remove '&' ??
    global const_dict, const_lastVal

    id = const_dict.get(name)
    if id != None:
        return id
    else:
        global const_lastVal
        const_lastVal += 1
        const_dict[name] = const_lastVal
        # g.trace(name,const_lastVal)
        return const_lastVal
#@-node:ekr.20070130115253:const
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
        self.findText = plainTextWidget (
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
        self.changeText = plainTextWidget (
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
        
        self.find_ctrl   = plainTextWidget(f,name='find-text',  size=(300,-1))
        self.change_ctrl = plainTextWidget(f,name='change-text',size=(300,-1))
        
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
    #@+node:ekr.20070130212844:masterMenuHandler
    def masterMenuHandler (self,stroke,func,commandName):
        
        k = self ; c = k.c ; w = c.frame.getFocus()
        
        g.trace('wx: stroke',stroke,'func',func and func.__name__,commandName,g.callers())
        
        # Create a minimal event for commands that require them.
        event = g.Bunch(char='',keysym='',widget=w)
        
        if stroke:
            return k.masterKeyHandler(event,stroke=stroke)
        else:
            return k.masterCommand(event,func,stroke,commandName)
    #@-node:ekr.20070130212844:masterMenuHandler
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
        self.forceFullRecolorFlag = False
    #@nonl
    #@-node:edream.110203113231.541:wxBody.__init__
    #@+node:edream.110203113231.542:wxBody.createControl
    def createControl (self,frame,parentFrame):
        
        w = plainTextWidget(
            parentFrame,
            pos = wx.DefaultPosition,
            size = wx.DefaultSize,
            style = (wx.TE_RICH | wx.TE_RICH2 | wx.TE_MULTILINE),
            name = 'body', # Must be body for k.masterKeyHandler.
        )
    
        # wx.EVT_CHAR(w,self.onKey) # Provides translated keycodes.
        wx.EVT_SET_FOCUS    (w,self.onFocusIn)
        wx.EVT_KEY_DOWN     (w,self.onKeyDown) # Provides raw key codes.
        wx.EVT_KEY_UP       (w,self.onKeyUp) # Provides raw key codes.
    
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
        
        pass
        
        ### return self.bodyCtrl.tag_configure(colorName,**keys)
    #@-node:edream.111303205611.2:wxBody.tag_configure
    #@+node:edream.111303205611.3:wxBody.tag_delete
    def tag_delete(self,tagName):
        
        return ###
    
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
    def onKeyDown (self,event,*args,**keys):
        keycode = event.GetKeyCode()
        self.keyDownModifiers = event.GetModifiers()
        if keycode == wx.WXK_ALT:
            event.Skip() # Do default processing.
        else:
            pass # This is required to suppress wx event handling.
        
    def onKeyUp (self,event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_ALT:
            event.Skip() # Do default processing.
        else:
            event.keyDownModifiers = self.keyDownModifiers
            keysym = g.app.gui.eventKeysym(event)
            if keysym:
                # g.trace(keysym)
                self.c.k.masterKeyHandler(event,stroke=keysym)
    #@-node:ekr.20061116083454:wxBody.onKeyUp/Down
    #@+node:ekr.20070125111939:wxBody.onFocuIn
    def onFocusIn (self,event=None):
        
        g.app.gui.focus_widget = self.bodyCtrl
        event.Skip()
    #@nonl
    #@-node:ekr.20070125111939:wxBody.onFocuIn
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
            s = w.getAllText()
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
    #@+node:ekr.20070204123745:wxBody.forceFullRecolor
    def forceFullRecolor (self):
       
        self.forceFullRecolorFlag = True
    #@nonl
    #@-node:ekr.20070204123745:wxBody.forceFullRecolor
    #@-others
#@nonl
#@-node:edream.110203113231.539:wxLeoBody class
#@+node:ekr.20070130091315:wxComparePanel class (not ready yet)
"""Leo's base compare class."""

#@@language python
#@@tabwidth -4
#@@pagewidth 80

import leoGlobals as g
import leoCompare

class wxComparePanel (leoCompare.leoCompare): #,leoWxDialog):
    
    """A class that creates Leo's compare panel."""

    #@    @+others
    #@+node:ekr.20070130091315.1:Birth...
    #@+node:ekr.20070130091315.2:wxComparePanel.__init__
    def __init__ (self,c):
        
        # Init the base class.
        leoCompare.leoCompare.__init__ (self,c)
        ###leoTkinterDialog.leoTkinterDialog.__init__(self,c,"Compare files and directories",resizeable=False)
    
        if g.app.unitTesting: return
    
        self.c = c
        
        if 0:
            #@        << init tkinter compare ivars >>
            #@+node:ekr.20070130091315.3:<< init tkinter compare ivars >>
            # Ivars pointing to Tk elements.
            self.browseEntries = []
            self.extensionEntry = None
            self.countEntry = None
            self.printButtons = []
                
            # No corresponding ivar in the leoCompare class.
            self.useOutputFileVar = Tk.IntVar()
            
            # These all correspond to ivars in leoCompare
            self.appendOutputVar             = Tk.IntVar()
            
            self.ignoreBlankLinesVar         = Tk.IntVar()
            self.ignoreFirstLine1Var         = Tk.IntVar()
            self.ignoreFirstLine2Var         = Tk.IntVar()
            self.ignoreInteriorWhitespaceVar = Tk.IntVar()
            self.ignoreLeadingWhitespaceVar  = Tk.IntVar()
            self.ignoreSentinelLinesVar      = Tk.IntVar()
            
            self.limitToExtensionVar         = Tk.IntVar()
            self.makeWhitespaceVisibleVar    = Tk.IntVar()
            
            self.printBothMatchesVar         = Tk.IntVar()
            self.printMatchesVar             = Tk.IntVar()
            self.printMismatchesVar          = Tk.IntVar()
            self.printTrailingMismatchesVar  = Tk.IntVar()
            self.stopAfterMismatchVar        = Tk.IntVar()
            #@-node:ekr.20070130091315.3:<< init tkinter compare ivars >>
            #@nl
        
        # These ivars are set from Entry widgets.
        self.limitCount = 0
        self.limitToExtension = None
        
        # The default file name in the "output file name" browsers.
        self.defaultOutputFileName = "CompareResults.txt"
        
        if 0:
            self.createTopFrame()
            self.createFrame()
    #@-node:ekr.20070130091315.2:wxComparePanel.__init__
    #@+node:ekr.20070130091315.4:finishCreate (tkComparePanel)
    # Initialize ivars from config parameters.
    
    def finishCreate (self):
        
        c = self.c
        
        # File names.
        for i,option in (
            (0,"compare_file_1"),
            (1,"compare_file_2"),
            (2,"output_file") ):
                
            name = c.config.getString(option)
            if name and len(name) > 0:
                e = self.browseEntries[i]
                e.delete(0,"end")
                e.insert(0,name)
                
        name = c.config.getString("output_file")
        b = g.choose(name and len(name) > 0,1,0)
        self.useOutputFileVar.set(b)
    
        # File options.
        b = c.config.getBool("ignore_first_line_of_file_1")
        if b == None: b = 0
        self.ignoreFirstLine1Var.set(b)
        
        b = c.config.getBool("ignore_first_line_of_file_2")
        if b == None: b = 0
        self.ignoreFirstLine2Var.set(b)
        
        b = c.config.getBool("append_output_to_output_file")
        if b == None: b = 0
        self.appendOutputVar.set(b)
    
        ext = c.config.getString("limit_directory_search_extension")
        b = ext and len(ext) > 0
        b = g.choose(b and b != 0,1,0)
        self.limitToExtensionVar.set(b)
        if b:
            e = self.extensionEntry
            e.delete(0,"end")
            e.insert(0,ext)
            
        # Print options.
        b = c.config.getBool("print_both_lines_for_matches")
        if b == None: b = 0
        self.printBothMatchesVar.set(b)
        
        b = c.config.getBool("print_matching_lines")
        if b == None: b = 0
        self.printMatchesVar.set(b)
        
        b = c.config.getBool("print_mismatching_lines")
        if b == None: b = 0
        self.printMismatchesVar.set(b)
        
        b = c.config.getBool("print_trailing_lines")
        if b == None: b = 0
        self.printTrailingMismatchesVar.set(b)
        
        n = c.config.getInt("limit_count")
        b = n and n > 0
        b = g.choose(b and b != 0,1,0)
        self.stopAfterMismatchVar.set(b)
        if b:
            e = self.countEntry
            e.delete(0,"end")
            e.insert(0,str(n))
    
        # bool options...
        for option,var,default in (
            # Whitespace options.
            ("ignore_blank_lines",self.ignoreBlankLinesVar,1),
            ("ignore_interior_whitespace",self.ignoreInteriorWhitespaceVar,0),
            ("ignore_leading_whitespace",self.ignoreLeadingWhitespaceVar,0),
            ("ignore_sentinel_lines",self.ignoreSentinelLinesVar,0),
            ("make_whitespace_visible", self.makeWhitespaceVisibleVar,0),
        ):
            b = c.config.getBool(option)
            if b is None: b = default
            var.set(b)
        
        if 0: # old code
            b = c.config.getBool("ignore_blank_lines")
            if b == None: b = 1 # unusual default.
            self.ignoreBlankLinesVar.set(b)
            
            b = c.config.getBool("ignore_interior_whitespace")
            if b == None: b = 0
            self.ignoreInteriorWhitespaceVar.set(b)
            
            b = c.config.getBool("ignore_leading_whitespace")
            if b == None: b = 0
            self.ignoreLeadingWhitespaceVar.set(b)
            
            b = c.config.getBool("ignore_sentinel_lines")
            if b == None: b = 0
            self.ignoreSentinelLinesVar.set(b)
            
            b = c.config.getBool("make_whitespace_visible")
            if b == None: b = 0
            self.makeWhitespaceVisibleVar.set(b)
    #@-node:ekr.20070130091315.4:finishCreate (tkComparePanel)
    #@+node:ekr.20070130091315.5:createFrame (tkComparePanel)
    def createFrame (self):
    
        gui = g.app.gui ; top = self.top
    
        #@    << create the organizer frames >>
        #@+node:ekr.20070130091315.6:<< create the organizer frames >>
        outer = Tk.Frame(self.frame, bd=2,relief="groove")
        outer.pack(pady=4)
        
        row1 = Tk.Frame(outer)
        row1.pack(pady=4)
        
        row2 = Tk.Frame(outer)
        row2.pack(pady=4)
        
        row3 = Tk.Frame(outer)
        row3.pack(pady=4)
        
        row4 = Tk.Frame(outer)
        row4.pack(pady=4,expand=1,fill="x") # for left justification.
        
        options = Tk.Frame(outer)
        options.pack(pady=4)
        
        ws = Tk.Frame(options)
        ws.pack(side="left",padx=4)
        
        pr = Tk.Frame(options)
        pr.pack(side="right",padx=4)
        
        lower = Tk.Frame(outer)
        lower.pack(pady=6)
        #@-node:ekr.20070130091315.6:<< create the organizer frames >>
        #@nl
        #@    << create the browser rows >>
        #@+node:ekr.20070130091315.7:<< create the browser rows >>
        for row,text,text2,command,var in (
            (row1,"Compare path 1:","Ignore first line",self.onBrowse1,self.ignoreFirstLine1Var),
            (row2,"Compare path 2:","Ignore first line",self.onBrowse2,self.ignoreFirstLine2Var),
            (row3,"Output file:",   "Use output file",  self.onBrowse3,self.useOutputFileVar) ):
        
            lab = Tk.Label(row,anchor="e",text=text,width=13)
            lab.pack(side="left",padx=4)
            
            e = Tk.Entry(row)
            e.pack(side="left",padx=2)
            self.browseEntries.append(e)
            
            b = Tk.Button(row,text="browse...",command=command)
            b.pack(side="left",padx=6)
        
            b = Tk.Checkbutton(row,text=text2,anchor="w",variable=var,width=15)
            b.pack(side="left")
        #@-node:ekr.20070130091315.7:<< create the browser rows >>
        #@nl
        #@    << create the extension row >>
        #@+node:ekr.20070130091315.8:<< create the extension row >>
        b = Tk.Checkbutton(row4,anchor="w",var=self.limitToExtensionVar,
            text="Limit directory compares to type:")
        b.pack(side="left",padx=4)
        
        self.extensionEntry = e = Tk.Entry(row4,width=6)
        e.pack(side="left",padx=2)
        
        b = Tk.Checkbutton(row4,anchor="w",var=self.appendOutputVar,
            text="Append output to output file")
        b.pack(side="left",padx=4)
        #@-node:ekr.20070130091315.8:<< create the extension row >>
        #@nl
        #@    << create the whitespace options frame >>
        #@+node:ekr.20070130091315.9:<< create the whitespace options frame >>
        w,f = gui.create_labeled_frame(ws,caption="Whitespace options",relief="groove")
            
        for text,var in (
            ("Ignore Leo sentinel lines", self.ignoreSentinelLinesVar),
            ("Ignore blank lines",        self.ignoreBlankLinesVar),
            ("Ignore leading whitespace", self.ignoreLeadingWhitespaceVar),
            ("Ignore interior whitespace",self.ignoreInteriorWhitespaceVar),
            ("Make whitespace visible",   self.makeWhitespaceVisibleVar) ):
            
            b = Tk.Checkbutton(f,text=text,variable=var)
            b.pack(side="top",anchor="w")
            
        spacer = Tk.Frame(f)
        spacer.pack(padx="1i")
        #@-node:ekr.20070130091315.9:<< create the whitespace options frame >>
        #@nl
        #@    << create the print options frame >>
        #@+node:ekr.20070130091315.10:<< create the print options frame >>
        w,f = gui.create_labeled_frame(pr,caption="Print options",relief="groove")
        
        row = Tk.Frame(f)
        row.pack(expand=1,fill="x")
        
        b = Tk.Checkbutton(row,text="Stop after",variable=self.stopAfterMismatchVar)
        b.pack(side="left",anchor="w")
        
        self.countEntry = e = Tk.Entry(row,width=4)
        e.pack(side="left",padx=2)
        e.insert(01,"1")
        
        lab = Tk.Label(row,text="mismatches")
        lab.pack(side="left",padx=2)
        
        for padx,text,var in (    
            (0,  "Print matched lines",           self.printMatchesVar),
            (20, "Show both matching lines",      self.printBothMatchesVar),
            (0,  "Print mismatched lines",        self.printMismatchesVar),
            (0,  "Print unmatched trailing lines",self.printTrailingMismatchesVar) ):
            
            b = Tk.Checkbutton(f,text=text,variable=var)
            b.pack(side="top",anchor="w",padx=padx)
            self.printButtons.append(b)
            
        # To enable or disable the "Print both matching lines" button.
        b = self.printButtons[0]
        b.configure(command=self.onPrintMatchedLines)
        
        spacer = Tk.Frame(f)
        spacer.pack(padx="1i")
        #@-node:ekr.20070130091315.10:<< create the print options frame >>
        #@nl
        #@    << create the compare buttons >>
        #@+node:ekr.20070130091315.11:<< create the compare buttons >>
        for text,command in (
            ("Compare files",      self.onCompareFiles),
            ("Compare directories",self.onCompareDirectories) ):
            
            b = Tk.Button(lower,text=text,command=command,width=18)
            b.pack(side="left",padx=6)
        #@-node:ekr.20070130091315.11:<< create the compare buttons >>
        #@nl
    
        gui.center_dialog(top) # Do this _after_ building the dialog!
        self.finishCreate()
        top.protocol("WM_DELETE_WINDOW", self.onClose)
    #@-node:ekr.20070130091315.5:createFrame (tkComparePanel)
    #@+node:ekr.20070130091315.12:setIvarsFromWidgets
    def setIvarsFromWidgets (self):
    
        # File paths: checks for valid file name.
        e = self.browseEntries[0]
        self.fileName1 = e.get()
        
        e = self.browseEntries[1]
        self.fileName2 = e.get()
    
        # Ignore first line settings.
        self.ignoreFirstLine1 = self.ignoreFirstLine1Var.get()
        self.ignoreFirstLine2 = self.ignoreFirstLine2Var.get()
        
        # Output file: checks for valid file name.
        if self.useOutputFileVar.get():
            e = self.browseEntries[2]
            name = e.get()
            if name != None and len(name) == 0:
                name = None
            self.outputFileName = name
        else:
            self.outputFileName = None
    
        # Extension settings.
        if self.limitToExtensionVar.get():
            self.limitToExtension = self.extensionEntry.get()
            if len(self.limitToExtension) == 0:
                self.limitToExtension = None
        else:
            self.limitToExtension = None
            
        self.appendOutput = self.appendOutputVar.get()
        
        # Whitespace options.
        self.ignoreBlankLines         = self.ignoreBlankLinesVar.get()
        self.ignoreInteriorWhitespace = self.ignoreInteriorWhitespaceVar.get()
        self.ignoreLeadingWhitespace  = self.ignoreLeadingWhitespaceVar.get()
        self.ignoreSentinelLines      = self.ignoreSentinelLinesVar.get()
        self.makeWhitespaceVisible    = self.makeWhitespaceVisibleVar.get()
        
        # Print options.
        self.printMatches            = self.printMatchesVar.get()
        self.printMismatches         = self.printMismatchesVar.get()
        self.printTrailingMismatches = self.printTrailingMismatchesVar.get()
        
        if self.printMatches:
            self.printBothMatches = self.printBothMatchesVar.get()
        else:
            self.printBothMatches = False
        
        if self.stopAfterMismatchVar.get():
            try:
                count = self.countEntry.get()
                self.limitCount = int(count)
            except: self.limitCount = 0
        else:
            self.limitCount = 0
    #@-node:ekr.20070130091315.12:setIvarsFromWidgets
    #@-node:ekr.20070130091315.1:Birth...
    #@+node:ekr.20070130091315.13:bringToFront
    def bringToFront(self):
        
        self.top.deiconify()
        self.top.lift()
    #@-node:ekr.20070130091315.13:bringToFront
    #@+node:ekr.20070130091315.14:browser
    def browser (self,n):
        
        types = [
            ("C/C++ files","*.c"),
            ("C/C++ files","*.cpp"),
            ("C/C++ files","*.h"),
            ("C/C++ files","*.hpp"),
            ("Java files","*.java"),
            ("Lua files", "*.lua"),
            ("Pascal files","*.pas"),
            ("Python files","*.py"),
            ("Text files","*.txt"),
            ("All files","*") ]
    
        fileName = tkFileDialog.askopenfilename(
            title="Choose compare file" + n,
            filetypes=types,
            defaultextension=".txt")
            
        if fileName and len(fileName) > 0:
            # The dialog also warns about this, so this may never happen.
            if not g.os_path_exists(fileName):
                self.show("not found: " + fileName)
                fileName = None
        else: fileName = None
            
        return fileName
    #@-node:ekr.20070130091315.14:browser
    #@+node:ekr.20070130091315.15:Event handlers...
    #@+node:ekr.20070130091315.16:onBrowse...
    def onBrowse1 (self):
        
        fileName = self.browser("1")
        if fileName:
            e = self.browseEntries[0]
            e.delete(0,"end")
            e.insert(0,fileName)
        self.top.deiconify()
        
    def onBrowse2 (self):
        
        fileName = self.browser("2")
        if fileName:
            e = self.browseEntries[1]
            e.delete(0,"end")
            e.insert(0,fileName)
        self.top.deiconify()
        
    def onBrowse3 (self): # Get the name of the output file.
    
        fileName = tkFileDialog.asksaveasfilename(
            initialfile = self.defaultOutputFileName,
            title="Set output file",
            filetypes=[("Text files", "*.txt")],
            defaultextension=".txt")
            
        if fileName and len(fileName) > 0:
            self.defaultOutputFileName = fileName
            self.useOutputFileVar.set(1) # The user will expect this.
            e = self.browseEntries[2]
            e.delete(0,"end")
            e.insert(0,fileName)
    #@-node:ekr.20070130091315.16:onBrowse...
    #@+node:ekr.20070130091315.17:onClose
    def onClose (self):
        
        self.top.withdraw()
    #@-node:ekr.20070130091315.17:onClose
    #@+node:ekr.20070130091315.18:onCompare...
    def onCompareDirectories (self):
    
        self.setIvarsFromWidgets()
        self.compare_directories(self.fileName1,self.fileName2)
    
    def onCompareFiles (self):
    
        self.setIvarsFromWidgets()
        self.compare_files(self.fileName1,self.fileName2)
    #@-node:ekr.20070130091315.18:onCompare...
    #@+node:ekr.20070130091315.19:onPrintMatchedLines
    def onPrintMatchedLines (self):
        
        v = self.printMatchesVar.get()
        b = self.printButtons[1]
        state = g.choose(v,"normal","disabled")
        b.configure(state=state)
    #@-node:ekr.20070130091315.19:onPrintMatchedLines
    #@-node:ekr.20070130091315.15:Event handlers...
    #@-others
#@-node:ekr.20070130091315:wxComparePanel class (not ready yet)
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
        self.killed = False
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
        
        self.killed = True
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
        
            ### style = wx.TE_RICH | wx.TE_RICH2 | wx.TE_MULTILINE
            style = wx.TE_MULTILINE
            w = plainTextWidget(
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
            
            if g.app.gui.use_stc:
                pass
            else:
                w.defaultFont = font = wx.Font(pointSize=10,
                    family = wx.FONTFAMILY_TELETYPE,
                    style  = wx.FONTSTYLE_NORMAL,
                    weight = wx.FONTWEIGHT_NORMAL,
                )
                # w.defaultAttrib = wx.TextAttr(font=font)
                # w.defaultStyle = w.SetDefaultStyle(w.defaultAttrib)
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
    
    #@    @+others
    #@+node:ekr.20070125124900:Birth
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
        
        return ###
    
        d = self.acceleratorDict
        aList = d.get(menu,[])
        data = ch,accel,id,label
        aList.append(data)
        d [menu] = aList
    #@-node:ekr.20061118203148.1:createAccelData
    #@+node:ekr.20061118194416:createAcceleratorTables
    def createAcceleratorTables (self):
        
        return ###
        
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
    #@-node:ekr.20070125124900:Birth
    #@+node:ekr.20061106062514:Not called
    def bind (self,bind_shortcut,callback):
        
        g.trace(bind_shortcut,callback)
    
    def delete (self,menu,readItemName):
        
        g.trace(menu,readItemName)
    
    def destroy (self,menu):
        
        g.trace(menu)
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
    #@+node:edream.111303103141:add_command
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
    #@-node:edream.111303103141:add_command
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
    #@+node:ekr.20070130183007:index & invoke
    def index (self,name):
        
        '''Return the menu item whose name is given.'''
        
        g.trace(name)
        
    def invoke (self,i):
        
        '''Invoke the menu whose index is i'''
    #@-node:ekr.20070130183007:index & invoke
    #@+node:ekr.20070124111252:insert (TO DO)
    def insert (self,*args,**keys):
    
        pass # g.trace('wxMenu: to do',args,keys)
    #@nonl
    #@-node:ekr.20070124111252:insert (TO DO)
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
    
        font = wx.Font(pointSize=10,
            family = wx.FONTFAMILY_TELETYPE, # wx.FONTFAMILY_ROMAN,
            style  = wx.FONTSTYLE_NORMAL,
            weight = wx.FONTWEIGHT_NORMAL,
        )
        
        g.trace(font.GetPointSize())
    
        self.ctrl = w = wxTextWidget(
            parentFrame,
            pos = wx.DefaultPosition,
            size = (1000,-1),
            name = 'minibuffer',
        )
        
        w.defaultFont = font
        w.defaultAttrib = wx.TextAttr(font=font)
            
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
        
        if not self.c.frame.killed:
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
        
        if self.c.frame.killed:
            return ''
        else:
            return self.w.GetStatusText()
    #@-node:ekr.20070112173627.4:get
    #@+node:ekr.20070112173627.5:getFrame
    def getFrame (self):
        
        if self.c.frame.killed:
            return None
        else:
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
        
        if not self.c.frame.killed:
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
    
        if g.app.killed or not self.isVisible or self.c.frame.killed:
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
        self.idDict = {} # Keys are vnodes, values are wxTree id's.
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
        #wx.EVT_TREE_KEY_DOWN  (w,id,self.onTreeKeyDown) # Control keys do not fire this event.
    
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
        
        wx.EVT_SET_FOCUS            (w,self.onFocusIn)
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
    #@+node:ekr.20061118122218.1:setBindings
    def setBindings(self):
        
        pass # g.trace('wxLeoTree: to do')
    
    def bind(self,*args,**keys):
        
        pass # g.trace('wxLeoTree',args,keys)
    #@nonl
    #@-node:ekr.20061118122218.1:setBindings
    #@-node:edream.111603213219.1:wxTree.__init__
    #@+node:edream.111303202917:Drawing
    #@+node:edream.110203113231.295:beginUpdate
    def beginUpdate (self):
    
        self.updateCount += 1
    #@nonl
    #@-node:edream.110203113231.295:beginUpdate
    #@+node:edream.110203113231.296:endUpdate
    def endUpdate (self,flag=True,scroll=False):
    
        assert(self.updateCount > 0)
    
        self.updateCount -= 1
        if flag and self.updateCount <= 0:
            self.redraw()
            if self.updateCount < 0:
                g.trace("Can't happen: negative updateCount",g.callers())
    #@-node:edream.110203113231.296:endUpdate
    #@+node:edream.110203113231.298:redraw & redraw_now & helpers
    redraw_count = 0
    
    def redraw (self):
        
        c = self.c ; tree = self.treeCtrl
        if c is None: return
        p = c.rootPosition()
        if not p: return
        
        self.redraw_count += 1
        self.idDict = {}
        # g.trace(self.redraw_count)
    
        self.drawing = True # Tell event handlers not to call us.
        try:
            self.expandAllAncestors(c.currentPosition())
            tree.DeleteAllItems()
            self.root_id = root_id = tree.AddRoot('Root Node')
            ### tree.SetItemFont(root_id,self.defaultFont)
            while p:
                self.redraw_subtree(root_id,p)
                p.moveToNext()
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
        
        self.setEditWidget(p,id)
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
            
        # Do this *after* drawing the children so as to ensure the +- box is drawn properly.
        if p == self.c.currentPosition():
            tree.SelectItem(id) # Generates call to onTreeChanged.
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
        
        self.setEditWidget(p,id)
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
            
        # Do this *after* drawing the children so as to ensure the +- box is drawn properly.
        if p == self.c.currentPosition():
            tree.SelectItem(id) # Generates call to onTreeChanged.
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
        
        for p in self.c.rootPosition().self_and_siblings_iter():
            self.updateIconsInSubtree(p)
    
    def updateIconsInSubtree (self,p):
        self.updateIcon(p)
        if p.hasChildren() and p.isExpanded():
            for child in p.firstChild().self_and_siblings_iter():
                self.updateIconsInSubtree(child)
                
    def updateIcon(self,p):
        val = p.v.computeIcon()
        id = self.idDict.get(p.v)
        if id:
            self.treeCtrl.SetItemImage(id,val)
        else:
            g.trace('can not happen: no id',p.headString())
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
    def onKeyDown (self,event,*args,**keys):
        keycode = event.GetKeyCode()
        self.keyDownModifiers = event.GetModifiers()
        # g.trace('wxTree')
        event.Skip() # Prepare to handle the event later.
    
    def onKeyUp (self,event):
        keycode = event.GetKeyCode()
        g.trace('tree:keycode',keycode)
        if keycode == wx.WXK_ALT:
            event.Skip() # Do default processing.
        else:
            event.keyDownModifiers = self.keyDownModifiers
            event.Skip()
    
            # event = g.app.gui.leoKeyEvent(event,c=self.c) # Convert event to canonical form.
            # event.actualEvent.Skip()
    
            # if event.keysym: # The key may have been a raw key.
                # g.trace('wxTree',event.keysym,self.keyDownModifiers)
                # if event.keysym.isalnum() and len(event.keysym) == 1:
                    # event.actualEvent.Skip(True) # Let the widget handle it.
                # else:
                    # # g.trace(event.keysym)
                    # self.c.k.masterKeyHandler(event,stroke=event.keysym)
              
    #@nonl
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
        
        pass
    
        # # Disallow editing of the dummy root node.
        # id = event.GetItem()
        # if id == self.root_id:
            # event.Veto()
    #@nonl
    #@-node:edream.110203113231.286:onTreeBeginLabelEdit
    #@+node:edream.110203113231.287:onTreeEndLabelEdit
    # Editing will be allowed only if this routine exists.
    
    def onTreeEndLabelEdit(self,event):
    
        c = self.c ; tree = self.treeCtrl
        id = event.GetItem()
        s = tree.GetItemText(id)
        p = self.treeCtrl.GetItemData(id).GetData()
        
        if s != p.headString():
            c.beginUpdate()
            try:
                c.setHeadString(p,s)
            finally:
                c.endUpdate()
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
    #@+node:ekr.20070125111939.1:onFocusIn
    def onFocusIn (self,event=None):
        
        g.app.gui.focus_widget = self.treeCtrl
    #@-node:ekr.20070125111939.1:onFocusIn
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
    
        if not w:
            g.trace('Null w','c',c,'c.frame',c.frame,'c.frame.body',c.frame.body)
        old_p = c.currentPosition()
        if not p or not c.positionExists(p):
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
        
        redrawFlag = self.expandAllAncestors(p)
        if redrawFlag:
            c.redraw()
            
        id = self.idDict.get(p.v)
        assert(id)
        self.treeCtrl.EditLabel(id)
    #@-node:ekr.20050719121701.3:editLabel
    #@+node:ekr.20070125091308:setEditWidget
    def setEditWidget (self,p,id):
        
        w = self.editWidgetDict.get(p.v)
        self.idDict[p.v] = id
    
        if w:
            w.init(id)
        else:
            # g.trace(p.headString())
            w = wxLeoHeadlineTextWidget(self.treeCtrl,id)
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
    #@+node:ekr.20070130154139:headWidth
    def headWidth (self,s):
        
        return 0
    #@nonl
    #@-node:ekr.20070130154139:headWidth
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
    
        # try:
            # w.configure(state="disabled",highlightthickness=0,fg=fg,bg=bg,
                # selectbackground=bg,selectforeground=fg,highlightbackground=bg)
        # except:
            # g.es_exception()
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
    #@-others
#@nonl
#@-node:edream.111603213219:wxLeoTree class
#@+node:ekr.20070209074655:Text widgets
#@<< baseTextWidget class >>
#@+node:ekr.20070209074555:<< baseTextWidget class >> (to do: better repr)
class baseTextWidget:

    '''The base class for all wrapper classes for the Tk.Text widget.'''
        
    #@    @+others
    #@+node:ekr.20070209074555.1:Birth & special methods (baseText)
    def __init__ (self,parent,textBaseClass,*args,**keys):
        
        w = self
        
        self.textBaseClass = textBaseClass
        self.isRichText = textBaseClass == wx.richtext.RichTextCtrl
        self.name = keys.get('name')
        if self.isRichText: del keys['name']
    
        textBaseClass.__init__(self,parent,id=-1,*args,**keys)
        
          # Make sure there are no conflicts with base-class attributes.
        attribs = (
            'allowSyntaxColoring',
            'defaultAttrib','defaultFont','defaultStyle',
            'virtualInsertPoint')
        for z in attribs: assert not hasattr(self,z)
        
        self.defaultFont = font = wx.Font(pointSize=10,
            family = wx.FONTFAMILY_TELETYPE, # wx.FONTFAMILY_ROMAN,
            style  = wx.FONTSTYLE_NORMAL,
            weight = wx.FONTWEIGHT_NORMAL,
        )
        self.allowSyntaxColoring = False
        self.virtualInsertPoint = None
        if w.isRichText:
            pass
        else:
            self.defaultAttrib = wx.TextAttr(font=font)
            self.defaultStyle = w.SetDefaultStyle(w.defaultAttrib)
    
    def __repr__(self):
        return 'baseTextWidget: %s' % (id(self))  ### Should give name of base class.
    #@+node:ekr.20070209074555.2:GetName
    # This may override the base-class GetName method.
    
    def GetName (self):
    
        return self.name
    #@-node:ekr.20070209074555.2:GetName
    #@-node:ekr.20070209074555.1:Birth & special methods (baseText)
    #@+node:ekr.20070209074555.3:Do-nothing
    def update (self,*args,**keys):             pass
    def update_idletasks (self,*args,**keys):   pass
    #@-node:ekr.20070209074555.3:Do-nothing
    #@+node:ekr.20070209074555.4:Index conversion
    #@+node:ekr.20070209074555.5:w.toGuiIndex & toPythonIndex
    def toPythonIndex (self,index):
        
        w = self
    
        if type(index) == type(99):
            return index
        elif index == '1.0':
            return 0
        elif index == 'end':
            return w.GetLastPosition()
        else:
            s = textBaseClass.GetValue(w)
            row,col = index.split('.')
            row,col = int(row),int(col)
            i = g.convertRowColToPythonIndex(s,row-1,col)
            # g.trace(index,row,col,i,g.callers(6))
            return i
    
    toGuiIndex = toPythonIndex
    #@nonl
    #@-node:ekr.20070209074555.5:w.toGuiIndex & toPythonIndex
    #@+node:ekr.20070209074555.6:w.rowColToGuiIndex
    # This method is called only from the colorizer.
    # It provides a huge speedup over naive code.
    
    def rowColToGuiIndex (self,s,row,col):
    
        return g.convertRowColToPythonIndex(s,row,col)    
    #@-node:ekr.20070209074555.6:w.rowColToGuiIndex
    #@-node:ekr.20070209074555.4:Index conversion
    #@+node:ekr.20070209074555.7:Wrapper methods
    #@+node:ekr.20070209081738:May be overridden in subclasses
    #@+at 
    #@nonl
    # The base methods here are the wx.TextCtrl methods,
    # some of which are shared by the wx.richtext.RichTextCtrl's.
    #@-at
    #@nonl
    #@+node:ekr.20070209074555.10:delete
    def delete(self,i,j=None):
    
        w = self
        i = w.toGuiIndex(i)
        if j is None: j = i+ 1
        j = w.toGuiIndex(j)
    
        # g.trace(i,j,len(s),repr(s[:20]))
    
        w.textBaseClass.Replace(w,i,j,'')
    #@-node:ekr.20070209074555.10:delete
    #@+node:ekr.20070209074555.11:deleteTextSelection
    def deleteTextSelection (self):
        
        w = self
    
        i,j = w.getSelectionRange()
        if i == j: return
        
        s = w.getAllText()
        s = s[i:] + s[j:]
        # g.trace(len(s),repr(s[:20]))
        w.textBaseClass.ChangeValue(w,s)
    #@-node:ekr.20070209074555.11:deleteTextSelection
    #@+node:ekr.20070209074555.14:get
    def get(self,i,j=None):
    
        w = self
        i = w.toGuiIndex(i)
        if j is None: j = i+ 1
        j = w.toGuiIndex(j)
        
        s = w.textBaseClass.GetRange(w,i,j)
    
        return g.toUnicode(s,g.app.tkEncoding)
    #@-node:ekr.20070209074555.14:get
    #@+node:ekr.20070209074555.15:getAllText
    def getAllText (self):
        
        w = self
    
        s = w.textBaseClass.GetValue(w)
        
        return g.toUnicode(s,g.app.tkEncoding)
    #@nonl
    #@-node:ekr.20070209074555.15:getAllText
    #@+node:ekr.20070209074555.16:getInsertPoint (WRONG)
    def getInsertPoint(self):
        
        w = self ; i = self.virtualInsertPoint
    
        if i is None:
            i = w.textBaseClass.GetInsertionPoint(w)
        
        # g.trace(i,self.virtualInsertPoint)
        return i
    #@-node:ekr.20070209074555.16:getInsertPoint (WRONG)
    #@+node:ekr.20070209074555.17:getSelectedText
    def getSelectedText (self):
    
        w = self
        
        s = w.textBaseClass.GetStringSelection(w)
    
        return g.toUnicode(s,g.app.tkEncoding)
    #@-node:ekr.20070209074555.17:getSelectedText
    #@+node:ekr.20070209074555.18:getSelectionRange
    def getSelectionRange (self,sort=True):
        
        """Return a tuple representing the selected range of the widget.
        
        Return a tuple giving the insertion point if no range of text is selected."""
    
        # To get the current selection
        w = self
        sel =  w.textBaseClass.GetSelection(w)
        
        # wx.richtext.RichTextCtrl returns (-1,-1) on no selection.
        if len(sel) == 2 and sel[0] >=1 and sel[1] >= 0:
            # g.trace('sel',repr(sel),g.callers(6))
            i,j = sel
            if sort and i > j: i,j = j,i
            return sel
        else:
            # Return the insertion point if there is no selected text.
            i =  w.textBaseClass.GetInsertionPoint(w)
            # g.trace('i',i,g.callers(6))
            return i,i
    #@nonl
    #@-node:ekr.20070209074555.18:getSelectionRange
    #@+node:ekr.20070209074555.20:insert
    # The signature is more restrictive than the Tk.Text.insert method.
    
    def insert(self,i,s):
        
        w = self
        i = w.toPythonIndex(i)
        
        # g.trace(i,s,g.callers(4))
        w.textBaseClass.SetInsertionPoint(w,i)
        w.textBaseClass.WriteText(w,s)
    #@-node:ekr.20070209074555.20:insert
    #@+node:ekr.20070209074555.23:see & seeInsertPoint
    def see(self,index):
    
        w = self
        w.textBaseClass.ShowPosition(w,w.toGuiIndex(index))
    
    def seeInsertPoint(self):
        
        w = self
        w.textBaseClass.ShowPosition(w,w.GetInsertionPoint())
    #@-node:ekr.20070209074555.23:see & seeInsertPoint
    #@+node:ekr.20070209074555.25:setAllText
    def setAllText (self,s):
    
        w = self
    
        w.textBaseClass.Clear(w)
        w.textBaseClass.WriteText(w,s) # Uses style.
    #@-node:ekr.20070209074555.25:setAllText
    #@+node:ekr.20070209074555.26:setInsertPoint
    def setInsertPoint (self,pos):
    
        w = self
        
        self.virtualInsertPoint = i = w.toGuiIndex(pos)
        
        # g.trace('pos',pos,'i',i,g.callers(6))
    
        w.textBaseClass.SetInsertionPoint(w,i)
    #@nonl
    #@-node:ekr.20070209074555.26:setInsertPoint
    #@+node:ekr.20070209074555.27:setSelectionRange
    def setSelectionRange (self,i,j,insert=None):
        
        w = self
        
        i1, j1, insert1 = i,j,insert
        
        i = w.toGuiIndex(i)
        j = w.toGuiIndex(j)
        if insert is not None: insert = w.toGuiIndex(insert)
    
        # g.trace(repr(i1),'=',repr(i),repr(j1),'=',repr(j),repr(insert1),'=',repr(insert),g.callers(4))
        
        if i == j:
            self.virtualInsertPoint = ins = g.choose(insert is None,i,insert)
            w.textBaseClass.SetInsertionPoint(w,ins)
        else:
            if insert is not None: self.virtualInsertPoint = insert
            w.textBaseClass.SetSelection(w,i,j)
    #@-node:ekr.20070209074555.27:setSelectionRange
    #@+node:ekr.20070209080508:tags (to-do)
    #@+node:ekr.20070209074555.21:mark_set (to be removed)
    def mark_set(self,markName,i):
    
        w = self
        i = w.toGuiIndex(i)
        
        ### Tk.Text.mark_set(w,markName,i)
    #@-node:ekr.20070209074555.21:mark_set (to be removed)
    #@+node:ekr.20070209074555.28:tag_add
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
            # g.trace(i,j,tagName)
            w.textBaseClass.SetStyle(w,i,j,style)
    #@nonl
    #@-node:ekr.20070209074555.28:tag_add
    #@+node:ekr.20070209074555.29:tag_configure & helper
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
    #@+node:ekr.20070209074555.30:tkColorToWxColor
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
    #@-node:ekr.20070209074555.30:tkColorToWxColor
    #@-node:ekr.20070209074555.29:tag_configure & helper
    #@+node:ekr.20070209074555.31:tag_delete (NEW)
    def tag_delete (self,tagName,*args,**keys):
        
        pass # g.trace(tagName,args,keys)
    #@nonl
    #@-node:ekr.20070209074555.31:tag_delete (NEW)
    #@+node:ekr.20070209074555.32:tag_names
    def tag_names (self, *args):
        
        return []
    #@-node:ekr.20070209074555.32:tag_names
    #@+node:ekr.20070209074555.33:tag_ranges
    def tag_ranges(self,tagName):
        
        return tuple() ###
        
        w = self
        aList = Tk.Text.tag_ranges(w,tagName)
        aList = [w.toPythonIndex(z) for z in aList]
        return tuple(aList)
    #@-node:ekr.20070209074555.33:tag_ranges
    #@+node:ekr.20070209074555.34:tag_remove
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
            # g.trace(i,j,tagName)
            w.textBaseClass.SetStyle(w,i,j,style)
    #@nonl
    #@-node:ekr.20070209074555.34:tag_remove
    #@+node:ekr.20070209074555.35:yview
    def yview (self,*args):
        
        '''w.yview('moveto',y) or w.yview()'''
    
        return 0,0
    #@nonl
    #@-node:ekr.20070209074555.35:yview
    #@-node:ekr.20070209080508:tags (to-do)
    #@+node:ekr.20070209074555.36:xyToGui/PythonIndex
    def xyToPythonIndex (self,x,y):
        
        w = self
        pos = wx.Point(x.y)
        data = w.textBaseClass.HitTest(pos)
        # g.trace(data)
    #@-node:ekr.20070209074555.36:xyToGui/PythonIndex
    #@-node:ekr.20070209081738:May be overridden in subclasses
    #@+node:ekr.20070209081738.1:Should not be overridden in subclasses
    # These methods are generic and should not need to be over-ridden.
    #@nonl
    #@+node:ekr.20070209074555.8:bind
    def bind (self,kind,*args,**keys):
        
        pass # g.trace('wxLeoText',kind,args[0].__name__)
    #@nonl
    #@-node:ekr.20070209074555.8:bind
    #@+node:ekr.20070209074555.9:clipboard_clear & clipboard_append
    def clipboard_clear (self):
        
        g.app.gui.replaceClipboardWith('')
    
    def clipboard_append(self,s):
        
        s1 = g.app.gui.getTextFromClipboard()
    
        g.app.gui.replaceClipboardWith(s1 + s)
    #@-node:ekr.20070209074555.9:clipboard_clear & clipboard_append
    #@+node:ekr.20070209074555.12:event_generate (to do)
    def event_generate(self,stroke):
        
        pass ## g.trace('wxTextWidget',stroke)
    #@nonl
    #@-node:ekr.20070209074555.12:event_generate (to do)
    #@+node:ekr.20070209074555.13:flashCharacter (to do)
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
    #@-node:ekr.20070209074555.13:flashCharacter (to do)
    #@+node:ekr.20070209074555.19:hasSelection
    def hasSelection (self):
        
        w = self
        i,j = w.getSelectionRange()
        return i != j
    #@-node:ekr.20070209074555.19:hasSelection
    #@+node:ekr.20070209074555.22:replace
    def replace (self,i,j,s):
        
        w = self
    
        w.delete(i,j)
        w.insert(i,s)
    #@-node:ekr.20070209074555.22:replace
    #@+node:ekr.20070209074555.24:selectAllText
    def selectAllText (self,insert=None):
        
        '''Select all text of the widget.'''
        
        w = self
        w.setSelectionRange(0,'end',insert=insert)
    #@-node:ekr.20070209074555.24:selectAllText
    #@-node:ekr.20070209081738.1:Should not be overridden in subclasses
    #@-node:ekr.20070209074555.7:Wrapper methods
    #@-others
#@nonl
#@-node:ekr.20070209074555:<< baseTextWidget class >> (to do: better repr)
#@nl
#@<< wxTextWidget class >>
#@+node:ekr.20061115122034:<< wxTextWidget class >>
class wxTextWidget (baseTextWidget):

    '''The base class of classes using wx.TextCtrl and wx.richtext.RichTextCtrl widgets.'''
        
    #@    @+others
    #@+node:ekr.20061118101058:Birth & special methods (wxLeoTextCtrl)
    def __init__ (self,parent,textBaseClass,*args,**keys):
        
        w = self
        
        self.textBaseClass = textBaseClass
        self.isRichText = textBaseClass == wx.richtext.RichTextCtrl
        self.name = keys.get('name')
        if self.isRichText: del keys['name']
    
        baseTextWidget.__init__(self,parent,textBaseClass,
            id=-1,*args,**keys)
            # Init the base class.
            # Keys must include a proper Leo widget name.
        
          # Make sure there are no conflicts with base-class attributes.
        attribs = (
            'allowSyntaxColoring',
            'defaultAttrib','defaultFont','defaultStyle',
            'virtualInsertPoint')
        for z in attribs: assert not hasattr(self,z)
        
        self.defaultFont = font = wx.Font(pointSize=10,
            family = wx.FONTFAMILY_TELETYPE, # wx.FONTFAMILY_ROMAN,
            style  = wx.FONTSTYLE_NORMAL,
            weight = wx.FONTWEIGHT_NORMAL,
        )
        self.allowSyntaxColoring = False
        self.virtualInsertPoint = None
        if w.isRichText:
            pass
        else:
            self.defaultAttrib = wx.TextAttr(font=font)
            self.defaultStyle = w.SetDefaultStyle(w.defaultAttrib)
    
    def __repr__(self):
        return 'wxTextWidget: %s' % (id(self))
    #@+node:ekr.20070208160058:GetName
    def GetName (self):
        return self.name
    #@-node:ekr.20070208160058:GetName
    #@-node:ekr.20061118101058:Birth & special methods (wxLeoTextCtrl)
    #@+node:ekr.20061115122034.2:Wrapper methods
    #@+node:ekr.20061115122034.3:delete
    def delete(self,i,j=None):
    
        w = self
        i = w.toGuiIndex(i)
        if j is None: j = i+1
        j = w.toGuiIndex(j)
    
        # g.trace(i,j,len(s),repr(s[:20]))
        textBaseClass.Replace(w,i,j,'')
    #@-node:ekr.20061115122034.3:delete
    #@+node:ekr.20061115122034.10:deleteTextSelection
    def deleteTextSelection (self):
        
        w = self
    
        i,j = w.getSelectionRange()
        if i != j:
            s = w.getAllText()
            del s[i:j]
            # g.trace(len(s),repr(s[:20]))
            textBaseClass.ChangeValue(w,s)
    #@-node:ekr.20061115122034.10:deleteTextSelection
    #@+node:ekr.20061115122034.4:get
    def get(self,i,j=None):
    
        w = self
        i = w.toGuiIndex(i)
        if j is None: j = i+ 1
        j = w.toGuiIndex(j)
        
        s = textBaseClass.GetRange(w,i,j)
        return g.toUnicode(s,g.app.tkEncoding)
    #@-node:ekr.20061115122034.4:get
    #@+node:edream.111303093953.18:getAllText
    def getAllText (self):
        
        w = self
        s =  textBaseClass.GetValue(w)
        
        if s is None:
            return u""
        else:
            return g.toUnicode(s,g.app.tkEncoding)
    #@nonl
    #@-node:edream.111303093953.18:getAllText
    #@+node:edream.111303093953.9:getInsertPoint
    def getInsertPoint(self):
        
        w = self ; i = self.virtualInsertPoint
    
        if i is None:
            i = textBaseClass.GetInsertionPoint(w)
        
        # g.trace(i,self.virtualInsertPoint)
        return i
    #@-node:edream.111303093953.9:getInsertPoint
    #@+node:ekr.20061115122034.14:getSelectedText
    def getSelectedText (self): # tkTextWidget.
    
        w = self
        
        s = textBaseClass.GetStringSelection(w)
        return g.toUnicode(s,g.app.tkEncoding)
    #@-node:ekr.20061115122034.14:getSelectedText
    #@+node:edream.111303093953.13:getSelectionRange
    def getSelectionRange (self,sort=True):
        
        """Return a tuple representing the selected range of the widget.
        
        Return a tuple giving the insertion point if no range of text is selected."""
    
        # To get the current selection
        w = self
        sel =  textBaseClass.GetSelection(w)
        
        # wx.richtext.RichTextCtrl returns (-1,-1) on no selection.
        if len(sel) == 2 and sel[0] >=1 and sel[1] >= 0:
            # g.trace('sel',repr(sel),g.callers(6))
            i,j = sel
            if sort and i > j: i,j = j,i
            return sel
        else:
            # Return the insertion point if there is no selected text.
            i =  textBaseClass.GetInsertionPoint(w)
            # g.trace('i',i,g.callers(6))
            return i,i
    #@nonl
    #@-node:edream.111303093953.13:getSelectionRange
    #@+node:ekr.20061115122034.5:insert
    # The signature is more restrictive than the Tk.Text.insert method.
    
    def insert(self,i,s):
        
        w = self
        i = w.toPythonIndex(i)
        
        # g.trace(i,s,g.callers(4))
        textBaseClass.SetInsertionPoint(w,i)
        textBaseClass.WriteText(w,s)
    #@-node:ekr.20061115122034.5:insert
    #@+node:edream.111303093953.25:see & seeInsertPoint
    def see(self,index):
    
        w = self
        textBaseClass.ShowPosition(w,w.toGuiIndex(index))
    
    def seeInsertPoint(self):
        
        w = self
        textBaseClass.ShowPosition(w,w.GetInsertionPoint())
    #@-node:edream.111303093953.25:see & seeInsertPoint
    #@+node:ekr.20061115122034.19:setAllText
    def setAllText (self,s):
    
        w = self
        textBaseClass.Clear(w)
        textBaseClass.WriteText(w,s) # Uses style.
    #@-node:ekr.20061115122034.19:setAllText
    #@+node:edream.111303093953.10:setInsertPoint
    def setInsertPoint (self,pos):
    
        w = self
        
        self.virtualInsertPoint = i = w.toGuiIndex(pos)
        
        # g.trace('pos',pos,'i',i,g.callers(6))
    
        textBaseClass.SetInsertionPoint(w,i)
    #@nonl
    #@-node:edream.111303093953.10:setInsertPoint
    #@+node:edream.111303093953.16:setSelectionRange
    def setSelectionRange (self,i,j,insert=None):
        
        w = self
        
        i1, j1, insert1 = i,j,insert
        
        i = w.toGuiIndex(i)
        j = w.toGuiIndex(j)
        if insert is not None: insert = w.toGuiIndex(insert)
    
        # g.trace(repr(i1),'=',repr(i),repr(j1),'=',repr(j),repr(insert1),'=',repr(insert),g.callers(4))
        
        if i == j:
            self.virtualInsertPoint = ins = g.choose(insert is None,i,insert)
            textBaseClass.SetInsertionPoint(w,ins)
        else:
            if insert is not None: self.virtualInsertPoint = insert
            textBaseClass.SetSelection(w,i,j)
    #@-node:edream.111303093953.16:setSelectionRange
    #@+node:ekr.20070130185224:yview (to do)
    def yview (self,*args):
        
        '''w.yview('moveto',y) or w.yview()'''
    
        return 0,0
    #@nonl
    #@-node:ekr.20070130185224:yview (to do)
    #@+node:ekr.20061115122034.24:xyToGui/PythonIndex (to do)
    def xyToPythonIndex (self,x,y):
        
        w = self
        pos = wx.Point(x.y)
        data = textBaseClass.HitTest(pos)
        # g.trace(data)
    #@-node:ekr.20061115122034.24:xyToGui/PythonIndex (to do)
    #@-node:ekr.20061115122034.2:Wrapper methods
    #@-others
#@nonl
#@-node:ekr.20061115122034:<< wxTextWidget class >>
#@nl
#@+others
#@+node:ekr.20070125074101:headlineWidget class (baseTextWidget)
class headlineWidget (baseTextWidget):
    
    '''A class to make a wxWidgets headline look like a plainTextWidget.'''
    
    #@    @+others
    #@+node:ekr.20070125074101.2:Birth & special methods
    def __init__ (self,treeCtrl,id):
    
        self.tree = treeCtrl
        self.init(id)
        
    def init (self,id):
        self.id = id
        self.ins = 0
        self.sel = 0,0
    
    def __repr__(self):
        return 'headlineWidget: %s' % (id(self))
    #@-node:ekr.20070125074101.2:Birth & special methods
    #@+node:ekr.20070125075903:Do-nothing methods
    def bind (self,kind,*args,**keys):              pass
    
    def cget (self,*args,**keys):                   pass
    def configure (self,*args,**keys):              pass
    
    def mark_set(self,markName,i):                  pass
    
    def see (self,index):                           pass
    def seeInsertPoint (self):                      pass
    
    def tag_add (self,tagName,i,j=None,*args):      pass
    def tag_configure (self,colorName,**keys):      pass
    def tag_delete (self,tagName,*args,**keys):     pass
    def tag_ranges (self,tagName):                   return (0,0)
    def tag_remove (self,tagName,i,j=None,*args):   pass
    
    def update (self,*args,**keys):                 pass
    def update_idletasks (self,*args,**keys):       pass
    #@nonl
    #@-node:ekr.20070125075903:Do-nothing methods
    #@+node:ekr.20070125074101.3:Index conversion
    #@+node:ekr.20070125074101.4:w.toGuiIndex & toPythonIndex
    # This plugin uses Python indices everywhere.
    
    def toPythonIndex (self,index):
        
        w = self ; id = w.id ; tree = w.tree
    
        if type(index) == type(99):
            return index
        elif index == '1.0':
            return 0
        elif index == 'end':
            s = tree.GetItemText(id)
            return len(s)
        else:
            s = tree.GetItemText(id)
            g.trace(index,g.callers())
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
    #@+node:ekr.20070130155154:event_generate
    def event_generate(self,stroke):
        
        g.trace('wxTextWidget',stroke)
    #@-node:ekr.20070130155154:event_generate
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
    
        s = w.tree.GetItemText(w.id)
    
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
        w.tree.SetItemText(w.id,s)
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
#@-node:ekr.20070125074101:headlineWidget class (baseTextWidget)
#@+node:ekr.20070209092215:plainTextWidget (wxTextWidget)
class plainTextWidget (wxTextWidget):
    
    '''A class wrapping wx.TextCtrl widgets.'''
    
    #@    @+others
    #@-others
#@nonl
#@-node:ekr.20070209092215:plainTextWidget (wxTextWidget)
#@+node:ekr.20070209092215.1:richTextWidget (wxTextWidget)
class richTextWidget (wxTextWidget):
    
    '''A class wrapping wx.richtext.RichTextCtrl widgets.'''
    
    #@    @+others
    #@-others
#@nonl
#@-node:ekr.20070209092215.1:richTextWidget (wxTextWidget)
#@+node:ekr.20070205140140:stcWidget (baseTextWidget)
class stcWidget (baseTextWidget): # (wx.stc.StyledTextCtrl):
    
    '''A class to wrap the Tk.Text widget.
    Translates Python (integer) indices to and from Tk (string) indices.
    
    This class inherits almost all tkText methods: you call use them as usual.'''
    
    # The signatures of tag_add and insert are different from the Tk.Text signatures.
    __pychecker__ = '--no-override' # suppress warning about changed signature.
        
    # Note: this widget inherits the GetName method from the wxWindow class.
        
    #@    @+others
    #@+node:ekr.20070205140140.1:Birth & special methods
    def __init__ (self,parent,*args,**keys):
        
        w = self
    
        baseTextWidget.__init__(self,parent,wx.stc.StyledTextCtrl,
            id=-1,*args,**keys)
            # Init the base class.
            # Keys must include a proper Leo widget name.
    
        w.SetIndent(4) ### Should be variable.
        w.SetIndentationGuides(True)
    
    def __repr__(self):
        return 'wxLeoStcWidget: %s' % (id(self))
    #@-node:ekr.20070205140140.1:Birth & special methods
    #@+node:ekr.20070209080938.2:Wrapper methods
    #@+node:ekr.20070209080938.5:delete
    def delete(self,i,j=None):
    
        w = self
        i = w.toGuiIndex(i)
        if j is None: j = i+1
        j = w.toGuiIndex(j)
    
        # g.trace(i,j,len(s),repr(s[:20]))
        s = w.getAllText()
        s = s[:i] + s[j:]
    
        wx.stc.StyledTextCtrl.SetText(w,s)
        w.setInsertPoint(i)
     
    #@-node:ekr.20070209080938.5:delete
    #@+node:ekr.20070209080938.6:deleteTextSelection
    def deleteTextSelection (self):
        
        w = self
        s = w.getAllText()
        ins = w.getInsertPoint()
        i,j = w.getSelectionRange()
        # g.trace(i,j,repr(s[i:j]))
        if i != j:
            s = s[:i] + s[j:]
            w.setAllText(s)
    #@-node:ekr.20070209080938.6:deleteTextSelection
    #@+node:ekr.20070209080938.9:get
    def get(self,i,j=None):
    
        w = self
        i = w.toGuiIndex(i)
        if j is None: j = i+ 1
        j = w.toGuiIndex(j)
        
        s = wx.stc.StyledTextCtrl.GetTextRange(w,i,j)
        
        return g.toUnicode(s,g.app.tkEncoding)
    #@-node:ekr.20070209080938.9:get
    #@+node:ekr.20070209080938.10:getAllText
    def getAllText (self):
        
        w = self
        s = wx.stc.StyledTextCtrl.GetText(w)
        
        if s is None:
            return u""
        else:
            return g.toUnicode(s,g.app.tkEncoding)
    #@nonl
    #@-node:ekr.20070209080938.10:getAllText
    #@+node:ekr.20070209080938.11:getInsertPoint
    def getInsertPoint(self):
        
        w = self
        
        return  wx.stc.StyledTextCtrl.GetCurrentPos(w)
    #@-node:ekr.20070209080938.11:getInsertPoint
    #@+node:ekr.20070209080938.12:getSelectedText
    def getSelectedText (self): # tkTextWidget.
    
        w = self
        
        s = w.getAllText()
        i,j = wx.stc.StyledTextCtrl.GetSelection(w)
        s = s[i:j]
        # g.trace(repr(s))
        return g.toUnicode(s,g.app.tkEncoding)
    #@-node:ekr.20070209080938.12:getSelectedText
    #@+node:ekr.20070209080938.13:getSelectionRange
    def getSelectionRange (self,sort=True):
        
        """Return a tuple representing the selected range of the widget.
        
        Return a tuple giving the insertion point if no range of text is selected."""
    
        # To get the current selection
        w = self
        sel =  wx.stc.StyledTextCtrl.GetSelection(w)
        # g.trace('sel',repr(sel),g.callers(6))
        if len(sel) == 2:
            i,j = sel
            if sort and i > j: i,j = j,i
            sel = i,j
            return sel
        else:
            # Return the insertion point if there is no selected text.
            i =  wx.stc.StyledTextCtrl.GetInsertionPoint(w)
            return i,i
    #@nonl
    #@-node:ekr.20070209080938.13:getSelectionRange
    #@+node:ekr.20070209080938.15:insert
    # The signature is more restrictive than the Tk.Text.insert method.
    
    def insert(self,i,s):
        
        w = self
        i = w.toPythonIndex(i)
        wx.stc.StyledTextCtrl.InsertText(w,i,s)
        w.setInsertPoint(i)
    #@-node:ekr.20070209080938.15:insert
    #@+node:ekr.20070209080938.18:see & seeInsertPoint
    def see(self,index):
    
        w = self
        s = w.getAllText()
        row,col = g.convertPythonIndexToRowCol(s,index)
        wx.stc.StyledTextCtrl.ScrollToLine(w,row)
    
    def seeInsertPoint(self):
        
        w = self
        s = w.getAllText()
        i = w.getInsertPoint()
        row,col = g.convertPythonIndexToRowCol(s,i)
        wx.stc.StyledTextCtrl.ScrollToLine(w,row)
    #@-node:ekr.20070209080938.18:see & seeInsertPoint
    #@+node:ekr.20070209080938.20:setAllText
    def setAllText (self,s):
    
        w = self
        wx.stc.StyledTextCtrl.SetText(w,s)
    
    #@-node:ekr.20070209080938.20:setAllText
    #@+node:ekr.20070209080938.21:setInsertPoint
    def setInsertPoint (self,pos):
    
        w = self
        
        # g.trace('pos',pos,g.callers(6))
        i = w.toGuiIndex(pos)
        wx.stc.StyledTextCtrl.SetSelection(w,i,i)
    #@-node:ekr.20070209080938.21:setInsertPoint
    #@+node:ekr.20070209080938.22:setSelectionRange
    def setSelectionRange (self,i,j,insert=None):
        
        w = self
        i1,j1=i,j
        
        # if g.app.unitTesting: g.pdb()
    
        i = w.toGuiIndex(i)
        j = w.toGuiIndex(j)
        if insert is not None: insert = w.toGuiIndex(insert)
        
        # g.trace(i1,j1,'=',i,j,insert,repr(w))
    
        # Apparently, both parts of the selection must be set at once.  Yet another bug.
        if insert in (None,j):
            wx.stc.StyledTextCtrl.SetSelection(w,i,j)
        else:
            wx.stc.StyledTextCtrl.SetSelection(w,j,i)
    #@nonl
    #@-node:ekr.20070209080938.22:setSelectionRange
    #@+node:ekr.20070209080938.30:yview (to do)
    def yview (self,*args):
        
        '''w.yview('moveto',y) or w.yview()'''
    
        return 0,0
    #@nonl
    #@-node:ekr.20070209080938.30:yview (to do)
    #@+node:ekr.20070209080938.31:xyToGui/PythonIndex (to do)
    def xyToPythonIndex (self,x,y):
        
        w = self
        pos = wx.Point(x.y)
    
        data = wx.stc.StyledTextCtrl.HitTest(pos)
        # g.trace(data)
    #@-node:ekr.20070209080938.31:xyToGui/PythonIndex (to do)
    #@-node:ekr.20070209080938.2:Wrapper methods
    #@-others
#@nonl
#@-node:ekr.20070205140140:stcWidget (baseTextWidget)
#@-others
#@nonl
#@-node:ekr.20070209074655:Text widgets
#@-others
#@-node:edream.110203113231.302:@thin __wx_gui.py
#@-leo
