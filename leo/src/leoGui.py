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
import leoFrame # for nullGui.

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
        self.bodyTextWidget = None
        self.plainTextWidget = None
        
    #@-node:ekr.20031218072017.3722: leoGui.__init__
    #@+node:ekr.20061109211054:leoGui.mustBeDefinedOnlyInBaseClass
    mustBeDefinedOnlyInBaseClass = (
        'guiName',
        'oops',
        'setScript',
    )
    #@nonl
    #@-node:ekr.20061109211054:leoGui.mustBeDefinedOnlyInBaseClass
    #@+node:ekr.20061109211022:leoGui.mustBeDefinedInSubclasses
    mustBeDefinedInSubclasses = (
        # Startup & shutdown
        'attachLeoIcon',
        'center_dialog',
        'color',
        #'createComparePanel',          # optional
        #'createFindPanel',             # optional
        'createFindTab',
        'createKeyHandlerClass',
        'createLeoFrame',
        'createRootWindow',
        'create_labeled_frame',
        'destroySelf',
        'eventChar',
        'eventKeysym',
        'eventWidget',
        'eventXY',
        # 'finishCreate', # optional.
        # 'getFontFromParams', # optional
        # 'getFullVersion', # optional.
        'getTextFromClipboard',
        'get_focus',
        'get_window_info',
        'isTextWidget',
        'keysym',
        'killGui',
        # 'makeScriptButton', # optional
        'recreateRootWindow',
        'replaceClipboardWith',
        'runAboutLeoDialog',
        'runAskLeoIDDialog',
        'runAskOkCancelNumberDialog',
        'runAskOkDialog',
        'runAskYesNoCancelDialog',
        'runAskYesNoDialog',
        'runMainLoop',
        'runOpenFileDialog',
        'runSaveFileDialog',
        'set_focus',
        #'setIdleTimeHook',             # optional       
        #'setIdleTimeHookAfterDelay',   # optional
        'widget_name',
    )
    #@-node:ekr.20061109211022:leoGui.mustBeDefinedInSubclasses
    #@-node:ekr.20031218072017.3721:app.gui Birth & death
    #@+node:ekr.20031218072017.3741:oops
    def oops (self):
        
        # It is not usually an error to call methods of this class.
        # However, this message is useful when writing gui plugins.
        if 1:
            print "leoGui oops", g.callers(), "should be overridden in subclass"
    #@-node:ekr.20031218072017.3741:oops
    #@+node:ekr.20061109212618.1:Must be defined only in base class
    #@+node:ekr.20031218072017.3740:guiName
    def guiName(self):
        
        try:
            return self.mGuiName
        except:
            return "invalid gui name"
    #@-node:ekr.20031218072017.3740:guiName
    #@+node:ekr.20031218072017.2231:setScript
    def setScript (self,script=None,scriptFileName=None):
    
        self.script = script
        self.scriptFileName = scriptFileName
    #@-node:ekr.20031218072017.2231:setScript
    #@-node:ekr.20061109212618.1:Must be defined only in base class
    #@+node:ekr.20061109212618:Must be defined in subclasses
    #@+node:ekr.20031218072017.3723:app.gui create & destroy
    #@+node:ekr.20031218072017.3724:createRootWindow
    def createRootWindow(self):
    
        """Create the hidden root window for the gui.
        
        Nothing needs to be done if the root window need not exist."""
    
        self.oops()
    #@-node:ekr.20031218072017.3724:createRootWindow
    #@+node:ekr.20031218072017.3725:destroySelf
    def destroySelf (self):
    
        self.oops()
    #@-node:ekr.20031218072017.3725:destroySelf
    #@+node:ekr.20031218072017.3727:killGui
    def killGui(self,exitFlag=True):
    
        """Destroy the gui.
        
        The entire Leo application should terminate if exitFlag is True."""
    
        self.oops()
    #@-node:ekr.20031218072017.3727:killGui
    #@+node:ekr.20031218072017.3728:recreateRootWindow
    def recreateRootWindow(self):
    
        """Create the hidden root window of the gui
        after a previous gui has terminated with killGui(False)."""
    
        self.oops()
    #@-node:ekr.20031218072017.3728:recreateRootWindow
    #@+node:ekr.20031218072017.3729:runMainLoop
    def runMainLoop(self):
    
        """Run the gui's main loop."""
    
        self.oops()
    #@-node:ekr.20031218072017.3729:runMainLoop
    #@-node:ekr.20031218072017.3723:app.gui create & destroy
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
    
    def runAskOkCancelStringDialog(self,c,title,message):
        """Create and run askOkCancelString dialog ."""
        self.oops()
    
    def runAskYesNoDialog(self,c,title,message=None):
        """Create and run an askYesNo dialog."""
        self.oops()
    
    def runAskYesNoCancelDialog(self,c,title,
        message=None,yesMessage="Yes",noMessage="No",defaultButton="Yes"):
        """Create and run an askYesNoCancel dialog ."""
        self.oops()
    #@-node:ekr.20031218072017.3730:app.gui dialogs
    #@+node:ekr.20061031173016:app.gui.createKeyHandlerClass
    def createKeyHandlerClass (self,c,useGlobalKillbuffer=True,useGlobalRegisters=True):
        
        self.oops()
        
        # import leoKeys # Do this here to break a circular dependency.
                
        # return leoKeys.keyHandlerClass(c,useGlobalKillbuffer,useGlobalRegisters)
    #@nonl
    #@-node:ekr.20061031173016:app.gui.createKeyHandlerClass
    #@+node:ekr.20031218072017.3731:app.gui file dialogs
    def runOpenFileDialog(self,title,filetypes,defaultextension,multiple=False):
    
        """Create and run an open file dialog ."""
    
        self.oops()
    
    def runSaveFileDialog(self,initialfile,title,filetypes,defaultextension):
    
        """Create and run a save file dialog ."""
        
        self.oops()
    #@-node:ekr.20031218072017.3731:app.gui file dialogs
    #@+node:ekr.20031218072017.3732:app.gui panels
    # New in 4.3: it is not an error to call these...
        
    def createComparePanel(self,c):
        """Create Compare panel."""
        
    def createFindPanel(self,c):
        """Create a hidden Find panel."""
        
    def createLeoFrame(self,title):
        """Create a new Leo frame."""
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
    #@+node:ekr.20031218072017.3734:Clipboard (leoGui)
    def replaceClipboardWith (self,s):
        
        self.oops()
    
    def getTextFromClipboard (self):
        
        self.oops()
    #@-node:ekr.20031218072017.3734:Clipboard (leoGui)
    #@+node:ekr.20061031132712.1:color
    # g.es calls gui.color to do the translation,
    # so most code in Leo's core can simply use Tk color names.
    
    def color (self,color):
        '''Return the gui-specific color corresponding to the Tk color name.'''
        return color # Do not call oops: this method is essential for the config classes.
    #@-node:ekr.20061031132712.1:color
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
    #@+node:ekr.20061031132907:Events (leoGui)
    def event_generate(self,w,kind,*args,**keys):
        '''Generate an event.'''
        pass
    
    def eventChar (self,event,c=None):
        '''Return the char field of an event.'''
        return event and event.char or ''
        
    def eventKeysym (self,event,c=None):
        '''Return the keysym value of an event.'''
        return event and event.keysym
    
    def eventWidget (self,event,c=None):
        '''Return the widget field of an event.'''   
        return event and event.widget
    
    def eventXY (self,event,c=None):
        if event:
            return event.x,event.y
        else:
            return 0,0
    #@nonl
    #@-node:ekr.20061031132907:Events (leoGui)
    #@+node:ekr.20070212145124:getFullVersion
    def getFullVersion (self,c):
        
        return 'leoGui: dummy version'
    #@-node:ekr.20070212145124:getFullVersion
    #@+node:ekr.20031218072017.3737:Focus
    def get_focus(self,frame):
        """Return the widget that has focus, or the body widget if None."""
        self.oops()
            
    def set_focus(self,commander,widget):
        """Set the focus of the widget in the given commander if it needs to be changed."""
        self.oops()
    #@-node:ekr.20031218072017.3737:Focus
    #@+node:ekr.20031218072017.3736:Font (leoGui)
    def getFontFromParams(self,family,size,slant,weight,defaultSize=12):
        
        pass
        # self.oops()
    #@-node:ekr.20031218072017.3736:Font (leoGui)
    #@+node:ekr.20031218072017.3739:Idle time
    def setIdleTimeHook (self,idleTimeHookHandler):
        
        # print 'leoGui:setIdleTimeHook'
        pass # Not an error.
        
    def setIdleTimeHookAfterDelay (self,idleTimeHookHandler):
        
        # print 'leoGui:setIdleTimeHookAfterDelay'
        pass # Not an error.
    #@-node:ekr.20031218072017.3739:Idle time
    #@+node:ekr.20070212070820:makeScriptButton
    def makeScriptButton (c,
        p=None,
        script=None,
        buttonText=None,
        balloonText='Script Button',
        shortcut=None,
        bg='LightSteelBlue1',
        define_g=True,
        define_name='__main__',
        silent=False, 
    ):
     
        self.oops()
    #@-node:ekr.20070212070820:makeScriptButton
    #@+node:ekr.20061111165041:widget_name
    def widget_name (self,w):
        
        return self.oops()
    #@-node:ekr.20061111165041:widget_name
    #@-node:ekr.20031218072017.3733:app.gui utils
    #@-node:ekr.20061109212618:Must be defined in subclasses
    #@+node:ekr.20070219084912:finishCreate (may be overridden in subclasses)
    def finishCreate (self):
        
        pass
    #@nonl
    #@-node:ekr.20070219084912:finishCreate (may be overridden in subclasses)
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
        
        leoGui.__init__ (self,guiName) # init the base class.
        
        self.script = None
        self.lastFrame = None
        self.isNullGui = True
        self.bodyTextWidget = None
        self.plainTextWidget = None
    #@-node:ekr.20031218072017.2225: nullGui.__init__
    #@+node:ekr.20031219075221: nullGui.__getattr__
    if 0: # This causes no end of problems.
    
        def __getattr__(self,attr):
    
            g.trace("nullGui",attr)
            return nullObject()
    #@-node:ekr.20031219075221: nullGui.__getattr__
    #@+node:ekr.20031218072017.2226:nullGui.createLeoFrame
    def createLeoFrame(self,title):
        
        """Create a null Leo Frame."""
        
        # print 'nullGui.createLeoFrame'
        
        gui = self
        self.lastFrame = leoFrame.nullFrame(title,gui)
        return self.lastFrame
    #@-node:ekr.20031218072017.2226:nullGui.createLeoFrame
    #@+node:ekr.20070123092623:nullGui.createKeyHandlerClass
    def createKeyHandlerClass (self,c,useGlobalKillbuffer=True,useGlobalRegisters=True):
        
        import leoKeys # Do this here to break a circular dependency.
                
        return leoKeys.keyHandlerClass(c,useGlobalKillbuffer,useGlobalRegisters)
    #@nonl
    #@-node:ekr.20070123092623:nullGui.createKeyHandlerClass
    #@+node:ekr.20050328144031:attachLeoIcon
    def attachLeoIcon (self,w):
        
        pass
    #@-node:ekr.20050328144031:attachLeoIcon
    #@+node:ekr.20031218072017.2227:createRootWindow
    def createRootWindow(self):
        pass
    #@-node:ekr.20031218072017.2227:createRootWindow
    #@+node:ekr.20031218072017.2228:finishCreate
    def finishCreate (self):
        pass
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
    #@-node:ekr.20031218072017.2229:runMainLoop
    #@-node:ekr.20031218072017.2224:Birth & death
    #@+node:ekr.20070123093822:set_focus
    def set_focus(self,c,w):
        
        __pychecker__ = '--no-argsused' # c not used at present.
        
        pass
    #@nonl
    #@-node:ekr.20070123093822:set_focus
    #@+node:ekr.20031218072017.2230:oops
    def oops(self):
            
        """Default do-nothing method for nullGui class.
        
        It is NOT an error to use this method."""
        
        # It is not usually an error to call methods of this class.
        # However, this message is useful when writing gui plugins.
        if 1:
            g.trace("nullGui",g.callers())
    #@-node:ekr.20031218072017.2230:oops
    #@-others
