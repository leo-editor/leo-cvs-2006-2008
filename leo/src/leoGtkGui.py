# -*- coding: utf-8 -*-
#@+leo-ver=4-thin
#@+node:ekr.20080112145409.435:@thin leoGtkGui.py
#@@first

'''Leo's Gtk Gui module.'''

#@@language python
#@@tabwidth -4
#@@pagewidth 80

#@<< imports >>
#@+node:ekr.20080112145409.436:<< imports >>
import leoGlobals as g
import leoGui

import gtk
import os
import string
import sys

import leoFrame
import leoGtkFrame

# import leoTkinterComparePanel
# import leoTkinterDialog
# import leoTkinterFind
# import tkFont
# import tkFileDialog
#@-node:ekr.20080112145409.436:<< imports >>
#@nl

class gtkGui(leoGui.leoGui):

    """A class encapulating all calls to gtk."""

    #@    @+others
    #@+node:ekr.20080112145409.437:gtkGui birth & death
    #@+node:ekr.20080112145409.438: gtkGui.__init__
    def __init__ (self):

        # Initialize the base class.
        leoGui.leoGui.__init__(self,'gtk')

        self.root = None

        self.bodyTextWidget  = leoGtkFrame.leoGtkTextWidget
        self.plainTextWidget = leoGtkFrame.leoGtkTextWidget

        self.bitmap_name = None
        self.bitmap = None

        self.defaultFont = None
        self.defaultFontFamily = None

        # self.win32clipboard = None 
    #@nonl
    #@-node:ekr.20080112145409.438: gtkGui.__init__
    #@+node:ekr.20080112145409.439:createKeyHandlerClass (gtkGui)
    def createKeyHandlerClass (self,c,useGlobalKillbuffer=True,useGlobalRegisters=True):

        import leoGtkFrame # Do this here to break any circular dependency.

        return leoGtkFrame.gtkKeyHandlerClass(c,useGlobalKillbuffer,useGlobalRegisters)
    #@-node:ekr.20080112145409.439:createKeyHandlerClass (gtkGui)
    #@+node:ekr.20080112145409.440:runMainLoop (gtkGui)
    def runMainLoop(self):

        '''Start the gtk main loop.'''

        if self.script:
            log = g.app.log
            if log:
                print 'Start of batch script...\n'
                log.c.executeScript(script=self.script)
                print 'End of batch script'
            else:
                print 'no log, no commander for executeScript in gtkGui.runMainLoop'
        else:
            pass # no need to invoke a gtk main loop.
    #@-node:ekr.20080112145409.440:runMainLoop (gtkGui)
    #@+node:ekr.20080112145409.441:Not used
    def createRootWindow(self):
        pass

    def destroySelf (self):
        pass

    def killGui(self,exitFlag=True):
        """Destroy a gui and terminate Leo if exitFlag is True."""
        pass

    def recreateRootWindow(self):
        """A do-nothing base class to create the hidden root window of a gui
        after a previous gui has terminated with killGui(False)."""
        pass

    if 0:
        #@    @+others
        #@+node:ekr.20080112145409.442:gtkGui.setDefaultIcon
        def setDefaultIcon(self):

            """Set the icon to be used in all Leo windows.

            This code does nothing for gtk versions before 8.4.3."""

            gui = self

            try:
                version = gui.root.getvar("tk_patchLevel")
                # g.trace(repr(version),g.CheckVersion(version,"8.4.3"))
                if g.CheckVersion(version,"8.4.3") and sys.platform == "win32":

                    # gtk 8.4.3 or greater: load a 16 by 16 icon.
                    path = g.os_path_join(g.app.loadDir,"..","Icons")
                    if g.os_path_exists(path):
                        theFile = g.os_path_join(path,"LeoApp16.ico")
                        if g.os_path_exists(path):
                            self.bitmap = gtk.BitmapImage(theFile)
                        else:
                            g.es("LeoApp16.ico not in Icons directory", color="red")
                    else:
                        g.es("Icons directory not found: "+path, color="red")
            except:
                print "exception setting bitmap"
                import traceback ; traceback.print_exc()
        #@-node:ekr.20080112145409.442:gtkGui.setDefaultIcon
        #@+node:ekr.20080112145409.443:gtkGui.getDefaultConfigFont
        def getDefaultConfigFont(self,config):

            """Get the default font from a new text widget."""

            if not self.defaultFontFamily:
                # WARNING: retain NO references to widgets or fonts here!
                w = g.app.gui.plainTextWidget()
                fn = w.cget("font")
                font = gtkFont.Font(font=fn) 
                family = font.cget("family")
                self.defaultFontFamily = family[:]
                # print '***** getDefaultConfigFont',repr(family)

            config.defaultFont = None
            config.defaultFontFamily = self.defaultFontFamily
        #@-node:ekr.20080112145409.443:gtkGui.getDefaultConfigFont
        #@-others
    #@-node:ekr.20080112145409.441:Not used
    #@-node:ekr.20080112145409.437:gtkGui birth & death
    #@+node:ekr.20080112145409.444:gtkGui dialogs & panels
    def runAboutLeoDialog(self,c,version,theCopyright,url,email):
        """Create and run a gtk About Leo dialog."""
        d = leoGtkDialog.gtkAboutLeo(c,version,theCopyright,url,email)
        return d.run(modal=False)

    def runAskLeoIDDialog(self):
        """Create and run a dialog to get g.app.LeoID."""
        d = leoGtkDialog.gtkAskLeoID()
        return d.run(modal=True)

    def runAskOkDialog(self,c,title,message=None,text="Ok"):
        """Create and run a gtk an askOK dialog ."""
        d = leoGtkDialog.gtkAskOk(c,title,message,text)
        return d.run(modal=True)

    def runAskOkCancelNumberDialog(self,c,title,message):
        """Create and run askOkCancelNumber dialog ."""
        d = leoGtkDialog.gtkAskOkCancelNumber(c,title,message)
        return d.run(modal=True)

    def runAskOkCancelStringDialog(self,c,title,message):
        """Create and run askOkCancelString dialog ."""
        d = leoGtkDialog.gtkAskOkCancelString(c,title,message)
        return d.run(modal=True)

    def runAskYesNoDialog(self,c,title,message=None):
        """Create and run an askYesNo dialog."""
        d = leoGtkDialog.gtkAskYesNo(c,title,message)
        return d.run(modal=True)

    def runAskYesNoCancelDialog(self,c,title,
        message=None,yesMessage="Yes",noMessage="No",defaultButton="Yes"):
        """Create and run an askYesNoCancel dialog ."""
        d = leoGtkDialog.gtkAskYesNoCancel(
            c,title,message,yesMessage,noMessage,defaultButton)
        return d.run(modal=True)

    # The compare panel has no run dialog.

    # def runCompareDialog(self,c):
        # """Create and run an askYesNo dialog."""
        # if not g.app.unitTesting:
            # leoGtkCompareDialog(c)
    #@+node:ekr.20080112145409.445:gtkGui.createSpellTab
    def createSpellTab(self,c,spellHandler,tabName):

        ### return leoGtkFind.gtkSpellTab(c,spellHandler,tabName)

        pass
    #@-node:ekr.20080112145409.445:gtkGui.createSpellTab
    #@+node:ekr.20080112145409.446:gtkGui file dialogs
    # We no longer specify default extensions so that we can open and save files without extensions.
    #@+node:ekr.20080112145409.447:runOpenFileDialog
    def runOpenFileDialog(self,title,filetypes,defaultextension,multiple=False):

        """Create and run an gtk open file dialog ."""

        # __pychecker__ = '--no-argsused' # defaultextension not used.

        initialdir = g.app.globalOpenDir or g.os_path_abspath(os.getcwd())

        if multiple:
            # askopenfilenames requires Python 2.3 and gtk 8.4.
            version = '.'.join([str(sys.version_info[i]) for i in (0,1,2)])
            if (
                g.CheckVersion(version,"2.3") and
                g.CheckVersion(self.root.getvar("tk_patchLevel"),"8.4")
            ):
                files = gtkFileDialog.askopenfilenames(
                    title=title,filetypes=filetypes,initialdir=initialdir)
                # g.trace(files)
                return list(files)
            else:
                # Get one file and return it as a list.
                theFile = gtkFileDialog.askopenfilename(
                    title=title,filetypes=filetypes,initialdir=initialdir)
                return [theFile]
        else:
            # Return a single file name as a string.
            return gtkFileDialog.askopenfilename(
                title=title,filetypes=filetypes,initialdir=initialdir)
    #@-node:ekr.20080112145409.447:runOpenFileDialog
    #@+node:ekr.20080112145409.448:runSaveFileDialog
    def runSaveFileDialog(self,initialfile,title,filetypes,defaultextension):

        """Create and run an gtk save file dialog ."""

        # __pychecker__ = '--no-argsused' # defaultextension not used.

        initialdir=g.app.globalOpenDir or g.os_path_abspath(os.getcwd()),

        return gtkFileDialog.asksaveasfilename(
            initialdir=initialdir,initialfile=initialfile,
            title=title,filetypes=filetypes)
    #@-node:ekr.20080112145409.448:runSaveFileDialog
    #@-node:ekr.20080112145409.446:gtkGui file dialogs
    #@+node:ekr.20080112145409.449:gtkGui panels
    def createComparePanel(self,c):
        """Create a gtk color picker panel."""
        ### return leoGtkComparePanel.leoGtkComparePanel(c)

    def createFindPanel(self,c):
        """Create a hidden gtk find panel."""
        ### 
        # panel = leoGtkFind.leoGtkFind(c)
        # panel.top.withdraw()
        # return panel

    def createFindTab (self,c,parentFrame):
        """Create a gtk find tab in the indicated frame."""
        ### return leoGtkFind.gtkFindTab(c,parentFrame)

    def createLeoFrame(self,title):
        """Create a new Leo frame."""
        gui = self
        return leoGtkFrame.leoGtkFrame(title,gui)
    #@-node:ekr.20080112145409.449:gtkGui panels
    #@-node:ekr.20080112145409.444:gtkGui dialogs & panels
    #@+node:ekr.20080112145409.450:gtkGui utils (TO DO)
    #@+node:ekr.20080112145409.451:Clipboard (gtkGui)
    #@+node:ekr.20080112145409.452:replaceClipboardWith
    def replaceClipboardWith (self,s):

        # g.app.gui.win32clipboard is always None.
        wcb = g.app.gui.win32clipboard

        if wcb:
            try:
                wcb.OpenClipboard(0)
                wcb.EmptyClipboard()
                wcb.SetClipboardText(s)
                wcb.CloseClipboard()
            except:
                g.es_exception()
        else:
            self.root.clipboard_clear()
            self.root.clipboard_append(s)
    #@-node:ekr.20080112145409.452:replaceClipboardWith
    #@+node:ekr.20080112145409.453:getTextFromClipboard
    def getTextFromClipboard (self):

        # g.app.gui.win32clipboard is always None.
        wcb = g.app.gui.win32clipboard

        if wcb:
            try:
                wcb.OpenClipboard(0)
                data = wcb.GetClipboardData()
                wcb.CloseClipboard()
                # g.trace(data)
                return data
            except TypeError:
                # g.trace(None)
                return None
            except:
                g.es_exception()
                return None
        else:
            try:
                s = self.root.selection_get(selection="CLIPBOARD")
                return s
            except:
                return None
    #@-node:ekr.20080112145409.453:getTextFromClipboard
    #@-node:ekr.20080112145409.451:Clipboard (gtkGui)
    #@+node:ekr.20080112145409.454:color
    # g.es calls gui.color to do the translation,
    # so most code in Leo's core can simply use gtk color names.

    def color (self,color):
        '''Return the gui-specific color corresponding to the gtk color name.'''
        return color

    #@-node:ekr.20080112145409.454:color
    #@+node:ekr.20080112145409.455:Dialog
    #@+node:ekr.20080112145409.456:get_window_info
    # WARNING: Call this routine _after_ creating a dialog.
    # (This routine inhibits the grid and pack geometry managers.)

    def get_window_info (self,top):

        top.update_idletasks() # Required to get proper info.

        # Get the information about top and the screen.
        geom = top.geometry() # geom = "WidthxHeight+XOffset+YOffset"
        dim,x,y = string.split(geom,'+')
        w,h = string.split(dim,'x')
        w,h,x,y = int(w),int(h),int(x),int(y)

        return w,h,x,y
    #@-node:ekr.20080112145409.456:get_window_info
    #@+node:ekr.20080112145409.457:center_dialog
    def center_dialog(self,top):

        """Center the dialog on the screen.

        WARNING: Call this routine _after_ creating a dialog.
        (This routine inhibits the grid and pack geometry managers.)"""

        sw = top.winfo_screenwidth()
        sh = top.winfo_screenheight()
        w,h,x,y = self.get_window_info(top)

        # Set the new window coordinates, leaving w and h unchanged.
        x = (sw - w)/2
        y = (sh - h)/2
        top.geometry("%dx%d%+d%+d" % (w,h,x,y))

        return w,h,x,y
    #@-node:ekr.20080112145409.457:center_dialog
    #@+node:ekr.20080112145409.458:create_labeled_frame
    # Returns frames w and f.
    # Typically the caller would pack w into other frames, and pack content into f.

    def create_labeled_frame (self,parent,
        caption=None,relief="groove",bd=2,padx=0,pady=0):

        # Create w, the master frame.
        w = gtk.Frame(parent)
        w.grid(sticky="news")

        # Configure w as a grid with 5 rows and columns.
        # The middle of this grid will contain f, the expandable content area.
        w.columnconfigure(1,minsize=bd)
        w.columnconfigure(2,minsize=padx)
        w.columnconfigure(3,weight=1)
        w.columnconfigure(4,minsize=padx)
        w.columnconfigure(5,minsize=bd)

        w.rowconfigure(1,minsize=bd)
        w.rowconfigure(2,minsize=pady)
        w.rowconfigure(3,weight=1)
        w.rowconfigure(4,minsize=pady)
        w.rowconfigure(5,minsize=bd)

        # Create the border spanning all rows and columns.
        border = gtk.Frame(w,bd=bd,relief=relief) # padx=padx,pady=pady)
        border.grid(row=1,column=1,rowspan=5,columnspan=5,sticky="news")

        # Create the content frame, f, in the center of the grid.
        f = gtk.Frame(w,bd=bd)
        f.grid(row=3,column=3,sticky="news")

        # Add the caption.
        if caption and len(caption) > 0:
            caption = gtk.Label(parent,text=caption,highlightthickness=0,bd=0)
            # caption.tkraise(w)
            caption.grid(in_=w,row=0,column=2,rowspan=2,columnspan=3,padx=4,sticky="w")

        return w,f
    #@-node:ekr.20080112145409.458:create_labeled_frame
    #@-node:ekr.20080112145409.455:Dialog
    #@+node:ekr.20080112145409.459:Events (gtkGui)
    def event_generate(self,w,kind,*args,**keys):
        '''Generate an event.'''
        return w.event_generate(kind,*args,**keys)

    def eventChar (self,event,c=None):
        '''Return the char field of an event.'''
        return event and event.char or ''

    def eventKeysym (self,event,c=None):
        '''Return the keysym value of an event.'''
        return event and event.keysym

    def eventWidget (self,event,c=None):
        '''Return the widget field of an event.'''   
        return event and event.widget

    def eventXY (self,event,c=None):
        if event:
            return event.x,event.y
        else:
            return 0,0
    #@nonl
    #@-node:ekr.20080112145409.459:Events (gtkGui)
    #@+node:ekr.20080112145409.460:Focus
    #@+node:ekr.20080112145409.461:gtkGui.get_focus
    def get_focus(self,c):

        """Returns the widget that has focus, or body if None."""

        return c.frame.top.focus_displayof()
    #@-node:ekr.20080112145409.461:gtkGui.get_focus
    #@+node:ekr.20080112145409.462:gtk.Gui.set_focus
    set_focus_count = 0

    def set_focus(self,c,w):

        # __pychecker__ = '--no-argsused' # c not used at present.

        """Put the focus on the widget."""

        if not g.app.unitTesting and c and c.config.getBool('trace_g.app.gui.set_focus'):
            self.set_focus_count += 1
            # Do not call trace here: that might affect focus!
            print 'gui.set_focus: %4d %10s %s' % (
                self.set_focus_count,c and c.shortFileName(),
                c and c.widget_name(w)), g.callers(5)

        if w:
            try:
                if 0: # No longer needed.
                    # A call to findTab.bringToFront caused
                    # the focus problems with Pmw.Notebook.
                    w.update()

                # It's possible that the widget doesn't exist now.
                w.focus_set()
                return True
            except Exception:
                # g.es_exception()
                return False
    #@-node:ekr.20080112145409.462:gtk.Gui.set_focus
    #@-node:ekr.20080112145409.460:Focus
    #@+node:ekr.20080112145409.463:Font
    #@+node:ekr.20080112145409.464:gtkGui.getFontFromParams
    def getFontFromParams(self,family,size,slant,weight,defaultSize=12):

        # __pychecker__ = '--no-argsused' # defaultSize not used.

        family_name = family

        try:
            font = gtkFont.Font(family=family,size=size,slant=slant,weight=weight)
            # if g.app.trace: g.trace(font)
            return font
        except:
            g.es("exception setting font from ",family_name)
            g.es("family,size,slant,weight:",family,size,slant,weight)
            # g.es_exception() # This just confuses people.
            return g.app.config.defaultFont
    #@-node:ekr.20080112145409.464:gtkGui.getFontFromParams
    #@-node:ekr.20080112145409.463:Font
    #@+node:ekr.20080112145409.465:getFullVersion
    def getFullVersion (self,c):

        gtkLevel = '<gtkLevel>' ### c.frame.top.getvar("tk_patchLevel")

        return 'gtk %s' % (gtkLevel)
    #@-node:ekr.20080112145409.465:getFullVersion
    #@+node:ekr.20080112145409.466:Icons
    #@+node:ekr.20080112145409.467:attachLeoIcon & createLeoIcon
    def attachLeoIcon (self,w):

        """Try to attach a Leo icon to the Leo Window.

        Use gtk's wm_iconbitmap function if available (gtk 8.3.4 or greater).
        Otherwise, try to use the Python Imaging Library and the tkIcon package."""

        if self.bitmap != None:
            # We don't need PIL or tkicon: this is gtk 8.3.4 or greater.
            try:
                w.wm_iconbitmap(self.bitmap)
            except:
                self.bitmap = None

        if self.bitmap == None:
            try:
                #@            << try to use the PIL and tkIcon packages to draw the icon >>
                #@+node:ekr.20080112145409.468:<< try to use the PIL and tkIcon packages to draw the icon >>
                #@+at 
                #@nonl
                # This code requires Fredrik Lundh's PIL and tkIcon packages:
                # 
                # Download PIL    from 
                # http://www.pythonware.com/downloads/index.htm#pil
                # Download tkIcon from http://www.effbot.org/downloads/#tkIcon
                # 
                # Many thanks to Jonathan M. Gilligan for suggesting this 
                # code.
                #@-at
                #@@c

                import Image
                import tkIcon # pychecker complains, but this *is* used.

                # Wait until the window has been drawn once before attaching the icon in OnVisiblity.
                def visibilityCallback(event,self=self,w=w):
                    try: self.leoIcon.attach(w.winfo_id())
                    except: pass
                w.bind("<Visibility>",visibilityCallback)

                if not self.leoIcon:
                    # Load a 16 by 16 gif.  Using .gif rather than an .ico allows us to specify transparency.
                    icon_file_name = g.os_path_join(g.app.loadDir,'..','Icons','LeoWin.gif')
                    icon_file_name = g.os_path_normpath(icon_file_name)
                    icon_image = Image.open(icon_file_name)
                    if 1: # Doesn't resize.
                        self.leoIcon = self.createLeoIcon(icon_image)
                    else: # Assumes 64x64
                        self.leoIcon = tkIcon.Icon(icon_image)
                #@-node:ekr.20080112145409.468:<< try to use the PIL and tkIcon packages to draw the icon >>
                #@nl
            except:
                # import traceback ; traceback.print_exc()
                # g.es_exception()
                self.leoIcon = None
    #@+node:ekr.20080112145409.469:createLeoIcon
    # This code is adapted from tkIcon.__init__
    # Unlike the tkIcon code, this code does _not_ resize the icon file.

    def createLeoIcon (self,icon):

        try:
            import Image,_tkicon

            i = icon ; m = None
            # create transparency mask
            if i.mode == "P":
                try:
                    t = i.info["transparency"]
                    m = i.point(lambda i, t=t: i==t, "1")
                except KeyError: pass
            elif i.mode == "RGBA":
                # get transparency layer
                m = i.split()[3].point(lambda i: i == 0, "1")
            if not m:
                m = Image.new("1", i.size, 0) # opaque
            # clear unused parts of the original image
            i = i.convert("RGB")
            i.paste((0, 0, 0), (0, 0), m)
            # create icon
            m = m.tostring("raw", ("1", 0, 1))
            c = i.tostring("raw", ("BGRX", 0, -1))
            return _tkicon.new(i.size, c, m)
        except:
            return None
    #@-node:ekr.20080112145409.469:createLeoIcon
    #@-node:ekr.20080112145409.467:attachLeoIcon & createLeoIcon
    #@-node:ekr.20080112145409.466:Icons
    #@+node:ekr.20080112145409.470:Idle Time
    #@+node:ekr.20080112145409.471:gtkGui.setIdleTimeHook
    def setIdleTimeHook (self,idleTimeHookHandler):

        # if self.root:
            # self.root.after_idle(idleTimeHookHandler)

        pass
    #@nonl
    #@-node:ekr.20080112145409.471:gtkGui.setIdleTimeHook
    #@+node:ekr.20080112145409.472:setIdleTimeHookAfterDelay
    def setIdleTimeHookAfterDelay (self,idleTimeHookHandler):

        if self.root:
            g.app.root.after(g.app.idleTimeDelay,idleTimeHookHandler)
    #@-node:ekr.20080112145409.472:setIdleTimeHookAfterDelay
    #@-node:ekr.20080112145409.470:Idle Time
    #@+node:ekr.20080112145409.473:isTextWidget
    def isTextWidget (self,w):

        '''Return True if w is a Text widget suitable for text-oriented commands.'''

        return w and isinstance(w,leoFrame.stringTextWidget) ### gtk.Text)
    #@-node:ekr.20080112145409.473:isTextWidget
    #@+node:ekr.20080112145409.474:makeScriptButton
    def makeScriptButton (self,c,
        p=None, # A node containing the script.
        script=None, # The script itself.
        buttonText=None,
        balloonText='Script Button',
        shortcut=None,bg='LightSteelBlue1',
        define_g=True,define_name='__main__',silent=False, # Passed on to c.executeScript.
    ):

        '''Create a script button for the script in node p.
        The button's text defaults to p.headString'''

        k = c.k
        if p and not buttonText: buttonText = p.headString().strip()
        if not buttonText: buttonText = 'Unnamed Script Button'
        #@    << create the button b >>
        #@+node:ekr.20080112145409.475:<< create the button b >>
        iconBar = c.frame.getIconBarObject()
        b = iconBar.add(text=buttonText)

        # if balloonText and balloonText != buttonText:
            # Pmw = g.importExtension('Pmw',pluginName='gui.makeScriptButton',verbose=False)
            # if Pmw:
                # balloon = Pmw.Balloon(b,initwait=100)
                # balloon.bind(b,balloonText)

        # if sys.platform == "win32":
            # width = int(len(buttonText) * 0.9)
            # b.configure(width=width,font=('verdana',7,'bold'),bg=bg)
        #@-node:ekr.20080112145409.475:<< create the button b >>
        #@nl
        #@    << define the callbacks for b >>
        #@+node:ekr.20080112145409.476:<< define the callbacks for b >>
        def deleteButtonCallback(event=None,b=b,c=c):
            if b: b.pack_forget()
            c.bodyWantsFocus()

        def executeScriptCallback (event=None,
            b=b,c=c,buttonText=buttonText,p=p and p.copy(),script=script):

            if c.disableCommandsMessage:
                g.es(c.disableCommandsMessage,color='blue')
            else:
                g.app.scriptDict = {}
                c.executeScript(p=p,script=script,
                define_g= define_g,define_name=define_name,silent=silent)
                # Remove the button if the script asks to be removed.
                if g.app.scriptDict.get('removeMe'):
                    g.es("Removing '%s' button at its request" % buttonText)
                    b.pack_forget()
            # Do not assume the script will want to remain in this commander.
        #@-node:ekr.20080112145409.476:<< define the callbacks for b >>
        #@nl
        b.configure(command=executeScriptCallback)
        b.bind('<3>',deleteButtonCallback)
        if shortcut:
            #@        << bind the shortcut to executeScriptCallback >>
            #@+node:ekr.20080112145409.477:<< bind the shortcut to executeScriptCallback >>
            func = executeScriptCallback
            shortcut = k.canonicalizeShortcut(shortcut)
            ok = k.bindKey ('button', shortcut,func,buttonText)
            if ok:
                g.es_print('Bound @button %s to %s' % (buttonText,shortcut),color='blue')
            #@-node:ekr.20080112145409.477:<< bind the shortcut to executeScriptCallback >>
            #@nl
        #@    << create press-buttonText-button command >>
        #@+node:ekr.20080112145409.478:<< create press-buttonText-button command >>
        aList = [g.choose(ch.isalnum(),ch,'-') for ch in buttonText]

        buttonCommandName = ''.join(aList)
        buttonCommandName = buttonCommandName.replace('--','-')
        buttonCommandName = 'press-%s-button' % buttonCommandName.lower()

        # This will use any shortcut defined in an @shortcuts node.
        k.registerCommand(buttonCommandName,None,executeScriptCallback,pane='button',verbose=False)
        #@-node:ekr.20080112145409.478:<< create press-buttonText-button command >>
        #@nl
    #@-node:ekr.20080112145409.474:makeScriptButton
    #@-node:ekr.20080112145409.450:gtkGui utils (TO DO)
    #@+node:ekr.20080112145409.479:class leoKeyEvent (gtkGui)
    class leoKeyEvent:

        '''A gui-independent wrapper for gui events.'''

        def __init__ (self,event,c):

            # g.trace('leoKeyEvent(gtkGui)')
            self.actualEvent = event
            self.c      = c # Required to access c.k tables.
            self.char   = hasattr(event,'char') and event.char or ''
            self.keysym = hasattr(event,'keysym') and event.keysym or ''
            self.w      = hasattr(event,'widget') and event.widget or None
            self.x      = hasattr(event,'x') and event.x or 0
            self.y      = hasattr(event,'y') and event.y or 0
            # Support for fastGotoNode plugin
            self.x_root = hasattr(event,'x_root') and event.x_root or 0
            self.y_root = hasattr(event,'y_root') and event.y_root or 0

            if self.keysym and c.k:
                # Translate keysyms for ascii characters to the character itself.
                self.keysym = c.k.guiBindNamesInverseDict.get(self.keysym,self.keysym)

            self.widget = self.w

        def __repr__ (self):

            return 'gtkGui.leoKeyEvent: char: %s, keysym: %s' % (repr(self.char),repr(self.keysym))
    #@nonl
    #@-node:ekr.20080112145409.479:class leoKeyEvent (gtkGui)
    #@-others
#@-node:ekr.20080112145409.435:@thin leoGtkGui.py
#@-leo
