<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet ekr_stylesheet?>
<leo_file>
<leo_header file_format="2" tnodes="0" max_tnode_index="376" clone_windows="0"/>
<globals body_outline_ratio="0.5">
	<global_window_position top="68" left="324" height="835" width="872"/>
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
<v t="ekr.20060913222132"><vh>To do</vh></v>
<v t="ekr.20060904103412" a="ETV"
marks="ekr.20060904141220.34,"
expanded="ekr.20060904134958.164,"><vh>@thin leoOPML.py</vh></v>
</vnodes>
<tnodes>
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
<t tx="ekr.20060913222132">Set node.headString, node.bodyString and node.tnx in node.doAttribute.

Special case these ivars in node.dump.</t>
</tnodes>
</leo_file>
