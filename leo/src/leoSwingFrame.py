# -*- coding: utf-8 -*-
#@+leo-ver=4-thin
#@+node:ekr.20070930105125:@thin leoSwingFrame.py
#@@first

#@@language python
#@@tabwidth -4
#@@pagewidth 80

#@<< imports >>
#@+node:ekr.20070930105601.1:<< imports >>
import leoGlobals as g

import leoChapters
import leoColor
import leoFrame
import leoKeys
import leoMenu
import leoNodes

import javax.swing as swing
import java.awt as awt
import java.lang

# import leoTkinterMenu
# import leoTkinterTree
# import Tkinter as Tk
# import tkFont

import os
import string
import sys

# # The following imports _are_ used.
# __pychecker__ = '--no-import'
# import threading
# import time
#@-node:ekr.20070930105601.1:<< imports >>
#@nl

#@+others
#@+node:ekr.20070930105601.2:class leoSwingFrame
class leoSwingFrame (leoFrame.leoFrame):

    def __init__ (self,title,gui):

        # g.trace('leoSwingFrame',title,gui)
        self.title = title
        self.gui = gui
        self.iconBarClass = leoFrame.nullIconBarClass ###
        self.miniBufferWidget = None # Created below.

    def finishCreate (self,c):

        # g.trace('leoSwingFrame',c)

        # Official ivars.
        self.c = c
        self.ratio = 0.5
        self.secondary_ratio = 0.5

        # Frame components...
        self.body = leoSwingBody(frame=self,parentFrame=None)

        ### Dummy components...
        self.outerFrame = self.createOuterFrame()
        self.iconBar = None
        self.log  = leoFrame.nullLog(frame=self,parentFrame=None)
        self.menu = leoMenu.nullMenu(frame=self)
        self.miniBufferWidget = leoFrame.stringTextWidget(c,'minibuffer')
        self.statusLine = leoFrame.nullStatusLineClass(c,parentFrame=self)
        self.tree = leoFrame.nullTree(frame=self)

    #@    @+others
    #@+node:ekr.20070930122327:createOuterFrame
    def createOuterFrame (self):

        # The first script in Jython Essentials, by Pedroni & Rappin.

        def exit(event):
            java.lang.System.exit(0)

        def onButtonPressed(event):
            field.text=quotes[event.source.text]

        def createButton(name):
            return swing.JButton(name,preferredSize=(100,20),
                actionPerformed=onButtonPressed)

        names = [ 'Groucho','Chico','Harpo']
        quotes = {'Groucho':'Say the secret word','Chico':'Viaduct?','Harpo':'Honk!'}

        w = swing.JFrame('Welcome to jyLeo!',size=(200,200),windowClosing=exit)
        w.contentPane.layout = awt.FlowLayout()

        field = swing.JTextField(preferredSize=(200,20))
        w.contentPane.add(field)

        buttons = [createButton(name) for name in names]
        for button in buttons:
            w.contentPane.add(button)

        g.app.splash.hide()

        w.pack()
        w.show()

        return w
    #@-node:ekr.20070930122327:createOuterFrame
    #@+node:ekr.20070930114157:Overrides
    #@+node:ekr.20070930114157.1:Config...
    def resizePanesToRatio (self,ratio,secondary_ratio):    pass
    def setInitialWindowGeometry (self):                    pass
    def setMinibufferBindings(self):                        pass

    def setTopGeometry (self,w,h,x,y,adjustSize=True):

        __pychecker__ = '--no-argsused' # adjustSize used in derived classes.

        self.w = w
        self.h = h
        self.x = x
        self.y = y

    #@-node:ekr.20070930114157.1:Config...
    #@+node:ekr.20070930114157.3:Gui-dependent commands
    # Expanding and contracting panes.
    def contractPane         (self,event=None): pass
    def expandPane           (self,event=None): pass
    def contractBodyPane     (self,event=None): pass
    def contractLogPane      (self,event=None): pass
    def contractOutlinePane  (self,event=None): pass
    def expandBodyPane       (self,event=None): pass
    def expandLogPane        (self,event=None): pass
    def expandOutlinePane    (self,event=None): pass
    def fullyExpandBodyPane  (self,event=None): pass
    def fullyExpandLogPane   (self,event=None): pass
    def fullyExpandPane      (self,event=None): pass
    def fullyExpandOutlinePane (self,event=None): pass
    def hideBodyPane         (self,event=None): pass
    def hideLogPane          (self,event=None): pass
    def hidePane             (self,event=None): pass
    def hideOutlinePane      (self,event=None): pass

    # In the Window menu...
    def cascade              (self,event=None): pass
    def equalSizedPanes      (self,event=None): pass
    def hideLogWindow        (self,event=None): pass
    def minimizeAll          (self,event=None): pass
    def resizeToScreen       (self,event=None): pass
    def toggleActivePane     (self,event=None): pass
    def toggleSplitDirection (self,event=None): pass

    # In help menu...
    def leoHelp (self,event=None): pass
    #@nonl
    #@-node:ekr.20070930114157.3:Gui-dependent commands
    #@+node:ekr.20070930114157.4:Window...
    def bringToFront (self):    pass
    def deiconify (self):       pass
    def get_window_info(self):
        # Set w,h,x,y to a reasonable size and position.
        return 600,500,20,20
    def lift (self):            pass
    def setWrap (self,flag):    pass
    def update (self):          pass
    #@-node:ekr.20070930114157.4:Window...
    #@-node:ekr.20070930114157:Overrides
    #@-others
