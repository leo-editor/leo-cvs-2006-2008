#@+leo-ver=4-thin
#@+node:ekr.20031218072017.3655:@thin leoFrame.py
"""The base classes for all Leo Windows, their body, log and tree panes, key bindings and menus.

These classes should be overridden to create frames for a particular gui."""

#@@language python
#@@tabwidth -4
#@@pagewidth 80

import leoGlobals as g
import leoColor
import leoMenu
import leoNodes
import leoUndo

import re

#@<< About handling events >>
#@+node:ekr.20031218072017.2410:<< About handling events >>
#@+at
# Leo must handle events or commands that change the text in the outline or 
# body
# panes. We must ensure that headline and body text corresponds to the vnode 
# and
# tnode corresponding to presently selected outline, and vice versa. For 
# example,
# when the user selects a new headline in the outline pane, we must ensure 
# that:
# 
# 1) All vnodes and tnodes have up-to-date information and
# 
# 2) the body pane is loaded with the correct data.
# 
# Early versions of Leo attempted to satisfy these conditions when the user
# switched outline nodes. Such attempts never worked well; there were too many
# special cases. Later versions of Leo use a much more direct approach: every
# keystroke in the body pane updates the presently selected tnode immediately.
# 
# The leoTree class contains all the event handlers for the tree pane, and the
# leoBody class contains the event handlers for the body pane. The following
# convenience methods exists:
# 
# - body.updateBody & tree.updateBody:
#     Called by k.masterCommand after any keystroke not handled by 
# k.masterCommand.
#     These are suprising complex.
# 
# - body.bodyChanged & tree.headChanged:
#     Called by commands throughout Leo's core that change the body or 
# headline.
#     These are thin wrappers for updateBody and updateTree.
#@-at
#@-node:ekr.20031218072017.2410:<< About handling events >>
#@nl

#@+others
#@+node:ekr.20031218072017.3656:class leoBody
class leoBody:
    
    """The base class for the body pane in Leo windows."""
    
    __pychecker__ = '--no-argsused' # base classes have many unused args.
    
    #@    @+others
    #@+node:ekr.20031218072017.3657:leoBody.__init__
    def __init__ (self,frame,parentFrame):
    
        self.frame = frame
        self.c = frame.c
        self.editorWidgets = {} # keys are pane names, values are text widgets
        self.forceFullRecolorFlag = False
        frame.body = self
        
        # May be overridden in subclasses...
        self.bodyCtrl = self
        self.numberOfEditors = 1
        
        # Must be overridden in subclasses...
        self.colorizer = None
    #@+node:ekr.20031218072017.3660:leoBody.mustBeDefinedInSubclasses
    mustBeDefinedInSubclasses = (
        # Birth, death & config.
        '__init__',
        'createBindings',
        'createControl',
        'setColorFromConfig',
        'setFontFromConfig'   
        # Editors...
        'addEditor',
        'createLabel',
        'cycleEditorFocus',
        'deleteEditor',
        'selectEditor',
        'selectLabel',
        'selectMainEditor',
        'setEditorColors',
        'unselectLabel',
        'updateEditors',
        # Events...
        'onBodyChanged',
        'scheduleIdleTimeRoutine',
        # Low-level gui...(May be deleted)
        'getBodyPaneHeight',
        'getBodyPaneWidth',
        'hasFocus',
        'setFocus',
        'tag_add',
        'tag_bind',
        'tag_configure',
        'tag_delete',
        'tag_remove',
    )
    #@-node:ekr.20031218072017.3660:leoBody.mustBeDefinedInSubclasses
    #@+node:ekr.20061109102912:define leoBody.mustBeDefinedOnlyInBaseClass
    mustBeDefinedOnlyInBaseClass = (
        'getAllText',
        'getColorizer',
        'getInsertLines',
        'getInsertPoint',
        'getSelectedText',
        'getSelectionAreas',
        'getSelectionLines',
        'getYScrollPosition',
        'hasTextSelection',
        'oops',
        'onClick',
        'recolor',
        'recolor_now',
        'recolor_range',
        'see',
        'seeInsertPoint',
        'selectAllText',
        'setInsertPoint',
        'setSelectionRange',
        'setYScrollPosition',
        'setSelectionAreas',
        'setYScrollPosition',
        'updateSyntaxColorer',
    )
    
    #@-node:ekr.20061109102912:define leoBody.mustBeDefinedOnlyInBaseClass
    #@-node:ekr.20031218072017.3657:leoBody.__init__
    #@+node:ekr.20061109173122:leoBody: must be defined in subclasses
    # Birth, death & config
    def createBindings (self,w=None):               self.oops()
    def createControl (self,frame,parentFrame,p):   self.oops()
    def setColorFromConfig (self,w=None):           self.oops()
    def setFontFromConfig (self,w=None):            self.oops()
    # Editors...
    def addEditor (self,event=None):                self.oops()
    def createLabel (self,w):                       self.oops()
    def cycleEditorFocus (self,event=None):         self.oops()
    def deleteEditor (self,event=None):             self.oops()
    def selectEditor(self,w):                       self.oops()
    def selectLabel (self,w):                       self.oops()
    def selectMainEditor (self,p):                  self.oops()
    def setEditorColors (self,bg,fg):               self.oops()
    def unselectLabel (self,w):                     self.oops()
    def updateEditors (self):                       self.oops()
    # Events...
    def onBodyChanged (self,undoType,oldSel=None,oldText=None,oldYview=None): self.oops()
    def scheduleIdleTimeRoutine (self,function,*args,**keys): self.oops()
    # Low-level gui...
    def getBodyPaneHeight (self):                   self.oops() # return 500
    def getBodyPaneWidth (self):                    self.oops() # return 600
    def hasFocus (self):                            self.oops()
    def setFocus (self):                            self.oops()
    def tag_add (self,tagName,index1,index2):       self.oops()
    def tag_bind (self,tagName,event,callback):     self.oops()
    def tag_configure (self,colorName,**keys):      self.oops()
    def tag_delete(self,tagName):                   self.oops()
    def tag_remove (self,tagName,index1,index2):    self.oops()
    #@-node:ekr.20061109173122:leoBody: must be defined in subclasses
    #@+node:ekr.20061109173021:leoBody: must be defined in the base class
    #@+node:ekr.20031218072017.3677:Coloring
    def getColorizer(self):
        
        return self.colorizer
    
    def recolor_now(self,p,incremental=False):
    
        self.colorizer.colorize(p.copy(),incremental)
    
    def recolor_range(self,p,leading,trailing):
        
        self.colorizer.recolor_range(p.copy(),leading,trailing)
    
    def recolor(self,p,incremental=False):
        
        if 0: # Do immediately
            self.colorizer.colorize(p.copy(),incremental)
        else: # Do at idle time
            self.colorizer.schedule(p.copy(),incremental)
        
    def updateSyntaxColorer(self,p):
        
        return self.colorizer.updateSyntaxColorer(p.copy())
    #@-node:ekr.20031218072017.3677:Coloring
    #@+node:ekr.20061109095450.8:onClick (passed)
    def onClick (self,event):
        
        c = self.c ; k = c.k ; w = event and event.widget
        wname = c.widget_name(w)
        
        if wname.startswith('body'):
            # A hack to support middle-button pastes: remember the previous selection.
            k.previousSelection = w.getSelectionRange()
            x,y = g.app.gui.eventXY(event)
            i = w.xyToPythonIndex(x,y)
            # g.trace(x,y,repr(i))
            w.setSelectionRange(i,i,insert=i)
            c.editCommands.setMoveCol(w,i)
            c.frame.updateStatusLine()
            self.selectEditor(w)
        else:
            g.trace('can not happen')
    #@-node:ekr.20061109095450.8:onClick (passed)
    #@+node:ekr.20031218072017.3658:oops
    def oops (self):
        
        g.trace("leoBody oops:", g.callers(), "should be overridden in subclass")
    #@-node:ekr.20031218072017.3658:oops
    #@+node:ekr.20031218072017.4018:Text (leoBody)
    def getAllText (self):
        return self.bodyCtrl.getAllText()
    
    def getInsertPoint(self):
        return self.bodyCtrl.getInsertPoint()
    
    def getSelectedText (self):
        """Return the selected text of the body frame, converted to unicode."""
        return self.bodyCtrl.getSelectedText()
    
    def getSelectionRange (self,sort=True):
        """Return a tuple representing the selected range of body text.
        Return a tuple giving the insertion point if no range of text is selected."""
        return self.bodyCtrl.getSelectionRange(sort)
        
    def hasTextSelection (self):
        return self.bodyCtrl.hasSelection()
        
    # def scrollDown (self):
        # g.app.gui.yscroll(self.bodyCtrl,1,'units')
        
    # def scrollUp (self):
        # g.app.gui.yscroll(self.bodyCtrl,-1,'units')
        
    def see (self,index):
        self.bodyCtrl.see(index)
        
    def seeInsertPoint (self):
        self.bodyCtrl.seeInsertPoint()
        
    def selectAllText (self,event=None):
        w = g.app.gui.eventWidget(event) or self.bodyCtrl
        return w.selectAllText()
        
    def setInsertPoint (self,pos):
        return self.bodyCtrl.getInsertPoint(pos)
        
    def setSelectionRange (self,sel):
        i,j = sel
        self.bodyCtrl.setSelectionRange(i,j)
    
    # (?<!gui)\.getSelectionRange
    #@nonl
    #@+node:ekr.20031218072017.4030:getInsertLines (passed)
    def getInsertLines (self):
        
        """Return before,after where:
            
        before is all the lines before the line containing the insert point.
        sel is the line containing the insert point.
        after is all the lines after the line containing the insert point.
        
        All lines end in a newline, except possibly the last line."""
        
        w = self.bodyCtrl
        s = w.getAllText()
        insert = w.getInsertPoint()
        i,j = g.getLine(s,insert)
        before = s[0:i]
        ins = s[i:j]
        after = s[j:]
    
        before = g.toUnicode(before,g.app.tkEncoding)
        ins    = g.toUnicode(ins,   g.app.tkEncoding)
        after  = g.toUnicode(after ,g.app.tkEncoding)
    
        return before,ins,after
    #@-node:ekr.20031218072017.4030:getInsertLines (passed)
    #@+node:ekr.20031218072017.4031:getSelectionAreas (passed)
    def getSelectionAreas (self):
        
        """Return before,sel,after where:
            
        before is the text before the selected text
        (or the text before the insert point if no selection)
        sel is the selected text (or "" if no selection)
        after is the text after the selected text
        (or the text after the insert point if no selection)"""
    
        w = self.bodyCtrl
        s = w.getAllText()
        i,j = w.getSelectionRange()
        if i == j: j = i + 1
    
        before = s[0:i]
        sel    = s[i:j]
        after  = s[j:]
        
        before = g.toUnicode(before,g.app.tkEncoding)
        sel    = g.toUnicode(sel,   g.app.tkEncoding)
        after  = g.toUnicode(after ,g.app.tkEncoding)
        return before,sel,after
    #@nonl
    #@-node:ekr.20031218072017.4031:getSelectionAreas (passed)
    #@+node:ekr.20031218072017.2377:getSelectionLines (leoBody)
    def getSelectionLines (self):
        
        """Return before,sel,after where:
            
        before is the all lines before the selected text
        (or the text before the insert point if no selection)
        sel is the selected text (or "" if no selection)
        after is all lines after the selected text
        (or the text after the insert point if no selection)"""
        
        if g.app.batchMode:
            c.notValidInBatchMode(undoType)
            return '','',''
        
        # At present, called only by c.getBodyLines.
        w = self.bodyCtrl
        s = w.getAllText()
        i,j = w.getSelectionRange()
        if i == j:
            i,j = g.getLine(s,i)
        else:
            i,junk = g.getLine(s,i)
            junk,j = g.getLine(s,j)
       
        
        before = g.toUnicode(s[0:i],g.app.tkEncoding)
        sel    = g.toUnicode(s[i:j],g.app.tkEncoding)
        after  = g.toUnicode(s[j:len(s)],g.app.tkEncoding)
        
        # g.trace(i,j,'sel',repr(s[i:j]),'after',repr(after))
        return before,sel,after # 3 strings.
    #@-node:ekr.20031218072017.2377:getSelectionLines (leoBody)
    #@+node:ekr.20031218072017.4037:setSelectionAreas (leoBody)
    def setSelectionAreas (self,before,sel,after):
        
        """Replace the body text by before + sel + after and
        set the selection so that the sel text is selected."""
    
        w = self.bodyCtrl
        s = w.getAllText()
        before = before or ''
        sel = sel or ''
        after = after or ''
        w.delete(0,len(s))
        w.insert(0,before+sel+after)
        i = len(before)
        j = max(i,len(before)+len(sel)-1)
        # g.trace(i,j,repr(sel))
        w.setSelectionRange(i,j,insert=j)
        return i,j
    #@-node:ekr.20031218072017.4037:setSelectionAreas (leoBody)
    #@+node:ekr.20031218072017.4038:get/setYScrollPosition (leoBody)
    def getYScrollPosition (self):
        return self.bodyCtrl.getYScrollPosition()
        
    def setYScrollPosition (self,scrollPosition):
        if len(scrollPosition) == 2:
            first,last = scrollPosition
        else:
            first = scrollPosition
        self.bodyCtrl.setYScrollPosition(first)
    #@-node:ekr.20031218072017.4038:get/setYScrollPosition (leoBody)
    #@-node:ekr.20031218072017.4018:Text (leoBody)
    #@-node:ekr.20061109173021:leoBody: must be defined in the base class
    #@-others
