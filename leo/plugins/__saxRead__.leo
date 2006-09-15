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
<v t="ekr.20060904103412" a="E"
expanded="ekr.20060904132527.9,ekr.20060904132527.11,ekr.20060904103412.6,ekr.20060904134958.180,"><vh>@thin __saxRead__.py</vh></v>
<v t="ekr.20060915095311" a="E"><vh>To change</vh>
<v t="ekr.20060904134958.182"><vh>doEndElement</vh></v>
<v t="ekr.20060904134958.181"><vh>doStartElement</vh></v>
<v t="ekr.20060904141220.34"><vh>node.doAttribute</vh></v>
<v t="ekr.20060913220507"><vh>node.dump</vh></v>
</v>
</vnodes>
<tnodes>
<t tx="ekr.20060904134958.181">def doStartElement (self,elementName,attrs):
    
    elementName = elementName.lower()

    if elementName in printElements:
        self.printStartElement(elementName,attrs)

    if elementName == 'body':
        self.inBody= True
    elif elementName == 'head':
        self.inHead = True
    elif elementName == 'outline':
        if self.inHead:     self.error('&lt;outline&gt; inside &lt;head&gt;')
        if not self.inBody: self.error('&lt;outline&gt; outside &lt;body&gt;')
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

        self.nodeStack.append(parent)</t>
<t tx="ekr.20060904134958.182">def doEndElement (self,elementName):
    
    elementName = elementName.lower()
    
    if elementName in printElements:
        indent = '\t' * (self.level-1) or ''
        print '%s&lt;/%s&gt;' % (indent,self.clean(elementName).strip())
        
    if elementName == 'body':
        self.inBody= False
    elif elementName == 'head':
        self.inHead = False
    elif elementName == 'outline':
        self.level -= 1
        self.node = self.nodeStack.pop()</t>
<t tx="ekr.20060904141220.34">def doAttribute (self,name,val):
    
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
        node.attributes[name] = val</t>
<t tx="ekr.20060913220507">def dump (self):
    
    h = g.toUnicode(self.headString,'utf-8') or ''
    
    print
    print 'node: tnx: %s %s' % (self.tnx,h)
    print 'parent: %s' % self.parent or 'None'
    print 'children:',[child for child in self.children]
    print 'attrs:',self.attributes.values()</t>
<t tx="ekr.20060915095311"></t>
</tnodes>
</leo_file>
