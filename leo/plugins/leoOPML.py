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

# To do: handle unicode properly.

__version__ = '0.05'

# For traces.
printElements = [] # ['outline','head','body',]

#@<< version history >>
#@+node:ekr.20060904103412.2:<< version history >>
#@@killcolor
#@+at
# 
# 0.01 EKR: Initial version.
# 0.02 EKR: This plugin overrides leoFileCommands.fileCommands.putToOPML.
# - Changes to Leo's core:
#     - Added toOPML=False keyword argument to write_Leo_file.
#     - Added dummy putToOPML method.
# 0.03 EKR: Use SAX to read .opml files.  Parsing works.  More semantics are 
# needed.
# 0.04 EKR: Simplified the code.
# 0.05 EKR: Outline created with proper headlines: (wrote & debugged 
# createVnodes & helpers)
#@-at
#@nonl
#@-node:ekr.20060904103412.2:<< version history >>
#@nl
#@<< imports >>
#@+node:ekr.20060904103412.3:<< imports >>
import leoGlobals as g
import leoPlugins

import leoNodes
import leoFileCommands

import xml.sax
import xml.sax.saxutils
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
    leoPlugins.registerHandler(('open2','new'),onCreate)
    
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

    # Override the fileCommands class by opmlFileCommandsClass.
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
        
        self.put('%s<outline tx="%s" head="%s"' % (
            indent,
            g.app.nodeIndices.toString(p.v.t.fileIndex),
            self.xmlEscape(p.headString()),
            # str(len(p.bodyString()))
        ))
    
        if 0: # Probably works, but complicates debugging.
            if body:
                self.put(' body="%s"' % self.xmlEscape(body))
            else:
                self.put(' body=""')
    
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
    #@+node:ekr.20060904134958.116:parse_opml_file
    def parse_opml_file (self,inputFileName):
        
        g.trace(inputFileName)
    
        if not inputFileName or not inputFileName.endswith('.opml'):
            return None
            
        c = self.c
        path = g.os_path_normpath(g.os_path_join(g.app.loadDir,inputFileName))
        
        try: f = open(path)
        except IOError:
            g.trace('can not open %s'%path)
            return None
        try:
            try:
                node = None
                parser = xml.sax.make_parser()
                # Do not include external general entities.
                # The actual feature name is "http://xml.org/sax/features/external-general-entities"
                parser.setFeature(xml.sax.handler.feature_external_ges,0)
                handler = contentHandler(c,inputFileName)
                parser.setContentHandler(handler)
                parser.parse(f)
                node = handler.getNode()
            except:
                g.es('unexpected exception parsing %s' % (inputFileName),color='red')
                g.es_exception()
        finally:
            f.close()
            return node
    #@nonl
    #@-node:ekr.20060904134958.116:parse_opml_file
    #@-others
