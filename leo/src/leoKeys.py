#@+leo-ver=4-thin
#@+node:ekr.20061031131434:@thin leoKeys.py
"""Gui-independent keystroke handling for Leo.""" 

#@@language python
#@@tabwidth -4
#@@pagewidth 80

#@<< imports >>
#@+node:ekr.20061031131434.1:<< imports >>
import leoGlobals as g
import leoEditCommands

import glob
import inspect
import os
import re
import string
import sys
import types

# The following imports _are_ used.
__pychecker__ = '--no-import'

try:
    # These do not exist in IronPython or Python 2.4
    import compiler
    import parser
except ImportError:
    pass
#@-node:ekr.20061031131434.1:<< imports >>
#@nl
#@<< about 'internal' bindings >>
#@+node:ekr.20061031131434.2:<< about 'internal' bindings >>
#@@nocolor
#@+at
# 
# Here are the rules for translating key bindings (in leoSettings.leo) into 
# keys for k.bindingsDict:
# 
# 1.  The case of plain letters is significant:  a is not A.
# 
# 2. The Shift- prefix can be applied *only* to letters. Leo will ignore (with 
# a
# warning) the shift prefix applied to any other binding, e.g., Ctrl-Shift-(
# 
# 3. The case of letters prefixed by Ctrl-, Alt-, Key- or Shift- is *not*
# significant. Thus, the Shift- prefix is required if you want an upper-case
# letter (with the exception of 'bare' uppercase letters.)
# 
# The following table illustrates these rules. In each row, the first entry is 
# the
# key (for k.bindingsDict) and the other entries are equivalents that the user 
# may
# specify in leoSettings.leo:
# 
# a, Key-a, Key-A
# A, Shift-A
# Alt-a, Alt-A
# Alt-A, Alt-Shift-a, Alt-Shift-A
# Ctrl-a, Ctrl-A
# Ctrl-A, Ctrl-Shift-a, Ctrl-Shift-A
# !, Key-!,Key-exclam,exclam
# 
# This table is consistent with how Leo already works (because it is 
# consistent
# with Tk's key-event specifiers). It is also, I think, the least confusing 
# set of
# rules.
#@-at
#@nonl
#@-node:ekr.20061031131434.2:<< about 'internal' bindings >>
#@nl
#@<< about key dicts >>
#@+node:ekr.20061031131434.3:<< about key dicts >>
#@@nocolor
#@+at
# 
# ivars:
# 
# c.commandsDict:
#     Keys are emacs command names; values are functions f.
# 
# k.inverseCommandsDict:
#     Keys are f.__name__; values are emacs command names.
# 
# k.bindingsDict:
#     Keys are shortcuts; values are *lists* of 
# g.bunch(func,name,warningGiven)
# 
# k.masterBindingsDict:
#     Keys are scope names: 'all','text',etc. or mode names.
#     Values are dicts:  keys are strokes, values are 
# g.Bunch(commandName,func,pane,stroke)
# 
# k.masterGuiBindingsDict:
#     Keys are strokes; value is a list of widgets for which stroke is bound.
# 
# k.settingsNameDict:
#     Keys are lowercase settings; values are 'real' Tk key specifiers.
#     Important: this table has no inverse.
# 
# not an ivar (computed by k.computeInverseBindingDict):
# 
# inverseBindingDict
#     Keys are emacs command names; values are *lists* of shortcuts.
#@-at
#@-node:ekr.20061031131434.3:<< about key dicts >>
#@nl

