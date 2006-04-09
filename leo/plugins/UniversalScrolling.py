#@+leo-ver=4-thin
#@+node:ekr.20040831122004:@thin UniversalScrolling.py
#@<< docstring >>
#@+node:ekr.20050913084245:<< docstring >>
'''A plugin that enables the user to scroll down with a left mouse click and
hold, and to scroll up with a right mouse click and hold. Scrolling continues
until the user releases the mouse. 

Originally designed as a workaround for various bugs in Tkinter scrolling,
this may actually be superior to wheel scrolling, in that there is little work
a user has to do to scroll except to press a button.

We use a Thread and 4 Tkinter Events to enable this. Threading was
necessary to deserialise Button Press and Button Release. Without a Thread
there apparently was no way to split the two apart. Exterior processes were
not considered as serious pieces of the mechanism, threading kept things
simple.
'''
#@nonl
#@-node:ekr.20050913084245:<< docstring >>
#@nl
#@<< imports >>
#@+node:ekr.20050101090207.5:<< imports >>
import leoGlobals as g
import leoTkinterFrame

Tk = g.importExtension('Tkinter',pluginName=__name__,verbose=True)
    
import threading
import time
#@nonl
#@-node:ekr.20050101090207.5:<< imports >>
#@nl
__version__ = "0.2"
#@<< version history >>
#@+node:ekr.20050526121340:<< version history >>
#@@nocolor

#@+at
# 
# 0.2 EKR:
#     - Added init method.
#     - Simplified the code.
# 
# Note: This code appears to work. At present it suffers from re-binding 
# Button-1.
# The solution is to pick another binding :-)
#@-at
#@nonl
#@-node:ekr.20050526121340:<< version history >>
#@nl

createCanvas = leoTkinterFrame.leoTkinterFrame.createCanvas

#@+others
#@+node:ekr.20050526121026:init
def init ():
    
    ok = Tk and not g.app.unitTesting
    
    if ok:
        if g.app.gui is None:
            g.app.createTkGui(__file__)
            
        ok = g.app.gui.guiName() == "tkinter"

        if ok:
            leoTkinterFrame.leoTkinterFrame.createCanvas = addUThreading
            g.plugin_signon(__name__)
        
    return ok
#@nonl
#@-node:ekr.20050526121026:init
#@+node:ekr.20040915104230:addUThreading & callbacks
def addUThreading (tkFrame,parentFrame):

    '''Replaces createCanvas, adding UniversalScolling'''
    
    class directionClass:
        way = 'Down'
        
    canvas = createCanvas(tkFrame,parentFrame)
    ev = threading.Event()
    presentDirection = directionClass()
    
    # Define callbacks.
    #@    @+others
    #@+node:ekr.20040915104230.2:run
    # Watch for events to begin scrolling.  This is also the target of the thread.
    def run( ev = ev):
    
        while 1:
            ev.wait()
            # g.trace(presentDirection.way)
            if presentDirection.way == 'Down':
                # g.trace(canvas.yview())
                canvas.yview(Tk.SCROLL, 1, Tk.UNITS)
            else:
                canvas.yview( Tk.SCROLL, -1, Tk.UNITS )
            time.sleep(.1)
    #@-node:ekr.20040915104230.2:run
    #@+node:ekr.20050526094449.2:scroll & helpers
    def scroll(event,way):
    
        """A callback that starts scrolling."""
    
        x = event.widget.canvasx( event.x )
        y = event.widget.canvasy( event.y )
        item = event.widget.find_overlapping(x,y,x,y)
        if item:
            return "continue"
        else:
            # g.trace(event,way,event.widget)
            ev.set()
            presentDirection.way = way
            return 'break'
    
    def scrollDown(event):
        scroll(event,'Down')
        
    def scrollUp(event):
        scroll(event,'Up')
    #@nonl
    #@-node:ekr.20050526094449.2:scroll & helpers
    #@+node:ekr.20040915104230.4:stopScrolling
    def stopScrolling (event,ev=ev):
        
        """A callback that stops scrolling."""
    
        ev.clear()
    #@nonl
    #@-node:ekr.20040915104230.4:stopScrolling
    #@-others
    
    # Start the thread.
    t = threading.Thread(target = run)
    t.setDaemon(True)
    t.start()

    # Replace the canvas bindings.
    canvas.bind( '<Button-1>', scrollDown)
    canvas.bind( '<Button-3>', scrollUp)
    canvas.bind( '<ButtonRelease-1>', stopScrolling)
    canvas.bind( '<ButtonRelease-3>', stopScrolling)
    return canvas
#@nonl
#@-node:ekr.20040915104230:addUThreading & callbacks
#@-others
#@nonl
#@-node:ekr.20040831122004:@thin UniversalScrolling.py
#@-leo
