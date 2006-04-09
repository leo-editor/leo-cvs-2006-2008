#@+leo-ver=4-thin
#@+node:ekr.20040108095351:@thin rowcol.py
"""Add row/column indicators to the toolbar."""

#@@language python
#@@tabwidth -4

__name__ = "Row/Column indicators"
__version__ = "0.3"

#@<< imports >>
#@+node:ekr.20040908094021.2:<< imports >>
import leoGlobals as g
import leoPlugins

Tk = g.importExtension('Tkinter',pluginName=__name__,verbose=True)
#@nonl
#@-node:ekr.20040908094021.2:<< imports >>
#@nl
#@<< version history >>
#@+node:ekr.20041120114651:<< version history >>
#@@killcolor
#@+at
# 
# 0.1 Initial version.
# 
# 0.2 EKR:
# Make sure this works properly with multiple windows.
# 
# 0.3 EKR:
# Removed call to g.top.  We now test whether c is valid using 
# hasattr(c,'frame')
#@-at
#@nonl
#@-node:ekr.20041120114651:<< version history >>
#@nl

#@+others
#@+node:ekr.20041120114651.1:onCreate
def onCreate (tag,keywords):
    
    c = keywords.get("c")
    if c:
        rowCol = rowColClass(c)
        rowCol.addWidgets()
        leoPlugins.registerHandler("idle",rowCol.update)
#@nonl
#@-node:ekr.20041120114651.1:onCreate
#@+node:ekr.20040108095351.1:class rowColClass
class rowColClass:
    
    """Class that puts row/column indicators in the status bar."""
    
    #@    @+others
    #@+node:ekr.20040108100040:__init__
    def __init__ (self,c):
        
        self.c = c
        self.lastRow,self.lastCol = -1,-1
    #@nonl
    #@-node:ekr.20040108100040:__init__
    #@+node:ekr.20040108095351.2:addWidgets
    def addWidgets (self):
    
        c = self.c
        iconBar = c.frame.iconBar
        iconBarFrame = iconBar.getFrame()
    
        # Main container 
        self.frame = Tk.Frame(iconBarFrame) 
        self.frame.pack(side="left")
    
        text = "line 0, col 0"
        width = len(text) # Setting the width here prevents jitters.
        self.label = Tk.Label(self.frame,text=text,width=width,anchor="w")
        self.label.pack(side="left")
        
        # Update the row/column indicators immediately to reserve a place.
        self.update()
    #@nonl
    #@-node:ekr.20040108095351.2:addWidgets
    #@+node:ekr.20040108095351.4:update
    def update (self,*args,**keys):
        
        c = self.c
    
        # This is called at idle-time, and there can be problems when closing the window.
        if g.app.killed or not c or not hasattr(c,'frame'):
            return
    
        body = c.frame.body.bodyCtrl ; gui = g.app.gui
        tab_width = c.frame.tab_width
    
        index = body.index("insert")
        row,col = gui.getindex(body,index)
    
        if col > 0:
            s = body.get("%d.0" % (row),index)
            s = g.toUnicode(s,g.app.tkEncoding)
            col = g.computeWidth(s,tab_width)
    
        if row != self.lastRow or col != self.lastCol:
            s = "line %d, col %d " % (row,col)
            self.label.configure(text=s)
            self.lastRow,self.lastCol = row,col
            
        if 0: # Done in idle handler.
            self.label.after(500,self.update)
    #@nonl
    #@-node:ekr.20040108095351.4:update
    #@-others
#@nonl
#@-node:ekr.20040108095351.1:class rowColClass
#@-others

if Tk: # OK for unit testing.

    if g.app.gui is None: 
        g.app.createTkGui(__file__)

    if g.app.gui.guiName() == "tkinter":
        leoPlugins.registerHandler("after-create-leo-frame",onCreate)
        g.plugin_signon("rowcol")
#@nonl
#@-node:ekr.20040108095351:@thin rowcol.py
#@-leo
