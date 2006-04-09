#@+leo-ver=4-thin
#@+node:edream.110203113231.873:@thin at_folder.py
#@<< docstring >>
#@+node:edream.110203113231.874:<< docstring >>
'''Synchronize @folder nodes with folders.

If a node is named '@folder path_to_folder', the content (filenames) of the
folder and the children of that node will be sync. Whenever a new file is put
there, a new node will appear on top of the children list (with mark). So that
I can put my description (ie. annotation) as the content of that node. In this
way, I can find any files much easier from leo.

Moreover, I add another feature to allow you to group files(in leo) into
children of another group. This will help when there are many files in that
folder. You can logically group it in leo (or even clone it to many groups),
while keep every files in a flat/single directory on your computer.
'''
#@nonl
#@-node:edream.110203113231.874:<< docstring >>
#@nl

#@@language python
#@@tabwidth -4

import leoGlobals as g
import leoPlugins
import os  # added JD 2004-09-10

__version__ = "1.3"

#@+others
#@+node:edream.110203113231.875:sync_node_to_folder
def sync_node_to_folder(parent,d):

    oldlist = {}
    newlist = []
    #get children info
    v = parent
    after_v = parent.nodeAfterTree()
    while v != after_v:
        if not v.hasChildren():
            oldlist[v.headString()] = v.bodyString()
        v = v.threadNext()
    #compare folder content to children
    for name in os.listdir(d):
        if name in oldlist:
            del oldlist[name]
        else:
            newlist.append(name)
    #insert newlist
    newlist.sort()
    newlist.reverse()
    for name in newlist:
        v = parent.insertAsNthChild(0)
        v.setHeadStringOrHeadline(name)
        v.setMarked()
    #warn for orphan oldlist
    if len(oldlist)>0:
        g.es('missing: '+','.join(oldlist.keys()))
#@-node:edream.110203113231.875:sync_node_to_folder
#@-others

def onSelect (tag,keywords):
    v = keywords.get("new_v")
    h = v.headString()
    if g.match_word(h,0,"@folder"):
        sync_node_to_folder(v,h[8:])
        
if 1: # Ok for unit testing.
    leoPlugins.registerHandler("select1", onSelect)
    g.plugin_signon(__name__)
#@nonl
#@-node:edream.110203113231.873:@thin at_folder.py
#@-leo
