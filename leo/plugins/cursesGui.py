#@+leo-ver=4-thin
#@+node:ekr.20061207074949:@thin cursesGui.py
#@+at 
#@nonl
# Things not found in the GUI 'interface' classes (in leoFrame.py, leoGui.py, 
# etc)
# are labeled: # undoc: where the AttributeError comes from ; other 
# implementations of method
#@-at
#@@c

#@<< imports >>
#@+node:ekr.20061207074949.1:<< imports >>
import leoGlobals as g
import leoGui
import leoFrame
import leoMenu
import leoNodes

#@-node:ekr.20061207074949.1:<< imports >>
#@nl
#@<< TODO >>
#@+node:ekr.20061207075428:<< TODO >>
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
#@-node:ekr.20061207075428:<< TODO >>
#@nl
__version__ = '0.1'
#@<< version history >>
#@+node:ekr.20061207081338:<< version history >>
#@@nocolor
#@+at
# 
# 0.1: Initial checkin, converted to Leo outline(!) by EKR.
#@-at
#@nonl
#@-node:ekr.20061207081338:<< version history >>
#@nl
#@@language python
#@@tabwidth -2

#@+others
#@+node:ekr.20061207074949.2:init
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
#@-node:ekr.20061207074949.2:init
#@+node:ekr.20061207074949.44:underline
def underline(s, idx):
  if idx < 0 or idx > len(s) - 1:
    return s

  return s[:idx] + '&' + s[idx:]
#@-node:ekr.20061207074949.44:underline
#@+node:ekr.20061207074949.3:class textGui
class textGui(leoGui.leoGui):
  #@	@+others
  #@+node:ekr.20061207074949.4:__init__
  def __init__(self):
    leoGui.leoGui.__init__(self, "text")

    self.frames = []
    # TODO leoTkinterFrame finishCreate g.app.windowList.append(f) - use that?
  #@-node:ekr.20061207074949.4:__init__
  #@+node:ekr.20061207074949.5:oops
  def oops(self):
    print "textGui oops", g.callers(), "should be implemented"
  #@-node:ekr.20061207074949.5:oops
  #@+node:ekr.20061207074949.6:createLeoFrame
  def createLeoFrame(self, title):
    ret = textFrame(self, title)
    self.frames.append(ret)
    return ret
  #@-node:ekr.20061207074949.6:createLeoFrame
  #@+node:ekr.20061207074949.7:createRootWindow
  def createRootWindow(self):
    pass # N/A

  #@-node:ekr.20061207074949.7:createRootWindow
  #@+node:ekr.20061207074949.8:runMainLoop
  def runMainLoop(self):
    self.text_run()
  #@-node:ekr.20061207074949.8:runMainLoop
  #@+node:ekr.20061207074949.9:isTextWidget
  # undoc: leoKeys masterKeyHandler ; leoGui.mustBeDefinedInSubclasses but not nullGui (!)
  def isTextWidget(self, w):
    # HACK
    return True
  #@-node:ekr.20061207074949.9:isTextWidget
  #@+node:ekr.20061207074949.10:widget_name
  def widget_name(self, w):
    if isinstance(w, textBodyCtrl):
      return 'body'
    return leoGui.leoGui.widget_name(self, w)
  #@-node:ekr.20061207074949.10:widget_name
  #@+node:ekr.20061207074949.11:runOpenFileDialog
  def runOpenFileDialog(self, title, filetypes, defaultextension, multiple=False):
    import os

    initialdir = g.app.globalOpenDir or g.os_path_abspath(os.getcwd())
    ret = raw_input("Open which %s file (from %s?) > " % (`filetypes`, initialdir))
    if multiple:
      return [ret,]
    return ret
  #@-node:ekr.20061207074949.11:runOpenFileDialog
  #@+node:ekr.20061207074949.12:finishCreate
  def finishCreate(self):
    pass
  #@-node:ekr.20061207074949.12:finishCreate
  #@+node:ekr.20061207074949.13:text_run
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
  #@-node:ekr.20061207074949.13:text_run
  #@-others
