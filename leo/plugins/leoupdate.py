#@+leo-ver=4-thin
#@+node:pap.20050605183206:@thin leoupdate.py
#@<< docstring >>
#@+node:pap.20050605183206.1:<< docstring >>
"""

A plugin to automatically update Leo from the current CVS version
of the code stored on the SourceForge site. You can view individual
files and update your entire Leo installation directly without needing
a CVS client.

"""
#@-node:pap.20050605183206.1:<< docstring >>
#@nl

#@@language python
#@@tabwidth -4

__version__ = "0.1"
__plugin_name__ = "Leo Update"
__plugin_priority__ = 100
__plugin_group__ = "Core"
__plugin_requires__ = ["plugin_manager"]

#@<< imports >>
#@+node:pap.20050605183206.2:<< imports >>
import leoGlobals as g
import leoPlugins
import re
import sys
import glob

Tk   = g.importExtension('Tkinter',pluginName=__name__,verbose=True)
sets = g.importExtension('sets',pluginName=__name__,verbose=True)
#@nonl
#@-node:pap.20050605183206.2:<< imports >>
#@nl

#@<< version history >>
#@+node:pap.20050605183206.3:<< version history >>
#@@killcolor
#@+at
# 
# 0.1 Paul Paterson:
#     - Initial version
#@-at
#@-node:pap.20050605183206.3:<< version history >>
#@nl
#@<< todo >>
#@+node:pap.20050605183206.4:<< todo >>
"""

Todo list:

- allow individual update
- specific versions?

Done:

- scan CVS for files
- allow block update

"""
#@-node:pap.20050605183206.4:<< todo >>
#@nl

#@+others
#@+node:pap.20050605183206.5:Error Classes
class LeoUpdateError(Exception):
    """Something went wrong with the update"""
    
#@-node:pap.20050605183206.5:Error Classes
#@+node:pap.20050605183206.6:init
def init():

    ok = Tk and sets

    if ok:
        if g.app.gui is None:
            g.app.createTkGui(__file__)
            
        ok = g.app.gui.guiName() == "tkinter"

        if ok:
            if 0: # Use this if you want to create the commander class before the frame is fully created.
                leoPlugins.registerHandler('before-create-leo-frame',onCreate)
            else: # Use this if you want to create the commander class after the frame is fully created.
                leoPlugins.registerHandler('after-create-leo-frame',onCreate)
            g.plugin_signon(__name__)
        else:
            g.es("autotrees requires Tkinter",color='blue')
              
    return ok
#@nonl
#@-node:pap.20050605183206.6:init
#@+node:pap.20050605183206.7:onCreate
def onCreate (tag, keys):
    
    c = keys.get('c')
    if not c: return
    
    global thePluginController
    thePluginController = LeoUpdater(c)
#@nonl
#@-node:pap.20050605183206.7:onCreate
#@+node:pap.20050605183206.8:topLevelMenu
# This is called from plugins_menu plugin.

def topLevelMenu():   
    """Manage the tree handlers"""
    global thePluginController    
    thePluginController.showManagerDialog()
#@nonl
#@-node:pap.20050605183206.8:topLevelMenu
#@+node:pap.20050605183206.17:class LeoUpdater
class LeoUpdater:
    
    #@    @+others
    #@+node:pap.20050605183206.18:__init__
    def __init__ (self,c):
        """Initialise the commander"""
        self.c = c
        # 
        # Get the manager
        try:
            self.plugin_manager = __import__("plugin_manager")
        except ImportError, err:
            g.es("LeoUpdate did not load plugin manager: %s" % (err,), color="red")
            self.plugin_manager = None
        
    #@nonl
    #@-node:pap.20050605183206.18:__init__
    #@+node:pap.20050605183206.27:showManagerDialog
    def showManagerDialog(self):
        """Show the tree handler manager dialog"""
        if not self.plugin_manager:
            g.es("Plugin manager could not be loaded", color="red")
        else:
            #
            # The manager class is defined as a dynamic class because
            # we don't know if we will be able to import the 
            # base class!
            #@        << class HandlerDialog >>
            #@+node:pap.20050605183206.28:<< class HandlerDialog >>
            class HandlerDialog(self.plugin_manager.ManagerDialog):
                """A dialog to manager leo files"""
                
                dialog_caption = "Leo File Manager"
            
                #@    @+others
                #@+node:pap.20050605184344:initLocalCollection
                def initLocalCollection(self):
                    """Initialize the local file collection"""
                
                    # Get the local plugins information
                    self.local = plugin_manager.LocalPluginCollection()
                    self.local.initFrom(self.local_path)
                
                #@-node:pap.20050605184344:initLocalCollection
                #@+node:pap.20050605183206.29:setPaths
                def setPaths(self):
                    """Set paths to the plugin locations"""
                    self.local_path = g.os_path_join(g.app.loadDir,"..","src")
                    self.remote_path = r"cvs.sourceforge.net/viewcvs.py/leo/leo/src"
                    self.file_text = "File"
                    self.has_enable_buttons = False
                    self.has_conflict_buttons = False
                    self.install_text = "Install all"
                #@nonl
                #@-node:pap.20050605183206.29:setPaths
                #@+node:pap.20050605192322.1:installPlugin
                def installPlugin(self):
                    """Install all the files"""
                
                    # Write the files
                    for plugin in self.remote_plugin_list.getAllPlugins():     
                        self.messagebar.message("busy", "Writing file '%s'" % plugin.name)
                        plugin.writeTo(self.local_path)
                        plugin.enabled = "Up to date"
                        
                    self.messagebar.message("busy", "Scanning local files") 
                    # Go and check local filesystem for all plugins   
                    self.initLocalCollection()
                    # View is still pointing to the old list, so switch it now
                    self.plugin_list.plugins = self.local
                    self.plugin_list.populateList()
                    # Update the current list too
                    self.remote_plugin_list.populateList()
                    self.messagebar.resetmessages('busy')
                
                #@-node:pap.20050605192322.1:installPlugin
                #@-others
            #@nonl
            #@-node:pap.20050605183206.28:<< class HandlerDialog >>
            #@nl
            plugin_manager = self.plugin_manager
            dlg = HandlerDialog()    
    #@-node:pap.20050605183206.27:showManagerDialog
    #@-others
#@nonl
#@-node:pap.20050605183206.17:class LeoUpdater
#@-others

#@-node:pap.20050605183206:@thin leoupdate.py
#@-leo
