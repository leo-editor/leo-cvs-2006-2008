#@+leo-ver=4-thin
#@+node:ekr.20060123151617:@thin leoFind.py
'''Leo's gui-independent find classes.'''

#@@language python
#@@tabwidth -4
#@@pagewidth 80

import leoGlobals as g
import re

#@<< Theory of operation of find/change >>
#@+node:ekr.20031218072017.2414:<< Theory of operation of find/change >>
#@+at 
#@nonl
# The find and change commands are tricky; there are many details that must be 
# handled properly. This documentation describes the leo.py code. Previous 
# versions of Leo used an inferior scheme.  The following principles govern 
# the leoFind class:
# 
# 1. Find and Change commands initialize themselves using only the state of 
# the present Leo window. In particular, the Find class must not save internal 
# state information from one invocation to the next. This means that when the 
# user changes the nodes, or selects new text in headline or body text, those 
# changes will affect the next invocation of any Find or Change command. 
# Failure to follow this principle caused all kinds of problems in the Borland 
# and Macintosh codes. There is one exception to this rule: we must remember 
# where interactive wrapped searches start. This principle simplifies the code 
# because most ivars do not persist. However, each command must ensure that 
# the Leo window is left in a state suitable for restarting the incremental 
# (interactive) Find and Change commands. Details of initialization are 
# discussed below.
# 
# 2. The Find and Change commands must not change the state of the outline or 
# body pane during execution. That would cause severe flashing and slow down 
# the commands a great deal. In particular, c.selectVnode and c.editPosition 
# methods must not be called while looking for matches.
# 
# 3. When incremental Find or Change commands succeed they must leave the Leo 
# window in the proper state to execute another incremental command. We 
# restore the Leo window as it was on entry whenever an incremental search 
# fails and after any Find All and Change All command.
# 
# Initialization involves setting the c, p, in_headline, wrapping and s_ctrl 
# ivars. Setting in_headline is tricky; we must be sure to retain the state of 
# the outline pane until initialization is complete. Initializing the Find All 
# and Change All commands is much easier because such initialization does not 
# depend on the state of the Leo window.
# 
# Using Tk.Text widgets for both headlines and body text results in a huge 
# simplification of the code. Indeed, the searching code does not know whether 
# it is searching headline or body text. The search code knows only that 
# s_ctrl is a Tk.Text widget that contains the text to be searched or changed 
# and the insert and sel Tk attributes of self.search_text indicate the range 
# of text to be searched. Searching headline and body text simultaneously is 
# complicated. The selectNextPosition() method handles the many details 
# involved by setting s_ctrl and its insert and sel attributes.
#@-at
#@-node:ekr.20031218072017.2414:<< Theory of operation of find/change >>
#@nl

#@+others
#@+node:ekr.20070105092022.1:class searchWidget
class searchWidget:
    
    '''A class to simulating a hidden Tk Text widget.'''

    def __repr__(self):
        return 'searchWidget id: %s' % (id(self))
        
    #@    @+others
    #@+node:ekr.20070105092438:ctor
    def __init__ (self,*args,**keys):
        
        # g.trace ('searchWidget',g.callers())
        
        self.s = ''    # The widget text
        self.i = 0     # The insert point
        self.sel = 0,0 # The selection range
    #@-node:ekr.20070105092438:ctor
    #@+node:ekr.20070105093138:getters
    def getAllText (self):          return self.s
    def getInsertPoint (self):      return self.i       # Returns Python index.
    def getSelectionRange(self):    return self.sel     # Returns Python indices.
    
    #@-node:ekr.20070105093138:getters
    #@+node:ekr.20070105102419:setters
    def delete(self,i,j=None):
        i = self.toPythonIndex(i)
        if j is None: j = i + 1
        else: j = self.toPythonIndex(j)
        self.s = self.s[:i] + self.s[j:]
    
    def insert(self,i,s):
        if not s: return
        i = self.toPythonIndex(i)
        self.s = self.s[:i] + s + self.s[i:]
        self.i = i
        self.sel = i,i
        
    def setAllText (self,s):
        self.s = s
        self.i = 0
        self.sel = 0,0
    
    def setInsertPoint (self,i):
        self.i = i
    
    def setSelectionRange (self,i,j,insert=None):
        self.sel = self.toPythonIndex(i),self.toPythonIndex(j)
        if insert is not None:
            self.i = self.toPythonIndex(insert)
    #@-node:ekr.20070105102419:setters
    #@+node:ekr.20070105092022.4:toPythonIndex
    def toPythonIndex (self,i):
        
        '''Make sure i is a Python index.'''
    
        if i is None:
            return 0
    
        elif type(i) in (type('a'),type(u'a')):
            row,col = i.split('.')
            row,col = int(row),int(col)
            row -= 1
            i = g.convertRowColToPythonIndex(self.s,row,col)
    
        return i
    #@-node:ekr.20070105092022.4:toPythonIndex
    #@-others
