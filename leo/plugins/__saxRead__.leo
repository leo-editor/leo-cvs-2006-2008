<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet ekr_stylesheet?>
<leo_file>
<leo_header file_format="2" tnodes="0" max_tnode_index="587" clone_windows="0"/>
<globals body_outline_ratio="0.5">
	<global_window_position top="89" left="458" height="816" width="850"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="ekr.20060904103412" a="ETV"
expanded="ekr.20060914171659.1,ekr.20060904134958.166,ekr.20060915101510.1,"><vh>@thin __saxRead__.py</vh></v>
<v t="ekr.20060915095311"><vh>Recent</vh>
<v t="ekr.20060904134958.165"><vh> __init__ &amp; helpers</vh>
<v t="ekr.20060915210537"><vh>&lt;&lt; define dispatch dict &gt;&gt;</vh></v>
</v>
<v t="ekr.20060904134958.116" a="M"><vh>parse_leo_file</vh></v>
<v t="ekr.20060904103721"><vh>readFile</vh></v>
<v t="ekr.20060904134958.178"><vh>characters</vh></v>
<v t="ekr.20060904134958.180"><vh>startElement &amp; helpers</vh>
<v t="ekr.20060916112053"><vh>getPositionAttributes</vh></v>
<v t="ekr.20060916111049" a="E"><vh>startGlobals</vh></v>
<v t="ekr.20060915210537.4"><vh>startWinPos</vh></v>
<v t="ekr.20060915210537.5"><vh>startLeoHeader</vh></v>
<v t="ekr.20060915104021"><vh>startVH</vh></v>
<v t="ekr.20060915101510"><vh>startTnode</vh>
<v t="ekr.20060916071326"><vh>tnodeAttributes</vh></v>
</v>
<v t="ekr.20060915101510.1" a="E"><vh>startVnode</vh>
<v t="ekr.20060916064339"><vh>vnodeAttributes</vh></v>
</v>
</v>
<v t="ekr.20060904134958.179"><vh>endElement &amp; helpers</vh>
<v t="ekr.20060916074444"><vh>endTnode</vh></v>
<v t="ekr.20060915211611"><vh>endVnode</vh></v>
<v t="ekr.20060915211611.1"><vh>endVH</vh></v>
</v>
<v t="ekr.20060914163456" a="E"><vh>createVnodes &amp; helpers</vh>
<v t="ekr.20060914171659.2"><vh>createChildren</vh></v>
<v t="ekr.20060914171659"><vh>createVnodeTree</vh></v>
<v t="ekr.20060914171659.1" a="E"><vh>createVnode</vh>
<v t="ekr.20060916115633"><vh>handleVnodeAttributes</vh></v>
</v>
<v t="ekr.20060914174806"><vh>linkParentAndChildren</vh></v>
<v t="ekr.20060914165257"><vh>linkSiblings</vh></v>
</v>
</v>
</vnodes>
<tnodes>
<t tx="ekr.20060904103721">def readFile (self,event=None,fileName=None):
    
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
        c2.redraw()</t>
<t tx="ekr.20060904134958.116">def parse_leo_file (self,inputFileName):

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
            # Hopefully the content handler can figure out the encoding from the &lt;?xml&gt; element.
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
        return node</t>
<t tx="ekr.20060904134958.165">def __init__ (self,c,inputFileName):

    self.c = c
    self.inputFileName = inputFileName

    # Init the base class.
    xml.sax.saxutils.XMLGenerator.__init__(self)
    
    &lt;&lt; define dispatch dict &gt;&gt;
    
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
</t>
<t tx="ekr.20060904134958.178">def characters(self,content):
    
    if 1:
        if content and type(content) != type(u''):
            g.trace('Non-unicode content',repr(content))

    content = content.replace('\r','')
    if not content: return

    elementName = self.elementStack and self.elementStack[-1].lower() or '&lt;no element name&gt;'
    
    if elementName in ('t','vh'):
        # if elementName == 'vh': g.trace(elementName,repr(content))
        self.content.append(content)

    elif content.strip():
        print 'unexpected content:',elementName,repr(content)</t>
<t tx="ekr.20060904134958.179">def endElement(self,name):
    
    name = name.lower()
    if name in printElements or 'all' in printElements:
        indent = '\t' * (self.level-1) or ''
        print '%s&lt;/%s&gt;' % (indent,self.clean(name).strip())
    
    data = self.dispatchDict.get(name)

    if data is None:
        g.trace('unknown element',name)
    else:
        junk,func = data
        if func:
            func()

    name2 = self.elementStack.pop()
    assert name == name2</t>
<t tx="ekr.20060904134958.180">def startElement(self,name,attrs):
    
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
            func(attrs)</t>
