<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet ekr_stylesheet?>
<leo_file>
<leo_header file_format="2" tnodes="0" max_tnode_index="586" clone_windows="0"/>
<globals body_outline_ratio="0.48622754491">
	<global_window_position top="61" left="408" height="835" width="872"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="ekr.20060913211939"><vh>Not used</vh>
<v t="ekr.20060913211939.1"><vh>From nodeClass</vh>
<v t="ekr.20060904141220.40"><vh>startElement</vh></v>
<v t="ekr.20060904141220.36"><vh>endElement</vh></v>
<v t="ekr.20060904141220.35"><vh>doContent</vh></v>
<v t="ekr.20060904141220.38"><vh>getters</vh></v>
</v>
</v>
<v t="ekr.20060914203123"><vh>Reference</vh>
<v t="ekr.20060914203123.1"><vh>v.Link/Unlink/Insert methods (used by file read logic)</vh>
<v t="ekr.20060914203123.2"><vh>v.detach</vh></v>
<v t="ekr.20060914203123.3"><vh>v.insertAfter</vh></v>
<v t="ekr.20060914203123.4"><vh>v.insertAsNthChild</vh></v>
<v t="ekr.20060914203123.5"><vh>v.linkAsNthChild</vh></v>
<v t="ekr.20060914203123.6"><vh>v.linkAsRoot</vh></v>
<v t="ekr.20060914203123.7"><vh>v.moveToRoot</vh></v>
<v t="ekr.20060914203123.8"><vh>v.linkAfter</vh></v>
<v t="ekr.20060914203123.9"><vh>v.unlink</vh></v>
</v>
<v t="ekr.20060914203123.10"><vh>class tnode</vh>
<v t="ekr.20060914203123.11"><vh>&lt;&lt; tnode constants &gt;&gt;</vh></v>
<v t="ekr.20060914203123.12"><vh>t.__init__</vh></v>
<v t="ekr.20060914203123.13"><vh>t.__repr__ &amp; t.__str__</vh></v>
<v t="ekr.20060914203123.14"><vh>t.__hash__ (only for zodb)</vh></v>
<v t="ekr.20060914203123.15"><vh>Getters</vh>
<v t="ekr.20060914203123.16"><vh>getBody</vh></v>
<v t="ekr.20060914203123.17"><vh>t.hasBody</vh></v>
<v t="ekr.20060914203123.18"><vh>Status bits</vh>
<v t="ekr.20060914203123.19"><vh>isDirty</vh></v>
<v t="ekr.20060914203123.20"><vh>isRichTextBit</vh></v>
<v t="ekr.20060914203123.21"><vh>isVisited</vh></v>
<v t="ekr.20060914203123.22"><vh>isWriteBit</vh></v>
</v>
</v>
<v t="ekr.20060914203123.23"><vh>Setters</vh>
<v t="ekr.20060914203123.24"><vh>Setting body text</vh>
<v t="ekr.20060914203123.25"><vh>setTnodeText</vh></v>
<v t="ekr.20060914203123.26"><vh>setSelection</vh></v>
</v>
<v t="ekr.20060914203123.27"><vh>Status bits</vh>
<v t="ekr.20060914203123.28"><vh>clearDirty</vh></v>
<v t="ekr.20060914203123.29"><vh>clearRichTextBit</vh></v>
<v t="ekr.20060914203123.30"><vh>clearVisited</vh></v>
<v t="ekr.20060914203123.31"><vh>clearWriteBit</vh></v>
<v t="ekr.20060914203123.32"><vh>setDirty</vh></v>
<v t="ekr.20060914203123.33"><vh>setRichTextBit</vh></v>
<v t="ekr.20060914203123.34"><vh>setVisited</vh></v>
<v t="ekr.20060914203123.35"><vh>setWriteBit</vh></v>
</v>
<v t="ekr.20060914203123.36"><vh>setCloneIndex (used in 3.x)</vh></v>
<v t="ekr.20060914203123.37"><vh>setFileIndex</vh></v>
<v t="ekr.20060914203123.38"><vh>t.setHeadString (new in 4.3)</vh></v>
</v>
</v>
<v t="ekr.20060914203123.39"><vh>class vnode</vh>
<v t="ekr.20060914203123.40"><vh>&lt;&lt; vnode constants &gt;&gt;</vh></v>
<v t="ekr.20060914203123.41"><vh>Birth &amp; death</vh>
<v t="ekr.20060914203123.42"><vh>v.__cmp__ (not used)</vh></v>
<v t="ekr.20060914203123.43"><vh>v.__init__</vh></v>
<v t="ekr.20060914203123.44"><vh>v.__repr__ &amp; v.__str__</vh></v>
<v t="ekr.20060914203123.45"><vh>v.dump</vh></v>
<v t="ekr.20060914203123.46"><vh>v.__hash__ (only for zodb)</vh></v>
</v>
<v t="ekr.20060914203123.47"><vh>v.Comparisons</vh>
<v t="ekr.20060914203123.48"><vh>v.findAtFileName (new in 4.2 b3)</vh></v>
<v t="ekr.20060914203123.49"><vh>anyAtFileNodeName</vh></v>
<v t="ekr.20060914203123.50"><vh>at...FileNodeName</vh></v>
<v t="ekr.20060914203123.51"><vh>isAtAllNode</vh></v>
<v t="ekr.20060914203123.52"><vh>isAnyAtFileNode good</vh></v>
<v t="ekr.20060914203123.53"><vh>isAt...FileNode (vnode)</vh></v>
<v t="ekr.20060914203123.54"><vh>isAtIgnoreNode</vh></v>
<v t="ekr.20060914203123.55"><vh>isAtOthersNode</vh></v>
<v t="ekr.20060914203123.56"><vh>matchHeadline</vh></v>
</v>
<v t="ekr.20060914203123.57"><vh>Getters (vnode)</vh>
<v t="ekr.20060914203123.58"><vh>Tree Traversal getters</vh>
<v t="ekr.20060914203123.59"><vh>v.back</vh></v>
<v t="ekr.20060914203123.60"><vh>v.next</vh></v>
</v>
<v t="ekr.20060914203123.61"><vh>Children</vh>
<v t="ekr.20060914203123.62"><vh>v.childIndex</vh></v>
<v t="ekr.20060914203123.63"><vh>v.firstChild (changed for 4.2)</vh></v>
<v t="ekr.20060914203123.64"><vh>v.hasChildren &amp; hasFirstChild</vh></v>
<v t="ekr.20060914203123.65"><vh>v.lastChild</vh></v>
<v t="ekr.20060914203123.66"><vh>v.nthChild</vh></v>
<v t="ekr.20060914203123.67"><vh>v.numberOfChildren (n)</vh></v>
</v>
<v t="ekr.20060914203123.68"><vh>Status Bits</vh>
<v t="ekr.20060914203123.69"><vh>v.isCloned (4.2)</vh></v>
<v t="ekr.20060914203123.70"><vh>isDirty</vh></v>
<v t="ekr.20060914203123.71"><vh>isExpanded</vh></v>
<v t="ekr.20060914203123.72"><vh>isMarked</vh></v>
<v t="ekr.20060914203123.73"><vh>isOrphan</vh></v>
<v t="ekr.20060914203123.74"><vh>isSelected</vh></v>
<v t="ekr.20060914203123.75"><vh>isTopBitSet</vh></v>
<v t="ekr.20060914203123.76"><vh>isVisited</vh></v>
<v t="ekr.20060914203123.77"><vh>status</vh></v>
</v>
<v t="ekr.20060914203123.78"><vh>v.bodyString</vh></v>
<v t="ekr.20060914203123.79"><vh>v.headString &amp; v.cleanHeadString</vh></v>
<v t="ekr.20060914203123.80"><vh>v.directParents (new method in 4.2)</vh></v>
</v>
<v t="ekr.20060914203123.81"><vh>Setters</vh>
<v t="ekr.20060914203123.82"><vh> v.Status bits</vh>
<v t="ekr.20060914203123.83"><vh>clearClonedBit</vh></v>
<v t="ekr.20060914203123.84" a="M"><vh>v.clearDirty (no change needed)</vh></v>
<v t="ekr.20060914203123.85"><vh>v.clearMarked</vh></v>
<v t="ekr.20060914203123.86"><vh>clearOrphan</vh></v>
<v t="ekr.20060914203123.87"><vh>clearVisited</vh></v>
<v t="ekr.20060914203123.88"><vh>contract &amp; expand &amp; initExpandedBit</vh></v>
<v t="ekr.20060914203123.89"><vh>initStatus</vh></v>
<v t="ekr.20060914203123.90"><vh>setClonedBit &amp; initClonedBit</vh></v>
<v t="ekr.20060914203123.91"><vh>v.setMarked &amp; initMarkedBit</vh></v>
<v t="ekr.20060914203123.92"><vh>setOrphan</vh></v>
<v t="ekr.20060914203123.93"><vh>setSelected (vnode)</vh></v>
<v t="ekr.20060914203123.94"><vh>t.setVisited</vh></v>
</v>
<v t="ekr.20060914203123.95"><vh>v.computeIcon &amp; setIcon</vh></v>
<v t="ekr.20060914203123.96"><vh>v.initHeadString</vh></v>
<v t="ekr.20060914203123.97"><vh>v.setSelection</vh></v>
<v t="ekr.20060914203123.98"><vh>v.setTnodeText</vh></v>
</v>
<v t="ekr.20060914203123.99"><vh>v.Iterators</vh>
<v t="ekr.20060914203123.100"><vh>self_subtree_iter</vh></v>
<v t="ekr.20060914203123.101"><vh>unique_subtree_iter</vh></v>
</v>
</v>
<v t="ekr.20060914203123.102"><vh>class position</vh>
<v t="ekr.20060914203123.103"><vh>&lt;&lt; about the position class &gt;&gt;</vh></v>
<v t="ekr.20060914203123.104"><vh>&lt;&lt; positions may become invalid when outlines change &gt;&gt;</vh></v>
<v t="ekr.20060914203123.105"><vh> ctor &amp; other special methods...</vh>
<v t="ekr.20060914203123.106"><vh>p.__cmp__</vh></v>
<v t="ekr.20060914203123.107"><vh>p.__getattr__  ON:  must be ON if use_plugins</vh></v>
<v t="ekr.20060914203123.108"><vh>p.__init__</vh></v>
<v t="ekr.20060914203123.109"><vh>p.__nonzero__</vh></v>
<v t="ekr.20060914203123.110"><vh>p.__str__ and p.__repr__</vh></v>
<v t="ekr.20060914203123.111"><vh>p.copy</vh></v>
<v t="ekr.20060914203123.112"><vh>p.dump &amp; p.vnodeListIds</vh></v>
<v t="ekr.20060914203123.113"><vh>p.equal &amp; isEqual</vh></v>
<v t="ekr.20060914203123.114"><vh>p.key (new in 4.4b2)</vh></v>
</v>
<v t="ekr.20060914203123.115"><vh>Getters</vh>
<v t="ekr.20060914203123.116"><vh> vnode proxies</vh>
<v t="ekr.20060914203123.117"><vh>p.Comparisons</vh></v>
<v t="ekr.20060914203123.118"><vh>p.Headline &amp; body strings</vh></v>
<v t="ekr.20060914203123.119"><vh>p.Status bits</vh></v>
<v t="ekr.20060914203123.120"><vh>p.directParents</vh></v>
<v t="ekr.20060914203123.121"><vh>p.childIndex</vh></v>
</v>
<v t="ekr.20060914203123.122"><vh>children</vh>
<v t="ekr.20060914203123.123"><vh>p.hasChildren</vh></v>
<v t="ekr.20060914203123.124"><vh>p.numberOfChildren</vh></v>
</v>
<v t="ekr.20060914203123.125"><vh>p.getX &amp; vnode compatibility traversal routines</vh></v>
<v t="ekr.20060914203123.126"><vh>p.hasX</vh>
<v t="ekr.20060914203123.127"><vh>hasThreadNext (the only complex hasX method)</vh></v>
</v>
<v t="ekr.20060914203123.128"><vh>p.isAncestorOf</vh></v>
<v t="ekr.20060914203123.129"><vh>p.isCloned</vh></v>
<v t="ekr.20060914203123.130"><vh>p.isRoot</vh></v>
<v t="ekr.20060914203123.131"><vh>p.isVisible</vh></v>
<v t="ekr.20060914203123.132"><vh>p.level &amp; simpleLevel</vh></v>
</v>
<v t="ekr.20060914203123.133"><vh>Setters</vh>
<v t="ekr.20060914203123.134"><vh>vnode proxies</vh>
<v t="ekr.20060914203123.135" a="M"><vh> Status bits (position)</vh></v>
<v t="ekr.20060914203123.136"><vh>p.computeIcon &amp; p.setIcon</vh></v>
<v t="ekr.20060914203123.137"><vh>p.setSelection</vh></v>
<v t="ekr.20060914203123.138"><vh>p.setTnodeText</vh></v>
</v>
<v t="ekr.20060914203123.139"><vh>Head &amp; body text (position)</vh>
<v t="ekr.20060914203123.140"><vh>p.setHeadString &amp; p.initHeadString</vh></v>
<v t="ekr.20060914203123.141"><vh>p.scriptSetBodyString</vh></v>
</v>
<v t="ekr.20060914203123.142"><vh>Visited bits</vh>
<v t="ekr.20060914203123.143"><vh>p.clearVisitedInTree</vh></v>
<v t="ekr.20060914203123.144"><vh>p.clearAllVisitedInTree (4.2)</vh></v>
</v>
<v t="ekr.20060914203123.145"><vh>p.Dirty bits</vh>
<v t="ekr.20060914203123.146"><vh>p.clearDirty</vh></v>
<v t="ekr.20060914203123.147"><vh>p.findAllPotentiallyDirtyNodes</vh></v>
<v t="ekr.20060914203123.148" a="M"><vh>p.setAllAncestorAtFileNodesDirty</vh></v>
<v t="ekr.20060914203123.149" a="M"><vh>p.setDirty</vh></v>
<v t="ekr.20060914203123.150"><vh>p.inAtIgnoreRange</vh></v>
</v>
</v>
<v t="ekr.20060914203123.151"><vh>File Conversion</vh>
<v t="ekr.20060914203123.152"><vh>convertTreeToString</vh></v>
<v t="ekr.20060914203123.153"><vh>moreHead</vh></v>
<v t="ekr.20060914203123.154"><vh>moreBody</vh></v>
</v>
<v t="ekr.20060914203123.155"><vh>p.Iterators</vh>
<v t="ekr.20060914203123.156"><vh>p.tnodes_iter &amp; unique_tnodes_iter</vh></v>
<v t="ekr.20060914203123.157"><vh>p.vnodes_iter &amp; unique_vnodes_iter</vh></v>
<v t="ekr.20060914203123.158"><vh>p.subtree_iter</vh>
<v t="ekr.20060914203123.159"><vh>__init__ &amp; __iter__</vh></v>
<v t="ekr.20060914203123.160"><vh>next</vh></v>
</v>
<v t="ekr.20060914203123.161"><vh>p.children_iter</vh>
<v t="ekr.20060914203123.162"><vh>__init__ &amp; __iter__</vh></v>
<v t="ekr.20060914203123.163"><vh>next</vh></v>
</v>
<v t="ekr.20060914203123.164"><vh>p.parents_iter</vh>
<v t="ekr.20060914203123.165"><vh>__init__ &amp; __iter__</vh></v>
<v t="ekr.20060914203123.166"><vh>next</vh></v>
</v>
<v t="ekr.20060914203123.167"><vh>p.siblings_iter</vh>
<v t="ekr.20060914203123.168"><vh>__init__ &amp; __iter__</vh></v>
<v t="ekr.20060914203123.169"><vh>next</vh></v>
</v>
</v>
<v t="ekr.20060914203123.170"><vh>p.Moving, Inserting, Deleting, Cloning, Sorting (position)</vh>
<v t="ekr.20060914203123.171"><vh>p.clone (does not need any args)</vh></v>
<v t="ekr.20060914203123.172"><vh>p.copyTreeAfter, copyTreeTo</vh></v>
<v t="ekr.20060914203123.173" a="M"><vh>p.doDelete</vh></v>
<v t="ekr.20060914203123.174" a="M"><vh>p.insertAfter</vh></v>
<v t="ekr.20060914203123.175"><vh>p.insertAsLastChild</vh></v>
<v t="ekr.20060914203123.176" a="M"><vh>p.insertAsNthChild</vh></v>
<v t="ekr.20060914203123.177"><vh>p.invalidOutline</vh></v>
<v t="ekr.20060914203123.178" a="M"><vh>p.moveAfter</vh></v>
<v t="ekr.20060914203123.179" a="M"><vh>p.moveToLastChildOf</vh></v>
<v t="ekr.20060914203123.180" a="M"><vh>p.moveToNthChildOf</vh></v>
<v t="ekr.20060914203123.181"><vh>p.moveToRoot</vh></v>
<v t="ekr.20060914203123.182"><vh>p.validateOutlineWithParent</vh>
<v t="ekr.20060914203123.183"><vh>&lt;&lt; validate parent ivar &gt;&gt;</vh></v>
<v t="ekr.20060914203123.184"><vh>&lt;&lt; validate childIndex ivar &gt;&gt;</vh></v>
<v t="ekr.20060914203123.185"><vh>&lt;&lt; validate x ivar &gt;&gt;</vh></v>
</v>
</v>
<v t="ekr.20060914203123.186"><vh>p.moveToX</vh>
<v t="ekr.20060914203123.187"><vh>p.moveToBack</vh></v>
<v t="ekr.20060914203123.188"><vh>p.moveToFirstChild (pushes stack for cloned nodes)</vh></v>
<v t="ekr.20060914203123.189"><vh>p.moveToLastChild (pushes stack for cloned nodes)</vh></v>
<v t="ekr.20060914203123.190"><vh>p.moveToLastNode (Big improvement for 4.2)</vh></v>
<v t="ekr.20060914203123.191"><vh>p.moveToNext</vh></v>
<v t="ekr.20060914203123.192"><vh>p.moveToNodeAfterTree</vh></v>
<v t="ekr.20060914203123.193"><vh>p.moveToNthChild (pushes stack for cloned nodes)</vh></v>
<v t="ekr.20060914203123.194"><vh>p.moveToParent (pops stack when multiple parents)</vh></v>
<v t="ekr.20060914203123.195"><vh>p.moveToThreadBack</vh></v>
<v t="ekr.20060914203123.196"><vh>p.moveToThreadNext</vh></v>
<v t="ekr.20060914203123.197"><vh>p.moveToVisBack</vh></v>
<v t="ekr.20060914203123.198"><vh>p.moveToVisNext</vh></v>
</v>
<v t="ekr.20060914203123.199"><vh>p.utils...</vh>
<v t="ekr.20060914203123.200"><vh>p.vParentWithStack</vh>
<v t="ekr.20060914203123.201"><vh>&lt;&lt; about the vParentWithStack utility method &gt;&gt;</vh></v>
</v>
<v t="ekr.20060914203123.202"><vh>p.restoreLinksInTree</vh></v>
<v t="ekr.20060914203123.203"><vh>p.deleteLinksInTree &amp; allies</vh>
<v t="ekr.20060914203123.204"><vh>p.deleteLinksInSubtree</vh></v>
<v t="ekr.20060914203123.205"><vh>p.adjustParentLinksInSubtree</vh></v>
</v>
</v>
<v t="ekr.20060914203123.206"><vh>p.Link/Unlink methods</vh>
<v t="ekr.20060914203123.207"><vh>p.linkAfter</vh></v>
<v t="ekr.20060914203123.208"><vh>p.linkAsNthChild</vh></v>
<v t="ekr.20060914203123.209" a="M"><vh>p.linkAsRoot</vh></v>
<v t="ekr.20060914203123.210" a="M"><vh>p.unlink</vh></v>
</v>
</v>
</v>
<v t="ekr.20060904103412" a="E"><vh>@thin leoOPML.py</vh></v>
<v t="ekr.20060904103721"><vh>readFile</vh></v>
<v t="ekr.20060914163456"><vh>createVnodes &amp; helpers</vh>
<v t="ekr.20060914171659.2"><vh>createChildren</vh></v>
<v t="ekr.20060914171659"><vh>createVnodeTree</vh></v>
<v t="ekr.20060914171659.1"><vh>createVnode</vh></v>
<v t="ekr.20060914174806"><vh>linkParentAndChildren</vh></v>
<v t="ekr.20060914165257"><vh>linkSiblings</vh></v>
</v>
</vnodes>
<tnodes>
<t tx="ekr.20060904103721">def readFile (self,event=None,fileName=None):
    
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
        c2.redraw()</t>
