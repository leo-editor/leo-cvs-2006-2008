#@+leo-ver=4-thin
#@+node:ekr.20060328125248:@thin mod_scripting.py
#@<< docstring >>
#@+node:ekr.20060328125248.1:<< docstring >>
"""A plugin to create script buttons and @button, @command, @plugin and @script
nodes.

This plugin puts buttons in the icon area. Depending on settings the plugin will
create the 'Run Script', the 'Script Button' and the 'Debug Script' buttons.

The 'Run Script' button is simply another way of doing the Execute Script
command: it executes the selected text of the presently selected node, or the
entire text if no text is selected.

The 'Script Button' button creates *another* button in the icon area every time
you push it. The name of the button is the headline of the presently selected
node. Hitting this *newly created* button executes the button's script.

For example, to run a script on any part of an outline do the following:

1.  Select the node containing the script.
2.  Press the scriptButton button.  This will create a new button.
3.  Select the node on which you want to run the script.
4.  Push the *new* button.

That's all.

For every @button node, this plugin creates two new minibuffer commands: x and
delete-x-button, where x is the 'cleaned' name of the button. The 'x' command is
equivalent to pushing the script button.

The cleaned name of an @button node is the headline text of the button with:
    
- Leading @button or @command removed,
- @key and all following text removed, and
- all non-alphanumeric characters converted to a single '-' characters.

Thus, cleaning headline text converts it to a valid minibuffer command name.

You can delete a script button by right-clicking on it, or by
executing the delete-x-button command.

The 'Debug Script' button runs a script using an external debugger.

This plugin optionally scans for @button nodes, @command, @plugin nodes and
@script nodes whenever a .leo file is opened.

- @button nodes create script buttons.
- @command nodes create minibuffer commands.
- @plugin nodes cause plugins to be loaded.
- @script nodes cause a script to be executed when opening a .leo file.

Such nodes may be security risks. This plugin scans for such nodes only if the
corresponding atButtonNodes, atPluginNodes, and atScriptNodes constants are set
to True in this plugin.

You can specify the following options in leoSettings.leo.  See the node:
@settings-->Plugins-->scripting plugin.  Recommended defaults are shown.

- @bool scripting-at-button-nodes = True
  True: adds a button for every @button node.

- @bool scripting-at-commands-nodes = True
  True: define a minibuffer command for every @command node.

- @bool scripting-at-plugin-nodes = False
  True: dynamically loads plugins in @plugins nodes when a window is created.

- @bool scripting-at-script-nodes = False
  True: dynamically executes script in @script nodes when a window is created.  DANGEROUS!

- @bool scripting-create-debug-button = False
  True: create Debug Script button.

- @bool scripting-create-run-script-button = False
  True: create Run Script button.
  Note: The plugin creates the press-run-script-button regardless of this setting.

- @bool scripting-create-script-button-button = True
  True: create Script Button button in icon area.
  Note: The plugin creates the press-script-button-button regardless of this setting.

- @int scripting-max-button-size = 18
  The maximum length of button names: longer names are truncated.

You can bind key shortcuts to @button and @command nodes as follows:

@button name @key=shortcut

This binds the shortcut to the script in the script button. The button's name is
'name', but you can see the full headline in the status line when you move the
mouse over the button.

@command name @key=shortcut

This creates a new minibuffer command and binds shortcut to it. As with @buffer
nodes, the name of the command is the cleaned name of the headline.

This plugin is based on ideas from e's dynabutton plugin, quite possibly the
most brilliant idea in Leo's history. """
#@nonl
#@-node:ekr.20060328125248.1:<< docstring >>
#@nl
#@<< imports >>
#@+node:ekr.20060328125248.2:<< imports >>
import leoGlobals as g
import leoPlugins

Tk  = g.importExtension('Tkinter',pluginName=__name__,verbose=True)
Pmw = g.importExtension('Pmw',pluginName=__name__,verbose=True)