#@nonl
#@-node:ekr.20060904132527.11:class opmlFileCommandsClass (fileCommands)
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
        c.opmlCommands = self
    
        if 0:
            for name,func in (
                ('read-opml-file',  self.readFile),
                ('write-opml-file', self.writeFile),
            ):
                c.k.registerCommand (name,shortcut=None,func=func,pane='all',verbose=False)
    #@nonl
    #@-node:ekr.20060904103412.8:createCommands
    #@+node:ekr.20060914163456:createVnodes & helpers
    def createVnodes (self, dummyRoot):
        
        '''**Important**: this method and its helpers are low-level code.
        Modify this with extreme care.'''
        
        self.firstChildren = {}
    
        children = self.createChildren(dummyRoot,parent_v = None)
        firstChild = children and children[0]
        
        g.trace(firstChild)
        return firstChild
    #@+node:ekr.20060914171659.2:createChildren
    # node is a nodeClass object, parent_v is a vnode.
    
    def createChildren (self, node, parent_v):
        
        children = node.children
        if not children: return []
        
        # g.trace('parent',parent_v,len(children))
        
        firstChild = children[0]
        tnx = firstChild.tnx
        firstChild_v = self.firstChildren.get(tnx)
    
        if firstChild_v:
            g.trace('previous firstChild',firstChild_v.headString())
            children = [firstChild_v]
        else:
            # Create the first child, and remember it immediately.
            firstChild_v = self.createVnodeTree(children[0],parent_v)
            self.firstChildren[tnx] = firstChild_v
            # Create the other children.
            children = [self.createVnodeTree(child,parent_v) for child in children[1:]]
            children.insert(0,firstChild_v)
            self.linkSiblings(children)
            if parent_v: self.linkParentAndChildren(parent_v,children)
    
        return children
            
            
    #@nonl
    #@-node:ekr.20060914171659.2:createChildren
    #@+node:ekr.20060914171659:createVnodeTree
    def createVnodeTree (self,node,parent_v):
    
        v = self.createVnode(node,parent_v)
        self.createChildren(node,v)
        
        # children = self.createChildren(node,v)
        # firstChild = children and children[0]
        # self.linkParentAndChildren(v,children)
    
        return v
    #@nonl
    #@-node:ekr.20060914171659:createVnodeTree
    #@+node:ekr.20060914171659.1:createVnode
    def createVnode (self,node,parent_v):
        
        h = node.headString
        b = node.bodyString
        t = leoNodes.tnode(bodyString=b,headString=h)
        v = leoNodes.vnode(t)
        v.t.vnodeList.append(v)
        v._parent = parent_v
        
        if 0:
            h1 = v.headString()
            h2 = parent_v and parent_v.headString() or 'None'
            g.trace('node: %12s parent: %12s' % (h1[:12],h2[:12]))
        
        return v
    #@nonl
    #@-node:ekr.20060914171659.1:createVnode
    #@+node:ekr.20060914174806:linkParentAndChildren
    def linkParentAndChildren (self, parent_v, children):
        
        # if children: g.trace(parent_v,len(children))
        
        firstChild_v = children and children[0] or None
    
        parent_v.t._firstChild = firstChild_v
        
        for child in children:
            child._parent = parent_v
    
        # if firstChild_v:
            # firstChild_v._parent = parent_v
        
        v = parent_v
        if v not in v.t.vnodeList:
            v.t.vnodeList.append(v)
    #@nonl
    #@-node:ekr.20060914174806:linkParentAndChildren
    #@+node:ekr.20060914165257:linkSiblings
    def linkSiblings (self, sibs):
        
        '''Set the v._back and v._next links for all vnodes v in sibs.'''
        
        n = len(sibs)
    
        for i in xrange(n):
            v = sibs[i]
            v._back = (i-1 >= 0 and sibs[i-1]) or None
            v._next = (i+1 <  n and sibs[i+1]) or None
    #@nonl
    #@-node:ekr.20060914165257:linkSiblings
    #@-node:ekr.20060914163456:createVnodes & helpers
    #@+node:ekr.20060913220707:dumpTree
    def dumpTree (self,root,dummy):
        
        if not dummy:
            root.dump()
        for child in root.children:
            self.dumpTree(child,dummy=False)
    #@nonl
    #@-node:ekr.20060913220707:dumpTree
    #@+node:ekr.20060904103721:readFile
    def readFile (self,event=None,fileName=None):
        
        if not fileName: return
        
        g.trace('='*60)
    
        c = self.c
        self.dummyRoot = dummyRoot = c.fileCommands.parse_opml_file(fileName)
        
        # g.trace('dummyRoot.children',dummyRoot.children)
        # self.dumpTree(dummyRoot,dummy=True)
    
        v = self.createVnodes(dummyRoot)
        if v:
            c2 = c.new()
            c2.setRootVnode(v)
            c2.checkOutline()
            c2.redraw()
    #@nonl
    #@-node:ekr.20060904103721:readFile
    #@+node:ekr.20060904103721.1:writeFile
    def writeFile (self,event=None,fileName=None):
        
        if fileName:
        
            g.trace(fileName)
    
            self.c.fileCommands.write_Leo_file(fileName,outlineOnlyFlag=True,toString=False,toOPML=True)
    #@nonl
    #@-node:ekr.20060904103721.1:writeFile
    #@-others
