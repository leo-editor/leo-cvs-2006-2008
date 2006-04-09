#@+leo-ver=4-thin
#@+node:ekr.20040108062655:@thin nodenavigator.py
"""Add "Recent" and "Marks" pulldown buttons to the toolbar."""

#@@language python
#@@tabwidth -4

__name__ = "Node Navigator"
__version__ = "0.10"

#@<< version history >>
#@+node:ekr.20040908093511.2:<< version history >>
#@+at
# 
# 0.4 EKR:
# - Rewrote to handle multiple commanders correctly.
# - Created ctor, set hooks on "new" and "open2".
# - Saved marks so we don't have to rescan:  a major performance boost.
#   This was slowing down write logic considerably.
# - Added basic unit testing.
# 
# 0.5 EKR:
# - Use constant spacing for buttons on MacOs/darwin.
# 
# 0.6 EKR:
# - Create a separate Navigator instance for each open window.
#     This eliminates problems when multiple windows are open.
# - Limit size of recent menu to 25 entries.
# - Limit width of entries to 40 characters.
# 
# 0.7 EKR, following suggestions of Bernhard Mulder.
# - Fix problems with initialization:
#     - Bind onCreate to the "open2" hook.
#     - Set c = keywords.get("new_c") in onCreate.
# 0.8 EKR:
#     - Changed 'new_c' logic to 'c' logic.
#     - Added init function.
# 0.9 EKR:
#     - Make sure buttons appear in a new window.
# 0.10 EKR:
#     - Make sure self.c == keywords.get('c') in all hook handlers.
#@-at
#@nonl
#@-node:ekr.20040908093511.2:<< version history >>
#@nl
#@<< imports >>
#@+node:ekr.20040908094021.1:<< imports >>
import leoGlobals as g
import leoPlugins

Tk = g.importExtension('Tkinter',pluginName=__name__,verbose=True)

import sys
#@nonl
#@-node:ekr.20040908094021.1:<< imports >>
#@nl

# Set this to 0 if the sizing of the toolbar controls doesn't look good on your platform. 
USE_FIXED_SIZES = sys.platform != "darwin"

#@+others
#@+node:ekr.20050311090939.4:init
def init ():
    
    ok = Tk is not None # OK for unit testing.
    
    if ok:
        if g.app.gui is None:
            g.app.createTkGui(__file__)
    
        if g.app.gui.guiName() == "tkinter":
            leoPlugins.registerHandler(('new','open2'), onCreate)
            g.plugin_signon("nodenavigator")
    
    return ok
#@nonl
#@-node:ekr.20050311090939.4:init
#@+node:ekr.20040909132810:onCreate
def onCreate(tag, keywords):
    
    # Not ok for unit testing: can't use unitTestGui.
    if g.app.unitTesting:
        return

    c = keywords.get("c")
    nav = Navigator(c)
    nav.addWidgets()

    leoPlugins.registerHandler("set-mark",nav.addMark)
    leoPlugins.registerHandler("clear-mark",nav.clearMark)
    leoPlugins.registerHandler("select3",nav.updateRecent)