import os
import string
import sys
#@nonl
#@-node:ekr.20060328125248.2:<< imports >>
#@nl

__version__ = '1.5'
#@<< version history >>
#@+node:ekr.20060328125248.3:<< version history >>
#@+at
# 
# 0.3 EKR: Don't mess with button sizes or fonts on MacOs/darwin
# 0.4 EKR: Added support for @button, @script and @plugin.
# 0.5 EKR: Added patch by Davide Salomoni: added start2 hook and related code.
# 0.5 EKR: Use g.importExtention to import Tk.
# 0.6.1 EKR: Improved docstring.
# 0.7 EKR:
# - Added support for 'removeMe' hack.
#     Buttons can asked to be removed by setting s.app.scriptDict['removeMe'] 
# = True.
# 0.8 EKR: c.disableCommandsMessage disables buttons.
# 0.9 EKR:
# - Added init, onCreate.
# - Created scriptingController class.
# 0.10 EKR: Changed 'new_c' logic to 'c' logic.
# 0.11 EKR:
# - Removed bindLate options: it should always be on.
# - Added support for:
#     - @button name [@key=shortcut]
#     - @command name [@key=shortcut]
# 0.12 EKR:
# - Use c.executeScript(p=p,silent=True) in @command so the
#   'end of script' message doesn't switch tabs.
# 0.13 EKR: Use set silent=True in all calls to c.executeScript except for the 
# 'Run Script' button.
# 0.14 EKR: All created buttons call bodyWantsFocus when the script completes.
# 0.15 EKR: Fixed a recent crasher in deleteButton.
# 0.16 EKR:
# - Removed the unused bindLate global.
# - Set silent=True in the Run Script callback.
# 0.17 EKR: Added calls to c.updateScreen.
# 0.18 EKR:
# - Removed calls to c.updateScreen and c.frame.bodyWantsFocus.
#   These calls would shift focus improperly when opening a new window.
# 0.19 btheado: Refactored the code in scriptingController to remove 
# duplication.
# 0.20 EKR: converted to @thin.
# 0.21 EKR: Added Debug button & balloons.
# 0.22 EKR: Created leoScriptModule for use by the debugger and Debug Script 
# button.
# 0.23 EKR: Creating a script button creates the press-xxx-button command,
#           and you can specify settings for such commands using @shortcuts 
# nodes.
# 0.24 EKR: Use 'button' pane for bindings.
# 0.25 EKR:
# - Added createRunButton and createScriptButton option.
# - All standard buttons now create the corresponding press-x-button commands.
# - cleanButtonText removes leading @..@button and does various other 
# cleanings.
# 1.0 EKR: Use settigns in leoSettings.leo instead of hard-coded settings.
# 1.1 EKR: Updated docstring to reflect new settings.
# 1.2 EKR: Make sure balloon exists before binding to it.
# - cleanButtonText cleans less.  In particular, it retains interior --> and 
# <--.
# 1.3 EKR: Give up the attempt to use <-- and -->.
# LeoSlideShows.leo now minibuffer names for buttons, and defines those same 
# command.
# 1.4 EKR: Create a delete-x-button command for each button.
# 1.5 EKR: Reorganized and simplified much of the code, added many docstrings 
# and revised the plugin's docstring.
#@-at
#@nonl
#@-node:ekr.20060328125248.3:<< version history >>
#@nl

#@+others
#@+node:ekr.20060328125248.4:init
def init ():
    
    ok = Tk is not None # OK for unit tests.
    
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
#@-node:ekr.20060328125248.4:init
#@+node:ekr.20060328125248.5:onCreate
def onCreate (tag, keys):

    """Handle the onCreate event in the mod_scripting plugin."""
    
    c = keys.get('c')

    if c:
        sc = scriptingController(c)
        sc.createAllButtons()
