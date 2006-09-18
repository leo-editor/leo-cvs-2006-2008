#@+leo-ver=4-thin
#@+node:ekr.20060904103412:@thin __saxRead__.py
'''A *temporary* plugin to read Leo outlines using a SAX parser.'''

#@@language python
#@@tabwidth -4
#@@pagewidth 80

__version__ = '0.8'

# To do: body text in cloned trees not set properly.
# To do: Handle uA's

# For traces.
printElements = [] # 'v', 'all',

#@<< version history >>
#@+node:ekr.20060904103412.2:<< version history >>
#@@killcolor
#@+at
# 
# 0.1 EKR: Initial version based on version 0.06 of the opml plugin.
# 0.2 EKR: Beginning transition to elements found in .leo files.
# 0.3 EKR: Most of read logic is working.
# 0.4 EKR:
# - Refactored using start/end methods called via dispatch table.
# - Added inElement method and removed all inX flags and knownElements list.
# 0.5 EKR: tnodes now handled properly, so body text is read correctly.
# 0.6 EKR: Removed all calls to g.toUnicode.
# All contentHandler data is unicode.
# Hopefully the content handler can determine the encoding from the <?xml> 
# element.
# 0.7 EKR: Handled <globals> and <global_window_position> elements.
# 0.8 EKR: Handled 'a' attributes (marked, etc) of vnodes.
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
        saxReadController(c)
#@nonl
#@-node:ekr.20060904103412.5:onCreate
#@+node:ekr.20060904132527.10:onStart2 (overrides leoFileCommands.fileCommands)
def onStart2 (tag,keys):

    # Override the fileCommands class with the saxReadCommandsClass.
    leoFileCommands.fileCommands = saxReadCommandsClass
#@nonl
#@-node:ekr.20060904132527.10:onStart2 (overrides leoFileCommands.fileCommands)
#@-node:ekr.20060904132527.9:Module level
#@+node:ekr.20060904132527.11:class saxReadCommandsClass (fileCommands)
class saxReadCommandsClass (leoFileCommands.fileCommands):
    
    #@    @+others
    #@+node:ekr.20060904134958.116:parse_leo_file
    def parse_leo_file (self,inputFileName):
    
        if not inputFileName or not inputFileName.endswith('.leo'):
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
                # Hopefully the content handler can figure out the encoding from the <?xml> element.
                handler = contentHandler(c,inputFileName)
                parser.setContentHandler(handler)
                parser.parse(f)
                node = handler.getNode()
            except xml.sax.SAXParseException:
                g.es_print('Error parsing %s' % (inputFileName),color='red')
                g.es_exception()
            except Exception:
                g.es_print('Unexpected exception parsing %s' % (inputFileName),color='red')
                g.es_exception()
        finally:
            f.close()
            return node
    #@nonl
    #@-node:ekr.20060904134958.116:parse_leo_file
    #@-others
