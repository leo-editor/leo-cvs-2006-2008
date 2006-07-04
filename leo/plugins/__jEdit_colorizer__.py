#@+leo-ver=4-thin
#@+node:ekr.20060530091119.20:@thin __jEdit_colorizer__.py
'''Replace colorizer with colorizer using jEdit language description files'''

#@@language python
#@@tabwidth -4
#@@pagewidth 80

__version__ = '0.26'
#@<< imports >>
#@+node:ekr.20060530091119.21:<< imports >>
import leoGlobals as g
import leoPlugins

import os
import re
import string
import threading
import xml.sax
import xml.sax.saxutils

# php_re = re.compile("<?(\s|=|[pP][hH][pP])")
php_re = re.compile("<?(\s[pP][hH][pP])")
#@nonl
#@-node:ekr.20060530091119.21:<< imports >>
#@nl
#@<< version history >>
#@+node:ekr.20060530091119.22:<< version history >>
#@@nocolor
#@+at
# 
# 0.20 EKR: Use x.py files rather than x.xml files.
# - The colorizer now works on most text.
# 0.21 EKR: No known crashers or serious problems.
# - The colorizer now switches modes properly.
# - Possible fix for unicode crasher.
# 0.22 EKR: colorOneChunk now allows for good response to key events.
# 0.23 EKR: use g.app.gui.toGuiIndex in colorRangeWithTag.  Fixes a bug and is 
# simpler.
# 0.24 EKR: Fixed unicode crasher.  All unit tests now pass with the new 
# colorizer enabled.
# 0.25 EKR: Fixed bug in match_doc_part.
# 0.26 EKR: Added support for show/hide-invisibles commands.
#@-at
#@nonl
#@-node:ekr.20060530091119.22:<< version history >>
#@nl

#@<< define leoKeywords >>
#@+middle:ekr.20060530091119.23:module-level
#@+node:ekr.20060530091119.24:<< define leoKeywords >>
# leoKeywords is used by directivesKind, so it should be a module-level symbol.

# leoKeywords must be a list so that plugins may alter it.

leoKeywords = [
    "@","@all","@c","@code","@color","@comment",
    "@delims","@doc","@encoding","@end_raw",
    "@first","@header","@ignore",
    "@killcolor",
    "@language","@last","@lineending",
    "@nocolor","@noheader","@nowrap","@others",
    "@pagewidth","@path","@quiet","@raw","@root","@root-code","@root-doc",
    "@silent","@tabwidth","@terse",
    "@unit","@verbose","@wrap",
]

leoKeywordsDict = {}
for key in leoKeywords:
    leoKeywordsDict [key] = 'leoKeyword'
#@nonl
#@-node:ekr.20060530091119.24:<< define leoKeywords >>
#@-middle:ekr.20060530091119.23:module-level
#@nl
#@<< define default_colors_dict >>
#@+middle:ekr.20060530091119.23:module-level
#@+node:ekr.20060530091119.25:<< define default_colors_dict >>
# These defaults are sure to exist.

default_colors_dict = {
    # tag name       :(     option name,           default color),
    'comment'        :('comment_color',               'red'),
    'cwebName'       :('cweb_section_name_color',     'red'),
    'pp'             :('directive_color',             'blue'),
    'docPart'        :('doc_part_color',              'red'),
    'keyword'        :('keyword_color',               'blue'),
    'leoKeyword'     :('leo_keyword_color',           'blue'),
    'link'           :('section_name_color',          'red'),
    'nameBrackets'   :('section_name_brackets_color', 'blue'),
    'string'         :('string_color',                '#00aa00'), # Used by IDLE.
    'name'           :('undefined_section_name_color','red'),
    'latexBackground':('latex_background_color',      'white'),
    
    # jEdit tags.
    'comment1'  :('comment1_color', 'red'),
    'comment2'  :('comment2_color', 'red'),
    'comment3'  :('comment3_color', 'red'),
    'comment4'  :('comment4_color', 'red'),
    'function'  :('function_color', 'black'),
    'keyword1'  :('keyword1_color', 'blue'),
    'keyword2'  :('keyword2_color', 'blue'),
    'keyword3'  :('keyword3_color', 'blue'),
    'keyword4'  :('keyword4_color', 'blue'),
    'label'     :('label_color',    'black'),
    'literal1'  :('literal1_color', '#00aa00'),
    'literal2'  :('literal2_color', '#00aa00'),
    'literal3'  :('literal3_color', '#00aa00'),
    'literal4'  :('literal4_color', '#00aa00'),
    'markup'    :('markup_color',   'red'), ### '#00aa00'),
    'null'      :('null_color',     'black'),
    'operator'  :('operator_color', 'black'),
    }
#@nonl
#@-node:ekr.20060530091119.25:<< define default_colors_dict >>
#@-middle:ekr.20060530091119.23:module-level
#@nl
trace_match = False

#@+others
#@+node:ekr.20060530091119.23:module-level
#@+node:ekr.20060530091119.26:init
def init ():

    leoPlugins.registerHandler('start1',onStart1)
    g.plugin_signon(__name__)

    return True
#@nonl
#@-node:ekr.20060530091119.26:init
#@+node:ekr.20060530091119.27:onStart1
def onStart1 (tag, keywords):
    
    '''Override Leo's core colorizer classes.'''
    
    import leoColor

    leoColor.colorizer = colorizer
    
    leoColor.nullColorizer = nullColorizer
#@nonl
#@-node:ekr.20060530091119.27:onStart1
#@+node:ekr.20060530091119.28:Leo rule functions
#@+at
# These rule functions recognize noweb syntactic constructions. These are 
# treated
# just like rule functions, so they are module-level objects whose first 
# argument
# is 'self'.
#@-at
#@nonl
#@+node:ekr.20060530091119.29:match_at_color
def match_at_color (self,s,i):
    
    if trace_match: g.trace()

    seq = '@color'
    
    if i != 0 and s[i-1] != '\n': return 0

    if g.match_word(s,i,seq):
        self.flag = True # Enable coloring.
        j = i + len(seq)
        self.colorRangeWithTag(s,i,j,'leoKeyword')
        return j - i
    else:
        return 0
#@nonl
#@-node:ekr.20060530091119.29:match_at_color
#@+node:ekr.20060530091119.30:match_at_nocolor
def match_at_nocolor (self,s,i):
    
    if trace_match: g.trace()
    
    seq = '@nocolor'
    
    if i != 0 and s[i-1] != '\n':
        return 0

    if g.match_word(s,i,seq):
        j = i + len(seq)
        self.flag = False # Disable coloring.
        self.colorRangeWithTag(s,i,j,'leoKeyword')
        return len(seq)
    else:
        return 0