#@+others
#@+node:ekr.20061031131434.4:class autoCompleterClass
class autoCompleterClass:

    '''A class that inserts autocompleted and calltip text in text widgets.
    This class shows alternatives in the tabbed log pane.

    The keyHandler class contains hooks to support these characters:
    invoke-autocompleter-character (default binding is '.')
    invoke-calltips-character (default binding is '(')
    '''

    #@    @+others
    #@+node:ekr.20061031131434.5: ctor (autocompleter)
    def __init__ (self,k):

        self.c = c = k.c
        self.k = k
        self.allClassesDict = {} # Will be completed after more classes exist.
        self.attrDictDict = {}  # Keys are languages (strings); values are anonymous attrDicts.
            # attrDicts: keys are strings; values are list of strings (attributes).
        self.calltips = {} # Keys are language, values are dicts: keys are ids, values are signatures.
        self.classScanner = self.classScannerClass(c)
        self.forgivingParser = self.forgivingParserClass(c)
        self.globalPythonFunctionsDict = {}
        self.language = None
        self.leadinWord = None
        self.membersList = None
        self.objectDict = {} # Created on first use of the autocompleter.
        self.selection = None # The selection range on entry to autocompleter or calltips.
        self.selectedText = None # The selected text on entry to autocompleter or calltips.
        self.selfClassName = None
        self.selfObjectsDict = {} # Keys are classNames, values are real proxy objects.
        self.selfTnodesDict = {} # Keys are tnodes, values are real proxy objects.
        self.prefix = None
        self.prevObjects = []
        self.tabList = []
        self.tabListIndex = -1
        self.tabName = None # The name of the main completion tab.
        self.object = None # The previously found object, for . chaining.
        self.trace = c.config.getBool('trace_autocompleter')
        self.verbose = False # True: print all members.
        self.watchwords = {} # Keys are ids, values are lists of ids that can follow a id dot.
        self.widget = None # The widget that should get focus after autocomplete is done.
    #@+node:ekr.20061031131434.6:defineClassesDict
    def defineClassesDict (self):

        self.allClassesDict = {}

        # gc may not exist.
        try: import gc
        except ImportError: return

        for z in gc.get_objects():
            t = type(z)
            if t == types.ClassType:
                name = z.__name__
            elif t == types.InstanceType:
                name = z.__class__.__name__
            elif repr(t).startswith('<class'): # A wretched kludge.
                name = z.__class__.__name__
            elif t == types.TypeType:
                name = z.__name__
            else:
                name = None
            if name:
                # if name == 'position': g.trace(t,z)
                self.allClassesDict [name] = z

        # g.printList(self.allClassesDict.keys(),tag='Classes',sort=True)
        # g.trace(len(self.allClassesDict.keys()))
        # g.trace('position:',self.allClassesDict.get('position'))
    #@-node:ekr.20061031131434.6:defineClassesDict
    #@+node:ekr.20061031131434.7:defineObjectDict
    def defineObjectDict (self):

        c = self.c ; k = c.k ; p = c.currentPosition()

        table = [
            # Python globals...
            (['aList','bList'],     'python','list'),
            (['aString'],           'object','aString'), # An actual string object.
            (['cc'],                'object',c.chapterController),
            (['c','old_c','new_c'], 'object',c),            
            (['d','d1','d2'],       'python','dict'),
            (['f'],                 'object',c.frame), 
            (['g'],                 'object',g),       
            (['gui'],               'object',g.app.gui),
            (['k'],                 'object',k),
            (['p','p1','p2'],       'object',p),             
            (['s','s1','s2','ch'],  'object','aString'),
            (['string'],            'object',string), # Python's string module.
            (['t','t1','t2'],       'object',p.v.t),  
            (['v','v1','v2'],       'object',p.v),
            (['w','widget'],        'object',c.frame.body.bodyCtrl),
        ]

        if 0: # Not useful at this point.
            for key in __builtins__.keys():
                obj = __builtins__.get(key)
                if obj in (True,False,None): continue
                data = [key],'object',obj
                table.append(data)

        d = {'dict':{},'int':1,'list':[],'string':''}

        for idList,kind,nameOrObject in table:
            if kind == 'object':
                # Works, but hard to generalize for settings.
                obj = nameOrObject
            elif kind == 'python':
                className = nameOrObject
                o = d.get(className)
                obj = o is not None and o.__class__
            else:
                module = g.importModule (kind,verbose=True)
                if not module:
                    g.trace('Can not import ',nameOrObject)
                    continue
                self.appendToKnownObjects(module)
                if nameOrObject:
                    className = nameOrObject
                    obj = hasattr(module,className) and getattr(module,className) or None
                    if not obj:
                        g.trace('%s module has no class %s' % (kind,nameOrObject))
                    else:
                        self.appendToKnownObjects(getattr(module,className))
                else:
                    obj = module
            for z in idList:
                if obj:
                    self.objectDict[z]=obj
    #@-node:ekr.20061031131434.7:defineObjectDict
    #@-node:ekr.20061031131434.5: ctor (autocompleter)
    #@+node:ekr.20061031131434.8:Top level
    #@+node:ekr.20061031131434.9:autoComplete
    def autoComplete (self,event=None,force=False):

        '''An event handler called from k.masterKeyHanderlerHelper.'''

        c = self.c ; k = self.k ; gui = g.app.gui
        w = gui.eventWidget(event) or c.get_focus()

        # First, handle the invocation character as usual.
        k.masterCommand(event,func=None,stroke=None,commandName=None)

        # Don't allow autocompletion in headlines.
        if not c.widget_name(w).startswith('head'):
            self.language = g.scanForAtLanguage(c,c.currentPosition())
            if w and self.language == 'python' and (k.enable_autocompleter or force):
                self.start(event=event,w=w)

        return 'break'
    #@-node:ekr.20061031131434.9:autoComplete
    #@+node:ekr.20061031131434.10:autoCompleteForce
    def autoCompleteForce (self,event=None):

        '''Show autocompletion, even if autocompletion is not presently enabled.'''

        return self.autoComplete(event,force=True)
    #@-node:ekr.20061031131434.10:autoCompleteForce
    #@+node:ekr.20061031131434.11:autoCompleterStateHandler
    def autoCompleterStateHandler (self,event):

        c = self.c ; k = self.k ; gui = g.app.gui
        tag = 'auto-complete' ; state = k.getState(tag)
        keysym = gui.eventKeysym(event) ; ch = gui.eventChar(event)
        trace = self.trace and not g.app.unitTesting
        if trace: g.trace(repr(ch),repr(keysym),state)

        if state == 0:
            c.frame.log.clearTab(self.tabName)
            self.computeCompletionList()
            k.setState(tag,1,handler=self.autoCompleterStateHandler) 
        elif keysym in (' ','Return'):
            self.finish()
        elif keysym == 'Escape':
            self.abort()
        elif keysym == 'Tab':
            self.doTabCompletion()
        elif keysym == 'BackSpace':
            self.doBackSpace()
        elif keysym == '.':
            self.chain()
        elif keysym == '?':
            self.info()
        elif keysym == '!':
            # Toggle between verbose and brief listing.
            self.verbose = not self.verbose
            if type(self.object) == types.DictType:
                self.membersList = self.object.keys()
            elif type(self.object) in (types.ListType,types.TupleType):
                self.membersList = self.object
            self.computeCompletionList(verbose=self.verbose)
        elif ch and ch in string.printable:
            self.insertNormalChar(ch,keysym)
        else:
            if trace: g.trace('ignore',repr(ch))
            return 'do-standard-keys'
    #@-node:ekr.20061031131434.11:autoCompleterStateHandler
    #@+node:ekr.20061031131434.12:enable/disable/toggleAutocompleter/Calltips
    def disableAutocompleter (self,event=None):
        '''Disable the autocompleter.'''
        self.k.enable_autocompleter = False
        self.showAutocompleterStatus()

    def disableCalltips (self,event=None):
        '''Disable calltips.'''
        self.k.enable_calltips = False
        self.showCalltipsStatus()

    def enableAutocompleter (self,event=None):
        '''Enable the autocompleter.'''
        self.k.enable_autocompleter = True
        self.showAutocompleterStatus()

    def enableCalltips (self,event=None):
        '''Enable calltips.'''
        self.k.enable_calltips = True
        self.showCalltipsStatus()

    def toggleAutocompleter (self,event=None):
        '''Toggle whether the autocompleter is enabled.'''
        self.k.enable_autocompleter = not self.k.enable_autocompleter
        self.showAutocompleterStatus()

    def toggleCalltips (self,event=None):
        '''Toggle whether calltips are enabled.'''
        self.k.enable_calltips = not self.k.enable_calltips
        self.showCalltipsStatus()
    #@-node:ekr.20061031131434.12:enable/disable/toggleAutocompleter/Calltips
    #@+node:ekr.20061031131434.13:showCalltips
    def showCalltips (self,event=None,force=False):

        '''Show the calltips at the cursor.'''

        c = self.c ; k = c.k ; w = g.app.gui.eventWidget(event)
        if not w: return

        # Insert the calltip if possible, but not in headlines.
        if (k.enable_calltips or force) and not c.widget_name(w).startswith('head'):
            self.widget = w
            self.prefix = ''
            self.selection = w.getSelectionRange()
            self.selectedText = w.getSelectedText()
            self.leadinWord = self.findCalltipWord(w)
            # g.trace(self.leadinWord)
            self.object = None
            self.membersList = None
            self.calltip()
        else:
            # Just insert the invocation character as usual.
            k.masterCommand(event,func=None,stroke=None,commandName=None)

        return 'break'
    #@-node:ekr.20061031131434.13:showCalltips
    #@+node:ekr.20061031131434.14:showCalltipsForce
    def showCalltipsForce (self,event=None):

        '''Show the calltips at the cursor, even if calltips are not presently enabled.'''

        return self.showCalltips(event,force=True)
    #@-node:ekr.20061031131434.14:showCalltipsForce
    #@+node:ekr.20061031131434.15:showAutocompleter/CalltipsStatus
    def showAutocompleterStatus (self):
        '''Show the autocompleter status on the status line.'''

        k = self.k
        g.es('Autocompleter %s' % (g.choose(k.enable_autocompleter,'On','Off')),color='red')

    def showCalltipsStatus (self):
        '''Show the autocompleter status on the status line.'''
        k = self.k
        g.es('Calltips %s' % (g.choose(k.enable_calltips,'On','Off')),color='red')
    #@nonl
    #@-node:ekr.20061031131434.15:showAutocompleter/CalltipsStatus
    #@-node:ekr.20061031131434.8:Top level
    #@+node:ekr.20061031131434.16:Helpers
    #@+node:ekr.20061031131434.17:.abort & exit (autocompleter) (test)
    def abort (self):

        k = self.k
        k.keyboardQuit(event=None)
        self.exit(restore=True)

    def exit (self,restore=False): # Called from keyboard-quit.

        k = self ; c = self.c 
        w = self.widget or c.frame.body.bodyCtrl
        for name in (self.tabName,'Modules','Info'):
            c.frame.log.deleteTab(name)
        c.widgetWantsFocusNow(w)
        i,j = w.getSelectionRange()
        if restore:
            if i != j: w.delete(i,j)
            w.insert(i,self.selectedText)
        w.setSelectionRange(j,j,insert=j)

        self.clear()
        self.object = None
    #@-node:ekr.20061031131434.17:.abort & exit (autocompleter) (test)
    #@+node:ekr.20061031131434.18:append/begin/popTabName
    def appendTabName (self,word):

        self.setTabName(self.tabName + word + '.')

    def beginTabName (self,word):

        # g.trace(word,g.callers())
        if word == 'self' and self.selfClassName:
            word = '%s (%s)' % (word,self.selfClassName)
        self.setTabName('AutoComplete ' + word + '.')

    def clearTabName (self):

        self.setTabName('AutoComplete ')

    def popTabName (self):

        s = self.tabName
        i = s.rfind('.',0,-1)
        if i > -1:
            self.setTabName(s[0:i])

    # Underscores are not valid in Pmw tab names!
    def setTabName (self,s):

        c = self.c
        if self.tabName:
            c.frame.log.deleteTab(self.tabName)
        self.tabName = s.replace('_','') or ''
        c.frame.log.clearTab(self.tabName)
    #@-node:ekr.20061031131434.18:append/begin/popTabName
    #@+node:ekr.20061031131434.19:appendToKnownObjects
    def appendToKnownObjects (self,obj):

        if 0:
            if type(obj) in (types.InstanceType,types.ModuleType,types):
                if hasattr(obj,'__name__'):
                    self.knownObjects[obj.__name__] = obj
                    # g.trace('adding',obj.__name__)
    #@-node:ekr.20061031131434.19:appendToKnownObjects
    #@+node:ekr.20061031131434.20:calltip
    def calltip (self,obj=None):

        c = self.c
        w = self.widget
        isStringMethod = False ; s = None
        # g.trace(self.leadinWord,obj)

        if self.leadinWord and (not obj or type(obj) == types.BuiltinFunctionType):
            #@        << try to set s from a Python global function >>
            #@+node:ekr.20061031131434.21:<< try to set s from a Python global function >>
            # The first line of the docstring is good enough, except for classes.
            f = __builtins__.get(self.leadinWord)
            doc = f and type(f) != types.ClassType and f.__doc__
            if doc:
                # g.trace(doc)
                s = g.splitLines(doc)
                s = args = s and s [0] or ''
                i = s.find('(')
                if i > -1: s = s [i:]
                else: s = '(' + s
                s = s and s.strip() or ''
            #@-node:ekr.20061031131434.21:<< try to set s from a Python global function >>
            #@nl

        if not s:
            #@        << get s using inspect >>
            #@+node:ekr.20061031131434.22:<< get s using inspect >>
            isStringMethod = self.prevObjects and type(self.prevObjects[-1]) == types.StringType

            # g.trace(self.prevObjects)

            if isStringMethod and hasattr(string,obj.__name__):
                # A hack. String functions are builtins, and getargspec doesn't handle them.
                # Get the corresponding string function instead, and remove the s arg later.
                obj = getattr(string,obj.__name__)

            try:
                s1,s2,s3,s4 = inspect.getargspec(obj)
            except:
                # g.es('inspect failed:',repr(obj))
                self.extendSelection('(')
                self.finish()
                return # Not a function.  Just '('.

            s = args = inspect.formatargspec(s1,s2,s3,s4)
            #@-node:ekr.20061031131434.22:<< get s using inspect >>
            #@nl

        #@    << remove 'self' from s, but not from args >>
        #@+node:ekr.20061031131434.23:<< remove 'self' from s, but not from args >>
        if g.match(s,1,'self,'):
            s = s[0] + s[6:].strip()
        elif g.match_word(s,1,'self'):
            s = s[0] + s[5:].strip()
        #@-node:ekr.20061031131434.23:<< remove 'self' from s, but not from args >>
        #@nl
        if isStringMethod:
            #@        << remove 's' from s *and* args >>
            #@+node:ekr.20061031131434.24:<< remove 's' from s *and* args >>
            if g.match(s,1,'s,'):
                s = s[0] + s[3:]
                args = args[0] + args[3:]
            elif g.match_word(s,1,'s'):
                s = s[0] + s[2:]
                args = args[0] + args[2:]
            #@-node:ekr.20061031131434.24:<< remove 's' from s *and* args >>
            #@nl

        s = s.rstrip(')') # Convenient.
        #@    << insert the text and set j1 and j2 >>
        #@+node:ekr.20061031131434.25:<< insert the text and set j1 and j2 >>
        junk,j = w.getSelectionRange() # Returns insert point if no selection.
        w.insert(j,s)
        c.frame.body.onBodyChanged('Typing')
        j1 = j + 1 ; j2 = j + len(s)
        #@-node:ekr.20061031131434.25:<< insert the text and set j1 and j2 >>
        #@nl

        # End autocompletion mode, putting the insertion point after the suggested calltip.
        self.finish()
        c.widgetWantsFocusNow(w)
        if 1: # Seems to be more useful.
            w.setSelectionRange(j1,j2,insert=j2)
        else:
            w.setInsertPoint(j2)
        #@    << put the status line >>
        #@+node:ekr.20061031131434.26:<< put the status line >>
        c.frame.clearStatusLine()
        if obj:
            name = hasattr(obj,'__name__') and obj.__name__ or repr(obj)
        else:
            name = self.leadinWord
        c.frame.putStatusLine('%s %s' % (name,args))
        #@-node:ekr.20061031131434.26:<< put the status line >>
        #@nl
    #@-node:ekr.20061031131434.20:calltip
    #@+node:ekr.20061031131434.27:chain
    def chain (self):

        c = self.c ; w = self.widget
        word = w.getSelectedText()
        old_obj = self.object

        if word and old_obj and type(old_obj) == type([]) and old_obj == sys.modules:
            obj = old_obj.get(word)
            if obj:
                self.object = obj
                self.clearTabName()
        elif word and old_obj and self.hasAttr(old_obj,word):
            self.push(old_obj)
            self.object = obj = self.getAttr(old_obj,word)
        else: obj = None

        if obj:
            self.appendToKnownObjects(obj)
            self.leadinWord = word
            self.membersList = self.getMembersList(obj)
            self.appendTabName(word)
            self.extendSelection('.')
            i = w.getInsertPoint()
            w.setSelectionRange(i,i,insert=i)
            # g.trace('chaining to',word,self.object)
            # Similar to start logic.
            self.prefix = ''
            self.selection = w.getSelectionRange()
            self.selectedText = w.getSelectedText()
            if self.membersList:
                # self.autoCompleterStateHandler(event=None)
                self.computeCompletionList()
                return
        self.extendSelection('.')
        self.finish()
    #@-node:ekr.20061031131434.27:chain
    #@+node:ekr.20061031131434.28:computeCompletionList
    def computeCompletionList (self,verbose=False):

        c = self.c ; w = self.widget
        c.widgetWantsFocus(w)
        s = w.getSelectedText()
        self.tabList,common_prefix = g.itemsMatchingPrefixInList(
            s,self.membersList,matchEmptyPrefix=True)

        if not common_prefix:
            if verbose or len(self.tabList) < 25:
                self.tabList,common_prefix = g.itemsMatchingPrefixInList(
                    s,self.membersList,matchEmptyPrefix=True)
            else: # Show the possible starting letters.
                d = {}
                for z in self.tabList:
                    ch = z and z[0] or ''
                    if ch:
                        n = d.get(ch,0)
                        d[ch] = n + 1
                aList = [ch+'...%d' % (d.get(ch)) for ch in d.keys()] ; aList.sort()
                self.tabList = aList

        c.frame.log.clearTab(self.tabName) # Creates the tab if necessary.
        if self.tabList:
            self.tabListIndex = -1 # The next item will be item 0.
            self.setSelection(common_prefix)
        for name in self.tabList:
            g.es('%s' % (name),tabName=self.tabName)
    #@-node:ekr.20061031131434.28:computeCompletionList
    #@+node:ekr.20061031131434.29:doBackSpace (autocompleter)
    def doBackSpace (self):

        '''Cut back to previous prefix.'''

        # g.trace(self.prefix,self.object,self.prevObjects)

        c = self.c
        if self.prefix:
            self.prefix = self.prefix[:-1]
            self.setSelection(self.prefix)
            self.computeCompletionList()
        elif self.object:
            if self.prevObjects:
                obj = self.pop()
            else:
                obj = self.object
            # g.trace(self.object,obj)
            w = self.widget
            s = w.getAllText()
            i,junk = w.getSelectionRange()
            ch = 0 <= i-1 < len(s) and s[i-1] or ''
            # g.trace(ch)
            if ch == '.':
                self.object = obj
                w.delete(i-1)
                c.frame.body.onBodyChanged(undoType='Typing')
                i,j = g.getWord(s,i-2)
                word = s[i:j]
                # g.trace(i,j,repr(word))
                w.setSelectionRange(i,j,insert=j)
                self.prefix = word
                self.popTabName()
                self.membersList = self.getMembersList(obj)
                # g.trace(len(self.membersList))
                if self.membersList:
                    self.computeCompletionList()
                else:
                    self.abort()
            else:
                self.abort() # should not happen.
        else:
            self.abort()            
    #@nonl
    #@-node:ekr.20061031131434.29:doBackSpace (autocompleter)
    #@+node:ekr.20061031131434.30:doTabCompletion (autocompleter)
    def doTabCompletion (self):

        '''Handle tab completion when the user hits a tab.'''

        c = self.c ; w = self.widget
        s = w.getSelectedText()

        if s.startswith(self.prefix) and self.tabList:
            # g.trace('cycle','prefix',repr(self.prefix),len(self.tabList),repr(s))
            # Set the label to the next item on the tab list.
            self.tabListIndex +=1
            if self.tabListIndex >= len(self.tabList):
               self.tabListIndex = 0
            self.setSelection(self.tabList[self.tabListIndex])
        else:
            self.computeCompletionList()

        c.widgetWantsFocusNow(w)
    #@-node:ekr.20061031131434.30:doTabCompletion (autocompleter)
    #@+node:ekr.20061031131434.31:extendSelection
    def extendSelection (self,s):

        '''Append s to the presently selected text.'''

        c = self.c ; w = self.widget
        c.widgetWantsFocusNow(w)

        i,j = w.getSelectionRange()
        w.insert(j,s)
        j += 1
        w.setSelectionRange(i,j,insert=j)
        c.frame.body.onBodyChanged('Typing')
    #@nonl
    #@-node:ekr.20061031131434.31:extendSelection
    #@+node:ekr.20061031131434.32:findAnchor
    def findAnchor (self,w):

        '''Returns (j,word) where j is a Python index.'''

        i = j = w.getInsertPoint()
        s = w.getAllText()

        while i > 0 and s[i-1] == '.':
            i,j = g.getWord(s,i-2)

        word = s[i:j]
        if word == '.': word = None

        # g.trace(i,j,repr(word))
        return j,word
    #@nonl
    #@-node:ekr.20061031131434.32:findAnchor
    #@+node:ekr.20061031131434.33:findCalltipWord
    def findCalltipWord (self,w):

        i = w.getInsertPoint()
        s = w.getAllText()
        if i > 0:
            i,j = g.getWord(s,i-1)
            word = s[i:j]
            return word
        else:
            return ''
    #@nonl
    #@-node:ekr.20061031131434.33:findCalltipWord
    #@+node:ekr.20061031131434.34:finish
    def finish (self):

        c = self.c ; k = self.k

        k.keyboardQuit(event=None)

        for name in (self.tabName,'Modules','Info'):
            c.frame.log.deleteTab(name)

        c.frame.body.onBodyChanged('Typing')
        c.recolor()
        self.clear()
        self.object = None
    #@-node:ekr.20061031131434.34:finish
    #@+node:ekr.20061031131434.35:getAttr and hasAttr
    # The values of self.attrDictDic are anonymous attrDict's.
    # attrDicts: keys are strings, values are lists of strings.

    def getAttr (self,obj,attr):

        '''Simulate getattr function, regardless of langauge.'''

        if self.language == 'python':
            return getattr(obj,attr)
        else:
            d = self.attrDictDict.get(self.language)
            aList = d.get(obj,[])
            return attr in aList and attr

    def hasAttr (self,obj,attr):

        '''Simulate hasattr function, regardless of langauge.'''

        if self.language == 'python':
            return hasattr(obj,attr)
        else:
            d = self.attrDictDict.get(self.language)
            aList = d.get(obj,[])
            return attr in aList
    #@-node:ekr.20061031131434.35:getAttr and hasAttr
    #@+node:ekr.20061031131434.36:getLeadinWord
    def getLeadinWord (self,w):

        self.verbose = False # User must explicitly ask for verbose.
        self.leadinWord = None
        start = w.getInsertPoint()
        s = w.getAllText()
        start -= 1
        i,word = self.findAnchor(w)

        if word and word.isdigit():
            self.membersList = []
            return False

        self.setObjectAndMembersList(word)
        # g.trace(word,self.object,len(self.membersList))

        if not word:
            self.membersList = []
            return False
        elif not self.object:
            self.membersList = []
            return False
        else:
            self.beginTabName(word)
            while 0 <= i < start and i <len(s):
                if s[i] != '.':
                    return False
                i,j = g.getWord(s,i+1)
                word = s[i:j]
                # g.trace(word,i,j,start)
                self.setObjectAndMembersList(word)
                if not self.object:
                    # g.trace('unknown',word)
                    return False
                self.appendTabName(word)
                i = j
            self.leadinWord = word
            return True
    #@-node:ekr.20061031131434.36:getLeadinWord
    #@+node:ekr.20061031131434.37:getMembersList
    def getMembersList (self,obj):

        '''Return a list of possible autocompletions for self.leadinWord.'''

        if obj:
            aList = inspect.getmembers(obj)
            members = ['%s:%s' % (a,g.prettyPrintType(b))
                for a,b in aList if not a.startswith('__')]
            members.sort()
            return members
        else:
            return []
    #@-node:ekr.20061031131434.37:getMembersList
    #@+node:ekr.20061031131434.38:info
    def info (self):

        c = self.c ; doc = None ; obj = self.object ; w = self.widget

        word = w.getSelectedText()

        if not word:
            # Never gets called, but __builtin__.f will work.
            word = self.findCalltipWord(w)
            if word:
                # Try to get the docstring for the Python global.
                f = __builtins__.get(self.leadinWord)
                doc = f and f.__doc__

        if not doc:
            if not self.hasAttr(obj,word):
                g.es('No docstring for %s' % (word),color='blue')
                return
            obj = self.getAttr(obj,word)
            doc = inspect.getdoc(obj)

        if doc:
            c.frame.log.clearTab('Info',wrap='word')
            g.es(doc,tabName='Info')
        else:
            g.es('No docstring for %s' % (word),color='blue')
    #@-node:ekr.20061031131434.38:info
    #@+node:ekr.20061031131434.39:insertNormalChar
    def insertNormalChar (self,ch,keysym):

        k = self.k ; w = self.widget

        if g.isWordChar(ch):
            # Look ahead to see if the character completes any item.
            s = w.getSelectedText() + ch
            tabList,common_prefix = g.itemsMatchingPrefixInList(
                s,self.membersList,matchEmptyPrefix=True)
            if tabList:
                # Add the character.
                self.tabList = tabList
                self.extendSelection(ch)
                s = w.getSelectedText()
                if s.startswith(self.prefix):
                    self.prefix = self.prefix + ch
                self.computeCompletionList()
        else:
            word = w.getSelectedText()
            if ch == '(':
                # Similar to chain logic.
                obj = self.object
                # g.trace(obj,word,self.hasAttr(obj,word))
                if self.hasAttr(obj,word):
                    obj = self.getAttr(obj,word)
                    self.push(self.object)
                    self.object = obj
                    self.leadinWord = word
                    self.membersList = self.getMembersList(obj)
                    if k.enable_calltips:
                        # This calls self.finish if the '(' is valid.
                        self.calltip(obj)
                        return
            self.extendSelection(ch)
            self.finish()
    #@-node:ekr.20061031131434.39:insertNormalChar
    #@+node:ekr.20061031131434.40:push, pop, clear, stackNames
    def push (self,obj):

        if obj is not None:
            self.prevObjects.append(obj)
            # g.trace(self.stackNames())

    def pop (self):

        obj = self.prevObjects.pop()
        # g.trace(obj)
        return obj

    def clear (self):

        self.prevObjects = []
        # g.trace(g.callers())

    def stackNames (self):

        aList = []
        for z in self.prevObjects:
            if hasattr(z,'__name__'):
                aList.append(z.__name__)
            elif hasattr(z,'__class__'):
                aList.append(z.__class__.__name__)
            else:
                aList.append(str(z))
        return aList
    #@-node:ekr.20061031131434.40:push, pop, clear, stackNames
    #@+node:ekr.20061031131434.41:setObjectAndMembersList & helpers
    def setObjectAndMembersList (self,word):

        c = self.c

        if not word:
            # Leading dot shows all classes.
            self.leadinWord = None
            self.object = sys.modules
            self.membersList = sys.modules.keys()
            self.beginTabName('Modules')
        elif word in ( "'",'"'):
            word = 'aString' # This is in the objectsDict.
            self.clear()
            self.push(self.object)
            self.object = 'aString'
            self.membersList = self.getMembersList(self.object)
        elif self.object:
            self.getObjectFromAttribute(word)
        # elif word == 'self':
            # self.completeSelf()
        else:
            obj = self.objectDict.get(word) or sys.modules.get(word)
            self.completeFromObject(obj)

        # g.trace(word,self.object,len(self.membersList))
    #@+node:ekr.20061031131434.42:getObjectFromAttribute
    def getObjectFromAttribute (self,word):

        obj = self.object

        if obj and self.hasAttr(obj,word):
            self.push(self.object)
            self.object = self.getAttr(obj,word)
            self.appendToKnownObjects(self.object)
            self.membersList = self.getMembersList(self.object)
        else:
            # No special support for 'self' here.
            # Don't clear the stack here!
            self.membersList = []
            self.object = None
    #@-node:ekr.20061031131434.42:getObjectFromAttribute
    #@+node:ekr.20061031131434.43:completeSelf
    def completeSelf (self):

        # This scan will be fast if an instant object already exists.
        className,obj,p,s = self.classScanner.scan()
        # g.trace(className,obj,p,s and len(s))

        # First, look up the className.
        if not obj and className:
            obj = self.allClassesDict.get(className)
            # if obj: g.trace('found in allClassesDict: %s = %s' % (className,obj))

        # Second, create the object from class definition.
        if not obj and s:
            theClass = self.computeClassObjectFromString(className,s)
            if theClass:
                obj = self.createProxyObjectFromClass(className,theClass)
                if obj:
                    self.selfObjectsDict [className] = obj
                    # This prevents future rescanning, even if the node moves.
                    self.selfTnodesDict [p.v.t] = obj
        if obj:
            self.selfClassName = className
            self.push(self.object)
            self.object = obj
            self.membersList = self.getMembersList(obj=obj)
        else:
            # No further action possible or desirable.
            self.selfClassName = None
            self.object = None
            self.clear()
            self.membersList = []
    #@-node:ekr.20061031131434.43:completeSelf
    #@+node:ekr.20061031131434.44:completeFromObject
    def completeFromObject (self,obj):

        if obj:
            self.appendToKnownObjects(obj)
            self.push(self.object)
            self.object = obj
            self.membersList = self.getMembersList(obj=obj)
        else:
            self.object = None
            self.clear()
            self.membersList = []
    #@-node:ekr.20061031131434.44:completeFromObject
    #@-node:ekr.20061031131434.41:setObjectAndMembersList & helpers
    #@+node:ekr.20061031131434.45:setSelection
    def setSelection (self,s):

        c = self.c ; w = self.widget
        c.widgetWantsFocusNow(w)

        if w.hasSelection():
            i,j = w.getSelectionRange()
            w.delete(i,j)
        else:
            i = w.getInsertPoint()

        # Don't go past the ':' that separates the completion from the type.
        n = s.find(':')
        if n > -1: s = s[:n]

        w.insert(i,s)
        j = i + len(s)
        w.setSelectionRange(i,j,insert=j)

        # New in Leo 4.4.2: recolor immediately to preserve the new selection in the new colorizer.
        c.frame.body.recolor_now(c.currentPosition(),incremental=True)
        # Usually this call will have no effect because the body text has not changed.
        c.frame.body.onBodyChanged('Typing')
    #@-node:ekr.20061031131434.45:setSelection
    #@+node:ekr.20061031131434.46:start
    def start (self,event=None,w=None):

        c = self.c
        if w: self.widget = w
        else: w = self.widget

        # We wait until now to define these dicts so that more classes and objects will exist.
        if not self.objectDict:
            self.defineClassesDict()
            self.defineObjectDict()

        self.prefix = ''
        self.selection = w.getSelectionRange()
        self.selectedText = w.getSelectedText()
        flag = self.getLeadinWord(w)
        if self.membersList:
            if not flag:
                # Remove the (leading) invocation character.
                i = w.getInsertPoint()
                s = w.getAllText()
                if i > 0 and s[i-1] == '.':
                    s = g.app.gui.stringDelete(s,i-1)
                    w.setAllText(s)
                    c.frame.body.onBodyChanged('Typing')
            self.autoCompleterStateHandler(event)
        else:
            self.abort()
    #@-node:ekr.20061031131434.46:start
    #@-node:ekr.20061031131434.16:Helpers
    #@+node:ekr.20061031131434.47:Scanning
    # Not used at present, but soon.
    #@+node:ekr.20061031131434.48:initialScan
    # Don't call this finishCreate: the startup logic would call it too soon.

    def initialScan (self):

        g.trace(g.callers())

        self.scan(thread=True)
    #@-node:ekr.20061031131434.48:initialScan
    #@+node:ekr.20061031131434.49:scan
    def scan (self,event=None,verbose=True,thread=True):

        __pychecker__ = '--no-argsused' # thread arg not used at present.

        c = self.c
        if not c or not c.exists or c.frame.isNullFrame: return
        if g.app.unitTesting: return

        # g.trace('autocompleter')

        if 0: # thread:
            # Use a thread to do the initial scan so as not to interfere with the user.            
            def scan ():
                #g.es( "This is for testing if g.es blocks in a thread", color = 'pink' )
                # During unit testing c gets destroyed before the scan finishes.
                if not g.app.unitTesting:
                    self.scanOutline(verbose=True)

            t = threading.Thread(target=scan)
            t.setDaemon(True)
            t.start()
        else:
            self.scanOutline(verbose=verbose)
    #@-node:ekr.20061031131434.49:scan
    #@+node:ekr.20061031131434.50:definePatterns
    def definePatterns (self):

        self.space = r'[ \t\r\f\v ]+' # one or more whitespace characters.
        self.end = r'\w+\s*\([^)]*\)' # word (\w) ws ( any ) (can cross lines)

        # Define re patterns for various languages.
        # These patterns match method/function definitions.
        self.pats = {}
        self.pats ['python'] = re.compile(r'def\s+%s' % self.end)  # def ws word ( any ) # Can cross line boundaries.
        self.pats ['java'] = re.compile(
            r'((public\s+|private\s+|protected\s+)?(static%s|\w+%s){1,2}%s)' % (
                self.space,self.space,self.end))
        self.pats ['perl'] = re.compile(r'sub\s+%s' % self.end)
        self.pats ['c++'] = re.compile(r'((virtual\s+)?\w+%s%s)' % (self.space,self.end))
        self.pats ['c'] = re.compile(r'\w+%s%s' % (self.space,self.end))

        # Define self.okchars for getCleaString.
        okchars = {}
        for z in string.ascii_letters:
            okchars [z] = z
        okchars ['_'] = '_'
        self.okchars = okchars 
    #@nonl
    #@-node:ekr.20061031131434.50:definePatterns
    #@+node:ekr.20061031131434.51:scanOutline
    def scanOutline (self,verbose=True):

        '''Traverse an outline and build the autocommander database.'''

        if verbose: g.es_print('Scanning for auto-completer...')

        c = self.c ; k = self.k ; count = 0
        for p in c.allNodes_iter():
            if verbose:
                count += 1 ;
                if (count % 200) == 0: g.es('.',newline=False)
            language = g.scanForAtLanguage(c,p)
            # g.trace('language',language,p.headString())
            s = p.bodyString()
            if k.enable_autocompleter:
                self.scanForAutoCompleter(s)
            if k.enable_calltips:
                self.scanForCallTip(s,language)

        if 0:
            g.trace('watchwords...\n\n')
            keys = self.watchwords.keys() ; keys.sort()
            for key in keys:
                aList = self.watchwords.get(key)
                g.trace('%s:\n\n' % (key), g.listToString(aList))
        if 0:
            g.trace('calltips...\n\n')
            keys = self.calltips.keys() ; keys.sort()
            for key in keys:
                d = self.calltips.get(key)
                if d:
                    g.trace('%s:\n\n' % (key), g.dictToString(d))

        if verbose:        
            g.es_print('\nauto-completer scan complete',color='blue')
    #@-node:ekr.20061031131434.51:scanOutline
    #@+node:ekr.20061031131434.52:scanForCallTip
    def scanForCallTip (self,s,language):

        '''this function scans text for calltip info'''

        d = self.calltips.get(language,{})
        pat = self.pats.get(language or 'python')

        # Set results to a list of all the function/method defintions in s.
        results = pat and pat.findall(s) or []

        for z in results:
            if isinstance(z,tuple): z = z [0]
            pieces2 = z.split('(')
            # g.trace(pieces2)
            pieces2 [0] = pieces2 [0].split() [-1]
            a, junk = pieces2 [0], pieces2 [1]
            aList = d.get(a,[])
            if str(z) not in aList:
                aList.append(str(z))
                d [a] = aList

        self.calltips [language] = d
    #@-node:ekr.20061031131434.52:scanForCallTip
    #@+node:ekr.20061031131434.53:scanForAutoCompleter
    def scanForAutoCompleter (self,s):

        '''This function scans text for the autocompleter database.'''

        aList = [] ; t1 = s.split('.')

        if 1: # Slightly faster.
            t1 = s.split('.') ; 
            i = 0 ; n = len(t1)-1
            while i < n:
                self.makeAutocompletionList(t1[i],t1[i+1],aList)
                i += 1
        else:
            reduce(lambda a,b: self.makeAutocompletionList(a,b,aList),t1)

        if aList:
            for a, b in aList:
                z = self.watchwords.get(a,[])
                if str(b) not in z:
                    z.append(str(b))
                    self.watchwords [a] = z
    #@+node:ekr.20061031131434.54:makeAutocompletionList
    def makeAutocompletionList (self,a,b,glist):

        '''We have seen a.b, where a and b are arbitrary strings.
        Append (a1.b1) to glist.
        To compute a1, scan backwards in a until finding whitespace.
        To compute b1, scan forwards in b until finding a char not in okchars.
        '''

        if 1: # Do everything inline.  It's a few percent faster.

            # Compute reverseFindWhitespace inline.
            i = len(a) -1
            while i >= 0:
                if a[i].isspace() or a [i] == '.':
                    a1 = a [i+1:] ; break
                i -= 1
            else:
                a1 = a

            # Compute getCleanString inline.
            i = 0
            for ch in b:
                if ch not in self.okchars:
                    b1 = b[:i] ; break
                i += 1
            else:
                b1 = b

            if b1:
                glist.append((a1,b1),)

            return b # Not needed unless we are using reduce.
        else:
            a1 = self.reverseFindWhitespace(a)
            if a1:
                b1 = self.getCleanString(b)
                if b1:
                    glist.append((a1,b1))
            return b
    #@+node:ekr.20061031131434.55:reverseFindWhitespace
    def reverseFindWhitespace (self,s):

        '''Return the longest tail of s containing no whitespace or period.'''

        i = len(s) -1
        while i >= 0:
            if s[i].isspace() or s [i] == '.': return s [i+1:]
            i -= 1

        return s
    #@-node:ekr.20061031131434.55:reverseFindWhitespace
    #@+node:ekr.20061031131434.56:getCleanString
    def getCleanString (self,s):

        '''Return the prefix of s containing only chars in okchars.'''

        i = 0
        for ch in s:
            if ch not in self.okchars:
                return s[:i]
            i += 1

        return s
    #@-node:ekr.20061031131434.56:getCleanString
    #@-node:ekr.20061031131434.54:makeAutocompletionList
    #@-node:ekr.20061031131434.53:scanForAutoCompleter
    #@-node:ekr.20061031131434.47:Scanning
    #@+node:ekr.20061031131434.57:Proxy classes and objects
    #@+node:ekr.20061031131434.58:createProxyObjectFromClass
    def createProxyObjectFromClass (self,className,theClass):

        '''Create a dummy instance object by instantiating theClass with a dummy ctor.'''

        if 0: # Calling the real ctor is way too dangerous.
            # Set args to the list of required arguments.
            args = inspect.getargs(theClass.__init__.im_func.func_code)
            args = args[0] ; n = len(args)-1
            args = [None for z in xrange(n)]

        def dummyCtor (self):
            pass

        try:
            obj = None
            old_init = hasattr(theClass,'__init__') and theClass.__init__
            theClass.__init__ = dummyCtor
            obj = theClass()
        finally:
            if old_init:
                theClass.__init__ = old_init
            else:
                delattr(theClass,'__init__')

        g.trace(type(theClass),obj)

        # Verify that it has all the proper attributes.
        # g.trace(g.listToString(dir(obj)))
        return obj
    #@-node:ekr.20061031131434.58:createProxyObjectFromClass
    #@+node:ekr.20061031131434.59:createClassObjectFromString
    def computeClassObjectFromString (self,className,s):

        try:
            # Add the the class definition to the present environment.
            exec s

            # Get the newly created object from the locals dict.
            theClass = locals().get(className)
            return theClass

        except Exception:
            if 1: # Could be a weird kind of user error.
                g.es_print('unexpected exception in computeProxyObject')
                g.es_exception()
            return None
    #@-node:ekr.20061031131434.59:createClassObjectFromString
    #@-node:ekr.20061031131434.57:Proxy classes and objects
    #@+node:ekr.20061031131434.60:class forgivingParserClass
    class forgivingParserClass:

        '''A class to create a valid class instances from
        a class definition that may contain syntax errors.'''

        #@    @+others
        #@+node:ekr.20061031131434.61:ctor (forgivingParserClass)
        def __init__ (self,c):

            self.c = c
            self.excludedTnodesList = []
            self.old_putBody = None # Set in parse for communication with newPutBody.
        #@-node:ekr.20061031131434.61:ctor (forgivingParserClass)
        #@+node:ekr.20061031131434.62:parse
        def parse (self,p):

            '''The top-level parser method.

            It patches c.atFileCommands.putBody, calls the forgiving parser and finally
            restores c.atFileCommands.putBody.'''

            c = self.c

            # Create an ivar for communication with newPutBody.
            self.old_putBody = c.atFileCommands.putBody

            # Override atFile.putBody.
            c.atFileCommands.putBody = self.newPutBody

            try:
                s = None
                s = self.forgivingParser(p)
            finally:
                c.atFileCommands.putBody = self.old_putBody

            return s # Bug fix: 4/29/07: Don't put a return in a finally clause.


        #@-node:ekr.20061031131434.62:parse
        #@+node:ekr.20061031131434.63:forgivingParser
        def forgivingParser (self,p):

            c = self.c ; root = p.copy()
            self.excludedTnodesList = []
            s = g.getScript(c,root,useSelectedText=False)
            while s:
                try:
                    val = compiler.parse(s+'\n')
                    break
                except (parser.ParserError,SyntaxError):
                    fileName, n = g.getLastTracebackFileAndLineNumber()
                    p = self.computeErrorNode(c,root,n,lines=g.splitLines(s))
                    if not p or p == root:
                        g.es_print('Syntax error in class node: can not continue')
                        s = None ; break
                    else:
                        # g.es_print('Syntax error: deleting %s' % p.headString())
                        self.excludedTnodesList.append(p.v.t)
                        s = g.getScript(c,root,useSelectedText=False)
            return s or ''
        #@-node:ekr.20061031131434.63:forgivingParser
        #@+node:ekr.20061031131434.64:computeErrorNode
        def computeErrorNode (self,c,root,n,lines):

            '''The from c.goToLineNumber that applies to scripts.
            Unlike c.gotoLineNumberOpen, this function returns a position.'''

            if n == 1 or n >= len(lines):
                return root

            vnodeName, junk, junk, junk, junk = c.convertLineToVnodeNameIndexLine(
                lines, n, root, scriptFind = True)

            if vnodeName:
                for p in root.self_and_subtree_iter():
                    if p.matchHeadline(vnodeName):
                        return p

            return None
        #@-node:ekr.20061031131434.64:computeErrorNode
        #@+node:ekr.20061031131434.65:newPutBody
        def newPutBody (self,p,oneNodeOnly=False,fromString=''):

            if p.v.t in self.excludedTnodesList:
                pass
                # g.trace('ignoring',p.headString())
            else:
                self.old_putBody(p,oneNodeOnly,fromString)
        #@-node:ekr.20061031131434.65:newPutBody
        #@-others
    #@-node:ekr.20061031131434.60:class forgivingParserClass
    #@+node:ekr.20061031131434.66:class classScannerClass
    class classScannerClass:

        '''A class to find class definitions in a node or its parents.'''

        #@    @+others
        #@+node:ekr.20061031131434.67:ctor
        def __init__ (self,c):

            self.c = c

            # Ignore @root for now:
            # self.start_in_doc = c.config.getBool('at_root_bodies_start_in_doc_mode')

            self.start_in_doc = False
        #@-node:ekr.20061031131434.67:ctor
        #@+node:ekr.20061031131434.68:scan
        def scan (self):

            c = self.c

            className,obj,p = self.findParentClass(c.currentPosition())
            # g.trace(className,obj,p)

            if p and not obj:
                parser = c.k.autoCompleter.forgivingParser
                s = parser.parse(p)
            else:
                s = None

            return className,obj,p,s
        #@-node:ekr.20061031131434.68:scan
        #@+node:ekr.20061031131434.69:findParentClass
        def findParentClass (self,root):

            autoCompleter = self.c.k.autoCompleter

            # First, see if any parent has already been scanned.
            for p in root.self_and_parents_iter():
                obj = autoCompleter.selfTnodesDict.get(p.v.t)
                if obj:
                    # g.trace('found',obj,'in',p.headString())
                    return None,obj,p

            # Next, do a much slower scan.
            # g.trace('slow scanning...')
            for p in root.self_and_parents_iter():
                className = self.findClass(p)
                if className:
                    # g.trace('found',className,'in',p.headString())
                    return className,None,p

            return None,None,None
        #@-node:ekr.20061031131434.69:findParentClass
        #@+node:ekr.20061031131434.70:findClass & helpers
        def findClass (self,p):

            lines = g.splitLines(p.bodyString())
            inDoc = self.start_in_doc
            # g.trace(p.headString())
            for s in lines:
                if inDoc:
                    if self.endsDoc(s):
                        inDoc = False
                else:
                    if self.startsDoc(s):
                        inDoc = True
                    else:
                        # Not a perfect scan: a triple-string could start with 'class',
                        # but perfection is not important.
                        className = self.startsClass(s)
                        if className: return className
            else:
                return None
        #@+node:ekr.20061031131434.71:endsDoc
        def endsDoc (self,s):

            return s.startswith('@c')
        #@-node:ekr.20061031131434.71:endsDoc
        #@+node:ekr.20061031131434.72:startsClass
        def startsClass (self,s):

            if s.startswith('class'):
                i = 5
                i = g.skip_ws(s,i)
                j = g.skip_id(s,i)
                word = s[i:j]
                # g.trace(word)
                return word
            else:
                return None
        #@-node:ekr.20061031131434.72:startsClass
        #@+node:ekr.20061031131434.73:startsDoc
        def startsDoc (self,s):

            for s2 in ('@doc','@ ','@\n', '@r', '@\t'):
                if s.startswith(s2):
                    return True
            else:
                return False
        #@-node:ekr.20061031131434.73:startsDoc
        #@-node:ekr.20061031131434.70:findClass & helpers
        #@-others
    #@-node:ekr.20061031131434.66:class classScannerClass
    #@-others
