#@+leo-ver=4-thin
#@+node:EKR.20040517080555.2:@thin plugins_menu.py
#@<< docstring >>
#@+node:ekr.20050101090207.9:<< docstring >>
'''Create a Plugins menu

Adds an item to the plugin menu for each active plugin. Selecting
this menu item will bring up a short About dialog with the details of the
plugin.

Plugins can create additional menu items by defining functions named
"cmd_XZY". These will apear in a sub menu. 

If the plugin requires an INI file then a configure menu item will be
created which will show an INI file editor. the plugin can define an
"applyConfiguration" function, which will be called when the configuration 
changes.

Plugins can also define a top level function to be called instead of
the default "About" dialog by defining a "topLevelMenu" function in
the plugin. This function will be called when the user clicks on the
plugin name in the plugins menu, but only if the plugin was loaded
properly and registered with g.plugin_signon.

Plugins can define their name by setting the __plugin_name__ property.

Plugins can also attempt to select the order they will apear in the menu
by defining a __plugin_prioriy__. The menu will be created with the
highest priority items first. This behaviour is not guaranteed since
other plugins can define any priority. This priority does not affect
the order of calling handlers.

To change the order select a number outside the range 0-200 since this
range is used internally for sorting alphabetically.
'''
#@nonl
#@-node:ekr.20050101090207.9:<< docstring >>
#@nl

# Written by Paul A. Paterson.  Revised by Edward K. Ream.
# To do: add Revert button to each dialog.

#@@language python
#@@tabwidth -4

#@<< imports >>
#@+node:ekr.20050101090207.10:<< imports >>
import leoGlobals as g
import leoPlugins

Tk = g.importExtension('Tkinter',pluginName=__name__,verbose=True)

import ConfigParser
import glob
import os
import sys
#@nonl
#@-node:ekr.20050101090207.10:<< imports >>
#@nl
__version__ = "1.15"
#@<< version history >>
#@+node:ekr.20050101100033:<< version history >>
#@@nocolor
#@+at
# 
# 1.4 EKR: Check at runtime to make sure that the plugin has been loaded 
# before calling topLevelMenu function.
# 1.5 EKR:
# - Check for ImportError directly in Plugin.__init__.
#   Alas, this can not report import problems without more work.
#   This _really_ should be done, but it will have to wait.
#   As a workaround, plugins_manager.py now has an init method and reports its 
# own import problems.
# 1.6 Paul Paterson:
# - Add support for plugin groups. Each group gets its own sub menu now
# - Set __plugin_group__ to "Core"
# 1.7 EKR: Set default version in Plugin.__init__ so plugins without version 
# still appear in plugin menu.
# 1.8 Paul Paterson: Changed the names in the plugin menu to remove at_, mod_ 
# and capitalized.
# 1.9 Paul Paterson:
# - Refactored to allow dynamically adding plugins to the menu after initial 
# load
# - Reformatted menu items for cmd_ThisIsIt to be "This Is It"
# 1.10 EKR: Removed the g.app.dialog hack.
# 1.11 EKR: Added event arg to cmd_callback.  This was causing crashes in 
# several plugins.
# 1.12 EKR: Fixed bug per 
# http://sourceforge.net/forum/message.php?msg_id=3810157
# 1.13 EKR:
# - Always Plugin.name and Plugin.realname for use by createPluginsMenu.
# - Add plugins to Plugins menu *only* if they have been explicitly enabled.
#   This solves the HTTP mystery: HTTP was being imported by mod_scripting 
# plugin.
# 1.14 EKR: Added init function.
# 1.15 plumloco: Separated out the gui elements of the 'properties' and 
# 'about' dialogs to make the plugin gui independant.
#@-at
#@nonl
#@-node:ekr.20050101100033:<< version history >>
#@nl

__plugin_name__ = "Plugins Menu"
__plugin_priority__ = -100
__plugin_group__ = "Core"