<t tx="ekr.20060904141220.35">def doContent (self,elementName,content):
    
    name = str(elementName.lower())
    g.trace(name)</t>
<t tx="ekr.20060904141220.36">def endElement (self,elementName):

    name = elementName.lower()
    
    if name == 'props':
        self.inProps = True
    if name == 'rules':
        self.inRules = False
        ruleset = rulesetClass(self.rulesetAttributes,self.keywords,self.rulesetProperties,self.rules)
        self.rulesets.append(ruleset)
        #g.trace('rules...\n',g.listToString(self.rules))
        #g.trace('ruleset attributes...\n',g.dictToString(self.rulesetAttributes))
    if name == 'property':
        bunch = self.presentProperty
        if bunch:
            if self.inRules:
                self.rulesetProperties.append(bunch)
            else:
                self.modeProperties.append(bunch)
        else:
            self.error('end %s not matched by start %s' % (name,name))
        self.presentProperty = None
    if name in self.ruleElements:
        if self.inRule(name):
            self.rules.append(self.rule)
            self.rule = None
        else:
            self.error('end %s not matched by start %s' % (name,name))</t>
<t tx="ekr.20060904141220.38">def getAttributes (self):
    return self.attributes
    
def getAttributesForRuleset (self,ruleset):
    bunch = ruleset
    return bunch.attributes

def getFileName (self):
    return self.fileName

def getKeywords (self,n,ruleset):
    bunch = ruleset
    keywords = bunch.keywords
    if keywords:
        return keywords.get('keyword%d'%(n),[])
    return []

def getLanguage (self):
    path,name = g.os_path_split(self.fileName)
    language,ext = g.os_path_splitext(name)
    return language

def getPropertiesForMode (self):
    return self.props
    
def getPropertiesForRuleset (self,name=''):
    bunch = self.getRuleset(name)
    if bunch:
        return bunch.properties
    else:
        return []
    
def getRuleset(self,name=''):
    if not name:
        return self.rulesets[0] # Return the main ruleset.
    for ruleset in self.rulesets:
        if ruleset.name.lower()==name.lower():
            return ruleset
    else: return None

