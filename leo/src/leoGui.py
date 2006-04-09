# -*- coding: utf-8 -*-
#@+leo-ver=4-thin
#@+node:ekr.20031218072017.3719:@thin leoGui.py
#@@first

"""A module containing the base leoGui class.

This class and its subclasses hides the details of which gui is actually being used.
Leo's core calls this class to allocate all gui objects.

Plugins may define their own gui classes by setting g.app.gui."""

#@@language python
#@@tabwidth -4
#@@pagewidth 80

import leoGlobals as g
import leoFrame # for null gui.

#@+others
#@+node:ekr.20031218072017.3720:class leoGui
class leoGui:
    
    """The base class of all gui classes.
    
    Subclasses are expected to override all do-nothing methods of this class."""
    
    __pychecker__ = '--no-argsused' # base classes have many unused args.
    
    #@    << define leoGui file types >>
    #@+node:ekr.20040131103531:<< define leoGui file types >> (not used yet)
    allFullFiletypes = [
        ("All files",   "*"),
        ("C/C++ files", "*.c"),
        ("C/C++ files", "*.cpp"),
        ("C/C++ files", "*.h"),
        ("C/C++ files", "*.hpp"),
        ("Java files",  "*.java"),
        ("Lua files",   "*.lua"),
        ("Pascal files","*.pas"),
        ("Python files","*.py")]
        # To do: *.php, *.php3, *.php4")
    pythonFullFiletypes = [
        ("Python files","*.py"),
        ("All files","*"),
        ("C/C++ files","*.c"),
        ("C/C++ files","*.cpp"),
        ("C/C++ files","*.h"),
        ("C/C++ files","*.hpp"),
        ("Java files","*.java"),
        ("Lua files",   "*.lua"),
        ("Pascal files","*.pas")]
        # To do: *.php, *.php3, *.php4")
    textFullFiletypes = [
        ("Text files","*.txt"),
        ("C/C++ files","*.c"),
        ("C/C++ files","*.cpp"),
        ("C/C++ files","*.h"),
        ("C/C++ files","*.hpp"),
        ("Java files","*.java"),
        ("Lua files",   "*.lua"),
        ("Pascal files","*.pas"),
        ("Python files","*.py"),
        ("All files","*")]
        # To do: *.php, *.php3, *.php4")
    CWEBTextAllFiletypes = [
        ("CWEB files","*.w"),
        ("Text files","*.txt"),
        ("All files", "*")]
    leoAllFiletypes = [
        ("Leo files","*.leo"),
        ("All files","*")]
    leoFiletypes = [
        ("Leo files","*.leo")]
    nowebTextAllFiletypes = [
        ("Noweb files","*.nw"),
        ("Text files", "*.txt"),
        ("All files",  "*")]
    textAllFiletypes = [
        ("Text files","*.txt"),
        ("All files", "*")]
    #@nonl
    #@-node:ekr.20040131103531:<< define leoGui file types >> (not used yet)
    #@nl
    
    #@    @+others
    #@+node:ekr.20031218072017.3721:app.gui Birth & death
    #@+node:ekr.20031218072017.3722: leoGui.__init__
    def __init__ (self,guiName):
        
        # g.trace("leoGui",guiName,g.callers())
        
        self.lastFrame = None
        self.leoIcon = None
        self.mGuiName = guiName
        self.mainLoop = None
        self.root = None
        self.script = None
        self.utils = None
        self.isNullGui = False
    #@nonl
    #@-node:ekr.20031218072017.3722: leoGui.__init__
    #@+node:ekr.20031218072017.3723:stubs
    #@+node:ekr.20031218072017.3724:createRootWindow
    def createRootWindow(self):
    
        """Create the hidden root window for the gui.
        
        Nothing needs to be done if the root window need not exist."""
    
        self.oops()
    #@nonl
    #@-node:ekr.20031218072017.3724:createRootWindow
    #@+node:ekr.20031218072017.3725:destroySelf
    def destroySelf (self):
    
        self.oops()
    #@nonl
    #@-node:ekr.20031218072017.3725:destroySelf
    #@+node:ekr.20031218072017.3726:finishCreate
    def finishCreate (self):
    
        """Do any remaining chores after the root window has been created."""
    
        self.oops()
    #@nonl
    #@-node:ekr.20031218072017.3726:finishCreate
    #@+node:ekr.20031218072017.3727:killGui
    def killGui(self,exitFlag=True):
    
        """Destroy the gui.
        
        The entire Leo application should terminate if exitFlag is True."""
    
        self.oops()
    #@nonl
    #@-node:ekr.20031218072017.3727:killGui
    #@+node:ekr.20031218072017.3728:recreateRootWindow
    def recreateRootWindow(self):
    
        """Create the hidden root window of the gui
        after a previous gui has terminated with killGui(False)."""
    
        self.oops()
    #@nonl
    #@-node:ekr.20031218072017.3728:recreateRootWindow
    #@+node:ekr.20031218072017.3729:runMainLoop
    def runMainLoop(self):
    
        """Run the gui's main loop."""
    
        self.oops()
    #@nonl
    #@-node:ekr.20031218072017.3729:runMainLoop
    #@-node:ekr.20031218072017.3723:stubs
    #@-node:ekr.20031218072017.3721:app.gui Birth & death
    #@+node:ekr.20031218072017.3730:app.gui dialogs
    def runAboutLeoDialog(self,c,version,theCopyright,url,email):
        """Create and run Leo's About Leo dialog."""
        self.oops()
        
    def runAskLeoIDDialog(self):
        """Create and run a dialog to get g.app.LeoID."""
        self.oops()
    
    def runAskOkDialog(self,c,title,message=None,text="Ok"):
        """Create and run an askOK dialog ."""
        self.oops()
    
    def runAskOkCancelNumberDialog(self,c,title,message):
        """Create and run askOkCancelNumber dialog ."""
        self.oops()
    
    def runAskYesNoDialog(self,c,title,message=None):
        """Create and run an askYesNo dialog."""
        self.oops()
    
    def runAskYesNoCancelDialog(self,c,title,
        message=None,yesMessage="Yes",noMessage="No",defaultButton="Yes"):
        """Create and run an askYesNoCancel dialog ."""
        self.oops()
    #@nonl
    #@-node:ekr.20031218072017.3730:app.gui dialogs
    #@+node:ekr.20031218072017.3731:app.gui file dialogs
    def runOpenFileDialog(self,title,filetypes,defaultextension,multiple=False):
    
        """Create and run an open file dialog ."""
    
        self.oops()
    
    def runSaveFileDialog(self,initialfile,title,filetypes,defaultextension):
    
        """Create and run a save file dialog ."""
        
        self.oops()
    #@nonl
    #@-node:ekr.20031218072017.3731:app.gui file dialogs
    #@+node:ekr.20031218072017.3732:app.gui panels
    # New in 4.3: it is not an error to call these...
        
    def createComparePanel(self,c):
        """Create Compare panel."""
        
    def createFindPanel(self,c):
        """Create a hidden Find panel."""
        
    def createLeoFrame(self,title):
        """Create a new Leo frame."""
    #@nonl
    #@-node:ekr.20031218072017.3732:app.gui panels
    #@+node:ekr.20031218072017.3733:app.gui utils
    #@+at 
    #@nonl
    # Subclasses are expected to subclass all of the following methods.
    # 
    # These are all do-nothing methods: callers are expected to check for None 
    # returns.
    # 
    # The type of commander passed to methods depends on the type of frame or 
    # dialog being created.  The commander may be a Commands instance or one 
    # of its subcommanders.
    #@-at
    #@nonl
    #@+node:ekr.20031218072017.3734:Clipboard
    def replaceClipboardWith (self,s):
        
        self.oops()
    
    def getTextFromClipboard (self):
        
        self.oops()
    #@nonl
    #@-node:ekr.20031218072017.3734:Clipboard
    #@+node:ekr.20031218072017.3735:Dialog utils
    def attachLeoIcon (self,window):
        """Attach the Leo icon to a window."""
        self.oops()
        
    def center_dialog(self,dialog):
        """Center a dialog."""
        self.oops()
        
    def create_labeled_frame (self,parent,caption=None,relief="groove",bd=2,padx=0,pady=0):
        """Create a labeled frame."""
        self.oops()
        
    def get_window_info (self,window):
        """Return the window information."""
        self.oops()
    #@-node:ekr.20031218072017.3735:Dialog utils
    #@+node:ekr.20031218072017.3736:Font
    def getFontFromParams(self,family,size,slant,weight,defaultSize=12):
        
        pass
        # self.oops()
    #@nonl
    #@-node:ekr.20031218072017.3736:Font
    #@+node:ekr.20031218072017.3737:Focus
    def get_focus(self,frame):
    
        """Return the widget that has focus, or the body widget if None."""
    
        self.oops()
            
    def set_focus(self,commander,widget):
    
        """Set the focus of the widget in the given commander if it needs to be changed."""
        
        __pychecker__ = '--no-argsused' # widget
    
        self.oops()
        
    def widget_wants_focus(self,commander,widget):
    
        """Indicate that a widget want to get focus."""
        
        __pychecker__ = '--no-argsused' # widget
    
        self.oops()
    #@nonl
    #@-node:ekr.20031218072017.3737:Focus
    #@+node:ekr.20031218072017.3738:Index
    def firstIndex (self):
    
        self.oops()
        
    def lastIndex (self):
    
        self.oops()
        
    def moveIndexForward(self,t,index,n):
    
        self.oops()
        
    def moveIndexToNextLine(self,t,index):
    
        self.oops()
    #@nonl
    #@-node:ekr.20031218072017.3738:Index
    #@+node:ekr.20031218072017.3739:Idle time
    def setIdleTimeHook (self,idleTimeHookHandler):
        
        # print 'leoGui:setIdleTimeHook'
        pass # Not an error.
        
    def setIdleTimeHookAfterDelay (self,idleTimeHookHandler):
        
        # print 'leoGui:setIdleTimeHookAfterDelay'
        pass # Not an error.
    #@-node:ekr.20031218072017.3739:Idle time
    #@+node:ekr.20051220144306:isTextWidget
    def isTextWidget (self,w):
        
        '''Return True if w is a Text widget suitable for text-oriented commands.'''
        
        self.oops()
    #@nonl
    #@-node:ekr.20051220144306:isTextWidget
    #@-node:ekr.20031218072017.3733:app.gui utils
    #@+node:ekr.20031218072017.3740:guiName
    def guiName(self):
        
        try:
            return self.mGuiName
        except:
            return "invalid gui name"
    #@nonl
    #@-node:ekr.20031218072017.3740:guiName
    #@+node:ekr.20031218072017.2231:setScript
    def setScript (self,script=None,scriptFileName=None):
    
        self.script = script
        self.scriptFileName = scriptFileName
    #@nonl
    #@-node:ekr.20031218072017.2231:setScript
    #@+node:ekr.20051206103652:widget_name
    def widget_name (self,w):
        
        return w and hasattr(w,'_name') and w._name or repr(w)
    #@nonl
    #@-node:ekr.20051206103652:widget_name
    #@+node:ekr.20031218072017.3741:oops
    def oops (self):
        
        # It is not usually an error to call methods of this class.
        # However, this message is useful when writing gui plugins.
        if 0:
            print "leoGui oops", g.callers(), "should be overridden in subclass"
    #@nonl
    #@-node:ekr.20031218072017.3741:oops
    #@-others
