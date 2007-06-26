#@+leo-ver=4-thin
#@+node:ajones.20070122153625:@thin expfolder.py
#@<< docstring >>
#@+node:ajones.20070122153625.1:<< docstring >>
'''Makes @expfolder expandable representations of folders in the filesystem.

Double clicking on the icon of an @expfolder heading reads the files in the directory at the path specified and creates child nodes for each file in the subfolder.  Subdirectories are made into child @expfolder nodes so the tree can be easily traversed.  If files have extensions specified in the expfolder.ini file they are made into @text nodes so the content of the files can be easily loaded into leo and edited.  Double clicking a second time will delete all child nodes and refresh the directory listing.  If there are any changed @text nodes contained inside you will be prompted about saving them.

The textextensions field on the expfolder Properties page contains a list of extensions which will be made into @text nodes, seperated by spaces.

For the @text and @expfolder nodes to interact correctly, the textnode plugin must load before the expfolder plugin.  This can be set using the Plugin Manager's Plugin Load Order pane.
'''
#@nonl
#@-node:ajones.20070122153625.1:<< docstring >>
#@nl

#@@language python
#@@tabwidth -4

import leoGlobals as g
import leoPlugins
import os
import os.path
import ConfigParser
from textnode import savetextnode

__version__ = "1.0"

textexts = []

#@+others
#@+node:ajones.20070122154835:init
def init():
    g.plugin_signon(__name__)
    leoPlugins.registerHandler("icondclick1", on_icondclick)

    fileName = os.path.join(g.app.loadDir,"../","plugins","expfolder.ini")
    config = ConfigParser.ConfigParser()
    config.read(fileName)


    textexts.extend(config.get("Main", "TextExtensions").split())

    #g.es("textexts =", str(textexts))

    return 1
#@nonl
#@-node:ajones.20070122154835:init
#@+node:ajones.20070122153625.2:on_icondclick
def on_icondclick(tag, keywords):    
    c = keywords.get("c")
    p = keywords.get("p")
    h = p.headString()
    if g.match_word(h,0,"@expfolder"):
        if p.hasChildren():
            result = g.app.gui.runAskYesNoDialog(c, "Reread?", "Reread contents of folder "+h[11:]+"?")
            if result == "no":
                return
            kids = []
            for cp in p.subtree_iter():
                if cp.isDirty() and g.match_word(cp.headString(), 0, "@text"):
                    kids.append(cp.copy())
            if kids != []:
                result = g.app.gui.runAskYesNoDialog(c, "Reread?", "Save changed @text nodes?")
                if result == "yes":
                    for kid in kids:
                        savetextnode(c, kid)

            # delete children
            while p.firstChild():
                p.firstChild().doDelete()

        #changed = c.isChanged()
        dir = h[11:]
        dirs = []
        files = []
        for file in os.listdir(dir):
            path = os.path.join(dir, file)
            if os.path.isdir(path):
                dirs.append(path)
            else:
                files.append(path)

        #g.es('dirs: '+str(dirs))
        #g.es('files: '+str(files))

        dirs.sort()
        files.sort()

        for f in files:
            pn = p.insertAsNthChild(0)
            if os.path.splitext(f)[1] in textexts:
                c.setHeadString(pn, "@text "+f)
                pn.clearDirty()
            else:
                c.setHeadString(pn, f)
            #pn.clearDirty()

        for d in dirs:
            pn = p.insertAsNthChild(0)
            c.setHeadString(pn, "@expfolder "+d)
            #pn.clearDirty()

        #p.clearDirty()

        #c.setChanged(changed)

        c.expandSubtree(p)
#@nonl
#@-node:ajones.20070122153625.2:on_icondclick
#@-others
#@nonl
#@-node:ajones.20070122153625:@thin expfolder.py
#@-leo
