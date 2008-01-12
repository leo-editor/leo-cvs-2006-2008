# -*- coding: utf-8 -*-
#@+leo-ver=4-thin
#@+node:ekr.20080112145409.53:@thin leoGtkFrame.py
#@@first

#@@language python
#@@tabwidth -4
#@@pagewidth 80

#@<< imports >>
#@+node:ekr.20080112145409.54:<< imports >>
import leoGlobals as g

import leoChapters
import leoColor
import leoFrame
import leoKeys
import leoMenu
import leoNodes

import javax.gtk as gtk
import java.awt as awt
import java.lang

import os
import string
import sys

# # The following imports _are_ used.
# __pychecker__ = '--no-import'
# import threading
# import time
#@-node:ekr.20080112145409.54:<< imports >>
#@nl

#@+others
#@+node:ekr.20080112145409.55:class leoGtkFrame
class leoGtkFrame (leoFrame.leoFrame):

    #@    @+others
    #@+node:ekr.20080112145409.56: Birth & Death (gtkFrame)
    #@+node:ekr.20080112145409.57:__init__ (gtkFrame)
    def __init__(self,title,gui):

        g.trace('gtkFrame',g.callers(20))

        # Init the base class.
        leoFrame.leoFrame.__init__(self,gui)

        self.use_chapters = False ###

        self.title = title

        leoGtkFrame.instances += 1

        self.c = None # Set in finishCreate.
        self.iconBarClass = self.gtkIconBarClass
        self.statusLineClass = self.gtkStatusLineClass
        self.iconBar = None

        self.trace_status_line = None # Set in finishCreate.

        #@    << set the leoGtkFrame ivars >>
        #@+node:ekr.20080112145409.58:<< set the leoGtkFrame ivars >> (removed frame.bodyCtrl ivar)
        # "Official ivars created in createLeoFrame and its allies.
        self.bar1 = None
        self.bar2 = None
        self.body = None
        self.f1 = self.f2 = None
        self.findPanel = None # Inited when first opened.
        self.iconBarComponentName = 'iconBar'
        self.iconFrame = None 
        self.log = None
        self.canvas = None
        self.outerFrame = None
        self.statusFrame = None
        self.statusLineComponentName = 'statusLine'
        self.statusText = None 
        self.statusLabel = None 
        self.top = None
        self.tree = None
        # self.treeBar = None # Replaced by injected frame.canvas.leo_treeBar.

        # Used by event handlers...
        self.controlKeyIsDown = False # For control-drags
        self.draggedItem = None
        self.isActive = True
        self.redrawCount = 0
        self.wantedWidget = None
        self.wantedCallbackScheduled = False
        self.scrollWay = None
        #@-node:ekr.20080112145409.58:<< set the leoGtkFrame ivars >> (removed frame.bodyCtrl ivar)
        #@nl
    #@-node:ekr.20080112145409.57:__init__ (gtkFrame)
    #@+node:ekr.20080112145409.59:__repr__ (gtkFrame)
    def __repr__ (self):

        return "<leoGtkFrame: %s>" % self.title
    #@-node:ekr.20080112145409.59:__repr__ (gtkFrame)
    #@+node:ekr.20080112145409.60:gtkFrame.finishCreate & helpers
    def finishCreate (self,c):

        f = self ; f.c = c
        g.trace('gtkFrame')

        self.trace_status_line = c.config.getBool('trace_status_line')
        self.use_chapters      = False and c.config.getBool('use_chapters') ###
        self.use_chapter_tabs  = False and c.config.getBool('use_chapter_tabs') ###

        # This must be done after creating the commander.
        f.splitVerticalFlag,f.ratio,f.secondary_ratio = f.initialRatios()

        f.createOuterFrames()

        ### f.createIconBar()

        f.createSplitterComponents()

        ### f.createStatusLine()
        f.createFirstTreeNode()
        f.menu = leoGtkMenu(f)
            # c.finishCreate calls f.createMenuBar later.
        c.setLog()
        g.app.windowList.append(f)
        c.initVersion()
        c.signOnWithVersion()
        f.miniBufferWidget = f.createMiniBufferWidget()
        c.bodyWantsFocusNow()
    #@+node:ekr.20080112145409.61:createOuterFrames
    def createOuterFrames (self):


        f = self ; c = f.c
        ### f.top = top = Tk.Toplevel()
        ### g.app.gui.attachLeoIcon(top)
        ### top.title(f.title)
        ### top.minsize(30,10) # In grid units.

        def exit(event):
            java.lang.System.exit(0)

        # def onButtonPressed(event):
            # field.text=quotes[event.source.text]

        # def createButton(name):
            # return gtk.JButton(name,preferredSize=(100,20),
                # actionPerformed=onButtonPressed)

        f.top = w = gtk.JFrame('jyLeo!',size=(700,700),windowClosing=exit)
        w.contentPane.layout = awt.FlowLayout()

        # if g.os_path_exists(g.app.user_xresources_path):
            # f.top.option_readfile(g.app.user_xresources_path)

        # f.top.protocol("WM_DELETE_WINDOW", f.OnCloseLeoEvent)
        # f.top.bind("<Button-1>", f.OnActivateLeoEvent)

        # f.top.bind("<Control-KeyPress>",f.OnControlKeyDown)
        # f.top.bind("<Control-KeyRelease>",f.OnControlKeyUp)

        # These don't work on Windows. Because of bugs in window managers,
        # there is NO WAY to know which window is on top!
        # f.top.bind("<Activate>",f.OnActivateLeoEvent)
        # f.top.bind("<Deactivate>",f.OnDeactivateLeoEvent)

        # Create the outer frame, the 'hull' component.
        # f.outerFrame = Tk.Frame(top)
        # f.outerFrame.pack(expand=1,fill="both")
    #@-node:ekr.20080112145409.61:createOuterFrames
    #@+node:ekr.20080112145409.62:createSplitterComponents (removed frame.bodyCtrl ivar)
    def createSplitterComponents (self):

        f = self ; c = f.c

        g.trace()

        f.createLeoSplitters(f.outerFrame)

        if 0:
            # Create the canvas, tree, log and body.
            if f.use_chapters:
                c.chapterController = cc = leoChapters.chapterController(c)

            if self.use_chapters and self.use_chapter_tabs:
                cc.tt = leoGtkTreeTab(c,f.split2Pane1,cc)

            f.canvas = f.createCanvas(f.split2Pane1)
            f.tree   = leoGtkTree.leoGtkTree(c,f,f.canvas)
            f.log    = leoGtkLog(f,f.split2Pane2)
            f.body   = leoGtkBody(f,f.split1Pane2)

        f.body = leoGtkBody(f,f.top)
        f.tree = leoGtkTree(c,f,f.top)
        f.log  = leoGtkLog(f,f.top)

        # Configure.
        f.setTabWidth(c.tab_width)
        f.reconfigurePanes()
        f.body.setFontFromConfig()
        f.body.setColorFromConfig()
    #@-node:ekr.20080112145409.62:createSplitterComponents (removed frame.bodyCtrl ivar)
    #@+node:ekr.20080112145409.63:createFirstTreeNode
    def createFirstTreeNode (self):

        f = self ; c = f.c

        t = leoNodes.tnode()
        v = leoNodes.vnode(t)
        p = leoNodes.position(v,[])
        v.initHeadString("NewHeadline")
        p.moveToRoot(oldRoot=None)
        c.setRootPosition(p) # New in 4.4.2.
        c.editPosition(p)
    #@-node:ekr.20080112145409.63:createFirstTreeNode
    #@-node:ekr.20080112145409.60:gtkFrame.finishCreate & helpers
    #@+node:ekr.20080112145409.64:gtkFrame.createCanvas & helpers
    def createCanvas (self,parentFrame,pack=True):

        c = self.c

        scrolls = c.config.getBool('outline_pane_scrolls_horizontally')
        scrolls = g.choose(scrolls,1,0)
        canvas = self.createTkTreeCanvas(parentFrame,scrolls,pack)
        self.setCanvasColorFromConfig(canvas)

        return canvas
    #@nonl
    #@+node:ekr.20080112145409.65:f.createTkTreeCanvas & callbacks
    def createTkTreeCanvas (self,parentFrame,scrolls,pack):

        frame = self

        canvas = Tk.Canvas(parentFrame,name="canvas",
            bd=0,bg="white",relief="flat")

        treeBar = Tk.Scrollbar(parentFrame,name="treeBar")

        # New in Leo 4.4.3 b1: inject the ivar into the canvas.
        canvas.leo_treeBar = treeBar

        # Bind mouse wheel event to canvas
        if sys.platform != "win32": # Works on 98, crashes on XP.
            canvas.bind("<MouseWheel>", frame.OnMouseWheel)
            if 1: # New in 4.3.
                #@            << workaround for mouse-wheel problems >>
                #@+node:ekr.20080112145409.66:<< workaround for mouse-wheel problems >>
                # Handle mapping of mouse-wheel to buttons 4 and 5.

                def mapWheel(e):
                    if e.num == 4: # Button 4
                        e.delta = 120
                        return frame.OnMouseWheel(e)
                    elif e.num == 5: # Button 5
                        e.delta = -120
                        return frame.OnMouseWheel(e)

                canvas.bind("<ButtonPress>",mapWheel,add=1)
                #@-node:ekr.20080112145409.66:<< workaround for mouse-wheel problems >>
                #@nl

        canvas['yscrollcommand'] = self.setCallback
        treeBar['command']     = self.yviewCallback
        treeBar.pack(side="right", fill="y")
        if scrolls: 
            treeXBar = Tk.Scrollbar( 
                parentFrame,name='treeXBar',orient="horizontal") 
            canvas['xscrollcommand'] = treeXBar.set 
            treeXBar['command'] = canvas.xview 
            treeXBar.pack(side="bottom", fill="x")

        if pack:
            canvas.pack(expand=1,fill="both")

        canvas.bind("<Button-1>", frame.OnActivateTree)

        # Handle mouse wheel in the outline pane.
        if sys.platform == "linux2": # This crashes tcl83.dll
            canvas.bind("<MouseWheel>", frame.OnMouseWheel)
        if 0:
            #@        << do scrolling by hand in a separate thread >>
            #@+node:ekr.20080112145409.67:<< do scrolling by hand in a separate thread >>
            # New in 4.3: replaced global way with scrollWay ivar.
            ev = threading.Event()

            def run(self=self,canvas=canvas,ev=ev):

                while 1:
                    ev.wait()
                    if self.scrollWay =='Down': canvas.yview("scroll", 1,"units")
                    else:                       canvas.yview("scroll",-1,"units")
                    time.sleep(.1)

            t = threading.Thread(target = run)
            t.setDaemon(True)
            t.start()

            def scrollUp(event): scrollUpOrDown(event,'Down')
            def scrollDn(event): scrollUpOrDown(event,'Up')

            def scrollUpOrDown(event,theWay):
                if event.widget!=canvas: return
                if 0: # This seems to interfere with scrolling.
                    if canvas.find_overlapping(event.x,event.y,event.x,event.y): return
                ev.set()
                self.scrollWay = theWay

            def off(event,ev=ev,canvas=canvas):
                if event.widget!=canvas: return
                ev.clear()

            if 1: # Use shift-click
                # Shift-button-1 scrolls up, Shift-button-2 scrolls down
                canvas.bind_all('<Shift Button-3>',scrollDn)
                canvas.bind_all('<Shift Button-1>',scrollUp)
                canvas.bind_all('<Shift ButtonRelease-1>',off)
                canvas.bind_all('<Shift ButtonRelease-3>',off)
            else: # Use plain click.
                canvas.bind_all( '<Button-3>',scrollDn)
                canvas.bind_all( '<Button-1>',scrollUp)
                canvas.bind_all( '<ButtonRelease-1>',off)
                canvas.bind_all( '<ButtonRelease-3>',off)
            #@-node:ekr.20080112145409.67:<< do scrolling by hand in a separate thread >>
            #@nl

        # g.print_bindings("canvas",canvas)
        return canvas
    #@+node:ekr.20080112145409.68:Scrolling callbacks (gtkFrame)
    def setCallback (self,*args,**keys):

        """Callback to adjust the scrollbar.

        Args is a tuple of two floats describing the fraction of the visible area."""

        #g.trace(self.tree.redrawCount,args,g.callers())

        apply(self.canvas.leo_treeBar.set,args,keys)

        if self.tree.allocateOnlyVisibleNodes:
            self.tree.setVisibleArea(args)

    def yviewCallback (self,*args,**keys):

        """Tell the canvas to scroll"""

        #g.trace(vyiewCallback,args,keys,g.callers())

        if self.tree.allocateOnlyVisibleNodes:
            self.tree.allocateNodesBeforeScrolling(args)

        apply(self.canvas.yview,args,keys)
    #@nonl
    #@-node:ekr.20080112145409.68:Scrolling callbacks (gtkFrame)
    #@-node:ekr.20080112145409.65:f.createTkTreeCanvas & callbacks
    #@+node:ekr.20080112145409.69:f.setCanvasColorFromConfig
    def setCanvasColorFromConfig (self,canvas):

        c = self.c

        bg = c.config.getColor("outline_pane_background_color") or 'white'

        try:
            canvas.configure(bg=bg)
        except:
            g.es("exception setting outline pane background color")
            g.es_exception()
    #@-node:ekr.20080112145409.69:f.setCanvasColorFromConfig
    #@-node:ekr.20080112145409.64:gtkFrame.createCanvas & helpers
    #@+node:ekr.20080112145409.70:gtkFrame.createLeoSplitters & helpers
    #@+at 
    #@nonl
    # The key invariants used throughout this code:
    # 
    # 1. self.splitVerticalFlag tells the alignment of the main splitter and
    # 2. not self.splitVerticalFlag tells the alignment of the secondary 
    # splitter.
    # 
    # Only the general-purpose divideAnySplitter routine doesn't know about 
    # these
    # invariants. So most of this code is specialized for Leo's window. OTOH, 
    # creating
    # a single splitter window would be much easier than this code.
    #@-at
    #@@c

    def createLeoSplitters (self,parentFrame):

        # Splitter 1 is the main splitter containing splitter2 and the body pane.
        f1,bar1,split1Pane1,split1Pane2 = self.createLeoGtkSplitter(
            parentFrame,self.splitVerticalFlag,'splitter1')

        self.f1,self.bar1 = f1,bar1
        self.split1Pane1,self.split1Pane2 = split1Pane1,split1Pane2

        # Splitter 2 is the secondary splitter containing the tree and log panes.
        f2,bar2,split2Pane1,split2Pane2 = self.createLeoGtkSplitter(
            split1Pane1,not self.splitVerticalFlag,'splitter2')

        self.f2,self.bar2 = f2,bar2
        self.split2Pane1,self.split2Pane2 = split2Pane1,split2Pane2
    #@nonl
    #@+node:ekr.20080112145409.71:createLeoGtkSplitter
    def createLeoGtkSplitter (self,parent,verticalFlag,componentName):

        c = self.c

        return None,None,None,None ###

        # # Create the frames.
        # f = Tk.Frame(parent,bd=0,relief="flat")
        # f.pack(expand=1,fill="both",pady=1)

        # f1 = Tk.Frame(f)
        # f2 = Tk.Frame(f)
        # bar = Tk.Frame(f,bd=2,relief="raised",bg="LightSteelBlue2")

        # # Configure and place the frames.
        # self.configureBar(bar,verticalFlag)
        # self.bindBar(bar,verticalFlag)
        # self.placeSplitter(bar,f1,f2,verticalFlag)

        # return f, bar, f1, f2
    #@-node:ekr.20080112145409.71:createLeoGtkSplitter
    #@+node:ekr.20080112145409.72:bindBar
    def bindBar (self, bar, verticalFlag):

        if verticalFlag == self.splitVerticalFlag:
            bar.bind("<B1-Motion>", self.onDragMainSplitBar)

        else:
            bar.bind("<B1-Motion>", self.onDragSecondarySplitBar)
    #@-node:ekr.20080112145409.72:bindBar
    #@+node:ekr.20080112145409.73:divideAnySplitter
    # This is the general-purpose placer for splitters.
    # It is the only general-purpose splitter code in Leo.

    def divideAnySplitter (self, frac, verticalFlag, bar, pane1, pane2):

        pass ###

        # if verticalFlag:
            # # Panes arranged vertically; horizontal splitter bar
            # bar.place(rely=frac)
            # pane1.place(relheight=frac)
            # pane2.place(relheight=1-frac)
        # else:
            # # Panes arranged horizontally; vertical splitter bar
            # bar.place(relx=frac)
            # pane1.place(relwidth=frac)
            # pane2.place(relwidth=1-frac)
    #@-node:ekr.20080112145409.73:divideAnySplitter
    #@+node:ekr.20080112145409.74:divideLeoSplitter
    # Divides the main or secondary splitter, using the key invariant.
    def divideLeoSplitter (self, verticalFlag, frac):

        if self.splitVerticalFlag == verticalFlag:
            self.divideLeoSplitter1(frac,verticalFlag)
            self.ratio = frac # Ratio of body pane to tree pane.
        else:
            self.divideLeoSplitter2(frac,verticalFlag)
            self.secondary_ratio = frac # Ratio of tree pane to log pane.

    # Divides the main splitter.
    def divideLeoSplitter1 (self, frac, verticalFlag): 
        self.divideAnySplitter(frac, verticalFlag,
            self.bar1, self.split1Pane1, self.split1Pane2)

    # Divides the secondary splitter.
    def divideLeoSplitter2 (self, frac, verticalFlag): 
        self.divideAnySplitter (frac, verticalFlag,
            self.bar2, self.split2Pane1, self.split2Pane2)
    #@-node:ekr.20080112145409.74:divideLeoSplitter
    #@+node:ekr.20080112145409.75:onDrag...
    def onDragMainSplitBar (self, event):
        self.onDragSplitterBar(event,self.splitVerticalFlag)

    def onDragSecondarySplitBar (self, event):
        self.onDragSplitterBar(event,not self.splitVerticalFlag)

    def onDragSplitterBar (self, event, verticalFlag):

        # x and y are the coordinates of the cursor relative to the bar, not the main window.
        bar = event.widget
        x = event.x
        y = event.y
        top = bar.winfo_toplevel()

        if verticalFlag:
            # Panes arranged vertically; horizontal splitter bar
            wRoot = top.winfo_rooty()
            barRoot = bar.winfo_rooty()
            wMax = top.winfo_height()
            offset = float(barRoot) + y - wRoot
        else:
            # Panes arranged horizontally; vertical splitter bar
            wRoot = top.winfo_rootx()
            barRoot = bar.winfo_rootx()
            wMax = top.winfo_width()
            offset = float(barRoot) + x - wRoot

        # Adjust the pixels, not the frac.
        if offset < 3: offset = 3
        if offset > wMax - 2: offset = wMax - 2
        # Redraw the splitter as the drag is occuring.
        frac = float(offset) / wMax
        # g.trace(frac)
        self.divideLeoSplitter(verticalFlag, frac)
    #@-node:ekr.20080112145409.75:onDrag...
    #@+node:ekr.20080112145409.76:placeSplitter
    def placeSplitter (self,bar,pane1,pane2,verticalFlag):

        if verticalFlag:
            # Panes arranged vertically; horizontal splitter bar
            pane1.place(relx=0.5, rely =   0, anchor="n", relwidth=1.0, relheight=0.5)
            pane2.place(relx=0.5, rely = 1.0, anchor="s", relwidth=1.0, relheight=0.5)
            bar.place  (relx=0.5, rely = 0.5, anchor="c", relwidth=1.0)
        else:
            # Panes arranged horizontally; vertical splitter bar
            # adj gives tree pane more room when tiling vertically.
            adj = g.choose(verticalFlag != self.splitVerticalFlag,0.65,0.5)
            pane1.place(rely=0.5, relx =   0, anchor="w", relheight=1.0, relwidth=adj)
            pane2.place(rely=0.5, relx = 1.0, anchor="e", relheight=1.0, relwidth=1.0-adj)
            bar.place  (rely=0.5, relx = adj, anchor="c", relheight=1.0)
    #@-node:ekr.20080112145409.76:placeSplitter
    #@-node:ekr.20080112145409.70:gtkFrame.createLeoSplitters & helpers
    #@+node:ekr.20080112145409.77:Destroying the gtkFrame
    #@+node:ekr.20080112145409.78:destroyAllObjects
    def destroyAllObjects (self):

        """Clear all links to objects in a Leo window."""

        frame = self ; c = self.c ; tree = frame.tree ; body = self.body

        # g.printGcAll()

        # Do this first.
        #@    << clear all vnodes and tnodes in the tree >>
        #@+node:ekr.20080112145409.79:<< clear all vnodes and tnodes in the tree>>
        # Using a dict here is essential for adequate speed.
        vList = [] ; tDict = {}

        for p in c.allNodes_iter():
            vList.append(p.v)
            if p.v.t:
                key = id(p.v.t)
                if not tDict.has_key(key):
                    tDict[key] = p.v.t

        for key in tDict.keys():
            g.clearAllIvars(tDict[key])

        for v in vList:
            g.clearAllIvars(v)

        vList = [] ; tDict = {} # Remove these references immediately.
        #@-node:ekr.20080112145409.79:<< clear all vnodes and tnodes in the tree>>
        #@nl

        # Destroy all ivars in subcommanders.
        g.clearAllIvars(c.atFileCommands)
        if c.chapterController: # New in Leo 4.4.3 b1.
            g.clearAllIvars(c.chapterController)
        g.clearAllIvars(c.fileCommands)
        g.clearAllIvars(c.keyHandler) # New in Leo 4.4.3 b1.
        g.clearAllIvars(c.importCommands)
        g.clearAllIvars(c.tangleCommands)
        g.clearAllIvars(c.undoer)

        g.clearAllIvars(c)
        g.clearAllIvars(body.colorizer)
        g.clearAllIvars(body)
        g.clearAllIvars(tree)

        # This must be done last.
        frame.destroyAllPanels()
        g.clearAllIvars(frame)

    #@-node:ekr.20080112145409.78:destroyAllObjects
    #@+node:ekr.20080112145409.80:destroyAllPanels
    def destroyAllPanels (self):

        """Destroy all panels attached to this frame."""

        panels = (self.comparePanel, self.colorPanel, self.findPanel, self.fontPanel, self.prefsPanel)

        for panel in panels:
            if panel:
                panel.top.destroy()
    #@-node:ekr.20080112145409.80:destroyAllPanels
    #@+node:ekr.20080112145409.81:destroySelf (gtkFrame)
    def destroySelf (self):

        # Remember these: we are about to destroy all of our ivars!
        top = self.top 
        c = self.c

        # Indicate that the commander is no longer valid.
        c.exists = False 

        # g.trace(self)

        # Important: this destroys all the objects of the commander too.
        self.destroyAllObjects()

        c.exists = False # Make sure this one ivar has not been destroyed.

        top.destroy()
    #@-node:ekr.20080112145409.81:destroySelf (gtkFrame)
    #@-node:ekr.20080112145409.77:Destroying the gtkFrame
    #@-node:ekr.20080112145409.56: Birth & Death (gtkFrame)
    #@+node:ekr.20080112145409.82:class gtkStatusLineClass
    class gtkStatusLineClass:

        '''A class representing the status line.'''

        #@    @+others
        #@+node:ekr.20080112145409.83: ctor
        def __init__ (self,c,parentFrame):

            self.c = c
            self.colorTags = [] # list of color names used as tags.
            self.enabled = False
            self.isVisible = False
            self.lastRow = self.lastCol = 0
            self.log = c.frame.log
            #if 'black' not in self.log.colorTags:
            #    self.log.colorTags.append("black")
            self.parentFrame = parentFrame
            self.statusFrame = Tk.Frame(parentFrame,bd=2)
            text = "line 0, col 0"
            width = len(text) + 4
            self.labelWidget = Tk.Label(self.statusFrame,text=text,width=width,anchor="w")
            self.labelWidget.pack(side="left",padx=1)

            bg = self.statusFrame.cget("background")
            self.textWidget = w = g.app.gui.bodyTextWidget(
                self.statusFrame,
                height=1,state="disabled",bg=bg,relief="groove",name='status-line')
            self.textWidget.pack(side="left",expand=1,fill="x")
            w.bind("<Button-1>", self.onActivate)
            self.show()

            c.frame.statusFrame = self.statusFrame
            c.frame.statusLabel = self.labelWidget
            c.frame.statusText  = self.textWidget
        #@-node:ekr.20080112145409.83: ctor
        #@+node:ekr.20080112145409.84:clear
        def clear (self):

            w = self.textWidget
            if not w: return

            w.configure(state="normal")
            w.delete(0,"end")
            w.configure(state="disabled")
        #@-node:ekr.20080112145409.84:clear
        #@+node:ekr.20080112145409.85:enable, disable & isEnabled
        def disable (self,background=None):

            c = self.c ; w = self.textWidget
            if w:
                if not background:
                    background = self.statusFrame.cget("background")
                w.configure(state="disabled",background=background)
            self.enabled = False
            c.bodyWantsFocus()

        def enable (self,background="white"):

            # g.trace()
            c = self.c ; w = self.textWidget
            if w:
                w.configure(state="normal",background=background)
                c.widgetWantsFocus(w)
            self.enabled = True

        def isEnabled(self):
            return self.enabled
        #@nonl
        #@-node:ekr.20080112145409.85:enable, disable & isEnabled
        #@+node:ekr.20080112145409.86:get
        def get (self):

            w = self.textWidget
            if w:
                return w.getAllText()
            else:
                return ""
        #@-node:ekr.20080112145409.86:get
        #@+node:ekr.20080112145409.87:getFrame
        def getFrame (self):

            return self.statusFrame
        #@-node:ekr.20080112145409.87:getFrame
        #@+node:ekr.20080112145409.88:onActivate
        def onActivate (self,event=None):

            # Don't change background as the result of simple mouse clicks.
            background = self.statusFrame.cget("background")
            self.enable(background=background)
        #@-node:ekr.20080112145409.88:onActivate
        #@+node:ekr.20080112145409.89:pack & show
        def pack (self):

            if not self.isVisible:
                self.isVisible = True
                self.statusFrame.pack(fill="x",pady=1)

        show = pack
        #@-node:ekr.20080112145409.89:pack & show
        #@+node:ekr.20080112145409.90:put (leoGtkFrame:statusLineClass)
        def put(self,s,color=None):

            # g.trace('gtkStatusLine',self.textWidget,s)

            w = self.textWidget
            if not w:
                g.trace('gtkStatusLine','***** disabled')
                return

            w.configure(state="normal")
            w.insert("end",s)

            if color:
                if color not in self.colorTags:
                    self.colorTags.append(color)
                    w.tag_config(color,foreground=color)
                w.tag_add(color,"end-%dc" % (len(s)+1),"end-1c")
                w.tag_config("black",foreground="black")
                w.tag_add("black","end")

            w.configure(state="disabled")
        #@-node:ekr.20080112145409.90:put (leoGtkFrame:statusLineClass)
        #@+node:ekr.20080112145409.91:unpack & hide
        def unpack (self):

            if self.isVisible:
                self.isVisible = False
                self.statusFrame.pack_forget()

        hide = unpack
        #@-node:ekr.20080112145409.91:unpack & hide
        #@+node:ekr.20080112145409.92:update (statusLine)
        def update (self):

            c = self.c ; bodyCtrl = c.frame.body.bodyCtrl

            if g.app.killed or not self.isVisible:
                return

            s = bodyCtrl.getAllText()    
            index = bodyCtrl.getInsertPoint()
            row,col = g.convertPythonIndexToRowCol(s,index)
            if col > 0:
                s2 = s[index-col:index]
                s2 = g.toUnicode(s2,g.app.tkEncoding)
                col = g.computeWidth (s2,c.tab_width)

            # Important: this does not change the focus because labels never get focus.
            self.labelWidget.configure(text="line %d, col %d" % (row,col))
            self.lastRow = row
            self.lastCol = col
        #@-node:ekr.20080112145409.92:update (statusLine)
        #@-others
    #@-node:ekr.20080112145409.82:class gtkStatusLineClass
    #@+node:ekr.20080112145409.93:class gtkIconBarClass
    class gtkIconBarClass:

        '''A class representing the singleton Icon bar'''

        #@    @+others
        #@+node:ekr.20080112145409.94: ctor
        def __init__ (self,c,parentFrame):

            self.c = c

            self.buttons = {}
            self.iconFrame = w = Tk.Frame(parentFrame,height="5m",bd=2,relief="groove")
            self.c.frame.iconFrame = self.iconFrame
            self.font = None
            self.parentFrame = parentFrame
            self.visible = False
            self.show()
        #@-node:ekr.20080112145409.94: ctor
        #@+node:ekr.20080112145409.95:add
        def add(self,*args,**keys):

            """Add a button containing text or a picture to the icon bar.

            Pictures take precedence over text"""

            c = self.c ; f = self.iconFrame
            text = keys.get('text')
            imagefile = keys.get('imagefile')
            image = keys.get('image')
            command = keys.get('command')
            bg = keys.get('bg')

            if not imagefile and not image and not text: return

            # First define n.
            try:
                g.app.iconWidgetCount += 1
                n = g.app.iconWidgetCount
            except:
                n = g.app.iconWidgetCount = 1

            if not command:
                def command():
                    print "command for widget %s" % (n)

            if imagefile or image:
                #@        << create a picture >>
                #@+node:ekr.20080112145409.96:<< create a picture >>
                try:
                    if imagefile:
                        # Create the image.  Throws an exception if file not found
                        imagefile = g.os_path_join(g.app.loadDir,imagefile)
                        imagefile = g.os_path_normpath(imagefile)
                        image = Tk.PhotoImage(master=g.app.root,file=imagefile)

                        # Must keep a reference to the image!
                        try:
                            refs = g.app.iconImageRefs
                        except:
                            refs = g.app.iconImageRefs = []

                        refs.append((imagefile,image),)

                    if not bg:
                        bg = f.cget("bg")

                    b = Tk.Button(f,image=image,relief="flat",bd=0,command=command,bg=bg)
                    b.pack(side="left",fill="y")
                    return b

                except:
                    g.es_exception()
                    return None
                #@-node:ekr.20080112145409.96:<< create a picture >>
                #@nl
            elif text:
                b = Tk.Button(f,text=text,relief="groove",bd=2,command=command)
                if not self.font:
                    self.font = c.config.getFontFromParams(
                        "button_text_font_family", "button_text_font_size",
                        "button_text_font_slant",  "button_text_font_weight",)
                b.configure(font=self.font)
                # elif sys.platform.startswith('win'):
                    # width = max(6,len(text))
                    # b.configure(width=width,font=('verdana',7,'bold'))
                if bg: b.configure(bg=bg)
                b.pack(side="left", fill="none")
                return b

            return None
        #@-node:ekr.20080112145409.95:add
        #@+node:ekr.20080112145409.97:clear
        def clear(self):

            """Destroy all the widgets in the icon bar"""

            f = self.iconFrame

            for slave in f.pack_slaves():
                slave.destroy()
            self.visible = False

            f.configure(height="5m") # The default height.
            g.app.iconWidgetCount = 0
            g.app.iconImageRefs = []
        #@-node:ekr.20080112145409.97:clear
        #@+node:ekr.20080112145409.98:deleteButton (new in Leo 4.4.3)
        def deleteButton (self,w):

            w.pack_forget()
        #@-node:ekr.20080112145409.98:deleteButton (new in Leo 4.4.3)
        #@+node:ekr.20080112145409.99:getFrame
        def getFrame (self):

            return self.iconFrame
        #@-node:ekr.20080112145409.99:getFrame
        #@+node:ekr.20080112145409.100:pack (show)
        def pack (self):

            """Show the icon bar by repacking it"""

            if not self.visible:
                self.visible = True
                self.iconFrame.pack(fill="x",pady=2)

        show = pack
        #@-node:ekr.20080112145409.100:pack (show)
        #@+node:ekr.20080112145409.101:setCommandForButton (new in Leo 4.4.3)
        def setCommandForButton(self,b,command):

            b.configure(command=command)
        #@-node:ekr.20080112145409.101:setCommandForButton (new in Leo 4.4.3)
        #@+node:ekr.20080112145409.102:unpack (hide)
        def unpack (self):

            """Hide the icon bar by unpacking it.

            A later call to show will repack it in a new location."""

            if self.visible:
                self.visible = False
                self.iconFrame.pack_forget()

        hide = unpack
        #@-node:ekr.20080112145409.102:unpack (hide)
        #@-others
    #@-node:ekr.20080112145409.93:class gtkIconBarClass
    #@+node:ekr.20080112145409.103:Minibuffer methods
    #@+node:ekr.20080112145409.104:showMinibuffer
    def showMinibuffer (self):

        '''Make the minibuffer visible.'''

        frame = self

        if not frame.minibufferVisible:
            frame.minibufferFrame.pack(side='bottom',fill='x')
            frame.minibufferVisible = True
    #@-node:ekr.20080112145409.104:showMinibuffer
    #@+node:ekr.20080112145409.105:hideMinibuffer
    def hideMinibuffer (self):

        '''Hide the minibuffer.'''

        frame = self
        if frame.minibufferVisible:
            frame.minibufferFrame.pack_forget()
            frame.minibufferVisible = False
    #@-node:ekr.20080112145409.105:hideMinibuffer
    #@+node:ekr.20080112145409.106:f.createMiniBufferWidget
    def createMiniBufferWidget (self):

        '''Create the minbuffer below the status line.'''

        frame = self ; c = frame.c

        # frame.minibufferFrame = f = Tk.Frame(frame.outerFrame,relief='flat',borderwidth=0)
        # if c.showMinibuffer:
            # f.pack(side='bottom',fill='x')

        # lab = Tk.Label(f,text='mini-buffer',justify='left',anchor='nw',foreground='blue')
        # lab.pack(side='left')

        # if c.useTextMinibuffer:
            # label = g.app.gui.plainTextWidget(
                # f,height=1,relief='groove',background='lightgrey',name='minibuffer')
            # label.pack(side='left',fill='x',expand=1,padx=2,pady=1)
        # else:
            # label = Tk.Label(f,relief='groove',justify='left',anchor='w',name='minibuffer')
            # label.pack(side='left',fill='both',expand=1,padx=2,pady=1)

        # frame.minibufferVisible = c.showMinibuffer

        # return label
    #@-node:ekr.20080112145409.106:f.createMiniBufferWidget
    #@+node:ekr.20080112145409.107:f.setMinibufferBindings
    def setMinibufferBindings (self):

        '''Create bindings for the minibuffer..'''

        f = self ; c = f.c ; k = c.k ; w = f.miniBufferWidget

        if not c.useTextMinibuffer: return

        # for kind,callback in (
            # ('<Key>',           k.masterKeyHandler),
            # ('<Button-1>',      k.masterClickHandler),
            # ('<Button-3>',      k.masterClick3Handler),
            # ('<Double-1>',      k.masterDoubleClickHandler),
            # ('<Double-3>',      k.masterDoubleClick3Handler),
        # ):
            # w.bind(kind,callback)

        # if 0:
            # if sys.platform.startswith('win'):
                # # Support Linux middle-button paste easter egg.
                # w.bind("<Button-2>",frame.OnPaste)
    #@-node:ekr.20080112145409.107:f.setMinibufferBindings
    #@-node:ekr.20080112145409.103:Minibuffer methods
    #@+node:ekr.20080112145409.108:Configuration (gtkFrame)
    #@+node:ekr.20080112145409.109:configureBar (gtkFrame)
    def configureBar (self,bar,verticalFlag):

        c = self.c

        # Get configuration settings.
        w = c.config.getInt("split_bar_width")
        if not w or w < 1: w = 7
        relief = c.config.get("split_bar_relief","relief")
        if not relief: relief = "flat"
        color = c.config.getColor("split_bar_color")
        if not color: color = "LightSteelBlue2"

        try:
            if verticalFlag:
                # Panes arranged vertically; horizontal splitter bar
                bar.configure(relief=relief,height=w,bg=color,cursor="sb_v_double_arrow")
            else:
                # Panes arranged horizontally; vertical splitter bar
                bar.configure(relief=relief,width=w,bg=color,cursor="sb_h_double_arrow")
        except: # Could be a user error. Use all defaults
            g.es("exception in user configuration for splitbar")
            g.es_exception()
            if verticalFlag:
                # Panes arranged vertically; horizontal splitter bar
                bar.configure(height=7,cursor="sb_v_double_arrow")
            else:
                # Panes arranged horizontally; vertical splitter bar
                bar.configure(width=7,cursor="sb_h_double_arrow")
    #@-node:ekr.20080112145409.109:configureBar (gtkFrame)
    #@+node:ekr.20080112145409.110:configureBarsFromConfig (gtkFrame)
    def configureBarsFromConfig (self):

        c = self.c

        w = c.config.getInt("split_bar_width")
        if not w or w < 1: w = 7

        relief = c.config.get("split_bar_relief","relief")
        if not relief or relief == "": relief = "flat"

        color = c.config.getColor("split_bar_color")
        if not color or color == "": color = "LightSteelBlue2"

        if self.splitVerticalFlag:
            bar1,bar2=self.bar1,self.bar2
        else:
            bar1,bar2=self.bar2,self.bar1

        try:
            bar1.configure(relief=relief,height=w,bg=color)
            bar2.configure(relief=relief,width=w,bg=color)
        except: # Could be a user error.
            g.es("exception in user configuration for splitbar")
            g.es_exception()
    #@-node:ekr.20080112145409.110:configureBarsFromConfig (gtkFrame)
    #@+node:ekr.20080112145409.111:reconfigureFromConfig (gtkFrame)
    def reconfigureFromConfig (self):

        frame = self ; c = frame.c

        frame.tree.setFontFromConfig()
        ### frame.tree.setColorFromConfig()

        frame.configureBarsFromConfig()

        frame.body.setFontFromConfig()
        frame.body.setColorFromConfigt()

        frame.setTabWidth(c.tab_width)
        frame.log.setFontFromConfig()
        frame.log.setColorFromConfig()

        c.redraw_now()
    #@-node:ekr.20080112145409.111:reconfigureFromConfig (gtkFrame)
    #@+node:ekr.20080112145409.112:setInitialWindowGeometry (gtkFrame)
    def setInitialWindowGeometry(self):

        """Set the position and size of the frame to config params."""

        c = self.c

        h = c.config.getInt("initial_window_height") or 500
        w = c.config.getInt("initial_window_width") or 600
        x = c.config.getInt("initial_window_left") or 10
        y = c.config.getInt("initial_window_top") or 10

        if h and w and x and y:
            pass ### self.setTopGeometry(w,h,x,y)
    #@-node:ekr.20080112145409.112:setInitialWindowGeometry (gtkFrame)
    #@+node:ekr.20080112145409.113:setTabWidth (gtkFrame)
    def setTabWidth (self, w):

        pass

        # try: # This can fail when called from scripts
            # # Use the present font for computations.
            # font = self.bodyCtrl.cget("font")
            # root = g.app.root # 4/3/03: must specify root so idle window will work properly.
            # font = gtkFont.Font(root=root,font=font)
            # tabw = font.measure(" " * abs(w)) # 7/2/02
            # self.bodyCtrl.configure(tabs=tabw)
            # self.tab_width = w
            # # g.trace(w,tabw)
        # except:
            # g.es_exception()
            # pass
    #@-node:ekr.20080112145409.113:setTabWidth (gtkFrame)
    #@+node:ekr.20080112145409.114:setWrap (gtkFrame)
    def setWrap (self,p):

        c = self.c ; w = c.frame.body.bodyCtrl

        theDict = g.scanDirectives(c,p)
        if not theDict: return

        wrap = theDict.get("wrap")

        ### if self.body.wrapState == wrap: return

        self.body.wrapState = wrap
        # g.trace(wrap)

        ### Rewrite for gtk.
    #@nonl
    #@-node:ekr.20080112145409.114:setWrap (gtkFrame)
    #@+node:ekr.20080112145409.115:setTopGeometry (gtkFrame)
    def setTopGeometry(self,w,h,x,y,adjustSize=True):

        # Put the top-left corner on the screen.
        x = max(10,x) ; y = max(10,y)

        if adjustSize:
            top = self.top
            sw = top.winfo_screenwidth()
            sh = top.winfo_screenheight()

            # Adjust the size so the whole window fits on the screen.
            w = min(sw-10,w)
            h = min(sh-10,h)

            # Adjust position so the whole window fits on the screen.
            if x + w > sw: x = 10
            if y + h > sh: y = 10

        geom = "%dx%d%+d%+d" % (w,h,x,y)

        self.top.geometry(geom)
    #@-node:ekr.20080112145409.115:setTopGeometry (gtkFrame)
    #@+node:ekr.20080112145409.116:reconfigurePanes (use config bar_width) (gtkFrame)
    def reconfigurePanes (self):

        c = self.c

        border = c.config.getInt('additional_body_text_border')
        if border == None: border = 0

        # The body pane needs a _much_ bigger border when tiling horizontally.
        border = g.choose(self.splitVerticalFlag,2+border,6+border)
        ### self.bodyCtrl.configure(bd=border)

        # The log pane needs a slightly bigger border when tiling vertically.
        border = g.choose(self.splitVerticalFlag,4,2) 
        ### self.log.configureBorder(border)
    #@-node:ekr.20080112145409.116:reconfigurePanes (use config bar_width) (gtkFrame)
    #@+node:ekr.20080112145409.117:resizePanesToRatio (gtkFrame)
    def resizePanesToRatio(self,ratio,ratio2):

        # g.trace(ratio,ratio2,g.callers())

        self.divideLeoSplitter(self.splitVerticalFlag,ratio)
        self.divideLeoSplitter(not self.splitVerticalFlag,ratio2)
    #@nonl
    #@-node:ekr.20080112145409.117:resizePanesToRatio (gtkFrame)
    #@-node:ekr.20080112145409.108:Configuration (gtkFrame)
    #@+node:ekr.20080112145409.118:Event handlers (gtkFrame)
    #@+node:ekr.20080112145409.119:frame.OnCloseLeoEvent
    # Called from quit logic and when user closes the window.
    # Returns True if the close happened.

    def OnCloseLeoEvent(self):

        f = self ; c = f.c

        if c.inCommand:
            # g.trace('requesting window close')
            c.requestCloseWindow = True
        else:
            g.app.closeLeoWindow(self)
    #@-node:ekr.20080112145409.119:frame.OnCloseLeoEvent
    #@+node:ekr.20080112145409.120:frame.OnControlKeyUp/Down
    def OnControlKeyDown (self,event=None):

        # __pychecker__ = '--no-argsused' # event not used.

        self.controlKeyIsDown = True

    def OnControlKeyUp (self,event=None):

        # __pychecker__ = '--no-argsused' # event not used.

        self.controlKeyIsDown = False
    #@-node:ekr.20080112145409.120:frame.OnControlKeyUp/Down
    #@+node:ekr.20080112145409.121:OnActivateBody (gtkFrame)
    def OnActivateBody (self,event=None):

        # __pychecker__ = '--no-argsused' # event not used.

        try:
            frame = self ; c = frame.c
            c.setLog()
            w = c.get_focus()
            if w != c.frame.body.bodyCtrl:
                frame.tree.OnDeactivate()
            c.bodyWantsFocus()
        except:
            g.es_event_exception("activate body")

        return 'break'
    #@-node:ekr.20080112145409.121:OnActivateBody (gtkFrame)
    #@+node:ekr.20080112145409.122:OnActivateLeoEvent, OnDeactivateLeoEvent
    def OnActivateLeoEvent(self,event=None):

        '''Handle a click anywhere in the Leo window.'''

        # __pychecker__ = '--no-argsused' # event.

        self.c.setLog()

    def OnDeactivateLeoEvent(self,event=None):

        pass # This causes problems on the Mac.
    #@-node:ekr.20080112145409.122:OnActivateLeoEvent, OnDeactivateLeoEvent
    #@+node:ekr.20080112145409.123:OnActivateTree
    def OnActivateTree (self,event=None):

        try:
            frame = self ; c = frame.c
            c.setLog()

            if 0: # Do NOT do this here!
                # OnActivateTree can get called when the tree gets DE-activated!!
                c.bodyWantsFocus()

        except:
            g.es_event_exception("activate tree")
    #@-node:ekr.20080112145409.123:OnActivateTree
    #@+node:ekr.20080112145409.124:OnBodyClick, OnBodyRClick (Events)
    def OnBodyClick (self,event=None):

        try:
            c = self.c ; p = c.currentPosition()
            if not g.doHook("bodyclick1",c=c,p=p,v=p,event=event):
                self.OnActivateBody(event=event)
            g.doHook("bodyclick2",c=c,p=p,v=p,event=event)
        except:
            g.es_event_exception("bodyclick")

    def OnBodyRClick(self,event=None):

        try:
            c = self.c ; p = c.currentPosition()
            if not g.doHook("bodyrclick1",c=c,p=p,v=p,event=event):
                pass # By default Leo does nothing.
            g.doHook("bodyrclick2",c=c,p=p,v=p,event=event)
        except:
            g.es_event_exception("iconrclick")
    #@-node:ekr.20080112145409.124:OnBodyClick, OnBodyRClick (Events)
    #@+node:ekr.20080112145409.125:OnBodyDoubleClick (Events)
    def OnBodyDoubleClick (self,event=None):

        try:
            c = self.c ; p = c.currentPosition()
            if event and not g.doHook("bodydclick1",c=c,p=p,v=p,event=event):
                c.editCommands.extendToWord(event) # Handles unicode properly.
            g.doHook("bodydclick2",c=c,p=p,v=p,event=event)
        except:
            g.es_event_exception("bodydclick")

        return "break" # Restore this to handle proper double-click logic.
    #@-node:ekr.20080112145409.125:OnBodyDoubleClick (Events)
    #@+node:ekr.20080112145409.126:OnMouseWheel (Tomaz Ficko)
    # Contributed by Tomaz Ficko.  This works on some systems.
    # On XP it causes a crash in tcl83.dll.  Clearly a Tk bug.

    def OnMouseWheel(self, event=None):

        try:
            if event.delta < 1:
                self.canvas.yview(Tk.SCROLL, 1, Tk.UNITS)
            else:
                self.canvas.yview(Tk.SCROLL, -1, Tk.UNITS)
        except:
            g.es_event_exception("scroll wheel")

        return "break"
    #@-node:ekr.20080112145409.126:OnMouseWheel (Tomaz Ficko)
    #@-node:ekr.20080112145409.118:Event handlers (gtkFrame)
    #@+node:ekr.20080112145409.127:Gui-dependent commands
    #@+node:ekr.20080112145409.128:Minibuffer commands... (gtkFrame)

    #@+node:ekr.20080112145409.129:contractPane
    def contractPane (self,event=None):

        '''Contract the selected pane.'''

        f = self ; c = f.c
        w = c.get_requested_focus()
        wname = c.widget_name(w)

        # g.trace(wname)
        if not w: return

        if wname.startswith('body'):
            f.contractBodyPane()
        elif wname.startswith('log'):
            f.contractLogPane()
        elif wname.startswith('head') or wname.startswith('canvas'):
            f.contractOutlinePane()
    #@-node:ekr.20080112145409.129:contractPane
    #@+node:ekr.20080112145409.130:expandPane
    def expandPane (self,event=None):

        '''Expand the selected pane.'''

        f = self ; c = f.c

        w = c.get_requested_focus()
        wname = c.widget_name(w)

        # g.trace(wname)
        if not w: return

        if wname.startswith('body'):
            f.expandBodyPane()
        elif wname.startswith('log'):
            f.expandLogPane()
        elif wname.startswith('head') or wname.startswith('canvas'):
            f.expandOutlinePane()
    #@-node:ekr.20080112145409.130:expandPane
    #@+node:ekr.20080112145409.131:fullyExpandPane
    def fullyExpandPane (self,event=None):

        '''Fully expand the selected pane.'''

        f = self ; c = f.c

        w = c.get_requested_focus()
        wname = c.widget_name(w)

        # g.trace(wname)
        if not w: return

        if wname.startswith('body'):
            f.fullyExpandBodyPane()
        elif wname.startswith('log'):
            f.fullyExpandLogPane()
        elif wname.startswith('head') or wname.startswith('canvas'):
            f.fullyExpandOutlinePane()
    #@-node:ekr.20080112145409.131:fullyExpandPane
    #@+node:ekr.20080112145409.132:hidePane
    def hidePane (self,event=None):

        '''Completely contract the selected pane.'''

        f = self ; c = f.c

        w = c.get_requested_focus()
        wname = c.widget_name(w)

        g.trace(wname)
        if not w: return

        if wname.startswith('body'):
            f.hideBodyPane()
            c.treeWantsFocusNow()
        elif wname.startswith('log'):
            f.hideLogPane()
            c.bodyWantsFocusNow()
        elif wname.startswith('head') or wname.startswith('canvas'):
            f.hideOutlinePane()
            c.bodyWantsFocusNow()
    #@-node:ekr.20080112145409.132:hidePane
    #@+node:ekr.20080112145409.133:expand/contract/hide...Pane
    #@+at 
    #@nonl
    # The first arg to divideLeoSplitter means the following:
    # 
    #     f.splitVerticalFlag: use the primary   (tree/body) ratio.
    # not f.splitVerticalFlag: use the secondary (tree/log) ratio.
    #@-at
    #@@c

    def contractBodyPane (self,event=None):
        '''Contract the body pane.'''
        f = self ; r = min(1.0,f.ratio+0.1)
        f.divideLeoSplitter(f.splitVerticalFlag,r)

    def contractLogPane (self,event=None):
        '''Contract the log pane.'''
        f = self ; r = min(1.0,f.ratio+0.1)
        f.divideLeoSplitter(not f.splitVerticalFlag,r)

    def contractOutlinePane (self,event=None):
        '''Contract the outline pane.'''
        f = self ; r = max(0.0,f.ratio-0.1)
        f.divideLeoSplitter(f.splitVerticalFlag,r)

    def expandBodyPane (self,event=None):
        '''Expand the body pane.'''
        self.contractOutlinePane()

    def expandLogPane(self,event=None):
        '''Expand the log pane.'''
        f = self ; r = max(0.0,f.ratio-0.1)
        f.divideLeoSplitter(not f.splitVerticalFlag,r)

    def expandOutlinePane (self,event=None):
        '''Expand the outline pane.'''
        self.contractBodyPane()
    #@-node:ekr.20080112145409.133:expand/contract/hide...Pane
    #@+node:ekr.20080112145409.134:fullyExpand/hide...Pane
    def fullyExpandBodyPane (self,event=None):
        '''Fully expand the body pane.'''
        f = self ; f.divideLeoSplitter(f.splitVerticalFlag,0.0)

    def fullyExpandLogPane (self,event=None):
        '''Fully expand the log pane.'''
        f = self ; f.divideLeoSplitter(not f.splitVerticalFlag,0.0)

    def fullyExpandOutlinePane (self,event=None):
        '''Fully expand the outline pane.'''
        f = self ; f.divideLeoSplitter(f.splitVerticalFlag,1.0)

    def hideBodyPane (self,event=None):
        '''Completely contract the body pane.'''
        f = self ; f.divideLeoSplitter(f.splitVerticalFlag,1.0)

    def hideLogPane (self,event=None):
        '''Completely contract the log pane.'''
        f = self ; f.divideLeoSplitter(not f.splitVerticalFlag,1.0)

    def hideOutlinePane (self,event=None):
        '''Completely contract the outline pane.'''
        f = self ; f.divideLeoSplitter(f.splitVerticalFlag,0.0)
    #@-node:ekr.20080112145409.134:fullyExpand/hide...Pane
    #@-node:ekr.20080112145409.128:Minibuffer commands... (gtkFrame)
    #@+node:ekr.20080112145409.135:Window Menu...
    #@+node:ekr.20080112145409.136:toggleActivePane
    def toggleActivePane (self,event=None):

        '''Toggle the focus between the outline and body panes.'''

        frame = self ; c = frame.c

        if c.get_focus() == frame.body.bodyCtrl: # 2007:10/25
            c.treeWantsFocusNow()
        else:
            c.endEditing()
            c.bodyWantsFocusNow()
    #@-node:ekr.20080112145409.136:toggleActivePane
    #@+node:ekr.20080112145409.137:cascade
    def cascade (self,event=None):

        '''Cascade all Leo windows.'''

        x,y,delta = 10,10,10
        for frame in g.app.windowList:
            top = frame.top

            # Compute w,h
            top.update_idletasks() # Required to get proper info.
            geom = top.geometry() # geom = "WidthxHeight+XOffset+YOffset"
            dim,junkx,junky = string.split(geom,'+')
            w,h = string.split(dim,'x')
            w,h = int(w),int(h)

            # Set new x,y and old w,h
            frame.setTopGeometry(w,h,x,y,adjustSize=False)

            # Compute the new offsets.
            x += 30 ; y += 30
            if x > 200:
                x = 10 + delta ; y = 40 + delta
                delta += 10
    #@-node:ekr.20080112145409.137:cascade
    #@+node:ekr.20080112145409.138:equalSizedPanes
    def equalSizedPanes (self,event=None):

        '''Make the outline and body panes have the same size.'''

        frame = self
        frame.resizePanesToRatio(0.5,frame.secondary_ratio)
    #@-node:ekr.20080112145409.138:equalSizedPanes
    #@+node:ekr.20080112145409.139:hideLogWindow
    def hideLogWindow (self,event=None):

        frame = self
        frame.divideLeoSplitter2(0.99, not frame.splitVerticalFlag)
    #@-node:ekr.20080112145409.139:hideLogWindow
    #@+node:ekr.20080112145409.140:minimizeAll
    def minimizeAll (self,event=None):

        '''Minimize all Leo's windows.'''

        self.minimize(g.app.pythonFrame)
        for frame in g.app.windowList:
            self.minimize(frame)
            self.minimize(frame.findPanel)

    def minimize(self,frame):

        if frame and frame.top.state() == "normal":
            frame.top.iconify()
    #@-node:ekr.20080112145409.140:minimizeAll
    #@+node:ekr.20080112145409.141:toggleSplitDirection (gtkFrame)
    # The key invariant: self.splitVerticalFlag tells the alignment of the main splitter.

    def toggleSplitDirection (self,event=None):

        '''Toggle the split direction in the present Leo window.'''

        # Switch directions.
        c = self.c
        self.splitVerticalFlag = not self.splitVerticalFlag
        orientation = g.choose(self.splitVerticalFlag,"vertical","horizontal")
        c.config.set("initial_splitter_orientation","string",orientation)

        self.toggleTkSplitDirection(self.splitVerticalFlag)
    #@+node:ekr.20080112145409.142:toggleTkSplitDirection
    def toggleTkSplitDirection (self,verticalFlag):

        # Abbreviations.
        frame = self
        bar1 = self.bar1 ; bar2 = self.bar2
        split1Pane1,split1Pane2 = self.split1Pane1,self.split1Pane2
        split2Pane1,split2Pane2 = self.split2Pane1,self.split2Pane2
        # Reconfigure the bars.
        bar1.place_forget()
        bar2.place_forget()
        self.configureBar(bar1,verticalFlag)
        self.configureBar(bar2,not verticalFlag)
        # Make the initial placements again.
        self.placeSplitter(bar1,split1Pane1,split1Pane2,verticalFlag)
        self.placeSplitter(bar2,split2Pane1,split2Pane2,not verticalFlag)
        # Adjust the log and body panes to give more room around the bars.
        self.reconfigurePanes()
        # Redraw with an appropriate ratio.
        vflag,ratio,secondary_ratio = frame.initialRatios()
        self.resizePanesToRatio(ratio,secondary_ratio)
    #@-node:ekr.20080112145409.142:toggleTkSplitDirection
    #@-node:ekr.20080112145409.141:toggleSplitDirection (gtkFrame)
    #@+node:ekr.20080112145409.143:resizeToScreen
    def resizeToScreen (self,event=None):

        '''Resize the Leo window so it fill the entire screen.'''

        top = self.top

        w = top.winfo_screenwidth()
        h = top.winfo_screenheight()

        if sys.platform.startswith('win'):
            top.state('zoomed')
        elif sys.platform == 'darwin':
            # Must leave room to get at very small resizing area.
            geom = "%dx%d%+d%+d" % (w-20,h-55,10,25)
            top.geometry(geom)
        else:
            # Fill almost the entire screen.
            # Works on Windows. YMMV for other platforms.
            geom = "%dx%d%+d%+d" % (w-8,h-46,0,0)
            top.geometry(geom)
    #@-node:ekr.20080112145409.143:resizeToScreen
    #@-node:ekr.20080112145409.135:Window Menu...
    #@+node:ekr.20080112145409.144:Help Menu...
    #@+node:ekr.20080112145409.145:leoHelp
    def leoHelp (self,event=None):

        '''Open Leo's offline tutorial.'''

        frame = self ; c = frame.c

        theFile = g.os_path_join(g.app.loadDir,"..","doc","sbooks.chm")

        if g.os_path_exists(theFile):
            os.startfile(theFile)
        else:
            answer = g.app.gui.runAskYesNoDialog(c,
                "Download Tutorial?",
                "Download tutorial (sbooks.chm) from SourceForge?")

            if answer == "yes":
                try:
                    if 0: # Download directly.  (showProgressBar needs a lot of work)
                        url = "http://umn.dl.sourceforge.net/sourceforge/leo/sbooks.chm"
                        import urllib
                        self.scale = None
                        urllib.urlretrieve(url,theFile,self.showProgressBar)
                        if self.scale:
                            self.scale.destroy()
                            self.scale = None
                    else:
                        url = "http://prdownloads.sourceforge.net/leo/sbooks.chm?download"
                        import webbrowser
                        os.chdir(g.app.loadDir)
                        webbrowser.open_new(url)
                except:
                    g.es("exception dowloading sbooks.chm")
                    g.es_exception()
    #@+node:ekr.20080112145409.146:showProgressBar
    def showProgressBar (self,count,size,total):

        # g.trace("count,size,total:",count,size,total)
        if self.scale == None:
            #@        << create the scale widget >>
            #@+node:ekr.20080112145409.147:<< create the scale widget >>
            top = Tk.Toplevel()
            top.title("Download progress")
            self.scale = scale = Tk.Scale(top,state="normal",orient="horizontal",from_=0,to=total)
            scale.pack()
            top.lift()
            #@-node:ekr.20080112145409.147:<< create the scale widget >>
            #@nl
        self.scale.set(count*size)
        self.scale.update_idletasks()
    #@-node:ekr.20080112145409.146:showProgressBar
    #@-node:ekr.20080112145409.145:leoHelp
    #@-node:ekr.20080112145409.144:Help Menu...
    #@-node:ekr.20080112145409.127:Gui-dependent commands
    #@+node:ekr.20080112145409.148:Delayed Focus (gtkFrame)
    #@+at 
    #@nonl
    # New in 4.3. The proper way to change focus is to call 
    # c.frame.xWantsFocus.
    # 
    # Important: This code never calls select, so there can be no race 
    # condition here
    # that alters text improperly.
    #@-at
    #@-node:ekr.20080112145409.148:Delayed Focus (gtkFrame)
    #@+node:ekr.20080112145409.149:Tk bindings... (gtkFrame)
    def bringToFront (self):
        # g.trace(g.callers())
        self.top.deiconify()
        self.top.lift()

    def getFocus(self):
        """Returns the widget that has focus, or body if None."""
        try:
            # This method is unreliable while focus is changing.
            # The call to update_idletasks may help.  Or not.
            self.top.update_idletasks()
            f = self.top.focus_displayof()
        except Exception:
            f = None
        if f:
            return f
        else:
            return self.body.bodyCtrl

    def getTitle (self):
        return self.top.title()

    def setTitle (self,title):
        return self.top.title(title)

    def get_window_info(self):
        return g.app.gui.get_window_info(self.top)

    def iconify(self):
        self.top.iconify()

    def deiconify (self):
        self.top.deiconify()

    def lift (self):
        self.top.lift()

    def update (self):
        self.top.update()
    #@-node:ekr.20080112145409.149:Tk bindings... (gtkFrame)
    #@-others
