<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet ekr_stylesheet?>
<leo_file>
<leo_header file_format="2" tnodes="0" max_tnode_index="586" clone_windows="0"/>
<globals body_outline_ratio="0.5">
	<global_window_position top="61" left="430" height="816" width="850"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="ekr.20060904103412" a="E"><vh>@thin __saxRead__.py</vh></v>
<v t="ekr.20060915095311" a="E"><vh>Recent</vh>
<v t="ekr.20060904134958.165"><vh> __init__ &amp; helpers</vh></v>
<v t="ekr.20060904103721"><vh>readFile</vh></v>
<v t="ekr.20060904134958.181"><vh>doStartElement</vh></v>
<v t="ekr.20060904134958.182"><vh>doEndElement</vh></v>
<v t="ekr.20060904134958.178"><vh>characters</vh></v>
<v t="ekr.20060904141220.34"><vh>node.doAttribute</vh></v>
<v t="ekr.20060913220507"><vh>node.dump</vh></v>
<v t="ekr.20060914163456"><vh>createVnodes &amp; helpers</vh>
<v t="ekr.20060914171659.2"><vh>createChildren</vh></v>
<v t="ekr.20060914171659"><vh>createVnodeTree</vh></v>
<v t="ekr.20060914171659.1"><vh>createVnode</vh></v>
<v t="ekr.20060914174806"><vh>linkParentAndChildren</vh></v>
<v t="ekr.20060914165257"><vh>linkSiblings</vh></v>
</v>
<v t="ekr.20060904134958.171"><vh>printStartElement</vh></v>
</v>
</vnodes>
<tnodes>
<t tx="ekr.20060904103721">def readFile (self,event=None,fileName=None):
    
    if not fileName: return
    
    # g.trace('='*60)

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
        c2.redraw()</t>
<t tx="ekr.20060904134958.165">def __init__ (self,c,inputFileName):

    self.c = c
    self.inputFileName = inputFileName

    # Init the base class.
    xml.sax.saxutils.XMLGenerator.__init__(self)
    
    # Parsing.
    self.knownElements = (
        'find_panel_settings','globals',
        'global_log_window_position','global_window_position',
        'leo_file','leo_header','preferences',
    )
  
    # Semantics.
    self.content = None
    self.elementStack = []
    self.inHead = False
    self.inTnode = False
    self.inTnodes = False
    self.inVnode = False
    self.inVnodes = False
    
    self.level = 0
    self.node = None
    self.nodeStack = []
    self.rootNode = None</t>
<t tx="ekr.20060904134958.171">def printStartElement(self,name,attrs):
    
    indent = '\t' * self.level or ''

    if attrs.getLength() &gt; 0:
        print '%s&lt;%s %s&gt;' % (
            indent,
            self.clean(name).strip(),
            self.attrsToString(attrs,sep=' ')),
    else:
        print '%s&lt;%s&gt;' % (
            indent,
            self.clean(name).strip()),

    if name.lower() in ['v','t','vnodes','tnodes',]:
        print</t>
<t tx="ekr.20060904134958.178">def characters(self,content):

    content = g.toUnicode(content,encoding='utf-8') or ''
    content = content.replace('\r','')
    if not content: return

    elementName = self.elementStack and self.elementStack[-1].lower() or '&lt;no element name&gt;'
    
    if elementName == 'vh':
        g.trace('vh:',repr(content))
        self.content.append(content)

    elif content and elementName not in ('t','v','tnodes'):
        print 'unexpected content:',elementName,content</t>
<t tx="ekr.20060904134958.181">def doStartElement (self,elementName,attrs):
    
    elementName = elementName.lower()

    if elementName in printElements:
        self.printStartElement(elementName,attrs)
        
    if elementName == 't':
        self.inTnode = True
        self.startTnode(attrs)
    elif elementName == 'tnodes':
        self.inTnodes = True
    elif elementName == 'v':
        self.inVnode = True
        self.level += 1
        node = self.startVnode(attrs)
        self.nodeStack.append(node)
    elif elementName == 'vh':
        self.inHead = True
        self.startHead(attrs)
    elif elementName == 'vnodes':
        self.inVnodes= True
    elif elementName not in self.knownElements:
        g.trace('unknown element',elementName)
   </t>