#@+others
#@+node:ekr.20060107091318:Functions
#@+node:EKR.20040517080555.24:addPluginMenuItem
def addPluginMenuItem (p,c):

    # g.trace(p.name,g.callers())

    if p.hastoplevel:
        # Check at runtime to see if the plugin has actually been loaded.
        # This prevents us from calling hasTopLevel() on unloaded plugins.
        def callback (event,c=c,p=p):
            path, name = g.os_path_split(p.filename)
            name, ext = g.os_path_splitext(name)
            # g.trace(name,g.app.loadedPlugins)
            if name in g.app.loadedPlugins:
                p.hastoplevel(c)
            else:
                p.about()
        table = ((p.name,None,callback),)
        c.frame.menu.createMenuEntries(PluginDatabase.getMenu(p),table,dynamicMenu=True)
    elif p.hasconfig or p.othercmds:
        #@        << Get menu location >>
        #@+node:pap.20050305153147:<< Get menu location >>
        if p.group:
            menu_location = p.group
        else:
            menu_location = "&Plugins"
        #@-node:pap.20050305153147:<< Get menu location >>
        #@nl
        m = c.frame.menu.createNewMenu(p.name,menu_location)
        table = [("About...",None,p.about)]
        if p.hasconfig:
            table.append(("Properties...",None,p.properties))
        if p.othercmds:
            table.append(("-",None,None))
            items = []
            for cmd, fn in p.othercmds.iteritems():
                # New in 4.4: this callback gets called with an event arg.
                def cmd_callback (event,c=c,fn=fn):
                    fn(c)
                items.append((cmd,None,cmd_callback),)
            items.sort()
            table.extend(items)
        c.frame.menu.createMenuEntries(m,table,dynamicMenu=True)
    else:
        table = ((p.name,None,p.about),)
        c.frame.menu.createMenuEntries(PluginDatabase.getMenu(p),table,dynamicMenu=True)
#@nonl
#@-node:EKR.20040517080555.24:addPluginMenuItem
#@+node:EKR.20040517080555.23:createPluginsMenu
def createPluginsMenu (tag,keywords):

    c = keywords.get("c")
    if not c: return

    old_path = sys.path[:] # Make a _copy_ of the path.

    path = os.path.join(g.app.loadDir,"..","plugins")
    sys.path = path

    if os.path.exists(path):
        # Create a list of all active plugins.
        files = glob.glob(os.path.join(path,"*.py"))
        files.sort()
        plugins = [PlugIn(file) for file in files]
        PluginDatabase.storeAllPlugins(files)
        loaded = [z.lower() for z in g.app.loadedPlugins]
        # items = [(p.name,p) for p in plugins if p.version]
        items = [(p.name,p) for p in plugins if p.moduleName and p.moduleName.lower() in loaded]
        # g.trace('loaded',g.app.loadedPlugins)
        # g.trace('realnames',[p.realname for p in plugins if p.realname])
        # g.trace('names',[p.name for p in plugins if p.name])
        # g.trace('moduleNamesnames',[p.moduleName for p in plugins if p.moduleName])
        if items:
            #@            << Sort items >>
            #@+node:pap.20041009133925:<< sort items >>
            dec = [(item[1].priority, item) for item in items]
            dec.sort()
            dec.reverse()
            items = [item[1] for item in dec]
            #@nonl
            #@-node:pap.20041009133925:<< sort items >>
            #@nl
            c.pluginsMenu = pluginMenu = c.frame.menu.createNewMenu("&Plugins")
            PluginDatabase.setMenu("Default", pluginMenu)
            #@            << Add group menus >>
            #@+node:pap.20050305152223:<< Add group menus >>
            for group_name in PluginDatabase.getGroups():
                PluginDatabase.setMenu(group_name, c.frame.menu.createNewMenu(group_name, "&Plugins"))
            #@-node:pap.20050305152223:<< Add group menus >>
            #@nl
            for name,p in items:
                addPluginMenuItem(p, c)

    sys.path = old_path
#@nonl
#@-node:EKR.20040517080555.23:createPluginsMenu
#@+node:ekr.20070302175530:init
def init ():



    if g.app.unitTesting: return None

    if g.app.gui is None:
            g.app.createTkGui(__file__)

            if g.app.gui.guiName() != "tkinter":
                return False

    leoPlugins.registerHandler("create-optional-menus",createPluginsMenu)
    g.plugin_signon(__name__)


    if g.app.gui.guiName() == 'tkinter':
        g.app.gui.runPropertiesDialog = runPropertiesDialog
        g.app.gui.runScrolledMessageDialog = runScrolledMessageDialog

    return True
