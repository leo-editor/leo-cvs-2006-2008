#@+leo-ver=4-thin
#@+node:edream.110203113231.925:@thin script_io_to_body.py
"""Send output from the Execute Script command to the end of the body pane"""

#@@language python
#@@tabwidth -4

__version__ = "1.5"

#@<< imports >>
#@+node:ekr.20050101090207.4:<< imports >>
import leoGlobals as g
import leoPlugins

Tk = g.importExtension('Tkinter',pluginName=__name__,verbose=True)
#@nonl
#@-node:ekr.20050101090207.4:<< imports >>
#@nl
#@<< version history >>
#@+node:ekr.20071212114235:<< version history >>
#@@nocolor
#@+at
# 
# 1.5 EKR: A complete rewrite. Now works with Leo 4.4.5 code base.
#@-at
#@nonl
#@-node:ekr.20071212114235:<< version history >>
#@nl

#@+others
#@+node:ekr.20071025195133:init
def init():

    ok = Tk and not g.app.unitTesting
        # Not for unit testing: modifies core classes.
    if not ok: return False

    if g.app.gui is None:
        g.app.createTkGui(__file__)

    if g.app.gui.guiName() != "tkinter": return False

    leoPlugins.registerHandler('after-create-leo-frame',onCreate)

    g.plugin_signon(__name__)

    return True
#@-node:ekr.20071025195133:init
#@+node:ekr.20071212092332:onCreate
def onCreate (tag, keys):

    c = keys.get('c')
    if c and c.frame.log:

        print 'overriding c.executeScript'

        # Inject ivars.
        log = c.frame.log
        c.script_io_to_body_oldexec  = c.executeScript
        c.script_io_to_body_oldput   = log.put
        c.script_io_to_body_oldputnl = log.putnl

        # Override c.executeScript.
        g.funcToMethod(newExecuteScript,c.__class__,'executeScript')
        c.k.overrideCommand('execute-script',c.executeScript)
#@-node:ekr.20071212092332:onCreate
#@+node:edream.110203113231.929:newEs, etc. (not used)
# def newEnl():
    # print

# def newEcnl():
    # print

# def newEcnls(n):
    # while n > 0:
        # n -= 1
        # print

# def newEs(s,*args,**keys):
    # newline = keys.get("newline",True)
    # if type(s) != type("") and type(s) != type(u""):
        # s = repr(s)
    # for arg in args:
        # if type(arg) != type("") and type(arg) != type(u""):
            # arg = repr(arg)
        # s = s + ", " + arg
    # if newline:
        # print s
    # else:
        # print s,
#@-node:edream.110203113231.929:newEs, etc. (not used)
#@+node:edream.110203113231.928:newPut and newPutNl
# Same as frame.put except sends output to the end of the body text.
def newPut (self,s,*args,**keys):

    body = self.frame.body ; w = body.bodyCtrl

    # print 'newPut',repr(s),w,g.callers()

    if w:
        w.insert("end",s)
        body.onBodyChanged("Typing")
    # else: print s,

# Same as frame.putnl except sends output to the end of the body text.
def newPutNl (self,s,*args,**keys):

    newPut (self,'\n')
#@-node:edream.110203113231.928:newPut and newPutNl
#@+node:ekr.20071212091008.1:newExecuteScript & helpers
def newExecuteScript (self,
    event=None,p=None,script=None,
    useSelectedText=True,define_g=True,
    define_name='__main__',silent=False
):

    c = self ; log = c.frame.log
    redirect(c)

    # Use silent to suppress 'end of script message'
    c.script_io_to_body_oldexec(event,p,script,useSelectedText,define_g,define_name,silent=True)
    undirect(c)

    # Now issue the 'end of script' message'
    if not silent:
        tabName = log and hasattr(log,'tabName') and log.tabName or 'Log'
        g.ecnl()
        g.es("end of script",color="purple",tabName=tabName)
#@+node:ekr.20071212090128:redirect
def redirect (c):

    log = c.frame.log.__class__

    g.funcToMethod(newPut,log,"put")
    g.funcToMethod(newPutNl,log,"putnl")
#@nonl
#@-node:ekr.20071212090128:redirect
#@+node:ekr.20071212091008:undirect
def undirect (c):

    log = c.frame.log.__class__

    g.funcToMethod(c.script_io_to_body_oldput,log,"put")
    g.funcToMethod(c.script_io_to_body_oldputnl,log,"putnl")
#@-node:ekr.20071212091008:undirect
#@-node:ekr.20071212091008.1:newExecuteScript & helpers
#@-others
#@-node:edream.110203113231.925:@thin script_io_to_body.py
#@-leo
