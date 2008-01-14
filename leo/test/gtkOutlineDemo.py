#@+leo-ver=4
#@+node:@file /home/bob/work/leo/workleo/test/gtkOutlineTest.py

import sys, os



import pygtk
pygtk.require('2.0')
import gtk
import operator
import time
import string


print '~~~~~~~~~~~~~~~~~~~~~~~~~~~  ', __file__, sys.path[0]

#@+others
#@+node:GtkLeoTreeDemo
#@@first

# example drawingarea.py



class GtkLeoTreeDemo(object):


    #@    @+others
    #@+node:__init__
    def __init__(self):

        print 'Drawing area'

        print '=================='

        #for n in c.allNodes_iter():
        #    print n.headString()


        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("gtkLeo Outline Widget Demo")
        window.connect("destroy", lambda w: gtk.main_quit())
        window.set_size_request(10, 10)
        window.resize(400, 300)

        loadIcons()

        self.panel = OutlineCanvasPanel(window, c, 'canvas')

        self.canvas = canvas = self.panel._canvas
        g.trace(canvas)

        canvas.set_events(gtk.gdk.ALL_EVENTS_MASK)
        canvas.connect('button_press_event', self.onButtonPress)
        #canvas.connect('button_release_event', self.onButtonPress)

        window.show_all()



    #@-node:__init__
    #@+node:onButtonPress
    def onButtonPress(self, w, event, *args):

        codes = {
            gtk.gdk.BUTTON_PRESS: 'click',
            gtk.gdk._2BUTTON_PRESS: 'double_click',
            gtk.gdk._3BUTTON_PRESS: 'triple_click',
            gtk.gdk.BUTTON_RELEASE: 'release'
        }


        sp, item = self.canvas.hitTest(event.x, event.y)
        print codes[event.type], '%s[%s]: %s'%(
            g.choose(isinstance(item, int), 'headStringIcon[%s]'%item, item),
            'button-%s'%event.button,
            sp.headString()
        )

        if item == 'ClickBox' and event.button == 1:
            if sp.isExpanded():
                sp.contract()
            else:
                sp.expand()

            self.canvas.update()
    #@-node:onButtonPress
    #@+node:onButtonRelease
    #@-node:onButtonRelease
    #@-others
#@nonl
#@-node:GtkLeoTreeDemo
#@+node:loadIcon
def loadIcon(fname):

    try:
        icon = gtk.gdk.pixbuf_new_from_file(fname)
    except:
        icon = None

    if icon and icon.get_width()>0:
        return icon

    print 'Can not load icon from', fname
#@-node:loadIcon
#@+node:loadIcons
def loadIcons():

    global icons, plusBoxIcon, minusBoxIcon, appIcon, namedIcons, globalImages

    import cStringIO



    icons = []
    namedIcons = {}


    path = g.os_path_abspath(g.os_path_join(g.app.loadDir, '..', 'Icons'))
    if g.os_path_exists(g.os_path_join(path, 'box01.GIF')):
        ext = '.GIF'
    else:
        ext = '.gif'

    for i in range(16):
        icon = loadIcon(g.os_path_join(path, 'box%02d'%i + ext))
        icons.append(icon)



    for name in (
        'lt_arrow_enabled',
        'rt_arrow_enabled',
        'lt_arrow_disabled',
        'rt_arrow_disabled',
        'plusnode',
        'minusnode'
    ):
        icon = loadIcon(g.os_path_join(path, name + '.gif'))
        if icon:
            namedIcons[name] = icon

    plusBoxIcon = namedIcons['plusnode']
    minusBoxIcon = namedIcons['minusnode']

    globalImages = {}

#@-node:loadIcons
#@+node:name2Color


def name2color(name, default=None, cairo=False):




    if isinstance(name, cls ):
        return name

    color = colors.getColorRGB(name)

    if color is None:
        if default:
            return name2color(default)
        else:
            return None

    r, g, b = color

    #trace(print r, g, b)

    if cairo:
        return r/255.0, g/255.0, b/255.0 


    return gtk.gdk.Color(r,g,b)
#@-node:name2Color
#@+node:getImage
def getImage (relPath, force=False):


    if not force and relPath in globalImages:
        image = globalImages[relPath]
        g.es('cach ', image, image.get_height(), getColor('magenta'))
        return image, image.get_height()

    try:
        path = g.os_path_normpath(g.os_path_join(g.app.loadDir,"..","Icons", relPath))
        globalImages[relPath] = image = loadIcon(path)
        return image

    except Exception:
        pass

    try:
        path = g.os_path_normpath(relPath)
        localImages[relPath] =  image = loadIcon(path)
        return image
    except Exception:
        pass

    return None
#@-node:getImage
#@+node:class OutlineCanvasPanel

class OutlineCanvasPanel(object):
    """A class to mimic a scrolled window to contain an OutlineCanvas."""

    #@    @+others
    #@+node:__init__

    def __init__(self, parent, leoTree, name):
        """Create an OutlineCanvasPanel instance."""

        #g.trace('OutlineCanvasPanel')

        #self._leoTree = leoTree
        #self.c = leoTree.c
        self.c = c

        self._x = 0
        self._y = 0

        self._canvas = canvas = OutlineCanvas(self)
        #canvas.resize(400, 300)

        self._table = gtk.Table(2,2)

        self._hscrollbar = gtk.HScrollbar()
        self._vscrollbar = gtk.VScrollbar()

        self._hadj = h = self._hscrollbar.get_adjustment()
        self._vadj = v = self._vscrollbar.get_adjustment()

        self._hscrollbar.set_range(0, 10)
        self._vscrollbar.set_range(0, 20)


        v.connect('value-changed', self.onScrollVertical)
        h.connect('value-changed', self.onScrollHorizontal)

        self._table.attach(self._hscrollbar, 0, 1, 1, 2, yoptions=0)
        self._table.attach(self._vscrollbar, 1, 2, 0, 1, xoptions=0)


        options = gtk.SHRINK | gtk.FILL | gtk.EXPAND
        self._table.attach(self._canvas, 0, 1, 0, 1, options, options)

        parent.add(self._table)

        self._canvas.set_events(
            gtk.gdk.POINTER_MOTION_MASK |
                    gtk.gdk.POINTER_MOTION_HINT_MASK
        )


        #self._entry = wx.TextCtrl(self._canvas,
        #    style = wx.SIMPLE_BORDER | wx.WANTS_CHARS
        #)

        #self._entry._virtualTop = -1000
        #self._entry.Hide()
        #self._canvas._widgets.append(self._entry)

        #self._canvas.update()


        # self.Bind(wx.EVT_SIZE, self.onSize)


        #self.SetBackgroundColour(self._leoTree.outline_pane_background_color)

        #self.Bind(wx.EVT_CHAR,
        #    lambda event, self=self._leoTree: onGlobalChar(self, event)
        #)

        #self.onScroll(wx.HORIZONTAL, 0)

    #@-node:__init__
    #@+node:showEntry
    showcount = 0
    def showEntry(self):

        # self.showcount +=1

        # print
        # g.trace(self.showcount, g.callers(20))
        # print

        entry = self._entry
        canvas = self._canvas

        ep = self._leoTree.editPosition()

        if not ep:
            return self.hideEntry()


        for sp in canvas._positions:
            if ep == sp:
                break
        else:
            return self.hideEntry()

        x, y, width, height = sp._textBoxRect
        #print '\t', x, y, width , height

        entry._virtualTop = canvas._virtualTop + y -2

        entry.MoveXY(x - 2, y -2)
        entry.SetSize((max(width + 4, 100), -1))

        tw = self._leoTree.headlineTextWidget

        range = tw.getSelectionRange()
        tw.setInsertPoint(0)
        #tw.setInsertPoint(len(sp.headString()))
        tw.setSelectionRange(*range)
        entry.Show()
    #@-node:showEntry
    #@+node:hideEntry

    def hideEntry(self):

        entry = self._entry
        entry._virtualTop = -1000
        entry.MoveXY(0, -1000)

        entry.Hide()
    #@-node:hideEntry
    #@+node:getPositions

    def getPositions(self):
        return self._canvas._positions
    #@nonl
    #@-node:getPositions
    #@+node:onScrollVertical
    def onScrollVertical(self, adjustment):
        """Scroll the outline vertically to a new position."""

        self._canvas.vscrollTo(int(adjustment.value))
    #@nonl
    #@-node:onScrollVertical
    #@+node:onScrollHorizontal
    def onScrollHorizontal(self, adjustment):
        """Scroll the outline horizontally to a new position.

        """
        self._canvas.hscrollTo(int(adjustment.value))
    #@-node:onScrollHorizontal
    #@+node:onScrollRelative

    def onScrollRelative(self, orient, value):

        return self.onScroll(orient, self.GetScrollPos(orient) + value)
    #@-node:onScrollRelative
    #@+node:vscrollUpdate

    def vscrollUpdate(self):
        """Set the vertical scroll bar to match current conditions."""

        canvas = self._canvas

        oldtop = top = canvas._virtualTop
        canvasHeight = canvas.get_allocation().height
        treeHeight = canvas._treeHeight

        if (treeHeight - top) < canvasHeight:
            top = treeHeight - canvasHeight

        if top < 0 :
            top = 0

        if oldtop != top:
            canvas._virtualTop = top
            canvas.redraw()
            top = canvas._virtualTop

        #self.showEntry()

        self._vadj.set_all(
            top, #value
            0, #lower
            treeHeight, #upper
            canvasHeight * 0.1, #step_increment
            canvasHeight * 0.9, #page_increment
            canvasHeight #page-size
        )


    #@-node:vscrollUpdate
    #@+node:hscrollUpdate

    def hscrollUpdate(self):
        """Set the vertical scroll bar to match current conditions."""

        canvas = self._canvas

        oldleft = left = canvas._virtualLeft
        canvasWidth = canvas.get_allocation().width
        treeWidth = canvas._treeWidth

        if (treeWidth - left) < canvasWidth:
            left = treeWidth - canvasWidth

        if left < 0 :
            left = 0

        if oldleft != left:
            canvas._virtualLeft = left
            canvas.redraw()
            left = canvas._virtualLeft

        #self.showEntry()

        self._hadj.set_all(
            left, #value
            0, #lower
            treeWidth, #upper
            canvasWidth * 0.1, #step_increment
            canvasWidth * 0.9, #page_increment
            canvasWidth #page-size
        )

    #@-node:hscrollUpdate
    #@+node:update

    def update(self):
        self._canvas.update()


    #@-node:update
    #@+node:redraw

    def redraw(self):
        self._canvas.redraw()
    #@nonl
    #@-node:redraw
    #@+node:refresh
    def refresh(self):
        self._canvas.refresh()
    #@nonl
    #@-node:refresh
    #@+node:GetName
    def GetName(self):
        return 'canvas'

    getName = GetName
    #@nonl
    #@-node:GetName
    #@-others