#@-node:ekr.20070302175530:init
#@-node:ekr.20060107091318:Functions
#@+node:pap.20050305152751:class PluginDatabase
class _PluginDatabase:
    """Stores information on Plugins"""

    #@    @+others
    #@+node:pap.20050305152751.1:__init__
    def __init__(self):
        """Initialize"""
        self.plugins_by_group = {}
        self.groups_by_plugin = {}
        self.menus = {}
        self.all_plugins = []
    #@nonl
    #@-node:pap.20050305152751.1:__init__
    #@+node:pap.20050305152751.2:addPlugin
    def addPlugin(self, item, group):
        """Add a plugin"""
        if group:
            self.plugins_by_group.setdefault(group, []).append(item)
            self.groups_by_plugin[item] = group
    #@-node:pap.20050305152751.2:addPlugin
    #@+node:pap.20050305152751.3:getGroups
    def getGroups(self):
        """Return a list of groups"""
        groups = self.plugins_by_group.keys()
        groups.sort()
        return groups
    #@nonl
    #@-node:pap.20050305152751.3:getGroups
    #@+node:pap.20050305153716:setMenu
    def setMenu(self, name, menu):
        """Store the menu for this group"""
        self.menus[name] = menu
    #@nonl
    #@-node:pap.20050305153716:setMenu
    #@+node:pap.20050305153716.1:getMenu
    def getMenu(self, item):
        """Get the menu for a particular item"""
        try:
            return self.menus[item.group]
        except KeyError:
            return self.menus["Default"]
    #@nonl
    #@-node:pap.20050305153716.1:getMenu
    #@+node:pap.20051008005012:storeAllPlugins
    def storeAllPlugins(self, files):
        """Store all the plugins for later reference if we need to enable them"""
        self.all_plugins = dict(
            [(g.os_path_splitext(g.os_path_basename(f))[0], f) for f in files])
    #@nonl
    #@-node:pap.20051008005012:storeAllPlugins
    #@-others

