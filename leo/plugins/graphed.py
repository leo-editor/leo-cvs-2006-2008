#@+leo-ver=4-thin
#@+node:ekr.20071004090250:@thin graphed.py
#@<< docstring >>
#@+node:ekr.20071004090250.1:<< docstring >>
"""
graphed.py  -- Edit graphs visually

Based on the Gred graph editor from the Gato Graph Animation Toolbox
at http://gato.sourceforge.net/

"""
#@-node:ekr.20071004090250.1:<< docstring >>
#@nl

#@@language python
#@@tabwidth -4
#@@nowrap

__version__ = "0.1"

#@<< imports >>
#@+node:ekr.20071004090250.2:<< imports >>
import leoGlobals as g
import leoPlugins
import leoTkinterTree

Tk = g.importExtension('Tkinter',pluginName=__name__,verbose=True)

import sys

gato_path = g.os_path_join(g.app.loadDir,'..','extensions','Gato')

if gato_path not in sys.path:
    sys.path.append(gato_path)

# GATO_path = "/home/tbrown/Desktop/Package/Gato"
# 
# if GATO_path not in sys.path:
#     sys.path.append(GATO_path)

try:
    from Gato import Gred, Embedder, Graph, GraphEditor, DataStructures
    Gato_ok = True
except:
    Gato_ok = False
    g.es_print('ERROR: graphed: could not import Gato')
#@-node:ekr.20071004090250.2:<< imports >>
#@nl
#@<< version history >>
#@+node:ekr.20071004090250.3:<< version history >>
#@@killcolor

#@+at 
#@nonl
# Use and distribute under the same terms as leo itself.
# 
# 0.0 - initial version
# 
# 0.1 EKR:
# - reassigned all gnx's (by cutting and pasting the
# entire @thin node) to avoid conflict with cleo (!!)
# 
# - Add leo/extensions/Gato to sys.path before importing from Gato.
#@-at
#@-node:ekr.20071004090250.3:<< version history >>
#@nl

#@+others
#@+node:ekr.20071004090250.9:init
def init():

    if Tk is None:
        return False

    if not Gato_ok:
        g.es('graphed: Gato import failed',color='red')
        return False

    leoPlugins.registerHandler('after-create-leo-frame', onCreate)
    g.plugin_signon(__name__)

    return True
#@-node:ekr.20071004090250.9:init
#@+node:ekr.20071004090250.10:onCreate
def onCreate (tag,key):
    GraphEd(key['c'])
