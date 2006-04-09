#@+leo-ver=4-thin
#@+node:ekr.20040422072343:@thin rClick.py
"""Create a context menu when right-clicking in the body pane."""

# Send bug reports to
# http://sourceforge.net/forum/forum.php?thread_id=980723&forum_id=10228

#@<< version history >>
#@+node:ekr.20040422081253:<< version history >>
#@+at
# 0.1, 0.2: Created by 'e'.
# 0.3 EKR:
#     - Converted to 4.2 code style. Use @file node.
#     - Simplified rClickBinder, rClicker, rc_help.  Disabled signon.
#     - Removed calls to registerHandler, "by" ivar, rClickNew, and shutdown 
# code.
#     - Added select all item for the log pane.
# 0.4 Maxim Krikun:
#     - added context-dependent commands:
#        open url, jump to reference, pydoc help
#     - replaced rc_help with context-dependent pydoc help;
#     - rc_help was not working for me :(
# 0.5 EKR:
#     - Style changes.
#     - Help sends output to console as well as log pane.
#     - Used code similar to rc_help code in getdoc.
#       Both kinds of code work for me (using 4.2 code base)
#     - Simplified crop method.
# 0.6 EKR:
#     - Use g.importExtension to import Tk.
# 0.7 EKR:
#     - Use e.widget._name.startswith('body') to test for the body pane.
# 0.8 EKR:
# - Added init function.
# - Eliminated g.top.
# 0.9 EKR:
# - Define callbacks so that all are accessible.
# 0.10 EKR:
# - Removed call to str that was causing a unicode error.
#@-at
#@nonl
#@-node:ekr.20040422081253:<< version history >>
#@nl
#@<< imports >>
#@+node:ekr.20050101090207.2:<< imports >>
import leoGlobals as g
import leoPlugins

Tk = g.importExtension('Tkinter')

import re
import sys
#@-node:ekr.20050101090207.2:<< imports >>
#@nl
__version__ = "0.10"

#@+others
#@+node:ekr.20060108122501:Module-level
#@+node:ekr.20060108122501.1:init
def init ():
    
    if Tk: # OK for unit tests.
    
        if g.app.gui is None:
            g.app.createTkGui(__file__)
    
        if g.app.gui.guiName() == "tkinter":
            leoPlugins.registerHandler("after-create-leo-frame",rClickbinder)
            leoPlugins.registerHandler("bodyrclick1",rClicker)
            g.plugin_signon(__name__)
            
    return Tk is not None
#@nonl
#@-node:ekr.20060108122501.1:init
#@+node:ekr.20040422072343.5:rClickbinder
def rClickbinder(tag,keywords):

    c = keywords.get('c')
    
    if c and c.exists:
        c.frame.log.logCtrl.bind  ('<Button-3>',c.frame.OnBodyRClick)
        # c.frame.body.bodyCtrl.bind('<Button-3>',c.frame.OnBodyRClick)
#@nonl
#@-node:ekr.20040422072343.5:rClickbinder
#@+node:ekr.20040422072343.6:rClicker
# EKR: it is not necessary to catch exceptions or to return "break".

