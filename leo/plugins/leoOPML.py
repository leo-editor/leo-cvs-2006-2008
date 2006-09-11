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

__version__ = '0.03'

opt_print_elements = False
opt_print_summary = False
opt_print_attributes = True

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
# 0.03 EKR: Use SAX to read .opml files.  Parsing works.  More semantics are 
# needed.
#@-at
#@-node:ekr.20060904103412.2:<< version history >>
#@nl
#@<< imports >>
#@+node:ekr.20060904103412.3:<< imports >>
import leoGlobals as g
import leoPlugins
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
        
        # Statistics.
        self.numberOfAttributes = 0
        self.numberOfElements = 0
        
        # Options...
        self.ignoreWs = True # True: don't print contents with only ws.
        self.newLineAfterStartElement = ['outline','head','body',]
        self.printCharacters = opt_print_elements
        self.printAttributes = opt_print_attributes
        if opt_print_elements:
            self.printElements =   ['outline','head','body',]
            self.suppressContent = ['outline','head','body','opml']
        else:
            self.printElements = []
            self.suppressContent = []
      
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
    
        if name.lower() in self.newLineAfterStartElement:
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
    
        content = g.toUnicode(content,encoding='utf-8')
        content = content.replace('\r','')
        if content.strip(): content = content.strip()
        # content = self.clean(content)
    
        elementName = self.elementStack and self.elementStack[-1].lower() or '<no element name>'
        
        if self.printCharacters and content and elementName not in self.suppressContent:
            print 'content:',elementName,repr(content)
    
        # if self.node:
            # self.node.doContent(elementName,content)
        # else:
            # self.error('characters outside of node')
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
        
        self.numberOfElements += 1
            
        self.elementStack.append(name)
        self.doStartElement(name,attrs)
    #@nonl
    #@-node:ekr.20060904134958.180:startElement
    #@-node:ekr.20060904134958.173:sax over-rides
    #@+node:ekr.20060904134958.181:doStartElement
    def doStartElement (self,elementName,attrs):
        
        elementName = elementName.lower()
        
        if elementName in self.printElements:
            self.printStartElement(elementName,attrs)
    
        if elementName == 'body':
            self.inBody= True
        elif elementName == 'head':
            self.inHead = True
        elif elementName == 'outline':
            self.level += 1
            self.node = nodeClass(contentHandler=self)
            self.nodeStack.append(self.node)
            self.node.startElement(elementName)
            for bunch in self.attrsToList(attrs):
                if self.printAttributes:
                    print 'attr:',elementName,bunch.name,'=',bunch.val
                self.node.doAttribute(bunch.name,bunch.val)
    #@nonl
    #@-node:ekr.20060904134958.181:doStartElement
    #@+node:ekr.20060904134958.182:doEndElement
    def doEndElement (self,elementName):
        
        elementName = elementName.lower()
        
        if elementName in self.printElements:
            indent = '\t' * (self.level-1) or ''
            print '%s</%s>' % (indent,self.clean(elementName).strip())
            
        if elementName == 'body':
            self.inBody= False
        elif elementName == 'head':
            self.inHead = False
        elif elementName == 'outline':
            self.level -= 1
            self.nodeStack.pop()
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
    #@+node:ekr.20060904103721:readFile
    def readFile (self,event=None,fileName=None):
        
        if fileName: 
    
            node = self.c.fileCommands.parse_opml_file(fileName)
        
            g.trace(fileName,node)
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
#@+node:ekr.20060904141220:class nodeClass
class nodeClass:
    
    '''A class representing one outline element.
    
    Use getters to access the attributes, properties and rules of this mode.'''
    
    #@    @+others
    #@+node:ekr.20060904141220.1: node.__init__
    def __init__ (self,contentHandler):
        
        # g.trace('mode',fileName)
    
        self.contentHandler = contentHandler
        self.c = contentHandler.c
        self.parent = None
        self.children = []
    
        # Mode statistics...
        self.numberOfAttributes = 0
        self.numberOfElements = 0
        self.numberOfErrors = 0
    
        
        # # List of boolean attributes.
        # self.boolAttrs = [
            # 'at_line_start','at_whitespace_end','at_word_start',
            # 'exclude_match','highlight_digits','ignore_case',
            # 'no_escape','no_line_break','no_word_break',]
     
        # # List of elements that start a rule.
        # self.ruleElements = [
            # 'eol_span','eol_span_regexp','import','keywords',
            # 'mark_following','mark_previous','seq','seq_regexp',
            # 'span','span_regexp','terminate',]
     
        # if 0: # Not used at present.
            # self.seqSpanElements = [
                # 'eol_span','eol_span_regexp','seq','seq_regexp',
                # 'span','span_regexp',]
    
        # Node semantics.
        self.attributes = {}
        self.handlerCount = 0
    #@nonl
    #@-node:ekr.20060904141220.1: node.__init__
    #@+node:ekr.20060904141220.2: node.__str__ & __repr__
    def __str__ (self):
        
        return '<nodeClass %s>' % id(self)
        
    __repr__ = __str__
    #@nonl
    #@-node:ekr.20060904141220.2: node.__str__ & __repr__
    #@+node:ekr.20060904141220.34:doAttribute
    def doAttribute (self,name,val):
        
        name = g.toUnicode(name,encoding='utf-8').lower()
        val  = g.toUnicode(val,encoding='utf-8')
        g.trace(name,val)
        return ###
        
        if name in self.boolAttrs:
            val = g.choose(val.lower()=='true',True,False)
        else:
            val = str(val) # Do NOT lower this value!
    
        if self.rule:
            d = self.rule.attributes
            d [name] = val
            self.numberOfRuleAttributes += 1
        elif self.presentProperty:
            d = self.presentProperty.get('attributes')
            d [name] = val
            self.numberOfPropertyAttributes += 1
        elif self.inRules:
            self.rulesetAttributes[name] = val
            self.numberOfAttributes += 1
        else:
            self.attributes[name] = val
            self.numberOfAttributes += 1
    #@nonl
    #@-node:ekr.20060904141220.34:doAttribute
    #@+node:ekr.20060904141220.35:doContent
    def doContent (self,elementName,content):
        
        if not content:
            return
        
        name = str(elementName.lower())
        
        g.trace(name)
        return ###
        
        if self.inRule('keywords'):
            # g.trace('in keywords',name,content)
            d = self.rule.keywordsDict
            d [ content ] = name
    
        elif self.rule:
            d = self.rule.contents
            s = d.get(name,'')
            d [name] = s + content
            self.contents = d
    #@nonl
    #@-node:ekr.20060904141220.35:doContent
    #@+node:ekr.20060904141220.36:endElement
    def endElement (self,elementName):
    
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
                self.error('end %s not matched by start %s' % (name,name))
    #@nonl
    #@-node:ekr.20060904141220.36:endElement
    #@+node:ekr.20060904141220.37:error
    def error (self,message):
        
        self.numberOfErrors += 1
    
        self.contentHandler.error(message)
    #@nonl
    #@-node:ekr.20060904141220.37:error
    #@+node:ekr.20060904141220.38:getters
    def getAttributes (self):
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
            return []
    #@nonl
    #@-node:ekr.20060904141220.38:getters
    #@+node:ekr.20060904141220.40:startElement
    def startElement (self,elementName):
        
        g.trace(elementName)
        
        return ####
    
        name = elementName.lower()
        
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
                self.error('%s not in rules element' % name)
    #@nonl
    #@-node:ekr.20060904141220.40:startElement
    #@-others
#@nonl
#@-node:ekr.20060904141220:class nodeClass
#@-others
#@nonl
#@-node:ekr.20060904103412:@thin leoOPML.py
#@-leo