#@-node:ekr.20080112145409.55:class leoGtkFrame
#@+node:ekr.20080112145409.150:class leoGtkBody
class leoGtkBody (leoFrame.leoBody):

    ###

    # def __init__ (self,frame,parentFrame):
        # # g.trace('leoGtkBody')
        # leoFrame.leoBody.__init__(self,frame,parentFrame) # Init the base class.

    # # Birth, death & config...
    # def createBindings (self,w=None):         pass
    # def createControl (self,parentFrame,p):   pass
    # def setColorFromConfig (self,w=None):     pass
    # def setFontFromConfig (self,w=None):      pass

    # # Editor...
    # def createEditorLabel (self,pane):  pass
    # def setEditorColors (self,bg,fg):   pass

    # # Events...
    # def scheduleIdleTimeRoutine (self,function,*args,**keys): pass

    #@    @+others
    #@+node:ekr.20080112145409.151: Birth & death
    #@+node:ekr.20080112145409.152:gtkBody. __init__
    def __init__ (self,frame,parentFrame):

        g.trace('leoGtkBody')

        # Call the base class constructor.
        leoFrame.leoBody.__init__(self,frame,parentFrame)

        c = self.c ; p = c.currentPosition()
        self.editor_name = None
        self.editor_v = None

        self.trace_onBodyChanged = c.config.getBool('trace_onBodyChanged')
        self.bodyCtrl = self.createControl(parentFrame,p)
        self.colorizer = leoColor.colorizer(c)
    #@-node:ekr.20080112145409.152:gtkBody. __init__
    #@+node:ekr.20080112145409.153:gtkBody.createBindings
    def createBindings (self,w=None):

        '''(gtkBody) Create gui-dependent bindings.
        These are *not* made in nullBody instances.'''

        frame = self.frame ; c = self.c ; k = c.k
        if not w: w = self.bodyCtrl

        # w.bind('<Key>', k.masterKeyHandler)

        # for kind,func,handler in (
            # ('<Button-1>',  frame.OnBodyClick,          k.masterClickHandler),
            # ('<Button-3>',  frame.OnBodyRClick,         k.masterClick3Handler),
            # ('<Double-1>',  frame.OnBodyDoubleClick,    k.masterDoubleClickHandler),
            # ('<Double-3>',  None,                       k.masterDoubleClick3Handler),
            # ('<Button-2>',  frame.OnPaste,              k.masterClickHandler),
        # ):
            # def bodyClickCallback(event,handler=handler,func=func):
                # return handler(event,func)

            # w.bind(kind,bodyClickCallback)
    #@nonl
    #@-node:ekr.20080112145409.153:gtkBody.createBindings
    #@+node:ekr.20080112145409.154:gtkBody.createControl
    def createControl (self,parentFrame,p):

        c = self.c

        g.trace('gtkBody')

        # New in 4.4.1: make the parent frame a PanedWidget.
        self.numberOfEditors = 1 ; name = '1'
        self.totalNumberOfEditors = 1

        orient = c.config.getString('editor_orientation') or 'horizontal'
        if orient not in ('horizontal','vertical'): orient = 'horizontal'

        # self.pb = pb = Pmw.PanedWidget(parentFrame,orient=orient)
        # parentFrame = pb.add(name)
        # pb.pack(expand=1,fill='both') # Must be done after the first page created.

        w = self.createTextWidget(parentFrame,p,name)
        self.editorWidgets[name] = w

        return w
    #@-node:ekr.20080112145409.154:gtkBody.createControl
    #@+node:ekr.20080112145409.155:gtkBody.createTextWidget
    def createTextWidget (self,parentFrame,p,name):

        c = self.c

        # parentFrame.configure(bg='LightSteelBlue1')

        wrap = c.config.getBool('body_pane_wraps')
        wrap = g.choose(wrap,"word","none")

        # # Setgrid=1 cause severe problems with the font panel.
        body = w = leoGtkTextWidget (parentFrame,name='body-pane',
            bd=2,bg="white",relief="flat",setgrid=0,wrap=wrap)

        # bodyBar = Tk.Scrollbar(parentFrame,name='bodyBar')

        # def yscrollCallback(x,y,bodyBar=bodyBar,w=w):
            # # g.trace(x,y,g.callers())
            # if hasattr(w,'leo_scrollBarSpot'):
                # w.leo_scrollBarSpot = (x,y)
            # return bodyBar.set(x,y)

        # body['yscrollcommand'] = yscrollCallback # bodyBar.set

        # bodyBar['command'] =  body.yview
        # bodyBar.pack(side="right", fill="y")

        # # Always create the horizontal bar.
        # bodyXBar = Tk.Scrollbar(
            # parentFrame,name='bodyXBar',orient="horizontal")
        # body['xscrollcommand'] = bodyXBar.set
        # bodyXBar['command'] = body.xview

        # if wrap == "none":
            # # g.trace(parentFrame)
            # bodyXBar.pack(side="bottom", fill="x")

        # body.pack(expand=1,fill="both")

        # self.wrapState = wrap

        # if 0: # Causes the cursor not to blink.
            # body.configure(insertofftime=0)

        # # Inject ivars
        if name == '1':
            w.leo_p = w.leo_v = None # Will be set when the second editor is created.
        else:
            w.leo_p = p.copy()
            w.leo_v = w.leo_p.v
                # pychecker complains body.leo_p does not exist.
        w.leo_active = True
        w.leo_bodyBar = bodyBar
        w.leo_bodyXBar = bodyXBar
        w.leo_chapter = None
        w.leo_frame = parentFrame
        w.leo_name = name
        w.leo_label = None
        w.leo_label_s = None
        w.leo_scrollBarSpot = None
        w.leo_insertSpot = None
        w.leo_selection = None

        return w
    #@-node:ekr.20080112145409.155:gtkBody.createTextWidget
    #@-node:ekr.20080112145409.151: Birth & death
    #@+node:ekr.20080112145409.156:gtkBody.setColorFromConfig
    def setColorFromConfig (self,w=None):

        c = self.c
        if w is None: w = self.bodyCtrl

        return ###

        bg = c.config.getColor("body_text_background_color") or 'white'
        # g.trace(id(w),bg)

        try: w.configure(bg=bg)
        except:
            g.es("exception setting body text background color")
            g.es_exception()

        fg = c.config.getColor("body_text_foreground_color") or 'black'
        try: w.configure(fg=fg)
        except:
            g.es("exception setting body textforeground color")
            g.es_exception()

        bg = c.config.getColor("body_insertion_cursor_color")
        if bg:
            try: w.configure(insertbackground=bg)
            except:
                g.es("exception setting body pane cursor color")
                g.es_exception()

        sel_bg = c.config.getColor('body_text_selection_background_color') or 'Gray80'
        try: w.configure(selectbackground=sel_bg)
        except Exception:
            g.es("exception setting body pane text selection background color")
            g.es_exception()

        sel_fg = c.config.getColor('body_text_selection_foreground_color') or 'white'
        try: w.configure(selectforeground=sel_fg)
        except Exception:
            g.es("exception setting body pane text selection foreground color")
            g.es_exception()

        if sys.platform != "win32": # Maybe a Windows bug.
            fg = c.config.getColor("body_cursor_foreground_color")
            bg = c.config.getColor("body_cursor_background_color")
            if fg and bg:
                cursor="xterm" + " " + fg + " " + bg
                try: w.configure(cursor=cursor)
                except:
                    import traceback ; traceback.print_exc()
    #@-node:ekr.20080112145409.156:gtkBody.setColorFromConfig
    #@+node:ekr.20080112145409.157:gtkBody.setFontFromConfig
    def setFontFromConfig (self,w=None):

        c = self.c

        if not w: w = self.bodyCtrl

        font = c.config.getFontFromParams(
            "body_text_font_family", "body_text_font_size",
            "body_text_font_slant",  "body_text_font_weight",
            c.config.defaultBodyFontSize)

        self.fontRef = font # ESSENTIAL: retain a link to font.
        ### w.configure(font=font)

        # g.trace("BODY",body.cget("font"),font.cget("family"),font.cget("weight"))
    #@-node:ekr.20080112145409.157:gtkBody.setFontFromConfig
    #@+node:ekr.20080112145409.158:Focus (gtkBody)
    def hasFocus (self):

        return self.bodyCtrl == self.frame.top.focus_displayof()

    def setFocus (self):

        self.c.widgetWantsFocus(self.bodyCtrl)
    #@-node:ekr.20080112145409.158:Focus (gtkBody)
    #@+node:ekr.20080112145409.159:forceRecolor
    def forceFullRecolor (self):

        self.forceFullRecolorFlag = True
    #@-node:ekr.20080112145409.159:forceRecolor
    #@+node:ekr.20080112145409.160:Tk bindings (gtkBbody)
    #@+node:ekr.20080112145409.161:bind (new)
    def bind (self,*args,**keys):

        pass
    #@-node:ekr.20080112145409.161:bind (new)
    #@+node:ekr.20080112145409.162:Tags (Tk spelling) (gtkBody)
    def tag_add (self,tagName,index1,index2):
        self.bodyCtrl.tag_add(tagName,index1,index2)

    def tag_bind (self,tagName,event,callback):
        self.bodyCtrl.tag_bind(tagName,event,callback)

    def tag_configure (self,colorName,**keys):
        self.bodyCtrl.tag_configure(colorName,keys)

    def tag_delete(self,tagName):
        self.bodyCtrl.tag_delete(tagName)

    def tag_names(self,*args): # New in Leo 4.4.1.
        return self.bodyCtrl.tag_names(*args)

    def tag_remove (self,tagName,index1,index2):
        return self.bodyCtrl.tag_remove(tagName,index1,index2)
    #@-node:ekr.20080112145409.162:Tags (Tk spelling) (gtkBody)
    #@+node:ekr.20080112145409.163:Configuration (Tk spelling) (gtkBody)
    def cget(self,*args,**keys):

        body = self ; w = self.bodyCtrl
        val = w.cget(*args,**keys)

        if g.app.trace:
            g.trace(val,args,keys)

        return val

    def configure (self,*args,**keys):

        # g.trace(args,keys)

        body = self ; w = body.bodyCtrl
        return w.configure(*args,**keys)
    #@-node:ekr.20080112145409.163:Configuration (Tk spelling) (gtkBody)
    #@+node:ekr.20080112145409.164:Height & width (gtkBody)
    def getBodyPaneHeight (self):

        return self.bodyCtrl.winfo_height()

    def getBodyPaneWidth (self):

        return self.bodyCtrl.winfo_width()
    #@-node:ekr.20080112145409.164:Height & width (gtkBody)
    #@+node:ekr.20080112145409.165:Idle time... (gtkBody)
    def scheduleIdleTimeRoutine (self,function,*args,**keys):

        pass ### self.bodyCtrl.after_idle(function,*args,**keys)
    #@-node:ekr.20080112145409.165:Idle time... (gtkBody)
    #@+node:ekr.20080112145409.166:Menus (gtkBody)
    def bind (self,*args,**keys):

        pass ### return self.bodyCtrl.bind(*args,**keys)
    #@-node:ekr.20080112145409.166:Menus (gtkBody)
    #@+node:ekr.20080112145409.167:Text (now in base class) (gtkBody)
    # def getAllText (self):              return self.bodyCtrl.getAllText()
    # def getInsertPoint(self):           return self.bodyCtrl.getInsertPoint()
    # def getSelectedText (self):         return self.bodyCtrl.getSelectedText()
    # def getSelectionRange (self,sort=True): return self.bodyCtrl.getSelectionRange(sort)
    # def hasTextSelection (self):        return self.bodyCtrl.hasSelection()
    # # def scrollDown (self):            g.app.gui.yscroll(self.bodyCtrl,1,'units')
    # # def scrollUp (self):              g.app.gui.yscroll(self.bodyCtrl,-1,'units')
    # def see (self,index):               self.bodyCtrl.see(index)
    # def seeInsertPoint (self):          self.bodyCtrl.seeInsertPoint()
    # def selectAllText (self,event=None):
        # w = g.app.gui.eventWidget(event) or self.bodyCtrl
        # return w.selectAllText()
    # def setInsertPoint (self,pos):      return self.bodyCtrl.getInsertPoint(pos)
    # def setSelectionRange (self,sel):
        # i,j = sel
        # self.bodyCtrl.setSelectionRange(i,j)
    #@nonl
    #@-node:ekr.20080112145409.167:Text (now in base class) (gtkBody)
    #@-node:ekr.20080112145409.160:Tk bindings (gtkBbody)
    #@+node:ekr.20080112145409.168:Editors (gtkBody)
    #@+node:ekr.20080112145409.169:createEditorFrame
    def createEditorFrame (self,pane):

        f = Tk.Frame(pane)
        f.pack(side='top',expand=1,fill='both')
        return f
    #@-node:ekr.20080112145409.169:createEditorFrame
    #@+node:ekr.20080112145409.170:packEditorLabelWidget
    def packEditorLabelWidget (self,w):

        '''Create a Tk label widget.'''

        if not hasattr(w,'leo_label') or not w.leo_label:
            # g.trace('w.leo_frame',id(w.leo_frame))
            w.pack_forget()
            w.leo_label = Tk.Label(w.leo_frame)
            w.leo_label.pack(side='top')
            w.pack(expand=1,fill='both')
    #@nonl
    #@-node:ekr.20080112145409.170:packEditorLabelWidget
    #@+node:ekr.20080112145409.171:setEditorColors
    def setEditorColors (self,bg,fg):

        c = self.c ; d = self.editorWidgets

        ###

        # for key in d.keys():
            # w2 = d.get(key)
            # # g.trace(id(w2),bg,fg)
            # try:
                # w2.configure(bg=bg,fg=fg)
            # except Exception:
                # g.es_exception()
                # pass
    #@-node:ekr.20080112145409.171:setEditorColors
    #@-node:ekr.20080112145409.168:Editors (gtkBody)
    #@-others