#@-node:ekr.20031218072017.3656:class leoBody
#@+node:ekr.20031218072017.3678:class leoFrame
class leoFrame:
    
    """The base class for all Leo windows."""
    
    __pychecker__ = '--no-argsused' # base classes have many unused args.
    
    instances = 0
    
    #@    @+others
    #@+node:ekr.20031218072017.3679:  leoFrame.__init__
    def __init__ (self,gui):
        
        self.c = None # Must be created by subclasses.
        self.title = None # Must be created by subclasses.
        self.gui = gui
        
        # Objects attached to this frame.
        self.colorPanel = None 
        self.comparePanel = None
        self.findPanel = None
        self.fontPanel = None
        self.iconBar = None
        self.isNullFrame = False
        self.keys = None
        self.menu = None
        self.miniBufferWidget = None # New in 4.4.
        self.prefsPanel = None
        self.statusLine = None
        self.useMiniBufferWidget = False # New in 4.4
    
        # Gui-independent data
        self.componentsDict = {} # Keys are names, values are componentClass instances.
        self.es_newlines = 0 # newline count for this log stream
        self.openDirectory = ""
        self.requestRecolorFlag = False
        self.saved=False # True if ever saved
        self.splitVerticalFlag,self.ratio, self.secondary_ratio = True,0.5,0.5 # Set by initialRatios later.
        self.startupWindow=False # True if initially opened window
        self.stylesheet = None # The contents of <?xml-stylesheet...?> line.
        self.tab_width = 0 # The tab width in effect in this pane.
    #@+node:ekr.20061109120726:leoFrame.mustBeDefinedOnlyInBaseClass
    mustBeDefinedOnlyInBaseClass = (
       
        'initialRatios',
        'longFileName',
        'oops',
        'promptForSave',
        'scanForTabWidth',
        'shortFileName',
        
        # Headline editing.
        'abortEditLabelCommand',
        'endEditLabelCommand',
        'insertHeadlineTime',
        
        # Cut/Copy/Paste.
        'OnPaste',
        'OnPasteFromMenu',
        'copyText',
        'cutText',
        'pasteText',
    
        # Icon bar convenience methods.    
        'addIconButton',
        'clearIconBar',
        'createIconBar',
        'getIconBar',
        'getIconBarObject',
        'hideIconBar',
        
        # Status line convenience methods.
        'createStatusLine',
        'clearStatusLine',
        'disableStatusLine',
        'enableStatusLine',
        'getStatusLine',
        'getStatusObject',
        'putStatusLine',
        'setFocusStatusLine',
        'statusLineIsEnabled',
        'updateStatusLine',
    )
    #@nonl
    #@-node:ekr.20061109120726:leoFrame.mustBeDefinedOnlyInBaseClass
    #@+node:ekr.20061109120704:leoFrame.mustBeDefinedInSubclasses
    mustBeDefinedInSubclasses = (
        #Gui-dependent commands.
        'cascade',
        'contractBodyPane',
        'contractLogPane',
        'contractOutlinePane',
        'contractPane',
        'equalSizedPanes',
        'expandLogPane',
        'expandPane',
        'fullyExpandBodyPane',
        'fullyExpandLogPane',
        'fullyExpandOutlinePane',
        'fullyExpandPane',
        'hideBodyPane',
        'hideLogPane',
        'hideLogWindow',
        'hideOutlinePane',
        'hidePane',
        'leoHelp',
        'minimizeAll',
        'resizeToScreen',
        'toggleActivePane',
        'toggleSplitDirection',
        # Windowutilities...
        'bringToFront',
        'deiconify',
        'get_window_info',
        'lift',
        'update',
        # Config...
        'resizePanesToRatio',
        'setInitialWindowGeometry',
        'setTopGeometry',
    )
    #@nonl
    #@-node:ekr.20061109120704:leoFrame.mustBeDefinedInSubclasses
    #@-node:ekr.20031218072017.3679:  leoFrame.__init__
    #@+node:ekr.20031218072017.3680:Must be defined in subclasses
    #@+node:ekr.20031218072017.3683:Config...
    def resizePanesToRatio (self,ratio,secondary_ratio):    self.oops()
    def setInitialWindowGeometry (self):                    self.oops()
    
    def setTopGeometry (self,w,h,x,y,adjustSize=True):
        __pychecker__ = '--no-argsused' # adjustSize used in derived classes.
        self.oops()
    #@-node:ekr.20031218072017.3683:Config...
    #@+node:ekr.20031218072017.3681:Gui-dependent commands
    # In the Edit menu...
    
    def OnCopy  (self,event=None): self.oops()
    def OnCut   (self,event=None): self.oops()
    def OnCutFromMenu  (self,event=None):     self.oops()
    def OnCopyFromMenu (self,event=None):     self.oops()
    
    # Expanding and contracting panes.
    def contractPane         (self,event=None): self.oops()
    def expandPane           (self,event=None): self.oops()
    def contractBodyPane     (self,event=None): self.oops()
    def contractLogPane      (self,event=None): self.oops()
    def contractOutlinePane  (self,event=None): self.oops()
    def expandLogPane        (self,event=None): self.oops()
    def fullyExpandBodyPane  (self,event=None): self.oops()
    def fullyExpandLogPane   (self,event=None): self.oops()
    def fullyExpandPane      (self,event=None): self.oops()
    def fullyExpandOutlinePane (self,event=None): self.oops()
    def hideBodyPane         (self,event=None): self.oops()
    def hideLogPane          (self,event=None): self.oops()
    def hidePane             (self,event=None): self.oops()
    def hideOutlinePane      (self,event=None): self.oops()
        
    expandBodyPane = contractOutlinePane
    expandOutlinePane = contractBodyPane
    
    # In the Window menu...
    def cascade              (self,event=None): self.oops()
    def equalSizedPanes      (self,event=None): self.oops()
    def hideLogWindow        (self,event=None): self.oops()
    def minimizeAll          (self,event=None): self.oops()
    def resizeToScreen       (self,event=None): self.oops()
    def toggleActivePane     (self,event=None): self.oops()
    def toggleSplitDirection (self,event=None): self.oops()
    
    # In help menu...
    def leoHelp (self,event=None): self.oops()
    #@-node:ekr.20031218072017.3681:Gui-dependent commands
    #@+node:ekr.20031218072017.3682:Window...
    # Important: nothing would be gained by calling gui versions of these methods:
    #            they can be defined in a gui-dependent way in a subclass.
    
    def bringToFront (self):    self.oops()
    def deiconify (self):       self.oops()
    def get_window_info(self):  self.oops()
    def lift (self):            self.oops()
    def update (self):          self.oops()
    #@-node:ekr.20031218072017.3682:Window...
    #@-node:ekr.20031218072017.3680:Must be defined in subclasses
    #@+node:ekr.20061109125528:May be defined in subclasses
    #@+node:ekr.20031218072017.3687:setTabWidth
    def setTabWidth (self,w):
        
        # Subclasses may override this to affect drawing.
        self.tab_width = w
    #@-node:ekr.20031218072017.3687:setTabWidth
    #@+node:ekr.20031218072017.3688:getTitle & setTitle
    def getTitle (self):
        return self.title
        
    def setTitle (self,title):
        self.title = title
    #@-node:ekr.20031218072017.3688:getTitle & setTitle
    #@-node:ekr.20061109125528:May be defined in subclasses
    #@+node:ekr.20061109125528.1:Must be defined in base class
    #@+node:ekr.20031218072017.3689:initialRatios
    def initialRatios (self):
        
        c = self.c
    
        s = c.config.get("initial_splitter_orientation","string")
        verticalFlag = s == None or (s != "h" and s != "horizontal")
    
        if verticalFlag:
            r = c.config.getRatio("initial_vertical_ratio")
            if r == None or r < 0.0 or r > 1.0: r = 0.5
            r2 = c.config.getRatio("initial_vertical_secondary_ratio")
            if r2 == None or r2 < 0.0 or r2 > 1.0: r2 = 0.8
        else:
            r = c.config.getRatio("initial_horizontal_ratio")
            if r == None or r < 0.0 or r > 1.0: r = 0.3
            r2 = c.config.getRatio("initial_horizontal_secondary_ratio")
            if r2 == None or r2 < 0.0 or r2 > 1.0: r2 = 0.8
    
        # g.trace(r,r2)
        return verticalFlag,r,r2
    #@-node:ekr.20031218072017.3689:initialRatios
    #@+node:ekr.20031218072017.3690:longFileName & shortFileName
    def longFileName (self):
    
        return self.c.mFileName
        
    def shortFileName (self):
    
        return g.shortFileName(self.c.mFileName)
    #@-node:ekr.20031218072017.3690:longFileName & shortFileName
    #@+node:ekr.20031218072017.3691:oops
    def oops(self):
        
        print "leoFrame oops:", g.callers(3), "should be overridden in subclass"
    #@-node:ekr.20031218072017.3691:oops
    #@+node:ekr.20031218072017.3692:promptForSave
    def promptForSave (self):
        
        """Prompt the user to save changes.
        
        Return True if the user vetos the quit or save operation."""
        
        c = self.c
        name = g.choose(c.mFileName,c.mFileName,self.title)
        theType = g.choose(g.app.quitting, "quitting?", "closing?")
    
        answer = g.app.gui.runAskYesNoCancelDialog(c,
            "Confirm",
            'Save changes to %s before %s' % (name,theType))
            
        # print answer
        if answer == "cancel":
            return True # Veto.
        elif answer == "no":
            return False # Don't save and don't veto.
        else:
            if not c.mFileName:
                #@            << Put up a file save dialog to set mFileName >>
                #@+node:ekr.20031218072017.3693:<< Put up a file save dialog to set mFileName >>
                # Make sure we never pass None to the ctor.
                if not c.mFileName:
                    c.mFileName = ""
                
                c.mFileName = g.app.gui.runSaveFileDialog(
                    initialfile = c.mFileName,
                    title="Save",
                    filetypes=[("Leo files", "*.leo")],
                    defaultextension=".leo")
                c.bringToFront()
                #@-node:ekr.20031218072017.3693:<< Put up a file save dialog to set mFileName >>
                #@nl
            if c.mFileName:
                ok = c.fileCommands.save(c.mFileName)
                return not ok # New in 4.2: Veto if the save did not succeed.
            else:
                return True # Veto.
    #@-node:ekr.20031218072017.3692:promptForSave
    #@+node:ekr.20031218072017.1375:scanForTabWidth
    # Similar to code in scanAllDirectives.
    
    def scanForTabWidth (self,p):
    
        c = self.c ; w = c.tab_width
    
        for p in p.self_and_parents_iter():
            s = p.v.t.bodyString
            theDict = g.get_directives_dict(s)
            #@        << set w and break on @tabwidth >>
            #@+node:ekr.20031218072017.1376:<< set w and break on @tabwidth >>
            if theDict.has_key("tabwidth"):
                
                val = g.scanAtTabwidthDirective(s,theDict,issue_error_flag=False)
                if val and val != 0:
                    w = val
                    break
            #@-node:ekr.20031218072017.1376:<< set w and break on @tabwidth >>
            #@nl
    
        c.frame.setTabWidth(w)
    #@-node:ekr.20031218072017.1375:scanForTabWidth
    #@+node:ekr.20061119120006:Icon area convenience methods
    def addIconButton (self,*args,**keys):
        return self.iconBar and self.iconBar.add(*args,**keys)
    
    def clearIconBar (self):
        self.iconBar and self.iconBar.clear()
    
    def createIconBar (self):
        if not self.iconBar:
            self.iconBar = self.iconBarClass(self.c,self.outerFrame)
        return self.iconBar
        
    def getIconBar(self):
        if not self.iconBar:
            self.iconBar = self.iconBarClass(self.c,self.outerFrame)
        return self.iconBar
    
    getIconBarObject = getIconBar
    
    def hideIconBar (self):
        self.iconBar and self.iconBar.hide()
    #@nonl
    #@-node:ekr.20061119120006:Icon area convenience methods
    #@+node:ekr.20041223105114.1:Status line convenience methods
    def createStatusLine (self):
        if not self.statusLine:
            self.statusLine  = self.statusLineClass(self.c,self.outerFrame)
        return self.statusLine
    
    def clearStatusLine (self):
        self.statusLine and self.statusLine.clear()
        
    def disableStatusLine (self,background=None):
        self.statusLine and self.statusLine.disable(background)
    
    def enableStatusLine (self,background="white"):
        self.statusLine and self.statusLine.enable(background)
    
    def getStatusLine (self):
        return self.statusLine
        
    getStatusObject = getStatusLine
        
    def putStatusLine (self,s,color=None):
        self.statusLine and self.statusLine.put(s,color)
        
    def setFocusStatusLine (self):
        self.statusLine and self.statusLine.setFocus()
    
    def statusLineIsEnabled(self):
        return self.statusLine and self.statusLine.isEnabled()
        
    def updateStatusLine(self):
        self.statusLine and self.statusLine.update()
    #@nonl
    #@-node:ekr.20041223105114.1:Status line convenience methods
    #@+node:ekr.20070130115927.4:Cut/Copy/Paste (leoFrame)
    #@+node:ekr.20070130115927.5:copyText
    def copyText (self,event=None):
        
        '''Copy the selected text from the widget to the clipboard.'''
        
        f = self ; c = f.c ; w = event and event.widget
        if not w or not g.app.gui.isTextWidget(w): return
    
        # Set the clipboard text.
        i,j = w.getSelectionRange()
        if i != j:
            s = w.get(i,j)
            g.app.gui.replaceClipboardWith(s)
            
    OnCopyFromMenu = copyText
    #@-node:ekr.20070130115927.5:copyText
    #@+node:ekr.20070130115927.6:leoFrame.cutText
    def cutText (self,event=None):
        
        '''Invoked from the mini-buffer and from shortcuts.'''
    
        f = self ; c = f.c ; w = event and event.widget
        if not w or not g.app.gui.isTextWidget(w): return
    
        name = c.widget_name(w)
        oldSel = w.getSelectionRange()
        oldText = w.getAllText()
        i,j = w.getSelectionRange()
        
        # Update the widget and set the clipboard text.
        s = w.get(i,j)
        if i != j:
            w.delete(i,j)
            g.app.gui.replaceClipboardWith(s)
    
        if name.startswith('body'):
            c.frame.body.forceFullRecolor()
            c.frame.body.onBodyChanged('Cut',oldSel=oldSel,oldText=oldText)
        elif name.startswith('head'):
            # The headline is not officially changed yet.
            # p.initHeadString(s)
            s = w.getAllText()
            width = f.tree.headWidth(p=None,s=s)
            w.setWidth(width)
        else: pass
    
    OnCutFromMenu = cutText
    #@-node:ekr.20070130115927.6:leoFrame.cutText
    #@+node:ekr.20070130115927.7:leoFrame.pasteText
    def pasteText (self,event=None,middleButton=False):
    
        '''Paste the clipboard into a widget.
        If middleButton is True, support x-windows middle-mouse-button easter-egg.'''
    
        f = self ; c = f.c ; w = event and event.widget
        if not w or not g.app.gui.isTextWidget(w): return
    
        wname = c.widget_name(w)
        i,j = oldSel = w.getSelectionRange()  # Returns insert point if no selection.
        oldText = w.getAllText()
        
        # print 'pasteText',i,j,middleButton,wname,repr(c.k.previousSelection)
        
        if middleButton and c.k.previousSelection is not None:
            start,end = c.k.previousSelection
            s = w.getAllText()
            s = s[start:end]
            c.k.previousSelection = None
        else:
            s = s1 = g.app.gui.getTextFromClipboard()
        
        singleLine = wname.startswith('head') or wname.startswith('minibuffer')
        
        if singleLine:
            # Strip trailing newlines so the truncation doesn't cause confusion.
            while s and s [ -1] in ('\n','\r'):
                s = s [: -1]
    
        try:
            # Update the widget.
            if i != j:
                w.delete(i,j)
            w.insert(i,s)
        
            if wname.startswith('body'):
                c.frame.body.forceFullRecolor()
                c.frame.body.onBodyChanged('Paste',oldSel=oldSel,oldText=oldText)
            elif singleLine:
                s = w.getAllText()
                while s and s [ -1] in ('\n','\r'):
                    s = s [: -1]
                if wname.startswith('head'):
                    # The headline is not officially changed yet.
                    # p.initHeadString(s)
                    width = f.tree.headWidth(p=None,s=s)
                    w.setWidth(width)
            else: pass
        except Exception:
            pass # Tk sometimes throws weird exceptions here.
            
        return 'break' # Essential
    
    OnPasteFromMenu = pasteText
    #@-node:ekr.20070130115927.7:leoFrame.pasteText
    #@+node:ekr.20061016071937:OnPaste (To support middle-button paste)
    def OnPaste (self,event=None):
        
        return self.pasteText(event=event,middleButton=True)
    #@nonl
    #@-node:ekr.20061016071937:OnPaste (To support middle-button paste)
    #@-node:ekr.20070130115927.4:Cut/Copy/Paste (leoFrame)
    #@+node:ekr.20031218072017.3980:Edit Menu... (leoFrame)
    #@+node:ekr.20031218072017.3981:abortEditLabelCommand
    def abortEditLabelCommand (self,event=None):
        
        '''End editing of a headline and revert to its previous value.'''
        
        frame = self ; c = frame.c ; tree = frame.tree
        p = c.currentPosition() ; w = c.edit_widget(p)
        
        if g.app.batchMode:
            c.notValidInBatchMode("Abort Edit Headline")
            return
            
        # g.trace('isEditing',p == tree.editPosition(),'revertHeadline',repr(tree.revertHeadline))
            
        if w and p == tree.editPosition():
            # Revert the headline text.
            w.delete(0,"end")
            w.insert("end",tree.revertHeadline)
            p.initHeadString(tree.revertHeadline)
            c.beginUpdate()
            try:
                c.endEditing()
                c.selectPosition(p)
            finally:
                c.endUpdate()
    #@-node:ekr.20031218072017.3981:abortEditLabelCommand
    #@+node:ekr.20031218072017.3982:endEditLabelCommand
    def endEditLabelCommand (self,event=None):
        
        '''End editing of a headline and move focus to the body pane.'''
    
        frame = self ; c = frame.c
        if g.app.batchMode:
            c.notValidInBatchMode("End Edit Headline")
        else:
            c.endEditing()
            if c.config.getBool('stayInTreeAfterEditHeadline'):
                c.treeWantsFocusNow()
            else:
                c.bodyWantsFocusNow()
    #@nonl
    #@-node:ekr.20031218072017.3982:endEditLabelCommand
    #@+node:ekr.20031218072017.3983:insertHeadlineTime
    def insertHeadlineTime (self,event=None):
        
        '''Insert a date/time stamp in the headline of the selected node.'''
    
        frame = self ; c = frame.c ; p = c.currentPosition()
        
        if g.app.batchMode:
            c.notValidInBatchMode("Insert Headline Time")
            return
            
        c.editPosition(p)
        c.frame.tree.setEditLabelState(p)
        w = c.edit_widget(p)
        if w:
            time = c.getTime(body=False)
            if 1: # We can't know if we were already editing, so insert at end.
                w.setSelectionRange('end','end')
                w.insert('end',time)
            else:
                i, j = w.getSelectionRange()
                if i != j: w.delete(i,j)
                w.insert("insert",time)
            c.frame.tree.onHeadChanged(p,'Insert Headline Time')
    #@-node:ekr.20031218072017.3983:insertHeadlineTime
    #@-node:ekr.20031218072017.3980:Edit Menu... (leoFrame)
    #@-node:ekr.20061109125528.1:Must be defined in base class
    #@+node:ekr.20060206093313:Focus (leoFrame)
    # For compatibility with old scripts.
    # Using the commander methods directly is recommended.
    
    def getFocus(self):
        return g.app.gui.get_focus(self.c) # Used by wxGui plugin.
    
    def bodyWantsFocus(self):
        return self.c.bodyWantsFocus()
    
    def headlineWantsFocus(self,p):
        return self.c.headlineWantsFocus(p)
    
    def logWantsFocus(self):
        return self.c.logWantsFocus()
    
    def minibufferWantsFocus(self):
        return self.c.minibufferWantsFocus()
    #@-node:ekr.20060206093313:Focus (leoFrame)
    #@-others
