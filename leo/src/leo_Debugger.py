#@+leo-ver=4-thin
#@+node:ekr.20060516135654.94:@thin leo_Debugger.py
#@<< imports >>
#@+node:ekr.20060516135654.95:<< imports >>
import leoGlobals as g

import sys
import leo_FileList
import leo_run
import leo_RemoteDebugger

import idlelib.rpc as rpc
import idlelib.ScrolledList as ScrolledList
from code import InteractiveInterpreter

import bdb
import linecache
import os
import socket
import sys
import time
import types

#from Tkinter import *
import Tkinter as Tk
import tkMessageBox

import __main__

### from WindowList import ListedToplevel
## from ScrolledList import ScrolledList
#@nonl
#@-node:ekr.20060516135654.95:<< imports >>
#@nl

LOCALHOST = '127.0.0.1'

#@+others
#@+node:ekr.20060516142615.4:go
def go (c):
    
    # From Pyshell.ctor
    interp = ModifiedInterpreter(dummyShell(c))
    
    # From Pyshell.begin:
    client = interp.start_subprocess()
    g.trace('client',client,'interp',interp)
    open_debugger(c,interp.rpcclt,interp)
#@nonl
#@-node:ekr.20060516142615.4:go
#@+node:ekr.20060516142615.5:open_debugger
def open_debugger(c,rpcClient,interp):

    dbg_gui = leo_RemoteDebugger.start_remote_debugger(c,rpcClient,interp)
    interp.setdebugger(dbg_gui)
    dbg_gui.load_breakpoints()

    if 0: ### old code
        if self.interp.rpcclt:
            dbg_gui = RemoteDebugger.start_remote_debugger(self.interp.rpcclt,self)
        else:
            dbg_gui = Debugger.Debugger(self)
        self.interp.setdebugger(dbg_gui)
        dbg_gui.load_breakpoints()
        sys.ps1 = "[DEBUG ON]\n>>> "
        self.showprompt()
        self.set_debugger_indicator()
#@nonl
#@-node:ekr.20060516142615.5:open_debugger
#@+node:ekr.20060516142615.6:class dummyShell
class dummyShell:
    
    def __init__ (self,c):
        self.c = c
        self.stdout = sys.__stdout__
        self.stderr = sys.__stderr__
        self.flist = []
        self.closing = False
        self.executing = False
        self.text = Tk.Text() # Ignored completely
        self.pollinterval = 50  # millisec
        # g.trace('dummyShell')
