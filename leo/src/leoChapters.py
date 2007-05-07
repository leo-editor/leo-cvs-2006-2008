#@+leo-ver=4-thin
#@+node:ekr.20070317085508.1:@thin leoChapters.py
'''Classes that manage chapters in Leo's core.'''

#@@language python
#@@tabwidth -4
#@@pagewidth 80

import leoGlobals as g

# To do: later or never:
# - Create commands to choose chapters.
# - Make body editors persistent. Create @body-editor node?

#@+others
#@+node:ekr.20070317085437:class chapterController
class chapterController:
    
    '''A per-commander controller that manages chapters and related nodes.'''
    
    #@    @+others
    #@+node:ekr.20070317085437.2: ctor: chapterController
    def __init__ (self,c):
        
        self.c = c
        self.chaptersDict = {}
            # Keys are tabNames, values are chapters.
            # Important: tabNames never change, even if their button text changes.
        self.chaptersLinked = True # True: the @chapters node is linked into the outline.
        self.chaptersNode = None # Set later
        self.inited = False # Set in makeTrees.
        self.mainRoot = None # Set later
        self.oldMainRoot = None # Set to cc.mainRoot in cc.unlinkChaptersNode.
        self.selectedChapter = None
        self.tabNames = []
        self.trace = False
        self.tt = None # Set in finishCreate.
    #@-node:ekr.20070317085437.2: ctor: chapterController
    #@+node:ekr.20070320091806:Callbacks (chapter)
    def selectCallback (self,tabName):
        
        cc = self ; chapter = cc.chaptersDict.get(tabName)
        if chapter:
            chapter.select()
        else:
            cc.error('select: no such chapter: %s' % tabName)
            
    def unselectCallback (self,tabName):
        
        cc = self ; chapter = cc.chaptersDict.get(tabName)
        if chapter:
            chapter.unselect()
        else:
            cc.error('unselect: no such chapter: %s' % tabName)
    #@-node:ekr.20070320091806:Callbacks (chapter)
    #@+node:ekr.20070318124624.1:cc.finishCreate
    def finishCreate (self,treeTabController):
        
        cc = self ; c = cc.c
    
        cc.tt = treeTabController
        cc.createChapter(name='trash')
        cc.createChapter(name='main')
    #@nonl
    #@-node:ekr.20070318124624.1:cc.finishCreate
    #@+node:ekr.20070325104904:cc.makeTrees
    def makeTrees (self):
        
        '''Find or make the @chapters and @chapter trash nodes.'''
        
        # This must be called late in the init process:
        # at present, called by g.openWithFileName and c.new.
    
        cc = self ; c = cc.c ; tt = cc.tt
    
        # Create the @chapters node if needed, and set cc.chaptersNode.
        if not cc.chaptersNode and not cc.findChaptersNode():
            cc.createChaptersNode()
            
        # The chapters node is always unlinked, except when saving .leo files.
        cc.unlinkChaptersNode()
            
        if not cc.findChapterNode('trash'):
            cc.createChapterNode('trash')
            
        # Create a chapter for each @chapter node.
        tag = '@chapter'
        for p in cc.chaptersNode.children_iter():
            h = p.headString()
            if h.startswith(tag):
                tabName = h[len(tag):].strip()
                if tabName and tabName not in ('main','trash') and not cc.chaptersDict.get(tabName):
                    theChapter = chapter(c=c,chapterController=cc,name=tabName,p=p,root=p)
                    cc.chaptersDict[tabName] = theChapter
                    tt.createTab(tabName,select=False)
                    tt.makeTabMenu(tabName)
        
        for tabName in ('trash',):
            if not cc.chaptersDict.get(tabName):
                p = cc.getChapterNode(tabName)
                cc.chaptersDict[tabName] = chapter(c=c,chapterController=cc,name=tabName,p=p,root=p)
                
        for tabName in ('main',):
            if not cc.chaptersDict.get(tabName):
                p = c.currentPosition()
                cc.chaptersDict[tabName] = chapter(c=c,chapterController=cc,name=tabName,p=p,root=None)
                
        cc.selectChapter('main')
        cc.inited = True
    #@nonl
    #@-node:ekr.20070325104904:cc.makeTrees
    #@+node:ekr.20070317085437.30:Chapter commands
    #@+node:ekr.20070317085437.31:cc.createChapter
    def createChapter (self,event=None,name=None):
    
        cc = self ; c = cc.c ; tt = cc.tt
    
        if name:
            tabName = name
        else:
            # Find an unused name.  This is *not* the present number of chapters + 1
            # The **immutable** chapter name is 'Chapter n'.
            n  = 1
            while True:
                tabName = 'Chapter %d' % n
                if self.chaptersDict.get(tabName):
                    n += 1
                else:
                    break
            
        # g.trace(name)
    
        if name in ('trash','main',):
            tt.selectTab(tabName)
        else:
            root = cc.getChapterNode(tabName)
            cc.chaptersDict[tabName] = chapter(c=c,chapterController=cc,name=tabName,p=root,root=root)
            tt.selectTab(tabName)
            tt.renameChapterHelper(cc,tabName)
            
        theChapter = cc.chaptersDict.get(tabName)
        tt.makeTabMenu(tabName)
            
        # tt.selectTab indirectly unselects the previous chapter.
        cc.selectChapter(tabName)
       
        c.bodyWantsFocusNow()
    #@-node:ekr.20070317085437.31:cc.createChapter
    #@+node:ekr.20070317085437.39:cc.makeNodeIntoChapter (TO DO)
    def makeNodeIntoChapter (self,p=None,redraw=True):
        
        pass
        
        # cc = self ; c = cc.c
        # renum = p and p.copy()
        # if not p: p = c.currentPosition()
        
        # if p == c.rootPosition() and not p.next(): return
        
        # c.beginUpdate()
        # try:
            # p.doDelete()
        # finally:
            # c.endUpdate(False)
        
        # page,pageName = cc.addPage()
        # mnChapter = cc.getChapter(pageName)
        # oldChapter = cc.currentChapter
        # mnChapter.makeCurrent()
        # root = mnChapter.rp
        # p.moveAfter(root)
        # c.setRootPosition(p)
        # oldChapter.makeCurrent()
       
        # c.beginUpdate()
        # try:
            # c.selectPosition(oldChapter.rp)
        # finally:
            # c.endUpdate(redraw)
            # if redraw: cc.nb.selectpage(pageName)
    #@nonl
    #@-node:ekr.20070317085437.39:cc.makeNodeIntoChapter (TO DO)
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
        finally:
            c.endUpdate(False)
    
        toChapter.p = p2.copy()
        tt.selectTab(toChapter.name)
        fromChapter.p = p.copy()
    #@-node:ekr.20070317085437.51:cc.copyToChapter
    #@+node:ekr.20070317085437.52:cc.moveToChapter
    def moveToChapter (self,event=None,toChapter=None):
        
        cc = self ; c = cc.c ; tt = cc.tt
        p = c.currentPosition() ; h = p.headString()
        fromChapter = cc.getSelectedChapter()
        toChapter = cc.getChapter(toChapter)
        if fromChapter.name == 'main' and h.startswith('@chapter'):
            return cc.error('can not move @chapter node')
        # g.trace('from',fromChapter.name,'to',toChapter.name)
    
        c.beginUpdate()
        try:
            parent = cc.getChapterNode(toChapter.name)
            sel = p.back() or p.next() or parent
            p.unlink()
            p.moveToLastChildOf(parent)
            c.selectPosition(p)
        finally:
            c.endUpdate(False)
    
        toChapter.p = p.copy() # Must be done before tt.selectTab.
        tt.selectTab(toChapter.name)
        fromChapter.p = sel.copy() # Must be done after tt.selectTab.
    #@-node:ekr.20070317085437.52:cc.moveToChapter
    #@+node:ekr.20070317085437.29:cc.emptyTrash
    def emptyTrash (self):
        
        cc = self ; c = cc.c
        chapter = cc.getChapter('trash')
    
        root = chapter.rp
        chapter.setVariables()
        p = root.insertAfter()
        p.moveToRoot()
        p.setHeadString('trash barrel')
        chapter.rp = c.rootPosition()
        chapter.cp = c.currentPosition()
        chapter.tp = c.topPosition()
        cc.currentChapter.setVariables()
        
        c.beginUpdate()
        try:
            c.selectPosition(p)
        finally:
            c.endUpdate()
    #@nonl
    #@-node:ekr.20070317085437.29:cc.emptyTrash
    #@-node:ekr.20070317085437.49:Node commands
    #@+node:ekr.20070317130648:Utils
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
            t = p.v.t
            if t.fileIndex:
                self.error('***** t.fileIndex already exists')
            else:
                t.setFileIndex(g.app.nodeIndices.getNewIndex())
        finally:
            c.endUpdate(False)
            
        return p
    #@-node:ekr.20070325063303.2:cc.createChapterNode
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
    #@+node:ekr.20070325063303.4:cc.deleteChapterNode
    def deleteChapterNode (self,chapterName):
    
        '''Delete the @chapter with the given name.'''
        
        cc = self ; c = cc.c
        
        chapter = cc.chaptersDict.get(chapterName)
    
        if chapter:
            c.beginUpdate()
            try:
                c.setCurrentPosition(chapter.root)
                c.deleteOutline(event=None,op_name=None)
            finally:
                c.endUpdate(False)
    #@nonl
    #@-node:ekr.20070325063303.4:cc.deleteChapterNode
    #@+node:ekr.20070320085610:cc.error
    def error (self,s):
        
        cc = self
        
        if cc.inited:
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
            if p.headString() == s:
                return p
    
        if giveError:
            cc.error('*** findChapterNode: no @chapter node for: %s' % (chapterName))
    
        return None
    #@-node:ekr.20070325093617:cc.findChapterNode
    #@+node:ekr.20070325094401:cc.findChaptersNode
    def findChaptersNode (self):
    
        '''Return the position of the @chapters node.'''
    
        cc = self ; c = cc.c
    
        if not cc.mainRoot:
            if self.trace: g.trace('*** setting mainRoot',c.rootPosition())
            cc.mainRoot = c.rootPosition()
    
        root = cc and cc.mainRoot
    
        for p in root.self_and_siblings_iter():
            if p.headString() == '@chapters':
                cc.chaptersNode = p.copy()
                return p
                
        if 0: # This is *not* an error.
            g.trace('*** no @chapters node','cc.mainRoot',cc.mainRoot)
    
        return None
    #@-node:ekr.20070325094401:cc.findChaptersNode
    #@+node:ekr.20070421092158:cc.forceMainChapter
    def forceMainChapter (self):
        
        cc = self
        oldChapter = cc.getSelectedChapter()
        # g.trace(oldChapter)
        
        if oldChapter:
            if oldChapter.name == 'main':
                oldChapter = None # Don't unlink the main chapter in unlinkChaptersNode.
            else:
                oldChapter.link()
                if self.trace: g.trace('oldChapter',oldChapter.name)
        
        cc.linkChaptersNode()
    
        return oldChapter
    #@-node:ekr.20070421092158:cc.forceMainChapter
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
    #@+node:ekr.20070503083301:cc.linkChaptersNode
    def linkChaptersNode (self):
        
        cc = self
        
        if not cc.chaptersNode:
            self.error('***** no @chapters node')
        elif not cc.mainRoot:
            self.error('***** no cc.mainRoot')
        elif cc.chaptersLinked:
            g.trace('***** can not happen: @chapters already linked')
        else:
            cc.chaptersLinked = True
            cc.oldMainRoot = cc.mainRoot
            cc.chaptersNode.linkAsRoot(oldRoot=cc.mainRoot)
            if self.trace: g.trace('*** setting mainRoot',cc.chaptersNode)
            cc.mainRoot = cc.chaptersNode
    #@-node:ekr.20070503083301:cc.linkChaptersNode
    #@+node:ekr.20070503082757:cc.restoreOldChapter
    def restoreOldChapter (self, oldChapter):
        
        cc = self ; c = self.c
        
        # g.trace(oldChapter)
        cc.unlinkChaptersNode()
        if oldChapter:
            oldChapter.unlink()
            oldChapter.select()
       
    #@nonl
    #@-node:ekr.20070503082757:cc.restoreOldChapter
    #@+node:ekr.20070317130250:cc.selectChapter
    def selectChapter (self,tabName):
    
        cc = self ; chapter = cc.chaptersDict.get(tabName)
    
        if chapter:
            chapter.select()
        else:
            cc.error('select chapter: no such chapter: %s' % tabName)
    #@-node:ekr.20070317130250:cc.selectChapter
    #@+node:ekr.20070503081539:cc.unlinkChaptersNode
    def unlinkChaptersNode (self):
        
        '''unlink the @chapters node from the headline.'''
        
        cc = self ; c = cc.c
        
        if not cc.chaptersNode:
            g.trace('***** can not happen: no @chapters node')
        elif not cc.chaptersLinked:
            g.trace('***** can not happen: @chapters already unlinked')
        else:
            c.beginUpdate()
            try:
                p = cc.chaptersNode
                newRoot = cc.oldMainRoot or p.back() or p.next()
                if newRoot:
                    # Test whether we are in the @chpaters tree **before** unlinking.
                    current = c.currentPosition()
                    inChaptersFlag = cc.chaptersNode == current or cc.chaptersNode.isAncestorOf(current)
                    if self.trace: g.trace('*** unlinking @chapters node','newRoot',newRoot)
                    cc.chaptersNode.unlink() # unlink the node.
                    if self.trace: g.trace('*** setting mainRoot',newRoot)
                    cc.mainRoot = newRoot
                    c.setRootPosition(newRoot)
                    if inChaptersFlag:
                        # g.trace('setting position to',newRoot.headString())
                        c.setCurrentPosition(newRoot)
                else:
                    self.error('***** no new root')
            finally:
                cc.oldMainRoot = None
                cc.chaptersLinked = False
                c.endUpdate(flag=False) # Do not redraw: the canvas has not been saved/restored.
    #@-node:ekr.20070503081539:cc.unlinkChaptersNode
    #@+node:ekr.20070325121800:cc.updateChapterName
    def updateChapterName(self,oldName,newName):
        
        '''oldName is the immutable name of a chapter.
        Set the visible name of that chapter to newName.'''
        
    
        cc = self ; c = cc.c
        
        p = cc.findChapterNode(oldName)
        
        if p:
            c.setBodyString(p,newName)
        else:
            cc.error('no such chapter: %s' % oldName)
      
    #@nonl
    #@-node:ekr.20070325121800:cc.updateChapterName
    #@-node:ekr.20070317130648:Utils
    #@-others