def getRulesets(self):
    return self.rulesets
    
def getRulesForRuleset (self,name=''):
    bunch = self.getRuleset(name)
    if bunch:
        return bunch.rules
    else:
        return []</t>
<t tx="ekr.20060904141220.40">def startElement (self,elementName):
    
    name = elementName.lower()
    
    g.trace(name)
    
    return ####

    
    
    if name == 'props':
        self.inProps = True
    if name == 'rules':
        self.inRules = True
        self.attributes=[]
        self.keywords=[]
        self.rulesetProperties=[]
        self.rules=[]
    if name == 'property':
        if self.inProps:
            self.presentProperty = g.bunch(name=name,attributes={})
        else:
            self.error('property not in props element')
    if name in self.ruleElements:
        if self.inRules:
            self.rule = ruleClass(name=name)
            if name == 'keywords':
                self.keywords = self.rule
        else:
            self.error('%s not in rules element' % name)</t>
<t tx="ekr.20060913211939"></t>
<t tx="ekr.20060913211939.1"></t>
<t tx="ekr.20060914163456">def createVnodes (self, dummyRoot):
    
    '''**Important**: this method and its helpers are low-level code.
    Modify this with extreme care.'''
    
    self.firstChildren = {}

    children = self.createChildren(dummyRoot,parent_v = None)
    firstChild = children and children[0]
    
    g.trace(firstChild)
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
    self.createChildren(node,v)
    
    # children = self.createChildren(node,v)
    # firstChild = children and children[0]
    # self.linkParentAndChildren(v,children)

    return v</t>
<t tx="ekr.20060914171659.1">def createVnode (self,node,parent_v):
    
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
    
    return v</t>
<t tx="ekr.20060914171659.2"># node is a nodeClass object, parent_v is a vnode.

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
        
        </t>
<t tx="ekr.20060914174806">def linkParentAndChildren (self, parent_v, children):
    
    # if children: g.trace(parent_v,len(children))
    
    firstChild_v = children and children[0] or None

    parent_v.t._firstChild = firstChild_v
    
    for child in children:
        child._parent = parent_v

    # if firstChild_v:
        # firstChild_v._parent = parent_v
    
    v = parent_v
    if v not in v.t.vnodeList:
        v.t.vnodeList.append(v)</t>
<t tx="ekr.20060914203123"></t>
<t tx="ekr.20060914203123.1"># These remain in 4.2: the file read logic calls these before creating positions.
</t>
<t tx="ekr.20060914203123.2">def detach (self):
    
    '''Return a standalone copy of a vnode,
    detached from all other nodes and with a new tnode.'''
    
    v = self
    
    # Create a completely separate tnode.
    t2 = tnode(
        bodyString=v.bodyString(),
        headString=v.headString())
    
    return vnode(t2)</t>
<t tx="ekr.20060914203123.3">def insertAfter (self,t=None):

    """Inserts a new vnode after self"""

    if not t:
        t = tnode(headString="NewHeadline")

    v = vnode(t)
    v.linkAfter(self)

    return v
</t>
<t tx="ekr.20060914203123.4">def insertAsNthChild (self,n,t=None):

    """Inserts a new node as the the nth child of the receiver.
    The receiver must have at least n-1 children"""

    if not t:
        t = tnode(headString="NewHeadline")

    v = vnode(t)
    v.linkAsNthChild(self,n)

    return v
</t>
<t tx="ekr.20060914203123.5">def linkAsNthChild (self,pv,n):

    """Links self as the n'th child of vnode pv"""

    v = self
    # g.trace(v,pv,n)
    v._parent = pv
    if n == 0:
        v._back = None
        v._next = pv.t._firstChild
        if pv.t._firstChild:
            pv.t._firstChild._back = v
        pv.t._firstChild = v
    else:
        prev = pv.nthChild(n-1) # zero based
        assert(prev)
        v._back = prev
        v._next = prev._next
        prev._next = v
        if v._next:
            v._next._back = v
</t>
<t tx="ekr.20060914203123.6">def linkAsRoot (self,oldRoot):
    
    """Link a vnode as the root node and set the root _position_."""

    v = self

    # Clear all links except the child link.
    v._parent = None
    v._back = None
    v._next = oldRoot
    
    # Add v to it's tnode's vnodeList. Bug fix: 5/02/04.
    if v not in v.t.vnodeList:
        v.t.vnodeList.append(v)
        v.t._p_changed = 1

    # Link in the rest of the tree only when oldRoot != None.
    # Otherwise, we are calling this routine from init code and
    # we want to start with a pristine tree.
    if oldRoot: oldRoot._back = v</t>
<t tx="ekr.20060914203123.7">def moveToRoot (self,oldRoot=None):

    '''Moves a vnode to the root position.
    
    Important: oldRoot must the previous root vnode if it exists.'''

    v = self

    v.unlink()
    v.linkAsRoot(oldRoot)
    
    return v</t>
<t tx="ekr.20060914203123.8">def linkAfter (self,v):

    """Link self after v."""
    
    self._parent = v._parent
    self._back = v
    self._next = v._next
    v._next = self
    if self._next:
        self._next._back = self
</t>
<t tx="ekr.20060914203123.9">def unlink (self):

    """Unlinks a vnode from the tree."""

    v = self

    # g.trace(v._parent," child: ",v.t._firstChild," back: ", v._back, " next: ", v._next)

    # Clear the links in other nodes.
    if v._back:
        v._back._next = v._next
    if v._next:
        v._next._back = v._back

    if v._parent and v == v._parent.t._firstChild:
        v._parent.t._firstChild = v._next

    # Clear the links in this node.
    v._parent = v._next = v._back = None</t>
<t tx="ekr.20060914203123.10">if use_zodb and ZODB:
    class baseTnode (ZODB.Persistence.Persistent):
        pass
else:
    class baseTnode (object):
        pass
    
class tnode (baseTnode):
    """A class that implements tnodes."""
    &lt;&lt; tnode constants &gt;&gt;
    @others</t>
<t tx="ekr.20060914203123.11">dirtyBit    = 0x01
richTextBit = 0x02 # Determines whether we use &lt;bt&gt; or &lt;btr&gt; tags.
visitedBit  = 0x04
writeBit    = 0x08 # Set: write the tnode.
</t>
<t tx="ekr.20060914203123.12"># All params have defaults, so t = tnode() is valid.

def __init__ (self,bodyString=None,headString=None):

    # To support ZODB the code must set t._p_changed = 1 whenever
    # t.vnodeList, t.unknownAttributes or any mutable tnode object changes.

    self.cloneIndex = 0 # For Pre-3.12 files.  Zero for @file nodes
    self.fileIndex = None # The immutable file index for this tnode.
    self.insertSpot = None # Location of previous insert point.
    self.scrollBarSpot = None # Previous value of scrollbar position.
    self.selectionLength = 0 # The length of the selected body text.
    self.selectionStart = 0 # The start of the selected body text.
    self.statusBits = 0 # status bits

    # Convert everything to unicode...
    self.headString = g.toUnicode(headString,g.app.tkEncoding)
    self.bodyString = g.toUnicode(bodyString,g.app.tkEncoding)
    
    self.vnodeList = [] # List of all vnodes pointing to this tnode.
    self._firstChild = None</t>
<t tx="ekr.20060914203123.13">def __repr__ (self):
    
    return "&lt;tnode %d&gt;" % (id(self))
        
__str__ = __repr__
</t>
<t tx="ekr.20060914203123.14">if use_zodb and ZODB:
    def __hash__(self):
        # The only required property is that objects
        # which compare equal have the same hash value.
        return sum([ord(ch) for ch in g.app.nodeIndices.toString(self.fileIndex)])</t>
<t tx="ekr.20060914203123.15"></t>
<t tx="ekr.20060914203123.16">def getBody (self):

    return self.bodyString
</t>
<t tx="ekr.20060914203123.17">def hasBody (self):
    
    '''Return True if this tnode contains body text.'''

    s = self.bodyString

    return s and len(s) &gt; 0
</t>
<t tx="ekr.20060914203123.18"></t>
<t tx="ekr.20060914203123.19">def isDirty (self):

    return (self.statusBits &amp; self.dirtyBit) != 0
</t>
<t tx="ekr.20060914203123.20">def isRichTextBit (self):

    return (self.statusBits &amp; self.richTextBit) != 0
</t>
<t tx="ekr.20060914203123.21">def isVisited (self):

    return (self.statusBits &amp; self.visitedBit) != 0
</t>
<t tx="ekr.20060914203123.22">def isWriteBit (self):

    return (self.statusBits &amp; self.writeBit) != 0
</t>
<t tx="ekr.20060914203123.23"></t>
<t tx="ekr.20060914203123.24"></t>
<t tx="ekr.20060914203123.25"># This sets the text in the tnode from the given string.

def setTnodeText (self,s,encoding="utf-8"):
    
    """Set the body text of a tnode to the given string."""
    
    s = g.toUnicode(s,encoding,reportErrors=True)
    
    if 0: # DANGEROUS:  This automatically converts everything when reading files.
    
        # New in Leo 4.4.2: self.c does not exist!
        # This must be done in the Commands class.
        option = self.c.config.trailing_body_newlines
        
        if option == "one":
            s = s.rstrip() + '\n'
        elif option == "zero":
            s = s.rstrip()

    self.bodyString = s
    
    # g.trace(repr(s))
</t>
<t tx="ekr.20060914203123.26">def setSelection (self,start,length):

    self.selectionStart = start
    self.selectionLength = length
</t>
<t tx="ekr.20060914203123.27"></t>
<t tx="ekr.20060914203123.28">def clearDirty (self):

    self.statusBits &amp;= ~ self.dirtyBit
</t>
<t tx="ekr.20060914203123.29">def clearRichTextBit (self):

    self.statusBits &amp;= ~ self.richTextBit
</t>
<t tx="ekr.20060914203123.30">def clearVisited (self):

    self.statusBits &amp;= ~ self.visitedBit
</t>
<t tx="ekr.20060914203123.31">def clearWriteBit (self):

    self.statusBits &amp;= ~ self.writeBit
</t>
<t tx="ekr.20060914203123.32">def setDirty (self):

    self.statusBits |= self.dirtyBit
</t>
<t tx="ekr.20060914203123.33">def setRichTextBit (self):

    self.statusBits |= self.richTextBit
</t>
<t tx="ekr.20060914203123.34">def setVisited (self):

    self.statusBits |= self.visitedBit
</t>
<t tx="ekr.20060914203123.35">def setWriteBit (self):

    self.statusBits |= self.writeBit
</t>
<t tx="ekr.20060914203123.36">def setCloneIndex (self, index):

    self.cloneIndex = index
</t>
<t tx="ekr.20060914203123.37">def setFileIndex (self, index):

    self.fileIndex = index
</t>
<t tx="ekr.20060914203123.38">def setHeadString (self,s,encoding="utf-8"):
    
    t = self

    s = g.toUnicode(s,encoding,reportErrors=True)
    t.headString = s
</t>
<t tx="ekr.20060914203123.39">if use_zodb and ZODB:
    class baseVnode (ZODB.Persistence.Persistent):
        pass
else:
    class baseVnode (object):
       pass
    
class vnode (baseVnode):
    &lt;&lt; vnode constants &gt;&gt;
    @others</t>
<t tx="ekr.20060914203123.40"># Define the meaning of status bits in new vnodes.

# Archived...
clonedBit   = 0x01 # True: vnode has clone mark.