#@-node:ekr.20070930105601.2:class leoSwingFrame
#@+node:ekr.20070930110535:class leoSwingBody
class leoSwingBody (leoFrame.leoBody):

    def __init__ (self,frame,parentFrame):
        # g.trace('leoSwingBody')
        leoFrame.leoBody.__init__(self,frame,parentFrame) # Init the base class.

    # Birth, death & config...
    def createBindings (self,w=None):               pass
    def createControl (self,frame,parentFrame,p):   pass
    def setColorFromConfig (self,w=None):           pass
    def setFontFromConfig (self,w=None):            pass

    # Editor...
    def createEditorLabel (self,pane):  pass
    def setEditorColors (self,bg,fg):   pass

    # Events...
    def scheduleIdleTimeRoutine (self,function,*args,**keys): pass
#@-node:ekr.20070930110535:class leoSwingBody
#@+node:ekr.20070930111347:class leoSwingKeys
class swingKeyHandlerClass (leoKeys.keyHandlerClass):

    '''swing overrides of base keyHandlerClass.'''

    def __init__(self,c,useGlobalKillbuffer=False,useGlobalRegisters=False):

        # g.trace('swingKeyHandlerClass',c)

        # Init the base class.
        leoKeys.keyHandlerClass.__init__(self,c,useGlobalKillbuffer,useGlobalRegisters)
#@-node:ekr.20070930111347:class leoSwingKeys
#@+node:ekr.20070930184746.8:class leoSplash (java.lang.Runnable)
class leoSplash ( java.lang.Runnable ):

    #@    @+others
    #@+node:ekr.20070930185331:run (leoSplash)
    def run (self):

        g.trace(g.callers())

        self.splash = splash = swing.JWindow()
        splash.setAlwaysOnTop(1)
        cpane = splash.getContentPane()
        rp = splash.getRootPane()
        tb = swing.border.TitledBorder('Leo')
        tb.setTitleJustification(tb.CENTER)
        rp.setBorder(tb)
        splash.setBackground(awt.Color.ORANGE)
        dimension = awt.Dimension(400,400)
        splash.setPreferredSize(dimension)
        splash.setSize(400,400)

        sicon = g.os_path_join(g.app.loadDir,"..","Icons","Leosplash.GIF")
        ii = swing.ImageIcon(sicon)
        image = swing.JLabel(ii)
        image.setBackground(awt.Color.ORANGE)
        cpane.add(image)
        self.splashlabel = splashlabel = swing.JLabel("Leo is starting....")
        splashlabel.setBackground(awt.Color.ORANGE)
        splashlabel.setForeground(awt.Color.BLUE)
        cpane.add(splashlabel,awt.BorderLayout.SOUTH)
        w, h = self._calculateCenteredPosition(splash)
        splash.setLocation(w,h)
        splash.visible = True
    #@-node:ekr.20070930185331:run (leoSplash)
    #@+node:ekr.20070930185331.1:utils
    def _calculateCenteredPosition( self, widget ):

        size = widget.getPreferredSize()
        height = size.height/2
        width = size.width/2
        h,w = self._getScreenPositionForDialog()
        height = h - height
        width = w - width
        return width, height

    def _getScreenPositionForDialog( self ):

        #tk = self.c.frame.top.getToolkit()
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
    #@-node:ekr.20070930185331.1:utils
    #@-others
#@-node:ekr.20070930184746.8:class leoSplash (java.lang.Runnable)
#@-others
#@-node:ekr.20070930105125:@thin leoSwingFrame.py
#@-leo
