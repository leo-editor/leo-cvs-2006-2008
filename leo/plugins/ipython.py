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

__version__ = '0.1'
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
