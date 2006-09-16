<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet ekr_stylesheet?>
<leo_file>
<leo_header file_format="2" tnodes="0" max_tnode_index="586" clone_windows="0"/>
<globals body_outline_ratio="0.5">
	<global_window_position top="84" left="373" height="816" width="850"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="ekr.20060904103412" a="ETV"><vh>@thin __saxRead__.py</vh></v>
<v t="ekr.20060915095311" a="E"><vh>Recent</vh>
<v t="ekr.20060915210537"><vh>&lt;&lt; define dispatch dict &gt;&gt;</vh></v>
<v t="ekr.20060904103721"><vh>readFile</vh></v>
<v t="ekr.20060904134958.178"><vh>characters</vh></v>
<v t="ekr.20060914163456"><vh>createVnodes &amp; helpers</vh>
<v t="ekr.20060914171659.2"><vh>createChildren</vh></v>
<v t="ekr.20060914171659"><vh>createVnodeTree</vh></v>
<v t="ekr.20060914171659.1"><vh>createVnode</vh></v>
<v t="ekr.20060914174806"><vh>linkParentAndChildren</vh></v>
<v t="ekr.20060914165257"><vh>linkSiblings</vh></v>
</v>
<v t="ekr.20060904134958.180"><vh>startElement &amp; helpers</vh>
<v t="ekr.20060915210537.3"><vh>startLogPos</vh></v>
<v t="ekr.20060915210537.4"><vh>startWinPos</vh></v>
<v t="ekr.20060915210537.5"><vh>startLeoHeader</vh></v>
<v t="ekr.20060915104021"><vh>startVH</vh></v>
<v t="ekr.20060915101510"><vh>startTnode</vh>
<v t="ekr.20060916071326"><vh>tnodeAttributes</vh></v>
</v>
<v t="ekr.20060915101510.1"><vh>startVnode</vh>
<v t="ekr.20060916064339"><vh>vnodeAttributes</vh></v>
</v>
</v>
<v t="ekr.20060904134958.179"><vh>endElement &amp; helpers</vh>
<v t="ekr.20060916074444"><vh>endTnode</vh></v>
<v t="ekr.20060915211611"><vh>endVnode</vh></v>
<v t="ekr.20060915211611.1"><vh>endVH</vh></v>
</v>
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
<t tx="ekr.20060904134958.178">def characters(self,content):

    content = g.toUnicode(content,encoding='utf-8') or ''
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

    parent = self.node
    self.node = nodeClass()

    if parent:
        self.node.parent = parent
    else:
        self.rootNode = parent = nodeClass() # This is a dummy parent node.
        parent.headString = 'dummyNode'
    
    parent.children.append(self.node)
    self.vnodeAttributes(attrs)
    self.nodeStack.append(parent)
        
    return parent</t>
<t tx="ekr.20060915104021">def startVH (self,attrs):

    self.content = []</t>
<t tx="ekr.20060915210537"># There is no need for an 'end' method if all info is carried in attributes.

self.dispatchDict = {
    'find_panel_settings':         (None,None),
    'globals':                     (None,None),
    'global_log_window_position':  (self.startLogPos,None),
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
<t tx="ekr.20060915210537.3">def startLogPos (self,attrs):
    
    pass</t>
<t tx="ekr.20060915210537.4">def startWinPos (self,attrs):
    
    pass</t>
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
</tnodes>
</leo_file>