#@nonl
#@-node:ekr.20060904103412.6:class opmlController
#@+node:ekr.20060904134958.164:class contentHandler (XMLGenerator)
class contentHandler (xml.sax.saxutils.XMLGenerator):
    
    '''A sax content handler class that reads OPML files.'''

    #@    @+others
    #@+node:ekr.20060904134958.165: __init__ & helpers
    def __init__ (self,c,inputFileName):
    
        self.c = c
        self.inputFileName = inputFileName
    
        # Init the base class.
        xml.sax.saxutils.XMLGenerator.__init__(self)
      
        # Semantics.
        self.elementStack = []
        self.inBody = False
        self.inHead = False
        self.level = 0
        self.node = None
        self.nodeStack = []
        self.rootNode = None
    #@nonl
    #@-node:ekr.20060904134958.165: __init__ & helpers
    #@+node:ekr.20060904134958.166:helpers
    #@+node:ekr.20060904134958.167:attrsToList
    def attrsToList (self,attrs):
        
        '''Convert the attributes to a list of g.Bunches.
        
        attrs: an Attributes item passed to startElement.'''
        
        # g.trace(g.listToString([attrs.getValue(name) for name in attrs.getNames()]))
        
        return [
            g.Bunch(name=name,val=g.toUnicode(attrs.getValue(name),encoding='utf-8'))
                for name in attrs.getNames()]
    #@nonl
    #@-node:ekr.20060904134958.167:attrsToList
    #@+node:ekr.20060904134958.168:attrsToString
    def attrsToString (self,attrs,sep='\n'):
        
        '''Convert the attributes to a string.
        
        attrs: an Attributes item passed to startElement.
        
        sep: the separator charater between attributes.'''
    
        result = [
            '%s="%s"' % (bunch.name,bunch.val)
            for bunch in self.attrsToList(attrs)
        ]
    
        return sep.join(result)
    #@nonl
    #@-node:ekr.20060904134958.168:attrsToString
    #@+node:ekr.20060904134958.169:clean
    def clean(self,s):
    
        return g.toEncodedString(s,"ascii")
    #@nonl
    #@-node:ekr.20060904134958.169:clean
    #@+node:ekr.20060904134958.170:error
    def error (self, message):
        
        print
        print
        print 'XML error: %s' % (message)
        print
    #@nonl
    #@-node:ekr.20060904134958.170:error
    #@+node:ekr.20060904134958.171:printStartElement
    def printStartElement(self,name,attrs):
        
        indent = '\t' * self.level or ''
    
        if attrs.getLength() > 0:
            print '%s<%s %s>' % (
                indent,
                self.clean(name).strip(),
                self.attrsToString(attrs,sep=' ')),
        else:
            print '%s<%s>' % (
                indent,
                self.clean(name).strip()),
    
        if name.lower() in ['outline','head','body',]:
            print
    #@nonl
    #@-node:ekr.20060904134958.171:printStartElement
    #@-node:ekr.20060904134958.166:helpers
    #@+node:ekr.20060904134958.173:sax over-rides
    #@+node:ekr.20060904134958.174: Do nothing...
    #@+node:ekr.20060904134958.175:other methods
    def ignorableWhitespace(self):
        g.trace()
    
    def processingInstruction (self,target,data):
        g.trace()
    
    def skippedEntity(self,name):
        g.trace(name)
    
    def startElementNS(self,name,qname,attrs):
        g.trace(name)
    
    def endElementNS(self,name,qname):
        g.trace(name)
    #@nonl
    #@-node:ekr.20060904134958.175:other methods
    #@+node:ekr.20060904134958.176:endDocument
    def endDocument(self):
    
        pass
    
    
    #@-node:ekr.20060904134958.176:endDocument
    #@+node:ekr.20060904134958.177:startDocument
    def startDocument(self):
        
        pass
    #@nonl
    #@-node:ekr.20060904134958.177:startDocument
    #@-node:ekr.20060904134958.174: Do nothing...
    #@+node:ekr.20060904134958.178:characters
    def characters(self,content):
    
        content = g.toUnicode(content,encoding='utf-8') or ''
        content = content.replace('\r','').strip()
    
        elementName = self.elementStack and self.elementStack[-1].lower() or '<no element name>'
        
        if content:
            print 'content:',elementName,repr(content)
    #@nonl
    #@-node:ekr.20060904134958.178:characters
    #@+node:ekr.20060904134958.179:endElement
    def endElement(self,name):
    
        self.doEndElement(name)
    
        name2 = self.elementStack.pop()
        assert name == name2
    #@nonl
    #@-node:ekr.20060904134958.179:endElement
    #@+node:ekr.20060904134958.180:startElement
    def startElement(self,name,attrs):
    
        self.elementStack.append(name)
        self.doStartElement(name,attrs)
    #@nonl
    #@-node:ekr.20060904134958.180:startElement
    #@-node:ekr.20060904134958.173:sax over-rides
    #@+node:ekr.20060904134958.181:doStartElement
    def doStartElement (self,elementName,attrs):
        
        elementName = elementName.lower()
    
        if elementName in printElements:
            self.printStartElement(elementName,attrs)
    
        if elementName == 'body':
            self.inBody= True
        elif elementName == 'head':
            self.inHead = True
        elif elementName == 'outline':
            if self.inHead:     self.error('<outline> inside <head>')
            if not self.inBody: self.error('<outline> outside <body>')
            self.level += 1
            parent = self.node
            self.node = nodeClass()
            if parent:
                self.node.parent = parent
            else:
                self.rootNode = parent = nodeClass() # This is a dummy parent node.
                parent.headString = 'dummyNode'
            parent.children.append(self.node)
            
            for bunch in self.attrsToList(attrs):
                self.node.doAttribute(bunch.name,bunch.val)
    
            self.nodeStack.append(parent)
    #@nonl
    #@-node:ekr.20060904134958.181:doStartElement
    #@+node:ekr.20060904134958.182:doEndElement
    def doEndElement (self,elementName):
        
        elementName = elementName.lower()
        
        if elementName in printElements:
            indent = '\t' * (self.level-1) or ''
            print '%s</%s>' % (indent,self.clean(elementName).strip())
            
        if elementName == 'body':
            self.inBody= False
        elif elementName == 'head':
            self.inHead = False
        elif elementName == 'outline':
            self.level -= 1
            self.node = self.nodeStack.pop()
    #@nonl
    #@-node:ekr.20060904134958.182:doEndElement
    #@+node:ekr.20060904134958.183:getNode
    def getNode (self):
        
        return self.rootNode
    #@nonl
    #@-node:ekr.20060904134958.183:getNode
    #@-others