PluginDatabase = _PluginDatabase()
#@nonl
#@-node:pap.20050305152751:class PluginDatabase
#@+node:EKR.20040517080555.3:class Plugin
class PlugIn:

    """A class to hold information about one plugin"""

    #@    @+others
    #@+node:EKR.20040517080555.4:__init__
    def __init__(self, filename):

        """Initialize the plug-in"""

        # Import the file to find out some interesting stuff
        # Do not use the imp module: we only want to import these files once!
        self.name = self.realname = self.moduleName = None
        self.mod = self.doc = self.version = None
        self.filename = g.os_path_abspath(filename)
        try:
            self.mod = __import__(g.os_path_splitext(g.os_path_basename(filename))[0])
            if not self.mod: return

            try:
                self.name = self.mod.__plugin_name__
            except AttributeError:
                self.name = self.getNiceName(self.mod.__name__)

            self.moduleName = self.mod.__name__
            self.realname = self.name

            self.group = getattr(self.mod, "__plugin_group__", None)
            PluginDatabase.addPlugin(self, self.group)

            try:
                self.priority = self.mod.__plugin_priority__
            except AttributeError:
                self.priority = 200 - ord(self.name[0])
            #
            self.doc = self.mod.__doc__
            self.version = self.mod.__dict__.get("__version__","<unknown>") # EKR: 3/17/05
            # if self.version: print self.version,g.shortFileName(filename)
        except ImportError:
            # s = 'Can not import %s in plugins_menu plugin' % g.shortFileName(filename)
            # print s ; g.es(s,color='blue')
            return
        except Exception:
            s = 'Unexpected exception in plugins_menu plugin importing %s' % filename
            print s ; g.es(s,color='red')
            return

        #@    << Check if this can be configured >>
        #@+node:EKR.20040517080555.5:<< Check if this can be configured >>
        # Look for a configuration file
        self.configfilename = "%s.ini" % os.path.splitext(filename)[0]
        self.hasconfig = os.path.isfile(self.configfilename)
        #@-node:EKR.20040517080555.5:<< Check if this can be configured >>
        #@nl
        #@    << Check if this has an apply >>
        #@+node:EKR.20040517080555.6:<< Check if this has an apply >>
        #@+at 
        #@nonl
        # Look for an apply function ("applyConfiguration") in the module.
        # 
        # This is used to apply changes in configuration from the properties 
        # window
        #@-at
        #@@c

        self.hasapply = hasattr(self.mod, "applyConfiguration")
        #@-node:EKR.20040517080555.6:<< Check if this has an apply >>
        #@nl
        #@    << Look for additional commands >>
        #@+node:EKR.20040517080555.7:<< Look for additional commands >>
        #@+at 
        #@nonl
        # Additional commands can be added to the plugin menu by having 
        # functions in the module called "cmd_whatever". These are added to 
        # the main menu and will be called when clicked
        #@-at
        #@@c

        self.othercmds = {}

        for item in self.mod.__dict__.keys():
            if item.startswith("cmd_"):
                self.othercmds[self.niceMenuName(item)] = self.mod.__dict__[item]
        #@-node:EKR.20040517080555.7:<< Look for additional commands >>
        #@nl
        #@    << Look for toplevel menu item >>
        #@+node:pap.20041009131822:<< Look for toplevel menu item >>
        #@+at 
        #@nonl
        # Check to see if there is a toplevel menu item - this will be used 
        # instead of the default About
        #@-at
        #@@c

        try:
            self.hastoplevel = self.mod.__dict__["topLevelMenu"]
        except KeyError:
            self.hastoplevel = False
        #@nonl
        #@-node:pap.20041009131822:<< Look for toplevel menu item >>
        #@nl
    #@-node:EKR.20040517080555.4:__init__
    #@+node:EKR.20040517080555.8:about
    def about(self,event=None):

        """Put information about this plugin in a scrolledMessage dialog."""

        g.app.gui.runScrolledMessageDialog(
            title="About Plugin ( " + self.name + " )",
            label="Version: " + self.version,
            msg=self.doc
        )

    #@-node:EKR.20040517080555.8:about
    #@+node:pap.20050317183526:getNiceName
    def getNiceName(self, name):
        """Return a nice version of the plugin name

        Historically some plugins had "at_" and "mod_" prefixes to their
        name which makes the name look a little ugly in the lists. There is
        no real reason why the majority of users need to know the underlying
        name so here we create a nice readable version.

        """
        lname = name.lower()
        if lname.startswith("at_"):
            name = name[3:]
        elif lname.startswith("mod_"):
            name = name[4:]
        return name.capitalize()
    #@-node:pap.20050317183526:getNiceName
    #@+node:EKR.20040517080555.9:properties
    def properties(self, event=None):
        """Display a modal properties dialog for this plugin"""


        if self.hasapply:

            def callback(name, data):
                self.updateConfiguration(data)
                self.mod.applyConfiguration(self.config)
                self.writeConfiguration()

            buttons = ['Apply']

        else:
            callback = None
            buttons = []

        self.config = config = ConfigParser.ConfigParser()
        config.read(self.configfilename)

        # Load config data into dictionary of dictianaries.
        # Do no allow for nesting of sections.

        data = {}

        for section in config.sections():
            options = {}
            for option in config.options(section):
                #print 'config', section, option 
                options[option] = unicode(config.get(section,option))
            data[section] = options

        # Save the original config data. This will not be changed.

        self.sourceConfig = data

        # Open a modal dialog and wait for it to return.
        # Provide the dialog with a callback for the 'Appply' function.

        title = "Properties of " + self.name

        result, data = g.app.gui.runPropertiesDialog(title, data, callback, buttons)

        if result != 'Cancel' and data:
            self.updateConfiguration(data)
            self.writeConfiguration()

    #@-node:EKR.20040517080555.9:properties
    #@+node:bob.20071209102050:updateConfiguration
    def updateConfiguration(self, data):
        """Update the config object from the dialog 'data' structure"""

        # Should we clear the config object first?


        for section in data.keys():
            for option in data[section].keys():
                self.config.set(section, option, data[section][option])
    #@-node:bob.20071209102050:updateConfiguration
    #@+node:bob.20071208033759:writeConfiguration
    def writeConfiguration(self):
        """Write the configuration to a file."""

        f = open(self.configfilename, "w")
        try:
            self.config.write(f)
        except:
            f.close()
    #@-node:bob.20071208033759:writeConfiguration
    #@+node:pap.20051011215345:niceMenuName
    def niceMenuName(self, name):
        """Return a nice version of the command name for the menu

        The command will be of the form::

            cmd_ThisIsIt

        We want to convert this to "This Is It".

        """
        text = ""
        for char in name[4:]:
            if char.isupper() and text:
                text += " "
            text += char
        return text
    #@nonl
    #@-node:pap.20051011215345:niceMenuName
    #@-others

