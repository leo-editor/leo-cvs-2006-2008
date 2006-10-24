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

# As in leo.py we must be very careful about imports.
g = None # set by init: do *not* import it here!

inited = False

#@+others
#@+node:ekr.20061024131236:dump
def dump (anObject):
    
    return str(g.toEncodedString(repr(anObject),encoding='ascii'))
#@-node:ekr.20061024131236:dump
#@+node:ekr.20061024130957:getters
def app ():
    '''Scripts can use g.app.scriptDict for communication with pymacs.'''
    return g.app
    
def g():
    return g
#@nonl
#@-node:ekr.20061024130957:getters
#@+node:ekr.20061024060248.3:hello
def hello():

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
    
    import leoGlobals
    global g ; g = leoGlobals

    # These traces show up in the pymacs buffer.
    g.trace('app',g.app)
    g.trace('gui',g.app.gui)
#@-node:ekr.20061024075542:init
#@+node:ekr.20061024075542.1:open
def open (fileName=None):
    
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
        return c
    else:
        g.trace('Can not open %s' % fileName)
        return None
#@nonl
#@-node:ekr.20061024075542.1:open
#@+node:ekr.20061024084200:run-script
def run_script(c,script,p=None):
    
    # It is possible to use script=None, in which case p must be defined.

    c.executeScript(
        event=None,
        p=p,
        script=script,
        useSelectedText=False,
        define_g=True,
        define_name='__main__',
        silent=True,  # Don't write to the log.
    )
    
    g.trace('script done')
#@nonl
#@-node:ekr.20061024084200:run-script
#@-others

init()
#@nonl
#@-node:ekr.20061024060248.1:@thin leoPymacs.py
#@-leo