#@-node:ekr.20061207074949.3:class textGui
#@+node:ekr.20061207074949.14:class textFrame
class textFrame(leoFrame.leoFrame):
  #@	@+others
  #@+node:ekr.20061207074949.15:__init__
  def __init__(self, gui, title):
    leoFrame.leoFrame.__init__(self, gui)

    self.title = title # Per leoFrame.__init__
  #@-node:ekr.20061207074949.15:__init__
  #@+node:ekr.20061207074949.16:finishCreate
  # undoc: newLeoCommanderAndFrame -> leoFrame.finishCreate() ; nullFrame 
  def finishCreate(self, c):
    f = self ; f.c = c

    f.tree = textTree(self)
    f.body = textBody(frame=self, parentFrame=None)    
    f.log = textLog(frame=self, parentFrame=None)
    f.menu = textLeoMenu(self)

    f.createFirstTreeNode()

    # (*after* setting self.log)
    c.setLog() # writeWaitingLog hangs without this(!)

    # So updateRecentFiles will update our menus.
    g.app.windowList.append(f)
  #@-node:ekr.20061207074949.16:finishCreate
  #@+node:ekr.20061207074949.17:createFirstTreeNode
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
  #@-node:ekr.20061207074949.17:createFirstTreeNode
  #@+node:ekr.20061207074949.18:setMinibufferBindings
  # undoc: leoKeys.makeAllBindings ; nullFrame 
  def setMinibufferBindings(self):
    self.oops()
  #@-node:ekr.20061207074949.18:setMinibufferBindings
  #@+node:ekr.20061207074949.19:setMinibufferBindings
  def setMinibufferBindings(self):
    pass

  def setTopGeometry(self, w, h, x, y):
    pass # N/A
  #@-node:ekr.20061207074949.19:setMinibufferBindings
  #@+node:ekr.20061207074949.20:deiconify
  def deiconify(self): pass # N/A
  def lift(self): pass # N/A
  #@-node:ekr.20061207074949.20:deiconify
  #@+node:ekr.20061207074949.21:update
  def update(self): pass
  def resizePanesToRatio(self, ratio, ratio2): pass # N/A
  #@-node:ekr.20061207074949.21:update
  #@+node:ekr.20061207074949.22:setInitialWindowGeometry
  def setInitialWindowGeometry(self): pass # N/A
  #@-node:ekr.20061207074949.22:setInitialWindowGeometry
  #@+node:ekr.20061207074949.23:text_key
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
  #@-node:ekr.20061207074949.23:text_key
  #@-others
#@-node:ekr.20061207074949.14:class textFrame
#@+node:ekr.20061207074949.24:class textBody
class textBody(leoFrame.leoBody):
  #@	@+others
  #@+node:ekr.20061207074949.25:__init__
  def __init__(self, frame, parentFrame):
    leoFrame.leoBody.__init__(self, frame, parentFrame)

    self.bodyCtrl = textBodyCtrl()
  #@-node:ekr.20061207074949.25:__init__
  #@+node:ekr.20061207074949.26:bind
  # undoc: newLeoCommanderAndFrame -> c.finishCreate -> k.finishCreate -> k.completeAllBindings -> k.makeMasterGuiBinding -> 2156 w.bind ; nullBody 
  def bind(self, bindStroke, callback): 
    # Quiet, please.    
    ##self.oops()
    pass
  #@-node:ekr.20061207074949.26:bind
  #@+node:ekr.20061207074949.27:setEditorColors
  # TODO Tkinter onBodyChanged undo call and many others. =(

  def setEditorColors(self, bg, fg): pass # N/A
  def createBindings(self, w=None): pass
  #@-node:ekr.20061207074949.27:setEditorColors
  #@+node:ekr.20061207074949.28:text_show
  def text_show(self):
    print self.bodyCtrl.text, self.bodyCtrl.pos
  #@-node:ekr.20061207074949.28:text_show
  #@-others