#@-node:ekr.20031218072017.3720:class leoGui
#@+node:ekr.20031218072017.2223:class nullGui (leoGui)
class nullGui(leoGui):
    
    """Null gui class."""
    
    __pychecker__ = '--no-argsused' # This class has many unused args.
    
    #@    @+others
    #@+node:ekr.20031218072017.2224:Birth & death
    #@+node:ekr.20031218072017.2225: nullGui.__init__
    def __init__ (self,guiName):
        
        # g.trace("nullGui")
        
        leoGui.__init__ (self,guiName) # init the base class.
        
        self.script = None
        self.lastFrame = None
        self.isNullGui = True
    #@nonl
    #@-node:ekr.20031218072017.2225: nullGui.__init__
    #@+node:ekr.20031219075221: nullGui.__getattr__
    if 0: # This causes no end of problems.
    
        def __getattr__(self,attr):
    
            g.trace("nullGui",attr)
            return nullObject()
    #@nonl
    #@-node:ekr.20031219075221: nullGui.__getattr__
    #@+node:ekr.20031218072017.2226:nullGui.createLeoFrame
    def createLeoFrame(self,title):
        
        """Create a null Leo Frame."""
        
        # print 'nullGui.createLeoFrame'
        
        gui = self
        self.lastFrame = leoFrame.nullFrame(title,gui)
        return self.lastFrame
    #@-node:ekr.20031218072017.2226:nullGui.createLeoFrame
    #@+node:ekr.20050328144031:attachLeoIcon
    def attachLeoIcon (self,w):
        
        pass
    #@nonl
    #@-node:ekr.20050328144031:attachLeoIcon
    #@+node:ekr.20031218072017.2227:createRootWindow
    def createRootWindow(self):
        pass
    #@nonl
    #@-node:ekr.20031218072017.2227:createRootWindow
    #@+node:ekr.20031218072017.2228:finishCreate
    def finishCreate (self):
        pass
    #@nonl
    #@-node:ekr.20031218072017.2228:finishCreate
    #@+node:ekr.20031218072017.2229:runMainLoop
    def runMainLoop(self):
    
        """Run the gui's main loop."""
        
        if self.script:
            frame = self.lastFrame
            g.app.log = frame.log
            # g.es("Start of batch script...\n")
            self.lastFrame.c.executeScript(script=self.script)
            # g.es("\nEnd of batch script")
        
        # Getting here will terminate Leo.
    #@nonl
    #@-node:ekr.20031218072017.2229:runMainLoop
    #@-node:ekr.20031218072017.2224:Birth & death
    #@+node:ekr.20031218072017.2230:oops
    def oops(self):
            
        """Default do-nothing method for nullGui class.
        
        It is NOT an error to use this method."""
        
        # It is not usually an error to call methods of this class.
        # However, this message is useful when writing gui plugins.
        if 0:
            g.trace("nullGui",g.callers())
    #@nonl
    #@-node:ekr.20031218072017.2230:oops
    #@-others