#@-node:ekr.20080112145409.150:class leoGtkBody
#@+node:ekr.20080112145409.172:class leoGtkKeys
class gtkKeyHandlerClass (leoKeys.keyHandlerClass):

    '''gtk overrides of base keyHandlerClass.'''

    def __init__(self,c,useGlobalKillbuffer=False,useGlobalRegisters=False):

        # g.trace('gtkKeyHandlerClass',c)

        # Init the base class.
        leoKeys.keyHandlerClass.__init__(self,c,useGlobalKillbuffer,useGlobalRegisters)
#@-node:ekr.20080112145409.172:class leoGtkKeys
#@+node:ekr.20080112145409.173:class leoGtkMenu
class leoGtkMenu( leoMenu.leoMenu ):

    #@    @+others
    #@+node:ekr.20080112145409.174: leoGtkMenu.__init__
    def __init__ (self,frame):

        if 0:
            ld = io.File( g.app.loadDir )
            ijcl.addToSearchPath( ld )
            ijcl.beginLoading()
            self.font = frame.top.getFont()
            self.executor = java.util.concurrent.Executors.newCachedThreadPool()
            self.queue = java.util.concurrent.LinkedBlockingQueue()
            self.menu_changer = self.MenuChanger( self.queue )
            self.names_and_commands = {}
            self.keystrokes_and_actions = {}

        leoMenu.leoMenu.__init__( self, frame )

        #self.createLeoGtkPrint()
        #self.defineLeoGtkPrintTable()
        #self.addCommanderSupplemental()








    #@-node:ekr.20080112145409.174: leoGtkMenu.__init__
    #@+node:ekr.20080112145409.175:not ready yet
    if 0:
        #@    @+others
        #@+node:ekr.20080112145409.176:class MenuChanger
        class MenuChanger( java.lang.Runnable, java.util.concurrent.Callable ):

            def __init__( self, queue ):
                self.queue = queue

            def run( self ):

                ft = java.util.concurrent.FutureTask( self )
                java.awt.EventQueue.invokeLater( ft )


            def call( self ):

                menu , name , label, enabled = self.queue.take() 
                target = None
                for z in menu.getMenuComponents():
                    if hasattr( z, "getText" ) and z.getText() == name:
                        target = z
                        break


                if target:
                    target.setText( label )
                    target.setEnabled( enabled )
        #@-node:ekr.20080112145409.176:class MenuChanger
        #@+node:ekr.20080112145409.177:print menu stuff...

        #@+node:ekr.20080112145409.178:defineLeoGtkPrintTable
        def defineLeoGtkPrintTable( self ):

            self.printNodeTable= (

            ( "Print Current Node" , None, lambda event: self.lsp.printNode() ),
            ( "Print Current Node as HTML", None, lambda event: self.lsp.printNode( type = "HTML" ) ),
            ( "Print Marked Nodes", None, lambda event:  self.lsp.printMarkedNodes() ),
            ( "Print Marked Nodes as HTML", None, lambda event: self.lsp.printNode( type ="HTML" ) ),

            )

            for z in self.printNodeTable:
                self.names_and_commands[ z[ 0 ] ] = z[ 2 ]
        #@-node:ekr.20080112145409.178:defineLeoGtkPrintTable
        #@+node:ekr.20080112145409.179:createLeoGtkPrintMenu
        def createLeoGtkPrintMenu( self ):

            fmenu = self.getMenu( "File" )

            components = fmenu.getMenuComponents()

            x = 0
            for z in components:

                if hasattr( z, 'getText' ) and z.getText() == "Recent Files...":
                    break
                x += 1


            spot = x + 1

            pmenu = gtk.JMenu( "Printing" )

            pnodes = gtk.JMenu( "Print Nodes" )
            pmenu.add( pnodes )
            for z in self.printNodeTable:
                item = gtk.JMenuItem( z[ 0 ] )
                item.actionPerformed = z[ 2 ]
                pnodes.add( item )

            sep = gtk.JSeparator()
            fmenu.add( sep, spot  )
            fmenu.add( pmenu, spot + 1 )

            print_tree = gtk.JMenuItem( "Print Tree As Is" )
            print_tree.actionPerformed = self.lsp.printTreeAsIs
            pmenu.add( print_tree )
            self.names_and_commands[ "Print Tree As Is" ] = self.lsp.printTreeAsIs
            print_as_more = gtk.JMenuItem( "Print Outline in More Format" )
            print_as_more.actionPerformed = self.lsp.printOutlineAsMore
            self.names_and_commands[ "Print Outline in More Formet" ] = self.lsp.printOutlineAsMore
            pmenu.add( print_as_more )











        #@-node:ekr.20080112145409.179:createLeoGtkPrintMenu
        #@+node:ekr.20080112145409.180:createLeoGtkPrint
        def createLeoGtkPrint( self ):

            c = self.c
            import leoGtkPrint
            lsp = leoGtkPrint.leoGtkPrint( c )
            menu = lsp.getAsMenu()

            fmenu = self.getMenu( "File" )

            components = fmenu.getMenuComponents()

            x = 0
            for z in components:

                if hasattr( z, 'getText' ) and z.getText() == "Recent Files...":
                    break
                x += 1


            spot = x + 1


            sep = gtk.JSeparator()
            fmenu.add( sep, spot  )
            fmenu.add( menu, spot + 1 )


        #@-node:ekr.20080112145409.180:createLeoGtkPrint
        #@-node:ekr.20080112145409.177:print menu stuff...
        #@+node:ekr.20080112145409.181:plugin menu stuff...
        #@+node:ekr.20080112145409.182:createPluginMenu
        def createPluginMenu( self ):

            top = self.getMenu( 'top' )
            oline = self.getMenu( 'Outline' )
            ind = top.getComponentIndex( oline ) + 1
            import leoGtkPluginManager
            self.plugin_menu = pmenu = leoGtkPluginManager.createPluginsMenu()
            #self.plugin_menu = pmenu = gtk.JMenu( "Plugins" )
            top.add( pmenu, ind )
            #cpm = gtk.JMenuItem( "Plugin Manager" )
            #cpm.actionPerformed = self.createPluginManager
            #pmenu.add( cpm )
            #pmenu.addSeparator()


            #self.names_and_commands[ "Plugin Manager" ] = self.createPluginManager


        #@-node:ekr.20080112145409.182:createPluginMenu
        #@+node:ekr.20080112145409.183:createPluginManager
        def createPluginManager( self, event ):

            import leoGtkPluginManager as lspm
            lspm.topLevelMenu()

        #@-node:ekr.20080112145409.183:createPluginManager
        #@+node:ekr.20080112145409.184:getPluginMenu
        def getPluginMenu( self ):

            return self.plugin_menu
        #@-node:ekr.20080112145409.184:getPluginMenu
        #@-node:ekr.20080112145409.181:plugin menu stuff...
        #@+node:ekr.20080112145409.185:JythonShell stuff

        #@+node:ekr.20080112145409.186:openJythonShell
        def openJythonShell( self ):

            js = ijcl.getJythonShell()
            jd = js.getDelegate()
            config = g.app.config
            c = self.c

            import leoGtkFrame
            getColorInstance = leoGtkFrame.getColorInstance 

            colorconfig = js.getColorConfiguration()
            color = config.getColor( c, "jyshell_background" )
            colorconfig.setBackgroundColor( getColorInstance( color, awt.Color.WHITE ) )

            color = config.getColor( c, "jyshell_foreground" )
            colorconfig.setForegroundColor( getColorInstance( color, awt.Color.GRAY ) )

            color = config.getColor( c, "jyshell_keyword" )
            colorconfig.setKeywordColor( getColorInstance( color, awt.Color.GREEN ) )

            color = config.getColor( c, "jyshell_local" )
            colorconfig.setLocalColor( getColorInstance( color, awt.Color.ORANGE ) )

            color = config.getColor( c, "jyshell_ps1color" )
            colorconfig.setPromptOneColor( getColorInstance( color, awt.Color.BLUE ) )

            color = config.getColor( c, "jyshell_ps2color" )
            colorconfig.setPromptTwoColor( getColorInstance( color, awt.Color.GREEN ) )

            color = config.getColor( c, "jyshell_syntax" )
            colorconfig.setSyntaxColor( getColorInstance( color, awt.Color.RED ) )

            color = config.getColor( c, "jyshell_output" )
            colorconfig.setOutColor( getColorInstance( color, awt.Color.GRAY ) )

            color = config.getColor( c, "jyshell_error" )
            colorconfig.setErrColor( getColorInstance( color, awt.Color.RED ) )

            family = config.get( c, "jyshell_text_font_family", "family" )
            size = config.get( c, "jyshell_text_font_size", "size" )
            weight = config.get( c, "jyshell_text_font_weight", "weight" )
            slant = None
            font = config.getFontFromParams( c, "jyshell_text_font_family", "jyshell_text_font_size", None, "jyshell_text_font_weight")

            use_bgimage = g.app.config.getBool( c, "jyshell_background_image" )
            if use_bgimage:

                image_location = g.app.config.getString( c, "jyshell_image_location@as-filedialog" )
                test_if_exists = java.io.File( image_location )
                if test_if_exists.exists():
                    ii = gtk.ImageIcon( image_location )
                    alpha = g.app.config.getFloat( c, "jyshell_background_alpha" )
                    js.setBackgroundImage( ii.getImage(), float( alpha ) )

            if font:
                js.setFont( font )

            js.setVisible( True )
            widget = js.getWidget()
            log = self.c.frame.log    
            self.addMenuToJythonShell( js )
            log.addTab( "JythonShell", widget )
            log.selectTab( widget )


        #@-node:ekr.20080112145409.186:openJythonShell
        #@+node:ekr.20080112145409.187:addMenuToJythonShell
        def addMenuToJythonShell( self, js ):

            c = self.c
            jd = js.getDelegate()
            jmenu = gtk.JMenu( "Leo" )
            jd.addToMenu( jmenu )

            e = gtk.JMenuItem( "Execute Node As Script" )  
            e.actionPerformed = lambda event, jd = jd: self.fireNodeAsScript( event, jd )
            jmenu.add( e )

            p = gtk.JMenuItem( "Run Node in Pdb" )
            p.actionPerformed = self.getRunNodeInPdb( c, jd )
            jmenu.add( p )

            captext = "Capture Shell Input In Node"
            totext = "Turn Off Shell Input Capture"
            sc = gtk.JMenuItem( captext )
            import org.leo.JTextComponentOutputStream as jtcos
            class logcontrol:
                def __init__( self, menu ):
                    self.menu = menu
                    self.loging = False
                    self.ostream = jtcos( c.frame.body.editor.editor )

                def __call__( self, event ):  
                    menu = self.menu
                    loging = self.loging
                    if not loging:
                        js.addLogger( self.ostream )
                        menu.setText( totext )
                        self.loging = True
                    else:
                        js.removeLogger( self.ostream )
                        menu.setText( captext )
                        self.loging = False

            sc.actionPerformed = logcontrol( sc )           
            jmenu.add( sc )

            d = gtk.JMenuItem( "Detach Shell" )
            class detacher( java.util.concurrent.Callable ):

                def __init__( self, menu ):
                    self.menu = menu
                    self.embeded = True
                    js.setCloser( self )

                def call( self ):

                    if self.embeded:
                        log = c.frame.log
                        widget = js.getWidget()
                        log.removeTab( widget )
                    else:
                        widget = js.getWidget()
                        parent = widget.getTopLevelAncestor()
                        parent.dispose();

                def __call__( self, event ):
                    d = self.menu
                    text = d.getText()
                    if( text == "Detach Shell" ):
                        d.setText( "Retach Shell" )
                        jf = gtk.JFrame( "JythonShell" )
                        widget = js.getWidget()
                        log = c.frame.log 
                        log.removeTab( widget )
                        jf.add( widget )
                        jf.setSize( 500, 500 )
                        jf.visible = 1
                        self.embeded = False
                    else:
                        d.setText( "Detach Shell" )
                        widget = js.getWidget()
                        parent = widget.getTopLevelAncestor()
                        parent.dispose();
                        log = c.frame.log
                        log.addTab( "JythonShell", widget  )
                        log.selectTab( widget ) 
                        self.embeded = True

            d.actionPerformed = detacher( d )
            jmenu.add( d )    


        #@-node:ekr.20080112145409.187:addMenuToJythonShell
        #@+node:ekr.20080112145409.188:getInsertNodeIntoShell
        def getInsertNodeIntoShell( self, c, jd ):

            jm = gtk.JMenuItem( "Write Node Into Shell as Reference" )
            def writeNode( event ):

                cp = c.currentPosition()
                at = c.atFileCommands 
                c.fileCommands.assignFileIndices()
                at.write(cp.copy(),nosentinels=True,toString=True,scriptWrite=True)
                data = at.stringOutput

                jtf = self._GetReferenceName( jd, data )
                jtf.rmv_spot = jd.insertWidget( jtf )
                jtf.requestFocusInWindow()



            jm.actionPerformed = writeNode
            return jm
        #@-node:ekr.20080112145409.188:getInsertNodeIntoShell
        #@+node:ekr.20080112145409.189:getInsertReferenceIntoLeo
        def getInsertReferenceIntoLeo( self, jd ):

            jmi = gtk.JMenuItem( "Insert Reference As Node" )

            def action( event ):

                jtf = self._GetReferenceAsObject( jd, self.c )
                jtf.rmv_spot = jd.insertWidget( jtf )
                jtf.requestFocusInWindow()

            jmi.actionPerformed = action
            return jmi
        #@nonl
        #@-node:ekr.20080112145409.189:getInsertReferenceIntoLeo
        #@+node:ekr.20080112145409.190:getRunNodeInPdb
        def getRunNodeInPdb( self, c, jd ):

            def runInPdb( event ):

                cp = c.currentPosition()
                name = cp.headString()
                name = name.split()[ 0 ]
                at = c.atFileCommands 
                c.fileCommands.assignFileIndices()
                at.write(cp.copy(),nosentinels=True,toString=True,scriptWrite=True)
                data = at.stringOutput

                f = java.io.File.createTempFile( "leopdbrun", None )
                pw = java.io.PrintWriter( f )
                pw.println( "import pdb" )
                pw.println( "pdb.set_trace()" )
                for z in data.split( "\n" ):
                    pw.println( z )            
                pw.close()
                f.deleteOnExit()       
                l = java.util.Vector()
                l.add( "execfile( '%s', globals(), locals())" % f.getAbsolutePath() )
                jd.processAsScript( l )


            return runInPdb      
        #@-node:ekr.20080112145409.190:getRunNodeInPdb
        #@+node:ekr.20080112145409.191:fireNodeAsScript
        def fireNodeAsScript( self, event, jd ):

            c = self.c        
            cp = c.currentPosition()    
            at = c.atFileCommands 
            c.fileCommands.assignFileIndices()
            at.write(cp.copy(),nosentinels=True,toString=True,scriptWrite=True)
            data = at.stringOutput.split( '\n' ) 


            l = java.util.Vector()
            for z in data:
                l.add( java.lang.String( z ) )

            jd.processAsScript( l )
        #@nonl
        #@-node:ekr.20080112145409.191:fireNodeAsScript
        #@+node:ekr.20080112145409.192:class _GetReferenceName
        class _GetReferenceName( gtk.JTextField, aevent.KeyListener ):


            def __init__( self, jd, data ):
                gtk.JTextField.__init__( self )
                self.jd = jd
                self.data = data
                border = self.getBorder()
                tborder = sborder.TitledBorder( border )
                tborder.setTitle( "Choose Reference Name:" )
                self.setBorder( tborder )
                self.addKeyListener( self )
                self.rmv_spot = None

            def keyPressed( self, event ):

                kc = event.getKeyChar();
                if kc == '\n':
                    self.execute()
                elif java.lang.Character.isWhitespace( kc ):
                    event.consume

            def execute( self ):

                self.jd.setReference( self.getText(), self.data )
                if self.rmv_spot:
                    self.jd.remove( self.rmv_spot)
                self.jd.requestFocusInWindow()

            def keyTyped( self, event ):

                kc = event.getKeyChar()
                if kc == '\n': return
                elif java.lang.Character.isWhitespace( kc ):
                    event.consume()

            def keyReleased( self, event ):

                kc = event.getKeyChar()
                if kc == '\n': return
                elif java.lang.Character.isWhitespace( kc ):
                    event.consume()


        class _GetReferenceAsObject( _GetReferenceName ):

            def __init__( self, jd, c ):
                leoGtkMenu._GetReferenceName.__init__( self, jd, None )
                self.c = c
                border = self.getBorder()
                border.setTitle( "Which Reference To Insert:" )


            def execute( self ):

                ref = self.jd.getReference( self.getText() )
                if ref:
                    self.c.beginUpdate()
                    pos = self.c.currentPosition()
                    npos = pos.insertAfter()
                    npos.setHeadString( "Reference: %s" % self.getText() )
                    npos.setTnodeText( str( ref ) )
                    self.c.endUpdate()
                if self.rmv_spot:
                    self.jd.remove( self.rmv_spot )
        #@-node:ekr.20080112145409.192:class _GetReferenceName
        #@-node:ekr.20080112145409.185:JythonShell stuff
        #@+node:ekr.20080112145409.193:addUserGuide
        def addUserGuide( self ):

            help = self.getMenu( 'Help' )
            c = self.c
            help.addSeparator()
            jmi = gtk.JCheckBoxMenuItem( "View User Guide" )
            widgets = []
            def showUserGuide( event ):
                if jmi.getState() and not widgets:
                    import leoGtkLeoTutorial
                    lswlt = leoGtkLeoTutorial.leoGtkLeoTutorial()
                    widget = lswlt.getWidget()
                    widgets.append( widget )
                    c.frame.body.addTab( "User Guide", widget )
                elif jmi.getState() and widgets:
                    widget = widgets[ 0 ]
                    c.frame.body.addTab( "User Guide", widget )
                else:
                    widget = widgets[ 0 ]
                    c.frame.body.removeTab( widget )


            jmi.actionPerformed = showUserGuide
            help.add( jmi )
        #@-node:ekr.20080112145409.193:addUserGuide
        #@+node:ekr.20080112145409.194:createRecentFilesMenuItems (leoMenu)
        def createRecentFilesMenuItems (self):

            c = self.c ; frame = c.frame
            recentFilesMenu = self.getMenu("Recent Files...")

            # Delete all previous entries.
            if len( recentFilesMenu.getMenuComponents() ) != 0:
                deferable = lambda :self.delete_range(recentFilesMenu,0,len(c.recentFiles)+2)
                if not gtk.GtkUtilities.isEventDispatchThread():
                    dc = DefCallable( deferable )
                    ft = dc.wrappedAsFutureTask()
                    gtk.GtkUtilities.invokeAndWait( ft )
                else:
                    deferable()
            # Create the first two entries.
            table = (
                ("Clear Recent Files",None,c.clearRecentFiles),
                ("-",None,None))
            self.createMenuEntries(recentFilesMenu,table,init=True)

            # Create all the other entries.
            i = 3
            for name in c.recentFiles:
                def callback (event=None,c=c,name=name): # 12/9/03
                    c.openRecentFile(name)
                label = "%d %s" % (i-2,g.computeWindowTitle(name))
                self.add_command(recentFilesMenu,label=label,command=callback,underline=0)
                i += 1
        #@nonl
        #@-node:ekr.20080112145409.194:createRecentFilesMenuItems (leoMenu)
        #@+node:ekr.20080112145409.195:oops
        def oops (self):

            print "leoMenu oops:", g.callerName(2), "should be overridden in subclass"
        #@nonl
        #@-node:ekr.20080112145409.195:oops
        #@+node:ekr.20080112145409.196:Must be overridden in menu subclasses
        #@+node:ekr.20080112145409.197:9 Routines with Tk spellings
        def add_cascade (self,parent,label,menu,underline):

            menu.setText( label )

        def add_command (self,menu,**keys):

            if keys[ 'label' ] == "Open Python Window":
                keys[ 'command' ] = self.openJythonShell

            self.names_and_commands[ keys[ 'label' ] ] = keys[ 'command' ]

            action = self.MenuRunnable( keys[ 'label' ], keys[ 'command' ], self.c, self.executor )
            jmenu = gtk.JMenuItem( action )
            if keys.has_key( 'accelerator' ) and keys[ 'accelerator' ]:
                accel = keys[ 'accelerator' ]
                acc_list = accel.split( '+' )
                changeTo = { 'Alt': 'alt', 'Shift':'shift', #translation table
                             'Ctrl':'ctrl', 'UpArrow':'UP', 'DnArrow':'DOWN',
                             '-':'MINUS', '+':'PLUS', '=':'EQUALS',
                             '[':'typed [', ']':'typed ]', '{':'typed {',
                             '}':'typed }', 'Esc':'ESCAPE', '.':'typed .',
                              "`":"typed `", "BkSp":"BACK_SPACE"} #SEE java.awt.event.KeyEvent for further translations
                chg_list = []
                for z in acc_list:
                    if z in changeTo:
                        chg_list.append( changeTo[ z ] )
                    else:
                        chg_list.append( z )
                accelerator = " ".join( chg_list )
                ks = gtk.KeyStroke.getKeyStroke( accelerator )
                if ks:
                    self.keystrokes_and_actions[ ks ] = action
                    jmenu.setAccelerator( ks )
                else:
                    pass
            menu.add( jmenu )
            label = keys[ 'label' ]
            return jmenu

        def add_separator(self,menu):
            menu.addSeparator()

        def bind (self,bind_shortcut,callback):
            #self.oops() 
            pass

        def delete (self,menu,realItemName):
            self.oops()

        def delete_range (self,menu,n1,n2):


            items = menu.getMenuComponents()
            n3 = n1
            components = []
            while 1:
                if n3 == n2:
                    break
                item = menu.getMenuComponent( n3 )
                components.append( item )
                n3 += 1

            for z in components:
                menu.remove( z )


        def destroy (self,menu):
            self.oops()

        def insert_cascade (self,parent,index,label,menu,underline):
            self.oops()

        def new_menu(self,parent,tearoff=0):
            jm = gtk.JMenu( "1" )
            #jm = self.LeoMenu( "1" )
            parent.add( jm )
            #jm.setFont( self.font)
            return jm
        #@nonl
        #@-node:ekr.20080112145409.197:9 Routines with Tk spellings
        #@+node:ekr.20080112145409.198:7 Routines with new spellings
        def createMenuBar (self,frame):

            top = frame.top
            self.defineMenuTables()
            topMenu = gtk.JMenuBar()
            top.setJMenuBar( topMenu )
            topMenu.setFont( self.font )
            # Do gui-independent stuff.
            self.setMenu("top",topMenu)
            self.createMenusFromTables()
            self.createLeoGtkPrint()
            self.createPluginMenu()
            self.addUserGuide()

        def createOpenWithMenuFromTable (self,table):
            self.oops()

        def defineMenuCallback(self,command,name):
            return command

        def defineOpenWithMenuCallback(self,command):
            self.oops()

        def disableMenu (self,menu,name):
            for z in menu.getMenuComponents():
                if hasattr( z, "getText" ) and z.getText() == name:
                    z.setEnabled( False )

        def enableMenu (self,menu,name,val):
            for z in menu.getMenuComponents():
                if hasattr( z, "getText" ) and z.getText() == name:
                    z.setEnabled( bool( val ) )

        def setMenuLabel (self,menu,name,label,underline=-1, enabled = 1):

            item = ( menu, name, label, enabled )
            self.queue.offer( item )
            self.executor.submit( self.menu_changer )
        #@-node:ekr.20080112145409.198:7 Routines with new spellings
        #@+node:ekr.20080112145409.199:class MenuRunnable
        class MenuRunnable( gtk.AbstractAction, java.lang.Runnable): 

            def __init__( self, name, command, c , executor):
                gtk.AbstractAction.__init__( self, name )
                self.command = command
                self.c = c
                self.name = name
                self.executor = executor

            def run( self ):
                self.c.doCommand( self.command, self.name ) #command()

            def actionPerformed( self, aE ):

                #print self.command
                #if self.name == 'Save':
                self.executor.submit( self )

                #else:        
                #    se
        #@nonl
        #@-node:ekr.20080112145409.199:class MenuRunnable
        #@+node:ekr.20080112145409.200:class MenuExecuteOnSelect
        class MenuExecuteOnSelect( sevent.MenuListener ):

            def __init__( self, method ):
                self.method = method

            def menuSelected( self, me ):
                self.method()

            def menuCanceled( self, me ):
                pass

            def menuDeselected( self, me ):
                pass
        #@nonl
        #@-node:ekr.20080112145409.200:class MenuExecuteOnSelect
        #@+node:ekr.20080112145409.201:class LeoMenu
        class LeoMenu( gtk.JMenu ):

            def __init__( self, *args ):
                gtk.JMenu.__init__( self, *args )

            def add( self, *items ):
                if hasattr( items[ 0 ], "setFont" ):
                    items[ 0 ].setFont( self.getFont() )
                return self.super__add( *items )

        #@-node:ekr.20080112145409.201:class LeoMenu
        #@-node:ekr.20080112145409.196:Must be overridden in menu subclasses
        #@-others
    #@nonl
    #@-node:ekr.20080112145409.175:not ready yet
    #@-others
