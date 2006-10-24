# -*- coding: utf-8 -*-
#@+leo-ver=4-thin
#@+node:ekr.20061024060248.1:@thin leoPymacs.py
#@@first

#@<< docstring>>
#@+node:ekr.20061024060248.2:<< docstring >>
'''A module to allow the Pymacs bridge to access Leo data.

All code in this module must be called *from* Emacs:
calling Pymacs.lisp in other situations will hang Leo.

Emacs code initiallizes this module with::
    
    (pymacs-eval "sys.path.append('c:\\prog\\tigris-cvs\\leo\\src')")
    (setq leo (pymacs-load "leoPymacs"))

'''
#@-node:ekr.20061024060248.2:<< docstring >>
#@nl

#@@language python
#@@tabwidth -4

# Each entry does its own imports.

inited = False
commanders = {} # Keys are absolute file names; values are commanders.

#@+others
#@+node:ekr.20061024060248.3:hello
def hello():
    
    import leoGlobals as g
    return 'Hello from Leo.  g.app: %s' % g.app
#@nonl
#@-node:ekr.20061024060248.3:hello
#@+node:ekr.20061024075542:init
def init ():
    
    global inited
    if inited:
        g.trace('already inited')
        return
    else:
        inited = True
    
    # Create the dummy app
    import leo 
    leo.run(pymacs=True)
    
    import leoGlobals as g
    # These traces show up in the pymacs buffer.
    g.trace(g.app)
    g.trace(g.app.gui)
#@nonl
#@-node:ekr.20061024075542:init
#@+node:ekr.20061024075542.1:open
def open (fileName=None):
    
    import leoGlobals as g
    
    if not fileName:
        fileName = r'c:\prog\tigris-cvs\leo\test\test.leo'

    # openWithFileName checks to see if the file is already open.
    ok, frame = g.openWithFileName(
        fileName,
        old_c=None,
        enableLog=False,
        readAtFileNodesFlag=True)

    c = ok and frame.c or None
    if c:
        global commanders
        cid = str('cid: %s' % c.fileName()) # Pymacs converts unicode strings to handles.
        commanders[cid] = c
        g.trace(cid)
        return cid
    else:
        g.trace('Can not open %s' % fileName)
        return None
#@nonl
#@-node:ekr.20061024075542.1:open
#@+node:ekr.20061024084200:test
def test():
    
    pass
#@nonl
#@-node:ekr.20061024084200:test
#@-others

init()
#@nonl
#@-node:ekr.20061024060248.1:@thin leoPymacs.py
#@-leo