#@-node:ekr.20031218072017.3678:class leoFrame
#@+node:ekr.20031218072017.3694:class leoLog
class leoLog:
    
    """The base class for the log pane in Leo windows."""
    
    __pychecker__ = '--no-argsused' # base classes have many unused args.
    
    #@    @+others
    #@+node:ekr.20070114071054:Birth
    #@+node:ekr.20031218072017.3695:leoLog.__init__
    def __init__ (self,frame,parentFrame):
        
        self.frame = frame
        if frame: # 7/16/05: Allow no commander for Null logs.
            self.c = frame.c
        else:
            self.c = None
        self.enabled = True
        self.newlines = 0
        self.isNull = False
    
        # Note: self.logCtrl is None for nullLog's.
        self.logCtrl = self.createControl(parentFrame)
        self.setFontFromConfig()
        self.setColorFromConfig()
    #@-node:ekr.20031218072017.3695:leoLog.__init__
    #@+node:ekr.20031218072017.3698:leoLog.createControl
    def createControl (self,parentFrame):
        
        self.oops()
    #@-node:ekr.20031218072017.3698:leoLog.createControl
    #@+node:ekr.20070114070939.1:leoLog.finishCreate (may be overridden)
    def finishCreate (self):
        
        pass
    #@nonl
    #@-node:ekr.20070114070939.1:leoLog.finishCreate (may be overridden)
    #@-node:ekr.20070114071054:Birth
    #@+node:ekr.20031218072017.3696:leoLog.configure
    def configure (self,*args,**keys):
        
        __pychecker__ = '--no-argsused'
        
        self.oops()
    #@-node:ekr.20031218072017.3696:leoLog.configure
    #@+node:ekr.20031218072017.3697:leoLog.configureBorder
    def configureBorder(self,border):
        
        self.oops()
    #@-node:ekr.20031218072017.3697:leoLog.configureBorder
    #@+node:ekr.20031218072017.3699:leoLog.enable & disable
    def enable (self,enabled=True):
        
        self.enabled = enabled
        
    def disable (self):
        
        self.enabled = False
    #@-node:ekr.20031218072017.3699:leoLog.enable & disable
    #@+node:ekr.20031218072017.3700:leoLog.oops
    def oops (self):
        
        print "leoLog oops:", g.callers(), "should be overridden in subclass"
    #@-node:ekr.20031218072017.3700:leoLog.oops
    #@+node:ekr.20031218072017.3701:leoLog.setFontFromConfig & setColorFromConfig
    def setFontFromConfig (self):
        
        self.oops()
        
    def setColorFromConfig (self):
        
        self.oops()
    #@-node:ekr.20031218072017.3701:leoLog.setFontFromConfig & setColorFromConfig
    #@+node:ekr.20031218072017.3702:leoLog.onActivateLog
    def onActivateLog (self,event=None):
    
        self.c.setLog()
    #@-node:ekr.20031218072017.3702:leoLog.onActivateLog
    #@+node:ekr.20031218072017.3703:leoLog.put & putnl
    # All output to the log stream eventually comes here.
    
    def put (self,s,color=None,tabName='Log'):
        self.oops()
    
    def putnl (self,tabName='Log'):
        self.oops()
    #@-node:ekr.20031218072017.3703:leoLog.put & putnl
    #@-others
