#@+leo-ver=4-thin
#@+node:ekr.20040331151007:@thin niceNosent.py
"""Preprocess @file-nosent nodes: make sure each subnode ends
with exactly one newline, replace all tabs with spaces, and
add a newline before class and functions in the derived file.
"""

#@@language python
#@@tabwidth -4

__version__ = "0.3"
#@<< version history >>
#@+node:ekr.20040909122647:<< version history >>
#@+at
# 
# 0.2 EKR:
#     - Use isAtNoSentinelsFileNode and atNoSentinelsFileNodeName.
#     - Use g.os_path_x methods for better unicode support.
# 0.3 EKR:
#     - Converted to 4.2 code base:
#         - Use keywords.get('c') instead of g.top().
#         - Use explicit positions everywhere.
#         - removed reference to new_df.
#@-at
#@nonl
#@-node:ekr.20040909122647:<< version history >>
#@nl
#@<< imports >>
#@+node:ekr.20040909122647.1:<< imports >>
import leoGlobals as g
import leoPlugins
import os
#@nonl
#@-node:ekr.20040909122647.1:<< imports >>
#@nl

NSPACES = ' '*4
nosentNodes = []

#@+others
#@+node:ekr.20050917082031:init
def init ():
    
    # Don't bother with unit testing.
    return not g.app.unitTesting
#@nonl
#@-node:ekr.20050917082031:init
#@+node:ekr.20040331151007.1:onPreSave
def onPreSave(tag=None, keywords=None):

    """Before saving a nosentinels file, make sure that all nodes have a blank line at the end."""
    
    global nosentNodes
    c = keywords.get('c')
    if c:
        for p in c.allNodes_iter():
            if p.isAtNoSentinelsFileNode() and p.isDirty():
                nosentNodes.append(p.copy())
                for p2 in p.self_and_subtree_iter():
                    s = p2.bodyString()
                    lastline = s.split("\n")[-1]
                    if lastline.strip():
                        p2.setBodyStringOrPane(s+"\n")
#@nonl
#@-node:ekr.20040331151007.1:onPreSave
#@+node:ekr.20040331151007.2:onPostSave
def onPostSave(tag=None, keywords=None):
    """After saving a nosentinels file, replace all tabs with spaces."""
    
    global nosentNodes
    c = keywords.get('c')
    if c:
        at = c.atFileCommands
        for p in nosentNodes:
            g.es("node %s found" % p.headString(), color="red")
            at.scanAllDirectives(p)
            name = p.atNoSentinelsFileNodeName()
            fname = g.os_path_join(at.default_directory,name)
            f = open(fname,"r")
            lines = f.readlines()
            f.close()
            #@            << add a newline before def or class >>
            #@+node:ekr.20040331151007.3:<< add a newline before def or class >>
            for i in range(len(lines)):
                ls = lines[i].lstrip()
                if ls.startswith("def ") or ls.startswith("class "):
                    try:
                        if lines[i-1].strip() != "":
                            lines[i] = "\n" + lines[i]
                    except IndexError:
                        pass
            #@nonl
            #@-node:ekr.20040331151007.3:<< add a newline before def or class >>
            #@nl
            #@            << replace tabs with spaces >>
            #@+node:ekr.20040331151007.4:<< replace tabs with spaces >>
            s = ''.join(lines)
            fh = open(fname,"w")
            fh.write(s.replace("\t",NSPACES))
            fh.close()
            #@nonl
            #@-node:ekr.20040331151007.4:<< replace tabs with spaces >>
            #@nl

    nosentNodes = []
#@nonl
#@-node:ekr.20040331151007.2:onPostSave
#@-others

if 1: # Should be safe for unit testing.  Only works on @nosent files.

    leoPlugins.registerHandler("save1",onPreSave)
    leoPlugins.registerHandler("save2",onPostSave)
    g.plugin_signon(__name__)
#@nonl
#@-node:ekr.20040331151007:@thin niceNosent.py
#@-leo
