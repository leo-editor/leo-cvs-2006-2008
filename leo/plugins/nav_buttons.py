#@+leo-ver=4-thin
#@+node:edream.110203113231.758:@thin nav_buttons.py
"""Adds navigation buttons to icon bar"""

#@@language python
#@@tabwidth -4

#@<< imports >>
#@+node:ekr.20050219114353:<< imports >>

import leoGlobals as g
import leoPlugins

from leoTkinterDialog import tkinterListBoxDialog

try: import Tkinter as Tk
except ImportError: Tk = None

import os
#@nonl
#@-node:ekr.20050219114353:<< imports >>
#@nl
__version__ = "1.5"
#@<< version history >>
#@+node:ekr.20050219114353.1:<< version history >>
#@@killcolor
#@+at
# 
# 1.3 EKR:
#     - Rewritten to use:
#         - init and onCreate functions.
#         - Common imageClass.
#         - per-commander dialogs.
#         - positions rather than vnodes.
#     - Fixed numerous bugs.
#     - The code is _much_ simpler than before.
#     - Added marksInitiallyVisible and recentInitiallyVisible config 
# constants.
# 
# 1.4 EKR: 2 bug fixes
#     - Allways fill the box when clicking on the 'Recent' button.
#     - Use keywords.get('c') NOT self.c in hook handlers.  They may not be 
# the same!
#         - This is actually a bug in leoPlugins.registerHandler, but it can't 
# be
#           fixed because there is no way to associate commanders with hook 
# handlers.
# 
# 1.5 EKR: Fixed crasher in tkinterListBoxDialog.go().
#     updateMarks must set positionList ivar in the base class.
#@-at
#@-node:ekr.20050219114353.1:<< version history >>
#@nl

marksInitiallyVisible = False
recentInitiallyVisible = False

#@+others
#@+node:ekr.20050219114353.2:init
def init ():
    
    ok = Tk is not None
    
    if ok:
        if g.app.gui is None:
            g.app.createTkGui(__file__)

        if g.app.gui.guiName() == "tkinter":
            leoPlugins.registerHandler('after-create-leo-frame',onCreate)
            g.plugin_signon(__name__)
            
    return ok
#@nonl
#@-node:ekr.20050219114353.2:init
#@+node:ekr.20050219115116:onCreate
def onCreate (tag,keywords):

    # Not ok for unit testing: can't use unitTestGui.
    if g.app.unitTesting:
        return
        
    c = keywords.get("c")
    r = leoPlugins.registerHandler
    
    images = imageClass()
    
    # Create the marks dialog and hooks.
    marks = marksDialog(c,images)
    r(('open2','new2','set-mark','clear-mark'),marks.updateMarks)

    # Create the recent nodes dialog.
    recent = recentSectionsDialog(c,images)
    r(('open2','new2','select2'),recent.updateRecent)
#@nonl
#@-node:ekr.20050219115116:onCreate
#@+node:ekr.20050219115859:class imageClass
class imageClass:
    
    #@    @+others
    #@+node:ekr.20050219115859.1:ctor
    def __init__ (self):
        
        self.path = g.os_path_join(g.app.loadDir,'..','Icons')
        
        # Create images and set ivars.
        for ivar,icon in (
            ('lt_nav_disabled_image','lt_arrow_disabled.gif'),
            ('lt_nav_enabled_image', 'lt_arrow_enabled.gif'),
            ('rt_nav_disabled_image','rt_arrow_disabled.gif'),
            ('rt_nav_enabled_image', 'rt_arrow_enabled.gif'),
        ):
            image = self.createImage(icon)
            setattr(self,ivar,image)
    #@nonl
    #@-node:ekr.20050219115859.1:ctor
    #@+node:ekr.20050219115859.2:createImage
    def createImage (self,iconName):
        
        path = os.path.normpath(os.path.join(self.path,iconName))
        
        try:
            image = Tk.PhotoImage(master=g.app.root,file=path)
        except:
            g.es("can not load icon: %s" % iconName)
            image = None
    
        return image
    #@nonl
    #@-node:ekr.20050219115859.2:createImage
    #@-others
