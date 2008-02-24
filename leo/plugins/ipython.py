# -*- coding: utf-8 -*-
#@+leo-ver=4-thin
#@+node:ekr.20080201143145:@thin ipython.py
#@@first

#@<< docstring >>
#@+node:ekr.20080201151802:<< docstring >>
''' The ipython plugin provides two-way communication (a bridge) between Leo
scripts and IPython running in the console from which Leo was launched.

Using this bridge, scripts running in Leo can affect IPython, and vice versa.
In particular, scripts running in IPython can alter Leo outlines!

There are too many details to cover in this docstring.  For full details,
see: LeoDocs.leo or http://webpages.charter.net/edreamleo/IPythonBridge.html
'''
#@-node:ekr.20080201151802:<< docstring >>
#@nl

__version__ = '0.7'
#@<< version history >>
#@+node:ekr.20080201143145.2:<< version history >>
#@@killcolor
#@+at
# 
# v 0.1: Ideas by Ville M. Vainio, code by EKR.
# 
# v 0.2 EKR: Use g.getScript to synthesize scripts.
# 
# v 0.3 EKR:
# - Moved all code from scripts to this plugin.
# - Added leoInterface and leoInterfaceResults classes.
# - Added createNode function for use by the interface classes.
# - Created minibuffer commands.
# - c.ipythonController is now an official ivar.
# - Docstring now references Chapter 21 of Leo's Users Guide.
# 
# v 0.4 EKR:
# - Disable the command lockout logic for the start-ipython command.
# - (In leoSettings.leo): add shortcuts for ipython commands.
# - The init top-level function now requires the tkinter gui.
# 
# v 0.5 VMV & EKR:  Added leoInterfaceResults.__getattr__.
# 
# v 0.6 EKR:
# - Inject leox into the user_ns in start-ipython.
#   As a result, there is no need for init_ipython and it has been removed.
# 
# v 0.7 EKR:
# - changed execute-ipython-script to push-to-ipython.
# - Disabled trace of script in push-to-ipython.
#@-at
#@-node:ekr.20080201143145.2:<< version history >>
#@nl
#@<< to do >>
#@+node:ekr.20080203092534:<< to do >>
#@@nocolor
#@+at
# 
# - Read the docs re saving and restoring the IPython namespace.
# 
# - Is it possible to start IPShellEmbed automatically?
# 
#     Calling IPShellEmbed.ipshell() blocks, so it can't be done
#     outside the event loop.  It might be possible to do this in
#     an idle-time handler.
# 
#     If it is possible several more settings would be possible.
#@-at
#@nonl
#@-node:ekr.20080203092534:<< to do >>
#@nl
#@<< imports >>
#@+node:ekr.20080201143145.3:<< imports >>
import leoGlobals as g
import leoPlugins

import sys

import_ok = True

try:
    import Tkinter as Tk
except ImportError:
    g.es_print('ipython plugin: can not Tkinter',color='red')
    import_ok = False

try:
    import IPython.ipapi
except ImportError:
    g.es_print('ipython plugin: can not import IPython.ipapi',color='red')
    import_ok = False

try:
    from IPython.Shell import IPShellEmbed
except ImportError:
    g.es_print('ipython plugin: can not import IPython.Shell.IPShellEmbed')
    import_ok = False

#@-node:ekr.20080201143145.3:<< imports >>
#@nl

# Globals
gIPythonStarted = False # True: the start-ipythoncommand has been run.

#@+others
#@+node:ekr.20080201144219:Module-level functions
#@+node:ekr.20080201143145.4:init
def init ():

    if not import_ok: return

    # This plugin depends on the properties of the Tk event loop.
    # It may work for other gui's, but this is not guaranteed.
    if g.app.gui is None:
        g.app.createTkGui(__file__)

    ok = g.app.gui.guiName() == "tkinter"
    if ok:

        # Call onCreate after the commander and the key handler exist.
        leoPlugins.registerHandler('after-create-leo-frame',onCreate)
        g.plugin_signon(__name__)

    return ok
#@-node:ekr.20080201143145.4:init
#@+node:ekr.20080201143145.5:onCreate
def onCreate (tag, keys):

    c = keys.get('c')

    if c:
        # Inject the controller into the commander.
        c.ipythonController = ipythonController(c)