#@nonl
#@-node:ekr.20080112145409.173:class leoGtkMenu
#@+node:ekr.20080112145409.202:class leoSplash (java.lang.Runnable)
class leoSplash ( java.lang.Runnable ):

    #@    @+others
    #@+node:ekr.20080112145409.203:run (leoSplash)
    def run (self):

        g.trace(g.callers())

        self.splash = splash = gtk.JWindow()
        splash.setAlwaysOnTop(1)
        cpane = splash.getContentPane()
        rp = splash.getRootPane()
        tb = gtk.border.TitledBorder('Leo')
        tb.setTitleJustification(tb.CENTER)
        rp.setBorder(tb)
        splash.setBackground(awt.Color.ORANGE)
        dimension = awt.Dimension(400,400)
        splash.setPreferredSize(dimension)
        splash.setSize(400,400)

        sicon = g.os_path_join(g.app.loadDir,"..","Icons","Leosplash.GIF")
        ii = gtk.ImageIcon(sicon)
        image = gtk.JLabel(ii)
        image.setBackground(awt.Color.ORANGE)
        cpane.add(image)
        self.splashlabel = splashlabel = gtk.JLabel("Leo is starting....")
        splashlabel.setBackground(awt.Color.ORANGE)
        splashlabel.setForeground(awt.Color.BLUE)
        cpane.add(splashlabel,awt.BorderLayout.SOUTH)
        w, h = self._calculateCenteredPosition(splash)
        splash.setLocation(w,h)
        splash.visible = True
    #@-node:ekr.20080112145409.203:run (leoSplash)
    #@+node:ekr.20080112145409.204:utils
    def _calculateCenteredPosition( self, widget ):

        size = widget.getPreferredSize()
        height = size.height/2
        width = size.width/2
        h,w = self._getScreenPositionForDialog()
        height = h - height
        width = w - width
        return width, height

    def _getScreenPositionForDialog( self ):

        tk = awt.Toolkit.getDefaultToolkit()
        dim = tk.getScreenSize()
        h = dim.height/2
        w = dim.width/2
        return h, w   

    def setText( self, text ):  
        self.splashlabel.setText( text )

    def hide( self ):
        self.splash.visible = 0

    def toBack( self ):
        if self.splash.visible:
            self.splash.toBack()

    def toFront( self ):
        if self.splash.visible:
            self.splash.setAlwaysOnTop( 1 )
            self.splash.toFront()

    def isVisible( self ):
        return self.splash.visible
    #@-node:ekr.20080112145409.204:utils
    #@-others
#@-node:ekr.20080112145409.202:class leoSplash (java.lang.Runnable)
#@+node:ekr.20080112145409.205:class leoGtkLog (REWRITE)
class leoGtkLog (leoFrame.leoLog):

    """A class that represents the log pane of a gtk window."""

    #@    @+others
    #@+node:ekr.20080112145409.206:gtkLog Birth
    #@+node:ekr.20080112145409.207:gtkLog.__init__
    def __init__ (self,frame,parentFrame):

        # g.trace("leoGtkLog")

        # Call the base class constructor and calls createControl.
        leoFrame.leoLog.__init__(self,frame,parentFrame)

        self.c = c = frame.c # Also set in the base constructor, but we need it here.

        self.colorTags = []
            # The list of color names used as tags in present tab.
            # This gest switched by selectTab.

        self.wrap = g.choose(c.config.getBool('log_pane_wraps'),"word","none")

        # New in 4.4a2: The log pane is a Pmw.Notebook...

        self.nb = None      # The Pmw.Notebook that holds all the tabs.
        self.colorTagsDict = {} # Keys are page names.  Values are saved colorTags lists.
        self.menu = None # A menu that pops up on right clicks in the hull or in tabs.

        self.logCtrl = self.createControl(parentFrame)
        self.setFontFromConfig()
        self.setColorFromConfig()



    #@-node:ekr.20080112145409.207:gtkLog.__init__
    #@+node:ekr.20080112145409.208:gtkLog.createControl
    def createControl (self,parentFrame):

        c = self.c

        return self ### self.logCtrl

        # self.nb = Pmw.NoteBook(parentFrame,
            # borderwidth = 1, pagemargin = 0,
            # raisecommand = self.raiseTab,
            # lowercommand = self.lowerTab,
            # arrownavigation = 0,
        # )

        # menu = self.makeTabMenu(tabName=None)

        # def hullMenuCallback(event):
            # return self.onRightClick(event,menu)

        # self.nb.bind('<Button-3>',hullMenuCallback)

        # self.nb.pack(fill='both',expand=1)
        # self.selectTab('Log') # Create and activate the default tabs.

        # return self.logCtrl
    #@-node:ekr.20080112145409.208:gtkLog.createControl
    #@+node:ekr.20080112145409.209:gtkLog.finishCreate
    def finishCreate (self):

        # g.trace('gtkLog')

        c = self.c ; log = self

        c.searchCommands.openFindTab(show=False)
        c.spellCommands.openSpellTab()
        log.selectTab('Log')
    #@-node:ekr.20080112145409.209:gtkLog.finishCreate
    #@+node:ekr.20080112145409.210:gtkLog.createTextWidget
    def createTextWidget (self,parentFrame):

        self.logNumber += 1

        log = g.app.gui.plainTextWidget(
            parentFrame,name="log-%d" % self.logNumber,
            setgrid=0,wrap=self.wrap,bd=2,bg="white",relief="flat")

        # logBar = Tk.Scrollbar(parentFrame,name="logBar")

        # log['yscrollcommand'] = logBar.set
        # logBar['command'] = log.yview

        # logBar.pack(side="right", fill="y")
        # # rr 8/14/02 added horizontal elevator 
        # if self.wrap == "none": 
            # logXBar = Tk.Scrollbar( 
                # parentFrame,name='logXBar',orient="horizontal") 
            # log['xscrollcommand'] = logXBar.set 
            # logXBar['command'] = log.xview 
            # logXBar.pack(side="bottom", fill="x")
        # log.pack(expand=1, fill="both")

        return log
    #@-node:ekr.20080112145409.210:gtkLog.createTextWidget
    #@+node:ekr.20080112145409.211:gtkLog.makeTabMenu
    def makeTabMenu (self,tabName=None):

        '''Create a tab popup menu.'''

        # g.trace(tabName,g.callers())

        c = self.c
        # hull = self.nb.component('hull') # A Tk.Canvas.

        # menu = Tk.Menu(hull,tearoff=0)
        # menu.add_command(label='New Tab',command=self.newTabFromMenu)

        # if tabName:
            # # Important: tabName is the name when the tab is created.
            # # It is not affected by renaming, so we don't have to keep
            # # track of the correspondence between this name and what is in the label.
            # def deleteTabCallback():
                # return self.deleteTab(tabName)

            # label = g.choose(
                # tabName in ('Find','Spell'),'Hide This Tab','Delete This Tab')
            # menu.add_command(label=label,command=deleteTabCallback)

            # def renameTabCallback():
                # return self.renameTabFromMenu(tabName)

            # menu.add_command(label='Rename This Tab',command=renameTabCallback)

        # return menu
    #@-node:ekr.20080112145409.211:gtkLog.makeTabMenu
    #@-node:ekr.20080112145409.206:gtkLog Birth
    #@+node:ekr.20080112145409.212:Config & get/saveState
    #@+node:ekr.20080112145409.213:gtkLog.configureBorder & configureFont
    def configureBorder(self,border):

        self.logCtrl.configure(bd=border)

    def configureFont(self,font):

        self.logCtrl.configure(font=font)
    #@-node:ekr.20080112145409.213:gtkLog.configureBorder & configureFont
    #@+node:ekr.20080112145409.214:gtkLog.getFontConfig
    def getFontConfig (self):

        font = self.logCtrl.cget("font")
        # g.trace(font)
        return font
    #@-node:ekr.20080112145409.214:gtkLog.getFontConfig
    #@+node:ekr.20080112145409.215:gtkLog.restoreAllState
    def restoreAllState (self,d):

        '''Restore the log from a dict created by saveAllState.'''

        logCtrl = self.logCtrl

        # Restore the text.
        text = d.get('text')
        logCtrl.insert('end',text)

        # Restore all colors.
        colors = d.get('colors')
        for color in colors.keys():
            if color not in self.colorTags:
                self.colorTags.append(color)
                logCtrl.tag_config(color,foreground=color)
            items = list(colors.get(color))
            while items:
                start,stop = items[0],items[1]
                items = items[2:]
                logCtrl.tag_add(color,start,stop)
    #@-node:ekr.20080112145409.215:gtkLog.restoreAllState
    #@+node:ekr.20080112145409.216:gtkLog.saveAllState
    def saveAllState (self):

        '''Return a dict containing all data needed to recreate the log in another widget.'''

        logCtrl = self.logCtrl ; colors = {}

        # Save the text
        text = logCtrl.getAllText()

        # Save color tags.
        tag_names = logCtrl.tag_names()
        for tag in tag_names:
            if tag in self.colorTags:
                colors[tag] = logCtrl.tag_ranges(tag)

        d = {'text':text,'colors': colors}
        # g.trace('\n',g.dictToString(d))
        return d
    #@-node:ekr.20080112145409.216:gtkLog.saveAllState
    #@+node:ekr.20080112145409.217:gtkLog.setColorFromConfig
    def setColorFromConfig (self):

        c = self.c

        bg = c.config.getColor("log_pane_background_color") or 'white'

        try:
            self.logCtrl.configure(bg=bg)
        except:
            g.es("exception setting log pane background color")
            g.es_exception()
    #@-node:ekr.20080112145409.217:gtkLog.setColorFromConfig
    #@+node:ekr.20080112145409.218:gtkLog.setFontFromConfig
    def SetWidgetFontFromConfig (self,logCtrl=None):

        c = self.c

        if not logCtrl: logCtrl = self.logCtrl

        font = c.config.getFontFromParams(
            "log_text_font_family", "log_text_font_size",
            "log_text_font_slant", "log_text_font_weight",
            c.config.defaultLogFontSize)

        self.fontRef = font # ESSENTIAL: retain a link to font.
        ### logCtrl.configure(font=font)

        # g.trace("LOG",logCtrl.cget("font"),font.cget("family"),font.cget("weight"))

        bg = c.config.getColor("log_text_background_color")
        if bg:
            try: logCtrl.configure(bg=bg)
            except: pass

        fg = c.config.getColor("log_text_foreground_color")
        if fg:
            try: logCtrl.configure(fg=fg)
            except: pass

    setFontFromConfig = SetWidgetFontFromConfig # Renaming supresses a pychecker warning.
    #@-node:ekr.20080112145409.218:gtkLog.setFontFromConfig
    #@-node:ekr.20080112145409.212:Config & get/saveState
    #@+node:ekr.20080112145409.219:Focus & update (gtkLog)
    #@+node:ekr.20080112145409.220:gtkLog.onActivateLog
    def onActivateLog (self,event=None):

        try:
            self.c.setLog()
            self.frame.tree.OnDeactivate()
            self.c.logWantsFocus()
        except:
            g.es_event_exception("activate log")
    #@-node:ekr.20080112145409.220:gtkLog.onActivateLog
    #@+node:ekr.20080112145409.221:gtkLog.hasFocus
    def hasFocus (self):

        return self.c.get_focus() == self.logCtrl
    #@-node:ekr.20080112145409.221:gtkLog.hasFocus
    #@+node:ekr.20080112145409.222:forceLogUpdate
    def forceLogUpdate (self,s):

        if sys.platform == "darwin": # Does not work on MacOS X.
            try:
                print s, # Don't add a newline.
            except UnicodeError:
                # g.app may not be inited during scripts!
                print g.toEncodedString(s,'utf-8')
        else:
            self.logCtrl.update_idletasks()
    #@-node:ekr.20080112145409.222:forceLogUpdate
    #@-node:ekr.20080112145409.219:Focus & update (gtkLog)
    #@+node:ekr.20080112145409.223:put & putnl (gtkLog)
    #@+at 
    #@nonl
    # Printing uses self.logCtrl, so this code need not concern itself
    # with which tab is active.
    # 
    # Also, selectTab switches the contents of colorTags, so that is not 
    # concern.
    # It may be that Pmw will allow us to dispense with the colorTags logic...
    #@-at
    #@+node:ekr.20080112145409.224:put
    # All output to the log stream eventually comes here.
    def put (self,s,color=None,tabName='Log'):

        c = self.c

        # print 'gtkLog.put',self.c.shortFileName(),tabName,g.callers()

        if g.app.quitting or not c or not c.exists:
            return

        if tabName:
            self.selectTab(tabName)

        # if self.logCtrl:
            # 
            #@nonl
            #@<< put s to log control >>
            #@+node:ekr.20080112145409.225:<< put s to log control >>
            # if color:
                # if color not in self.colorTags:
                    # self.colorTags.append(color)
                    # self.logCtrl.tag_config(color,foreground=color)
                # self.logCtrl.insert("end",s)
                # self.logCtrl.tag_add(color,"end-%dc" % (len(s)+1),"end-1c")
                # self.logCtrl.tag_add("black","end")
            # else:
                # self.logCtrl.insert("end",s)

            # self.logCtrl.see('end')
            # self.forceLogUpdate(s)
            #@-node:ekr.20080112145409.225:<< put s to log control >>
            #@nl
            # self.logCtrl.update_idletasks()
        # else:
            # 
            #@nonl
            #@<< put s to logWaiting and print s >>
            #@+node:ekr.20080112145409.226:<< put s to logWaiting and print s >>
            # g.app.logWaiting.append((s,color),)

            # print "Null gtk log"

            # if type(s) == type(u""):
                # s = g.toEncodedString(s,"ascii")

            # print s
            #@-node:ekr.20080112145409.226:<< put s to logWaiting and print s >>
            #@nl
    #@-node:ekr.20080112145409.224:put
    #@+node:ekr.20080112145409.227:putnl
    def putnl (self,tabName='Log'):

        if g.app.quitting:
            return
        if tabName:
            self.selectTab(tabName)

        # if self.logCtrl:
            # self.logCtrl.insert("end",'\n')
            # self.logCtrl.see('end')
            # self.forceLogUpdate('\n')
        # else:
            # # Put a newline to logWaiting and print newline
            # g.app.logWaiting.append(('\n',"black"),)
            # print "Null gtk log"
            # print
    #@-node:ekr.20080112145409.227:putnl
    #@-node:ekr.20080112145409.223:put & putnl (gtkLog)
    #@+node:ekr.20080112145409.228:Tab (TkLog)
    #@+node:ekr.20080112145409.229:clearTab
    def clearTab (self,tabName,wrap='none'):

        self.selectTab(tabName,wrap=wrap)
        w = self.logCtrl
        w and w.delete(0,'end')
    #@-node:ekr.20080112145409.229:clearTab
    #@+node:ekr.20080112145409.230:createTab
    def createTab (self,tabName,createText=True,wrap='none'):

        # g.trace(tabName,wrap)

        c = self.c ; k = c.k

        # tabFrame = self.nb.add(tabName)
        # self.menu = self.makeTabMenu(tabName)
        # if createText:
            # 
            #@nonl
            #@<< Create the tab's text widget >>
            #@+node:ekr.20080112145409.231:<< Create the tab's text widget >>
            # w = self.createTextWidget(tabFrame)

            # # Set the background color.
            # configName = 'log_pane_%s_tab_background_color' % tabName
            # bg = c.config.getColor(configName) or 'MistyRose1'

            # if wrap not in ('none','char','word'): wrap = 'none'
            # try: w.configure(bg=bg,wrap=wrap)
            # except Exception: pass # Could be a user error.

            # self.SetWidgetFontFromConfig(logCtrl=w)

            # self.frameDict [tabName] = tabFrame
            # self.textDict [tabName] = w

            # # Switch to a new colorTags list.
            # if self.tabName:
                # self.colorTagsDict [self.tabName] = self.colorTags [:]

            # self.colorTags = ['black']
            # self.colorTagsDict [tabName] = self.colorTags
            #@-node:ekr.20080112145409.231:<< Create the tab's text widget >>
            #@nl
            # if tabName != 'Log':
                # # c.k doesn't exist when the log pane is created.
                # # k.makeAllBindings will call setTabBindings('Log')
                # self.setTabBindings(tabName)
        # else:
            # self.textDict [tabName] = None
            # self.frameDict [tabName] = tabFrame
    #@-node:ekr.20080112145409.230:createTab
    #@+node:ekr.20080112145409.232:cycleTabFocus
    def cycleTabFocus (self,event=None,stop_w = None):

        '''Cycle keyboard focus between the tabs in the log pane.'''

        c = self.c ; d = self.frameDict # Keys are page names. Values are Tk.Frames.
        w = d.get(self.tabName)
        # g.trace(self.tabName,w)
        values = d.values()
        if self.numberOfVisibleTabs() > 1:
            i = i2 = values.index(w) + 1
            if i == len(values): i = 0
            tabName = d.keys()[i]
            self.selectTab(tabName)
            return 
    #@nonl
    #@-node:ekr.20080112145409.232:cycleTabFocus
    #@+node:ekr.20080112145409.233:deleteTab
    def deleteTab (self,tabName,force=False):

        if tabName == 'Log':
            pass

        elif tabName in ('Find','Spell') and not force:
            self.selectTab('Log')

        # elif tabName in self.nb.pagenames():
            # # g.trace(tabName,force)
            # self.nb.delete(tabName)
            # self.colorTagsDict [tabName] = []
            # self.textDict [tabName] = None
            # self.frameDict [tabName] = None
            # self.tabName = None
            # self.selectTab('Log')

        # New in Leo 4.4b1.
        self.c.invalidateFocus()
        self.c.bodyWantsFocus()
    #@-node:ekr.20080112145409.233:deleteTab
    #@+node:ekr.20080112145409.234:hideTab
    def hideTab (self,tabName):

        # __pychecker__ = '--no-argsused' # tabName

        self.selectTab('Log')
    #@-node:ekr.20080112145409.234:hideTab
    #@+node:ekr.20080112145409.235:getSelectedTab
    def getSelectedTab (self):

        return self.tabName
    #@-node:ekr.20080112145409.235:getSelectedTab
    #@+node:ekr.20080112145409.236:lower/raiseTab
    def lowerTab (self,tabName):

        # if tabName:
            # b = self.nb.tab(tabName) # b is a Tk.Button.
            # b.config(bg='grey80')
        self.c.invalidateFocus()
        self.c.bodyWantsFocus()

    def raiseTab (self,tabName):

        # if tabName:
            # b = self.nb.tab(tabName) # b is a Tk.Button.
            # b.config(bg='LightSteelBlue1')
        self.c.invalidateFocus()
        self.c.bodyWantsFocus()
    #@-node:ekr.20080112145409.236:lower/raiseTab
    #@+node:ekr.20080112145409.237:numberOfVisibleTabs
    def numberOfVisibleTabs (self):

        return len([val for val in self.frameDict.values() if val != None])
    #@-node:ekr.20080112145409.237:numberOfVisibleTabs
    #@+node:ekr.20080112145409.238:renameTab
    def renameTab (self,oldName,newName):

        # g.trace('newName',newName)

        # label = self.nb.tab(oldName)
        # label.configure(text=newName)

        pass
    #@-node:ekr.20080112145409.238:renameTab
    #@+node:ekr.20080112145409.239:selectTab
    def selectTab (self,tabName,createText=True,wrap='none'):

        '''Create the tab if necessary and make it active.'''

        c = self.c

        # tabFrame = self.frameDict.get(tabName)
        # logCtrl = self.textDict.get(tabName)

        # if tabFrame and logCtrl:
            # # Switch to a new colorTags list.
            # newColorTags = self.colorTagsDict.get(tabName)
            # self.colorTagsDict [self.tabName] = self.colorTags [:]
            # self.colorTags = newColorTags
        # elif not tabFrame:
            # self.createTab(tabName,createText=createText,wrap=wrap)

        # self.nb.selectpage(tabName)
        # # Update the status vars.
        # self.tabName = tabName
        # self.logCtrl = self.textDict.get(tabName)
        # self.tabFrame = self.frameDict.get(tabName)

        # if 0: # Absolutely do not do this here!  It is a cause of the 'sticky focus' problem.
            # c.widgetWantsFocusNow(self.logCtrl)
        # return tabFrame
    #@-node:ekr.20080112145409.239:selectTab
    #@+node:ekr.20080112145409.240:setTabBindings
    def setTabBindings (self,tabName):

        c = self.c ; k = c.k
        # tab = self.nb.tab(tabName)
        # w = self.textDict.get(tabName)

        # # Send all event in the text area to the master handlers.
        # for kind,handler in (
            # ('<Key>',       k.masterKeyHandler),
            # ('<Button-1>',  k.masterClickHandler),
            # ('<Button-3>',  k.masterClick3Handler),
        # ):
            # w.bind(kind,handler)

        # # Clicks in the tab area are harmless: use the old code.
        # def tabMenuRightClickCallback(event,menu=self.menu):
            # return self.onRightClick(event,menu)

        # def tabMenuClickCallback(event,tabName=tabName):
            # return self.onClick(event,tabName)

        # tab.bind('<Button-1>',tabMenuClickCallback)
        # tab.bind('<Button-3>',tabMenuRightClickCallback)

        # k.completeAllBindingsForWidget(w)
    #@-node:ekr.20080112145409.240:setTabBindings
    #@+node:ekr.20080112145409.241:Tab menu callbacks & helpers
    #@+node:ekr.20080112145409.242:onRightClick & onClick
    def onRightClick (self,event,menu):

        c = self.c
        menu.post(event.x_root,event.y_root)


    def onClick (self,event,tabName):

        self.selectTab(tabName)
    #@-node:ekr.20080112145409.242:onRightClick & onClick
    #@+node:ekr.20080112145409.243:newTabFromMenu
    def newTabFromMenu (self,tabName='Log'):

        self.selectTab(tabName)

        # This is called by getTabName.
        def selectTabCallback (newName):
            return self.selectTab(newName)

        self.getTabName(selectTabCallback)
    #@-node:ekr.20080112145409.243:newTabFromMenu
    #@+node:ekr.20080112145409.244:renameTabFromMenu
    def renameTabFromMenu (self,tabName):

        if tabName in ('Log','Completions'):
            g.es('can not rename %s tab' % (tabName),color='blue')
        else:
            def renameTabCallback (newName):
                return self.renameTab(tabName,newName)

            self.getTabName(renameTabCallback)
    #@-node:ekr.20080112145409.244:renameTabFromMenu
    #@+node:ekr.20080112145409.245:getTabName
    def getTabName (self,exitCallback):

        canvas = self.nb.component('hull')

        # Overlay what is there!
        c = self.c
        f = Tk.Frame(canvas)
        f.pack(side='top',fill='both',expand=1)

        row1 = Tk.Frame(f)
        row1.pack(side='top',expand=0,fill='x',pady=10)
        row2 = Tk.Frame(f)
        row2.pack(side='top',expand=0,fill='x')

        Tk.Label(row1,text='Tab name').pack(side='left')

        e = Tk.Entry(row1,background='white')
        e.pack(side='left')

        def getNameCallback (event=None):
            s = e.get().strip()
            f.pack_forget()
            if s: exitCallback(s)

        def closeTabNameCallback (event=None):
            f.pack_forget()

        b = Tk.Button(row2,text='Ok',width=6,command=getNameCallback)
        b.pack(side='left',padx=10)

        b = Tk.Button(row2,text='Cancel',width=6,command=closeTabNameCallback)
        b.pack(side='left')

        g.app.gui.set_focus(c,e)
        e.bind('<Return>',getNameCallback)
    #@-node:ekr.20080112145409.245:getTabName
    #@-node:ekr.20080112145409.241:Tab menu callbacks & helpers
    #@-node:ekr.20080112145409.228:Tab (TkLog)
    #@+node:ekr.20080112145409.246:gtkLog color tab stuff
    def createColorPicker (self,tabName):

        log = self

        #@    << define colors >>
        #@+node:ekr.20080112145409.247:<< define colors >>
        colors = (
            "gray60", "gray70", "gray80", "gray85", "gray90", "gray95",
            "snow1", "snow2", "snow3", "snow4", "seashell1", "seashell2",
            "seashell3", "seashell4", "AntiqueWhite1", "AntiqueWhite2", "AntiqueWhite3",
            "AntiqueWhite4", "bisque1", "bisque2", "bisque3", "bisque4", "PeachPuff1",
            "PeachPuff2", "PeachPuff3", "PeachPuff4", "NavajoWhite1", "NavajoWhite2",
            "NavajoWhite3", "NavajoWhite4", "LemonChiffon1", "LemonChiffon2",
            "LemonChiffon3", "LemonChiffon4", "cornsilk1", "cornsilk2", "cornsilk3",
            "cornsilk4", "ivory1", "ivory2", "ivory3", "ivory4", "honeydew1", "honeydew2",
            "honeydew3", "honeydew4", "LavenderBlush1", "LavenderBlush2",
            "LavenderBlush3", "LavenderBlush4", "MistyRose1", "MistyRose2",
            "MistyRose3", "MistyRose4", "azure1", "azure2", "azure3", "azure4",
            "SlateBlue1", "SlateBlue2", "SlateBlue3", "SlateBlue4", "RoyalBlue1",
            "RoyalBlue2", "RoyalBlue3", "RoyalBlue4", "blue1", "blue2", "blue3", "blue4",
            "DodgerBlue1", "DodgerBlue2", "DodgerBlue3", "DodgerBlue4", "SteelBlue1",
            "SteelBlue2", "SteelBlue3", "SteelBlue4", "DeepSkyBlue1", "DeepSkyBlue2",
            "DeepSkyBlue3", "DeepSkyBlue4", "SkyBlue1", "SkyBlue2", "SkyBlue3",
            "SkyBlue4", "LightSkyBlue1", "LightSkyBlue2", "LightSkyBlue3",
            "LightSkyBlue4", "SlateGray1", "SlateGray2", "SlateGray3", "SlateGray4",
            "LightSteelBlue1", "LightSteelBlue2", "LightSteelBlue3",
            "LightSteelBlue4", "LightBlue1", "LightBlue2", "LightBlue3",
            "LightBlue4", "LightCyan1", "LightCyan2", "LightCyan3", "LightCyan4",
            "PaleTurquoise1", "PaleTurquoise2", "PaleTurquoise3", "PaleTurquoise4",
            "CadetBlue1", "CadetBlue2", "CadetBlue3", "CadetBlue4", "turquoise1",
            "turquoise2", "turquoise3", "turquoise4", "cyan1", "cyan2", "cyan3", "cyan4",
            "DarkSlateGray1", "DarkSlateGray2", "DarkSlateGray3",
            "DarkSlateGray4", "aquamarine1", "aquamarine2", "aquamarine3",
            "aquamarine4", "DarkSeaGreen1", "DarkSeaGreen2", "DarkSeaGreen3",
            "DarkSeaGreen4", "SeaGreen1", "SeaGreen2", "SeaGreen3", "SeaGreen4",
            "PaleGreen1", "PaleGreen2", "PaleGreen3", "PaleGreen4", "SpringGreen1",
            "SpringGreen2", "SpringGreen3", "SpringGreen4", "green1", "green2",
            "green3", "green4", "chartreuse1", "chartreuse2", "chartreuse3",
            "chartreuse4", "OliveDrab1", "OliveDrab2", "OliveDrab3", "OliveDrab4",
            "DarkOliveGreen1", "DarkOliveGreen2", "DarkOliveGreen3",
            "DarkOliveGreen4", "khaki1", "khaki2", "khaki3", "khaki4",
            "LightGoldenrod1", "LightGoldenrod2", "LightGoldenrod3",
            "LightGoldenrod4", "LightYellow1", "LightYellow2", "LightYellow3",
            "LightYellow4", "yellow1", "yellow2", "yellow3", "yellow4", "gold1", "gold2",
            "gold3", "gold4", "goldenrod1", "goldenrod2", "goldenrod3", "goldenrod4",
            "DarkGoldenrod1", "DarkGoldenrod2", "DarkGoldenrod3", "DarkGoldenrod4",
            "RosyBrown1", "RosyBrown2", "RosyBrown3", "RosyBrown4", "IndianRed1",
            "IndianRed2", "IndianRed3", "IndianRed4", "sienna1", "sienna2", "sienna3",
            "sienna4", "burlywood1", "burlywood2", "burlywood3", "burlywood4", "wheat1",
            "wheat2", "wheat3", "wheat4", "tan1", "tan2", "tan3", "tan4", "chocolate1",
            "chocolate2", "chocolate3", "chocolate4", "firebrick1", "firebrick2",
            "firebrick3", "firebrick4", "brown1", "brown2", "brown3", "brown4", "salmon1",
            "salmon2", "salmon3", "salmon4", "LightSalmon1", "LightSalmon2",
            "LightSalmon3", "LightSalmon4", "orange1", "orange2", "orange3", "orange4",
            "DarkOrange1", "DarkOrange2", "DarkOrange3", "DarkOrange4", "coral1",
            "coral2", "coral3", "coral4", "tomato1", "tomato2", "tomato3", "tomato4",
            "OrangeRed1", "OrangeRed2", "OrangeRed3", "OrangeRed4", "red1", "red2", "red3",
            "red4", "DeepPink1", "DeepPink2", "DeepPink3", "DeepPink4", "HotPink1",
            "HotPink2", "HotPink3", "HotPink4", "pink1", "pink2", "pink3", "pink4",
            "LightPink1", "LightPink2", "LightPink3", "LightPink4", "PaleVioletRed1",
            "PaleVioletRed2", "PaleVioletRed3", "PaleVioletRed4", "maroon1",
            "maroon2", "maroon3", "maroon4", "VioletRed1", "VioletRed2", "VioletRed3",
            "VioletRed4", "magenta1", "magenta2", "magenta3", "magenta4", "orchid1",
            "orchid2", "orchid3", "orchid4", "plum1", "plum2", "plum3", "plum4",
            "MediumOrchid1", "MediumOrchid2", "MediumOrchid3", "MediumOrchid4",
            "DarkOrchid1", "DarkOrchid2", "DarkOrchid3", "DarkOrchid4", "purple1",
            "purple2", "purple3", "purple4", "MediumPurple1", "MediumPurple2",
            "MediumPurple3", "MediumPurple4", "thistle1", "thistle2", "thistle3",
            "thistle4" )
        #@-node:ekr.20080112145409.247:<< define colors >>
        #@nl

        parent = log.frameDict.get(tabName)
        w = log.textDict.get(tabName)
        w.pack_forget()

        colors = list(colors)
        bg = parent.cget('background')

        outer = Tk.Frame(parent,background=bg)
        outer.pack(side='top',fill='both',expand=1,pady=10)

        f = Tk.Frame(outer)
        f.pack(side='top',expand=0,fill='x')
        f1 = Tk.Frame(f) ; f1.pack(side='top',expand=0,fill='x')
        f2 = Tk.Frame(f) ; f2.pack(side='top',expand=1,fill='x')
        f3 = Tk.Frame(f) ; f3.pack(side='top',expand=1,fill='x')

        label = g.app.gui.plainTextWidget(f1,height=1,width=20)
        label.insert('1.0','Color name or value...')
        label.pack(side='left',pady=6)

        #@    << create optionMenu and callback >>
        #@+node:ekr.20080112145409.248:<< create optionMenu and callback >>
        colorBox = Pmw.ComboBox(f2,scrolledlist_items=colors)
        colorBox.pack(side='left',pady=4)

        def colorCallback (newName): 
            label.delete('1.0','end')
            label.insert('1.0',newName)
            try:
                for theFrame in (parent,outer,f,f1,f2,f3):
                    theFrame.configure(background=newName)
            except: pass # Ignore invalid names.

        colorBox.configure(selectioncommand=colorCallback)
        #@-node:ekr.20080112145409.248:<< create optionMenu and callback >>
        #@nl
        #@    << create picker button and callback >>
        #@+node:ekr.20080112145409.249:<< create picker button and callback >>
        def pickerCallback ():
            rgb,val = gtkColorChooser.askcolor(parent=parent,initialcolor=f.cget('background'))
            if rgb or val:
                # label.configure(text=val)
                label.delete('1.0','end')
                label.insert('1.0',val)
                for theFrame in (parent,outer,f,f1,f2,f3):
                    theFrame.configure(background=val)

        b = Tk.Button(f3,text="Color Picker...",
            command=pickerCallback,background=bg)
        b.pack(side='left',pady=4)
        #@-node:ekr.20080112145409.249:<< create picker button and callback >>
        #@nl
    #@-node:ekr.20080112145409.246:gtkLog color tab stuff
    #@+node:ekr.20080112145409.250:gtkLog font tab stuff
    #@+node:ekr.20080112145409.251:createFontPicker
    def createFontPicker (self,tabName):

        log = self
        parent = log.frameDict.get(tabName)
        w = log.textDict.get(tabName)
        w.pack_forget()

        bg = parent.cget('background')
        font = self.getFont()
        #@    << create the frames >>
        #@+node:ekr.20080112145409.252:<< create the frames >>
        f = Tk.Frame(parent,background=bg) ; f.pack (side='top',expand=0,fill='both')
        f1 = Tk.Frame(f,background=bg)     ; f1.pack(side='top',expand=1,fill='x')
        f2 = Tk.Frame(f,background=bg)     ; f2.pack(side='top',expand=1,fill='x')
        f3 = Tk.Frame(f,background=bg)     ; f3.pack(side='top',expand=1,fill='x')
        f4 = Tk.Frame(f,background=bg)     ; f4.pack(side='top',expand=1,fill='x')
        #@-node:ekr.20080112145409.252:<< create the frames >>
        #@nl
        #@    << create the family combo box >>
        #@+node:ekr.20080112145409.253:<< create the family combo box >>
        names = gtkFont.families()
        names = list(names)
        names.sort()
        names.insert(0,'<None>')

        self.familyBox = familyBox = Pmw.ComboBox(f1,
            labelpos="we",label_text='Family:',label_width=10,
            label_background=bg,
            arrowbutton_background=bg,
            scrolledlist_items=names)

        familyBox.selectitem(0)
        familyBox.pack(side="left",padx=2,pady=2)
        #@-node:ekr.20080112145409.253:<< create the family combo box >>
        #@nl
        #@    << create the size entry >>
        #@+node:ekr.20080112145409.254:<< create the size entry >>
        Tk.Label(f2,text="Size:",width=10,background=bg).pack(side="left")

        sizeEntry = Tk.Entry(f2,width=4)
        sizeEntry.insert(0,'12')
        sizeEntry.pack(side="left",padx=2,pady=2)
        #@-node:ekr.20080112145409.254:<< create the size entry >>
        #@nl
        #@    << create the weight combo box >>
        #@+node:ekr.20080112145409.255:<< create the weight combo box >>
        weightBox = Pmw.ComboBox(f3,
            labelpos="we",label_text="Weight:",label_width=10,
            label_background=bg,
            arrowbutton_background=bg,
            scrolledlist_items=['normal','bold'])

        weightBox.selectitem(0)
        weightBox.pack(side="left",padx=2,pady=2)
        #@-node:ekr.20080112145409.255:<< create the weight combo box >>
        #@nl
        #@    << create the slant combo box >>
        #@+node:ekr.20080112145409.256:<< create the slant combo box>>
        slantBox = Pmw.ComboBox(f4,
            labelpos="we",label_text="Slant:",label_width=10,
            label_background=bg,
            arrowbutton_background=bg,
            scrolledlist_items=['roman','italic'])

        slantBox.selectitem(0)
        slantBox.pack(side="left",padx=2,pady=2)
        #@-node:ekr.20080112145409.256:<< create the slant combo box>>
        #@nl
        #@    << create the sample text widget >>
        #@+node:ekr.20080112145409.257:<< create the sample text widget >>
        self.sampleWidget = sample = g.app.gui.plainTextWidget(f,height=20,width=80,font=font)
        sample.pack(side='left')

        s = 'The quick brown fox\njumped over the lazy dog.\n0123456789'
        sample.insert(0,s)
        #@-node:ekr.20080112145409.257:<< create the sample text widget >>
        #@nl
        #@    << create and bind the callbacks >>
        #@+node:ekr.20080112145409.258:<< create and bind the callbacks >>
        def fontCallback(event=None):
            self.setFont(familyBox,sizeEntry,slantBox,weightBox,sample)

        for w in (familyBox,slantBox,weightBox):
            w.configure(selectioncommand=fontCallback)

        sizeEntry.bind('<Return>',fontCallback)
        #@-node:ekr.20080112145409.258:<< create and bind the callbacks >>
        #@nl
        self.createBindings()
    #@-node:ekr.20080112145409.251:createFontPicker
    #@+node:ekr.20080112145409.259:createBindings (fontPicker)
    def createBindings (self):

        c = self.c ; k = c.k

        table = (
            ('<Button-1>',  k.masterClickHandler),
            ('<Double-1>',  k.masterClickHandler),
            ('<Button-3>',  k.masterClickHandler),
            ('<Double-3>',  k.masterClickHandler),
            ('<Key>',       k.masterKeyHandler),
            ("<Escape>",    self.hideFontTab),
        )

        w = self.sampleWidget
        for event, callback in table:
            w.bind(event,callback)

        k.completeAllBindingsForWidget(w)
    #@-node:ekr.20080112145409.259:createBindings (fontPicker)
    #@+node:ekr.20080112145409.260:getFont
    def getFont(self,family=None,size=12,slant='roman',weight='normal'):

        try:
            return gtkFont.Font(family=family,size=size,slant=slant,weight=weight)
        except Exception:
            g.es("exception setting font")
            g.es("family,size,slant,weight:",family,size,slant,weight)
            # g.es_exception() # This just confuses people.
            return g.app.config.defaultFont
    #@-node:ekr.20080112145409.260:getFont
    #@+node:ekr.20080112145409.261:setFont
    def setFont(self,familyBox,sizeEntry,slantBox,weightBox,label):

        d = {}
        for box,key in (
            (familyBox, 'family'),
            (None,      'size'),
            (slantBox,  'slant'),
            (weightBox, 'weight'),
        ):
            if box: val = box.get()
            else:
                val = sizeEntry.get().strip() or ''
                try: int(val)
                except ValueError: val = None
            if val and val.lower() not in ('none','<none>',):
                d[key] = val

        family=d.get('family',None)
        size=d.get('size',12)
        weight=d.get('weight','normal')
        slant=d.get('slant','roman')
        font = self.getFont(family,size,slant,weight)
        label.configure(font=font)
    #@-node:ekr.20080112145409.261:setFont
    #@+node:ekr.20080112145409.262:hideFontTab
    def hideFontTab (self,event=None):

        c = self.c
        c.frame.log.selectTab('Log')
        c.bodyWantsFocus()
    #@-node:ekr.20080112145409.262:hideFontTab
    #@-node:ekr.20080112145409.250:gtkLog font tab stuff
    #@-others
