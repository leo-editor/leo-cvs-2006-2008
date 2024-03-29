#@+leo-ver=4-thin
#@+node:ajones.20070122160142:@thin textnode.py
#@<< docstring >>
#@+node:ajones.20070122160142.1:<< docstring >>
'''The @text node is for embedding text files in a leo node that won't be saved with the leo file, and won't contain any sentinel leo comments.  Children of @text nodes are not saved with the derived file, though they will stay in the outline.  When a outline is first loaded any @text nodes are filled with the contents of the text files on disk.  To refresh the contents of an @text node, double click on the heading icon.
'''
#@nonl
#@-node:ajones.20070122160142.1:<< docstring >>
#@nl

#@@language python
#@@tabwidth -4

import leoGlobals as g
import leoPlugins
import os.path
__version__ = "1.1"
    # Terry Brown: support for @path ancestors and uses universal newline mode for opening.

#@+others
#@+node:ajones.20070122160142.2:init
def init():
    leoPlugins.registerHandler(('new','open2'), on_open)
    leoPlugins.registerHandler("save1", on_save)
    leoPlugins.registerHandler("save2", on_open)
    leoPlugins.registerHandler("icondclick1", on_icondclick)

    g.plugin_signon(__name__)

    return 1
#@nonl
#@-node:ajones.20070122160142.2:init
#@+node:ajones.20070122181914:on_icondclick
def on_icondclick(tag, keywords):
    c = keywords['c']
    p = keywords['p']
    h = p.headString()
    if g.match_word(h,0,"@text"): 
        if p.bodyString() != "":
            result = g.app.gui.runAskYesNoDialog(c, "Query", "Read from file "+h[6:]+"?")
            if result == "no":
                return
        readtextnode(c, p)
#@nonl
#@-node:ajones.20070122181914:on_icondclick
#@+node:ajones.20070122160142.3:on_open
def on_open(tag,keywords):
    c = keywords.get("c")
    if not c: return

    c.beginUpdate()
    for p in c.allNodes_iter():
        h = p.headString()
        if g.match_word(h,0,"@text"):
            readtextnode(c, p)
    c.endUpdate()
#@-node:ajones.20070122160142.3:on_open
#@+node:ajones.20070122161942:on_save
def on_save(tag,keywords):
    c = keywords.get("c")
    if not c: return

    for p in c.allNodes_iter():
        h = p.headString()
        if g.match_word(h,0,"@text") and p.isDirty():
            savetextnode(c, p)
            c.setBodyString(p, "")
#@nonl
#@-node:ajones.20070122161942:on_save
#@+node:tbrown.20080128221824:getPath
def getPath(c,p):
    path = [i.headString()[6:] for i in p.self_and_parents_iter()
            if i.headString()[:6] in ('@path ', '@text ')]
    path.append(g.getBaseDirectory(c))
    path.reverse()
    return os.path.join(*path)
#@nonl
#@-node:tbrown.20080128221824:getPath
#@+node:ajones.20070122181914.1:readtextnode
def readtextnode(c, p):
    changed = c.isChanged()

    name = getPath(c,p)

    try:
        file = open(name,"rU")
        g.es("..." + name)
        c.setBodyString(p, file.read())
        p.clearDirty()
        c.setChanged(changed)
        file.close()
    except IOError,msg:
        g.es("error reading %s: %s" % (name, msg))
        g.es("...not found: " + name)
        c.setBodyString(p,"") # Clear the body text.
        p.setDirty()
#@-node:ajones.20070122181914.1:readtextnode
#@+node:ajones.20070122185020:savetextnode
def savetextnode(c, p):
    name = getPath(c,p)
    try:
        file = open(name,"w")
        g.es("writing " + name)
        file.write(p.bodyString())
        file.close()
    except IOError,msg:
        g.es("error writing %s: %s" % (name, msg))
        p.setDirty()
        p.setMarked(1)
#@nonl
#@-node:ajones.20070122185020:savetextnode
#@-others
#@nonl
#@-node:ajones.20070122160142:@thin textnode.py
#@-leo