#@-node:EKR.20040517080555.3:class Plugin
#@+node:EKR.20040517080555.10:class TkPropertiesDialog
class TkPropertiesDialog:

    """A class to create and run a Properties dialog"""

    #@    @+others
    #@+node:bob.20071208030419:__init__
    def __init__(self, title, data, callback=None, buttons=[]):
        #@    << docstring >>
        #@+node:bob.20071208211442:<< docstring >>
        """ Initialize and show a Properties dialog.

            'buttons' should be a list of names for buttons.

            'callback' should be None or a function of the form:

                def cb(name, data)
                    ...
                    return 'close' # or anything other than 'close'

            where name is the name of the button clicked and data is
            a data structure representing the current state of the dialog.

            If a callback is provided then when a button (other than
            'OK' or 'Cancel') is clicked then the callback will be called
            with name and data as parameters.

                If the literal string 'close' is returned from the callback
                the dialog will be closed and self.result will be set to a
                tuple (button, data).

                If anything other than the literal string 'close' is returned
                from the callback, the dialog will continue to be displayed.

            If no callback is provided then when a button is clicked the
            dialog will be closed and self.result set to  (button, data).

            The 'ok' and 'cancel' buttons (which are always provided) behave as
            if no callback was supplied.

        """
        #@-node:bob.20071208211442:<< docstring >>
        #@nl

        if buttons is None:
            buttons = []

        self.entries = []
        self.title = title
        self.callback = callback
        self.buttons = buttons
        self.data = data

        #@    << create the frame from the configuration data >>
        #@+node:bob.20071208030419.2:<< Create the frame from the configuration data >>
        root = g.app.root

        #@<< Create the top level and the main frame >>
        #@+node:bob.20071208030419.3:<< Create the top level and the main frame >>
        self.top = top = Tk.Toplevel(root)
        g.app.gui.attachLeoIcon(self.top)
        #top.title("Properties of "+ plugin.name)
        top.title(title)

        top.resizable(0,0) # neither height or width is resizable.

        self.frame = frame = Tk.Frame(top)
        frame.pack(side="top")
        #@nonl
        #@-node:bob.20071208030419.3:<< Create the top level and the main frame >>
        #@nl
        #@<< Create widgets for each section and option >>
        #@+node:bob.20071208030419.4:<< Create widgets for each section and option >>
        # Create all the entry boxes on the screen to allow the user to edit the properties

        sections = data.keys()
        sections.sort()

        for section in sections:

            # Create a frame for the section.
            f = Tk.Frame(top, relief="groove",bd=2)
            f.pack(side="top",padx=5,pady=5)
            Tk.Label(f, text=section.capitalize()).pack(side="top")

            # Create an inner frame for the options.
            b = Tk.Frame(f)
            b.pack(side="top",padx=2,pady=2)

            options = data[section].keys()
            options.sort()

            row = 0
            # Create a Tk.Label and Tk.Entry for each option.
            for option in options:
                e = Tk.Entry(b)
                e.insert(0, data[section][option])
                Tk.Label(b, text=option).grid(row=row, column=0, sticky="e", pady=4)
                e.grid(row=row, column=1, sticky="ew", pady = 4)
                row += 1
                self.entries.append((section, option, e))
        #@-node:bob.20071208030419.4:<< Create widgets for each section and option >>
        #@nl
        #@<< Create the buttons >>
        #@+node:bob.20071208030419.5:<< Create the buttons >>
        box = Tk.Frame(top, borderwidth=5)
        box.pack(side="bottom")

        buttons.extend(("OK", "Cancel"))

        for name in buttons:
            Tk.Button(box,
                text=name,
                width=6,
                command=lambda self=self, name=name: self.onButton(name)
            ).pack(side="left",padx=5)

        #@-node:bob.20071208030419.5:<< Create the buttons >>
        #@nl

        g.app.gui.center_dialog(top) # Do this after packing.
        top.grab_set() # Make the dialog a modal dialog.
        top.focus_force() # Get all keystrokes.

        self.result = ('Cancel', '')

        root.wait_window(top)
        #@nonl
        #@-node:bob.20071208030419.2:<< Create the frame from the configuration data >>
        #@nl
    #@nonl
    #@-node:bob.20071208030419:__init__
    #@+node:EKR.20040517080555.17:Event Handlers

    def onButton(self, name):
        """Event handler for all button clicks."""

        data = self.getData()
        self.result = (name, data)

        if name in ('OK', 'Cancel'):
            self.top.destroy()
            return

        if self.callback:
            retval = self.callback(name, data)
            if retval == 'close':
                self.top.destroy()
            else:
                self.result = ('Cancel', None)


    #@-node:EKR.20040517080555.17:Event Handlers
    #@+node:EKR.20040517080555.18:getData
    def getData(self):
        """Return the modified configuration."""

        data = {}
        for section, option, entry in self.entries:
            if section not in data:
                data[section] = {}
            s = entry.get()
            s = g.toEncodedString(s,"ascii",reportErrors=True) # Config params had better be ascii.
            data[section][option] = s

        return data


    #@-node:EKR.20040517080555.18:getData
    #@-others
