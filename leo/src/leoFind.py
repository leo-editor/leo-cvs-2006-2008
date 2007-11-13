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
    #@+node:ekr.20031218072017.3053:leoFind.__init__ & helpers
    def __init__ (self,c,title=None):

        # g.trace('leoFind',c)

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
            self.wrap = None
            self.whole_word = None

        if 1:
            self.change_ctrl = None
            self.find_ctrl = None
            self.frame = None
            self.svarDict = {}
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
        #@-node:ekr.20031218072017.3054:<< init the gui-independent ivars >>
        #@nl

    def init (self,c):
        self.oops()
    #@-node:ekr.20031218072017.3053:leoFind.__init__ & helpers
    #@+node:ekr.20060123065756.1:Top Level Buttons
    #@+node:ekr.20031218072017.3057:changeAllButton
    # The user has pushed the "Change All" button from the find panel.

    def changeAllButton(self):

        c = self.c
        self.setup_button()
        c.clearAllVisited() # Clear visited for context reporting.

        if self.script_change:
            self.doChangeAllScript()
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
    #@+node:ekr.20031218072017.3069:changeAll
    def changeAll(self):

        # g.trace(g.callers())

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
    #@-node:ekr.20031218072017.3069:changeAll
    #@+node:ekr.20031218072017.3070:changeSelection (changed)
    # Replace selection with self.change_text.
    # If no selection, insert self.change_text at the cursor.

    def changeSelection(self):

        c = self.c ; p = self.p
        w = g.choose(self.in_headline,c.edit_widget(p),c.frame.body.bodyCtrl) # 2007:10/25
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
    #@-node:ekr.20031218072017.3070:changeSelection (changed)
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

        if pos is None:
            if self.wrapping:
                g.es("end of wrapped search")
            else:
                g.es("not found: " + "'" + self.find_text + "'")
            self.restore(data)
        else:
            self.showSuccess(pos,newpos)
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

        p = self.p ; self.errors = 0
        attempts = 0
        self.backwardAttempts = 0
        while p:
            pos, newpos = self.search()
            # g.trace('pos',pos,'p',p.headString(),g.callers())
            if pos is not None:
                if self.mark_finds:
                    p.setMarked()
                    c.frame.tree.drawIcon(p) # redraw only the icon.
                return pos, newpos
            elif self.errors:
                g.trace('find errors')
                return None,None # Abort the search.
            elif self.node_only:
                return None,None # We are only searching one node.
            else:
                attempts += 1
                p = self.p = self.selectNextPosition()
        # g.trace('attempts',attempts,'backwardAttempts',self.backwardAttempts)
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
        if self.wrapping and self.wrapPos is not None and self.wrapPosition and p == self.wrapPosition:

            if self.reverse and pos < self.wrapPos:
                # g.trace("reverse wrap done")
                return None, None

            if not self.reverse and newpos > self.wrapPos:
                # g.trace('wrap done')
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
            # if s: g.trace('empty',i,j,'len(s)',len(s),'pattern',pattern)
            return -1,-1

        if regexp:
            pos,newpos = self.regexHelper(s,i,j,pattern,backwards,nocase)
        elif backwards:
            pos,newpos = self.backwardsHelper(s,i,j,pattern,nocase,word)
        else:
            pos,newpos = self.plainHelper(s,i,j,pattern,nocase,word)

        return pos,newpos
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

        if backwards: # Scan to the last match.  We must use search here.
            last_mo = None ; i = 0
            while i < len(s):
                mo = re_obj.search(s,i,j)
                if not mo: break
                i += 1 ; last_mo = mo
            mo = last_mo
        else:
            mo = re_obj.search(s,i,j)

        if 0:
            g.trace('i',i,'j',j,'s[i:j]',repr(s[i:j]),
                'mo.start',mo and mo.start(),'mo.end',mo and mo.end())

        while mo and 0 <= i < len(s):
            if mo.start() == mo.end():
                if backwards:
                    # Search backward using match instead of search.
                    i -= 1
                    while 0 <= i < len(s):
                        mo = re_obj.match(s,i,j)
                        if mo: break
                        i -= 1
                else:
                    i += 1 ; mo = re_obj.search(s,i,j)
            else:
                self.match_obj = mo
                return mo.start(),mo.end()
        self.match_obj = None
        return -1,-1
    #@-node:ekr.20060526092203:regexHelper
    #@+node:ekr.20060526140744:backwardsHelper
    debugIndices = []

    #@+at
    # rfind(sub [,start [,end]])
    # 
    # Return the highest index in the string where substring sub is found, 
    # such that
    # sub is contained within s[start,end]. Optional arguments start and end 
    # are
    # interpreted as in slice notation. Return -1 on failure.
    #@-at
    #@@c

    def backwardsHelper (self,s,i,j,pattern,nocase,word):

        debug = False
        if nocase:
            s = s.lower() ; pattern = pattern.lower() # Bug fix: 10/5/06: At last the bug is found!
        pattern = self.replaceBackSlashes(pattern)
        n = len(pattern)

        if i < 0 or i > len(s) or j < 0 or j > len(s):
            g.trace('bad index: i = %s, j = %s' % (i,j))
            i = 0 ; j = len(s)

        if debug and (s and i == 0 and j == 0):
            g.trace('two zero indices')

        self.backwardAttempts += 1

        # short circuit the search: helps debugging.
        if s.find(pattern) == -1:
            if debug:
                self.debugCount += 1
                if self.debugCount < 50:
                    g.trace(i,j,'len(s)',len(s),self.p.headString())
            return -1,-1

        if word:
            while 1:
                k = s.rfind(pattern,i,j)
                if debug: g.trace('**word** %3s %3s %5s -> %s %s' % (i,j,g.choose(j==len(s),'(end)',''),k,self.p.headString()))
                if k == -1: return -1, -1
                if self.matchWord(s,k,pattern):
                    return k,k+n
                else:
                    j = max(0,k-1)
        else:
            k = s.rfind(pattern,i,j)
            if debug: g.trace('%3s %3s %5s -> %s %s' % (i,j,g.choose(j==len(s),'(end)',''),k,self.p.headString()))
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

        c = self.c ; p = self.p ; trace = False

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
            if trace: g.trace('switching to body',g.callers(5))
            return p

        if self.reverse: p = p.threadBack()
        else:            p = p.threadNext()

        # if trace: g.trace(p and p.headString() or 'None')

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
            if trace: g.trace("ending wrapped search")
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

        # g.trace(g.callers())
        c.widgetWantsFocusNow(w)
        g.app.gui.selectAllText(w)
        c.widgetWantsFocus(w)
    #@-node:ekr.20051020120306.26:bringToFront (leoFind)
    #@+node:ekr.20061111084423.1:oops (leoFind)
    def oops(self):
        print ("leoFind oops:",
            g.callers(10),"should be overridden in subclass")
    #@-node:ekr.20061111084423.1:oops (leoFind)
    #@+node:ekr.20051020120306.27:selectAllFindText (leoFind)
    def selectAllFindText (self,event=None):

        # __pychecker__ = '--no-argsused' # event

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
    #@+node:ekr.20031218072017.3084:initBatchCommands
    # Initializes for the Find All and Change All commands.

    def initBatchCommands (self):

        c = self.c
        self.in_headline = self.search_headline # Search headlines first.
        self.errors = 0

        # Select the first node.
        if self.suboutline_only or self.node_only:
            self.p = c.currentPosition()
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
    #@+node:ekr.20031218072017.3085:initBatchText, initNextText & init_s_ctrl
    # Returns s_ctrl with "insert" point set properly for batch searches.
    def initBatchText(self,ins=None):
        p = self.p
        self.wrapping = False # Only interactive commands allow wrapping.
        s = g.choose(self.in_headline,p.headString(), p.bodyString())
        self.init_s_ctrl(s,ins)

    # Call this routine when moving to the next node when a search fails.
    # Same as above except we don't reset wrapping flag.
    def initNextText(self,ins=None):
        p = self.p
        s = g.choose(self.in_headline,p.headString(), p.bodyString())
        self.init_s_ctrl(s,ins)

    def init_s_ctrl (self,s,ins):

        w = self.s_ctrl
        w.setAllText(s)
        if ins is None:
            ins = g.choose(self.reverse,len(s),0)
            # print g.choose(self.reverse,'.','*'),
        else:
            pass # g.trace('ins',ins)
        w.setInsertPoint(ins)
    #@-node:ekr.20031218072017.3085:initBatchText, initNextText & init_s_ctrl
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
    def initInteractiveCommands(self):

        c = self.c ; p = self.p
        w = g.choose(self.in_headline,c.edit_widget(p),c.frame.body.bodyCtrl)
        self.errors = 0

        # We only use the insert point, *never* the selection range.
        ins = w.getInsertPoint()
        # g.trace('ins',ins)
        self.debugCount = 0
        self.initNextText(ins=ins)
        c.widgetWantsFocus(w)

        self.wrapping = self.wrap
        if self.wrap and self.wrapPosition == None:
            self.wrapPos = ins
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
        w = g.choose(self.in_headline,c.edit_widget(p),c.frame.body.bodyCtrl)

        # 2007/10/24: defensive programming for unit tests.
        if w:
            insert = w.getInsertPoint()
            sel = w.getSelectionRange()
            if len(sel) == 2:
                start,end = sel
            else:
                start,end = None,None
        else:
            start,end = None,None

        return (self.in_headline,p,w,insert,start,end)
    #@-node:ekr.20031218072017.3090:save
    #@+node:ekr.20031218072017.3091:showSuccess
    def showSuccess(self,pos,newpos):

        """Displays the final result.

        Returns self.dummy_vnode, c.edit_widget(p) or c.frame.body.bodyCtrl with
        "insert" and "sel" points set properly."""

        c = self.c ; p = self.p
        sparseFind = c.config.getBool('collapse_nodes_during_finds')
        c.frame.bringToFront() # Needed on the Mac
        redraw = not p.isVisible(c)
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
            if not p: g.trace('can not happen: self.p is None')
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
    #@+node:ekr.20051020120306.11:__init__ & initGui
    def __init__(self,c,parentFrame):

        # g.trace('findTab',c)

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
    #@-node:ekr.20051020120306.11:__init__ & initGui
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
    #@+node:ekr.20061212092124:Defined in subclasses
    def createBindings (self):
        self.oops()

    def createFrame (self,parent):
        # __pychecker__ = '--no-argsused'
        self.oops()

    def getOption (self,ivar):
        self.oops()

    def init (self,c):
        self.oops()

    def initGui (self):
        pass # Optional method.

    def setOption (self,ivar,val):
        # __pychecker__ = '--no-argsused'
        self.oops()

    def toggleOption (self,ivar):
        self.oops()

    # self.oops is defined in the leoFind class.
    #@-node:ekr.20061212092124:Defined in subclasses
    #@-others