#@-node:class OutlineCanvasPanel
#@+node:class OutlineCanvas
class OutlineCanvas(gtk.DrawingArea):
    """Implements a virtual view of a leo outline tree.

    The class uses an off-screen buffer for drawing which it
    blits to the window during paint calls for expose events, etc,

    A redraw is only required when the size of the canvas changes,
    a scroll event occurs, or if the outline changes.

    """
    #@    @+others
    #@+node:__init__
    def __init__(self, parent):
        """Create an OutlineCanvas instance."""

        #g.trace('OutlineCanvas')

        self.c = parent.c

        self._parent = parent
        #self.leoTree = parent.leoTree

        self.c = c

        #@    << define ivars >>
        #@+node:<< define ivars >>
        #self._icons = icons

        self._widgets = []

        self.drag_p = None

        self._size =  [1000, 1000]

        self._virtualTop = 0
        self._virtualLeft = 0

        self._textIndent = 30

        self._xPad = 30
        self._yPad = 2

        self._treeHeight = 500
        self._treeWidth = 500

        self._positions = []

        self._fontHeight = None
        self._iconSize = [20, 11]

        self._clickBoxSize = None
        self._lineHeight =  10
        self._requestedLineHeight = 10

        self._yTextOffset = None
        self._yIconOffset = None

        self._clickBoxCenterOffset = None

        self._clickBoxOffset = None


        #@-node:<< define ivars >>
        #@nl

        gtk.DrawingArea.__init__(self)
        self._pangoLayout = self.create_pango_layout("")  

        self._buffer = None

        self.contextChanged()

        #self.Bind(wx.EVT_PAINT, self.onPaint)

        self.connect('map-event', self.onMap)


        #for o in (self, parent):
        #    
        #@nonl
        #@<< create  bindings >>
        #@+node:<< create bindings >>
        # onmouse = self._leoTree.onMouse

        # for e, s in (
           # ( wx.EVT_LEFT_DOWN,     'LeftDown'),
           # ( wx.EVT_LEFT_UP,       'LeftUp'),
           # ( wx.EVT_LEFT_DCLICK,   'LeftDoubleClick'),
           # ( wx.EVT_MIDDLE_DOWN,   'MiddleDown'),
           # ( wx.EVT_MIDDLE_UP,     'MiddleUp'),
           # ( wx.EVT_MIDDLE_DCLICK, 'MiddleDoubleClick'),
           # ( wx.EVT_RIGHT_DOWN,    'RightDown'),
           # ( wx.EVT_RIGHT_UP,      'RightUp'),
           # ( wx.EVT_RIGHT_DCLICK,  'RightDoubleClick'),
           # ( wx.EVT_MOTION,        'Motion')
        # ):
            # o.Bind(e, lambda event, type=s: onmouse(event, type))



        # #self.Bind(wx.EVT_KEY_UP, self._leoTree.onChar)
        # #self.Bind(wx.EVT_KEY_DOWN, lambda event: self._leoTree.onKeyDown(event))

        # self.Bind(wx.EVT_CHAR,
            # lambda event, self=self._leoTree: onGlobalChar(self, event)
        # )

        #@-node:<< create bindings >>
        #@nl

    #@+at
    # self.box_padding = 5 # extra padding between box and icon
    # self.box_width = 9 + self.box_padding
    # self.icon_width = 20
    # self.text_indent = 4 # extra padding between icon and tex
    # 
    # self.hline_y = 7 # Vertical offset of horizontal line
    # self.root_left = 7 + self.box_width
    # self.root_top = 2
    # 
    # self.default_line_height = 17 + 2 # default if can't set line_height 
    # from font.
    # self.line_height = self.default_line_height
    # 
    #@-at
    #@-node:__init__
    #@+node:hitTest
    def hitTest(self, x, y):
        result = self._hitTest(point)
        g.trace(result)
        return result

    def hitTest(self, xx, yy):

        for sp in self._positions:

            if yy < (sp._top + self._lineHeight):

                x, y, w, h = sp._clickBoxRect
                if xx > x  and xx < (x + w) and yy > y and yy < (y + h):
                    return sp, 'ClickBox'

                x, y, w, h = sp._iconBoxRect
                if xx > x  and xx < (x + w) and yy > y and yy < (y + h):
                    return sp, 'IconBox'

                x, y, w, h = sp._textBoxRect
                if xx > x  and xx < (x + w) and yy > y and yy < (y + h): 
                    return sp, 'TextBox'

                i = -1  
                for x, y, w, h in sp._headStringIcons:
                    i += 1
                    if xx > x  and xx < (x + w) and yy > y and yy <(y + h):
                       return sp, i

                return sp, 'Headline'

        return None, 'Canvas'

    #@-node:hitTest
    #@+node:_createNewBuffer
    def _createNewBuffer(self):
        """Create a new buffer for drawing."""


        if not self.window:
            g.trace('no window !!!!!!!!!!!!!!!!')
            g.trace(g.callers())
            return


        w, h = self.window.get_size()
        #g.trace(g.callers())


        if self._buffer:
            bw, bh = self._buffer.get_size()
            if bw >= w and bh >= h:
                return

        self._buffer = gtk.gdk.Pixmap(self.window, w, h)





    #@-node:_createNewBuffer
    #@+node:vscrollTo

    def vscrollTo(self, pos):
        """Scroll the canvas vertically to the specified position."""

        canvasHeight = self.get_allocation().height
        if (self._treeHeight - canvasHeight) < pos :
            pos = self._treeHeight - canvasHeight

        pos = max(0, pos)

        self._virtualTop = pos

        self.redraw()
    #@-node:vscrollTo
    #@+node:hscrollTo
    def hscrollTo(self, pos):
        """Scroll the canvas vertically to the specified position."""

        canvasWidth = self.get_allocation().width

        #g.trace(pos)

        if (self._treeWidth - canvasWidth) < pos :
            pos = min(0, self._treeWidth - canvasWidth)

        pos = max( 0, pos)

        self._virtualLeft = pos

        self.redraw()
    #@-node:hscrollTo
    #@+node:resize

    def resize(self):
        """Resize the outline canvas and, if required, create and draw on a new buffer."""

        c = self.c

        #c.beginUpdate()     #lock out events
        if 1: #try:

            self._createNewBuffer()

            #self._parent.hscrollUpdate()


            self.draw()
            self.refresh()


        #finally:
        #    c.endUpdate(False)


        return True





    #@-node:resize
    #@+node:redraw
    def redraw(self):
        self.draw()
        self.refresh()
    #@-node:redraw
    #@+node:update

    def update(self):
        """Do a full update assuming the tree has been changed."""

        c = self.c

        canvasHeight = self.get_allocation().height

        hoistFlag = bool(self.c.hoistStack)

        if hoistFlag:
            stk = [self.c.hoistStack[-1].p]
        else:
            stk = [self.c.rootPosition()]

        #@    << find height of tree and position of currentNode >>
        #@+node:<< find height of tree and position of currentNode >>

        # Find the number of visible nodes in the outline.

        cp = c.currentPosition().copy()
        cpCount = None

        count = 0
        while stk:

            p = stk.pop()

            while p:


                if stk or not hoistFlag:
                    newp = p.next()
                else:
                    newp = None

                if cp and cp == p:
                    cpCount = count
                    cp = False

                count += 1

                #@        << if p.isExpanded() and p.hasFirstChild():>>
                #@+node:<< if p.isExpanded() and p.hasFirstChild():>>
                ## if p.isExpanded() and p.hasFirstChild():

                v=p.v
                if v.statusBits & v.expandedBit and v.t._firstChild:
                #@nonl
                #@-node:<< if p.isExpanded() and p.hasFirstChild():>>
                #@nl
                    stk.append(newp)
                    p = p.firstChild()
                    continue

                p = newp

        lineHeight = self._lineHeight

        self._treeHeight = count * lineHeight
        g.trace( 'treeheight ', self._treeHeight)

        if cpCount is not None:
            cpTop = cpCount * lineHeight

            if cpTop < self._virtualTop:
                self._virtualTop = cpTop

            elif cpTop + lineHeight > self._virtualTop + canvasHeight:
                self._virtualTop += (cpTop + lineHeight) - (self._virtualTop + canvasHeight)



        #@-node:<< find height of tree and position of currentNode >>
        #@nl

        if (self._treeHeight - self._virtualTop) < canvasHeight:
            self._virtualTop = self._treeHeight - canvasHeight

        # if (self._treeHeight - self._virtualTop) < canvasHeight:
            # self._virtualTop = self._treeHeight - canvasHeight

        self.contextChanged()

        self.redraw()
        self._parent.vscrollUpdate()
        self._parent.hscrollUpdate()


    #@-node:update
    #@+node:onPaint

    def onPaint(self, *args):
        """Renders the off-screen buffer to the outline canvas."""

        # w, h are needed because the buffer may be bigger than the window.

        w, h = self.window.get_size()

        # We use self.style.black_gc only because we need a gc, it has no relavence.

        self.window.draw_drawable(self.style.black_gc ,self._buffer, 0, 0, 0, 0, w, h)
    #@-node:onPaint
    #@+node:onMap
    def onMap(self, *args):
        self._createNewBuffer()
        self.update()
        self.connect('expose-event', self.onPaint)
        self.connect("size-allocate", self.onSize)
    #@-node:onMap
    #@+node:onSize
    def onSize(self, *args):
        """React to changes in the size of the outlines display area."""


        c = self.c
        c.beginUpdate()
        try:
            self.resize()
            self._parent.vscrollUpdate()
            self._parent.hscrollUpdate()
        finally:
            c.endUpdate(False)


    #@-node:onSize
    #@+node:refresh

    #def refresh(self):
        # """Renders the offscreen buffer to the outline canvas."""
        # return

        # #print 'refresh'
        # wx.ClientDC(self).BlitPointSize((0,0), self._size, self._buffer, (0, 0))

    refresh = onPaint
    #@nonl
    #@-node:refresh
    #@+node:contextChanged
    def contextChanged(self):
        """Adjust canvas attributes after a change in context.

        This should be called after setting or changing fonts or icon size or
        anything that effects the tree display.

        """

        self._pangoLayout.set_text('Wy')
        self._fontHeight = self._pangoLayout.get_pixel_size()[1]
        self._iconSize = (20, 11) #(icons[0].GetWidth(), icons[0].GetHeight())

        self._clickBoxSize = (9, 9) #(plusBoxIcon.GetWidth(), plusBoxIcon.GetHeight())

        self._lineHeight = max(
            self._fontHeight,
            self._iconSize[1],
            self._requestedLineHeight
        ) + 2 * self._yPad

        # y offsets

        self._yTextOffset = (self._lineHeight - self._fontHeight)//2

        self._yIconOffset = (self._lineHeight - self._iconSize[1])//2

        self._clickBoxCenterOffset = (
            -self._textIndent*2 + self._iconSize[0]//2,
            self._lineHeight//2
        )

        self._clickBoxOffset = (
            self._clickBoxCenterOffset[0] - self._clickBoxSize[0]//2,
            (self._lineHeight  - self._clickBoxSize[1])//2
        )


    #@-node:contextChanged
    #@+node:requestLineHeight
    def requestLineHeight(height):
        """Request a minimum height for lines."""

        assert int(height) and height < 200
        self.requestedHeight = height
        self.beginUpdate()
        self.endUpdate()
    #@-node:requestLineHeight
    #@+node:def draw

    def draw(self, *args):
        """Draw the outline on the off-screen buffer."""

        r, g, b = colors.getColorRGB('leoyellow')
        r, g, b = r/255.0, g/255.0, b/255.0

        x, y, canvasWidth, canvasHeight = self.get_allocation()


        pangoLayout = self._pangoLayout   

        cr = self._buffer.cairo_create()


        cr.set_source_rgb(r, g, b)
        cr.rectangle(x, y, canvasWidth, canvasHeight)
        cr.fill()

        c = self.c


        top = self._virtualTop
        if top < 0:
            self._virtualTop = top = 0

        left = self._virtualLeft
        if left < 0:
            self._virtualLeft = left = 0   


        bottom = top + canvasHeight


        textIndent = self._textIndent
        treeWidth = self._treeWidth

        yPad = self._yPad
        xPad = self._xPad - left

        yIconOffset = self._yIconOffset

        yTextOffset = self._yTextOffset

        clickBoxOffset_x, clickBoxOffset_y = self._clickBoxOffset

        clickBoxCenterOffset_x, clickBoxCenterOffset_y = \
            self._clickBoxCenterOffset

        clickBoxSize_w, clickBoxSize_h = self._clickBoxSize

        iconSize_w, iconSize_h = self._iconSize

        lineHeight = self._lineHeight
        halfLineHeight = lineHeight//2

        #@    << draw tree >>
        #@+node:<< draw tree >>
        y = 0

        hoistFlag = bool(c.hoistStack)

        if hoistFlag:
            stk = [c.hoistStack[-1].p]
        else:
            stk = [c.rootPosition()]

        self._positions = positions = []

        #@+at
        # My original reason for writing the loop this way was to make it as 
        # fast as
        # possible. Perhaps I was being a bit too paranoid and we should 
        # change back to
        # more conventional iterations.
        #@-at
        #@@c


        while stk:

            p = stk.pop()

            while p:

                if stk or not hoistFlag:
                    newp = p.next()
                else:
                    newp = None

                mytop = y
                y = y + lineHeight

                if mytop > bottom:
                    stk = []
                    p = None
                    break

                if y > top:

                    sp = p.copy()

                    #@            << setup object >>
                    #@+node:<< set up object >>
                    # depth: the depth of indentation relative to the current hoist.
                    sp._depth = len(stk)

                    # virtualTop: top of the line in virtual canvas coordinates
                    sp._virtualTop =  mytop

                    # top: top of the line in real canvas coordinates
                    sp._top = mytop - top


                    pangoLayout.set_text(sp.headString())

                    textSize_w, textSize_h = pangoLayout.get_pixel_size()

                    xTextOffset = ((sp._depth +1) * textIndent) + xPad

                    textPos_x = xTextOffset # - self._hadj.value
                    textPos_y =  sp._top + yTextOffset

                    iconPos_x = textPos_x - textIndent
                    iconPos_y = textPos_y + yIconOffset

                    clickBoxPos_x = textPos_x + clickBoxOffset_x
                    clickBoxPos_y = textPos_y + clickBoxOffset_y

                    sp._clickBoxCenter_x = clickBoxPos_x + clickBoxCenterOffset_x
                    sp._clickBoxCenter_y = clickBoxPos_y + clickBoxCenterOffset_y

                    sp._textBoxRect = [textPos_x, textPos_y, textSize_w, textSize_h]
                    sp._iconBoxRect = [iconPos_x, iconPos_y, iconSize_w, iconSize_h]
                    sp._clickBoxRect = [clickBoxPos_x, clickBoxPos_y, clickBoxSize_w, clickBoxSize_h]

                    sp._icon = icons[p.v.computeIcon()]


                    if sp.hasFirstChild():
                        sp._clickBoxIcon = plusBoxIcon
                        if sp.isExpanded():
                            sp._clickBoxIcon = minusBoxIcon
                    else:
                        sp._clickBoxIcon = None

                    sp._clickRegions = []

                    #@-node:<< set up object >>
                    #@nl

                    positions.append(sp)

                    treeWidth = max(
                        treeWidth,
                        textSize_w + xTextOffset + left
                    )

                #@        << if p.isExpanded() and p.hasFirstChild():>>
                #@+node:<< if p.isExpanded() and p.hasFirstChild():>>
                ## if p.isExpanded() and p.hasFirstChild():

                v=p.v
                if v.statusBits & v.expandedBit and v.t._firstChild:
                #@nonl
                #@-node:<< if p.isExpanded() and p.hasFirstChild():>>
                #@nl
                    stk.append(newp)
                    p = p.firstChild()
                    continue

                p = newp

        if treeWidth > self._treeWidth:
            # theoretically this could be recursive
            # but its unlikely ...
            self._treeWidth = treeWidth
            self._parent.hscrollUpdate()

        if not positions:
            #g.trace('No positions!')
            return

        self._virtualTop =  positions[0]._virtualTop


        # try:
            # result = self._leoTree.drawTreeHook(self)
            # print 'result =', result
        # except:
            # result = False
            # print 'result is False'

        # if hasattr(self._leoTree, 'drawTreeHook'):
            # try:
                # result = self._leoTree.drawTreeHook(self)
            # except:
                # result = False
        # else:
            # #print 'drawTreeHook not known'
            # result = None

        # if not result:
        if 1:
            #@    << draw text >>
            #@+node:<< draw text >>

            current = c.currentPosition()



            for sp in positions:

                #@    << draw user icons >>
                #@+node:<< draw user icons >>


                try:
                    headStringIcons = sp.v.t.unknownAttributes.get('icons', [])
                except:
                    headStringIcons = None

                sp._headStringIcons = hsi = []

                if headStringIcons:

                    for headStringIcon in headStringIcons:
                        try:
                            image = globalImages[headStringIcon['relPath']]
                        except KeyError:
                            path = headStringIcon['relPath']
                            image = getImage(path)
                            if image is None:
                                return


                        x, y, w, h = sp._textBoxRect

                        hsi.append((x, y, image.get_width(), image.get_height()))       

                        cr.set_source_pixbuf(image, x, y)
                        cr.paint()

                        sp._textBoxRect[0] = x + image.get_width() + 5

                #@-node:<< draw user icons >>
                #@nl

                # if current and current == sp:
                    # dc.SetBrush(wx.LIGHT_GREY_BRUSH)
                    # dc.SetPen(wx.LIGHT_GREY_PEN)
                    # dc.DrawRectangleRect(
                        # wx.Rect(*sp._textBoxRect).Inflate(3, 3)
                    # )
                    # current = False
                    # #dc.SetBrush(wx.TRANSPARENT_BRUSH)
                    # #dc.SetPen(wx.BLACK_PEN)


                pangoLayout.set_text(sp.headString())
                x, y, w, h = sp._textBoxRect
                cr.set_source_rgb(0, 0, 0)
                cr.move_to(x, y)
                #cr.update_layout(pangoLayout)
                cr.show_layout(pangoLayout)


            #@-node:<< draw text >>
            #@nl
            #@    << draw lines >>
            #@+node:<< draw lines >>
            #@-node:<< draw lines >>
            #@nl
            #@    << draw bitmaps >>
            #@+node:<< draw bitmaps >>

            for sp in positions:

                x, y, w, h = sp._iconBoxRect

                cr.set_source_pixbuf(sp._icon,x,y)
                cr.paint()
                #cr.stroke()

                if sp._clickBoxIcon:
                    x, y, w, h = sp._clickBoxRect
                    cr.set_source_pixbuf(sp._clickBoxIcon, x, y)
                    cr.paint()

            #@+at
            #   ctx = da.window.cairo_create()
            #   # You can put ctx.scale(..) or ctx.rotate(..) here, if you 
            # need some
            #   ct = gtk.gdk.CairoContext(ctx)
            #   ct.set_source_pixbuf(pixbuf,0,0)
            #   ctx.paint()
            #   ctx.stroke()
            # 
            # 
            # 
            # 
            #@-at
            #@-node:<< draw bitmaps >>
            #@nl

            #@    << draw focus >>
            #@+node:<< draw focus >>
            if 0:
                dc.SetBrush(wx.TRANSPARENT_BRUSH)
                if self._leoTree.hasFocus():
                    dc.SetPen(wx.BLACK_PEN)
                #else:
                #    dc.SetPen(wx.GREEN_PEN)
                    dc.DrawRectanglePointSize( (0,0), self.GetSize())
            #@nonl
            #@-node:<< draw focus >>
            #@nl




        #@-node:<< draw tree >>
        #@nl

        #self._parent.showEntry()

        return True






    #@-node:def draw
    #@-others
