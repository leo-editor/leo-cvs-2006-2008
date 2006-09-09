#@+leo-ver=4-thin
#@+node:ekr.20050825154553:@thin zodb.py
#@<< docstring >>
#@+node:ekr.20050825154605:<< docstring >>
'''A plugin to use a ZODB database instead of the file system. 

This plugin creates the read/write-zodb-file commands.
'''
#@nonl
#@-node:ekr.20050825154605:<< docstring >>
#@nl

__version__ = '0.0.7'

#@<< imports >>
#@+node:ekr.20050825154553.1:<< imports >>
from __future__ import generators # To make this plugin work with Python 2.2.

import leoGlobals as g
import leoPlugins
import leoNodes

try:
    import ZODB
    import ZODB.FileStorage
    # print ZODB
except ImportError:
    ZODB = None
#@nonl
#@-node:ekr.20050825154553.1:<< imports >>
#@nl
#@<< change log >>
#@+node:ekr.20050825154553.2:<< change log >>
#@@nocolor

#@+at 
#@nonl
# This plugin was written by Edward K. Ream.
# 
# 0.0.1: Initial version. Experimented with replacing tnode class from this 
# plugin.
# 0.0.2:
# - Replaced g.app.gui.newLeoCommanderAndFrame with 
# g.app.newLeoCommanderAndFrame.
# - Update to reflect new c argument to position.__init__.
# 0.0.4 EKR: Added from __future__ import generators to suppress warning in 
# Python 2.2.
# 0.0.5 EKR:
# - Define persistent version of classes in Leo's core.  Much easier than 
# doing so here.
# - Create zodbCommandsClass that defines the read/write-zodb-file commands.
#   This is **much** easier and safer during development than messing with 
# Leo's core.
# - Removed zodbControllerClass: the read/write commands open and close the 
# zodb.
# 0.0.6 EKR:
# - Improved the docstring.
# - Replaced global zodb_file with self.storageName ivar.
# 0.0.7 EKR:  Progress in creating model for zodb interractions.
# - Added new commands, and leave connection open more often.
# - zodb_storage is now opened just once at the module level.
# - Problems remain with interactions between multiple zodbController objects.
#@-at
#@nonl
#@-node:ekr.20050825154553.2:<< change log >>
#@nl

# These globals are inited by first instances of zodbCommandsClass.

zodb_storage = None # Global instance of ZODB.FileStorage.FileStorage.
zodb_storage_name = None # Name of zodb_storage file.

#@+others
#@+node:ekr.20050825165419:Module level...
#@+node:ekr.20050825155043:init
def init ():
    
    global ZODB
    
    if g.app.unitTesting:
        return False
        
    ok = ZODB is not None and leoNodes is not None
        
    if ok:
        leoPlugins.registerHandler(('open2','new2'),onCreate)
        g.plugin_signon(__name__)
    else:
        s = 'zodb plugin: can not import zodb'
        print s ; g.es(s,color='red')
    
    return ok
#@nonl
#@-node:ekr.20050825155043:init
#@+node:ekr.20060904192907:onCreate
def onCreate (tag, keys):
    
    # g.trace('tag',tag,'keys',keys)
    
    c = keys.get('c')
    if c:
        # Create the read/write-zodb-file commands.
        zodbCommandsClass(c)