#@-node:ekr.20061031131434.4:class autoCompleterClass
#@+node:ekr.20061031131434.74:class keyHandlerClass
class keyHandlerClass:

    '''A class to support emacs-style commands.'''

    # Gui-independent class vars.

    global_killbuffer = []
        # Used only if useGlobalKillbuffer arg to Emacs ctor is True.
        # Otherwise, each Emacs instance has its own local kill buffer.

    global_registers = {}
        # Used only if useGlobalRegisters arg to Emacs ctor is True.
        # Otherwise each Emacs instance has its own set of registers.

    lossage = []
        # A case could be made for per-instance lossage, but this is not supported.

    #@    @+others
    #@+node:ekr.20061031131434.75: Birth (keyHandler)
    #@+node:ekr.20061031131434.76: ctor (keyHandler)
    def __init__ (self,c,useGlobalKillbuffer=False,useGlobalRegisters=False):

        '''Create a key handler for c.
        c.frame.miniBufferWidget is a Tk.Label.

        useGlobalRegisters and useGlobalKillbuffer indicate whether to use
        global (class vars) or per-instance (ivars) for kill buffers and registers.'''

        # g.trace('base keyHandler',g.callers())

        self.c = c
        self.widget = c.frame.miniBufferWidget
        self.useTextWidget = c.useTextMinibuffer
            # A Tk Label or Text widget.
            # Exists even if c.showMinibuffer is False.
        self.useGlobalKillbuffer = useGlobalKillbuffer
        self.useGlobalRegisters = useGlobalRegisters

        # Generalize...
        self.x_hasNumeric = ['sort-lines','sort-fields']

        self.altX_prompt = 'full-command: '

        # These must be defined here to avoid memory leaks.
        self.enable_autocompleter           = c.config.getBool('enable_autocompleter_initially')
        self.enable_calltips                = c.config.getBool('enable_calltips_initially')
        self.ignore_caps_lock               = c.config.getBool('ignore_caps_lock')
        self.ignore_unbound_non_ascii_keys  = c.config.getBool('ignore_unbound_non_ascii_keys')
        self.swap_mac_keys                  = c.config.getBool('swap_mac_keys')
        self.trace_bind_key_exceptions      = c.config.getBool('trace_bind_key_exceptions')
        self.trace_masterClickHandler       = c.config.getBool('trace_masterClickHandler')
        self.traceMasterCommand             = c.config.getBool('trace_masterCommand')
        self.trace_masterKeyHandler         = c.config.getBool('trace_masterKeyHandler')
        self.trace_masterKeyHandlerGC       = c.config.getBool('trace_masterKeyHandlerGC')
        self.trace_key_event                = c.config.getBool('trace_key_event')
        self.trace_minibuffer               = c.config.getBool('trace_minibuffer')
        self.warn_about_redefined_shortcuts = c.config.getBool('warn_about_redefined_shortcuts')
        #@    << define externally visible ivars >>
        #@+node:ekr.20061031131434.78:<< define externally visible ivars >>
        self.abbrevOn = False # True: abbreviations are on.
        self.arg = '' # The value returned by k.getArg.
        self.commandName = None # The name of the command being executed.
        self.funcReturn = None # For k.simulateCommand
        self.getArgEscape = None # A signal that the user escaped getArg in an unusual way.
        self.inputModeBindings = {}
        self.inputModeName = '' # The name of the input mode, or None.
        self.inverseCommandsDict = {}
            # Completed in k.finishCreate, but leoCommands.getPublicCommands adds entries first.
        self.negativeArg = False
        self.newMinibufferWidget = None # Usually the minibuffer restores focus.  This overrides this default.
        self.regx = g.bunch(iter=None,key=None)
        self.repeatCount = None
        self.previousSelection = None # A hack for middle-button paste: set by masterClickHandler, used by pasteText.
        self.state = g.bunch(kind=None,n=None,handler=None)
        #@-node:ekr.20061031131434.78:<< define externally visible ivars >>
        #@nl
        #@    << define internal ivars >>
        #@+node:ekr.20061031131434.79:<< define internal ivars >>
        self.abbreviationsDict = {} # Abbreviations created by @alias nodes.

        # Previously defined bindings.
        self.bindingsDict = {}
            # Keys are Tk key names, values are lists of g.bunch(pane,func,commandName)
        # Previously defined binding tags.
        self.bindtagsDict = {}
            # Keys are strings (the tag), values are 'True'
        self.masterBindingsDict = {}
            # Keys are scope names: 'all','text',etc. or mode names.
            # Values are dicts: keys are strokes, values are g.bunch(commandName,func,pane,stroke)
        self.masterGuiBindingsDict = {}
            # Keys are strokes; value is True;

        # Special bindings for k.fullCommand.
        self.mb_copyKey = None
        self.mb_pasteKey = None
        self.mb_cutKey = None
        self.mb_help = False

        self.abortAllModesKey = None
        self.fullCommandKey = None
        self.universalArgKey = None

        # Keepting track of the characters in the mini-buffer.
        self.arg_completion = True
        self.mb_event = None
        self.mb_history = []
        self.mb_prefix = ''
        self.mb_tabListPrefix = ''
        self.mb_tabList = []
        self.mb_tabListIndex = -1
        self.mb_prompt = ''

        self.func = None
        self.previous = []
        self.stroke = None

        # For onIdleTime
        self.idleCount = 0

        # For modes
        self.afterGetArgState = None
        self.argTabList = []
        self.getArgEscapes = []
        self.modeBindingsDict = {}
        self.modeWidget = None
        self.silentMode = False

        # The actual values are set later in k.finishCreate.
        self.command_mode_bg_color = 'white'
        self.command_mode_fg_color = 'black'
        self.insert_mode_bg_color = 'white'
        self.insert_mode_fg_color = 'black'
        self.overwrite_mode_bg_color = 'white'
        self.overwrite_mode_fg_color = 'black'
        #@-node:ekr.20061031131434.79:<< define internal ivars >>
        #@nl

        self.defineTkNames()
        self.defineSpecialKeys()
        self.autoCompleter = autoCompleterClass(self)
        self.setDefaultUnboundKeyAction()
    #@-node:ekr.20061031131434.76: ctor (keyHandler)
    #@+node:ekr.20061031131434.80:k.finishCreate & helpers
    def finishCreate (self):

        '''Complete the construction of the keyHandler class.
        c.commandsDict has been created when this is called.'''

        k = self ; c = k.c
        # g.trace('keyHandler')
        k.createInverseCommandsDict()

        # Important: bindings exist even if c.showMiniBuffer is False.
        k.makeAllBindings()

        # Set mode colors used by k.setInputState.
        bg = c.config.getColor('body_text_background_color') or 'white'
        fg = c.config.getColor('body_text_foreground_color') or 'black'

        k.command_mode_bg_color = c.config.getColor('command_mode_bg_color') or bg
        k.command_mode_fg_color = c.config.getColor('command_mode_fg_color') or fg
        k.insert_mode_bg_color = c.config.getColor('insert_mode_bg_color') or bg
        k.insert_mode_fg_color = c.config.getColor('insert_mode_fg_color') or fg
        k.overwrite_mode_bg_color = c.config.getColor('overwrite_mode_bg_color') or bg
        k.overwrite_mode_fg_color = c.config.getColor('overwrite_mode_fg_color') or fg

        # g.trace(k.insert_mode_bg_color,k.insert_mode_fg_color,k)

        k.setInputState(self.unboundKeyAction)
    #@nonl
    #@+node:ekr.20061031131434.81:createInverseCommandsDict
    def createInverseCommandsDict (self):

        '''Add entries to k.inverseCommandsDict using c.commandDict.

        c.commandsDict:        keys are command names, values are funcions f.
        k.inverseCommandsDict: keys are f.__name__, values are minibuffer command names.
        '''

        k = self ; c = k.c

        for name in c.commandsDict.keys():
            f = c.commandsDict.get(name)
            try:
                k.inverseCommandsDict [f.__name__] = name
                # g.trace('%24s = %s' % (f.__name__,name))

            except Exception:
                g.es_exception()
                g.trace(repr(name),repr(f),g.callers())
    #@-node:ekr.20061031131434.81:createInverseCommandsDict
    #@-node:ekr.20061031131434.80:k.finishCreate & helpers
    #@+node:ekr.20061031131434.82:setDefaultUnboundKeyAction
    def setDefaultUnboundKeyAction (self):

        k = self ; c = k.c

        # g.trace(g.callers())

        defaultAction = c.config.getString('top_level_unbound_key_action') or 'insert'
        defaultAction.lower()

        if defaultAction in ('command','insert','overwrite'):
            self.unboundKeyAction = defaultAction
        else:
            g.trace('ignoring top_level_unbound_key_action setting: %s' % defaultAction)
            self.unboundKeyAction = 'insert'

        k.setInputState(self.unboundKeyAction)
    #@-node:ekr.20061031131434.82:setDefaultUnboundKeyAction
    #@+node:ekr.20070123143428:k.defineTkNames
    def defineTkNames (self):

        k = self

        # These names are used in Leo's core *regardless* of the gui actually in effect.
        # The gui is responsible for translating gui-dependent keycodes into these values.
        k.tkNamesList = (
            'BackSpace','Begin','Break',
            'Caps_Lock','Clear',
            'Delete','Down',
            'End','Escape',
            'F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12',
            'Home',
            'Left','Linefeed',
            'Next','Num_Lock',
            'Prior',
            'Return','Right',
            'Tab',
            'Up',
            # 'space',
        )

        # These keys settings that may be specied in leoSettings.leo.
        # Keys are lowercase, so that case is not significant *for these items only* in leoSettings.leo.
        k.settingsNameDict = {
            'bksp'    : 'BackSpace',
            'dnarrow' : 'Down',
            'esc'     : 'Escape',
            'ltarrow' : 'Left',
            'pageup'  : 'Prior',
            'pagedn'  : 'Next',
            'rtarrow' : 'Right',
            'uparrow' : 'Up',
        }

        # Add lowercase version of special keys.
        for s in k.tkNamesList:
            k.settingsNameDict [s.lower()] = s


    #@+at  
    #@nonl
    # The following are not translated, so what appears in the menu is the 
    # same as what is passed to Tk.  Case is significant.
    # Note: the Tk documentation states that not all of these may be available 
    # on all platforms.
    # 
    # Num_Lock, Pause, Scroll_Lock, Sys_Req,
    # KP_Add, KP_Decimal, KP_Divide, KP_Enter, KP_Equal,
    # KP_Multiply, KP_Separator,KP_Space, KP_Subtract, KP_Tab,
    # KP_F1,KP_F2,KP_F3,KP_F4,
    # KP_0,KP_1,KP_2,KP_3,KP_4,KP_5,KP_6,KP_7,KP_8,KP_9
    #@-at
    #@-node:ekr.20070123143428:k.defineTkNames
    #@+node:ekr.20070123085931:k.defineSpecialKeys
    def defineSpecialKeys (self):

        '''Define k.guiBindNamesDict and k.guiBindNamesInverseDict.

        Important: all gui's use these dictionaries because bindings in
        leoSettings.leo use these representations.'''

        k = self

        # g.trace('base keyHandler')

        # These are defined at http://tcl.activestate.com/man/tcl8.4/TkCmd/keysyms.htm.
        # Important: only the inverse dict is actually used in the new key binding scheme.
        # Tk may return the *values* of this dict in event.keysym fields.
        # Leo will warn if it gets a event whose keysym not in values of this table.
        k.guiBindNamesDict = {
            "&" : "ampersand",
            "^" : "asciicircum",
            "~" : "asciitilde",
            "*" : "asterisk",
            "@" : "at",
            "\\": "backslash",
            "|" : "bar",
            "{" : "braceleft",
            "}" : "braceright",
            "[" : "bracketleft",
            "]" : "bracketright",
            ":" : "colon",      # removed from code.
            "," : "comma",
            "$" : "dollar",
            "=" : "equal",
            "!" : "exclam",     # removed from code.
            ">" : "greater",
            "<" : "less",
            "-" : "minus",
            "#" : "numbersign",
            '"' : "quotedbl",
            "'" : "quoteright",
            "(" : "parenleft",
            ")" : "parenright", # removed from code.
            "%" : "percent",
            "." : "period",     # removed from code.
            "+" : "plus",
            "?" : "question",
            "`" : "quoteleft",
            ";" : "semicolon",
            "/" : "slash",
            " " : "space",      # removed from code.
            "_" : "underscore",
        }

        # No translation.
        for s in k.tkNamesList:
            k.guiBindNamesDict[s] = s

        # Create the inverse dict.
        k.guiBindNamesInverseDict = {}
        for key in k.guiBindNamesDict.keys():
            k.guiBindNamesInverseDict [k.guiBindNamesDict.get(key)] = key

    #@-node:ekr.20070123085931:k.defineSpecialKeys
    #@+node:ekr.20061101071425:oops
    def oops (self):

        g.trace('Should be defined in subclass:',g.callers())
    #@-node:ekr.20061101071425:oops
    #@-node:ekr.20061031131434.75: Birth (keyHandler)
    #@+node:ekr.20061031131434.88:Binding (keyHandler)
    #@+node:ekr.20061031131434.89:bindKey
    def bindKey (self,pane,shortcut,callback,commandName,modeFlag=False):

        '''Bind the indicated shortcut (a Tk keystroke) to the callback.

        No actual gui bindings are made: only entries in k.masterBindingsDict.'''

        k = self ; c = k.c

        # g.trace(pane,shortcut,commandName)
        if not shortcut:
            # g.trace('No shortcut for %s' % commandName)
            return False
        #@    << give warning and return if we try to bind to Enter or Leave >>
        #@+node:ekr.20061031131434.90:<< give warning and return if we try to bind to Enter or Leave >>
        if shortcut:
            for s in ('enter','leave'):
                if -1 != shortcut.lower().find(s):
                    g.es_print('Ignoring invalid key binding: %s = %s' % (
                        commandName,shortcut),color='blue')
                    return
        #@-node:ekr.20061031131434.90:<< give warning and return if we try to bind to Enter or Leave >>
        #@nl
        if pane.endswith('-mode'):
            g.trace('oops: ignoring mode binding',shortcut,commandName,g.callers())
            return False
        bunchList = k.bindingsDict.get(shortcut,[])
        #@    << trace bindings >>
        #@+node:ekr.20061031131434.91:<< trace bindings >>
        if c.config.getBool('trace_bindings_verbose'):
            theFilter = c.config.getString('trace_bindings_filter') or ''
            # g.trace(repr(theFilter))
            if not theFilter or shortcut.find(theFilter) != -1:
                pane_filter = c.config.getString('trace_bindings_pane_filter')
                if not pane_filter or pane_filter.lower() == pane:
                    g.trace(pane,shortcut,commandName)
        #@-node:ekr.20061031131434.91:<< trace bindings >>
        #@nl
        try:
            k.bindKeyToDict(pane,shortcut,callback,commandName)
            b = g.bunch(pane=pane,func=callback,commandName=commandName)
            #@        << remove previous conflicting definitions from bunchList >>
            #@+node:ekr.20061031131434.92:<< remove previous conflicting definitions from bunchList >>
            if not modeFlag and self.warn_about_redefined_shortcuts:
                redefs = [str(b2.commandName) for b2 in bunchList
                    if b2.commandName != commandName and pane in ('button','all',b2.pane)
                        and not b2.pane.endswith('-mode')]
                for z in redefs:
                    g.es_print('redefining %s in %s to %s in %s' % (
                        z,b2.pane,commandName,pane),color='red')

            if not modeFlag:
                bunchList = [b2 for b2 in bunchList if pane not in ('button','all',b2.pane)]
            #@-node:ekr.20061031131434.92:<< remove previous conflicting definitions from bunchList >>
            #@nl
            bunchList.append(b)
            shortcut = g.stripBrackets(shortcut.strip())
            k.bindingsDict [shortcut] = bunchList
            return True
        except Exception: # Could be a user error.
            if not g.app.menuWarningsGiven:
                g.es_print('Exception binding %s to %s' % (shortcut,commandName))
                g.es_exception()
                g.app.menuWarningsGiven = True
            return False

    bindShortcut = bindKey # For compatibility
    #@-node:ekr.20061031131434.89:bindKey
    #@+node:ekr.20061031131434.93:bindKeyToDict
    def bindKeyToDict (self,pane,stroke,func,commandName):

        k = self
        d =  k.masterBindingsDict.get(pane,{})

        stroke = g.stripBrackets(stroke)

        if 0:
            g.trace('%-4s %-18s %-40s %s' % (
                pane,repr(stroke),commandName,func and func.__name__))

        # New in Leo 4.4.1: Allow redefintions.
        d [stroke] = g.Bunch(commandName=commandName,func=func,pane=pane,stroke=stroke)
        k.masterBindingsDict [pane] = d
    #@-node:ekr.20061031131434.93:bindKeyToDict
    #@+node:ekr.20061031131434.94:bindOpenWith
    def bindOpenWith (self,shortcut,name,data):

        '''Register an open-with command.'''

        k = self ; c = k.c

        # The first parameter must be event, and it must default to None.
        def openWithCallback(event=None,c=c,data=data):
            return c.openWith(data=data)

        # Use k.registerCommand to set the shortcuts in the various binding dicts.
        commandName = 'open-with-%s' % name.lower()
        k.registerCommand(commandName,shortcut,openWithCallback,pane='all',verbose=False)
    #@-node:ekr.20061031131434.94:bindOpenWith
    #@+node:ekr.20061031131434.95:checkBindings
    def checkBindings (self):

        '''Print warnings if commands do not have any @shortcut entry.
        The entry may be `None`, of course.'''

        k = self ; c = k.c

        if not c.config.getBool('warn_about_missing_settings'): return

        names = c.commandsDict.keys() ; names.sort()

        for name in names:
            abbrev = k.abbreviationsDict.get(name)
            key = c.frame.menu.canonicalizeMenuName(abbrev or name)
            key = key.replace('&','')
            if not g.app.config.exists(c,key,'shortcut'):
                if abbrev:
                     g.trace('No shortcut for abbrev %s -> %s = %s' % (
                        name,abbrev,key))
                else:
                    g.trace('No shortcut for %s = %s' % (name,key))
    #@-node:ekr.20061031131434.95:checkBindings
    #@+node:ekr.20070218130238:dumpMasterBindingsDict
    def dumpMasterBindingsDict (self):

        k = self ; d = k.masterBindingsDict

        print ; print 'k.masterBindingsDict...' ; print
        keys = d.keys()
        keys.sort()
        for key in keys:
            print key, '-' * 40
            d2 = d.get(key)
            keys2 = d2.keys()
            keys2.sort()
            for key2 in keys2:
                b = d2.get(key2)
                print '%20s %s' % (key2,b.commandName)
    #@-node:ekr.20070218130238:dumpMasterBindingsDict
    #@+node:ekr.20061031131434.96:k.completeAllBindingsForWidget
    def completeAllBindingsForWidget (self,w):

        k = self ; d = k.bindingsDict

        # g.trace('w',w,d.has_key('Alt+Key-4'))

        for stroke in d.keys():
            k.makeMasterGuiBinding(stroke,w=w)
    #@-node:ekr.20061031131434.96:k.completeAllBindingsForWidget
    #@+node:ekr.20061031131434.97:k.completeAllBindings
    def completeAllBindings (self,w=None):

        '''New in 4.4b3: make an actual binding in *all* the standard places.

        The event will go to k.masterKeyHandler as always, so nothing really changes.
        except that k.masterKeyHandler will know the proper stroke.'''

        # g.trace(w)

        k = self
        for stroke in k.bindingsDict.keys():
            k.makeMasterGuiBinding(stroke,w=w)
    #@-node:ekr.20061031131434.97:k.completeAllBindings
    #@+node:ekr.20061031131434.98:k.makeAllBindings
    def makeAllBindings (self):

        k = self ; c = k.c

        # g.trace(c.fileName(),g.callers())

        k.bindingsDict = {}
        k.addModeCommands() 
        k.makeBindingsFromCommandsDict()
        k.initSpecialIvars()
        k.initAbbrev()
        c.frame.body.createBindings()
        c.frame.log.setTabBindings('Log')
        c.frame.tree.setBindings()
        c.frame.setMinibufferBindings()
        k.completeAllBindings()
        k.checkBindings()
    #@-node:ekr.20061031131434.98:k.makeAllBindings
    #@+node:ekr.20061031131434.99:k.initAbbrev
    def initAbbrev (self):

        k = self ; c = k.c ; d = c.config.getAbbrevDict()
        if d:
            for key in d.keys():
                commandName = d.get(key)
                if commandName.startswith('press-') and commandName.endswith('-button'):
                    pass # Must be done later in k.registerCommand.
                else:
                    self.initOneAbbrev(commandName,key)

    def initOneAbbrev (self,commandName,key):
        k = self ; c = k.c
        if c.commandsDict.get(key):
            g.trace('ignoring duplicate abbrev: %s',key)
        else:
            func = c.commandsDict.get(commandName)
            if func:
                # g.trace(key,commandName,func.__name__)
                c.commandsDict [key] = func
                # k.inverseCommandsDict[func.__name__] = key
            else:
                g.es_print('bad abbrev: %s: unknown command name: %s' %
                    (key,commandName),color='blue')
    #@-node:ekr.20061031131434.99:k.initAbbrev
    #@+node:ekr.20061031131434.100:addModeCommands (enterModeCallback)
    def addModeCommands (self):

        '''Add commands created by @mode settings to c.commandsDict and k.inverseCommandsDict.'''

        k = self ; c = k.c
        d = g.app.config.modeCommandsDict # Keys are command names: enter-x-mode.

        # Create the callback functions and update c.commandsDict and k.inverseCommandsDict.
        for key in d.keys():

            def enterModeCallback (event=None,name=key):
                k.enterNamedMode(event,name)

            c.commandsDict[key] = f = enterModeCallback
            k.inverseCommandsDict [f.__name__] = key
            # g.trace('leoCommands %24s = %s' % (f.__name__,key))
    #@-node:ekr.20061031131434.100:addModeCommands (enterModeCallback)
    #@+node:ekr.20061031131434.101:initSpecialIvars
    def initSpecialIvars (self):

        '''Set ivars for special keystrokes from previously-existing bindings.'''

        k = self ; c = k.c
        trace = False or c.config.getBool('trace_bindings_verbose')
        warn  = c.config.getBool('warn_about_missing_settings')

        for ivar,commandName in (
            ('fullCommandKey',  'full-command'),
            ('abortAllModesKey','keyboard-quit'),
            ('universalArgKey', 'universal-argument'),
        ):
            junk, bunchList = c.config.getShortcut(commandName)
            bunchList = bunchList or [] ; found = False
            for pane in ('text','all'):
                for bunch in bunchList:
                    if bunch.pane == pane:
                        stroke = k.strokeFromSetting(bunch.val)
                        if trace: g.trace(commandName,stroke)
                        setattr(k,ivar,stroke) ; found = True ;break
            if not found and warn:
                g.trace('no setting for %s' % commandName)
    #@-node:ekr.20061031131434.101:initSpecialIvars
    #@+node:ekr.20061031131434.102:makeBindingsFromCommandsDict
    def makeBindingsFromCommandsDict (self):

        '''Add bindings for all entries in c.commandDict.'''

        k = self ; c = k.c ; d = c.commandsDict
        keys = d.keys() ; keys.sort()

        for commandName in keys:
            command = d.get(commandName)
            key, bunchList = c.config.getShortcut(commandName)
            # if commandName == 'keyboard-quit': g.trace(key,bunchList)
            for bunch in bunchList:
                accel = bunch.val ; pane = bunch.pane
                # if pane.endswith('-mode'): g.trace('skipping',shortcut,commandName)
                if accel and not pane.endswith('-mode'):
                    shortcut = k.shortcutFromSetting(accel)
                    k.bindKey(pane,shortcut,command,commandName)

        # g.trace(g.listToString(k.bindingsDict.keys(),sort=True))
        # g.trace('Ctrl+g',k.bindingsDict.get('Ctrl+g'))
    #@-node:ekr.20061031131434.102:makeBindingsFromCommandsDict
    #@+node:ekr.20061031131434.103:k.makeMasterGuiBinding
    def makeMasterGuiBinding (self,stroke,w=None):

        '''Make a master gui binding for stroke in pane w, or in all the standard widgets.'''

        k = self ; c = k.c ; f = c.frame

        bindStroke = k.tkbindingFromStroke(stroke)
        # g.trace('stroke',stroke,'bindStroke',bindStroke)

        if w:
            widgets = [w]
        else:
            bodyCtrl = f.body and hasattr(f.body,'bodyCtrl') and f.body.bodyCtrl or None     
            if 1: # Canvas and bindingWidget bindings are now set in tree.setBindings.
                widgets = (c.miniBufferWidget,bodyCtrl)
            else:
                bindingWidget = f.tree and hasattr(f.tree,'bindingWidget') and f.tree.bindingWidget or None
                canvas = f.tree and hasattr(f.tree,'canvas') and f.tree.canvas   or None
                widgets = (c.miniBufferWidget,bodyCtrl,canvas,bindingWidget)

        # This is the only real key callback.
        def masterBindKeyCallback (event,k=k,stroke=stroke):
            # g.trace(stroke)
            return k.masterKeyHandler(event,stroke=stroke)

        for w in widgets:
            if not w: continue
            # Make the binding only if no binding for the stroke exists in the widget.
            aList = k.masterGuiBindingsDict.get(bindStroke,[])
            if w not in aList:
                aList.append(w)
                k.masterGuiBindingsDict [bindStroke] = aList
                try:
                    w.bind(bindStroke,masterBindKeyCallback)
                    # g.trace(stroke,bindStroke,g.app.gui.widget_name(w))
                except Exception:
                    if self.trace_bind_key_exceptions:
                        g.es_exception()
                    g.es_print('exception binding %s to %s' % (
                        bindStroke, c.widget_name(w)), color = 'blue')
                    if g.app.unitTesting: raise
    #@-node:ekr.20061031131434.103:k.makeMasterGuiBinding
    #@-node:ekr.20061031131434.88:Binding (keyHandler)
    #@+node:ekr.20061031131434.104:Dispatching (keyHandler)
    #@+node:ekr.20061031131434.105:masterCommand & helpers
    def masterCommand (self,event,func,stroke,commandName=None):

        '''This is the central dispatching method.
        All commands and keystrokes pass through here.'''

        k = self ; c = k.c ; gui = g.app.gui
        trace = False or k.traceMasterCommand
        traceGC = False
        if traceGC: g.printNewObjects('masterCom 1')

        c.setLog()
        c.startRedrawCount = c.frame.tree.redrawCount
        k.stroke = stroke # Set this global for general use.
        keysym = gui.eventKeysym(event)
        ch = gui.eventChar(event)
        w = gui.eventWidget(event)
        state = event and hasattr(event,'state') and event.state or 0
        k.func = func
        k.funcReturn = None # For unit testing.
        commandName = commandName or func and func.__name__ or '<no function>'
        #@    << define specialKeysyms >>
        #@+node:ekr.20061031131434.106:<< define specialKeysyms >>
        specialKeysyms = (
            'Alt_L','Alt_R',
            'Caps_Lock','Control_L','Control_R',
            'Num_Lock',
            'Shift_L','Shift_R',
        )
        #@nonl
        #@-node:ekr.20061031131434.106:<< define specialKeysyms >>
        #@nl
        special = keysym in specialKeysyms
        interesting = func is not None
        inserted = not special

        if trace: #  and interesting:
            g.trace(
                # 'stroke: ',stroke,'state:','%x' % state,'ch:',repr(ch),'keysym:',repr(keysym),
                'w:',w and c.widget_name(w),'func:',func and func.__name__
            )

        if inserted:
            # g.trace(stroke,keysym)
            #@        << add character to history >>
            #@+node:ekr.20061031131434.107:<< add character to history >>
            if stroke or len(ch) > 0:
                if len(keyHandlerClass.lossage) > 99:
                    keyHandlerClass.lossage.pop()

                # This looks like a memory leak, but isn't.
                keyHandlerClass.lossage.insert(0,(ch,stroke),)
            #@-node:ekr.20061031131434.107:<< add character to history >>
            #@nl

        # We *must not* interfere with the global state in the macro class.
        if c.macroCommands.recordingMacro:
            done = c.macroCommands.startKbdMacro(event)
            if done: return 'break'

        # g.trace(stroke,k.abortAllModesKey)

        if k.abortAllModesKey and stroke == k.abortAllModesKey: # 'Control-g'
            k.keyboardQuit(event)
            k.endCommand(event,commandName)
            return 'break'

        if special: # Don't pass these on.
            return 'break' 

        if 0: # *** This is now handled by k.masterKeyHandler.
            if k.inState():
                val = k.callStateFunction(event) # Calls end-command.
                if val != 'do-func': return 'break'
                g.trace('Executing key outside of mode')

        if k.regx.iter:
            try:
                k.regXKey = keysym
                k.regx.iter.next() # EKR: next() may throw StopIteration.
            except StopIteration:
                pass
            return 'break'

        if k.abbrevOn:
            expanded = c.abbrevCommands.expandAbbrev(event)
            if expanded: return 'break'

        if func: # Func is an argument.
            if commandName == 'propagate-key-event':
                # Do *nothing* with the event.
                return k.propagateKeyEvent(event)
            elif commandName.startswith('specialCallback'):
                # The callback function will call c.doCommand
                if trace: g.trace('calling specialCallback for',commandName)
                val = func(event)
                # k.simulateCommand uses k.funcReturn.
                k.funcReturn = k.funcReturn or val # For unit tests.
            else:
                # Call c.doCommand directly
                if trace: g.trace('calling command directly',commandName)
                c.doCommand(func,commandName,event=event)
            if c.exists:
                k.endCommand(event,commandName)
                c.frame.updateStatusLine()
            if traceGC: g.printNewObjects('masterCom 2')
            return 'break'
        elif k.inState():
            return 'break' #Ignore unbound keys in a state.
        else:
            if traceGC: g.printNewObjects('masterCom 3')
            val = k.handleDefaultChar(event,stroke)
            if c.exists:
                c.frame.updateStatusLine()
            if traceGC: g.printNewObjects('masterCom 4')
            return val
    #@nonl
    #@+node:ekr.20061031131434.108:callStateFunction
    def callStateFunction (self,event):

        k = self ; val = None

        # g.trace(k.state.kind)

        if k.state.kind:
            if k.state.handler:
                val = k.state.handler(event)
                if val != 'continue':
                    k.endCommand(event,k.commandName)
            else:
                g.es_print('no state function for %s' % (k.state.kind),color='red')

        return val
    #@-node:ekr.20061031131434.108:callStateFunction
    #@+node:ekr.20061031131434.109:callKeystrokeFunction (not used)
    def callKeystrokeFunction (self,event):

        '''Handle a quick keystroke function.
        Return the function or None.'''

        k = self
        numberOfArgs, func = k.keystrokeFunctionDict [k.stroke]

        if func:
            func(event)
            commandName = k.inverseCommandsDict.get(func) # Get the emacs command name.
            k.endCommand(event,commandName)

        return func
    #@-node:ekr.20061031131434.109:callKeystrokeFunction (not used)
    #@+node:ekr.20061031131434.110:handleDefaultChar
    def handleDefaultChar(self,event,stroke):

        k = self ; c = k.c
        w = event and event.widget
        name = c.widget_name(w)

        if name.startswith('body'):
            action = k.unboundKeyAction
            if action in ('insert','overwrite'):
                c.editCommands.selfInsertCommand(event,action=action)
            else: pass # Ignore the key.
            return 'break'
        elif name.startswith('head'):
            c.frame.tree.onHeadlineKey(event)
            return 'break'
        elif name.startswith('canvas'):
            if not stroke: # Not exactly right, but it seems to be good enough.
                c.onCanvasKey(event) # New in Leo 4.4.2
            return 'break'
        else:
            # Let tkinter handle the event.
            # ch = event and event.char ; g.trace('to tk:',name,repr(ch))
            return None
    #@-node:ekr.20061031131434.110:handleDefaultChar
    #@-node:ekr.20061031131434.105:masterCommand & helpers
    #@+node:ekr.20061031131434.111:fullCommand (alt-x) & helper
    def fullCommand (self,event,specialStroke=None,specialFunc=None,help=False,helpHandler=None):

        '''Handle 'full-command' (alt-x) mode.'''

        k = self ; c = k.c ; gui = g.app.gui
        state = k.getState('full-command')
        helpPrompt = 'Help for command: '
        keysym = gui.eventKeysym(event) ; ch = gui.eventChar(event)
        trace = False or c.config.getBool('trace_modes')
        if trace: g.trace('state',state,keysym)
        if state == 0:
            k.mb_event = event # Save the full event for later.
            k.setState('full-command',1,handler=k.fullCommand)
            prompt = g.choose(help,helpPrompt,k.altX_prompt)
            k.setLabelBlue('%s' % (prompt),protect=True)
            # Init mb_ ivars. This prevents problems with an initial backspace.
            k.mb_prompt = k.mb_tabListPrefix = k.mb_prefix = prompt
            k.mb_tabList = [] ; k.mb_tabListIndex = -1
            k.mb_help = help
            k.mb_helpHandler = helpHandler
            c.minibufferWantsFocus()
        elif keysym == 'Escape':
            k.keyboardQuit(event)
        elif keysym == 'Return':
            c.frame.log.deleteTab('Completion')
            if k.mb_help:
                s = k.getLabel()
                commandName = s[len(helpPrompt):].strip()
                k.clearState()
                k.resetLabel()
                if k.mb_helpHandler: k.mb_helpHandler(commandName)
            else:
                k.callAltXFunction(k.mb_event)
        elif keysym == 'Tab':
            k.doTabCompletion(c.commandsDict.keys())
            c.minibufferWantsFocus()
        elif keysym == 'BackSpace':
            k.doBackSpace(c.commandsDict.keys())
            c.minibufferWantsFocus()
        elif k.ignore_unbound_non_ascii_keys and len(ch) > 1:
            # g.trace('non-ascii')
            if specialStroke:
                g.trace(specialStroke)
                specialFunc()
            c.minibufferWantsFocus()
        else:
            # Clear the list, any other character besides tab indicates that a new prefix is in effect.
            k.mb_tabList = []
            k.updateLabel(event)
            k.mb_tabListPrefix = k.getLabel()
            c.minibufferWantsFocus()
            # g.trace('new prefix',k.mb_tabListPrefix)

        return 'break'
    #@+node:ekr.20061031131434.112:callAltXFunction
    def callAltXFunction (self,event):

        k = self ; c = k.c ; s = k.getLabel()
        k.mb_tabList = []
        commandName = s[len(k.mb_prefix):].strip()
        func = c.commandsDict.get(commandName)
        k.newMinibufferWidget = None

        # print 'callAltXFunc',func

        if func:
            # These must be done *after* getting the command.
            k.clearState()
            k.resetLabel()
            if commandName != 'repeat-complex-command':
                k.mb_history.insert(0,commandName)
            c.widgetWantsFocusNow(event.widget) # Important, so cut-text works, e.g.
            func(event)
            k.endCommand(event,commandName)
        else:
            if 1: # Useful.
                k.doTabCompletion(c.commandsDict.keys())
            else: # Annoying.
                k.keyboardQuit(event)
                k.setLabel('Command does not exist: %s' % commandName)
                c.bodyWantsFocus()
    #@-node:ekr.20061031131434.112:callAltXFunction
    #@-node:ekr.20061031131434.111:fullCommand (alt-x) & helper
    #@+node:ekr.20061031131434.113:endCommand
    def endCommand (self,event,commandName):

        '''Make sure Leo updates the widget following a command.

        Never changes the minibuffer label: individual commands must do that.
        '''

        # pychecker complains about initAllEditCommanders.

        k = self ; c = k.c
        # The command may have closed the window.
        if g.app.quitting or not c.exists: return

        # Set the best possible undoType: prefer explicit commandName to k.commandName.
        commandName = commandName or k.commandName or ''
        k.commandName = k.commandName or commandName or ''
        if commandName:
            bodyCtrl = c.frame.body.bodyCtrl
            if not k.inState():
                __pychecker__ = '--no-classattr --no-objattrs'
                    # initAllEditCommanders *does* exist.
                k.commandName = None
                leoEditCommands.initAllEditCommanders(c)
                try:
                    bodyCtrl.tag_delete('color')
                    bodyCtrl.tag_delete('color1')
                except Exception:
                    pass
            if 0: # Do *not* call this by default.  It interferes with undo.
                c.frame.body.onBodyChanged(undoType='Typing')
            if k.newMinibufferWidget:
                c.widgetWantsFocusNow(k.newMinibufferWidget)
                # print 'endCommand', g.app.gui.widget_name(k.newMinibufferWidget),g.callers()
                k.newMinibufferWidget = None
    #@-node:ekr.20061031131434.113:endCommand
    #@-node:ekr.20061031131434.104:Dispatching (keyHandler)
    #@+node:ekr.20061031131434.114:Externally visible commands
    #@+node:ekr.20061031131434.115:digitArgument & universalArgument
    def universalArgument (self,event):

        '''Prompt for a universal argument.'''
        k = self
        k.setLabelBlue('Universal Argument: ',protect=True)
        k.universalDispatcher(event)

    def digitArgument (self,event):

        '''Prompt for a digit argument.'''
        k = self
        k.setLabelBlue('Digit Argument: ',protect=True)
        k.universalDispatcher(event)
    #@-node:ekr.20061031131434.115:digitArgument & universalArgument
    #@+node:ekr.20061031131434.116:k.show/hide/toggleMinibuffer
    def hideMinibuffer (self,event):
        '''Hide the minibuffer.'''
        k = self ; c = k.c
        c.frame.hideMinibuffer()
        g.es('Minibuffer hidden',color='red')
        for commandName in ('show-mini-buffer','toggle-mini-buffer'):
            shortcut = k.getShortcutForCommandName(commandName)
            if shortcut:
                g.es('%s is bound to: %s' % (commandName,shortcut))

    def showMinibuffer (self,event):
        '''Show the minibuffer.'''
        k = self ; c = k.c
        c.frame.showMinibuffer()

    def toggleMinibuffer (self,event):
        '''Show or hide the minibuffer.'''
        k = self ; c = k.c
        if c.frame.minibufferVisible:
            k.hideMinibuffer(event)
        else:
            k.showMinibuffer(event)
    #@-node:ekr.20061031131434.116:k.show/hide/toggleMinibuffer
    #@+node:ekr.20070613133500:k.menuCommandKey
    def menuCommandKey (self,event=None):

        # This method must exist, but it never gets called.
        pass 
    #@-node:ekr.20070613133500:k.menuCommandKey
    #@+node:ekr.20070613190936:k.propagateKeyEvent
    def propagateKeyEvent (self,event):

        self.oops() # Should be overridden.
    #@nonl
    #@-node:ekr.20070613190936:k.propagateKeyEvent
    #@+node:ekr.20061031131434.117:negativeArgument (redo?)
    def negativeArgument (self,event):

        '''Prompt for a negative digit argument.'''

        k = self ; state = k.getState('neg-arg')

        if state == 0:
            k.setLabelBlue('Negative Argument: ',protect=True)
            k.setState('neg-arg',1,k.negativeArgument)
        else:
            k.clearState()
            k.resetLabel()
            func = k.negArgFunctions.get(k.stroke)
            if func:
                func(event)

        return 'break'
    #@-node:ekr.20061031131434.117:negativeArgument (redo?)
    #@+node:ekr.20061031131434.118:numberCommand
    def numberCommand (self,event,stroke,number):

        k = self ; k.stroke = stroke ; w = event.widget
        k.universalDispatcher(event)
        g.app.gui.event_generate(w,'<Key>',keysym=number)
        return 'break'

    def numberCommand0 (self,event):
        '''Execute command number 0.'''
        return self.numberCommand (event,None,0)

    def numberCommand1 (self,event):
        '''Execute command number 1.'''
        return self.numberCommand (event,None,1)

    def numberCommand2 (self,event):
        '''Execute command number 2.'''
        return self.numberCommand (event,None,2)

    def numberCommand3 (self,event):
        '''Execute command number 3.'''
        return self.numberCommand (event,None,3)

    def numberCommand4 (self,event):
        '''Execute command number 4.'''
        return self.numberCommand (event,None,4)

    def numberCommand5 (self,event):
        '''Execute command number 5.'''
        return self.numberCommand (event,None,5)

    def numberCommand6 (self,event):
        '''Execute command number 6.'''
        return self.numberCommand (event,None,6)

    def numberCommand7 (self,event):
        '''Execute command number 7.'''
        return self.numberCommand (event,None,7)

    def numberCommand8 (self,event):
        '''Execute command number 8.'''
        return self.numberCommand (event,None,8)

    def numberCommand9 (self,event):
        '''Execute command number 9.'''
        return self.numberCommand (event,None,9)
    #@-node:ekr.20061031131434.118:numberCommand
    #@+node:ekr.20061031131434.119:printBindings & helper
    def printBindings (self,event=None):

        '''Print all the bindings presently in effect.'''

        k = self ; c = k.c
        d = k.bindingsDict ; tabName = 'Bindings'
        keys = d.keys() ; keys.sort()
        c.frame.log.clearTab(tabName)
        data = [] ; n1 = 4 ; n2 = 20
        if not keys: return g.es('no bindings')
        for key in keys:
            bunchList = d.get(key,[])
            for b in bunchList:
                pane = g.choose(b.pane=='all','',' %s:' % (b.pane))
                s1 = pane
                s2 = k.prettyPrintKey(key,brief=True)
                s3 = b.commandName
                n1 = max(n1,len(s1))
                n2 = max(n2,len(s2))
                data.append((s1,s2,s3),)

        # Print keys by type:
        sep = '-' * n1
        for prefix in (
            'Alt+Ctrl+Shift', 'Alt+Shift', 'Alt+Ctrl', 'Alt+Key','Alt',
            'Ctrl+Shift', 'Ctrl', 'Shift',
        ):
            data2 = []
            for item in data:
                s1,s2,s3 = item
                if s2.startswith(prefix):
                    data2.append(item)
            g.es('%s %s' % (sep, prefix),tabName=tabName)
            self.printBindingsHelper(data2,n1,n2,prefix=prefix)
            # Remove all the items in data2 from data.
            # This must be done outside the iterator on data.
            for item in data2:
                data.remove(item)
        # Print all plain bindings.
        g.es('%s %s' % (sep, 'Plain Keys',),tabName=tabName)
        self.printBindingsHelper(data,n1,n2,prefix=None)
        state = k.unboundKeyAction 
        k.showStateAndMode()
    #@+node:ekr.20061031131434.120:printBindingsHelper
    def printBindingsHelper (self,data,n1,n2,prefix):

        n = prefix and len(prefix)+1 or 0 # Add 1 for the '+' after the prefix.

        data1 = [z for z in data if z and z[1] and len(z[1][n:]) == 1]
            # The list of all items with only one character following the prefix.
        data2 = [z for z in data if z and z[1] and len(z[1][n:]) >  1]
            # The list of all other items.

        # This isn't perfect in variable-width fonts.
        for data in (data1,data2):
            data.sort(lambda x,y: cmp(x[1],y[1]))
            for s1,s2,s3 in data:
                g.es('%*s %*s %s' % (-n1,s1,-(min(12,n2)),s2,s3),tabName='Bindings')
    #@-node:ekr.20061031131434.120:printBindingsHelper
    #@-node:ekr.20061031131434.119:printBindings & helper
    #@+node:ekr.20061031131434.121:printCommands
    def printCommands (self,event=None):

        '''Print all the known commands and their bindings, if any.'''

        k = self ; c = k.c ; tabName = 'Commands'

        c.frame.log.clearTab(tabName)

        inverseBindingDict = k.computeInverseBindingDict()
        commandNames = c.commandsDict.keys() ; commandNames.sort()

        data = [] ; n1 = 4 ; n2 = 20
        for commandName in commandNames:
            dataList = inverseBindingDict.get(commandName,[('',''),])
            for z in dataList:
                pane, key = z
                s1 = pane
                s2 = k.prettyPrintKey(key,brief=True)
                s3 = commandName
                n1 = max(n1,len(s1))
                n2 = max(n2,len(s2))
                data.append((s1,s2,s3),)

        # This isn't perfect in variable-width fonts.
        for s1,s2,s3 in data:
            g.es('%*s %*s %s' % (-n1,s1,-(min(12,n2)),s2,s3),tabName=tabName)
    #@-node:ekr.20061031131434.121:printCommands
    #@+node:ekr.20061031131434.122:repeatComplexCommand & helper
    def repeatComplexCommand (self,event):

        '''Repeat the previously executed minibuffer command.'''
        k = self
        if k.mb_history:
            k.setState('last-full-command',1,handler=k.repeatComplexCommandHelper)
            k.setLabelBlue("Redo: %s" % str(k.mb_history[0]))
        else:
            g.es('No previous command',color='blue')
        return 'break'

    def repeatComplexCommandHelper (self,event):

        k = self ; c = k.c ; gui = g.app.gui

        keysym = gui.eventKeysym(event)
        # g.trace('state',k.state.kind,'event',repr(event),g.callers())
        if keysym == 'Return' and k.mb_history:
        # if k.mb_history:
            last = k.mb_history [0]
            k.resetLabel()
            k.clearState() # Bug fix.
            c.commandsDict [last](event)
            return 'break'
        else:
            g.trace('oops')
            return k.keyboardQuit(event)
    #@-node:ekr.20061031131434.122:repeatComplexCommand & helper
    #@+node:ekr.20061031131434.123:set-xxx-State
    def setCommandState (self,event):
        '''Enter the 'command' editing state.'''
        # g.trace(g.callers())
        k = self
        k.setInputState('command',showState=True)

    def setInsertState (self,event):
        '''Enter the 'insert' editing state.'''
        # g.trace(g.callers())
        k = self
        k.setInputState('insert',showState=True)

    def setOverwriteState (self,event):
        '''Enter the 'overwrite' editing state.'''
        # g.trace(g.callers())
        k = self
        k.setInputState('overwrite',showState=True)
    #@-node:ekr.20061031131434.123:set-xxx-State
    #@+node:ekr.20061031131434.124:toggle-input-state
    def toggleInputState (self,event=None):

        '''The toggle-input-state command.'''

        k = self ; c = k.c
        default = c.config.getString('top_level_unbound_key_action') or 'insert'
        state = k.unboundKeyAction

        if default == 'insert':
            state = g.choose(state=='insert','command','insert')
        elif default == 'overwrite':
            state = g.choose(state=='overwrite','command','overwrite')
        else:
            state = g.choose(state=='command','insert','command') # prefer insert to overwrite.

        k.setInputState(state)
    #@-node:ekr.20061031131434.124:toggle-input-state
    #@-node:ekr.20061031131434.114:Externally visible commands
    #@+node:ekr.20061031131434.125:Externally visible helpers
    #@+node:ekr.20061031131434.126:manufactureKeyPressForCommandName
    def manufactureKeyPressForCommandName (self,w,commandName):

        '''Implement a command by passing a keypress to Tkinter.'''

        k = self ; c = k.c

        stroke = k.getShortcutForCommandName(commandName)

        if stroke and w:
            # g.trace(stroke)
            g.app.gui.event_generate(w,stroke)
        else:
            g.trace('no shortcut for %s' % (commandName),color='red')
    #@-node:ekr.20061031131434.126:manufactureKeyPressForCommandName
    #@+node:ekr.20061031131434.127:simulateCommand
    def simulateCommand (self,commandName):

        k = self ; c = k.c

        func = c.commandsDict.get(commandName)

        if func:
            # g.trace(commandName,func.__name__)
            stroke = None
            if commandName.startswith('specialCallback'):
                event = None # A legacy function.
            else: # Create a dummy event as a signal.
                event = g.bunch(c=c,keysym='',char='',widget=None)
            k.masterCommand(event,func,stroke)
            return k.funcReturn
        else:
            g.trace('no command for %s' % (commandName),color='red')
            if g.app.unitTesting:
                raise AttributeError
            else:
                return None
    #@-node:ekr.20061031131434.127:simulateCommand
    #@+node:ekr.20061031131434.128:getArg
    def getArg (self,event,
        returnKind=None,returnState=None,handler=None,
        prefix=None,tabList=[],completion=True,oneCharacter=False,
        stroke=None, # New in 4.4.1.
        useMinibuffer=True # New in 4.4.1
    ):

        '''Accumulate an argument until the user hits return (or control-g).
        Enter the given return state when done.
        The prefix does not form the arg.  The prefix defaults to the k.getLabel().
        '''

        k = self ; c = k.c ; gui  = g.app.gui
        state = k.getState('getArg')
        keysym = gui.eventKeysym(event)
        trace = False or c.config.getBool('trace_modes') and not g.app.unitTesting
        if trace: g.trace(
            'state',state,'keysym',keysym,'stroke',stroke,'escapes',k.getArgEscapes,
            'completion', state==0 and completion or state!=0 and k.arg_completion)
        if state == 0:
            k.arg = ''
            #@        << init altX vars >>
            #@+node:ekr.20061031131434.129:<< init altX vars >>
            k.argTabList = tabList and tabList[:] or []
            k.arg_completion = completion
            # g.trace('completion',completion,'tabList',tabList)

            k.mb_prefix = prefix or k.getLabel()
            k.mb_prompt = prefix or ''
            k.mb_tabList = []

            # Clear the list: any non-tab indicates that a new prefix is in effect.
            k.mb_tabListPrefix = k.getLabel()
            k.oneCharacterArg = oneCharacter
            #@-node:ekr.20061031131434.129:<< init altX vars >>
            #@nl
            # Set the states.
            bodyCtrl = c.frame.body.bodyCtrl
            c.widgetWantsFocus(bodyCtrl)
            k.afterGetArgState=returnKind,returnState,handler
            k.setState('getArg',1,k.getArg)
            k.afterArgWidget = event and event.widget or c.frame.body.bodyCtrl
            if useMinibuffer and k.useTextWidget: c.minibufferWantsFocusNow()
        elif keysym == 'Escape':
            k.keyboardQuit(event)
        elif keysym == 'Return' or k.oneCharacterArg or stroke in k.getArgEscapes:
            if stroke in k.getArgEscapes: k.getArgEscape = stroke
            if k.oneCharacterArg:
                k.arg = event.char
            else:
                k.arg = k.getLabel(ignorePrompt=True)
            kind,n,handler = k.afterGetArgState
            if kind: k.setState(kind,n,handler)
            c.frame.log.deleteTab('Completion')
            trace and g.trace('kind',kind,'n',n,'handler',handler and handler.__name__)
            if handler: handler(event)
        elif keysym == 'Tab':
            k.doTabCompletion(k.argTabList,k.arg_completion)
        elif keysym == 'BackSpace':
            k.doBackSpace(k.argTabList,k.arg_completion)
            c.minibufferWantsFocus()
        else:
            # Clear the list, any other character besides tab indicates that a new prefix is in effect.
            k.mb_tabList = []
            k.updateLabel(event)
            k.mb_tabListPrefix = k.getLabel()
        return 'break'
    #@-node:ekr.20061031131434.128:getArg
    #@+node:ekr.20061031131434.130:keyboardQuit
    def keyboardQuit (self,event,hideTabs=True,setDefaultUnboundKeyAction=True):

        '''This method clears the state and the minibuffer label.

        k.endCommand handles all other end-of-command chores.'''

        k = self ; c = k.c

        if g.app.quitting:
            return

        if hideTabs:
            k.autoCompleter.exit()
            c.frame.log.deleteTab('Mode')
            c.frame.log.hideTab('Completion')

        # Completely clear the mode.
        if k.inputModeName:
            k.endMode(event)

        # Complete clear the state.
        k.state.kind = None
        k.state.n = None

        k.clearState()
        k.resetLabel()

        if setDefaultUnboundKeyAction: k.setDefaultUnboundKeyAction()
        k.showStateAndMode()
        c.endEditing()
        c.bodyWantsFocus()
    #@-node:ekr.20061031131434.130:keyboardQuit
    #@+node:ekr.20061031131434.131:k.registerCommand & test
    def registerCommand (self,commandName,shortcut,func,pane='all',verbose=False):

        '''Make the function available as a minibuffer command,
        and optionally attempt to bind a shortcut.

        You can wrap any method in a callback function, so the
        restriction to functions is not significant.'''

        k = self ; c = k.c
        f = c.commandsDict.get(commandName)
        verbose = (False or verbose) and not g.app.unitTesting
        if f and f.__name__ != 'dummyCallback' and verbose:
            g.es_print('Redefining %s' % (commandName), color='red')

        c.commandsDict [commandName] = func
        k.inverseCommandsDict [func.__name__] = commandName
        # g.trace('leoCommands %24s = %s' % (func.__name__,commandName))

        if shortcut:
            stroke = k.shortcutFromSetting(shortcut)
        elif commandName.lower() == 'shortcut': # Causes problems.
            stroke = None
        else:
            # Try to get a shortcut from leoSettings.leo.
            junk,bunchList = c.config.getShortcut(commandName)
            for bunch in bunchList:
                accel2 = bunch.val ; pane2 = bunch.pane
                if accel2 and not pane2.endswith('-mode'):
                    shortcut2 = accel2
                    stroke = k.shortcutFromSetting(shortcut2)
                    if stroke: break
            else: stroke = None

        if stroke:
            # g.trace('stroke',stroke,'pane',pane,commandName,g.callers())
            ok = k.bindKey (pane,stroke,func,commandName) # Must be a stroke.
            k.makeMasterGuiBinding(stroke) # Must be a stroke.
            if verbose and ok and not g.app.silentMode:
                g.es_print('@command: %s = %s' % (
                    commandName,k.prettyPrintKey(stroke)),color='blue')
                if 0:
                    d = k.masterBindingsDict.get('button',{})
                    g.print_dict(d)
            c.frame.tree.setBindings()
        elif verbose and not g.app.silentMode:
            g.es_print('@command: %s' % (commandName),color='blue')

        # Fixup any previous abbreviation to press-x-button commands.
        if commandName.startswith('press-') and commandName.endswith('-button'):
            d = c.config.getAbbrevDict()
                # Keys are full command names, values are abbreviations.
            if commandName in d.values():
                for key in d.keys():
                    if d.get(key) == commandName:
                        c.commandsDict [key] = c.commandsDict.get(commandName)
                        break
    #@+node:ekr.20070627082044.831:@test k.registerCommand
    if g.unitTesting:
        __pychecker__ = '--no-reimport'
        import leoTest
        u = leoTest.testUtils(c)
        k = c.k ; p = c.currentPosition() ; w = c.edit_widget(p)
        commandName = 'test-registerCommand'

        def callback (event=None,c=c): # Must have an event param to pass later unit test.
            g.app.unitTestDict[commandName] = True

        # Test 1
        g.app.unitTestDict[commandName] = False
        k.registerCommand(commandName,'Alt-Ctrl-Shift-z',callback,pane='all',verbose=True)
        k.simulateCommand(commandName)
        assert g.app.unitTestDict.get(commandName)

        if 0: # Test 2
            g.app.unitTestDict[commandName] = False
            k.manufactureKeyPressForCommandName(w,commandName)
            assert g.app.unitTestDict.get(commandName)
    #@nonl
    #@-node:ekr.20070627082044.831:@test k.registerCommand
    #@-node:ekr.20061031131434.131:k.registerCommand & test
    #@-node:ekr.20061031131434.125:Externally visible helpers
    #@+node:ekr.20061031131434.145:Master event handlers (keyHandler)
    #@+node:ekr.20061031131434.146:masterKeyHandler
    master_key_count = 0

    def masterKeyHandler (self,event,stroke=None):

        '''This is the handler for almost all key bindings.'''

        # g.trace('event.keysym_num',event.keysym_num,event,dir(event))

        #@    << define vars >>
        #@+node:ekr.20061031131434.147:<< define vars >>
        k = self ; c = k.c ; gui = g.app.gui

        if event: event = gui.leoKeyEvent(event,c)

        w = event.widget
        char = event.char
        keysym = event.keysym
        if stroke and not keysym:
            event.keysym = keysym = stroke

        w_name = c.widget_name(w)
        state = k.state.kind

        special_keys = (
            'Alt_L','Alt_R',
            'Caps_Lock','Control_L','Control_R',
            'Num_Lock',
            'Shift_L','Shift_R',
            'Win_L','Win_R',
        )

        self.master_key_count += 1
        #@nonl
        #@-node:ekr.20061031131434.147:<< define vars >>
        #@nl
        if keysym in special_keys: return None

        trace = (False or self.trace_masterKeyHandler) and not g.app.unitTesting
        traceGC = (False or self.trace_masterKeyHandlerGC) and not g.app.unitTesting
        if traceGC: g.printNewObjects('masterKey 1')
        if trace:
            g.trace('stroke:',repr(stroke),'keysym:',repr(event.keysym),'ch:',repr(event.char),
                'state.kind:',k.state.kind,'\n',g.callers())
            # if (self.master_key_count % 100) == 0: g.printGcSummary()

        # Handle keyboard-quit first.
        if k.abortAllModesKey and stroke == k.abortAllModesKey:
            # g.trace('special case')
            return k.masterCommand(event,k.keyboardQuit,stroke,'keyboard-quit')

        if k.inState():
            # This will return unless k.autoCompleterStateHandler
            # (called from k.callStateFunction) returns 'do-standard-keys'
            #@        << handle mode bindings >>
            #@+node:ekr.20061031131434.149:<< handle mode bindings >>
            # First, honor minibuffer bindings for all except user modes.
            if state in ('getArg','getFileName','full-command','auto-complete'):
                if k.handleMiniBindings(event,state,stroke):
                    return 'break'

            # Second, honor general modes.
            if state == 'getArg':
                return k.getArg(event,stroke=stroke)
            elif state == 'getFileName':
                return k.getFileName(event)
            elif state in ('full-command','auto-complete'):
                # Do the default state action.
                if trace: g.trace('calling state function')
                val = k.callStateFunction(event) # Calls end-command.
                if val != 'do-standard-keys': return 'break'

            # Third, pass keys to user modes.
            else:
                d =  k.masterBindingsDict.get(state)
                if d:
                    b = d.get(stroke)
                    if b:
                        if trace: g.trace('calling generalModeHandler')
                        k.generalModeHandler (event,
                            commandName=b.commandName,func=b.func,
                            modeName=state,nextMode=b.nextMode)
                        return 'break'
                    else:
                        ok = k.handleMiniBindings(event,state,stroke)
                        if ok:
                            return 'break'
                        elif stroke and len(stroke) == 1:
                            # if trace: g.trace('calling modeHelp')
                            k.modeHelp(event)
                            return 'break'
                        else:
                            # End the mode and fall through to the pane bindings!
                            k.endMode(event)
                else:
                    # New in 4.4b4.
                    handler = k.getStateHandler()
                    if handler:
                        handler(event)
                    else:
                        g.trace('No state handler for %s' % state)
                    return 'break'
            #@-node:ekr.20061031131434.149:<< handle mode bindings >>
            #@nl

        if traceGC: g.printNewObjects('masterKey 2')

        #@    << handle per-pane bindings >>
        #@+node:ekr.20061031131434.150:<< handle per-pane bindings >>
        keyStatesTuple = ('command','insert','overwrite')
        isPlain =  k.isPlainKey(stroke)

        # g.trace('w_name',w_name,'w',w,'isTextWidget(w)',g.app.gui.isTextWidget(w))
        # g.trace('button',k.masterBindingsDict.get('button'))

        for key,name in (
            # Order here is similar to bindtags order.
            ('command',None),
            ('insert',None),
            ('overwrite',None),
            ('button',None),
            ('body','body'),
            ('text','head'), # Important: text bindings in head before tree bindings.
            ('tree','head'),
            ('tree','canvas'),
            ('log', 'log'),
            ('text','log'),
            ('text',None), ('all',None),
        ):
            if (
                key in keyStatesTuple and isPlain and k.unboundKeyAction == key or
                name and w_name.startswith(name) or
                key in ('text','all') and g.app.gui.isTextWidget(w) or
                key in ('button','all')
            ):
                d = k.masterBindingsDict.get(key,{})
                # g.trace('key',key,'name',name,'stroke',stroke,'stroke in d.keys',stroke in d.keys())
                if d:
                    b = d.get(stroke)
                    if b:
                        if trace: g.trace('%s found %s = %s' % (key,repr(b.stroke),b.commandName))
                        if traceGC: g.printNewObjects('masterKey 3')
                        return k.masterCommand(event,b.func,b.stroke,b.commandName)
        #@-node:ekr.20061031131434.150:<< handle per-pane bindings >>
        #@nl
        #@    << handle keys without bindings >>
        #@+node:ekr.20061031131434.151:<< handle keys without bindings >>
        if traceGC: g.printNewObjects('masterKey 5')

        modesTuple = ('insert','overwrite')

        if stroke and k.isPlainKey(stroke) and k.unboundKeyAction in modesTuple:
            # insert/overwrite normal character.  <Return> is *not* a normal character.
            if trace: g.trace('plain key in insert mode',repr(stroke))
            if traceGC: g.printNewObjects('masterKey 4')
            return k.masterCommand(event,func=None,stroke=stroke,commandName=None)

        elif k.ignore_unbound_non_ascii_keys and len(char) > 1:
            # (stroke.find('Alt+') > -1 or stroke.find('Ctrl+') > -1)):
            if trace: g.trace('ignoring unbound non-ascii key')
            return 'break'

        elif keysym.find('Escape') != -1:
            # Never insert escape characters.
            return 'break'

        else:
            if trace: g.trace(repr(stroke),'no func')
            if traceGC: g.printNewObjects('masterKey 6')
            return k.masterCommand(event,func=None,stroke=stroke,commandName=None)
        #@-node:ekr.20061031131434.151:<< handle keys without bindings >>
        #@nl
    #@+node:ekr.20061031131434.152:handleMiniBindings
    def handleMiniBindings (self,event,state,stroke):

        k = self ; c = k.c
        trace = False or self.trace_masterKeyHandler and not g.app.unitTesting

        if not state.startswith('auto-'):
            d = k.masterBindingsDict.get('mini')
            if d:
                b = d.get(stroke)
                if b:
                    if trace: g.trace(repr(stroke),'mini binding',b.commandName)
                    # Pass this on for macro recording.
                    k.masterCommand(event,b.func,stroke,b.commandName)
                    if not k.silentMode:
                        c.minibufferWantsFocus()
                    return True

        return False
    #@-node:ekr.20061031131434.152:handleMiniBindings
    #@-node:ekr.20061031131434.146:masterKeyHandler
    #@+node:ekr.20061031131434.153:masterClickHandler
    def masterClickHandler (self,event,func=None):

        k = self ; c = k.c ; gui = g.app.gui
        if not event: return
        w = event.widget ; wname = c.widget_name(w)
        trace = not g.app.unitTesting and (False or k.trace_masterClickHandler)

        if trace: g.trace(wname,func and func.__name__)
        # c.frame.body.colorizer.interrupt() # New in 4.4.1

        # A click outside the minibuffer terminates any state.
        if k.inState() and c.useTextMinibuffer and w != c.frame.miniBufferWidget:
            if not c.widget_name(w).startswith('log'):
                k.keyboardQuit(event,hideTabs=False)
                # k.endMode(event) # Less drastic than keyboard-quit.
                w and c.widgetWantsFocusNow(w)
                if trace: g.trace('inState: break')
                return 'break'

        # Update the selection point immediately for updateStatusLine.
        k.previousSelection = None
        if wname.startswith('body'):
            c.frame.body.onClick(event) # New in Leo 4.4.2.
        elif wname.startswith('mini'):
            x,y = gui.eventXY(event)
            x = w.xyToPythonIndex(x,y)
            i,j = k.getEditableTextRange()
            if i <= x <= j:
                w.setSelectionRange(x,x,insert=x)
            else:
                if trace: g.trace('2: break')
                return 'break'
        if event and func:
            if trace: g.trace(func.__name__)
            val = func(event) # Don't even *think* of overriding this.
            c.masterFocusHandler()
            if trace: g.trace('val:',val,g.callers())
            return val
        else:
            # All tree callbacks have a func, so we can't be in the tree.
            # g.trace('*'*20,'auto-deactivate tree: %s' % wname)
            c.frame.tree.OnDeactivate()
            c.widgetWantsFocusNow(w)
            if trace: g.trace('end: None')
            return None

    masterClick3Handler = masterClickHandler
    masterDoubleClick3Handler = masterClickHandler
    #@-node:ekr.20061031131434.153:masterClickHandler
    #@+node:ekr.20061031131434.154:masterDoubleClickHandler
    def masterDoubleClickHandler (self,event,func=None):

        k = self ; c = k.c ; w = event and event.widget

        if c.config.getBool('trace_masterClickHandler'):
            g.trace(c.widget_name(w),func and func.__name__)

        if event and func:
            # Don't event *think* of overriding this.
            return func(event)
        else:
            gui = g.app.gui
            x,y = gui.eventXY(event)
            i = w.xyToPythonIndex(x,y)
            s = w.getAllText()
            start,end = g.getWord(s,i)
            w.setSelectionRange(start,end)
            return 'break'
    #@-node:ekr.20061031131434.154:masterDoubleClickHandler
    #@+node:ekr.20061031131434.155:masterMenuHandler
    def masterMenuHandler (self,stroke,func,commandName):

        k = self ; c = k.c ; w = c.frame.getFocus()

        # g.trace('stroke',stroke,'func',func and func.__name__,commandName,g.callers())

        # Create a minimal event for commands that require them.
        event = g.Bunch(c=c,char='',keysym='',widget=w)

        if stroke:
            return k.masterKeyHandler(event,stroke=stroke)
        else:
            return k.masterCommand(event,func,stroke,commandName)
    #@-node:ekr.20061031131434.155:masterMenuHandler
    #@-node:ekr.20061031131434.145:Master event handlers (keyHandler)
    #@+node:ekr.20061031170011.3:Minibuffer (keyHandler)
    # These may be overridden, but this code is now gui-independent.
    #@nonl
    #@+node:ekr.20061031131434.135:k.minibufferWantsFocus/Now
    def minibufferWantsFocus(self):

        c = self.c
        if self.useTextWidget:
            c.widgetWantsFocus(c.miniBufferWidget)
        else:
            c.bodyWantsFocus()

    def minibufferWantsFocusNow(self):

        c = self.c
        if self.useTextWidget:
            c.widgetWantsFocusNow(c.miniBufferWidget)
        else:
            c.bodyWantsFocusNow()
    #@-node:ekr.20061031131434.135:k.minibufferWantsFocus/Now
    #@+node:ekr.20061031170011.5:getLabel
    def getLabel (self,ignorePrompt=False):

        k = self ; w = self.widget
        if not w: return ''

        if self.useTextWidget:
            s = w.getAllText()
        else:
            s = k.svar and k.svar.get()

        if ignorePrompt:
            return s[len(k.mb_prefix):]
        else:
            return s or ''
    #@-node:ekr.20061031170011.5:getLabel
    #@+node:ekr.20061031170011.6:protectLabel
    def protectLabel (self):

        k = self ; w = self.widget
        if not w: return

        if self.useTextWidget:
            k.mb_prefix = w.getAllText()
        else:
            if k.svar:
                k.mb_prefix = k.svar.get()
    #@-node:ekr.20061031170011.6:protectLabel
    #@+node:ekr.20061031170011.7:resetLabel
    def resetLabel (self):

        k = self
        k.setLabelGrey('')
        k.mb_prefix = ''
    #@-node:ekr.20061031170011.7:resetLabel
    #@+node:ekr.20061031170011.8:setLabel
    def setLabel (self,s,protect=False):

        k = self ; c = k.c ; w = self.widget
        if not w: return
        trace = self.trace_minibuffer and not g.app.unitTesting

        trace and g.trace(repr(s),g.callers())

        if self.useTextWidget:
            w.setAllText(s)
            n = len(s)
            w.setSelectionRange(n,n,insert=n)
            c.masterFocusHandler() # Restore to the previously requested focus.
        else:
            if k.svar: k.svar.set(s)

        if protect:
            k.mb_prefix = s
    #@-node:ekr.20061031170011.8:setLabel
    #@+node:ekr.20061031170011.9:extendLabel
    def extendLabel(self,s,select=False,protect=False):

        k = self ; c = k.c ; w = self.widget
        if not w: return
        trace = self.trace_minibuffer and not g.app.unitTesting

        trace and g.trace(repr(s))
        if not s: return

        if self.useTextWidget:
            c.widgetWantsFocusNow(w)
            w.insert('end',s)
            if select:
                i,j = k.getEditableTextRange()
                w.setSelectionRange(i,j,insert=j)
            if protect:
                k.protectLabel()
    #@-node:ekr.20061031170011.9:extendLabel
    #@+node:ekr.20061031170011.10:setLabelBlue
    def setLabelBlue (self,label=None,protect=False):

        k = self ; w = k.widget
        if not w: return

        w.setBackgroundColor('lightblue')

        if label is not None:
            k.setLabel(label,protect)
    #@-node:ekr.20061031170011.10:setLabelBlue
    #@+node:ekr.20061031170011.11:setLabelGrey
    def setLabelGrey (self,label=None):

        k = self ; w = self.widget
        if not w: return

        w.setBackgroundColor('lightgrey')

        if label is not None:
            k.setLabel(label)

    setLabelGray = setLabelGrey
    #@-node:ekr.20061031170011.11:setLabelGrey
    #@+node:ekr.20061031170011.12:updateLabel
    def updateLabel (self,event):

        '''Mimic what would happen with the keyboard and a Text editor
        instead of plain accumalation.'''

        k = self ; c = k.c ; w = self.widget
        ch = (event and event.char) or ''
        keysym = (event and event.keysym) or ''
        trace = self.trace_minibuffer and not g.app.unitTesting

        trace and g.trace('ch',ch,'keysym',keysym,'k.stroke',k.stroke)

        if ch and ch not in ('\n','\r'):
            if self.useTextWidget:
                c.widgetWantsFocusNow(w)
                i,j = w.getSelectionRange()
                ins = w.getInsertPoint()
                if i != j:
                    w.delete(i,j)
                if ch == '\b':
                    s = w.getAllText()
                    if len(s) > len(k.mb_prefix):
                        w.delete(i-1)
                else:
                    w.insert(ins,ch)
                # g.trace(k.mb_prefix)       
            else:
                # Just add the character.
                k.setLabel(k.getLabel() + ch)
    #@-node:ekr.20061031170011.12:updateLabel
    #@+node:ekr.20061031170011.13:getEditableTextRange
    def getEditableTextRange (self):

        k = self ; w = self.widget
        s = w.getAllText()
        # g.trace(len(s),repr(s))

        i = len(k.mb_prefix)
        j = len(s)
        return i,j
    #@nonl
    #@-node:ekr.20061031170011.13:getEditableTextRange
    #@-node:ekr.20061031170011.3:Minibuffer (keyHandler)
    #@+node:ekr.20061031131434.156:Modes
    #@+node:ekr.20061031131434.157:badMode
    def badMode(self,modeName):

        k = self

        k.clearState()
        if modeName.endswith('-mode'): modeName = modeName[:-5]
        k.setLabelGrey('@mode %s is not defined (or is empty)' % modeName)
    #@-node:ekr.20061031131434.157:badMode
    #@+node:ekr.20061031131434.158:createModeBindings
    def createModeBindings (self,modeName,d,w):

        '''Create mode bindings for the named mode using dictionary d for w, a text widget.'''

        __pychecker__ = '--no-argsused' # w not used (except for debugging).

        k = self ; c = k.c

        # g.trace(g.listToString(d.keys()))

        for commandName in d.keys():
            if commandName == '*entry-commands*': continue
            func = c.commandsDict.get(commandName)
            if not func:
                g.es_print('No such command: %s. Referenced from %s' % (
                    commandName,modeName))
                continue
            bunchList = d.get(commandName,[])
            for bunch in bunchList:
                stroke = bunch.val
                # Important: bunch.val is a stroke returned from k.strokeFromSetting.
                # Do not call k.strokeFromSetting again here!
                if stroke and stroke not in ('None','none',None):
                    if 0:
                        g.trace(
                            g.app.gui.widget_name(w), modeName,
                            '%10s' % (stroke),
                            '%20s' % (commandName),
                            bunch.nextMode)

                    k.makeMasterGuiBinding(stroke)

                    # Create the entry for the mode in k.masterBindingsDict.
                    # Important: this is similar, but not the same as k.bindKeyToDict.
                    # Thus, we should **not** call k.bindKey here!
                    d2 = k.masterBindingsDict.get(modeName,{})
                    d2 [stroke] = g.Bunch(
                        commandName=commandName,
                        func=func,
                        nextMode=bunch.nextMode,
                        stroke=stroke)
                    k.masterBindingsDict [ modeName ] = d2
    #@-node:ekr.20061031131434.158:createModeBindings
    #@+node:ekr.20061031131434.159:endMode
    def endMode(self,event):

        k = self ; c = k.c

        c.frame.log.deleteTab('Mode')

        k.endCommand(event,k.stroke)
        k.inputModeName = None
        k.clearState()
        k.resetLabel()
        k.showStateAndMode() # Restores focus.
    #@-node:ekr.20061031131434.159:endMode
    #@+node:ekr.20061031131434.160:enterNamedMode
    def enterNamedMode (self,event,commandName):

        k = self ; c = k.c
        modeName = commandName[6:]
        k.generalModeHandler(event,modeName=modeName)
    #@-node:ekr.20061031131434.160:enterNamedMode
    #@+node:ekr.20061031131434.161:exitNamedMode
    def exitNamedMode (self,event):

        k = self

        if k.inState():
            k.endMode(event)

        k.showStateAndMode()
    #@-node:ekr.20061031131434.161:exitNamedMode
    #@+node:ekr.20061031131434.162:generalModeHandler
    def generalModeHandler (self,event,
        commandName=None,func=None,modeName=None,nextMode=None):

        '''Handle a mode defined by an @mode node in leoSettings.leo.'''

        k = self ; c = k.c
        state = k.getState(modeName)
        trace = False or c.config.getBool('trace_modes')

        if trace: g.trace(modeName,'state',state)

        if state == 0:
            # self.initMode(event,modeName)
            k.inputModeName = modeName
            k.modeWidget = event and event.widget
            k.setState(modeName,1,handler=k.generalModeHandler)
            self.initMode(event,modeName)
            if not k.silentMode:
                if c.config.getBool('showHelpWhenEnteringModes'):
                    k.modeHelp(event)
                else:
                    c.frame.log.hideTab('Mode')
                if k.useTextWidget:
                    c.minibufferWantsFocus()
                else:
                    c.restoreRequestedFocus()
        elif not func:
            g.trace('No func: improper key binding')
            return 'break'
        else:
            if commandName == 'mode-help':
                func(event)
            else:
                savedModeName = k.inputModeName # Remember this: it may be cleared.
                self.endMode(event)
                if trace or c.config.getBool('trace_doCommand'): g.trace(func.__name__)
                # New in 4.4.1 b1: pass an event describing the original widget.
                if event:
                    event.widget = k.modeWidget
                else:
                    event = g.Bunch(widget = k.modeWidget)
                if trace: g.trace(modeName,'state',state,commandName,'nextMode',nextMode)
                func(event)
                if nextMode in (None,'none'):
                    # Do *not* clear k.inputModeName or the focus here.
                    # func may have put us in *another* mode.
                    pass
                elif nextMode == 'same':
                    silent = k.silentMode
                    k.setState(modeName,1,handler=k.generalModeHandler)
                    self.reinitMode(modeName) # Re-enter this mode.
                    k.silentMode = silent
                else:
                    k.silentMode = False # All silent modes must do --> set-silent-mode.
                    self.initMode(event,nextMode) # Enter another mode.

        return 'break'
    #@-node:ekr.20061031131434.162:generalModeHandler
    #@+node:ekr.20061031131434.163:initMode
    def initMode (self,event,modeName):

        k = self ; c = k.c
        trace = c.config.getBool('trace_modes')
        if trace: g.trace(modeName)

        if not modeName:
            g.trace('oops: no modeName')
            return

        d = g.app.config.modeCommandsDict.get('enter-'+modeName)
        if not d:
            self.badMode(modeName)
            return
        else:
            k.modeBindingsDict = d

        k.inputModeName = modeName
        k.silentMode = False

        entryCommands = d.get('*entry-commands*',[])
        if entryCommands:
            for commandName in entryCommands:
                if trace: g.trace('entry command:',commandName)
                k.simulateCommand(commandName)

        # Create bindings after we know whether we are in silent mode.
        w = g.choose(k.silentMode,k.modeWidget,k.widget)
        k.createModeBindings(modeName,d,w)

        if k.silentMode:
            k.showStateAndMode()
        else:
            k.setLabelBlue(modeName+': ',protect=True)
            k.showStateAndMode()
            if k.useTextWidget:
                c.minibufferWantsFocus()
            else:
                pass # Do *not* change the focus here!
    #@-node:ekr.20061031131434.163:initMode
    #@+node:ekr.20061031131434.164:reinitMode
    def reinitMode (self,modeName):

        k = self ; c = k.c

        d = k.modeBindingsDict

        k.inputModeName = modeName
        w = g.choose(k.silentMode,k.modeWidget,k.widget)
        k.createModeBindings(modeName,d,w)

        if k.silentMode:
            k.showStateAndMode()
        else:
            # Do not set the status line here.
            k.setLabelBlue(modeName+': ',protect=True)
            if k.useTextWidget:
                c.minibufferWantsFocus()
            else:
                pass # Do *not* change the focus here!
    #@-node:ekr.20061031131434.164:reinitMode
    #@+node:ekr.20061031131434.165:modeHelp
    def modeHelp (self,event):

        '''The mode-help command.

        A possible convention would be to bind <Tab> to this command in most modes,
        by analogy with tab completion.'''

        k = self ; c = k.c

        c.endEditing()

        # g.trace(k.inputModeName)

        if k.inputModeName:
            d = g.app.config.modeCommandsDict.get('enter-'+k.inputModeName)
            k.modeHelpHelper(d)

        if k.useTextWidget and not k.silentMode:
            c.minibufferWantsFocus()

        return 'break'
    #@+node:ekr.20061031131434.166:modeHelpHelper
    def modeHelpHelper (self,d):

        k = self ; c = k.c ; tabName = 'Mode'
        c.frame.log.clearTab(tabName)
        keys = d.keys() ; keys.sort()

        data = [] ; n = 20
        for key in keys:
            if key != '*entry-commands*':
                bunchList = d.get(key)
                for bunch in bunchList:
                    shortcut = bunch.val
                    if shortcut not in (None,'None'):
                        s1 = key ; s2 = k.prettyPrintKey(shortcut,brief=True)
                        n = max(n,len(s1))
                        data.append((s1,s2),)

        data.sort()

        # g.es('%s\n\n' % (k.inputModeName),tabName=tabName)

        modeName = k.inputModeName.replace('-',' ')
        if modeName.endswith('mode'): modeName = modeName[:-4].strip()

        g.es('%s mode\n\n' % modeName,tabName=tabName)

        # This isn't perfect in variable-width fonts.
        for s1,s2 in data:
            g.es('%*s %s' % (n,s1,s2),tabName=tabName)
    #@-node:ekr.20061031131434.166:modeHelpHelper
    #@-node:ekr.20061031131434.165:modeHelp
    #@-node:ekr.20061031131434.156:Modes
    #@+node:ekr.20061031131434.167:Shared helpers
    #@+node:ekr.20061031131434.175:k.computeCompletionList
    # Important: this code must not change mb_tabListPrefix.  Only doBackSpace should do that.

    def computeCompletionList (self,defaultTabList,backspace):

        k = self ; c = k.c ; s = k.getLabel() ; tabName = 'Completion'
        command = s [len(k.mb_prompt):]
            # s always includes prefix, so command is well defined.

        k.mb_tabList,common_prefix = g.itemsMatchingPrefixInList(command,defaultTabList)
        c.frame.log.clearTab(tabName)

        if k.mb_tabList:
            k.mb_tabListIndex = -1 # The next item will be item 0.

            if not backspace:
                k.setLabel(k.mb_prompt + common_prefix)

            inverseBindingDict = k.computeInverseBindingDict()
            data = [] ; n1 = 20; n2 = 4
            for commandName in k.mb_tabList:
                dataList = inverseBindingDict.get(commandName,[('',''),])
                for z in dataList:
                    pane,key = z
                    s1 = commandName
                    s2 = pane
                    s3 = k.prettyPrintKey(key)
                    n1 = max(n1,len(s1))
                    n2 = max(n2,len(s2))
                    data.append((s1,s2,s3),)
            for s1,s2,s3 in data:
                g.es('%*s %*s %s' % (-(min(20,n1)),s1,n2,s2,s3),tabName=tabName)

        c.bodyWantsFocus()
    #@-node:ekr.20061031131434.175:k.computeCompletionList
    #@+node:ekr.20061031131434.176:computeInverseBindingDict
    def computeInverseBindingDict (self):

        k = self ; d = {}

        # keys are minibuffer command names, values are shortcuts.
        for shortcut in k.bindingsDict.keys():
            bunchList = k.bindingsDict.get(shortcut,[])
            for b in bunchList:
                shortcutList = d.get(b.commandName,[])
                bunchList = k.bindingsDict.get(shortcut,[g.Bunch(pane='all')])
                for b in bunchList:
                    #pane = g.choose(b.pane=='all','','%s:' % (b.pane))
                    pane = '%s:' % (b.pane)
                    data = (pane,shortcut)
                    if data not in shortcutList:
                        shortcutList.append(data)

                d [b.commandName] = shortcutList

        return d
    #@-node:ekr.20061031131434.176:computeInverseBindingDict
    #@+node:ekr.20061031131434.168:getFileName & helpers
    def getFileName (self,event=None,handler=None,prefix='',filterExt='.leo'):

        '''Similar to k.getArg, but uses completion to indicate files on the file system.'''

        k = self ; c = k.c ; gui = g.app.gui
        tag = 'getFileName' ; state = k.getState(tag)
        tabName = 'Completion'
        keysym = gui.eventKeysym(event)
        # g.trace('state',state,'keysym',keysym)
        if state == 0:
            k.arg = ''
            #@        << init altX vars >>
            #@+node:ekr.20061031131434.169:<< init altX vars >>
            k.filterExt = filterExt
            k.mb_prefix = (prefix or k.getLabel())
            k.mb_prompt = prefix or k.getLabel()
            k.mb_tabList = []

            # Clear the list: any non-tab indicates that a new prefix is in effect.
            theDir = g.os_path_abspath(os.curdir)
            k.extendLabel(theDir,select=False,protect=False)

            k.mb_tabListPrefix = k.getLabel()
            #@-node:ekr.20061031131434.169:<< init altX vars >>
            #@nl
            # Set the states.
            k.getFileNameHandler = handler
            k.setState(tag,1,k.getFileName)
            k.afterArgWidget = event and event.widget or c.frame.body.bodyCtrl
            c.frame.log.clearTab(tabName)
            c.minibufferWantsFocusNow()
        elif keysym == 'Return':
            k.arg = k.getLabel(ignorePrompt=True)
            handler = k.getFileNameHandler
            c.frame.log.deleteTab(tabName)
            if handler: handler(event)
        elif keysym == 'Tab':
            k.doFileNameTab()
            c.minibufferWantsFocus()
        elif keysym == 'BackSpace':
            k.doFileNameBackSpace() 
            c.minibufferWantsFocus()
        else:
            k.doFileNameChar(event)
        return 'break'
    #@+node:ekr.20061031131434.170:k.doFileNameBackSpace
    def doFileNameBackSpace (self):

        '''Cut back to previous prefix and update prefix.'''

        k = self ; c = k.c

        if 0:
            g.trace(
                len(k.mb_tabListPrefix) > len(k.mb_prefix),
                repr(k.mb_tabListPrefix),repr(k.mb_prefix))

        if len(k.mb_tabListPrefix) > len(k.mb_prefix):
            k.mb_tabListPrefix = k.mb_tabListPrefix [:-1]
            k.setLabel(k.mb_tabListPrefix)
    #@-node:ekr.20061031131434.170:k.doFileNameBackSpace
    #@+node:ekr.20061031131434.171:k.doFileNameChar
    def doFileNameChar (self,event):

        k = self

        # Clear the list, any other character besides tab indicates that a new prefix is in effect.
        k.mb_tabList = []
        k.updateLabel(event)
        k.mb_tabListPrefix = k.getLabel()

        common_prefix = k.computeFileNameCompletionList()

        if k.mb_tabList:
            k.setLabel(k.mb_prompt + common_prefix)
        else:
            # Restore everything.
            old = k.getLabel(ignorePrompt=True)[:-1]
            k.setLabel(k.mb_prompt + old)
    #@-node:ekr.20061031131434.171:k.doFileNameChar
    #@+node:ekr.20061031131434.172:k.doFileNameTab
    def doFileNameTab (self):

        k = self
        common_prefix = k.computeFileNameCompletionList()

        if k.mb_tabList:
            k.setLabel(k.mb_prompt + common_prefix)
    #@-node:ekr.20061031131434.172:k.doFileNameTab
    #@+node:ekr.20061031131434.173:k.computeFileNameCompletionList
    # This code must not change mb_tabListPrefix.
    def computeFileNameCompletionList (self):

        k = self ; c = k.c ; s = k.getLabel() ; tabName = 'Completion'
        path = k.getLabel(ignorePrompt=True)
        sep = os.path.sep
        tabList = []
        for f in glob.glob(path+'*'):
            if g.os_path_isdir(f):
                tabList.append(f + sep)
            else:
                junk,ext = g.os_path_splitext(f)
                if not ext or ext == k.filterExt:
                    tabList.append(f)
        k.mb_tabList = tabList
        junk,common_prefix = g.itemsMatchingPrefixInList(path,tabList)
        if tabList:
            c.frame.log.clearTab(tabName)
            k.showFileNameTabList()
        return common_prefix
    #@-node:ekr.20061031131434.173:k.computeFileNameCompletionList
    #@+node:ekr.20061031131434.174:k.showFileNameTabList
    def showFileNameTabList (self):

        k = self ; tabName = 'Completion'

        for path in k.mb_tabList:
            theDir,fileName = g.os_path_split(path)
            s = g.choose(path.endswith('\\'),theDir,fileName)
            s = fileName or g.os_path_basename(theDir) + '\\'
            g.es(s,tabName=tabName)
    #@-node:ekr.20061031131434.174:k.showFileNameTabList
    #@-node:ekr.20061031131434.168:getFileName & helpers
    #@+node:ekr.20061031131434.179:getShortcutForCommand/Name (should return lists)
    def getShortcutForCommandName (self,commandName):

        k = self ; c = k.c

        command = c.commandsDict.get(commandName)

        if command:
            for key in k.bindingsDict:
                bunchList = k.bindingsDict.get(key,[])
                for b in bunchList:
                    if b.commandName == commandName:
                        return k.tkbindingFromStroke(key)
        return ''

    def getShortcutForCommand (self,command):

        k = self ; c = k.c

        if command:
            for key in k.bindingsDict:
                bunchList = k.bindingsDict.get(key,[])
                for b in bunchList:
                    if b.commandName == command.__name__:
                         return k.tkbindingFromStroke(key)
        return ''
    #@-node:ekr.20061031131434.179:getShortcutForCommand/Name (should return lists)
    #@+node:ekr.20061031131434.177:k.doBackSpace
    # Used by getArg and fullCommand.

    def doBackSpace (self,defaultCompletionList,completion=True):

        '''Cut back to previous prefix and update prefix.'''

        k = self ; c = k.c

        if 0:
            g.trace('completion',completion,
                len(k.mb_tabListPrefix) > len(k.mb_prefix),
                repr(k.mb_tabListPrefix),repr(k.mb_prefix))

        if completion:
            if len(k.mb_tabListPrefix) > len(k.mb_prefix):
                k.mb_tabListPrefix = k.mb_tabListPrefix [:-1]
                k.setLabel(k.mb_tabListPrefix)
                k.computeCompletionList(defaultCompletionList,backspace=True)
            # else:
                # k.keyboardQuit(event=None)
        else:
            s = k.getLabel(ignorePrompt=False)
            # g.trace(repr(s),repr(k.mb_prefix))
            if s and len(s) > len(k.mb_prefix):
                k.setLabel(s[:-1])
    #@-node:ekr.20061031131434.177:k.doBackSpace
    #@+node:ekr.20061031131434.178:k.doTabCompletion
    # Used by getArg and fullCommand.

    def doTabCompletion (self,defaultTabList,redraw=True):

        '''Handle tab completion when the user hits a tab.'''

        k = self ; c = k.c ; s = k.getLabel().strip()

        if k.mb_tabList and s.startswith(k.mb_tabListPrefix):
            # g.trace('cycle',repr(s))
            # Set the label to the next item on the tab list.
            k.mb_tabListIndex +=1
            if k.mb_tabListIndex >= len(k.mb_tabList):
                k.mb_tabListIndex = 0
            k.setLabel(k.mb_prompt + k.mb_tabList [k.mb_tabListIndex])
        else:
            if redraw:
                k.computeCompletionList(defaultTabList,backspace=False)

        c.minibufferWantsFocusNow()
    #@-node:ekr.20061031131434.178:k.doTabCompletion
    #@+node:ekr.20061031131434.180:traceBinding
    def traceBinding (self,bunch,shortcut,w):

        k = self ; c = k.c ; gui = g.app.gui

        if not c.config.getBool('trace_bindings'): return

        theFilter = c.config.getString('trace_bindings_filter') or ''
        if theFilter and shortcut.lower().find(theFilter.lower()) == -1: return

        pane_filter = c.config.getString('trace_bindings_pane_filter')

        if not pane_filter or pane_filter.lower() == bunch.pane:
             g.trace(bunch.pane,shortcut,bunch.commandName,gui.widget_name(w))
    #@-node:ekr.20061031131434.180:traceBinding
    #@-node:ekr.20061031131434.167:Shared helpers
    #@+node:ekr.20061031131434.133:setInputState
    def setInputState (self,state,showState=False):

        k = self ; c = k.c ; body = c.frame.body ; w = body.bodyCtrl

        # g.trace(state,g.callers())
        k.unboundKeyAction = state
        k.showStateAndMode()
        assert state in ('insert','command','overwrite')

        if w:
            if state == 'insert':
                bg = k.insert_mode_bg_color ; fg = k.insert_mode_fg_color
            elif state == 'command':
                bg = k.command_mode_bg_color ; fg = k.command_mode_fg_color
            elif state == 'overwrite':
                bg = k.overwrite_mode_bg_color, fg = k.overwrite_mode_fg_color

            # g.trace(id(w),bg,fg,self)

            body.setEditorColors(bg=bg,fg=fg)
    #@nonl
    #@-node:ekr.20061031131434.133:setInputState
    #@+node:ekr.20061031131434.181:Shortcuts (keyHandler)
    #@+node:ekr.20061031131434.182:isPlainKey & test
    def isPlainKey (self,shortcut):

        '''Return true if the shortcut refers to a plain (non-Alt,non-Ctl) key.'''

        k = self ; shortcut = shortcut or ''

        for s in ('Alt','Ctrl','Command'):
            if shortcut.find(s) != -1:
                return False
        else:
            # Careful, allow bare angle brackets for unit tests.
            if shortcut.startswith('<') and shortcut.endswith('>'):
                shortcut = shortcut[1:-1]

            isPlain = (
                len(shortcut) == 1 or
                len(k.guiBindNamesInverseDict.get(shortcut,'')) == 1 or
                # A hack: allow Return to be bound to command.
                shortcut == 'Tab'
            )

            # g.trace(isPlain,repr(shortcut))
            return isPlain
    #@+node:ekr.20061031131434.183:@test isPlainKey
    if g.unitTesting:

        __pychecker__ = '--no-reimport'
        import string

        c,p = g.getTestVars() # Optional: prevents pychecker warnings.
        k = c.k

        for ch in (string.printable):
            if ch == '\n': continue # A special case.
            assert k.isPlainKey(ch), 'wrong: not plain: %s' % (ch)

        special = (
            'Return', # A special case.
            'Begin','Break','Caps_Lock','Clear','Down','End','Escape',
            'F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12',
            'KP_Add', 'KP_Decimal', 'KP_Divide', 'KP_Enter', 'KP_Equal',
            'KP_Multiply, KP_Separator,KP_Space, KP_Subtract, KP_Tab',
            'KP_F1','KP_F2','KP_F3','KP_F4',
            'KP_0','KP_1','KP_2','KP_3','KP_4','KP_5','KP_6','KP_7','KP_8','KP_9',
            'Home','Left','Linefeed','Next','Num_Lock',
            'PageDn','PageUp','Pause','Prior','Right','Up',
            'Sys_Req',
        )

        for ch in special:
            assert not k.isPlainKey(ch), 'wrong: is plain: %s' % (ch)
    #@-node:ekr.20061031131434.183:@test isPlainKey
    #@-node:ekr.20061031131434.182:isPlainKey & test
    #@+node:ekr.20061031131434.184:shortcutFromSetting (uses k.guiBindNamesDict)
    def shortcutFromSetting (self,setting):

        k = self

        if not setting:
            return None

        s = g.stripBrackets(setting.strip())
        #@    << define cmd, ctrl, alt, shift >>
        #@+node:ekr.20061031131434.185:<< define cmd, ctrl, alt, shift >>
        s2 = s.lower()

        cmd   = s2.find("cmd") >= 0     or s2.find("command") >= 0
        ctrl  = s2.find("control") >= 0 or s2.find("ctrl") >= 0
        alt   = s2.find("alt") >= 0
        shift = s2.find("shift") >= 0   or s2.find("shft") >= 0
        #@-node:ekr.20061031131434.185:<< define cmd, ctrl, alt, shift >>
        #@nl
        if k.swap_mac_keys and sys.platform == "darwin":
            #@        << swap cmd and ctrl keys >>
            #@+node:ekr.20061031131434.186:<< swap cmd and ctrl keys >>
            if ctrl and not cmd:
                cmd = True ; ctrl = False
            if alt and not ctrl:
                ctrl = True ; alt = False
            #@-node:ekr.20061031131434.186:<< swap cmd and ctrl keys >>
            #@nl
        #@    << convert minus signs to plus signs >>
        #@+node:ekr.20061031131434.187:<< convert minus signs to plus signs >>
        # Replace all minus signs by plus signs, except a trailing minus:
        if s.endswith('-'):
            s = s[:-1].replace('-','+') + '-'
        else:
            s = s.replace('-','+')
        #@-node:ekr.20061031131434.187:<< convert minus signs to plus signs >>
        #@nl
        #@    << compute the last field >>
        #@+node:ekr.20061031131434.188:<< compute the last field >>
        if s.endswith('+'):
            last = '+'
        else:
            fields = s.split('+') # Don't lower this field.
            last = fields and fields[-1]
            if not last:
                if not g.app.menuWarningsGiven:
                    print "bad shortcut specifier:", s
                return None

        if len(last) == 1:
            last2 = k.guiBindNamesDict.get(last) # Fix new bug introduced in 4.4b2.
            # g.trace(last,last2)
            if last2:
                last = last2 ; shift = False # Ignore the shift state for these special chars.
            else:
                if shift:
                    last = last.upper()
                    shift = False
                else:
                    last = last.lower()

                # New in Leo 4.4.2: Alt-2 is not a key event!
                if last.isdigit():
                    last = 'Key-' + last
        else:
            # Translate from a made-up (or lowercase) name to 'official' Tk binding name.
            # This is a *one-way* translation, done only here.
            d = k.settingsNameDict
            last = d.get(last.lower(),last)
        #@-node:ekr.20061031131434.188:<< compute the last field >>
        #@nl
        #@    << compute shortcut >>
        #@+node:ekr.20061031131434.189:<< compute shortcut >>
        table = (
            (alt, 'Alt+'),
            (ctrl,'Ctrl+'),
            (cmd, 'Command+'),
            (shift,'Shift+'),
            (True, last),
        )

        # new in 4.4b3: convert all characters to unicode first.
        shortcut = ''.join([g.toUnicode(val,g.app.tkEncoding) for flag,val in table if flag])
        #@-node:ekr.20061031131434.189:<< compute shortcut >>
        #@nl
        # g.trace(setting,shortcut)
        return shortcut

    canonicalizeShortcut = shortcutFromSetting # For compatibility.
    strokeFromSetting = shortcutFromSetting
    #@-node:ekr.20061031131434.184:shortcutFromSetting (uses k.guiBindNamesDict)
    #@+node:ekr.20061031131434.190:k.tkbindingFromStroke
    def tkbindingFromStroke (self,stroke):

        '''Convert a stroke (key to k.bindingsDict) to an actual Tk binding.'''

        stroke = g.stripBrackets(stroke)

        for a,b in (
            ('Alt+','Alt-'),
            ('Ctrl+','Control-'),
            ('Shift+','Shift-'),
            ('Command+','Command-'),
        ):
            stroke = stroke.replace(a,b)

        # g.trace('<%s>' % stroke)
        return '<%s>' % stroke
    #@-node:ekr.20061031131434.190:k.tkbindingFromStroke
    #@+node:ekr.20061031131434.191:k.prettyPrintKey
    def prettyPrintKey (self,stroke,brief=False):

        k = self
        s = stroke and g.stripBrackets(stroke.strip())
        if not s: return ''

        shift = s.find("shift") >= 0 or s.find("shft") >= 0

        # Replace all minus signs by plus signs, except a trailing minus:
        if s.endswith('-'): s = s[:-1].replace('-','+') + '-'
        else:               s = s.replace('-','+')
        fields = s.split('+')
        last = fields and fields[-1]
        if last and len(last) == 1:
            prev = s[:-1]
            if last.isalpha():
                if last.isupper():
                    if not shift:
                        s = prev + 'Shift+' + last
                elif last.islower():
                    if not prev and not brief:
                        s = 'Key+' + last.upper()
                    else:
                        s = prev + last.upper()
        else:
            last = k.guiBindNamesInverseDict.get(last,last)
            if fields and fields[:-1]:
                s = '%s+%s' % ('+'.join(fields[:-1]),last)
            else:
                s = last
        return g.choose(brief,s,'<%s>' % s)
    #@-node:ekr.20061031131434.191:k.prettyPrintKey
    #@-node:ekr.20061031131434.181:Shortcuts (keyHandler)
    #@+node:ekr.20061031131434.192:showStateAndMode
    def showStateAndMode(self):

        k = self ; c = k.c ; frame = c.frame
        state = k.unboundKeyAction
        mode = k.getStateKind()

        if hasattr(frame,'clearStatusLine') and not state.capitalize()=='Insert':
            frame.clearStatusLine()
            put = frame.putStatusLine
            put('Key state: ',color='blue')
            put('%s' % state.capitalize())
            if mode:
                # put(' mode: ',color='blue')
                if mode.endswith('-mode'): mode = mode[:-5]
                mode = mode.replace('-',' ').capitalize()
                put(' Mode: ',color='blue')
                put(mode)

            # Restore the focus.
            c.restoreFocus()
    #@-node:ekr.20061031131434.192:showStateAndMode
    #@+node:ekr.20061031131434.193:States
    #@+node:ekr.20061031131434.194:clearState
    def clearState (self):

        k = self
        k.state.kind = None
        k.state.n = None
        k.state.handler = None
    #@-node:ekr.20061031131434.194:clearState
    #@+node:ekr.20061031131434.195:getStateHandler
    def getStateHandler (self):

        return self.state.handler
    #@-node:ekr.20061031131434.195:getStateHandler
    #@+node:ekr.20061031131434.196:getState
    def getState (self,kind):

        k = self
        val = g.choose(k.state.kind == kind,k.state.n,0)
        # g.trace(state,'returns',val)
        return val
    #@-node:ekr.20061031131434.196:getState
    #@+node:ekr.20061031131434.197:getStateKind
    def getStateKind (self):

        return self.state.kind
    #@-node:ekr.20061031131434.197:getStateKind
    #@+node:ekr.20061031131434.198:inState
    def inState (self,kind=None):

        k = self

        if kind:
            return k.state.kind == kind and k.state.n != None
        else:
            return k.state.kind and k.state.n != None
    #@-node:ekr.20061031131434.198:inState
    #@+node:ekr.20061031131434.199:setState
    def setState (self,kind,n,handler=None):

        k = self
        if kind and n != None:
            k.state.kind = kind
            k.state.n = n
            if handler:
                k.state.handler = handler
        else:
            k.clearState()

        # k.showStateAndMode()
    #@-node:ekr.20061031131434.199:setState
    #@-node:ekr.20061031131434.193:States
    #@+node:ekr.20061031131434.200:universalDispatcher & helpers
    def universalDispatcher (self,event):

        '''Handle accumulation of universal argument.'''

        #@    << about repeat counts >>
        #@+node:ekr.20061031131434.201:<< about repeat counts >>
        #@@nocolor

        #@+at  
        #@nonl
        # Any Emacs command can be given a numeric argument. Some commands 
        # interpret the
        # argument as a repetition count. For example, giving an argument of 
        # ten to the
        # key C-f (the command forward-char, move forward one character) moves 
        # forward ten
        # characters. With these commands, no argument is equivalent to an 
        # argument of
        # one. Negative arguments are allowed. Often they tell a command to 
        # move or act
        # backwards.
        # 
        # If your keyboard has a META key, the easiest way to specify a 
        # numeric argument
        # is to type digits and/or a minus sign while holding down the the 
        # META key. For
        # example,
        # 
        # M-5 C-n
        # 
        # moves down five lines. The characters Meta-1, Meta-2, and so on, as 
        # well as
        # Meta--, do this because they are keys bound to commands 
        # (digit-argument and
        # negative-argument) that are defined to contribute to an argument for 
        # the next
        # command.
        # 
        # Another way of specifying an argument is to use the C-u 
        # (universal-argument)
        # command followed by the digits of the argument. With C-u, you can 
        # type the
        # argument digits without holding down shift keys. To type a negative 
        # argument,
        # start with a minus sign. Just a minus sign normally means -1. C-u 
        # works on all
        # terminals.
        # 
        # C-u followed by a character which is neither a digit nor a minus 
        # sign has the
        # special meaning of "multiply by four". It multiplies the argument 
        # for the next
        # command by four. C-u twice multiplies it by sixteen. Thus, C-u C-u 
        # C-f moves
        # forward sixteen characters. This is a good way to move forward 
        # "fast", since it
        # moves about 1/5 of a line in the usual size screen. Other useful 
        # combinations
        # are C-u C-n, C-u C-u C-n (move down a good fraction of a screen), 
        # C-u C-u C-o
        # (make "a lot" of blank lines), and C-u C-k (kill four lines).
        # 
        # Some commands care only about whether there is an argument and not 
        # about its
        # value. For example, the command M-q (fill-paragraph) with no 
        # argument fills
        # text; with an argument, it justifies the text as well. (See section 
        # Filling
        # Text, for more information on M-q.) Just C-u is a handy way of 
        # providing an
        # argument for such commands.
        # 
        # Some commands use the value of the argument as a repeat count, but 
        # do something
        # peculiar when there is no argument. For example, the command C-k 
        # (kill-line)
        # with argument n kills n lines, including their terminating newlines. 
        # But C-k
        # with no argument is special: it kills the text up to the next 
        # newline, or, if
        # point is right at the end of the line, it kills the newline itself. 
        # Thus, two
        # C-k commands with no arguments can kill a non-blank line, just like 
        # C-k with an
        # argument of one. (See section Deletion and Killing, for more 
        # information on
        # C-k.)
        # 
        # A few commands treat a plain C-u differently from an ordinary 
        # argument. A few
        # others may treat an argument of just a minus sign differently from 
        # an argument
        # of -1. These unusual cases will be described when they come up; they 
        # are always
        # to make the individual command more convenient to use.
        #@-at
        #@-node:ekr.20061031131434.201:<< about repeat counts >>
        #@nl

        k = self ; gui = g.app.gui
        state = k.getState('u-arg')

        if state == 0:
            # The call should set the label.
            k.setState('u-arg',1,k.universalDispatcher)
            k.repeatCount = 1
        elif state == 1:
            stroke = k.stroke ; keysym = gui.eventKeysym(event)
                # Stroke is <Key> for plain keys, <Control-u> (k.universalArgKey)
            # g.trace(state,stroke)
            if stroke == k.universalArgKey:
                k.repeatCount = k.repeatCount * 4
            elif stroke == '<Key>' and (keysym.isdigit() or keysym == u'-'):
                k.updateLabel(event)
            elif stroke == '<Key>' and keysym in (
                'Alt_L','Alt_R',
                'Control_L','Control_R',
                'Shift_L','Shift_R',
            ):
                 # g.trace('stroke',k.stroke,'keysym',keysym)
                 k.updateLabel(event)
            else:
                # *Anything* other than C-u, '-' or a numeral is taken to be a command.
                # g.trace('stroke',k.stroke,'keysym',keysym)
                val = k.getLabel(ignorePrompt=True)
                try:                n = int(val) * k.repeatCount
                except ValueError:  n = 1
                # g.trace('val',repr(val),'n',n,'k.repeatCount',k.repeatCount)
                k.clearState()
                k.executeNTimes(event,n)
                k.clearState()
                k.setLabelGrey()
                if 0: # Not ready yet.
                    # This takes us to macro state.
                    # For example Control-u Control-x ( will execute the last macro and begin editing of it.
                    if stroke == '<Control-x>':
                        k.setState('uC',2,k.universalDispatcher)
                        return k.doControlU(event,stroke)
        elif state == 2:
            k.doControlU(event,stroke)

        return 'break'
    #@+node:ekr.20061031131434.202:executeNTimes
    def executeNTimes (self,event,n):

        __pychecker__ = '--no-local' # z is used just for a repeat count.

        k = self ; stroke = k.stroke ; w = event.widget
        # g.trace('stroke',stroke,'keycode',event.keycode,'n',n)

        if stroke == k.fullCommandKey:
            for z in xrange(n):
                k.fullCommand()
        else:
            stroke = g.stripBrackets(stroke)
            bunchList = k.bindingsDict.get(stroke,[])
            if bunchList:
                b = bunchList[0]
                g.trace('method',b.f)
                for z in xrange(n):
                    if 1: # No need to do this: commands never alter events.
                        # ev = Tk.Event()
                        event = g.Bunch(
                            c = self.c,
                            widget = event.widget,
                            keysym = event.keysym,
                            keycode = event.keycode,
                            char = event.char,
                        )
                    k.masterCommand(event,b.f,'<%s>' % stroke)
            else:
                for z in xrange(n):
                    g.app.gui.event_generate(w,'<Key>',keycode=event.keycode,keysym=event.keysym)

    #@-node:ekr.20061031131434.202:executeNTimes
    #@+node:ekr.20061031131434.203:doControlU
    def doControlU (self,event,stroke):

        k = self ; c = k.c
        ch = g.app.gui.eventChar(event)

        k.setLabelBlue('Control-u %s' % g.stripBrackets(stroke))

        if ch == '(':
            k.clearState()
            k.resetLabel()
            c.macroCommands.startKbdMacro(event)
            c.macroCommands.callLastKeyboardMacro(event)
    #@-node:ekr.20061031131434.203:doControlU
    #@-node:ekr.20061031131434.200:universalDispatcher & helpers
    #@-others
