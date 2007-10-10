#@+leo-ver=4-thin
#@+node:ekr.20070718094819:@thin threading_colorizer.py	
'''A threading colorizer using jEdit language description files.

See: http://webpages.charter.net/edreamleo/coloring.html for documentation.
'''

#@@language python
#@@tabwidth -4
#@@pagewidth 80

__version__ = '0.5'

trace_all_matches = False
trace_leo_matches = False

#@<< imports >>
#@+node:ekr.20070718131458.1:<< imports >>
import leoGlobals as g
import leoPlugins

import os
import re
import string
import threading
import traceback
import xml.sax
import xml.sax.saxutils

# php_re = re.compile("<?(\s|=|[pP][hH][pP])")
php_re = re.compile("<?(\s[pP][hH][pP])")
#@nonl
#@-node:ekr.20070718131458.1:<< imports >>
#@nl
#@<< version history >>
#@+node:ekr.20070718100326.1:<< version history >>
#@@nocolor
#@+at
# 
# 0.1 EKR: Initial version based on code in test.leo.
# 0.2 EKR: Do not restore the selection range or insert point: it messes 
# things up.
# 0.3 EKR: A rewrite of the incremental coloring logic.
# 0.4 EKR: Minor changes.
# 0.5 EKR: Several optimizations, of unknown real value:
# - Minimize the time spent in critical sections.
# - Process only 'limit' items in finishColoring.
# - finishColoring now returns a 'done' indicator, and idleHandler
#   re-queues itself if more work remains.
#@-at
#@nonl
#@-node:ekr.20070718100326.1:<< version history >>
#@nl
#@<< define leoKeywordsDict >>
#@+node:ekr.20070725161027:<< define leoKeywordsDict >>
leoKeywordsDict = {}

for key in g.globalDirectiveList:
    leoKeywordsDict [key] = 'leoKeyword'
#@nonl
#@-node:ekr.20070725161027:<< define leoKeywordsDict >>
#@nl
#@<< define default_colors_dict >>
#@+node:ekr.20070718131458.7:<< define default_colors_dict >>
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
    'markup'    :('markup_color',   'red'),
    'null'      :('null_color',     'black'),
    'operator'  :('operator_color', 'black'),
    }
#@nonl
#@-node:ekr.20070718131458.7:<< define default_colors_dict >>
#@nl
#@<< define default_font_dict >>
#@+node:ekr.20070718131458.8:<< define default_font_dict >>
default_font_dict = {
    # tag name       : option name
    'comment'        :'comment_font',
    'cwebName'       :'cweb_section_name_font',
    'pp'             :'directive_font',
    'docPart'        :'doc_part_font',
    'keyword'        :'keyword_font',
    'leoKeyword'     :'leo_keyword_font',
    'link'           :'section_name_font',
    'nameBrackets'   :'section_name_brackets_font',
    'string'         :'string_font',
    'name'           :'undefined_section_name_font',
    'latexBackground':'latex_background_font',

    # jEdit tags.
    'comment1'  :'comment1_font',
    'comment2'  :'comment2_font',
    'comment3'  :'comment3_font',
    'comment4'  :'comment4_font',
    'function'  :'function_font',
    'keyword1'  :'keyword1_font',
    'keyword2'  :'keyword2_font',
    'keyword3'  :'keyword3_font',
    'keyword4'  :'keyword4_font',
    'label'     :'label_font',
    'literal1'  :'literal1_font',
    'literal2'  :'literal2_font',
    'literal3'  :'literal3_font',
    'literal4'  :'literal4_font',
    'markup'    :'markup_font',
    # 'nocolor' This tag is used, but never generates code.
    'null'      :'null_font',
    'operator'  :'operator_font',
    }
#@nonl
#@-node:ekr.20070718131458.8:<< define default_font_dict >>
#@nl

#@+others
#@+node:ekr.20070718131458.5:module-level
#@+node:ekr.20070718131458.9:init
def init ():

    leoPlugins.registerHandler('start1',onStart1)
    g.plugin_signon(__name__)

    return True
#@nonl
#@-node:ekr.20070718131458.9:init
#@+node:ekr.20070718131458.10:onStart1
def onStart1 (tag, keywords):

    '''Override Leo's core colorizer classes.'''

    import leoColor
    leoColor.colorizer = colorizer
    leoColor.nullColorizer = nullColorizer
#@-node:ekr.20070718131458.10:onStart1
#@+node:ekr.20070718131458.11:Leo rule functions (in helper thread)
#@+at
# These rule functions recognize noweb syntactic constructions. These are 
# treated
# just like rule functions, so they are module-level objects whose first 
# argument
# is 'self'.
#@-at
#@@c

#@+node:ekr.20070718131458.12:match_at_color
def match_at_color (self,s,i):

    if trace_leo_matches: g.trace()

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
#@-node:ekr.20070718131458.12:match_at_color
#@+node:ekr.20070718131458.13:match_at_nocolor
def match_at_nocolor (self,s,i):

    if trace_leo_matches: g.trace()

    if i != 0 and s[i-1] != '\n':
        return 0
    if not g.match_word(s,i,'@nocolor'):
        return 0

    j = i + len('@nocolor')
    k = s.find('\n@color',j)
    if k == -1:
        # No later @color: don't color the @nocolor directive.
        self.flag = False # Disable coloring.
        return len(s) - j
    else:
        # A later @color: do color the @nocolor directive.
        self.colorRangeWithTag(s,i,j,'leoKeyword')
        self.flag = False # Disable coloring.
        return k+1-j

#@-node:ekr.20070718131458.13:match_at_nocolor
#@+node:ekr.20070718131458.14:match_doc_part
def match_doc_part (self,s,i):

    if g.match_word(s,i,'@doc'):
        j = i+4
        self.colorRangeWithTag(s,i,j,'leoKeyword')
    elif g.match(s,i,'@') and (i+1 >= len(s) or s[i+1] in (' ','\t','\n')):
        j = i + 1
        self.colorRangeWithTag(s,i,j,'leoKeyword')
    else: return 0

    i = j ; n = len(s)
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
#@-node:ekr.20070718131458.14:match_doc_part
#@+node:ekr.20070718131458.15:match_leo_keywords
def match_leo_keywords(self,s,i):

    '''Succeed if s[i:] is a Leo keyword.'''

    # We must be at the start of a word.
    if i > 0 and s[i-1] in self.word_chars:
        return 0

    if s[i] != '@':
        return 0

    # Get the word as quickly as possible.
    j = i
    while j < len(s) and s[j] in self.word_chars:
        j += 1

    word = s[i:j]
    # g.trace(i,word,repr(self.word_chars))
    if leoKeywordsDict.get(word):
        kind = 'leoKeyword'
        self.colorRangeWithTag(s,i,j,kind)
        self.prev = (i,j,kind)
        result = j-i
        # g.trace(g.callers(3),'result',result,'i',i,repr(s[i:i+g.choose(result,result,20)]))
        return result
    else:
        return 0
