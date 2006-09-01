#@+leo-ver=4-thin
#@+node:ekr.20060831165821:@thin slideshow.py
#@<< docstring >>
#@+node:ekr.20060831165845.1:<< docstring >>
'''A plugin to support slideshows in Leo outlines.

It defines three new commands:
    
- slide-show-start: start a slide show
- slide-show-next:  move to the next slide of a slide show.
- slide-show-back:  move to the previous slide of a slide show.

Slides shows consist of a root @slides node with descendent @slide nodes.
@slide nodes may be organized via non-@slide nodes that do not appear in the slideshow.
'''
#@-node:ekr.20060831165845.1:<< docstring >>
#@nl

__version__ = '0.02'

#@+at
# To do:
# - Support multiple slideshows: slide-show-start prompts for a slideshow name 
# somehow.
# - Add sound/script support for slides.
# - Save/restore changes to slides when entering/leaving a slide.
#@-at
#@@c

#@<< version history >>
#@+node:ekr.20060831165845.2:<< version history >>
#@@killcolor
#@+at
# 
# 0.01 EKR: Initial version.
# 0.02 EKR: Improved docstring and added todo notes.
# 0.03 EKR: Simplified createCommands.
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
            
        for name,func in (
            ('slide-show-back',self.back),
            ('slide-show-next',self.next),
            ('slide-show-start',self.start),
        ):
            k.registerCommand (name,shortcut=None,func=func,pane='all',verbose=False)
    #@nonl
    #@-node:ekr.20060831171016:createCommands
    #@+node:ekr.20060831172205:start
    def start (self,event=None):
        
        c = self.c ; p = c.currentPosition()
    
        self.slides = g.findNodeAnywhere(c,'@slides')
        if self.slides:
            self.next()
            if not self.slide:
                g.es('No slide show found')
    #@nonl
    #@-node:ekr.20060831172205:start
    #@+node:ekr.20060831171016.4:back
    def back (self,event=None):
        
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
    def next (self,event=None):
        
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
