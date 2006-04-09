#@+leo-ver=4-thin
#@+node:ekr.20040915075530:@thin UASearch.py
"""
A plugin for searching unknownAttributes (uA's).
"""

#@@language python
#@@tabwidth -4

__version__ = ".4"
#@<< version history >>
#@+node:ekr.20040915075530.1:<< version history >>
#@+at
# 
# 0.1: Original
# 
# 0.2 EKR:
#     - Style changes.
#     - Converted to outline.
#     - Enable this plugin only if Tk and Pmw can be imported.
#     - Added found function to handle selecting found nodes properly.
# 0.3 EKR:
#     - Changed 'new_c' logic to 'c' logic.
#     - Added init function.
#     - Removed 'start2' hook and haveseen dict.
# 0.4 EKR:
#     - use c.frame.log.select.selectTab instead of TabbedLog plugin.
#@-at
#@nonl
#@-node:ekr.20040915075530.1:<< version history >>
#@nl
#@<< imports >>
#@+node:ekr.20040915075530.2:<< imports >>
import leoGlobals as g
import leoPlugins
import leoTkinterFrame

Tk        = g.importExtension('Tkinter',  pluginName=__name__,verbose=True)
Pmw       = g.importExtension("Pmw",      pluginName=__name__,verbose=True)

import re
import weakref
#@nonl
#@-node:ekr.20040915075530.2:<< imports >>
#@nl

#@+others
#@+node:ekr.20050311090939.6:init
def init ():
    
    ok = Tk is not None # Ok for unit tests: adds menu.
    
    if ok:
        leoPlugins.registerHandler(('new','open2'),addPMenu)
        g.plugin_signon( __name__ )

    return ok
#@nonl
#@-node:ekr.20050311090939.6:init
#@+node:ekr.20040915075530.3:addPMenu
def addPMenu (tag,keywords):
    c = keywords.get('c')
    if not c: return

    # New in Leo 4.4: the log is always tabbed.
    if 1: x = c.frame.log.selectTab("UASearch")
    else: x = TabbedLog.getPane("UASearch",c)

    ef = Pmw.EntryField(x,labelpos='w',label_text='uaname:')
    e = ef.component('entry')
    e.configure(background='white',foreground='blue')
    ef.pack()
    ev = Pmw.EntryField(x,labelpos='w',label_text='uavalue:')
    e = ev.component('entry')
    e.configure(background='white',foreground='blue')
    ev.pack()
    rs = Pmw.RadioSelect(x,labelpos='n',
        label_text = 'Search by:',
        frame_borderwidth = 2,
        frame_relief = 'ridge',
        buttontype = 'radiobutton')
    rs.add("uaname")
    rs.add("uavalue")
    rs.add("regex")
    rs.pack()
    rs.setvalue("uaname")
    b = Tk.Button(x,text="Search")
    b.pack()
    l = Tk.Label(x)
    l.pack()
    #@    << define callbacks >>
    #@+node:ekr.20040915075808:<< define callbacks >>
    def firesearch( event, rs = rs, ef = ef, ev = ev, c = c, l = l ):
    
        stype = rs.getvalue()
        name = ef.getvalue()
        value = ev.getvalue()
        l.configure( text = "Searching    " )
        search( name, value, stype, c )
        l.configure( text = "" )
    #@nonl
    #@-node:ekr.20040915075808:<< define callbacks >>
    #@nl
    b.bind('<Button-1>',firesearch)
#@-node:ekr.20040915075530.3:addPMenu
#@+node:ekr.20040915081837:found
def found (porv,name):
    
    c = porv.c
    note("found: " + name)
    c.selectVnode(porv)
    c.redraw()
#@nonl
#@-node:ekr.20040915081837:found
#@+node:ekr.20040915082303:note
def note (s):
    
    print s
    g.es(s)
#@nonl
#@-node:ekr.20040915082303:note
#@+node:ekr.20040915075530.4:search
def search( name, value, stype, c ):
    cv = c.currentVnode().threadNext()
    if name.strip() == '':
        return note("empty name")
    if stype == "uaname":
        while cv:
            t = getT( cv )
            if hasattr(t,'unknownAttributes'): 
                if t.unknownAttributes.has_key( name ):
                    return found(cv,name)
            cv = cv.threadNext()
    else:
        if value.strip() == '': return
        if stype == 'regex':
            sea = re.compile( value )
        while cv:
            t = getT( cv )
            if hasattr(t,'unknownAttributes' ):
                if t.unknownAttributes.has_key( name ):
                    if stype == 'uavalue':
                        if t.unknownAttributes[ name ] == value:
                            return found(cv,name)
                    else:
                        st = t.unknownAttributes[ name ]
                        if sea.search( st ):
                            return found(cv,name)
            cv = cv.threadNext()
    note ("not found: " + name)
#@nonl
#@-node:ekr.20040915075530.4:search
#@+node:ekr.20040915075530.5:getT
def getT( node ):

    if str( node.__class__ )== 'leoNodes.vnode':
        return node.t
    else:
        return node.v.t
#@nonl
#@-node:ekr.20040915075530.5:getT
#@-others
#@nonl
#@-node:ekr.20040915075530:@thin UASearch.py
#@-leo
