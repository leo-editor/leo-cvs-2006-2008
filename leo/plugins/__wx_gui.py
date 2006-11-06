# -*- coding: utf-8 -*-
#@+leo-ver=4-thin
#@+node:edream.110203113231.302:@thin __wx_gui.py
#@@first

"""A plugin to use wxPython as Leo's gui."""

__version__ = '0.5' # Start of development with Leo 4.4.2 code base and wxWidgets 2.6.3
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
import leoMenu
import leoNodes
import leoUndo

import os
import sys
import traceback

try:
    import wx
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
#@+node:ekr.20050719111045.1:init
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
#@-node:ekr.20050719111045.1:init
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
    #@nonl
    #@-node:edream.110203113231.307: wxGui.__init__
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
    
       pass
        
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
    
        g.trace('wx gui')
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
    #@+node:edream.111303090930:app.gui.wx utils
    #@+node:edream.110203113231.320:Clipboard
    def replaceClipboardWith (self,s):
    
        cb = wx.TheClipboard
        if cb.Open():
            cb.Clear()
            cb.SetData(s)
            cb.Flush()
            cb.Close()
        
    def getTextFromClibboard (self):
        
        return None
        
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
    #@+node:edream.110203113231.335:Focus (wxGui) (to do)
    #@+node:edream.110203113231.336:get_focus
    def get_focus(self,top):
        
        """Returns the widget that has focus, or body if None."""
    
        pass # wx code not ready yet.
    #@nonl
    #@-node:edream.110203113231.336:get_focus
    #@+node:edream.110203113231.337:set_focus
    def set_focus(self,c,widget):
        
        """Set the focus of the widget in the given commander if it needs to be changed."""
        
        pass # wx code not ready yet.
    #@nonl
    #@-node:edream.110203113231.337:set_focus
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
        
        g.trace(w)
    
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
    #@+node:edream.111303093953.8:Insert Point
    #@+node:edream.111303093953.9:getInsertPoint
    def getInsertPoint(self,t,python=False):
        
        # The python arg is ignored.
    
        if t:
            t.GetInsertionPoint()
        else:
            return 0
    #@nonl
    #@-node:edream.111303093953.9:getInsertPoint
    #@+node:edream.111303093953.10:setInsertPoint
    def setInsertPoint (self,t,pos,python=False):
        
        # The python arg is ignored.
    
        if t and pos: # s_text control doesn't exist.
            g.trace(pos)
            t.bodyCtrl.SetInsertionPoint(pos)
    #@nonl
    #@-node:edream.111303093953.10:setInsertPoint
    #@-node:edream.111303093953.8:Insert Point
    #@+node:edream.111303093953.11:Selection
    #@+node:edream.111303093953.13:getSelectionRange
    def getSelectionRange (self,t):
        
        """Return a tuple representing the selected range of t, a Tk.Text widget.
        
        Return a tuple giving the insertion point if no range of text is selected."""
    
        # To get the current selection
        sel = t.bodyCtrl.GetSelection()
        if len(sel) == 2:
            return sel
        else:
            # Return the insertion point if there is no selected text.
            insert = t.bodyCtrl.GetInsertionPoint()
            return insert,insert
    #@nonl
    #@-node:edream.111303093953.13:getSelectionRange
    #@+node:edream.111303093953.14:setSelectionRange
    def setSelectionRange(self,t,n1,n2):
    
        if t and n1 and n2:
            g.trace(n1,n2)
            t.bodyCtrl.SetSelection(n1,n2)
    #@nonl
    #@-node:edream.111303093953.14:setSelectionRange
    #@+node:edream.111303093953.15:setSelectionRangeWithLength
    def setSelectionRangeWithLength(self,t,start,length):
        
        t.bodyCtrl.SetSelection(n1,start+length)
    #@nonl
    #@-node:edream.111303093953.15:setSelectionRangeWithLength
    #@+node:edream.111303093953.16:setSelectionRange
    def setSelectionRange (self,t,start,end):
    
        if not start or not end:
            return
            
        if start > end:
            start,end = end,start
            
        t.bodyCtrl.SetSelection(start,end)
    #@nonl
    #@-node:edream.111303093953.16:setSelectionRange
    #@-node:edream.111303093953.11:Selection
    #@+node:edream.111303093953.17:Text
    #@+node:edream.111303093953.18:getAllText
    def getAllText (self,t):
        
        """Return all the text of Tk.Text t converted to unicode."""
        
        s = t.get("1.0","end")
        if s is None:
            return u""
        else:
            return g.toUnicode(s,g.app.tkEncoding)
    #@nonl
    #@-node:edream.111303093953.18:getAllText
    #@+node:edream.111303093953.23:replaceSelectionRangeWithText
    def replaceSelectionRangeWithText (self,t,start,end,text):
    
        t.delete(start,end)
        t.insert(start,text)
    #@nonl
    #@-node:edream.111303093953.23:replaceSelectionRangeWithText
    #@-node:edream.111303093953.17:Text
    #@+node:edream.111303093953.24:Visibility
    #@+node:edream.111303093953.25:see
    def see(self,t,index):
    
        if t and index:
            t.bodyCtrl.ShowPosition(index)
    #@-node:edream.111303093953.25:see
    #@-node:edream.111303093953.24:Visibility
    #@+node:ekr.20061105125717:toGuiIndex & toPythonIndex
    # This plugin uses Python indices everywhere, so these can be do-nothings.
    
    def toGuiIndex (self,s,w,index):
        
        return index
    
    def toPythonIndex (self,s,w,index):
    
        return index
    #@-node:ekr.20061105125717:toGuiIndex & toPythonIndex
    #@-node:edream.111303090930:app.gui.wx utils
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
    #@+node:edream.110203113231.541:wxLeoBody.__init__
    def __init__ (self,frame,parentFrame):
    
        # Init the base class: calls createControl.
        leoFrame.leoBody.__init__(self,frame,parentFrame)
        
        self.bodyCtrl = self.createControl(frame,parentFrame)
    
        self.colorizer = leoColor.colorizer(self.c)
    
        self.styles = {} # For syntax coloring.
    
        wx.EVT_TEXT(self.bodyCtrl,const("cBodyCtrl"),self.onBodyTextUpdated)
    #@nonl
    #@-node:edream.110203113231.541:wxLeoBody.__init__
    #@+node:edream.110203113231.542:wxLeoBody.createControl
    def createControl (self,frame,parentFrame):
        
        ctrl = wx.TextCtrl(parentFrame,
                const("cBodyCtrl"), "",
                wx.DefaultPosition, wx.DefaultSize,
                wx.TE_RICH | wx.TE_RICH2 | wx.TE_MULTILINE)
    
        return ctrl
    #@nonl
    #@-node:edream.110203113231.542:wxLeoBody.createControl
    #@-node:edream.110203113231.540:Birth & death (wxLeoBody)
    #@+node:edream.111303204836:Tk wrappers (wxBody) (much work needed) (some will be removed from Leo's core)
    #@+node:edream.110203113231.543:Bounding box...
    def bbox (self,index):
        
        return self.bodyCtrl.GetClientSizeTuple()  
    #@nonl
    #@-node:edream.110203113231.543:Bounding box...
    #@+node:edream.111303204517:Color tags (wxBody) (to do)
    #@+node:edream.111303205611:tag_add
    def tag_add (self,tagName,index1,index2):
        
        g.trace(tagName,repr(index1),repr(index2),g.callers())
    
        style = self.styles.get(tagName)
        if style:
            self.bodyCtrl.SetStyle(index1,index2,style)
    #@nonl
    #@-node:edream.111303205611:tag_add
    #@+node:edream.111303205611.1:tag_bind
    def tag_bind (self,tagName,event,callback):
        
        # g.trace(tagName,event,callback)
        pass
    #@-node:edream.111303205611.1:tag_bind
    #@+node:edream.111303205611.2:tag_configure & helper
    def tag_configure (self,colorName,**keys):
        
        foreground = keys.get("foreground")
        background = keys.get("background")
    
        fcolor = self.tkColorToWxColor (foreground) or wx.BLACK
        bcolor = self.tkColorToWxColor (background) or wx.WHITE
        # g.trace('%20s %10s %15s %10s %15s' % (colorName,foreground,fcolor,background,bcolor))
        style = wx.TextAttr(fcolor,bcolor)
        self.styles[colorName] = style
    #@nonl
    #@+node:edream.111403082513:tkColorToWxColor
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
    #@-node:edream.111403082513:tkColorToWxColor
    #@-node:edream.111303205611.2:tag_configure & helper
    #@+node:edream.111303205611.3:tag_delete
    def tag_delete(self,tagName):
    
        if tagName == "keyword": # A kludge.
    
            # g.trace(tagName)
            style = wx.TextAttr(wx.BLACK)
            last = self.bodyCtrl.GetLastPosition()
            
            if 1: # This may cause the screen flash.
                self.bodyCtrl.SetStyle(0,last,style)
    #@nonl
    #@-node:edream.111303205611.3:tag_delete
    #@+node:edream.111303205611.4:tag_remove
    def tag_remove (self,tagName,index1,index2):
        
        g.trace(tagName,index1,index2)
        pass
    #@-node:edream.111303205611.4:tag_remove
    #@-node:edream.111303204517:Color tags (wxBody) (to do)
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
    #@+node:edream.111303171218:Insert point (wxBody) (TO BE REMOVED FROM LEO's CORE)
    #@+node:ekr.20060629123738.1:getInsertionPoint & getBeforeInsertionPoint
    def getBeforeInsertionPoint (self):
        g.trace()
        
    def getInsertionPoint (self):
    
        return self.bodyCtrl.GetInsertionPoint()
        
    #@-node:ekr.20060629123738.1:getInsertionPoint & getBeforeInsertionPoint
    #@+node:ekr.20060629123738.3:setInsertionPointTo 
    def setInsertionPoint (self,index):
    
        g.trace(g.callers())
        self.bodyCtrl.SetInsertionPoint(index)
    
    def setInsertPointToEnd (self):
        
        g.trace(g.callers())
        self.bodyCtrl.SetInsertionPointEnd()
        
    def setInsertPointToStartOfLine (self,lineNumber):
        g.trace(g.callers())
    #@nonl
    #@-node:ekr.20060629123738.3:setInsertionPointTo 
    #@-node:edream.111303171218:Insert point (wxBody) (TO BE REMOVED FROM LEO's CORE)
    #@+node:edream.111303204025.5:getImageIndex (wxBody) (to do)
    def getImageIndex (self,image):
        
        g.trace(image)
    #@nonl
    #@-node:edream.111303204025.5:getImageIndex (wxBody) (to do)
    #@+node:edream.111303171218.1:Selection
    
    
    
    
    #@+node:ekr.20060629124102.1:deleteSelection
    def deleteSelection (self):
        t = self.bodyCtrl
        t.Remove(t.GetSelection())
    #@nonl
    #@-node:ekr.20060629124102.1:deleteSelection
    #@+node:ekr.20060629125105:getSelectedText
    def getSelectedText (self):
        
        """Return the selected text of the body frame, converted to unicode."""
        
        start, end = self.bodyCtrl.GetSelection()
        # g.trace(start,end)
    
        if start is not None and end is not None and start != end:
            s = self.bodyCtrl.GetRange(start,end)
            if s:
                return g.toUnicode(s,g.app.tkEncoding)
            else:
                return u''
        else:
            return u''
    #@nonl
    #@-node:ekr.20060629125105:getSelectedText
    #@+node:ekr.20060629124102.2:getSelectionRange
    def getSelectionRange (self):
        
        """Return a tuple representing the selected range of body text.
        
        Return a tuple giving the insertion point if no range of text is selected."""
    
        return self.bodyCtrl.GetSelection()
    #@nonl
    #@-node:ekr.20060629124102.2:getSelectionRange
    #@+node:ekr.20060629124102.3:hasTextSelection
    def hasTextSelection (self):
        start,end = self.bodyCtrl.GetSelection()
        return start != end
    #@nonl
    #@-node:ekr.20060629124102.3:hasTextSelection
    #@+node:ekr.20060629124102.4:selectAllText
    def selectAllText (self):
    
        self.bodyCtrl.SetSelection(-1,-1)
    #@nonl
    #@-node:ekr.20060629124102.4:selectAllText
    #@+node:ekr.20060629124102.5:setSelectionRange
    def setSelectionRange (self,sel):
    
        self.bodyCtrl.SetSelection(sel)
    #@nonl
    #@-node:ekr.20060629124102.5:setSelectionRange
    #@-node:edream.111303171218.1:Selection
    #@+node:edream.111303171238:Text
    # These routines replace most of the former insert/delete and index routines.
    #@nonl
    #@+node:edream.111303171238.1:delete... (untested)
    def deleteAllText(self):
        self.bodyCtrl.Clear()
        
    def deleteCharacter (self,index):
        self.bodyCtrl.Remove(index,index+1)
        
    def deleteLine (self,lineNumber): # zero based line number.
        t = self.bodyCtrl
        pos1 = t.XYToPosition(lineNumber)
        n = t.GetLineLength(lineNumber)
        t.Remove(pos1,pos1 + n)
    
    def deleteLines (self,lineNumber,numberOfLines): # zero based line number.
        t = self.bodyCtrl
        pos1 = t.XYToPosition(lineNumber)
        pos2 = t.XYToPosition(lineNumber+numberOfLine-1)
        n = t.GetLineLength(lineNumber+numberOfLine-1)
        t.Remove(pos1,pos2 + n)
    
    def deleteRange (self,index1,index2):
        self.bodyCtrl.Remove(index1,index2)
    #@nonl
    #@-node:edream.111303171238.1:delete... (untested)
    #@+node:edream.111303171238.2:get... (wxBody) (some to be deleted from Leo's core)
    def getAllText (self):
        return self.bodyCtrl.GetValue()
        
    def getTextRange(self,n1,n2):
        return self.bodyCtrl.GetRange(n1,n2)
        
    if 0: # To be deleted from Leo's core
        
        def getCharAtIndex (self,index):
            return self.bodyCtrl.GetRange(index,index+1)
        
        def getInsertLines (self):
            g.trace()
        
        def getSelectionAreas (self):
            g.trace()
        
        def getSelectionLines (self):
            g.trace()
    #@-node:edream.111303171238.2:get... (wxBody) (some to be deleted from Leo's core)
    #@+node:edream.111303171238.3:insert... (wxBody) (to be deleted from Leo's core)
    def insertAtEnd (self,s):
    
        return self.bodyCtrl.AppendText(s)
        
    def insertAtInsertPoint (self,s):
        
        self.bodyCtrl.WriteText(s)
    #@nonl
    #@-node:edream.111303171238.3:insert... (wxBody) (to be deleted from Leo's core)
    #@+node:edream.111303171238.4:setSelectionAreas (wxBody) (to be deleted from Leo's core)
    def setSelectionAreas (self,before,sel,after):
    
        g.trace()
    #@nonl
    #@-node:edream.111303171238.4:setSelectionAreas (wxBody) (to be deleted from Leo's core)
    #@-node:edream.111303171238:Text
    #@+node:edream.110203113231.552:Visibility & scrolling... (wxBody) (to do)
    def see (self,index):
        self.bodyCtrl.ShowPosition()
        
    # def setFirstVisibleIndex (self,index):
        # g.trace()
        # 
    # def getFirstVisibleIndex (self):
        # g.trace()
        
    def scrollUp (self):
        g.trace()
        
    def scrollDown (self):
        g.trace()
    #@nonl
    #@-node:edream.110203113231.552:Visibility & scrolling... (wxBody) (to do)
    #@-node:edream.111303204836:Tk wrappers (wxBody) (much work needed) (some will be removed from Leo's core)
    #@+node:edream.110203113231.275:onBodyTextUpdated MORE WORK NEEDED
    def onBodyTextUpdated(self,event):
    
        frame = self.frame ; c = self.c
        if not c:  return
        p = c.currentPosition()
        if not p: return
        if self.frame.lockout > 0: return
        
        # Similar to idle_body_key
        self.frame.lockout += 1
    
        s = frame.body.bodyCtrl.GetValue()
        p.v.t.setTnodeText(s)
        p.v.t.insertSpot = c.frame.body.getInsertionPoint()
        #@    << recolor the body >>
        #@+node:edream.111303201144.6:<< recolor the body >>
        if 0:  ### Not ready yet.
            self.frame.scanForTabWidth(p)
        
            incremental = undoType not in ("Cut","Paste") and not self.forceFullRecolorFlag
            self.frame.body.recolor_now(p,incremental=incremental)
            
            self.forceFullRecolorFlag = False
        #@nonl
        #@-node:edream.111303201144.6:<< recolor the body >>
        #@nl
        if not c.changed:
            c.setChanged(True)
        #@    << redraw the screen if necessary >>
        #@+node:edream.111303201144.7:<< redraw the screen if necessary >>
        redraw_flag = False
        
        c.beginUpdate()
        
        # Update dirty bits.
        if not p.isDirty() and p.setDirty(): # Sets all cloned and @file dirty bits
            redraw_flag = True
            
        # Update icons.
        val = p.computeIcon()
        
        # During unit tests the node may not have been drawn,
        # so p.v.iconVal may not exist yet.
        if not hasattr(p.v,"iconVal") or val != p.v.iconVal:
            p.v.iconVal = val
            redraw_flag = True
        
        c.endUpdate(redraw_flag) # redraw only if necessary
        #@nonl
        #@-node:edream.111303201144.7:<< redraw the screen if necessary >>
        #@nl
        if 0: # ch, etc. are not defined.
            g.doHook("bodykey2",c=c,p=p,v=p.v,ch=ch,oldSel=oldSel,undoType=undoType)
            
        self.frame.lockout -= 1
    #@nonl
    #@-node:edream.110203113231.275:onBodyTextUpdated MORE WORK NEEDED
    #@-others
