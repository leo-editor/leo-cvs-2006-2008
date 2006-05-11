#@+leo-ver=4-thin
#@+node:ekr.20050529142847:@thin __jEdit_colorizer__.py
'''Replace colorizer with colorizer using jEdit language description files'''

#@@language python
#@@tabwidth -4
#@@pagewidth 80

__version__ = '0.21'
#@<< imports >>
#@+node:ekr.20050529142916.3:<< imports >>
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
#@-node:ekr.20050529142916.3:<< imports >>
#@nl
#@<< version history >>
#@+node:ekr.20050529142916.2:<< version history >>
#@@killcolor
#@+at
# 
# 0.20 EKR: Use x.py files rather than x.xml files.
# - The colorizer now works on most text.
# 
# 0.21 EKR: No known crashers or serious problems.
# - The colorizer now switches modes properly.
# - Possible fix for unicode crasher.
#@-at
#@nonl
#@-node:ekr.20050529142916.2:<< version history >>
#@nl
#@<< to do >>
#@+node:ekr.20050601081132:<< to do >>
#@@nocolor
#@+at
# 
# - Use attributes in attributes dicts:
#     - Add all characters in 'no_word_sep' attribute to word_chars.
#     - Use 'ignore_case' attribute in match_keywords.
# 
# - Improve quick coloring.
# 
# - Handle (and then delete) import rules when first loading a mode.
# 
# - Handle the delegate attribute, i.e., recursive coloring.
# 
# - Finish all rules: mark_previous, mark_following, match_regexp_helper.
# 
# - Support coloring of digits.
#     ?? Create a match_digits rule matcher??
#     Use 'default_digit_re' and 'highlight_digits' attributes in rules 
# element.
# 
# - Document all properties.
# 
# - Tell how to use custom rule matchers.
# 
#@-at
#@@c
#@@color

#@<< later >>
#@+node:ekr.20050603121815:<< later >>
#@@killcolor
#@+at
# - Support comment properties and self.comment_string:
#     - Conditionally add rules for comment ivars: 
# single_comment_start,block_comment_start,block_comment_end
#     - commentEnd - the comment end string, used by the Range Comment 
# command.
#     - commentStart - the comment start string, used by the Range Comment 
# command.
#     - lineComment - the line comm
# 
# - Support Show Invisibles.
#     Conditionally add rule for whitespace.
# 
# - Handle cweb section references correctly.
# 
# - Handle logic of setFirstLineState.
#     - Change match_doc_part: Start in doc mode for some @root's.
# 
# - Make sure pictures get drawn properly.
# 
# - Create forth.xml
#@-at
#@nonl
#@-node:ekr.20050603121815:<< later >>
#@nl
#@-node:ekr.20050601081132:<< to do >>
#@nl

#@<< define leoKeywords >>
#@+middle:ekr.20060425113823.1:module-level
#@+node:ekr.20050529143413:<< define leoKeywords >>
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
    "@unit","@verbose","@wrap", ]
#@nonl
#@-node:ekr.20050529143413:<< define leoKeywords >>
#@-middle:ekr.20060425113823.1:module-level
#@nl
#@<< define default_colors_dict >>
#@+middle:ekr.20060425113823.1:module-level
#@+node:ekr.20050529143413.1:<< define default_colors_dict >>
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
    'markup'    :('markup_color',   '#00aa00'),
    'null'      :('null_color',     'black'),
    'operator'  :('operator_color', 'black'),
    }
#@nonl
#@-node:ekr.20050529143413.1:<< define default_colors_dict >>
#@-middle:ekr.20060425113823.1:module-level
#@nl

#@+others
#@+node:ekr.20060425113823.1:module-level
#@+node:ekr.20050529142916.4:init
def init ():

    leoPlugins.registerHandler('start1',onStart1)
    g.plugin_signon(__name__)

    return True
#@nonl
#@-node:ekr.20050529142916.4:init
#@+node:ekr.20050529142916.5:onStart1
def onStart1 (tag, keywords):
    
    '''Override Leo's core colorizer classes.'''
    
    import leoColor
    
    leoColor.colorizer = baseColorizer
    
    leoColor.colorizer = colorizer
    
    leoColor.nullColorizer = nullColorizer
