#! /usr/bin/env python
#@+leo-ver=4-thin
#@+node:ekr.20070227091955.1:@thin leoBridge.py
#@@first

'''A module to allow full access to Leo commanders from outside Leo.'''

#@@language python
#@@tabwidth -4

#@<< about the leoBridge module >>
#@+node:ekr.20070227091955.2:<< about the leoBridge module >>
#@@nocolor
#@+at
# 
# A **host** program is a Python program separate from Leo. Host programs may 
# be
# created by Leo, but at the time they are run host programs are no part of 
# Leo in
# any way. The leoBridge module gives host programs access to all aspects of 
# Leo,
# including all of Leo's source code, the contents of any .leo file, all
# configuration settings in .leo files, etc.
# 
# Host programs will use the leoBridge module something like this::
#     import leoBridge
#     bridge = leoBridge.controller(gui='nullGui')
#     if bridge.isOpen():
#         g = bridge.globals()
#         c = bridge.openLeoFile('test.leo')
# Notes:
# - The leoBridge module imports no modules at all at the top level.
# - leoBridge.controller creates a singleton *bridge controller* that grants 
# access to Leo's objects, in particular the g and c objects.  These objects 
# are fully initialized.  In particular, the g.app and g.app.gui vars are 
# fully initialized.
# 
# - By default, leoBridge.controller creates a null gui: no Leo windows ever 
# appear on the screen.
# 
# - The host program will not import leoGlobals directly, but will instead 
# gain access to Leo's leoGlobals using bridge.globals().
# 
# - bridge.openLeoFile(path) returns a completely standard Leo commander.  
# Host programs can use these commanders as described in Leo's scripting 
# chapter.
#@-at
#@nonl
#@-node:ekr.20070227091955.2:<< about the leoBridge module >>
#@nl

gBridgeController = None # The singleton bridge controller.

# This module must import *no* modules at the outer level!

#@+others
#@+node:ekr.20070227092442:controller
def controller(gui='nullGui',verbose='True'):
    
    '''Create an singleton instance of a bridge controller.'''
    
    global gBridgeController

    if not gBridgeController:
        gBridgeController = bridgeController(gui,verbose)
    
    return gBridgeController
