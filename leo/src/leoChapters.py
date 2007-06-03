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
            # Keys are chapter ames, values are chapters.
            # Important: chapter names never change, even if their @chapter node changes.

        self.chaptersNode = None # Set later
        self.selectedChapter = None
        self.trace = False
    #@-node:ekr.20070317085437.2: ctor: chapterController
    #@+node:ekr.20070325104904:cc.finishCreate
    def finishCreate (self):

        '''Find or make the @chapters and @chapter trash nodes.'''

        # This must be called late in the init process:
        # at present, called by g.openWithFileName and c.new.

        cc = self ; c = cc.c

        # Create the @chapters node if needed, and set cc.chaptersNode.
        if not cc.chaptersNode and not cc.findChaptersNode():
            cc.createChaptersNode()

        # Create the main chapter
        cc.chaptersDict['main'] = chapter(c=c,chapterController=cc,name='main',root=c.rootPosition())

        tag = '@chapter'
        for p in c.allNodes_iter():
            h = p.headString()
            if h.startswith(tag):
                tabName = h[len(tag):].strip()
                if tabName and tabName not in ('main',):
                    if cc.chaptersDict.get(tabName):
                        self.error('duplicate chapter name: %s' % tabName)
                    else:
                        cc.chaptersDict[tabName] = chapter(c=c,chapterController=cc,name=tabName,root=p)

        cc.selectChapterByName('main')
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

        cc = self ; c = cc.c

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

        if name not in ('main',):
            root = cc.getChapterNode(tabName) # Creates @chapter node and one child.
            cc.chaptersDict[tabName] = chapter(c=c,chapterController=cc,name=tabName,root=root)
            ###tt.createTab(tabName)
            ###tt.makeTabMenu(tabName)
            ###tree = tt.getTree(tabName)
            ###tree.setBindings()
            ###tt.selectTab(tabName)
            c.redraw_now()
            ###tt.renameChapterHelper(cc,tabName)

        # tt.selectTab unselects the previous chapter and selects the present chapter.
        c.bodyWantsFocusNow()
    #@-node:ekr.20070317085437.31:cc.createChapter
    #@+node:ekr.20070317085437.40:cc.removeChapter
    def removeChapter (self,event=None):

        cc = self ; c = cc.c

        theChapter = cc.selectedChapter
        if not theChapter: return

        ## name = tt.getSelectedTabName()
        name = theChapter.name

        ###if name == 'trash':
            ###return cc.error('Can not remove the trash')

        if name == 'main':
            return cc.error('Can not remove the main chapter')
        else:
            cc.deleteChapterNode(name)
            ###tt.destroyTab(name)
    #@-node:ekr.20070317085437.40:cc.removeChapter
    #@+node:ekr.20070317085437.41:cc.renameChapter (to do)
    def renameChapter (self,event=None):

        '''Handle the rename chapter command.'''

        cc = self

        theChapter = cc.selectedChapter
        if not theChapter: return

        ## name = tt.getSelectedTabName()
        name = theChapter.name

        if name == 'main':
            return cc.error('Can not rename the main chapter')

        ### tt.renameChapterHelper(cc,tabName)
    #@-node:ekr.20070317085437.41:cc.renameChapter (to do)
    #@+node:ekr.20070317130250:cc.selectChapterByName
    def selectChapterByName (self,name):

        cc = self ; chapter = cc.chaptersDict.get(name)

        if chapter:
            if chapter != cc.selectedChapter:
                if cc.selectedChapter:
                    cc.selectedChapter.unselect()
                chapter.select()
                cc.selectedChapter = chapter
        else:
            cc.error('cc.selectShapter: no such chapter: %s' % name)
    #@-node:ekr.20070317130250:cc.selectChapterByName
    #@-node:ekr.20070317085437.30:Chapter commands
    #@+node:ekr.20070317085437.49:Node commands
    #@+node:ekr.20070317085437.50:cc.cloneToChapter
    def cloneToChapter (self,event=None,toChapter=None):

        cc = self ; c = cc.c
        p = c.currentPosition() ; h = p.headString()
        fromChapter = cc.getSelectedChapter()
        toChapter = cc.getChapter(toChapter)
        if fromChapter.name == 'main' and h.startswith('@chapter'):
            return cc.error('can not clone @chapter node')
        # g.trace('from',fromChapter.name,'to',toChapter)

        c.beginUpdate()
        try:
            clone = c.clone()
            clone.unlink()
            if toChapter.name == 'main':
                clone.moveAfter(toChapter.p)
            else:
                parent = cc.getChapterNode(toChapter.name)
                clone.moveToLastChildOf(parent)
            ###c.selectPosition(clone)
            # Set the 'raw' current position without affecting c._rootPosition.
            # Do *not* call c.selectPosition: it calls tree.select, which causes lots of problems.
            c._currentPosition = clone
            c.setChanged(True)
        finally:
            c.endUpdate(False)

        toChapter.p = clone.copy()
        ###tt.selectTab(toChapter.name)
        fromChapter.p = p.copy()
    #@-node:ekr.20070317085437.50:cc.cloneToChapter
    #@+node:ekr.20070317085437.51:cc.copyToChapter
    def copyToChapter (self,event=None,toChapter=None):

        cc = self ; c = cc.c
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
            ###c.selectPosition(p2)
            # Set the 'raw' current position without affecting c._rootPosition.
            # Do *not* call c.selectPosition: it calls tree.select, which causes lots of problems.
            c._currentPosition = p2
            c.setChanged(True)
        finally:
            c.endUpdate(False)

        toChapter.p = p2.copy()
        ###tt.selectTab(toChapter.name)
        fromChapter.p = p.copy()
    #@-node:ekr.20070317085437.51:cc.copyToChapter
    #@+node:ekr.20070317085437.52:cc.moveToChapter
    def moveToChapter (self,event=None,toChapter=None):

        cc = self ; c = cc.c ; p = c.currentPosition()
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
                ###c.selectPosition(sel)
                # Set the 'raw' current position without affecting c._rootPosition.
                # Do *not* call c.selectPosition: it calls tree.select, which causes lots of problems.
                c._currentPosition = sel
        finally:
            c.endUpdate(False)

        if sel:
            toChapter.p = p.copy() # Must be done before tt.selectTab.
            ### tt.selectTab(toChapter.name)
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

        for p in c.rootPosition().self_and_siblings_iter():
            if p.headString() == '@chapters':
                cc.chaptersNode = p.copy()
                return p

        # This is *not* an error.
        return None
    #@-node:ekr.20070325094401:cc.findChaptersNode
    #@+node:ekr.20070325115102:cc.getChaperNode
    def getChapterNode (self,chapterName):

        '''Return the position of the @chapter node with the given name.'''

        cc = self ; c = cc.c

        if chapterName == 'main':
            return c.rootPosition()
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

        return cc.selectedChapter

        # tabName = cc.tt.nb.getcurselection()
        # theChapter = cc.chaptersDict.get(tabName) or cc.selectedChapter
        # if self.trace: g.trace(theChapter and theChapter.name or '<no chapter>')
        # return theChapter
    #@-node:ekr.20070318122708:cc.getSelectedChapter
    #@+node:ekr.20070510064813:cc.printChaptersTree
    def printChaptersTree(self,tag=''):

        cc = self ; root = cc.chaptersNode

        for p in c.rootPosition().self_and_siblings_iter():
            for p2 in p.self_and_subtree_iter():
                if p2 == root:
                    inTree = True ; break
        else:
            inTree = False

        g.trace('-'*40)

        full = True

        if root and full:
            print '@chapters tree...','(in main tree: %s)' % inTree
            for p in root.self_and_subtree_iter():
                print '.'*p.level(),p.v
    #@nonl
    #@-node:ekr.20070510064813:cc.printChaptersTree
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
        self.name = name
        self.selectLockout = False # True: in chapter.select logic.
        self.trace = False

        # State variables: saved/restored when the chapter is unselected/selected.
        if self.name == 'main':
            self.p = c.currentPosition() or c.rootPosition()
            self.root = None # Not used.
        else:
            self.p = None # Set later.
            self.root = root and root.copy() # The immutable @chapter node.
            bunch = g.Bunch(p=self.root.copy(),expanded=True)
            self.hoistStack.append(bunch)

        # g.trace('chapter',self.name,'root',root)
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

        c = self.c ; cc = self.cc ; name = self.name

        g.trace(name,'self.p',self.p,'self.root',self.root) # 'w.leo_p',w and w.leo_p)

        cc.selectedChapter = self

        # Next, recompute p and possibly select a new editor.
        if w:
            assert w == c.frame.body.bodyCtrl
            assert w == c.frame.bodyCtrl
            assert w.leo_p
            ### root = w.leo_p or self.root.firstChild() or self.root
            self.p = p = self.findPositionInChapter(w.leo_p)
            if p != w.leo_p: g.trace('****** can not happen: lost p',w.leo_p)
        else:
            # This must be done *after* switching roots.
            target_p = self.p or self.root.firstChild() or self.root
            self.p = p = self.findPositionInChapter(target_p)
            if selectEditor:
                w = self.findEditorInChapter(p)
                c.frame.body.selectEditor(w) # Switches text.

        c.beginUpdate()
        try:
            if name == 'main' and cc.chaptersNode:
                cc.chaptersNode.contract()    
            c.hoistStack = self.hoistStack[:]
            c.selectPosition(p)
        finally:
            c.endUpdate()
            c.bodyWantsFocusNow()
    #@nonl
    #@-node:ekr.20070423102603.1:chapterSelectHelper
    #@+node:ekr.20070317131708:chapter.findPositionInChapter
    def findPositionInChapter (self,p1):

        '''Return a valid position p such that p.v == v.'''

        # Do nothing if the present position is in the proper chapter.
        c = self.c ; name = self.name 

        root = g.choose(self.name=='main',c.rootPosition(),self.root)
        # g.trace('root',root,'p',p)
        if p1 and c.positionExists(p1,root=root):
            # g.trace('using existing position',p)
            return p1

        if name == 'main':
            for p in self.c.allNodes_iter():
                if p.v == p1.v:
                    # g.trace('*** found in main chapter',p)
                    self.p = p.copy()
                    return self.p
            self.p = c.rootPosition()
        else:
            for p in self.root.self_and_subtree_iter():
                if p.v == p1.v:
                    # g.trace('*** found in chapter',p)
                    self.p = p.copy()
                    return self.p
            self.p = self.root.copy()

        if 1:
            self.error('***** findPositionInChapter: lost %s in %s' % (
                p1.v.t.headString,self.name))
            g.trace(g.callers())

        return self.p.copy()
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
    #@+node:ekr.20070529171934.1:chapter.rename (not used)
    def rename (self,newName):

        p = self.root
        s = '@chapter ' + newName
        p.setHeadString(s)
    #@-node:ekr.20070529171934.1:chapter.rename (not used)
    #@-node:ekr.20070317131205.1:chapter.select & helpers
    #@+node:ekr.20070320091806.1:chapter.unselect
    def unselect (self):

        '''Remember chapter info when a chapter is about to be unselected.'''

        c = self.c ; cc = self.cc
        self.hoistStack = c.hoistStack[:]
        self.p = c.currentPosition()
        if self.trace: g.trace('chapter',self.name,'p',self.p.headString())
    #@-node:ekr.20070320091806.1:chapter.unselect
    #@-others
#@nonl
#@-node:ekr.20070317085708:class chapter
#@-others
#@nonl
#@-node:ekr.20070317085508.1:@thin leoChapters.py
#@-leo
