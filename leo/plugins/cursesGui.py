#@+leo-ver=4
#@+node:@file cursesGui.py
#@+at 
#@nonl
# Things not found in the GUI 'interface' classes (in leoFrame.py, leoGui.py, 
# etc)
# are labeled: # undoc: where the AttributeError comes from ; other 
# implementations of method
#@-at
#@@c

#@<< imports >>
#@+node:<< imports >>
import leoGlobals as g
import leoGui
import leoFrame
import leoMenu
import leoNodes

#@-node:<< imports >>
#@nl
#@<< TODO >>
#@+node:<< TODO >>
#@+at
# Body text:
# Is the "signature" of the typing event right?
# What does the InsertPoint do when text is inserted and deleted?
# What does the SelectionRange do, period?
# What about mouse input? What does createBindings() do?
# What does set_focus() do?
# What does the GUI need to do for Leo's undo features?
# What about that minibuffer thing? (I've never used it.)
# When should runMainLoop return?
# What kind of newlines does the body text control get? How should it treat 
# them?
# Headline editing?
# Body text selection.
# (Strip trailing whitespace from this file. :P)
# < < Random cruft >>
# Pay attention to being direct and code-terse.
# Not at all user-friendly.
# Comments in the body reflect current status only.
# Ideally, comments in the body go away as the "leoGUI interface" improves.
# Written on a hundred-column terminal. :S
#@-at
#@nonl
#@-node:<< TODO >>
#@nl
__version__ = '0.1'
#@<< version history >>
#@+node:<< version history >>
#@@nocolor
#@+at
# 
# 0.1: Initial checkin, converted to Leo outline(!) by EKR.
#@-at
#@nonl
#@-node:<< version history >>
#@nl
#@@language python
#@@tabwidth -2

#@+others
#@+node:init
def init ():

    ok = not g.app.gui and not g.app.unitTesting # Not Ok for unit testing!
    
    if ok:
        g.app.gui = textGui()
        g.app.root = g.app.gui.createRootWindow()
        g.app.gui.finishCreate()
        g.plugin_signon(__name__)
        
    elif g.app.gui and not g.app.unitTesting:
        s = "Can't install text gui: previous gui installed"
        g.es_print(s,color="red")
        
    return ok
#@-node:init
#@+node:underline
def underline(s, idx):
  if idx < 0 or idx > len(s) - 1:
    return s
  
  return s[:idx] + '&' + s[idx:]
#@-node:underline
#@+node:class textGui
class textGui(leoGui.leoGui):
  #@	@+others
  #@+node:__init__
  def __init__(self):
    leoGui.leoGui.__init__(self, "text")
    
    self.frames = []
    # TODO leoTkinterFrame finishCreate g.app.windowList.append(f) - use that?
  #@-node:__init__
  #@+node:oops
  def oops(self):
    print "textGui oops", g.callers(), "should be implemented"
  #@-node:oops
  #@+node:createLeoFrame
  def createLeoFrame(self, title):
    ret = textFrame(self, title)
    self.frames.append(ret)
    return ret
  #@-node:createLeoFrame
  #@+node:createRootWindow
  def createRootWindow(self):
    pass # N/A
  
  #@-node:createRootWindow
  #@+node:runMainLoop
  def runMainLoop(self):
    self.text_run()
  #@-node:runMainLoop
  #@+node:isTextWidget
  # undoc: leoKeys masterKeyHandler ; leoGui.mustBeDefinedInSubclasses but not nullGui (!)
  def isTextWidget(self, w):
    # HACK
    return True
  #@-node:isTextWidget
  #@+node:widget_name
  def widget_name(self, w):
    if isinstance(w, textBodyCtrl):
      return 'body'
    return leoGui.leoGui.widget_name(self, w)
  #@-node:widget_name
  #@+node:runOpenFileDialog
  def runOpenFileDialog(self, title, filetypes, defaultextension, multiple=False):
    import os
  
    initialdir = g.app.globalOpenDir or g.os_path_abspath(os.getcwd())
    ret = raw_input("Open which %s file (from %s?) > " % (`filetypes`, initialdir))
    if multiple:
      return [ret,]
    return ret
  #@-node:runOpenFileDialog
  #@+node:finishCreate
  def finishCreate(self):
    pass
  #@-node:finishCreate
  #@+node:text_run
  def text_run(self):
    frame_idx = 0
    
    while True:
      # Frames can come and go.
      if frame_idx > len(self.frames) - 1:
        frame_idx = 0
  
      f = self.frames[frame_idx]
  
      choice = raw_input(f.getTitle() + ': Do what? (menu, key, body, frames, tree) > ')
  
      if choice == 'menu':
        f.menu.text_menu()
      elif choice == 'key':
        f.text_key()
      elif choice == 'body':
        f.body.text_show()
      elif choice == 'frames':
        for i, f in enumerate(self.frames):
          print i, ')', f.getTitle()
        choice = raw_input('Operate on which frame? > ')
        choice = int(choice)
        if choice >= 0 and choice <= len(self.frames) - 1:
          frame_idx = choice
      elif choice == 'tree':
        f.tree.text_draw_tree()
  #@-node:text_run
  #@-others