#@-node:ekr.20061207074949.24:class textBody
#@+node:ekr.20061207074949.29:class textBodyCtrl
class textBodyCtrl:
  #@	@+others
  #@+node:ekr.20061207074949.30:__init__
  def __init__(self):
    self.pos = 0
  #@-node:ekr.20061207074949.30:__init__
  #@+node:ekr.20061207074949.31:oops
  def oops(self):
    print "textBodyCtrl oops", g.callers(), "should be implemented"
  #@-node:ekr.20061207074949.31:oops
  #@+node:ekr.20061207074949.32:setAllText
  def setAllText(self, s): 
    self.text = s
  #@-node:ekr.20061207074949.32:setAllText
  #@+node:ekr.20061207074949.33:getAllText
  def getAllText(self): 
    return self.text
  #@-node:ekr.20061207074949.33:getAllText
  #@+node:ekr.20061207074949.34:getInsertPoint
  # TODO How should this behave when text is inserted and deleted?  
  def getInsertPoint(self): 
    return self.pos
  #@-node:ekr.20061207074949.34:getInsertPoint
  #@+node:ekr.20061207074949.35:setInsertPoint
  def setInsertPoint(self, pos):
    self.pos = pos
  #@-node:ekr.20061207074949.35:setInsertPoint
  #@+node:ekr.20061207074949.36:seeInsertPoint
  def seeInsertPoint(self): pass # N/A

  # TODO ... ?
  #@-node:ekr.20061207074949.36:seeInsertPoint
  #@+node:ekr.20061207074949.37:getSelectionRange
  def getSelectionRange(self): 
    return (self.pos, self.pos,)   
  #@-node:ekr.20061207074949.37:getSelectionRange
  #@+node:ekr.20061207074949.38:setSelectionRange
  def setSelectionRange(self, i, j, insert=None):
    if insert is not None:
      raise NotImplementedError
    if i != j:
      raise NotImplementedError
    self.pos = i
  #@-node:ekr.20061207074949.38:setSelectionRange
  #@+node:ekr.20061207074949.39:insert
  # undoc: selfInsertCommand ; leoTkTextWidget, wxLeoTextWidget
  def insert(self, i, s):
    # TODO Put this fencepost through Leo's unit-tests.
    self.text = self.text[:i] + s + self.text[i:]
  #@-node:ekr.20061207074949.39:insert
  #@+node:ekr.20061207074949.40:toPythonIndex
  # undoc: setMoveCol -> w.toPythonIndex
  def toPythonIndex(self, spot):
    # Um, since we already work in Python indices, or something... ?
    return spot
  #@-node:ekr.20061207074949.40:toPythonIndex
  #@+node:ekr.20061207074949.41:see
  def see(self, index): pass # N/A 

  # HACK bringToFront 
  #@-node:ekr.20061207074949.41:see
  #@+node:ekr.20061207074949.42:update_idletasks
  def update_idletasks(self): pass 

  #@-node:ekr.20061207074949.42:update_idletasks
  #@+node:ekr.20061207074949.43:bind
  # undoc: leoKeys.py makeMasterGuiBinding ; nullBody
  def bind(self, stroke, callback): pass

  #@-node:ekr.20061207074949.43:bind
  #@-others
#@-node:ekr.20061207074949.29:class textBodyCtrl
#@+node:ekr.20061207074949.45:class textMenu
class textMenu:
  #@	@+others
  #@+node:ekr.20061207074949.46:__init__
  def __init__(self):
    self.entries = []
  #@-node:ekr.20061207074949.46:__init__
  #@-others
#@-node:ekr.20061207074949.45:class textMenu
#@+node:ekr.20061207074949.47:class textMenuCascade
class textMenuCascade:
  #@	@+others
  #@+node:ekr.20061207074949.48:__init__
  def __init__(self, menu, label, underline):
    self.menu = menu
    self.label = label
    self.underline = underline
  #@-node:ekr.20061207074949.48:__init__
  #@+node:ekr.20061207074949.49:display
  def display(self):      
    ret = underline(self.label, self.underline)
    if len(self.menu.entries) == 0:
      ret += ' [Submenu with no entries]'
    return ret
  #@-node:ekr.20061207074949.49:display
  #@-others
#@-node:ekr.20061207074949.47:class textMenuCascade
#@+node:ekr.20061207074949.50:class textMenuEntry
class textMenuEntry:
  #@	@+others
  #@+node:ekr.20061207074949.51:__init__
  def __init__(self, label, underline, accel, callback):
    self.label = label
    self.underline = underline
    self.accel = accel
    self.callback = callback
  #@-node:ekr.20061207074949.51:__init__
  #@+node:ekr.20061207074949.52:display
  def display(self):
    return "%s %s" % (underline(self.label, self.underline), self.accel,)
  #@-node:ekr.20061207074949.52:display
  #@-others
#@-node:ekr.20061207074949.50:class textMenuEntry
#@+node:ekr.20061207074949.53:class textMenuSep
class textMenuSep:  
  #@	@+others
  #@+node:ekr.20061207074949.54:display
  def display(self): 
    return '-' * 5
  #@-node:ekr.20061207074949.54:display
  #@-others
