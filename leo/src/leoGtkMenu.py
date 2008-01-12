# -*- coding: utf-8 -*-
#@+leo-ver=4-thin
#@+node:ekr.20080112171213:@thin leoGtkMenu.py
#@@first

'''Leo's Gtk Gui module.'''

#@@language python
#@@tabwidth -4
#@@pagewidth 80

#@<< imports >>
#@+node:ekr.20080112171315:<< imports >>
import leoGlobals as g

import gtk

import leoMenu
#@-node:ekr.20080112171315:<< imports >>
#@nl

class leoGtkMenu(leoMenu.leoMenu):

    #@    @+others
    #@+node:ekr.20080112145409.174: leoGtkMenu.__init__
    def __init__ (self,frame):

        # Init the base class.
        leoMenu.leoMenu.__init__(self,frame)
    #@-node:ekr.20080112145409.174: leoGtkMenu.__init__
    #@+node:ekr.20080112145409.181:plugin menu stuff... (not ready yet)
    if 0:
        #@    @+others
        #@+node:ekr.20080112145409.182:createPluginMenu
        def createPluginMenu (self):

            top = self.getMenu('top')
            oline = self.getMenu('Outline')
            ind = top.getComponentIndex(oline) + 1
            import leoGtkPluginManager
            self.plugin_menu = pmenu = leoGtkPluginManager.createPluginsMenu()
            #self.plugin_menu = pmenu = gtk.JMenu( "Plugins" )
            top.add(pmenu,ind)
            #cpm = gtk.JMenuItem( "Plugin Manager" )
            #cpm.actionPerformed = self.createPluginManager
            #pmenu.add( cpm )
            #pmenu.addSeparator()


            #self.names_and_commands[ "Plugin Manager" ] = self.createPluginManager


        #@-node:ekr.20080112145409.182:createPluginMenu
        #@+node:ekr.20080112145409.183:createPluginManager
        def createPluginManager (self,event):

            import leoGtkPluginManager as lspm
            lspm.topLevelMenu()

        #@-node:ekr.20080112145409.183:createPluginManager
        #@+node:ekr.20080112145409.184:getPluginMenu
        def getPluginMenu (self):

            return self.plugin_menu
        #@-node:ekr.20080112145409.184:getPluginMenu
        #@-others
    #@nonl
    #@-node:ekr.20080112145409.181:plugin menu stuff... (not ready yet)
    #@+node:ekr.20080112145409.195:oops
    def oops (self):

        print "leoMenu oops:", g.callers(2), "should be overridden in subclass"
    #@nonl
    #@-node:ekr.20080112145409.195:oops
    #@+node:ekr.20080112145409.194:createRecentFilesMenuItems (gtkMenu)
    def createRecentFilesMenuItems (self):

        c = self.c ; frame = c.frame
        recentFilesMenu = self.getMenu("Recent Files...")

        # Delete all previous entries.
        # if len( recentFilesMenu.getMenuComponents() ) != 0:
            # deferable = lambda :self.delete_range(recentFilesMenu,0,len(c.recentFiles)+2)
            # if not gtk.GtkUtilities.isEventDispatchThread():
                # dc = DefCallable( deferable )
                # ft = dc.wrappedAsFutureTask()
                # gtk.GtkUtilities.invokeAndWait( ft )
            # else:
                # deferable()
        # Create the first two entries.
        table = (
            ("Clear Recent Files",None,c.clearRecentFiles),
            ("-",None,None))
        self.createMenuEntries(recentFilesMenu,table)

        # Create all the other entries.
        i = 3
        for name in c.recentFiles:
            def callback (event=None,c=c,name=name): # 12/9/03
                c.openRecentFile(name)
            label = "%d %s" % (i-2,g.computeWindowTitle(name))
            self.add_command(recentFilesMenu,label=label,command=callback,underline=0)
            i += 1
    #@nonl
    #@-node:ekr.20080112145409.194:createRecentFilesMenuItems (gtkMenu)
    #@+node:ekr.20080112145409.196:Must be overridden in menu subclasses
    #@+node:ekr.20080112145409.197:9 Routines with Tk spellings
    def add_cascade (self,parent,label,menu,underline):

        menu.setText(label)

    def add_command (self,menu,**keys):

        return None

        # if keys[ 'label' ] == "Open Python Window":
            # keys[ 'command' ] = self.openJythonShell

        # self.names_and_commands[ keys[ 'label' ] ] = keys[ 'command' ]

        # action = self.MenuRunnable( keys[ 'label' ], keys[ 'command' ], self.c, self.executor )
        # jmenu = gtk.JMenuItem( action )
        # if keys.has_key( 'accelerator' ) and keys[ 'accelerator' ]:
            # accel = keys[ 'accelerator' ]
            # acc_list = accel.split( '+' )
            # changeTo = { 'Alt': 'alt', 'Shift':'shift', #translation table
                         # 'Ctrl':'ctrl', 'UpArrow':'UP', 'DnArrow':'DOWN',
                         # '-':'MINUS', '+':'PLUS', '=':'EQUALS',
                         # '[':'typed [', ']':'typed ]', '{':'typed {',
                         # '}':'typed }', 'Esc':'ESCAPE', '.':'typed .',
                          # "`":"typed `", "BkSp":"BACK_SPACE"} #SEE java.awt.event.KeyEvent for further translations
            # chg_list = []
            # for z in acc_list:
                # if z in changeTo:
                    # chg_list.append( changeTo[ z ] )
                # else:
                    # chg_list.append( z )
            # accelerator = " ".join( chg_list )
            # ks = gtk.KeyStroke.getKeyStroke( accelerator )
            # if ks:
                # self.keystrokes_and_actions[ ks ] = action
                # jmenu.setAccelerator( ks )
            # else:
                # pass
        # menu.add( jmenu )
        # label = keys[ 'label' ]
        # return jmenu

    def add_separator (self,menu):
        pass

    def bind (self,bind_shortcut,callback):
        #self.oops() 
        pass

    def delete (self,menu,realItemName):
        self.oops()

    def delete_range (self,menu,n1,n2):

        pass
        # items = menu.getMenuComponents()
        # n3 = n1
        # components = []
        # while 1:
            # if n3 == n2:
                # break
            # item = menu.getMenuComponent( n3 )
            # components.append( item )
            # n3 += 1

        # for z in components:
            # menu.remove( z )


    def destroy (self,menu):
        self.oops()

    def insert_cascade (self,parent,index,label,menu,underline):
        self.oops()

    def new_menu (self,parent,tearoff=0):

        return None ###
    #@-node:ekr.20080112145409.197:9 Routines with Tk spellings
    #@+node:ekr.20080112145409.198:7 Routines with new spellings
    def createMenuBar (self,frame):

        top = frame.top
        self.defineMenuTables()
        # topMenu = gtk.JMenuBar()
        # top.setJMenuBar( topMenu )
        # topMenu.setFont( self.font )
        # # Do gui-independent stuff.
        # self.setMenu("top",topMenu)
        # self.createMenusFromTables()
        # self.createLeoGtkPrint()
        # self.createPluginMenu()
        # self.addUserGuide()

    def createOpenWithMenuFromTable (self,table):
        self.oops()

    def defineMenuCallback (self,command,name):
        return command

    def defineOpenWithMenuCallback (self,command):
        self.oops()

    def disableMenu (self,menu,name):
        for z in menu.getMenuComponents():
            if hasattr(z,"getText") and z.getText() == name:
                z.setEnabled(False)

    def enableMenu (self,menu,name,val):
        for z in menu.getMenuComponents():
            if hasattr(z,"getText") and z.getText() == name:
                z.setEnabled(bool(val))

    def setMenuLabel (self,menu,name,label,underline=-1,enabled=1):

        item = (menu,name,label,enabled)
        self.queue.offer(item)
        self.executor.submit(self.menu_changer)
    #@-node:ekr.20080112145409.198:7 Routines with new spellings
    #@-node:ekr.20080112145409.196:Must be overridden in menu subclasses
    #@-others
#@nonl
#@-node:ekr.20080112171213:@thin leoGtkMenu.py
#@-leo
