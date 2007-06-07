#@+leo-ver=4-thin
#@+node:ekr.20070317085508.1:@thin leoChapters.py
'''Classes that manage chapters in Leo's core.'''

#@@language python
#@@tabwidth -4
#@@pagewidth 80

import leoGlobals as g
import leoNodes

# To do later or never: Make body editors persistent. Create @body-editor node?

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
            # Keys are chapter names, values are chapters.
            # Important: chapter names never change, even if their @chapter node changes.

        self.chaptersNode = None # Set later
        self.selectedChapter = None
        self.trace = False
        self.tt = None # May be set in finishCreate.
        self.use_tabs = c.config.getBool('use_chapter_tabs')

        # g.trace('chapterController',g.callers())
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
            if h.startswith(tag) and not h.startswith('@chapters'):
                tabName = h[len(tag):].strip()
                if tabName and tabName not in ('main',):
                    if cc.chaptersDict.get(tabName):
                        self.error('duplicate chapter name: %s' % tabName)
                    else:
                        cc.chaptersDict[tabName] = chapter(c=c,chapterController=cc,name=tabName,root=p)

        cc.selectChapterByName('main')
    #@-node:ekr.20070325104904:cc.finishCreate
    #@-node:ekr.20070530075604:Birth
    #@+node:ekr.20070317085437.30:Commands
    #@+node:ekr.20070317085437.50:cc.cloneNodeToChapter & helper
    def cloneNodeToChapter (self,event=None):

        '''Prompt for a chapter name,
        then clone the selected node to the chapter.'''

        cc = self ; k = cc.c.k ; tag = 'clone-node-to-chapter'
        state = k.getState(tag)

        if state == 0:
            names = cc.chaptersDict.keys()
            prefix = 'Clone node to chapter: '
            k.setLabelBlue(prefix,protect=True)
            k.getArg(event,tag,1,self.cloneNodeToChapter,prefix=prefix,tabList=names)
        else:
            k.clearState()
            k.resetLabel()
            if k.arg:
                cc.cloneNodeToChapterHelper(k.arg)
    #@nonl
    #@+node:ekr.20070604155815.1:cc.cloneToChapterHelper
    def cloneNodeToChapterHelper (self,toChapterName):

        cc = self ; c = cc.c
        p = c.currentPosition() ; h = p.headString()
        fromChapter = cc.getSelectedChapter()
        toChapter = cc.getChapter(toChapterName)
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
            c.selectPosition(clone)
            c.setChanged(True)
        finally:
            c.endUpdate(False)

        toChapter.p = clone.copy()
        toChapter.select()
        fromChapter.p = p.copy()
    #@-node:ekr.20070604155815.1:cc.cloneToChapterHelper
    #@-node:ekr.20070317085437.50:cc.cloneNodeToChapter & helper
    #@+node:ekr.20070317085437.51:cc.copyNodeToChapter & helper
    def copyNodeToChapter (self,event=None):

        '''Prompt for a chapter name,
        then copy the selected node to the chapter.'''

        cc = self ; k = cc.c.k ; tag = 'copy-node-to-chapter'
        state = k.getState(tag)

        if state == 0:
            names = cc.chaptersDict.keys()
            prefix = 'Copy node to chapter: '
            k.setLabelBlue(prefix,protect=True)
            k.getArg(event,tag,1,self.copyNodeToChapter,prefix=prefix,tabList=names)
        else:
            k.clearState()
            k.resetLabel()
            if k.arg:
                cc.copyNodeToChapterHelper(k.arg)
    #@nonl
    #@+node:ekr.20070604155815.2:cc.copyNodeToChapterHelper
    def copyNodeToChapterHelper (self,toChapterName):

        cc = self ; c = cc.c
        p = c.currentPosition() ; h = p.headString()
        fromChapter = cc.getSelectedChapter()
        toChapter = cc.getChapter(toChapterName)
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
        toChapter.select()
        fromChapter.p = p.copy()
    #@-node:ekr.20070604155815.2:cc.copyNodeToChapterHelper
    #@-node:ekr.20070317085437.51:cc.copyNodeToChapter & helper
    #@+node:ekr.20070317085437.31:cc.createChapter
    def createChapter (self,event=None,verbose=True):

        '''Use the minibuffer to get a chapter name,
        then create the chapter.'''

        cc = self ; k = cc.c.k ; tag = 'create-chapter'
        state = k.getState(tag)

        if state == 0:
            names = cc.chaptersDict.keys()
            k.setLabelBlue('Create chapter: ',protect=True)
            k.getArg(event,tag,1,self.createChapter,tabList=names)
        else:
            k.clearState()
            k.resetLabel()
            if k.arg:
                cc.createChapterByName(k.arg)
    #@nonl
    #@-node:ekr.20070317085437.31:cc.createChapter
    #@+node:ekr.20070607092909:cc.createChapterFromNode
    def createChapterFromNode (self,event=None):

        '''Use the minibuffer to get a chapter name,
        then create the chapter.'''

        cc = self ; c = cc.c ; k = c.k ; tag = 'create-chapter-from-node'
        state = k.getState(tag)

        p = c.currentPosition()
        if p.headString().startswith('@chapter'):
            cc.error('Can not create a new chapter from from an @chapter or @chapters node.')
            return

        if state == 0:
            names = cc.chaptersDict.keys()
            k.setLabelBlue('Create chapter from node: ',protect=True)
            k.getArg(event,tag,1,self.createChapterFromNode,tabList=names)
        else:
            k.clearState()
            k.resetLabel()
            if k.arg:
                cc.createChapterByName(k.arg,p=c.currentPosition())
    #@-node:ekr.20070607092909:cc.createChapterFromNode
    #@+node:ekr.20070603190617:cc.createChapterByName
    def createChapterByName (self,name,p=None):

        cc = self ; c = cc.c ; u = c.undoer

        if not name:
            return cc.error('No name')

        oldChapter = cc.getSelectedChapter()
        theChapter = cc.chaptersDict.get(name)
        if theChapter:
            return cc.error('Duplicate chapter name: %s' % name)

        bunch = u.beforeCreateChapter(c.currentPosition(),oldChapter.name,name)
        root = cc.getChapterNode(name,p=p) # Creates @chapter node and one child.
        cc.chaptersDict[name] = chapter(c=c,chapterController=cc,name=name,root=root)
        cc.selectChapterByName(name)
        u.afterCreateChapter(bunch,c.currentPosition())

        # g.es('created chapter %s' % (name),color='blue')
        return True
    #@-node:ekr.20070603190617:cc.createChapterByName
    #@+node:ekr.20070604155815.3:cc.moveNodeToChapter & helper
    def moveNodeToChapter (self,event=None):

        '''Prompt for a chapter name,
        then move the selected node to the chapter.'''

        cc = self ; k = cc.c.k ; tag = 'move-node-to-chapter'
        state = k.getState(tag)

        if state == 0:
            names = cc.chaptersDict.keys()
            prefix = 'Copy node to chapter: '
            k.setLabelBlue(prefix,protect=True)
            k.getArg(event,tag,1,self.moveNodeToChapter,prefix=prefix,tabList=names)
        else:
            k.clearState()
            k.resetLabel()
            if k.arg:
                cc.moveNodeToChapterHelper(k.arg)
    #@nonl
    #@+node:ekr.20070317085437.52:cc.moveNodeToChapterHelper
    def moveNodeToChapterHelper (self,toChapterName):

        cc = self ; c = cc.c ; p = c.currentPosition()
        fromChapter = cc.getSelectedChapter()
        toChapter = cc.getChapter(toChapterName)

        if 1: # Defensive code: should never happen.
            if fromChapter.name == 'main' and p.headString().startswith('@chapter'):
                return cc.error('can not move @chapter node')

        c.beginUpdate()
        try:
            if toChapter.name == 'main':
                sel = (p.threadBack() != fromChapter.root and p.threadBack()) or p.nodeAfterTree()
                if sel:
                    p.unlink()
                    p.moveAfter(toChapter.p)
                    c.selectPosition(sel)
                    c.setChanged(True)
            else:
                sel = p.threadBack() or p.nodeAfterTree()
                if sel:
                    parent = cc.getChapterNode(toChapter.name)
                    p.unlink()
                    p.moveToLastChildOf(parent)
                    c.selectPosition(sel)
                    c.setChanged(True)
        finally:
            c.endUpdate(False)

        if sel:
            toChapter.p = p.copy()
            toChapter.select()
            fromChapter.p = sel.copy()
        else:
            cc.error('Can not move the last node of a chapter.')
    #@-node:ekr.20070317085437.52:cc.moveNodeToChapterHelper
    #@-node:ekr.20070604155815.3:cc.moveNodeToChapter & helper
    #@+node:ekr.20070317085437.40:cc.removeChapter
    def removeChapter (self,event=None):

        cc = self ; c = cc.c

        theChapter = cc.selectedChapter
        if not theChapter: return

        name = theChapter.name

        if name == 'main':
            return cc.error('Can not remove the main chapter')
        else:
            cc.removeChapterByName(name)
    #@-node:ekr.20070317085437.40:cc.removeChapter
    #@+node:ekr.20070606075434:cc.removeChapterByName
    def removeChapterByName (self,name):

        cc = self ; c = cc.c ; tt = cc.tt

        c.beginUpdate()
        try:
            cc.deleteChapterNode(name)
            if name in cc.chaptersDict.keys():
                del cc.chaptersDict[name]
            if tt:tt.destroyTab(name)
            cc.selectChapterByName('main')
        finally:
            c.endUpdate()
    #@-node:ekr.20070606075434:cc.removeChapterByName
    #@+node:ekr.20070317085437.41:cc.renameChapter & testHelper
    # newName is for unitTesting.

    def renameChapter (self,event=None,newName=None):

        '''Use the minibuffer to get a new name for the present chapter.'''

        cc = self ; c = cc.c ; k = cc.c.k ; tt = cc.tt
        tag = 'rename-chapter'
        theChapter = cc.selectedChapter
        if not theChapter: return
        if theChapter.name == 'main':
            return cc.error('Can not rename the main chapter')

        state = k.getState(tag)

        if state == 0 and not newName:
            names = cc.chaptersDict.keys()
            prefix = 'Rename this chapter: '
            k.setLabelBlue(prefix,protect=True)
            k.getArg(event,tag,1,self.renameChapter,prefix=prefix,tabList=names)
        else:
            k.clearState()
            k.resetLabel()
            if newName: k.arg = newName
            if k.arg and k.arg != theChapter.name:
                oldChapterName = theChapter.name
                del cc.chaptersDict[theChapter.name]
                cc.chaptersDict[k.arg] = theChapter
                theChapter.name = k.arg
                root = theChapter.root
                root.initHeadString('@chapter %s' % k.arg)
                if tt:
                    tt.setTabLabel(k.arg)
                    tt.destroyTab(oldChapterName)
                    tt.createTab(k.arg)
                c.redraw_now()
    #@-node:ekr.20070317085437.41:cc.renameChapter & testHelper
    #@+node:ekr.20070604165126:cc.selectChapter
    def selectChapter (self,event=None):

        '''Use the minibuffer to get a chapter name,
        then create the chapter.'''

        cc = self ; k = cc.c.k ; tag = 'select-chapter'
        state = k.getState(tag)

        if state == 0:
            names = cc.chaptersDict.keys()
            prefix = 'Select chapter: '
            k.setLabelBlue(prefix,protect=True)
            k.getArg(event,tag,1,self.selectChapter,prefix=prefix,tabList=names)
        else:
            k.clearState()
            k.resetLabel()
            if k.arg:
                cc.selectChapterByName(k.arg)
    #@-node:ekr.20070604165126:cc.selectChapter
    #@+node:ekr.20070317130250:cc.selectChapterByName
    def selectChapterByName (self,name):

        cc = self ; c = cc.c ; chapter = cc.chaptersDict.get(name)

        if chapter:
            if chapter != cc.selectedChapter:
                if cc.selectedChapter:
                    cc.selectedChapter.unselect()
                chapter.select()
                c.setCurrentPosition(chapter.p)
                cc.selectedChapter = chapter
        else:
            cc.error('cc.selectShapter: no such chapter: %s' % name)
    #@-node:ekr.20070317130250:cc.selectChapterByName
    #@-node:ekr.20070317085437.30:Commands
    #@+node:ekr.20070511081405:Creating/deleting nodes (chapterController)
    #@+node:ekr.20070325101652:cc.createChaptersNode
    def createChaptersNode (self):

        cc = self ; c = cc.c ; root = c.rootPosition()

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
            c.setChanged(True)
        finally:
            c.endUpdate(False)
    #@nonl
    #@-node:ekr.20070325101652:cc.createChaptersNode
    #@+node:ekr.20070325063303.2:cc.createChapterNode
    def createChapterNode (self,chapterName,p=None):

        '''Create an @chapter node for the named chapter.
        Use p for the first child, or create a first child if p is None.'''

        cc = self ; c = cc.c
        current = c.currentPosition() or c.rootPosition()

        c.beginUpdate()
        try:
            # Create the node with a postion method
            # so we don't involve the undo logic.
            root = current.insertAsLastChild()
            root.initHeadString('@chapter ' + chapterName)
            root.moveToFirstChildOf(cc.chaptersNode)
            if p:
                # Clone p and move it to the first child of the root.
                clone = p.clone()
                clone.moveToFirstChildOf(root)
            else:
                cc.createChild(root,'%s node 1' % chapterName)
            c.setChanged(True)
        finally:
            c.endUpdate(False)

        return root
    #@-node:ekr.20070325063303.2:cc.createChapterNode
    #@+node:ekr.20070509081915.1:cc.createChild
    def createChild (self,parent,s):

        '''Create a child node of parent without changing the undo stack.
        set the headString of the new node to s.'''

        c = self.c
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
                c.setChanged(True)
            finally:
                c.endUpdate(False)
    #@nonl
    #@-node:ekr.20070325063303.4:cc.deleteChapterNode
    #@-node:ekr.20070511081405:Creating/deleting nodes (chapterController)
    #@+node:ekr.20070317130648:Utils
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

        for p in c.allNodes_iter():
            if p.headString() == '@chapters':
                cc.chaptersNode = p.copy()
                return p

        # This is *not* an error.
        return None
    #@-node:ekr.20070325094401:cc.findChaptersNode
    #@+node:ekr.20070605124356:cc.inChapter
    def inChapter (self):

        cc = self
        return cc.selectedChapter and cc.selectedChapter.name != 'main'
    #@-node:ekr.20070605124356:cc.inChapter
    #@+node:ekr.20070325115102:cc.getChaperNode
    def getChapterNode (self,chapterName,p=None):

        '''Return the position of the @chapter node with the given name.'''

        cc = self ; c = cc.c

        if chapterName == 'main':
            return c.rootPosition()
        else:
            val = (
                cc.findChapterNode(chapterName,giveError=False) or
                cc.createChapterNode(chapterName,p=p))
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
        self.cc = cc = chapterController
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

        if cc.tt:
            cc.tt.createTab(name)
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
    #@+node:ekr.20070317131205.1:chapter.select & helpers
    def select (self,w=None,selectEditor=True):

        '''Restore chapter information and redraw the tree when a chapter is selected.'''

        if self.selectLockout: return

        try:
            self.selectLockout = True
            self.chapterSelectHelper(w,selectEditor)
            if self.cc.tt:
                self.cc.tt.setTabLabel(self.name)
        finally:
            self.selectLockout = False
    #@+node:ekr.20070423102603.1:chapterSelectHelper
    def chapterSelectHelper (self,w=None,selectEditor=True):

        c = self.c ; cc = self.cc ; name = self.name

        # g.trace(name,'self.p',self.p) # ,'self.root',self.root) # 'w.leo_p',w and w.leo_p)

        cc.selectedChapter = self

        # Next, recompute p and possibly select a new editor.
        if w:
            assert w == c.frame.body.bodyCtrl
            assert w == c.frame.bodyCtrl
            assert w.leo_p
            # g.trace(name,'w.leo_p',w.leo_p,'p',p)
            self.p = p = self.findPositionInChapter(w.leo_p)
            if p != w.leo_p: g.trace('****** can not happen: lost p',w.leo_p)
        else:
            # This must be done *after* switching roots.
            target_p = self.p or self.root.firstChild() or self.root
            #g.trace(name,'target_p',target_p)
            #g.trace(name,'self.p',self.p,'self.root',self.root)
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
            g.doHook('hoist-changed',c=c)
            c.bodyWantsFocusNow()
    #@nonl
    #@-node:ekr.20070423102603.1:chapterSelectHelper
    #@+node:ekr.20070317131708:chapter.findPositionInChapter
    def findPositionInChapter (self,p1):

        '''Return a valid position p such that p.v == v.'''

        # Do nothing if the present position is in the proper chapter.
        c = self.c ; name = self.name 

        root = g.choose(self.name=='main',c.rootPosition(),self.root)
        # g.trace('p1',p1)
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
            self.error('***** chapter: %s findPositionInChapter: lost %s' % (
                self.name,p1.v.t.headString))
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