#@-node:class OutlineCanvas
#@+node:== TREE WIDGETS ==
if 0:
    #@    @+others
    #@+node:wxLeoTree class (leoFrame.leoTree):
    class wxLeoTree (leoFrame.leoTree):
        #@    @+others
        #@+node:__init__
        def __init__ (self, c, parentFrame):


            self.c = c
            #self.frame = c.frame

            # Init the base class.
            #leoFrame.leoTree.__init__(self, self.frame)


            #@    << init config >>
            #@+node:<< init config >>
            # Configuration and debugging settings.
            # ?? These must be defined here to eliminate memory leaks. ??

            # c = self.c

            # self.allow_clone_drags          = c.config.getBool('allow_clone_drags')
            # self.center_selected_tree_node  = c.config.getBool('center_selected_tree_node')
            # self.enable_drag_messages       = c.config.getBool("enable_drag_messages")
            # self.expanded_click_area        = c.config.getBool('expanded_click_area')
            # self.gc_before_redraw           = c.config.getBool('gc_before_redraw')


            # for item, default in (
                # ('headline_text_editing_foreground_color', 'black'),
                # ('headline_text_editing_background_color', 'white'),
                # ('headline_text_editing_selection_foreground_color', None),
                # ('headline_text_editing_selection_background_color', None),
                # ('headline_text_selected_foreground_color', None),
                # ('headline_text_selected_background_color', None),
                # ('headline_text_editing_selection_foreground_color', None),
                # ('headline_text_editing_selection_background_color', None),
                # ('headline_text_unselected_foreground_color', None),
                # ('headline_text_unselected_background_color', None),
                # ('outline_pane_background_color', 'leo yellow')
            # ):
                # setattr(self, item, name2color(c.config.getColor(item), default))

            # self.idle_redraw = c.config.getBool('idle_redraw')

            # self.initialClickExpandsOrContractsNode = c.config.getBool(
                # 'initialClickExpandsOrContractsNode')
            # self.look_for_control_drag_on_mouse_down = c.config.getBool(
                # 'look_for_control_drag_on_mouse_down')
            # self.select_all_text_when_editing_headlines = c.config.getBool(
                # 'select_all_text_when_editing_headlines')

            # self.stayInTree     = c.config.getBool('stayInTreeAfterSelect')
            # self.trace          = c.config.getBool('trace_tree')
            # self.trace_alloc    = c.config.getBool('trace_tree_alloc')
            # self.trace_chapters = c.config.getBool('trace_chapters')
            # self.trace_edit     = c.config.getBool('trace_tree_edit')
            # self.trace_gc       = c.config.getBool('trace_tree_gc')
            # self.trace_redraw   = c.config.getBool('trace_tree_redraw')
            # self.trace_select   = c.config.getBool('trace_select')
            # self.trace_stats    = c.config.getBool('show_tree_stats')
            # self.use_chapters   = c.config.getBool('use_chapters')
            #@-node:<< init config >>
            #@nl

            #g.trace('tree', frame)


            # A dummy ivar used in c.treeWantsFocus, etc.
            self.canvas = self

            # A lockout that prevents event handlers from firing during redraws.
            self.drawing = False

            #self.effects = wx.Effects()

            self.keyDownModifiers = None

            self.updateCount = 0

            self.treeCtrl = None
            self.treeCtrl = self.createControl(parentFrame)

            self.drag_p = None
            self.dragging = None
            self.controlDrag = None







        #@+node:createBindings

        def createBindings (self): # wxLeoTree
            pass

        #@-node:createBindings
        #@+node:createControl

        def createControl (self, parentFrame):
            """Create an OutlineCanvasPanel."""

            treeCtrl = OutlineCanvasPanel(
                parentFrame,
                leoTree=self,
                name='tree'
            )

            entry = treeCtrl._entry
            self.headlineTextWidget = hw = headlineTextWidget(self, widget=entry)


            entry.Bind(wx.EVT_KILL_FOCUS, self.entryLostFocus)
            entry.Bind(wx.EVT_SET_FOCUS, self.entryGotFocus)

            treeCtrl.Bind(wx.EVT_KILL_FOCUS, self.treeLostFocus)
            treeCtrl.Bind(wx.EVT_SET_FOCUS, self.treeGotFocus)


            return treeCtrl
        #@-node:createControl
        #@+node:setBindings
        def setBindings(self):

            pass # g.trace('wxLeoTree: to do')

        def bind(self,*args,**keys):

            pass # g.trace('wxLeoTree',args,keys)
        #@nonl
        #@-node:setBindings
        #@-node:__init__
        #@+node:__str__ & __repr__

        def __repr__ (self):

            return "Tree %d" % id(self)

        __str__ = __repr__

        #@-node:__str__ & __repr__
        #@+node:edit_widget

        def edit_widget(self, p=None):
            """Return the headlineTextWidget."""

            return self.headlineTextWidget
        #@-node:edit_widget
        #@+node:Focus Gain/Lose

        def entryLostFocus(self, event):
            self.endEditLabel(event)

        def entryGotFocus(self, event):
            pass

        def treeGotFocus(self, event):
            #g.trace()
            if self.treeCtrl:
                self.treeCtrl.redraw()
            self.c.focusManager.gotFocus(self, event)

        def treeLostFocus(self, event):
            #g.trace()
            if self.treeCtrl:
                self.treeCtrl.redraw()
            self.c.focusManager.lostFocus(self, event)
            #g.trace()

        def hasFocus(self):
            if not self.treeCtrl:
                return None
            fw = wx.Window.FindFocus()
            return fw is self.treeCtrl #or fw is self.treeCtrl._canvas
        #@-node:Focus Gain/Lose
        #@+node:SetFocus
        def setFocus(self):

            if not self.treeCtrl or g.app.killed or self.c.frame.killed: return

            self.treeCtrl.SetFocus()

        SetFocus = setFocus

        #@-node:SetFocus
        #@+node:getCanvas
        def getCanvas(self):
            return self.treeCtrl._canvas
        #@nonl
        #@-node:getCanvas
        #@+node:getCanvasHeight
        def getCanvasHeight(self):
            x, y, w, h = self
            print '++++++', self.treeCtrl._canvas._size.height
            return self.treeCtrl._canvas._size.height

        #@-node:getCanvasHeight
        #@+node:getLineHeight
        #@-node:getLineHeight
        #@+node:onScrollRelative
        def onScrollRelative(self, orient, value):
            self.treeCtrl.onScrollRelative(orient, value)
        #@nonl
        #@-node:onScrollRelative
        #@+node:HasCapture / Capture / Release Mouse
        def HasCapture(self):
            return self.getCanvas().HasCapture()

        def CaptureMouse(self):
            return self.getCanvas().CaptureMouse()

        def ReleaseMouse(self):
            return self.getCanvas().ReleaseMouse()
        #@-node:HasCapture / Capture / Release Mouse
        #@+node:setCursor
        def setCursor(self, cursor):
            if cursor == 'drag':
                self.getCanvas().SetCursor(wx.StockCursor(wx.CURSOR_HAND))
            else:
                self.getCanvas().SetCursor(wx.StockCursor(wx.CURSOR_ARROW))

        #@-node:setCursor
        #@+node:idle_redraw
        def idle_redraw(*args, **kw):
            return
        #@nonl
        #@-node:idle_redraw
        #@+node:Drawing
        #@+node:beginUpdate
        def beginUpdate(self):

            self.updateCount += 1
        #@-node:beginUpdate
        #@+node:endUpdate
        def endUpdate(self, flag=True, scroll=False):

            assert(self.updateCount > 0)

            self.updateCount -= 1
            if flag and self.updateCount <= 0:
                self.redraw()

                if self.updateCount < 0:
                    g.trace("Can't happen: negative updateCount", g.callers())



        #@-node:endUpdate
        #@+node:redraw & redraw_now & helpers
        redrawCount = 0

        def redraw (self, scroll=True):

            c = self.c ;
            cc = c.chapterController
            tree = self.treeCtrl

            if c is None or self.drawing:
                return

            #self.redrawCount += 1
            #if not g.app.unitTesting: g.trace(self.redrawCount,g.callers())

            self.drawing = True # Disable event handlers.

            if cc and cc.chapterSelector:
                cc.chapterSelector.update()

            try:
                self.expandAllAncestors(c.currentPosition())
                tree.update()
                self.scrollTo()
            finally:
                self.drawing = False # Enable event handlers.

            #if not g.app.unitTesting: g.trace('done')

        redraw_now = redraw
        #@-node:redraw & redraw_now & helpers
        #@+node:scrollTo
        def scrollTo(self,p=None):
            """Scrolls the canvas so that p is in view.

            Assumes that the canvas is in a valid state.
            """

            __pychecker__ = '--no-argsused' # event not used.
            __pychecker__ = '--no-intdivide' # suppress warning about integer division.

            c = self.c
            tree = self.treeCtrl

            if not p or not c.positionExists(p):
                p = c.currentPosition()

            if not p or not c.positionExists(p):
                # g.trace('current p does not exist',p)
                p = c.rootPosition()

            if not p or not c.positionExists(p):
                # g.trace('no position')
                return

            target_p = p

            positions = tree.getPositions()

            #@    << virtual top for target >>
            #@+node:<< virtual top for target >>

            #
            # Find the virtual top for node.
            #

            hoistFlag = bool(c.hoistStack)

            if hoistFlag:
                stk = [c.hoistStack[-1].p]
            else:
                stk = [c.rootPosition()]
            #g.trace('====================')
            count = 0
            while stk:

                p = stk.pop()

                while p:

                    if p == target_p:
                        stk = None
                        p = None
                        break

                    #g.trace('count', p)
                    if stk or not hoistFlag:
                        newp = p.next()
                    else:
                        newp = None

                    count += 1

                    if p.isExpanded() and p.hasFirstChild():
                        stk.append(newp)
                        p = p.firstChild()
                        continue

                    p = newp

            targetTop = count * tree._canvas._lineHeight
            #g.trace(targetTop, count)
            #@nonl
            #@-node:<< virtual top for target >>
            #@nl

            if 1 and self.center_selected_tree_node:
                newtop = targetTop - (self.treeCtrl.GetClientSize().height)//2
                if newtop < 0:
                    newtop = 0

                #tree.onScroll(wx.VERTICAL, newtop)
                #g.trace(newtop, targetTop, self.treeCtrl.GetClientSize())
            else:
                assert False, 'FIXME - tree.ScrollTo'

        idle_scrollTo = scrollTo # For compatibility.
        #@-node:scrollTo
        #@-node:Drawing
        #@+node:== Event handlers ==
        #@+node:def onChar
        def onChar(self, event, keycode, keysym):
            pass
        #@nonl
        #@-node:def onChar
        #@+node:onHeadlineKey

        # k.handleDefaultChar calls onHeadlineKey.
        def onHeadlineKey (self, event):

            #g.trace(event)

            if g.app.killed or self.c.frame.killed:
                return

            if event and event.keysym:
                self.updateHead(event, event.widget)
        #@-node:onHeadlineKey
        #@+node:Drag
        #@+node:startDrag
        def startDrag(self, p, event):

            c = self.c
            c.setLog()

            if not p:
                return
            #g.trace()


            self.startDragPoint = self.dragPoint = event.GetPosition()

            self.drag_p = p # don't copy as p is enhanced

            self.dragging = True

            #g.trace("\n\t*** start drag ***", self.drag_p.headString())

            #print '\tself.controlDrag', self.controlDrag

            if self.allow_clone_drags:
                self.controlDrag = c.frame.controlKeyIsDown
                if self.look_for_control_drag_on_mouse_down:
                    if self.enable_drag_messages:
                        if self.controlDrag:
                            g.es("dragged node will be cloned")
                        else:
                            g.es("dragged node will be moved")
            else:
                 self.controlDrag = False

            self.setCursor('drag')
        #@-node:startDrag
        #@+node:onDrag
        def onDrag(self, p, event):

            #print 'onDrag',

            c = self.c

            if not p:
                p = self.drag_p

            c.setLog()

            if not self.dragging:
                if not g.doHook("drag1",c=c,p=p,v=p,event=event):
                    self.startDrag(p, event)
                g.doHook("drag2",c=c,p=p,v=p,event=event)

            if not g.doHook("dragging1",c=c,p=p,v=p,event=event):
                self.continueDrag(p, event)
            g.doHook("dragging2",c=c,p=p,v=p,event=event)
        #@-node:onDrag
        #@+node:onEndDrag
        def onEndDrag(self, drop_p, event):

            """Tree end-of-drag handler."""

            c = self.c ; p = self.drag_p
            if not (drop_p and self.drag_p):
                self.cancelDrag()

            c.setLog()

            if not g.doHook("enddrag1",c=c,p=p,v=p,event=event):
                self.endDrag(drop_p, event)
            g.doHook("enddrag2",c=c,p=p,v=p,event=event)
        #@+node:endDrag
        def endDrag (self, drop_p, event):

            """The official helper of the onEndDrag event handler."""

            c = self.c
            c.setLog()

            #g.trace()

            p = self.drag_p

            if not event:
                return

            c.beginUpdate()
            redrawFlag = False
            try:

                #@        << set drop_p, childFlag >>
                #@+node:<< set drop_p, childFlag >>



                childFlag = drop_p and drop_p.hasChildren() and drop_p.isExpanded()
                #@-node:<< set drop_p, childFlag >>
                #@nl
                if self.allow_clone_drags:
                    if not self.look_for_control_drag_on_mouse_down:
                        self.controlDrag = c.frame.controlKeyIsDown

                redrawFlag = drop_p and drop_p.v.t != p.v.t
                if redrawFlag: # Disallow drag to joined node.
                    #@            << drag p to drop_p >>
                    #@+node:<< drag p to drop_p>>
                    #g.trace('\n')
                    #print '\tsource:', p.headString()
                    #print '\ttarget:', drop_p.headString()

                    if self.controlDrag: # Clone p and move the clone.
                        if childFlag:
                            c.dragCloneToNthChildOf(p, drop_p, 0)
                        else:
                            c.dragCloneAfter(p, drop_p)
                    else: # Just drag p.
                        if childFlag:
                            c.dragToNthChildOf(p, drop_p, 0)
                        else:
                            c.dragAfter(p,drop_p)
                    #@-node:<< drag p to drop_p>>
                    #@nl
                elif self.trace and self.verbose:
                    g.trace("Cancel drag")

                # Reset the old cursor by brute force.
                self.setCursor('default')
                self.dragging = False
                self.drag_p = None
            finally:
                # Must set self.drag_p = None first.
                c.endUpdate(redrawFlag)
                c.recolor_now() # Dragging can affect coloring.
        #@-node:endDrag
        #@-node:onEndDrag
        #@+node:cancelDrag
        def cancelDrag(self, p, event):

            #g.trace()

            if self.trace and self.verbose:
                g.trace("Cancel drag")

            # Reset the old cursor by brute force.
            self.setCursor('default')
            self.dragging = False
            self.drag_p = None
        #@-node:cancelDrag
        #@+node:continueDrag
        def continueDrag(self, p, event):

            #g.trace()

            p = self.drag_p
            if not p:
                return

            try:
                point = event.GetPosition()
                if self.dragging: # This gets cleared by onEndDrag()
                    self.dragPoint = point
                    #print 'ContiueDrag',
                    #@            << scroll the canvas as needed >>
                    #@+node:<< scroll the canvas as needed >>

                    # Scroll the screen.

                    # TODO: This is rough, scrolling needs to be much smoother
                    # TODO: Use a timer instead of mouse motion

                    canvas = self.getCanvas()

                    treeHeight = canvas._treeHeight
                    treeWidth = canvas._treeWidth

                    top = canvas._virtualTop
                    treeLeft = cavas._virtualLeft

                    width, height = canvas._size

                    pos = point.y
                    vpos = pos + top


                    updelta = max(1, vpos/treeHeight)
                    downdelta = max(1, (treeHeight - vpos)/treeHeight)

                    cx = canvas.GetPosition().x


                    diff = downdelta = updelta = 1
                    if pos < 10:
                        diff = (10 - pos)*5
                        self.onScrollRelative(wx.VERTICAL, -min(updelta*diff, 5000) )

                    elif pos > height - 10:
                        diff = (height - 10 - pos)*5
                        self.onScrollRelative(wx.VERTICAL, -min(downdelta*diff, 5000) )

                    if point.x + cx < 10:
                        self.onScrollRelative(wx.HORIZONTAL, -10)

                    elif point.x + cx > self.treeCtrl.GetClientSize().width:
                        self.onScrollRelative(wx.HORIZONTAL, 10)

                    #g.trace(updelta*diff, downdelta*diff, diff)
                    #@-node:<< scroll the canvas as needed >>
                    #@nl
            except:
                g.es_event_exception("continue drag")
        #@-node:continueDrag
        #@-node:Drag
        #@+node:Mouse Events
        """
        All mouse events are collected by the treeCtrl and sent
        to a dispatcher (onMouse).

        onMouse is called with dispatcher is called with a position,

        a 'source' which is the name of an region inside the headline
            this could be 'ClickBox', 'IconBox', 'TextBox' or a user supplied



        """


        #@+node:onMouse (Dispatcher)
        def onMouse(self, event, type):
            '''
            Respond to mouse events and call appropriate handlers.

            'event' is the raw 'event' object from the original event.

            'type' is a string representing the type of event and may
            have one of the following values:

                + LeftDown, LeftUp, LeftDoubleClick
                + MiddleDown, MiddleUp, MiddleDoubleClick
                + RightDown, RightUp, RightDoubleClick
                + and Motion

            'source' is a string derived from 'event' which represents
            the position of the event in the headline and may have one
            of the following values:

                ClickBox, IconBox, TextBox, Headline.

            'source' may also have a user defined value representing,
            for example, a user defined icon.

            'sp' is leo position object, derived from event via HitTest,
            representing the node on which the event occured. It is
            called sp rather than the usual 'p' because it is 'special',
            in that it contains extra information.

            The value of 'source' and 'type' are combined and the
            following three methods are called in order for each event:

                + onPreMouse{type}(sp, event, source, type)
                + onMouse{source}{type}(sp, event, source, type)
                + onPostMouse{type}(sp, event, source, type)

            None of these methods need exist and are obviously not called
            if they don't.

            The 'source' value is always an empty string for
            Motion events.

            Note to self: Refrain from taking drugs while proramming.
            '''

            point = event.GetPosition()

            sp, source = self.hitTest(point)

            #g.trace(self, type, source, sp)

            if False and type != 'Motion':
                #@        << trace mouse >>
                #@+node:<< trace mouse >>
                g.trace('\n\tsource:', source)
                print '\ttype:', type
                print '\theadline', sp and sp.headString()
                print

                s = 'onPreMouse' + type
                print '\t', s
                if hasattr(self, s):
                    getattr(self, s)(sp, event, source, type)

                s = 'onMouse' + source + type
                print '\t', s
                if hasattr(self, s):
                    getattr(self, s)(sp, event, source, type)

                s = 'onPostMouse' + type
                print '\t', s
                if hasattr(self, s):
                    getattr(self, s)(sp, event, source, type)

                #@-node:<< trace mouse >>
                #@nl
            else:

                s = 'onPreMouse' + type
                if hasattr(self, s):
                    getattr(self, s)(sp, event, source, type)

                if type == 'Motion':
                    s='onMouseMotion'
                    if hasattr(self, s):
                        getattr(self, s)(sp, event, source, type)
                else:
                    s = 'onMouse' + source + type
                    if hasattr(self, s):
                        #print 'ok for ', source, type
                        getattr(self, s)(sp, event, source, type)
                    else:
                        #print 'fail for ', source, type
                        pass
                s = 'onPostMouse' + type
                if hasattr(self, s):
                    getattr(self, s)(sp, event, source, type)

        #@-node:onMouse (Dispatcher)
        #@+node:HitTest
        def hitTest(self, point):
            return self.treeCtrl._canvas.hitTest(point)



        #@-node:HitTest
        #@+node:Pre
        #@+node:onPreMouseLeftDown
        def onPreMouseLeftDown(self, sp, event, source, type):
            #g.trace('source:', source, 'type:', type, 'Position:', sp and sp.headString())

            self.setFocus()
        #@-node:onPreMouseLeftDown
        #@+node:onPreMouseLeftUp
        #@+at
        # def onPreMouseLeftUp(self, sp, event, source, type):
        #     g.trace('source:', source, 'type:', type, 'Position:', sp and
        # sp.headString())
        #@-at
        #@-node:onPreMouseLeftUp
        #@+node:onPreMouseRightDown
        #@+at
        # def onPreMouseRightDown(self, sp, event, source, type):
        #     g.trace('source:', source, 'type:', type, 'Position:', sp and
        # sp.headString())
        #@-at
        #@-node:onPreMouseRightDown
        #@+node:onPreMouseRightUp
        #@+at
        # def onPreMouseRightUp(self, sp, event, source, type):
        #     g.trace('source:', source, 'type:', type, 'Position:', sp and
        # sp.headString())
        #@-at
        #@-node:onPreMouseRightUp
        #@+node:onPreMouseMotion
        #@-node:onPreMouseMotion
        #@-node:Pre
        #@+node:Post
        #@+node:onPostMouseLeftDown
        #@+at
        # def onPostMouseLeftDown(self, sp, event, source, type):
        #     g.trace('source:', source, 'type:', type, 'Position:', sp and
        # sp.headString())
        #@-at
        #@-node:onPostMouseLeftDown
        #@+node:onPostMouseLeftUp
        def onPostMouseLeftUp(self, sp, event, source, type):
            #g.trace('source:', source, 'type:', type, 'Position:', sp and sp.headString())

            self.setCursor('default')
            if self.HasCapture():
                self.ReleaseMouse()

            #If we are still dragging here something as gone wrong.
            if self.dragging:
                self.cancelDrag(sp, event)
        #@-node:onPostMouseLeftUp
        #@+node:onPostMouseRightDown
        #@+at
        # def onPostMouseRightDown(self, sp, event, source, type):
        #     g.trace('source:', source, 'type:', type, 'Position:', sp and
        # sp.headString())
        # 
        #@-at
        #@-node:onPostMouseRightDown
        #@+node:onPostMouseRightUp
        #@+at
        # def onPostMouseRightUp(self, sp, event, source, type):
        #     g.trace('source:', source, 'type:', type, 'Position:', sp and
        # sp.headString())
        # 
        #@-at
        #@-node:onPostMouseRightUp
        #@+node:onPostMouseMotion
        #@-node:onPostMouseMotion
        #@-node:Post
        #@+node:Motion
        def onMouseMotion(self, p, event, source, type):
            if self.dragging:
                self.onDrag(p, event)
        #@-node:Motion
        #@+node:Click Box
        #@+node:onMouseClickBoxLeftDown
        def onMouseClickBoxLeftDown (self, p, event, source, type):
            """React to leftMouseDown event on ClickBox.

            Toggles expanded status for this node.

            """

            c = self.c

            p1 = c.currentPosition()
            #g.trace(source, type, p)
            c.beginUpdate()
            try:
                if not g.doHook("boxclick1", c=c, p=p, v=p, event=event):

                    self.endEditLabel()

                    if p == p1 or self.initialClickExpandsOrContractsNode:
                        if p.isExpanded():
                            p.contract()
                        else:
                            p.expand()

                    self.select(p)

                    if c.frame.findPanel:
                        c.frame.findPanel.handleUserClick(p)
                    if self.stayInTree:
                        c.treeWantsFocus()
                    else:
                        c.bodyWantsFocus()

                g.doHook("boxclick2", c=c, p=p, v=p, event=event)

            finally:
                c.endUpdate()


        #@-node:onMouseClickBoxLeftDown
        #@-node:Click Box
        #@+node:Icon Box...
        #@+node:onMouseIconBoxLeftDown
        def onMouseIconBoxLeftDown(self, p, event, source , type):
            """React to leftMouseDown event on the icon box."""

            #g.trace(source, type)
            c = self.c
            c.setLog()

            if not self.HasCapture():
                self.CaptureMouse()

            c.beginUpdate()
            try:
                if not g.doHook("iconclick1", c=c, p=p, v=p, event=event):

                    self.endEditLabel()
                    self.onDrag(p, event)

                    self.select(p)

                    if c.frame.findPanel:
                        c.frame.findPanel.handleUserClick(p)
                    if self.stayInTree:
                        c.treeWantsFocus()
                    else:
                        c.bodyWantsFocus()

                g.doHook("iconclick2", c=c, p=p, v=p, event=event)

            finally:
                c.endUpdate()

        #@-node:onMouseIconBoxLeftDown
        #@+node:onMouseIconBoxLeftUp

        def onMouseIconBoxLeftUp(self, sp, event, source, type):
            #g.trace('\n\tDrop:', self.drag_p, '\n\tOn:', sp and sp.headString())

            if self.dragging:
                self.onEndDrag(sp, event)
        #@nonl
        #@-node:onMouseIconBoxLeftUp
        #@+node:onMouseIconBoxLeftDoubleClick
        def onMouseIconBoxLeftDoubleClick(self, sp, event, source, type):

            c = self.c

            assert sp

            #g.trace()

            if self.trace and self.verbose: g.trace()

            try:
                if not g.doHook("icondclick1",c=c,p=sp,v=sp,event=event):
                    self.endEditLabel() # Bug fix: 11/30/05
                    self.OnIconDoubleClick(sp) # Call the method in the base class.
                g.doHook("icondclick2",c=c,p=sp,v=sp,event=event)
            except:
                g.es_event_exception("icondclick")
        #@-node:onMouseIconBoxLeftDoubleClick
        #@-node:Icon Box...
        #@+node:Text Box
        #@+node:onMouseTextBoxLeftDown

        def onMouseTextBoxLeftDown(self, p, event, source, type):
            """React to leftMouseDown event on the label of a headline."""

            c = self.c
            c.setLog()

            c.beginUpdate()
            try:
                if c.isCurrentPosition(p):

                    self.editLabel(p)

                else:
                    if not g.doHook("headclick1",c=c,p=p,v=p,event=event):

                        self.endEditLabel()
                        self.select(p)

                        if c.frame.findPanel:
                            c.frame.findPanel.handleUserClick(p)

                        if self.stayInTree:
                            c.treeWantsFocus()
                        else:
                            c.bodyWantsFocus()
                    g.doHook("headclick2",c=c,p=p,v=p,event=event)
            finally:
                c.endUpdate()

        #@-node:onMouseTextBoxLeftDown
        #@-node:Text Box
        #@+node:Headline
        #@+node:onMouseHeadlineLeftDown

        def onMouseHeadlineLeftDown(self, sp, event, source, type):
            """React to leftMouseDown event outside of main headline regions."""

            #g.trace('FIXME')
            if not self.expanded_click_area:

                return
            self.onMouseClickBoxLeftDown(sp, event, source, type)
        #@-node:onMouseHeadlineLeftDown
        #@-node:Headline
        #@-node:Mouse Events
        #@-node:== Event handlers ==
        #@+node:editLabel
        def editLabel (self,p,selectAll=False):
            '''The edit-label command.'''

            #g.trace(g.callers())

            if g.app.killed or self.c.frame.killed: return

            c = self.c

            entry = self.headlineTextWidget

            if p:

                c.beginUpdate()
                try:
                    self.endEditLabel()
                    self.setEditPosition(p)
                    #g.trace('ep', self.editPosition())
                finally:
                    c.endUpdate()

                # Help for undo.
                self.revertHeadline = s = p.headString()

                self.setEditLabelState(p)

                entry.setAllText(s)

                selectAll = selectAll or self.select_all_text_when_editing_headlines
                if selectAll:
                    entry.ctrl.SetSelection(-1, -1)
                else:
                    entry.ctrl.SetInsertionPointEnd()
                entry.ctrl.SetFocus()
                c.headlineWantsFocus(p)
        #@-node:editLabel
        #@+node:endEditLabel
        def endEditLabel (self, event=None):
            '''End editing of a headline and update p.headString().'''

            c = self.c

            if event:
                #g.trace('kill focus')
                pass

            if g.app.killed or c.frame.killed:
                return

            w = self.headlineTextWidget

            ep = self.editPosition()
            if not ep:
                return

            s = w.getAllText()

            h = ep.headString()

            #g.trace('old:',h,'new:',s)

            # Don't clear the headline by default.
            if s and s != h:
                self.onHeadChanged(ep,undoType='Typing',s=s)

            self.setEditPosition(None)
            c.beginUpdate()
            c.endUpdate()

            if c.config.getBool('stayInTreeAfterEditHeadline'):
                c.treeWantsFocusNow()
            else:
                c.bodyWantsFocusNow()

            if event:
                event.Skip()
        #@-node:endEditLabel
        #@+node:tree.setHeadline (new in 4.4b2)
        def setHeadline (self,p,s):

            '''Set the actual text of the headline widget.

            This is called from the undo/redo logic to change the text before redrawing.'''

            w = self.editPosition() and self.headlineTextWidget

            w = self.edit_widget(p)
            if w:
                w.setAllText(s)
                self.revertHeadline = s
            elif g.app.killed or self.c.frame.killed:
                return
            else:
                g.trace('#'*20,'oops')
        #@-node:tree.setHeadline (new in 4.4b2)
        #@+node:tree.set...LabelState
        #@+node:setEditLabelState
        def setEditLabelState(self, p, selectAll=False):

            #g.trace()
            pass

        #@-node:setEditLabelState
        #@+node:setSelectedLabelState

        def setSelectedLabelState(self, p):

            # g.trace(p, g.callers())

            if p:
                p.setSelected()

        #@-node:setSelectedLabelState
        #@+node:setUnselectedLabelState

        def setUnselectedLabelState(self,p): # not selected.

            # g.trace(p, g.callers())

            if p:
                # clear 'selected' status flag
                p.v.statusBits &= ~ p.v.selectedBit

        #@-node:setUnselectedLabelState
        #@-node:tree.set...LabelState
        #@+node:do nothings
        def headWidth (self,p=None,s=''): return 0

        # Colors.
        def setDisabledHeadlineColors (self,p):             pass
        def setEditHeadlineColors (self,p):                 pass
        def setUnselectedHeadlineColors (self,p):           pass


        # Focus
        def focus_get (self):
            return self.FindFocus()

        def setFocus (self):
            self.treeCtrl.SetFocusIgnoringChildren()

        SetFocus = setFocus


        #@-node:do nothings
        #@+node:GetName
        def GetName(self):
            return 'canvas'

        getName = GetName
        #@-node:GetName
        #@+node:Reparent
        def reparent(self, parent):
            self.treeCtrl.Reparent(parent)

        Reparent = reparent
        #@-node:Reparent
        #@+node:Font Property
        def getFont(self):
            g.trace('not ready')

        def setFont(self):
            g.trace('not ready')

        font = property(getFont, setFont)



        #@-node:Font Property
        #@+node:requestLineHeight
        def requestLineHeight(height):
            self.getCanvas().requestLineHeight(height)
        #@nonl
        #@-node:requestLineHeight
        #@+node:line_height property
        def getLineHeight(self):
            return self.treeCtrl._canvas._lineHeight

        line_height = property(getLineHeight)
        #@nonl
        #@-node:line_height property
        #@-others
    #@nonl
    #@-node:wxLeoTree class (leoFrame.leoTree):
    #@-others
#@nonl
#@-node:== TREE WIDGETS ==
#@-others

def abspath(*args):
    return os.path.abspath(os.path.join(*args))



if __name__ == "__main__": 

    leoDir = abspath(sys.path[0],'..')

    sys.path.insert(0, abspath(leoDir, 'src'))

    import leoBridge

    controller = leoBridge.controller(gui='nullGui')
    g = controller.globals()
    c = controller.openLeoFile(abspath(leoDir, 'test', 'unitTest.leo'))

    colors = g.importExtension('colors')

    GtkLeoTreeDemo()

    gtk.main()


#@-node:@file /home/bob/work/leo/workleo/test/gtkOutlineTest.py
#@-leo
