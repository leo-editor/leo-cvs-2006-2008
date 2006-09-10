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

__version__ = '0.0.9'

#@<< imports >>
#@+node:ekr.20050825154553.1:<< imports >>
from __future__ import generators # To make this plugin work with Python 2.2.

import leoGlobals as g
import leoPlugins
import leoNodes

if leoNodes.use_zodb:
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
# 
# 0.0.9 EKR: Revised the commands to match the experimental @button nodes in 
# test.leo.
# 
# **Important** These commands appear to work, but there may be fundamental,
# impossible-to-solve problems. It appears that connections must be held open
# while editing .leo files, but that just won't be pleasant.
#@-at
#@nonl
#@-node:ekr.20050825154553.2:<< change log >>
#@nl

# These globals are inited by first instances of zodbCommandsClass.
zodb_db     = None
zodb_failed = False

#@+others
#@+node:ekr.20050825165419:Module level...
#@+node:ekr.20050825155043:init
def init ():
    
    global ZODB
    
    if g.app.unitTesting:
        return False
        
    if not leoNodes.use_zodb:
        return False
        
    ok = ZODB is not None
        
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
        self.db = None # Set in init_zodb.
        self.fileName = (fileName and fileName.strip()) or c.fileName()
    
        ok = self.init_zodb()
    
        if ok:
            self.createCommands()
    #@nonl
    #@-node:ekr.20060904192907.2:__init__
    #@+node:ekr.20060909115750:init_zodb
    def init_zodb (self):
        
        global zodb_db, zodb_failed
        
        g.trace(zodb_db)
        
        self.db = zodb_db # Set the default.
        
        if zodb_db:     return True
        if zodb_failed: return False
    
        # The path to the zodb file must exist.  No reasonable default is possible.
        name = self.c.config.getString('zodb_storage_file')
        if not name.strip():
            self.es('No setting: @string zodb_storage_file')
        else:
            try:
                storage = ZODB.FileStorage.FileStorage(name)
                self.db = zodb_db = ZODB.DB(storage)
            except Exception:
                g.es_exception()
    
        ok = self.db is not None
        zodb_failed = not ok
        self.es(g.choose(ok,'zodb inited','zodb init failed'))
        return ok
    #@nonl
    #@-node:ekr.20060909115750:init_zodb
    #@+node:ekr.20060904192907.3:createCommands
    def createCommands (self):
        
        c = self.c
    
        c.zodbCommands = self
        g.trace(c)
    
        if 0:
            table = (
                ('open-zodb-file',  self.openFile),
                ('read-zodb-file',  self.readFile),
                ('write-zodb-file', self.writeFile),
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
    #@+node:ekr.20060910141324:openFile
    def openFile (self,event=None,fileName=None):
        
        c = self.c ; fileName = fileName or self.fileName
    
        connection = self.db.open()
        try:
            root = connection.root()
            rv = root.get(fileName)
            if not rv:
                return self.es('zodb read: not found: %s' % (fileName))
            c2 = c.new()
            hasattr(c2,'zodbCommands') or zodbCommandsClass(c2,fileName)
            c2.openDirectory = c.openDirectory # A hack.
            c2.mFileName = fileName # Another hack.
            c2.beginUpdate()
            try:
                c2.setRootVnode(rv)
                c2Root = c2.rootPosition()
                c2.atFileCommands.readAll(c2Root)
                self.es('zodb read: %s' % (fileName))
            finally:
                c2.endUpdate()
        finally:
            get_transaction().commit()
            connection.close()
    #@nonl
    #@-node:ekr.20060910141324:openFile
    #@+node:ekr.20060904192907.4:readFile (for testing only)
    def readFile (self,event=None,fileName=None):
        
        c = self.c ; fileName = fileName or self.fileName
    
        connection = self.db.open()
        try:
            root = connection.root()
            rv = root.get(fileName)
            g.trace(rv)
        finally:
            get_transaction().commit()
            connection.close()
    #@nonl
    #@-node:ekr.20060904192907.4:readFile (for testing only)
    #@+node:ekr.20060908210902:writeFile
    def writeFile (self,event=None,fileName=None):
        
        c = self.c ; fileName = fileName or self.fileName
        
        connection = self.db.open()
        try:
            root = connection.root()
            root[fileName] = c.rootPosition().v
            get_transaction().commit()
            self.es('zodb wrote: %s' % fileName)
        finally:
            connection.close()
    #@nonl
    #@-node:ekr.20060908210902:writeFile
    #@-others
#@nonl
#@-node:ekr.20060904192907.1:class zodbCommandsClass
#@-others
#@nonl
#@-node:ekr.20050825154553:@thin zodb.py
#@-leo