def rClicker(tag,keywords):
    
    c = keywords.get("c")
    e = keywords.get("event")
    if not c or not c.exists or not e: return

    e.widget.focus()

    #@    << define callbacks >>
    #@+node:ekr.20060110123700:<< define callbacks >>
    def rc_helpCallback(c=c):       rc_help(c)
    def rc_dbodyCallback(c=c):      rc_dbody(c)
    def rc_nlCallback(c=c):         rc_nl(c)
    def rc_selectAllCallback(c=c):  rc_selectAll(c)
    #@nonl
    #@-node:ekr.20060110123700:<< define callbacks >>
    #@nl
    if e.widget._name.startswith('body'):
        #@        << define commandList for body >>
        #@+node:ekr.20040422072343.7:<< define commandList for body >>
        commandList = [
            #('-||-|-||-',None),   #
            #('U',c.undoer.undo),  #no c.undoer
            #('R',undoer.redo),
            # ('-',None),
            ('Cut', c.frame.OnCutFromMenu), 
            ('Copy',c.frame.OnCopyFromMenu),
            ('Paste', c.frame.OnPasteFromMenu),
            ('Delete',rc_dbodyCallback),
            ('-',None),
            ('SelectAll',c.frame.body.selectAllText),
            ('Indent',c.indentBody),
            ('Dedent',c.dedentBody),  
            ('Find Bracket',c.findMatchingBracket),
            ('Insert newline', rc_nlCallback),
            
            # this option seems not working, at least in win32
            # replaced with context-sensitive "pydoc help"  --Maxim Krikun
            # ('Help(txt)',rc_helpCallback),   #how to highlight 'txt' in the menu?
            
            ('Execute Script',c.executeScript)
            # ('-||-|-||-',None),   # 1st & last needed because of freaky sticky finger
            ]
        #@nonl
        #@-node:ekr.20040422072343.7:<< define commandList for body >>
        #@nl
        #@        << add entries for context sensitive commands in body >>
        #@+node:ekr.20040422072343.8:<< add entries for context sensitive commands in body >>
        #@+at 
        #@nonl
        # Context-sensitive rclick commands.
        # 
        # On right-click get the selected text, or the whole line containing 
        # cursor if no selection.
        # Scan this text for certain regexp pattern. For each occurrence of a 
        # pattern add a command,
        # which name and action depend on the text matched.
        # 
        # Example below extracts URL's from the text and puts "Open URL:..." 
        # th menu.
        # 
        #@-at
        #@@c
        
        #@<< get text and word from the body text >>
        #@+node:ekr.20040422073911:<< get text and word from the body text >>
        text = c.frame.body.getSelectedText()
        if text:
            word = text.strip()
        else:
            ind0,ind1=c.frame.body.getTextSelection()
            n0,p0=ind0.split('.',2)
            n1,p1=ind1.split('.',2)
            assert n0==n1
            assert p0==p1
            text=c.frame.body.getTextRange(n0+".0",n1+".end")
            word=getword(text,int(p0))
        #@nonl
        #@-node:ekr.20040422073911:<< get text and word from the body text >>
        #@nl
        
        if 0:
            g.es("selected text: "+text)
            g.es("selected word: "+repr(word))
        
        contextCommands=[]
        
        #@<< add entry for open url >>
        #@+node:ekr.20040422072343.13:<< add entry for open url >>
        scan_url_re="""(http|https|ftp)://([^/?#\s'"]*)([^?#\s"']*)(\\?([^#\s"']*))?(#(.*))?"""
        
        for match in re.finditer(scan_url_re, text):
            
            #get the underlying text
            url=match.group()
            
            #create new command callback
            def url_open_command(*k,**kk):
                import webbrowser
                try:
                    webbrowser.open_new(url)
                except:
                    g.es("not found: " + url,color='red')
        
            #add to menu
            menu_item=( 'Open URL: '+crop(url,30), url_open_command)
            contextCommands.append( menu_item )
        #@nonl
        #@-node:ekr.20040422072343.13:<< add entry for open url >>
        #@nl
        #@<< add entry for jump to section >>
        #@+node:ekr.20040422072343.14:<< add entry for jump to section >>
        scan_jump_re="<"+"<[^<>]+>"+">"
        
        p=c.currentPosition()
        for match in re.finditer(scan_jump_re,text):
            name=match.group()
            ref=g.findReference(name,p)
            if ref:
                # Bug fix 1/8/06: bind c here.
                # This is safe because we only get called from the proper commander.
                def jump_command(c=c,*k,**kk):
                    c.beginUpdate()
                    c.selectPosition(ref)
                    c.endUpdate()
                menu_item=( 'Jump to: '+crop(name,30), jump_command)
                contextCommands.append( menu_item )
            else:
                # could add "create section" here?
                pass
        #@nonl
        #@-node:ekr.20040422072343.14:<< add entry for jump to section >>
        #@nl
        if word:
            #@    << add epydoc help >>
            #@+node:ekr.20040422072343.15:<< add epydoc help >>
            def help_command(*k,**kk):
                # g.trace(word)
                try:
                    doc=getdoc(word,"="*60+"\nHelp on %s")
                    # It would be nice to save log pane position
                    # and roll log back to make this position visible,
                    # since the text returned by pydoc can be several 
                    # pages long
                    g.es(doc,color="blue")
                    print doc
                except Exception, value:
                    g.es(str(value),color="red")
            
            menu_item=('Help on: '+crop(word,30), help_command)
            contextCommands.append( menu_item )
            #@nonl
            #@-node:ekr.20040422072343.15:<< add epydoc help >>
            #@nl
        
        if contextCommands:
            commandList.append(("-",None))
            commandList.extend(contextCommands)
        #@nonl
        #@-node:ekr.20040422072343.8:<< add entries for context sensitive commands in body >>
        #@nl
    else:
        #@        << define commandList for log pane >>
        #@+node:ekr.20040422072343.16:<< define commandList for log pane >>
        commandList=[
            ('Cut', c.frame.OnCutFromMenu), 
            ('Copy',c.frame.OnCopyFromMenu),
            ('Paste', c.frame.OnPasteFromMenu),
            ('Select All', rc_selectAllCallback)]
        #@nonl
        #@-node:ekr.20040422072343.16:<< define commandList for log pane >>
        #@nl
                
    rmenu = Tk.Menu(None,tearoff=0,takefocus=0)
    for (txt,cmd) in commandList:
        if txt == '-':
            rmenu.add_separator()
        else:
            rmenu.add_command(label=txt,command=cmd)

    rmenu.tk_popup(e.x_root-23,e.y_root+13)