#@nonl
#@-node:ekr.20060904134958.164:class contentHandler (XMLGenerator)
#@+node:ekr.20060904141220:class nodeClass
class nodeClass:
    
    '''A class representing one outline element.
    
    Use getters to access the attributes, properties and rules of this mode.'''
    
    #@    @+others
    #@+node:ekr.20060904141220.1: node.__init__
    def __init__ (self):
    
        self.attributes = {}
        self.bodyString = ''
        self.headString = ''
        self.children = []
        self.parent = None
        self.tnx = None
    #@nonl
    #@-node:ekr.20060904141220.1: node.__init__
    #@+node:ekr.20060904141220.2: node.__str__ & __repr__
    def __str__ (self):
        
        h = g.toUnicode(self.headString,'utf-8') or ''
        return '<node: %s>' % h
        
    __repr__ = __str__
    #@nonl
    #@-node:ekr.20060904141220.2: node.__str__ & __repr__
    #@+node:ekr.20060904141220.34:doAttribute
    def doAttribute (self,name,val):
        
        node = self
        name = g.toUnicode(name,encoding='utf-8').lower()
        val  = g.toUnicode(val,encoding='utf-8')
        
        # g.trace(name,val)
        
        if name == 'head':
            node.headString = val
        elif name == 'body':
            node.bodyString = val
        elif name == 'tx':
            node.tnx = val
        else:
            node.attributes[name] = val
    #@nonl
    #@-node:ekr.20060904141220.34:doAttribute
    #@+node:ekr.20060913220507:dump
    def dump (self):
        
        h = g.toUnicode(self.headString,'utf-8') or ''
        
        print
        print 'node: %s' % h
        print 'parent: %s' % self.parent or 'None'
        print 'children:',[child for child in self.children]
        print 'attrs:',self.attributes.values()
    #@nonl
    #@-node:ekr.20060913220507:dump
    #@-others
#@nonl
#@-node:ekr.20060904141220:class nodeClass
#@-others
#@nonl
#@-node:ekr.20060904103412:@thin leoOPML.py
#@-leo
