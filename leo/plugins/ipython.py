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

__version__ = '0.6'
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
# 
# - Allow get-ipython-results to store actual objects using Leo's uA 
# mechanism.
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
#@+node:ekr.20080204103804.1:createNode
def createNode(c,parent,head,body):

    '''A convenience method for use the leoInterface classes.'''

    c.beginUpdate()
    try:
        p = c.insertHeadline()
        p.moveToLastChildOf(parent)
        c.setHeadString(p,head)
        c.setBodyString(p,body)
        c.frame.tree.expandAllAncestors(p)
        c.selectPosition(p)
    finally:
        c.endUpdate()
    return p

#@-node:ekr.20080204103804.1:createNode
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
        self.last_index = 0 # The index of the last result shown.
        self.last_p = None # The last-created results node.
        self.root = None # The root of the results tree.

        # Options...
        self.createNodes = True # True: print results in log pane.
        self.printResults = False # True: create results nodes.
        self.leoxName =    c.config.getString('ipython-interface-object-name') or 'leox'
        self.resultsName = c.config.getString('ipython-results-node-headline') or '@ipython-results'

        # Set by .startIPython...
        self.api = None
        self.d_out = {}
        self.in_list = []
        self.ip = None # The _ip var returned by ipshell.IP.getapi()
        self.ipshell = None

        self.createCommands()
    #@-node:ekr.20080201143145.7:ctor
    #@+node:ekr.20080204080848:createCommands
    def createCommands(self):

        '''Create all of the ipython plugin's minibuffer commands.'''

        c = self.c ; k = c.k

        table = (
            ('start-ipython',           self.startIPython),
            ('get-ipython-results',     self.getIPythonResults),
            ('execute-ipython-script',  self.executeIPythonScriptCommand),
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

        global gIPythonStarted

        if gIPythonStarted:
            return self.error('IPython is already running')

        try:
            c = self.c
            #self.ipshell = IPShellEmbed() # Create object to be bound to .api.

            self.api = api = IPython.ipapi
            self.message('creating IPython shell...')
            gIPythonStarted = True # Do this *before* calling ipshell.
            leox = leoInterface(c,g) # inject leox into the namespace.
            my_ns = { self.leoxName:leox }
            ses = self.api.make_session(my_ns)
            self.ip = ip = ses.IP.getapi()
            self.in_list, self.d_out = ip.IP.input_hist, ip.IP.output_hist

            c.inCommand = False # Disable the command lockout logic, just as for scripts.
            sys.argv = []
            ses.mainloop()
                # Does not return until IPython closes!
            # self.ipshell() # This doesn't return until IPython closes!
        except Exception:
            self.error('exception creating IPython shell')
            g.es_exception()
    #@-node:ekr.20080201143319.10:startIPython
    #@+node:ekr.20080201150746.1:getIPythonResults
    def getIPythonResults (self,event=None):

        '''The get-ipython-results command.

        IPython must be started, but need not be inited.'''

        if not gIPythonStarted:
            self.startIpython() # Does not return
        else:
            self.showResults()
    #@-node:ekr.20080201150746.1:getIPythonResults
    #@+node:ekr.20080204111314:executeIPythonScriptCommand
    def executeIPythonScriptCommand(self,event=None):

        '''The execute-ipython-script command.

        IPython must be started, but need not be inited.'''

        self.executeIPythonScript(script=None)
    #@-node:ekr.20080204111314:executeIPythonScriptCommand
    #@-node:ekr.20080201151802.1:Commands
    #@+node:ekr.20080201151802.2:Utils...
    #@+node:ekr.20080201143319.12:createRoot
    def createRoot (self):

        c = self.c

        if self.root: return self.root

        self.root = g.findNodeAnywhere(c,self.resultsName)
        if not self.root:
            self.root = p.insertAfter()
            c.setHeadString(self.root,tag)
            c.setBodyString(self.root,'@nocolor\n\n')

        return self.root
    #@-node:ekr.20080201143319.12:createRoot
    #@+node:ekr.20080204075924:error & message
    def error (self,s):

        g.es_print(s,color='red')

    def message (self,s):

        g.es_print(s,color='blue')
    #@-node:ekr.20080204075924:error & message
    #@+node:ekr.20080201150746.2:executeIPythonScript
    def executeIPythonScript (self,script=None):
        '''Execute the script in Ipython.
        Use the presently selected body text if no script is given.'''
        if not gIPythonStarted:
            self.startIpython() # Does not return
        else:
            c = self.c ; p = c.currentPosition()
            sys.argv = [] # Clear the argv vector.

            # Get the script.
            if script is None:
                # script = g.splitLines(p.bodyString() + '\n')
                script = g.getScript(c,p,useSelectedText=False,forcePythonSentinels=True,useSentinels=True)
                script = g.splitLines(script + '\n')
                script = ''.join([z for z in script  if z.strip()])
                print 'script\n',script

            # Run the script.
            self.ip.runlines(script)
    #@-node:ekr.20080201150746.2:executeIPythonScript
    #@+node:ekr.20080201143319.11:showResults & helper
    def showResults (self):

        c = self.c

        c.beginUpdate()
        try:
            for key in self.d_out.keys():
                if int(key) > self.last_index:
                    in_val = self.in_list[int(key)]
                    out_val = self.d_out.get(key)
                    self.showResult(key,in_val,out_val)
                    self.last_index = int(key)
        finally:
            if self.last_p:
                c.selectPosition(self.last_p)
            c.endUpdate()
    #@+node:ekr.20080201143319.13:showResult
    def showResult (self,n,in_val,out_val):

        c = self.c

        if self.printResults:
            tabName = 'IPython'
            g.es('in [%s]: %s' % (n,in_val),tabName=tabName)
            g.es('out[%s]: %s' % (n,out_val),tabName=tabName)

        if self.createNodes:
            if not self.last_p:
                self.createRoot()
                self.last_p = self.root.copy()
            p2 = self.root.insertAsLastChild()
            self.last_p = p2.copy()
            c.setHeadString(p2,'result %s' % (n))
            c.setBodyString(p2,'%s\n%s' % (
                'in [%s]: %s' % (n,in_val),
                'out[%s]: %s' % (n,out_val)))
    #@-node:ekr.20080201143319.13:showResult
    #@-node:ekr.20080201143319.11:showResults & helper
    #@+node:ekr.20080204083034:started
    def started (self):

        global gIPythonStarted
        return gIPythonStarted
    #@-node:ekr.20080204083034:started
    #@-node:ekr.20080201151802.2:Utils...
    #@-others
#@-node:ekr.20080201143145.6:class ipythonController
#@+node:ekr.20080204103804.2:class leoInterfaceResults
class leoInterfaceResults:

    '''A class representing the saved results of IPython computations.

    results.a = x # creates a results node in the Leo outline.
    x = results.a # returns the saved results in a.
    '''


    #@    @+others
    #@+node:ekr.20080204162955:ctor
    def __init__(self,c,g,root):

        assert(root)

        self._c = c
        self._g = g
        self._root = root

        self._inited = True # Disable any further attributes.
    #@-node:ekr.20080204162955:ctor
    #@+node:ekr.20080204162955.1:__getattr__
    def __getattr__(self, key):

        for p in self._root.children_iter():
            if p.headString() == key:
                break
        else:
            raise AttributeError

        return IPython.genutils.SList(p.bodyString().splitlines())
    #@-node:ekr.20080204162955.1:__getattr__
    #@+node:ekr.20080204162955.2:__setattr__
    def __setattr__(self, item, value):

        if self.__dict__.has_key('_inited'):
            # print '__setattr__.result','item',item,'value',value
            createNode(self._c,self._root,head=item,body=str(value))
        else:
            # Allow attributes to be set in the ctor.
            # print '__setattr__','item',item,'value',value
            self.__dict__ [item] = value
    #@-node:ekr.20080204162955.2:__setattr__
    #@-others
#@-node:ekr.20080204103804.2:class leoInterfaceResults
#@+node:ekr.20080204103804.3:class leoInterface
class leoInterface:

    '''A class to allow full access to Leo from Ipython.

    An instance of this class called leox is typically injected
    into IPython's user_ns namespace by the init-ipython-command.'''

    def __init__(self,c,g,tag='@ipython-results'):
        self.c, self.g = c,g
        # Find or create the parent for all results nodes.
        self.root = g.findNodeAnywhere(c,tag)
        if not self.root:
            parent = c.currentPosition()
            self.root = createNode(c=c,parent=parent,head=tag,body='')
        # Create the results interface object.
        self.results = leoInterfaceResults(c,g,self.root)
#@nonl
#@-node:ekr.20080204103804.3:class leoInterface
#@-others
#@nonl
#@-node:ekr.20080201143145:@thin ipython.py
#@-leo