#@-node:ekr.20031218072017.3694:class leoLog
#@+node:ekr.20031218072017.3704:class leoTree
# This would be useful if we removed all the tree redirection routines.
# However, those routines are pretty ingrained into Leo...

class leoTree:
    
    """The base class for the outline pane in Leo windows."""
    
    __pychecker__ = '--no-argsused' # base classes have many unused args.
    
    #@    @+others
    #@+node:ekr.20031218072017.3705:  tree.__init__ (base class)
    def __init__ (self,frame):
        
        self.frame = frame
        self.c = frame.c
    
        self.edit_text_dict = {}
            # New in 3.12: keys vnodes, values are edit_widget (Tk.Text widgets)
            # New in 4.2: keys are vnodes, values are pairs (p,Tk.Text).
        
        # "public" ivars: correspond to setters & getters.
        self._editPosition = None
        self.redrawCount = 0 # For traces
    #@+node:ekr.20061109164512:leoTree.mustBeDefinedOnlyInBaseClass
    mustBeDefinedOnlyInBaseClass = (
        # Getters & setters.
        'editPosition',
        'getEditTextDict',
        'setEditPosition',
        # Others.
        'expandAllAncestors',
        'injectCallbacks',
        'OnIconDoubleClick',
        'onHeadChanged',
        'onHeadlineKey',
        'updateHead',
        'oops',
    )
    #@nonl
    #@-node:ekr.20061109164512:leoTree.mustBeDefinedOnlyInBaseClass
    #@+node:ekr.20061109164610:leoTree.mustBeDefinedInSubclasses
    mustBeDefinedInSubclasses = (
        # Colors & fonts.
        'getFont',
        'setColorFromConfig ',
        'setFont',
        'setFontFromConfig ',
        # Drawing & scrolling.
        'drawIcon',
        'redraw_now',
        'scrollTo',
        # Headlines.
        'editLabel',
        'endEditLabel',
        'setEditLabelState',
        # Selecting.
        'select',
    )
    #@-node:ekr.20061109164610:leoTree.mustBeDefinedInSubclasses
    #@-node:ekr.20031218072017.3705:  tree.__init__ (base class)
    #@+node:ekr.20031218072017.3706: Must be defined in subclasses
    # Colors & fonts.
    def getFont(self):                              self.oops()
    def setColorFromConfig (self):                  self.oops()
    def setFont(self,font=None,fontName=None):      self.oops()
    def setFontFromConfig (self):                   self.oops()
    # Drawing & scrolling.
    def drawIcon(self,v,x=None,y=None):             self.oops()
    def redraw_now(self,scroll=True):               self.oops()
    def scrollTo(self,p):                           self.oops()
    idle_scrollTo = scrollTo # For compatibility.
    # Headlines.
    def editLabel(self,v,selectAll=False):          self.oops()
    def endEditLabel(self):                         self.oops()
    def setEditLabelState(self,v,selectAll=False):  self.oops()
    # Selecting & expanding.
    def select(self,p,updateBeadList=True,scroll=True): self.oops()
    #@-node:ekr.20031218072017.3706: Must be defined in subclasses
    #@+node:ekr.20061109165848:Must be defined in base class
    #@+node:ekr.20031218072017.3716:Getters/Setters (tree)
    def getEditTextDict(self,v):
        # New in 4.2: the default is an empty list.
        return self.edit_text_dict.get(v,[])
    
    def editPosition(self):
        return self._editPosition
    
    def setEditPosition(self,p):
        self._editPosition = p
    #@-node:ekr.20031218072017.3716:Getters/Setters (tree)
    #@+node:ekr.20031218072017.2312:tree.OnIconDoubleClick (@url) & helper
    def OnIconDoubleClick (self,p):
    
        # Note: "icondclick" hooks handled by vnode callback routine.
    
        c = self.c
        s = p.headString().strip()
        if g.match_word(s,0,"@url"):
            url = s[4:].strip()
            if url.lstrip().startswith('--'):
                # Get the url from the first body line.
                lines = p.bodyString().split('\n')
                url = lines and lines[0] or ''
            else:
                #@            << stop the url after any whitespace >>
                #@+node:ekr.20031218072017.2313:<< stop the url after any whitespace  >>
                # For safety, the URL string should end at the first whitespace, unless quoted.
                # This logic is also found in the UNL plugin so we don't have to change the 'unl1' hook.
                
                url = url.replace('\t',' ')
                
                # Strip quotes.
                i = -1
                if url and url[0] in ('"',"'"):
                    i = url.find(url[0],1)
                    if i > -1:
                        url = url[1:i]
                
                if i == -1:
                    # Not quoted or no matching quote.
                    i = url.find(' ')
                    if i > -1:
                        if 0: # No need for a warning.  Assume everything else is a comment.
                            g.es("ignoring characters after space in url:"+url[i:])
                            g.es("use %20 instead of spaces")
                        url = url[:i]
                #@-node:ekr.20031218072017.2313:<< stop the url after any whitespace  >>
                #@nl
            if not g.doHook("@url1",c=c,p=p,v=p,url=url):
                self.handleUrlInUrlNode(url)
            g.doHook("@url2",c=c,p=p,v=p)
    
        return 'break' # 11/19/06
    #@nonl
    #@+node:ekr.20061030161842:handleUrlInUrlNode
    def handleUrlInUrlNode(self,url):
        
        # Note: the UNL plugin has its own notion of what a good url is.
        
        c = self.c
        # g.trace(url)
        #@    << check the url; return if bad >>
        #@+node:ekr.20031218072017.2314:<< check the url; return if bad >>
        #@+at 
        #@nonl
        # A valid url is (according to D.T.Hein):
        # 
        # 3 or more lowercase alphas, followed by,
        # one ':', followed by,
        # one or more of: (excludes !"#;<>[\]^`|)
        #   $%&'()*+,-./0-9:=?@A-Z_a-z{}~
        # followed by one of: (same as above, except no minus sign or comma).
        #   $%&'()*+/0-9:=?@A-Z_a-z}~
        #@-at
        #@@c
        
        urlPattern = "[a-z]{3,}:[\$-:=?-Z_a-z{}~]+[\$-+\/-:=?-Z_a-z}~]"
        
        if not url or len(url) == 0:
            g.es("no url following @url")
            return
        
        # Add http:// if required.
        if not re.match('^([a-z]{3,}:)',url):
            url = 'http://' + url
        if not re.match(urlPattern,url):
            g.es("invalid url: "+url)
            return
        #@nonl
        #@-node:ekr.20031218072017.2314:<< check the url; return if bad >>
        #@nl
        #@    << pass the url to the web browser >>
        #@+node:ekr.20031218072017.2315:<< pass the url to the web browser >>
        #@+at 
        #@nonl
        # Most browsers should handle the following urls:
        #   ftp://ftp.uu.net/public/whatever.
        #   http://localhost/MySiteUnderDevelopment/index.html
        #   file://home/me/todolist.html
        #@-at
        #@@c
        
        try:
            import os
            os.chdir(g.app.loadDir)
            if g.match(url,0,"file:") and url[-4:]==".leo":
                ok,frame = g.openWithFileName(url[5:],c)
            else:
                import webbrowser
                # Mozilla throws a weird exception, then opens the file!
                try: webbrowser.open(url)
                except: pass
        except:
            g.es("exception opening " + url)
            g.es_exception()
        #@-node:ekr.20031218072017.2315:<< pass the url to the web browser >>
        #@nl
    #@-node:ekr.20061030161842:handleUrlInUrlNode
    #@-node:ekr.20031218072017.2312:tree.OnIconDoubleClick (@url) & helper
    #@+node:ekr.20040803072955.143:tree.expandAllAncestors
    def expandAllAncestors (self,p):
        
        '''Expand all ancestors without redrawing.
        
        Return a flag telling whether a redraw is needed.'''
        
        c = self.c ; redraw_flag = False
    
        c.beginUpdate()
        try:
            for p in p.parents_iter():
                if not p.isExpanded():
                    p.expand()
                    redraw_flag = True
        finally:
            c.endUpdate(False)
    
        return redraw_flag
    #@-node:ekr.20040803072955.143:tree.expandAllAncestors
    #@+node:ekr.20040803072955.21:tree.injectCallbacks
    def injectCallbacks(self):
        
        c = self.c
        
        #@    << define callbacks to be injected in the position class >>
        #@+node:ekr.20040803072955.22:<< define callbacks to be injected in the position class >>
        # N.B. These vnode methods are entitled to know about details of the leoTkinterTree class.
        
        #@+others
        #@+node:ekr.20040803072955.23:OnHyperLinkControlClick
        def OnHyperLinkControlClick (self,event=None,c=c):
            
            """Callback injected into position class."""
            
            p = self
            try:
                if not g.doHook("hypercclick1",c=c,p=p,v=p,event=event):
                    c.beginUpdate()
                    try:
                        c.selectPosition(p)
                    finally:
                        c.endUpdate()
                    c.frame.bodyCtrl.setInsertPoint(0)
                g.doHook("hypercclick2",c=c,p=p,v=p,event=event)
            except:
                g.es_event_exception("hypercclick")
        #@-node:ekr.20040803072955.23:OnHyperLinkControlClick
        #@+node:ekr.20040803072955.24:OnHyperLinkEnter
        def OnHyperLinkEnter (self,event=None,c=c):
            
            """Callback injected into position class."""
        
            try:
                p = self
                if not g.doHook("hyperenter1",c=c,p=p,v=p,event=event):
                    if 0: # This works, and isn't very useful.
                        c.frame.bodyCtrl.tag_config(p.tagName,background="green")
                g.doHook("hyperenter2",c=c,p=p,v=p,event=event)
            except:
                g.es_event_exception("hyperenter")
        #@-node:ekr.20040803072955.24:OnHyperLinkEnter
        #@+node:ekr.20040803072955.25:OnHyperLinkLeave
        def OnHyperLinkLeave (self,event=None,c=c):
            
            """Callback injected into position class."""
        
            try:
                p = self
                if not g.doHook("hyperleave1",c=c,p=p,v=p,event=event):
                    if 0: # This works, and isn't very useful.
                        c.frame.bodyCtrl.tag_config(p.tagName,background="white")
                g.doHook("hyperleave2",c=c,p=p,v=p,event=event)
            except:
                g.es_event_exception("hyperleave")
        #@-node:ekr.20040803072955.25:OnHyperLinkLeave
        #@-others
        #@-node:ekr.20040803072955.22:<< define callbacks to be injected in the position class >>
        #@nl
    
        for f in (OnHyperLinkControlClick,OnHyperLinkEnter,OnHyperLinkLeave):
            
            g.funcToMethod(f,leoNodes.position)
    #@nonl
    #@-node:ekr.20040803072955.21:tree.injectCallbacks
    #@+node:ekr.20040803072955.90:head key handlers
    #@+node:ekr.20040803072955.91:onHeadChanged
    # Tricky code: do not change without careful thought and testing.
    
    def onHeadChanged (self,p,undoType='Typing',s=None):
        
        '''Officially change a headline.
        Set the old undo text to the previous revert point.'''
        
        c = self.c ; u = c.undoer ; w = c.edit_widget(p)
        if not w: return
        
        ch = '\n' # New in 4.4: we only report the final keystroke.
        if g.doHook("headkey1",c=c,p=p,v=p,ch=ch):
            return # The hook claims to have handled the event.
    
        if s is None: s = w.getAllText()
        #@    << truncate s if it has multiple lines >>
        #@+node:ekr.20040803072955.94:<< truncate s if it has multiple lines >>
        # Remove one or two trailing newlines before warning of truncation.
        for i in (0,1):
            if s and s[-1] == '\n':
                if len(s) > 1: s = s[:-1]
                else: s = ''
        
        # Warn if there are multiple lines.
        i = s.find('\n')
        if i > -1:
            # g.trace(i,len(s),repr(s))
            g.es("Truncating headline to one line",color="blue")
            s = s[:i]
        
        limit = 1000
        if len(s) > limit:
            g.es("Truncating headline to %d characters" % (limit),color="blue")
            s = s[:limit]
        
        s = g.toUnicode(s or '',g.app.tkEncoding)
        #@-node:ekr.20040803072955.94:<< truncate s if it has multiple lines >>
        #@nl
        c.beginUpdate()
        try:
            # Make the change official, but undo to the *old* revert point.
            oldRevert = self.revertHeadline
            changed = s != oldRevert
            self.revertHeadline = s
            p.initHeadString(s)
            # if self.trace_edit and not g.app.unitTesting:
                # if changed:
                    # g.trace('changed: old',repr(oldRevert),'new',repr(s))
            if changed:
                undoData = u.beforeChangeNodeContents(p,oldHead=oldRevert)
                if not c.changed: c.setChanged(True)
                dirtyVnodeList = p.setDirty()
                u.afterChangeNodeContents(p,undoType,undoData,
                    dirtyVnodeList=dirtyVnodeList)
        finally:
            c.endUpdate(scroll=False) # New in 4.4.1
            if changed:
                if self.stayInTree:
                    c.treeWantsFocus()
                else:
                    c.bodyWantsFocus()
       
        g.doHook("headkey2",c=c,p=p,v=p,ch=ch)
    #@-node:ekr.20040803072955.91:onHeadChanged
    #@+node:ekr.20040803072955.88:onHeadlineKey
    def onHeadlineKey (self,event):
        
        '''Handle a key event in a headline.'''
    
        w = event and event.widget or None
        ch = event and event.char or ''
        
        # g.trace(repr(ch),g.callers())
    
        # Testing for ch here prevents flashing in the headline
        # when the control key is held down.
        if ch:
            # g.trace(repr(ch),g.callers())
            self.updateHead(event,w)
    
        return 'break' # Required
    #@-node:ekr.20040803072955.88:onHeadlineKey
    #@+node:ekr.20051026083544.2:updateHead
    def updateHead (self,event,w):
        
        '''Update a headline from an event.
        
        The headline officially changes only when editing ends.'''
        
        c = self.c ; k = c.k
        ch = event and event.char or ''
        i,j = w.getSelectionRange()
        ins = w.getInsertPoint()
        if i != j: ins = i
        
        # g.trace('ch',repr(ch),g.callers())
    
        if ch == '\b':
            if i != j:  w.delete(i,j)
            else:       w.delete(ins-1)
            w.setSelectionRange(i,i,insert=i)
        elif ch and ch not in ('\n','\r'):
            if i != j:                              w.delete(i,j)
            elif k.unboundKeyAction == 'overwrite': w.delete(i,i+1)
            w.insert(ins,ch)
            w.setSelectionRange(ins+1,ins+1,insert=ins+1)
    
        s = w.getAllText()
        if s.endswith('\n'):
            # g.trace('can not happen: trailing newline')
            s = s[:-1]
        w.setWidth(self.headWidth(s=s))
    
        if ch in ('\n','\r'):
            self.endEditLabel() # Now calls self.onHeadChanged.
    #@-node:ekr.20051026083544.2:updateHead
    #@-node:ekr.20040803072955.90:head key handlers
    #@-node:ekr.20061109165848:Must be defined in base class
    #@+node:ekr.20031218072017.3718:oops
    def oops(self):
        
        print "leoTree oops:", g.callers(), "should be overridden in subclass"
    #@-node:ekr.20031218072017.3718:oops
    #@-others