#@nonl
#@-node:ekr.20060328125248.5:onCreate
#@+node:ekr.20060328125248.6:class scriptingController
class scriptingController:
    
    #@    @+others
    #@+node:ekr.20060328125248.7: ctor
    def __init__ (self,c,iconBar=None):
        
        self.c = c
        getBool = c.config.getBool
        self.scanned = False
        kind = c.config.getString('debugger_kind') or 'idle'
        self.buttonsDict = {} # Keys are buttons, values are button names (strings).
        self.debuggerKind = kind.lower()
        
        self.atButtonNodes = getBool('scripting-at-button-nodes')
            # True: adds a button for every @button node.
        self.atCommandsNodes = getBool('scripting-at-commands-nodes')
            # True: define a minibuffer command for every @command node.
        self.atPluginNodes = getBool('scripting-at-plugin-nodes')
            # True: dynamically loads plugins in @plugins nodes when a window is created.
        self.atScriptNodes = getBool('scripting-at-script-nodes')
            # True: dynamically executes script in @script nodes when a window is created.  DANGEROUS!
        self.createDebugButton = getBool('scripting-create-debug-button')
            # True: create Debug Script button.
        self.createRunScriptButton = getBool('scripting-create-run-script-button')
            # True: create Run Script button.
        self.createScriptButtonButton = getBool('scripting-create-script-button-button')
            # True: create Script Button button.
        self.maxButtonSize = c.config.getInt('scripting-max-button-size')
            # Maximum length of button names.
        
        if not iconBar:
            self.iconBar = c.frame.getIconBarObject()
        else:
            self.iconBar = iconBar
    #@nonl
    #@-node:ekr.20060328125248.7: ctor
    #@+node:ekr.20060328125248.8:createAllButtons & helpers
    def createAllButtons (self):
        
        '''Scans the outline looking for @button, @command, @plugin and @script nodes.'''
        
        c = self.c
    
        if not self.scanned: # Not really needed, but can't hurt.
            self.scanned = True
            if self.createRunScriptButton:
                self.createRunScriptIconButton()
            if self.createScriptButtonButton:
                self.createScriptButtonIconButton()
            if self.createDebugButton:
                self.createDebugIconButton()
    
            # scan for user-defined nodes.
            for p in c.allNodes_iter():
                if self.atButtonNodes and p.headString().startswith("@button"):
                    self.handleAtButtonNode(p)
                if self.atCommandsNodes and p.headString().startswith("@command"):
                    self.handleAtCommandNode(p)
                if self.atPluginNodes and p.headString().startswith("@plugin"):
                    self.handleAtPluginNode(p)
                if self.atScriptNodes and p.headString().startswith("@script"):
                    self.handleAtScriptNode(p)
    #@nonl
    #@+node:ekr.20060328125248.20:createRunScriptIconButton 'run-script' & callback
    def createRunScriptIconButton (self):
        
        '''Create the 'run-script' button and the run-script command.'''
    
        b = self.createIconButton(
            text='run-script',
            command = self.runScriptCommand,
            shortcut=None,
            statusLine='Run script in selected node',
            bg='MistyRose1')
        
        return b
    #@nonl
    #@+node:ekr.20060328125248.21:runScriptCommand
    def runScriptCommand (self,event=None):
        
        '''Called when user presses the 'run-script' button or executes the run-script command.'''
    
        c = self.c
        c.executeScript(c.currentPosition(),useSelectedText=True,silent=True)
        
        if 0:
            # Do not assume the script will want to remain in this commander.
            c.frame.bodyWantsFocus()
    #@nonl
    #@-node:ekr.20060328125248.21:runScriptCommand
    #@-node:ekr.20060328125248.20:createRunScriptIconButton 'run-script' & callback
    #@+node:ekr.20060522105937:createDebugIconButton 'debug-script' & callback
    def createDebugIconButton (self):
        
        '''Create the 'debug-script' button and the debug-script command.'''
    
        b = self.createIconButton(
            text='debug-script',
            command=self.runDebugScriptCommand,
            shortcut=None,
            statusLine='Debug script in selected node',
            bg='MistyRose1')
       
        return b
    #@nonl
    #@+node:ekr.20060522105937.1:runDebugScriptCommand
    def runDebugScriptCommand (self,event=None):
        
        '''Called when user presses the 'debug-script' button or executes the debug-script command.'''
    
        c = self.c ; p = c.currentPosition()
        
        script = g.getScript(c,p,useSelectedText=True,useSentinels=False)
        if script:
            #@        << set debugging if debugger is active >>
            #@+node:ekr.20060523084441:<< set debugging if debugger is active >>
            g.trace(self.debuggerKind)
            
            if self.debuggerKind == 'winpdb':
                try:
                    import rpdb2
                    debugging = rpdb2.g_debugger is not None
                except ImportError:
                    debugging = False
            elif self.debuggerKind == 'idle':
                # import idlelib.Debugger.py as Debugger
                # debugging = Debugger.interacting
                debugging = True #######
            else:
                debugging = False
            #@nonl
            #@-node:ekr.20060523084441:<< set debugging if debugger is active >>
            #@nl
            if debugging:
                #@            << create leoScriptModule >>
                #@+node:ekr.20060524073716:<< create leoScriptModule >>
                target = g.os_path_join(g.app.loadDir,'leoScriptModule.py')
                f = None
                try:
                    f = file(target,'w')
                    f.write('# A module holding the script to be debugged.\n')
                    if self.debuggerKind == 'idle':
                        # This works, but uses the lame pdb debugger.
                        f.write('import pdb\n')
                        f.write('pdb.set_trace() # Hard breakpoint.\n')
                    elif self.debuggerKind == 'winpdb':
                        f.write('import rpdb2\n')
                        f.write('if rpdb2.g_debugger is not None: # don\'t hang if the debugger isn\'t running.\n')
                        f.write('  rpdb2.start_embedded_debugger(pwd="",fAllowUnencrypted=True) # Hard breakpoint.\n')
                    # f.write('# Remove all previous variables.\n')
                    f.write('# Predefine c, g and p.\n')
                    f.write('import leoGlobals as g\n')
                    f.write('c = g.app.scriptDict.get("c")\n')
                    f.write('p = c.currentPosition()\n')
                    f.write('# Actual script starts here.\n')
                    f.write(script + '\n')
                finally:
                    if f: f.close()
                #@nonl
                #@-node:ekr.20060524073716:<< create leoScriptModule >>
                #@nl
                g.app.scriptDict ['c'] = c
                if 'leoScriptModule' in sys.modules.keys():
                    del sys.modules ['leoScriptModule'] # Essential.
                import leoScriptModule      
            else:
                g.es('No debugger active',color='blue')
        
        c.frame.bodyWantsFocus()
    #@nonl
    #@-node:ekr.20060522105937.1:runDebugScriptCommand
    #@-node:ekr.20060522105937:createDebugIconButton 'debug-script' & callback
    #@+node:ekr.20060328125248.22:createScriptButtonIconButton 'script-button' & callback
    def createScriptButtonIconButton (self):
        
        '''Create the 'script-button' button and the script-button command.'''
        
        b = self.createIconButton(
            'script-button',
            command = self.addScriptButtonCommand,
            shortcut=None,
            statusLine='Make script button from selected node',
            bg="#ffffcc")
    
        return b
    #@nonl
    #@+node:ekr.20060328125248.23:addScriptButtonCommand
    def addScriptButtonCommand (self,event=None):
        
        '''Called when the user presses the 'script-button' button or executes the script-button command.'''
    
        c = self.c ; p = c.currentPosition(); h = p.headString()
        buttonText = self.getButtonText(h)
        shortcut = self.getShortcut(h)
        statusLine = "Run Script: %s" % buttonText
        if shortcut:
            statusLine = statusLine + " @key=" + shortcut
        b = self.createAtButtonHelper(p,buttonText,statusLine,shortcut,'MistyRose1')
        c.frame.bodyWantsFocus()
    #@nonl
    #@-node:ekr.20060328125248.23:addScriptButtonCommand
    #@-node:ekr.20060328125248.22:createScriptButtonIconButton 'script-button' & callback
    #@+node:ekr.20060328125248.12:handleAtButtonNode @button
    def handleAtButtonNode (self,p):
        
        '''Create a button in the icon area for an @button node.
        
        An optional @key=shortcut defines a shortcut that is bound to the button's script.
        The @key=shortcut does not appear in the button's name, but
        it *does* appear in the statutus line shown when the mouse moves over the button.'''
    
        c = self.c ; h = p.headString()
        buttonText = self.getButtonText(h)
        shortcut = self.getShortcut(h)
        statusLine = shortcut and " @key=" + shortcut or 'Script button'
        
        # This helper is also called by the script-button callback.
        b = self.createAtButtonHelper(p,buttonText,statusLine,shortcut)
    #@-node:ekr.20060328125248.12:handleAtButtonNode @button
    #@+node:ekr.20060328125248.10:handleAtCommandNode @command
    def handleAtCommandNode (self,p):
        
        '''Handle @command name [@key[=]shortcut].'''
        
        c = self.c ; k = c.keyHandler ; h = p.headString()
        if not h.strip(): return
        
        #@    << get the commandName and optional shortcut >>
        #@+node:ekr.20060328125248.11:<< get the commandName and optional shortcut >>
        tag = '@command' ; shortcut = None
        
        i = h.find('@key')
        if i > -1:
            commandName = h[len(tag):i].strip()
            j = g.skip_ws(h,i+len('@key'))
            if g.match(h,j,'='): # Make the equal sign optional.
                j += 1
            shortcut = h[j:].strip()
        else:
            commandName = h[len(tag):].strip()
        #@nonl
        #@-node:ekr.20060328125248.11:<< get the commandName and optional shortcut >>
        #@nl
    
        def atCommandCallback (event=None,c=c,p=p.copy()):
            # The 'end-of-script command messes up tabs.
            c.executeScript(p=p,silent=True)
    
        k.registerCommand(commandName,shortcut,atCommandCallback,verbose=True)
    #@nonl
    #@-node:ekr.20060328125248.10:handleAtCommandNode @command
    #@+node:ekr.20060328125248.13:handleAtPluginNode @plugin
    def handleAtPluginNode (self,p):
        
        '''Handle @plugin nodes.'''
            
        c = self.c
        tag = "@plugin"
        h = p.headString()
        assert(g.match(h,0,tag))
        
        # Get the name of the module.
        theFile = h[len(tag):].strip()
        if theFile[-3:] == ".py":
            theFile = theFile[:-3]
        theFile = g.toUnicode(theFile,g.app.tkEncoding)
        
        if not self.atPluginNodes:
            g.es("disabled @plugin: %s" % (theFile),color="blue")
        elif theFile in g.app.loadedPlugins:
            g.es("plugin already loaded: %s" % (theFile),color="blue")
        else:
            plugins_path = g.os_path_join(g.app.loadDir,"..","plugins")
            theModule = g.importFromPath(theFile,plugins_path,
                pluginName=__name__,verbose=False)
            if theModule:
                g.es("plugin loaded: %s" % (theFile),color="blue")
                g.app.loadedPlugins.append(theFile)
            else:
                g.es("can not load plugin: %s" % (theFile),color="blue")
    #@nonl
    #@-node:ekr.20060328125248.13:handleAtPluginNode @plugin
    #@+node:ekr.20060328125248.14:handleAtScriptNode @script
    def handleAtScriptNode (self,p):
        
        '''Handle @script nodes.'''
        
        c = self.c
        tag = "@script"
        h = p.headString()
        assert(g.match(h,0,tag))
        name = h[len(tag):].strip()
    
        if self.atPluginNodes:
            g.es("executing script %s" % (name),color="blue")
            c.executeScript(p,useSelectedText=False,silent=True)
        else:
            g.es("disabled @script: %s" % (name),color="blue")
    
        if 0:
            # Do not assume the script will want to remain in this commander.
            c.frame.bodyWantsFocus()
    #@nonl
    #@-node:ekr.20060328125248.14:handleAtScriptNode @script
    #@-node:ekr.20060328125248.8:createAllButtons & helpers
    #@+node:ekr.20061014075212:Utils
    #@+node:ekr.20060929135558:cleanButtonText
    def cleanButtonText (self,s):
        
        '''Clean the text following @button or @command so that it is a valid name of a minibuffer command.'''
        
        # Strip @...@button.
        while s.startswith('@'):
            s = s[1:]
        if s.startswith('button'):
            s = s[6:]
        if 1: # Not great, but spaces, etc. interfere with tab completion.
            chars = g.toUnicode(string.letters + string.digits,g.app.tkEncoding)
            aList = [g.choose(ch in chars,ch,'-') for ch in g.toUnicode(s,g.app.tkEncoding)]
            s = ''.join(aList)
            s = s.replace('--','-')
        while s.startswith('-'):
            s = s[1:]
        while s.endswith('-'):
            s = s[:-1]
        return s
    #@nonl
    #@-node:ekr.20060929135558:cleanButtonText
    #@+node:ekr.20060328125248.24:createAtButtonHelper & callback
    def createAtButtonHelper (self,p,buttonText,statusLine,shortcut,bg='LightSteelBlue1'):
        
        '''Create a button from an @button node.
        
        - Calls createIconButton to do all standard button creation tasks.
        - Binds button presses to a callback that executes the script in node p.
        '''
        c = self.c ; k = c.k
        buttonText = self.cleanButtonText(buttonText)
        
        # We must define the callback *after* defining b, so set both command and shortcut to None here.
        b = self.createIconButton(text=buttonText,command=None,shortcut=None,statusLine=statusLine,bg=bg)
        
        # Now that b is defined we can define the callback.
        # Yes, executeScriptFromButton *does* use b (to delete b if requested by the script).
        def atButtonCallback (event=None,self=self,p=p.copy(),b=b,buttonText=buttonText):
            self.executeScriptFromButton (p,b,buttonText)
        b.configure(command=atButtonCallback)
        
        # At last we can define the command and use the shortcut.
        k.registerCommand(buttonText,shortcut=shortcut,func=atButtonCallback,pane='button',verbose=shortcut)
       
        return b
    #@nonl
    #@+node:ekr.20060328125248.28:executeScriptFromButton
    def executeScriptFromButton (self,p,b,buttonText):
        
        '''Called from callbacks to execute the script in node p.'''
        
        c = self.c
    
        if c.disableCommandsMessage:
            g.es(c.disableCommandsMessage,color='blue')
        else:
            g.app.scriptDict = {}
            c.executeScript(p=p,silent=True)
            # Remove the button if the script asks to be removed.
            if g.app.scriptDict.get('removeMe'):
                g.es("Removing '%s' button at its request" % buttonText)
                self.deleteButton(b)
    
        if 0: # Do *not* set focus here: the script may have changed the focus.
            c.frame.bodyWantsFocus()
    #@nonl
    #@-node:ekr.20060328125248.28:executeScriptFromButton
    #@-node:ekr.20060328125248.24:createAtButtonHelper & callback
    #@+node:ekr.20060328125248.17:createIconButton & helpers
    def createIconButton (self,text,command,shortcut,statusLine,bg):
        
        '''Create an icon button.  All icon buttons get created using this utility.
        
        - Creates the actual button and its balloon.
        - Adds the button to buttonsDict.
        - Registers command with the shortcut.
        - Creates x amd delete-x-button commands, where x is the cleaned button name.
        - Binds a right-click in the button to a callback that deletes the button.'''
        
        c = self.c ; k = c.k
        
        # Create the button and add it to the buttons dict.
        buttonText = self.cleanButtonText(text).lower()
        
        # Truncate only the text of the button, not the command name.
        b = self.iconBar.add(text=buttonText[:self.maxButtonSize])
        self.buttonsDict[b] = buttonText
        
        if statusLine:
            self.createBalloon(b,statusLine)
    
        if sys.platform == "win32":
            width = int(min(self.maxButtonSize,len(text)) * 0.9)
            b.configure(width=width,font=('verdana',7,'bold'),bg=bg)
            
        # Register the command name if it exists.
        if command:
            b.configure(command=command)
            k.registerCommand(buttonText,shortcut=shortcut,func=command,pane='button',verbose=shortcut)
        
        # Bind right-clicks to deleteButton.
        def deleteButtonCallback(event=None,self=self,b=b):
            self.deleteButton(b)
        b.bind('<3>',deleteButtonCallback)
        
        # Register the delete-x-button command
        deleteCommandName= 'delete-%s-button' % buttonText
        k.registerCommand(deleteCommandName,shortcut=None,func=deleteButtonCallback,pane='button',verbose=False)
            # Reporting this command is way too annoying.
    
        return b
    #@nonl
    #@+node:ekr.20060522104419.1:createBalloon
    def createBalloon (self,w,label):
    
        'Create a balloon for a widget.'
    
        balloon = Pmw.Balloon(w,initwait=100)
        if balloon:
            balloon.bind(w,label)
    #@nonl
    #@-node:ekr.20060522104419.1:createBalloon
    #@-node:ekr.20060328125248.17:createIconButton & helpers
    #@+node:ekr.20060929131245:definePressButtonCommand (no longer used)
    def definePressButtonCommand (self,buttonText,atButtonCallback,shortcut=None):
        
        '''Define the press-x-button command, were x is the cleaned button text.
        
        Called to create the run-script, script-button and debug-script buttons.'''
    
        # This will use any shortcut defined in an @shortcuts node if no shortcut is defined.
        
        # New in Leo 4.4.2: Just use the (cleaned) name of the button text
        c = self.c ; k = c.k
        buttonText = self.cleanButtonText(buttonText).lower()
    
        # if shortcut: shortcut = k.canonicalizeShortcut(shortcut)
    
        k.registerCommand(buttonText,shortcut=shortcut,func=atButtonCallback,pane='button',verbose=shortcut)
    #@-node:ekr.20060929131245:definePressButtonCommand (no longer used)
    #@+node:ekr.20060328125248.26:deleteButton
    def deleteButton(self,button):
        
        """Delete the given button.
        This is called from callbacks, it is not a callback."""
    
        if button and self.buttonsDict.get(button):
            del self.buttonsDict[button]
            button.pack_forget()
            button.destroy() # So that Pmw doesn't crash later.
            self.c.bodyWantsFocusNow()
    #@nonl
    #@-node:ekr.20060328125248.26:deleteButton
    #@+node:ekr.20060328125248.15:getButtonText
    def getButtonText(self,h):
        
        '''Returns the button text found in the given headline string'''
        
        tag = "@button"
        if h.startswith(tag):
            h = h[len(tag):].strip()
        
        i = h.find('@key')
    
        if i > -1:
            buttonText = h[:i].strip()
        
        else:
            buttonText = h
        
        fullButtonText = buttonText
        return buttonText
    #@nonl
    #@-node:ekr.20060328125248.15:getButtonText
    #@+node:ekr.20060328125248.16:getShortcut
    def getShortcut(self,h):
        
        '''Returns the keyboard shortcut from the given headline string'''
        
        shortcut = None
        i = h.find('@key')
    
        if i > -1:
            j = g.skip_ws(h,i+len('@key'))
            if g.match(h,j,'='):
                shortcut = h[j+1:].strip()
    
        return shortcut
    #@nonl
    #@-node:ekr.20060328125248.16:getShortcut
    #@-node:ekr.20061014075212:Utils
    #@-others
#@nonl
#@-node:ekr.20060328125248.6:class scriptingController
#@-others
#@nonl
#@-node:ekr.20060328125248:@thin mod_scripting.py
#@-leo