# not used = 0x02
expandedBit = 0x04 # True: vnode is expanded.
markedBit   = 0x08 # True: vnode is marked
orphanBit   = 0x10 # True: vnode saved in .leo file, not derived file.
selectedBit = 0x20 # True: vnode is current vnode.
topBit      = 0x40 # True: vnode was top vnode when saved.

# Not archived...
dirtyBit    = 0x060
richTextBit = 0x080 # Determines whether we use &lt;bt&gt; or &lt;btr&gt; tags.
visitedBit  = 0x100
</t>
<t tx="ekr.20060914203123.41"></t>
<t tx="ekr.20060914203123.42">if 0: # not used
    def __cmp__(self,other):
        
        g.trace(self,other)
        return not (self is other) # Must return 0, 1 or -1
</t>
<t tx="ekr.20060914203123.43">def __init__ (self,t):

    assert(t)
    
    # To support ZODB the code must set v._p_changed = 1 whenever
    # v.unknownAttributes or any mutable vnode object changes.

    self.t = t # The tnode.
    self.statusBits = 0 # status bits
    
    # Structure links.
    self._parent = self._next = self._back = None</t>
<t tx="ekr.20060914203123.44">def __repr__ (self):
    
    if self.t:
        return "&lt;vnode %d:'%s'&gt;" % (id(self),self.cleanHeadString())
    else:
        return "&lt;vnode %d:NULL tnode&gt;" % (id(self))
        
__str__ = __repr__
</t>
<t tx="ekr.20060914203123.45">def dumpLink (self,link):
    return g.choose(link,link,"&lt;none&gt;")

def dump (self,label=""):
    
    v = self

    if label:
        print '-'*10,label,v
    else:
        print "self    ",v.dumpLink(v)
        print "len(vnodeList)",len(v.t.vnodeList)

    print "_back   ",v.dumpLink(v._back)
    print "_next   ",v.dumpLink(v._next)
    print "_parent ",v.dumpLink(v._parent)
    print "t._child",v.dumpLink(v.t._firstChild)
    
    if 1:
        print "t",v.dumpLink(v.t)
        print "vnodeList"
        for v in v.t.vnodeList:
            print v
</t>
<t tx="ekr.20060914203123.46">if use_zodb and ZODB:
    def __hash__(self):
        # The only required property is that objects
        # which compare equal have the same hash value.
        return self.t.__hash__()</t>
<t tx="ekr.20060914203123.47"></t>
<t tx="ekr.20060914203123.48">def findAtFileName (self,names):
    
    """Return the name following one of the names in nameList.
    Return an empty string."""

    h = self.headString()
    
    if not g.match(h,0,'@'):
        return ""
    
    i = g.skip_id(h,1,'-')
    word = h[:i]
    if word in names and g.match_word(h,0,word):
        name = h[i:].strip()
        # g.trace(word,name)
        return name
    else:
        return ""
</t>
<t tx="ekr.20060914203123.49">def anyAtFileNodeName (self):
    
    """Return the file name following an @file node or an empty string."""

    names = (
        "@file",
        "@thin",   "@file-thin",   "@thinfile",
        "@asis",   "@file-asis",   "@silentfile",
        "@noref",  "@file-noref",  "@rawfile",
        "@nosent", "@file-nosent", "@nosentinelsfile")

    return self.findAtFileName(names)
</t>
<t tx="ekr.20060914203123.50"># These return the filename following @xxx, in v.headString.
# Return the the empty string if v is not an @xxx node.

def atFileNodeName (self):
    names = ("@file"),
    return self.findAtFileName(names)

def atNoSentinelsFileNodeName (self):
    names = ("@nosent", "@file-nosent", "@nosentinelsfile")
    return self.findAtFileName(names)

def atRawFileNodeName (self):
    names = ("@noref", "@file-noref", "@rawfile")
    return self.findAtFileName(names)
    
def atSilentFileNodeName (self):
    names = ("@asis", "@file-asis", "@silentfile")
    return self.findAtFileName(names)
    
def atThinFileNodeName (self):
    names = ("@thin", "@file-thin", "@thinfile")
    return self.findAtFileName(names)
    
# New names, less confusing
atNoSentFileNodeName  = atNoSentinelsFileNodeName
atNorefFileNodeName   = atRawFileNodeName
atAsisFileNodeName     = atSilentFileNodeName
</t>
<t tx="ekr.20060914203123.51">def isAtAllNode (self):

    """Returns True if the receiver contains @others in its body at the start of a line."""

    flag, i = g.is_special(self.t.bodyString,0,"@all")
    return flag
</t>
<t tx="ekr.20060914203123.52">def isAnyAtFileNode (self):
    
    """Return True if v is any kind of @file or related node."""
    
    # This routine should be as fast as possible.
    # It is called once for every vnode when writing a file.

    h = self.headString()
    return h and h[0] == '@' and self.anyAtFileNodeName()
</t>
<t tx="ekr.20060914203123.53">def isAtFileNode (self):
    return g.choose(self.atFileNodeName(),True,False)
    
def isAtNoSentinelsFileNode (self):
    return g.choose(self.atNoSentinelsFileNodeName(),True,False)

def isAtRawFileNode (self): # @file-noref
    return g.choose(self.atRawFileNodeName(),True,False)

def isAtSilentFileNode (self): # @file-asis
    return g.choose(self.atSilentFileNodeName(),True,False)

def isAtThinFileNode (self):
    return g.choose(self.atThinFileNodeName(),True,False)
    
# New names, less confusing:
isAtNoSentFileNode = isAtNoSentinelsFileNode
isAtNorefFileNode  = isAtRawFileNode
isAtAsisFileNode   = isAtSilentFileNode
</t>
<t tx="ekr.20060914203123.54">def isAtIgnoreNode (self):

    """Returns True if the receiver contains @ignore in its body at the start of a line."""

    flag, i = g.is_special(self.t.bodyString, 0, "@ignore")
    return flag
</t>
<t tx="ekr.20060914203123.55">def isAtOthersNode (self):

    """Returns True if the receiver contains @others in its body at the start of a line."""

    flag, i = g.is_special(self.t.bodyString,0,"@others")
    return flag
</t>
<t tx="ekr.20060914203123.56">def matchHeadline (self,pattern):

    """Returns True if the headline matches the pattern ignoring whitespace and case.
    
    The headline may contain characters following the successfully matched pattern."""
    
    v = self
    
    h = g.toUnicode(v.headString(),'utf-8')
    h = h.lower().replace(' ','').replace('\t','')

    pattern = g.toUnicode(pattern,'utf-8')
    pattern = pattern.lower().replace(' ','').replace('\t','')
    
    return h.startswith(pattern)
</t>
<t tx="ekr.20060914203123.57"></t>
<t tx="ekr.20060914203123.58"></t>
<t tx="ekr.20060914203123.59"># Compatibility routine for scripts

def back (self):

    return self._back
</t>
<t tx="ekr.20060914203123.60"># Compatibility routine for scripts
# Used by p.findAllPotentiallyDirtyNodes.

def next (self):

    return self._next
</t>
<t tx="ekr.20060914203123.61"></t>
<t tx="ekr.20060914203123.62">def childIndex(self):
    
    v = self

    if not v._back:
        return 0

    n = 0 ; v = v._back
    while v:
        n += 1
        v = v._back
    return n
</t>
<t tx="ekr.20060914203123.63">def firstChild (self):
    
    return self.t._firstChild
</t>
<t tx="ekr.20060914203123.64">def hasChildren (self):
    
    v = self
    return v.firstChild()

hasFirstChild = hasChildren
</t>
<t tx="ekr.20060914203123.65">def lastChild (self):

    child = self.firstChild()
    while child and child.next():
        child = child.next()
    return child
</t>
<t tx="ekr.20060914203123.66"># childIndex and nthChild are zero-based.

def nthChild (self, n):

    child = self.firstChild()
    if not child: return None
    while n &gt; 0 and child:
        n -= 1
        child = child.next()
    return child
</t>
<t tx="ekr.20060914203123.67">def numberOfChildren (self):

    n = 0
    child = self.firstChild()
    while child:
        n += 1
        child = child.next()
    return n
</t>
<t tx="ekr.20060914203123.68"></t>
<t tx="ekr.20060914203123.69">def isCloned (self):
    
    return len(self.t.vnodeList) &gt; 1
</t>
<t tx="ekr.20060914203123.70">def isDirty (self):

    return self.t.isDirty()
</t>
<t tx="ekr.20060914203123.71">def isExpanded (self):

    return ( self.statusBits &amp; self.expandedBit ) != 0
</t>
<t tx="ekr.20060914203123.72">def isMarked (self):

    return ( self.statusBits &amp; vnode.markedBit ) != 0
</t>
<t tx="ekr.20060914203123.73">def isOrphan (self):

    return ( self.statusBits &amp; vnode.orphanBit ) != 0
</t>
<t tx="ekr.20060914203123.74">def isSelected (self):

    return ( self.statusBits &amp; vnode.selectedBit ) != 0
</t>
<t tx="ekr.20060914203123.75">def isTopBitSet (self):

    return ( self.statusBits &amp; self.topBit ) != 0
</t>
<t tx="ekr.20060914203123.76">def isVisited (self):

    return ( self.statusBits &amp; vnode.visitedBit ) != 0
</t>
<t tx="ekr.20060914203123.77">def status (self):

    return self.statusBits
</t>
<t tx="ekr.20060914203123.78"># Compatibility routine for scripts

def bodyString (self):

    # This message should never be printed and we want to avoid crashing here!
    if not g.isUnicode(self.t.bodyString):
        s = "v.bodyString: Leo internal error: not unicode:" + repr(self.t.bodyString)
        g.es_print(s,color="red")

    # Make _sure_ we return a unicode string.
    return g.toUnicode(self.t.bodyString,g.app.tkEncoding)
</t>
<t tx="ekr.20060914203123.79">def headString (self):
    
    """Return the headline string."""
    
    # This message should never be printed and we want to avoid crashing here!
    if not g.isUnicode(self.t.headString):
        s = "Leo internal error: not unicode:" + repr(self.t.headString)
        g.es_print(s,color="red")
        
    # Make _sure_ we return a unicode string.
    return g.toUnicode(self.t.headString,g.app.tkEncoding)

def cleanHeadString (self):
    
    s = self.headString()
    return g.toEncodedString(s,"ascii") # Replaces non-ascii characters by '?'
</t>
<t tx="ekr.20060914203123.80">def directParents (self):
    
    """(New in 4.2) Return a list of all direct parent vnodes of a vnode.
    
    This is NOT the same as the list of ancestors of the vnode."""
    
    v = self
    
    if v._parent:
        return v._parent.t.vnodeList
    else:
        return []
</t>
<t tx="ekr.20060914203123.81"></t>
<t tx="ekr.20060914203123.82"></t>
<t tx="ekr.20060914203123.83">def clearClonedBit (self):

    self.statusBits &amp;= ~ self.clonedBit
</t>
<t tx="ekr.20060914203123.84">def clearDirty (self):

    v = self
    v.t.clearDirty()</t>
<t tx="ekr.20060914203123.85">def clearMarked (self):

    self.statusBits &amp;= ~ self.markedBit
</t>
<t tx="ekr.20060914203123.86">def clearOrphan (self):

    self.statusBits &amp;= ~ self.orphanBit
</t>
<t tx="ekr.20060914203123.87">def clearVisited (self):

    self.statusBits &amp;= ~ self.visitedBit
</t>
<t tx="ekr.20060914203123.88">def contract(self):

    self.statusBits &amp;= ~ self.expandedBit
    
    # g.trace(self.statusBits)