#@-node:ekr.20031218072017.3704:class leoTree
#@+node:ekr.20031218072017.2191:class nullBody
class nullBody (leoBody):
    
    __pychecker__ = '--no-argsused' # null classes have many unused args.

    #@    @+others
    #@+node:ekr.20031218072017.2192: nullBody.__init__
    def __init__ (self,frame,parentFrame):
        
        leoBody.__init__ (self,frame,parentFrame) # Init the base class.
    
        self.insertPoint = 0
        self.selection = 0,0
        self.s = "" # The body text
        
        self.colorizer = leoColor.nullColorizer(self.c)
    #@-node:ekr.20031218072017.2192: nullBody.__init__
    #@+node:ekr.20031218072017.2193:Utils (internal use)
    #@+node:ekr.20031218072017.2194:findStartOfLine
    def findStartOfLine (self,lineNumber):
        
        lines = g.splitLines(self.s)
        i = 0 ; index = 0
        for line in lines:
            if i == lineNumber: break
            i += 1
            index += len(line)
        return index
    #@-node:ekr.20031218072017.2194:findStartOfLine
    #@+node:ekr.20031218072017.2195:scanToStartOfLine
    def scanToStartOfLine (self,i):
        
        if i <= 0:
            return 0
            
        assert(self.s[i] != '\n')
        
        while i >= 0:
            if self.s[i] == '\n':
                return i + 1
        
        return 0
    #@-node:ekr.20031218072017.2195:scanToStartOfLine
    #@+node:ekr.20031218072017.2196:scanToEndOfLine
    def scanToEndOfLine (self,i):
        
        if i >= len(self.s):
            return len(self.s)
            
        assert(self.s[i] != '\n')
        
        while i < len(self.s):
            if self.s[i] == '\n':
                return i - 1
        
        return i
    #@-node:ekr.20031218072017.2196:scanToEndOfLine
    #@-node:ekr.20031218072017.2193:Utils (internal use)
    #@+node:ekr.20031218072017.2197:nullBody: leoBody interface
    # Birth, death & config
    def bind(self,*args,**keys):                pass
    def createBindings (self,w=None):           pass
    def createControl (self,frame,parentFrame,p): pass
    def setColorFromConfig (self,w=None):       pass
    def setFontFromConfig (self,w=None):        pass
    # Editors...
    def addEditor (self,event=None):            pass
    def createLabel (self,w):                   pass
    def cycleEditorFocus (self,event=None):     pass
    def deleteEditor (self,event=None):         pass
    def selectEditor(self,w):                   pass
    def selectLabel (self,w):                   pass
    def setEditorColors (self,bg,fg):           pass
    def selectMainEditor (self,p):              pass
    def unselectLabel (self,w):                 pass
    def updateEditors (self):                   pass
    # Events...
    def onBodyChanged (self,undoType,oldSel=None,oldText=None,oldYview=None): pass
    def scheduleIdleTimeRoutine (self,function,*args,**keys): pass
    # Low-level gui...
    def getBodyPaneHeight (self):               return 500
    def getBodyPaneWidth (self):                return 600
    def hasFocus (self):                        pass
    def setFocus (self):                        pass
    def tag_add (self,tagName,index1,index2):   pass
    def tag_bind (self,tagName,event,callback): pass
    def tag_configure (self,colorName,**keys):  pass
    def tag_delete(self,tagName):               pass
    def tag_remove (self,tagName,index1,index2):pass
    #@-node:ekr.20031218072017.2197:nullBody: leoBody interface
    #@-others
