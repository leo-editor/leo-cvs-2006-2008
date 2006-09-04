#@+leo-ver=4-thin
#@+node:ekr.20060904103412:@thin leoOPML.py
#@<< docstring >>
#@+node:ekr.20060904103412.1:<< docstring >>
'''A plugin to read and write Leo outlines in .opml format.

It defines the read-opml-file and write-opml-file commands and corresponding buttons.

'''
#@nonl
#@-node:ekr.20060904103412.1:<< docstring >>
#@nl

#@@language python
#@@tabwidth -4
#@@pagewidth 80

__version__ = '0.01'

#@<< version history >>
#@+node:ekr.20060904103412.2:<< version history >>
#@@killcolor
#@+at
# 
# 0.01 EKR: Initial version.
# 0.02 EKR:
# - Changes to Leo's core:
#     - Added toOPML=False keyword argument to write_Leo_file.
#     - Added dummy putToOPML method.
# - This plugin overrides leoFileCommands.fileCommands.putToOPML.
#@-at
#@-node:ekr.20060904103412.2:<< version history >>
#@nl
#@<< imports >>
#@+node:ekr.20060904103412.3:<< imports >>
import leoGlobals as g
import leoPlugins
import leoFileCommands
#@nonl
#@-node:ekr.20060904103412.3:<< imports >>
#@nl

#@+others
#@+node:ekr.20060904132527.9:Module level
#@+node:ekr.20060904103412.4:init
def init ():
    
    # override the base class
    leoPlugins.registerHandler('start1',onStart2)

    # Register the commands.
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
#@+node:ekr.20060904132527.10:onStart2
def onStart2 (tag,keys):

    g.trace(tag,keys)
    leoFileCommands.fileCommands = opmlFileCommandsClass
#@nonl
#@-node:ekr.20060904132527.10:onStart2
#@-node:ekr.20060904132527.9:Module level
#@+node:ekr.20060904132527.11:class opmlFileCommandsClass (fileCommands)
class opmlFileCommandsClass (leoFileCommands.fileCommands):
    
    #@    @+others
    #@+node:ekr.20060904132527.13:putToOPML & helpers
    def putToOPML (self):
    
        self.putOPMLProlog()
        self.putOPMLHeader()
        self.putOPMLNodes()
        self.putOPMLPostlog()
        g.trace('wrote',self.mFileName)
    #@nonl
    #@+node:ekr.20060904132527.14:putOPMLProlog
    def putOPMLProlog (self):
        
        self.put('<opml version="1.0">\n')
    #@nonl
    #@-node:ekr.20060904132527.14:putOPMLProlog
    #@+node:ekr.20060904132527.15:putOPMLHeader
    def putOPMLHeader (self):
        
        '''Put the OPML header, including attributes for globals, prefs and  find settings.'''
        
        self.put('<head>\n')
        
        self.put('</head>\n')
    #@nonl
    #@-node:ekr.20060904132527.15:putOPMLHeader
    #@+node:ekr.20060904132527.16:putOPMLNodes
    def putOPMLNodes (self):
        
        c = self.c ; root = c.rootPosition()
        
        self.put('<body>\n')
        
        for p in root.self_and_siblings_iter():
            self.putOPMLNode(p)
        
        self.put('</body>\n')
    #@nonl
    #@-node:ekr.20060904132527.16:putOPMLNodes
    #@+node:ekr.20060904132527.17:putOPMLNode
    def putOPMLNode (self,p):
        
        c = self.c ; indent = '\t' * p.level() ; body = p.bodyString()
        
        # g.trace(p.headString())
        
        self.put('%s<outline tx=%s, head="%s" body=' % (
            indent,
            g.app.nodeIndices.toString(p.v.t.fileIndex),
            self.xmlEscape(p.headString()),
            # str(len(p.bodyString()))
        ))
    
        if body:
            self.put('"%s"' % self.xmlEscape(body))
        else:
            self.put('""')
    
        if p.hasChildren():
            self.put('>\n')
            for p2 in p.children_iter():
                self.putOPMLNode(p2)
            self.put('%s</outline>\n' % indent)
        else:
            self.put('/>\n')
    #@nonl
    #@-node:ekr.20060904132527.17:putOPMLNode
    #@+node:ekr.20060904132527.18:putOPMLPostlog
    def putOPMLPostlog (self):
        
        self.put('</opml>\n')
    #@nonl
    #@-node:ekr.20060904132527.18:putOPMLPostlog
    #@-node:ekr.20060904132527.13:putToOPML & helpers
    #@-others
#@nonl
#@-node:ekr.20060904132527.11:class opmlFileCommandsClass (fileCommands)
#@+node:ekr.20060904103412.6:class opmlController
class opmlController:
    
    #@    @+others
    #@+node:ekr.20060904112626:Birth
    #@+node:ekr.20060904103412.7:__init__
    def __init__ (self,c):
        
        self.c = c
        self.frame = c.frame
        self.fc = c.fileCommands # The file controller contains many useful utils.
        
        self.createCommands()
        ### self.initIvars()
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
    #@-node:ekr.20060904112626:Birth
    #@+node:ekr.20060904103721:readFile
    def readFile (self,event=None):
        
        g.trace()
    #@nonl
    #@-node:ekr.20060904103721:readFile
    #@+node:ekr.20060904103721.1:writeFile
    def writeFile (self,event=None):
        
        g.trace()
        
        fileName = r'c:\prog\test\OPMLtest.leo'
    
        self.fc.write_Leo_file(fileName,outlineOnlyFlag=True,toString=False,toOPML=True)
    #@nonl
    #@-node:ekr.20060904103721.1:writeFile
    #@-others
#@nonl
#@-node:ekr.20060904103412.6:class opmlController
#@-others
#@nonl
#@-node:ekr.20060904103412:@thin leoOPML.py
#@-leo