#@nonl
#@-node:ekr.20070718131458.15:match_leo_keywords
#@+node:ekr.20070718131458.16:match_section_ref
def match_section_ref (self,s,i):

    if trace_leo_matches: g.trace()
    c=self.c

    if not g.match(s,i,'<<'):
        return 0
    k = g.find_on_line(s,i+2,'>>')
    if k is not None:
        j = k + 2
        self.colorRangeWithTag(s,i,i+2,'nameBrackets')
        ref = g.findReference(c,s[i:j],self.p)
        if ref:
            if self.use_hyperlinks:
                #@                << set the hyperlink >>
                #@+node:ekr.20070718131458.17:<< set the hyperlink >>
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
                #@-node:ekr.20070718131458.17:<< set the hyperlink >>
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
#@-node:ekr.20070718131458.16:match_section_ref
#@+node:ekr.20070718131458.18:match_blanks
def match_blanks (self,s,i):

    # if trace_leo_matches: g.trace()

    j = i ; n = len(s)

    while j < n and s[j] == ' ':
        j += 1

    if j > i:
        # g.trace(i,j)
        if self.showInvisibles:
            self.colorRangeWithTag(s,i,j,'blank')
        return j - i
    else:
        return 0
#@nonl
#@-node:ekr.20070718131458.18:match_blanks
#@+node:ekr.20070718131458.19:match_tabs
def match_tabs (self,s,i):

    if trace_leo_matches: g.trace()

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
#@-node:ekr.20070718131458.19:match_tabs
#@+node:ekr.20070720161950:match_incomplete_strings
# def match_incomplete_strings (self,s,i):

    # if trace_leo_matches: g.trace()

    # if not g.match(s,i,'"') and not g.match(s,i,"'"):
        # return 0

    # if self.language == 'python' and (g.match(s,i-2,'"""') or g.match(s,i-2,"'''")):
        # return 0 # Do not interfere with docstrings.

    # delim = s[i]
    # j = g.skip_line(s,i)

    # if s.find(delim,i+1,j) == -1:
        # g.trace(repr(s[i:j]))
        # self.colorRangeWithTag(s,i,j,'literal1')
        # return j-i
    # else:
        # return 0