#@-node:ekr.20051020120306.6:class findTab (leoFind)
#@+node:ekr.20070302090616:class nullFindTab class (findTab)
class nullFindTab (findTab):

    #@    @+others
    #@+node:ekr.20070302090616.1:Birth (nullFindTab)
    #@+node:ekr.20070302090616.2: ctor (nullFindTab)
    if 0: # Use the base-class ctor.

        def __init__ (self,c,parentFrame):

            findTab.__init__(self,c,parentFrame)
                # Init the base class.
                # Calls initGui, createFrame, createBindings & init(c), in that order.
    #@-node:ekr.20070302090616.2: ctor (nullFindTab)
    #@+node:ekr.20070302090616.3:initGui
    # Called from findTab.ctor.

    def initGui (self):

        self.svarDict = {} # Keys are ivar names, values are svar objects.

        for key in self.intKeys:
            self.svarDict[key] = self.svar() # Was Tk.IntVar.

        for key in self.newStringKeys:
            self.svarDict[key] = self.svar() # Was Tk.StringVar.
    #@-node:ekr.20070302090616.3:initGui
    #@+node:ekr.20070302090616.4:init
    # Called from findTab.ctor.

    def init (self,c):

        # Separate c.ivars are much more convenient than a svarDict.
        for key in self.intKeys:
            # Get ivars from @settings.
            val = c.config.getBool(key)
            setattr(self,key,val)
            val = g.choose(val,1,0)
            svar = self.svarDict.get(key)
            if svar: svar.set(val)
            #g.trace(key,val)

        #@    << set find/change widgets >>
        #@+node:ekr.20070302090616.5:<< set find/change widgets >>
        self.find_ctrl.delete(0,"end")
        self.change_ctrl.delete(0,"end")

        # Get setting from @settings.
        for w,setting,defaultText in (
            (self.find_ctrl,"find_text",'<find pattern here>'),
            (self.change_ctrl,"change_text",''),
        ):
            s = c.config.getString(setting)
            if not s: s = defaultText
            w.insert("end",s)
        #@-node:ekr.20070302090616.5:<< set find/change widgets >>
        #@nl
        #@    << set radio buttons from ivars >>
        #@+node:ekr.20070302090616.6:<< set radio buttons from ivars >>
        # In Tk, setting the var also sets the widget.
        # Here, we do so explicitly.
        d = self.widgetsDict
        for ivar,key in (
            ("pattern_match","pattern-search"),
            #("script_search","script-search")
        ):
            svar = self.svarDict[ivar].get()
            if svar:
                self.svarDict["radio-find-type"].set(key)
                w = d.get(key)
                if w: w.set(True)
                break
        else:
            self.svarDict["radio-find-type"].set("plain-search")

        for ivar,key in (
            ("suboutline_only","suboutline-only"),
            ("node_only","node-only"),
            # ("selection_only","selection-only")
        ):
            svar = self.svarDict[ivar].get()
            if svar:
                self.svarDict["radio-search-scope"].set(key)
                break
        else:
            key = 'entire-outline'
            self.svarDict["radio-search-scope"].set(key)
            w = self.widgetsDict.get(key)
            if w: w.set(True)
        #@-node:ekr.20070302090616.6:<< set radio buttons from ivars >>
        #@nl
        #@    << set checkboxes from ivars >>
        #@+node:ekr.20070302090616.7:<< set checkboxes from ivars >>
        for ivar in (
            'ignore_case',
            'mark_changes',
            'mark_finds',
            'pattern_match',
            'reverse',
            'search_body',
            'search_headline',
            'whole_word',
            'wrap',
        ):
            svar = self.svarDict[ivar].get()
            if svar:
                w = self.widgetsDict.get(ivar)
                if w: w.set(True)
        #@-node:ekr.20070302090616.7:<< set checkboxes from ivars >>
        #@nl
    #@-node:ekr.20070302090616.4:init
    #@+node:ekr.20070302090616.15:createBindings
    def createBindings (self):
        pass
    #@nonl
    #@-node:ekr.20070302090616.15:createBindings
    #@+node:ekr.20070302090616.9:createFrame
    def createFrame (self,parentFrame):

        self.parentFrame = self.top = parentFrame

        self.createFindChangeAreas()
        self.createBoxes()
    #@nonl
    #@+node:ekr.20070302090616.10:createFindChangeAreas
    def createFindChangeAreas (self):

        c = self.c

        # A plainTextWidget must be a stringTextWidget
        plainTextWidget = g.app.gui.plainTextWidget

        import leoFrame
        assert issubclass(plainTextWidget,leoFrame.stringTextWidget)

        self.find_ctrl   = plainTextWidget(c,name='find-text')
        self.change_ctrl = plainTextWidget(c,name='change-text')
    #@-node:ekr.20070302090616.10:createFindChangeAreas
    #@+node:ekr.20070302090616.12:createBoxes
    def createBoxes (self):

        '''Create two columns of radio buttons & check boxes.'''

        c = self.c
        # f = self.parentFrame
        self.boxes = []
        self.widgetsDict = {} # Keys are ivars, values are checkboxes or radio buttons.

        data = ( # Leading star denotes a radio button.
            ('Whole &Word', 'whole_word',),
            ('&Ignore Case','ignore_case'),
            ('Wrap &Around','wrap'),
            ('&Reverse',    'reverse'),
            ('Rege&xp',     'pattern_match'),
            ('Mark &Finds', 'mark_finds'),
            ("*&Entire Outline","entire-outline"),
            ("*&Suboutline Only","suboutline-only"),  
            ("*&Node Only","node-only"),
            ('Search &Headline','search_headline'),
            ('Search &Body','search_body'),
            ('Mark &Changes','mark_changes'),
        )

        # Important: changing these controls merely changes entries in self.svarDict.
        # First, leoFind.update_ivars sets the find ivars from self.svarDict.
        # Second, self.init sets the values of widgets from the ivars.
        # inGroup = False
        for label,ivar in data:
            if label.startswith('*'):
                label = label[1:]
                # style = g.choose(inGroup,0,wx.RB_GROUP)
                # inGroup = True
                # w = wx.RadioButton(f,label=label,style=style)
                w = self.buttonWidget(label)
                self.widgetsDict[ivar] = w
                # def radioButtonCallback(event=None,ivar=ivar):
                    # svar = self.svarDict["radio-search-scope"]
                    # svar.set(ivar)
                # w.Bind(wx.EVT_RADIOBUTTON,radioButtonCallback)
            else:
                #w = wx.CheckBox(f,label=label)
                w = self.buttonWidget(label)
                self.widgetsDict[ivar] = w
                # def checkBoxCallback(event=None,ivar=ivar):
                    # svar = self.svarDict.get(ivar)
                    # val = svar.get()
                    # svar.set(g.choose(val,False,True))
                    # # g.trace(ivar,val)
                # w.Bind(wx.EVT_CHECKBOX,checkBoxCallback)
            self.boxes.append(w)
    #@nonl
    #@-node:ekr.20070302090616.12:createBoxes
    #@+node:ekr.20070302090616.14:createButtons (not used)
    def createButtons (self):

        '''Create two columns of buttons.'''

        # # Create the alignment panes.
        # buttons  = Tk.Frame(outer,background=bg)
        # buttons1 = Tk.Frame(buttons,bd=1,background=bg)
        # buttons2 = Tk.Frame(buttons,bd=1,background=bg)
        # buttons.pack(side='top',expand=1)
        # buttons1.pack(side='left')
        # buttons2.pack(side='right')

        # width = 15 ; defaultText = 'Find' ; buttons = []

        # for text,boxKind,frame,callback in (
            # # Column 1...
            # ('Find','button',buttons1,self.findButtonCallback),
            # ('Find All','button',buttons1,self.findAllButton),
            # # Column 2...
            # ('Change','button',buttons2,self.changeButton),
            # ('Change, Then Find','button',buttons2,self.changeThenFindButton),
            # ('Change All','button',buttons2,self.changeAllButton),
        # ):
            # w = underlinedTkButton(boxKind,frame,
                # text=text,command=callback)
            # buttons.append(w)
            # if text == defaultText:
                # w.button.configure(width=width-1,bd=4)
            # elif boxKind != 'check':
                # w.button.configure(width=width)
            # w.button.pack(side='top',anchor='w',pady=2,padx=2)
    #@-node:ekr.20070302090616.14:createButtons (not used)
    #@-node:ekr.20070302090616.9:createFrame
    #@-node:ekr.20070302090616.1:Birth (nullFindTab)
    #@+node:ekr.20070302090616.8:class svar (nullFindTab)
    class svar:
        '''A class like Tk's IntVar and StringVar classes.'''
        def __init__(self):
            self.val = None
        def get (self):
            return self.val
        def set (self,val):
            self.val = val

        SetValue = set # SetValue is the wxWidgets spelling.
    #@nonl
    #@-node:ekr.20070302090616.8:class svar (nullFindTab)
    #@+node:ekr.20070302092907:class buttonWidget (nullFindTab)
    class buttonWidget:

        '''A class to simulate a Tk.Button.'''

        def __init__ (self,label):
            self.label = label
            self.val = False

        def __repr (self):
            return 'nullFindTab.buttonWidget: %s' % self.label

        def get (self):
            return self.val

        def set (self,val):
            self.val = val
    #@-node:ekr.20070302092907:class buttonWidget (nullFindTab)
    #@+node:ekr.20070302090616.16:Options
    # This is the same as the Tk code because we simulate Tk svars.
    #@nonl
    #@+node:ekr.20070302090616.17:getOption
    def getOption (self,ivar):

        var = self.svarDict.get(ivar)

        if var:
            val = var.get()
            # g.trace('%s = %s' % (ivar,val))
            return val
        else:
            g.trace('bad ivar name: %s' % ivar)
            return None
    #@-node:ekr.20070302090616.17:getOption
    #@+node:ekr.20070302090616.18:setOption
    def setOption (self,ivar,val):

        if ivar in self.intKeys:
            if val is not None:
                var = self.svarDict.get(ivar)
                var.set(val)
                # g.trace('%s = %s' % (ivar,val))

        elif not g.app.unitTesting:
            g.trace('oops: bad find ivar %s' % ivar)
    #@-node:ekr.20070302090616.18:setOption
    #@+node:ekr.20070302090616.19:toggleOption
    def toggleOption (self,ivar):

        if ivar in self.intKeys:
            var = self.svarDict.get(ivar)
            val = not var.get()
            var.set(val)
            # g.trace('%s = %s' % (ivar,val),var)
        else:
            g.trace('oops: bad find ivar %s' % ivar)
    #@-node:ekr.20070302090616.19:toggleOption
    #@-node:ekr.20070302090616.16:Options
    #@-others
#@nonl
#@-node:ekr.20070302090616:class nullFindTab class (findTab)
#@-others
#@-node:ekr.20060123151617:@thin leoFind.py
#@-leo