#@-node:class textGui
#@+node:class textFrame
class textFrame(leoFrame.leoFrame):
  #@	@+others
  #@+node:__init__
  def __init__(self, gui, title):
    leoFrame.leoFrame.__init__(self, gui)
  
    self.title = title # Per leoFrame.__init__
  #@-node:__init__
  #@+node:finishCreate
  # undoc: newLeoCommanderAndFrame -> leoFrame.finishCreate() ; nullFrame 
  def finishCreate(self, c):
    f = self ; f.c = c
  
    f.tree = textTree(self)
    f.body = textBody(frame=self, parentFrame=None)    
    f.log = textLog(frame=self, parentFrame=None)
    f.menu = textLeoMenu(self)
    
    # Yes, this an "official" ivar: this is a kludge.
    f.bodyCtrl = f.body.bodyCtrl
  
    f.createFirstTreeNode()
  
    # (*after* setting self.log)
    c.setLog() # writeWaitingLog hangs without this(!)
    
    # So updateRecentFiles will update our menus.
    g.app.windowList.append(f)
  #@-node:finishCreate
  #@+node:createFirstTreeNode
  # From leoTkinterFrame.py
  def createFirstTreeNode (self):
  
    f = self ; c = f.c
  
    t = leoNodes.tnode()
    v = leoNodes.vnode(t)
    p = leoNodes.position(v,[])
    v.initHeadString("NewHeadline")
    p.moveToRoot(oldRoot=None)
    c.setRootPosition(p) # New in 4.4.2.
    c.editPosition(p)
  #@-node:createFirstTreeNode
  #@+node:setMinibufferBindings
  # undoc: leoKeys.makeAllBindings ; nullFrame 
  def setMinibufferBindings(self):
    self.oops()
  #@-node:setMinibufferBindings
  #@+node:setMinibufferBindings
  def setMinibufferBindings(self):
    pass
  
  def setTopGeometry(self, w, h, x, y):
    pass # N/A
  #@-node:setMinibufferBindings
  #@+node:deiconify
  def deiconify(self): pass # N/A
  def lift(self): pass # N/A
  #@-node:deiconify
  #@+node:update
  def update(self): pass
  def resizePanesToRatio(self, ratio, ratio2): pass # N/A
  #@-node:update
  #@+node:setInitialWindowGeometry
  def setInitialWindowGeometry(self): pass # N/A
  #@-node:setInitialWindowGeometry
  #@+node:text_key
  def text_key(self):
    c = self.c ; k = c.k
    foo = raw_input('Keystroke > ')
    if foo == '': return
  
    class leoTypingEvent:
      def __init__(self, w, ch):
        self.keysym = 427 # What's a keysym?
        self.widget = w 
        self.char = ch
    
    # Leo uses widget_name(event.widget) to decide if a 'default' keystroke belongs
    # to typing in the body text, in the tree control, or whereever. 
    
    e = leoTypingEvent(self.bodyCtrl, foo) # ?
    k.masterKeyHandler(event=e,stroke=foo)
  #@-node:text_key
  #@-others
#@-node:class textFrame
#@+node:class textBody
class textBody(leoFrame.leoBody):
  #@	@+others
  #@+node:__init__
  def __init__(self, frame, parentFrame):
    leoFrame.leoBody.__init__(self, frame, parentFrame)
    
    self.bodyCtrl = textBodyCtrl()
  #@-node:__init__
  #@+node:bind
  # undoc: newLeoCommanderAndFrame -> c.finishCreate -> k.finishCreate -> k.completeAllBindings -> k.makeMasterGuiBinding -> 2156 w.bind ; nullBody 
  def bind(self, bindStroke, callback): 
    # Quiet, please.    
    ##self.oops()
    pass
  #@-node:bind
  #@+node:setEditorColors
  # TODO Tkinter onBodyChanged undo call and many others. =(
  
  def setEditorColors(self, bg, fg): pass # N/A
  def createBindings(self, w=None): pass
  #@-node:setEditorColors
  #@+node:text_show
  def text_show(self):
    print self.bodyCtrl.text, self.bodyCtrl.pos
  #@-node:text_show
  #@-others
