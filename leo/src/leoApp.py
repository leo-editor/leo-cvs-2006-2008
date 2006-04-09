# -*- coding: utf-8 -*-
#@+leo-ver=4-thin
#@+node:ekr.20031218072017.2608:@thin leoApp.py
#@@first

#@@language python
#@@tabwidth -4
#@@pagewidth 80

import leoGlobals as g
import os
import sys

class LeoApp:

    """A class representing the Leo application itself.
    
    Ivars of this class are Leo's global variables."""
    
    #@    @+others
    #@+node:ekr.20031218072017.1416:app.__init__
    def __init__(self):
    
        # These ivars are the global vars of this program.
        self.afterHandler = None
        self.batchMode = False # True: run in batch mode.
        self.commandName = None # The name of the command being executed.
        self.config = None # The leoConfig instance.
        self.count = 0 # General purpose debugging count.
        self.debug = False # True: enable extra debugging tests (not used at present).
            # WARNING: this could greatly slow things down.
        self.debugSwitch = 0
            # 0: default behavior
            # 1: full traces in g.es_exception.
            # 2: call pdb.set_trace in g.es_exception, etc.
        self.disableSave = False
        self.globalConfigDir = None # The directory that is assumed to contain the global configuration files.
        self.globalOpenDir = None # The directory last used to open a file.
        self.gui = None # The gui class.
        self.hasOpenWithMenu = False # True: open with plugin has been loaded.
        self.hookError = False # True: suppress further calls to hooks.
        self.hookFunction = None # Application wide hook function.
        self.homeDir = None # The user's home directory.
        self.idle_imported = False # True: we have done an import idle
        self.idleTimeDelay = 100 # Delay in msec between calls to "idle time" hook.
        self.idleTimeHook = False # True: the global idleTimeHookHandler will reshedule itself.
        self.initing = True # True: we are initiing the app.
        self.killed = False # True: we are about to destroy the root window.
        self.leoID = None # The id part of gnx's.
        self.loadDir = None # The directory from which Leo was loaded.
        self.loadedPlugins = [] # List of loaded plugins that have signed on.
        self.log = None # The LeoFrame containing the present log.
        self.logIsLocked = False # True: no changes to log are allowed.
        self.logWaiting = [] # List of messages waiting to go to a log.
        self.menuWarningsGiven = False # True: supress warnings in menu code.
        self.nodeIndices = None # Singleton node indices instance.
        self.numberOfWindows = 0 # Number of opened windows.
        self.openWithFiles = [] # List of data used by Open With command.
        self.openWithFileNum = 0 # Used to generate temp file names for Open With command.
        self.openWithTable = None # The table passed to createOpenWithMenuFromTable.
        self.positions = 0 # Count of the number of positions generated.
        self.quitting = False # True if quitting.  Locks out some events.
        self.realMenuNameDict = {} # Contains translations of menu names and menu item names.
        self.root = None # The hidden main window. Set later.
        self.searchDict = {} # For communication between find/change scripts.
        self.scanErrors = 0 # The number of errors seen by g.scanError.
        self.scriptDict = {} # For communication between Execute Script command and scripts.
        self.statsDict = {} # Statistics dict used by g.stat, g.clear_stats, g.print_stats.
        self.trace = False # True: enable debugging traces.
        self.trace_gc = False # defined in run()
        self.trace_gc_calls = False # defined in run()
        self.trace_gc_verbose = False # defined in run()
        self.trace_gc_inited = False
        self.tracePositions = False
        self.trace_list = [] # "Sherlock" argument list for tracing().
        self.tkEncoding = "utf-8"
        self.unicodeErrorGiven = True # True: suppres unicode tracebacks.
        self.unitTestDict = {} # For communication between unit tests and code.
        self.unitTesting = False # True if unit testing.
        self.use_psyco = False # Can't be a config param because it is used before config module can be inited.
        self.user_xresources_path = None # Resource file for Tk/tcl.
        self.windowList = [] # Global list of all frames.  Does not include hidden root window.
    
        # Global panels.  Destroyed when Leo ends.
        self.pythonFrame = None
        
        #@    << Define global constants >>
        #@+node:ekr.20031218072017.1417:<< define global constants >>
        self.prolog_string = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
        
        # New in leo.py 3.0
        self.prolog_prefix_string = "<?xml version=\"1.0\" encoding="
        self.prolog_postfix_string = "?>"
        
        # leo.py 3.11
        self.use_unicode = True # True: use new unicode logic.
        #@-node:ekr.20031218072017.1417:<< define global constants >>
        #@nl
        #@    << Define global data structures >>
        #@+node:ekr.20031218072017.368:<< define global data structures >> app
        # Internally, lower case is used for all language names.
        self.language_delims_dict = {
            "ada" : "--",
            "actionscript" : "// /* */", #jason 2003-07-03
            "c" : "// /* */", # C, C++ or objective C.
            "csharp" : "// /* */", # C#
            "css" : "/* */", # 4/1/04
            "cweb" : "@q@ @>", # Use the "cweb hack"
            "elisp" : ";",
            "forth" : "\\_ _(_ _)", # Use the "REM hack"
            "fortran" : "C",
            "fortran90" : "!",
            "html" : "<!-- -->",
            "java" : "// /* */",
            "latex" : "%",
            "lua" : "--",  # ddm 13/02/06
            "pascal" : "// { }",
            "perl" : "#",
            "perlpod" : "# __=pod__ __=cut__", # 9/25/02: The perlpod hack.
            "php" : "//",
            "plain" : "#", # We must pick something.
            "plsql" : "-- /* */", # SQL scripts qt02537 2005-05-27
            "python" : "#",
            "rapidq" : "'", # fil 2004-march-11
            "rebol" : ";",  # jason 2003-07-03
            "shell" : "#",  # shell scripts
            "tcltk" : "#",
            "unknown" : "#" } # Set when @comment is seen.
        
        self.language_extension_dict = {
            "ada" : "ads",
            "actionscript" : "as", #jason 2003-07-03
            "c" : "c",
            "css" : "css", # 4/1/04
            "cweb" : "w",
            "elisp" : "el",
            "forth" : "forth",
            "fortran" : "f",
            "fortran90" : "f",
            "html" : "html",
            "java" : "java",
            "latex" : "tex", # 1/8/04
            "lua" : "lua",  # ddm 13/02/06
            "noweb" : "nw",
            "pascal" : "p",
            # "perl" : "perl",
            # "perlpod" : "perl",
            "perl" : "pl",      # 11/7/05
            "perlpod" : "pod",  # 11/7/05
            "php" : "php",
            "plain" : "txt",
            "python" : "py",
            "plsql" : "sql", # qt02537 2005-05-27
            "rapidq" : "bas", # fil 2004-march-11
            "rebol" : "r",    # jason 2003-07-03
            "shell" : "sh",   # DS 4/1/04
            "tex" : "tex",
            "tcltk" : "tcl",
            "unknown" : "txt" } # Set when @comment is seen.
            
        self.extension_dict = {
            "ads"   : "ada",
            "adb"   : "ada",
            "as"    : "actionscript",
            "bas"   : "rapidq",
            "c"     : "c",
            "css"   : "css",
            "el"    : "elisp",
            "forth" : "forth",
            "f"     : "fortran90", # or fortran ?
            "html"  : "html",
            "java"  : "java",
            "lua" : "lua",  # ddm 13/02/06
            "noweb" : "nw",
            "p"     : "pascal",
            # "perl"  : "perl",
            "pl"    : "perl",   # 11/7/05
            "pod"   : "perlpod", # 11/7/05
            "php"   : "php",
            "py"    : "python",
            "sql"   : "plsql", # qt02537 2005-05-27
            "r"     : "rebol",
            "sh"    : "shell",
            "tex"   : "tex",
            "txt"   : "plain",
            "tcl"   : "tcltk",
            "w"     : "cweb" }
        #@nonl
        #@-node:ekr.20031218072017.368:<< define global data structures >> app
        #@nl
    #@nonl
    #@-node:ekr.20031218072017.1416:app.__init__
    #@+node:ekr.20031218072017.2609:app.closeLeoWindow
    def closeLeoWindow (self,frame):
        
        """Attempt to close a Leo window.
        
        Return False if the user veto's the close."""
        
        c = frame.c
        
        if c.promptingForClose:
            # There is already a dialog open asking what to do.
            return False
            
        g.app.config.writeRecentFilesFile(c) # Make sure .leoRecentFiles.txt is written.
    
        if c.changed:
            c.promptingForClose = True
            veto = frame.promptForSave()
            c.promptingForClose = False
            if veto: return False
    
        g.app.setLog(None) # no log until we reactive a window.
        
        g.doHook("close-frame",c=c) # This may remove frame from the window list.
        
        if frame in g.app.windowList:
            g.app.destroyWindow(frame)
        
        if g.app.windowList:
            # Pick a window to activate so we can set the log.
            w = g.app.windowList[0]
            w.deiconify()
            w.lift()
            w.c.setLog()
            w.c.bodyWantsFocus()
        else:
            g.app.finishQuit()
    
        return True # The window has been closed.
    #@nonl
    #@-node:ekr.20031218072017.2609:app.closeLeoWindow
    #@+node:ekr.20031218072017.2610:app.createTkGui
    def createTkGui (self,fileName=None):
        
        # Do NOT omit fileName param: it is used in plugin code.
        __pychecker__ = '--no-argsused'
        
        """A convenience routines for plugins to create the default Tk gui class."""
        
        import leoTkinterGui # Do this import after app module is fully imported.
    
        g.app.gui = leoTkinterGui.tkinterGui()
        g.app.root = g.app.gui.createRootWindow()
        
        # Show a dialog and exit immediately if Pmw can not be imported.
        g.importExtension("Pmw",pluginName="Leo's core",verbose=False,required=True)
        g.app.gui.finishCreate()
        
        if 0:
            if fileName:
                print "Tk gui created in", g.shortFileName(fileName)
    
    
    
    #@-node:ekr.20031218072017.2610:app.createTkGui
    #@+node:ekr.20031218072017.2612:app.destroyAllOpenWithFiles
    def destroyAllOpenWithFiles (self):
    
        """Try to remove temp files created with the Open With command.
        
        This may fail if the files are still open."""
        
        # We can't use g.es here because the log stream no longer exists.
    
        for theDict in self.openWithFiles[:]: # 7/10/03.
            g.app.destroyOpenWithFileWithDict(theDict)
            
        # Delete the list so the gc can recycle Leo windows!
        g.app.openWithFiles = []
    #@nonl
    #@-node:ekr.20031218072017.2612:app.destroyAllOpenWithFiles
    #@+node:ekr.20031218072017.2613:app.destroyOpenWithFilesForFrame
    def destroyOpenWithFilesForFrame (self,frame):
        
        """Close all "Open With" files associated with frame"""
        
        # Make a copy of the list: it may change in the loop.
        openWithFiles = g.app.openWithFiles
    
        for theDict in openWithFiles[:]: # 6/30/03
            c = theDict.get("c")
            if c.frame == frame:
                g.app.destroyOpenWithFileWithDict(theDict)
    #@-node:ekr.20031218072017.2613:app.destroyOpenWithFilesForFrame
    #@+node:ekr.20031218072017.2614:app.destroyOpenWithFileWithDict
    def destroyOpenWithFileWithDict (self,theDict):
        
        path = theDict.get("path")
        if path and g.os_path_exists(path):
            try:
                os.remove(path)
                print "deleting temp file:", g.shortFileName(path)
            except:
                print "can not delete temp file:", path
                
        # Remove theDict from the list so the gc can recycle the Leo window!
        g.app.openWithFiles.remove(theDict)
    #@nonl
    #@-node:ekr.20031218072017.2614:app.destroyOpenWithFileWithDict
    #@+node:ekr.20031218072017.2615:app.destroyWindow
    def destroyWindow (self,frame):
        
        # g.trace(frame in g.app.windowList,frame)
            
        g.app.destroyOpenWithFilesForFrame(frame)
    
        if frame in g.app.windowList:
            g.app.windowList.remove(frame)
            # g.trace(g.app.windowList)
    
        # force the window to go away now.
        # Important: this also destroys all the objects of the commander.
        frame.destroySelf()
    #@nonl
    #@-node:ekr.20031218072017.2615:app.destroyWindow
    #@+node:ekr.20031218072017.1732:app.finishQuit
    def finishQuit(self):
        
        # forceShutdown may already have fired the "end1" hook.
        if not g.app.killed:
            g.doHook("end1")
    
        self.destroyAllOpenWithFiles()
        
        if g.app.gui:
            g.app.gui.destroySelf()
            
        g.app.killed = True
            # Disable all further hooks and events.
            # Alas, "idle" events can still be called even after the following code.
    
        if 0: # Do not use g.trace here!
            print "finishQuit",g.app.killed
            
        if g.app.afterHandler:
            # TK bug: This appears to have no effect, at least on Windows.
            # print "finishQuit: cancelling",g.app.afterHandler
            if g.app.gui and g.app.gui.guiName() == "tkinter":
                self.root.after_cancel(g.app.afterHandler)
            g.app.afterHandler = None
    #@nonl
    #@-node:ekr.20031218072017.1732:app.finishQuit
    #@+node:ekr.20031218072017.2616:app.forceShutdown
    def forceShutdown (self):
        
        """Forces an immediate shutdown of Leo at any time.
        
        In particular, may be called from plugins during startup."""
        
        # Wait until everything is quiet before really quitting.
        g.doHook("end1")
        
        self.log = None # Disable writeWaitingLog
        self.killed = True # Disable all further hooks.
        
        for w in self.windowList[:]:
            self.destroyWindow(w)
    
        self.finishQuit()
    #@nonl
    #@-node:ekr.20031218072017.2616:app.forceShutdown
    #@+node:ekr.20031218072017.2617:app.onQuit
    def onQuit (self,event=None):
        
        g.app.quitting = True
        
        while g.app.windowList:
            w = g.app.windowList[0]
            if not g.app.closeLeoWindow(w):
                break
    
        if g.app.windowList:
            g.app.quitting = False # If we get here the quit has been disabled.
    #@nonl
    #@-node:ekr.20031218072017.2617:app.onQuit
    #@+node:ekr.20031218072017.2618:app.setEncoding
    #@+at 
    #@nonl
    # According to Martin v. Löwis, getdefaultlocale() is broken, and cannot 
    # be fixed. The workaround is to copy the g.getpreferredencoding() 
    # function from locale.py in Python 2.3a2.  This function is now in 
    # leoGlobals.py.
    #@-at
    #@@c
    
    def setEncoding (self):
        
        """Set g.app.tkEncoding."""
    
        try: locale_encoding = g.getpreferredencoding()
        except Exception: locale_encoding = None
        
        try: sys_encoding = sys.getdefaultencoding()
        except Exception: sys_encoding = None
    
        for (encoding,src) in (
            (self.config.tkEncoding,"config"),
            (locale_encoding,"locale"),
            (sys_encoding,"sys"),
            ("utf-8","default")):
        
            if g.isValidEncoding (encoding):
                self.tkEncoding = encoding
                # g.trace(self.tkEncoding,src)
                break
            elif encoding:
                color = g.choose(self.tkEncoding=="ascii","red","blue")
                g.trace("ignoring invalid %s encoding: %s" % (src,encoding),color=color)
    #@nonl
    #@-node:ekr.20031218072017.2618:app.setEncoding
    #@+node:ekr.20031218072017.1978:app.setLeoID
    def setLeoID (self,verbose=True):
    
        tag = ".leoID.txt"
        homeDir = g.app.homeDir
        globalConfigDir = g.app.globalConfigDir
        loadDir = g.app.loadDir
        
        verbose = not g.app.unitTesting
        #@    << return if we can set leoID from sys.leoID >>
        #@+node:ekr.20031218072017.1979:<< return if we can set leoID from sys.leoID>>
        # This would be set by in Python's sitecustomize.py file.
        
        # 7/2/04: Use hasattr & getattr to suppress pychecker warning.
        # We also have to use a "non-constant" attribute to suppress another warning!
        
        nonConstantAttr = "leoID"
        
        if hasattr(sys,nonConstantAttr):
            g.app.leoID = getattr(sys,nonConstantAttr)
            if verbose: g.es_print("leoID = " + g.app.leoID, color='red')
            return
        else:
            g.app.leoID = None
        #@nonl
        #@-node:ekr.20031218072017.1979:<< return if we can set leoID from sys.leoID>>
        #@nl
        #@    << return if we can set leoID from "leoID.txt" >>
        #@+node:ekr.20031218072017.1980:<< return if we can set leoID from "leoID.txt" >>
        for theDir in (homeDir,globalConfigDir,loadDir):
            # N.B. We would use the _working_ directory if theDir is None!
            if theDir:
                try:
                    fn = g.os_path_join(theDir,tag)
                    f = open(fn,'r')
                    s = f.readline()
                    f.close()
                    if s and len(s) > 0:
                        g.app.leoID = s
                        if verbose:
                            g.es_print("leoID = %s (in %s)" % (g.app.leoID,theDir), color="red")
                        return
                    elif verbose:
                        g.es_print("empty %s (in %s)" % (tag,theDir), color = "red")
                except IOError:
                    g.app.leoID = None
                    # g.es("%s not found in %s" % (tag,theDir),color="red")
                except Exception:
                    g.app.leoID = None
                    g.es_print('Unexpected exception in app.setLeoID',color='red')
                    g.es_exception()
        #@nonl
        #@-node:ekr.20031218072017.1980:<< return if we can set leoID from "leoID.txt" >>
        #@nl
        #@    << return if we can set leoID from os.getenv('USER') >>
        #@+node:ekr.20060211140947.1:<< return if we can set leoID from os.getenv('USER') >>
        try:
            theId = os.getenv('USER')
            if theId:
                if verbose: g.es_print("using os.getenv('USER'): %s " % (repr(theId)),color='red')
                g.app.leoID = theId
                return
                
        except Exception:
            pass
        #@nonl
        #@-node:ekr.20060211140947.1:<< return if we can set leoID from os.getenv('USER') >>
        #@nl
        #@    << put up a dialog requiring a valid id >>
        #@+node:ekr.20031218072017.1981:<< put up a dialog requiring a valid id >>
        # New in 4.1: get an id for gnx's.  Plugins may set g.app.leoID.
        
        # Create an emergency gui and a Tk root window.
        g.app.createTkGui("startup")
        
        # Bug fix: 2/6/05: put result in g.app.leoID.
        g.app.leoID = g.app.gui.runAskLeoIDDialog()
        
        # g.trace(g.app.leoID)
        g.es_print("leoID = %s" % (repr(g.app.leoID)),color="blue")
        #@nonl
        #@-node:ekr.20031218072017.1981:<< put up a dialog requiring a valid id >>
        #@nl
        #@    << attempt to create leoID.txt >>
        #@+node:ekr.20031218072017.1982:<< attempt to create leoID.txt >>
        for theDir in (homeDir,globalConfigDir,loadDir):
            # N.B. We would use the _working_ directory if theDir is None!
            if theDir:
                cant = "can not create %s in %s" % (tag,theDir)
                try:
                    fn = g.os_path_join(theDir,tag)
                    f = open(fn,'w')
                    f.write(g.app.leoID)
                    f.close()
                    if g.os_path_exists(fn):
                        s = "%s created in %s" % (tag,theDir)
                        g.es_print(s, color="red")
                        return
                    else:
                        g.es(cant,color='red')
                except IOError:
                    g.es(cant,color='red')
        #@nonl
        #@-node:ekr.20031218072017.1982:<< attempt to create leoID.txt >>
        #@nl
    #@nonl
    #@-node:ekr.20031218072017.1978:app.setLeoID
    #@+node:ekr.20031218072017.1847:app.setLog, lockLog, unlocklog
    def setLog (self,log):
    
        """set the frame to which log messages will go"""
        
        # print "setLog:",tag,"locked:",self.logIsLocked,log
        if not self.logIsLocked:
            self.log = log
    
    def lockLog(self):
        """Disable changes to the log"""
        self.logIsLocked = True
        
    def unlockLog(self):
        """Enable changes to the log"""
        self.logIsLocked = False
    #@nonl
    #@-node:ekr.20031218072017.1847:app.setLog, lockLog, unlocklog
    #@+node:ekr.20031218072017.2619:app.writeWaitingLog
    def writeWaitingLog (self):
    
        # g.trace(g.app.gui,self.log)
    
        if self.log:
            if 1: ## not self.log.isNull: # The test for isNull would probably interfere with batch mode.
                for s,color in self.logWaiting:
                    g.es(s,color=color,newline=0) # The caller must write the newlines.
                self.logWaiting = []
        else:
            print 'writeWaitingLog: still no log!'
    #@nonl
    #@-node:ekr.20031218072017.2619:app.writeWaitingLog
    #@+node:ekr.20031218072017.2188:app.newLeoCommanderAndFrame
    def newLeoCommanderAndFrame(self,fileName,updateRecentFiles=True):
        
        """Create a commander and its view frame for the Leo main window."""
        
        app = self
        
        import leoCommands
        
        if not fileName: fileName = ""
        #@    << compute the window title >>
        #@+node:ekr.20031218072017.2189:<< compute the window title >>
        # Set the window title and fileName
        if fileName:
            title = g.computeWindowTitle(fileName)
        else:
            s = "untitled"
            n = g.app.numberOfWindows
            if n > 0:
                s += str(n)
            title = g.computeWindowTitle(s)
            g.app.numberOfWindows = n+1
        
        #@-node:ekr.20031218072017.2189:<< compute the window title >>
        #@nl
    
        # Create an unfinished frame to pass to the commanders.
        frame = app.gui.createLeoFrame(title)
        
        # Create the commander and its subcommanders.
        c = leoCommands.Commands(frame,fileName)
        
        if not app.initing:
            g.doHook("before-create-leo-frame",c=c) # Was 'onCreate': too confusing.
            
        frame.finishCreate(c)
        c.finishCreate()
        
        # Finish initing the subcommanders.
        c.undoer.clearUndoState() # Menus must exist at this point.
        
        if updateRecentFiles:
            c.updateRecentFiles(fileName)
        
        if not g.app.initing:
            g.doHook("after-create-leo-frame",c=c)
    
        return c,frame
    #@nonl
    #@-node:ekr.20031218072017.2188:app.newLeoCommanderAndFrame
    #@-others
#@-node:ekr.20031218072017.2608:@thin leoApp.py
#@-leo
