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
        self.forceFullRecolorFlag = False
        frame.body = self
        
        # May be overridden in subclasses...
        self.bodyCtrl = self
        self.numberOfEditors = 1
        
        # Must be overridden in subclasses...
        self.colorizer = None
        
    #@nonl
    #@+node:ekr.20031218072017.3660:leoBody.mustBeDefinedInSubclasses
    mustBeDefinedInSubclasses = (
        # Birth, death & config.
        '__init__',
        'cget',
        'configure',
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
        'bbox',
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
        'getColorizer',
        'getInsertLines',
        # 'getInsertionPoint',
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
        'scrollDown',
        'scrollUp',
        'see',
        'seeInsertPoint',
        'selectAllText',
        #'setInsertionPoint',
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
    def cget(self,*args,**keys):                    self.oops()
    def configure (self,*args,**keys):              self.oops()
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
    def onBodyChanged (self,undoType,oldSel=None,oldText=None,oldYview=None,python=False): self.oops()
    def scheduleIdleTimeRoutine (self,function,*args,**keys): self.oops()
    # Low-level gui...
    def bbox(self,index):                           self.oops()
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
        
        c = self.c ; k = c.k ; gui = g.app.gui
        w = event and event.widget
        wname = c.widget_name(w)
        
        if wname.startswith('body'):
            # A hack to support middle-button pastes: remember the previous selection.
            k.previousSelection = gui.getSelectionRange(w,python=True)
            x,y = gui.eventXY(event)
            i = gui.xyToPythonIndex(w,x,y)
            # g.trace(x,y,repr(i))
            g.app.gui.setSelectionRange(w,i,i,insert=i,python=True)
            c.editCommands.setMoveCol(w,i,python=True)
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
    #@+node:ekr.20031218072017.4030:getInsertLines (passed)
    def getInsertLines (self):
        
        """Return before,after where:
            
        before is all the lines before the line containing the insert point.
        sel is the line containing the insert point.
        after is all the lines after the line containing the insert point.
        
        All lines end in a newline, except possibly the last line."""
        
        gui = g.app.gui ; w = self.bodyCtrl
        s = gui.getAllText(w)
        insert = gui.getInsertPoint(w,python=True)
        i,j = g.getLine(s,insert)
        before = s[0:i]
        ins = s[i:j]
        after = s[j:]
    
        before = g.toUnicode(before,g.app.tkEncoding)
        ins    = g.toUnicode(ins,   g.app.tkEncoding)
        after  = g.toUnicode(after ,g.app.tkEncoding)
    
        return before,ins,after
    #@-node:ekr.20031218072017.4030:getInsertLines (passed)
    #@+node:ekr.20031218072017.4020:getSelectedText (leoBody)
    def getSelectedText (self):
        
        """Return the selected text of the body frame, converted to unicode."""
    
        return g.app.gui.getSelectedText(self.bodyCtrl)
    #@-node:ekr.20031218072017.4020:getSelectedText (leoBody)
    #@+node:ekr.20031218072017.4031:getSelectionAreas (passed)
    def getSelectionAreas (self):
        
        """Return before,sel,after where:
            
        before is the text before the selected text
        (or the text before the insert point if no selection)
        sel is the selected text (or "" if no selection)
        after is the text after the selected text
        (or the text after the insert point if no selection)"""
    
        gui = g.app.gui ; w = self.bodyCtrl
        
        s = gui.getAllText(w)
        i,j = gui.getSelectionRange(w,python=True)
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
        
        # At present, called only by c.getBodyLines.
        gui = g.app.gui ; w = self.bodyCtrl
        s = gui.getAllText(w)
        i,j = gui.getSelectionRange(w,python=True)
        if i == j:
            i,j = g.getLine(s,i)
        else:
            i,junk = g.getLine(s,i)
            junk,j = g.getLine(s,j)
        #g.trace(i,j,repr(s[i:j]))
        
        before = g.toUnicode(s[0:i],g.app.tkEncoding)
        sel    = g.toUnicode(s[i:j],g.app.tkEncoding)
        after  = g.toUnicode(s[j:len(s)],g.app.tkEncoding)
        return before,sel,after # 3 strings.
    #@-node:ekr.20031218072017.2377:getSelectionLines (leoBody)
    #@+node:ekr.20031218072017.4021:getSelectionRange (leoBody)
    def getSelectionRange (self,sort=True,python=False):
        
        """Return a tuple representing the selected range of body text.
        
        Return a tuple giving the insertion point if no range of text is selected."""
    
        w = self.bodyCtrl
        return g.app.gui.getSelectionRange(w,sort,python)
    #@nonl
    #@-node:ekr.20031218072017.4021:getSelectionRange (leoBody)
    #@+node:ekr.20031218072017.4022:hasTextSelection (leoBody)
    def hasTextSelection (self):
        return g.app.gui.hasSelection(self.bodyCtrl)
    #@-node:ekr.20031218072017.4022:hasTextSelection (leoBody)
    #@+node:ekr.20031218072017.4023:selectAllText (leoBody) (select-all)
    # This is the select-all command.
    
    def selectAllText (self,event=None):
        
        gui = g.app.gui ; w = gui.eventWidget(event) or self.bodyCtrl
        return g.app.gui.selectAllText(w)
    #@-node:ekr.20031218072017.4023:selectAllText (leoBody) (select-all)
    #@+node:ekr.20031218072017.4037:setSelectionAreas (leoBody)
    def setSelectionAreas (self,before,sel,after,python=False):
        
        """Replace the body text by before + sel + after and
        set the selection so that the sel text is selected."""
    
        w = self.bodyCtrl ; gui = g.app.gui
        s = gui.getAllText(w)
        before = before or ''
        sel = sel or ''
        after = after or ''
        gui.rawDelete(w,s,0,len(s),python=True)
        gui.rawInsert(w,s,0,before+sel+after,python=True)
        i,j = len(before),len(before)+len(sel)
        gui.setSelectionRange(w,i,j,insert=j,python=True)
        if python:
            return i,j
        else:
            return gui.toGuiIndex(s,w,i),gui.toGuiIndex(s,w,j)
    #@-node:ekr.20031218072017.4037:setSelectionAreas (leoBody)
    #@+node:ekr.20031218072017.4024:setSelectionRange (leoBody)
    def setSelectionRange (self,i,j=None,insert='sel.end',python=False):
        
        gui = g.app.gui ; w = self.bodyCtrl
        
        # Allow the user to pass either a 2-tuple or two separate args.
        if i is None:
            i = j = 0
            python = True
        elif len(i) == 2:
            i,j = i
        
        if not python:
            s = gui.getAllText(w)
            i,j = gui.toPythonIndex(s,w,i),gui.toPythonIndex(s,w,j)
    
        g.app.gui.setSelectionRange(w,i,j,insert,python=True)
    #@-node:ekr.20031218072017.4024:setSelectionRange (leoBody)
    #@+node:ekr.20031218072017.4038:Visibility & scrolling (leoBody)
    def getYScrollPosition (self):
        return g.app.gui.getYview(self.bodyCtrl)
        
    def scrollDown (self):
        g.app.gui.yscroll(self.bodyCtrl,1,'units')
        
    def scrollUp (self):
        g.app.gui.yscroll(self.bodyCtrl,-1,'units')
        
    def see (self,index,python=False):
        g.app.gui.see(self.bodyCtrl,index,python=python)
        
    def seeInsertPoint (self):
        g.app.gui.seeInsertPoint(self.bodyCtrl)
        
    def setYScrollPosition (self,scrollPosition):
        if len(scrollPosition) == 2:
            first,last = scrollPosition
        else:
            first = scrollPosition
        g.app.gui.yview(self.bodyCtrl,first)
        
    #@-node:ekr.20031218072017.4038:Visibility & scrolling (leoBody)
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
    
        # 'bodyWantsFocus',
        # 'headlineWantsFocus',
        # 'logWantsFocus',
        # 'minibufferWantsFocus',
    )
    #@nonl
    #@-node:ekr.20061109120726:leoFrame.mustBeDefinedOnlyInBaseClass
    #@+node:ekr.20061109120704:leoFrame.mustBeDefinedInSubclasses
    mustBeDefinedInSubclasses = (
        #Gui-dependent commands.
        'OnPaste',
        'OnPasteFromMenu',
        'abortEditLabelCommand',
        'cascade',
        'contractBodyPane',
        'contractLogPane',
        'contractOutlinePane',
        'contractPane',
        'copyText',
        'cutText',
        'endEditLabelCommand',
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
        'insertHeadlineTime',
        'leoHelp',
        'minimizeAll',
        'pasteText',
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
        # Statusline...
        'createStatusLine',
        'clearStatusLine',
        'disableStatusLine',
        'enableStatusLine',
        'getStatusLine',
        'putStatusLine',
        'setFocusStatusLine',
        'statusLineIsEnabled',
        'updateStatusLine',
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
    
    def OnPaste (self,event=None): self.oops()
    def OnPasteFromMenu (self,event=None):    self.oops()
    
    def copyText  (self,event=None): self.oops()
    def cutText   (self,event=None): self.oops()
    def pasteText (self,event=None,middleButton=False): self.oops()
    
    def abortEditLabelCommand (self,event=None): self.oops()
    def endEditLabelCommand   (self,event=None): self.oops()
    def insertHeadlineTime    (self,event=None): self.oops()
    
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
    #@+node:ekr.20061106064948:Status line...
    def createStatusLine (self):                    self.oops()
    def clearStatusLine (self):                     self.oops()
    def disableStatusLine (self,background=None):   self.oops()
    def enableStatusLine (self,background="white"): self.oops()
    def getStatusLine (self):                       self.oops()
    def putStatusLine (self,s,color=None):          self.oops()
    def setFocusStatusLine (self):                  self.oops()
    def statusLineIsEnabled(self):                  self.oops()
    def updateStatusLine(self):                     self.oops()
    #@nonl
    #@-node:ekr.20061106064948:Status line...
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
    #@+node:ekr.20031218072017.3696:leoLog.configure
    def configure (self,*args,**keys):
        
        __pychecker__ = '--no-argsused'
        
        self.oops()
    #@-node:ekr.20031218072017.3696:leoLog.configure
    #@+node:ekr.20031218072017.3697:leoLog.configureBorder
    def configureBorder(self,border):
        
        self.oops()
    #@-node:ekr.20031218072017.3697:leoLog.configureBorder
    #@+node:ekr.20031218072017.3698:leoLog.createControl
    def createControl (self,parentFrame):
        
        self.oops()
    #@-node:ekr.20031218072017.3698:leoLog.createControl
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
        'OnIconDoubleClick',
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
        # Selecting & expanding.
        'expandAllAncestors',
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
    def expandAllAncestors(self,v):                 self.oops()
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
    #@+node:ekr.20031218072017.3718:oops
    def oops(self):
        
        print "leoTree oops:", g.callers(), "should be overridden in subclass"
    #@-node:ekr.20031218072017.3718:oops
    #@-node:ekr.20061109165848:Must be defined in base class
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
    def cget(self,*args,**keys):                pass
    def configure (self,*args,**keys):          pass
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
    def onBodyChanged (self,undoType,oldSel=None,oldText=None,oldYview=None,python=False): pass
    def scheduleIdleTimeRoutine (self,function,*args,**keys): pass
    # Low-level gui...
    def bbox(self,index):                       return
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
    # In the Edit menu...
    
    def OnPaste (self,event=None):              pass
    def OnPasteFromMenu (self,event=None):      pass
    
    def copyText  (self,event=None): pass
    def cutText   (self,event=None): pass
    def pasteText (self,event=None,middleButton=False): pass
    
    def abortEditLabelCommand (self,event=None): pass
    def endEditLabelCommand   (self,event=None): pass
    def insertHeadlineTime    (self,event=None): pass
    
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
    #@+node:ekr.20061109124039:Status line...
    def createStatusLine (self):                    pass
    def clearStatusLine (self):                     pass
    def disableStatusLine (self,background=None):   pass
    def enableStatusLine (self,background="white"): pass
    def getStatusLine (self):                       pass
    def putStatusLine (self,s,color=None):          pass
    def setFocusStatusLine (self):                  pass
    def statusLineIsEnabled(self):                  pass
    def updateStatusLine(self):                     pass
    #@nonl
    #@-node:ekr.20061109124039:Status line...
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
    def clearTab        (self,tabName): pass
    def createTab       (self,tabName): pass
    def deleteTab       (self,tabName): pass
    def getSelectedTab          (self): pass
    def lowerTab        (self,tabName): pass
    def raiseTab        (self,tabName): pass
    def renameTab (self,oldName,newName): pass
    def selectTab       (self,tabName): pass
    def setTabBindings  (self,tabName): pass
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
    # Selecting and expanding.
    def expandAllAncestors(self,v):                 pass
    def select(self,p,updateBeadList=True,scroll=True):
        self.c.setCurrentPosition(p)
        self.frame.scanForTabWidth(p)
    #@-node:ekr.20031218072017.2236:Overrides
    #@-others
#@-node:ekr.20031218072017.2233:class nullTree
#@-others
#@-node:ekr.20031218072017.3655:@thin leoFrame.py
#@-leo
