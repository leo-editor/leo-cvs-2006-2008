#@+leo-ver=4-thin
#@+node:ekr.20070317085508.1:@thin leoChapters.py
'''Classes that manage chapters in Leo's core.'''

#@@language python
#@@tabwidth -4
#@@pagewidth 80

import leoGlobals as g
import leoNodes

# To do: later or never:
# - Create commands to choose chapters.
# - Make body editors persistent. Create @body-editor node?

#@+others
#@+node:ekr.20070317085437:class chapterController
class chapterController:

    '''A per-commander controller that manages chapters and related nodes.'''

    #@    @+others
    #@+node:ekr.20070530075604:Birth
    #@+node:ekr.20070317085437.2: ctor: chapterController
    def __init__ (self,c):

        self.c = c

        self.chaptersDict = {}
            # Keys are tabNames, values are chapters.
            # Important: tabNames never change, even if their button text changes.
        self.chaptersNode = None # Set later
        self.enabled = True # False: do not link or unlink any tree.
        self.mainRoot = None
            # c.rootPosition() when the main chapter is active.
            # It must be updated whenever we choose another chapter.
        self.selectedChapter = None
        self.tabNames = []
        self.trace = False
        self.tt = None # Set in finishCreate.

        # Save/restore vars used *only* by a cooperating pair of methods.
        # For forceMainChapter/restoreOldChapter...
        self.savedCurrent = None
            # c.currentPosition() when forceMainChapter is called.
        self.savedRoot = None
            # c.rootPosition() when forceMainChapter is called.
        # For link/unlinkChaptersNode...
        self.chaptersLinked = True
            # True if the @chapters node is linked into the outline.
    #@-node:ekr.20070317085437.2: ctor: chapterController
    #@+node:ekr.20070325104904:cc.finishCreate
    def finishCreate (self):

        '''Find or make the @chapters and @chapter trash nodes.'''

        # This must be called late in the init process:
        # at present, called by g.openWithFileName and c.new.

        cc = self ; c = cc.c ; k = c.k ; tt = cc.tt ; trace = False or self.trace

        # g.trace(g.callers())

        current = c.currentPosition()
        cc.mainRoot = c.rootPosition()
        if trace: g.trace('chapterController: currentPosition',current,'rootPosition',cc.mainRoot)

        # Create the @chapters node if needed, and set cc.chaptersNode.
        if not cc.chaptersNode and not cc.findChaptersNode():
            cc.createChaptersNode()

        if cc.mainRoot == cc.chaptersNode and cc.mainRoot.hasNext():
            cc.mainRoot = cc.mainRoot.next()
            c.setRootPosition(cc.mainRoot)
            c.setCurrentPosition(current)

        if trace:g.trace('chapterController: mainRoot',cc.mainRoot)

        # The chapters node is always unlinked, except when saving .leo files.
        cc.unlinkChaptersNode()

        if not cc.findChapterNode('trash',giveError=False):
            cc.createChapterNode('trash')

        # Create the two default chapters.
        for tabName in ('trash','main'):
            p = cc.getChapterNode(tabName)
            cc.chaptersDict[tabName] = chapter(c=c,chapterController=cc,name=tabName,root=p)
            if tabName == 'main':
                # The main tab, tree and canvas were created earlier.
                c.frame.tree = tree = tt.getTree(tabName)
                c.frame.canvas = tt.getCanvas(tabName)
            else:
                tt.createTab(tabName,select=False)
                tree = tt.getTree(tabName)

            # This is required even in the 'main' chapter so that
            # bindings set by k.registerCommand are updated.
            tree.setBindings()
            tt.makeTabMenu(tabName)

        # Create a chapter for each @chapter node.
        tag = '@chapter'
        for p in cc.chaptersNode.children_iter():
            h = p.headString()
            if h.startswith(tag):
                tabName = h[len(tag):].strip()
                if tabName and tabName not in ('main','trash'):
                    if cc.chaptersDict.get(tabName):
                        self.error('duplicate chapter name: %s' % tabName)
                    else:
                        cc.chaptersDict[tabName] = chapter(c=c,chapterController=cc,name=tabName,root=p)
                        tt.createTab(tabName,select=False)
                        tt.makeTabMenu(tabName)
                        tree = tt.getTree(tabName)
                        tree.setBindings()

        cc.selectChapter('main')
    #@nonl
    #@-node:ekr.20070325104904:cc.finishCreate
    #@-node:ekr.20070530075604:Birth
    #@+node:ekr.20070320091806:Callbacks (chapter)
    def selectCallback (self,tabName):

        cc = self ; chapter = cc.chaptersDict.get(tabName)
        if chapter:
            chapter.select()

    def unselectCallback (self,tabName):

        cc = self ; chapter = cc.chaptersDict.get(tabName)
        if chapter:
            chapter.unselect()
    #@nonl
    #@-node:ekr.20070320091806:Callbacks (chapter)
    #@+node:ekr.20070317085437.30:Chapter commands
    #@+node:ekr.20070317085437.31:cc.createChapter
    def createChapter (self,event=None,name=None):

        cc = self ; c = cc.c ; tt = cc.tt

        if name:
            tabName = name
        else:
            # Find an unused name.  This is *not* 1 + the present number of chapters.
            # The **immutable** chapter name is 'Chapter n'.
            n  = 1
            while True:
                tabName = 'Chapter %d' % n
                if self.chaptersDict.get(tabName):
                    n += 1
                else:
                    break

        if name in ('trash','main',):
            tt.selectTab(tabName)
            tt.makeTabMenu(tabName)
        else:
            root = cc.getChapterNode(tabName) # Creates @chapter node and one child.
            cc.chaptersDict[tabName] = chapter(c=c,chapterController=cc,name=tabName,root=root)
            tt.createTab(tabName)
            tt.makeTabMenu(tabName)
            tree = tt.getTree(tabName)
            tree.setBindings()
            tt.selectTab(tabName)
            c.redraw_now()
            tt.renameChapterHelper(cc,tabName)

        # tt.selectTab unselects the previous chapter and selects the present chapter.
        c.bodyWantsFocusNow()
    #@-node:ekr.20070317085437.31:cc.createChapter
    #@+node:ekr.20070529163321:cc.hideChapters
    def hideChapters(self):

        cc = self ; c = cc.c

        if not cc.enabled: return

        if cc.chaptersLinked:
            c.beginUpdate()
            try:
                cc.restoreOldChapter(None)
                cc.selectChapter('main')
            finally:
                c.endUpdate()


    #@-node:ekr.20070529163321:cc.hideChapters
    #@+node:ekr.20070317085437.40:cc.removeChapter
    def removeChapter (self,event=None):

        cc = self ; c = cc.c ; tt = cc.tt
        name = tt.getSelectedTabName()

        if name == 'trash':
            return cc.error('Can not remove the trash')
        elif name == 'main':
            return cc.error('Can not remove the main chapter')
        else:
            cc.deleteChapterNode(name)
            tt.destroyTab(name)
    #@-node:ekr.20070317085437.40:cc.removeChapter
    #@+node:ekr.20070317085437.41:cc.renameChapter
    def renameChapter (self,event=None):

        '''Handle the rename chapter command.'''

        cc = self ; tt = cc.tt
        tabName = tt.getSelectedTabName()

        if tabName == 'trash':
            return cc.error('Can not rename the trash')
        if tabName == 'main':
            return cc.error('Can not rename the main chapter')

        tt.renameChapterHelper(cc,tabName)
    #@-node:ekr.20070317085437.41:cc.renameChapter
    #@+node:ekr.20070511075249:cc.showChapters
    def showChapters(self):

        cc = self ; c = cc.c

        if not cc.enabled: return

        if not cc.chaptersLinked:
            c.beginUpdate()
            try:
                cc.selectChapter('main')
                cc.forceMainChapter()
            finally:
                c.endUpdate()
    #@nonl
    #@-node:ekr.20070511075249:cc.showChapters
    #@-node:ekr.20070317085437.30:Chapter commands
    #@+node:ekr.20070317085437.49:Node commands
    #@+node:ekr.20070317085437.50:cc.cloneToChapter
    def cloneToChapter (self,event=None,toChapter=None):

        cc = self ; c = cc.c ; tt = cc.tt
        p = c.currentPosition() ; h = p.headString()
        fromChapter = cc.getSelectedChapter()
        toChapter = cc.getChapter(toChapter)
        if fromChapter.name == 'main' and h.startswith('@chapter'):
            return cc.error('can not clone @chapter node')
        # g.trace('from',fromChapter.name,'to',toChapter)

        c.beginUpdate()
        try:
            parent = cc.getChapterNode(toChapter.name)
            clone = c.clone()
            clone.unlink()
            clone.moveToLastChildOf(parent)
            c.selectPosition(clone)
            c.setChanged(True)
        finally:
            c.endUpdate(False)

        toChapter.p = clone.copy()
        tt.selectTab(toChapter.name)
        fromChapter.p = p.copy()
    #@-node:ekr.20070317085437.50:cc.cloneToChapter
    #@+node:ekr.20070317085437.51:cc.copyToChapter
    def copyToChapter (self,event=None,toChapter=None):

        cc = self ; c = cc.c ; tt = cc.tt
        p = c.currentPosition() ; h = p.headString()
        fromChapter = cc.getSelectedChapter()
        toChapter = cc.getChapter(toChapter)
        if fromChapter.name == 'main' and h.startswith('@chapter'):
            return cc.error('can not copy @chapter node')
        # g.trace('from',fromChapter.name,'to',toChapter.name)

        c.beginUpdate()
        try:
            parent = cc.getChapterNode(toChapter.name)
            s = c.fileCommands.putLeoOutline()
            p2 = c.fileCommands.getLeoOutline(s)
            p2.unlink()
            p2.moveToLastChildOf(parent)
            c.selectPosition(p2)
            c.setChanged(True)
        finally:
            c.endUpdate(False)

        toChapter.p = p2.copy()
        tt.selectTab(toChapter.name)
        fromChapter.p = p.copy()
    #@-node:ekr.20070317085437.51:cc.copyToChapter
    #@+node:ekr.20070317085437.29:cc.emptyTrash
    def emptyTrash (self):

        cc = self ; c = cc.c
        trashChapter = cc.getChapter('trash')
        selChapter = cc.getSelectedChapter()
        flag=selChapter.name=='trash'

        c.beginUpdate()
        try:
            root = cc.findChapterNode('trash')
            while root.hasChildren():
                root.firstChild().doDelete()
            trashChapter.p = cc.createChild(root,'trash')
            if flag:
                c.selectPosition(trashChapter.p)
        finally:
            c.endUpdate(flag=flag)
    #@nonl
    #@-node:ekr.20070317085437.29:cc.emptyTrash
    #@+node:ekr.20070317085437.52:cc.moveToChapter
    def moveToChapter (self,event=None,toChapter=None):

        cc = self ; c = cc.c ; tt = cc.tt ; p = c.currentPosition()
        fromChapter = cc.getSelectedChapter()
        toChapter = cc.getChapter(toChapter)

        if 1: # Defensive code: should never happen.
            if fromChapter.name == 'main' and p.headString().startswith('@chapter'):
                return cc.error('can not move @chapter node')

        c.beginUpdate()
        try:
            sel = p.visBack() or p.visNext()
            if sel:
                if toChapter.name == 'main':
                    p.unlink()
                    p.moveAfter(toChapter.p)
                else:
                    parent = cc.getChapterNode(toChapter.name)
                    p.unlink()
                    p.moveToLastChildOf(parent)
                c.selectPosition(sel)
        finally:
            c.endUpdate(False)

        if sel:
            toChapter.p = p.copy() # Must be done before tt.selectTab.
            tt.selectTab(toChapter.name)
            fromChapter.p = sel.copy() # Must be done after tt.selectTab.
            c.setChanged(True)
        else:
            cc.error('Can not move the last node of a chapter.')
    #@-node:ekr.20070317085437.52:cc.moveToChapter
    #@-node:ekr.20070317085437.49:Node commands
    #@+node:ekr.20070511081405:Creating/deleting nodes (chapterController)
    #@+node:ekr.20070325101652:cc.createChaptersNode
    def createChaptersNode (self):

        cc = self ; c = cc.c ; root = c.rootPosition()

        # g.trace('root',root)

        c.beginUpdate()
        try:
            # Create the node with a postion method
            # so we don't involve the undo logic.
            p = root.insertAsLastChild()
            p.initHeadString('@chapters')
            p.moveToRoot(oldRoot=root)
            c.setRootPosition(p)
            cc.chaptersNode = p.copy()
            t = p.v.t
            if t.fileIndex:
                self.error('***** t.fileIndex already exists')
            else:
                t.setFileIndex(g.app.nodeIndices.getNewIndex())
        finally:
            c.endUpdate(False)
    #@nonl
    #@-node:ekr.20070325101652:cc.createChaptersNode
    #@+node:ekr.20070325063303.2:cc.createChapterNode
    def createChapterNode (self,chapterName):

        '''Create an @chapter node for the named chapter,
        creating an @chapters node if necessary.'''

        cc = self ; c = cc.c ; current = c.currentPosition() or c.rootPosition()

        # g.trace(chapterName,'current',current)

        c.beginUpdate()
        try:
            # Create the node with a postion method
            # so we don't involve the undo logic.
            p = current.insertAsLastChild()
            p.initHeadString('@chapter ' + chapterName)
            c.setBodyString(p,chapterName)
            p.moveToFirstChildOf(cc.chaptersNode)
            cc.createChild(p,'%s node 1' % chapterName)
        finally:
            c.endUpdate(False)

        return p
    #@-node:ekr.20070325063303.2:cc.createChapterNode
    #@+node:ekr.20070509081915.1:cc.createChild
    def createChild (self,parent,s):

        '''Create a child node of parent without changing the undo stack.
        set the headString of the new node to s.'''

        c = self.c

        # g.trace('parent',parent,'s',s)

        p = parent.insertAsLastChild()
        p.initHeadString(s)
        c.setChanged(True)

        return p
    #@-node:ekr.20070509081915.1:cc.createChild
    #@+node:ekr.20070325063303.4:cc.deleteChapterNode
    def deleteChapterNode (self,chapterName):

        '''Delete the @chapter with the given name.'''

        cc = self ; c = cc.c

        chapter = cc.chaptersDict.get(chapterName)

        if chapter:
            c.beginUpdate()
            try:
                # Do not involve undo logic.
                c.setCurrentPosition(chapter.root)
                chapter.root.doDelete()
                # The chapter selection logic will select a new node.
            finally:
                c.endUpdate(False)
    #@nonl
    #@-node:ekr.20070325063303.4:cc.deleteChapterNode
    #@-node:ekr.20070511081405:Creating/deleting nodes (chapterController)
    #@+node:ekr.20070511065107:Linking/unlinking trees (chapterController)
    #@+node:ekr.20070421092158:cc.forceMainChapter
    def forceMainChapter (self):

        cc = self ; c = self.c ; trace = False or self.trace
        if not cc.enabled: return

        if cc.chaptersLinked: return # We have done a show-chapters command.

        cc.savedRoot = c.rootPosition()
        cc.savedCurrent = current = c.currentPosition()
        oldChapter = cc.getSelectedChapter()

        if trace: g.trace('****',oldChapter and oldChapter.name,'savedRoot',cc.savedRoot)

        if oldChapter:
            if oldChapter.name == 'main':
                oldChapter = None # Don't unlink the main chapter in unlinkChaptersNode.
            else:
                oldChapter.link()
                if trace: g.trace('oldChapter',oldChapter.name)

        cc.linkChaptersNode() # sets c.rootPosition()

        # Tricky code:
        # 1. Set the 'raw' current position without affecting c._rootPosition.
        #    Do *not* call c.selectPosition: it calls tree.select, which causes lots of problems.
        # 2. Use current only if we are in the main chapter; otherwise use cc.main.
        #    The reason for this hack is that cc.finishCreate always selects the main chapter,
        #    so cc.finishCreate won't find a vnode that exists only in another chapter.
        c._currentPosition = g.choose(oldChapter,cc.mainRoot,current)

        if trace: g.printEntireTree(cc.c,'forceMainChapter:after')

        return oldChapter
    #@-node:ekr.20070421092158:cc.forceMainChapter
    #@+node:ekr.20070503082757:cc.restoreOldChapter
    def restoreOldChapter (self, oldChapter):

        cc = self ; c = self.c ; trace = False or self.trace
        if not cc.enabled: return

        if trace: g.trace(oldChapter,'savedRoot',cc.savedRoot)

        cc.unlinkChaptersNode()

        if oldChapter:
            oldChapter.unlink()

        # Set the current position first.
        c.selectPosition(cc.savedCurrent)
        cc.savedCurrent = None

        # Set the root position second, so it will be unaffected by c.selectPosition.
        c.setRootPosition(cc.savedRoot)
        cc.savedRoot = None

        if trace: g.printEntireTree(cc.c,'restoreOldChapter:after')
    #@-node:ekr.20070503082757:cc.restoreOldChapter
    #@+node:ekr.20070503083301:cc.linkChaptersNode
    def linkChaptersNode (self):

        '''Called only from forceMainChapter to link in the @chapters node.
        The caller is responsible for saving state.'''

        cc = self ; c = cc.c ; trace = False or self.trace

        if not cc.enabled:
            return
        elif not cc.chaptersNode:
            self.error('***** no @chapters node')
        elif not cc.mainRoot:
            self.error('***** no cc.mainRoot')
        elif cc.chaptersLinked:
            g.trace('***** can not happen: @chapters already linked')
        else:
            if trace: g.printEntireTree(c,'linkChaptersNode:before')

            cc.chaptersLinked = True
            v = cc.chaptersNode.v
            v.linkAsRoot(oldRoot=cc.mainRoot.v)
            p = leoNodes.position(v,[])
            c.setRootPosition(p)

            if trace: g.printEntireTree(c,'linkChaptersNode:after')

    #@-node:ekr.20070503083301:cc.linkChaptersNode
    #@+node:ekr.20070503081539:cc.unlinkChaptersNode
    def unlinkChaptersNode (self):

        '''unlink the @chapters node from the headline.'''

        cc = self ; c = cc.c ; trace = False or self.trace

        if not cc.enabled:
            return
        elif not cc.chaptersNode:
            g.trace('***** can not happen: no @chapters node')
        elif not cc.chaptersLinked:
            g.trace('***** can not happen: @chapters already unlinked')
        else:
            if trace: cc.printChaptersTree('unlinkChaptersNode:before')
            p = cc.chaptersNode
            if cc.mainRoot == p:
                # Do *not* use visNext here: it might be in the @chapters tree.
                newRoot = p.visBack() or p.next()
                if trace:
                    g.trace('*** c.rootPosition',c.rootPosition())
                    g.trace('*** setting mainRoot',newRoot)
                cc.mainRoot = newRoot
                c.setCurrentPosition(cc.mainRoot)
                c.setRootPosition(cc.mainRoot)

            # Do not call p.unlink here: it removes p.v from p.v.t._vnodeList
            p.v.unlink()
            cc.chaptersLinked = False

            if trace:
                cc.printChaptersTree('unlinkChaptersNode:after')
                g.printEntireTree(c,'unlinkChaptersNode:after')
    #@nonl
    #@-node:ekr.20070503081539:cc.unlinkChaptersNode
    #@-node:ekr.20070511065107:Linking/unlinking trees (chapterController)
    #@+node:ekr.20070317130648:Utils
    #@+node:ekr.20070529171934:cc.completeChapterRename
    def completeChapterRename (self,theChapter,newName):

        theChapter.rename(newName)


    #@-node:ekr.20070529171934:cc.completeChapterRename
    #@+node:ekr.20070320085610:cc.error
    def error (self,s):

        g.es_print(s,color='red')
    #@-node:ekr.20070320085610:cc.error
    #@+node:ekr.20070325093617:cc.findChapterNode
    def findChapterNode (self,chapterName,giveError=True):

        '''Return the position of the @chapter node with the given name.'''

        cc = self

        if not cc.chaptersNode:
            return # An error has already been given.

        s = '@chapter ' + chapterName
        for p in cc.chaptersNode.children_iter():
            h = p.headString()
            if h == s:
                return p
            # elif h.startswith('@chapter '):
                # body = p.bodyString()
                # if body:
                    # lines = g.splitLines(body)
                    # line = lines[0].strip()
                    # if line == chapterName:
                        # return p

        if giveError:
            cc.error('*** findChapterNode: no @chapter node for: %s' % (chapterName))

        return None
    #@-node:ekr.20070325093617:cc.findChapterNode
    #@+node:ekr.20070325094401:cc.findChaptersNode
    def findChaptersNode (self):

        '''Return the position of the @chapters node.'''

        cc = self ; c = cc.c ; trace = False or self.trace

        for p in cc.mainRoot.self_and_siblings_iter():
            if p.headString() == '@chapters':
                cc.chaptersNode = p.copy()
                return p

        if trace: # This is *not* an error.
            g.trace('*** no @chapters node','cc.mainRoot',cc.mainRoot)

        return None
    #@-node:ekr.20070325094401:cc.findChaptersNode
    #@+node:ekr.20070325115102:cc.getChaperNode
    def getChapterNode (self,chapterName):

        '''Return the position of the @chapter node with the given name.'''

        cc = self ; c = cc.c

        if chapterName == 'main':
            if not cc.mainRoot:
                if self.trace: g.trace('*** setting mainRoot',c.rootPosition())
                cc.mainRoot = c.rootPosition()
            # g.trace('mainRoot',cc.mainRoot,'c.rootPosition',c.rootPosition())
            return cc.mainRoot
        else:
            val = (
                cc.findChapterNode(chapterName,giveError=False) or
                cc.createChapterNode(chapterName))
            # g.trace('chapterName',chapterName,'val',val)
            return val
    #@-node:ekr.20070325115102:cc.getChaperNode
    #@+node:ekr.20070318124004:cc.getChapter
    def getChapter(self,name):

        cc = self

        return cc.chaptersDict.get(name)
    #@-node:ekr.20070318124004:cc.getChapter
    #@+node:ekr.20070318122708:cc.getSelectedChapter
    def getSelectedChapter (self):

        cc = self

        tabName = cc.tt.nb.getcurselection()
        theChapter = cc.chaptersDict.get(tabName) or cc.selectedChapter
        if self.trace: g.trace(theChapter and theChapter.name or '<no chapter>')
        return theChapter
    #@-node:ekr.20070318122708:cc.getSelectedChapter
    #@+node:ekr.20070510064813:cc.printChaptersTree
    def printChaptersTree(self,tag=''):

        cc = self ; root = cc.chaptersNode

        for p in cc.mainRoot.self_and_siblings_iter():
            for p2 in p.self_and_subtree_iter():
                if p2 == root:
                    inTree = True ; break
        else:
            inTree = False

        g.trace('-'*40)
        g.trace(tag,'cc.mainRoot',cc.mainRoot)

        full = True

        if root and full:
            print '@chapters tree...','(in main tree: %s)' % inTree
            for p in root.self_and_subtree_iter():
                print '.'*p.level(),p.v
    #@nonl
    #@-node:ekr.20070510064813:cc.printChaptersTree
    #@+node:ekr.20070317130250:cc.selectChapter
    def selectChapter (self,tabName):

        cc = self ; chapter = cc.chaptersDict.get(tabName)

        if chapter:
            chapter.select()
        else:
            cc.error('cc.selectShapter: no such chapter: %s' % tabName)
    #@-node:ekr.20070317130250:cc.selectChapter
    #@+node:ekr.20070601070812:cc.setRoot
    def setRoot (self,p):

        cc = self
        theChapter = cc.getSelectedChapter()

        if theChapter and theChapter.name == 'main':
            # g.trace(p,theChapter)
            cc.mainRoot = p
    #@-node:ekr.20070601070812:cc.setRoot
    #@+node:ekr.20070325121800:cc.updateChapterName (not used)
    def updateChapterName(self,oldName,newName):

        '''oldName is the immutable name of a chapter.
        Set the visible name of that chapter to newName.'''


        cc = self ; c = cc.c

        p = cc.findChapterNode(oldName)

        g.trace(g.callers())

        if p:
            c.setBodyString(p,newName)
        else:
            cc.error('no such chapter: %s' % oldName)
    #@-node:ekr.20070325121800:cc.updateChapterName (not used)
    #@-node:ekr.20070317130648:Utils
    #@-others