#@nonl
#@-node:ekr.20040909132810:onCreate
#@+node:ekr.20040108062655.2:class Navigator
class Navigator:
    
    """A node navigation aid for Leo"""

    #@    @+others
    #@+node:ekr.20040801062218:__init__
    def __init__ (self,c):
        
        self.c = c
        self.inited = False
        self.markLists = {}
            # Keys are commanders, values are lists of marked tnodes.
        self.marksMenus = {}
            # Keys are commanders, values are marks menus.
        self.recentMenus = {}
            # Keys are commanders, values are recent menus.
    #@nonl
    #@-node:ekr.20040801062218:__init__
    #@+node:ekr.20040108062655.4:_getSizer
    def _getSizer(self, parent, height, width):
    
        """Return a sizer object to force a Tk widget to be the right size"""
    
        if USE_FIXED_SIZES: 
            sizer = Tk.Frame(parent,height=height,width=width) 
            sizer.pack_propagate(0) # don't shrink 
            sizer.pack(side="right") 
            return sizer 
        else: 
            return parent 
    #@nonl
    #@-node:ekr.20040108062655.4:_getSizer
    #@+node:ekr.20040108062655.6:addMark
    def addMark(self, tag, keywords):
    
        """Add a mark to the marks list"""
    
        c = keywords.get("c")
        p = keywords.get("p")
        if c != self.c or not p: return
    
        marks = self.markLists.get(c,[])
        if p.v.t in marks: return
    
        menu = self.marksMenus.get(c)
        if menu is None: return
        menu = menu["menu"]
    
        def callback(event=None,self=self,c=c,p=p.copy()):
            self.select(c,p)
    
        name = p.headString().strip()
        menu.add_command(label=name[:40],command=callback)
        marks.append(p.v.t)
    
        # Unlike the recent menu, which gets recreated each time, we remember the marks.
        self.markLists[c] = marks
    #@nonl
    #@-node:ekr.20040108062655.6:addMark
    #@+node:ekr.20040108062655.3:addWidgets
    def addWidgets(self):
    
        """Add the widgets to the navigation bar"""
    
        c = self.c
        # Create the main container.
        self.frame = Tk.Frame(c.frame.iconFrame)
        self.frame.pack(side="left")
        # Create the two menus.
        menus = []
        for (name,side) in (("Marks","right"),("Recent","left")):
            args = [name]
            val = Tk.StringVar() 
            menu = Tk.OptionMenu(self._getSizer(self.frame,29,70),val,*args)
            val.set(name) 
            menu.pack(side=side,fill="both",expand=1)
            menus.append(menu)
        self.marksMenus[c] = menus[0]
        self.recentMenus[c] = menus[1]
        # Update the menus.
        self.updateRecent("tag",{"c":c})
        self.initMarks("tag",{"c":c})
    #@nonl
    #@-node:ekr.20040108062655.3:addWidgets
    #@+node:ekr.20040730092357:initMarks
    def initMarks(self, tag, keywords):
    
        """Initialize the marks list."""
    
        c = keywords.get("c")
        if c != self.c: return
    
        # Clear old marks menu
        menu = self.marksMenus.get(c)
        if menu is None: return
    
        menu = menu["menu"]
        menu.delete(0,"end")
    
        # Find all marked nodes. We only do this once!
        marks = self.markLists.get(c,[])
        for p in c.all_positions_iter():
            if p.isMarked() and p.v.t not in marks:
                def callback(event=None,self=self,c=c,p=p.copy()):
                    self.select(c,p)
                name = p.headString().strip()
                menu.add_command(label=name,command=callback)
                marks.append(p.v.t)
        self.markLists[c] = marks
    #@nonl
    #@-node:ekr.20040730092357:initMarks
    #@+node:ekr.20040730093250:clearMark
    def clearMark(self, tag, keywords):
    
        """Remove a mark to the marks list"""
    
        c = keywords.get("c")
        p = keywords.get("p")
        if c != self.c or not p: return
    
        marks = self.markLists.get(c,[])
        if not p.v.t in marks: return
    
        menu = self.marksMenus.get(c)
        if menu is None: return # This should never happen.
        menu = menu["menu"]
    
        name = p.headString().strip()
        try:
            # 9/7/04: The headline may be in the process of being changed.
            # If so, there is no way to clear the old entry.
            menu.delete(name)
        except Tk.TclError:
            pass
        marks.remove(p.v.t)
    
        # Unlike the recent menu, which gets recreated each time, we remember the marks.
        self.markLists[c] = marks
    #@nonl
    #@-node:ekr.20040730093250:clearMark
    #@+node:ekr.20040730094103:select
    def select(self,c,p):
    
        """Callback that selects position p."""
    
        if p.exists(c):
            c.beginUpdate()
            c.frame.tree.expandAllAncestors(p)
            c.selectPosition(p)
            c.endUpdate()
    #@nonl
    #@-node:ekr.20040730094103:select
    #@+node:ekr.20040108091136:updateRecent
    def updateRecent(self,tag,keywords):
    
        """Add all entries to the recent nodes list."""
    
        c = keywords.get("c")
        if c != self.c: return
    
        # Clear old recent menu
        menu = self.recentMenus.get(c)
        if not menu: return
    
        menu = menu["menu"]
        menu.delete(0,"end")
    
        for p in c.visitedList[:25]:
            if p.exists(c):
                def callback(event=None,self=self,c=c,p=p):
                    self.select(c,p)
                menu.add_command(label=p.headString()[:40],command=callback)
    #@nonl
    #@-node:ekr.20040108091136:updateRecent
    #@-others
#@-node:ekr.20040108062655.2:class Navigator
#@-others
#@nonl
#@-node:ekr.20040108062655:@thin nodenavigator.py
#@-leo