def expand(self):

    self.statusBits |= self.expandedBit
    
    # g.trace(self.statusBits)

def initExpandedBit (self):

    self.statusBits |= self.expandedBit
</t>
<t tx="ekr.20060914203123.89">def initStatus (self, status):

    self.statusBits = status
</t>
<t tx="ekr.20060914203123.90">def setClonedBit (self):

    self.statusBits |= self.clonedBit

def initClonedBit (self, val):

    if val:
        self.statusBits |= self.clonedBit
    else:
        self.statusBits &amp;= ~ self.clonedBit
</t>
<t tx="ekr.20060914203123.91">def setMarked (self):

    self.statusBits |= self.markedBit

def initMarkedBit (self):

    self.statusBits |= self.markedBit
</t>
<t tx="ekr.20060914203123.92">def setOrphan (self):

    self.statusBits |= self.orphanBit
</t>
<t tx="ekr.20060914203123.93"># This only sets the selected bit.

def setSelected (self):

    self.statusBits |= self.selectedBit
</t>
<t tx="ekr.20060914203123.94"># Compatibility routine for scripts

def setVisited (self):

    self.statusBits |= self.visitedBit
</t>
<t tx="ekr.20060914203123.95">def computeIcon (self):

    val = 0 ; v = self
    if v.t.hasBody(): val += 1
    if v.isMarked(): val += 2
    if v.isCloned(): val += 4
    if v.isDirty(): val += 8
    return val
    
def setIcon (self):

    pass # Compatibility routine for old scripts
</t>
<t tx="ekr.20060914203123.96">def initHeadString (self,s,encoding="utf-8"):
    
    v = self
    s = g.toUnicode(s,encoding,reportErrors=True)
    v.t.headString = s
    
    # g.trace(g.callers(5))
</t>
<t tx="ekr.20060914203123.97">def setSelection (self, start, length):

    self.t.setSelection ( start, length )
</t>
<t tx="ekr.20060914203123.98">def setTnodeText (self,s,encoding="utf-8"):
    
    return self.t.setTnodeText(s,encoding)
</t>
<t tx="ekr.20060914203123.99"></t>
<t tx="ekr.20060914203123.100">def subtree_iter(self):

    """Return all nodes of self's tree in outline order."""
    
    v = self

    if v:
        yield v
        child = v.t._firstChild
        while child:
            for v1 in child.subtree_iter():
                yield v1
            child = child.next()
            
self_and_subtree_iter = subtree_iter
</t>
<t tx="ekr.20060914203123.101">def unique_subtree_iter(self,marks=None):

    """Return all vnodes in self's tree, discarding duplicates """
    
    v = self

    if marks == None: marks = {}

    if v and v not in marks:
        marks[v] = v
        yield v
        if v.t._firstChild:
            for v1 in v.t._firstChild.unique_subtree_iter(marks):
                yield v1
        v = v._next
        while v:
            for v in v.unique_subtree_iter(marks):
                yield v
            v = v._next
            
self_and_unique_subtree_iter = unique_subtree_iter
</t>
<t tx="ekr.20060914203123.102">&lt;&lt; about the position class &gt;&gt;
&lt;&lt; positions may become invalid when outlines change &gt;&gt;

# Positions should *never* be saved by the ZOBD.

class basePosition (object):
    @others

class position (basePosition):
    pass</t>
<t tx="ekr.20060914203123.103">@killcolor

@ This class provides tree traversal methods that operate on positions, not vnodes.  Positions encapsulate the notion of present position within a traversal.

Positions consist of a vnode and a stack of parent nodes used to determine the next parent when a vnode has mutliple parents.

Calling, e.g., p.moveToThreadNext() results in p being an invalid position.  That is, p represents the position following the last node of the outline.  The test "if p" is the _only_ correct way to test whether a position p is valid.  In particular, tests like "if p is None" or "if p is not None" will not work properly.

The only changes to vnodes and tnodes needed to implement shared tnodes are:

- The firstChild field becomes part of tnodes.
- t.vnodes contains a list of all vnodes sharing the tnode.

The advantages of using shared tnodes:

- Leo no longer needs to create or destroy "dependent" trees when changing descendents of cloned trees.
- There is no need for join links and no such things as joined nodes.

These advantages are extremely important: Leo is now scalable to very large outlines.

An important complication is the need to avoid creating temporary positions while traversing trees:
- Several routines use p.vParentWithStack to avoid having to call tempPosition.moveToParent().
  These include p.level, p.isVisible and p.hasThreadNext.
- p.moveToLastNode and p.moveToThreadBack use new algorithms that don't use temporary data.
- Several lookahead routines compute whether a position exists without computing the actual position.
</t>
<t tx="ekr.20060914203123.104">@killcolor

@ If a vnode has only one parent, v._parent is that parent. Otherwise,
v.t.vnodeList is the list of vnodes v2 such that v2._firstChild == v. Alas, this
means that positions can become invalid when vnodeList's change!

There is no use trying to solve the problem in p.moveToParent or
p.vParentWithStack: the invalidated positions simply don't have the stack
entries needed to compute parent fields properly. In short, changing t.vnodeList
may invalidate existing positions!
</t>
<t tx="ekr.20060914203123.105"></t>
<t tx="ekr.20060914203123.106">def __cmp__(self,p2):

    """Return 0 if two postions are equivalent."""

    # Use p.equal if speed is crucial.
    p1 = self
    
    # g.trace(p1.headString(),p2 and p2.headString())

    if p2 is None: # Allow tests like "p == None"
        if p1.v: return 1 # not equal
        else:    return 0 # equal

    # Check entire stack quickly.
    # The stack contains vnodes, so this is not a recursive call.
    if p1.v != p2.v or p1.stack != p2.stack:
        return 1 # notEqual

    # This is slow: do this last!
    if p1.childIndex() != p2.childIndex():
        # Disambiguate clones having the same parents.
        return 1 # notEqual

    return 0 # equal
</t>
<t tx="ekr.20060914203123.107">if 1: # Good for compatibility, bad for finding conversion problems.

    def __getattr__ (self,attr):
        
        """Convert references to p.t into references to p.v.t.
        
        N.B. This automatically keeps p.t in synch with p.v.t."""

        if attr=="t":
            return self.v.t
        else:
            # New in 4.3: _silently_ raise the attribute error.
            # This allows plugin code to use hasattr(p,attr) !
            if 0:
                print "unknown position attribute:",attr
                import traceback ; traceback.print_stack()
            raise AttributeError,attr</t>
<t tx="ekr.20060914203123.108"># New in Leo 4.4.2: make stack default to None.

def __init__ (self,v,stack=None,trace=True):

    """Create a new position."""
    
    __pychecker__ = '--no-argsused' # trace not used.

    # To support ZODB the code must set vort._p_changed = 1 whenever
    # t.vnodeList (or any mutable tnode or vnode object) changes.

    self.v = v
    # assert(v is None or v.t)
    
    if stack:
        self.stack = stack[:] # Creating a copy here is safest and best.
    else:
        self.stack = []
    
    g.app.positions += 1
    
    # if g.app.tracePositions and trace: g.trace(g.callers())
    
    # Note: __getattr__ implements p.t.</t>
<t tx="ekr.20060914203123.109">@
Tests such as 'if p' or 'if not p' are the _only_ correct ways to test whether a position p is valid.
In particular, tests like 'if p is None' or 'if p is not None' will not work properly.
@c

def __nonzero__ ( self):
    
    """Return True if a position is valid."""
    
    # if g.app.trace: "__nonzero__",self.v

    return self.v is not None
</t>
<t tx="ekr.20060914203123.110">def __str__ (self):
    
    p = self
    
    if p.v:
        return "&lt;pos %d lvl: %d [%d] %s&gt;" % (id(p),p.level(),len(p.stack),p.cleanHeadString())
    else:
        return "&lt;pos %d        [%d] None&gt;" % (id(p),len(p.stack))
        
__repr__ = __str__
</t>
<t tx="ekr.20060914203123.111"># Using this routine can generate huge numbers of temporary positions during a tree traversal.

def copy (self):
    
    """"Return an independent copy of a position."""
    
    # if g.app.tracePositions: g.trace(g.callers())

    return position(self.v,self.stack,trace=False)
</t>
<t tx="ekr.20060914203123.112">def dumpLink (self,link):

    return g.choose(link,link,"&lt;none&gt;")

def dump (self,label=""):
    
    p = self
    print '-'*10,label,p
    if p.v:
        p.v.dump() # Don't print a label
        
def vnodeListIds (self):
    
    p = self
    return [id(v) for v in p.v.t.vnodeList]
</t>
<t tx="ekr.20060914203123.113">def equal(self,p2):

    """Return True if two postions are equivalent.
    
    Use this method when the speed comparisons is crucial
    
    N.B. Unlike __cmp__, p2 must not be None.
    """

    p1 = self

    # Check entire stack quickly.
    # The stack contains vnodes, so this does not call p.__cmp__.
    return (
        p1.v == p2.v and
        p1.stack == p2.stack and
        p1.childIndex() == p2.childIndex())
        
isEqual = equal
</t>
<t tx="ekr.20060914203123.114">def key (self):
    
    p = self

    return '%s:%d.%s' % (
        id(p.v),
        p.childIndex(),
        ','.join([str(id(v)) for v in p.stack])
    )
</t>
<t tx="ekr.20060914203123.115"></t>
<t tx="ekr.20060914203123.116"></t>
<t tx="ekr.20060914203123.117">def anyAtFileNodeName         (self): return self.v.anyAtFileNodeName()
def atFileNodeName            (self): return self.v.atFileNodeName()
def atNoSentinelsFileNodeName (self): return self.v.atNoSentinelsFileNodeName()
def atRawFileNodeName         (self): return self.v.atRawFileNodeName()
def atSilentFileNodeName      (self): return self.v.atSilentFileNodeName()
def atThinFileNodeName        (self): return self.v.atThinFileNodeName()

# New names, less confusing
atNoSentFileNodeName  = atNoSentinelsFileNodeName
atNorefFileNodeName   = atRawFileNodeName
atAsisFileNodeName    = atSilentFileNodeName

def isAnyAtFileNode         (self): return self.v.isAnyAtFileNode()
def isAtAllNode             (self): return self.v.isAtAllNode()
def isAtFileNode            (self): return self.v.isAtFileNode()
def isAtIgnoreNode          (self): return self.v.isAtIgnoreNode()
def isAtNoSentinelsFileNode (self): return self.v.isAtNoSentinelsFileNode()
def isAtOthersNode          (self): return self.v.isAtOthersNode()
def isAtRawFileNode         (self): return self.v.isAtRawFileNode()
def isAtSilentFileNode      (self): return self.v.isAtSilentFileNode()
def isAtThinFileNode        (self): return self.v.isAtThinFileNode()

# New names, less confusing:
isAtNoSentFileNode = isAtNoSentinelsFileNode
isAtNorefFileNode  = isAtRawFileNode
isAtAsisFileNode   = isAtSilentFileNode

# Utilities.
def matchHeadline (self,pattern): return self.v.matchHeadline(pattern)
## def afterHeadlineMatch (self,s): return self.v.afterHeadlineMatch(s)
</t>
<t tx="ekr.20060914203123.118">def bodyString (self):
    
    return self.v.bodyString()

def headString (self):
    
    return self.v.headString()
    
def cleanHeadString (self):
    
    return self.v.cleanHeadString()