#@-node:ekr.20080112145409.205:class leoGtkLog (REWRITE)
#@+node:ekr.20080112145409.263:class leoGtkTreeTab (REWRITE)
class leoGtkTreeTab (leoFrame.leoTreeTab):

    '''A class representing a tabbed outline pane drawn with gtk.'''

    #@    @+others
    #@+node:ekr.20080112145409.264: Birth & death
    #@+node:ekr.20080112145409.265: ctor (leoTreeTab)
    def __init__ (self,c,parentFrame,chapterController):

        leoFrame.leoTreeTab.__init__ (self,c,chapterController,parentFrame)
            # Init the base class.  Sets self.c, self.cc and self.parentFrame.

        self.tabNames = [] # The list of tab names.  Changes when tabs are renamed.

        self.createControl()
    #@-node:ekr.20080112145409.265: ctor (leoTreeTab)
    #@+node:ekr.20080112145409.266:tt.createControl
    def createControl (self):

        tt = self ; c = tt.c

        # Create the main container.
        tt.frame = Tk.Frame(c.frame.iconFrame)
        tt.frame.pack(side="left")

        # Create the chapter menu.
        self.chapterVar = var = Tk.StringVar()
        var.set('main')

        tt.chapterMenu = menu = Pmw.OptionMenu(tt.frame,
            labelpos = 'w', label_text = 'chapter',
            menubutton_textvariable = var,
            items = [],
            command = tt.selectTab,
        )
        menu.pack(side='left',padx=5)
    #@nonl
    #@-node:ekr.20080112145409.266:tt.createControl
    #@-node:ekr.20080112145409.264: Birth & death
    #@+node:ekr.20080112145409.267:Tabs...
    #@+node:ekr.20080112145409.268:tt.createTab
    def createTab (self,tabName,select=True):

        tt = self

        if tabName not in tt.tabNames:
            tt.tabNames.append(tabName)
            tt.setNames()
    #@-node:ekr.20080112145409.268:tt.createTab
    #@+node:ekr.20080112145409.269:tt.destroyTab
    def destroyTab (self,tabName):

        tt = self

        if tabName in tt.tabNames:
            tt.tabNames.remove(tabName)
            tt.setNames()
    #@-node:ekr.20080112145409.269:tt.destroyTab
    #@+node:ekr.20080112145409.270:tt.selectTab
    def selectTab (self,tabName):

        tt = self

        if tabName not in self.tabNames:
            tt.createTab(tabName)

        tt.cc.selectChapterByName(tabName)
    #@-node:ekr.20080112145409.270:tt.selectTab
    #@+node:ekr.20080112145409.271:tt.setTabLabel
    def setTabLabel (self,tabName):

        tt = self
        tt.chapterVar.set(tabName)
    #@-node:ekr.20080112145409.271:tt.setTabLabel
    #@+node:ekr.20080112145409.272:tt.setNames
    def setNames (self):

        '''Recreate the list of items.'''

        tt = self
        names = tt.tabNames[:]
        if 'main' in names: names.remove('main')
        names.sort()
        names.insert(0,'main')
        tt.chapterMenu.setitems(names)
    #@-node:ekr.20080112145409.272:tt.setNames
    #@-node:ekr.20080112145409.267:Tabs...
    #@-others
#@nonl
#@-node:ekr.20080112145409.263:class leoGtkTreeTab (REWRITE)
#@+node:ekr.20080112145409.273:class leoGtkTextWidget (revise)
class leoGtkTextWidget: ### (leoFrame.baseTextWidget):

    '''A class to wrap the Tk.Text widget.
    Translates Python (integer) indices to and from Tk (string) indices.

    This class inherits almost all gtkText methods: you call use them as usual.'''

    # The signatures of tag_add and insert are different from the Tk.Text signatures.
    # __pychecker__ = '--no-override' # suppress warning about changed signature.

    def __repr__(self):
        name = hasattr(self,'_name') and self._name or '<no name>'
        return 'gtkTextWidget id: %s name: %s' % (id(self),name)

    #@    @+others
    #@+node:ekr.20080112145409.274:gtkTextWidget.__init__

    def __init__ (self,parentFrame,*args,**keys):

        # Create the actual gui widget.
        ### self.widget = Tk.Text(*args,**keys)

        ### To do: probably need to subclass JTextField so we can inject ivars.

        self.widget = w = gtk.JTextField() ###preferredSize=(200,20))
        parentFrame.contentPane.add(w)

        ### Probably should be somewhere else.
        parentFrame.pack()
        parentFrame.show()

        # Init the base class.
        # name = keys.get('name') or '<unknown gtkTextWidget>'
        # leoFrame.baseTextWidget.__init__(self,c=c,
            # baseClassName='gtkTextWidget',name=name,widget=self.widget)

        # self.defaultFont = font = wx.Font(pointSize=10,
            # family = wx.FONTFAMILY_TELETYPE, # wx.FONTFAMILY_ROMAN,
            # style  = wx.FONTSTYLE_NORMAL,
            # weight = wx.FONTWEIGHT_NORMAL,)
    #@-node:ekr.20080112145409.274:gtkTextWidget.__init__
    #@+node:ekr.20080112145409.275:bindings (not used)
    # Specify the names of widget-specific methods.
    # These particular names are the names of wx.TextCtrl methods.

    # def _appendText(self,s):            return self.widget.insert(s)
    # def _get(self,i,j):                 return self.widget.get(i,j)
    # def _getAllText(self):              return self.widget.get('1.0','end')
    # def _getFocus(self):                return self.widget.focus_get()
    # def _getInsertPoint(self):          return self.widget.index('insert')
    # def _getLastPosition(self):         return self.widget.index('end')
    # def _getSelectedText(self):         return self.widget.get('sel.start','sel.end')
    # def _getSelectionRange(self):       return self.widget.index('sel.start'),self.widget.index('sel.end')
    # def _hitTest(self,pos):             pass ###
    # def _insertText(self,i,s):          return self.widget.insert(i,s)
    # def _scrollLines(self,n):           pass ###
    # def _see(self,i):                   return self.widget.see(i)
    # def _setAllText(self,s):            self.widget.delete('1.0','end') ; self.widget.insert('1.0',s)
    # def _setBackgroundColor(self,color): return self.widget.configure(background=color)
    # def _setFocus(self):                return self.widget.focus_set()
    # def _setInsertPoint(self,i):        return self.widget.mark_set('insert',i)
    # # def _setSelectionRange(self,i,j):   return self.widget.SetSelection(i,j)
    #@-node:ekr.20080112145409.275:bindings (not used)
    #@+node:ekr.20080112145409.276:Index conversion (gtkTextWidget)
    #@+node:ekr.20080112145409.277:w.toGuiIndex
    def toGuiIndex (self,i,s=None):
        '''Convert a Python index to a Tk index as needed.'''
        w = self
        if i is None:
            g.trace('can not happen: i is None',g.callers())
            return '1.0'
        elif type(i) == type(99):
            # The 's' arg supports the threaded colorizer.
            if s is None:
                # This *must* be 'end-1c', even if other code must change.
                s = '' ### s = Tk.Text.get(w,'1.0','end-1c')
            row,col = g.convertPythonIndexToRowCol(s,i)
            i = '%s.%s' % (row+1,col)
            # g.trace(len(s),i,repr(s))
        else:
            try:
                i = 0 ### i = Tk.Text.index(w,i)
            except Exception:
                # g.es_exception()
                g.trace('Tk.Text.index failed:',repr(i),g.callers())
                i = '1.0'
        return i
    #@nonl
    #@-node:ekr.20080112145409.277:w.toGuiIndex
    #@+node:ekr.20080112145409.278:w.toPythonIndex
    def toPythonIndex (self,i):
        '''Convert a Tk index to a Python index as needed.'''
        w =self
        if i is None:
            g.trace('can not happen: i is None')
            return 0
        elif type(i) in (type('a'),type(u'a')):
            s = '' ### s = Tk.Text.get(w,'1.0','end') # end-1c does not work.
            i = '1.0' ### i = Tk.Text.index(w,i) # Convert to row/column form.
            row,col = i.split('.')
            row,col = int(row),int(col)
            row -= 1
            i = g.convertRowColToPythonIndex(s,row,col)
            #g.es_print(i)
        return i
    #@-node:ekr.20080112145409.278:w.toPythonIndex
    #@+node:ekr.20080112145409.279:w.rowColToGuiIndex
    # This method is called only from the colorizer.
    # It provides a huge speedup over naive code.

    def rowColToGuiIndex (self,s,row,col):

        return '%s.%s' % (row+1,col)
    #@nonl
    #@-node:ekr.20080112145409.279:w.rowColToGuiIndex
    #@-node:ekr.20080112145409.276:Index conversion (gtkTextWidget)
    #@+node:ekr.20080112145409.280:getName (Tk.Text)
    def getName (self):

        w = self
        return hasattr(w,'_name') and w._name or repr(w)
    #@nonl
    #@-node:ekr.20080112145409.280:getName (Tk.Text)
    #@+node:ekr.20080112145409.281:_setSelectionRange
    if 0:
        def _setSelectionRange (self,i,j,insert=None):

            w = self.widget

            i,j = w.toGuiIndex(i),w.toGuiIndex(j)

            # g.trace('i,j,insert',repr(i),repr(j),repr(insert),g.callers())

            # g.trace('i,j,insert',i,j,repr(insert))
            if w.compare(w,i, ">", j): i,j = j,i
            w.tag_remove(w,"sel","1.0",i)
            w.tag_add(w,"sel",i,j)
            w.tag_remove(w,"sel",j,"end")

            if insert is not None:
                w.setInsertPoint(insert)
    #@-node:ekr.20080112145409.281:_setSelectionRange
    #@+node:ekr.20080112145409.282:Wrapper methods (gtkTextWidget)
    #@+node:ekr.20080112145409.283:after_idle (new)
    def after_idle(self,*args,**keys):

        pass
    #@-node:ekr.20080112145409.283:after_idle (new)
    #@+node:ekr.20080112145409.284:bind (new)
    def bind (self,*args,**keys):

        pass
    #@-node:ekr.20080112145409.284:bind (new)
    #@+node:ekr.20080112145409.285:delete
    def delete(self,i,j=None):

        w = self
        i = w.toGuiIndex(i)

        if j is None:
            pass ### Tk.Text.delete(w,i)
        else:
            j = w.toGuiIndex(j)
            pass ### Tk.Text.delete(w,i,j)
    #@-node:ekr.20080112145409.285:delete
    #@+node:ekr.20080112145409.286:flashCharacter
    def flashCharacter(self,i,bg='white',fg='red',flashes=3,delay=75): # gtkTextWidget.

        w = self

        # def addFlashCallback(w,count,index):
            # # g.trace(count,index)
            # i,j = w.toGuiIndex(index),w.toGuiIndex(index+1)
            # Tk.Text.tag_add(w,'flash',i,j)
            # Tk.Text.after(w,delay,removeFlashCallback,w,count-1,index)

        # def removeFlashCallback(w,count,index):
            # # g.trace(count,index)
            # Tk.Text.tag_remove(w,'flash','1.0','end')
            # if count > 0:
                # Tk.Text.after(w,delay,addFlashCallback,w,count,index)

        # try:
            # Tk.Text.tag_configure(w,'flash',foreground=fg,background=bg)
            # addFlashCallback(w,flashes,i)
        # except Exception:
            # pass ; g.es_exception()
    #@nonl
    #@-node:ekr.20080112145409.286:flashCharacter
    #@+node:ekr.20080112145409.287:get
    def get(self,i,j=None):

        w = self
        i = w.toGuiIndex(i)

        if j is None:
            return '' ### return Tk.Text.get(w,i)
        else:
            j = w.toGuiIndex(j)
            return ### return Tk.Text.get(w,i,j)
    #@-node:ekr.20080112145409.287:get
    #@+node:ekr.20080112145409.288:getAllText
    def getAllText (self): # gtkTextWidget.

        """Return all the text of Tk.Text widget w converted to unicode."""

        w = self
        ### s = Tk.Text.get(w,"1.0","end-1c") # New in 4.4.1: use end-1c.
        s = '' ###

        if s is None:
            return u""
        else:
            return g.toUnicode(s,g.app.tkEncoding)
    #@-node:ekr.20080112145409.288:getAllText
    #@+node:ekr.20080112145409.289:getInsertPoint
    def getInsertPoint(self): # gtkTextWidget.

        w = self
        i = 0 ### i = Tk.Text.index(w,'insert')
        i = w.toPythonIndex(i)
        return i
    #@-node:ekr.20080112145409.289:getInsertPoint
    #@+node:ekr.20080112145409.290:getSelectedText
    def getSelectedText (self): # gtkTextWidget.

        w = self
        i,j = w.getSelectionRange()
        if i != j:
            i,j = w.toGuiIndex(i),w.toGuiIndex(j)
            s = '' ### s = Tk.Text.get(w,i,j)
            return g.toUnicode(s,g.app.tkEncoding)
        else:
            return u""
    #@-node:ekr.20080112145409.290:getSelectedText
    #@+node:ekr.20080112145409.291:getSelectionRange
    def getSelectionRange (self,sort=True): # gtkTextWidget.

        """Return a tuple representing the selected range.

        Return a tuple giving the insertion point if no range of text is selected."""

        w = self
        sel = 0,0 ### sel = Tk.Text.tag_ranges(w,"sel")
        if len(sel) == 2:
            i,j = sel
        else:
            i = j = 0 ### i = j = Tk.Text.index(w,"insert")

        i,j = w.toPythonIndex(i),w.toPythonIndex(j)  
        if sort and i > j: i,j = j,i
        return i,j
    #@nonl
    #@-node:ekr.20080112145409.291:getSelectionRange
    #@+node:ekr.20080112145409.292:getYScrollPosition
    def getYScrollPosition (self):

         w = self
         return 0 ### return w.yview()
    #@-node:ekr.20080112145409.292:getYScrollPosition
    #@+node:ekr.20080112145409.293:getWidth
    def getWidth (self):

        '''Return the width of the widget.
        This is only called for headline widgets,
        and gui's may choose not to do anything here.'''

        w = self
        return 0 ### return w.cget('width')
    #@-node:ekr.20080112145409.293:getWidth
    #@+node:ekr.20080112145409.294:hasSelection
    def hasSelection (self):

        w = self
        i,j = w.getSelectionRange()
        return i != j
    #@-node:ekr.20080112145409.294:hasSelection
    #@+node:ekr.20080112145409.295:insert
    # The signature is more restrictive than the Tk.Text.insert method.

    def insert(self,i,s):

        w = self
        i = w.toGuiIndex(i)
        ### Tk.Text.insert(w,i,s)

    #@-node:ekr.20080112145409.295:insert
    #@+node:ekr.20080112145409.296:indexIsVisible
    def indexIsVisible (self,i):

        w = self

        return True ### return w.dlineinfo(i)
    #@nonl
    #@-node:ekr.20080112145409.296:indexIsVisible
    #@+node:ekr.20080112145409.297:mark_set NO LONGER USED
    # def mark_set(self,markName,i):

        # w = self
        # i = w.toGuiIndex(i)
        # Tk.Text.mark_set(w,markName,i)
    #@-node:ekr.20080112145409.297:mark_set NO LONGER USED
    #@+node:ekr.20080112145409.298:replace
    def replace (self,i,j,s): # gtkTextWidget

        w = self
        i,j = w.toGuiIndex(i),w.toGuiIndex(j)

        ### Tk.Text.delete(w,i,j)
        ### Tk.Text.insert(w,i,s)
    #@-node:ekr.20080112145409.298:replace
    #@+node:ekr.20080112145409.299:see
    def see (self,i): # gtkTextWidget.

        w = self
        i = w.toGuiIndex(i)
        ### Tk.Text.see(w,i)
    #@-node:ekr.20080112145409.299:see
    #@+node:ekr.20080112145409.300:seeInsertPoint
    def seeInsertPoint (self): # gtkTextWidget.

        w = self
        ### Tk.Text.see(w,'insert')
    #@-node:ekr.20080112145409.300:seeInsertPoint
    #@+node:ekr.20080112145409.301:selectAllText
    def selectAllText (self,insert=None): # gtkTextWidget

        '''Select all text of the widget, *not* including the extra newline.'''

        w = self ; s = w.getAllText()
        if insert is None: insert = len(s)
        w.setSelectionRange(0,len(s),insert=insert)
    #@-node:ekr.20080112145409.301:selectAllText
    #@+node:ekr.20080112145409.302:setAllText
    def setAllText (self,s): # gtkTextWidget

        w = self

        # state = Tk.Text.cget(w,"state")
        # Tk.Text.configure(w,state="normal")

        # Tk.Text.delete(w,'1.0','end')
        # Tk.Text.insert(w,'1.0',s)

        # Tk.Text.configure(w,state=state)
    #@-node:ekr.20080112145409.302:setAllText
    #@+node:ekr.20080112145409.303:setBackgroundColor
    def setBackgroundColor (self,color):

        w = self
        w.configure(background=color)
    #@nonl
    #@-node:ekr.20080112145409.303:setBackgroundColor
    #@+node:ekr.20080112145409.304:setInsertPoint
    def setInsertPoint (self,i): # gtkTextWidget.

        w = self
        i = w.toGuiIndex(i)
        # g.trace(i,g.callers())
        ### Tk.Text.mark_set(w,'insert',i)
    #@-node:ekr.20080112145409.304:setInsertPoint
    #@+node:ekr.20080112145409.305:setSelectionRange
    def setSelectionRange (self,i,j,insert=None): # gtkTextWidget

        w = self

        i,j = w.toGuiIndex(i),w.toGuiIndex(j)

        # g.trace('i,j,insert',repr(i),repr(j),repr(insert),g.callers())

        # g.trace('i,j,insert',i,j,repr(insert))

        ###
        # if Tk.Text.compare(w,i, ">", j): i,j = j,i
        # Tk.Text.tag_remove(w,"sel","1.0",i)
        # Tk.Text.tag_add(w,"sel",i,j)
        # Tk.Text.tag_remove(w,"sel",j,"end")

        # if insert is not None:
            # w.setInsertPoint(insert)
    #@-node:ekr.20080112145409.305:setSelectionRange
    #@+node:ekr.20080112145409.306:setYScrollPosition
    def setYScrollPosition (self,i):

         w = self
         w.yview('moveto',i)
    #@nonl
    #@-node:ekr.20080112145409.306:setYScrollPosition
    #@+node:ekr.20080112145409.307:setWidth
    def setWidth (self,width):

        '''Set the width of the widget.
        This is only called for headline widgets,
        and gui's may choose not to do anything here.'''

        w = self
        w.configure(width=width)
    #@-node:ekr.20080112145409.307:setWidth
    #@+node:ekr.20080112145409.308:tag_add
    # The signature is slightly different than the Tk.Text.insert method.

    def tag_add(self,tagName,i,j=None,*args):

        w = self
        i = w.toGuiIndex(i)

        # if j is None:
            # Tk.Text.tag_add(w,tagName,i,*args)
        # else:
            # j = w.toGuiIndex(j)
            # Tk.Text.tag_add(w,tagName,i,j,*args)

    #@-node:ekr.20080112145409.308:tag_add
    #@+node:ekr.20080112145409.309:tag_configure (NEW)
    def tag_configure (self,*args,**keys):

        pass

    tag_config = tag_configure
    #@-node:ekr.20080112145409.309:tag_configure (NEW)
    #@+node:ekr.20080112145409.310:tag_ranges
    def tag_ranges(self,tagName):

        w = self
        aList = [] ### aList = Tk.Text.tag_ranges(w,tagName)
        aList = [w.toPythonIndex(z) for z in aList]
        return tuple(aList)
    #@-node:ekr.20080112145409.310:tag_ranges
    #@+node:ekr.20080112145409.311:tag_remove
    def tag_remove (self,tagName,i,j=None,*args):

        w = self
        i = w.toGuiIndex(i)

        if j is None:
            pass ### Tk.Text.tag_remove(w,tagName,i,*args)
        else:
            j = w.toGuiIndex(j)
            ### Tk.Text.tag_remove(w,tagName,i,j,*args)


    #@-node:ekr.20080112145409.311:tag_remove
    #@+node:ekr.20080112145409.312:w.deleteTextSelection
    def deleteTextSelection (self): # gtkTextWidget

        w = self
        # sel = Tk.Text.tag_ranges(w,"sel")
        # if len(sel) == 2:
            # start,end = sel
            # if Tk.Text.compare(w,start,"!=",end):
                # Tk.Text.delete(w,start,end)
    #@-node:ekr.20080112145409.312:w.deleteTextSelection
    #@+node:ekr.20080112145409.313:xyToGui/PythonIndex
    def xyToGuiIndex (self,x,y): # gtkTextWidget

        w = self
        return 0 ### return Tk.Text.index(w,"@%d,%d" % (x,y))

    def xyToPythonIndex(self,x,y): # gtkTextWidget

        w = self
        i = 0 ### i = Tk.Text.index(w,"@%d,%d" % (x,y))
        i = w.toPythonIndex(i)
        return i
    #@-node:ekr.20080112145409.313:xyToGui/PythonIndex
    #@-node:ekr.20080112145409.282:Wrapper methods (gtkTextWidget)
    #@-others