#@-node:ekr.20061031131434.74:class keyHandlerClass
#@+node:ekr.20070627082044.827:Unit tests
#@+node:ekr.20070627082044.828:@@@test strokeFromEvent (no longer used)
if g.unitTesting:

    c,p = g.getTestVars()
    alt = 0x20000 ; ctrl  = 4 ; shift = 1 ; key = 0
    table = (
        (key, 'a','a','a'),
        (shift,'A','A','A'),
        (alt,'','a','Alt+a'),
        (alt+shift,'','A','Alt+A'),
        (shift,'A','A','A',),
        (key,'','Right','Right'),
        (shift,'','Right','Shift+Right'),
        (ctrl,'','Right','Ctrl+Right'),
        (ctrl+shift,'','Right','Ctrl+Shift+Right'),
    )
    for state, ch, keysym, result in table:
        val = c.k.strokeFromEvent(g.Bunch(state=state,char=ch,keysym=keysym))
        assert val==result,'Expected %s, Got %s' % (result,val)
#@nonl
#@-node:ekr.20070627082044.828:@@@test strokeFromEvent (no longer used)
#@+node:ekr.20070627082044.829:@test k.inverseCommandsDict is inverse of c.commandsDict
if g.unitTesting:
    # c.commandsDict: keys are emacs command names, values are functions f.
    # k.inverseCommandsDict: keys are f.__name__, values are emacs command names.
    d1 = c.commandsDict ; d2 = c.k.inverseCommandsDict
    if 0:
        vals = d2.values() ; vals.sort()
        vals = [z for z in vals if z.startswith('contract')]
        print 'inverseCommandsDict.values()',vals

    keys1 = d1.keys() ; keys1.sort()
    vals1 = d1.values()
    vals1 = [f.__name__ for f in vals1]
    vals1.sort()
    keys2 = d2.keys() ; keys2.sort()
    vals2 = d2.values(); vals2.sort()
    if 0:
        print keys1 ; print ; print
        print vals2 ; print ; print
        print keys2 ; print ; print
        print vals1

    # g.trace(g.dictToString(c.k.abbreviationsDict))
    abbrevDict = c.config.getAbbrevDict()

    # Find @button and @command nodes in this file.
    buttonKeys = []
    for p in c.allNodes_iter():
        h = p.headString().strip().lower()
        for kind in ('@button','@command'):
            if h.startswith(kind):
                key = h[len(kind):].strip()
                i = key.find('@key')
                if i > -1: key = key[:i].strip()
                key = key.replace(' ','-')
                # g.trace(key)
                if key not in buttonKeys:
                    buttonKeys.append(key)

    for key in keys1:
        if key not in vals2:
            if (
                key.startswith('enter-') and key.endswith('-mode') or
                key.startswith('press-') and key.endswith('-button') or
                key.startswith('delete-') and key.endswith('-button')
            ):
                vals2.append(key)
            elif key in buttonKeys:
                # List of buttons defined in this file.
                vals2.append(key)
            elif key.startswith('open-with-'):
                vals2.append(key)
            elif key in abbrevDict.keys():
                pass # g.trace('abbrev',key)
            else:
                assert False, '%s not in inverseCommandsDict.values()' % key

    vals2.sort()
    for val in vals2:
        if val not in keys1:
            assert False, '%s not in commandsDict.keys()' % (val)
