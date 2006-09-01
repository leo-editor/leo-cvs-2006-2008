#@+leo-ver=4-thin
#@+node:ekr.20060831165821:@thin slideshow.py
#@<< docstring >>
#@+node:ekr.20060831165845.1:<< docstring >>
'''A plugin to support Leo outlines representing slideshows.
'''
#@-node:ekr.20060831165845.1:<< docstring >>
#@nl

__version__ = '0.01'

#@<< version history >>
#@+node:ekr.20060831165845.2:<< version history >>
#@@killcolor
#@+at
# 
# 0.01 EKR: Initial version.
#@-at
#@nonl
#@-node:ekr.20060831165845.2:<< version history >>
#@nl
#@<< imports >>
#@+node:ekr.20060831165845.3:<< imports >>
import leoGlobals as g
import leoPlugins

Tk  = g.importExtension('Tkinter',pluginName=__name__,verbose=True,required=True)
#@-node:ekr.20060831165845.3:<< imports >>
#@nl

#@+others
#@+node:ekr.20060831165845.4:init
def init ():
    
    ok = Tk is not None
    
    if ok:
        if g.app.gui is None:
            g.app.createTkGui(__file__)
            
        ok = g.app.gui.guiName() == "tkinter"

        if ok:
            leoPlugins.registerHandler('after-create-leo-frame',onCreate)
            g.plugin_signon(__name__)
        
    return ok
#@nonl
#@-node:ekr.20060831165845.4:init
#@+node:ekr.20060831165845.5:onCreate
def onCreate (tag, keys):
    
    c = keys.get('c')
    if not c: return
    
    slideshowController(c)
#@nonl
#@-node:ekr.20060831165845.5:onCreate
#@+node:ekr.20060831165845.6:class slideshowController
class slideshowController:
    
    #@    @+others
    #@+node:ekr.20060831165845.7:__init__
    def __init__ (self,c):
        
        self.c = c
        self.slides = None
        self.slide = None
        
        self.createCommands()
    #@nonl
    #@-node:ekr.20060831165845.7:__init__
    #@+node:ekr.20060831171016:createCommands
    def createCommands (self):
        
        c = self.c ; k = c.k
        
        def slideshowBackCallback(event,self=self):
            self.back()
            
        def slideshowNextCallback(event,self=self):
            self.next()
            
        def slideshowStartCallback(event,self=self):
            self.start()
            
        for name,func in (
            ('slide-show-back',slideshowBackCallback),
            ('slide-show-next',slideshowNextCallback),
            ('slide-show-start',slideshowStartCallback),
        ):
            k.registerCommand (name,shortcut=None,func=func,pane='all',verbose=False)
    #@nonl
    #@-node:ekr.20060831171016:createCommands
    #@+node:ekr.20060831172205:start
    def start (self):
        
        c = self.c ; p = c.currentPosition()
    
        self.slides = g.findNodeAnywhere(c,'@slides')
        if self.slides:
            self.next()
            if not self.slide:
                g.es('No slide show found')
    #@nonl
    #@-node:ekr.20060831172205:start
    #@+node:ekr.20060831171016.4:back
    def back (self):
        
        c = self.c ; slide = self.slide
        if not slide: return
        p = slide.threadBack()
        done = False
        while p and not done:
            h = p.headString().strip()
            if h.startswith('@slides'):
                done = True
            elif h.startswith('@slide'):
                self.slide = p.copy()
                g.es_print('%s' % h)
                c.frame.tree.expandAllAncestors(p)
                c.selectPosition(p)
                break
            else: p = p.threadBack()
        else: done = True
        if done:
            g.es('Start of slide show')
            self.slide = None
    #@nonl
    #@-node:ekr.20060831171016.4:back
    #@+node:ekr.20060831171016.5:next
    def next (self):
        
        c = self.c ; slide = self.slide or self.slides
        if not slide: return
        p = slide.threadNext()
        done = False
        while p and not done:
            h = p.headString().strip()
            if h.startswith('@slides'):
                done = True
            elif h.startswith('@slide'):
                self.slide = p.copy()
                g.es_print('%s' % h)
                c.frame.tree.expandAllAncestors(p)
                c.selectPosition(p)
                return
            else: p = p.threadNext()
        else: done = True 
        if done and self.slide:
            g.es('End of slide show')
    #@nonl
    #@-node:ekr.20060831171016.5:next
    #@-others
#@nonl
#@-node:ekr.20060831165845.6:class slideshowController
#@-others
#@nonl
#@-node:ekr.20060831165821:@thin slideshow.py
#@-leo