#@-node:ekr.20031218072017.2191:class nullBody
#@+node:ekr.20031218072017.2222:class nullFrame
class nullFrame (leoFrame):
    
    """A null frame class for tests and batch execution."""
    
    __pychecker__ = '--no-argsused' # null classes have many unused args.
    
    #@    @+others
    #@+node:ekr.20040327105706: ctor
    def __init__ (self,title,gui,useNullUndoer=False):
    
        leoFrame.__init__(self,gui) # Init the base class.
        assert(self.c is None)
        
        self.isNullFrame = True
        self.title = title
        self.useNullUndoer = useNullUndoer
        
        # Default window position.
        self.w = 600
        self.h = 500
        self.x = 40
        self.y = 40
    #@-node:ekr.20040327105706: ctor
    #@+node:ekr.20041120073824:destroySelf
    def destroySelf (self):
        
        pass
    #@-node:ekr.20041120073824:destroySelf
    #@+node:ekr.20040327105706.2:finishCreate
    def finishCreate(self,c):
    
        self.c = c
    
        # Create do-nothing component objects.
        self.tree = nullTree(frame=self)
        self.body = nullBody(frame=self,parentFrame=None)
        self.log  = nullLog (frame=self,parentFrame=None)
        self.menu = leoMenu.nullMenu(frame=self)
        
        assert(c.undoer)
        if self.useNullUndoer:
            c.undoer = leoUndo.nullUndoer(c)
    #@-node:ekr.20040327105706.2:finishCreate
    #@+node:ekr.20061109124552:Overrides
    #@+node:ekr.20061109123828:Config...
    def resizePanesToRatio (self,ratio,secondary_ratio):    pass
    def setInitialWindowGeometry (self):                    pass
    def setMinibufferBindings(self):                        pass
    #@+node:ekr.20041130065718.1:setTopGeometry
    def setTopGeometry (self,w,h,x,y,adjustSize=True):
        
        __pychecker__ = '--no-argsused' # adjustSize used in derived classes.
        
        self.w = w
        self.h = h
        self.x = x
        self.y = y
    #@-node:ekr.20041130065718.1:setTopGeometry
    #@-node:ekr.20061109123828:Config...
    #@+node:ekr.20061109124129:Gui-dependent commands
    # Expanding and contracting panes.
    def contractPane         (self,event=None): pass
    def expandPane           (self,event=None): pass
    def contractBodyPane     (self,event=None): pass
    def contractLogPane      (self,event=None): pass
    def contractOutlinePane  (self,event=None): pass
    def expandLogPane        (self,event=None): pass
    def fullyExpandBodyPane  (self,event=None): pass
    def fullyExpandLogPane   (self,event=None): pass
    def fullyExpandPane      (self,event=None): pass
    def fullyExpandOutlinePane (self,event=None): pass
    def hideBodyPane         (self,event=None): pass
    def hideLogPane          (self,event=None): pass
    def hidePane             (self,event=None): pass
    def hideOutlinePane      (self,event=None): pass
        
    expandBodyPane = contractOutlinePane
    expandOutlinePane = contractBodyPane
    
    # In the Window menu...
    def cascade              (self,event=None): pass
    def equalSizedPanes      (self,event=None): pass
    def hideLogWindow        (self,event=None): pass
    def minimizeAll          (self,event=None): pass
    def resizeToScreen       (self,event=None): pass
    def toggleActivePane     (self,event=None): pass
    def toggleSplitDirection (self,event=None): pass
    
    # In help menu...
    def leoHelp (self,event=None): pass
    #@nonl
    #@-node:ekr.20061109124129:Gui-dependent commands
    #@+node:ekr.20041130065921:Window...
    def bringToFront (self):    pass
    def deiconify (self):       pass
    def get_window_info(self):  pass
    def lift (self):            pass
    def update (self):          pass
    #@-node:ekr.20041130065921:Window...
    #@-node:ekr.20061109124552:Overrides
    #@-others