#@nonl
#@-node:ekr.20050529142916.5:onStart1
#@+node:ekr.20060503153603:Leo rule functions
#@+at
# These rule functions recognize noweb syntactic constructions. These are 
# treated
# just like rule functions, so they are module-level objects whose first 
# argument
# is 'self'.
#@-at
#@nonl
#@+node:ekr.20050603043840.1:match_at_color
def match_at_color (self,s,i):

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
#@-node:ekr.20050603043840.1:match_at_color
#@+node:ekr.20050603043840.2:match_at_nocolor
def match_at_nocolor (self,s,i):
    
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
#@-node:ekr.20050603043840.2:match_at_nocolor
#@+node:ekr.20050602211253:match_doc_part
def match_doc_part (self,s,i):
    
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
            j = n - 1
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
#@-node:ekr.20050602211253:match_doc_part
#@+node:ekr.20050602211219:match_section_ref
def match_section_ref (self,s,i):
    
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
                #@+node:ekr.20060504090341:<< set the hyperlink >>
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
                #@-node:ekr.20060504090341:<< set the hyperlink >>
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
#@-node:ekr.20050602211219:match_section_ref
#@-node:ekr.20060503153603:Leo rule functions
#@-node:ekr.20060425113823.1:module-level
#@+node:ekr.20050606214036:class colorizer (baseColorizer)
class baseColorizer:

    '''New colorizer using jEdit language description files'''
    #@    @+others
    #@+node:ekr.20050529143413.24:Birth and init
    #@+node:ekr.20050602150957:__init__
    def __init__(self,c):
        # Copies of ivars.
        self.c = c
        self.frame = c.frame
        self.body = c.frame.body
        self.p = None
        # Config settings.
        self.comment_string = None # Set by scanColorDirectives on @comment
        self.showInvisibles = False # True: show "invisible" characters.
        self.underline_undefined = c.config.getBool("underline_undefined_section_names")
        self.use_hyperlinks = c.config.getBool("use_hyperlinks")
        # State ivars...
        self.colored_ranges = {}
            # Keys are indices, values are tags.
        self.chunk_count = 0
        self.color_pass = 0
        self.comment_string = None # Can be set by @comment directive.
        self.defaultRulesList = []
        self.enabled = True # Set to False by unit tests.
        self.flag = True # True unless in range of @nocolor
        self.keywordNumber = 0 # The kind of keyword for keywordsColorHelper.
        self.kill_chunk = False
        self.language = 'python' # set by scanColorDirectives.
        self.queue_count = 0
        self.ranges = 0
        self.redoColoring = False # May be set by plugins.
        self.redoingColoring = False
        self.was_non_incremental = False # True: we are coloring as the result of a non-incremental call.
        # Data...
        self.keywords = {} # Keys are keywords, values are 0..5.
        self.modes = {} # Keys are languages, values are modes.
        self.mode = None # The mode object for the present language.
        self.trace = c.config.getBool('trace_colorizer')
        if 0:
            self.defineAndExtendForthWords()
        self.word_chars = {} # Inited by init_keywords().
        self.setFontFromConfig()
        self.tags = [
            "blank","comment","cwebName","docPart","keyword","leoKeyword",
            "latexModeBackground","latexModeKeyword",
            "latexBackground","latexKeyword",
            "link","name","nameBrackets","pp","string","tab",
            "elide","bold","bolditalic","italic", # new for wiki styling.
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
    #@-node:ekr.20050602150957:__init__
    #@+node:ekr.20060504083828:addLeoRules
    def addLeoRules (self,theDict):
    
        '''Prepend Leo-specific rules to theList.'''
    
        # Order does not matter here.
        for ch, rule in (
            ('@',match_at_color),
            ('@',match_at_nocolor),
            ('@',match_doc_part),
            ('<',match_section_ref),
        ):
            theList = theDict.get(ch,[])
            theList.insert(0,rule)
            theDict [ch] = theList
    #@nonl
    #@-node:ekr.20060504083828:addLeoRules
    #@+node:ekr.20060504081338:init_keywords
    def init_keywords (self,d):
        
        '''Initialize the keywords for the present language.
        
         Set self.word_chars ivar to string.letters + string.digits
         plus any other character appearing in any keyword.'''
    
        # Add any new user keywords to leoKeywords.
        keys = d.keys()
        for s in g.globalDirectiveList:
            key = '@' + s
            if key not in keys:
                d [key] = 'leoKeyword'
            
        for key in leoKeywords:
            d [ key ] = 'leoKeyword'
    
        # Create the word_chars list. 
        self.word_chars = [ch for ch in (string.letters + string.digits)]
        for key in d.keys():
            for ch in key:
                if ch not in self.word_chars:
                    self.word_chars.append(g.toUnicode(ch,encoding='UTF-8'))
    #@nonl
    #@-node:ekr.20060504081338:init_keywords
    #@+node:ekr.20050529143413.33:configure_tags
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
                
        # Only create tags for whitespace when showing invisibles.
        if self.showInvisibles:
            for name,option_name,default_color in (
                ("blank","show_invisibles_space_background_color","Gray90"),
                ("tab",  "show_invisibles_tab_background_color",  "Gray80")):
                option_color = c.config.getColor(option_name)
                color = g.choose(option_color,option_color,default_color)
                try:
                    self.body.tag_configure(name,background=color)
                except: # Recover after a user error.
                    self.body.tag_configure(name,background=default_color)
            
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
        if self.showInvisibles:
            self.body.tag_configure("elide",background="yellow")
        else:
            self.body.tag_configure("elide",elide="1")
        self.body.tag_configure("bold",font=self.bold_font)
        self.body.tag_configure("italic",font=self.italic_font)
        self.body.tag_configure("bolditalic",font=self.bolditalic_font)
        for name in self.color_tags_list:
            self.body.tag_configure(name,foreground=name)
    #@nonl
    #@-node:ekr.20050529143413.33:configure_tags
    #@+node:ekr.20050602150619:init_mode
    def init_mode (self,language):
        
        if not language: return
        bunch = self.modes.get(language)
        if bunch:
            self.defaultColor = bunch.defaultColor
            self.keywordsDict = bunch.keywordsDict
            self.mode         = bunch.mode
            self.rulesDict    = bunch.rulesDict
            self.rulesetName  = bunch.rulesetName
        else:
            path = g.os_path_join(g.app.loadDir,'..','modes')
            mode = g.importFromPath (language,path)
            if mode:
                g.trace('loading mode for: ',language)
                self.rulesetName = self.computeRulesetName(language)
                self.keywordsDict = d = mode.keywordsDictDict.get(self.rulesetName,{})
                self.init_keywords(d)
                # g.trace(len(self.keywordsDict.keys()))
                self.rulesDict = mode.rulesDictDict.get(self.rulesetName)
                self.addLeoRules(self.rulesDict)
                self.defaultColor = 'null'
                ### To do: append imported rules.
                # g.trace(len(self.rules))
                self.mode = mode
                self.modes [language] = g.Bunch(
                    defaultColor = self.defaultColor,
                    keywordsDict = self.keywordsDict,
                    mode         = self.mode,
                    rulesDict    = self.rulesDict,
                    rulesetName  = self.rulesetName)
            else:
                g.trace('No language description for %s' % language)
    #@nonl
    #@-node:ekr.20050602150619:init_mode
    #@-node:ekr.20050529143413.24:Birth and init
    #@+node:ekr.20050529145203:Entry points (3 to be REWRITTEN)
    #@+node:ekr.20050529143413.30:colorize
    colorize_count = 0
    
    def colorize(self,p,incremental=False):
        
        '''The main colorizer entry point.'''
        
        if 0:
            self.colorize_count += 1
            g.trace(incremental,self.colorize_count)
    
        if self.enabled:
            self.updateSyntaxColorer(p)
            return self.colorizeAnyLanguage(p)
        else:
            return "ok" # For unit testing.
    #@nonl
    #@-node:ekr.20050529143413.30:colorize
    #@+node:ekr.20050529143413.28:enable & disable
    def disable (self):
    
        print "disabling all syntax coloring"
        self.enabled=False
        
    def enable (self):
        self.enabled=True
    #@nonl
    #@-node:ekr.20050529143413.28:enable & disable
    #@+node:ekr.20050602144940:interrupt
    # This is needed, even without threads.
    
    def interrupt(self):
        '''Interrupt colorOneChunk'''
        self.chunk_s = ''
        self.chunk_i = 0
        self.tagList = []
        self.chunks_done = True
        g.trace('%3d %3d' % (self.chunk_count,self.queue_count))
    #@nonl
    #@-node:ekr.20050602144940:interrupt
    #@+node:ekr.20050529145203.1:recolor_range  (TO BE DELETED)
    def recolor_range(self,p,leading,trailing):
        
        '''An entry point for the colorer called from incremental undo code.
        Colorizes the lines between the leading and trailing lines.'''
        
        return self.colorize(p)
    
        # if self.enabled:
            # self.incremental=True
            # self.invalidate_range(leading,trailing)
            # self.updateSyntaxColorer(p)
            # return self.colorizeAnyLanguage(p,leading=leading,trailing=trailing)
        # else:
            # return "ok" # For unit testing.
    #@nonl
    #@-node:ekr.20050529145203.1:recolor_range  (TO BE DELETED)
    #@+node:ekr.20050529143413.42:recolor_all (MUST BE REWRITTEN)
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
            #@+node:ekr.20050529143413.43:<< kludge: insert a blank in s for every image in the line >>
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
            #@-node:ekr.20050529143413.43:<< kludge: insert a blank in s for every image in the line >>
            #@nl
            state = self.colorizeLine(s,state)
            self.line_index += 1
    #@nonl
    #@-node:ekr.20050529143413.42:recolor_all (MUST BE REWRITTEN)
    #@+node:ekr.20050529143413.84:schedule & idle_colorize (TO BE DELETED)
    def schedule(self,p,incremental=0):
        
        __pychecker__ = '--no-argsused'
        # p not used, but it is difficult to remove.
    
        if self.enabled:
            g.app.gui.setIdleTimeHook(self.idle_colorize)
            self.idle_colorize()
            
    def idle_colorize(self):
    
        # New in 4.3b1: make sure the colorizer still exists!
        if hasattr(self,'enabled') and self.enabled:
            p = self.c.currentPosition()
            p and self.colorize(p)
    #@nonl
    #@-node:ekr.20050529143413.84:schedule & idle_colorize (TO BE DELETED)
    #@+node:ekr.20050529143413.88:useSyntaxColoring
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
    #@-node:ekr.20050529143413.88:useSyntaxColoring
    #@+node:ekr.20050529143413.87:updateSyntaxColorer
    def updateSyntaxColorer (self,p):
    
        p = p.copy()
        # self.flag is True unless an unambiguous @nocolor is seen.
        self.flag = self.useSyntaxColoring(p)
        self.scanColorDirectives(p)
    #@nonl
    #@-node:ekr.20050529143413.87:updateSyntaxColorer
    #@-node:ekr.20050529145203:Entry points (3 to be REWRITTEN)
    #@+node:ekr.20050529150436:Colorizer code
    #@+node:ekr.20050601042620:colorAll
    def colorAll(self,s):
        
        '''Colorize all of s.'''
    
        # Init ivars used by colorOneChunk.
        self.chunk_s = s
        self.chunk_i = 0
        self.tagList = []
        self.queue_count = 0
        self.chunk_count = 0
        self.recolor_count = 0 # Number of times through the loop before a recolor.
        self.chunks_done = False
        self.quickColor()
        self.colorOneChunk()
    #@nonl
    #@-node:ekr.20050601042620:colorAll
    #@+node:ekr.20050529143413.31:colorizeAnyLanguage
    def colorizeAnyLanguage (self,p,leading=None,trailing=None):
        
        '''Color the body pane.  All coloring starts here.'''
    
        self.init_mode(self.language)
        if self.killcolorFlag or not self.mode:
            self.removeAllTags() ; return
        try:
            c = self.c ; self.p = p
            self.redoColoring = False
            self.redoingColoring = False
            g.doHook("init-color-markup",colorer=self,p=self.p,v=self.p)
            s = self.body.getAllText()
            self.colorAll(s)
            if self.redoColoring: # Set only from plugins.
                self.recolor_all()
            return "ok" # for unit testing.
        except Exception:
            g.es_exception()
            return "error" # for unit testing.
    #@nonl
    #@-node:ekr.20050529143413.31:colorizeAnyLanguage
    #@+node:ekr.20050601105358:colorOneChunk
    def colorOneChunk(self,allowBreak=True):
        '''Colorize a fixed number of tokens.
        If not done, queue this method again to continue coloring later.'''
        if self.chunks_done:
            return
        s,i = self.chunk_s,self.chunk_i
        count = 0 ; self.chunk_count += 1
        limit = 10 # Number of times through the loop before a pause.
        limit2 = 5000 # Number of times throught the loop before a recolor.
        while i < len(s):
            count += 1
            self.recolor_count += 1
            # This apparently interferes with event handling.
            # if limit2 > 0 and self.recolor_count > limit2:
                # g.trace('coloring',self.chunk_count)
                # self.recolor_count = 0
                # self.tagAll()
                # self.pause(s,i)
                # return
            if count >= limit:
                self.chunk_s, self.chunk_i = s,i
                self.queue_count += 1
                self.c.frame.top.after_idle(self.colorOneChunk)
                return 'break'
            for f in self.rulesDict.get(s[i],[]):
                n = f(self,s,i)
                if n > 0:
                    i += n ; break
            else: i += 1
    
        # g.trace('%3d %3d' % (self.chunk_count,self.queue_count))
        self.removeAllTags()
        self.tagAll()
        self.tagList = []
        self.chunks_done = True # Prohibit any more queued calls.
    #@nonl
    #@-node:ekr.20050601105358:colorOneChunk
    #@+node:ekr.20050602205810.4:colorRangeWithTag
    def colorRangeWithTag (self,s,i,j,tag):
    
        '''Add an item to the tagList if colorizing is enabled.'''
        
        # g.convertPythonIndexToRowCol could be slow for large s.
        if self.flag:
            row,col = g.convertPythonIndexToRowCol(s,i)
            x1 = '%d.%d' % (row+1,col)
            row,col = g.convertPythonIndexToRowCol(s,j)
            x2 = '%d.%d' % (row+1,col)
            self.tagList.append((tag,x1,x2),)
    #@nonl
    #@-node:ekr.20050602205810.4:colorRangeWithTag
    #@+node:ekr.20060510154647:pause
    def pause (self,s,i):
        
        '''Pause the colorOneChunk method by queuing it up at idle time.'''
        self.chunk_s, self.chunk_i = s,i
        self.queue_count += 1
        self.c.frame.top.after_idle(self.colorOneChunk)
        # g.trace(self.queue_count)
    #@nonl
    #@-node:ekr.20060510154647:pause
    #@+node:ekr.20060507192431:quickColor
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
    #@-node:ekr.20060507192431:quickColor
    #@-node:ekr.20050529150436:Colorizer code
    #@+node:ekr.20060503153603.1:jEdit matchers (todo: exclude_match)
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
    #@+node:ekr.20050529190857:match_keywords
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
    #@-node:ekr.20050529190857:match_keywords
    #@+node:ekr.20050529182335:match_regexp_helper (TO DO)
    def match_regexp_helper (self,s,i,seq):
        
        '''Return the length of the matching text if seq (a regular expression) matches the present position.'''
        
        ### We may want to return a match object too.
        
        return 0 ### Not ready yet.
    #@nonl
    #@-node:ekr.20050529182335:match_regexp_helper (TO DO)
    #@+node:ekr.20050601045930:match_eol_span
    def match_eol_span (self,s,i,kind,seq,
        at_line_start,at_whitespace_end,at_word_start,
        delegate,exclude_match):
        
        '''Succeed if seq matches s[i:]'''
    
        if at_line_start and i != 0 and s[i-1] != '\n': return 0
        if at_whitespace_end and i != g.skip_ws(s,0): return 0
        if at_word_start and i > 0 and s[i-1] not in self.word_chars: return 0
        
        # g.trace(i,repr(s[i]),repr(seq))
    
        if g.match(s,i,seq):
            j = g.skip_to_end_of_line(s,i)
            self.colorRangeWithTag(s,i,j,kind)
            self.prev = (i,j,kind)
            return j - i 
        else:
            return 0
    #@-node:ekr.20050601045930:match_eol_span
    #@+node:ekr.20050601063317:match_eol_span_regexp
    def match_eol_span_regexp (self,s,i,kind,regex,hash_char,
        at_line_start,at_whitespace_end,at_word_start,
        delegate,exclude_match):
        
        '''Succeed if the regular expression regex matches s[i:].'''
    
        if at_line_start and i != 0 and s[i-1] != '\n': return 0
        if at_whitespace_end and i != g.skip_ws(s,0): return 0
        if at_word_start and i > 0 and s[i-1] not in self.word_chars: return 0
        
        # Test hash_char first to increase speed.
        if i < len(s) and s[i] == hash_char:
            n = self.match_regexp_helper(s,i,regex)
            if n > 0:
                j = g.skip_to_end_of_line(s,i)
                self.colorRangeWithTag(s,i,j,kind)
                self.prev = (i,j,kind)
                return j - i
            else:
                return 0
        else:
            return 0
    #@nonl
    #@-node:ekr.20050601063317:match_eol_span_regexp
    #@+node:ekr.20060503173247:match_mark_following
    def match_mark_following (self,s,i,kind,pattern,
        at_line_start,at_whitespace_end,at_word_start,exclude_match):
        
        '''Succeed if s[i:] matches pattern.'''
    
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
    #@-node:ekr.20060503173247:match_mark_following
    #@+node:ekr.20060503173247.1:match_mark_previous
    def match_mark_previous (self,s,i,kind,pattern,
        at_line_start,at_whitespace_end,at_word_start,exclude_match):
        
        '''Return the length of a matched SEQ or 0 if no match.
    
        'at_line_start':    True: sequence must start the line.
        'at_whitespace_end':True: sequence must be first non-whitespace text of the line.
        'at_word_start':    True: sequence must start a word.'''
    
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
    #@-node:ekr.20060503173247.1:match_mark_previous
    #@+node:ekr.20050529182335.1:match_seq
    def match_seq (self,s,i,kind,seq,
        at_line_start,at_whitespace_end,at_word_start,delegate):
        
        '''Succeed if s[:] mathces seq.'''
    
        if at_line_start and i != 0 and s[i-1] != '\n': return 0
        if at_whitespace_end and i != g.skip_ws(s,0): return 0
        if at_word_start and i > 0 and s[i-1] not in self.word_chars: return 0
    
        if g.match(s,i,seq):
            j = i + len(seq)
            self.colorRangeWithTag(s,i,j,kind)
            self.prev = (i,j,kind)
            return j - i
        else:
            return 0
    #@nonl
    #@-node:ekr.20050529182335.1:match_seq
    #@+node:ekr.20050529215620:match_seq_regexp
    def match_seq_regexp (self,s,i,kind,regexp,hash_char,
        at_line_start,at_whitespace_end,at_word_start,delegate):
        
        '''Succeed if the regular expression regexp matches at s[i:].'''
    
        if at_line_start and i != 0 and s[i-1] != '\n': return 0
        if at_whitespace_end and i != g.skip_ws(s,0): return 0
        if at_word_start and i > 0 and s[i-1] not in self.word_chars: return 0
        
        # Test hash_char first to increase speed.
        if i < len(s) and s[i] == hash_char:
            j = self.match_regexp_helper(s,i,regexp)
            self.colorRangeWithTag(s,i,j,kind)
            self.prev = (i,j,kind)
        else:
            return 0
    #@nonl
    #@-node:ekr.20050529215620:match_seq_regexp
    #@+node:ekr.20050529185208.2:match_span
    def match_span (self,s,i,kind,begin,end,
        at_line_start,at_whitespace_end,at_word_start,
        delegate,exclude_match,
        no_escape,no_line_break,no_word_break):
    
        '''Succeed if s[i:] starts with 'begin' and contains a following 'end'.'''
        
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
                self.colorRangeWithTag(s,i,j,kind)
                self.prev = (i,j,kind)
                return j - i
        else:
            return 0
    #@nonl
    #@-node:ekr.20050529185208.2:match_span
    #@+node:ekr.20050529215732:match_span_regexp
    def match_span_regexp (self,s,i,kind,begin,end,hash_char,
        at_line_start,at_whitespace_end,at_word_start,
        delegate,exclude_match):
            
        '''Succeed if s[i:] starts with 'begin' ( a regular expression) and contains a following 'end'.'''
        
        if at_line_start and i != 0 and s[i-1] != '\n': return 0
        if at_whitespace_end and i != g.skip_ws(s,0): return 0
        if at_word_start and i > 0 and s[i-1] not in self.word_chars: return 0
        
        # Test hash_char first to increase speed.
        if i < len(s) and s[i] == hash_char:
            n = self.match_regexp_helper(s,i,begin)
            # We may have to allow $n here, in which case we must use a regex object?
            if n > 0 and g.match(s,i+n,end):
                self.colorRangeWithTag(s,i,j,kind)
                self.prev = (i,j,kind)
                return n + len(end)
        else:
            return 0
    #@nonl
    #@-node:ekr.20050529215732:match_span_regexp
    #@-node:ekr.20060503153603.1:jEdit matchers (todo: exclude_match)
    #@+node:ekr.20050529143413.89:Utils
    #@+at 
    #@nonl
    # These methods are like the corresponding functions in leoGlobals.py 
    # except they issue no error messages.
    #@-at
    #@+node:ekr.20060503171558:computeRulesetName
    def computeRulesetName (self,language,name='main'):
        
        return '%s_%s' % (language,name)
    #@nonl
    #@-node:ekr.20060503171558:computeRulesetName
    #@+node:ekr.20050529143413.90:index
    def index (self,i):
        
        return self.body.convertRowColumnToIndex(self.line_index,i)
        
    #@nonl
    #@-node:ekr.20050529143413.90:index
    #@+node:ekr.20050529143413.86:removeAllImages
    def removeAllImages (self):
        
        for photo,image,line_index,i in self.image_references:
            try:
                self.body.deleteCharacter(image)
            except:
                pass # The image may have been deleted earlier.
        
        self.image_references = []
    #@nonl
    #@-node:ekr.20050529143413.86:removeAllImages
    #@+node:ekr.20050529143413.80:removeAllTags
    def removeAllTags (self):
        
        # g.trace(g.callers())
        
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
    #@-node:ekr.20050529143413.80:removeAllTags
    #@+node:ekr.20050529143413.81:scanColorDirectives
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
            #@+node:ekr.20050529143413.82:<< Test for @comment or @language >>
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
            #@-node:ekr.20050529143413.82:<< Test for @comment or @language >>
            #@nl
            #@        << Test for @root, @root-doc or @root-code >>
            #@+node:ekr.20050529143413.83:<< Test for @root, @root-doc or @root-code >>
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
            #@-node:ekr.20050529143413.83:<< Test for @root, @root-doc or @root-code >>
            #@nl
    
        return self.language # For use by external routines.
    #@nonl
    #@-node:ekr.20050529143413.81:scanColorDirectives
    #@+node:ekr.20050529143413.29:setFontFromConfig
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
    #@-node:ekr.20050529143413.29:setFontFromConfig
    #@+node:ekr.20060507175312:tagAll
    def tagAll (self):
        
        for tag,x1,x2 in self.tagList:
            self.body.tag_add(tag,x1,x2)
    #@nonl
    #@-node:ekr.20060507175312:tagAll
    #@-node:ekr.20050529143413.89:Utils
    #@-others

class colorizer (baseColorizer):
    pass
#@nonl
#@-node:ekr.20050606214036:class colorizer (baseColorizer)
#@-others

#@<< class nullColorizer (colorizer) >>
#@+node:ekr.20050606213440:<< class nullColorizer (colorizer) >>
class nullColorizer (colorizer):
    
    """A do-nothing colorer class"""
    
    #@    @+others
    #@+node:ekr.20050606213440.1:__init__
    def __init__ (self,c):
        
        colorizer.__init__(self,c) # init the base class.
    
        self.c = c
        self.enabled = False
    #@-node:ekr.20050606213440.1:__init__
    #@+node:ekr.20050606213440.2:entry points
    def colorize(self,p,incremental=False): pass
    
    def disable(self): pass
        
    def enable(self): pass
        
    def idle_colorize(self): pass
            
    def recolor_range(self,p,leading,trailing): pass
    
    def scanColorDirectives(self,p): pass
        
    def schedule(self,p,incremental=0): pass
    
    def updateSyntaxColorer (self,p): pass
    #@nonl
    #@-node:ekr.20050606213440.2:entry points
    #@-others
#@nonl
#@-node:ekr.20050606213440:<< class nullColorizer (colorizer) >>
#@nl
#@nonl
#@-node:ekr.20050529142847:@thin __jEdit_colorizer__.py
#@-leo
