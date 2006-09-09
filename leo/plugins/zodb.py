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

__version__ = '0.0.8'

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
# 0.0.8 EKR: zodb_db and zodb_connection are now globals.
# - Removed open and isOpen: the connection should probably stay open till 
# shutdown.
# - The interaction model is starting to work reliably.
#@-at
#@nonl
#@-node:ekr.20050825154553.2:<< change log >>
#@nl

# These globals are inited by first instances of zodbCommandsClass.

zodb_storage        = None  # Global instance of ZODB.FileStorage.FileStorage.
zodb_storage_name   = None  # Name of global zodb_storage file.
zodb_db             = None  # Global db instance.
zodb_connection     = None  # Global connection instance.  How is this closed??

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
    def __init__ (self,c,fileName = None):
        
        self.c = c
        self.fileName = (fileName and fileName.strip()) or c.shortFileName()
        
        ok = self.init_zodb()
    
        if ok:
            self.createCommands()
    #@nonl
    #@-node:ekr.20060904192907.2:__init__
    #@+node:ekr.20060909115750:init_zodb
    def init_zodb (self):
        
        global zodb_storage, zodb_storage_name, zodb_db, zodb_connection
        
        if zodb_storage:
            return zodb_connection is not None
        else:
            # The path to the zodb file must exist.  No reasonable default is possible.
            zodb_storage_name = self.c.config.getString('zodb_storage_file')
            if not zodb_storage_name.strip():
                self.es('zodb init failed. No setting: @string zodb_storage_file')
                return False
            try:
                zodb_storage = ZODB.FileStorage.FileStorage(zodb_storage_name)
                zodb_db = ZODB.DB(zodb_storage)
                zodb_connection = zodb_db.open()
                self.es('zodb inited: %s' % self.fileName) # zodb_storage, zodb_db, zodb_connection)
                return zodb_connection is not None
            except Exception:
                self.es('zodb init failed')
                g.es_exception()
                return False
    #@nonl
    #@-node:ekr.20060909115750:init_zodb
    #@+node:ekr.20060904204806.1:close
    def close (self):
        
        global zodb_connection
        
        if zodb_connection:
            zodb_connection.close()
            zodb_connection = None
            self.es('zodb close connection')
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
        
        global zodb_connection
    
        c = self.c ; fileName = self.fileName
        
        if zodb_connection:
            root = zodb_connection.root()
            root[fileName] = c.rootPosition().v
            get_transaction().commit()
            self.es('zodb init: %s' % fileName)
        else:
            self.es('zodb init: no connection')
    #@nonl
    #@-node:ekr.20060904192907.5:initFile
    #@+node:ekr.20060909075604:openFile
    def openFile (self,event=None,fileName=None):
        
        global zodb_connection
        
        if not fileName:
            self.es('zodb open: no file name')
        elif zodb_connection:
            self.readFile(fileName=fileName)
        else:
            self.es('zodb open file: no connection')
    #@nonl
    #@-node:ekr.20060909075604:openFile
    #@+node:ekr.20060909073917:quitFile
    def quitFile (self,event=None):
        
        global zodb_connection
        
        if zodb_connection:
            get_transaction().commit()
            self.close()
    #@nonl
    #@-node:ekr.20060909073917:quitFile
    #@+node:ekr.20060904192907.4:readFile
    def readFile (self,event=None,fileName=None):
        
        global zodb_connection
        c = self.c
        if not fileName:
            return self.es('zodb read file: no file name')
        if not zodb_connection:
            return self.es('zodb read file: no connection')
        rv = zodb_connection.root().get(fileName)
        if rv:
            c2 = c.new()
            hasattr(c2,'zodbCommands') or zodbCommandsClass(c2,fileName)
            c2.openDirectory=c.openDirectory # A hack.
            c2.beginUpdate()
            try:
                c2.setRootVnode(rv)
                c2Root = c2.rootPosition()
                c2.atFileCommands.readAll(c2Root)
                self.es('zodb read: %s' % (fileName))
            finally:
                c2.endUpdate()
        else:
            self.es('zodb read file: key not found: %s' % (fileName))
    #@nonl
    #@-node:ekr.20060904192907.4:readFile
    #@+node:ekr.20060908210902:saveFile
    def saveFile (self,event=None):
    
        global zodb_connection
    
        c = self.c ; fileName = self.fileName
        
        if zodb_connection:
            get_transaction().commit()
            root = zodb_connection.root()
            root[fileName] = c.rootPosition().v
            get_transaction().commit()
            self.es('zodb saved: %s' % fileName)
        else:
            self.es('zodb save: no connection')
    #@nonl
    #@-node:ekr.20060908210902:saveFile
    #@-others
#@nonl
#@-node:ekr.20060904192907.1:class zodbCommandsClass
#@-others
#@nonl
#@-node:ekr.20050825154553:@thin zodb.py
#@-leo