<t tx="ekr.20060904134958.182">def doEndElement (self,elementName):
    
    elementName = elementName.lower()
    
    if elementName in printElements:
        indent = '\t' * (self.level-1) or ''
        print '%s&lt;/%s&gt;' % (indent,self.clean(elementName).strip())
        
    if elementName == 't':
        self.inTnode = False
    elif elementName == 'tnodes':
        self.inTnodes = False
    elif elementName == 'v':
        self.inVnode = False
        self.level -= 1
        # self.node.headString = ''.join(self.content)
        # self.content = []
        self.node = self.nodeStack.pop()
    elif elementName == 'vh':
        self.inHead = False
        if self.node:
            self.node.headString = ''.join(self.content)
        self.content = []
    elif elementName == 'vnodes':
        self.inVnodes= False
    elif elementName not in self.knownElements:
        g.trace('unknown element',elementName)</t>
<t tx="ekr.20060904141220.34">def doAttribute (self,name,val):
    
    node = self
    name = g.toUnicode(name,encoding='utf-8').lower()
    val  = g.toUnicode(val,encoding='utf-8')
    
    if not name.startswith('xcc') and not name in ('t',):
        g.trace(name,len(str(val)))
    
    if name == 't':
        node.tnx = val
    else:
        node.attributes[name] = val</t>
<t tx="ekr.20060913220507">def dump (self):
    
    h = g.toUnicode(self.headString,'utf-8') or ''
    
    print
    print 'node: tnx: %s %s' % (self.tnx,h)
    print 'parent: %s' % self.parent or 'None'
    print 'children:',[child for child in self.children]
    print 'attrs:',self.attributes.values()</t>
<t tx="ekr.20060914163456">def createVnodes (self, dummyRoot):
    
    '''**Important**: this method and its helpers are low-level code
    corresponding to link/unlink methods in leoNodes.py.
    Modify this with extreme care.'''
    
    self.generatedTnxs = {}

    children = self.createChildren(dummyRoot,parent_v = None)
    firstChild = children and children[0]

    return firstChild
</t>
<t tx="ekr.20060914165257">def linkSiblings (self, sibs):
    
    '''Set the v._back and v._next links for all vnodes v in sibs.'''
    
    n = len(sibs)

    for i in xrange(n):
        v = sibs[i]
        v._back = (i-1 &gt;= 0 and sibs[i-1]) or None
        v._next = (i+1 &lt;  n and sibs[i+1]) or None</t>
<t tx="ekr.20060914171659">def createVnodeTree (self,node,parent_v):

    v = self.createVnode(node,parent_v)
    
    # To do: create the children only if v is not a clone.
    self.createChildren(node,v)

    return v</t>
<t tx="ekr.20060914171659.1">def createVnode (self,node,parent_v,t=None):
    
    h = node.headString
    b = node.bodyString
    if not t:
        t = leoNodes.tnode(bodyString=b,headString=h)
    v = leoNodes.vnode(t)
    v.t.vnodeList.append(v)
    v._parent = parent_v
    
    if 0:
        h1 = v.headString()
        h2 = parent_v and parent_v.headString() or 'None'
        g.trace('node: %12s parent: %12s' % (h1[:12],h2[:12]))
    
    return v</t>
<t tx="ekr.20060914171659.2"># node is a nodeClass object, parent_v is a vnode.

def createChildren (self, node, parent_v):
    
    result = []
    
    for child in node.children:
        tnx = child.tnx
        v = self.generatedTnxs.get(tnx)
        if v:
            # A clone.  Create a new clone node, but share the subtree, i.e., the tnode.
            # g.trace('clone',child.headString)
            v = self.createVnode(child,parent_v,t=v.t)
        else:
            v = self.createVnodeTree(child,parent_v)
            self.generatedTnxs [tnx] = v
        result.append(v)
        
    self.linkSiblings(result)
    if parent_v: self.linkParentAndChildren(parent_v,result)
    return result</t>
<t tx="ekr.20060914174806">def linkParentAndChildren (self, parent_v, children):
    
    # if children: g.trace(parent_v,len(children))
    
    firstChild_v = children and children[0] or None

    parent_v.t._firstChild = firstChild_v
    
    for child in children:
        child._parent = parent_v
    
    v = parent_v
    if v not in v.t.vnodeList:
        v.t.vnodeList.append(v)</t>
<t tx="ekr.20060915095311"></t>
</tnodes>
</leo_file>