</t>
<t tx="ekr.20060914203123.119">def isDirty     (self): return self.v.isDirty()
def isExpanded  (self): return self.v.isExpanded()
def isMarked    (self): return self.v.isMarked()
def isOrphan    (self): return self.v.isOrphan()
def isSelected  (self): return self.v.isSelected()
def isTopBitSet (self): return self.v.isTopBitSet()
def isVisited   (self): return self.v.isVisited()
def status      (self): return self.v.status()
</t>
<t tx="ekr.20060914203123.120">def directParents (self):
    
    return self.v.directParents()
</t>
<t tx="ekr.20060914203123.121">def childIndex(self):
    
    p = self ; v = p.v
    
    # This is time-critical code!
    
    # 3/25/04: Much faster code:
    if not v or not v._back:
        return 0

    n = 0 ; v = v._back
    while v:
        n += 1
        v = v._back

    return n
</t>
<t tx="ekr.20060914203123.122"></t>
<t tx="ekr.20060914203123.123">def hasChildren(self):
    
    p = self
    # g.trace(p,p.v)
    return p.v and p.v.t and p.v.t._firstChild
</t>
<t tx="ekr.20060914203123.124">def numberOfChildren (self):
    
    return self.v.numberOfChildren()
</t>
<t tx="ekr.20060914203123.125"># These methods are useful abbreviations.
# Warning: they make copies of positions, so they should be used _sparingly_

def getBack          (self): return self.copy().moveToBack()
def getFirstChild    (self): return self.copy().moveToFirstChild()
def getLastChild     (self): return self.copy().moveToLastChild()
def getLastNode      (self): return self.copy().moveToLastNode()
def getLastVisible   (self): return self.copy().moveToLastVisible()
def getNext          (self): return self.copy().moveToNext()
def getNodeAfterTree (self): return self.copy().moveToNodeAfterTree()
def getNthChild    (self,n): return self.copy().moveToNthChild(n)
def getParent        (self): return self.copy().moveToParent()
def getThreadBack    (self): return self.copy().moveToThreadBack()
def getThreadNext    (self): return self.copy().moveToThreadNext()
def getVisBack       (self): return self.copy().moveToVisBack()
def getVisNext       (self): return self.copy().moveToVisNext()

# These are efficient enough now that iterators are the normal way to traverse the tree!

back          = getBack
firstChild    = getFirstChild
lastChild     = getLastChild
lastNode      = getLastNode
lastVisible   = getLastVisible # New in 4.2 (was in tk tree code).
next          = getNext
nodeAfterTree = getNodeAfterTree
nthChild      = getNthChild
parent        = getParent
threadBack    = getThreadBack
threadNext    = getThreadNext
visBack       = getVisBack
visNext       = getVisNext
</t>
<t tx="ekr.20060914203123.126">def hasBack(self):
    return self.v and self.v._back

hasFirstChild = hasChildren
    
def hasNext(self):
    return self.v and self.v._next
    
def hasParent(self):
    return self.v and self.v._parent is not None
    
def hasThreadBack(self):
    return self.hasParent() or self.hasBack() # Much cheaper than computing the actual value.
    
hasVisBack = hasThreadBack
</t>
<t tx="ekr.20060914203123.127">def hasThreadNext(self):

    p = self ; v = p.v
    if not p.v: return False

    if v.t._firstChild or v._next:
        return True
    else:
        n = len(p.stack)-1
        v,n = p.vParentWithStack(v,p.stack,n)
        while v:
            if v._next:
                return True
            v,n = p.vParentWithStack(v,p.stack,n)
        return False

hasVisNext = hasThreadNext
</t>
<t tx="ekr.20060914203123.128">def isAncestorOf (self, p2):
    
    p = self
    
    if 0: # Avoid the copies made in the iterator.
        for p3 in p2.parents_iter():
            if p3 == p:
                return True

    # Avoid calling p.copy() or copying the stack.
    v2 = p2.v ; n = len(p2.stack)-1
        # Major bug fix 7/22/04: changed len(p.stack) to len(p2.stack.)
    v2,n = p2.vParentWithStack(v2,p2.stack,n)
    while v2:
        if v2 == p.v:
            return True
        v2,n = p2.vParentWithStack(v2,p2.stack,n)

    return False
</t>
<t tx="ekr.20060914203123.129">def isCloned (self):
    
    return len(self.v.t.vnodeList) &gt; 1
</t>
<t tx="ekr.20060914203123.130">def isRoot (self):
    
    p = self

    return not p.hasParent() and not p.hasBack()
</t>
<t tx="ekr.20060914203123.131">def isVisible (self):
    
    """Return True if all of a position's parents are expanded."""

    # v.isVisible no longer exists.
    p = self

    # Avoid calling p.copy() or copying the stack.
    v = p.v ; n = len(p.stack)-1

    v,n = p.vParentWithStack(v,p.stack,n)
    while v:
        if not v.isExpanded():
            return False
        v,n = p.vParentWithStack(v,p.stack,n)

    return True
</t>
<t tx="ekr.20060914203123.132">def simpleLevel(self):
    
    return len([p for p in self.parents_iter()])

def level(self,verbose=False):
    
    p = self ; level = 0
    if not p: return level
        
    # Avoid calling p.copy() or copying the stack.
    v = p.v ; n = len(p.stack)-1
    while 1:
        assert(p)
        v,n = p.vParentWithStack(v,p.stack,n)
        if v:
            level += 1
            if verbose: g.trace(level,"level %2d, n: %2d" % (level,n))
        else:
            if verbose: g.trace(level,"level %2d, n: %2d" % (level,n))
            # if g.app.debug: assert(level==self.simpleLevel())
            break
    return level
</t>
<t tx="ekr.20060914203123.133"></t>
<t tx="ekr.20060914203123.134"></t>
<t tx="ekr.20060914203123.135"># Clone bits are no longer used.
# Dirty bits are handled carefully by the position class.

def clearMarked  (self): return self.v.clearMarked()
def clearOrphan  (self): return self.v.clearOrphan()
def clearVisited (self): return self.v.clearVisited()

def contract (self): return self.v.contract()
def expand   (self): return self.v.expand()

def initExpandedBit    (self): return self.v.initExpandedBit()
def initMarkedBit      (self): return self.v.initMarkedBit()
def initStatus (self, status): return self.v.initStatus(status)
    
def setMarked   (self): return self.v.setMarked()
def setOrphan   (self): return self.v.setOrphan()
def setSelected (self): return self.v.setSelected()
def setVisited  (self): return self.v.setVisited()
</t>
<t tx="ekr.20060914203123.136">def computeIcon (self):
    
    return self.v.computeIcon()
    
def setIcon (self):

    pass # Compatibility routine for old scripts
</t>
<t tx="ekr.20060914203123.137">def setSelection (self,start,length):

    return self.v.setSelection(start,length)
</t>
<t tx="ekr.20060914203123.138">def setTnodeText (self,s,encoding="utf-8"):
    
    return self.v.setTnodeText(s,encoding)
</t>
<t tx="ekr.20060914203123.139"></t>
<t tx="ekr.20060914203123.140">def setHeadString (self,s,encoding="utf-8"):
    
    p = self
    p.v.initHeadString(s,encoding)
    p.setDirty()
    
def initHeadString (self,s,encoding="utf-8"):
    
    p = self
    p.v.initHeadString(s,encoding)
</t>
<t tx="ekr.20060914203123.141">def scriptSetBodyString (self,s,encoding="utf-8"):
    
    """Update the body string for the receiver.
    
    Should be called only from scripts: does NOT update body text."""

    self.v.t.bodyString = g.toUnicode(s,encoding)
</t>
<t tx="ekr.20060914203123.142"></t>
<t tx="ekr.20060914203123.143"># Compatibility routine for scripts.

def clearVisitedInTree (self):
    
    for p in self.self_and_subtree_iter():
        p.clearVisited()
</t>
<t tx="ekr.20060914203123.144">def clearAllVisitedInTree (self):
    
    for p in self.self_and_subtree_iter():
        p.v.clearVisited()
        p.v.t.clearVisited()
        p.v.t.clearWriteBit()
</t>
<t tx="ekr.20060914203123.145"></t>
<t tx="ekr.20060914203123.146">def clearDirty (self):

    p = self
    p.v.clearDirty()
</t>
<t tx="ekr.20060914203123.147">def findAllPotentiallyDirtyNodes(self):
    
    p = self 
    
    # Start with all nodes in the vnodeList.
    nodes = []
    newNodes = p.v.t.vnodeList[:]

    # Add nodes until no more are added.
    while newNodes:
        addedNodes = []
        nodes.extend(newNodes)
        for v in newNodes:
            for v2 in v.t.vnodeList:
                if v2 not in nodes and v2 not in addedNodes:
                    addedNodes.append(v2)
                for v3 in v2.directParents():
                    if v3 not in nodes and v3 not in addedNodes:
                        addedNodes.append(v3)
        newNodes = addedNodes[:]

    # g.trace(len(nodes))
    return nodes
</t>
<t tx="ekr.20060914203123.148">def setAllAncestorAtFileNodesDirty (self,setDescendentsDirty=False):

    p = self
    dirtyVnodeList = []
    
    # Calculate all nodes that are joined to p or parents of such nodes.
    nodes = p.findAllPotentiallyDirtyNodes()
    
    if setDescendentsDirty:
        # N.B. Only mark _direct_ descendents of nodes.
        # Using the findAllPotentiallyDirtyNodes algorithm would mark way too many nodes.
        for p2 in p.subtree_iter():
            # Only @thin nodes need to be marked.
            if p2.v not in nodes and p2.isAtThinFileNode():
                nodes.append(p2.v)
                
    dirtyVnodeList = [v for v in nodes
        if not v.t.isDirty() and v.isAnyAtFileNode()]
    changed = len(dirtyVnodeList) &gt; 0
    
    for v in dirtyVnodeList:
        v.t.setDirty() # Do not call v.setDirty here!

    return dirtyVnodeList</t>
<t tx="ekr.20060914203123.149">def setDirty (self,setDescendentsDirty=True):
    
    '''Mark a node and all ancestor @file nodes dirty.'''

    p = self ; dirtyVnodeList = []
    
    # g.trace(p.headString(),g.callers())

    if not p.v.t.isDirty():
        p.v.t.setDirty()
        dirtyVnodeList.append(p.v)

    # Important: this must be called even if p.v is already dirty.
    # Typing can change the @ignore state!
    dirtyVnodeList2 = p.setAllAncestorAtFileNodesDirty(setDescendentsDirty)
    dirtyVnodeList.extend(dirtyVnodeList2)
   
    return dirtyVnodeList
</t>
<t tx="ekr.20060914203123.150">def inAtIgnoreRange (self):
    
    """Returns True if position p or one of p's parents is an @ignore node."""
    
    p = self
    
    for p in p.self_and_parents_iter():
        if p.isAtIgnoreNode():
            return True

    return False
</t>
<t tx="ekr.20060914203123.151">@
- convertTreeToString and moreHead can't be vnode methods because they uses level().
- moreBody could be anywhere: it may as well be a postion method.
</t>
<t tx="ekr.20060914203123.152">def convertTreeToString (self):
    
    """Convert a positions  suboutline to a string in MORE format."""

    p = self ; level1 = p.level()
    
    array = []
    for p in p.self_and_subtree_iter():
        array.append(p.moreHead(level1)+'\n')
        body = p.moreBody()
        if body:
            array.append(body +'\n')

    return ''.join(array)
