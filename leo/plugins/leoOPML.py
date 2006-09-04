#@+leo-ver=4-thin
#@+node:ekr.20060904103412:@thin leoOPML.py
#@<< docstring >>
#@+node:ekr.20060904103412.1:<< docstring >>
'''An **experimental** plugin to represent Leo outlines as OPML files.

It defines these new commands:

- read-opml-file:
    
- write-opml-file:
'''
#@nonl
#@-node:ekr.20060904103412.1:<< docstring >>
#@nl

__version__ = '0.01'

#@<< version history >>
#@+node:ekr.20060904103412.2:<< version history >>
#@@killcolor
#@+at
# 
# 0.01 EKR: Initial version.
#@-at
#@nonl
#@-node:ekr.20060904103412.2:<< version history >>
#@nl
#@<< imports >>
#@+node:ekr.20060904103412.3:<< imports >>
import leoGlobals as g
import leoPlugins
#@nonl
#@-node:ekr.20060904103412.3:<< imports >>
#@nl

#@+others
#@+node:ekr.20060904103412.4:init
def init ():
    
    leoPlugins.registerHandler(('open2','new2'),onCreate)
    g.plugin_signon(__name__)

    return True
#@nonl
#@-node:ekr.20060904103412.4:init
#@+node:ekr.20060904103412.5:onCreate
def onCreate (tag, keys):
    
    c = keys.get('c')
    if c:
        opmlController(c)
#@nonl
#@-node:ekr.20060904103412.5:onCreate
#@+node:ekr.20060904103412.6:class opmlController
class opmlController:
    
    #@    @+others
    #@+node:ekr.20060904103412.7:__init__
    def __init__ (self,c):
        
        self.c = c
    
        self.createCommands()
    #@nonl
    #@-node:ekr.20060904103412.7:__init__
    #@+node:ekr.20060904103412.8:createCommands
    def createCommands (self):
        
        c = self.c
            
        for name,func in (
            ('read-opml-file',  self.readFile),
            ('write-opml-file', self.writeFile),
        ):
            c.k.registerCommand (name,shortcut=None,func=func,pane='all',verbose=False)
    #@nonl
    #@-node:ekr.20060904103412.8:createCommands
    #@+node:ekr.20060904103721:readFile
    def readFile (self):
        
        g.trace()
    #@nonl
    #@-node:ekr.20060904103721:readFile
    #@+node:ekr.20060904103721.1:writeFile
    def writeFile (self):
        
        g.trace()
    #@nonl
    #@-node:ekr.20060904103721.1:writeFile
    #@-others
#@nonl
#@-node:ekr.20060904103412.6:class opmlController
#@-others
#@nonl
#@-node:ekr.20060904103412:@thin leoOPML.py
#@-leo
