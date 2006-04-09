#@+leo-ver=4-thin
#@+node:leo4u.20040924130601.1:@thin TabWindow.py
"""
a Tk implimentation of notebook tabbed windows like PMW has 
PMW is  little flaky for me.
replacement for TabbedLog
for URLLoader and other use
more default tabs than the Log in Leo to pick from.

I could have never figured this out myself.
e
"""
__version__ = ".012"

#@<< imports >>
#@+node:leo4u.20040924130601.2:<< imports >>
import leoGlobals as g
import weakref

try:
    import Tkinter as Tk
except ImportError:
    Tk = g.cantImport("Tk")

try:
    import Tknotebook
except ImportError:
    Tknotebook = g.cantImport("Tknotebook")
#@-node:leo4u.20040924130601.2:<< imports >>
#@nl

#@+others
#@+node:leo4u.20040924130601.3:how to
# To get a new tab in TabWindow:

# import TabWindow as TabbedLog  #mimic TabbedLog
# tw = TabbedLog.getPane(name, c)
# 
# 
# tw is the pane returned for you to work with.
# name is the name of the tab you want for the pane.
# c is the commander for the leoFrame.
#@nonl
#@-node:leo4u.20040924130601.3:how to
#@+node:leo4u.20040924130601.8:createLog
def createLog (self,parentframe):

    nb = Tknotebook.notebook(parentframe) # notebook returns callable
    #, borderwidth= 1, pagemargin= 0
    #nb.pack({'fill':'both', 'expand':1, })

    nbs [self] = nb()
    pn = nb.add("Log")
    return oldCLog(self,pn)
#@nonl
#@-node:leo4u.20040924130601.8:createLog
#@+node:leo4u.20040924130601.9:getPane
def getPane (name,c):
    
    f = c.frame.log
    nb = nbs [f]
    return nb.add(name)
#@-node:leo4u.20040924130601.9:getPane
#@-others

if Tk and Tknotebook:
    import leoPlugins
    import leoTkinterFrame

    nbs = weakref.WeakKeyDictionary()
    oldCLog = leoTkinterFrame.leoTkinterLog.createControl
    leoTkinterFrame.leoTkinterLog.createControl = createLog
    
    #g.plugin_signon( __name__ )

#@@language python
#@@tabwidth -4
#@@color 
#@-node:leo4u.20040924130601.1:@thin TabWindow.py
#@-leo