#@-node:ekr.20080201143145.5:onCreate
#@-node:ekr.20080201144219:Module-level functions
#@+node:ekr.20080201143145.6:class ipythonController
class ipythonController:

    '''A per-commander controller that manages the
    singleton IPython ipshell instance.'''

    #@    @+others
    #@+node:ekr.20080204110426:Birth
    #@+node:ekr.20080201143145.7:ctor
    def __init__ (self,c):

        self.c = c

        # Set by .startIPython...
        self.ip = None # The _ip var returned by ipshell.IP.getapi()

        self.createCommands()
    #@-node:ekr.20080201143145.7:ctor
    #@+node:ekr.20080204080848:createCommands
    def createCommands(self):

        '''Create all of the ipython plugin's minibuffer commands.'''

        c = self.c ; k = c.k

        table = (
            ('start-ipython',           self.startIPython),
            ('push-to-ipython',         self.pushToIPythonCommand),
        )

        shortcut = None
        for commandName,func in table:
            k.registerCommand (commandName,shortcut,func,pane='all',verbose=True)
    #@-node:ekr.20080204080848:createCommands
    #@-node:ekr.20080204110426:Birth
    #@+node:ekr.20080201151802.1:Commands
    #@+node:ekr.20080201143319.10:startIPython
    def startIPython(self,event=None):

        '''The start-ipython command'''

        c = self.c
        global gIPythonStarted
        try:
            import ipy_leo
        except ImportError:
            self.error("ipy_leo.py extension not available - upgrade your IPython!")
            return
        
        if gIPythonStarted:
            # if we are already running, just inject a new commander for current document
            
            leox = leoInterface(c,g) # inject leox into the namespace.
            ipy_leo.update_commander(leox)
            return

        try:


            api = IPython.ipapi
            self.message('creating IPython shell...')
            gIPythonStarted = True
            leox = leoInterface(c,g) # inject leox into the namespace.
            my_ns = { '_leo': leox }
            ses = api.make_session(my_ns)
            self.ip = ses.IP.getapi()
            ipy_leo_m = self.ip.load('ipy_leo')
            ipy_leo_m.update_commander(leox)

            c.inCommand = False # Disable the command lockout logic, just as for scripts.
            sys.argv = []
            ses.mainloop()
                # Does not return until IPython closes!
        except Exception:
            self.error('exception creating IPython shell')
            g.es_exception()
    #@-node:ekr.20080201143319.10:startIPython
    #@+node:ekr.20080204111314:pushToIPythonCommand
    def pushToIPythonCommand(self,event=None):

        '''The push-to-ipython command.

        IPython must be started, but need not be inited.'''

        self.pushToIPython(script=None)
    #@-node:ekr.20080204111314:pushToIPythonCommand
    #@-node:ekr.20080201151802.1:Commands
    #@+node:ekr.20080201151802.2:Utils...
    #@+node:ekr.20080204075924:error & message
    def error (self,s):

        g.es_print(s,color='red')

    def message (self,s):

        g.es_print(s,color='blue')
    #@-node:ekr.20080204075924:error & message
    #@+node:ekr.20080201150746.2:pushToIPython
    def pushToIPython (self,script=None):
        ''' Push the node to IPython'''
        if not gIPythonStarted:
            self.startIpython() # Does not return
        else:
            if script:
                self.ip.runlines(script)
                return
            c = self.c ; p = c.currentPosition()
            sys.argv = [] # Clear the argv vector.
            push = self.ip.user_ns['_leo'].push
            push(p)
            return
    #@-node:ekr.20080201150746.2:pushToIPython
    #@+node:ekr.20080204083034:started
    def started (self):

        global gIPythonStarted
        return gIPythonStarted
    #@-node:ekr.20080204083034:started
    #@-node:ekr.20080201151802.2:Utils...
    #@-others
#@-node:ekr.20080201143145.6:class ipythonController
#@+node:ekr.20080204103804.3:class leoInterface
class leoInterface:

    '''A class to allow full access to Leo from Ipython.

    An instance of this class called leox is typically injected
    into IPython's user_ns namespace by the init-ipython-command.'''

    def __init__(self,c,g,tag='@ipython-results'):
        self.c, self.g = c,g
#@-node:ekr.20080204103804.3:class leoInterface
#@-others
#@nonl
#@-node:ekr.20080201143145:@thin ipython.py
#@-leo