#@nonl
#@-node:ekr.20060904132527.11:class saxReadCommandsClass (fileCommands)
#@+node:ekr.20060904103412.6:class saxReadController
class saxReadController:
    
    #@    @+others
    #@+node:ekr.20060904103412.7:__init__
    def __init__ (self,c):
        
        self.c = c
        
        c.saxReadCommands = self # Override Leo's core commands.
        
        self.currentVnode = None
        self.topVnode = None
    #@nonl
    #@-node:ekr.20060904103412.7:__init__
    #@+node:ekr.20060914163456:createVnodes & helpers
    def createVnodes (self, dummyRoot):
        
        '''**Important**: this method and its helpers are low-level code
        corresponding to link/unlink methods in leoNodes.py.
        Modify this with extreme care.'''
        
        self.txnToVnodeDict = {}
    
        children = self.createChildren(dummyRoot,parent_v = None)
        firstChild = children and children[0]
    
        return firstChild
    #@+node:ekr.20060914171659.2:createChildren
    # node is a nodeClass object, parent_v is a vnode.
    
    def createChildren (self, node, parent_v):
        
        result = []
        
        for child in node.children:
            tnx = child.tnx
            v = self.txnToVnodeDict.get(tnx)
            if v:
                # A clone.  Create a new clone node, but share the subtree, i.e., the tnode.
                g.trace('clone',child.headString,v.t) # len(v.t.bodyString))
                v = self.createVnode(child,parent_v,t=v.t)
            else:
                v = self.createVnodeTree(child,parent_v)
                self.txnToVnodeDict [tnx] = v
            result.append(v)
            
        self.linkSiblings(result)
        if parent_v: self.linkParentAndChildren(parent_v,result)
        return result
    #@nonl
    #@-node:ekr.20060914171659.2:createChildren
    #@+node:ekr.20060914171659:createVnodeTree
    def createVnodeTree (self,node,parent_v):
    
        v = self.createVnode(node,parent_v)
        
        # To do: create the children only if v is not a clone.
        self.createChildren(node,v)
    
        return v
    #@nonl
    #@-node:ekr.20060914171659:createVnodeTree
    #@+node:ekr.20060914171659.1:createVnode
    def createVnode (self,node,parent_v,t=None):
        
        h = node.headString
        b = node.bodyString
    
        if not t:
            t = leoNodes.tnode(bodyString=b,headString=h)
        v = leoNodes.vnode(t)
        v.t.vnodeList.append(v)
        v._parent = parent_v
        
        self.handleVnodeAttributes(node,v)
        
        if 0:
            h1 = v.headString()
            h2 = parent_v and parent_v.headString() or 'None'
            g.trace('node: %12s parent: %12s' % (h1[:12],h2[:12]))
        
        return v
    #@nonl
    #@+node:ekr.20060916115633:handleVnodeAttributes
    def handleVnodeAttributes (self,node,v):
    
        attrs = node.attributes.get('a')
        if attrs:
            # g.trace('a=%s %s' % (attrs,v.headString()))
            
            # 'C' (clone) and 'D' bits are not used.
            if 'M' in attrs: v.setMarked()
            if 'E' in attrs: v.expand()
            if 'O' in attrs: v.setOrphan()
            if 'T' in attrs: self.topVnode = v
            if 'V' in attrs: self.currentVnode = v
    #@nonl
    #@-node:ekr.20060916115633:handleVnodeAttributes
    #@-node:ekr.20060914171659.1:createVnode
    #@+node:ekr.20060914174806:linkParentAndChildren
    def linkParentAndChildren (self, parent_v, children):
        
        # if children: g.trace(parent_v,len(children))
        
        firstChild_v = children and children[0] or None
    
        parent_v.t._firstChild = firstChild_v
        
        for child in children:
            child._parent = parent_v
        
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
        
        if not root:
            print 'dumpTree: empty tree'
            return
        if not dummy:
            root.dump()
        for child in root.children:
            self.dumpTree(child,dummy=False)
    #@nonl
    #@-node:ekr.20060913220707:dumpTree
    #@+node:ekr.20060904103721:readFile
    def readFile (self,event=None,fileName=None):
        
        if not fileName: return
    
        c = self.c
        
        # Pass one: create the intermediate nodes.
        self.dummyRoot = dummyRoot = c.fileCommands.parse_leo_file(fileName)
    
        # self.dumpTree(dummyRoot,dummy=True)
    
        # Pass two: create the tree of vnodes and tnodes from the intermediate nodes.
        v = dummyRoot and self.createVnodes(dummyRoot)
        if v:
            c2 = c.new()
            c2.setRootVnode(v)
            c2.checkOutline()
            self.setCurrentPosition(c2)
            c2.redraw()
            return c2 # For testing.
        return None
    #@nonl
    #@-node:ekr.20060904103721:readFile
    #@+node:ekr.20060916120609:setCurrentPosition
    def setCurrentPosition (self,c):
        
        v = self.currentVnode
        if not v: return
    
        for p in c.allNodes_iter():
            if p.v == v:
                c.selectPosition(p)
                break
    #@nonl
    #@-node:ekr.20060916120609:setCurrentPosition
    #@-others
#@nonl
#@-node:ekr.20060904103412.6:class saxReadController
#@+node:ekr.20060904141220:class nodeClass
class nodeClass:
    
    '''A class representing one <v> element.
    
    Use getters to access the attributes, properties and rules of this mode.'''
    
    #@    @+others
    #@+node:ekr.20060904141220.1: node.__init__
    def __init__ (self):
    
        self.attributes = {}
        self.bodyString = ''
        self.headString = ''
        self.children = []
        self.tnx = None
    #@nonl
    #@-node:ekr.20060904141220.1: node.__init__
    #@+node:ekr.20060904141220.2: node.__str__ & __repr__
    def __str__ (self):
    
        return '<v: %s>' % self.headString
    
    __repr__ = __str__
    #@nonl
    #@-node:ekr.20060904141220.2: node.__str__ & __repr__
    #@+node:ekr.20060913220507:node.dump
    def dump (self):
         
        print
        print 'node: tnx: %s %s' % (self.tnx,self.headString)
        print 'children:',g.listToString([child for child in self.children])
        print 'attrs:',self.attributes.values()
    #@nonl
    #@-node:ekr.20060913220507:node.dump
    #@-others
