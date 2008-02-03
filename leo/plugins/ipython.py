# -*- coding: utf-8 -*-
#@+leo-ver=4-thin
#@+node:ekr.20080201143145:@thin ipython.py
#@@first

#@<< docstring >>
#@+node:ekr.20080201151802:<< docstring >>
'''

The ipython plugin provides two-way communication between Leo scripts and
IPython running in the console from which Leo was launched.

The plugin creates an instance of the pluginController class for each Leo
window. The getIPythonResulst and execIPythonScript methods are public. Use
these as follows::

    controller = c.ipythonController
        # Get the instance of the 

    controller.getIpythonResults
        # Adds a result node as the last child of  the @ipython-results node.

    controller.execIPythonScript(script)
        # Executes the script in IPython.  The contents of the presently
        # selected node are used as the script if script is None.
'''
#@-node:ekr.20080201151802:<< docstring >>
#@nl

__version__ = '0.2'
#@<< version history >>
#@+node:ekr.20080201143145.2:<< version history >>
#@@killcolor
#@+at
# 
# - Version 0.1: Ville M. Vainio and EKR.
#   This version uses g.getScript to synthesize scripts.
#@-at
#@nonl
#@-node:ekr.20080201143145.2:<< version history >>
#@nl
#@<< what's next >>
#@+node:ekr.20080203092534:<< what's next >>
#@@nocolor
#@+at
# 
# It is now absolutely clear that a two-way bridge can be established between 
# Leo and IPython. Indeed, there are many easy and good ways to get the job 
# done.
# 
# One task now is to settle on just one design. Some experimentation will 
# happen before we settle on a way that suffices for the vast majority of Leo 
# and IPython users. The goal: we want the ipython plugin to be extensible by 
# users (from either IPython or Leo), so that users will never (or hardly 
# ever) have to hack on the ipython plugin directly. Some possibilities:
# 
# - A command-oriented approach: define commands sufficient to do all typical 
# tasks.
# 
# - An object-based approach: define extensions to the leox interface class 
# sufficient for all typical tasks.
# 
# - A script-based approach: define ways of executing arbitrary scripts in 
# IPython.
# 
# All these approaches are equivalent; perhaps the are actually identical.
# 
# For example, it is far from obvious that we actually need an 
# execute-ipython-script command(!) Indeed, this script assumes that Leo is 
# the place from which scripts will be run. But it might be simpler for most 
# IPython users to save Leo scripts in IPython's namespace, and to run those 
# scripts directly from IPython. We have already seen that this works.
# 
# However, the first task is code and design cleanup. Here is a partial to-do 
# list:
# 
# 1. Should IPython be a singleton? That is, should the ipython plugin refrain 
# from creating more than one copy of IPShellEmbedd.ipshell()? Probably yes, 
# but I don't understand the fine points of IPython to answer this question 
# for sure.
# 
# 2. I have questions about saving and restoring what in IPython terms is 
# called the "namespace": the dict that defines the execution environment. 
# I've got to read the docs: probably this is a non-issue.
# 
# 3. It is, indeed, possible to run the bridge from Leo when Leo has been 
# started from IPython. But it is still necessary to create the bridge using 
# the alt-5 script, and this script appears to start yet another instance of 
# IPython. But killing this second instance of IPython does not restore the 
# previous IPython instance. It's not clear what is going on, and I'd like to 
# understand...
# 
# 4. The ipython plugin should be driven, at least in part, by user options 
# specified in @settings trees. Some possibilities:
# 
# @string ipython-bridge-interface-object-name = leox
# # The name of the interface object injected into IPython when the bridge is 
# created.
# 
# @string ipython-bridge-immediate-startup = False
#@-at
#@+at 
#@nonl
# True: create the bridge when Leo creates the first Leo window.
# 
# @data ipython-bridge-startup-script
# # The body text is a script to be run when the bridge is first created.
# 
# @data ipython-bridge-auto-open-leo-files
# # The body text is a list of .leo files to be opened
# # automatically when the ipython bridge opens.
# # OTOH, this can be done by the ipython-bridge-startup-script
# 
# etc.!
# 
# 5. I shall revise the IPython docs on Leo's wiki and the corresponding docs 
# on the IPython Cookbook page. I shall also start a new chapter in Leo's 
# Users Guide discussing the IPython bridge.
# 
# In short, the prototyping phase is complete, and we are moving on to the 
# polishing phase.
# 
#@-at
#@-node:ekr.20080203092534:<< what's next >>
#@nl
#@<< imports >>
#@+node:ekr.20080201143145.3:<< imports >>
import leoGlobals as g
import leoPlugins

import sys

import_ok = True

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

#@+others
#@+node:ekr.20080201144219:Module-level functions
#@+node:ekr.20080201143145.4:init
def init ():

    if import_ok:

        leoPlugins.registerHandler('after-create-leo-frame',onCreate)
        g.plugin_signon(__name__)

    return import_ok
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

    #@    @+others
    #@+node:ekr.20080201150746: Birth...
    #@+node:ekr.20080201143145.7:__init__
    def __init__ (self,c):

        self.c = c
        self.inited = False
        self.last_index = 0 # The index of the last result shown.
        self.last_p = None # The last-created results node.
        self.resultsName = '@ipython-results'
        self.root = None # The root of the results tree.

        # Options...
        self.createNodes = True # True: print results in log pane.
        self.printResults = False # True: create results nodes.

        # Set by .initIPython...
        self.d_out = {}
        self.in_list = []
        self.ip = None # The _ip var returned by ipshell.IP.getapi()
        self.ipshell = None

    #@-node:ekr.20080201143145.7:__init__
    #@+node:ekr.20080201143319.10:initIPython
    def initIPython(self):

        if self.inited:
            return True

        try:
            self.ipshell = IPShellEmbed()
            self.ip = ip = self.ipshell.IP.getapi()
            self.in_list, self.d_out = ip.IP.input_hist, ip.IP.output_hist
            g.es_print('created IPython shell...',color='blue')
            self.inited = True # Set the lockout *before* calling ipshell.
            self.ipshell()
            return True
        except Exception:
            g.es_print('exception creating IPython shell',color='red')
            g.es_exception()
            return False
    #@-node:ekr.20080201143319.10:initIPython
    #@-node:ekr.20080201150746: Birth...
    #@+node:ekr.20080201151802.1:Public methods
    #@+node:ekr.20080201150746.1:getIPythonResults
    def getIPythonResults (self):

        if self.initIPython():
            self.showResults()
    #@-node:ekr.20080201150746.1:getIPythonResults
    #@+node:ekr.20080201150746.2:execIPythonScript
    def execIPythonScript (self,script=None):

        c = self.c ; p = c.currentPosition()

        # Init if necessary.
        if not self.initIPython(): return

        # Clear the argv vector.
        sys.argv = [] 

        # Get the script.
        if script is None:
            # script = g.splitLines(p.bodyString() + '\n')
            script = g.getScript(c,p,useSelectedText=False,forcePythonSentinels=True,useSentinels=True)
            script = g.splitLines(script + '\n')
            script = ''.join([z for z in script  if z.strip()])
            print 'script\n',script

        # Run the script.
        self.ip.runlines(script)
    #@-node:ekr.20080201150746.2:execIPythonScript
    #@-node:ekr.20080201151802.1:Public methods
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
    #@-node:ekr.20080201151802.2:Utils...
    #@-others
#@-node:ekr.20080201143145.6:class ipythonController
#@-others
#@nonl
#@-node:ekr.20080201143145:@thin ipython.py
#@-leo