#@nonl
#@-node:ekr.20040422072343.6:rClicker
#@-node:ekr.20060108122501:Module-level
#@+node:ekr.20040422072343.1:rc_help
def rc_help(c):
    
    """Highlight txt then rclick for python help() builtin."""
    
    if c.frame.body.hasTextSelection():

        newSel = c.frame.body.getSelectedText()

        # EKR: nothing bad happens if the status line does not exist.
        c.frame.clearStatusLine()
        c.frame.putStatusLine(' Help for '+newSel) 
    
        # Redirect stdout to a "file like object".
        sys.stdout = fo = g.fileLikeObject()
    
        # Python's builtin help function writes to stdout.
        help(str(newSel))
        
        # Restore original stdout.
        sys.stdout = sys.__stdout__

        # Print what was written to fo.
        s = fo.get() ; g.es(s) ; print s
#@nonl
#@-node:ekr.20040422072343.1:rc_help
#@+node:ekr.20040422072343.2:rc_dbody
def rc_dbody(c):

    if c.frame.body.hasTextSelection():
        c.frame.body.deleteTextSelection()
        c.frame.body.onBodyChanged("Delete")
#@nonl
#@-node:ekr.20040422072343.2:rc_dbody
#@+node:ekr.20040422072343.3:rc_nl
def rc_nl(c):
    
    """Insert a newline at the current curser position."""

    c.frame.body.insertAtInsertPoint('\n')
    c.frame.body.onBodyChanged("Typing")
#@nonl
#@-node:ekr.20040422072343.3:rc_nl
#@+node:ekr.20040422072343.4:rc_selectAll
def rc_selectAll(c):
    
    """Select the entire log pane."""
    
    g.app.gui.setTextSelection(c.frame.log.logCtrl,"1.0","end")
#@nonl
#@-node:ekr.20040422072343.4:rc_selectAll
#@+node:ekr.20040422072343.9:Utils for context sensitive commands
#@+node:ekr.20040422072343.10:crop
def crop(s,n=20,end="..."):

    """return a part of string s, no more than n characters; optionally add ... at the end"""
    
    if len(s)<=n:
        return s
    else:
        return s[:n]+end # EKR
#@nonl
#@-node:ekr.20040422072343.10:crop
#@+node:ekr.20040422072343.11:getword
def getword(s,pos):

    """returns a word in string s around position pos"""

    for m in re.finditer("\w+",s):
        if m.start()<=pos and m.end()>=pos:
            return m.group()
    return None			
#@-node:ekr.20040422072343.11:getword
#@+node:ekr.20040422072343.12:getdoc
def getdoc(thing, title='Help on %s', forceload=0):
    
    #g.trace(thing)

    if 1: # Both seem to work.

        # Redirect stdout to a "file like object".
        old_stdout = sys.stdout
        sys.stdout = fo = g.fileLikeObject()
        # Python's builtin help function writes to stdout.
        help(str(thing))
        # Restore original stdout.
        sys.stdout = old_stdout
        # Return what was written to fo.
        return fo.get()

    else:
        # Similar to doc function from pydoc module.
        from pydoc import resolve, describe, inspect, text, plain
        object, name = resolve(thing, forceload)
        desc = describe(object)
        module = inspect.getmodule(object)
        if name and '.' in name:
            desc += ' in ' + name[:name.rfind('.')]
        elif module and module is not object:
            desc += ' in module ' + module.__name__
        doc = title % desc + '\n\n' + text.document(object, name)
        return plain(doc)
#@nonl
#@-node:ekr.20040422072343.12:getdoc
#@-node:ekr.20040422072343.9:Utils for context sensitive commands
#@-others
#@nonl
#@-node:ekr.20040422072343:@thin rClick.py
#@-leo