#@nonl
#@-node:ekr.20060530091119.30:match_at_nocolor
#@+node:ekr.20060530091119.31:match_doc_part
def match_doc_part (self,s,i):
    
    if trace_match: g.trace()
    
    if i >= len(s) or s[i] != '@':
        return 0
    elif i + 1 >= len(s):
        j = i + 1
        self.colorRangeWithTag(s,i,j,'docPart')
        return 1
    elif not g.match_word(s,i,'@doc') and not s[i+1] in (' ','\t','\n'):
        return 0

    j = i ; n = len(s)
    while j < n:
        k = s.find('@c',j)
        if k == -1:
            # g.trace('i,len(s)',i,len(s))
            j = n
            self.colorRangeWithTag(s,i,j,'docPart')
            return j - i
        if s[k-1] == '\n' and (g.match_word(s,k,'@c') or g.match_word(s,k,'@code')):
            j = k
            self.colorRangeWithTag(s,i,j,'docPart')
            return j - i
        else:
            j = k + 2
    j = n - 1
    return j - i
#@nonl
#@-node:ekr.20060530091119.31:match_doc_part
#@+node:ekr.20060703123822:match_leo_keywords
def match_leo_keywords(self,s,i):
    
    '''Succeed if s[i:] is a Leo keyword.'''
    
    # We must be at the start of a word.
    if i > 0 and s[i-1] in self.word_chars:
        return 0
        
    if s[i] != '@':
        return 0

    # Get the word as quickly as possible.
    j = i ; n = len(s) ; w = self.word_chars
    while j < n and s[j] in w:
        j += 1
        
    word = s[i:j]
    kind = leoKeywordsDict.get(s[i:j])
    if kind:
        # g.trace('%3d %10s %s' % (i,word,repr(kind)))
        self.colorRangeWithTag(s,i,j,kind)
        self.prev = (i,j,kind)
        return j-i
    else:
        return 0
#@nonl
#@-node:ekr.20060703123822:match_leo_keywords
#@+node:ekr.20060530091119.32:match_section_ref
def match_section_ref (self,s,i):
    
    if trace_match: g.trace()
    
    if not g.match(s,i,'<<'):
        return 0
    k = g.find_on_line(s,i+2,'>>')
    if k is not None:
        j = k + 2
        self.colorRangeWithTag(s,i,i+2,'nameBrackets')
        ref = g.findReference(s[i:j],self.p)
        if ref:
            if self.use_hyperlinks:
                #@                << set the hyperlink >>
                #@+node:ekr.20060530091119.33:<< set the hyperlink >>
                # Set the bindings to vnode callbacks.
                # Create the tag.
                # Create the tag name.
                tagName = "hyper" + str(self.hyperCount)
                self.hyperCount += 1
                self.body.tag_delete(tagName)
                self.tag(tagName,i+2,j)
                
                ref.tagName = tagName
                self.body.tag_bind(tagName,"<Control-1>",ref.OnHyperLinkControlClick)
                self.body.tag_bind(tagName,"<Any-Enter>",ref.OnHyperLinkEnter)
                self.body.tag_bind(tagName,"<Any-Leave>",ref.OnHyperLinkLeave)
                #@nonl
                #@-node:ekr.20060530091119.33:<< set the hyperlink >>
                #@nl
            else:
                self.colorRangeWithTag(s,i+2,k,'link')
        else:
            self.colorRangeWithTag(s,i+2,k,'name')
        self.colorRangeWithTag(s,k,j,'nameBrackets')
        return j - i
    else:
        return 0
#@nonl
#@-node:ekr.20060530091119.32:match_section_ref
#@+node:ekr.20060601083619:match_blanks
def match_blanks (self,s,i):
    
    if trace_match: g.trace()
    
    j = i ; n = len(s)
    
    while j < n and s[j] == ' ':
        j += 1
        
    if j > i:
        # g.trace(i,j)
        self.colorRangeWithTag(s,i,j,'blank')
        return j - i
    else:
        return 0
#@nonl
#@-node:ekr.20060601083619:match_blanks
#@+node:ekr.20060601083619.1:match_tabs
def match_tabs (self,s,i):
    
    if trace_match: g.trace()
    
    j = i ; n = len(s)
    
    while j < n and s[j] == '\t':
        j += 1
        
    if j > i:
        # g.trace(i,j)
        self.colorRangeWithTag(s,i,j,'tab')
        return j - i
    else:
        return 0