#@nonl
#@-node:ekr.20080112145409.273:class leoGtkTextWidget (revise)
#@+node:ekr.20080112145409.314:class leoGtkTree (REWRITE)
class leoGtkTree (leoFrame.leoTree):

    callbacksInjected = False

    """Leo gtk tree class."""

    #@    @+others
    #@+node:ekr.20080112145409.315:  Notes
    #@@killcolor
    #@+node:ekr.20080112145409.316:Changes made since first update
    #@+at
    # 
    # - disabled drawing of user icons.  They weren't being hidden, which 
    # messed up scrolling.
    # 
    # - Expanded clickBox so all clicks fall inside it.
    # 
    # - Added binding for plugBox so it doesn't interfere with the clickBox.  
    # Another weirdness.
    # 
    # - Re-enabled code in drawText that sets the headline state.
    # 
    # - eventToPosition now returns p.copy, which means that nobody can change 
    # the list.
    # 
    # - Likewise, clear self.iconIds so old icon id's don't confuse 
    # findVnodeWithIconId.
    # 
    # - All drawing methods must do p = p.copy() at the beginning if they make 
    # any changes to p.
    #     - This ensures neither they nor their allies can change the caller's 
    # position.
    #     - In fact, though, only drawTree changes position.  It makes a copy 
    # before calling drawNode.
    #     *** Therefore, all positions in the drawing code are immutable!
    # 
    # - Fixed the race conditions that caused drawing sometimes to fail.  The 
    # essential idea is that we must not call w.config if we are about to do a 
    # redraw.  For full details, see the Notes node in the Race Conditions 
    # section.
    #@-at
    #@-node:ekr.20080112145409.316:Changes made since first update
    #@+node:ekr.20080112145409.317:Changes made since second update
    #@+at
    # 
    # - Removed duplicate code in tree.select.  The following code was being 
    # called twice (!!):
    #     self.endEditLabel()
    #     self.setUnselectedLabelState(old_p)
    # 
    # - Add p.copy() instead of p when inserting nodes into data structures in 
    # select.
    # 
    # - Fixed a _major_ bug in Leo's core.  c.setCurrentPosition must COPY the 
    # position given to it!  It's _not_ enough to return a copy of position: 
    # it may already have changed!!
    # 
    # - Fixed a another (lesser??) bug in Leo's core.  handleUserClick should 
    # also make a copy.
    # 
    # - Fixed bug in mod_scripting.py.  The callback was failing if the script 
    # was empty.
    # 
    # - Put in the self.recycle ivar AND THE CODE STILL FAILS.
    #     It seems to me that this shows there is a bug in my code somewhere, 
    # but where ???????????????????
    #@-at
    #@-node:ekr.20080112145409.317:Changes made since second update
    #@+node:ekr.20080112145409.318:Most recent changes
    #@+at
    # 
    # - Added generation count.
    #     - Incremented on each redraw.
    #     - Potentially a barrior to race conditions, but it never seemed to 
    # do anything.
    #     - This code is a candidate for elimination.
    # 
    # - Used vnodes rather than positions in several places.
    #     - I actually don't think this was involved in the real problem, and 
    # it doesn't hurt.
    # 
    # - Added much better traces: the beginning of the end for the bugs :-)
    #     - Added self.verbose option.
    #     - Added align keyword option to g.trace.
    #     - Separate each set of traces by a blank line.
    #         - This makes clear the grouping of id's.
    # 
    # - Defensive code: Disable dragging at start of redraw code.
    #     - This protects against race conditions.
    # 
    # - Fixed blunder 1: Fixed a number of bugs in the dragging code.
    #     - I had never looked at this code!
    #     - Eliminating false drags greatly simplifies matters.
    # 
    # - Fixed blunder 2: Added the following to eventToPosition:
    #         x = canvas.canvasx(x)
    #         y = canvas.canvasy(y)
    #     - Apparently this was the cause of false associations between icons 
    # and id's.
    #     - It's amazing that the code didn't fail earlier without these!
    # 
    # - Converted all module-level constants to ivars.
    # 
    # - Lines no longer interfere with eventToPosition.
    #     - The problem was that find_nearest or find_overlapping don't depend 
    # on stacking order!
    #     - Added p param to horizontal lines, but not vertical lines.
    #     - EventToPosition adds 1 to the x coordinate of vertical lines, then 
    # recomputes the id.
    # 
    # - Compute indentation only in forceDrawNode.  Removed child_indent 
    # constant.
    # 
    # - Simplified drawTree to use indentation returned from forceDrawNode.
    # 
    # - setHeadlineText now ensures that state is "normal" before attempting 
    # to set the text.
    #     - This is the robust way.
    # 
    # 7/31/04: newText must call setHeadlineText for all nodes allocated, even 
    # if p matches.
    #@-at
    #@-node:ekr.20080112145409.318:Most recent changes
    #@-node:ekr.20080112145409.315:  Notes
    #@+node:ekr.20080112145409.319: Birth... (gtkTree)
    #@+node:ekr.20080112145409.320:__init__ (gtkTree)
    def __init__(self,c,frame,canvas):

        # Init the base class.
        leoFrame.leoTree.__init__(self,frame)

        # Configuration and debugging settings.
        # These must be defined here to eliminate memory leaks.
        self.allow_clone_drags          = c.config.getBool('allow_clone_drags')
        self.center_selected_tree_node  = c.config.getBool('center_selected_tree_node')
        self.enable_drag_messages       = c.config.getBool("enable_drag_messages")
        self.expanded_click_area        = c.config.getBool('expanded_click_area')
        self.gc_before_redraw           = c.config.getBool('gc_before_redraw')

        self.headline_text_editing_foreground_color = c.config.getColor(
            'headline_text_editing_foreground_color')
        self.headline_text_editing_background_color = c.config.getColor(
            'headline_text_editing_background_color')
        self.headline_text_editing_selection_foreground_color = c.config.getColor(
            'headline_text_editing_selection_foreground_color')
        self.headline_text_editing_selection_background_color = c.config.getColor(
            'headline_text_editing_selection_background_color')
        self.headline_text_selected_foreground_color = c.config.getColor(
            "headline_text_selected_foreground_color")
        self.headline_text_selected_background_color = c.config.getColor(
            "headline_text_selected_background_color")
        self.headline_text_editing_selection_foreground_color = c.config.getColor(
            "headline_text_editing_selection_foreground_color")
        self.headline_text_editing_selection_background_color = c.config.getColor(
            "headline_text_editing_selection_background_color")
        self.headline_text_unselected_foreground_color = c.config.getColor(
            'headline_text_unselected_foreground_color')
        self.headline_text_unselected_background_color = c.config.getColor(
            'headline_text_unselected_background_color')

        self.idle_redraw = c.config.getBool('idle_redraw')
        self.initialClickExpandsOrContractsNode = c.config.getBool(
            'initialClickExpandsOrContractsNode')
        self.look_for_control_drag_on_mouse_down = c.config.getBool(
            'look_for_control_drag_on_mouse_down')
        self.select_all_text_when_editing_headlines = c.config.getBool(
            'select_all_text_when_editing_headlines')

        self.stayInTree     = c.config.getBool('stayInTreeAfterSelect')
        self.trace          = c.config.getBool('trace_tree')
        self.trace_alloc    = c.config.getBool('trace_tree_alloc')
        self.trace_chapters = c.config.getBool('trace_chapters')
        self.trace_edit     = c.config.getBool('trace_tree_edit')
        self.trace_gc       = c.config.getBool('trace_tree_gc')
        self.trace_redraw   = c.config.getBool('trace_tree_redraw')
        self.trace_select   = c.config.getBool('trace_select')
        self.trace_stats    = c.config.getBool('show_tree_stats')
        self.use_chapters   = False and c.config.getBool('use_chapters') ###

        # Objects associated with this tree.
        self.canvas = canvas

        #@    << define drawing constants >>
        #@+node:ekr.20080112145409.321:<< define drawing constants >>
        self.box_padding = 5 # extra padding between box and icon
        self.box_width = 9 + self.box_padding
        self.icon_width = 20
        self.text_indent = 4 # extra padding between icon and tex

        self.hline_y = 7 # Vertical offset of horizontal line
        self.root_left = 7 + self.box_width
        self.root_top = 2

        self.default_line_height = 17 + 2 # default if can't set line_height from font.
        self.line_height = self.default_line_height
        #@-node:ekr.20080112145409.321:<< define drawing constants >>
        #@nl
        #@    << old ivars >>
        #@+node:ekr.20080112145409.322:<< old ivars >>
        # Miscellaneous info.
        self.iconimages = {} # Image cache set by getIconImage().
        self.active = False # True if present headline is active
        self._editPosition = None # Returned by leoTree.editPosition()
        self.lineyoffset = 0 # y offset for this headline.
        self.lastClickFrameId = None # id of last entered clickBox.
        self.lastColoredText = None # last colored text widget.

        # Set self.font and self.fontName.
        self.setFontFromConfig()

        # Drag and drop
        self.drag_p = None
        self.controlDrag = False # True: control was down when drag started.

        # Keep track of popup menu so we can handle behavior better on Linux Context menu
        self.popupMenu = None

        # Incremental redraws:
        self.allocateOnlyVisibleNodes = False # True: enable incremental redraws.
        self.prevMoveToFrac = 0.0
        self.visibleArea = None
        self.expandedVisibleArea = None

        ###
        # if self.allocateOnlyVisibleNodes:
            # self.frame.bar1.bind("<B1-ButtonRelease>", self.redraw_now)
        #@-node:ekr.20080112145409.322:<< old ivars >>
        #@nl
        #@    << inject callbacks into the position class >>
        #@+node:ekr.20080112145409.323:<< inject callbacks into the position class >>
        # The new code injects 3 callbacks for the colorizer.

        if not leoGtkTree.callbacksInjected: # Class var.
            leoGtkTree.callbacksInjected = True
            self.injectCallbacks()
        #@-node:ekr.20080112145409.323:<< inject callbacks into the position class >>
        #@nl

        self.dragging = False
        self.generation = 0
        self.prevPositions = 0
        self.redrawing = False # Used only to disable traces.
        self.redrawCount = 0 # Count for debugging.
        self.revertHeadline = None # Previous headline text for abortEditLabel.

        # New in 4.4: We should stay in the tree to use per-pane bindings.
        self.textBindings = [] # Set in setBindings.
        self.textNumber = 0 # To make names unique.
        self.updateCount = 0 # Drawing is enabled only if self.updateCount <= 0
        self.verbose = True

        self.setEditPosition(None) # Set positions returned by leoTree.editPosition()

        # Keys are id's, values are positions...
        self.ids = {}
        self.iconIds = {}

        # Lists of visible (in-use) widgets...
        self.visibleBoxes = []
        self.visibleClickBoxes = []
        self.visibleIcons = []
        self.visibleLines = []
        self.visibleText  = {}
            # Pre 4.4b2: Keys are vnodes, values are Tk.Text widgets.
            #     4.4b2: Keys are p.key(), values are Tk.Text widgets.
        self.visibleUserIcons = []

        # Lists of free, hidden widgets...
        self.freeBoxes = []
        self.freeClickBoxes = []
        self.freeIcons = []
        self.freeLines = []
        self.freeText = [] # New in 4.4b2: a list of free Tk.Text widgets

        self.freeUserIcons = []
    #@-node:ekr.20080112145409.320:__init__ (gtkTree)
    #@+node:ekr.20080112145409.324:gtkTtree.setBindings
    def setBindings (self,):

        '''Create master bindings for all headlines.'''

        tree = self ; k = self.c.k ; canvas = self.canvas

        if 0:

            # g.trace('self',self,'canvas',canvas)

            #@        << make bindings for a common binding widget >>
            #@+node:ekr.20080112145409.325:<< make bindings for a common binding widget >>
            self.bindingWidget = w = g.app.gui.plainTextWidget(
                self.canvas,name='bindingWidget')

            w.bind('<Key>',k.masterKeyHandler)

            table = (
                ('<Button-1>',       k.masterClickHandler,          tree.onHeadlineClick),
                ('<Button-3>',       k.masterClick3Handler,         tree.onHeadlineRightClick),
                ('<Double-Button-1>',k.masterDoubleClickHandler,    tree.onHeadlineClick),
                ('<Double-Button-3>',k.masterDoubleClick3Handler,   tree.onHeadlineRightClick),
            )

            for a,handler,func in table:
                def treeBindingCallback(event,handler=handler,func=func):
                    # g.trace('func',func)
                    return handler(event,func)
                w.bind(a,treeBindingCallback)

            ### self.textBindings = w.bindtags()
            #@-node:ekr.20080112145409.325:<< make bindings for a common binding widget >>
            #@nl

            tree.setCanvasBindings(canvas)

            k.completeAllBindingsForWidget(canvas)

            k.completeAllBindingsForWidget(self.bindingWidget)

    #@-node:ekr.20080112145409.324:gtkTtree.setBindings
    #@+node:ekr.20080112145409.326:gtkTree.setCanvasBindings
    def setCanvasBindings (self,canvas):

        k = self.c.k

        if 0: ###

            canvas.bind('<Key>',k.masterKeyHandler)
            canvas.bind('<Button-1>',self.onTreeClick)

            #@        << make bindings for tagged items on the canvas >>
            #@+node:ekr.20080112145409.327:<< make bindings for tagged items on the canvas >>
            where = g.choose(self.expanded_click_area,'clickBox','plusBox')

            ###
            # table = (
                # (where,    '<Button-1>',self.onClickBoxClick),
                # ('iconBox','<Button-1>',self.onIconBoxClick),
                # ('iconBox','<Double-1>',self.onIconBoxDoubleClick),
                # ('iconBox','<Button-3>',self.onIconBoxRightClick),
                # ('iconBox','<Double-3>',self.onIconBoxRightClick),
                # ('iconBox','<B1-Motion>',self.onDrag),
                # ('iconBox','<Any-ButtonRelease-1>',self.onEndDrag),
            # )
            # for tag,event,callback in table:
                # canvas.tag_bind(tag,event,callback)
            #@-node:ekr.20080112145409.327:<< make bindings for tagged items on the canvas >>
            #@nl
            #@        << create baloon bindings for tagged items on the canvas >>
            #@+node:ekr.20080112145409.328:<< create baloon bindings for tagged items on the canvas >>
            if 0: # I find these very irritating.
                for tag,text in (
                    # ('plusBox','plusBox'),
                    ('iconBox','Icon Box'),
                    ('selectBox','Click to select'),
                    ('clickBox','Click to expand or contract'),
                    # ('textBox','Headline'),
                ):
                    # A fairly long wait is best.
                    balloon = Pmw.Balloon(self.canvas,initwait=700)
                    balloon.tagbind(self.canvas,tag,balloonHelp=text)
            #@-node:ekr.20080112145409.328:<< create baloon bindings for tagged items on the canvas >>
            #@nl
    #@-node:ekr.20080112145409.326:gtkTree.setCanvasBindings
    #@-node:ekr.20080112145409.319: Birth... (gtkTree)
    #@+node:ekr.20080112145409.329:Allocation...
    #@+node:ekr.20080112145409.330:newBox
    def newBox (self,p,x,y,image):

        canvas = self.canvas ; tag = "plusBox"

        if self.freeBoxes:
            theId = self.freeBoxes.pop(0)
            canvas.coords(theId,x,y)
            canvas.itemconfigure(theId,image=image)
        else:
            theId = canvas.create_image(x,y,image=image,tag=tag)
            if self.trace_alloc: g.trace("%3d %s" % (theId,p and p.headString()),align=-20)

        if theId not in self.visibleBoxes: 
            self.visibleBoxes.append(theId)

        if p:
            self.ids[theId] = p

        return theId
    #@-node:ekr.20080112145409.330:newBox
    #@+node:ekr.20080112145409.331:newClickBox
    def newClickBox (self,p,x1,y1,x2,y2):

        canvas = self.canvas ; defaultColor = ""
        tag = g.choose(p.hasChildren(),'clickBox','selectBox')

        if self.freeClickBoxes:
            theId = self.freeClickBoxes.pop(0)
            canvas.coords(theId,x1,y1,x2,y2)
            canvas.itemconfig(theId,tag=tag)
        else:
            theId = self.canvas.create_rectangle(x1,y1,x2,y2,tag=tag)
            canvas.itemconfig(theId,fill=defaultColor,outline=defaultColor)
            if self.trace_alloc: g.trace("%3d %s" % (theId,p and p.headString()),align=-20)

        if theId not in self.visibleClickBoxes:
            self.visibleClickBoxes.append(theId)
        if p:
            self.ids[theId] = p

        return theId
    #@-node:ekr.20080112145409.331:newClickBox
    #@+node:ekr.20080112145409.332:newIcon
    def newIcon (self,p,x,y,image):

        canvas = self.canvas ; tag = "iconBox"

        if self.freeIcons:
            theId = self.freeIcons.pop(0)
            canvas.itemconfigure(theId,image=image)
            canvas.coords(theId,x,y)
        else:
            theId = canvas.create_image(x,y,image=image,anchor="nw",tag=tag)
            if self.trace_alloc: g.trace("%3d %s" % (theId,p and p.headString()),align=-20)

        if theId not in self.visibleIcons:
            self.visibleIcons.append(theId)

        if p:
            data = p,self.generation
            self.iconIds[theId] = data # Remember which vnode belongs to the icon.
            self.ids[theId] = p

        return theId
    #@-node:ekr.20080112145409.332:newIcon
    #@+node:ekr.20080112145409.333:newLine
    def newLine (self,p,x1,y1,x2,y2):

        canvas = self.canvas

        if self.freeLines:
            theId = self.freeLines.pop(0)
            canvas.coords(theId,x1,y1,x2,y2)
        else:
            theId = canvas.create_line(x1,y1,x2,y2,tag="lines",fill="gray50") # stipple="gray25")
            if self.trace_alloc: g.trace("%3d %s" % (theId,p and p.headString()),align=-20)

        if p:
            self.ids[theId] = p

        if theId not in self.visibleLines:
            self.visibleLines.append(theId)

        return theId
    #@-node:ekr.20080112145409.333:newLine
    #@+node:ekr.20080112145409.334:newText (gtkTree) and helper
    def newText (self,p,x,y):

        canvas = self.canvas ; tag = "textBox"
        c = self.c ;  k = c.k
        if self.freeText:
            w,theId = self.freeText.pop()
            canvas.coords(theId,x,y) # Make the window visible again.
                # theId is the id of the *window* not the text.
        else:
            # Tags are not valid in Tk.Text widgets.
            self.textNumber += 1
            w = g.app.gui.plainTextWidget(
                canvas,name='head-%d' % self.textNumber,
                state="normal",font=self.font,bd=0,relief="flat",height=1)
            ### w.bindtags(self.textBindings) # Set the bindings for this widget.

            if 0: # Crashes on XP.
                #@            << patch by Maciej Kalisiak to handle scroll-wheel events >>
                #@+node:ekr.20080112145409.335:<< patch by Maciej Kalisiak  to handle scroll-wheel events >>
                def PropagateButton4(e):
                    canvas.event_generate("<Button-4>")
                    return "break"

                def PropagateButton5(e):
                    canvas.event_generate("<Button-5>")
                    return "break"

                def PropagateMouseWheel(e):
                    canvas.event_generate("<MouseWheel>")
                    return "break"

                ### 
                # instance_tag = w.bindtags()[0]
                # w.bind_class(instance_tag, "<Button-4>", PropagateButton4)
                # w.bind_class(instance_tag, "<Button-5>", PropagateButton5)
                # w.bind_class(instance_tag, "<MouseWheel>",PropagateMouseWheel)
                #@-node:ekr.20080112145409.335:<< patch by Maciej Kalisiak  to handle scroll-wheel events >>
                #@nl

            theId = canvas.create_window(x,y,anchor="nw",window=w,tag=tag)
            w.leo_window_id = theId # Never changes.

            if self.trace_alloc: g.trace('%3d %6s' % (theId,id(w)),align=-20)

        # Common configuration.
        if 0: # Doesn't seem to work.
            balloon = Pmw.Balloon(canvas,initwait=700)
            balloon.tagbind(canvas,theId,balloonHelp='Headline')

        if p:
            self.ids[theId] = p # Add the id of the *window*
            self.setHeadlineText(theId,w,p.headString())
            w.configure(width=self.headWidth(p=p))
            w.leo_position = p # This p never changes.
                # *Required*: onHeadlineClick uses w.leo_position to get p.

            # Keys are p.key().  Entries are (w,theId)
            self.visibleText [p.key()] = w,theId
        else:
            g.trace('**** can not happen.  No p')

        return w
    #@+node:ekr.20080112145409.336:tree.setHeadlineText
    def setHeadlineText (self,theId,w,s):

        """All changes to text widgets should come here."""

        # __pychecker__ = '--no-argsused' # theId not used.

        # if self.trace_alloc: g.trace('%4d %6s %s' % (theId,self.textAddr(w),s),align=-20)

        state = w.cget("state")
        if state != "normal":
            w.configure(state="normal")
        w.delete(0,"end")
        # Important: do not allow newlines in headlines.
        while s.endswith('\n') or s.endswith('\r'):
            s = s[:-1]
        w.insert("end",s)
        # g.trace(repr(s))
        if state != "normal":
            w.configure(state=state)
    #@-node:ekr.20080112145409.336:tree.setHeadlineText
    #@-node:ekr.20080112145409.334:newText (gtkTree) and helper
    #@+node:ekr.20080112145409.337:recycleWidgets
    def recycleWidgets (self):

        canvas = self.canvas

        for theId in self.visibleBoxes:
            if theId not in self.freeBoxes:
                self.freeBoxes.append(theId)
            canvas.coords(theId,-100,-100)
        self.visibleBoxes = []

        for theId in self.visibleClickBoxes:
            if theId not in self.freeClickBoxes:
                self.freeClickBoxes.append(theId)
            canvas.coords(theId,-100,-100,-100,-100)
        self.visibleClickBoxes = []

        for theId in self.visibleIcons:
            if theId not in self.freeIcons:
                self.freeIcons.append(theId)
            canvas.coords(theId,-100,-100)
        self.visibleIcons = []

        for theId in self.visibleLines:
            if theId not in self.freeLines:
                self.freeLines.append(theId)
            canvas.coords(theId,-100,-100,-100,-100)
        self.visibleLines = []

        aList = self.visibleText.values()
        for data in aList:
            w,theId = data
            # assert theId == w.leo_window_id
            canvas.coords(theId,-100,-100)
            w.leo_position = None # Allow the position to be freed.
            if data not in self.freeText:
                self.freeText.append(data)
        self.visibleText = {}

        for theId in self.visibleUserIcons:
            # The present code does not recycle user Icons.
            self.canvas.delete(theId)
        self.visibleUserIcons = []
    #@-node:ekr.20080112145409.337:recycleWidgets
    #@+node:ekr.20080112145409.338:destroyWidgets
    def destroyWidgets (self):

        self.ids = {}

        self.visibleBoxes = []
        self.visibleClickBoxes = []
        self.visibleIcons = []
        self.visibleLines = []
        self.visibleUserIcons = []

        self.visibleText = {}

        self.freeText = []
        self.freeBoxes = []
        self.freeClickBoxes = []
        self.freeIcons = []
        self.freeLines = []

        self.canvas.delete("all")
    #@-node:ekr.20080112145409.338:destroyWidgets
    #@+node:ekr.20080112145409.339:showStats
    def showStats (self):

        z = []
        for kind,a,b in (
            ('boxes',self.visibleBoxes,self.freeBoxes),
            ('clickBoxes',self.visibleClickBoxes,self.freeClickBoxes),
            ('icons',self.visibleIcons,self.freeIcons),
            ('lines',self.visibleLines,self.freeLines),
            ('tesxt',self.visibleText.values(),self.freeText),
        ):
            z.append('%10s used: %4d free: %4d' % (kind,len(a),len(b)))

        g.es_print('\n' + '\n'.join(z))
    #@-node:ekr.20080112145409.339:showStats
    #@-node:ekr.20080112145409.329:Allocation...
    #@+node:ekr.20080112145409.340:Config & Measuring...
    #@+node:ekr.20080112145409.341:tree.getFont,setFont,setFontFromConfig
    def getFont (self):

        return self.font

    def setFont (self,font=None, fontName=None):

        # ESSENTIAL: retain a link to font.
        if fontName:
            self.fontName = fontName
            self.font = gtkFont.Font(font=fontName)
        else:
            self.fontName = None
            self.font = font

        self.setLineHeight(self.font)

    # Called by ctor and when config params are reloaded.
    def setFontFromConfig (self):
        c = self.c
        # g.trace()
        font = c.config.getFontFromParams(
            "headline_text_font_family", "headline_text_font_size",
            "headline_text_font_slant",  "headline_text_font_weight",
            c.config.defaultTreeFontSize)

        self.setFont(font)
    #@-node:ekr.20080112145409.341:tree.getFont,setFont,setFontFromConfig
    #@+node:ekr.20080112145409.342:headWidth & widthInPixels
    def headWidth(self,p=None,s=''):

        """Returns the proper width of the entry widget for the headline."""

        if p: s = p.headString()

        return self.font.measure(s)/self.font.measure('0')+1


    def widthInPixels(self,s):

        s = g.toEncodedString(s,g.app.tkEncoding)

        return self.font.measure(s)
    #@-node:ekr.20080112145409.342:headWidth & widthInPixels
    #@+node:ekr.20080112145409.343:setLineHeight
    def setLineHeight (self,font):

        pass ###

        # try:
            # metrics = font.metrics()
            # linespace = metrics ["linespace"]
            # self.line_height = linespace + 5 # Same as before for the default font on Windows.
            # # print metrics
        # except:
            # self.line_height = self.default_line_height
            # g.es("exception setting outline line height")
            # g.es_exception()
    #@-node:ekr.20080112145409.343:setLineHeight
    #@-node:ekr.20080112145409.340:Config & Measuring...
    #@+node:ekr.20080112145409.344:Debugging...
    #@+node:ekr.20080112145409.345:textAddr
    def textAddr(self,w):

        """Return the address part of repr(Tk.Text)."""

        return repr(w)[-9:-1].lower()
    #@-node:ekr.20080112145409.345:textAddr
    #@+node:ekr.20080112145409.346:traceIds (Not used)
    # Verbose tracing is much more useful than this because we can see the recent past.

    def traceIds (self,full=False):

        tree = self

        for theDict,tag,flag in ((tree.ids,"ids",True),(tree.iconIds,"icon ids",False)):
            print '=' * 60
            print ; print "%s..." % tag
            keys = theDict.keys()
            keys.sort()
            for key in keys:
                p = tree.ids.get(key)
                if p is None: # For lines.
                    print "%3d None" % key
                else:
                    print "%3d" % key,p.headString()
            if flag and full:
                print '-' * 40
                values = theDict.values()
                values.sort()
                seenValues = []
                for value in values:
                    if value not in seenValues:
                        seenValues.append(value)
                        for item in theDict.items():
                            key,val = item
                            if val and val == value:
                                print "%3d" % key,val.headString()
    #@-node:ekr.20080112145409.346:traceIds (Not used)
    #@-node:ekr.20080112145409.344:Debugging...
    #@+node:ekr.20080112145409.347:Drawing... (gtkTree)
    #@+node:ekr.20080112145409.348:tree.begin/endUpdate
    def beginUpdate (self):

        self.updateCount += 1
        # g.trace('tree',id(self),self.updateCount,g.callers())

    def endUpdate (self,flag,scroll=False):

        self.updateCount -= 1
        # g.trace(self.updateCount,'scroll',scroll,g.callers())

        if self.updateCount <= 0:
            if flag:
                self.redraw_now(scroll=scroll)
            if self.updateCount < 0:
                g.trace("Can't happen: negative updateCount",g.callers())
    #@-node:ekr.20080112145409.348:tree.begin/endUpdate
    #@+node:ekr.20080112145409.349:tree.redraw_now & helper
    # New in 4.4b2: suppress scrolling by default.

    def redraw_now (self,scroll=False):

        '''Redraw immediately: used by Find so a redraw doesn't mess up selections in headlines.'''

        if g.app.quitting or self.drag_p or self.frame not in g.app.windowList:
            return

        c = self.c

        # g.trace(g.callers())

        if not g.app.unitTesting:
            if self.gc_before_redraw:
                g.collectGarbage()
            if g.app.trace_gc_verbose:
                if (self.redrawCount % 5) == 0:
                    g.printGcSummary()
            if self.trace_redraw or self.trace_alloc:
                # g.trace(self.redrawCount,g.callers())
                # g.trace(c.rootPosition().headString(),'canvas:',id(self.canvas),g.callers())
                if self.trace_stats:
                    g.print_stats()
                    g.clear_stats()

        # New in 4.4b2: Call endEditLabel, but suppress the redraw.
        self.beginUpdate()
        try:
            self.endEditLabel()
        finally:
            self.endUpdate(False)

        # Do the actual redraw.
        self.expandAllAncestors(c.currentPosition())
        if self.idle_redraw:
            def idleRedrawCallback(event=None,self=self,scroll=scroll):
                self.redrawHelper(scroll=scroll)
            ### self.canvas.after_idle(idleRedrawCallback)
        else:
            self.redrawHelper(scroll=scroll)
        if g.app.unitTesting:
            self.canvas.update_idletasks() # Important for unit tests.
        c.masterFocusHandler()

    redraw = redraw_now # Compatibility
    #@+node:ekr.20080112145409.350:redrawHelper
    def redrawHelper (self,scroll=True):

        c = self.c

        ###

        # oldcursor = self.canvas['cursor']
        # self.canvas['cursor'] = "watch"

        # if not g.doHook("redraw-entire-outline",c=c):
            # c.setTopVnode(None)
            # self.setVisibleAreaToFullCanvas()
            # self.drawTopTree()
            # # Set up the scroll region after the tree has been redrawn.
            # bbox = self.canvas.bbox('all')
            # # g.trace('canvas',self.canvas,'bbox',bbox)
            # if bbox is None:
                # x0,y0,x1,y1 = 0,0,100,100
            # else:
                # x0, y0, x1, y1 = bbox
            # self.canvas.configure(scrollregion=(0, 0, x1, y1))
            # if scroll:
                # self.canvas.update_idletasks() # Essential.
                # self.scrollTo()

        g.doHook("after-redraw-outline",c=c)

        ### self.canvas['cursor'] = oldcursor
    #@-node:ekr.20080112145409.350:redrawHelper
    #@-node:ekr.20080112145409.349:tree.redraw_now & helper
    #@+node:ekr.20080112145409.351:idle_second_redraw
    def idle_second_redraw (self):

        c = self.c

        # Erase and redraw the entire tree the SECOND time.
        # This ensures that all visible nodes are allocated.
        c.setTopVnode(None)
        args = self.canvas.yview()
        self.setVisibleArea(args)

        if 0:
            self.deleteBindings()
            self.canvas.delete("all")

        self.drawTopTree()

        if self.trace:
            g.trace(self.redrawCount)
    #@-node:ekr.20080112145409.351:idle_second_redraw
    #@+node:ekr.20080112145409.352:drawX...
    #@+node:ekr.20080112145409.353:drawBox
    def drawBox (self,p,x,y):

        tree = self ; c = self.c
        y += 7 # draw the box at x, y+7

        theId = g.doHook("draw-outline-box",tree=tree,c=c,p=p,v=p,x=x,y=y)

        if theId is None:
            # if self.trace_gc: g.printNewObjects(tag='box 1')
            iconname = g.choose(p.isExpanded(),"minusnode.gif", "plusnode.gif")
            image = self.getIconImage(iconname)
            theId = self.newBox(p,x,y+self.lineyoffset,image)
            # if self.trace_gc: g.printNewObjects(tag='box 2')
            return theId
        else:
            return theId
    #@-node:ekr.20080112145409.353:drawBox
    #@+node:ekr.20080112145409.354:drawClickBox
    def drawClickBox (self,p,y):

        h = self.line_height

        # Define a slighly larger rect to catch clicks.
        if self.expanded_click_area:
            self.newClickBox(p,0,y,1000,y+h-2)
    #@-node:ekr.20080112145409.354:drawClickBox
    #@+node:ekr.20080112145409.355:drawIcon
    def drawIcon(self,p,x=None,y=None):

        """Draws icon for position p at x,y, or at p.v.iconx,p.v.icony if x,y = None,None"""

        # if self.trace_gc: g.printNewObjects(tag='icon 1')

        c = self.c ; v = p.v
        #@    << compute x,y and iconVal >>
        #@+node:ekr.20080112145409.356:<< compute x,y and iconVal >>
        if x is None and y is None:
            try:
                x,y = v.iconx, v.icony
            except:
                # Inject the ivars.
                x,y = v.iconx, v.icony = 0,0
        else:
            # Inject the ivars.
            v.iconx, v.icony = x,y

        y += 2 # draw icon at y + 2

        # Always recompute v.iconVal.
        # This is an important drawing optimization.
        val = v.computeIcon()
        assert(0 <= val <= 15)
        # g.trace(v,val)
        #@nonl
        #@-node:ekr.20080112145409.356:<< compute x,y and iconVal >>
        #@nl
        v.iconVal = val

        if not g.doHook("draw-outline-icon",tree=self,c=c,p=p,v=p,x=x,y=y):

            # Get the image.
            imagename = "box%02d.GIF" % val
            image = self.getIconImage(imagename)
            self.newIcon(p,x,y+self.lineyoffset,image)

        return 0,self.icon_width # dummy icon height,width
    #@-node:ekr.20080112145409.355:drawIcon
    #@+node:ekr.20080112145409.357:drawLine
    def drawLine (self,p,x1,y1,x2,y2):

        theId = self.newLine(p,x1,y1,x2,y2)

        return theId
    #@-node:ekr.20080112145409.357:drawLine
    #@+node:ekr.20080112145409.358:drawNode & force_draw_node (good trace)
    def drawNode(self,p,x,y):

        c = self.c

        # g.trace(x,y,p,id(self.canvas))

        data = g.doHook("draw-outline-node",tree=self,c=c,p=p,v=p,x=x,y=y)
        if data is not None: return data

        if 1:
            self.lineyoffset = 0
        else:
            if hasattr(p.v.t,"unknownAttributes"):
                self.lineyoffset = p.v.t.unknownAttributes.get("lineYOffset",0)
            else:
                self.lineyoffset = 0

        # Draw the horizontal line.
        self.drawLine(p,
            x,y+7+self.lineyoffset,
            x+self.box_width,y+7+self.lineyoffset)

        if self.inVisibleArea(y):
            return self.force_draw_node(p,x,y)
        else:
            return self.line_height,0
    #@+node:ekr.20080112145409.359:force_draw_node
    def force_draw_node(self,p,x,y):

        h = 0 # The total height of the line.
        indent = 0 # The amount to indent this line.

        h2,w2 = self.drawUserIcons(p,"beforeBox",x,y)
        h = max(h,h2) ; x += w2 ; indent += w2

        if p.hasChildren():
            self.drawBox(p,x,y)

        indent += self.box_width
        x += self.box_width # even if box isn't drawn.

        h2,w2 = self.drawUserIcons(p,"beforeIcon",x,y)
        h = max(h,h2) ; x += w2 ; indent += w2

        h2,w2 = self.drawIcon(p,x,y)
        h = max(h,h2) ; x += w2 ; indent += w2/2

        # Nothing after here affects indentation.
        h2,w2 = self.drawUserIcons(p,"beforeHeadline",x,y)
        h = max(h,h2) ; x += w2

        h2 = self.drawText(p,x,y)
        h = max(h,h2)
        x += self.widthInPixels(p.headString())

        h2,w2 = self.drawUserIcons(p,"afterHeadline",x,y)
        h = max(h,h2)

        self.drawClickBox(p,y)

        return h,indent
    #@-node:ekr.20080112145409.359:force_draw_node
    #@-node:ekr.20080112145409.358:drawNode & force_draw_node (good trace)
    #@+node:ekr.20080112145409.360:drawText
    def drawText(self,p,x,y):

        """draw text for position p at nominal coordinates x,y."""

        assert(p)

        c = self.c
        x += self.text_indent

        data = g.doHook("draw-outline-text-box",tree=self,c=c,p=p,v=p,x=x,y=y)
        if data is not None: return data

        self.newText(p,x,y+self.lineyoffset)

        self.configureTextState(p)

        return self.line_height
    #@-node:ekr.20080112145409.360:drawText
    #@+node:ekr.20080112145409.361:drawUserIcons
    def drawUserIcons(self,p,where,x,y):

        """Draw any icons specified by p.v.t.unknownAttributes["icons"]."""

        h,w = 0,0 ; t = p.v.t

        if not hasattr(t,"unknownAttributes"):
            return h,w

        iconsList = t.unknownAttributes.get("icons")
        if not iconsList:
            return h,w

        try:
            for theDict in iconsList:
                h2,w2 = self.drawUserIcon(p,where,x,y,w,theDict)
                h = max(h,h2) ; w += w2
        except:
            g.es_exception()

        # g.trace(where,h,w)

        return h,w
    #@-node:ekr.20080112145409.361:drawUserIcons
    #@+node:ekr.20080112145409.362:drawUserIcon
    def drawUserIcon (self,p,where,x,y,w2,theDict):

        h,w = 0,0

        if where != theDict.get("where","beforeHeadline"):
            return h,w

        # if self.trace_gc: g.printNewObjects(tag='userIcon 1')

        # g.trace(where,x,y,theDict)

        #@    << set offsets and pads >>
        #@+node:ekr.20080112145409.363:<< set offsets and pads >>
        xoffset = theDict.get("xoffset")
        try:    xoffset = int(xoffset)
        except: xoffset = 0

        yoffset = theDict.get("yoffset")
        try:    yoffset = int(yoffset)
        except: yoffset = 0

        xpad = theDict.get("xpad")
        try:    xpad = int(xpad)
        except: xpad = 0

        ypad = theDict.get("ypad")
        try:    ypad = int(ypad)
        except: ypad = 0
        #@-node:ekr.20080112145409.363:<< set offsets and pads >>
        #@nl
        theType = theDict.get("type")
        if theType == "icon":
            if 0: # not ready yet.
                s = theDict.get("icon")
                #@            << draw the icon in string s >>
                #@+node:ekr.20080112145409.364:<< draw the icon in string s >>
                pass
                #@-node:ekr.20080112145409.364:<< draw the icon in string s >>
                #@nl
        elif theType == "file":
            theFile = theDict.get("file")
            #@        << draw the icon at file >>
            #@+node:ekr.20080112145409.365:<< draw the icon at file >>
            try:
                image = self.iconimages[theFile]
                # Get the image from the cache if possible.
            except KeyError:
                try:
                    fullname = g.os_path_join(g.app.loadDir,"..","Icons",theFile)
                    fullname = g.os_path_normpath(fullname)
                    image = Tk.PhotoImage(master=self.canvas,file=fullname)
                    self.iconimages[fullname] = image
                except:
                    #g.es("Exception loading: " + fullname)
                    #g.es_exception()
                    image = None

            if image:
                theId = self.canvas.create_image(
                    x+xoffset+w2,y+yoffset,
                    anchor="nw",image=image,tag="userIcon")
                self.ids[theId] = p
                # assert(theId not in self.visibleIcons)
                self.visibleUserIcons.append(theId)

                h = image.height() + yoffset + ypad
                w = image.width()  + xoffset + xpad
            #@-node:ekr.20080112145409.365:<< draw the icon at file >>
            #@nl
        elif theType == "url":
            ## url = theDict.get("url")
            #@        << draw the icon at url >>
            #@+node:ekr.20080112145409.366:<< draw the icon at url >>
            pass
            #@-node:ekr.20080112145409.366:<< draw the icon at url >>
            #@nl

        # Allow user to specify height, width explicitly.
        h = theDict.get("height",h)
        w = theDict.get("width",w)

        # if self.trace_gc: g.printNewObjects(tag='userIcon 2')

        return h,w
    #@-node:ekr.20080112145409.362:drawUserIcon
    #@+node:ekr.20080112145409.367:drawTopTree
    def drawTopTree (self):

        """Draws the top-level tree, taking into account the hoist state."""

        c = self.c ; canvas = self.canvas
        trace = False or self.trace or self.trace_redraw

        self.redrawing = True

        # Recycle all widgets and clear all widget lists.
        self.recycleWidgets()
        # Clear all ids so invisible id's don't confuse eventToPosition & findPositionWithIconId
        self.ids = {}
        self.iconIds = {}
        self.generation += 1
        self.redrawCount += 1
        self.drag_p = None # Disable drags across redraws.
        self.dragging = False
        if trace:
            g.trace('redrawCount',self.redrawCount,g.callers()) # 'len(c.hoistStack)',len(c.hoistStack))
            if 0:
                delta = g.app.positions - self.prevPositions
                g.trace("**** gen: %-3d positions: %5d +%4d" % (
                    self.generation,g.app.positions,delta),g.callers())

        self.prevPositions = g.app.positions
        if self.trace_gc: g.printNewObjects(tag='top 1')

        hoistFlag = c.hoistStack
        if c.hoistStack:
            bunch = c.hoistStack[-1] ; p = bunch.p
            h = p.headString()
            if len(c.hoistStack) == 1 and h.startswith('@chapter') and p.hasChildren():
                p = p.firstChild()
                hoistFlag = False
        else:
            p = c.rootPosition()

        self.drawTree(p,self.root_left,self.root_top,0,0,hoistFlag=hoistFlag)

        if self.trace_gc: g.printNewObjects(tag='top 2')
        if self.trace_stats: self.showStats()

        canvas.lower("lines")  # Lowest.
        canvas.lift("textBox") # Not the Tk.Text widget: it should be low.
        canvas.lift("userIcon")
        canvas.lift("plusBox")
        canvas.lift("clickBox")
        canvas.lift("clickExpandBox")
        canvas.lift("iconBox") # Higest.

        self.redrawing = False
    #@-node:ekr.20080112145409.367:drawTopTree
    #@+node:ekr.20080112145409.368:drawTree
    def drawTree(self,p,x,y,h,level,hoistFlag=False):

        tree = self ; c = self.c
        yfirst = ylast = y ; h1 = None
        data = g.doHook("draw-sub-outline",tree=tree,
            c=c,p=p,v=p,x=x,y=y,h=h,level=level,hoistFlag=hoistFlag)
        if data is not None: return data

        while p: # Do not use iterator.
            # This is the ONLY copy of p that needs to be made;
            # no other drawing routine calls any p.moveTo method.
            const_p = p.copy()
            h,indent = self.drawNode(const_p,x,y)
            if h1 is None: h1 = h # Set h1 *after* calling drawNode.
            y += h ; ylast = y
            if p.isExpanded() and p.hasFirstChild():
                # Must make an additional copy here by calling firstChild.
                y = self.drawTree(p.firstChild(),x+indent,y,h,level+1)
            if hoistFlag: break
            else:         p = p.next()
        # Draw the vertical line.
        if h1 is None: h1 = h
        y2 = g.choose(level==0,yfirst+(h1-1)/2,yfirst-h1/2-1)
        self.drawLine(None,x,y2,x,ylast+self.hline_y-h)
        return y
    #@-node:ekr.20080112145409.368:drawTree
    #@-node:ekr.20080112145409.352:drawX...
    #@+node:ekr.20080112145409.369:Helpers...
    #@+node:ekr.20080112145409.370:getIconImage
    def getIconImage (self, name):

        # Return the image from the cache if possible.
        if self.iconimages.has_key(name):
            return self.iconimages[name]

        # g.trace(name)

        try:
            fullname = g.os_path_join(g.app.loadDir,"..","Icons",name)
            fullname = g.os_path_normpath(fullname)
            image = Tk.PhotoImage(master=self.canvas,file=fullname)
            self.iconimages[name] = image
            return image
        except:
            g.es("Exception loading: " + fullname)
            g.es_exception()
            return None
    #@-node:ekr.20080112145409.370:getIconImage
    #@+node:ekr.20080112145409.371:inVisibleArea & inExpandedVisibleArea
    def inVisibleArea (self,y1):

        if self.allocateOnlyVisibleNodes:
            if self.visibleArea:
                vis1,vis2 = self.visibleArea
                y2 = y1 + self.line_height
                return y2 >= vis1 and y1 <= vis2
            else: return False
        else:
            return True # This forces all nodes to be allocated on all redraws.

    def inExpandedVisibleArea (self,y1):

        if self.expandedVisibleArea:
            vis1,vis2 = self.expandedVisibleArea
            y2 = y1 + self.line_height
            return y2 >= vis1 and y1 <= vis2
        else:
            return False
    #@-node:ekr.20080112145409.371:inVisibleArea & inExpandedVisibleArea
    #@+node:ekr.20080112145409.372:numberOfVisibleNodes
    def numberOfVisibleNodes(self):

        c = self.c

        n = 0 ; p = self.c.rootPosition()
        while p:
            n += 1
            p.moveToVisNext(c)
        return n
    #@-node:ekr.20080112145409.372:numberOfVisibleNodes
    #@+node:ekr.20080112145409.373:scrollTo (gtkTree)
    def scrollTo(self,p=None):

        """Scrolls the canvas so that p is in view."""

        # __pychecker__ = '--no-argsused' # event not used.
        # __pychecker__ = '--no-intdivide' # suppress warning about integer division.

        c = self.c ; frame = c.frame ; trace = True
        if not p or not c.positionExists(p):
            p = c.currentPosition()
        if not p or not c.positionExists(p):
            if trace: g.trace('current p does not exist',p)
            p = c.rootPosition()
        if not p or not c.positionExists(p):
            if trace: g.trace('no root position')
            return
        try:
            h1 = self.yoffset(p)
            if self.center_selected_tree_node: # New in Leo 4.4.3.
                #@            << compute frac0 >>
                #@+node:ekr.20080112145409.374:<< compute frac0 >>
                # frac0 attempt to put the 
                scrollRegion = self.canvas.cget('scrollregion')
                geom = self.canvas.winfo_geometry()

                if scrollRegion and geom:
                    scrollRegion = scrollRegion.split(' ')
                    # g.trace('scrollRegion',repr(scrollRegion))
                    htot = int(scrollRegion[3])
                    wh,junk,junk = geom.split('+')
                    junk,h = wh.split('x')
                    if h: wtot = int(h)
                    else: wtot = 500
                    # g.trace('geom',geom,'wtot',wtot)
                    if htot > 0.1:
                        frac0 = float(h1-wtot/2)/float(htot)
                        frac0 = max(min(frac0,1.0),0.0)
                    else:
                        frac0 = 0.0
                else:
                    frac0 = 0.0 ; htot = wtot = 0
                #@-node:ekr.20080112145409.374:<< compute frac0 >>
                #@nl
                delta = abs(self.prevMoveToFrac-frac0)
                # g.trace(delta)
                if delta > 0.0:
                    self.prevMoveToFrac = frac0
                    self.canvas.yview("moveto",frac0)
                    if trace: g.trace("frac0 %1.2f %3d %3d %3d" % (frac0,h1,htot,wtot))
            else:
                last = c.lastVisible()
                nextToLast = last.visBack(c)
                h2 = self.yoffset(last)
                #@            << compute approximate line height >>
                #@+node:ekr.20080112145409.375:<< compute approximate line height >>
                if nextToLast: # 2/2/03: compute approximate line height.
                    lineHeight = h2 - self.yoffset(nextToLast)
                else:
                    lineHeight = 20 # A reasonable default.
                #@-node:ekr.20080112145409.375:<< compute approximate line height >>
                #@nl
                #@            << Compute the fractions to scroll down/up >>
                #@+node:ekr.20080112145409.376:<< Compute the fractions to scroll down/up >>
                data = frame.canvas.leo_treeBar.get() # Get the previous values of the scrollbar.
                try: lo, hi = data
                except: lo,hi = 0.0,1.0

                # h1 and h2 are the y offsets of the present and last nodes.
                if h2 > 0.1:
                    frac = float(h1)/float(h2) # For scrolling down.
                    frac2 = float(h1+lineHeight/2)/float(h2) # For scrolling up.
                    frac2 = frac2 - (hi - lo)
                else:
                    frac = frac2 = 0.0 # probably any value would work here.

                frac =  max(min(frac,1.0),0.0)
                frac2 = max(min(frac2,1.0),0.0)
                #@nonl
                #@-node:ekr.20080112145409.376:<< Compute the fractions to scroll down/up >>
                #@nl
                if frac <= lo: # frac is for scrolling down.
                    if self.prevMoveToFrac != frac:
                        self.prevMoveToFrac = frac
                        self.canvas.yview("moveto",frac)
                        if trace: g.trace("frac  %1.2f %3d %3d %1.2f %1.2f" % (frac, h1,h2,lo,hi))
                elif frac2 + (hi - lo) >= hi: # frac2 is for scrolling up.
                    if self.prevMoveToFrac != frac2:
                        self.prevMoveToFrac = frac2
                        self.canvas.yview("moveto",frac2)
                        if trace: g.trace("frac2 1.2f %3d %3d %1.2f %1.2f" % (frac2,h1,h2,lo,hi))

            if self.allocateOnlyVisibleNodes:
                pass ### self.canvas.after_idle(self.idle_second_redraw)

            c.setTopVnode(p) # 1/30/04: remember a pseudo "top" node.

        except:
            g.es_exception()

    idle_scrollTo = scrollTo # For compatibility.
    #@nonl
    #@-node:ekr.20080112145409.373:scrollTo (gtkTree)
    #@+node:ekr.20080112145409.377:yoffset (gtkTree)
    #@+at 
    #@nonl
    # We can't just return icony because the tree hasn't been redrawn yet.
    # For the same reason we can't rely on any TK canvas methods here.
    #@-at
    #@@c

    def yoffset(self,p1):
        # if not p1.isVisible(): print "yoffset not visible:",p1
        if not p1: return 0
        if c.hoistStack:
            bunch = c.hoistStack[-1]
            root = bunch.p.copy()
        else:
            root = self.c.rootPosition()
        if root:
            h,flag = self.yoffsetTree(root,p1)
            # flag can be False during initialization.
            # if not flag: print "yoffset fails:",h,v1
            return h
        else:
            return 0

    def yoffsetTree(self,p,p1):
        h = 0 ; trace = False
        if not self.c.positionExists(p):
            if trace: g.trace('does not exist',p.headString())
            return h,False # An extra precaution.
        p = p.copy()
        for p2 in p.self_and_siblings_iter():  # was p.siblings_iter
            print "yoffsetTree:", p2
            if p2 == p1:
                if trace: g.trace(p.headString(),p1.headString(),h)
                return h, True
            h += self.line_height
            if p2.isExpanded() and p2.hasChildren():
                child = p2.firstChild()
                h2, flag = self.yoffsetTree(child,p1)
                h += h2
                if flag:
                    if trace: g.trace(p.headString(),p1.headString(),h)
                    return h, True

        if trace: g.trace('not found',p.headString(),p1.headString())
        return h, False
    #@-node:ekr.20080112145409.377:yoffset (gtkTree)
    #@-node:ekr.20080112145409.369:Helpers...
    #@-node:ekr.20080112145409.347:Drawing... (gtkTree)
    #@+node:ekr.20080112145409.378:Event handlers (gtkTree)
    #@+node:ekr.20080112145409.379:Helpers
    #@+node:ekr.20080112145409.380:checkWidgetList
    def checkWidgetList (self,tag):

        return True # This will fail when the headline actually changes!

        for w in self.visibleText:

            p = w.leo_position
            if p:
                s = w.getAllText().strip()
                h = p.headString().strip()

                if h != s:
                    self.dumpWidgetList(tag)
                    return False
            else:
                self.dumpWidgetList(tag)
                return False

        return True
    #@-node:ekr.20080112145409.380:checkWidgetList
    #@+node:ekr.20080112145409.381:dumpWidgetList
    def dumpWidgetList (self,tag):

        print
        print "checkWidgetList: %s" % tag

        for w in self.visibleText:

            p = w.leo_position
            if p:
                s = w.getAllText().strip()
                h = p.headString().strip()

                addr = self.textAddr(w)
                print "p:",addr,h
                if h != s:
                    print "w:",'*' * len(addr),s
            else:
                print "w.leo_position == None",w
    #@-node:ekr.20080112145409.381:dumpWidgetList
    #@+node:ekr.20080112145409.382:tree.edit_widget
    def edit_widget (self,p):

        """Returns the Tk.Edit widget for position p."""

        return self.findEditWidget(p)
    #@nonl
    #@-node:ekr.20080112145409.382:tree.edit_widget
    #@+node:ekr.20080112145409.383:eventToPosition
    def eventToPosition (self,event):

        canvas = self.canvas
        x,y = event.x,event.y
        x = canvas.canvasx(x) 
        y = canvas.canvasy(y)
        if self.trace: g.trace(x,y)
        item = canvas.find_overlapping(x,y,x,y)
        if not item: return None

        # Item may be a tuple, possibly empty.
        try:    theId = item[0]
        except: theId = item
        if not theId: return None

        p = self.ids.get(theId)

        # A kludge: p will be None for vertical lines.
        if not p:
            item = canvas.find_overlapping(x+1,y,x+1,y)
            try:    theId = item[0]
            except: theId = item
            if not theId:
                g.es_print('oops: eventToPosition failed')
                return None
            p = self.ids.get(theId)
            # g.trace("was vertical line",p)

        if self.trace and self.verbose:
            if p:
                w = self.findEditWidget(p)
                g.trace("%3d %3d %3d %d" % (theId,x,y,id(w)),p.headString())
            else:
                g.trace("%3d %3d %3d" % (theId,x,y),None)

        # defensive programming: this copy is not needed.
        if p: return p.copy() # Make _sure_ nobody changes this table!
        else: return None
    #@-node:ekr.20080112145409.383:eventToPosition
    #@+node:ekr.20080112145409.384:findEditWidget
    def findEditWidget (self,p):

        """Return the Tk.Text item corresponding to p."""

        c = self.c

        if p and c:
            aTuple = self.visibleText.get(p.key())
            if aTuple:
                w,theId = aTuple
                # g.trace('%4d' % (theId),self.textAddr(w),p.headString())
                return w
            else:
                # g.trace('oops: not found',p)
                return None

        # g.trace(not found',p.headString())
        return None
    #@-node:ekr.20080112145409.384:findEditWidget
    #@+node:ekr.20080112145409.385:findVnodeWithIconId
    def findPositionWithIconId (self,theId):

        # Due to an old bug, theId may be a tuple.
        try:
            data = self.iconIds.get(theId[0])
        except:
            data = self.iconIds.get(theId)

        if data:
            p,generation = data
            if generation==self.generation:
                if self.trace and self.verbose:
                    g.trace(theId,p.headString())
                return p
            else:
                if self.trace and self.verbose:
                    g.trace("*** wrong generation: %d ***" % theId)
                return None
        else:
            if self.trace and self.verbose: g.trace(theId,None)
            return None
    #@-node:ekr.20080112145409.385:findVnodeWithIconId
    #@-node:ekr.20080112145409.379:Helpers
    #@+node:ekr.20080112145409.386:Click Box...
    #@+node:ekr.20080112145409.387:onClickBoxClick
    def onClickBoxClick (self,event,p=None):

        c = self.c ; p1 = c.currentPosition()

        if not p: p = self.eventToPosition(event)
        if not p: return

        c.setLog()

        c.beginUpdate()
        try:
            if p and not g.doHook("boxclick1",c=c,p=p,v=p,event=event):
                c.endEditing()
                if p == p1 or self.initialClickExpandsOrContractsNode:
                    if p.isExpanded(): p.contract()
                    else:              p.expand()
                self.select(p)
                if c.frame.findPanel:
                    c.frame.findPanel.handleUserClick(p)
                if self.stayInTree:
                    c.treeWantsFocus()
                else:
                    c.bodyWantsFocus()
            g.doHook("boxclick2",c=c,p=p,v=p,event=event)
        finally:
            c.endUpdate()
    #@-node:ekr.20080112145409.387:onClickBoxClick
    #@-node:ekr.20080112145409.386:Click Box...
    #@+node:ekr.20080112145409.388:Dragging (gtkTree)
    #@+node:ekr.20080112145409.389:endDrag
    def endDrag (self,event):

        """The official helper of the onEndDrag event handler."""

        c = self.c ; p = self.drag_p
        c.setLog()
        canvas = self.canvas
        if not event: return

        c.beginUpdate()
        try:
            #@        << set vdrag, childFlag >>
            #@+node:ekr.20080112145409.390:<< set vdrag, childFlag >>
            x,y = event.x,event.y
            canvas_x = canvas.canvasx(x)
            canvas_y = canvas.canvasy(y)

            theId = self.canvas.find_closest(canvas_x,canvas_y)
            # theId = self.canvas.find_overlapping(canvas_x,canvas_y,canvas_x,canvas_y)

            vdrag = self.findPositionWithIconId(theId)
            childFlag = vdrag and vdrag.hasChildren() and vdrag.isExpanded()
            #@-node:ekr.20080112145409.390:<< set vdrag, childFlag >>
            #@nl
            if self.allow_clone_drags:
                if not self.look_for_control_drag_on_mouse_down:
                    self.controlDrag = c.frame.controlKeyIsDown

            redrawFlag = vdrag and vdrag.v.t != p.v.t
            if redrawFlag: # Disallow drag to joined node.
                #@            << drag p to vdrag >>
                #@+node:ekr.20080112145409.391:<< drag p to vdrag >>
                # g.trace("*** end drag   ***",theId,x,y,p.headString(),vdrag.headString())

                if self.controlDrag: # Clone p and move the clone.
                    if childFlag:
                        c.dragCloneToNthChildOf(p,vdrag,0)
                    else:
                        c.dragCloneAfter(p,vdrag)
                else: # Just drag p.
                    if childFlag:
                        c.dragToNthChildOf(p,vdrag,0)
                    else:
                        c.dragAfter(p,vdrag)
                #@-node:ekr.20080112145409.391:<< drag p to vdrag >>
                #@nl
            elif self.trace and self.verbose:
                g.trace("Cancel drag")

            # Reset the old cursor by brute force.
            self.canvas['cursor'] = "arrow"
            self.dragging = False
            self.drag_p = None
        finally:
            # Must set self.drag_p = None first.
            c.endUpdate(redrawFlag)
            c.recolor_now() # Dragging can affect coloring.
    #@-node:ekr.20080112145409.389:endDrag
    #@+node:ekr.20080112145409.392:startDrag
    # This precomputes numberOfVisibleNodes(), a significant optimization.
    # We also indicate where findPositionWithIconId() should start looking for tree id's.

    def startDrag (self,event,p=None):

        """The official helper of the onDrag event handler."""

        c = self.c ; canvas = self.canvas

        if not p:
            assert(not self.drag_p)
            x = canvas.canvasx(event.x)
            y = canvas.canvasy(event.y)
            theId = canvas.find_closest(x,y)
            # theId = canvas.find_overlapping(canvas_x,canvas_y,canvas_x,canvas_y)
            if theId is None: return
            try: theId = theId[0]
            except: pass
            p = self.ids.get(theId)
        if not p: return
        c.setLog()
        self.drag_p = p.copy() # defensive programming: not needed.
        self.dragging = True
        # g.trace("*** start drag ***",theId,self.drag_p.headString())
        # Only do this once: greatly speeds drags.
        self.savedNumberOfVisibleNodes = self.numberOfVisibleNodes()
        # g.trace('self.controlDrag',self.controlDrag)
        if self.allow_clone_drags:
            self.controlDrag = c.frame.controlKeyIsDown
            if self.look_for_control_drag_on_mouse_down:
                if self.enable_drag_messages:
                    if self.controlDrag:
                        g.es("dragged node will be cloned")
                    else:
                        g.es("dragged node will be moved")
        else: self.controlDrag = False
        self.canvas['cursor'] = "hand2" # "center_ptr"
    #@-node:ekr.20080112145409.392:startDrag
    #@+node:ekr.20080112145409.393:onContinueDrag
    def onContinueDrag(self,event):

        p = self.drag_p
        if not p: return

        try:
            canvas = self.canvas ; frame = self.c.frame
            if event:
                x,y = event.x,event.y
            else:
                x,y = frame.top.winfo_pointerx(),frame.top.winfo_pointery()
                # Stop the scrolling if we go outside the entire window.
                if x == -1 or y == -1: return 
            if self.dragging: # This gets cleared by onEndDrag()
                #@            << scroll the canvas as needed >>
                #@+node:ekr.20080112145409.394:<< scroll the canvas as needed >>
                # Scroll the screen up or down one line if the cursor (y) is outside the canvas.
                h = canvas.winfo_height()

                if y < 0 or y > h:
                    lo, hi = frame.canvas.leo_treeBar.get()
                    n = self.savedNumberOfVisibleNodes
                    line_frac = 1.0 / float(n)
                    frac = g.choose(y < 0, lo - line_frac, lo + line_frac)
                    frac = min(frac,1.0)
                    frac = max(frac,0.0)
                    # g.es("lo,hi,frac:",lo,hi,frac)
                    canvas.yview("moveto", frac)

                    # Queue up another event to keep scrolling while the cursor is outside the canvas.
                    lo, hi = frame.canvas.leo_treeBar.get()
                    if (y < 0 and lo > 0.1) or (y > h and hi < 0.9):
                        pass ### canvas.after_idle(self.onContinueDrag,None) # Don't propagate the event.
                #@-node:ekr.20080112145409.394:<< scroll the canvas as needed >>
                #@nl
        except:
            g.es_event_exception("continue drag")
    #@-node:ekr.20080112145409.393:onContinueDrag
    #@+node:ekr.20080112145409.395:onDrag
    def onDrag(self,event):

        c = self.c ; p = self.drag_p
        if not event: return

        c.setLog()

        if not self.dragging:
            if not g.doHook("drag1",c=c,p=p,v=p,event=event):
                self.startDrag(event)
            g.doHook("drag2",c=c,p=p,v=p,event=event)

        if not g.doHook("dragging1",c=c,p=p,v=p,event=event):
            self.onContinueDrag(event)
        g.doHook("dragging2",c=c,p=p,v=p,event=event)
    #@-node:ekr.20080112145409.395:onDrag
    #@+node:ekr.20080112145409.396:onEndDrag
    def onEndDrag(self,event):

        """Tree end-of-drag handler called from vnode event handler."""

        c = self.c ; p = self.drag_p
        if not p: return

        c.setLog()

        if not g.doHook("enddrag1",c=c,p=p,v=p,event=event):
            self.endDrag(event)
        g.doHook("enddrag2",c=c,p=p,v=p,event=event)
    #@-node:ekr.20080112145409.396:onEndDrag
    #@-node:ekr.20080112145409.388:Dragging (gtkTree)
    #@+node:ekr.20080112145409.397:Icon Box...
    #@+node:ekr.20080112145409.398:onIconBoxClick
    def onIconBoxClick (self,event,p=None):

        c = self.c ; tree = self

        if not p: p = self.eventToPosition(event)
        if not p: return

        c.setLog()

        if self.trace and self.verbose: g.trace()

        if not g.doHook("iconclick1",c=c,p=p,v=p,event=event):
            if event:
                self.onDrag(event)
            tree.endEditLabel()
            tree.select(p,scroll=False)
            if c.frame.findPanel:
                c.frame.findPanel.handleUserClick(p)
        g.doHook("iconclick2",c=c,p=p,v=p,event=event)

        return "break" # disable expanded box handling.
    #@-node:ekr.20080112145409.398:onIconBoxClick
    #@+node:ekr.20080112145409.399:onIconBoxRightClick
    def onIconBoxRightClick (self,event,p=None):

        """Handle a right click in any outline widget."""

        c = self.c

        if not p: p = self.eventToPosition(event)
        if not p: return

        c.setLog()

        try:
            if not g.doHook("iconrclick1",c=c,p=p,v=p,event=event):
                self.OnActivateHeadline(p)
                self.endEditLabel()
                self.OnPopup(p,event)
            g.doHook("iconrclick2",c=c,p=p,v=p,event=event)
        except:
            g.es_event_exception("iconrclick")

        return 'break'
    #@-node:ekr.20080112145409.399:onIconBoxRightClick
    #@+node:ekr.20080112145409.400:onIconBoxDoubleClick
    def onIconBoxDoubleClick (self,event,p=None):

        c = self.c

        if not p: p = self.eventToPosition(event)
        if not p: return

        c.setLog()

        if self.trace and self.verbose: g.trace()

        try:
            if not g.doHook("icondclick1",c=c,p=p,v=p,event=event):
                self.endEditLabel() # Bug fix: 11/30/05
                self.OnIconDoubleClick(p) # Call the method in the base class.
            g.doHook("icondclick2",c=c,p=p,v=p,event=event)
        except:
            g.es_event_exception("icondclick")

        return 'break' # 11/19/06
    #@-node:ekr.20080112145409.400:onIconBoxDoubleClick
    #@-node:ekr.20080112145409.397:Icon Box...
    #@+node:ekr.20080112145409.401:OnActivateHeadline (gtkTree)
    def OnActivateHeadline (self,p,event=None):

        '''Handle common process when any part of a headline is clicked.'''

        # g.trace(p.headString())

        returnVal = 'break' # Default: do nothing more.
        trace = False

        try:
            c = self.c
            c.setLog()
            #@        << activate this window >>
            #@+node:ekr.20080112145409.402:<< activate this window >>
            if p == c.currentPosition():

                if trace: g.trace('current','active',self.active)
                self.editLabel(p) # sets focus.
                # If we are active, pass the event along so the click gets handled.
                # Otherwise, do *not* pass the event along so the focus stays the same.
                returnVal = g.choose(self.active,'continue','break')
                self.active = True
            else:
                if trace: g.trace("not current")
                self.select(p,scroll=False)
                w  = c.frame.body.bodyCtrl
                if c.frame.findPanel:
                    c.frame.findPanel.handleUserClick(p)
                if p.v.t.insertSpot != None:
                    spot = p.v.t.insertSpot
                    w.setInsertPoint(spot)
                    w.see(spot)
                else:
                    w.setInsertPoint(0)
                # An important detail.
                # The *canvas* (not the headline) gets the focus so that
                # tree bindings take priority over text bindings.
                c.treeWantsFocus()
                self.active = False
                returnVal = 'break'
            #@nonl
            #@-node:ekr.20080112145409.402:<< activate this window >>
            #@nl
        except:
            g.es_event_exception("activate tree")

        return returnVal
    #@-node:ekr.20080112145409.401:OnActivateHeadline (gtkTree)
    #@+node:ekr.20080112145409.403:Text Box...
    #@+node:ekr.20080112145409.404:configureTextState
    def configureTextState (self,p):

        c = self.c

        if not p: return

        # g.trace(p.headString(),self.c._currentPosition)

        if c.isCurrentPosition(p):
            if p == self.editPosition():
                self.setEditLabelState(p) # selected, editing.
            else:
                self.setSelectedLabelState(p) # selected, not editing.
        else:
            self.setUnselectedLabelState(p) # unselected
    #@-node:ekr.20080112145409.404:configureTextState
    #@+node:ekr.20080112145409.405:onCtontrolT
    # This works around an apparent Tk bug.

    def onControlT (self,event=None):

        # If we don't inhibit further processing the Tx.Text widget switches characters!
        return "break"
    #@-node:ekr.20080112145409.405:onCtontrolT
    #@+node:ekr.20080112145409.406:onHeadlineClick
    def onHeadlineClick (self,event,p=None):

        # g.trace('p',p)
        c = self.c ; w = event.widget

        if not p:
            try:
                p = w.leo_position
            except AttributeError:
                g.trace('*'*20,'oops')
        if not p: return 'break'

        # g.trace(g.app.gui.widget_name(w)) #p.headString())

        c.setLog()

        try:
            if not g.doHook("headclick1",c=c,p=p,v=p,event=event):
                returnVal = self.OnActivateHeadline(p)
            g.doHook("headclick2",c=c,p=p,v=p,event=event)
        except:
            returnVal = 'break'
            g.es_event_exception("headclick")

        # 'continue' is sometimes correct here.
        # 'break' would make it impossible to unselect the headline text.
        # g.trace('returnVal',returnVal,'stayInTree',self.stayInTree)
        return returnVal
    #@-node:ekr.20080112145409.406:onHeadlineClick
    #@+node:ekr.20080112145409.407:onHeadlineRightClick
    def onHeadlineRightClick (self,event):

        """Handle a right click in any outline widget."""

        c = self.c ; w = event.widget

        try:
            p = w.leo_position
        except AttributeError:
            g.trace('*'*20,'oops')
            return 'break'

        c.setLog()

        try:
            if not g.doHook("headrclick1",c=c,p=p,v=p,event=event):
                self.OnActivateHeadline(p)
                self.endEditLabel()
                self.OnPopup(p,event)
            g.doHook("headrclick2",c=c,p=p,v=p,event=event)
        except:
            g.es_event_exception("headrclick")

        # 'continue' *is* correct here.
        # 'break' would make it impossible to unselect the headline text.
        return 'continue'
    #@-node:ekr.20080112145409.407:onHeadlineRightClick
    #@-node:ekr.20080112145409.403:Text Box...
    #@+node:ekr.20080112145409.408:tree.OnDeactivate
    def OnDeactivate (self,event=None):

        """Deactivate the tree pane, dimming any headline being edited."""

        # __pychecker__ = '--no-argsused' # event not used.

        tree = self ; c = self.c

        # g.trace(g.callers())

        c.beginUpdate()
        try:
            tree.endEditLabel()
            tree.dimEditLabel()
        finally:
            c.endUpdate(False)
    #@-node:ekr.20080112145409.408:tree.OnDeactivate
    #@+node:ekr.20080112145409.409:tree.OnPopup & allies
    def OnPopup (self,p,event):

        """Handle right-clicks in the outline.

        This is *not* an event handler: it is called from other event handlers."""

        # Note: "headrclick" hooks handled by vnode callback routine.

        if event != None:
            c = self.c
            c.setLog()

            if not g.doHook("create-popup-menu",c=c,p=p,v=p,event=event):
                self.createPopupMenu(event)
            if not g.doHook("enable-popup-menu-items",c=c,p=p,v=p,event=event):
                self.enablePopupMenuItems(p,event)
            if not g.doHook("show-popup-menu",c=c,p=p,v=p,event=event):
                self.showPopupMenu(event)

        return "break"
    #@+node:ekr.20080112145409.410:OnPopupFocusLost
    #@+at 
    #@nonl
    # On Linux we must do something special to make the popup menu "unpost" if 
    # the mouse is clicked elsewhere.  So we have to catch the <FocusOut> 
    # event and explicitly unpost.  In order to process the <FocusOut> event, 
    # we need to be able to find the reference to the popup window again, so 
    # this needs to be an attribute of the tree object; hence, 
    # "self.popupMenu".
    # 
    # Aside: though Tk tries to be muli-platform, the interaction with 
    # different window managers does cause small differences that will need to 
    # be compensated by system specific application code. :-(
    #@-at
    #@@c

    # 20-SEP-2002 DTHEIN: This event handler is only needed for Linux.

    def OnPopupFocusLost(self,event=None):

        # __pychecker__ = '--no-argsused' # event not used.

        self.popupMenu.unpost()
    #@-node:ekr.20080112145409.410:OnPopupFocusLost
    #@+node:ekr.20080112145409.411:createPopupMenu
    def createPopupMenu (self,event):

        # __pychecker__ = '--no-argsused' # event not used.

        c = self.c ; frame = c.frame

        # If we are going to recreate it, we had better destroy it.
        if self.popupMenu:
            self.popupMenu.destroy()
            self.popupMenu = None

        self.popupMenu = menu = Tk.Menu(g.app.root, tearoff=0)

        # Add the Open With entries if they exist.
        if g.app.openWithTable:
            frame.menu.createOpenWithMenuItemsFromTable(menu,g.app.openWithTable)
            table = (("-",None,None),)
            frame.menu.createMenuEntries(menu,table)

        #@    << Create the menu table >>
        #@+node:ekr.20080112145409.412:<< Create the menu table >>
        table = (
            ("&Read @file Nodes",c.readAtFileNodes),
            ("&Write @file Nodes",c.fileCommands.writeAtFileNodes),
            ("-",None),
            ("&Tangle",c.tangle),
            ("&Untangle",c.untangle),
            ("-",None),
            ("Toggle Angle &Brackets",c.toggleAngleBrackets),
            ("-",None),
            ("Cut Node",c.cutOutline),
            ("Copy Node",c.copyOutline),
            ("&Paste Node",c.pasteOutline),
            ("&Delete Node",c.deleteOutline),
            ("-",None),
            ("&Insert Node",c.insertHeadline),
            ("&Clone Node",c.clone),
            ("Sort C&hildren",c.sortChildren),
            ("&Sort Siblings",c.sortSiblings),
            ("-",None),
            ("Contract Parent",c.contractParent),
        )
        #@-node:ekr.20080112145409.412:<< Create the menu table >>
        #@nl

        # New in 4.4.  There is no need for a dontBind argument because
        # Bindings from tables are ignored.
        frame.menu.createMenuEntries(menu,table)
    #@-node:ekr.20080112145409.411:createPopupMenu
    #@+node:ekr.20080112145409.413:enablePopupMenuItems
    def enablePopupMenuItems (self,v,event):

        """Enable and disable items in the popup menu."""

        # __pychecker__ = '--no-argsused' # event not used.

        c = self.c ; menu = self.popupMenu

        #@    << set isAtRoot and isAtFile if v's tree contains @root or @file nodes >>
        #@+node:ekr.20080112145409.414:<< set isAtRoot and isAtFile if v's tree contains @root or @file nodes >>
        isAtFile = False
        isAtRoot = False

        for v2 in v.self_and_subtree_iter():
            if isAtFile and isAtRoot:
                break
            if (v2.isAtFileNode() or
                v2.isAtNorefFileNode() or
                v2.isAtAsisFileNode() or
                v2.isAtNoSentFileNode()
            ):
                isAtFile = True

            isRoot,junk = g.is_special(v2.bodyString(),0,"@root")
            if isRoot:
                isAtRoot = True
        #@-node:ekr.20080112145409.414:<< set isAtRoot and isAtFile if v's tree contains @root or @file nodes >>
        #@nl
        isAtFile = g.choose(isAtFile,1,0)
        isAtRoot = g.choose(isAtRoot,1,0)
        canContract = v.parent() != None
        canContract = g.choose(canContract,1,0)

        enable = self.frame.menu.enableMenu

        for name in ("Read @file Nodes", "Write @file Nodes"):
            enable(menu,name,isAtFile)
        for name in ("Tangle", "Untangle"):
            enable(menu,name,isAtRoot)

        enable(menu,"Cut Node",c.canCutOutline())
        enable(menu,"Delete Node",c.canDeleteHeadline())
        enable(menu,"Paste Node",c.canPasteOutline())
        enable(menu,"Sort Children",c.canSortChildren())
        enable(menu,"Sort Siblings",c.canSortSiblings())
        enable(menu,"Contract Parent",c.canContractParent())
    #@-node:ekr.20080112145409.413:enablePopupMenuItems
    #@+node:ekr.20080112145409.415:showPopupMenu
    def showPopupMenu (self,event):

        """Show a popup menu."""

        c = self.c ; menu = self.popupMenu

        ###

        # if sys.platform == "linux2": # 20-SEP-2002 DTHEIN: not needed for Windows
            # menu.bind("<FocusOut>",self.OnPopupFocusLost)

        # menu.post(event.x_root, event.y_root)

        # # Set the focus immediately so we know when we lose it.
        # c.widgetWantsFocus(menu)
    #@-node:ekr.20080112145409.415:showPopupMenu
    #@-node:ekr.20080112145409.409:tree.OnPopup & allies
    #@+node:ekr.20080112145409.416:onTreeClick
    def onTreeClick (self,event=None):

        '''Handle an event in the tree canvas, outside of any tree widget.'''

        c = self.c

        # New in Leo 4.4.2: a kludge: disable later event handling after a double-click.
        # This allows focus to stick in newly-opened files opened by double-clicking an @url node.
        if c.doubleClickFlag:
            c.doubleClickFlag = False
        else:
            c.treeWantsFocusNow()

        return 'break'
    #@-node:ekr.20080112145409.416:onTreeClick
    #@-node:ekr.20080112145409.378:Event handlers (gtkTree)
    #@+node:ekr.20080112145409.417:Incremental drawing...
    #@+node:ekr.20080112145409.418:allocateNodes
    def allocateNodes(self,where,lines):

        """Allocate Tk widgets in nodes that will become visible as the result of an upcoming scroll"""

        assert(where in ("above","below"))

        # print "allocateNodes: %d lines %s visible area" % (lines,where)

        # Expand the visible area: a little extra delta is safer.
        delta = lines * (self.line_height + 4)
        y1,y2 = self.visibleArea

        if where == "below":
            y2 += delta
        else:
            y1 = max(0.0,y1-delta)

        self.expandedVisibleArea=y1,y2
        # print "expandedArea:   %5.1f %5.1f" % (y1,y2)

        # Allocate all nodes in expanded visible area.
        self.updatedNodeCount = 0
        self.updateTree(self.c.rootPosition(),self.root_left,self.root_top,0,0)
        # if self.updatedNodeCount: print "updatedNodeCount:", self.updatedNodeCount
    #@-node:ekr.20080112145409.418:allocateNodes
    #@+node:ekr.20080112145409.419:allocateNodesBeforeScrolling
    def allocateNodesBeforeScrolling (self, args):

        """Calculate the nodes that will become visible as the result of an upcoming scroll.

        args is the tuple passed to the Tk.Canvas.yview method"""

        if not self.allocateOnlyVisibleNodes: return

        # print "allocateNodesBeforeScrolling:",self.redrawCount,args

        assert(self.visibleArea)
        assert(len(args)==2 or len(args)==3)
        kind = args[0] ; n = args[1]
        lines = 2 # Update by 2 lines to account for rounding.
        if len(args) == 2:
            assert(kind=="moveto")
            frac1,frac2 = args
            if float(n) != frac1:
                where = g.choose(n<frac1,"above","below")
                self.allocateNodes(where=where,lines=lines)
        else:
            assert(kind=="scroll")
            linesPerPage = self.canvas.winfo_height()/self.line_height + 2
            n = int(n) ; assert(abs(n)==1)
            where = g.choose(n == 1,"below","above")
            lines = g.choose(args[2] == "pages",linesPerPage,lines)
            self.allocateNodes(where=where,lines=lines)
    #@-node:ekr.20080112145409.419:allocateNodesBeforeScrolling
    #@+node:ekr.20080112145409.420:updateNode
    def updateNode (self,p,x,y):

        """Draw a node that may have become visible as a result of a scrolling operation"""

        c = self.c

        if self.inExpandedVisibleArea(y):
            # This check is a major optimization.
            if not c.edit_widget(p):
                return self.force_draw_node(p,x,y)
            else:
                return self.line_height

        return self.line_height
    #@-node:ekr.20080112145409.420:updateNode
    #@+node:ekr.20080112145409.421:setVisibleAreaToFullCanvas
    def setVisibleAreaToFullCanvas(self):

        if self.visibleArea:
            y1,y2 = self.visibleArea
            y2 = max(y2,y1 + self.canvas.winfo_height())
            self.visibleArea = y1,y2
    #@-node:ekr.20080112145409.421:setVisibleAreaToFullCanvas
    #@+node:ekr.20080112145409.422:setVisibleArea
    def setVisibleArea (self,args):

        r1,r2 = args
        r1,r2 = float(r1),float(r2)
        # print "scroll ratios:",r1,r2

        try:
            s = self.canvas.cget("scrollregion")
            x1,y1,x2,y2 = g.scanf(s,"%d %d %d %d")
            x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
        except:
            self.visibleArea = None
            return

        scroll_h = y2-y1
        # print "height of scrollregion:", scroll_h

        vy1 = y1 + (scroll_h*r1)
        vy2 = y1 + (scroll_h*r2)
        self.visibleArea = vy1,vy2
        # print "setVisibleArea: %5.1f %5.1f" % (vy1,vy2)
    #@-node:ekr.20080112145409.422:setVisibleArea
    #@+node:ekr.20080112145409.423:tree.updateTree
    def updateTree (self,v,x,y,h,level):

        yfirst = y
        if level==0: yfirst += 10
        while v:
            # g.trace(x,y,v)
            h,indent = self.updateNode(v,x,y)
            y += h
            if v.isExpanded() and v.firstChild():
                y = self.updateTree(v.firstChild(),x+indent,y,h,level+1)
            v = v.next()
        return y
    #@-node:ekr.20080112145409.423:tree.updateTree
    #@-node:ekr.20080112145409.417:Incremental drawing...
    #@+node:ekr.20080112145409.424:Selecting & editing... (gtkTree)
    #@+node:ekr.20080112145409.425:dimEditLabel, undimEditLabel
    # Convenience methods so the caller doesn't have to know the present edit node.

    def dimEditLabel (self):

        p = self.c.currentPosition()
        self.setSelectedLabelState(p)

    def undimEditLabel (self):

        p = self.c.currentPosition()
        self.setSelectedLabelState(p)
    #@-node:ekr.20080112145409.425:dimEditLabel, undimEditLabel
    #@+node:ekr.20080112145409.426:tree.editLabel
    def editLabel (self,p,selectAll=False):

        """Start editing p's headline."""

        c = self.c
        trace = not g.app.unitTesting and (False or self.trace_edit)

        if p and p != self.editPosition():

            if trace:
                g.trace(p.headString(),g.choose(c.edit_widget(p),'','no edit widget'))

            c.beginUpdate()
            try:
                self.endEditLabel()
            finally:
                c.endUpdate(True)

        self.setEditPosition(p) # That is, self._editPosition = p

        if trace: g.trace(c.edit_widget(p))

        if p and c.edit_widget(p):
            self.revertHeadline = p.headString() # New in 4.4b2: helps undo.
            self.setEditLabelState(p,selectAll=selectAll) # Sets the focus immediately.
            c.headlineWantsFocus(p) # Make sure the focus sticks.
    #@-node:ekr.20080112145409.426:tree.editLabel
    #@+node:ekr.20080112145409.427:tree.set...LabelState
    #@+node:ekr.20080112145409.428:setEditLabelState
    def setEditLabelState (self,p,selectAll=False): # selected, editing

        c = self.c ; w = c.edit_widget(p)

        if p and w:
            # g.trace('*****',g.callers())
            c.widgetWantsFocusNow(w)
            self.setEditHeadlineColors(p)
            selectAll = selectAll or self.select_all_text_when_editing_headlines
            if selectAll:
                w.setSelectionRange(0,'end',insert='end')
            else:
                w.setInsertPoint('end') # Clears insert point.
        else:
            g.trace('no edit_widget')

    setNormalLabelState = setEditLabelState # For compatibility.
    #@-node:ekr.20080112145409.428:setEditLabelState
    #@+node:ekr.20080112145409.429:setSelectedLabelState
    def setSelectedLabelState (self,p): # selected, disabled

        # g.trace(p.headString(),g.callers())

        c = self.c

        if p and c.edit_widget(p):
            self.setDisabledHeadlineColors(p)
    #@-node:ekr.20080112145409.429:setSelectedLabelState
    #@+node:ekr.20080112145409.430:setUnselectedLabelState
    def setUnselectedLabelState (self,p): # not selected.

        c = self.c

        if p and c.edit_widget(p):
            self.setUnselectedHeadlineColors(p)
    #@-node:ekr.20080112145409.430:setUnselectedLabelState
    #@+node:ekr.20080112145409.431:setDisabledHeadlineColors
    def setDisabledHeadlineColors (self,p):

        c = self.c ; w = c.edit_widget(p)

        if self.trace and self.verbose:
            if not self.redrawing:
                g.trace("%10s %d %s" % ("disabled",id(w),p.headString()))
                # import traceback ; traceback.print_stack(limit=6)

        fg = self.headline_text_selected_foreground_color or 'black'
        bg = self.headline_text_selected_background_color or 'grey80'
        selfg = self.headline_text_editing_selection_foreground_color
        selbg = self.headline_text_editing_selection_background_color

        try:
            w.configure(state="disabled",highlightthickness=0,fg=fg,bg=bg,
                selectbackground=bg,selectforeground=fg,highlightbackground=bg)
        except:
            g.es_exception()
    #@-node:ekr.20080112145409.431:setDisabledHeadlineColors
    #@+node:ekr.20080112145409.432:setEditHeadlineColors
    def setEditHeadlineColors (self,p):

        c = self.c ; w = c.edit_widget(p)

        if self.trace and self.verbose:
            if not self.redrawing:
                print "%10s %d %s" % ("edit",id(2),p.headString())

        fg    = self.headline_text_editing_foreground_color or 'black'
        bg    = self.headline_text_editing_background_color or 'white'
        selfg = self.headline_text_editing_selection_foreground_color or 'white'
        selbg = self.headline_text_editing_selection_background_color or 'black'

        try: # Use system defaults for selection foreground/background
            w.configure(state="normal",highlightthickness=1,
            fg=fg,bg=bg,selectforeground=selfg,selectbackground=selbg)
        except:
            g.es_exception()
    #@-node:ekr.20080112145409.432:setEditHeadlineColors
    #@+node:ekr.20080112145409.433:setUnselectedHeadlineColors
    def setUnselectedHeadlineColors (self,p):

        c = self.c ; w = c.edit_widget(p)

        if self.trace and self.verbose:
            if not self.redrawing:
                print "%10s %d %s" % ("unselect",id(w),p.headString())
                # import traceback ; traceback.print_stack(limit=6)

        fg = self.headline_text_unselected_foreground_color or 'black'
        bg = self.headline_text_unselected_background_color or 'white'

        try:
            w.configure(state="disabled",highlightthickness=0,fg=fg,bg=bg,
                selectbackground=bg,selectforeground=fg,highlightbackground=bg)
        except:
            g.es_exception()
    #@-node:ekr.20080112145409.433:setUnselectedHeadlineColors
    #@-node:ekr.20080112145409.427:tree.set...LabelState
    #@+node:ekr.20080112145409.434:tree.setHeadline (gtkTree)
    def setHeadline (self,p,s):

        '''Set the actual text of the headline widget.

        This is called from the undo/redo logic to change the text before redrawing.'''

        w = self.edit_widget(p)
        if w:
            w.configure(state='normal')
            w.delete(0,'end')
            if s.endswith('\n') or s.endswith('\r'):
                s = s[:-1]
            w.insert(0,s)
            self.revertHeadline = s
            # g.trace(repr(s),w.getAllText())
        else:
            g.trace('-'*20,'oops')
    #@-node:ekr.20080112145409.434:tree.setHeadline (gtkTree)
    #@-node:ekr.20080112145409.424:Selecting & editing... (gtkTree)
    #@-others
#@-node:ekr.20080112145409.314:class leoGtkTree (REWRITE)
#@-others
#@-node:ekr.20080112145409.53:@thin leoGtkFrame.py
#@-leo