#@nonl
#@-node:ekr.20070105092022.1:class searchWidget
#@+node:ekr.20061212084717:class leoFind
class leoFind:

    """The base class for Leo's Find commands."""

    #@    @+others
    #@+node:ekr.20031218072017.3053:leoFind.__init__
    def __init__ (self,c,title=None):
    
        self.c = c
        
        # Spell checkers use this class, so we can't always compute a title.
        if title:
            self.title = title
        else:
            #@        << compute self.title >>
            #@+node:ekr.20041121145452:<< compute self.title >>
            if not c.mFileName:
                s = "untitled"
            else:
                path,s = g.os_path_split(c.mFileName)
                
            self.title = "Find/Change for %s" %  s
            #@-node:ekr.20041121145452:<< compute self.title >>
            #@nl
    
        #@    << init the gui-independent ivars >>
        #@+node:ekr.20031218072017.3054:<< init the gui-independent ivars >>
        self.wrapPosition = None
        self.onlyPosition = None
        self.find_text = ""
        self.change_text = ""
        self.unstick = False
        
        #@+at
        # New in 4.3:
        # - These are the names of leoFind ivars. (no more _flag hack).
        # - There are no corresponding commander ivars to keep in synch 
        # (hurray!)
        # - These ivars are inited (in the subclass by init) when this class 
        # is created.
        # - These ivars are updated by update_ivars just before doing any 
        # find.
        #@-at
        #@@c
        
        #@<< do dummy initialization to keep Pychecker happy >>
        #@+node:ekr.20050123164539:<< do dummy initialization to keep Pychecker happy >>
        if 1:
            self.batch = None
            self.clone_find_all = None
            self.ignore_case = None
            self.node_only = None
            self.pattern_match = None
            self.search_headline = None
            self.search_body = None
            self.suboutline_only = None
            self.mark_changes = None
            self.mark_finds = None
            self.reverse = None
            self.script_search = None
            self.script_change = None
            self.selection_only = None
            self.wrap = None
            self.whole_word = None
        #@-node:ekr.20050123164539:<< do dummy initialization to keep Pychecker happy >>
        #@nl
        
        self.intKeys = [
            "batch","ignore_case", "node_only",
            "pattern_match", "search_headline", "search_body",
            "suboutline_only", "mark_changes", "mark_finds", "reverse",
            "script_search","script_change","selection_only",
            "wrap", "whole_word",
        ]
        
        self.newStringKeys = ["radio-find-type", "radio-search-scope"]
        
        # Ivars containing internal state...
        self.c = None # The commander for this search.
        self.clone_find_all = False
        self.p = None # The position being searched.  Never saved between searches!
        self.in_headline = False # True: searching headline text.
        self.s_ctrl = searchWidget() # The search text for this search.
        self.wrapping = False # True: wrapping is enabled.
            # This is _not_ the same as self.wrap for batch searches.
        
        #@+at 
        #@nonl
        # Initializing a wrapped search is tricky.  The search() method will 
        # fail if p==wrapPosition and pos >= wrapPos.  selectNextPosition() 
        # will fail if p == wrapPosition.  We set wrapPos on entry, before the 
        # first search.  We set wrapPosition in selectNextPosition after the 
        # first search fails.  We also set wrapPosition on exit if the first 
        # search suceeds.
        #@-at
        #@@c
        
        self.wrapPosition = None # The start of wrapped searches: persists between calls.
        self.onlyPosition = None # The starting node for suboutline-only searches.
        self.wrapPos = None # The starting position of the wrapped search: persists between calls.
        self.errors = 0
        self.selStart = self.selEnd = None # For selection-only searches.
        #@-node:ekr.20031218072017.3054:<< init the gui-independent ivars >>
        #@nl
    #@+node:ekr.20031218072017.2059:find.init
    def init (self,c):
    
        # N.B.: separate c.ivars are much more convenient than a dict.
        for key in self.intKeys:
            # New in 4.3: get ivars from @settings.
            val = c.config.getBool(key)
            setattr(self,key,val)
            val = g.choose(val,1,0) # Work around major Tk problem.
            self.svarDict[key].set(val)
            # g.trace(key,val)
    
        #@    << set find/change widgets >>
        #@+node:ekr.20031218072017.2060:<< set find/change widgets >>
        self.find_ctrl.delete(0,"end")
        self.change_ctrl.delete(0,"end")
        
        # New in 4.3: Get setting from @settings.
        for w,setting,defaultText in (
            (self.find_ctrl,"find_text",'<find pattern here>'),
            (self.change_ctrl,"change_text",''),
        ):
            s = c.config.getString(setting)
            if not s: s = defaultText
            w.insert("end",s)
        #@-node:ekr.20031218072017.2060:<< set find/change widgets >>
        #@nl
        #@    << set radio buttons from ivars >>
        #@+node:ekr.20031218072017.2061:<< set radio buttons from ivars >>
        found = False
        for var,setting in (
            ("pattern_match","pattern-search"),
            ("script_search","script-search")):
            val = self.svarDict[var].get()
            if val:
                self.svarDict["radio-find-type"].set(setting)
                found = True ; break
        if not found:
            self.svarDict["radio-find-type"].set("plain-search")
            
        found = False
        for var,setting in (
            ("suboutline_only","suboutline-only"),
            ("node_only","node-only"),
            # ("selection_only","selection-only"),
        ):
            val = self.svarDict[var].get()
            if val:
                self.svarDict["radio-search-scope"].set(setting)
                found = True ; break
        if not found:
            self.svarDict["radio-search-scope"].set("entire-outline")
        #@-node:ekr.20031218072017.2061:<< set radio buttons from ivars >>
        #@nl
    #@-node:ekr.20031218072017.2059:find.init
    #@-node:ekr.20031218072017.3053:leoFind.__init__
    #@+node:ekr.20060123065756.1:Top Level Buttons
    #@+node:ekr.20031218072017.3057:changeAllButton
    # The user has pushed the "Change All" button from the find panel.
    
    def changeAllButton(self):
    
        c = self.c
        self.setup_button()
        c.clearAllVisited() # Clear visited for context reporting.
    
        if self.script_change:
            self.doChangeAllScript()
        elif self.selection_only:
            self.change()
        else:
            self.changeAll()
    #@-node:ekr.20031218072017.3057:changeAllButton
    #@+node:ekr.20031218072017.3056:changeButton
    # The user has pushed the "Change" button from the find panel.
    
    def changeButton(self):
    
        self.setup_button()
    
        if self.script_change:
            self.doChangeScript()
        else:
            self.change()
    #@-node:ekr.20031218072017.3056:changeButton
    #@+node:ekr.20031218072017.3058:changeThenFindButton
    # The user has pushed the "Change Then Find" button from the find panel.
    
    def changeThenFindButton(self):
    
        self.setup_button()
    
        if self.script_change:
            self.doChangeScript()
            if self.script_search:
                self.doFindScript()
            else:
                self.findNext()
        else:
            if self.script_search:
                self.change()
                self.doFindScript()
            else:
                self.changeThenFind()
    #@-node:ekr.20031218072017.3058:changeThenFindButton
    #@+node:ekr.20031218072017.3060:findAllButton
    # The user has pushed the "Find All" button from the find panel.
    
    def findAllButton(self):
    
        c = self.c
        self.setup_button()
        c.clearAllVisited() # Clear visited for context reporting.
    
        if self.script_search:
            self.doFindAllScript()
        elif self.selection_only:
            self.findNext()
        else:
            self.findAll()
    #@-node:ekr.20031218072017.3060:findAllButton
    #@+node:ekr.20031218072017.3059:findButton
    # The user has pushed the "Find" button from the find panel.
    
    def findButton(self):
    
        self.setup_button()
    
        if self.script_search:
            self.doFindScript()
        else:
            self.findNext()
    #@-node:ekr.20031218072017.3059:findButton
    #@+node:ekr.20031218072017.3065:setup_button
    # Initializes a search when a button is pressed in the Find panel.
    
    def setup_button(self):
        
        c = self.c
        self.p = c.currentPosition()
    
        c.bringToFront()
        if 0: # We _must_ retain the editing status for incremental searches!
            c.endEditing()
    
        self.update_ivars()
    #@-node:ekr.20031218072017.3065:setup_button
    #@-node:ekr.20060123065756.1:Top Level Buttons
    #@+node:ekr.20031218072017.3055:Top Level Commands
    #@+node:ekr.20031218072017.3061:changeCommand
    # The user has selected the "Replace" menu item.
    
    def changeCommand(self,c):
    
        self.setup_command()
    
        if self.script_search:
            self.doChangeScript()
        else:
            self.change()
    #@-node:ekr.20031218072017.3061:changeCommand
    #@+node:ekr.20031218072017.3062:changeThenFindCommand
    # The user has pushed the "Change Then Find" button from the Find menu.
    
    def changeThenFindCommand(self,c):
    
        self.setup_command()
    
        if self.script_search:
            self.doChangeScript()
            self.doFindScript()
        else:
            self.changeThenFind()
    #@-node:ekr.20031218072017.3062:changeThenFindCommand
    #@+node:ekr.20051013084200.1:dismiss: defined in subclass class
    def dismiss (self):
        pass
    #@-node:ekr.20051013084200.1:dismiss: defined in subclass class
    #@+node:ekr.20031218072017.3063:findNextCommand
    # The user has selected the "Find Next" menu item.
    
    def findNextCommand(self,c):
    
        self.setup_command()
    
        if self.script_search:
            self.doFindScript()
        else:
            self.findNext()
    #@-node:ekr.20031218072017.3063:findNextCommand
    #@+node:ekr.20031218072017.3064:findPreviousCommand
    # The user has selected the "Find Previous" menu item.
    
    def findPreviousCommand(self,c):
    
        self.setup_command()
    
        self.reverse = not self.reverse
    
        if self.script_search:
            self.doFindScript()
        else:
            self.findNext()
    
        self.reverse = not self.reverse
    #@-node:ekr.20031218072017.3064:findPreviousCommand
    #@+node:EKR.20040503070514:handleUserClick
    def handleUserClick (self,p):
        
        """Reset suboutline-only search when the user clicks a headline."""
        
        try:
            if self.c and self.suboutline_only:
                # g.trace(p)
                self.onlyPosition = p.copy()
        except: pass
    #@-node:EKR.20040503070514:handleUserClick
    #@+node:ekr.20031218072017.3066:setup_command
    # Initializes a search when a command is invoked from the menu.
    
    def setup_command(self):
        
        # g.trace('leoFind')
    
        if 0: # We _must_ retain the editing status for incremental searches!
            self.c.endEditing()
    
        self.update_ivars()
    #@-node:ekr.20031218072017.3066:setup_command
    #@-node:ekr.20031218072017.3055:Top Level Commands
    #@+node:ekr.20031218072017.3067:Find/change utils
    #@+node:ekr.20031218072017.2293:batchChange (sets start of change-all group)
    #@+at 
    #@nonl
    # This routine performs a single batch change operation, updating the head 
    # or body string of p and leaving the result in s_ctrl.  We update the 
    # body if we are changing the body text of c.currentVnode().
    # 
    # s_ctrl contains the found text on entry and contains the changed text on 
    # exit.  pos and pos2 indicate the selection.  The selection will never be 
    # empty. NB: we can not assume that self.p is visible.
    #@-at
    #@@c
    
    def batchChange (self,pos1,pos2):
    
        c = self.c ; u = c.undoer
        p = self.p ; w = self.s_ctrl
        # Replace the selection with self.change_text
        if pos1 > pos2: pos1,pos2=pos2,pos1
        s = w.getAllText()
        if pos1 != pos2: w.delete(pos1,pos2)
        w.insert(pos1,self.change_text)
        # Update the selection.
        insert=g.choose(self.reverse,pos1,pos1+len(self.change_text))
        w.setSelectionRange(insert,insert)
        w.setInsertPoint(insert)
        # Update the node
        s = w.getAllText() # Used below.
        if self.in_headline:
            #@        << change headline >>
            #@+node:ekr.20031218072017.2294:<< change headline >>
            if len(s) > 0 and s[-1]=='\n': s = s[:-1]
            
            if s != p.headString():
                
                undoData = u.beforeChangeNodeContents(p)
            
                p.initHeadString(s)
                if self.mark_changes:
                    p.setMarked()
                p.setDirty()
                if not c.isChanged():
                    c.setChanged(True)
                
                u.afterChangeNodeContents(p,'Change Headline',undoData)
            #@-node:ekr.20031218072017.2294:<< change headline >>
            #@nl
        else:
            #@        << change body >>
            #@+node:ekr.20031218072017.2295:<< change body >>
            if len(s) > 0 and s[-1]=='\n': s = s[:-1]
            
            if s != p.bodyString():
                
                undoData = u.beforeChangeNodeContents(p)
            
                c.setBodyString(p,s)
                if self.mark_changes:
                    p.setMarked()
                p.setDirty()
                if not c.isChanged():
                    c.setChanged(True)
                 
                u.afterChangeNodeContents(p,'Change Body',undoData)
            #@-node:ekr.20031218072017.2295:<< change body >>
            #@nl
    #@-node:ekr.20031218072017.2293:batchChange (sets start of change-all group)
    #@+node:ekr.20031218072017.3068:change
    def change(self,event=None):
    
        if self.checkArgs():
            self.initInHeadline()
            self.changeSelection()
    #@-node:ekr.20031218072017.3068:change
    #@+node:ekr.20031218072017.3069:changeAll (sets end of change-all group)
    def changeAll(self):
        
        g.trace(g.callers())
    
        c = self.c ; u = c.undoer ; undoType = 'Change All'
        current = c.currentPosition()
        w = self.s_ctrl
        if not self.checkArgs(): return
        self.initInHeadline()
        saveData = self.save()
        self.initBatchCommands()
        count = 0
        c.beginUpdate()
        try: # In update...
            u.beforeChangeGroup(current,undoType)
            while 1:
                pos1, pos2 = self.findNextMatch()
                if pos1 is None: break
                count += 1
                self.batchChange(pos1,pos2)
                s = w.getAllText()
                i,j = g.getLine(s,pos1)
                line = s[i:j]
                self.printLine(line,allFlag=True)
            p = c.currentPosition()
            u.afterChangeGroup(p,undoType,reportFlag=True)
            g.es("changed: %d instances" % (count))
        finally:
            c.endUpdate()
            self.restore(saveData)
    #@-node:ekr.20031218072017.3069:changeAll (sets end of change-all group)
    #@+node:ekr.20031218072017.3070:changeSelection
    # Replace selection with self.change_text.
    # If no selection, insert self.change_text at the cursor.
    
    def changeSelection(self):
        
        c = self.c ; p = self.p
        w = g.choose(self.in_headline,c.edit_widget(p),c.frame.bodyCtrl)
        oldSel = sel = w.getSelectionRange()
        start,end = sel
        if start > end: start,end = end,start
        if start == end:
            g.es("No text selected") ; return False
            
        # g.trace(start,end)
    
        # Replace the selection in _both_ controls.
        start,end = oldSel
        change_text = self.change_text
        
        # Perform regex substitutions of \1, \2, ...\9 in the change text.
        if self.pattern_match and self.match_obj:
            groups = self.match_obj.groups()
            if groups:
                change_text = self.makeRegexSubs(change_text,groups)
        # change_text = change_text.replace('\\n','\n').replace('\\t','\t')
        change_text = self.replaceBackSlashes(change_text)
    
        for w2 in (w,self.s_ctrl):
            if start != end: w2.delete(start,end)
            w2.insert(start,change_text)
            w2.setInsertPoint(g.choose(self.reverse,start,start+len(change_text)))
    
        # Update the selection for the next match.
        w.setSelectionRange(start,start+len(change_text))
        c.widgetWantsFocus(w)
    
        # No redraws here: they would destroy the headline selection.
        c.beginUpdate()
        try:
            if self.mark_changes:
                p.setMarked()
            if self.in_headline:
                c.frame.tree.onHeadChanged(p,'Change')
            else:
                c.frame.body.onBodyChanged('Change',oldSel=oldSel)
        finally:
            c.endUpdate(False)
            c.frame.tree.drawIcon(p) # redraw only the icon.
         
        return True
    #@+node:ekr.20060526201951:makeRegexSubs
    def makeRegexSubs(self,s,groups):
        
        '''Carefully substitute group[i-1] for \i strings in s.
        The group strings may contain \i strings: they are *not* substituted.'''
        
        digits = '123456789'
        result = [] ; n = len(s)
        i = j = 0 # s[i:j] is the text between \i markers.
        while j < n:
            k = s.find('\\',j)
            if k == -1 or k + 1 >= n:
                break
            j = k + 1 ; ch = s[j]
            if ch in digits:
                j += 1
                result.append(s[i:k]) # Append up to \i
                i = j
                gn = int(ch)-1
                if gn < len(groups):
                    result.append(groups[gn]) # Append groups[i-1]
                else:
                    result.append('\\%s' % ch) # Append raw '\i'
        result.append(s[i:])
        return ''.join(result)
    #@-node:ekr.20060526201951:makeRegexSubs
    #@-node:ekr.20031218072017.3070:changeSelection
    #@+node:ekr.20031218072017.3071:changeThenFind
    def changeThenFind(self):
    
        if not self.checkArgs():
            return
    
        self.initInHeadline()
        if self.changeSelection():
            self.findNext(False) # don't reinitialize
    #@-node:ekr.20031218072017.3071:changeThenFind
    #@+node:ekr.20031218072017.2417:doChange...Script
    def doChangeScript (self):
    
        g.app.searchDict["type"] = "change"
        self.runChangeScript()
    
    def doChangeAllScript (self):
    
        """The user has just pressed the Change All button with script-change box checked.
    
        N.B. Only this code is executed."""
    
        g.app.searchDict["type"] = "changeAll"
        while 1:
            self.runChangeScript()
            if not g.app.searchDict.get("continue"):
                break
    
    def runChangeScript (self):
    
        try:
            assert(self.script_change)
            exec self.change_text in {} # Use {} to get a pristine environment.
        except:
            g.es("exception executing change script")
            g.es_exception(full=False)
            g.app.searchDict["continue"] = False # 2/1/04
    #@-node:ekr.20031218072017.2417:doChange...Script
    #@+node:ekr.20031218072017.3072:doFind...Script
    def doFindScript (self):
    
        g.app.searchDict["type"] = "find"
        self.runFindScript()
    
    def doFindAllScript (self):
    
        """The user has just pressed the Find All button with script-find radio button checked.
    
        N.B. Only this code is executed."""
    
        g.app.searchDict["type"] = "findAll"
        while 1:
            self.runFindScript()
            if not g.app.searchDict.get("continue"):
                break
    
    def runFindScript (self):
    
        try:
            exec self.find_text in {} # Use {} to get a pristine environment.
        except:
            g.es("exception executing find script")
            g.es_exception(full=False)
            g.app.searchDict["continue"] = False # 2/1/04
    #@-node:ekr.20031218072017.3072:doFind...Script
    #@+node:ekr.20031218072017.3073:findAll
    def findAll(self):
    
        c = self.c ; w = self.s_ctrl ; u = c.undoer
        undoType = 'Clone Find All'
        if not self.checkArgs():
            return
        self.initInHeadline()
        data = self.save()
        self.initBatchCommands()
        count = 0 ; clones = []
        while 1:
            pos, newpos = self.findNextMatch()
            if pos is None: break
            count += 1
            s = w.getAllText()
            i,j = g.getLine(s,pos)
            line = s[i:j]
            if not self.clone_find_all:
                self.printLine(line,allFlag=True)
            if self.clone_find_all and self.p.v.t not in clones:
                # g.trace(self.p.v.t,self.p.headString())
                if not clones:
                    #@                << create the found node and begin the undo group >>
                    #@+node:ekr.20051113110735:<< create the found node and begin the undo group >>
                    u.beforeChangeGroup(c.currentPosition(),undoType)
                    
                    undoData = u.beforeInsertNode(c.currentPosition())
                    
                    oldRoot = c.rootPosition()
                    found = oldRoot.insertAfter()
                    found.moveToRoot(oldRoot)
                    c.setHeadString(found,'Found: ' + self.find_text)
                    
                    u.afterInsertNode(found,undoType,undoData,dirtyVnodeList=[])
                    #@-node:ekr.20051113110735:<< create the found node and begin the undo group >>
                    #@nl
                clones.append(self.p.v.t)
                #@            << create a clone of p under the find node >>
                #@+node:ekr.20051113110851:<< create a clone of p under the find node >>
                undoData = u.beforeCloneNode(self.p)
                q = self.p.clone()
                q.moveToLastChildOf(found)
                u.afterCloneNode(q,undoType,undoData,dirtyVnodeList=[])
                #@-node:ekr.20051113110851:<< create a clone of p under the find node >>
                #@nl
        if self.clone_find_all and clones:
            c.setRootPosition(c.findRootPosition(found)) # New in 4.4.2.
            u.afterChangeGroup(found,undoType,reportFlag=True) 
            c.selectPosition(found) # Recomputes root.
            c.setChanged(True)
              
        c.redraw_now()
        g.es("found: %d matches" % (count))
        self.restore(data)
    #@-node:ekr.20031218072017.3073:findAll
    #@+node:ekr.20031218072017.3074:findNext
    def findNext(self,initFlag=True):
    
        c = self.c
        if not self.checkArgs():
            return
    
        if initFlag:
            self.initInHeadline()
            data = self.save()
            self.initInteractiveCommands()
        else:
            data = self.save()
    
        pos, newpos = self.findNextMatch()
    
        if pos is not None:
            self.showSuccess(pos,newpos)
        else:
            if self.wrapping:
                g.es("end of wrapped search")
            else:
                g.es("not found: " + "'" + self.find_text + "'")
            self.restore(data)
    #@-node:ekr.20031218072017.3074:findNext
    #@+node:ekr.20031218072017.3075:findNextMatch
    # Resumes the search where it left off.
    # The caller must call set_first_incremental_search or set_first_batch_search.
    
    def findNextMatch(self):
    
        c = self.c
    
        if not self.search_headline and not self.search_body:
            return None, None
    
        if len(self.find_text) == 0:
            return None, None
    
        p = self.p
        while p:
            pos, newpos = self.search()
            # g.trace('pos',pos,'p',p.headString(),g.callers())
            if pos is not None:
                if self.mark_finds:
                    p.setMarked()
                    c.frame.tree.drawIcon(p) # redraw only the icon.
                return pos, newpos
            elif self.errors:
                return None,None # Abort the search.
            elif self.node_only:
                return None,None # We are only searching one node.
            else:
                p = self.p = self.selectNextPosition()
        return None, None
    #@-node:ekr.20031218072017.3075:findNextMatch
    #@+node:ekr.20031218072017.3076:resetWrap
    def resetWrap (self,event=None):
    
        self.wrapPosition = None
        self.onlyPosition = None
    #@-node:ekr.20031218072017.3076:resetWrap
    #@+node:ekr.20031218072017.3077:search & helpers
    def search (self):
    
        """Search s_ctrl for self.find_text under the control of the
        whole_word, ignore_case, and pattern_match ivars.
        
        Returns (pos, newpos) or (None,None)."""
    
        c = self.c ; p = self.p ; w = self.s_ctrl
        index = w.getInsertPoint()
        
        s = w.getAllText()
        # g.trace(index,repr(s[index:index+20]))
        stopindex = g.choose(self.reverse,0,len(s)) # 'end' doesn't work here.
        pos,newpos = self.searchHelper(s,index,stopindex,self.find_text,
            backwards=self.reverse,nocase=self.ignore_case,
            regexp=self.pattern_match,word=self.whole_word)
        # g.trace('pos,newpos',pos,newpos)
        if pos == -1: return None,None
        #@    << fail if we are passed the wrap point >>
        #@+node:ekr.20060526140328:<< fail if we are passed the wrap point >>
        if self.wrapping and self.wrapPos and self.wrapPosition and p == self.wrapPosition:
        
            if self.reverse and pos < self.wrapPos:
                # g.trace("wrap done")
                return None, None
        
            if not self.reverse and newpos > self.wrapPos:
                return None, None
        #@-node:ekr.20060526140328:<< fail if we are passed the wrap point >>
        #@nl
        insert = g.choose(self.reverse,min(pos,newpos),max(pos,newpos))
        w.setSelectionRange(pos,newpos,insert=insert)
        return pos,newpos
    #@+node:ekr.20060526081931:searchHelper & allies
    def searchHelper (self,s,i,j,pattern,backwards,nocase,regexp,word,swapij=True):
        
        if swapij and backwards: i,j = j,i
            
        # g.trace(backwards,i,j,repr(s[i:i+20]))
    
        if not s[i:j] or not pattern:
            # g.trace('empty',i,j)
            return -1,-1
            
        if regexp:
            pos,newpos = self.regexHelper(s,i,j,pattern,backwards,nocase)
        elif backwards:
            pos,newpos = self.backwardsHelper(s,i,j,pattern,nocase,word)
        else:
            pos,newpos = self.plainHelper(s,i,j,pattern,nocase,word)
    
        return pos,newpos
    #@+node:ekr.20061207172210:patternLen
    #@-node:ekr.20061207172210:patternLen
    #@+node:ekr.20060526092203:regexHelper
    def regexHelper (self,s,i,j,pattern,backwards,nocase):
       
        try:
            flags = re.MULTILINE
            if nocase: flags |= re.IGNORECASE
            re_obj = re.compile(pattern,flags)
        except Exception:
            g.es('Invalid regular expression: %s' % (pattern),color='blue')
            self.errors += 1 # Abort the search.
            return -1, -1
            
        if backwards: # Scan to the last match.
            last_mo = None
            while 1:
                mo = re_obj.search(s,i,j)
                if mo is None: break
                i = mo.end()
                last_mo = mo
            self.match_obj = mo = last_mo
        else:
            self.match_obj = mo = re_obj.search(s,i,j)
            
        if mo is None:
            return -1, -1
        else:
            k  = mo.start()
            k2 = mo.end()
            if 0:
                g.trace('i: %d, j: %d k: %d, k2: %d, s[k:k2]: %s, len(s): %d, s[-1]: %s,' % (
                    i,j,k,k2,repr(s[k:k2]),len(s),repr(s[-1])))
            # g.trace('groups',mo.groups())
            if k == k2:
                return -1, -1 # A non-empty pattern can match an empty string.  Move on!
            else:
                return k, k2
    #@-node:ekr.20060526092203:regexHelper
    #@+node:ekr.20060526140744:backwardsHelper
    def backwardsHelper (self,s,i,j,pattern,nocase,word):
    
        if nocase:
            s = s.lower() ; pattern.lower()
        pattern = self.replaceBackSlashes(pattern)
        n = len(pattern)
        
        if word:
            while 1:
                k = s.rfind(pattern,i,j)
                # g.trace(i,j,k)
                if k == -1: return -1, -1
                if self.matchWord(s,k,pattern):
                    return k,k+n
                else:
                    j = max(0,k-1)
        else:
            k = s.rfind(pattern,i,j)
            # g.trace(i,j,k)
            if k == -1:
                return -1, -1
            else:
                return k,k+n
    #@-node:ekr.20060526140744:backwardsHelper
    #@+node:ekr.20060526093531:plainHelper
    #@@tabwidth 4
    
    def plainHelper (self,s,i,j,pattern,nocase,word):
        
        # g.trace(i,j,repr(s[i:i+20]),'pattern',repr(pattern),'word',repr(word))
        if nocase:
            s = s.lower() ; pattern = pattern.lower()
    	pattern = self.replaceBackSlashes(pattern)
        n = len(pattern)
        if word:
            while 1:
                k = s.find(pattern,i,j)
                # g.trace(k,n)
                if k == -1: return -1, -1
                elif self.matchWord(s,k,pattern):
                    return k, k + n
                else: i = k + n
        else:
            k = s.find(pattern,i,j)
            if k == -1:
                return -1, -1
            else:
                return k, k + n
    #@-node:ekr.20060526093531:plainHelper
    #@+node:ekr.20060526140744.1:matchWord
    def matchWord(self,s,i,pattern):
        
        pattern = self.replaceBackSlashes(pattern)
        if not s or not pattern or not g.match(s,i,pattern):
            return False
    
        pat1,pat2 = pattern[0],pattern[-1]
        # n = self.patternLen(pattern)
        n = len(pattern)
        ch1 = 0 <= i-1 < len(s) and s[i-1] or '.'
        ch2 = 0 <= i+n < len(s) and s[i+n] or '.'
        
        isWordPat1 = g.isWordChar(pat1)
        isWordPat2 = g.isWordChar(pat2)
        isWordCh1 = g.isWordChar(ch1)
        isWordCh2 = g.isWordChar(ch2)
        
        # g.trace('i',i,'ch1,ch2,pat',repr(ch1),repr(ch2),repr(pattern))
        
        if isWordPat1 and isWordCh1 or isWordPat2 and isWordCh2:
            return False
        else:
            return True
    #@-node:ekr.20060526140744.1:matchWord
    #@+node:ekr.20070105165924:replaceBackSlashes
    def replaceBackSlashes (self,s):
        
        '''Carefully replace backslashes in a search pattern.'''
        
        # This is NOT the same as s.replace('\\n','\n').replace('\\t','\t').replace('\\\\','\\')
        # because there is no rescanning.
        
        i = 0
        while i + 1 < len(s):
            if s[i] == '\\':
                ch = s[i+1]
                if ch == '\\':
                    s = s[:i] + s[i+1:] # replace \\ by \
                elif ch == 'n':
                    s = s[:i] + '\n' + s[i+2:] # replace the \n by a newline
                elif ch == 't':
                     s = s[:i] + '\t' + s[i+2:] # replace \t by a tab
                else:
                    i += 1 # Skip the escaped character.
            i += 1
        return s
    #@-node:ekr.20070105165924:replaceBackSlashes
    #@-node:ekr.20060526081931:searchHelper & allies
    #@-node:ekr.20031218072017.3077:search & helpers
    #@+node:ekr.20031218072017.3081:selectNextPosition
    # Selects the next node to be searched.
    
    def selectNextPosition(self):
    
        c = self.c ; p = self.p
    
        if self.selection_only:
            return None
    
        # Start suboutline only searches.
        if self.suboutline_only and not self.onlyPosition:
            # p.copy not needed because the find code never calls p.moveToX.
            # Furthermore, p might be None, so p.copy() would be wrong!
            self.onlyPosition = p 
    
        # Start wrapped searches.
        if self.wrapping and not self.wrapPosition:
            assert(self.wrapPos != None)
            # p.copy not needed because the find code never calls p.moveToX.
            # Furthermore, p might be None, so p.copy() would be wrong!
            self.wrapPosition = p 
    
        if self.in_headline and self.search_body:
            # just switch to body pane.
            self.in_headline = False
            self.initNextText()
            # g.trace('switching to body',g.callers(5))
            return p
    
        if self.reverse: p = p.threadBack()
        else:            p = p.threadNext()
        
        # New in 4.3: restrict searches to hoisted area.
        # End searches outside hoisted area.
        if c.hoistStack:
            if not p:
                if self.wrapping:
                    g.es('Wrap disabled in hoisted outlines',color='blue')
                return
            bunch = c.hoistStack[-1]
            if not bunch.p.isAncestorOf(p):
                g.es('Found match outside of hoisted outline',color='blue')
                return None
    
        # Wrap if needed.
        if not p and self.wrapping and not self.suboutline_only:
            p = c.rootPosition()
            if self.reverse:
                # Set search_v to the last node of the tree.
                while p and p.next():
                    p = p.next()
                if p: p = p.lastNode()
    
        # End wrapped searches.
        if self.wrapping and p and p == self.wrapPosition:
            # g.trace("ending wrapped search")
            p = None ; self.resetWrap()
    
        # End suboutline only searches.
        if (self.suboutline_only and self.onlyPosition and p and
            (p == self.onlyPosition or not self.onlyPosition.isAncestorOf(p))):
            # g.trace("end outline-only")
            p = None ; self.onlyPosition = None
    
        # p.copy not needed because the find code never calls p.moveToX.
        # Furthermore, p might be None, so p.copy() would be wrong!
        self.p = p # used in initNextText().
        if p: # select p and set the search point within p.
            self.in_headline = self.search_headline
            self.initNextText()
        return p
    #@-node:ekr.20031218072017.3081:selectNextPosition
    #@-node:ekr.20031218072017.3067:Find/change utils
    #@+node:ekr.20061212095134.1:General utils
    #@+node:ekr.20051020120306.26:bringToFront (leoFind)
    def bringToFront (self):
    
        """Bring the Find Tab to the front and select the entire find text."""
    
        c = self.c ; w = self.find_ctrl
            
        c.widgetWantsFocusNow(w)
        g.app.gui.selectAllText(w)
        c.widgetWantsFocus(w)
    #@-node:ekr.20051020120306.26:bringToFront (leoFind)
    #@+node:ekr.20061111084423.1:oops (leoFind)
    def oops(self):
        print ("leoFind oops:",
            g.callers(),"should be overridden in subclass")
    #@nonl
    #@-node:ekr.20061111084423.1:oops (leoFind)
    #@+node:ekr.20051020120306.27:selectAllFindText (leoFind)
    def selectAllFindText (self,event=None):
        
        __pychecker__ = '--no-argsused' # event
        
        # This is called only when the user presses ctrl-a in the find panel.
    
        w = self.frame.focus_get()
        if g.app.gui.isTextWidget(w):
            w.selectAllText()
    
        return "break"
    #@-node:ekr.20051020120306.27:selectAllFindText (leoFind)
    #@-node:ekr.20061212095134.1:General utils
    #@+node:ekr.20031218072017.3082:Initing & finalizing
    #@+node:ekr.20031218072017.3083:checkArgs
    def checkArgs (self):
    
        val = True
        if not self.search_headline and not self.search_body:
            g.es("not searching headline or body")
            val = False
        if len(self.find_text) == 0:
            g.es("empty find patttern")
            val = False
        return val
    #@-node:ekr.20031218072017.3083:checkArgs
    #@+node:ekr.20051020120306.28:init_s_ctrl
    def init_s_ctrl (self,s):
        
        w = self.s_ctrl
        w.setAllText(s)
        i = g.choose(self.reverse,len(s),0)
        w.setInsertPoint(i)
        return w
    #@-node:ekr.20051020120306.28:init_s_ctrl
    #@+node:ekr.20031218072017.3084:initBatchCommands
    # Initializes for the Find All and Change All commands.
    
    def initBatchCommands (self):
    
        c = self.c ; w = c.frame.body.bodyCtrl
        self.in_headline = self.search_headline # Search headlines first.
        self.errors = 0
    
        # Select the first node.
        if self.suboutline_only or self.node_only or self.selection_only:
            self.p = c.currentPosition()
            if self.selection_only: self.selStart,self.selEnd = w.getSelectionRange()
            else:                   self.selStart,self.selEnd = None,None
        else:
            p = c.rootPosition()
            if self.reverse:
                while p and p.next():
                    p = p.next()
                p = p.lastNode()
            self.p = p
    
        # Set the insert point.
        self.initBatchText()
    #@-node:ekr.20031218072017.3084:initBatchCommands
    #@+node:ekr.20031218072017.3085:initBatchText & initNextText
    # Returns s_ctrl with "insert" point set properly for batch searches.
    def initBatchText(self):
        p = self.p
        self.wrapping = False # Only interactive commands allow wrapping.
        s = g.choose(self.in_headline,p.headString(), p.bodyString())
        return self.init_s_ctrl(s)
    
    # Call this routine when moving to the next node when a search fails.
    # Same as above except we don't reset wrapping flag.
    def initNextText(self):
        p = self.p
        s = g.choose(self.in_headline,p.headString(), p.bodyString())
        return self.init_s_ctrl(s)
    #@-node:ekr.20031218072017.3085:initBatchText & initNextText
    #@+node:ekr.20031218072017.3086:initInHeadline
    # Guesses which pane to start in for incremental searches and changes.
    # This must not alter the current "insert" or "sel" marks.
    
    def initInHeadline (self):
    
        c = self.c ; p = self.p
    
        # Do not change this without careful thought and extensive testing!
        if self.search_headline and self.search_body:
            # A temporary expedient.
            if self.reverse:
                self.in_headline = False
            else:
                # Search headline first.
                self.in_headline = (
                    p == c.frame.tree.editPosition() and
                    c.get_focus() != c.frame.body.bodyCtrl)
        else:
            self.in_headline = self.search_headline
    #@-node:ekr.20031218072017.3086:initInHeadline
    #@+node:ekr.20031218072017.3087:initInteractiveCommands
    # For incremental searches
    
    def initInteractiveCommands(self):
    
        c = self.c ; p = self.p
    
        self.errors = 0
        if self.in_headline:
            c.frame.tree.setEditPosition(p)
            w = c.edit_widget(p)
            sel = None
        else:
            w = c.frame.bodyCtrl
            sel = w.getSelectionRange()
        pos = w.getInsertPoint()
        st = self.initNextText()
        c.widgetWantsFocus(w)
        st.setInsertPoint(pos)
        if sel:
            self.selStart,self.selEnd = sel
        else:
            self.selStart,self.selEnd = None,None
        self.wrapping = self.wrap
        if self.wrap and self.wrapPosition == None:
            self.wrapPos = pos
            # Do not set self.wrapPosition here: that must be done after the first search.
    #@-node:ekr.20031218072017.3087:initInteractiveCommands
    #@+node:ekr.20031218072017.3088:printLine
    def printLine (self,line,allFlag=False):
    
        both = self.search_body and self.search_headline
        context = self.batch # "batch" now indicates context
    
        if allFlag and both and context:
            g.es('-' * 20,self.p.headString())
            theType = g.choose(self.in_headline,"head: ","body: ")
            g.es(theType + line)
        elif allFlag and context and not self.p.isVisited():
            # We only need to print the context once.
            g.es('-' * 20,self.p.headString())
            g.es(line)
            self.p.setVisited()
        else:
            g.es(line)
    #@-node:ekr.20031218072017.3088:printLine
    #@+node:ekr.20031218072017.3089:restore
    # Restores the screen after a search fails
    
    def restore (self,data):
    
        c = self.c
        in_headline,p,t,insert,start,end = data
        
        c.frame.bringToFront() # Needed on the Mac
    
        # Don't try to reedit headline.
        c.selectPosition(p)
        
        if not in_headline:
            # Looks good and provides clear indication of failure or termination.
            t.setSelectionRange(insert,insert)
            t.setInsertPoint(insert)
            t.seeInsertPoint()
        
        #g.trace(c.widget_name(t))
        
        if 1: # I prefer always putting the focus in the body.
            c.invalidateFocus()
            c.bodyWantsFocusNow()
        else:
            c.widgetWantsFocusNow(t)
    #@-node:ekr.20031218072017.3089:restore
    #@+node:ekr.20031218072017.3090:save
    def save (self):
    
        c = self.c ; p = self.p
        w = g.choose(self.in_headline,c.edit_widget(p),c.frame.bodyCtrl)
        insert = w.getInsertPoint()
        sel = w.getSelectionRange()
        if len(sel) == 2:
            start,end = sel
        else:
            start,end = None,None
        return (self.in_headline,p,w,insert,start,end)
    #@-node:ekr.20031218072017.3090:save
    #@+node:ekr.20031218072017.3091:showSuccess
    def showSuccess(self,pos,newpos):
    
        """Displays the final result.
    
        Returns self.dummy_vnode, c.edit_widget(p) or c.frame.bodyCtrl with
        "insert" and "sel" points set properly."""
    
        c = self.c ; p = self.p
        sparseFind = c.config.getBool('collapse_nodes_during_finds')
        c.frame.bringToFront() # Needed on the Mac
        redraw = not p.isVisible()
        c.beginUpdate()
        try:
            if sparseFind:
                # New in Leo 4.4.2: show only the 'sparse' tree when redrawing.
                for p in c.allNodes_iter():
                    if not p.isAncestorOf(self.p):
                        p.contract()
                        redraw = True
                for p in self.p.parents_iter():
                    if not p.isExpanded():
                        p.expand()
                        redraw = True
            p = self.p
            c.selectPosition(p)
        finally:
            c.endUpdate(redraw)
        if self.in_headline:
            c.editPosition(p)
        # Set the focus and selection after the redraw.
        w = g.choose(self.in_headline,c.edit_widget(p),c.frame.body.bodyCtrl)
        c.widgetWantsFocusNow(w)
        # New in 4.4a3: a much better way to ensure progress in backward searches.
        insert = g.choose(self.reverse,min(pos,newpos),max(pos,newpos))
        #g.trace('reverse,pos,newpos,insert',self.reverse,pos,newpos,insert)
        w.setSelectionRange(pos,newpos,insert=insert)
        w.seeInsertPoint()
        if self.wrap and not self.wrapPosition:
            self.wrapPosition = self.p
    #@nonl
    #@-node:ekr.20031218072017.3091:showSuccess
    #@+node:ekr.20031218072017.1460:update_ivars (leoFind)
    # New in Leo 4.4.3: This is now gui-independent code.
    
    def update_ivars (self):
        
        """Called just before doing a find to update ivars from the find panel."""
        
        self.p = self.c.currentPosition()
        self.v = self.p.v
    
        for key in self.intKeys:
            # g.trace(self.svarDict.get(key))
            val = self.svarDict[key].get()
            setattr(self, key, val) # No more _flag hack.
    
        # Set ivars from radio buttons. Convert these to 1 or 0.
        search_scope = self.svarDict["radio-search-scope"].get()
        self.suboutline_only = g.choose(search_scope == "suboutline-only",1,0)
        self.node_only       = g.choose(search_scope == "node-only",1,0)
        self.selection       = g.choose(search_scope == "selection-only",1,0)
    
        # New in 4.3: The caller is responsible for removing most trailing cruft.
        # Among other things, this allows Leo to search for a single trailing space.
        s = self.find_ctrl.getAllText()
        s = g.toUnicode(s,g.app.tkEncoding)
        # g.trace(repr(s))
        if s and s[-1] in ('\r','\n'):
            s = s[:-1]
        self.find_text = s
    
        s = self.change_ctrl.getAllText()
        if s and s[-1] in ('\r','\n'):
            s = s[:-1]
        s = g.toUnicode(s,g.app.tkEncoding)
        self.change_text = s
    #@-node:ekr.20031218072017.1460:update_ivars (leoFind)
    #@-node:ekr.20031218072017.3082:Initing & finalizing
    #@-others
