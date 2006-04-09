#@+leo-ver=4-thin
#@+node:ekr.20051016160700:@thin testRegisterCommand.py
'''A plugin to test k.registerCommand.'''

#@@language python
#@@tabwidth -4

import leoPlugins
import leoGlobals as g

__version__ = '0.1'

#@+others
#@+node:ekr.20051016161205:init
def init():
    
    leoPlugins.registerHandler('after-create-leo-frame',onCreate)
    g.plugin_signon(__name__)
    return True
#@nonl
#@-node:ekr.20051016161205:init
#@+node:ekr.20051016161205.1:onCreate
def onCreate(tag,keys):
    
    c = keys.get('c')
    if c:
        def f (event):
            g.es_print('Hello',color='purple')
            
        c.keyHandler.registerCommand(
            'print-hello','Alt-Ctrl-Shift-p',f)
#@nonl
#@-node:ekr.20051016161205.1:onCreate
#@-others
#@nonl
#@-node:ekr.20051016160700:@thin testRegisterCommand.py
#@-leo