#@nonl
#@-node:ekr.20070317085437:class chapterController
#@+node:ekr.20070317085708:class chapter
class chapter:
    
    '''A class representing the non-gui data of a single chapter.'''
       
    #@    @+others
    #@+node:ekr.20070317085708.1: ctor: chapter
    def __init__ (self,c,chapterController,name,p,root):
    
        self.c = c 
        self.cc = chapterController
        self.hoistStack = []
        self.inited = False
        self.name = name # The immutable chapter name.  Not necessarily the same as the chapter's tabName.
        self.p = p.copy() # The current position...
        self.root = root and root.copy() # The immutable @chapter node (not used for the main chapter).
        self.selectLockout = False # True: in chapter.select logic.
        self.trace = False
        self.unlinkData = None # Used to link the @chapter node back into the outline.
        
        # g.trace('chapter','name',self.name,'p',self.p.headString())
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
    def link (self):
        
        '''Link the chapter's @chapter node back into the full outline.'''
    
        b = self.unlinkData ; c = self.c ; cc = self.cc
        if self.trace: g.trace('chapter',self.name,'unlinkData.root',b and b.root)
        if b:
            c.setRootPosition(cc.mainRoot) # Restore the main outline.
            parent = cc.chaptersNode
            n,root = b.childIndex,b.root
            root.linkAsNthChild(parent,n)
            self.unlinkData = None
        else:
            g.trace('**** can not happen: no unlinkData')
        
    def unlink (self):
        
        '''Unlink the root node (the chapter's @chapter node) from the full outine.
        set unlinkData for later use by self.link.'''
        
        cc = self.cc ; name = self.name ; root = self.root
        assert(name != 'main')
        assert(cc.chaptersNode)
        assert(root)
    
        # Remember the data.
        self.unlinkData = g.Bunch(childIndex=root.childIndex(),root=root)
        if self.trace: g.trace('chapter',self.name,'unlinkData.root',root)
        root.moveToRoot(oldRoot=None)
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
    def chapterSelectHelper (self,w,selectEditor):
    
        c = self.c ; cc = self.cc ; tt = cc.tt ; name = self.name
    
        # The big switcharoo.
        c.frame.canvas = canvas = tt.getCanvas(name)
        c.frame.tree = tree = tt.getTree(name)
        
        if self.trace: g.trace('chapter',self.name,'p',self.p.headString())
        
        if name == 'main':
            root = cc.mainRoot
            c.setRootPosition(root)
        else:
            root = self.root
            self.unlink()
            c.setRootPosition(root)
    
        cc.selectedChapter = self
    
        # Switch to the new editor.
        if selectEditor:
            if w:
                assert w == c.frame.body.bodyCtrl
                assert w == c.frame.bodyCtrl
                p = self.findPositionInChapter(w.leo_p.v)
                if p != w.leo_p: g.trace('****** can not happen: lost p',w.leo_p,p)
            else:
                 # This must be done *after* switching roots.
                p = self.findPositionInChapter(self.p.v) ######################
                w = self.findEditorInChapter(p)
                c.frame.body.selectEditor(w) # Switches text.
    
        # g.trace('   ***',id(w),root.headString(),p.headString())
    
        c.beginUpdate()
        try:
            if self.inited:
                c.selectPosition(p)
                c.hoistStack = self.hoistStack[:] # Restore the hoist state.
            else:
                self.inited = True
                if name == 'main': # Clear all hoists.
                    c.hoistStack = []
                    c.selectPosition(p)
                else: # Finish initing the canvas and do the initial hoist.
                    # g.trace('finish init',name)
                    tree.setBindings()
                    if name != 'main':
                        root.expand()
                    c.selectPosition(root)
                    c.hoistStack = []
                    c.hoist()
                    self.hoistStack = c.hoistStack[:]
            # g.trace('chapter',name,'p.v',id(p.v),p.headString())
        finally:
            c.endUpdate()
            c.bodyWantsFocusNow()
    #@nonl
    #@-node:ekr.20070423102603.1:chapterSelectHelper
    #@+node:ekr.20070317131708:chapter.findPositionInChapter
    def findPositionInChapter (self,v):
        
        '''Return a valid position p such that p.v == v.'''
        
        cc = self.cc ; name = self.name
    
        if name == 'main':
            # Search the entire tree, but not the @chapters tree.
            assert(cc.mainRoot)
            for p in cc.mainRoot.self_and_siblings_iter():
                if not p.headString().startswith('@chapters'):
                    for p2 in p.self_and_subtree_iter():
                        if p2.v == v:
                            if self.trace: g.trace('*** found outside @chapters','v',p2.v)
                            return p2
        else:
            # Search only the @chapter tree.
            for p in self.root.self_and_subtree_iter():
                if p.v == v:
                    if self.trace: g.trace('*** found in chapter',p)
                    return p
        
        self.error('***** findPositionInChapter: lost %s in %s' % (v.t.headString,name))
        g.trace(g.callers())
        if 0: # This could crash.
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