#@-node:ekr.20031218072017.2223:class nullGui (leoGui)
#@+node:ekr.20031218072017.3742:class unitTestGui (leoGui)
class unitTestGui(leoGui):
    
    '''A gui class for use by unit tests that would otherwise be interrupted by dialogs.
    
    Except for how dialogs are handled, it is in effect the same as a nullGui.'''
    
    __pychecker__ = '--no-argsused' # This class has many unused args.
    
    #@    @+others
    #@+node:ekr.20031218072017.3743: test.gui.__init__& destroySelf
    def __init__ (self,dict,trace=False):
        
        self.dict = dict
        self.oldGui = g.app.gui
        self.trace=trace
        
        # Init the base class
        leoGui.__init__ (self,"unitTestGui")
        
        # Use the same kind of widgets as the old gui.
        self.bodyTextWidget = self.oldGui.bodyTextWidget
        self.plainTextWidget = self.oldGui.plainTextWidget
    
        g.app.gui = self
        
    def destroySelf (self):
        
        g.app.gui = self.oldGui
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
        
    def runAskOkCancelStringDialog(self,c,title,message):
        return self.simulateDialog("stringDialog",'')
        
    def runCompareDialog(self,c):
        return self.simulateDialog("compareDialog",'')
        
    def runOpenFileDialog(self,title,filetypes,defaultextension,multiple=False):
        return self.simulateDialog("openFileDialog")
    
    def runSaveFileDialog(self,initialfile,title,filetypes,defaultextension):
        return self.simulateDialog("saveFileDialog")
    
    def runAskYesNoDialog(self,c,title,message=None):
        return self.simulateDialog("yesNoDialog","no")
    
    def runAskYesNoCancelDialog(self,c,title,
        message=None,yesMessage="Yes",noMessage="No",defaultButton="Yes"):
        return self.simulateDialog("yesNoCancelDialog","cancel")
    #@-node:ekr.20031218072017.3744:dialogs (unitTestGui)
    #@+node:ekr.20031218072017.3745:dummy routines (unitTestGui)
    def get_focus (self,frame):     pass
    def set_focus (self,c,widget):  pass
    #@-node:ekr.20031218072017.3745:dummy routines (unitTestGui)
    #@+node:ekr.20031218072017.3746:oops
    def oops(self):
        
        g.trace("unitTestGui",g.callers())
        
        if 0: # Fail the unit test.
            assert 0,"call to undefined method in unitTestMethod class"
    #@-node:ekr.20031218072017.3746:oops
    #@+node:ekr.20031218072017.3747:simulateDialog
    def simulateDialog (self,key,defaultVal=None):
        
        val = self.dict.get(key,defaultVal)
    
        if self.trace:
            print key, val
    
        return val
    #@-node:ekr.20031218072017.3747:simulateDialog
    #@+node:ekr.20070130094235:widget_name
    def widget_name (self,w):
        
        return repr(w)
    #@-node:ekr.20070130094235:widget_name
    #@-others
#@-node:ekr.20031218072017.3742:class unitTestGui (leoGui)
#@-others
#@-node:ekr.20031218072017.3719:@thin leoGui.py
#@-leo