#@-node:ekr.20071004090250.10:onCreate
#@+node:ekr.20071004090250.11:class GraphEd
class GraphEd:

    '''A per-commander class that recolors outlines.'''

    #@    @+others
    #@+node:ekr.20071004090250.12:__init__
    def __init__ (self,c):

        self.dictName = 'graphed'  # for uA dictionary

        self.c = c
        table = (("Edit node as graph",None,self.editGraph),
                 # BROKEN ("Edit whole tree as graph",None,self.editWholeTree),
                 ("Copy link to clipboard",None,self.copyLink),
                 ("Follow link",None,self.followLink),
                 ("Export to Graphviz dot format",None,self.undone), # FIXME
                 ("Make Graphviz dot node",None,self.undone), # FIXME
                 ("Layout using Graphviz dot",None,self.undone), # FIXME
                 )
        c.frame.menu.createNewMenu('Graph', 'Outline')
        c.frame.menu.createMenuItemsFromTable('Graph', table)
    #@-node:ekr.20071004090250.12:__init__
    #@+node:ekr.20071004090250.13:close
    def close(self, tag, key):
        "unregister handlers on closing commander"

        if self.c != key['c']: return  # not our problem

        for i in self.handlers:
            pass # FIXME no handlers?

    #@-node:ekr.20071004090250.13:close
    #@+node:ekr.20071004090250.14:setIndex
    def setIndex(self, p):
        try:
            theId,time,n = p.v.t.fileIndex
        except TypeError:
            p.v.t.fileIndex = g.app.nodeIndices.getNewIndex()
    #@-node:ekr.20071004090250.14:setIndex
    #@+node:ekr.20071004090250.15:indexStrFromStr
    def indexStrFromStr(self, s):
        """isolate the '(...)' part of s"""
        return s[s.find('(') : s.find(')')+1]
    #@-node:ekr.20071004090250.15:indexStrFromStr
    #@+node:ekr.20071004090250.16:attributes...
    #@+node:ekr.20071004090250.17:getat
    def getat(self, node, attrib):

        if (not hasattr(node,'unknownAttributes') or
            not node.unknownAttributes.has_key(self.dictName) or
            not type(node.unknownAttributes[self.dictName]) == type({}) or
            not node.unknownAttributes[self.dictName].has_key(attrib)):

            return None

        return node.unknownAttributes[self.dictName][attrib]
    #@nonl
    #@-node:ekr.20071004090250.17:getat
    #@+node:ekr.20071004090250.18:setat
    def setat(self, node, attrib, val):
        "new attrbiute setter"

        #X isDefault = self.testDefault(attrib, val)

        if (not hasattr(node,'unknownAttributes') or
            not node.unknownAttributes.has_key(self.dictName) or
            type(node.unknownAttributes[self.dictName]) != type({})):
            # dictionary doesn't exist

            #X if isDefault:
            #X     return  # don't create dict. for default value

            if not hasattr(node,'unknownAttributes'):  # node has no unknownAttributes
                node.unknownAttributes = {}
                node.unknownAttributes[self.dictName] = {}
            else:  # our private dictionary isn't present
                if (not node.unknownAttributes.has_key(self.dictName) or
                    type(node.unknownAttributes[self.dictName]) != type({})):
                    node.unknownAttributes[self.dictName] = {}

            node.unknownAttributes[self.dictName][attrib] = val

            return

        # dictionary exists

        node.unknownAttributes[self.dictName][attrib] = val

        #X if isDefault:  # check if all default, if so drop dict.
        #X     self.dropEmpty(node, dictOk = True)
    #@-node:ekr.20071004090250.18:setat
    #@+node:ekr.20071004090250.19:probably junk
    #@+at
    # 
    # These probably aren't needed for this app, but maybe we'll need to
    # offer an option to strip our uAs
    #@-at
    #@+node:ekr.20071004090250.20:delUD
    def delUD (self,node,udict=None):

        ''' Remove our dict from the node'''

        if udict == None: udict = self.dictName
        if (hasattr(node,"unknownAttributes" ) and 
            node.unknownAttributes.has_key(udict)):

            del node.unknownAttributes[udict]
    #@-node:ekr.20071004090250.20:delUD
    #@+node:ekr.20071004090250.21:hasUD
    def hasUD (self,node,udict=None):

        ''' Return True if the node has an UD.'''

        if udict == None: udict = self.dictName
        return (
            hasattr(node,"unknownAttributes") and
            node.unknownAttributes.has_key(udict) and
            type(node.unknownAttributes.get(udict)) == type({}) # EKR
        )
    #@-node:ekr.20071004090250.21:hasUD
    #@+node:ekr.20071004090250.22:testDefault
    def testDefault(self, attrib, val):
        "return true if val is default val for attrib"

        # if type(val) == self.typePickle: val = val.get()
        # not needed as only dropEmpty would call with such a thing, and it checks first

        return attrib == "priority" and val == 9999 or val == ""
    #@nonl
    #@-node:ekr.20071004090250.22:testDefault
    #@+node:ekr.20071004090250.23:dropEmptyAll
    def dropEmptyAll(self):
        "search whole tree for empty nodes"

        cnt = 0
        for p in self.c.allNodes_iter(): 
            if self.dropEmpty(p.v): cnt += 1

        g.es("cleo: dropped %d empty dictionaries" % cnt)
    #@-node:ekr.20071004090250.23:dropEmptyAll
    #@+node:ekr.20071004090250.24:dropEmpty
    def dropEmpty(self, node, dictOk = False):

        if (dictOk or
            hasattr(node,'unknownAttributes') and
            node.unknownAttributes.has_key(self.dictName) and
            type(node.unknownAttributes[self.dictName]) == type({})):

            isDefault = True
            for ky, vl in node.unknownAttributes[self.dictName].iteritems():
                if type(vl) == self.typePickle:
                    node.unknownAttributes[self.dictName][ky] = vl = vl.get()
                if not self.testDefault(ky, vl):
                    isDefault = False
                    break

            if isDefault:  # no non-defaults seen, drop the whole cleo dictionary
                del node.unknownAttributes[self.dictName]
                self.c.setChanged(True)
                return True

        return False
    #@nonl
    #@-node:ekr.20071004090250.24:dropEmpty
    #@-node:ekr.20071004090250.19:probably junk
    #@-node:ekr.20071004090250.16:attributes...
    #@+node:ekr.20071004090250.25:safe_del
    def safe_del(self, d, k):
        "delete a key from a dict. if present"
        if d.has_key(k): del d[k]
    #@nonl
    #@-node:ekr.20071004090250.25:safe_del
    #@+node:ekr.20071004090250.26:editGraph
    def editGraph(self, event=None, pos = None):

        c = self.c

        if pos == None:
            p = c.currentPosition()
        else:
            p = pos

        self.p = p

        # make sure fileIndex is set on everything
        for p2 in p.self_and_subtree_iter():
            self.setIndex(p2)

        self.graph = Graph.Graph()
        # graph.simple = 0  # only blocks self loops?
        self.graph.directed = 1

        self.tnode2gnode = {}
        self.gnode2attribs = {}
        self.loadGraph(self.graph, p)
        self.loadGraphLinks(self.graph, p)

        editor = Gred.SAGraphEditor(g.app.root)
        self.editor = editor
        editor.dirty = 0
        editor.cVertexDefault = '#d8d8ff'
        editor.cEdgeDefault = '#808080'
        editor.cLabelDefault = 'black'
        editor.leoQuit = self.exiting
        editor.master.protocol("WM_DELETE_WINDOW", self.exiting)
        editor.ShowGraph(self.graph, "test")
        # layout = Embedder.BFSTreeEmbedder()
        # layout.Embed(self.editor)
        # self.editor.grab_set()
        # self.editor.focus_force()
        # g.app.root.wait_window(self.editor)
    #@-node:ekr.20071004090250.26:editGraph
    #@+node:ekr.20071004090250.27:editWholeTree
    #@+at
    # 
    # This doesn't work
    # 
    # def editWholeTree(self, event=None):
    #     c = self.c
    #     print c.rootPosition().headString()
    #     self.editGraph(pos = c.rootPosition())
    #@-at
    #@-node:ekr.20071004090250.27:editWholeTree
    #@+node:ekr.20071004090250.28:loadGraph
    def loadGraph(self, graph, p):

        vid = graph.AddVertex()
        self.tnode2gnode[str(p.v.t.fileIndex)] = vid
        self.gnode2attribs[vid] = {}
        self.gnode2attribs[vid]['bodyString'] = p.bodyString()
        graph.SetLabeling(vid, p.headString())
        x,y = self.getat(p.v,'x'), self.getat(p.v,'y')
        if x == None: x = 0
        if y == None: y = 0
        graph.SetEmbedding(vid, x, y)

        for nd0 in p.children_iter():
            if nd0.headString().startswith('@link'): continue
            cid = self.loadGraph(graph, nd0)
            graph.AddEdge(vid, cid)
            graph.SetEdgeWeight(0, vid, cid, 30)
        return vid
    #@-node:ekr.20071004090250.28:loadGraph
    #@+node:ekr.20071004090250.29:loadGraphLinks
    def loadGraphLinks(self, graph, p):

        for nd0 in p.children_iter():
            if nd0.headString().startswith('@link'):
                s = self.indexStrFromStr(nd0.headString())
                vid = self.tnode2gnode[str(p.v.t.fileIndex)]
                try:
                    cid = self.tnode2gnode[s]
                    graph.AddEdge(vid, cid)
                    graph.SetEdgeWeight(0, vid, cid, 30)
                except:  # @link node went stale
                    g.es('Link to %s broke' % nd0.headString())
            self.loadGraphLinks(graph, nd0)
    #@-node:ekr.20071004090250.29:loadGraphLinks
    #@+node:ekr.20071004090250.30:exiting
    def exiting(self):
        ans = g.app.gui.runAskYesNoCancelDialog(
            self.c, 'Load changes?',
            'Load changes from graph editor?')
        if ans == 'yes':
            self.saveGraph(self.p, self.graph)
        if ans in ('yes', 'no'):
            self.editor.destroy()
            self.editor.master.withdraw()  # ???
        # if ans == cancel do nothing
    #@-node:ekr.20071004090250.30:exiting
    #@+node:ekr.20071004090250.31:saveGraph
    def saveGraph(self, p, graph):

        c = self.c
        c.beginUpdate()
        try:
            # FIXME should check p is ok and default to root if not

            todo = set(graph.Vertices())

            c.setHeadString(p, 'OLD: ' + p.headString())
            p.setDirty()
            c.selectPosition(p)
            c.contractNode()
            root = p.insertAfter()
            root.setHeadString('NEW: graph top level')
            root.expand()
            pos = root.copy()

            gnode2tnode = {}

            def label(i):
                """change undefined (numeric) labels from ints to strs"""
                return str(graph.GetLabeling(i))

            def nextStart():
                """find the node with the most outedges"""
                maxOut = -1
                maxIdx = None
                for i in todo:
                    out = len(graph.OutNeighbors(i))
                    if out > maxOut:
                        maxOut = out
                        maxIdx = i
                return maxIdx

            def makeTree(pos, node0):

                nd = pos.insertAsLastChild()
                nd.expand()
                self.setIndex(nd)
                gnode2tnode[node0] = str(nd.v.t.fileIndex)                
                nd.setHeadString(label(node0))
                x = graph.GetEmbedding(node0)
                x,y = x.x,x.y
                self.setat(nd.v, 'x', x)
                self.setat(nd.v, 'y', y)
                if node0 in self.gnode2attribs:
                    nd.setTnodeText(self.gnode2attribs[node0]['bodyString'])
                    # FIXME copy uAs over too

                for node1 in graph.OutNeighbors(node0):
                    if node1 in todo:
                        todo.remove(node1)
                        makeTree(nd, node1)
                    else:
                        lnk = nd.insertAsLastChild()
                        lnk.setHeadString(
                            self.formatLink(gnode2tnode[node1], label(node1)))

            while todo:
                next = nextStart()
                todo.remove(next)
                makeTree(pos, next)

            if pos.numberOfChildren() == 1:
                ch = pos.children_iter().next()
                ch.linkAfter(pos)
                c.selectPosition(ch)
                pos.unlink()
            else:
                c.selectPosition(pos)

        finally:
            c.setChanged(True)
            c.endUpdate()
    #@-node:ekr.20071004090250.31:saveGraph
    #@+node:ekr.20071004090250.32:copyLink
    def copyLink(self, event = None):
        c = self.c
        p = c.currentPosition()
        self.setIndex(p)
        nn = p.insertAfter()
        nn.setHeadString(self.formatLink(p.v.t.fileIndex, p.headString()))
        c.selectPosition(nn)
        c.cutOutline()
        c.selectPosition(p)
        g.es('Link copied to clipboard')
    #@-node:ekr.20071004090250.32:copyLink
    #@+node:ekr.20071004090250.33:followLink
    def followLink(self, event = None):
        c = self.c
        s = c.currentPosition().headString()
        s = self.indexStrFromStr(s)
        for p in c.allNodes_iter():
            if self.indexStrFromStr(str(p.v.t.fileIndex)) == s:
                c.selectPosition(p)
                break
        g.es('Not found')
    #@-node:ekr.20071004090250.33:followLink
    #@+node:ekr.20071004090250.34:formatLink
    def formatLink(self, tid, hs):
        return '@link %s %s' % (hs.replace('(','[').replace(')',']'),str(tid))
    #@-node:ekr.20071004090250.34:formatLink
    #@+node:ekr.20071004090250.35:undone
    def undone(self, event = None):
        g.app.gui.runAskOkDialog(self.c, 'Not implemented',
            "Sorry, that's not implemented yet.")
    #@-node:ekr.20071004090250.35:undone
    #@-others
#@nonl
#@-node:ekr.20071004090250.11:class GraphEd
#@-others
#@-node:ekr.20071004090250:@thin graphed.py
#@-leo