#@-node:class textBody
#@+node:class textBodyCtrl
class textBodyCtrl:
  #@	@+others
  #@+node:__init__
  def __init__(self):
    self.pos = 0
  #@-node:__init__
  #@+node:oops
  def oops(self):
    print "textBodyCtrl oops", g.callers(), "should be implemented"
  #@-node:oops
  #@+node:setAllText
  def setAllText(self, s): 
    self.text = s
  #@-node:setAllText
  #@+node:getAllText
  def getAllText(self): 
    return self.text
  #@-node:getAllText
  #@+node:getInsertPoint
  # TODO How should this behave when text is inserted and deleted?  
  def getInsertPoint(self): 
    return self.pos
  #@-node:getInsertPoint
  #@+node:setInsertPoint
  def setInsertPoint(self, pos):
    self.pos = pos
  #@-node:setInsertPoint
  #@+node:seeInsertPoint
  def seeInsertPoint(self): pass # N/A
  
  # TODO ... ?
  #@-node:seeInsertPoint
  #@+node:getSelectionRange
  def getSelectionRange(self): 
    return (self.pos, self.pos,)   
  #@-node:getSelectionRange
  #@+node:setSelectionRange
  def setSelectionRange(self, i, j, insert=None):
    if insert is not None:
      raise NotImplementedError
    if i != j:
      raise NotImplementedError
    self.pos = i
  #@-node:setSelectionRange
  #@+node:insert
  # undoc: selfInsertCommand ; leoTkTextWidget, wxLeoTextWidget
  def insert(self, i, s):
    # TODO Put this fencepost through Leo's unit-tests.
    self.text = self.text[:i] + s + self.text[i:]
  #@-node:insert
  #@+node:toPythonIndex
  # undoc: setMoveCol -> w.toPythonIndex
  def toPythonIndex(self, spot):
    # Um, since we already work in Python indices, or something... ?
    return spot
  #@-node:toPythonIndex
  #@+node:see
  def see(self, index): pass # N/A 
  
  # HACK bringToFront 
  #@-node:see
  #@+node:update_idletasks
  def update_idletasks(self): pass 
  
  #@-node:update_idletasks
  #@+node:bind
  # undoc: leoKeys.py makeMasterGuiBinding ; nullBody
  def bind(self, stroke, callback): pass
  
  #@-node:bind
  #@-others
#@-node:class textBodyCtrl
#@+node:class textMenu
class textMenu:
  #@	@+others
  #@+node:__init__
  def __init__(self):
    self.entries = []
  #@-node:__init__
  #@-others
#@-node:class textMenu
#@+node:class textMenuCascade
class textMenuCascade:
  #@	@+others
  #@+node:__init__
  def __init__(self, menu, label, underline):
    self.menu = menu
    self.label = label
    self.underline = underline
  #@-node:__init__
  #@+node:display
  def display(self):      
    ret = underline(self.label, self.underline)
    if len(self.menu.entries) == 0:
      ret += ' [Submenu with no entries]'
    return ret
  #@-node:display
  #@-others
#@-node:class textMenuCascade
#@+node:class textMenuEntry
class textMenuEntry:
  #@	@+others
  #@+node:__init__
  def __init__(self, label, underline, accel, callback):
    self.label = label
    self.underline = underline
    self.accel = accel
    self.callback = callback
  #@-node:__init__
  #@+node:display
  def display(self):
    return "%s %s" % (underline(self.label, self.underline), self.accel,)
  #@-node:display
  #@-others
#@-node:class textMenuEntry
#@+node:class textMenuSep
class textMenuSep:  
  #@	@+others
  #@+node:display
  def display(self): 
    return '-' * 5
  #@-node:display
  #@-others
#@-node:class textMenuSep
#@+node:class textLeoMenu
class textLeoMenu(leoMenu.leoMenu):
  #@	@+others
  #@+node:createMenuBar
  def createMenuBar(self, frame):
    self._top_menu = textMenu()
    
    self.createMenusFromTables()
  #@-node:createMenuBar
  #@+node:new_menu
  def new_menu(self, parent, tearoff=False):
    if tearoff != False: raise NotImplementedError(`tearoff`)
    
    # I don't know what the 'parent' argument is for; neither does the wx GUI.
    
    return textMenu()
  #@-node:new_menu
  #@+node:add_cascade
  def add_cascade(self, parent, label, menu, underline):    
    if parent == None:
      parent = self._top_menu
    parent.entries.append(textMenuCascade(menu, label, underline,))
  #@-node:add_cascade
  #@+node:add_command
  def add_command(self, menu, label, underline, command, accelerator=''):
    # ?
    # underline - Offset into label. For those who memorised Alt, F, X rather than Alt+F4.
    # accelerator - For display only; these are implemented by Leo's key handling.
  
    menu.entries.append(textMenuEntry(label, underline, accelerator, command))
  #@-node:add_command
  #@+node:add_separator
  def add_separator(self, menu):
    menu.entries.append(textMenuSep())
  #@-node:add_separator
  #@+node:text_menu
  def text_menu(self):
    last_menu = self._top_menu
    
    while True:
      entries = last_menu.entries
  
      for i, entry in enumerate(entries):
        print i, ')', entry.display()
      print len(last_menu.entries), ')', '[Forget it.]'
      
      which = raw_input('Which menu entry? > ')        
      if which.strip() == '': continue
      which = int(which)
      if which == len(entries):
        return
      if which < 0 or which > len(entries) - 1:
        continue
      
      which = entries[which]
      
      if isinstance(which, textMenuEntry):
        which.callback()
        return
      if isinstance(which, textMenuCascade):
        last_menu = which.menu
      else:        
        pass
  #@-node:text_menu
  #@-others