#@nonl
#@-node:ekr.20060904141220:class nodeClass
#@+node:ekr.20060904134958.164:class contentHandler (XMLGenerator)
class contentHandler (xml.sax.saxutils.XMLGenerator):
    
    '''A sax content handler class that reads Leo files.'''

    #@    @+others
    #@+node:ekr.20060904134958.165: __init__ & helpers
    def __init__ (self,c,inputFileName):
    
        self.c = c
        self.inputFileName = inputFileName
    
        # Init the base class.
        xml.sax.saxutils.XMLGenerator.__init__(self)
        
        #@    << define dispatch dict >>
        #@+node:ekr.20060915210537:<< define dispatch dict >>
        # There is no need for an 'end' method if all info is carried in attributes.
        
        self.dispatchDict = {
            'find_panel_settings':         (None,None),
            'globals':                     (self.startGlobals,None),
            'global_log_window_position':  (None,None), # The position of the log window is no longer used.
            'global_window_position':      (self.startWinPos,None),
            'leo_file':                    (None,None),
            'leo_header':                  (self.startLeoHeader,None),
            'preferences':                 (None,None),
            't':                           (self.startTnode,self.endTnode),
            'tnodes':                      (None,None),
            'v':                           (self.startVnode,self.endVnode),
            'vh':                          (self.startVH,self.endVH),
            'vnodes':                      (None,None),
        }
        #@nonl
        #@-node:ekr.20060915210537:<< define dispatch dict >>
        #@nl
        
        # Global attributes of the .leo file.
        self.body_outline_ratio = None
        
        self.global_window_position = {}
        self.encoding = 'utf-8'
        
        
        # Semantics.
        self.content = None
        self.elementStack = []
        self.errors = 0
        self.txnToVnodeDict = {} # Keys are tnx's (strings), values are vnodes.
        self.txnToNodeDict = {}  # Keys are tnx's (strings), values are nodeClass objects
        self.level = 0
        self.node = None
        self.nodeStack = []
        self.rootNode = None
    #@-node:ekr.20060904134958.165: __init__ & helpers
    #@+node:ekr.20060904134958.166:helpers
    #@+node:ekr.20060904134958.167:attrsToList
    def attrsToList (self,attrs):
        
        '''Convert the attributes to a list of g.Bunches.
        
        attrs: an Attributes item passed to startElement.'''
        
        if 1:
            for name in attrs.getNames():
                val = attrs.getValue(name)
                if type(val) != type(u''):
                    g.trace('Non-unicode attribute',name,val)
    
        # g.trace(g.listToString([repr() for name in attrs.getNames()]))
        
        return [
            g.Bunch(name=name,val=attrs.getValue(name))
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
        
        self.errors += 1
    #@nonl
    #@-node:ekr.20060904134958.170:error
    #@+node:ekr.20060915211757:inElement
    def inElement (self,name):
        
        return self.elementStack and name in self.elementStack
    #@nonl
    #@-node:ekr.20060915211757:inElement
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
    
        if name.lower() in ['v','t','vnodes','tnodes',]:
            print
    #@nonl
    #@-node:ekr.20060904134958.171:printStartElement
    #@-node:ekr.20060904134958.166:helpers
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
        
        if 1:
            if content and type(content) != type(u''):
                g.trace('Non-unicode content',repr(content))
    
        content = content.replace('\r','')
        if not content: return
    
        elementName = self.elementStack and self.elementStack[-1].lower() or '<no element name>'
        
        if elementName in ('t','vh'):
            # if elementName == 'vh': g.trace(elementName,repr(content))
            self.content.append(content)
    
        elif content.strip():
            print 'unexpected content:',elementName,repr(content)
    #@nonl
    #@-node:ekr.20060904134958.178:characters
    #@+node:ekr.20060904134958.179:endElement & helpers
    def endElement(self,name):
        
        name = name.lower()
        if name in printElements or 'all' in printElements:
            indent = '\t' * (self.level-1) or ''
            print '%s</%s>' % (indent,self.clean(name).strip())
        
        data = self.dispatchDict.get(name)
    
        if data is None:
            g.trace('unknown element',name)
        else:
            junk,func = data
            if func:
                func()
    
        name2 = self.elementStack.pop()
        assert name == name2
    #@nonl
    #@+node:ekr.20060916074444:endTnode
    def endTnode (self):
        
        if self.node:
            self.node.bodyString = ''.join(self.content)
    
        self.content = []
    #@nonl
    #@-node:ekr.20060916074444:endTnode
    #@+node:ekr.20060915211611:endVnode
    def endVnode (self):
        
        self.level -= 1
        self.node = self.nodeStack.pop()
    #@nonl
    #@-node:ekr.20060915211611:endVnode
    #@+node:ekr.20060915211611.1:endVH
    def endVH (self):
          
        if self.node:
            self.node.headString = ''.join(self.content)
    
        self.content = []
    #@nonl
    #@-node:ekr.20060915211611.1:endVH
    #@-node:ekr.20060904134958.179:endElement & helpers
    #@+node:ekr.20060904134958.180:startElement & helpers
    def startElement(self,name,attrs):
        
        name = name.lower()
        if name in printElements or 'all' in printElements:
            self.printStartElement(name,attrs)
    
        self.elementStack.append(name)
        
        data = self.dispatchDict.get(name)
    
        if data is None:
            g.trace('unknown element',name)
        else:
            func,junk = data
            if func:
                func(attrs)
    #@nonl
    #@+node:ekr.20060916112053:getPositionAttributes
    def getPositionAttributes (self,attrs):
        
        d = {}
        
        for bunch in self.attrsToList(attrs):
            name = bunch.name ; val = bunch.val
            if name in ('top','left','width','height'):
                try:
                    d[name] = int(val)
                except ValueError:
                    d[name] = 100 # A reasonable emergency default.
            else:
                g.trace(name,len(val))
                
        return d
    #@nonl
    #@-node:ekr.20060916112053:getPositionAttributes
    #@+node:ekr.20060916111049:startGlobals
    def startGlobals (self,attrs):
        
        for bunch in self.attrsToList(attrs):
            name = bunch.name ; val = bunch.val
            
            if name == 'body_outline_ratio':
                self.body_outline_ratio = val
                # g.trace(name,val)
            else:
                g.trace(name,len(val))
    #@nonl
    #@-node:ekr.20060916111049:startGlobals
    #@+node:ekr.20060915210537.4:startWinPos
    def startWinPos (self,attrs):
        
        self.global_window_position = self.getPositionAttributes(attrs)
        # g.trace(self.global_window_position)
    #@nonl
    #@-node:ekr.20060915210537.4:startWinPos
    #@+node:ekr.20060915210537.5:startLeoHeader
    def startLeoHeader (self,attrs):
        
        self.txnToNodeDict = {}
    #@nonl
    #@-node:ekr.20060915210537.5:startLeoHeader
    #@+node:ekr.20060915104021:startVH
    def startVH (self,attrs):
    
        self.content = []
    #@nonl
    #@-node:ekr.20060915104021:startVH
    #@+node:ekr.20060915101510:startTnode
    def startTnode (self,attrs):
        
        if not self.inElement('tnodes'):
            self.error('<t> outside <tnodes>')
            
        self.content = []
        
        self.tnodeAttributes(attrs)
    #@nonl
    #@+node:ekr.20060916071326:tnodeAttributes
    def tnodeAttributes (self,attrs):
        
        # The tnode must have a tx attribute to associate content with the proper node.
            
        self.node = None
    
        for bunch in self.attrsToList(attrs):
            name = bunch.name ; val = bunch.val
            if name == 'tx':
                self.node = self.txnToNodeDict.get(val)
                if not self.node:
                    self.error('Bad leo file: no node for <t tx=%s>' % (val))
            else:
                # Do **not** set any nodeClass attributes here!
                self.error('Unexpected tnode attribute %s = %s' % (name,val))
                
        if not self.node:
            self.error('Bad leo file: no tx attribute for tnode')
    #@nonl
    #@-node:ekr.20060916071326:tnodeAttributes
    #@-node:ekr.20060915101510:startTnode
    #@+node:ekr.20060915101510.1:startVnode
    def startVnode (self,attrs):
        
        if not self.inElement('vnodes'):
            self.error('<v> outside <vnodes>')
    
        if self.rootNode:
            parent = self.node
        else:
            self.rootNode = parent = nodeClass() # The dummy parent node.
            parent.headString = 'dummyNode'
    
        self.node = nodeClass()
    
        parent.children.append(self.node)
        self.vnodeAttributes(attrs)
        self.nodeStack.append(parent)
            
        return parent
    #@nonl
    #@+node:ekr.20060916064339:vnodeAttributes
    def vnodeAttributes (self,attrs):
        
        node = self.node
    
        for bunch in self.attrsToList(attrs):
            name = bunch.name ; val = bunch.val
            if name == 't':
                self.txnToNodeDict[val] = self.node
                node.tnx = val
            else:
                node.attributes[name] = val
                # g.trace(name,len(val))
    #@nonl
    #@-node:ekr.20060916064339:vnodeAttributes
    #@-node:ekr.20060915101510.1:startVnode
    #@-node:ekr.20060904134958.180:startElement & helpers
    #@+node:ekr.20060904134958.183:getNode
    def getNode (self):
        
        return self.rootNode
    #@nonl
    #@-node:ekr.20060904134958.183:getNode
    #@-others
#@nonl
#@-node:ekr.20060904134958.164:class contentHandler (XMLGenerator)
#@-others
#@nonl
#@-node:ekr.20060904103412:@thin __saxRead__.py
#@-leo