</t>
<t tx="ekr.20060914203123.153">def moreHead (self, firstLevel,useVerticalBar=False):
    
    """Return the headline string in MORE format."""
    
    # useVerticalBar is unused, but it would be useful in over-ridden methods.
    __pychecker__ = '--no-argsused'

    p = self
    level = self.level() - firstLevel
    plusMinus = g.choose(p.hasChildren(), "+", "-")
    
    return "%s%s %s" % ('\t'*level,plusMinus,p.headString())
</t>
<t tx="ekr.20060914203123.154">@ 
    + test line
    - test line
    \ test line
    test line +
    test line -
    test line \
    More lines...
@c

def moreBody (self):

    """Returns the body string in MORE format.  
    
    Inserts a backslash before any leading plus, minus or backslash."""

    p = self ; array = []
    lines = string.split(p.bodyString(),'\n')
    for s in lines:
        i = g.skip_ws(s,0)
        if i &lt; len(s) and s[i] in ('+','-','\\'):
            s = s[:i] + '\\' + s[i:]
        array.append(s)
    return '\n'.join(array)
</t>
<t tx="ekr.20060914203123.155">@ 3/18/04: a crucial optimization:

Iterators make no copies at all if they would return an empty sequence.
@c

@others
</t>
<t tx="ekr.20060914203123.156">def tnodes_iter(self):
    
    """Return all tnode's in a positions subtree."""
    
    p = self
    for p in p.self_and_subtree_iter():
        yield p.v.t
        
def unique_tnodes_iter(self):
    
    """Return all unique tnode's in a positions subtree."""
    
    p = self
    marks = {}
    for p in p.self_and_subtree_iter():
        if p.v.t not in marks:
            marks[p.v.t] = p.v.t
            yield p.v.t
</t>
<t tx="ekr.20060914203123.157">def vnodes_iter(self):
    
    """Return all vnode's in a positions subtree."""
    
    p = self
    for p in p.self_and_subtree_iter():
        yield p.v
        
def unique_vnodes_iter(self):
    
    """Return all unique vnode's in a positions subtree."""
    
    p = self
    marks = {}
    for p in p.self_and_subtree_iter():
        if p.v not in marks:
            marks[p.v] = p.v
            yield p.v
</t>
<t tx="ekr.20060914203123.158">class subtree_iter_class:

    """Returns a list of positions in a subtree, possibly including the root of the subtree."""

    @others

def subtree_iter (self,copy=False):
    
    return self.subtree_iter_class(self,copy,includeSelf=False)
    
def self_and_subtree_iter (self,copy=False):
    
    return self.subtree_iter_class(self,copy,includeSelf=True)
</t>
<t tx="ekr.20060914203123.159">def __init__(self,p,copy,includeSelf):
    
    if includeSelf:
        self.first = p.copy()
        self.after = p.nodeAfterTree()
    elif p.hasChildren():
        self.first = p.copy().moveToFirstChild() 
        self.after = p.nodeAfterTree()
    else:
        self.first = None
        self.after = None

    self.p = None
    self.copy = copy
    
def __iter__(self):

    return self
</t>
<t tx="ekr.20060914203123.160">def next(self):
    
    if self.first:
        self.p = self.first
        self.first = None

    elif self.p:
        self.p.moveToThreadNext()

    if self.p and self.p != self.after:
        if self.copy: return self.p.copy()
        else:         return self.p
    else:
        raise StopIteration
</t>
<t tx="ekr.20060914203123.161">class children_iter_class:

    """Returns a list of children of a position."""

    @others

def children_iter (self,copy=False):
    
    return self.children_iter_class(self,copy)
</t>
<t tx="ekr.20060914203123.162">def __init__(self,p,copy):

    if p.hasChildren():
        self.first = p.copy().moveToFirstChild()
    else:
        self.first = None

    self.p = None
    self.copy = copy

def __iter__(self):
    
    return self
</t>
<t tx="ekr.20060914203123.163">def next(self):
    
    if self.first:
        self.p = self.first
        self.first = None

    elif self.p:
        self.p.moveToNext()

    if self.p:
        if self.copy: return self.p.copy()
        else:         return self.p
    else: raise StopIteration
</t>
<t tx="ekr.20060914203123.164">class parents_iter_class:

    """Returns a list of positions of a position."""

    @others

def parents_iter (self,copy=False):

    return self.parents_iter_class(self,copy,includeSelf=False)
    
def self_and_parents_iter(self,copy=False):
    
    return self.parents_iter_class(self,copy,includeSelf=True)
</t>
<t tx="ekr.20060914203123.165">def __init__(self,p,copy,includeSelf):

    if includeSelf:
        self.first = p.copy()
    elif p.hasParent():
        self.first = p.copy().moveToParent()
    else:
        self.first = None

    self.p = None
    self.copy = copy

def __iter__(self):

    return self
</t>
<t tx="ekr.20060914203123.166">def next(self):
    
    if self.first:
        self.p = self.first
        self.first = None

    elif self.p:
        self.p.moveToParent()

    if self.p:
        if self.copy: return self.p.copy()
        else:         return self.p
    else:
        raise StopIteration
</t>
<t tx="ekr.20060914203123.167">class siblings_iter_class:

    '''Returns a list of siblings of a position, including the position itself!'''

    @others

def siblings_iter (self,copy=False,following=False):
    
    return self.siblings_iter_class(self,copy,following)
    
self_and_siblings_iter = siblings_iter
    
def following_siblings_iter (self,copy=False):
    
    return self.siblings_iter_class(self,copy,following=True)
</t>
<t tx="ekr.20060914203123.168">def __init__(self,p,copy,following):
    
    # We always include p, even if following is True.
    
    if following:
        self.first = p.copy()
    else:
        p = p.copy()
        while p.hasBack():
            p.moveToBack()
        self.first = p

    self.p = None
    self.copy = copy

def __iter__(self):
    
    return self
</t>
<t tx="ekr.20060914203123.169">def next(self):
    
    if self.first:
        self.p = self.first
        self.first = None

    elif self.p:
        self.p.moveToNext()

    if self.p:
        if self.copy: return self.p.copy()
        else:         return self.p
    else: raise StopIteration
</t>
<t tx="ekr.20060914203123.170"></t>
<t tx="ekr.20060914203123.171">def clone (self):
    
    """Create a clone of back.
    
    Returns the newly created position."""
    
    p = self

    p2 = p.copy()
    p2.v = vnode(p.v.t)
    p2.linkAfter(p)

    return p2</t>
<t tx="ekr.20060914203123.172"># These used by unit tests and by the group_operations plugin.

def copyTreeAfter(self):
    p = self
    p2 = p.insertAfter()
    p.copyTreeFromSelfTo(p2)
    return p2
    
def copyTreeFromSelfTo(self,p2):
    p = self
    p2.v.t.headString = p.headString()
    p2.v.t.bodyString = p.bodyString()
    for child in p.children_iter(copy=True):
        child2 = p2.insertAsLastChild()
        child.copyTreeFromSelfTo(child2)
</t>
<t tx="ekr.20060914203123.173">@ This is the main delete routine.  It deletes the receiver's entire tree from the screen.  Because of the undo command we never actually delete vnodes or tnodes.
@c

def doDelete (self):

    """Deletes position p from the outline."""

    p = self
    p.setDirty() # Mark @file nodes dirty!
    p.unlink()
    p.deleteLinksInTree()
</t>
<t tx="ekr.20060914203123.174">def insertAfter (self,t=None):

    """Inserts a new position after self.
    
    Returns the newly created position."""
    
    p = self
    p2 = self.copy()

    if not t:
        t = tnode(headString="NewHeadline")

    p2.v = vnode(t)
    p2.v.iconVal = 0
    p2.linkAfter(p)

    return p2
</t>
<t tx="ekr.20060914203123.175">def insertAsLastChild (self,t=None):

    """Inserts a new vnode as the last child of self.
    
    Returns the newly created position."""
    
    p = self
    n = p.numberOfChildren()

    if not t:
        t = tnode(headString="NewHeadline")
    
    return p.insertAsNthChild(n,t)
</t>
<t tx="ekr.20060914203123.176">def insertAsNthChild (self,n,t=None):

    """Inserts a new node as the the nth child of self.
    self must have at least n-1 children.
    
    Returns the newly created position."""
    
    p = self ; p2 = self.copy()

    if not t:
        t = tnode(headString="NewHeadline")

    p2.v = vnode(t)
    p2.v.iconVal = 0
    p2.linkAsNthChild(p,n)

    return p2
</t>
<t tx="ekr.20060914203123.177">def invalidOutline (self, message):
    
    p = self

    if p.hasParent():
        node = p.parent()
    else:
        node = p

    g.alert("invalid outline: %s\n%s" % (message,node))
</t>
<t tx="ekr.20060914203123.178">def moveAfter (self,a):

    """Move a position after position a."""
    
    p = self # Do NOT copy the position!
    p.unlink()
    p.linkAfter(a)

    return p</t>
<t tx="ekr.20060914203123.179">def moveToLastChildOf (self,parent):

    """Move a position to the last child of parent."""

    p = self # Do NOT copy the position!

    p.unlink()
    n = parent.numberOfChildren()
    p.linkAsNthChild(parent,n)
        
    return p</t>
<t tx="ekr.20060914203123.180">def moveToNthChildOf (self,parent,n):

    """Move a position to the nth child of parent."""

    p = self # Do NOT copy the position!
    p.unlink()
    p.linkAsNthChild(parent,n)

    return p</t>
<t tx="ekr.20060914203123.181">def moveToRoot (self,oldRoot=None):

    '''Moves a position to the root position.
    
    Important: oldRoot must the previous root position if it exists.'''

    p = self # Do NOT copy the position!
    p.unlink()
    p.linkAsRoot(oldRoot)
    
    return p
</t>
<t tx="ekr.20060914203123.182"># This routine checks the structure of the receiver's tree.

def validateOutlineWithParent (self,pv):
    
    p = self
    result = True # optimists get only unpleasant surprises.
    parent = p.getParent()
    childIndex = p.childIndex()
    
    # g.trace(p,parent,pv)
    &lt;&lt; validate parent ivar &gt;&gt;
    &lt;&lt; validate childIndex ivar &gt;&gt;
    &lt;&lt; validate x ivar &gt;&gt;

    # Recursively validate all the children.
    for child in p.children_iter():
        r = child.validateOutlineWithParent(p)
        if not r: result = False

    return result
</t>
<t tx="ekr.20060914203123.183">if parent != pv:
    p.invalidOutline( "Invalid parent link: " + repr(parent))
</t>
<t tx="ekr.20060914203123.184">if pv:
    if childIndex &lt; 0:
        p.invalidOutline ( "missing childIndex" + childIndex )
    elif childIndex &gt;= pv.numberOfChildren():
        p.invalidOutline ( "missing children entry for index: " + childIndex )
elif childIndex &lt; 0:
    p.invalidOutline ( "negative childIndex" + childIndex )
</t>
<t tx="ekr.20060914203123.185">if not p.v.t and pv:
    self.invalidOutline ( "Empty t" )
</t>
<t tx="ekr.20060914203123.186">@
These routines change self to a new position "in place".
That is, these methods must _never_ call p.copy().

When moving to a nonexistent position, these routines simply set p.v = None,
leaving the p.stack unchanged. This allows the caller to "undo" the effect of
the invalid move by simply restoring the previous value of p.v.

These routines all return self on exit so the following kind of code will work:
    after = p.copy().moveToNodeAfterTree()