#@-node:class textLeoMenu
#@+node:class textLog
class textLog(leoFrame.leoLog):
	# undoc: leoKeys.py makeAllBindings c.frame.log.setTabBindings('Log') ; nullLog 
  #@	@+others
  #@+node:setTabBindings
  def setTabBindings(self, tabName):
    pass  
  #@-node:setTabBindings
  #@+node:put
  def put(self, s, color=None, tabName='log'):
    print s, # no newline
  #@-node:put
  #@+node:putnl
  def putnl(self, tabName='log'):
    print
  #@-node:putnl
  #@+node:createControl
  # < < HACK Quiet, oops. >>
  def createControl(self, parentFrame): pass
  def setFontFromConfig(self): pass # N/A
  #@-node:createControl
  #@+node:setColorFromConfig
  def setColorFromConfig(self): pass
  
  #@-node:setColorFromConfig
  #@-others
#@-node:class textLog
#@+node:class textTree
class textTree(leoFrame.leoTree):
	# undoc: k.makeAllBindings ; nullTree 
  #@	@+others
  #@+node:setBindings
  def setBindings(self):
    pass
  #@-node:setBindings
  #@+node:beginUpdate
  # undoc: leoCommand beginUpdate c.frame.tree.beginUpdate() ; nullTree
  def beginUpdate(self): pass # N/A
  
  # undoc: (only when given file) leoGlobals openWithFileName -> c.endUpdate ; leoFrame.py nullTree 
  #@-node:beginUpdate
  #@+node:endUpdate
  def endUpdate(self, flag, scroll=True): 
    self.oops()
  
    # Print tree; it's changed, after all.
    # (What's flag for?)
    self.text_draw_tree()
  #@-node:endUpdate
  #@+node:__init__
  def __init__(self, frame):
    # undoc: openWithFileName -> treeWantsFocusNow -> c.frame.tree.canvas
    self.canvas = None
    
    leoFrame.leoTree.__init__(self, frame)
  #@-node:__init__
  #@+node:select
  def select(self,p,updateBeadList=True,scroll=True):
    # TODO Much more here: there's four hooks and all sorts of other things called in the TK version. 
      
    c = self.c ; frame = c.frame
    body = w = frame.bodyCtrl
    
    c.setCurrentPosition(p)
    
    # This is also where the body-text control is given the text of the selected node...
    # Always do this.  Otherwise there can be problems with trailing hewlines.
    s = g.toUnicode(p.v.t.bodyString,"utf-8")
    w.setAllText(s)
    # and something to do with undo?
  #@-node:select
  #@+node:editLabel
  def editLabel(self,p,selectAll=False):
    pass # N/A?
  #@-node:editLabel
  #@+node:text_draw_tree
  def text_draw_tree(self):
         
    def recurse(p, indent):
      # From leoTkinterTree.drawTree():
      while p: # Do not use iterator.
        # < < drawNode > >
    
        box = '|'
        if p.hasChildren():
          if p.isExpanded():
            box = '-'
          else:
            box = '+'
                
        # From drawIcon():
        v = p.v
        
        # (Completely obscure format, I know... :S)
        icon = ''
        # From computeIcon():
        if not v.t.hasBody():
          icon += 'b'
        if v.isMarked():
          icon += '|'
        if v.isCloned():
          icon += '@'
        if v.isDirty():
          icon += '*'
        
        print " " * indent * 2, box, icon, p.headString()
        
        if p.isExpanded() and p.hasFirstChild():
          # Must make an additional copy here by calling firstChild.
          recurse(p.firstChild(), indent + 1)
          
        p = p.next()
        
    recurse(self.c.rootPosition(), 0)
  #@-node:text_draw_tree
  #@-others
#@-node:class textTree
#@-others
#@-node:@file cursesGui.py
#@-leo