#@-node:ekr.20031218072017.2222:class nullFrame
#@+node:ekr.20031218072017.2232:class nullLog
class nullLog (leoLog):
    
    __pychecker__ = '--no-argsused' # null classes have many unused args.
    
    #@    @+others
    #@+node:ekr.20041012083237:nullLog.__init__
    def __init__ (self,frame=None,parentFrame=None):
            
        # Init the base class.
        leoLog.__init__(self,frame,parentFrame)
        self.isNull = True
    #@-node:ekr.20041012083237:nullLog.__init__
    #@+node:ekr.20041012083237.1:createControl
    def createControl (self,parentFrame):
        
        return None
    #@-node:ekr.20041012083237.1:createControl
    #@+node:ekr.20041012083237.2:oops
    def oops(self):
    
        g.trace("nullLog:", g.callers())
    #@-node:ekr.20041012083237.2:oops
    #@+node:ekr.20041012083237.3:put and putnl (nullLog)
    def put (self,s,color=None,tabName='Log'):
        if self.enabled:
            # g.trace('nullLog',s)
            g.rawPrint(s)
    
    def putnl (self,tabName='Log'):
        if self.enabled:
            g.rawPrint("")
    #@-node:ekr.20041012083237.3:put and putnl (nullLog)
    #@+node:ekr.20060124085830:tabs
    def clearTab        (self,tabName):     pass
    def createTab (self,tabName,createText=True,wrap='none'): pass
    def deleteTab       (self,tabName,force=False):     pass
    def getSelectedTab          (self):     pass
    def lowerTab        (self,tabName):     pass
    def raiseTab        (self,tabName):     pass
    def renameTab (self,oldName,newName):   pass
    def selectTab (self,tabName,createText=True,wrap='none'): pass
    def setTabBindings  (self,tabName):     pass
    #@-node:ekr.20060124085830:tabs
    #@+node:ekr.20041012083237.4:setColorFromConfig & setFontFromConfig
    def setFontFromConfig (self):
        pass
        
    def setColorFromConfig (self):
        pass
    #@-node:ekr.20041012083237.4:setColorFromConfig & setFontFromConfig
    #@-others