#@nonl
#@-node:ekr.20070627082044.829:@test k.inverseCommandsDict is inverse of c.commandsDict
#@+node:ekr.20070627082044.830:@test strokeFromSetting
if g.unitTesting:
    # print 'settingsNameDict',c.k.settingsNameDict
    table = (
        ('a','a'),
        ('A','a'),
        ('Alt-a','Alt+a'),
        ('Alt-A','Alt+a'),
        ('Alt-Shift-a','Alt+A'),
        ('Alt-=','Alt+equal'),
        ('Alt-+','Alt+plus'),
        ('Alt-Shift++','Alt+plus'), # Ignore the shift.
        ('Alt--','Alt+minus'),
        ('Shift-a','A'),
        ('Shift-A','A'),
        ('RtArrow','Right'),
        ('Shift-RtArrow','Shift+Right'),
        ('Ctrl-RtArrow','Ctrl+Right'),
        ('Control-Right','Ctrl+Right'),
        ('PageUp','Prior'), ('Prior','Prior'),('Shift-PageUp','Shift+Prior'),
        ('PageDn','Next'),('Next','Next'),('Shift-Next','Shift+Next'),
    )
    for setting, result in table:
        val = c.k.strokeFromSetting(setting)
        assert val==result,'Expected %s, Got %s' % (result,val)
#@nonl
#@-node:ekr.20070627082044.830:@test strokeFromSetting
#@+node:ekr.20070627082044.851:@test k.autoCompleterClass.calltip
if g.unitTesting:
    c.beginUpdate()
    try:
        k = c.k ; ac = k.autoCompleter
        w = c.frame.body.bodyCtrl
        ac.widget = w
        s = w.getAllText()
        import string
        # Just test that this doesn't crash.
        for obj in (None,g,string,c,p):
            w.setInsertPoint('end')
            c.k.autoCompleter.calltip(obj=g)
    finally:
        w.setAllText(s)
        p.v.t.bodyString = s
        c.recolor()
        c.endUpdate(False)
    # end:
#@nonl
#@-node:ekr.20070627082044.851:@test k.autoCompleterClass.calltip
#@-node:ekr.20070627082044.827:Unit tests
#@-others
#@-node:ekr.20061031131434:@thin leoKeys.py
#@-leo