#@nonl
#@-node:EKR.20040517080555.10:class TkPropertiesDialog
#@+node:EKR.20040517080555.19:class TkScrolledMessageDialog
class TkScrolledMessageDialog:

    """A class to create and run a Scrolled Message dialog for Tk"""

    #@    @+others
    #@+node:EKR.20040517080555.20:__init__
    def __init__(self, title='Message', label= '', msg='', callback=None, buttons=None):

        """Create and run a modal dialog showing 'msg' in a scrollable window."""

        if buttons is None:
            buttons = []

        self.result = ('Cancel', None)

        root = g.app.root
        self.top = top = Tk.Toplevel(root)
        g.app.gui.attachLeoIcon(self.top)
        top.title(title)
        top.resizable(0,0) # neither height or width is resizable.

        frame = Tk.Frame(top)
        frame.pack(side="top")
        #@    << Create the contents of the about box >>
        #@+node:EKR.20040517080555.21:<< Create the contents of the about box >>
        #Tk.Label(frame,text="Version " + version).pack()

        if label:
            Tk.Label(frame, text=label).pack()

        body = w = g.app.gui.plainTextWidget(
            frame,name='body-pane',
            bd=2,bg="white",relief="flat",setgrid=0,wrap='word')
        w.insert(0,msg)
        if 0: # prevents arrow keys from being visible.
            w.configure(state='disabled')
        w.setInsertPoint(0)
        w.see(0)

        bodyBar = Tk.Scrollbar(frame,name='bodyBar')
        body['yscrollcommand'] = bodyBar.set
        bodyBar['command'] = body.yview

        bodyBar.pack(side="right", fill="y")
        body.pack(expand=1,fill="both")

        def destroyCallback(event=None,top=top):
            self.result = ('Cancel', None)
            top.destroy()

        body.bind('<Return>',destroyCallback)

        g.app.gui.set_focus(None,body)
        #@nonl
        #@-node:EKR.20040517080555.21:<< Create the contents of the about box >>
        #@nl
        #@    << Create the buttons >>
        #@+node:EKR.20040517080555.22:<< Create the buttons >>

        box = Tk.Frame(top, borderwidth=5)
        box.pack(side="bottom")

        buttons.append("Close")

        for name in buttons:
            Tk.Button(box,
                text=name,
                width=6,
                command=lambda self=self, name=name: self.onButton(name)
            ).pack(side="left",padx=5)
        #@nonl
        #@-node:EKR.20040517080555.22:<< Create the buttons >>
        #@nl

        g.app.gui.center_dialog(top) # Do this after packing.
        top.grab_set() # Make the dialog a modal dialog.
        top.focus_force() # Get all keystrokes.

        root.wait_window(top)
    #@nonl
    #@-node:EKR.20040517080555.20:__init__
    #@+node:bob.20071209110304.1:Event Handlers

    def onButton(self, name):
        """Event handler for all button clicks."""


        if name in ('Close'):

            self.top.destroy()
            return

        if self.callback:
            retval = self.callback(name, data)
            if retval == 'close':
                self.top.destroy()
            else:
                self.result = ('Cancel', None)


    #@-node:bob.20071209110304.1:Event Handlers
    #@-others
#@-node:EKR.20040517080555.19:class TkScrolledMessageDialog
#@+node:bob.20071208211442.1:runPropertiesDialog
def runPropertiesDialog(title='Properties', data={}, callback=None, buttons=None):
    """Dispay a modal TkPropertiesDialog"""


    dialog = TkPropertiesDialog(title, data, callback, buttons)

    return dialog.result 
#@-node:bob.20071208211442.1:runPropertiesDialog
#@+node:bob.20071209110304:runScrolledMessageDialog
def runScrolledMessageDialog(title='Message', label= '', msg='', callback=None, buttons=None):
    """Display a modal TkScrolledMessageDialog."""


    dialog = TkScrolledMessageDialog(title, label, msg, callback, buttons)

    return dialog.result
#@-node:bob.20071209110304:runScrolledMessageDialog
#@-others
#@-node:EKR.20040517080555.2:@thin plugins_menu.py
#@-leo