#@-node:ekr.20070720161950:match_incomplete_strings
#@-node:ekr.20070718131458.11:Leo rule functions (in helper thread)
#@-node:ekr.20070718131458.5:module-level
#@+node:ekr.20070718131458.20:class colorizer
class colorizer:

    #@    @+others
    #@+node:ekr.20070718131458.21:Birth and init
    #@+node:ekr.20070718131458.22:__init__
    def __init__(self,c):
        # Copies of ivars.
        self.c = c
        self.frame = c.frame
        self.body = c.frame.body
        self.p = None
        self.w = self.body.bodyCtrl
        # Attributes dict ivars: defaults are as shown.
        self.default = 'null'
        self.digit_re = ''
        self.escape = ''
        self.highlight_digits = True
        self.ignore_case = True
        self.no_word_sep = ''
        # Config settings.
        self.comment_string = None # Set by scanColorDirectives on @comment
        self.showInvisibles = False # True: show "invisible" characters.
        self.underline_undefined = c.config.getBool("underline_undefined_section_names")
        self.use_hyperlinks = c.config.getBool("use_hyperlinks")
        self.enabled = c.config.getBool('use_syntax_coloring')
        # Debugging.
        self.lock_trace = False
        self.trace = False or c.config.getBool('trace_colorizer')
        self.trace_match_flag = False
        self.use_threads = True
        # State ivars...
        self.count = 0
        self.comment_string = None # Can be set by @comment directive.
        self.defaultRulesList = []
        self.flag = True # True unless in range of @nocolor
        self.importedRulesets = {}
        self.interruptable = True
        self.language = 'python' # set by scanColorDirectives.
        self.prev = None # The previous token.
        self.ranges = 0
        # Data...
        self.fonts = {} # Keys are config names.  Values are actual fonts.
        self.insertPoint = None
        self.keywords = {} # Keys are keywords, values are 0..5.
        self.modes = {} # Keys are languages, values are modes.
        self.mode = None # The mode object for the present language.
        self.modeBunch = None # A bunch fully describing a mode.
        self.modeStack = []
        self.selection = None
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
        # Incremental data.
        self.end_i = 0 # The ending index of the text that has been colored.
        self.marksDict = {} # Keys are indices of matches, values are lengths of the match.
        self.old_s = None # The previous value of self.s
        self.s = None # The string being colorized.
        self.start_i = 0 # The starting index of the text that has been colored.
        # Threading stuff.
        self.globalTagList = [] # The interface between the helper and main thread.
            # The helper thread puts items on the list.  The main thread removes items.
            # All accesses to this list *must* be protected by self.lock.
        self.lock = threading.Condition()
        self.threadCount = 0
        self.helperThread = None # A singleton helper thread.
        self.killFlag = False
    #@-node:ekr.20070718131458.22:__init__
    #@+node:ekr.20070718131458.23:addImportedRules
    def addImportedRules (self,mode,rulesDict,rulesetName):

        '''Append any imported rules at the end of the rulesets specified in mode.importDict'''

        if self.importedRulesets.get(rulesetName):
            return
        else:
            self.importedRulesets [rulesetName] = True

        names = hasattr(mode,'importDict') and mode.importDict.get(rulesetName,[]) or []

        for name in names:
            savedBunch = self.modeBunch
            ok = self.init_mode(name)
            if ok:
                rulesDict2 = self.rulesDict
                for key in rulesDict2.keys():
                    aList = rulesDict.get(key,[])
                    aList2 = rulesDict2.get(key)
                    if aList2:
                        # Don't add the standard rules again.
                        rules = [z for z in aList2 if z not in aList]
                        if rules:
                            # g.trace([z.__name__ for z in rules])
                            aList.extend(rules)
                            rulesDict [key] = aList
            # g.trace('***** added rules for %s from %s' % (name,rulesetName))
            self.initModeFromBunch(savedBunch)
    #@nonl
    #@-node:ekr.20070718131458.23:addImportedRules
    #@+node:ekr.20070718131458.24:addLeoRules
    def addLeoRules (self,theDict):

        '''Put Leo-specific rules to theList.'''

        for ch, rule, atFront, in (
            # Rules added at front are added in **reverse** order.
            ('@',  match_leo_keywords,True), # Called after all other Leo matchers.
                # Debatable: Leo keywords override langauge keywords.
            ('@',  match_at_color,    True),
            ('@',  match_at_nocolor,  True),
            ('@',  match_doc_part,    True), 
            ('<',  match_section_ref, True), # Called **first**.
            # Rules added at back are added in normal order.
            (' ',  match_blanks,      False),
            ('\t', match_tabs,        False),
            # Python rule 3 appears to work well enough.
            #('"',  match_incomplete_strings, False),
            #("'",  match_incomplete_strings, False),
        ):
            theList = theDict.get(ch,[])
            if atFront:
                theList.insert(0,rule)
            else:
                theList.append(rule)
            theDict [ch] = theList
    #@nonl
    #@-node:ekr.20070718131458.24:addLeoRules
    #@+node:ekr.20070718131458.25:configure_tags
    def configure_tags (self):

        c = self.c ; w = self.w

        # Get the default body font.
        defaultBodyfont = self.fonts.get('default_body_font')
        if not defaultBodyfont:
            defaultBodyfont = c.config.getFontFromParams(
                "body_text_font_family", "body_text_font_size",
                "body_text_font_slant",  "body_text_font_weight",
                c.config.defaultBodyFontSize)
            self.fonts['default_body_font'] = defaultBodyfont

        # Configure fonts.
        keys = default_font_dict.keys() ; keys.sort()
        for key in keys:
            option_name = default_font_dict[key]
            # First, look for the language-specific setting, then the general setting.
            for name in ('%s_%s' % (self.language,option_name),(option_name)):
                font = self.fonts.get(name)
                if font:
                    # g.trace('found',name,id(font))
                    w.tag_config(key,font=font)
                    break
                else:
                    family = c.config.get(name + '_family','family')
                    size   = c.config.get(name + '_size',  'size')   
                    slant  = c.config.get(name + '_slant', 'slant')
                    weight = c.config.get(name + '_weight','weight')
                    if family or slant or weight or size:
                        family = family or g.app.config.defaultFontFamily
                        size   = size or c.config.defaultBodyFontSize
                        slant  = slant or 'roman'
                        weight = weight or 'normal'
                        font = g.app.gui.getFontFromParams(family,size,slant,weight)
                        # Save a reference to the font so it 'sticks'.
                        self.fonts[name] = font 
                        # g.trace(key,name,family,size,slant,weight,id(font))
                        w.tag_config(key,font=font)
                        break
            else: # Neither the general setting nor the language-specific setting exists.
                if self.fonts.keys(): # Restore the default font.
                    # g.trace('default',key)
                    w.tag_config(key,font=defaultBodyfont)

        keys = default_colors_dict.keys() ; keys.sort()
        for name in keys:
            option_name,default_color = default_colors_dict[name]
            color = (
                c.config.getColor('%s_%s' % (self.language,option_name)) or
                c.config.getColor(option_name) or
                default_color
            )
            # g.trace(option_name,color)

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
    #@-node:ekr.20070718131458.25:configure_tags
    #@+node:ekr.20070718131458.26:configure_variable_tags
    def configure_variable_tags (self):

        c = self.c

        # g.trace()

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
    #@-node:ekr.20070718131458.26:configure_variable_tags
    #@+node:ekr.20070718131458.27:init_mode & helpers
    def init_mode (self,name):

        '''Name may be a language name or a delegate name.'''

        if not name: return False
        language,rulesetName = self.nameToRulesetName(name)
        bunch = self.modes.get(rulesetName)
        if bunch:
            # g.trace('found',language,rulesetName)
            self.initModeFromBunch(bunch)
            return True
        else:
            # g.trace('****',language,rulesetName)
            path = g.os_path_join(g.app.loadDir,'..','modes')
            mode = g.importFromPath (language,path)
            if not mode:
                # Create a dummy bunch to limit recursion.
                self.modes [rulesetName] = self.modeBunch = g.Bunch(
                    attributesDict  = {},
                    defaultColor    = None,
                    keywordsDict    = {},
                    language        = language,
                    mode            = mode,
                    properties      = {},
                    rulesDict       = {},
                    rulesetName     = rulesetName)
                # g.trace('No colorizer file: %s.py' % language)
                return False
            self.language = language
            self.rulesetName = rulesetName
            self.properties = hasattr(mode,'properties') and mode.properties or {}
            self.keywordsDict = hasattr(mode,'keywordsDictDict') and mode.keywordsDictDict.get(rulesetName,{}) or {}
            self.setKeywords()
            self.attributesDict = hasattr(mode,'attributesDictDict') and mode.attributesDictDict.get(rulesetName) or {}
            self.setModeAttributes()
            self.rulesDict = hasattr(mode,'rulesDictDict') and mode.rulesDictDict.get(rulesetName) or {}
            self.addLeoRules(self.rulesDict)

            self.defaultColor = 'null'
            self.mode = mode
            self.modes [rulesetName] = self.modeBunch = g.Bunch(
                attributesDict  = self.attributesDict,
                defaultColor    = self.defaultColor,
                keywordsDict    = self.keywordsDict,
                language        = self.language,
                mode            = self.mode,
                properties      = self.properties,
                rulesDict       = self.rulesDict,
                rulesetName     = self.rulesetName)
            # Do this after 'officially' initing the mode, to limit recursion.
            self.addImportedRules(mode,self.rulesDict,rulesetName)
            self.updateDelimsTables()
            return True
    #@nonl
    #@+node:ekr.20070718131458.28:nameToRulesetName
    def nameToRulesetName (self,name):

        '''Compute language and rulesetName from name, which is either a language or a delegate name.'''

        if not name: return ''

        i = name.find('::')
        if i == -1:
            language = name
            rulesetName = '%s_main' % (language)
        else:
            language = name[:i]
            delegate = name[i+2:]
            rulesetName = self.munge('%s_%s' % (language,delegate))

        # g.trace(name,language,rulesetName)
        return language,rulesetName
    #@nonl
    #@-node:ekr.20070718131458.28:nameToRulesetName
    #@+node:ekr.20070718131458.29:setKeywords
    def setKeywords (self):

        '''Initialize the keywords for the present language.

         Set self.word_chars ivar to string.letters + string.digits
         plus any other character appearing in any keyword.'''

        # Add any new user keywords to leoKeywordsDict.
        d = self.keywordsDict
        keys = d.keys()
        for s in g.globalDirectiveList:
            key = '@' + s
            if key not in keys:
                d [key] = 'leoKeyword'

        # Create the word_chars list. 
        self.word_chars = [g.toUnicode(ch,encoding='UTF-8') for ch in (string.letters + string.digits)]
        for key in d.keys():
            for ch in key:
                # if ch == ' ': g.trace('blank in key: %s' % repr (key))
                if ch not in self.word_chars:
                    self.word_chars.append(g.toUnicode(ch,encoding='UTF-8'))

        # jEdit2Py now does this check, so this isn't really needed.
        for ch in (' ', '\t'):
            if ch in self.word_chars:
                g.es_print('removing %s from word_chars' % (repr(ch)))
                self.word_chars.remove(ch)

        # g.trace(len(d.keys()))
    #@nonl
    #@-node:ekr.20070718131458.29:setKeywords
    #@+node:ekr.20070718131458.30:setModeAttributes
    def setModeAttributes (self):

        '''Set the ivars from self.attributesDict,
        converting 'true'/'false' to True and False.'''

        d = self.attributesDict
        aList = (
            ('default',         'null'),
    	    ('digit_re',        ''),
            ('escape',          ''), # New in Leo 4.4.2.
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
    #@-node:ekr.20070718131458.30:setModeAttributes
    #@+node:ekr.20070718131458.31:initModeFromBunch
    def initModeFromBunch (self,bunch):

        self.modeBunch = bunch
        self.attributesDict = bunch.attributesDict
        self.setModeAttributes()
        self.defaultColor   = bunch.defaultColor
        self.keywordsDict   = bunch.keywordsDict
        self.language       = bunch.language
        self.mode           = bunch.mode
        self.properties     = bunch.properties
        self.rulesDict      = bunch.rulesDict
        self.rulesetName    = bunch.rulesetName

        # g.trace(self.rulesetName)
    #@nonl
    #@-node:ekr.20070718131458.31:initModeFromBunch
    #@+node:ekr.20070718131458.32:updateDelimsTables
    def updateDelimsTables (self):

        '''Update g.app.language_delims_dict if no entry for the language exists.'''

        d = self.properties
        lineComment = d.get('lineComment')
        startComment = d.get('commentStart')
        endComment = d.get('commentEnd')

        if lineComment and startComment and endComment:
            delims = '%s %s %s' % (lineComment,startComment,endComment)
        elif startComment and endComment:
            delims = '%s %s' % (startComment,endComment)
        elif lineComment:
            delims = '%s' % lineComment
        else:
            delims = None

        if delims:
            d = g.app.language_delims_dict
            if not d.get(self.language):
                d [self.language] = delims
                # g.trace(self.language,'delims:',repr(delims))
    #@-node:ekr.20070718131458.32:updateDelimsTables
    #@-node:ekr.20070718131458.27:init_mode & helpers
    #@-node:ekr.20070718131458.21:Birth and init
    #@+node:ekr.20070718131458.33:Entry points
    def idleHandler (self,event=None):

        if not self.helpterThread: return
    #@+node:ekr.20070718131458.34:colorize
    def colorize(self,p,incremental=False,interruptable=True):

        '''The main colorizer entry point.'''

        self.count += 1 # For unit testing.

        c = self.c

        if self.enabled:
            self.updateSyntaxColorer(p) # Sets self.flag.
            # g.trace('self.flag',self.flag,'incremental',incremental)
            self.threadColorizer(p,incremental,interruptable)
        else:
            self.removeAllTags()

        return "ok" # For unit testing.
    #@-node:ekr.20070718131458.34:colorize
    #@+node:ekr.20070718131458.35:enable & disable
    def disable (self):

        print "disabling all syntax coloring"
        self.enabled=False

    def enable (self):
        self.enabled=True
    #@nonl
    #@-node:ekr.20070718131458.35:enable & disable
    #@+node:ekr.20071009093328:isSameColorState
    def isSameColorState (self):

        return False

        # g.trace(g.callers())

        def dumpState(state):
            flag,language = state
            return 'flag: %s, %s' % (flag,language)

        if not self.enable:
            # g.trace('returns False')
            return False

        state1 = self.flag,self.language
        language = self.updateSyntaxColorer(self.c.currentPosition()) # Sets self.flag.
        if language is None: language = self.language
        state2 = self.flag,language

        equal = state1 == state2
        # g.trace('=',equal,'state1',dumpState(state1),'state2',dumpState(state2))
        return equal
    #@-node:ekr.20071009093328:isSameColorState
    #@+node:ekr.20070718131458.36:interrupt (does nothing)
    # This is needed, even without threads.

    interrupt_count = 0

    def interrupt(self):

        '''Interrupt colorOneChunk'''

        pass
    #@-node:ekr.20070718131458.36:interrupt (does nothing)
    #@+node:ekr.20070718131458.40:useSyntaxColoring
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
    #@-node:ekr.20070718131458.40:useSyntaxColoring
    #@+node:ekr.20070718131458.41:updateSyntaxColorer
    def updateSyntaxColorer (self,p):

        p = p.copy()

        # self.flag is True unless an unambiguous @nocolor is seen.
        self.flag = self.useSyntaxColoring(p)
        self.scanColorDirectives(p)
    #@nonl
    #@-node:ekr.20070718131458.41:updateSyntaxColorer
    #@-node:ekr.20070718131458.33:Entry points
    #@+node:ekr.20070719111308:Colorers & helpers
    #@+node:ekr.20070720113510:findMarkAtIndex
    def findMarkAtIndex(self,d,i):

        '''Return the higest match that starts strictly before i.
        Return 0 if no such match.'''

        keys = d.keys()
        keys.sort()
        last_i = 0 
        for key in keys:
            if key >= i:
                break
            else:
                last_i = key

        if self.trace: g.trace('*******',last_i)
        return last_i
    #@-node:ekr.20070720113510:findMarkAtIndex
    #@+node:ekr.20070718131458.42:finishColoring
    def finishColoring (self,done):

        c = self.c ; w = self.w
        # if self.killFlag: return

        if self.trace: #  and self.globalTagList:
            g.trace('%d' % self.threadCount,'done',done,'globalTagList',len(self.globalTagList))

        # Critical section: must be as fast as possible.
        limit = 500
        if self.lock_trace: g.trace('lock on',self.threadCount)
        self.lock.acquire()
        try:
            if self.killFlag:
                tagList = []
                self.globalTagList = [] # Bug fix: 10/8/07
            # elif done: # Bug fix: 10/8/07
                # tagList = self.globalTagList[:]
                # self.globalTagList = []
            # elif limit:
                # tagList = self.globalTagList[:limit]
                # self.globalTagList = self.globalTagList[limit:]
            else:
                tagList = self.globalTagList[:]
                self.globalTagList = []
            # Apparently, this must be inside the lock.
            # This *must* be called, even if we are killing the thread.
            self.tagAll(tagList)
            done = len(self.globalTagList) == 0
        finally:
            self.lock.release()

        if self.lock_trace: g.trace('lock off',self.threadCount)

        ### w.update_idletasks()

        return done
    #@-node:ekr.20070718131458.42:finishColoring
    #@+node:ekr.20070718131458.50:idleHandler
    def idleHandler (self,n):

        if not self.use_threads:
            self.finishColoring(done=False)
        elif not self.helperThread or n < self.threadCount:
            return
        elif self.helperThread.isAlive():
            if self.trace: g.trace('*** alive %d' % self.threadCount)
            self.waitCount += 1
            self.finishColoring(done=False)
            # self.w.after_idle(self.idleHandler,n)
            self.w.after(200,self.idleHandler,n)
        else:
            # if self.waitCount: g.trace('waitCount',self.waitCount)
            if 1: # Much better response.
                done = self.finishColoring(done=True)
                if done:
                    if self.trace: g.trace('*** dead  %d' % n)
                else:
                    if self.trace: g.trace('*** dead, not done %d' % n)
                    self.w.after(200,self.idleHandler,n)
            else: # safe, slow
                if self.trace: g.trace('*** dead  %d' % n)
                self.finishColoring(done=True)



    #@-node:ekr.20070718131458.50:idleHandler
    #@+node:ekr.20070718131458.49:init
    def init (self,p,incremental,interruptable):

        self.w = w = self.c.frame.body.bodyCtrl

        self.incremental = incremental
        self.interruptable = interruptable
        self.insertPoint = w.getInsertPoint()  
        self.killFlag = False
        # self.language is set by self.updateSyntaxColorer.
        self.p = p.copy()
        self.s = w.getAllText()
        self.selection = w.getSelectionRange()
        # g.trace('ins',self.insertPoint,'sel',self.selection)
        self.globalTagList = []
        self.prev = None ### Bug fix: 10/3/07
        self.tagsRemoved = False
        self.waitCount = 0

        self.init_mode(self.language)
        self.configure_tags() # Must do this every time to support multiple editors.
    #@-node:ekr.20070718131458.49:init
    #@+node:ekr.20070718131458.43:removeAllImages
    def removeAllImages (self):

        # for photo,image,i in self.image_references:
            # try:
                # w = self.w
                # w.setAllText(w.getAllText())

                # # i = self.index(i)
                # # self.body.deleteCharacter(image)
                # # s = self.allBodyText ; w = self.w
                # # w.delete(s,i)
                # # self.allBodyText = w.getAllText()
            # except:
                # g.es_exception()
                # pass # The image may have been deleted earlier.

        self.image_references = []
    #@-node:ekr.20070718131458.43:removeAllImages
    #@+node:ekr.20070718131458.44:removeAllTags
    def removeAllTags (self):

        w = self.w

        if self.trace: g.trace()
        names = w.tag_names()
        i,j = w.toGuiIndex(0), w.toGuiIndex('end')
        for name in names:
            if name not in ('sel','insert'):
                w.tag_remove(name,i,j)
    #@-node:ekr.20070718131458.44:removeAllTags
    #@+node:ekr.20070720165737:removeTagsFromRange
    def removeTagsFromRange(self,i,j):

        s = self.s ; w = self.w

        if self.trace: g.trace('i',i,'j',j)

        names = [z for z in w.tag_names() if z not in ('sel','insert')]

        x1,x2 = w.toGuiIndex(self.start_i,s=s), w.toGuiIndex(self.end_i,s=s)
        for tag in names:
            # g.trace(tag,x1,x2)
            w.tag_remove(tag,x1,x2)
    #@-node:ekr.20070720165737:removeTagsFromRange
    #@+node:ekr.20070724120821:tag & index (threadingColorizer)
    def index (self,i):

        w = self.w
        x1 = w.toGuiIndex(i)
        # g.trace(i,x1)
        return x1

    def tag (self,name,i,j):

        s = self.s ; w = self.w
        # g.trace(name,i,j,repr(s[i:j]),g.callers())
        x1,x2 = w.toGuiIndex(i,s=s), w.toGuiIndex(j,s=s)
        w.tag_add(name,x1,x2)
    #@-node:ekr.20070724120821:tag & index (threadingColorizer)
    #@+node:ekr.20070718131458.45:tagAll
    def tagAll (self,tagList):

        '''Process all items on the tagList.'''

        s = self.s ; w = self.w ; trace = False

        if (self.trace or trace) and tagList:
            g.trace('len(tagList)',len(tagList),'start:end',self.start_i,self.end_i)

        if self.start_i == self.end_i:
            # self.start_i = self.end_i
            return

        self.removeTagsFromRange(self.start_i,self.end_i)

        if tagList:
            for tag,i,j in tagList:
                x1,x2 = w.toGuiIndex(i,s=s), w.toGuiIndex(j,s=s)
                # A crucial optimization for large body text.
                # Even so, the color_markup plugin slows down coloring considerably.
                if tag == 'docPart' or tag.startswith('comment'):
                    if not g.doHook("color-optional-markup",
                        colorer=self,p=self.p,v=self.p,s=s,i=i,j=j,colortag=tag):
                        w.tag_add(tag,x1,x2)
                else:
                    # g.trace(tag,x1,x2,i,j)
                    w.tag_add(tag,x1,x2)

        self.start_i = self.end_i
    #@-node:ekr.20070718131458.45:tagAll
    #@+node:ekr.20070718131458.46:threadColorizer
    thread_count = 0

    def threadColorizer (self,p,incremental,interruptable):

        if self.trace: g.trace(g.callers())

        # Kill the previous thread for this widget.
        if self.trace: g.trace('incremental',incremental,g.callers())
        t = self.helperThread
        if t and t.isAlive():
            self.killFlag = True
            if self.trace: g.trace('before join',self.threadCount)
            t.join()
            if self.trace: g.trace('after join',self.threadCount)
            self.killFlag = False
            # This produces bad response for big body text.
            # incremental = False # recolor **everything**.
        self.helperThread = None
        # Init the ivars *after* ending the previous helper thread.
        self.init(p,incremental,interruptable) # Sets 'p','s','w' and other ivars.
        g.doHook("init-color-markup",colorer=self,p=self.p,v=self.p)
        if self.killcolorFlag or not self.mode:
            self.finishColoring(done=True)
        elif self.use_threads: # Start the helper thread.
            self.threadCount += 1
            t = threading.Thread(target=self.target,kwargs={'s':self.s})
            self.helperThread = t
            t.start()
            self.w.after_idle(self.idleHandler,self.threadCount)
        else:
            self.target(s=self.s)
            self.w.after_idle(self.idleHandler,self.threadCount)
    #@-node:ekr.20070718131458.46:threadColorizer
    #@-node:ekr.20070719111308:Colorers & helpers
    #@+node:edreamleo.20070728081453:In helper thread
    #@+node:ekr.20070720101942:adjustMarksDict
    def adjustMarksDict (self,d,mid_i,delta):

        '''Adjust the marksDict d by adding delta to
        all keys and values whose keys are >= mid_i.'''

        # Pass 1: Add changed items to d2, and delete them from d.
        d2 = {}
        for i in d.keys():
            if i > mid_i:
                # d2 [i+delta] = d.get(i) + delta
                d2 [max(0,i+delta)] = max(0,d.get(i) + delta) # Bug fix: 10/10/07
                del d[i]

        # Pass 2: Insert changed items back into d.
        for i in d2.keys():
            d[i] = d2.get(i)

        return d
    #@-node:ekr.20070720101942:adjustMarksDict
    #@+node:ekr.20070718131458.48:colorRangeWithTag (in helper thread)
    def colorRangeWithTag (self,s,i,j,tag,delegate='',exclude_match=False):

        '''Add an item to the globalTagList if colorizing is enabled.'''

        if self.killFlag:
            if self.trace: g.trace('*** killed',self.threadCount)
            return

        if not self.flag: return

        if delegate:
            # g.trace(delegate,i,j,g.callers())
            self.modeStack.append(self.modeBunch)
            self.init_mode(delegate)
            # Color everything at once, using the same indices as the caller.
            while i < j:
                assert j >= 0, 'colorRangeWithTag: negative j'
                for f in self.rulesDict.get(s[i],[]):
                    n = f(self,s,i)
                    if n > 0:
                        # if f.__name__ != 'match_blanks': g.trace(delegate,i,f.__name__)
                        i += n ; break
                else: i += 1
            bunch = self.modeStack.pop()
            self.initModeFromBunch(bunch)
        elif not exclude_match:
            # g.trace('***',self.rulesetName,tag,i,j,s[i:j],g.callers())
            # if self.trace: g.trace(tag,i,j,repr(s[i:j]))
            # Critical section: must be as fast as possible.
            if self.lock_trace: g.trace('lock on',self.threadCount)
            self.lock.acquire()
            self.globalTagList.append((tag,i,j),)
            self.end_i = j
            self.lock.notify()
            self.lock.release()
            if self.lock_trace: g.trace('lock off',self.threadCount)
    #@-node:ekr.20070718131458.48:colorRangeWithTag (in helper thread)
    #@+node:ekr.20070720095702:computeIndices
    def computeIndices (self):

        '''Return (mid_i,tail_i,delta,all) where
        - mid_i is the index of the start of the changed text,
        - tail_i is the index of the start of the **new** trailing lines,
        - delta is the change in the size of the changed text,
        - all is true if all text must be recolored.'''

        old_s,new_s = self.old_s,self.s

        # The first optimization: recolor **everything** if all lines match.
        # Some routines delete, then insert the text again, deleting all tags in the process.
        if old_s == new_s:
            all = True
            return 0,0,0,all

        # The second optimization. Check to see if only one line has changed.
        ins = self.insertPoint # We must *not* call Tk here!
        new_i,new_j = g.getLine(new_s,ins)
        old_i,old_j = g.getLine(old_s,new_i)
        new_head = new_s[:new_i]
        old_head = old_s[:old_i]
        new_tail = new_s[new_j:]
        old_tail = old_s[old_j:]
        #g.trace('new_head',repr(new_head),'\n','old_head',repr(old_head))
        #g.trace('new_tail',repr(new_tail),'\n','old_tail',repr(old_tail))
        if new_head == old_head and new_tail == old_tail:
            # g.trace('**one line changed')
            mid_i = new_i
            tail_i = new_j
            #new_line = new_s[new_i:new_j]
            #old_line = old_s[old_i:old_j]
            #delta = len(new_line) - len(old_line)
            delta = (new_j-new_i) - (old_j-old_i)
            all = False
            return mid_i,tail_i,delta,all

        # The general case: compare line-by line to find the head and tail.
        new_lines = g.splitLines(new_s)
        old_lines = g.splitLines(old_s)
        new_len = len(new_lines)
        old_len = len(old_lines)
        # Find the head lines, the leading matching lines.
        i = 0
        while i < new_len and i < old_len and old_lines[i] == new_lines[i]:
            i += 1
        head = i
        # Find the tail lines, the trailing matching lines.
        i = 0
        while (
            old_len-i-1 >=0 and new_len-i-1 >=0 and
            old_lines[old_len-i-1] == new_lines[new_len-i-1]
        ):
            i += 1
        tail = i
        # Compute the change (middle) lines.
        new_head = ''.join(new_lines[:head])
        old_head = ''.join(old_lines[:head])
        # assert old_head == new_head
        if tail:
            new_tail = ''.join(new_lines[-tail:])
            old_tail = ''.join(old_lines[-tail:])
            new_middle = ''.join(new_lines[head:-tail])
            old_middle = ''.join(old_lines[head:-tail])
        else:
            # g.trace('no tail')
            new_tail = old_tail = ''
            new_middle = ''.join(new_lines[head:])
            old_middle = ''.join(old_lines[head:])
        # assert old_tail == new_tail

        # This recolors all of all changed lines.
        # We could optimize this a bit, but I doubt it would make much difference.
        mid_i = len(new_head)
        tail_i = mid_i + len(new_middle)
        delta = len(new_middle) - len(old_middle)
        all = False
        # g.trace('mid_i',mid_i,'tail_i',tail_i,'delta',delta,'all',all)
        return mid_i,tail_i,delta,all
    #@-node:ekr.20070720095702:computeIndices
    #@+node:ekr.20070719105813:fullColor (in helper thread)
    def fullColor (self,s):

        '''Fully recolor s.'''

        if self.trace: g.trace(self.language,self.threadCount) #,g.callers())
        i = self.start_i = self.end_i = 0
        self.marksDict = {}
        while i < len(s):
            progress = i
            if self.killFlag:
                if self.trace: g.trace('*** killed %d' % self.threadCount)
                return
            for f in self.rulesDict.get(s[i],[]):
                n = f(self,s,i)
                if n is None:
                    g.trace('Can not happen: matcher returns None')
                elif n > 0:
                    if 0:
                        if trace_all_matches and f.__name__ != 'match_blanks':
                            g.trace(f.__name__,repr(s[i:i+n]))
                    self.marksDict [i] = n
                    i += n ; break
            else:
                i += 1
            assert i > progress

        self.end_i = len(s)
        self.old_s = self.s
        if self.trace: g.trace('*** done',self.threadCount)
    #@-node:ekr.20070719105813:fullColor (in helper thread)
    #@+node:ekr.20070719110029:partialColor (in helper thread)
    def partialColor (self,s):

        '''Partially recolor s'''

        mid_i,tail_i,delta,all = self.computeIndices()
        if all:
            if self.trace: g.trace('*** all lines match: recolor all')
            return self.fullColor(s)

        d = self.marksDict = self.adjustMarksDict(self.marksDict,mid_i,delta)
        assert(mid_i == 0 or s[mid_i-1] == '\n')
        i = self.findMarkAtIndex(d,max(0,mid_i-1))
        self.start_i = self.self_end_i = i
        # if mid_i-1 != i: g.trace('backtrack',repr(s[i:mid_i]))

        # Create a list of (i,n) pairs from marksDict.
        d = self.marksDict ; keys = d.keys() ; keys.sort()
        endList = [(z,d.get(z)) for z in keys if z + d.get(z) >= tail_i]
        self.marksDict = {}
        if self.trace: g.trace(self.language,'thread',self.threadCount,'i',i)
        while i < len(s):
            progress = i
            if self.killFlag:
                if self.trace: g.trace('*** killed %d*' % self.threadCount)
                return
            if i < 0 or i >= len(s):
                g.trace('can not happen','i out of range',i)
            for f in self.rulesDict.get(s[i],[]):
                n = f(self,s,i)
                if n is None: g.trace('Can not happen: matcher returns None')
                elif n > 0:
                    if (trace_all_matches) and f.__name__ != 'match_blanks':
                        g.trace(f.__name__,repr(s[i:i+n]))
                    self.marksDict[i] = n
                    i += n ; break
            else:
                i += 1
            if i > tail_i:
                #@            << finish if no item in endList covers i >>
                #@+node:ekr.20070720141852:<< finish if no item in endList covers i >>
                done = False ; n = 0 # count of elements to be removed.
                for z in endList:
                    i2,n2 = z
                    if i2 <= i:
                        if i2 + n2 < i:
                            n += 1 # strictly before i. Remove it below.
                        else:
                            break # covers i.  Not done.
                    else: # i2 > i:
                        done = True
                    if done: # Add trailing items in endList to the marksDict.
                        self.marksDict[i2] = n2
                else:
                    done = True

                if done:
                    if self.trace: g.trace('*** found end: i: %d %s' % (i,repr(s[i:i+20])))
                    break
                else:
                    # Delete n entries from the front of endList.
                    if n > 0:
                        endList = endList[n:]
                #@nonl
                #@-node:ekr.20070720141852:<< finish if no item in endList covers i >>
                #@nl
            assert progress < i
        self.end_i = i
        self.old_s = self.s
        if self.trace: g.trace('*** done',self.threadCount)
    #@-node:ekr.20070719110029:partialColor (in helper thread)
    #@+node:ekr.20070718131458.52:target (in helper thread)
    def target(self,*args,**keys):

        s = keys.get('s')
        # if self.trace: g.trace(self.threadCount)

        try:
            if self.incremental:
                self.partialColor(s)
            else:
                self.fullColor(s)
            return "ok" # for testing.
        except:
            # We can not use g.es_exception: it calls Tk methods.
            traceback.print_exc()
            return "error" # for unit testing.
    #@-node:ekr.20070718131458.52:target (in helper thread)
    #@-node:edreamleo.20070728081453:In helper thread
    #@+node:ekr.20070718131458.53:jEdit matchers (in helper thread)
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
    # The following arguments affect coloring when a match succeeds:
    # 
    # - delegate              A ruleset name. The matched text will be colored 
    # recursively by the indicated ruleset.
    # - exclude_match         If True, the actual text that matched will not 
    # be colored.
    # - kind                  The color tag to be applied to colored text.
    #@-at
    #@@c
    #@@color
    #@+node:ekr.20070718131458.54:match_eol_span
    def match_eol_span (self,s,i,
        kind=None,seq='',
        at_line_start=False,at_whitespace_end=False,at_word_start=False,
        delegate='',exclude_match=False):

        '''Succeed if seq matches s[i:]'''

        if self.trace_match_flag: g.trace(g.callers(2),i,repr(s[i:i+20]))

        if at_line_start and i != 0 and s[i-1] != '\n': return 0
        if at_whitespace_end and i != g.skip_ws(s,0): return 0
        if at_word_start and i > 0 and s[i-1] not in self.word_chars: return 0

        if g.match(s,i,seq):
            j = g.skip_to_end_of_line(s,i)
            self.colorRangeWithTag(s,i,j,kind,delegate=delegate,exclude_match=exclude_match)
            self.prev = (i,j,kind)
            self.trace_match(kind,s,i,j)
            return j - i
        else:
            return 0
    #@-node:ekr.20070718131458.54:match_eol_span
    #@+node:ekr.20070718131458.55:match_eol_span_regexp
    def match_eol_span_regexp (self,s,i,
        kind='',regexp='',
        at_line_start=False,at_whitespace_end=False,at_word_start=False,
        delegate='',exclude_match=False):

        '''Succeed if the regular expression regex matches s[i:].'''

        if self.trace_match_flag: g.trace(g.callers(2),i,repr(s[i:i+20]))

        if at_line_start and i != 0 and s[i-1] != '\n': return 0
        if at_whitespace_end and i != g.skip_ws(s,0): return 0
        if at_word_start and i > 0 and s[i-1] not in self.word_chars: return 0

        n = self.match_regexp_helper(s,i,regexp)
        if n > 0:
            j = g.skip_to_end_of_line(s,i)
            self.colorRangeWithTag(s,i,j,kind,delegate=delegate,exclude_match=exclude_match)
            self.prev = (i,j,kind)
            self.trace_match(kind,s,i,j)
            return j - i
        else:
            return 0
    #@nonl
    #@-node:ekr.20070718131458.55:match_eol_span_regexp
    #@+node:ekr.20070718131458.56:match_keywords
    # This is a time-critical method.
    def match_keywords (self,s,i):

        '''Succeed if s[i:] is a keyword.'''

        # We must be at the start of a word.
        if i > 0 and s[i-1] in self.word_chars:
            return 0

        # Get the word as quickly as possible.
        j = i ; n = len(s) ; chars = self.word_chars
        while j < n and s[j] in chars:
            j += 1

        word = s[i:j]
        if self.ignore_case: word = word.lower()
        kind = self.keywordsDict.get(word)
        if kind:
            self.colorRangeWithTag(s,i,j,kind)
            self.prev = (i,j,kind)
            result = j - i
            self.trace_match(kind,s,i,j)
            return result
        else:
            return 0
    #@nonl
    #@-node:ekr.20070718131458.56:match_keywords
    #@+node:ekr.20070718131458.57:match_mark_following & getNextToken
    def match_mark_following (self,s,i,
        kind='',pattern='',
        at_line_start=False,at_whitespace_end=False,at_word_start=False,
        exclude_match=False):

        '''Succeed if s[i:] matches pattern.'''

        if self.trace_match_flag: g.trace(g.callers(2),i,repr(s[i:i+20]))

        if at_line_start and i != 0 and s[i-1] != '\n': return 0
        if at_whitespace_end and i != g.skip_ws(s,0): return 0
        if at_word_start and i > 0 and s[i-1] not in self.word_chars: return 0

        if g.match(s,i,pattern):
            j = i + len(pattern)
            self.colorRangeWithTag(s,i,j,kind,exclude_match=exclude_match)
            k = self.getNextToken(s,j)
            if k > j:
                self.colorRangeWithTag(s,j,k,kind,exclude_match=False)
                j = k
            self.prev = (i,j,kind)
            self.trace_match(kind,s,i,j)
            return j - i
        else:
            return 0
    #@nonl
    #@+node:ekr.20070718131458.58:getNextToken
    def getNextToken (self,s,i):

        '''Return the index of the end of the next token for match_mark_following.

        The jEdit docs are not clear about what a 'token' is, but experiments with jEdit
        show that token means a word, as defined by word_chars.'''

        while i < len(s) and s[i] in self.word_chars:
            i += 1

        return min(len(s),i+1)
    #@nonl
    #@-node:ekr.20070718131458.58:getNextToken
    #@-node:ekr.20070718131458.57:match_mark_following & getNextToken
    #@+node:ekr.20070718131458.59:match_mark_previous
    def match_mark_previous (self,s,i,
        kind='',pattern='',
        at_line_start=False,at_whitespace_end=False,at_word_start=False,
        exclude_match=False):

        '''Return the length of a matched SEQ or 0 if no match.

        'at_line_start':    True: sequence must start the line.
        'at_whitespace_end':True: sequence must be first non-whitespace text of the line.
        'at_word_start':    True: sequence must start a word.'''

        if self.trace_match_flag: g.trace(g.callers(2),i,repr(s[i:i+20]))

        if at_line_start and i != 0 and s[i-1] != '\n': return 0
        if at_whitespace_end and i != g.skip_ws(s,0): return 0
        if at_word_start and i > 0 and s[i-1] not in self.word_chars: return 0

        if g.match(s,i,pattern):
            j = i + len(pattern)
            # Color the previous token.
            if self.prev:
                i2,j2,kind2 = self.prev
                # g.trace(i2,j2,kind2)
                self.colorRangeWithTag(s,i2,j2,kind2,exclude_match=False)
            if not exclude_match:
                self.colorRangeWithTag(s,i,j,kind)
            self.prev = (i,j,kind)
            self.trace_match(kind,s,i,j)
            return j - i
        else:
            return 0
    #@-node:ekr.20070718131458.59:match_mark_previous
    #@+node:ekr.20070718131458.60:match_regexp_helper
    def match_regexp_helper (self,s,i,pattern):

        '''Return the length of the matching text if seq (a regular expression) matches the present position.'''

        if self.trace_match_flag: g.trace(pattern)

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
            # g.trace('match: %s' % repr(s[start: end]))
            # g.trace('groups',mo.groups())
            return end - start
    #@-node:ekr.20070718131458.60:match_regexp_helper
    #@+node:ekr.20070718131458.61:match_seq
    def match_seq (self,s,i,
        kind='',seq='',
        at_line_start=False,at_whitespace_end=False,at_word_start=False,
        delegate=''):

        '''Succeed if s[:] mathces seq.'''

        if at_line_start and i != 0 and s[i-1] != '\n':
            j = i
        elif at_whitespace_end and i != g.skip_ws(s,0):
            j = i
        elif at_word_start and i > 0 and s[i-1] not in self.word_chars:
            j = i
        elif g.match(s,i,seq):
            j = i + len(seq)
            self.colorRangeWithTag(s,i,j,kind,delegate=delegate)
            self.prev = (i,j,kind)
            self.trace_match(kind,s,i,j)
        else:
            j = i
        return j - i
    #@nonl
    #@-node:ekr.20070718131458.61:match_seq
    #@+node:ekr.20070718131458.62:match_seq_regexp
    def match_seq_regexp (self,s,i,
        kind='',regexp='',
        at_line_start=False,at_whitespace_end=False,at_word_start=False,
        delegate=''):

        '''Succeed if the regular expression regexp matches at s[i:].'''

        if self.trace_match_flag: g.trace(g.callers(2),i,repr(s[i:i+20]))

        if at_line_start and i != 0 and s[i-1] != '\n': return 0
        if at_whitespace_end and i != g.skip_ws(s,0): return 0
        if at_word_start and i > 0 and s[i-1] not in self.word_chars: return 0

        j = self.match_regexp_helper(s,i,regexp)
        self.colorRangeWithTag(s,i,j,kind,delegate=delegate)
        self.prev = (i,j,kind)
        self.trace_match(kind,s,i,j)
        return j - i
    #@nonl
    #@-node:ekr.20070718131458.62:match_seq_regexp
    #@+node:ekr.20070718131458.63:match_span & helper
    def match_span (self,s,i,
        kind='',begin='',end='',
        at_line_start=False,at_whitespace_end=False,at_word_start=False,
        delegate='',exclude_match=False,
        no_escape=False,no_line_break=False,no_word_break=False):

        '''Succeed if s[i:] starts with 'begin' and contains a following 'end'.'''

        if at_line_start and i != 0 and s[i-1] != '\n':
            j = i
        elif at_whitespace_end and i != g.skip_ws(s,0):
            j = i
        elif at_word_start and i > 0 and s[i-1] not in self.word_chars:
            j = i
        elif not g.match(s,i,begin):
            j = i
        else:
            j = self.match_span_helper(s,i+len(begin),end,no_escape,no_line_break)
            if j == -1:
                j = i
            else:

                i2 = i + len(begin) ; j2 = j + len(end)
                # g.trace(i,j,s[i:j2],kind)
                self.colorRangeWithTag(s,i,i2,kind,delegate=None,    exclude_match=exclude_match)
                self.colorRangeWithTag(s,i2,j,kind,delegate=delegate,exclude_match=exclude_match)
                self.colorRangeWithTag(s,j,j2,kind,delegate=None,    exclude_match=exclude_match)
                j = j2
                self.prev = (i,j,kind)

        self.trace_match(kind,s,i,j)
        return j - i
    #@+node:ekr.20070718131458.64:match_span_helper
    def match_span_helper (self,s,i,pattern,no_escape,no_line_break):

        '''Return n >= 0 if s[i] ends with a non-escaped 'end' string.'''

        esc = self.escape

        while 1:
            j = s.find(pattern,i)
            if j == -1:
                # 7/21/07: Match to end of text if not found and no_line_break is False
                if no_line_break:
                    return -1
                else:
                    # g.trace('match to end',
                        # 'len(globalTagList)',len(self.globalTagList),
                        # 'start_i',self.start_i,'i',i,repr(s[self.start_i:i]))
                    return len(s)
            elif no_line_break and '\n' in s[i:j]:
                return -1
            elif esc and not no_escape:
                # Only an odd number of escapes is a 'real' escape.
                escapes = 0 ; k = 1
                while j-k >=0 and s[j-k] == esc:
                    escapes += 1 ; k += 1
                if (escapes % 2) == 1:
                    # Continue searching past the escaped pattern string.
                    i = j + len(pattern) # Bug fix: 7/25/07.
                    # g.trace('escapes',escapes,repr(s[i:]))
                else:
                    return j
            else:
                return j
    #@nonl
    #@-node:ekr.20070718131458.64:match_span_helper
    #@-node:ekr.20070718131458.63:match_span & helper
    #@+node:ekr.20070718131458.65:match_span_regexp
    def match_span_regexp (self,s,i,
        kind='',begin='',end='',
        at_line_start=False,at_whitespace_end=False,at_word_start=False,
        delegate='',exclude_match=False,
        no_escape=False,no_line_break=False, no_word_break=False,
    ):

        '''Succeed if s[i:] starts with 'begin' (a regular expression) and contains a following 'end'.'''

        if self.trace_match_flag:
            g.trace('begin',repr(begin),'end',repr(end),self.dump(s[i:]))

        if at_line_start and i != 0 and s[i-1] != '\n': return 0
        if at_whitespace_end and i != g.skip_ws(s,0): return 0
        if at_word_start and i > 0 and s[i-1] not in self.word_chars: return 0

        n = self.match_regexp_helper(s,i,begin)
        # We may have to allow $n here, in which case we must use a regex object?
        if n > 0:
            j = i + n
            j2 = s.find(end,j)
            if j2 == -1: return 0
            if self.escape and not no_escape:
                # Only an odd number of escapes is a 'real' escape.
                escapes = 0 ; k = 1
                while j-k >=0 and s[j-k] == esc:
                    escapes += 1 ; k += 1
                if (escapes % 2) == 1:
                    # An escaped end **aborts the entire match**:
                    # there is no way to 'restart' the regex.
                    return 0
            i2 = j2 - len(end)
            self.colorRangeWithTag(s,i,j,kind, delegate=None,     exclude_match=exclude_match)
            self.colorRangeWithTag(s,j,i2,kind, delegate=delegate,exclude_match=False)
            self.colorRangeWithTag(s,i2,j2,kind,delegate=None,    exclude_match=exclude_match)
            self.prev = (i,j,kind)
            self.trace_match(kind,s,i,j2)
            return j2 - i
        else: return 0
    #@-node:ekr.20070718131458.65:match_span_regexp
    #@-node:ekr.20070718131458.53:jEdit matchers (in helper thread)
    #@+node:ekr.20070718131458.66:Utils
    #@+at 
    #@nonl
    # These methods are like the corresponding functions in leoGlobals.py 
    # except they issue no error messages.
    #@-at
    #@+node:ekr.20070718131458.67:dump
    def dump (self,s):

        if s.find('\n') == -1:
            return s
        else:
            return '\n' + s + '\n'
    #@nonl
    #@-node:ekr.20070718131458.67:dump
    #@+node:ekr.20070718131458.69:munge
    def munge(self,s):

        '''Munge a mode name so that it is a valid python id.'''

        valid = string.ascii_letters + string.digits + '_'

        return ''.join([g.choose(ch in valid,ch.lower(),'_') for ch in s])
    #@nonl
    #@-node:ekr.20070718131458.69:munge
    #@+node:ekr.20070718131458.70:scanColorDirectives
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
            #@+node:ekr.20070718131458.71:<< Test for @comment or @language >>
            # @comment and @language may coexist in the same node.

            if theDict.has_key("comment"):
                k = theDict["comment"]
                self.comment_string = s[k:]

            if theDict.has_key("language"):
                i = theDict["language"]
                tag = "@language"
                assert(g.match_word(s,i,tag))
                i = g.skip_ws(s,i+len(tag))
                j = g.skip_c_id(s,i)
                self.language = s[i:j].lower()

            if theDict.has_key("comment") or theDict.has_key("language"):
                break
            #@nonl
            #@-node:ekr.20070718131458.71:<< Test for @comment or @language >>
            #@nl
            #@        << Test for @root, @root-doc or @root-code >>
            #@+node:ekr.20070718131458.72:<< Test for @root, @root-doc or @root-code >>
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
            #@-node:ekr.20070718131458.72:<< Test for @root, @root-doc or @root-code >>
            #@nl

        # g.trace(self.language)

        return self.language # For use by external routines.
    #@nonl
    #@-node:ekr.20070718131458.70:scanColorDirectives
    #@+node:ekr.20070718131458.73:setFontFromConfig
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
    #@-node:ekr.20070718131458.73:setFontFromConfig
    #@+node:ekr.20070718131458.74:trace_match
    def trace_match(self,kind,s,i,j):

        if j != i and self.trace_match_flag:
            g.trace(kind,i,j,g.callers(4),self.dump(s[i:j]))
    #@nonl
    #@-node:ekr.20070718131458.74:trace_match
    #@-node:ekr.20070718131458.66:Utils
    #@-others
#@-node:ekr.20070718131458.20:class colorizer
#@-others

#@<< class nullColorizer (colorizer) >>
#@+node:ekr.20070718131458.2:<< class nullColorizer (colorizer) >>
class nullColorizer (colorizer):

    """A do-nothing colorer class"""

    #@    @+others
    #@+node:ekr.20070718131458.3:__init__
    def __init__ (self,c):

        colorizer.__init__(self,c) # init the base class.

        self.c = c
        self.enabled = False
    #@-node:ekr.20070718131458.3:__init__
    #@+node:ekr.20070718131458.4:entry points
    def colorize(self,p,incremental=False): pass

    def disable(self): pass

    def enable(self): pass

    def recolor_range(self,p,leading,trailing): pass

    def scanColorDirectives(self,p): pass

    def schedule(self,p,incremental=0): pass

    def updateSyntaxColorer (self,p): pass
    #@nonl
    #@-node:ekr.20070718131458.4:entry points
    #@-others
#@nonl
#@-node:ekr.20070718131458.2:<< class nullColorizer (colorizer) >>
#@nl
#@nonl
#@-node:ekr.20070718094819:@thin threading_colorizer.py	
#@-leo