#@nonl
#@-node:ekr.20060601083619.1:match_tabs
#@-node:ekr.20060530091119.28:Leo rule functions
#@-node:ekr.20060530091119.23:module-level
#@+node:ekr.20060530091119.34:class colorizer (baseColorizer)
class baseColorizer:

    '''New colorizer using jEdit language description files'''
    #@    @+others
    #@+node:ekr.20060530091119.35:Birth and init
    #@+node:ekr.20060530091119.8:__init__
    def __init__(self,c):
        # Copies of ivars.
        self.c = c
        self.frame = c.frame
        self.body = c.frame.body
        self.p = None
        # Attributes dict ivars: defaults are as shown.
        self.default = 'null'
    	self.digit_re = ''
    	self.highlight_digits = True
    	self.ignore_case = True
    	self.no_word_sep = ''
        # Config settings.
        self.comment_string = None # Set by scanColorDirectives on @comment
        self.showInvisibles = False # True: show "invisible" characters.
        self.interrupt_count1 = c.config.getInt("colorizer_interrupt_count1") or 10
        self.interrupt_count2 = c.config.getInt("colorizer_interrupt_count2") or 5000
        self.underline_undefined = c.config.getBool("underline_undefined_section_names")
        self.use_hyperlinks = c.config.getBool("use_hyperlinks")
        # Debugging settings
        self.trace_match = True
        # State ivars...
        self.colored_ranges = {}
            # Keys are indices, values are tags.
        self.chunk_count = 0
        self.color_pass = 0
        self.count = 0
        self.comment_string = None # Can be set by @comment directive.
        self.defaultRulesList = []
        self.enabled = True # Set to False by unit tests.
        self.flag = True # True unless in range of @nocolor
        self.keywordNumber = 0 # The kind of keyword for keywordsColorHelper.
        self.kill_chunk = False
        self.language = 'python' # set by scanColorDirectives.
        self.ranges = 0
        self.redoColoring = False # May be set by plugins.
        self.redoingColoring = False
        self.was_non_incremental = False # True: we are coloring as the result of a non-incremental call.
        # Data...
        self.keywords = {} # Keys are keywords, values are 0..5.
        self.modes = {} # Keys are languages, values are modes.
        self.mode = None # The mode object for the present language.
        self.modeBunch = None # A bunch fully describing a mode.
        self.modeStack = []
        self.trace = c.config.getBool('trace_colorizer')
        if 0:
            self.defineAndExtendForthWords()
        self.word_chars = {} # Inited by init_keywords().
        self.setFontFromConfig()
        self.tags = [
            "blank","comment","cwebName","docPart","keyword","leoKeyword",
            "latexModeBackground","latexModeKeyword",
            "latexBackground","latexKeyword",
            "link","name","nameBrackets","pp","string",
            "elide","bold","bolditalic","italic", # new for wiki styling.
            "tab",
            # Leo jEdit tags...
            '@color', '@nocolor', 'doc_part', 'section_ref',
            # jEdit tags.
            'comment1','comment2','comment3','comment4',
            'function',
            'keyword1','keyword2','keyword3','keyword4',
            'label','literal1','literal2','literal3','literal4',
            'markup','operator',
        ]
        self.configure_tags()
    #@nonl
    #@-node:ekr.20060530091119.8:__init__
    #@+node:ekr.20060623081100:addImportedRules
    def addImportedRules (self,mode,rulesDict,rulesetName):
        
        '''Append any imported rules at the end of the rulesets specified in mode.importDict'''
        
        names = mode.importDict.get(rulesetName,[])
        if names: g.trace(rulesetName,names)
        return #### Not yet: unbounded recursion.
    
        for name in names:
            bunch = self.modes.get(name)
            if bunch:
                importedRulesDict = bunch.rulesDict
                g.trace('importedRulesDict',importedRulesDict)
            else:
                i = name.find('_')
                if i > -1:
                    language = name[:i]
                    delegate = name[i+1:]
                    if delegate == 'main': delegate = None
                    g.trace('language',language,'delegate',delegate)
                    savedBunch = self.modeBunch
                    ok = self.init_mode(language,delegate)
                    if ok:
                        rulesDict2 = self.rulesDict
                        g.trace('len(keys)',len(rulesDict2.keys()))
                        for key in rulesDict2.keys():
                            aList = rulesDict.get(key,[])
                            aList2 = rulesDict2.get(key)
                            aList.extend(aList2)
                            rulesDict [key] = aList
                    self.initModeFromBunch(savedBunch)
                else:
                    g.trace('No imported ruleset',name)
    #@nonl
    #@-node:ekr.20060623081100:addImportedRules
    #@+node:ekr.20060530091119.36:addLeoRules
    def addLeoRules (self,theDict):
    
        '''Put Leo-specific rules to theList.'''
    
        for ch, rule, atFront, in (
            ('@',  match_at_color,    True),
            ('@',  match_at_nocolor,  True),
            ('@',  match_doc_part,    True),
            ('<',  match_section_ref, True),
            (' ',  match_blanks,      False),
            ('\t', match_tabs,        False),
            ('@',  match_leo_keywords,False),
        ):
            theList = theDict.get(ch,[])
            if atFront:
                theList.insert(0,rule)
            else:
                theList.append(rule)
            theDict [ch] = theList
    #@nonl
    #@-node:ekr.20060530091119.36:addLeoRules
    #@+node:ekr.20060530091119.37:configure_tags
    def configure_tags (self):
    
        c = self.c
    
        keys = default_colors_dict.keys() ; keys.sort()
        for name in keys:
            option_name,default_color = default_colors_dict[name]
            color = c.config.getColor(option_name) or default_color
            # g.trace(name,option_name,color)
                
            # Must use foreground, not fg.
            try:
                self.body.tag_configure(name, foreground=color)
            except: # Recover after a user error.
                g.es_exception()
                self.body.tag_configure(name, foreground=default_color)
        
        # underline=var doesn't seem to work.
        if 0: # self.use_hyperlinks: # Use the same coloring, even when hyperlinks are in effect.
            self.body.tag_configure("link",underline=1) # defined
            self.body.tag_configure("name",underline=0) # undefined
        else:
            self.body.tag_configure("link",underline=0)
            if self.underline_undefined:
                self.body.tag_configure("name",underline=1)
            else:
                self.body.tag_configure("name",underline=0)
                
        self.configure_variable_tags()
            
        # Colors for latex characters.  Should be user options...
        
        if 1: # Alas, the selection doesn't show if a background color is specified.
            self.body.tag_configure("latexModeBackground",foreground="black")
            self.body.tag_configure("latexModeKeyword",foreground="blue")
            self.body.tag_configure("latexBackground",foreground="black")
            self.body.tag_configure("latexKeyword",foreground="blue")
        else: # Looks cool, and good for debugging.
            self.body.tag_configure("latexModeBackground",foreground="black",background="seashell1")
            self.body.tag_configure("latexModeKeyword",foreground="blue",background="seashell1")
            self.body.tag_configure("latexBackground",foreground="black",background="white")
            self.body.tag_configure("latexKeyword",foreground="blue",background="white")
            
        # Tags for wiki coloring.
        self.body.tag_configure("bold",font=self.bold_font)
        self.body.tag_configure("italic",font=self.italic_font)
        self.body.tag_configure("bolditalic",font=self.bolditalic_font)
        for name in self.color_tags_list:
            self.body.tag_configure(name,foreground=name)
    #@nonl
    #@-node:ekr.20060530091119.37:configure_tags
    #@+node:ekr.20060601085857:configure_variable_tags
    def configure_variable_tags (self):
        
        c = self.c
    
        for name,option_name,default_color in (
            ("blank","show_invisibles_space_background_color","Gray90"),
            ("tab",  "show_invisibles_tab_background_color",  "Gray80"),
            ("elide", None,                                   "yellow"),
        ):
            if self.showInvisibles:
                color = option_name and c.config.getColor(option_name) or default_color
            else:
                option_name,default_color = default_colors_dict.get(name,(None,None),)
                color = option_name and c.config.getColor(option_name) or ''
            try:
                self.body.tag_configure(name,background=color)
            except: # A user error.
                self.body.tag_configure(name,background=default_color)
    
        # Special case:
        if not self.showInvisibles:
            self.body.tag_configure("elide",elide="1")
    #@nonl
    #@-node:ekr.20060601085857:configure_variable_tags
    #@+node:ekr.20060530091119.9:init_mode & helpers
    def init_mode (self,language,delegate=None):
        
        if not language: return
        rulesetName = self.computeRulesetName(language,delegate)
        if not delegate: self.modeStack = []
        bunch = self.modes.get(rulesetName)
        if bunch:
            self.initModeFromBunch(bunch)
            return True
        else:
            g.trace(rulesetName)
            path = g.os_path_join(g.app.loadDir,'..','modes')
            mode = g.importFromPath (language,path)
            if not mode:
                g.trace('Not found: %s' % rulesetName)
                return False
            self.language = language
            self.rulesetName = rulesetName
            self.keywordsDict = mode.keywordsDictDict.get(rulesetName,{})
            self.setKeywords()
            self.attributesDict = mode.attributesDictDict.get(rulesetName)
            self.setModeAttributes()
            self.rulesDict = mode.rulesDictDict.get(rulesetName)
            self.addLeoRules(self.rulesDict)
            self.addImportedRules(mode,self.rulesDict,rulesetName)
            self.defaultColor = 'null'
            self.mode = mode
            self.modes [rulesetName] = self.modeBunch = g.Bunch(
                attributesDict  = self.attributesDict,
                defaultColor    = self.defaultColor,
                keywordsDict    = self.keywordsDict,
                language        = self.language,
                mode            = self.mode,
                rulesDict       = self.rulesDict,
                rulesetName     = self.rulesetName)
            return True
    #@nonl
    #@+node:ekr.20060530091119.18:setKeywords
    def setKeywords (self):
        
        '''Initialize the keywords for the present language.
        
         Set self.word_chars ivar to string.letters + string.digits
         plus any other character appearing in any keyword.'''
         
        d = self.keywordsDict
    
        # Add any new user keywords to leoKeywords.
        keys = d.keys()
        for s in g.globalDirectiveList:
            key = '@' + s
            if key not in keys:
                d [key] = 'leoKeyword'
    
        # Create the word_chars list. 
        self.word_chars = [g.toUnicode(ch,encoding='UTF-8') for ch in (string.letters + string.digits)]
        for key in d.keys():
            for ch in key:
                if ch not in self.word_chars:
                    self.word_chars.append(g.toUnicode(ch,encoding='UTF-8'))
                    
        # g.trace(len(d.keys()))
    #@nonl
    #@-node:ekr.20060530091119.18:setKeywords
    #@+node:ekr.20060703070148:setModeAttributes
    def setModeAttributes (self):
    
        '''Set the ivars from self.attributesDict,
        converting 'true'/'false' to True and False.'''
    
        d = self.attributesDict
        aList = (
            ('default',         'null'),
    	    ('digit_re',        ''),
    	    ('highlight_digits',True),
    	    ('ignore_case',     True),
    	    ('no_word_sep',     ''),
        )
    
        for key, default in aList:
            val = d.get(key,default)
            if val in ('true','True'): val = True
            if val in ('false','False'): val = False
            setattr(self,key,val)
            # g.trace(key,val)
    #@nonl
    #@-node:ekr.20060703070148:setModeAttributes
    #@+node:ekr.20060703110708:initModeFromBunch
    def initModeFromBunch (self,bunch):
        
        self.modeBunch = bunch
        self.attributesDict = bunch.attributesDict
        self.setModeAttributes()
        self.defaultColor   = bunch.defaultColor
        self.keywordsDict   = bunch.keywordsDict
        self.setKeywords()
        self.language       = bunch.language
        self.mode           = bunch.mode
        self.rulesDict      = bunch.rulesDict
        self.rulesetName    = bunch.rulesetName
        
        # g.trace(self.rulesetName)
    #@nonl
    #@-node:ekr.20060703110708:initModeFromBunch
    #@+node:ekr.20060703090759:push/popDelegate
    def pushDelegate (self,delegate):
        
        delegate = delegate.lower()
        g.trace(delegate,g.callers(3))
        # This should not be necessary.
        for bunch in self.modeStack:
            if bunch.rulesetName == self.modeBunch.rulesetName:
                g.trace('already on stack',delegate)
                return False
        self.modeStack.append(self.modeBunch)
        ok = self.init_mode(self.language,delegate)
        return ok
    
    def popDelegate (self):
        
        g.trace()
        if self.modeStack:
            bunch = self.modeStack.pop()
            self.initModeFromBunch(bunch)
    #@nonl
    #@-node:ekr.20060703090759:push/popDelegate
    #@-node:ekr.20060530091119.9:init_mode & helpers
    #@-node:ekr.20060530091119.35:Birth and init
    #@+node:ekr.20060530091119.38:Entry points
    #@+node:ekr.20060530091119.11:colorize
    def colorize(self,p,incremental=False):
        
        '''The main colorizer entry point.'''
        
        self.count += 1 # For unit testing.
        
        if self.trace:
            g.trace(self.count,g.callers())
            
        self.interrupt() # New in 4.4.1
    
        if self.enabled:
            self.updateSyntaxColorer(p)
            val = self.colorizeAnyLanguage(p)
            if self.trace: g.trace('done')
            return val
        else:
            return "ok" # For unit testing.
    #@nonl
    #@-node:ekr.20060530091119.11:colorize
    #@+node:ekr.20060530091119.39:enable & disable
    def disable (self):
    
        print "disabling all syntax coloring"
        self.enabled=False
        
    def enable (self):
        self.enabled=True
    #@nonl
    #@-node:ekr.20060530091119.39:enable & disable
    #@+node:ekr.20060530091119.10:interrupt
    # This is needed, even without threads.
    
    def interrupt(self):
        
        '''Interrupt colorOneChunk'''
    
        self.chunk_s = ''
        self.chunk_i = 0
        self.tagList = []
        self.chunks_done = True
        if self.trace: g.trace('%3d' % (self.chunk_count))
    #@nonl
    #@-node:ekr.20060530091119.10:interrupt
    #@+node:ekr.20060530091119.41:recolor_all (rewrite)
    def recolor_all (self):
        
        g.trace()
    
        # This code is executed only if graphics characters will be inserted by user markup code.
        
        # Pass 1:  Insert all graphics characters.
        self.removeAllImages()
        s = self.body.getAllText()
        lines = s.split('\n')
        
        self.color_pass = 1
        self.line_index = 1
        state = self.setFirstLineState()
        for s in lines:
            state = self.colorizeLine(s,state)
            self.line_index += 1
        
        # Pass 2: Insert one blank for each previously inserted graphic.
        self.color_pass = 2
        self.line_index = 1
        state = self.setFirstLineState()
        for s in lines:
            #@        << kludge: insert a blank in s for every image in the line >>
            #@+node:ekr.20060530091119.42:<< kludge: insert a blank in s for every image in the line >>
            #@+at 
            #@nonl
            # A spectacular kludge.
            # 
            # Images take up a real index, yet the get routine does not return 
            # any character for them!
            # In order to keep the colorer in synch, we must insert dummy 
            # blanks in s at the positions corresponding to each image.
            #@-at
            #@@c
            
            inserted = 0
            
            for photo,image,line_index,i in self.image_references:
                if self.line_index == line_index:
                    n = i+inserted ; 	inserted += 1
                    s = s[:n] + ' ' + s[n:]
            #@-node:ekr.20060530091119.42:<< kludge: insert a blank in s for every image in the line >>
            #@nl
            state = self.colorizeLine(s,state)
            self.line_index += 1
    #@nonl
    #@-node:ekr.20060530091119.41:recolor_all (rewrite)
    #@+node:ekr.20060530091119.43:schedule & recolor_range
    # Called by body.recolor.
    
    def schedule(self,p,incremental=0):
        
        __pychecker__ = '--no-argsused' # incremental not used.
        
        self.colorize(p)
        
    def recolor_range(self,p,leading,trailing):
        
        '''An entry point for the colorer called from incremental undo code.
        Colorizes the lines between the leading and trailing lines.'''
        
        __pychecker__ = '--no-argsused' # leading,trailing not used.
        
        return self.colorize(p)
    #@nonl
    #@-node:ekr.20060530091119.43:schedule & recolor_range
    #@+node:ekr.20060530091119.44:useSyntaxColoring
    def useSyntaxColoring (self,p):
        
        """Return True unless p is unambiguously under the control of @nocolor."""
        
        p = p.copy() ; first = p.copy()
        val = True ; self.killcolorFlag = False
        for p in p.self_and_parents_iter():
            s = p.v.t.bodyString
            theDict = g.get_directives_dict(s)
            no_color = theDict.has_key("nocolor")
            color = theDict.has_key("color")
            kill_color = theDict.has_key("killcolor")
            # A killcolor anywhere disables coloring.
            if kill_color:
                val = False ; self.killcolorFlag = True ; break
            # A color anywhere in the target enables coloring.
            if color and p == first:
                val = True ; break
            # Otherwise, the @nocolor specification must be unambiguous.
            elif no_color and not color:
                val = False ; break
            elif color and not no_color:
                val = True ; break
    
        # g.trace(first.headString(),val)
        return val
    #@nonl
    #@-node:ekr.20060530091119.44:useSyntaxColoring
    #@+node:ekr.20060530091119.45:updateSyntaxColorer
    def updateSyntaxColorer (self,p):
    
        p = p.copy()
    
        # self.flag is True unless an unambiguous @nocolor is seen.
        self.flag = self.useSyntaxColoring(p)
        self.scanColorDirectives(p)
    #@nonl
    #@-node:ekr.20060530091119.45:updateSyntaxColorer
    #@-node:ekr.20060530091119.38:Entry points
    #@+node:ekr.20060530091119.46:Colorizer code
    #@+node:ekr.20060530091119.12:colorAll
    def colorAll(self,s):
        
        '''Colorize all of s.'''
    
        # Init ivars used by colorOneChunk.
        self.chunk_s = s
        self.chunk_i = 0
        self.tagList = []
        self.chunk_count = 0
        self.recolor_count = 0 # Number of times through the loop before a recolor.
        self.chunks_done = False
        self.quickColor()
        self.colorOneChunk()
        return 'break'
    #@nonl
    #@-node:ekr.20060530091119.12:colorAll
    #@+node:ekr.20060530091119.47:colorizeAnyLanguage
    def colorizeAnyLanguage (self,p,leading=None,trailing=None):
        
        '''Color the body pane.  All coloring starts here.'''
    
        self.init_mode(self.language)
        self.configure_variable_tags()
        if self.killcolorFlag or not self.mode:
            self.removeAllTags() ; return
        try:
            c = self.c ; self.p = p
            self.redoColoring = False
            self.redoingColoring = False
            g.doHook("init-color-markup",colorer=self,p=self.p,v=self.p)
            s = self.body.getAllText()
            self.colorAll(s)
            if 0:
                if self.redoColoring: # Set only from plugins.
                    self.recolor_all()
            return "ok" # for unit testing.
        except Exception:
            g.es_exception()
            return "error" # for unit testing.
    #@nonl
    #@-node:ekr.20060530091119.47:colorizeAnyLanguage
    #@+node:ekr.20060530091119.13:colorOneChunk
    def colorOneChunk (self):
        '''Colorize a limited number of tokens.
        If not done, queue this method again to continue coloring later.'''
        if self.chunks_done: return
        s, i = self.chunk_s, self.chunk_i
        limit = self.interrupt_count1 # Number of times through the loop before a pause. 10 is reasonable.
        limit2 = self.interrupt_count2 # Number of times throught the loop before a recolor. 5000 is reasonable.
        w = self.c.frame.body.bodyCtrl
        count = 0 ; self.chunk_count += 1
        while i < len(s):
            count += 1 ; self.recolor_count += 1
            if self.recolor_count > limit2 > 0:
                self.recolor_count, self.chunk_s, self.chunk_i = 0, s, i
                self.tagAll()
                w.after(50,self.colorOneChunk)
                return 'break'
            if count >= limit:
                self.chunk_s, self.chunk_i = s, i
                w.after_idle(self.colorOneChunk)
                return 'break'
            for f in self.rulesDict.get(s[i],[]):
                # g.trace(f.__name__)
                n = f(self,s,i)
                if n > 0:
                    i += n ; break
            else: i += 1
    
        self.removeAllTags()
        self.tagAll()
        self.tagList = []
        self.chunks_done = True # Prohibit any more queued calls.
        return 'break'
    #@-node:ekr.20060530091119.13:colorOneChunk
    #@+node:ekr.20060530091119.48:colorRangeWithTag
    def colorRangeWithTag (self,s,i,j,tag,delegate=''):
    
        '''Add an item to the tagList if colorizing is enabled.'''
        
        # toGuiIndex could be slow for large s.
        if not self.flag: return
        
        # Color the range, even if there is a delegate.
        w = self.body.bodyCtrl 
        x1 = g.app.gui.toGuiIndex(s,w,i)
        x2 = g.app.gui.toGuiIndex(s,w,j)
        self.tagList.append((tag,x1,x2),)
        if 1:
            if tag != 'blank':
                if delegate:
                    g.trace(delegate,tag,i,j,repr(s[i:j]))
                else:
                    g.trace(tag,i,j,len(self.tagList)/3)
        
        if delegate:
            ok = self.pushDelegate(delegate)
            if ok:
                # Similar logic as colorOneChunk, but we color everything at once.
                # We must use the same indices here as in the caller.
                while i < j:
                    for f in self.rulesDict.get(s[i],[]):
                        n = f(self,s,i)
                        if n > 0:
                            # g.trace(n > 0,i,f.__name__)
                            i += n ; break
                    else: i += 1
                self.popDelegate()
    #@nonl
    #@-node:ekr.20060530091119.48:colorRangeWithTag
    #@+node:ekr.20060530091119.14:quickColor
    def quickColor (self):
        
        '''Give the inserted character the previous color tag by default.'''
        
        w = self.c.frame.body.bodyCtrl
        i = w.index('insert-1c')
        if i == '1.0': return # No previous character.
        if w.tag_names(i): return # The character already has a color.
        j = w.index('insert-2c')
        theList = w.tag_names(j)
        if theList:
            w.tag_add(theList[0],i)
    #@nonl
    #@-node:ekr.20060530091119.14:quickColor
    #@-node:ekr.20060530091119.46:Colorizer code
    #@+node:ekr.20060530091119.49:jEdit matchers (todo: exclude_match)
    #@@nocolor
    #@+at
    # 
    # The following jEdit matcher methods return the length of the matched 
    # text if the
    # match succeeds, and zero otherwise.  In most cases, these methods 
    # colorize all the matched text.
    # 
    # The following arguments affect matching:
    # 
    # - at_line_start         True: sequence must start the line.
    # - at_whitespace_end     True: sequence must be first non-whitespace text 
    # of the line.
    # - at_word_start         True: sequence must start a word.
    # - hash_char             The first character that must match in a regular 
    # expression.
    # - no_escape:            True: ignore an 'end' string if it is preceded 
    # by the ruleset's escape character.
    # - no_line_break         True: the match will not succeed across line 
    # breaks.
    # - no_word_break:        True: the match will not cross word breaks.
    # 
    # The following arguments affect coloring when a match succeeds.
    # - delegate              A ruleset name. The matched text will be colored 
    # recursively by the indicated ruleset.
    # - exclude_match         If True, the actual text that matched will not 
    # be colored.
    # - kind                  The color tag to be applied to colored text.
    #@-at
    #@@c
    #@@color
    #@+node:ekr.20060530091119.17:match_keywords
    # This is a time-critical method.
    def match_keywords (self,s,i):
        
        '''Succeed if s[i:] is a keyword.'''
        
        # We must be at the start of a word.
        if i > 0 and s[i-1] in self.word_chars:
            return 0
    
        # Get the word as quickly as possible.
        j = i ; n = len(s) ; w = self.word_chars
        while j < n and s[j] in w:
            j += 1
            
        word = s[i:j]
        kind = self.keywordsDict.get(s[i:j])
        if kind:
            # g.trace('%3d %10s %s' % (i,word,repr(kind)))
            self.colorRangeWithTag(s,i,j,kind)
            self.prev = (i,j,kind)
            return j-i
        else:
            return 0
    #@nonl
    #@-node:ekr.20060530091119.17:match_keywords
    #@+node:ekr.20060530091119.50:match_regexp_helper
    def match_regexp_helper (self,s,i,pattern):
    
        '''Return the length of the matching text if seq (a regular expression) matches the present position.'''
        
        if trace_match: g.trace(pattern)
    
        try:
            flags = re.MULTILINE
            if self.ignore_case: flags|= re.IGNORECASE
            re_obj = re.compile(pattern,flags)
        except Exception:
            g.es('Invalid regular expression: %s' % (pattern),color='blue')
            return 0
    
        self.match_obj = mo = re_obj.search(s,i)
    
        if mo is None:
            return 0
        else:
            start, end = mo.start(), mo.end()
            g.trace('match: %s' % repr(s[start: end]))
            # g.trace('groups',mo.groups())
            return end - start
    #@nonl
    #@-node:ekr.20060530091119.50:match_regexp_helper
    #@+node:ekr.20060530091119.51:match_eol_span
    def match_eol_span (self,s,i,
        kind=None,seq='',
        at_line_start=False,at_whitespace_end=False,at_word_start=False,
        delegate='',exclude_match=False):
        
        '''Succeed if seq matches s[i:]'''
        
        if trace_match: g.trace()
    
        if at_line_start and i != 0 and s[i-1] != '\n': return 0
        if at_whitespace_end and i != g.skip_ws(s,0): return 0
        if at_word_start and i > 0 and s[i-1] not in self.word_chars: return 0
        
        # g.trace(i,repr(s[i]),repr(seq))
    
        if g.match(s,i,seq):
            j = g.skip_to_end_of_line(s,i)
            self.colorRangeWithTag(s,i,j,kind,delegate=delegate)
            self.prev = (i,j,kind)
            return j - i 
        else:
            return 0
    #@-node:ekr.20060530091119.51:match_eol_span
    #@+node:ekr.20060530091119.52:match_eol_span_regexp
    def match_eol_span_regexp (self,s,i,
        kind='',regexp='',hash_char='',
        at_line_start=False,at_whitespace_end=False,at_word_start=False,
        delegate='',exclude_match=False):
        
        '''Succeed if the regular expression regex matches s[i:].'''
        
        if trace_match: g.trace()
    
        if at_line_start and i != 0 and s[i-1] != '\n': return 0
        if at_whitespace_end and i != g.skip_ws(s,0): return 0
        if at_word_start and i > 0 and s[i-1] not in self.word_chars: return 0
        
        # Test hash_char first to increase speed.
        if i < len(s) and s[i] == hash_char:
            n = self.match_regexp_helper(s,i,regexp)
            if n > 0:
                j = g.skip_to_end_of_line(s,i)
                self.colorRangeWithTag(s,i,j,kind,delegate=delegate)
                self.prev = (i,j,kind)
                return j - i
            else:
                return 0
        else:
            return 0
    #@nonl
    #@-node:ekr.20060530091119.52:match_eol_span_regexp
    #@+node:ekr.20060530091119.53:match_mark_following
    def match_mark_following (self,s,i,
        kind='',pattern='',
        at_line_start=False,at_whitespace_end=False,at_word_start=False,
        exclude_match=False):
        
        '''Succeed if s[i:] matches pattern.'''
        
        if trace_match: g.trace()
    
        if at_line_start and i != 0 and s[i-1] != '\n': return 0
        if at_whitespace_end and i != g.skip_ws(s,0): return 0
        if at_word_start and i > 0 and s[i-1] not in self.word_chars: return 0
    
        if g.match(s,i,pattern):
            j = i + len(pattern)
            self.colorRangeWithTag(s,i,j,kind)
            self.prev = (i,j,kind)
            return j - i
        else:
            return 0
    #@-node:ekr.20060530091119.53:match_mark_following
    #@+node:ekr.20060530091119.54:match_mark_previous
    def match_mark_previous (self,s,i,
        kind='',pattern='',
        at_line_start=False,at_whitespace_end=False,at_word_start=False,
        exclude_match=False):
        
        '''Return the length of a matched SEQ or 0 if no match.
    
        'at_line_start':    True: sequence must start the line.
        'at_whitespace_end':True: sequence must be first non-whitespace text of the line.
        'at_word_start':    True: sequence must start a word.'''
        
        if trace_match: g.trace()
    
        if at_line_start and i != 0 and s[i-1] != '\n': return 0
        if at_whitespace_end and i != g.skip_ws(s,0): return 0
        if at_word_start and i > 0 and s[i-1] not in self.word_chars: return 0
    
        if g.match(s,i,pattern):
            j = i + len(pattern)
            self.colorRangeWithTag(s,i,j,kind)
            self.prev = (i,j,kind)
            return j - i
        else:
            return 0
    #@nonl
    #@-node:ekr.20060530091119.54:match_mark_previous
    #@+node:ekr.20060530091119.55:match_seq
    def match_seq (self,s,i,
        kind='',seq='',
        at_line_start=False,at_whitespace_end=False,at_word_start=False,
        delegate=''):
        
        '''Succeed if s[:] mathces seq.'''
    
        if at_line_start and i != 0 and s[i-1] != '\n': return 0
        if at_whitespace_end and i != g.skip_ws(s,0): return 0
        if at_word_start and i > 0 and s[i-1] not in self.word_chars: return 0
        
        if g.match(s,i,seq):
            j = i + len(seq)
            self.colorRangeWithTag(s,i,j,kind,delegate=delegate)
            self.prev = (i,j,kind)
            return j - i
        else:
            return 0
    #@nonl
    #@-node:ekr.20060530091119.55:match_seq
    #@+node:ekr.20060530091119.56:match_seq_regexp
    def match_seq_regexp (self,s,i,
        kind='',regexp='',hash_char='',
        at_line_start=False,at_whitespace_end=False,at_word_start=False,
        delegate=''):
        
        '''Succeed if the regular expression regexp matches at s[i:].'''
        
        if trace_match: g.trace()
    
        if at_line_start and i != 0 and s[i-1] != '\n': return 0
        if at_whitespace_end and i != g.skip_ws(s,0): return 0
        if at_word_start and i > 0 and s[i-1] not in self.word_chars: return 0
        
        # Test hash_char first to increase speed.
        if i < len(s) and s[i] == hash_char:
            j = self.match_regexp_helper(s,i,regexp)
            self.colorRangeWithTag(s,i,j,kind,delegate=delegate)
            self.prev = (i,j,kind)
        else:
            return 0
    #@nonl
    #@-node:ekr.20060530091119.56:match_seq_regexp
    #@+node:ekr.20060530091119.57:match_span
    def match_span (self,s,i,
        kind='',begin='',end='',
        at_line_start=False,at_whitespace_end=False,at_word_start=False,
        delegate='',exclude_match=False,
        no_escape=False,no_line_break=False,no_word_break=False):
    
        '''Succeed if s[i:] starts with 'begin' and contains a following 'end'.'''
        
        if trace_match: g.trace()
        
        if at_line_start and i != 0 and s[i-1] != '\n': return 0
        if at_whitespace_end and i != g.skip_ws(s,0): return 0
        if at_word_start and i > 0 and s[i-1] not in self.word_chars: return 0
    
        if g.match(s,i,begin):
            j = s.find(end,i+len(begin))
            if j == -1 or no_line_break and '\n' in s[i:j]:
                return 0
            else:
                j += len(end)
                # g.trace(i,j,s[i:j],kind,no_line_break)
                self.colorRangeWithTag(s,i,j,kind,delegate=delegate)
                self.prev = (i,j,kind)
                return j - i
        else:
            return 0
    #@nonl
    #@-node:ekr.20060530091119.57:match_span
    #@+node:ekr.20060530091119.58:match_span_regexp
    def match_span_regexp (self,s,i,
        kind='',begin='',end='',hash_char='',
        at_line_start=False,at_whitespace_end=False,at_word_start=False,
        delegate='',exclude_match=False,
        no_escape=False,no_line_break=False, no_word_break=False,
    ):
            
        '''Succeed if s[i:] starts with 'begin' ( a regular expression) and contains a following 'end'.'''
        
        if trace_match: g.trace('begin',repr(begin),'end',repr(end),'hash_char',repr(hash_char))
        
        if at_line_start and i != 0 and s[i-1] != '\n': return 0
        if at_whitespace_end and i != g.skip_ws(s,0): return 0
        if at_word_start and i > 0 and s[i-1] not in self.word_chars: return 0
        
        # Test hash_char first to increase speed.
        if i < len(s) and s[i] == hash_char:
            n = self.match_regexp_helper(s,i,begin)
            # We may have to allow $n here, in which case we must use a regex object?
            if n > 0 and g.match(s,i+n,end):
                g.trace('found',i,j,kind,delegate)
                self.colorRangeWithTag(s,i,j,kind,delegate=delegate)
                self.prev = (i,j,kind)
                return n + len(end)
        else:
            return 0
    #@nonl
    #@-node:ekr.20060530091119.58:match_span_regexp
    #@-node:ekr.20060530091119.49:jEdit matchers (todo: exclude_match)
    #@+node:ekr.20060530091119.59:Utils
    #@+at 
    #@nonl
    # These methods are like the corresponding functions in leoGlobals.py 
    # except they issue no error messages.
    #@-at
    #@+node:ekr.20060530091119.60:computeRulesetName
    def computeRulesetName (self,language,delegate=None):
    
        return self.munge('%s_%s' % (language,delegate or 'main'))
    #@nonl
    #@-node:ekr.20060530091119.60:computeRulesetName
    #@+node:ekr.20060530091119.61:index
    def index (self,i):
        
        return self.body.convertRowColumnToIndex(self.line_index,i)
        
    #@nonl
    #@-node:ekr.20060530091119.61:index
    #@+node:ekr.20060703120853:munge
    def munge(self,s):
        
        '''Munge a mode name so that it is a valid python id.'''
        
        valid = string.ascii_letters + string.digits + '_'
        
        return ''.join([g.choose(ch in valid,ch.lower(),'_') for ch in s])
    #@nonl
    #@-node:ekr.20060703120853:munge
    #@+node:ekr.20060530091119.62:removeAllImages
    def removeAllImages (self):
        
        for photo,image,line_index,i in self.image_references:
            try:
                self.body.deleteCharacter(image)
            except:
                pass # The image may have been deleted earlier.
        
        self.image_references = []
    #@nonl
    #@-node:ekr.20060530091119.62:removeAllImages
    #@+node:ekr.20060530091119.63:removeAllTags
    def removeAllTags (self):
        
        # g.trace(len(self.tagList)/3)
        
        w = self.c.frame.body.bodyCtrl
        names = w.tag_names()
        for name in names:
            if name not in ('sel','insert'):
                theList = w.tag_ranges(name)
                if theList:
                    n = len(theList) ; i = 0
                    while i < n:
                        w.tag_remove(name,theList[i],theList[i+1])
                        i += 2
    #@nonl
    #@-node:ekr.20060530091119.63:removeAllTags
    #@+node:ekr.20060530091119.64:scanColorDirectives
    def scanColorDirectives(self,p):
        
        """Scan position p and p's ancestors looking for @comment, @language and @root directives,
        setting corresponding colorizer ivars.
        """
    
        p = p.copy() ; c = self.c
        if c == None: return # self.c may be None for testing.
    
        self.language = language = c.target_language
        self.comment_string = None
        self.rootMode = None # None, "code" or "doc"
        
        for p in p.self_and_parents_iter():
            # g.trace(p)
            s = p.v.t.bodyString
            theDict = g.get_directives_dict(s)
            #@        << Test for @comment or @language >>
            #@+node:ekr.20060530091119.65:<< Test for @comment or @language >>
            # @comment and @language may coexist in the same node.
            
            if theDict.has_key("comment"):
                k = theDict["comment"]
                self.comment_string = s[k:]
            
            if theDict.has_key("language"):
                i = theDict["language"]
                language,junk,junk,junk = g.set_language(s,i)
                self.language = language
            
            if theDict.has_key("comment") or theDict.has_key("language"):
                break
            #@nonl
            #@-node:ekr.20060530091119.65:<< Test for @comment or @language >>
            #@nl
            #@        << Test for @root, @root-doc or @root-code >>
            #@+node:ekr.20060530091119.66:<< Test for @root, @root-doc or @root-code >>
            if theDict.has_key("root") and not self.rootMode:
            
                k = theDict["root"]
                if g.match_word(s,k,"@root-code"):
                    self.rootMode = "code"
                elif g.match_word(s,k,"@root-doc"):
                    self.rootMode = "doc"
                else:
                    doc = c.config.at_root_bodies_start_in_doc_mode
                    self.rootMode = g.choose(doc,"doc","code")
            #@nonl
            #@-node:ekr.20060530091119.66:<< Test for @root, @root-doc or @root-code >>
            #@nl
    
        return self.language # For use by external routines.
    #@nonl
    #@-node:ekr.20060530091119.64:scanColorDirectives
    #@+node:ekr.20060530091119.67:setFontFromConfig
    def setFontFromConfig (self):
        
        c = self.c
        
        self.bold_font = c.config.getFontFromParams(
            "body_text_font_family", "body_text_font_size",
            "body_text_font_slant",  "body_text_font_weight",
            c.config.defaultBodyFontSize) # , tag = "colorer bold")
        
        if self.bold_font:
            self.bold_font.configure(weight="bold")
        
        self.italic_font = c.config.getFontFromParams(
            "body_text_font_family", "body_text_font_size",
            "body_text_font_slant",  "body_text_font_weight",
            c.config.defaultBodyFontSize) # , tag = "colorer italic")
            
        if self.italic_font:
            self.italic_font.configure(slant="italic",weight="normal")
        
        self.bolditalic_font = c.config.getFontFromParams(
            "body_text_font_family", "body_text_font_size",
            "body_text_font_slant",  "body_text_font_weight",
            c.config.defaultBodyFontSize) # , tag = "colorer bold italic")
            
        if self.bolditalic_font:
            self.bolditalic_font.configure(weight="bold",slant="italic")
            
        self.color_tags_list = []
        self.image_references = []
    #@nonl
    #@-node:ekr.20060530091119.67:setFontFromConfig
    #@+node:ekr.20060530091119.19:tagAll
    def tagAll (self):
        
        # g.trace(len(self.tagList)/3)
        
        w = self.body ; tags = w.tag_names()
        
        for tag,x1,x2 in self.tagList:
            # Remove any old tags from the range.
            for tag2 in tags:
                w.tag_remove(tag2,x1,x2)
                
            # Add the new tag.
            w.tag_add(tag,x1,x2)
    #@nonl
    #@-node:ekr.20060530091119.19:tagAll
    #@-node:ekr.20060530091119.59:Utils
    #@-others