#@nonl
#@-node:ekr.20070317085437:class chapterController
#@+node:ekr.20070317085708:class chapter
class chapter:

    '''A class representing the non-gui data of a single chapter.'''

    #@    @+others
    #@+node:ekr.20070317085708.1: ctor: chapter
    def __init__ (self,c,chapterController,name,root):

        self.c = c 
        self.cc = chapterController
        self.hoistStack = []
        self.name = name # The immutable chapter name.  Not necessarily the same as the chapter's tabName.
        self.p = None # The current position...
        self.root = root and root.copy() # The immutable @chapter node (not used for the main chapter).
        self.selectLockout = False # True: in chapter.select logic.
        self.trace = False
        self.unlinkedRoot = None # data for link()

        # Init self.p only for the main chapter.
        if self.name == 'main':
            self.p = c.currentPosition() or c.rootPosition()

        # g.trace('chapter',self.name,'root',root,'firstChild',root.firstChild())
    #@nonl
    #@-node:ekr.20070317085708.1: ctor: chapter
    #@+node:ekr.20070317085708.2:__str__ and __repr__(chapter)
    def __str__ (self):

        return '<chapter id: %s name: %s p: %s>' % (
            id(self),
            self.name,
            self.p and self.p.headString() or '<no p>')

    __repr__ = __str__
    #@-node:ekr.20070317085708.2:__str__ and __repr__(chapter)
    #@+node:ekr.20070325155208.1:chapter.error
    def error (self,s):

        self.cc.error(s)
    #@nonl
    #@-node:ekr.20070325155208.1:chapter.error
    #@+node:ekr.20070420173354:chapter.link/unlink
    #@+node:ekr.20070509081411:link
    def link (self):

        '''Link the chapter's root.firstChild node back into the full outline.'''

        c = self.c ; cc = self.cc ; trace = False or self.trace
        if not cc.enabled: return

        # g.trace('chapter',self.name)

        if trace: g.printEntireTree(self.c,'link:before')
        if trace: cc.printChaptersTree('link:before')

        if self.name == 'main':
            self.error('!!! linking main chapter!')
        elif not self.root:
            self.error('!!! link: no root:',self)
        elif not self.unlinkedRoot:
            self.error('!!! link: no unlinkedRoot')
        else:
            # Like the demote logic.
            v = self.unlinkedRoot
            n = 0
            while v: # Do not use iterator here.
                # g.trace('linking',v)
                next = v._next
                v.unlink()
                v.linkAsNthChild(self.root.v,n)
                n += 1
                v = next
            self.unlinkedRoot = None
            if trace: cc.printChaptersTree('link:after')
    #@-node:ekr.20070509081411:link
    #@+node:ekr.20070509081411.1:unlink
    def unlink (self):

        '''Unlink the root node (the chapter's @chapter node) from the full outine.
        set unlinkData for later use by self.link.'''

        cc = self.cc ; c = cc.c ; trace = False or self.trace
        if not cc.enabled: return

        # g.trace('chapter',self.name,g.callers())

        if trace: g.printEntireTree(self.c,'link:before')
        if trace: cc.printChaptersTree('link:before')

        if self.name == 'main':
            self.error('!!! unlinking main chapter!')
        elif not self.root:
            self.error('!!! unlink: no @chapter node:',self)
        elif self.unlinkedRoot:
            self.error('!!! unlink: chapter already unlinked: unlinkedRoot: %s' % (self.unlinkedRoot))
        elif not self.root.firstChild():
            self.error('!!! unlink: no root.firstChild')
        else:
            # Like the promote logic.
            v = self.root.firstChild().v
            next = v._next
            v.unlink()
            v.linkAsRoot(oldRoot=None)
            p = leoNodes.position(v,[])
            c.setRootPosition(p)
            if not self.p: self.p = p.copy() # Init self.p the first time we open the chapter.
            self.unlinkedRoot = v
            last = v
            while next: # Don't use an iterator.
                v = next
                next = v._next
                v.unlink()
                v.linkAfter(last)
                last = v

            if trace: cc.printChaptersTree('link:after')
            if trace: g.printEntireTree(c,'link:after')
    #@-node:ekr.20070509081411.1:unlink
    #@-node:ekr.20070420173354:chapter.link/unlink
    #@+node:ekr.20070317131205.1:chapter.select & helpers
    def select (self,w=None,selectEditor=True):

        '''Restore chapter information and redraw the tree when a chapter is selected.'''

        if self.selectLockout: return

        try:
            self.selectLockout = True
            self.chapterSelectHelper(w,selectEditor)
        finally:
            self.selectLockout = False
    #@+node:ekr.20070423102603.1:chapterSelectHelper
    def chapterSelectHelper (self,w=None,selectEditor=True):

        c = self.c ; cc = self.cc ; tt = cc.tt ; name = self.name
        trace = False or self.trace

        # The big switcharoo.
        c.frame.canvas = canvas = tt.getCanvas(name)
        c.frame.tree = tt.getTree(name)

        # g.trace(name,g.callers())

        if trace: g.trace(
            'chapter',self.name,'w',w,
            'selectEditor',selectEditor,'p',self.p and self.p.headString())

        # First, switch roots.
        if name == 'main':
            c.setRootPosition(cc.mainRoot)
        else:
            self.unlink() # Sets root position.

        cc.selectedChapter = self

        # Next, recompute p and possibly select a new editor.
        if w:
            assert w == c.frame.body.bodyCtrl
            assert w == c.frame.bodyCtrl
            root = w.leo_p or self.root.firstChild() or self.root
            self.p = p = self.findPositionInChapter(root.v)
            if p != w.leo_p: g.trace('****** can not happen: lost p',root,p)
        else:
            # This must be done *after* switching roots.
            root = self.p or self.root.firstChild() or self.root
            self.p = p = self.findPositionInChapter(root.v)
            if selectEditor:
                w = self.findEditorInChapter(p)
                c.frame.body.selectEditor(w) # Switches text.

        c.beginUpdate()
        try:
            c.hoistStack = self.hoistStack[:]
            c.selectPosition(p)
        finally:
            c.endUpdate()
            c.bodyWantsFocusNow()
    #@nonl
    #@-node:ekr.20070423102603.1:chapterSelectHelper
    #@+node:ekr.20070317131708:chapter.findPositionInChapter
    def findPositionInChapter (self,v):

        '''Return a valid position p such that p.v == v.'''

        trace = False or self.trace

        # This should work regardless of what chapter is selected.
        for p in self.c.allNodes_iter():
            if p.v == v:
                if trace: g.trace('*** found in chapter',p)
                return p

        if 0:
            self.error('***** findPositionInChapter: lost %s in %s' % (
                v.t.headString,self.name))
            g.trace(g.callers())

        if 0: # This could crash.
            cc = self.cc
            print 'cc.mainRoot',cc.mainRoot
            print '******* top-level nodes *****'
            for p in cc.mainRoot.self_and_siblings_iter():
                print p.headStirng()
        return self.root
    #@nonl
    #@-node:ekr.20070317131708:chapter.findPositionInChapter
    #@+node:ekr.20070425175522:chapter.findEditorInChapter
    def findEditorInChapter (self,p):

        '''return w, an editor displaying position p.'''

        chapter = self ; c = self.c

        w = c.frame.body.findEditorForChapter(chapter,p)
        w.leo_chapter = chapter
        w.leo_p = p and p.copy()
        return w
    #@nonl
    #@-node:ekr.20070425175522:chapter.findEditorInChapter
    #@+node:ekr.20070529171934.1:chapter.rename
    def rename (self,newName):

        p = self.root
        s = '@chapter ' + newName
        p.setHeadString(s)
    #@-node:ekr.20070529171934.1:chapter.rename
    #@-node:ekr.20070317131205.1:chapter.select & helpers
    #@+node:ekr.20070320091806.1:chapter.unselect
    def unselect (self):

        '''Remember chapter info when a chapter is about to be unselected.'''

        c = self.c ; cc = self.cc
        self.hoistStack = c.hoistStack[:]
        self.p = c.currentPosition()
        if self.trace: g.trace('chapter',self.name,'p',self.p.headString())

        # Restore the entire outline and
        # link the chapter's @chapter node into the entire outline.
        if self.name != 'main':
            self.link()
    #@-node:ekr.20070320091806.1:chapter.unselect
    #@-others
#@nonl
#@-node:ekr.20070317085708:class chapter
#@-others
#@nonl
#@-node:ekr.20070317085508.1:@thin leoChapters.py
#@-leo
