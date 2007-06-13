#@+leo-ver=4-thin
#@+node:ekr.20040915073259.1:@thin maximizeNewWindows.py
"""Maximizes all new windows."""

#@@language python
#@@tabwidth -4

__version__ = "1.3"
#@<< version history >>
#@+node:ekr.20040915073259.2:<< version history >>
#@+at
# 
# Original written by Jaakko Kourula.
# 
# 1.0 EKR:
#     - Enabled only for windows platform.
#     - Minor style changes.
# 1.1 EKR: Make sure c exists in maximize_window.
# 1.2 EKR:
#     - The proper guard is:
#         if c and c.exists and c.frame and not c.frame.isNullFrame:
#     - Added init function.
# 1.3 EKR: Now works on Linux.
#@-at
#@nonl
#@-node:ekr.20040915073259.2:<< version history >>
#@nl
#@<< imports >>
#@+node:ekr.20070602072200:<< imports >>
import leoGlobals as g
import leoPlugins
import sys

Tk = g.importExtension('Tkinter',pluginName=__name__,verbose=True)
#@nonl
#@-node:ekr.20070602072200:<< imports >>
#@nl

#@+others
#@+node:ekr.20070602072200.1:init
def init():
    ok = Tk and not g.app.unitTesting
    if ok:
        leoPlugins.registerHandler("after-create-leo-frame", maximize_window)
        g.plugin_signon(__name__)
    return ok
#@-node:ekr.20070602072200.1:init
#@+node:ekr.20070602072200.2:maximize_window
def maximize_window(tag, keywords):

    c = keywords.get('c')
    if c and c.exists and c.frame and not c.frame.isNullFrame:
        top = c.frame.top
        if sys.platform.startswith('win'):
            top.state("zoomed")
        else:
            # Put the top-left corner on the screen.
            x,y = 0,0
            w = top.winfo_screenwidth()-8
            h = top.winfo_screenheight()- 46
            geom = "%dx%d%+d%+d" % (w,h,x,y)
            def maximize_window_callback(event=None,geom=geom,top=top):
                g.trace('w,h,x,y',w,h,x,y,'c',c.shortFileName())
                top.geometry(geom)
            c.frame.top.after_idle(maximize_window_callback)
#@nonl
#@-node:ekr.20070602072200.2:maximize_window
#@-others
#@-node:ekr.20040915073259.1:@thin maximizeNewWindows.py
#@-leo