#@nonl
#@-node:ekr.20050219115859:class imageClass
#@+node:edream.110203113231.775:class marksDialog (listBoxDialog)
class marksDialog (tkinterListBoxDialog):
    
    """A class to create the marks dialog"""

    #@    @+others
    #@+node:edream.110203113231.776: marksDialog.__init__
    def __init__ (self,c,images):
        
        """Create a Marks listbox dialog."""
        
        self.c = c
        self.images = images
    
        self.label = None
        self.title = 'Marks for %s' % g.shortFileName(c.mFileName) # c.frame.title
        
        # Init the base class and call self.createFrame.
        tkinterListBoxDialog.__init__(self,c,self.title,self.label)
        
        if not marksInitiallyVisible:
            self.top.withdraw()
        
        self.addButtons()
    #@nonl
    #@-node:edream.110203113231.776: marksDialog.__init__
    #@+node:ekr.20050219131752:addButtons
    def addButtons (self):
        
        c = self.c ; images = self.images
        
        def marksButtonCallback(*args,**keys):
            self.top.deiconify()
        
        self.marks_button = c.frame.addIconButton(
            text="Marks",command=marksButtonCallback)
    #@nonl
    #@-node:ekr.20050219131752:addButtons
    #@+node:edream.110203113231.777:createFrame
    def createFrame(self):
        
        """Create the frame for a Marks listbox dialog."""
    
        tkinterListBoxDialog.createFrame(self)
    
        f = Tk.Frame(self.outerFrame)
        f.pack()
    
        self.addStdButtons(f)
    #@nonl
    #@-node:edream.110203113231.777:createFrame
    #@+node:edream.110203113231.779:updateMarks
    def updateMarks(self,tag,keywords):
    
        '''Recreate the Marks listbox.'''
        
        # Warning: it is not correct to use self.c in hook handlers.
        c = keywords.get('c')
        if c != self.c: return
    
        self.box.delete(0,"end")
        
        # Bug fix 5/12/05: Set self.positionList for use by tkinterListBoxDialog.go().
        i = 0 ; self.positionList = [] ; tnodeList = []
    
        for p in c.allNodes_iter():
            if p.isMarked() and p.v.t not in tnodeList:
                self.box.insert(i,p.headString().strip())
                tnodeList.append(p.v.t)
                self.positionList.append(p.copy())
                i += 1
    #@nonl
    #@-node:edream.110203113231.779:updateMarks
    #@-others