#@nonl
#@-node:ekr.20060904192907:onCreate
#@-node:ekr.20050825165419:Module level...
#@+node:ekr.20060904192907.1:class zodbCommandsClass
class zodbCommandsClass:
    
    #@    @+others
    #@+node:ekr.20060904192907.2:__init__
    def __init__ (self,c):
        
        self.c = c
        self.clearedVnodes = []
        
        # Set by open, used by close.
        self.connection = None
        self.db = None
        self.root = None
        
        ok = self.init_zodb()
    
        if ok:
            self.createCommands()
    #@nonl
    #@-node:ekr.20060904192907.2:__init__
    #@+node:ekr.20060909115750:init_zodb
    def init_zodb (self):
        
        global zodb_storage, zodb_storage_name
        c = self.c
        
        if not zodb_storage:
        
            # The path to the zodb file must exist.  No reasonable default is possible.
            zodb_storage_name = c.config.getString('zodb_storage_file')
            
            if zodb_storage_name.strip():
                zodb_storage = ZODB.FileStorage.FileStorage(zodb_storage_name)
            else:
                self.es('No setting: @string zodb_storage_file')
            
        g.trace(zodb_storage)
        return zodb_storage is not None
    #@nonl
    #@-node:ekr.20060909115750:init_zodb
    #@+node:ekr.20060905094242:clear/setCommanders
    if 0: # No longer needed.  neither vnodes nor positions have a 'c' ivar.
    
        def clearCommanders (self,c):
    
            self.clearedVnodes = [p.v for p in c.allNodes_iter()]
            for v in self.clearedVnodes:
                v.c = None
                
        def setCommanders (self,c):
            
            for v in self.clearedVnodes:
                v.c = c
                
            self.clearedVnodes = []
        
    #@nonl
    #@-node:ekr.20060905094242:clear/setCommanders
    #@+node:ekr.20060904204806.1:close
    def close (self):
        
        if self.connection:
            self.connection.close()
    
        if self.db:
            self.db.close()
    
        self.root = self.db = self.connection = None
        
        self.es('zodb close: %s ' % (self.c.shortFileName()))
    #@nonl
    #@-node:ekr.20060904204806.1:close
    #@+node:ekr.20060904192907.3:createCommands
    def createCommands (self):
        
        c = self.c
    
        c.zodbCommands = self
        g.trace(c)
        
        if 0:
        
            table = (
                ('init-zodb-file',  self.initFile),
                ('open-zodb-file',  self.openFile),
                ('read-zodb-file',  self.readFile),
                ('quit-zodb-file',  self.quitFile),
                ('save-zodb-file',  self.saveFile),
            )
        
            for name,func in table:
                c.k.registerCommand (name,shortcut=None,func=func,pane='all',verbose=False)
    #@nonl
    #@-node:ekr.20060904192907.3:createCommands
    #@+node:ekr.20060909072915:es
    def es (self,s):
        
        g.es_print(s,color='red')
    #@nonl
    #@-node:ekr.20060909072915:es
    #@+node:ekr.20060904192907.5:initFile
    def initFile (self,event=None):
        
        c = self.c ; p = c.rootPosition()
        fileName = c.shortFileName()
    
        if self.isOpen():
            self.es('zodb init: file already open: %s' % fileName)
            return
            
        try:
            self.open(fileName)
            self.root[fileName] = p.v
            get_transaction().commit() # get_transaction is a builtin(!)
            self.es('zodb init: %s' % fileName)
        finally:
            self.close()
    #@nonl
    #@-node:ekr.20060904192907.5:initFile
    #@+node:ekr.20060909072915.1:isOpen
    def isOpen(self):
        
        return self.root is not None
    #@nonl
    #@-node:ekr.20060909072915.1:isOpen
    #@+node:ekr.20060904204806:open
    def open (self,fileName):
        
        global zodb_storage
        
        if self.root: return
        
        try:
            self.root = self.db = self.connection = None
            self.db         = ZODB.DB(zodb_storage)
            self.connection = self.db.open()
            self.root       = self.connection.root()
            self.es('zodb open: %s' % fileName)
            return True
        except Exception:
            g.es_exception()
            self.close()
            return False
    #@nonl
    #@-node:ekr.20060904204806:open
    #@+node:ekr.20060909075604:openFile
    def openFile (self,event=None,fileName=None):
        
        c = self.c
        
        if not self.isOpen():
            self.open(fileName)
        
        self.readFile(fileName=fileName)
        
        
            
    #@nonl
    #@-node:ekr.20060909075604:openFile
    #@+node:ekr.20060909073917:quitFile
    def quitFile (self,event=None):
        
        c = self.c
        
        if self.isOpen():
            get_transaction().commit()
            self.close()
    #@nonl
    #@-node:ekr.20060909073917:quitFile
    #@+node:ekr.20060904192907.4:readFile
    def readFile (self,event=None,fileName=None):
        
        c = self.c
        if not fileName:
            return self.es('zodb readFile: no file name')
        try:
            self.isOpen() or self.open(fileName)
            root = self.root
            rv = root.get(fileName)
            if not rv: return self.es('zodb key not found: %s' % (fileName))
            c2 = c.new()
            hasattr(c2,'zodbCommands') or zodbCommandsClass(c2)
            c2.openDirectory=c.openDirectory # A hack.
            c2.beginUpdate()
            try:
                c2.setRootVnode(rv)
                c2Root = c2.rootPosition()
                c2.atFileCommands.readAll(c2Root)
                self.es('zodb read: %s' % (fileName))
            finally:
                c2.endUpdate()
        finally:
            pass
            # get_transaction().commit()
            # Close the connection: we are about to move to a different outline.
            # self.close()
    #@nonl
    #@-node:ekr.20060904192907.4:readFile
    #@+node:ekr.20060908210902:saveFile
    def saveFile (self,event=None):
    
        c = self.c ; p = c.rootPosition()
        fileName = c.shortFileName()
        
        if not self.isOpen():
            self.open(fileName)
    
        get_transaction().commit()
        self.root[fileName] = p.v
        get_transaction().commit()
        self.es('zodb saved: %s' % fileName)
    #@nonl
    #@-node:ekr.20060908210902:saveFile
    #@-others
#@nonl
#@-node:ekr.20060904192907.1:class zodbCommandsClass
#@-others
#@nonl
#@-node:ekr.20050825154553:@thin zodb.py
#@-leo