#@-node:ekr.20061212084717:class leoFind
#@+node:ekr.20051020120306.6:class findTab (leoFind)
class findTab (leoFind):
    
    '''An adapter class that implements Leo's Find tab.'''

    #@    @+others
    #@+node:ekr.20051020120306.10:Birth & death
    #@+node:ekr.20051020120306.11:__init__ & initGui
    def __init__(self,c,parentFrame):
        
        # g.trace('findTab',g.callers())
    
        # Init the base class...
        leoFind.__init__(self,c,title='Find Tab')
    
        self.c = c
        self.parentFrame = parentFrame
        self.frame = self.outerFrame = self.top = None
        
        self.optionsOnly = c.config.getBool('show_only_find_tab_options')
        
        # These are created later.
        self.find_ctrl = None
        self.change_ctrl = None 
        self.outerScrolledFrame = None
    
        self.initGui()
        self.createFrame(parentFrame)
        self.createBindings()
        self.init(c) # New in 4.3: init only once.
        
    #@nonl
    #@-node:ekr.20051020120306.11:__init__ & initGui
    #@+node:ekr.20061212092124:Defined in subclasses
    def createBindings (self):
        self.oops()
        
    def createFrame (self):
        self.oops()
        
    def initGui (self):
        pass # Optional method.
        
    # self.oops is defined in the leoFind class.
    #@nonl
    #@-node:ekr.20061212092124:Defined in subclasses
    #@-node:ekr.20051020120306.10:Birth & death
    #@+node:ekr.20060221074900:Callbacks
    #@+node:ekr.20060221074900.1:findButtonCallback
    def findButtonCallback(self,event=None):
        
        self.findButton()
        return 'break'
    #@-node:ekr.20060221074900.1:findButtonCallback
    #@+node:ekr.20051020120306.25:hideTab
    def hideTab (self,event=None):
        
        c = self.c
        c.frame.log.selectTab('Log')
        c.bodyWantsFocus()
    #@-node:ekr.20051020120306.25:hideTab
    #@-node:ekr.20060221074900:Callbacks
    #@+node:ekr.20051024192602: Top level
    #@+node:ekr.20051024192642.3:change/ThenFindCommand
    def changeCommand (self,event=None):
    
        self.setup_command()
        self.change()
        
    def changeAllCommand (self,event=None):
    
        self.setup_command()
        self.changeAll()
        
    def changeThenFindCommand(self,event=None):
        
        self.setup_command()
        self.changeThenFind()
    #@-node:ekr.20051024192642.3:change/ThenFindCommand
    #@+node:ekr.20070105123638:changeAllCommand
    def changeAllCommand (self,event=None):
    
        self.setup_command()
        self.changeAll()
    #@-node:ekr.20070105123638:changeAllCommand
    #@+node:ekr.20060128075225:cloneFindAllCommand
    def cloneFindAllCommand (self,event=None):
        
        self.setup_command()
        self.clone_find_all = True
        self.findAll()
        self.clone_find_all = False
    #@-node:ekr.20060128075225:cloneFindAllCommand
    #@+node:ekr.20060204120158.1:findAgainCommand
    def findAgainCommand (self):
        
        s = self.find_ctrl.getAllText()
        
        if s and s != '<find pattern here>':
            self.findNextCommand()
            return True
        else:
            # Tell the caller that to get the find args.
            return False
    #@-node:ekr.20060204120158.1:findAgainCommand
    #@+node:ekr.20060209064832:findAllCommand
    def findAllCommand (self,event=None):
    
        self.setup_command()
        self.findAll()
    #@-node:ekr.20060209064832:findAllCommand
    #@+node:ekr.20051024192642.2:findNext/PrefCommand
    def findNextCommand (self,event=None):
    
        self.setup_command()
        self.findNext()
        
    def findPrevCommand (self,event=None):
        
        self.setup_command()
        self.reverse = not self.reverse
        self.findNext()
        self.reverse = not self.reverse
    #@-node:ekr.20051024192642.2:findNext/PrefCommand
    #@-node:ekr.20051024192602: Top level
    #@-others
#@-node:ekr.20051020120306.6:class findTab (leoFind)
#@-others
#@-node:ekr.20060123151617:@thin leoFind.py
#@-leo
