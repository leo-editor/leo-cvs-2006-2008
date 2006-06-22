#@+leo-ver=4-thin
#@+node:ekr.20060601151845:@thin shortcut_button.py
'''A plugin to create a 'Shortcut' button in the icon area.

Pressing the Shortcut button creates *another* button which when pressed will
select the presently selected node at the time the button was created.'''

#@<< imports >>
#@+node:ekr.20060601151845.2:<< imports >>
import leoGlobals as g
import leoPlugins
from mod_scripting import scriptingController

Tk = g.importExtension('Tkinter',pluginName=__name__,verbose=True)
#@nonl
#@-node:ekr.20060601151845.2:<< imports >>
#@nl

__version__ = "0.2"
#@<< version history >>
#@+node:ekr.20060601151845.3:<< version history >>
#@@nocolor
#@+at
# 
# 0.1 Initial version.  Suggested by Brian Theado.
# 0.2 EKR: Improved docstring.
#@-at
#@nonl
#@-node:ekr.20060601151845.3:<< version history >>
#@nl

#@+others
#@+node:ekr.20060601151845.4:init
def init ():
    
    ok = Tk and not g.app.unitTesting
    
    if ok:
        if g.app.gui is None:
            g.app.createTkGui(__file__)
            
        ok = g.app.gui.guiName() == "tkinter"

        if ok:
            # Note: call onCreate _after_ reading the .leo file.
            # That is, the 'after-create-leo-frame' hook is too early!
            leoPlugins.registerHandler(('new','open2'),onCreate)
            g.plugin_signon(__name__)
        
    return ok
#@nonl
#@-node:ekr.20060601151845.4:init
#@+node:ekr.20060601151845.5:onCreate
def onCreate (tag, keys):

    """Handle the onCreate event in the chapterHoist plugin."""
    
    c = keys.get('c')

    if c:
        sc = scriptingController(c)
        ch = shortcutButton(sc,c)
#@nonl
#@-node:ekr.20060601151845.5:onCreate
#@+node:ekr.20060601151845.6:class shortcutButton
class shortcutButton:
    
    #@    @+others
    #@+node:ekr.20060601151845.7: ctor
    def __init__ (self,sc,c):
    
        g.trace()
        self.createShortcutButtonButton(sc,c)
    #@-node:ekr.20060601151845.7: ctor
    #@+node:ekr.20060601153526:createShortcutButtonButton
    def createShortcutButtonButton(self,sc,c):
    
        b = sc.createIconButton('Shortcut', 'Create a shortcut button', bg='LightSteelBlue1')
    
        def shortcutButtonButtonCallback(self=self,sc=sc,c=c):
            self.createShortcutButton(sc,c)
            
        def deleteButtonCallback(event=None,sc=sc,b=b):
            sc.deleteButton(b)
    
        b.configure(command=shortcutButtonButtonCallback)
        b.bind('<3>',deleteButtonCallback)
    #@nonl
    #@-node:ekr.20060601153526:createShortcutButtonButton
    #@+node:ekr.20060601151845.10:createShortcutButton
    def createShortcutButton (self,sc,c):
        
        '''Create a button which selects the present position (when the button was created).'''
        p = c.currentPosition() ; h = p.headString()
        buttonText = sc.getButtonText(h)
        statusLine = "Shortcut %s" % h
        
        b = sc.createIconButton(
            text=buttonText,statusLine=statusLine,bg='LightSteelBlue1')
    
        def deleteButtonCallback(event=None,sc=sc,b=b):
            sc.deleteButton(b)
            
        def shortcutButtonCallback (event=None,c=c,p=p):
            c.beginUpdate()
            try:
                c.selectPosition(p)
            finally:
                c.endUpdate()
    
        b.configure(command=shortcutButtonCallback)
        b.bind('<3>',deleteButtonCallback)
    #@nonl
    #@-node:ekr.20060601151845.10:createShortcutButton
    #@-others
#@nonl
#@-node:ekr.20060601151845.6:class shortcutButton
#@-others
#@nonl
#@-node:ekr.20060601151845:@thin shortcut_button.py
#@-leo