class colorizer (baseColorizer):
    pass
#@nonl
#@-node:ekr.20060530091119.34:class colorizer (baseColorizer)
#@-others

#@<< class nullColorizer (colorizer) >>
#@+node:ekr.20060530091119.68:<< class nullColorizer (colorizer) >>
class nullColorizer (colorizer):
    
    """A do-nothing colorer class"""
    
    #@    @+others
    #@+node:ekr.20060530091119.69:__init__
    def __init__ (self,c):
        
        colorizer.__init__(self,c) # init the base class.
    
        self.c = c
        self.enabled = False
    #@-node:ekr.20060530091119.69:__init__
    #@+node:ekr.20060530091119.70:entry points
    def colorize(self,p,incremental=False): pass
    
    def disable(self): pass
        
    def enable(self): pass
            
    def recolor_range(self,p,leading,trailing): pass
    
    def scanColorDirectives(self,p): pass
        
    def schedule(self,p,incremental=0): pass
    
    def updateSyntaxColorer (self,p): pass
    #@nonl
    #@-node:ekr.20060530091119.70:entry points
    #@-others
#@nonl
#@-node:ekr.20060530091119.68:<< class nullColorizer (colorizer) >>
#@nl
#@nonl
#@-node:ekr.20060530091119.20:@thin __jEdit_colorizer__.py
#@-leo