#@nonl
#@-node:ekr.20031218072017.2223:class nullGui (leoGui)
#@+node:ekr.20031218072017.3742:class unitTestGui (leoGui)
class unitTestGui(leoGui):
    
    """gui class for use by unit tests."""
    
    __pychecker__ = '--no-argsused' # This class has many unused args.
    
    #@    @+others
    #@+node:ekr.20031218072017.3743: test.gui.__init__& destroySelf
    def __init__ (self,dict,trace=False):
        
        self.dict = dict
        self.oldGui = g.app.gui
        self.trace=trace
        
        # Init the base class
        leoGui.__init__ (self,"unitTestGui")
    
        g.app.gui = self
        
    def destroySelf (self):
        
        g.app.gui = self.oldGui
    #@nonl
    #@-node:ekr.20031218072017.3743: test.gui.__init__& destroySelf
    #@+node:ekr.20031218072017.3744:dialogs (unitTestGui)
    def runAboutLeoDialog(self,c,version,theCopyright,url,email):
        return self.simulateDialog("aboutLeoDialog")
        
    def runAskLeoIDDialog(self):
        return self.simulateDialog("leoIDDialog")
    
    def runAskOkDialog(self,c,title,message=None,text="Ok"):
        return self.simulateDialog("okDialog","Ok")
    
    def runAskOkCancelNumberDialog(self,c,title,message):
        return self.simulateDialog("numberDialog",-1)
        
    def runOpenFileDialog(self,title,filetypes,defaultextension,multiple=False):
        return self.simulateDialog("openFileDialog")
    
    def runSaveFileDialog(self,initialfile,title,filetypes,defaultextension):
        return self.simulateDialog("saveFileDialog")
    
    def runAskYesNoDialog(self,c,title,message=None):
        return self.simulateDialog("yesNoDialog","no")
    
    def runAskYesNoCancelDialog(self,c,title,
        message=None,yesMessage="Yes",noMessage="No",defaultButton="Yes"):
        return self.simulateDialog("yesNoCancelDialog","cancel")
    #@nonl
    #@-node:ekr.20031218072017.3744:dialogs (unitTestGui)
    #@+node:ekr.20031218072017.3745:dummy routines
    def getindex(self,body,index):
        return 0,0
        
    def get_focus(self,frame):
        pass
    
    def set_focus(self,c,widget):
        pass
        
    def getTextSelection (self,t,sort=True):
        return 0,0
    #@nonl
    #@-node:ekr.20031218072017.3745:dummy routines
    #@+node:ekr.20031218072017.3746:oops
    def oops(self):
        
        g.trace("unitTestGui",g.callers())
        
        if 0: # Fail the unit test.
            assert 0,"call to undefined method in unitTestMethod class"
    #@nonl
    #@-node:ekr.20031218072017.3746:oops
    #@+node:ekr.20031218072017.3747:simulateDialog
    def simulateDialog (self,key,defaultVal=None):
        
        val = self.dict.get(key,defaultVal)
    
        if self.trace:
            print key, val
    
        return val
    #@nonl
    #@-node:ekr.20031218072017.3747:simulateDialog
    #@-others
#@nonl
#@-node:ekr.20031218072017.3742:class unitTestGui (leoGui)
#@-others
#@nonl
#@-node:ekr.20031218072017.3719:@thin leoGui.py
#@-leo