#@nonl
#@-node:ekr.20060516142615.6:class dummyShell
#@+node:ekr.20060516135654.96:From Pyshell.py
#@+node:ekr.20060516135654.97:class ModifiedInterpreter
class ModifiedInterpreter(InteractiveInterpreter):

    #@	@+others
    #@+node:ekr.20060516135654.98:__init__
    def __init__(self, tkconsole):
    
        self.tkconsole = tkconsole # Required by later rpc registrations.
        
        self.active_seq = None
        self.port = 8833
        self.rpcclt = None
        self.rpcpid = None
        
        locals = sys.modules['__main__'].__dict__
        InteractiveInterpreter.__init__(self, locals=locals)
        self.save_warnings_filters = None
        self.restarting = False
    
        self.subprocess_arglist = self.build_subprocess_arglist()
    #@nonl
    #@-node:ekr.20060516135654.98:__init__
    #@+node:ekr.20060516135654.99:spawn_subprocess (sets self.rpcpid)
    def spawn_subprocess(self):
    
        args = self.subprocess_arglist
    
        self.rpcpid = os.spawnv(os.P_NOWAIT, sys.executable, args)
        
        g.trace('os.spawnv returns rpcpid',self.rpcpid)
    #@nonl
    #@-node:ekr.20060516135654.99:spawn_subprocess (sets self.rpcpid)
    #@+node:ekr.20060516135654.100:leo_Debugger.build_subprocess_arglist
    def build_subprocess_arglist(self):
        
        w = ['-W' + s for s in sys.warnoptions]
        # Maybe IDLE is installed and is being accessed via sys.path,
        # or maybe it's not installed and the idle.py script is being
        # run from the IDLE source directory.
        
        if 1: # EKR
            del_exitf = False
        else:
            del_exitf = idleConf.GetOption(
                'main', 'General', 'delete-exitfunc',
                default=False, type='bool')
        
        ###if __name__ == 'idlelib.PyShell':
        if 1: # Works only if leo/src is put in sys.path in sitecustomize or in the Python PATH variable.
            command = "__import__('leo_run').main(%r)" % (del_exitf,)
        elif 1: # EKR: Works using idlelib.run.  
            command = "__import__('idlelib.run').run.main(%r)" % (del_exitf,)
        else:
            command = "__import__('run').main(%r)" % (del_exitf,)
        if sys.platform[:3] == 'win' and ' ' in sys.executable:
            # handle embedded space in path by quoting the argument
            decorated_exec = '"%s"' % sys.executable
        else:
            decorated_exec = sys.executable
        
        return [decorated_exec] + w + ["-c", command, str(self.port)]
    #@nonl
    #@-node:ekr.20060516135654.100:leo_Debugger.build_subprocess_arglist
    #@+node:ekr.20060516135654.101:start_subprocess
    def start_subprocess(self):
        # spawning first avoids passing a listening socket to the subprocess
        self.spawn_subprocess()
        #time.sleep(20) # test to simulate GUI not accepting connection
        addr = (LOCALHOST, self.port)
        # Idle starts listening for connection on localhost
        for i in range(3):
            time.sleep(i)
            try:
                self.rpcclt = MyRPCClient(addr)
                g.trace(self.rpcclt)
                break
            except socket.error, err:
                pass
        else:
            self.display_port_binding_error()
            return None
        # Accept the connection from the Python execution server
        self.rpcclt.listening_sock.settimeout(10)
        try:
            self.rpcclt.accept()
        except socket.timeout, err:
            self.display_no_subprocess_error()
            return None
        self.rpcclt.register("stdin", self.tkconsole)
        self.rpcclt.register("stdout", self.tkconsole.stdout)
        self.rpcclt.register("stderr", self.tkconsole.stderr)
        self.rpcclt.register("flist", self.tkconsole.flist)
        self.rpcclt.register("linecache", linecache)
        self.rpcclt.register("interp", self)
        self.transfer_path()
        self.poll_subprocess()
        return self.rpcclt
    #@-node:ekr.20060516135654.101:start_subprocess
    #@+node:ekr.20060516135654.102:restart_subprocess
    def restart_subprocess(self):
        if self.restarting:
            return self.rpcclt
        self.restarting = True
        # close only the subprocess debugger
        debug = self.getdebugger()
        if debug:
            try:
                # Only close subprocess debugger, don't unregister gui_adap!
                RemoteDebugger.close_subprocess_debugger(self.rpcclt)
            except:
                pass
        # Kill subprocess, spawn a new one, accept connection.
        self.rpcclt.close()
        self.unix_terminate()
        console = self.tkconsole
        was_executing = console.executing
        console.executing = False
        self.spawn_subprocess()
        try:
            self.rpcclt.accept()
        except socket.timeout, err:
            self.display_no_subprocess_error()
            return None
        self.transfer_path()
        # annotate restart in shell window and mark it
        console.text.delete("iomark", "end-1c")
        if was_executing:
            console.write('\n')
            console.showprompt()
        halfbar = ((int(console.width) - 16) // 2) * '='
        console.write(halfbar + ' RESTART ' + halfbar)
        console.text.mark_set("restart", "end-1c")
        console.text.mark_gravity("restart", "left")
        console.showprompt()
        # restart subprocess debugger
        if debug:
            # Restarted debugger connects to current instance of debug GUI
            gui = RemoteDebugger.restart_subprocess_debugger(self.rpcclt)
            # reload remote debugger breakpoints for all PyShellEditWindows
            debug.load_breakpoints()
        self.restarting = False
        return self.rpcclt
    #@-node:ekr.20060516135654.102:restart_subprocess
    #@+node:ekr.20060516135654.103:__request_interrupt
    def __request_interrupt(self):
    
        self.rpcclt.remotecall("exec", "interrupt_the_server", (), {})
    #@-node:ekr.20060516135654.103:__request_interrupt
    #@+node:ekr.20060516135654.104:interrupt_subprocess
    def interrupt_subprocess(self):
        threading.Thread(target=self.__request_interrupt).start()
    #@-node:ekr.20060516135654.104:interrupt_subprocess
    #@+node:ekr.20060516135654.105:kill_subprocess
    def kill_subprocess(self):
        
        try:
            self.rpcclt.close()
        except AttributeError:  # no socket
            pass
        self.unix_terminate()
        self.tkconsole.executing = False
        self.rpcclt = None
    
    #@-node:ekr.20060516135654.105:kill_subprocess
    #@+node:ekr.20060516135654.106:unix_terminate
    def unix_terminate(self):
        "UNIX: make sure subprocess is terminated and collect status"
        if hasattr(os, 'kill'):
            try:
                os.kill(self.rpcpid, SIGTERM)
            except OSError:
                # process already terminated:
                return
            else:
                try:
                    os.waitpid(self.rpcpid, 0)
                except OSError:
                    return
    #@-node:ekr.20060516135654.106:unix_terminate
    #@+node:ekr.20060516135654.107:transfer_path
    def transfer_path(self):
        self.runcommand("""if 1:
        import sys as _sys
        _sys.path = %r
        del _sys
        _msg = 'Use File/Exit or your end-of-file key to quit Leo'
        __builtins__.quit = __builtins__.exit = _msg
        del _msg
        \n""" % (sys.path,))
    #@-node:ekr.20060516135654.107:transfer_path
    #@+node:ekr.20060516135654.108:poll_subprocess
    def poll_subprocess(self):
        clt = self.rpcclt
        if clt is None:
            return
        try:
            response = clt.pollresponse(self.active_seq, wait=0.05)
        except (EOFError, IOError, KeyboardInterrupt):
            # lost connection or subprocess terminated itself, restart
            # [the KBI is from rpc.SocketIO.handle_EOF()]
            if self.tkconsole.closing:
                return
            response = None
            self.restart_subprocess()
        if response:
            self.tkconsole.resetoutput()
            self.active_seq = None
            how, what = response
            console = self.tkconsole.console
            if how == "OK":
                if what is not None:
                    print >>console, repr(what)
            elif how == "EXCEPTION":
                if self.tkconsole.getvar(virtual_event_name('toggle-jit-stack-viewer')):
                    self.remote_stack_viewer()
            elif how == "ERROR":
                errmsg = "PyShell.ModifiedInterpreter: Subprocess ERROR:\n"
                print >>sys.__stderr__, errmsg, what
                print >>console, errmsg, what
            # we received a response to the currently active seq number:
            self.tkconsole.endexecuting()
        # Reschedule myself
        if not self.tkconsole.closing:
            self.tkconsole.text.after(self.tkconsole.pollinterval,
                                      self.poll_subprocess)
    #@-node:ekr.20060516135654.108:poll_subprocess
    #@+node:ekr.20060516135654.109:setdebugger
    debugger = None
    
    def setdebugger(self, debugger):
        self.debugger = debugger
    #@-node:ekr.20060516135654.109:setdebugger
    #@+node:ekr.20060516135654.110:getdebugger
    def getdebugger(self):
        return self.debugger
    #@-node:ekr.20060516135654.110:getdebugger
    #@+node:ekr.20060516135654.111:open_remote_stack_viewer
    def open_remote_stack_viewer(self):
        """Initiate the remote stack viewer from a separate thread.
    
        This method is called from the subprocess, and by returning from this
        method we allow the subprocess to unblock.  After a bit the shell
        requests the subprocess to open the remote stack viewer which returns a
        static object looking at the last exceptiopn.  It is queried through
        the RPC mechanism.
    
        """
        self.tkconsole.text.after(300, self.remote_stack_viewer)
        return
    #@-node:ekr.20060516135654.111:open_remote_stack_viewer
    #@+node:ekr.20060516135654.112:remote_stack_viewer
    def remote_stack_viewer(self):
        import RemoteObjectBrowser
        oid = self.rpcclt.remotequeue("exec", "stackviewer", ("flist",), {})
        if oid is None:
            self.tkconsole.root.bell()
            return
        item = RemoteObjectBrowser.StubObjectTreeItem(self.rpcclt, oid)
        from TreeWidget import ScrolledCanvas, TreeNode
        top = Toplevel(self.tkconsole.root)
        theme = idleConf.GetOption('main','Theme','name')
        background = idleConf.GetHighlight(theme, 'normal')['background']
        sc = ScrolledCanvas(top, bg=background, highlightthickness=0)
        sc.frame.pack(expand=1, fill="both")
        node = TreeNode(sc.canvas, None, item)
        node.expand()
    #@-node:ekr.20060516135654.112:remote_stack_viewer
    #@+node:ekr.20060516135654.113:execsource
        # XXX Should GC the remote tree when closing the window
    
    gid = 0
    
    def execsource(self, source):
        "Like runsource() but assumes complete exec source"
        filename = self.stuffsource(source)
        self.execfile(filename, source)
    #@-node:ekr.20060516135654.113:execsource
    #@+node:ekr.20060516135654.114:execfile
    def execfile(self, filename, source=None):
        
        g.trace(filename)
    
        "Execute an existing file"
        if source is None:
            source = open(filename, "r").read()
        try:
            code = compile(source, filename, "exec")
        except (OverflowError, SyntaxError):
            self.tkconsole.resetoutput()
            tkerr = self.tkconsole.stderr
            print>>tkerr, '*** Error in script or command!\n'
            print>>tkerr, 'Traceback (most recent call last):'
            InteractiveInterpreter.showsyntaxerror(self, filename)
            self.tkconsole.showprompt()
        else:
            self.runcode(code)
    #@-node:ekr.20060516135654.114:execfile
    #@+node:ekr.20060516135654.115:runsource
    def runsource(self, source):
        "Extend base class method: Stuff the source in the line cache first"
        filename = self.stuffsource(source)
        self.more = 0
        self.save_warnings_filters = warnings.filters[:]
        warnings.filterwarnings(action="error", category=SyntaxWarning)
        if isinstance(source, types.UnicodeType):
            import IOBinding
            try:
                source = source.encode(IOBinding.encoding)
            except UnicodeError:
                self.tkconsole.resetoutput()
                self.write("Unsupported characters in input")
                return
        try:
            return InteractiveInterpreter.runsource(self, source, filename)
        finally:
            if self.save_warnings_filters is not None:
                warnings.filters[:] = self.save_warnings_filters
                self.save_warnings_filters = None
    #@-node:ekr.20060516135654.115:runsource
    #@+node:ekr.20060516135654.116:stuffsource
    def stuffsource(self, source):
        "Stuff source in the filename cache"
        filename = "<pyshell#%d>" % self.gid
        self.gid = self.gid + 1
        lines = source.split("\n")
        linecache.cache[filename] = len(source)+1, 0, lines, filename
        return filename
    #@-node:ekr.20060516135654.116:stuffsource
    #@+node:ekr.20060516135654.117:prepend_syspath
    def prepend_syspath(self, filename):
        "Prepend sys.path with file's directory if not already included"
        self.runcommand("""if 1:
            _filename = %r
            import sys as _sys
            from os.path import dirname as _dirname
            _dir = _dirname(_filename)
            if not _dir in _sys.path:
                _sys.path.insert(0, _dir)
            del _filename, _sys, _dirname, _dir
            \n""" % (filename,))
    #@-node:ekr.20060516135654.117:prepend_syspath
    #@+node:ekr.20060516135654.118:showsyntaxerror
    def showsyntaxerror(self, filename=None):
        """Extend base class method: Add Colorizing
    
        Color the offending position instead of printing it and pointing at it
        with a caret.
    
        """
        text = self.tkconsole.text
        stuff = self.unpackerror()
        if stuff:
            msg, lineno, offset, line = stuff
            if lineno == 1:
                pos = "iomark + %d chars" % (offset-1)
            else:
                pos = "iomark linestart + %d lines + %d chars" % \
                      (lineno-1, offset-1)
            text.tag_add("ERROR", pos)
            text.see(pos)
            char = text.get(pos)
            if char and char in IDENTCHARS:
                text.tag_add("ERROR", pos + " wordstart", pos)
            self.tkconsole.resetoutput()
            self.write("SyntaxError: %s\n" % str(msg))
        else:
            self.tkconsole.resetoutput()
            InteractiveInterpreter.showsyntaxerror(self, filename)
        self.tkconsole.showprompt()
    #@-node:ekr.20060516135654.118:showsyntaxerror
    #@+node:ekr.20060516135654.119:unpackerror
    def unpackerror(self):
        type, value, tb = sys.exc_info()
        ok = type is SyntaxError
        if ok:
            try:
                msg, (dummy_filename, lineno, offset, line) = value
                if not offset:
                    offset = 0
            except:
                ok = 0
        if ok:
            return msg, lineno, offset, line
        else:
            return None
    #@-node:ekr.20060516135654.119:unpackerror
    #@+node:ekr.20060516135654.120:showtraceback
    def showtraceback(self):
    
        "Extend base class method to reset output properly"
        self.tkconsole.resetoutput()
        self.checklinecache()
        InteractiveInterpreter.showtraceback(self)
        if self.tkconsole.getvar(g.virtual_event_name('toggle-jit-stack-viewer')):
            self.tkconsole.open_stack_viewer()
    #@nonl
    #@-node:ekr.20060516135654.120:showtraceback
    #@+node:ekr.20060516135654.121:checklinecache
    def checklinecache(self):
        c = linecache.cache
        for key in c.keys():
            if key[:1] + key[-1:] != "<>":
                del c[key]
    #@-node:ekr.20060516135654.121:checklinecache
    #@+node:ekr.20060516135654.122:runcommand
    def runcommand(self, code):
        "Run the code without invoking the debugger"
        # The code better not raise an exception!
        if self.tkconsole.executing:
            self.display_executing_dialog()
            return 0
        if self.rpcclt:
            self.rpcclt.remotequeue("exec", "runcode", (code,), {})
        else:
            exec code in self.locals
        return 1
    #@-node:ekr.20060516135654.122:runcommand
    #@+node:ekr.20060516135654.123:runcode
    def runcode(self, code):
        "Override base class method"
        if self.tkconsole.executing:
            self.interp.restart_subprocess()
        self.checklinecache()
        if self.save_warnings_filters is not None:
            warnings.filters[:] = self.save_warnings_filters
            self.save_warnings_filters = None
        debugger = self.debugger
        try:
            self.tkconsole.beginexecuting()
            try:
                if not debugger and self.rpcclt is not None:
                    self.active_seq = self.rpcclt.asyncqueue("exec", "runcode",
                                                            (code,), {})
                elif debugger:
                    debugger.run(code, self.locals)
                else:
                    exec code in self.locals
            except SystemExit:
                if tkMessageBox.askyesno(
                    "Exit?",
                    "Do you want to exit altogether?",
                    default="yes",
                    master=self.tkconsole.text):
                    raise
                else:
                    self.showtraceback()
            except:
                self.showtraceback()
        finally:
            if not use_subprocess:
                self.tkconsole.endexecuting()
    #@-node:ekr.20060516135654.123:runcode
    #@+node:ekr.20060516135654.124:write
    def write(self, s):
        "Override base class method"
        self.tkconsole.stderr.write(s)
    #@-node:ekr.20060516135654.124:write
    #@+node:ekr.20060516135654.125:display_port_binding_error
    def display_port_binding_error(self):
        tkMessageBox.showerror(
            "Port Binding Error",
            "Leo can't bind TCP/IP port 8833, which is necessary to "
            "communicate with its Python execution server.  Either "
            "no networking is installed on this computer or another "
            "process (another Leo?) is using the port.  Run Leo with the -n "
            "command line switch to start without a subprocess and refer to "
            "Help/Leo Help 'Running without a subprocess' for further "
            "details.",
            master=self.tkconsole.text)
    #@-node:ekr.20060516135654.125:display_port_binding_error
    #@+node:ekr.20060516135654.126:display_no_subprocess_error
    def display_no_subprocess_error(self):
        tkMessageBox.showerror(
            "Subprocess Startup Error",
            "Leo's subprocess didn't make connection.  Either Leo can't "
            "start a subprocess or personal firewall software is blocking "
            "the connection.",
            master=self.tkconsole.text)
    #@-node:ekr.20060516135654.126:display_no_subprocess_error
    #@+node:ekr.20060516135654.127:display_executing_dialog
    def display_executing_dialog(self):
        
        if 1: ### EKR
            g.trace('Executing a command. Please wait until it is finished')
        else:
            tkMessageBox.showerror(
                "Already executing",
                "The Python Shell window is already executing a command; "
                "please wait until it is finished.",
                master=self.tkconsole.text)
    #@nonl
    #@-node:ekr.20060516135654.127:display_executing_dialog
    #@+node:ekr.20060516135654.128:close_debugger OVERRIDE
    def close_debugger(self):
        
        interp = self
        
        db = interp.getdebugger()
        if db:
            interp.setdebugger(None)
            db.close()
            if interp.rpcclt:
                 leo_RemoteDebugger.close_remote_debugger(interp.rpcclt)
        
        if 0: # original code
            db = self.interp.getdebugger()
            if db:
                self.interp.setdebugger(None)
                db.close()
                if self.interp.rpcclt:
                    RemoteDebugger.close_remote_debugger(self.interp.rpcclt)
                self.resetoutput()
                self.console.write("[DEBUG OFF]\n")
                sys.ps1 = ">>> "
                self.showprompt()
            self.set_debugger_indicator()
    #@nonl
    #@-node:ekr.20060516135654.128:close_debugger OVERRIDE
    #@-others
#@nonl
#@-node:ekr.20060516135654.97:class ModifiedInterpreter
#@+node:ekr.20060516135654.129:class MyRPCClient
class MyRPCClient(rpc.RPCClient):

    #@	@+others
    #@+node:ekr.20060516135654.130:handle_EOF
    def handle_EOF(self):
    
        "Override the base class - just re-raise EOFError"
        raise EOFError
    #@nonl
    #@-node:ekr.20060516135654.130:handle_EOF
    #@-others
#@nonl
#@-node:ekr.20060516135654.129:class MyRPCClient
#@-node:ekr.20060516135654.96:From Pyshell.py
#@+node:ekr.20060516135654.162:From Debugger.py
#@+node:ekr.20060516135654.163:class Idb (used by remote debugger code)
# Important: this class is used by the remote debugger code.

class Idb(bdb.Bdb):
    
    #@	@+others
    #@+node:ekr.20060516135654.164:__init__
    def __init__(self, gui):
    
        self.gui = gui
        bdb.Bdb.__init__(self)
    #@nonl
    #@-node:ekr.20060516135654.164:__init__
    #@+node:ekr.20060516135654.165:user_line
    def user_line(self, frame):
        
        if self.in_rpc_code(frame):
            self.set_step()
        else:
            message = self.__frame2message(frame)
            self.gui.interaction(message, frame)
    #@nonl
    #@-node:ekr.20060516135654.165:user_line
    #@+node:ekr.20060516135654.166:user_exception
    def user_exception(self, frame, info):
        
        if self.in_rpc_code(frame):
            self.set_step()
        else:
            message = self.__frame2message(frame)
            self.gui.interaction(message, frame, info)
    #@nonl
    #@-node:ekr.20060516135654.166:user_exception
    #@+node:ekr.20060516135654.167:in_rpc_code
    def in_rpc_code(self, frame):
    
        if frame.f_code.co_filename.count('rpc.py'):
            return True
        else:
            prev_frame = frame.f_back
            if prev_frame.f_code.co_filename.count('Debugger.py'):
                # (that test will catch both Debugger.py and RemoteDebugger.py)
                return False
            return self.in_rpc_code(prev_frame)
    #@-node:ekr.20060516135654.167:in_rpc_code
    #@+node:ekr.20060516135654.168:__frame2message
    def __frame2message(self, frame):
    
        code = frame.f_code
        filename = code.co_filename
        lineno = frame.f_lineno
        basename = os.path.basename(filename)
        message = "%s:%s" % (basename, lineno)
        if code.co_name != "?":
            message = "%s: %s()" % (message, code.co_name)
        return message
    #@nonl
    #@-node:ekr.20060516135654.168:__frame2message
    #@-others
#@-node:ekr.20060516135654.163:class Idb (used by remote debugger code)
#@+node:ekr.20060516135654.169:class StackViewer
class StackViewer(ScrolledList.ScrolledList):
    #@	@+others
    #@+node:ekr.20060516135654.170:__init__
    def __init__(self, master, flist, gui):
        
        g.trace('StackViewer: flist',flist,g.callers())
        
        ScrolledList.ScrolledList.__init__(self, master, width=80)
        self.flist = flist
        self.gui = gui
        self.stack = []
    #@nonl
    #@-node:ekr.20060516135654.170:__init__
    #@+node:ekr.20060516135654.171:load_stack
    def load_stack(self, stack, index=None):
        self.stack = stack
        self.clear()
        for i in range(len(stack)):
            frame, lineno = stack[i]
            try:
                modname = frame.f_globals["__name__"]
            except:
                modname = "?"
            code = frame.f_code
            filename = code.co_filename
            funcname = code.co_name
            import linecache
            sourceline = linecache.getline(filename, lineno)
            import string
            sourceline = string.strip(sourceline)
            if funcname in ("?", "", None):
                item = "%s, line %d: %s" % (modname, lineno, sourceline)
            else:
                item = "%s.%s(), line %d: %s" % (modname, funcname,
                                                 lineno, sourceline)
            if i == index:
                item = "> " + item
            self.append(item)
        if index is not None:
            self.select(index)
    #@-node:ekr.20060516135654.171:load_stack
    #@+node:ekr.20060516135654.172:popup_event
    def popup_event(self, event):
        "override base method"
        if self.stack:
            return ScrolledList.ScrolledList.popup_event(self, event)
    #@-node:ekr.20060516135654.172:popup_event
    #@+node:ekr.20060516135654.173:fill_menu
    def fill_menu(self):
        "override base method"
        menu = self.menu
        menu.add_command(label="Go to source line",
                         command=self.goto_source_line)
        menu.add_command(label="Show stack frame",
                         command=self.show_stack_frame)
    #@-node:ekr.20060516135654.173:fill_menu
    #@+node:ekr.20060516135654.174:on_select
    def on_select(self, index):
        "override base method"
        if 0 <= index < len(self.stack):
            self.gui.show_frame(self.stack[index])
    #@-node:ekr.20060516135654.174:on_select
    #@+node:ekr.20060516135654.175:on_double
    def on_double(self, index):
        "override base method"
        self.show_source(index)
    #@-node:ekr.20060516135654.175:on_double
    #@+node:ekr.20060516135654.176:goto_source_line
    def goto_source_line(self):
    
        index = self.listbox.index("active")
        self.show_source(index)
    #@-node:ekr.20060516135654.176:goto_source_line
    #@+node:ekr.20060516135654.177:show_stack_frame
    def show_stack_frame(self):
        index = self.listbox.index("active")
        if 0 <= index < len(self.stack):
            self.gui.show_frame(self.stack[index])
    #@-node:ekr.20060516135654.177:show_stack_frame
    #@+node:ekr.20060516135654.178:show_source
    def show_source(self, index):
        if not (0 <= index < len(self.stack)):
            return
        frame, lineno = self.stack[index]
        code = frame.f_code
        filename = code.co_filename
        if os.path.isfile(filename):
            edit = self.flist.open(filename)
            if edit:
                edit.gotoline(lineno)
    #@-node:ekr.20060516135654.178:show_source
    #@-others
#@-node:ekr.20060516135654.169:class StackViewer
#@+node:ekr.20060516135654.179:class NamespaceViewer


class NamespaceViewer:
    #@	@+others
    #@+node:ekr.20060516135654.180:__init__
    def __init__(self, master, title, dict=None):
        
        g.trace('NamespaceViewer','dict',dict,g.callers())
    
        width = 0
        height = 40
        if dict:
            height = 20*len(dict) # XXX 20 == observed height of Entry widget
        self.master = master
        self.title = title
        import repr
        self.repr = repr.Repr()
        self.repr.maxstring = 60
        self.repr.maxother = 60
        self.frame = frame = Tk.Frame(master)
        self.frame.pack(expand=1, fill="both")
        self.label = Tk.Label(frame, text=title, borderwidth=2, relief="groove")
        self.label.pack(fill="x")
        self.vbar = vbar = Tk.Scrollbar(frame, name="vbar")
        vbar.pack(side="right", fill="y")
        self.canvas = canvas = Tk.Canvas(frame,
                                      height=min(300, max(40, height)),
                                      scrollregion=(0, 0, width, height))
        canvas.pack(side="left", fill="both", expand=1)
        vbar["command"] = canvas.yview
        canvas["yscrollcommand"] = vbar.set
        self.subframe = subframe = Tk.Frame(canvas)
        self.sfid = canvas.create_window(0, 0, window=subframe, anchor="nw")
        self.load_dict(dict)
    #@nonl
    #@-node:ekr.20060516135654.180:__init__
    #@+node:ekr.20060516135654.181:load_dict
    dict = -1
    
    def load_dict(self, dict, force=0, rpc_client=None):
        if dict is self.dict and not force:
            return
        subframe = self.subframe
        frame = self.frame
        for c in subframe.children.values():
            c.destroy()
        self.dict = None
        if not dict:
            l = Tk.Label(subframe, text="None")
            l.grid(row=0, column=0)
        else:
            names = dict.keys()
            names.sort()
            row = 0
            for name in names:
                value = dict[name]
                svalue = self.repr.repr(value) # repr(value)
                # Strip extra quotes caused by calling repr on the (already)
                # repr'd value sent across the RPC interface:
                if rpc_client:
                    svalue = svalue[1:-1]
                l = Tk.Label(subframe, text=name)
                l.grid(row=row, column=0, sticky="nw")
                l = Entry(subframe, width=0, borderwidth=0)
                l.insert(0, svalue)
                l.grid(row=row, column=1, sticky="nw")
                row = row+1
        self.dict = dict
        # XXX Could we use a <Configure> callback for the following?
        subframe.update_idletasks() # Alas!
        width = subframe.winfo_reqwidth()
        height = subframe.winfo_reqheight()
        canvas = self.canvas
        self.canvas["scrollregion"] = (0, 0, width, height)
        if height > 300:
            canvas["height"] = 300
            frame.pack(expand=1)
        else:
            canvas["height"] = height
            frame.pack(expand=0)
    
    #@-node:ekr.20060516135654.181:load_dict
    #@+node:ekr.20060516135654.182:close
    def close(self):
        self.frame.destroy()
    #@-node:ekr.20060516135654.182:close
    #@-others
#@-node:ekr.20060516135654.179:class NamespaceViewer
#@+node:ekr.20060516135654.183:class Debugger
class Debugger:

    vstack = vsource = vlocals = vglobals = None

    #@    @+others
    #@+node:ekr.20060516135654.184:Birth
    #@+node:ekr.20060516135654.185:__init__
    def __init__(self, c, interp, idb=None):
        
        self.c = c
        
        # Were inited as needed.
        self.globalsviewer = None
        self.interacting = 0
        self.localsviewer = None
        self.stackviewer = None
    
        ###self.pyshell = pyshell
        self.interp = interp
        self.idb = idb or Idb(self)
        self.frame = None
        
        ### self.flist = pyshell.flist
        self.flist = leo_FileList.FileList(c)
        self.make_gui()
        
        g.trace('Debugger',interp,self.idb)
    #@nonl
    #@-node:ekr.20060516135654.185:__init__
    #@+node:ekr.20060516135654.186:make_gui
    def make_gui(self):
        
        #@    << create the top level frame >>
        #@+node:ekr.20060516135654.187:<< create the top level frame >>
        self.root = root = g.app.root
        self.top = top = Tk.Toplevel(self.root)
        top.title("Leo Debug Control")
        top.wm_iconname("Debug")
        top.wm_protocol("WM_DELETE_WINDOW", self.close)
        # self.top.bind("<Escape>", self.close)
        #@nonl
        #@-node:ekr.20060516135654.187:<< create the top level frame >>
        #@nl
        #@    << create the control buttons >>
        #@+node:ekr.20060516135654.188:<< create the control buttons >>
        self.bframe = bframe = Tk.Frame(top)
        self.bframe.pack(anchor="w")
        self.buttons = bl = []
        #
        self.bcont = b = Tk.Button(bframe, text="Go", command=self.cont)
        bl.append(b)
        self.bstep = b = Tk.Button(bframe, text="Step", command=self.step)
        bl.append(b)
        self.bnext = b = Tk.Button(bframe, text="Over", command=self.next)
        bl.append(b)
        self.bret = b = Tk.Button(bframe, text="Out", command=self.ret)
        bl.append(b)
        self.bret = b = Tk.Button(bframe, text="Quit", command=self.quit)
        bl.append(b)
        #
        for b in bl:
            b.configure(state="disabled")
            b.pack(side="left")
        #@nonl
        #@-node:ekr.20060516135654.188:<< create the control buttons >>
        #@nl
        #@    << create the check boxes >>
        #@+node:ekr.20060516135654.189:<< create the check boxes >>
        self.cframe = cframe = Tk.Frame(bframe)
        self.cframe.pack(side="left")
        
        if not self.vstack:
            self.__class__.vstack = Tk.BooleanVar(top)
            self.vstack.set(1)
        self.bstack = Tk.Checkbutton(cframe,text="Stack",
            command = self.show_stack, variable = self.vstack)
        self.bstack.grid(row=0,column=0)
        
        if not self.vsource:
            self.__class__.vsource = Tk.BooleanVar(top)
        self.bsource = Tk.Checkbutton(cframe,text="Source",
            command = self.show_source, variable = self.vsource)
        self.bsource.grid(row=0,column=1)
        
        if not self.vlocals:
            self.__class__.vlocals = Tk.BooleanVar(top)
            self.vlocals.set(1)
        self.blocals = Tk.Checkbutton(cframe,text="Locals",
            command = self.show_locals, variable = self.vlocals)
        self.blocals.grid(row=1,column=0)
        
        if not self.vglobals:
            self.__class__.vglobals = Tk.BooleanVar(top)
        self.bglobals = Tk.Checkbutton(cframe,text="Globals",
            command = self.show_globals, variable = self.vglobals)
        self.bglobals.grid(row=1,column=1)
        #@nonl
        #@-node:ekr.20060516135654.189:<< create the check boxes >>
        #@nl
        #
        self.status = Tk.Label(top, anchor="w")
        self.status.pack(anchor="w")
        self.error = Tk.Label(top, anchor="w")
        self.error.pack(anchor="w", fill="x")
        self.errorbg = self.error.cget("background")
        #
        self.fstack = Tk.Frame(top, height=1)
        self.fstack.pack(expand=1, fill="both")
        self.flocals = Tk.Frame(top)
        self.flocals.pack(expand=1, fill="both")
        self.fglobals = Tk.Frame(top, height=1)
        self.fglobals.pack(expand=1, fill="both")
        #
        if self.vstack.get():
            self.show_stack()
        if self.vlocals.get():
            self.show_locals()
        if self.vglobals.get():
            self.show_globals()
    #@-node:ekr.20060516135654.186:make_gui
    #@-node:ekr.20060516135654.184:Birth
    #@+node:ekr.20060516135654.190:run
    def run(self, *args):
        
        g.trace('Debugger',args)
    
        try:
            self.interacting = 1
            return self.idb.run(*args)
        finally:
            self.interacting = 0
    #@nonl
    #@-node:ekr.20060516135654.190:run
    #@+node:ekr.20060516135654.191:close
    def close(self, event=None):
    
        if self.interacting:
            self.top.bell()
        else:
            if self.stackviewer:
                self.stackviewer.close()
                self.stackviewer = None
    
            # Clean up pyshell if user clicked debugger control close widget.
            # (Causes a harmless extra cycle through close_debugger() if user
            # toggled debugger from pyshell Debug menu)
            ### self.pyshell.close_debugger()
            self.interp.close_debugger()
        
            # Now close the debugger control window....
            self.top.destroy()
    #@nonl
    #@-node:ekr.20060516135654.191:close
    #@+node:ekr.20060516135654.192:interaction
    def interaction(self, message, frame, info=None):
        
        g.trace('Debugger',message)
        self.frame = frame
        self.status.configure(text=message)
    
        if info:
            type, value, tb = info
            try:
                m1 = type.__name__
            except AttributeError:
                m1 = "%s" % str(type)
            if value is not None:
                try:
                    m1 = "%s: %s" % (m1, str(value))
                except:
                    pass
            bg = "yellow"
        else:
            m1 = ""
            tb = None
            bg = self.errorbg
        self.error.configure(text=m1, background=bg)
        #
        sv = self.stackviewer
        if sv:
            stack, i = self.idb.get_stack(self.frame, tb)
            sv.load_stack(stack, i)
        #
        self.show_variables(1)
        #
        if self.vsource.get():
            self.sync_source_line()
        #
        for b in self.buttons:
            b.configure(state="normal")
        #
        self.top.wakeup()
        self.root.mainloop()
        #
        for b in self.buttons:
            b.configure(state="disabled")
        self.status.configure(text="")
        self.error.configure(text="", background=self.errorbg)
        self.frame = None
    #@nonl
    #@-node:ekr.20060516135654.192:interaction
    #@+node:ekr.20060516135654.193:sync_source_line (used flist)
    def sync_source_line(self):
        
        frame = self.frame
        if not frame:
            return
        filename, lineno = self.__frame2fileline(frame)
        if filename[:1] + filename[-1:] != "<>" and os.path.exists(filename):
            g.trace(filename,lineno)
            if 0: ### Not yet
                f.gotoline(filename,lineno)
                # self.flist.gotofileline(filename, lineno)
    #@nonl
    #@-node:ekr.20060516135654.193:sync_source_line (used flist)
    #@+node:ekr.20060516135654.194:__frame2fileline
    def __frame2fileline(self, frame):
        code = frame.f_code
        filename = code.co_filename
        lineno = frame.f_lineno
        return filename, lineno
    #@-node:ekr.20060516135654.194:__frame2fileline
    #@+node:ekr.20060516135654.195:Callbacks
    #@+node:ekr.20060516135654.196:cont
    def cont(self):
        self.idb.set_continue()
        self.root.quit()
    #@-node:ekr.20060516135654.196:cont
    #@+node:ekr.20060516135654.197:step
    def step(self):
        self.idb.set_step()
        self.root.quit()
    #@-node:ekr.20060516135654.197:step
    #@+node:ekr.20060516135654.198:next
    def next(self):
        self.idb.set_next(self.frame)
        self.root.quit()
    #@-node:ekr.20060516135654.198:next
    #@+node:ekr.20060516135654.199:ret
    def ret(self):
        self.idb.set_return(self.frame)
        self.root.quit()
    #@-node:ekr.20060516135654.199:ret
    #@+node:ekr.20060516135654.200:quit
    def quit(self):
    
        self.idb.set_quit()
        self.root.quit()
    #@nonl
    #@-node:ekr.20060516135654.200:quit
    #@-node:ekr.20060516135654.195:Callbacks
    #@+node:ekr.20060516135654.201:refresh
    #@+node:ekr.20060516135654.202:show_stack
    def show_stack(self):
        
        g.trace(self.stackviewer)
    
        if not self.stackviewer and self.vstack.get():
            self.stackviewer = sv = StackViewer(self.fstack, self.flist, self)
            if self.frame:
                stack, i = self.idb.get_stack(self.frame, None)
                sv.load_stack(stack, i)
        else:
            sv = self.stackviewer
            if sv and not self.vstack.get():
                self.stackviewer = None
                sv.close()
            self.fstack['height'] = 1
    #@-node:ekr.20060516135654.202:show_stack
    #@+node:ekr.20060516135654.203:show_source
    def show_source(self):
    
        if self.vsource.get():
            self.sync_source_line()
    #@-node:ekr.20060516135654.203:show_source
    #@+node:ekr.20060516135654.204:show_frame
    def show_frame(self, (frame, lineno)):
    
        self.frame = frame
        self.show_variables()
    #@-node:ekr.20060516135654.204:show_frame
    #@+node:ekr.20060516135654.205:show_locals
    def show_locals(self):
    
        lv = self.localsviewer
        if self.vlocals.get():
            if not lv:
                self.localsviewer = NamespaceViewer(self.flocals, "Locals")
        else:
            if lv:
                self.localsviewer = None
                lv.close()
                self.flocals['height'] = 1
        self.show_variables()
    #@-node:ekr.20060516135654.205:show_locals
    #@+node:ekr.20060516135654.206:show_globals
    def show_globals(self):
        
        gv = self.globalsviewer
        if self.vglobals.get():
            if not gv:
                self.globalsviewer = NamespaceViewer(self.fglobals, "Globals")
        else:
            if gv:
                self.globalsviewer = None
                gv.close()
                self.fglobals['height'] = 1
        self.show_variables()
    
    #@-node:ekr.20060516135654.206:show_globals
    #@+node:ekr.20060516135654.207:show_variables
    def show_variables(self, force=0):
    
        lv = self.localsviewer
        gv = self.globalsviewer
        frame = self.frame
        if not frame:
            ldict = gdict = None
        else:
            ldict = frame.f_locals
            gdict = frame.f_globals
            if lv and gv and ldict is gdict:
                ldict = None
    
        if 1:
            if lv:
                ### lv.load_dict(ldict, force, self.pyshell.interp.rpcclt)
                lv.load_dict(ldict, force, self.interp.rpcclt)
            if gv:
                ### gv.load_dict(gdict, force, self.pyshell.interp.rpcclt)
                gv.load_dict(gdict, force, self.interp.rpcclt)
    #@-node:ekr.20060516135654.207:show_variables
    #@-node:ekr.20060516135654.201:refresh
    #@+node:ekr.20060516135654.208:breakpoints
    #@+node:ekr.20060516135654.209:set_breakpoint_here
    def set_breakpoint_here(self, filename, lineno):
    
        self.idb.set_break(filename, lineno)
    #@nonl
    #@-node:ekr.20060516135654.209:set_breakpoint_here
    #@+node:ekr.20060516135654.210:clear_breakpoint_here
    def clear_breakpoint_here(self, filename, lineno):
    
        self.idb.clear_break(filename, lineno)
    #@-node:ekr.20060516135654.210:clear_breakpoint_here
    #@+node:ekr.20060516135654.211:clear_file_breaks
    def clear_file_breaks(self, filename):
        
        self.idb.clear_all_file_breaks(filename)
    
    #@-node:ekr.20060516135654.211:clear_file_breaks
    #@+node:ekr.20060516135654.212:load_breakpoints
    def load_breakpoints(self):
        
        g.trace()
        
        if 0: # "Load PyShellEditorWindow breakpoints into subprocess debugger"
            pyshell_edit_windows = self.pyshell.flist.inversedict.keys()
            for editwin in pyshell_edit_windows:
                filename = editwin.io.filename
                try:
                    for lineno in editwin.breakpoints:
                        self.set_breakpoint_here(filename, lineno)
                except AttributeError:
                    continue
    #@nonl
    #@-node:ekr.20060516135654.212:load_breakpoints
    #@-node:ekr.20060516135654.208:breakpoints
    #@-others
#@nonl
#@-node:ekr.20060516135654.183:class Debugger
#@-node:ekr.20060516135654.162:From Debugger.py
#@-others
#@nonl
#@-node:ekr.20060516135654.94:@thin leo_Debugger.py
#@-leo
