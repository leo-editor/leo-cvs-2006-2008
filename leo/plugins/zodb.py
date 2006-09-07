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

__version__ = '0.0.6'

#@<< imports >>
#@+node:ekr.20050825154553.1:<< imports >>
from __future__ import generators # To make this plugin work with Python 2.2.

import leoGlobals as g
import leoPlugins

try:
    import ZODB
    import ZODB.FileStorage
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
#@-at
#@nonl
#@-node:ekr.20050825154553.2:<< change log >>
#@nl

# This should be a user option, NOT a module-level symbol.


#@+others
#@+node:ekr.20050825165419:Module level...
#@+node:ekr.20050825155043:init
def init ():
    
    global ZODB
    
    if g.app.unitTesting:
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
        self.storage = None
        
        # The path to the zodb file.
        self.storageName = c.config.getString('zodb_storage_file')
        if self.storageName:
            self.createCommands()
        else:
            g.es_print('No setting: @string zodb_storage_file')
    #@nonl
    #@-node:ekr.20060904192907.2:__init__
    #@+node:ekr.20060905094242:clear/setCommanders
    def clearCommanders (self,c):
    
        self.clearedVnodes = [p.v for p in c.allNodes_iter()]
        for v in self.clearedVnodes:
            v.c = None
            
    def setCommanders (self,c):
        
        for v in self.clearedVnodes:
            v.c = c
            
        self.clearedVnodes = []
    #@-node:ekr.20060905094242:clear/setCommanders
    #@+node:ekr.20060904204806.1:close
    def close (self):
        
        if self.connection:
            self.connection.close()
    
        if self.db:
            self.db.close()
    
        if self.storage:
            self.storage.close()
            
        self.root = self.storage = self.db = self.connection = None
    #@nonl
    #@-node:ekr.20060904204806.1:close
    #@+node:ekr.20060904192907.3:createCommands
    def createCommands (self):
        
        c = self.c
        
        table = (
            ('read-zodb-file',  self.readFile),
            ('write-zodb-file', self.writeFile),
        )
    
        for name,func in table:
            c.k.registerCommand (name,shortcut=None,func=func,pane='all',verbose=False)
    #@nonl
    #@-node:ekr.20060904192907.3:createCommands
    #@+node:ekr.20060904204806:open
    def open (self):
        
        try:
            self.root = self.storage = self.db = self.connection = None
            self.storage    = ZODB.FileStorage.FileStorage(self.storageName)
            self.db         = ZODB.DB(self.storage)
            self.connection = self.db.open()
            self.root       = self.connection.root()
            return True
        except Exception:
            g.es_exception()
            self.close()
            return False
    #@nonl
    #@-node:ekr.20060904204806:open
    #@+node:ekr.20060904192907.4:readFile
    def readFile (self,event=None):
        
        c = self.c
        
        try:
            self.open()
            g.trace(self.root)
        finally:
            self.close()
    #@nonl
    #@-node:ekr.20060904192907.4:readFile
    #@+node:ekr.20060904192907.5:writeFile
    def writeFile (self,event=None):
        
        c = self.c ; p = c.rootPosition()
    
        try:
            self.open()
            self.root['count'] = self.root.get('count',0) + 1
            # self.clearCommanders(c)
            self.root['root_vnode'] = p.v
            # self.root['root_tnode'] = p.v.t
            g.trace(self.root)
            get_transaction().commit() # get_transaction is a builtin(!)
        finally:
            # self.setCommanders(c)
            self.close()
    #@nonl
    #@-node:ekr.20060904192907.5:writeFile
    #@-others
#@nonl
#@-node:ekr.20060904192907.1:class zodbCommandsClass
#@-others
#@nonl
#@-node:ekr.20050825154553:@thin zodb.py
#@-leo