#@nonl
#@-node:edream.110203113231.539:wxLeoBody class
#@+node:edream.110203113231.349:wxLeoFrame class
class wxLeoFrame(wx.Frame,leoFrame.leoFrame):
        
    """A class to create a wxPython from for the main Leo window."""

    #@    @+others
    #@+node:edream.110203113231.350:Birth & death (wxLeoFrame)
    #@+node:edream.110203113231.266:__init__
    def __init__ (self,title):
        
        # Init the leoFrame base class.
        # We will init the wxFrame base class in finishCreate.
        leoFrame.leoFrame.__init__(self,g.app.gui)
        
        self.c = None # set in finishCreate.
        self.bodyCtrl = None # set in finishCreate
        self.title = title
        
        # g.trace("wxLeoFrame",title)
        self.activeFrame = None
        self.iconBar = None
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
        self.use_coloring = False # set True to enable coloring
        
        # These vars have corresponding getters/setters.
        if 0: # now defined in base tree class.
            self.mDragging = False
            self.mRootVnode = None
            self.mTopVnode = None
            self.mCurrentVnode = None
    #@nonl
    #@-node:edream.110203113231.266:__init__
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
        
        # Init the wxFrame base class.  The leoFrame base class has already been inited.
        wx.Frame.__init__(self, None, -1, self.title) # wx.NO_3D # hangs.
        #self.outerPanel = wx.Panel(self,-1)
        #self.iconPanel = wx.Panel(self.outerPanel, -1, "iconPanel")
    
        self.CreateStatusBar()
        #@    << create the splitters >>
        #@+node:edream.110203113231.261:<< create the splitters >>
        self.splitter1 = wx.SplitterWindow(self,
            const("cSplitterWindow"),
            wx.DefaultPosition, wx.DefaultSize,
            wx.SP_NOBORDER)
        
        # No effect, except to create a red flash.
        if 0:
            self.splitter1.SetForegroundColour(wx.RED)
            self.splitter1.SetBackgroundColour(wx.RED)
        
        self.splitter2 = wx.SplitterWindow(self.splitter1, -1,
            wx.DefaultPosition, wx.DefaultSize,
            wx.SP_NOBORDER)
            # wx.SP_BORDER | wx.SP_3D, "splitterWindow");
        
        self.splitter1.SetMinimumPaneSize(4)
        self.splitter2.SetMinimumPaneSize(4)
        #@nonl
        #@-node:edream.110203113231.261:<< create the splitters >>
        #@nl
        frame.tree = wxLeoTree(frame,self.splitter2)
        frame.log = wxLeoLog(frame,self.splitter2)
        frame.body = wxLeoBody(frame,self.splitter1)
        frame.bodyCtrl = frame.body
        g.app.setLog(frame.log) # writeWaitingLog hangs without this(!)
    
        # Attach the controls to the splitter.
        self.splitter1.SplitHorizontally(self.splitter2,self.body.bodyCtrl,0)
        self.splitter2.SplitVertically(self.tree.treeCtrl,self.log.logCtrl,cSplitterWidth/2)
        
        self.menu = wxLeoMenu(frame)
        ###self.menu.createMenuBar()
        
        #@    << set the window icon >>
        #@+node:edream.110203113231.265:<< set the window icon >>
        if wx.Platform == "__WXMSW__":
        
            path = os.path.join(g.app.loadDir,"..","Icons","LeoApp16.ico")
            icon = wx.Icon(path,wx.BITMAP_TYPE_ICO,16,16)
            self.SetIcon(icon)
        #@-node:edream.110203113231.265:<< set the window icon >>
        #@nl
        #@    << declare event handlers for frame >>
        #@+node:edream.110203113231.264:<< declare event handlers for frame >>
        if wx.Platform == "__WXMSW__": # Activate events exist only on Windows.
            wx.EVT_ACTIVATE(self,self.onActivate)
        else:
            wx.EVT_SET_FOCUS(self,self.OnSetFocus)
        
        wx.EVT_CLOSE(self,self.onCloseLeoFrame)
        
        wx.EVT_MENU_OPEN(self,self.updateAllMenus) 
        
        if 0: # Causes problems at present.  The screen isn't drawn properly.
            wx.EVT_SIZE(self,self.onResize)
        #@nonl
        #@-node:edream.110203113231.264:<< declare event handlers for frame >>
        #@nl
        
        if 0: # Not ready yet...
            self.App.SetTopWindow(self.Frame)
            self.Frame.Show(True)
            if not g.app.root:
                g.app.root = self.Frame
                
        self.colorizer = self.body.colorizer
                
        c.initVersion()
        self.signOnWithVersion()
        
        self.injectCallbacks()
    
        # Add the frame to the global window list.
        g.app.windowList.append(self)
        self.tree.redraw()
        self.Show(True) # required on some platforms: a cross-platform bug.
    #@nonl
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
    #@+node:edream.111503213533:destroySelf
    def destroySelf(self):
        
        self.Destroy()
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
    
    def get_window_info (self):
        """Return the window information."""
        return g.app.gui.get_window_info(self)
    
    def resizePanesToRatio(self,ratio1,ratio2):
        pass
    
    def setInitialWindowGeometry (self):
        pass
    
    def setTopGeometry (self,w,h,x,y,adjustSize=True):
        pass
    
    def lift (self):
        self.Raise()
    
    def update (self):
        pass
    #@nonl
    #@-node:edream.110203113231.379:wxFrame dummy routines: (to do: minor)
    #@+node:ekr.20061106070956:Icon area methods (to do)
    def addIconButton (self,*args,**keys):
        return self.iconBar and self.iconBar.add(*args,**keys)
    
    def clearIconBar (self):
        if self.iconBar: self.iconBar.clear()
    
    def createIconBar (self):
        f = self ; c = f.c
        if 1: ### Not ready yet.
            return None
        else:
            if not f.iconBar:
                f.iconBar = f.iconBarClass(c,f.outerFrame)
                f.iconFrame = f.iconBar.iconFrame
                f.iconBar.pack()
            return f.iconBar
        
    def getIconBar(self):
        return self.iconBar
    getIconBarObject = getIconBar
    
    def hideIconBar (self):
        if self.iconBar: self.iconBar.hide()
    #@nonl
    #@-node:ekr.20061106070956:Icon area methods (to do)
    #@+node:ekr.20061106070737:Status line (to do)
    def createStatusLine (self):                    pass
    def clearStatusLine (self):                     pass
    def disableStatusLine (self,background=None):   pass
    def enableStatusLine (self,background="white"): pass
    def getStatusLine (self):                       pass
    def putStatusLine (self,s,color=None):          pass
    def setFocusStatusLine (self):                  pass
    def statusLineIsEnabled(self):                  pass
    def updateStatusLine(self):                     pass
        
    # getStatusObject = getStatusLine
    #@-node:ekr.20061106070737:Status line (to do)
    #@+node:edream.110203113231.378:Externally visible routines...
    #@+node:edream.110203113231.380:deiconify
    def deiconify (self):
    
        self.Iconize(False)
    #@nonl
    #@-node:edream.110203113231.380:deiconify
    #@+node:edream.110203113231.381:getTitle
    def getTitle (self):
        
        return self.title
    #@-node:edream.110203113231.381:getTitle
    #@+node:edream.111303135410:setTitle
    def setTitle (self,title):
    
        self.title = title
        self.SetTitle(title) # Call the wx code.
    #@nonl
    #@-node:edream.111303135410:setTitle
    #@-node:edream.110203113231.378:Externally visible routines...
    #@+node:edream.111303100039:Gui-dependent commands (to do)
    #@+node:ekr.20061106070201:Minibuffer commands... (tkFrame)
    
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
    
        g.trace(wname)
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
    #@-node:ekr.20061106070201:Minibuffer commands... (tkFrame)
    #@+node:edream.111303100039.1:Edit Menu...
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
    
        if v and c.edit_widget(v):
            tree.select(v)
    
        if v: # Bug fix 10/9/02: also redraw ancestor headlines.
            # 3/26/03: changed redraw_now to force_redraw.
            tree.force_redraw() # force a redraw of joined headlines.
    
        gui.set_focus(c,c.frame.bodyCtrl) # 10/14/02
    #@nonl
    #@-node:edream.111303101257.1:endEditLabelCommand
    #@+node:edream.111303100039.6:insertHeadlineTime
    def insertHeadlineTime (self,event=None):
        
        g.es("insertHeadlineTime not ready yet")
        return
    
        frame = self ; c = frame.c ; v = c.currentVnode()
        h = v.headString() # Remember the old value.
    
        if c.edit_widget(v):
            sel1,sel2 = g.app.gui.getSelectionRange(c.edit_widget(v))
            if sel1 and sel2 and sel1 != sel2: # 7/7/03
                c.edit_widget(v).delete(sel1,sel2)
            c.edit_widget(v).insert("insert",c.getTime(body=False))
            frame.idle_head_key(v)
    
        # A kludge to get around not knowing whether we are editing or not.
        if h.strip() == v.headString().strip():
            g.es("Edit headline to append date/time")
    #@nonl
    #@-node:edream.111303100039.6:insertHeadlineTime
    #@-node:edream.111303100039.1:Edit Menu...
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
    def toggleActivePane(self,event=None):
        
        # This can't work from the menu...
        
        g.es("toggleActivePane not ready yet")
        return
    
        if self.FindFocus() == self.body.bodyCtrl:
            self.tree.SetFocus()
        else:
            self.body.bodyCtrl.SetFocus()
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
#@-node:edream.110203113231.349:wxLeoFrame class
#@+node:edream.110203113231.553:wxLeoLog class
class wxLeoLog (leoFrame.leoLog):
    
    """The base class for the log pane in Leo windows."""
    
    #@    @+others
    #@+node:edream.110203113231.554:leoLog.__init__
    def __init__ (self,frame,parentFrame):
        
        self.frame = frame
        self.c = frame.c
        self.isNull = False
        self.newlines = 0
    
        self.logCtrl = self.createControl(parentFrame)
        self.setFontFromConfig()
    #@-node:edream.110203113231.554:leoLog.__init__
    #@+node:edream.110203113231.555:leoLog.configure
    def configure (self,*args,**keys):
        
        g.trace(args,keys)
    #@nonl
    #@-node:edream.110203113231.555:leoLog.configure
    #@+node:edream.110203113231.556:leoLog.configureBorder
    def configureBorder(self,border):
        
        g.trace(border)
    #@-node:edream.110203113231.556:leoLog.configureBorder
    #@+node:edream.110203113231.557:leoLog.createControl
    def createControl (self,parentFrame):
    
        ctrl = wx.TextCtrl(parentFrame,
            const("cLogCtrl"), "",
            wx.DefaultPosition, wx.DefaultSize,
            wx.TE_MULTILINE )
            
        return ctrl
    #@nonl
    #@-node:edream.110203113231.557:leoLog.createControl
    #@+node:edream.110203113231.558:leoLog.setLogFontFromConfig
    def setFontFromConfig (self):
        
        pass # g.trace()
    #@nonl
    #@-node:edream.110203113231.558:leoLog.setLogFontFromConfig
    #@+node:edream.110203113231.559:wxLeoLog.put & putnl
    # All output to the log stream eventually comes here.
    
    def put (self,s,color=None,tabName=None):
    
        if self.logCtrl:
            self.logCtrl.AppendText(s)
    
    def putnl (self,tabName=None):
    
        if self.logCtrl:
            self.logCtrl.AppendText('\n')
    #@nonl
    #@-node:edream.110203113231.559:wxLeoLog.put & putnl
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
        
        self.menuDict = {}
    #@nonl
    #@-node:edream.111303095242.3:  wxLeoMenu.__init__
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
    #@-node:ekr.20061106062514:Not called
    #@+node:edream.111603104327:9 Routines with Tk names
    #@+node:edream.111303111942.1:add_cascade
    def add_cascade (self,parent,label,menu,underline):
    
        """Create a menu with the given parent menu."""
    
        if parent:
            # Create a submenu of the parent menu.
            id = const(label)
            parent.AppendMenu(id,label,menu,label)
        else:
            # Create a top-level menu.
            self.menuBar.Append(menu,label)
    #@nonl
    #@-node:edream.111303111942.1:add_cascade
    #@+node:edream.111303103141:add_command
    def add_command (self,menu,**keys):
        
        label    = keys.get("label")
        callback = keys.get("command")
        
        def wxMenuCallback (event,callback=callback):
            # The Tk code does not use the event arg, so neither do we.
            # g.trace('callback',callback.__name__)
            return callback() # All args were bound when the callback was created.
    
        if menu:
            id = const(label)
            menu.Append(id,label,label)
            key = (menu,label),
            self.menuDict[key] = id # Remember id 
            # g.trace(label,callback)
            wx.EVT_MENU(self.frame,id,wxMenuCallback)
        else:
            g.trace("no menu",label)
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
    #@+node:edream.111303111942:insert_cascade
    def insert_cascade (self,parent,index,label,menu,underline):
    
        if not parent:
            self.menuBar.append(menu,label)
    #@nonl
    #@-node:edream.111303111942:insert_cascade
    #@+node:edream.111303110018:new_menu
    def new_menu(self,parent,tearoff=0):
        
        return wx.Menu()
    #@nonl
    #@-node:edream.111303110018:new_menu
    #@-node:edream.111603104327:9 Routines with Tk names
    #@+node:edream.111603112846:7 Routines with other names...
    #@+node:edream.111303103457.2:createMenuBar
    def createMenuBar(self,frame):
        
        self.menuBar = menuBar = wx.MenuBar()
    
        self.createMenusFromTables()
    
        frame.SetMenuBar(menuBar)
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
    #@-node:edream.111603112846:7 Routines with other names...
    #@-node:edream.111303103457:wx menu bindings
    #@-others