#@nonl
#@-node:ekr.20070227092442:controller
#@+node:ekr.20070227092442.2:class bridgeController
class bridgeController:
    
    '''Creates a way for host programs to access Leo.'''
    
    #@    @+others
    #@+node:ekr.20070227092442.3:ctor (bridgeController)
    def __init__ (self,guiName,verbose):
        
        self.g = None
        self.gui = None
        self.guiName = guiName
        self.mainLoop = False # True only if a non-null-gui mainloop is active.
        self.verbose = verbose
    
        self.initLeo()
    #@nonl
    #@-node:ekr.20070227092442.3:ctor (bridgeController)
    #@+node:ekr.20070227092442.4:globals
    def globals (self):
        
        '''Return a fully initialized leoGlobals module.'''
    
        return self.isOpen() and self.g
    #@nonl
    #@-node:ekr.20070227092442.4:globals
    #@+node:ekr.20070227093530:initLeo & helpers
    def initLeo (self):
        
        '''Init the Leo app to which this class gives access.
        This code is based on leo.run().'''
    
        if not self.isValidPython(): return
        #@    << import leoGlobals and leoApp >>
        #@+node:ekr.20070227093629.1:<< import leoGlobals and leoApp >>
        # Import leoGlobals, but do NOT set g.
        try:
            import leoGlobals
        except ImportError:
            print "Error importing leoGlobals.py"
        
        # Create the application object.
        try:
            import leoApp
            leoGlobals.app = leoApp.LeoApp()
        except ImportError:
            print "Error importing leoApp.py"
            
        # NOW we can set g.
        self.g = g = leoGlobals
        assert(g.app)
        g.app.leoID = None
        #@-node:ekr.20070227093629.1:<< import leoGlobals and leoApp >>
        #@nl
        g.computeStandardDirectories()
        if not self.getLeoID(): return
        #@    << import leoNodes and leoConfig >>
        #@+node:ekr.20070227093629.2:<< import leoNodes and leoConfig >>
        try:
            import leoNodes
        except ImportError:
            print "Error importing leoNodes.py"
            import traceback ; traceback.print_exc()
        
        try:
            import leoConfig
        except ImportError:
            print "Error importing leoConfig.py"
            import traceback ; traceback.print_exc()
        #@-node:ekr.20070227093629.2:<< import leoNodes and leoConfig >>
        #@nl
        g.app.nodeIndices = leoNodes.nodeIndices(g.app.leoID)
        g.app.config = leoConfig.configClass()
        g.app.config.readSettingsFiles(None,verbose=True)
        self.createGui() # Create the gui *before* loading plugins.
        if self.verbose: self.reportDirectories()
        g.doHook("start1") # Load plugins.
        g.init_sherlock(args=[])
        g.app.initing = False
        g.doHook("start2",c=None,p=None,v=None,fileName=None)
        
    #@nonl
    #@+node:ekr.20070227095743:createGui
    def createGui (self):
        
        g = self.g
        
        if self.guiName == 'nullGui':
            import leoGui
            import leoFrame
            g.app.gui = leoGui.nullGui("nullGui")
            # print 'createGui:','g.app:',id(g.app),g.app
            # print 'createGui:','g.app.gui',g.app.gui
            g.app.log = g.app.gui.log = log = leoFrame.nullLog()
            log.isNull = False
            log.enabled = True # Allow prints from nullLog.
            # g.app.writeWaitingLog()
            
        if 0: # A gui main loop is probably a bad idea.
            if self.guiName == 'tkinter':
                import leoTkinterGui
                g.app.gui = leoTkinterGui.tkinterGui()
                g.app.root = g.app.gui.createRootWindow()
                g.app.gui.finishCreate()
    
    
       
    #@nonl
    #@-node:ekr.20070227095743:createGui
    #@+node:ekr.20070227093629.4:isValidPython
    def isValidPython(self):
        
        import sys
        
        if sys.platform == 'cli':
            return True
    
        message = """\
    Leo requires Python 2.2.1 or higher.
    You may download Python from http://python.org/download/
    """
        try:
            # This will fail if True/False are not defined.
            import leoGlobals as g
        except ImportError:
            print "isValidPython: can not import leoGlobals"
            return 0
        except:
            print "isValidPytyhon: unexpected exception: import leoGlobals.py as g"
            import traceback ; traceback.print_exc()
            return 0
        try:
            version = '.'.join([str(sys.version_info[i]) for i in (0,1,2)])
            ok = g.CheckVersion(version,'2.2.1')
            if not ok:
                print message
                g.app.gui.runAskOkDialog(None,"Python version error",message=message,text="Exit")
            return ok
        except:
            print "isValidPython: unexpected exception: g.CheckVersion"
            import traceback ; traceback.print_exc()
            return 0
    #@nonl
    #@-node:ekr.20070227093629.4:isValidPython
    #@+node:ekr.20070227094232:getLeoID
    def getLeoID (self):
        
        import os
        import sys
    
        g = self.g ; tag = ".leoID.txt"
        homeDir = g.app.homeDir
        globalConfigDir = g.app.globalConfigDir
        loadDir = g.app.loadDir
    
        verbose = False and not g.app.unitTesting
        #@    << try to get leoID from sys.leoID >>
        #@+node:ekr.20070227094232.1:<< try to get leoID from sys.leoID>>
        # This would be set by in Python's sitecustomize.py file.
        
        # Use hasattr & getattr to suppress pychecker warning.
        # We also have to use a "non-constant" attribute to suppress another warning!
        
        nonConstantAttr = "leoID"
        
        if hasattr(sys,nonConstantAttr):
            g.app.leoID = getattr(sys,nonConstantAttr)
            if verbose: g.es("leoID = " + g.app.leoID, color='red')
        #@nonl
        #@-node:ekr.20070227094232.1:<< try to get leoID from sys.leoID>>
        #@nl
        if not g.app.leoID:
            #@        << try to get leoID from "leoID.txt" >>
            #@+node:ekr.20070227094232.2:<< try to get leoID from "leoID.txt" >>
            for theDir in (homeDir,globalConfigDir,loadDir):
                # N.B. We would use the _working_ directory if theDir is None!
                if theDir:
                    try:
                        fn = g.os_path_join(theDir,tag)
                        f = open(fn,'r')
                        s = f.readline()
                        f.close()
                        if s and len(s) > 0:
                            g.app.leoID = s.strip()
                            if verbose:
                                g.es("leoID = %s (in %s)" % (g.app.leoID,theDir), color="red")
                            break
                        elif verbose:
                            g.es("empty %s (in %s)" % (tag,theDir), color = "red")
                    except IOError:
                        g.app.leoID = None
                        # g.es("%s not found in %s" % (tag,theDir),color="red")
                    except Exception:
                        g.app.leoID = None
                        g.es('Unexpected exception in app.setLeoID',color='red')
                        g.es_exception()
            #@-node:ekr.20070227094232.2:<< try to get leoID from "leoID.txt" >>
            #@nl
        if not g.app.leoID:
            #@        << try to get leoID from os.getenv('USER') >>
            #@+node:ekr.20070227094232.3:<< try to get leoID from os.getenv('USER') >>
            try:
                theId = os.getenv('USER')
                if theId:
                    if verbose: g.es_print("using os.getenv('USER'): %s " % (repr(theId)),color='red')
                    g.app.leoID = theId
                    return
                    
            except Exception:
                pass
            #@-node:ekr.20070227094232.3:<< try to get leoID from os.getenv('USER') >>
            #@nl
        return g.app.leoID
    #@-node:ekr.20070227094232:getLeoID
    #@+node:ekr.20070227093629.9:reportDirectories
    def reportDirectories (self):
        
        g = self.g
       
        for kind,theDir in (
            ("global config",g.app.globalConfigDir),
            ("home",g.app.homeDir),
        ):
            g.es('%s dir: %s' % (kind,theDir),color="blue")
    #@-node:ekr.20070227093629.9:reportDirectories
    #@-node:ekr.20070227093530:initLeo & helpers
    #@+node:ekr.20070227093918:isOpen
    def isOpen (self):
        
        g = self.g
    
        return g and g.app and g.app.gui
    #@nonl
    #@-node:ekr.20070227093918:isOpen
    #@+node:ekr.20070227092442.5:openLeoFile & helpers
    def openLeoFile (self,fileName):
        
        '''Open a .leo file, or create a new Leo frame if no fileName is given.'''
        
        g = self.g
        
        if self.isOpen():
            fileName = self.completeFileName(fileName)
            c = self.createFrame(fileName)
            g.app.gui.log = log = c.frame.log
            log.isNull = False
            log.enabled = True
            # print 'createGui:','g.app:',id(g.app),g.app
            # print 'createGui:','g.app.gui',g.app.gui
            return c
        else:
            return None
    #@+node:ekr.20070227093629.5:completeFileName
    def completeFileName (self,fileName):
        
        g = self.g
        
        if not fileName.strip(): return ''
        
        import os
    
        fileName = g.os_path_join(os.getcwd(),fileName)
        head,ext = g.os_path_splitext(fileName)
        if not ext: fileName = fileName + ".leo"
    
        return fileName
    #@-node:ekr.20070227093629.5:completeFileName
    #@+node:ekr.20070227093629.6:createFrame
    def createFrame (self,fileName):
        
        '''Create a commander and frame for the given file.
        Create a new frame if the fileName is empty or non-exisent.'''
        
        g = self.g
    
        if fileName.strip():
            if g.os_path_exists(fileName):
                ok, frame = g.openWithFileName(fileName,None)
                if ok: return frame.c
            else: g.es("File not found %s, creating new window: " % fileName)
                
        # Create a new frame. Unlike leo.run, this is not a startup window.
        c,frame = g.app.newLeoCommanderAndFrame(fileName=fileName)
        frame.setInitialWindowGeometry()
        frame.resizePanesToRatio(frame.ratio,frame.secondary_ratio)
        # Call the 'new' hook for compatibility with plugins.
        g.doHook("new",old_c=None,c=c,new_c=c)
        return c
    #@nonl
    #@-node:ekr.20070227093629.6:createFrame
    #@-node:ekr.20070227092442.5:openLeoFile & helpers
    #@-others
#@-node:ekr.20070227092442.2:class bridgeController
#@-others
#@-node:ekr.20070227091955.1:@thin leoBridge.py
#@-leo