#@nonl
#@-node:edream.110203113231.775:class marksDialog (listBoxDialog)
#@+node:edream.110203113231.780:class recentSectionsDialog (tkinterListBoxDialog)
class recentSectionsDialog (tkinterListBoxDialog):
    
    """A class to create the recent sections dialog"""

    #@    @+others
    #@+node:edream.110203113231.781:__init__  recentSectionsDialog
    def __init__ (self,c,images):
        
        """Create a Recent Sections listbox dialog."""
        
        self.c = c
        self.images = images
        self.label = None
        self.title = "Recent nodes for %s" % g.shortFileName(c.mFileName)
        self.lt_nav_button = self.rt_nav_button = None # Created by createFrame.
    
        self.addIconBarButtons()
    
        # Init the base class. (calls createFrame)
        # N.B.  The base class contains positionList ivar.
        tkinterListBoxDialog.__init__(self,c,self.title,self.label)
        
        self.fillbox() # Must be done initially.
        
        if not recentInitiallyVisible:
            self.top.withdraw()
    
        self.updateButtons()
    #@nonl
    #@-node:edream.110203113231.781:__init__  recentSectionsDialog
    #@+node:ekr.20050219131336:addIconBarButtons
    def addIconBarButtons (self):
        
        c = self.c ; images = self.images
        
        # Add 'Recent' button to icon bar.
        def recentButtonCallback(*args,**keys):
            self.fillbox(forceUpdate=True)
            self.top.deiconify()
    
        self.sections_button = c.frame.addIconButton(
            text="Recent",command=recentButtonCallback)
    
        # Add left and right arrows to icon bar.
        self.lt_nav_disabled_image = images.lt_nav_disabled_image
        self.lt_nav_enabled_image  = images.lt_nav_enabled_image
        self.rt_nav_disabled_image = images.rt_nav_disabled_image
        self.rt_nav_enabled_image  = images.rt_nav_enabled_image
    
        self.lt_nav_iconFrame_button = c.frame.addIconButton(
            image=self.lt_nav_disabled_image,
            command=c.goPrevVisitedNode)
    
        self.rt_nav_iconFrame_button = c.frame.addIconButton(
            image=self.rt_nav_disabled_image,
            command=c.goNextVisitedNode)
            
        # Don't dim the button when it is inactive.
        for b in (self.lt_nav_iconFrame_button,self.rt_nav_iconFrame_button):
            fg = b.cget("foreground")
            b.configure(disabledforeground=fg)
            
        # Package these buttons for the recentSectionsDialog class in leoTkinterDialog.py
        self.nav_buttons = (self.lt_nav_iconFrame_button, self.rt_nav_iconFrame_button)
    #@nonl
    #@-node:ekr.20050219131336:addIconBarButtons
    #@+node:edream.110203113231.782:addFrameButtons
    def addFrameButtons (self):
        
        """Add buttons to the listbox dialog."""
    
        self.buttonFrame = f = Tk.Frame(self.outerFrame)
        f.pack()
        
        row1 = Tk.Frame(f)
        row1.pack()
        
        # Create the back and forward buttons, cloning the images & commands of the already existing buttons.
        image   = self.lt_nav_iconFrame_button.cget("image")
        command = self.lt_nav_iconFrame_button.cget("command")
    
        self.lt_nav_button = b = Tk.Button(row1,image=image,command=command)
        b.pack(side="left",pady=2,padx=5)
        
        image   = self.rt_nav_iconFrame_button.cget("image")
        command = self.rt_nav_iconFrame_button.cget("command")
    
        self.rt_nav_button = b = Tk.Button(row1,image=image,command=command)
        b.pack(side="left",pady=2,padx=5)
        
        row2 = Tk.Frame(f)
        row2.pack()
        self.addStdButtons(row2)
        
        row3 = Tk.Frame(f)
        row3.pack()
        
        self.clear_button = b =  Tk.Button(row3,text="Clear All",
            width=6,command=self.clearAll)
        b.pack(side="left",pady=2,padx=5)
        
        self.delete_button = b =  Tk.Button(row3,text="Delete",
            width=6,command=self.deleteEntry)
        b.pack(side="left",pady=2,padx=5)
    #@-node:edream.110203113231.782:addFrameButtons
    #@+node:edream.110203113231.783:clearAll
    def clearAll (self,event=None):
    
        """Handle clicks in the "Delete" button of the Recent Sections listbox dialog."""
        
        c = self.c
    
        self.c.visitedList = []
        self.positionList = []
        self.fillbox()
    #@nonl
    #@-node:edream.110203113231.783:clearAll
    #@+node:edream.110203113231.784:createFrame
    def createFrame(self):
        
        """Create the frame of a Recent Sections listbox dialog."""
        
        tkinterListBoxDialog.createFrame(self)
        self.addFrameButtons()
    #@nonl
    #@-node:edream.110203113231.784:createFrame
    #@+node:edream.110203113231.785:deleteEntry
    def deleteEntry (self,event=None):
    
        """Handle clicks in the "Delete" button of a Recent Sections listbox dialog."""
        
        c = self.c ; box = self.box
        
        # Work around an old Python bug.  Convert strings to ints.
        items = box.curselection()
        try:
            items = map(int, items)
        except ValueError: pass
    
        if items:
            n = items[0]
            p = self.position[n]
            del self.positionList[n]
            if p in c.visitedList:
                c.visitedList.remove(p)
            self.fillbox()
    #@nonl
    #@-node:edream.110203113231.785:deleteEntry
    #@+node:edream.110203113231.786:destroy
    def destroy (self,event=None):
        
        """Hide a Recent Sections listbox dialog and mark it inactive.
        
        This is an escape from possible performace penalties"""
            
        # This is enough to disable fillbox.
        self.top.withdraw()
    #@-node:edream.110203113231.786:destroy
    #@+node:edream.110203113231.787:fillbox
    def fillbox(self,forceUpdate=False):
    
        """Update the Recent Sections listbox."""
    
        # Only fill the box if the dialog is visible.
        # This is an important protection against bad performance.
        if not forceUpdate and self.top.state() != "normal":
            return
            
        self.box.delete(0,"end")
        c = self.c ; i = 0
        self.positionList = [] ; tnodeList = []
        for p in c.visitedList:
            if p.exists(c) and p.v.t not in tnodeList:
                self.box.insert(i,p.headString().strip())
                tnodeList.append(p.v.t)
                self.positionList.append(p.copy())
                i += 1
    #@nonl
    #@-node:edream.110203113231.787:fillbox
    #@+node:ekr.20050508104217:testxxx.py
    import unittest
    
    #@+others
    #@+node:ekr.20050508104217.1:TestXXX
    class TestXXX(unittest.TestCase):
    
        """Tests for the XXX class"""
    
        #@    @+others
        #@+node:ekr.20050508104217.2:setUp
        def setUp(self):
        
            """Create the test fixture"""
        #@nonl
        #@-node:ekr.20050508104217.2:setUp
        #@-others
    #@nonl
    #@-node:ekr.20050508104217.1:TestXXX
    #@-others
    
    if __name__ == "__main__":
        unittest.main()
    #@nonl
    #@-node:ekr.20050508104217:testxxx.py
    #@+node:ekr.20050219122657:updateButtons
    def updateButtons (self):
        
        c = self.c
            
        for b,b2,enabled_image,disabled_image,cond in (
            (
                self.lt_nav_button,self.lt_nav_iconFrame_button,
                self.lt_nav_enabled_image,self.lt_nav_disabled_image,
                c.beadPointer > 1),
            (
                self.rt_nav_button,self.rt_nav_iconFrame_button,
                self.rt_nav_enabled_image,self.rt_nav_disabled_image,
                c.beadPointer + 1 < len(c.beadList)),
        ):
            # Disabled state makes the icon look bad.
            image = g.choose(cond,enabled_image,disabled_image)
            b.configure(image=image,state='normal')
            b2.configure(image=image,state='normal')
    #@nonl
    #@-node:ekr.20050219122657:updateButtons
    #@+node:ekr.20050219162434:updateRecent
    def updateRecent(self,tag,keywords):
    
        # Warning: it is not correct to use self.c in hook handlers.
        c = keywords.get('c')
        if c != self.c: return
    
        forceUpdate = tag in ('new2','open2')
        self.fillbox(forceUpdate)
        self.updateButtons()
    #@nonl
    #@-node:ekr.20050219162434:updateRecent
    #@-others
#@nonl
#@-node:edream.110203113231.780:class recentSectionsDialog (tkinterListBoxDialog)
#@-others
#@nonl
#@-node:edream.110203113231.758:@thin nav_buttons.py
#@-leo