#@nonl
#@-node:edream.111303095242:wxLeoMenu class
#@+node:edream.111603213219:wxLeoTree class
class wxLeoTree (leoFrame.leoTree):

    #@    @+others
    #@+node:edream.111603213219.1:__init__
    def __init__ (self,frame,parentFrame):
    
        # Init the base class.
        leoFrame.leoTree.__init__(self,frame)
    
        self.treeCtrl = wx.TreeCtrl(parentFrame,
            const("cTreeCtrl"),
            wx.DefaultPosition, wx.DefaultSize,
            wx.TR_HAS_BUTTONS | wx.TR_EDIT_LABELS, wx.DefaultValidator,
            "treeCtrl")
            
        self.canvas = True # A dummy ivar used in c.treeWantsFocus, etc.
    
        self.root_id = None
        self.updateCount = 0
        
        #@    << declare event handlers >>
        #@+node:edream.111603213329:<< declare event handlers >>
        id = const("cTreeCtrl")
        
        wx.EVT_TREE_KEY_DOWN        (self.treeCtrl,id,self.onTreeKeyDown) # Control keys do not fire this event.
        wx.EVT_TREE_SEL_CHANGED     (self.treeCtrl,id,self.onTreeChanged)
        wx.EVT_TREE_SEL_CHANGING    (self.treeCtrl,id,self.onTreeChanging)
        wx.EVT_TREE_BEGIN_DRAG      (self.treeCtrl,id,self.onTreeBeginDrag)
        wx.EVT_TREE_END_DRAG        (self.treeCtrl,id,self.onTreeEndDrag)
        wx.EVT_TREE_BEGIN_LABEL_EDIT(self.treeCtrl,id,self.onTreeBeginLabelEdit)
        wx.EVT_TREE_END_LABEL_EDIT  (self.treeCtrl,id,self.onTreeEndLabelEdit)
        
         
        wx.EVT_TREE_ITEM_COLLAPSED  (self.treeCtrl,id,self.onTreeCollapsed)
        wx.EVT_TREE_ITEM_EXPANDED   (self.treeCtrl,id,self.onTreeExpanded)
        
        wx.EVT_TREE_ITEM_COLLAPSING (self.treeCtrl,id,self.onTreeCollapsing)
        wx.EVT_TREE_ITEM_EXPANDING  (self.treeCtrl,id,self.onTreeExpanding)
        #@nonl
        #@-node:edream.111603213329:<< declare event handlers >>
        #@nl
    #@nonl
    #@-node:edream.111603213219.1:__init__
    #@+node:edream.111303202917:Drawing
    #@+node:ekr.20061105114250:drawIcon TO DO
    def drawIcon(self,v,x,y):
        g.trace(v)
    #@nonl
    #@-node:ekr.20061105114250:drawIcon TO DO
    #@+node:edream.110203113231.295:beginUpdate
    def beginUpdate (self):
        
        if self.updateCount == 0:
            pass # self.Freeze() # Seems not to work...
    
        self.updateCount += 1
    #@nonl
    #@-node:edream.110203113231.295:beginUpdate
    #@+node:edream.110203113231.296:endUpdate
    def endUpdate (self,flag=True,scroll=False):
    
        assert(self.updateCount > 0)
    
        self.updateCount -= 1
        if flag and self.updateCount == 0:
            ## self.Thaw()
            self.redraw()
    #@nonl
    #@-node:edream.110203113231.296:endUpdate
    #@+node:edream.110203113231.298:redraw & redraw_now
    def redraw (self):
    
        # g.trace(self.drawing)
        self.drawing = True # Tell event handlers not to call us.
    
        c = self.c ; tree = self.treeCtrl
        if c is None: return
        p = c.rootPosition()
        if not p: return
    
        tree.DeleteAllItems()
        self.root_id = root_id = tree.AddRoot("Leo Outline Pane")
        while p: # This may need copies...
            self.redraw_subtree(root_id,p)
            p = p.next()
        tree.Expand(root_id)
        
        self.drawing = False
            
    def redraw_now(self,scroll=True):
        # g.trace()
        self.redraw()
    #@nonl
    #@-node:edream.110203113231.298:redraw & redraw_now
    #@+node:edream.110203113231.299:redraw_node
    def redraw_node(self,parent_id,v):
        
        # g.trace(v)
        tree = self.treeCtrl
        data = wx.TreeItemData(v)
        id = tree.AppendItem(parent_id,v.headString(),data=data)
        v.wxTreeId = id # Inject the ivar into the vnode.
        assert (v == tree.GetItemData(id).GetData())
        return id
        
    #@nonl
    #@-node:edream.110203113231.299:redraw_node
    #@+node:edream.110203113231.300:redraw_subtree
    def redraw_subtree(self,parent_id,v):
    
        tree = self.treeCtrl
        id = self.redraw_node(parent_id,v)
        child = v.firstChild()
        
        if v.isExpanded():
            while child:
                self.redraw_subtree(id,child)
                child = child.next()
            tree.Expand(id)
        else:
            if 1: # tree.SetItemHasChildren changes the event handler logic.  So this is good enough.
                while child:
                    self.redraw_node(id,child)
                    child = child.next()
            else:
                if child:
                    tree.SetItemHasChildren(id)
            tree.Collapse(id)
    #@nonl
    #@-node:edream.110203113231.300:redraw_subtree
    #@-node:edream.111303202917:Drawing
    #@+node:edream.111403090242.1:Editing TO DO
    def editLabel(self,v):
        pass
    
    def editVnode(self):
        pass
    
    def endEditLabel(self):
        pass
        
    def setEditVnode(self,v):
        pass
    
    def setNormalLabelState(self,v):
        pass
    
    def OnActivateHeadline(self,v):
        g.trace()
    #@nonl
    #@-node:edream.111403090242.1:Editing TO DO
    #@+node:edream.110203113231.278:Event handlers
    #@+node:edream.110203113231.279:Expand/contract
    #@+node:edream.110203113231.280:onTreeCollapsed & onTreeExpanded
    def onTreeCollapsed(self,event):
        
        """Prepare to collapse the tree."""
    
        pass # No need to redraw the tree.
    
    def onTreeExpanded (self,event):
        
        """Redraw the tree when a tree collapses."""
    
        if not self.frame.lockout and not self.drawing:
    
            self.redraw()
    #@nonl
    #@-node:edream.110203113231.280:onTreeCollapsed & onTreeExpanded
    #@+node:edream.110203113231.281:onTreeCollapsing & onTreeExpanding
    def onTreeCollapsing(self,event):
        
        """Call v.contract for a later redraw."""
    
        tree = self.treeCtrl
        id = event.GetItem()
        if id.IsOk and not self.frame.lockout:
            v = tree.GetItemData(id).GetData()
            if v:
                #g.trace(v)
                v.contract()
        
    def onTreeExpanding (self,event):
        
        """Call v.expand for a later redraw."""
        
        tree = self.treeCtrl
        id = event.GetItem()
        if id.IsOk and not self.frame.lockout:
            v = tree.GetItemData(id).GetData()
            if v:
                #g.trace(v)
                v.expand()
    #@nonl
    #@-node:edream.110203113231.281:onTreeCollapsing & onTreeExpanding
    #@-node:edream.110203113231.279:Expand/contract
    #@+node:edream.110203113231.282:Selecting
    #@+node:edream.110203113231.283:onTreeChanged
    def onTreeChanged(self,event):
    
        frame = self ; c = self.c ; tree = self.treeCtrl
        
        if self.frame.lockout > 0: return 
        new_id = event.GetItem()
        if not new_id.IsOk(): return
        v = tree.GetItemData(new_id).GetData()
        if not v: return
    
        self.frame.lockout += 1 # MUST prevent further events.
        
        c.selectVnode(v)
        s = v.t.bodyString
        s = g.toUnicode(s,"utf-8")  # No g.app.tkEncoding or similar yet.
        t = self.frame.body.bodyCtrl
        g.trace('widget',t)
        t.Clear()
        t.WriteText(s)
        self.frame.body.recolor(v)
        
        self.frame.lockout -= 1
    #@nonl
    #@-node:edream.110203113231.283:onTreeChanged
    #@+node:edream.110203113231.284:onTreeChanging
    def onTreeChanging(self,event):
        
        """Event handler gets called whenever a new node gets selected"""
    
        g.trace(event)
        pass
    #@nonl
    #@-node:edream.110203113231.284:onTreeChanging
    #@-node:edream.110203113231.282:Selecting
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
    
        tree = self.treeCtrl
        s = event.GetLabel()
        id = event.GetItem()
        v = tree.GetItemData(id).GetData()
    
        return # Not yet: c.setChanged uses frame.top.
    
        # Set the dirty bit and the file-changed mark if the headline has changed.
        if not v.isDirty()and s != v.headString():
            v.setDirty()
            if not self.c.isChanged():
                self.c.setChanged(True)
    
        # Update all joined headlines.
        j = v.joinList()
        while j != v:
            c.setHeadString(j,s)
            j = j.joinList()
    #@nonl
    #@-node:edream.110203113231.287:onTreeEndLabelEdit
    #@+node:edream.110203113231.288:onTreeKeyDown
    def onTreeKeyDown(self,event):
        
        pass # Don't do anything until the end-edit event.
    #@nonl
    #@-node:edream.110203113231.288:onTreeKeyDown
    #@-node:edream.110203113231.285:Editing labels
    #@+node:ekr.20061105114250.1:Dragging
    #@+node:edream.110203113231.289:onTreeBeginDrag
    def onTreeBeginDrag(self,event):
    
        g.trace() ; return
    
        if event.GetItem()!= self.treeCtrl.GetRootItem():
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
    #@-node:edream.110203113231.278:Event handlers
    #@+node:edream.111403093559:Focus
    def focus_get(self):
        
        return self.FindFocus()
    #@nonl
    #@-node:edream.111403093559:Focus
    #@+node:edream.111403093559.1:Fonts TO DO
    def getFont(self):
        g.trace()
    
    def setFont(self,font):
        g.trace()
    #@nonl
    #@-node:edream.111403093559.1:Fonts TO DO
    #@+node:edream.111403090242:Scrolling TO DO
    # Scrolling... 
    def scrollTo(self,p):
        g.trace()
    
    def idle_scrollTo(self,p):
        pass
    #@nonl
    #@-node:edream.111403090242:Scrolling TO DO
    #@+node:ekr.20050719121701:Selection stuff...
    #@+node:edream.111603221343.1:OLDselect
    # Warning: do not try to "optimize" this by returning if v==tree.currentVnode.
    
    def OLDselect (self,v,updateBeadList=True):
    
        c = self.c ; frame = c.frame ; body = frame.bodyCtrl
        old_v = c.currentVnode()
    
        if not g.doHook("unselect1",c=c,new_v=v,old_v=old_v):
            if 0: ## Not ready yet.
                #@            << unselect the old node >>
                #@+node:edream.111603221343.3:<< unselect the old node >>
                # Remember the position of the scrollbar before making any changes.
                yview = body.yview()
                insertSpot = c.frame.body.getInsertionPoint()
                
                # Remember the old body text
                old_body = body.getAllText()
                
                if old and old != v and c.edit_widget(old):
                    old.t.scrollBarSpot = yview
                    old.t.insertSpot = insertSpot
                #@-node:edream.111603221343.3:<< unselect the old node >>
                #@nl
        else: old_body = u""
    
        g.doHook("unselect2",c=c,new_v=v,old_v=old_v)
        
        if not g.doHook("select1",c=c,new_v=v,old_v=old_v):
            #@        << select the new node >>
            #@+node:edream.111603221343.4:<< select the new node >>
            if 0: # Done in event handler??
            
                frame.setWrap(v)
            
                # Delete only if necessary: this may reduce flicker slightly.
                s = v.t.bodyString
                s = g.toUnicode(s,"utf-8")
                old_body = g.toUnicode(old_body,"utf-8")
                if old_body != s:
                    body.delete("1.0","end")
                    body.insert("1.0",s)
            
                # We must do a full recoloring: we may be changing context!
                self.frame.body.recolor_now(v)
            
                if v and v.t.scrollBarSpot != None:
                    first,last = v.t.scrollBarSpot
                    body.yview("moveto",first)
            
                if v.t.insertSpot != None: # 9/21/02: moved from c.selectVnode
                    c.frame.bodyCtrl.mark_set("insert",v.t.insertSpot)
                    c.frame.bodyCtrl.see(v.t.insertSpot)
                else:
                    c.frame.bodyCtrl.mark_set("insert","1.0")
            #@nonl
            #@-node:edream.111603221343.4:<< select the new node >>
            #@nl
            if v and v != old_v: # 3/26/03: Suppress duplicate call.
                try: # may fail during initialization
                    self.idle_scrollTo()
                except: pass
            #@        << update c.beadList or c.beadPointer >>
            #@+node:edream.111603221343.5:<< update c.beadList or c.beadPointer >>
            if updateBeadList:
                
                if c.beadPointer > -1:
                    present_v = c.beadList[c.beadPointer]
                else:
                    present_v = None
                
                if v != present_v:
                    # Replace the tail of c.beadList by c and make c the present node.
                    # print "updating c.beadList"
                    c.beadPointer += 1
                    c.beadList[c.beadPointer:] = []
                    c.beadList.append(v)
                    
                # g.trace(c.beadPointer,v,present_v)
            #@nonl
            #@-node:edream.111603221343.5:<< update c.beadList or c.beadPointer >>
            #@nl
            #@        << update c.visitedList >>
            #@+node:edream.111603221343.6:<< update c.visitedList >>
            # Make v the most recently visited node on the list.
            if v in c.visitedList:
                c.visitedList.remove(v)
                
            c.visitedList.insert(0,v)
            #@nonl
            #@-node:edream.111603221343.6:<< update c.visitedList >>
            #@nl
    
        #@    << set the current node and redraw >>
        #@+node:edream.111603221343.7:<< set the current node and redraw >>
        self.setCurrentVnode(v)
        
        if 0: ## Not ready yet
            self.setSelectedLabelState(v)
            self.scanForTabWidth(v) # 9/13/02 #GS I believe this should also get into the select1 hook.
        
        g.app.gui.set_focus(c,c.frame.bodyCtrl)
        #@nonl
        #@-node:edream.111603221343.7:<< set the current node and redraw >>
        #@nl
        g.doHook("select2",c=c,new_v=v,old_v=old_v)
        g.doHook("select3",c=c,new_v=v,old_v=old_v)
    #@-node:edream.111603221343.1:OLDselect
    #@+node:ekr.20050719120304:tree.select (MORE WORK NEEDED)
    # Warning: do not try to "optimize" this by returning if p==tree.currentPosition.
    
    def select (self,p,updateBeadList=True):
        
        c = self.c ; frame = c.frame ; body = frame.bodyCtrl
        old_p = c.currentPosition()
    
        if not p: return
        if not c.positionExists(p):
            g.trace('does not exist',p)
            return
    
        # g.trace('len(body)',len(p.bodyString()),p.headString())
    
        if not g.doHook("unselect1",c=c,new_p=p,old_p=old_p,new_v=p,old_v=old_p):
            #@        << unselect the old node >>
            #@+node:ekr.20050719120304.1:<< unselect the old node >>
            # Remember the position of the scrollbar before making any changes.
            if old_p:
                
                if 0:  ### Not ready yet.
            
                    yview=body.yview()
                    insertSpot = c.frame.body.getInsertionPoint()
                    
                    if old_p != p:
                        # g.trace("unselect:",old_p.headString())
                        self.endEditLabel() # sets editPosition = None
                        self.setUnselectedLabelState(old_p)
                    
                    if c.edit_widget(old_p):
                        old_p.v.t.scrollBarSpot = yview
                        old_p.v.t.insertSpot = insertSpot
            #@nonl
            #@-node:ekr.20050719120304.1:<< unselect the old node >>
            #@nl
    
        g.doHook("unselect2",c=c,new_p=p,old_p=old_p,new_v=p,old_v=old_p)
        
        if not g.doHook("select1",c=c,new_p=p,old_p=old_p,new_v=p,old_v=old_p):
            #@        << select the new node >>
            #@+node:ekr.20050719120304.2:<< select the new node >>
            if 0:  ### Not ready yet.
                frame.setWrap(p)
            
            # Always do this.  Otherwise there can be problems with trailing hewlines.
            s = g.toUnicode(p.v.t.bodyString,"utf-8")
            
            if 0: ### May not be needed.
                self.setText(body,s,tag="select:set body",isHeadline=False)
            
            # We must do a full recoloring: we may be changing context!
            self.frame.body.recolor_now(p) # recolor now uses p.copy(), so this is safe.
            
            if 0:  ### Not ready yet.
            
                if p.v and p.v.t.scrollBarSpot != None:
                    first,last = p.v.t.scrollBarSpot
                    body.yview("moveto",first)
                
                if p.v and p.v.t.insertSpot != None:
                    c.frame.bodyCtrl.mark_set("insert",p.v.t.insertSpot)
                    c.frame.bodyCtrl.see(p.v.t.insertSpot)
                else:
                    c.frame.bodyCtrl.mark_set("insert","1.0")
                
            # g.trace("select:",p.headString())
            #@nonl
            #@-node:ekr.20050719120304.2:<< select the new node >>
            #@nl
            if p and p != old_p: # Suppress duplicate call.
                try: # may fail during initialization.
                    self.idle_scrollTo(p) # p is NOT c.currentPosition() here!
                except: pass
            #@        << update c.beadList or c.beadPointer >>
            #@+node:ekr.20050719120304.3:<< update c.beadList or c.beadPointer >>
            if updateBeadList:
                
                if c.beadPointer > -1:
                    present_p = c.beadList[c.beadPointer]
                else:
                    present_p = c.nullPosition()
                
                if p != present_p:
                    # Replace the tail of c.beadList by c and make c the present node.
                    # print "updating c.beadList"
                    c.beadPointer += 1
                    c.beadList[c.beadPointer:] = []
                    c.beadList.append(p.copy())
                    
                # g.trace(c.beadPointer,p,present_p)
            #@nonl
            #@-node:ekr.20050719120304.3:<< update c.beadList or c.beadPointer >>
            #@nl
            #@        << update c.visitedList >>
            #@+node:ekr.20050719120304.4:<< update c.visitedList >>
            # Make p the most recently visited position on the list.
            if p in c.visitedList:
                c.visitedList.remove(p)
            
            c.visitedList.insert(0,p.copy())
            #@nonl
            #@-node:ekr.20050719120304.4:<< update c.visitedList >>
            #@nl
    
        #@    << set the current node >>
        #@+node:ekr.20050719120304.5:<< set the current node >>
        c.setCurrentPosition(p)
        
        if p != old_p:
            self.setSelectedLabelState(p)
        
        frame.scanForTabWidth(p) # GS I believe this should also get into the select1 hook
        
        
        if 0: ### Not ready yet.
            frame.bodyWantsFocus()
        #@nonl
        #@-node:ekr.20050719120304.5:<< set the current node >>
        #@nl
        
        g.doHook("select2",c=c,new_p=p,old_p=old_p,new_v=p,old_v=old_p)
        g.doHook("select3",c=c,new_p=p,old_p=old_p,new_v=p,old_v=old_p)
        
        # g.printGc()
    #@nonl
    #@-node:ekr.20050719120304:tree.select (MORE WORK NEEDED)
    #@+node:ekr.20050719121812:Disabled for now
    #@+node:ekr.20050719121701.2:endEditLabel
    def endEditLabel (self):
        
        return ###
        
        """End editing for self.editText."""
    
        c = self.c ; frame = c.frame
        
        p = self.editPosition()
    
        if p and c.edit_widget(p):
            if 0: # New in recycled widgets scheme: this could cause a race condition.
                # This will be done in the redraw code becaused editPosition will be None.
                self.setUnselectedLabelState(p)
    
            self.setEditPosition(None)
    
            # force a redraw of joined and ancestor headlines.
            self.force_redraw() 
    
        frame.bodyWantsFocus()
    #@nonl
    #@-node:ekr.20050719121701.2:endEditLabel
    #@+node:ekr.20050719121701.3:editLabel
    def editLabel (self,p):
        
        """Start editing p's headline."""
        
        # g.trace(p)
        
        return ###
    
        if self.editPosition() and p != self.editPosition():
            self.endEditLabel()
            self.frame.revertHeadline = None
            
        self.setEditPosition(p)
    
        # Start editing
        if p and c.edit_widget(p):
            self.setNormalLabelState(p)
            self.frame.revertHeadline = p.headString()
            self.setEditPosition(p)
    #@nonl
    #@-node:ekr.20050719121701.3:editLabel
    #@+node:ekr.20050719121701.10:tree.set...LabelState
    #@+node:ekr.20050719121701.11:setNormalLabelState
    def setNormalLabelState (self,p): # selected, editing
    
        return ###
    
        # Do nothing if a redraw is already sheduled.
        # This prevents race conditions.
        if self.redrawScheduled: return 
        
        if p and c.edit_widget(p):
            self.setEditHeadlineColors(p)
            c.edit_widget(p).tag_remove("sel","1.0","end")
            c.edit_widget(p).tag_add("sel","1.0","end")
            # Set the focus immediately
            self.frame.widgetWantsFocus(c.edit_widget(p))
    #@nonl
    #@-node:ekr.20050719121701.11:setNormalLabelState
    #@+node:ekr.20050719121701.12:setDisabledLabelState
    def setDisabledLabelState (self,p): # selected, disabled
    
        return ###
    
        # Do nothing if a redraw is already sheduled.
        # This prevents race conditions.
        if self.redrawScheduled: return
    
        if p and c.edit_widget(p):
            self.setDisabledHeadlineColors(p)
    #@nonl
    #@-node:ekr.20050719121701.12:setDisabledLabelState
    #@+node:ekr.20050719121701.13:setSelectedLabelState
    def setSelectedLabelState (self,p): # selected, not editing
    
        return ###
    
        # Do nothing if a redraw is already sheduled.
        # This prevents race conditions.
        if self.redrawScheduled: return 
    
        # g.trace(p)
        self.setDisabledLabelState(p)
    
    #@-node:ekr.20050719121701.13:setSelectedLabelState
    #@+node:ekr.20050719121701.14:setUnselectedLabelState
    def setUnselectedLabelState (self,p): # not selected.
        
        return ###
    
        # Do nothing if a redraw is already sheduled.
        # This prevents race conditions.
        if self.redrawScheduled: return 
    
        if p and c.edit_widget(p):
            self.setUnselectedHeadlineColors(p)
    #@nonl
    #@-node:ekr.20050719121701.14:setUnselectedLabelState
    #@+node:ekr.20050719121701.15:setDisabledHeadlineColors
    def setDisabledHeadlineColors (self,p):
        
        return ###
    
        c = self.c ; w = c.edit_widget(p)
    
        if self.trace and self.verbose:
            if not self.redrawing:
                print "%10s %d %s" % ("disabled",id(w),p.headString())
                # import traceback ; traceback.print_stack(limit=6)
    
        fg = c.config.getColor("headline_text_selected_foreground_color") or 'black'
        bg = c.config.getColor("headline_text_selected_background_color") or 'grey80'
        
        try:
            w.configure(state="disabled",highlightthickness=0,fg=fg,bg=bg)
        except:
            g.es_exception()
    #@nonl
    #@-node:ekr.20050719121701.15:setDisabledHeadlineColors
    #@+node:ekr.20050719121701.16:setEditHeadlineColors
    def setEditHeadlineColors (self,p):
        
        return ###
    
        c = self.c ; w = c.edit_widget(p)
        
        if self.trace and self.verbose:
            if not self.redrawing:
                print "%10s %d %s" % ("edit",id(2),p.headString())
        
        fg    = c.config.getColor("headline_text_editing_foreground_color") or 'black'
        bg    = c.config.getColor("headline_text_editing_background_color") or 'white'
        selfg = c.config.getColor("headline_text_editing_selection_foreground_color")
        selbg = c.config.getColor("headline_text_editing_selection_background_color")
        
        try: # Use system defaults for selection foreground/background
            if selfg and selbg:
                w.configure(
                    selectforeground=selfg,selectbackground=selbg,
                    state="normal",highlightthickness=1,fg=fg,bg=bg)
            elif selfg and not selbg:
                w.configure(
                    selectforeground=selfg,
                    state="normal",highlightthickness=1,fg=fg,bg=bg)
            elif selbg and not selfg:
                w.configure(
                    selectbackground=selbg,
                    state="normal",highlightthickness=1,fg=fg,bg=bg)
            else:
                w.configure(
                    state="normal",highlightthickness=1,fg=fg,bg=bg)
        except:
            g.es_exception()
    #@nonl
    #@-node:ekr.20050719121701.16:setEditHeadlineColors
    #@+node:ekr.20050719121701.17:setUnselectedHeadlineColors
    def setUnselectedHeadlineColors (self,p):
        
        return ###
        
        c = self.c ; w = c.edit_widget(p)
        
        if self.trace and self.verbose:
            if not self.redrawing:
                print "%10s %d %s" % ("unselect",id(w),p.headString())
                # import traceback ; traceback.print_stack(limit=6)
        
        fg = c.config.getColor("headline_text_unselected_foreground_color") or 'black'
        bg = c.config.getColor("headline_text_unselected_background_color") or 'white'
        
        try:
            w.configure(state="disabled",highlightthickness=0,fg=fg,bg=bg)
        except:
            g.es_exception()
    #@nonl
    #@-node:ekr.20050719121701.17:setUnselectedHeadlineColors
    #@-node:ekr.20050719121701.10:tree.set...LabelState
    #@-node:ekr.20050719121812:Disabled for now
    #@+node:ekr.20050719121701.18:dimEditLabel, undimEditLabel
    # Convenience methods so the caller doesn't have to know the present edit node.
    
    def dimEditLabel (self):
        
        p = self.c.currentPosition()
        self.setDisabledLabelState(p)
    
    def undimEditLabel (self):
    
        p = self.c.currentPosition()
        self.setSelectedLabelState(p)
    #@nonl
    #@-node:ekr.20050719121701.18:dimEditLabel, undimEditLabel
    #@-node:ekr.20050719121701:Selection stuff...
    #@+node:ekr.20050719121356:setText
    def setText (self,t,s,tag="",isHeadline=True):
        
        g.trace(s)
    #@nonl
    #@-node:ekr.20050719121356:setText
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
#@+node:edream.110203113231.560:Find...
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
    #@+node:edream.111503094322:Insert point
    # Simulating wxWindows calls (upper case)
    def GetInsertionPoint (self):
        return self.insertPoint
    
    def SetInsertionPoint (self,index):
        self.insertPoint = index
        
    def SetInsertionPointEND (self,index):
        self.insertPoint = len(self.text)+1
    
    # Returning indices...
    def getBeforeInsertionPoint (self):
        g.trace()
    
    # Returning chars...
    def getCharAtInsertPoint (self):
        g.trace()
    
    def getCharBeforeInsertPoint (self):
        g.trace()
    
    # Setting the insertion point...
    def setInsertPointToEnd (self):
        self.insertPoint = -1
        
    def setInsertPointToStartOfLine (self,lineNumber):
        g.trace()
    #@nonl
    #@-node:edream.111503094322:Insert point
    #@+node:edream.111503094014.1:Selection
    # Simulating wxWindows calls (upper case)
    def SetSelection(self,n1,n2):
        self.selection = n1,n2
        
    # Others...
    def deleteSelection (self):
        self.selection = 0,0
    
    def getSelectionRange (self):
        return self.selection
        
    def hasTextSelection (self):
        start,end = self.selection
        return start != end
    
    def selectAllText (self):
        self.selection = 0,-1
    
    def setSelectionRange (self,sel):
        try:
            start,end = sel
            self.selection = start,end
        except:
            self.selection = sel,sel
    #@nonl
    #@-node:edream.111503094014.1:Selection
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
        
        self.s_text = wxSearchWidget() # wx.TextCtrl(self,-1) # Working text widget.
    
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
        
        g.trace()
    
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
    def gui_search (self,t,find_text,index,
        stopindex,backwards,regexp,nocase):
            
        g.trace(index,stopindex,backwards,regexp,nocase)
        
        s = t.text # t is the dummy text widget
        
        if index is None:
            index = 0
    
        pos = s.find(find_text,index)
    
        if pos == -1:
            pos = None
        
        return pos
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
        self.findText = wx.TextCtrl(self,
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
        self.changeText = wx.TextCtrl(self,
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
#@-node:edream.110203113231.560:Find...
#@-others
#@nonl
#@-node:edream.110203113231.302:@thin __wx_gui.py
#@-leo