</t>
<t tx="ekr.20060914203123.187">def moveToBack (self):
    
    """Move self to its previous sibling."""
    
    p = self

    p.v = p.v and p.v._back
    
    return p
</t>
<t tx="ekr.20060914203123.188">def moveToFirstChild (self):

    """Move a position to it's first child's position."""
    
    p = self

    if p:
        child = p.v.t._firstChild
        if child:
            if p.isCloned():
                p.stack.append(p.v)
                # g.trace("push",p.v,p)
            p.v = child
        else:
            p.v = None
        
    return p

</t>
<t tx="ekr.20060914203123.189">def moveToLastChild (self):
    
    """Move a position to it's last child's position."""
    
    p = self

    if p:
        if p.v.t._firstChild:
            child = p.v.lastChild()
            if p.isCloned():
                p.stack.append(p.v)
                # g.trace("push",p.v,p)
            p.v = child
        else:
            p.v = None
            
    return p
</t>
<t tx="ekr.20060914203123.190">def moveToLastNode (self):
    
    """Move a position to last node of its tree.
    
    N.B. Returns p if p has no children."""
    
    p = self
    
    # Huge improvement for 4.2.
    while p.hasChildren():
        p.moveToLastChild()

    return p
</t>
<t tx="ekr.20060914203123.191">def moveToNext (self):
    
    """Move a position to its next sibling."""
    
    p = self
    
    p.v = p.v and p.v._next
    
    return p
</t>
<t tx="ekr.20060914203123.192">def moveToNodeAfterTree (self):
    
    """Move a position to the node after the position's tree."""
    
    p = self
    
    while p:
        if p.hasNext():
            p.moveToNext()
            break
        p.moveToParent()

    return p
</t>
<t tx="ekr.20060914203123.193">def moveToNthChild (self,n):
    
    p = self
    
    if p:
        child = p.v.nthChild(n) # Must call vnode method here!
        if child:
            if p.isCloned():
                p.stack.append(p.v)
                # g.trace("push",p.v,p)
            p.v = child
        else:
            p.v = None
            
    return p
</t>
<t tx="ekr.20060914203123.194">def moveToParent (self):
    
    """Move a position to its parent position."""
    
    p = self
    
    if not p: return p

    if p.v._parent and len(p.v._parent.t.vnodeList) == 1:
        p.v = p.v._parent
    elif p.stack:
        p.v = p.stack.pop()
    else:
        p.v = None
    return p
</t>
<t tx="ekr.20060914203123.195">def moveToThreadBack (self):
    
    """Move a position to it's threadBack position."""

    p = self

    if p.hasBack():
        p.moveToBack()
        p.moveToLastNode()
    else:
        p.moveToParent()

    return p
</t>
<t tx="ekr.20060914203123.196">def moveToThreadNext (self):
    
    """Move a position to the next a position in threading order."""
    
    p = self

    if p:
        if p.v.t._firstChild:
            p.moveToFirstChild()
        elif p.v._next:
            p.moveToNext()
        else:
            p.moveToParent()
            while p:
                if p.v._next:
                    p.moveToNext()
                    break #found
                p.moveToParent()
            # not found.
                
    return p
</t>
<t tx="ekr.20060914203123.197">def moveToVisBack (self):
    
    """Move a position to the position of the previous visible node."""

    p = self
    
    if p:
        p.moveToThreadBack()
        while p and not p.isVisible():
            p.moveToThreadBack()

    assert(not p or p.isVisible())
    return p
</t>
<t tx="ekr.20060914203123.198">def moveToVisNext (self):
    
    """Move a position to the position of the next visible node."""

    p = self

    p.moveToThreadNext()
    while p and not p.isVisible():
        p.moveToThreadNext()
            
    return p
</t>
<t tx="ekr.20060914203123.199"></t>
<t tx="ekr.20060914203123.200"># A crucial utility method.
# The p.level(), p.isVisible() and p.hasThreadNext() methods show how to use this method.

&lt;&lt; about the vParentWithStack utility method &gt;&gt;

def vParentWithStack(self,v,stack,n):
    
    """A utility that allows the computation of p.v without calling p.copy().
    
    v,stack[:n] correspond to p.v,p.stack for some intermediate position p.

    Returns (v,n) such that v,stack[:n] correpond to the parent position of p."""

    if not v:
        return None,n
    elif v._parent and len(v._parent.t.vnodeList) == 1:
        return v._parent,n # don't change stack.
    elif stack and n &gt;= 0:
        return self.stack[n],n-1 # simulate popping the stack.
    else:
        return None,n
</t>
<t tx="ekr.20060914203123.201">@ 
This method allows us to simulate calls to p.parent() without generating any intermediate data.

For example, the code below will compute the same values for list1 and list2:

# The first way depends on the call to p.copy:
list1 = []
p=p.copy() # odious.
while p:
    p = p.moveToParent()
    if p: list1.append(p.v)

# The second way uses p.vParentWithStack to avoid all odious intermediate data.

list2 = []
n = len(p.stack)-1
v,n = p.vParentWithStack(v,p.stack,n)
while v:
    list2.append(v)
    v,n = p.vParentWithStack(v,p.stack,n)
</t>
<t tx="ekr.20060914203123.202">def restoreLinksInTree (self):

    """Restore links when undoing a delete node operation."""
    
    root = p = self

    if p.v not in p.v.t.vnodeList:
        p.v.t.vnodeList.append(p.v)
        p.v.t._p_changed = 1 # Support for tnode class.
        
    for p in root.children_iter():
        p.restoreLinksInTree()
</t>
<t tx="ekr.20060914203123.203">def deleteLinksInTree (self):
    
    """Delete and otherwise adjust links when deleting node."""
    
    root = self

    root.deleteLinksInSubtree()
    
    for p in root.children_iter():
        p.adjustParentLinksInSubtree(parent=root)
</t>
<t tx="ekr.20060914203123.204">def deleteLinksInSubtree (self):

    root = p = self

    # Delete p.v from the vnodeList
    if p.v in p.v.t.vnodeList:
        # g.trace('**** remove p.v from %s' % p.headString())
        p.v.t.vnodeList.remove(p.v)
        p.v.t._p_changed = 1  # Support for tnode class.
        assert(p.v not in p.v.t.vnodeList)
    else:
        # g.trace("not in vnodeList",p.v,p.vnodeListIds())
        pass

    if len(p.v.t.vnodeList) == 0:
        # This node is not shared by other nodes.
        for p in root.children_iter():
            p.deleteLinksInSubtree()
</t>
<t tx="ekr.20060914203123.205">def adjustParentLinksInSubtree (self,parent):
    
    root = p = self
    
    assert(parent)
    
    if p.v._parent and parent.v.t.vnodeList and p.v._parent not in parent.v.t.vnodeList:
        # g.trace('**** adjust parent in %s' % p.headString())
        p.v._parent = parent.v.t.vnodeList[0]
        
    for p in root.children_iter():
        p.adjustParentLinksInSubtree(parent=root)
</t>
<t tx="ekr.20060914203123.206"># These remain in 4.2:  linking and unlinking does not depend on position.

# These are private routines:  the position class does not define proxies for these.
</t>
<t tx="ekr.20060914203123.207">def linkAfter (self,after):

    """Link self after v."""
    
    p = self
    # g.trace(p,after)
    
    p.stack = after.stack[:]
    p.v._parent = after.v._parent
    
    # Add v to it's tnode's vnodeList.
    if p.v not in p.v.t.vnodeList:
        p.v.t.vnodeList.append(p.v)
        p.v.t._p_changed = 1 # Support for tnode class.
    
    p.v._back = after.v
    p.v._next = after.v._next
    
    after.v._next = p.v
    
    if p.v._next:
        p.v._next._back = p.v

    if 0:
        g.trace('-'*20,after)
        p.dump(label="p")
        after.dump(label="back")
        if p.hasNext(): p.next().dump(label="next")
</t>
<t tx="ekr.20060914203123.208">def linkAsNthChild (self,parent,n):

    """Links self as the n'th child of vnode pv"""
    
    # g.trace(self,parent,n,parent.v)

    p = self

    # Recreate the stack using the parent.
    p.stack = parent.stack[:]

    if parent.isCloned():
        p.stack.append(parent.v)

    p.v._parent = parent.v

    # Add v to it's tnode's vnodeList.
    if p.v not in p.v.t.vnodeList:
        p.v.t.vnodeList.append(p.v)
        p.v.t._p_changed = 1 # Support for tnode class.

    if n == 0:
        child1 = parent.v.t._firstChild
        p.v._back = None
        p.v._next = child1
        if child1:
            child1._back = p.v
        parent.v.t._firstChild = p.v
    else:
        prev = parent.nthChild(n-1) # zero based
        assert(prev)
        p.v._back = prev.v
        p.v._next = prev.v._next
        prev.v._next = p.v
        if p.v._next:
            p.v._next._back = p.v
            
    if 0:
        g.trace('-'*20)
        p.dump(label="p")
        parent.dump(label="parent")
</t>
<t tx="ekr.20060914203123.209">def linkAsRoot (self,oldRoot):
    
    """Link self as the root node."""

    p = self ; v = p.v
    if oldRoot: oldRootVnode = oldRoot.v
    else:       oldRootVnode = None
    
    p.stack = [] # Clear the stack.
    
    # Clear all links except the child link.
    v._parent = None
    v._back = None
    v._next = oldRootVnode
    
    # Add v to it's tnode's vnodeList.
    if v not in v.t.vnodeList:
        v.t.vnodeList.append(v)
        v.t._p_changed = 1 # Support for tnode class.

    # Link in the rest of the tree only when oldRoot != None.
    # Otherwise, we are calling this routine from init code and
    # we want to start with a pristine tree.
    if oldRoot:
        oldRoot.v._back = v
    
    # p.dump(label="root")
</t>
<t tx="ekr.20060914203123.210">def unlink (self):

    """Unlinks a position p from the tree before moving or deleting.
    
    The p.v._fistChild link does NOT change."""
    
    # Warning: p.parent() is NOT necessarily the same as p.v._parent!

    p = self ; v = p.v
    
    # g.trace('p.v._parent',p.v._parent," child:",v.t._firstChild," back:",v._back, " next:",v._next)
    
    # Remove v from it's tnode's vnodeList.
    vnodeList = v.t.vnodeList
    if v in vnodeList:
        vnodeList.remove(v)
        v.t._p_changed = 1 # Support for tnode class.
    assert(v not in vnodeList)
    
    # Reset the firstChild link in its direct father.
    if p.v._parent:
        if 0: # This can fail.  I have no idea why it was present.
            assert(p.v and p.v._parent in p.v.directParents())
        if p.v._parent.t._firstChild == v:
            #g.trace('resetting _parent.v.t._firstChild to',v._next)
            p.v._parent.t._firstChild = v._next
    else:
        parent = p.parent()
        if parent:
            if 0: # This can fail.  I have no idea why it was present.
                assert(parent.v in p.v.directParents())
            if parent.v.t._firstChild == v:
                #g.trace('resetting parent().v.t._firstChild to',v._next)
                parent.v.t._firstChild = v._next

    # Do NOT delete the links in any child nodes.

    # Clear the links in other nodes.
    if v._back: v._back._next = v._next
    if v._next: v._next._back = v._back

    # Unlink _this_ node.
    v._parent = v._next = v._back = None

    if 0:
        g.trace('-'*20)
        p.dump(label="p")
        if parent: parent.dump(label="parent")</t>
</tnodes>
</leo_file>