<t tx="ekr.20060914163456">def createVnodes (self, dummyRoot):
    
    '''**Important**: this method and its helpers are low-level code
    corresponding to link/unlink methods in leoNodes.py.
    Modify this with extreme care.'''
    
    self.txnToVnodeDict = {}

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
    
    self.handleVnodeAttributes(node,v)
    
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
        v = self.txnToVnodeDict.get(tnx)
        if v:
            # A clone.  Create a new clone node, but share the subtree, i.e., the tnode.
            # g.trace('clone',child.headString)
            v = self.createVnode(child,parent_v,t=v.t)
        else:
            v = self.createVnodeTree(child,parent_v)
            self.txnToVnodeDict [tnx] = v
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
<t tx="ekr.20060915101510">def startTnode (self,attrs):
    
    if not self.inElement('tnodes'):
        self.error('&lt;t&gt; outside &lt;tnodes&gt;')
        
    self.content = []
    
    self.tnodeAttributes(attrs)</t>
<t tx="ekr.20060915101510.1">def startVnode (self,attrs):
    
    if not self.inElement('vnodes'):
        self.error('&lt;v&gt; outside &lt;vnodes&gt;')

    if self.rootNode:
        parent = self.node
    else:
        self.rootNode = parent = nodeClass() # The dummy parent node.
        parent.headString = 'dummyNode'

    self.node = nodeClass()

    parent.children.append(self.node)
    self.vnodeAttributes(attrs)
    self.nodeStack.append(parent)
        
    return parent</t>
<t tx="ekr.20060915104021">def startVH (self,attrs):

    self.content = []</t>
<t tx="ekr.20060915210537"># There is no need for an 'end' method if all info is carried in attributes.

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
}</t>
<t tx="ekr.20060915210537.4">def startWinPos (self,attrs):
    
    self.global_window_position = self.getPositionAttributes(attrs)
    # g.trace(self.global_window_position)</t>
<t tx="ekr.20060915210537.5">def startLeoHeader (self,attrs):
    
    self.txnToNodeDict = {}</t>
<t tx="ekr.20060915211611">def endVnode (self):
    
    self.level -= 1
    self.node = self.nodeStack.pop()</t>
<t tx="ekr.20060915211611.1">def endVH (self):
      
    if self.node:
        self.node.headString = ''.join(self.content)

    self.content = []</t>
<t tx="ekr.20060916064339">def vnodeAttributes (self,attrs):
    
    node = self.node

    for bunch in self.attrsToList(attrs):
        name = bunch.name ; val = bunch.val
        if name == 't':
            self.txnToNodeDict[val] = self.node
            node.tnx = val
        else:
            node.attributes[name] = val
            # g.trace(name,len(val))</t>
<t tx="ekr.20060916071326">def tnodeAttributes (self,attrs):
    
    # The tnode must have a tx attribute to associate content with the proper node.
        
    self.node = None

    for bunch in self.attrsToList(attrs):
        name = bunch.name ; val = bunch.val
        if name == 'tx':
            self.node = self.txnToNodeDict.get(val)
            if not self.node:
                self.error('Bad leo file: no node for &lt;t tx=%s&gt;' % (val))
        else:
            # Do **not** set any nodeClass attributes here!
            self.error('Unexpected tnode attribute %s = %s' % (name,val))
            
    if not self.node:
        self.error('Bad leo file: no tx attribute for tnode')</t>
<t tx="ekr.20060916074444">def endTnode (self):
    
    if self.node:
        self.node.bodyString = ''.join(self.content)

    self.content = []</t>
<t tx="ekr.20060916111049">def startGlobals (self,attrs):
    
    for bunch in self.attrsToList(attrs):
        name = bunch.name ; val = bunch.val
        
        if name == 'body_outline_ratio':
            self.body_outline_ratio = val
            # g.trace(name,val)
        else:
            g.trace(name,len(val))</t>
<t tx="ekr.20060916112053">def getPositionAttributes (self,attrs):
    
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
            
    return d</t>
<t tx="ekr.20060916115633">def handleVnodeAttributes (self,node,v):

    attrs = node.attributes.get('a')
    if attrs:
        g.trace('a=%s %s' % (attrs,v.headString()))
        # 'C' (clone) and 'D' bits are not used.
        if 'M' in attrs: v.setMarked()
        if 'E' in attrs: v.expand()
        if 'O' in attrs: v.setOrphan()
        if 'T' in attrs: self.topVnode = v
        if 'V' in attrs: self.currentVnode = v
        
    # if   self.matchChar('C'): pass # Not used: clone bits are recomputed later.
    # elif self.matchChar('D'): pass # Not used.
    # elif self.matchChar('E'): setExpanded = True
    # elif self.matchChar('M'): setMarked = True
    # elif self.matchChar('O'): setOrphan = True
    # elif self.matchChar('T'): setTop = True
    # elif self.matchChar('V'): setCurrent = True</t>
</tnodes>
</leo_file>
