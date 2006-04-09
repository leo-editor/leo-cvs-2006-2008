#@+leo-ver=4-thin
#@+node:EKR.20040517075715.12:@thin xemacs.py
'''This plugin allows you to edit nodes in emacs/xemacs.

Important: the open_with plugin must be enabled for this plugin to work properly.

Depending on your preference, selecting or double-clicking a node will pass the
body text of that node to emacs. You may edit the node in the emacs buffer and
changes will appear in Leo. '''

#@@language python
#@@tabwidth -4

#@<< imports >>
#@+node:ekr.20050218024153:<< imports >>
import leoGlobals as g
import leoPlugins
import os
import sys
#@nonl
#@-node:ekr.20050218024153:<< imports >>
#@nl
__version__ = "1.11"
#@<< version history >>
#@+node:ekr.20050218024153.1:<< version history >>
#@@killcolor
#@+at
# 
# Initial version: http://www.cs.mu.oz.au/~markn/leo/external_editors.leo
# 
# 1.5 EKR:
#     - Added commander-specific callback in onCreate.
#     - Added init method.
# 1.6 MCM
#     - Added sections from Vim mode and some clean-up.
# 1.7 EKR:
#     - Select _emacs_cmd using sys.platform.
# 1.8 EKR:
#     - Get c from keywords, not g.top().
#     - Simplified the search of g.app.openWithFiles.
#     - Fixed bug in open_in_emacs: hanged v.bodyString to v.bodyString()
# 1.9 EKR:
#     - Installed patch from mackal to find client on Linux.
#       See http://sourceforge.net/forum/message.php?msg_id=3219471
# 1.10 EKR:
#     - Corrected the call to openWith.  It must now use data=data due to a 
# new event param.
# 1.11 EKR:
#     - The docstring now states that the open_with plugin must be enabled for 
# this to work.
#@-at
#@nonl
#@-node:ekr.20050218024153.1:<< version history >>
#@nl

useDoubleClick = True

# Full path of emacsclient executable. We need the full path as spawnlp
# is not yet implemented in leoCommands.py

if sys.platform == "win32":
    # This path must not contain blanks in XP.  Sheesh.
    _emacs_cmd = r"c:\XEmacs\XEmacs-21.4.13\i586-pc-win32\xemacs.exe"
elif sys.platform.startswith("linux"):
    clients = ["gnuclient", "emacsclient", "xemacs"]
    _emacs_cmd = ""
    for client in clients:
        path = "/usr/bin/"+client
        if os.path.exists(path):
            _emacs_cmd = path
            break
    if not _emacs_cmd:
        print >> sys.stderr, "Unable to locate a usable version of *Emacs"
else:
    _emacs_cmd = "/Applications/Emacs.app/Contents/MacOS/bin/emacsclient"

#@+others
#@+node:ekr.20050218023308:init
def init ():

    ok = True

    if g.app.unitTesting:
        print "\nEmacs plugin installed: double clicking will start..."

    if useDoubleClick: # Open on double click
        leoPlugins.registerHandler("icondclick2", open_in_emacs)
    else: # Open on single click: interferes with dragging.
        leoPlugins.registerHandler("iconclick2", open_in_emacs,val=True)

    if g.app.unitTesting:
        os.system(_emacs_cmd)
    
    g.plugin_signon(__name__)
    
    return ok
#@nonl
#@-node:ekr.20050218023308:init
#@+node:ekr.20050313071202:open_in_emacs
def open_in_emacs (tag,keywords,val=None):
    
    c = keywords.get('c')
    p = keywords.get('p')
    if not c or not p: return
    v = p.v

    # Search g.app.openWithFiles for a file corresponding to v.
    for d in g.app.openWithFiles:
        if d.get('v') == id(v):
            path = d.get('path','') ; break
    else: path = ''

    if (
        not g.os_path_exists(path) or
        not hasattr(v,'OpenWithOldBody') or
        v.bodyString() != v.OpenWithOldBody
    ):
        # Open a new temp file.
        if path:
            # Remove the old file and the entry in g.app.openWithFiles.
            os.remove(path)
            g.app.openWithFiles = [d for d in g.app.openWithFiles if d.get('path') != path]
            os.system(_emacs_cmd)
        v.OpenWithOldBody=v.bodyString() # Remember the old contents
        # open the node in emacs (note the space after _emacs_cmd)
        data = "os.spawnl", _emacs_cmd, None
        c.openWith(data=data)
    else:
        # Reopen the old temp file.
        os.system(_emacs_cmd)

    return val
#@nonl
#@-node:ekr.20050313071202:open_in_emacs
#@-others
#@nonl
#@-node:EKR.20040517075715.12:@thin xemacs.py
#@-leo