#@-node:ekr.20061207074949.53:class textMenuSep
#@+node:ekr.20061207074949.55:class textLeoMenu
class textLeoMenu(leoMenu.leoMenu):
  #@	@+others
  #@+node:ekr.20061207074949.56:createMenuBar
  def createMenuBar(self, frame):
    self._top_menu = textMenu()

    self.createMenusFromTables()
  #@-node:ekr.20061207074949.56:createMenuBar
  #@+node:ekr.20061207074949.57:new_menu
  def new_menu(self, parent, tearoff=False):
    if tearoff != False: raise NotImplementedError(`tearoff`)

    # I don't know what the 'parent' argument is for; neither does the wx GUI.

    return textMenu()
  #@-node:ekr.20061207074949.57:new_menu
  #@+node:ekr.20061207074949.58:add_cascade
  def add_cascade(self, parent, label, menu, underline):    
    if parent == None:
      parent = self._top_menu
    parent.entries.append(textMenuCascade(menu, label, underline,))
  #@-node:ekr.20061207074949.58:add_cascade
  #@+node:ekr.20061207074949.59:add_command
  def add_command(self, menu, label, underline, command, accelerator=''):
    # ?
    # underline - Offset into label. For those who memorised Alt, F, X rather than Alt+F4.
    # accelerator - For display only; these are implemented by Leo's key handling.

    menu.entries.append(textMenuEntry(label, underline, accelerator, command))
  #@-node:ekr.20061207074949.59:add_command
  #@+node:ekr.20061207074949.60:add_separator
  def add_separator(self, menu):
    menu.entries.append(textMenuSep())
  #@-node:ekr.20061207074949.60:add_separator
  #@+node:ekr.20061207074949.61:text_menu
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
  #@-node:ekr.20061207074949.61:text_menu
  #@-others
#@-node:ekr.20061207074949.55:class textLeoMenu
#@+node:ekr.20061207074949.62:class textLog
class textLog(leoFrame.leoLog):
	# undoc: leoKeys.py makeAllBindings c.frame.log.setTabBindings('Log') ; nullLog 
  #@	@+others
  #@+node:ekr.20061207074949.64:setTabBindings
  def setTabBindings(self, tabName):
    pass  
  #@-node:ekr.20061207074949.64:setTabBindings
  #@+node:ekr.20061207074949.65:put
  def put(self, s, color=None, tabName='log'):
    print s, # no newline
  #@-node:ekr.20061207074949.65:put
  #@+node:ekr.20061207074949.66:putnl
  def putnl(self, tabName='log'):
    print
  #@-node:ekr.20061207074949.66:putnl
  #@+node:ekr.20061207074949.67:createControl
  # < < HACK Quiet, oops. >>
  def createControl(self, parentFrame): pass
  def setFontFromConfig(self): pass # N/A
  #@-node:ekr.20061207074949.67:createControl
  #@+node:ekr.20061207074949.68:setColorFromConfig
  def setColorFromConfig(self): pass

  #@-node:ekr.20061207074949.68:setColorFromConfig
  #@-others
#@-node:ekr.20061207074949.62:class textLog
#@+node:ekr.20061207074949.69:class textTree
class textTree(leoFrame.leoTree):
	# undoc: k.makeAllBindings ; nullTree 
  #@	@+others
  #@+node:ekr.20061207074949.71:setBindings
  def setBindings(self):
    pass
  #@-node:ekr.20061207074949.71:setBindings
  #@+node:ekr.20061207074949.72:beginUpdate
  # undoc: leoCommand beginUpdate c.frame.tree.beginUpdate() ; nullTree
  def beginUpdate(self): pass # N/A

  # undoc: (only when given file) leoGlobals openWithFileName -> c.endUpdate ; leoFrame.py nullTree 
  #@-node:ekr.20061207074949.72:beginUpdate
  #@+node:ekr.20061207074949.73:endUpdate
  def endUpdate(self, flag, scroll=True): 
    self.oops()

    # Print tree; it's changed, after all.
    # (What's flag for?)
    self.text_draw_tree()
  #@-node:ekr.20061207074949.73:endUpdate
  #@+node:ekr.20061207074949.74:__init__
  def __init__(self, frame):
    # undoc: openWithFileName -> treeWantsFocusNow -> c.frame.tree.canvas
    self.canvas = None

    leoFrame.leoTree.__init__(self, frame)
  #@-node:ekr.20061207074949.74:__init__
  #@+node:ekr.20061207074949.75:select
  def select(self,p,updateBeadList=True,scroll=True):
    # TODO Much more here: there's four hooks and all sorts of other things called in the TK version. 

    c = self.c ; frame = c.frame
    body = w = c.frame.body.bodyCtrl

    c.setCurrentPosition(p)

    # This is also where the body-text control is given the text of the selected node...
    # Always do this.  Otherwise there can be problems with trailing hewlines.
    s = g.toUnicode(p.v.t.bodyString,"utf-8")
    w.setAllText(s)
    # and something to do with undo?
  #@-node:ekr.20061207074949.75:select
  #@+node:ekr.20061207074949.76:editLabel
  def editLabel(self,p,selectAll=False):
    pass # N/A?
  #@-node:ekr.20061207074949.76:editLabel
  #@+node:ekr.20061207074949.77:text_draw_tree
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
  #@-node:ekr.20061207074949.77:text_draw_tree
  #@-others
#@-node:ekr.20061207074949.69:class textTree
#@-others
#@-node:ekr.20061207074949:@thin cursesGui.py
#@-leo