#@-node:ekr.20031218072017.2232:class nullLog
#@+node:ekr.20031218072017.2233:class nullTree
class nullTree (leoTree):
    
    __pychecker__ = '--no-argsused' # null classes have many unused args.

    #@    @+others
    #@+node:ekr.20031218072017.2234: nullTree.__init__
    def __init__ (self,frame):
        
        leoTree.__init__(self,frame) # Init the base class.
        
        assert(self.frame)
        self.font = None
        self.fontName = None
        self.canvas = None
    #@-node:ekr.20031218072017.2234: nullTree.__init__
    #@+node:ekr.20031218072017.2236:Overrides
    # Colors & fonts.
    def getFont(self):                              return self.font
    def setColorFromConfig (self):                  pass
    def setBindings (self):                         pass
    def setFont(self,font=None,fontName=None):      self.font,self.fontName = font,fontName
    def setFontFromConfig (self):                   pass
    # Drawing & scrolling.
    def beginUpdate (self):                         pass
    def endUpdate (self,flag,scroll=False):         pass
    def drawIcon(self,v,x=None,y=None):             pass
    def redraw_now(self,scroll=True):               pass
    def scrollTo(self,p):                           pass
    # Headlines.
    def editLabel(self,v,selectAll=False):          pass
    def endEditLabel(self):                         pass
    def setEditLabelState(self,v,selectAll=False):  pass
    # Selecting.
    def select(self,p,updateBeadList=True,scroll=True):
        self.c.setCurrentPosition(p)
        self.frame.scanForTabWidth(p)
    #@-node:ekr.20031218072017.2236:Overrides
    #@-others
#@-node:ekr.20031218072017.2233:class nullTree
#@-others
#@-node:ekr.20031218072017.3655:@thin leoFrame.py
#@-leo
