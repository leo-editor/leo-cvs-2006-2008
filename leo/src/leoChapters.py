#@+leo-ver=4-thin
#@+node:ekr.20070317085508.1:@thin leoChapters.py
'''Classes that manage chapters in Leo's core.'''

#@@language python
#@@tabwidth -4
#@@pagewidth 80

import leoGlobals as g
import leoNodes

#@+others
#@+node:ekr.20070317085437:class chapterController
class chapterController:
    
    '''A per-commander controller.'''
    
    #@    @+others
    #@+node:ekr.20070318124624:Birth
    #@+node:ekr.20070317085437.2: ctor: chapterController
    def __init__ (self,c):
        
        self.c = c
        self.chaptersDict = {}
            # Keys are tabNames, values are chapters.
            # Important: tabNames never change, even if their button text changes.
        self.chaptersNode = None # Set later
        self.inited = False # Set in makeTrees.
        self.mainRoot = None # Set later
        self.nc = chapterNodesController(c,self)
        self.selectedChapter = None
        self.tabNames = []
        self.tt = None # Set in finishCreate.
        
    #@nonl
    #@-node:ekr.20070317085437.2: ctor: chapterController
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
        
        cc = self ; c = cc.c ; nc = cc.nc ; tt = cc.tt
        
        # Create the @chapters node if needed, and set cc.chaptersNode.
        if not cc.chaptersNode and not nc.findChaptersNode():
            nc.createChaptersNode()
            assert(cc.chaptersNode)
    
        if not nc.findChapterNode('trash'):
            nc.createChapterNode('trash')
            
        # Create a chapter for each @chapter node.
        tag = '@chapter'
        for p in cc.chaptersNode.children_iter():
            h = p.headString()
            if h.startswith(tag):
                tabName = h[len(tag):].strip()
                if tabName and tabName not in ('main','trash') and not self.chaptersDict.get(tabName):
                    theChapter = chapter(c=c,chapterController=cc,name=tabName,p=p,root=p)
                    self.chaptersDict[tabName] = theChapter
                    tt.createTab(tabName,select=False)
                    tt.makeTabMenu(tabName,theChapter)
                    # tt.lowerTab(tabName)
        
        for tabName in ('trash',):
            if not self.chaptersDict.get(tabName):
                p = nc.getChapterNode(tabName)
                self.chaptersDict[tabName] = chapter(c=c,chapterController=cc,name=tabName,p=p,root=p)
                
        for tabName in ('main',):
            if not self.chaptersDict.get(tabName):
                p = c.currentPosition()
                self.chaptersDict[tabName] = chapter(c=c,chapterController=cc,name=tabName,p=p,root=None)
                
        self.inited = True
    #@-node:ekr.20070325104904:cc.makeTrees
    #@-node:ekr.20070318124624:Birth
    #@+node:ekr.20070320091806:Callbacks (chapter)
    def selectCallback (self,tabName):
        
        chapter = self.chaptersDict.get(tabName)
        
        if chapter:
            chapter.select()
        else:
            self.error('select: no such chapter: %s' % tabName)
            
    def unselectCallback (self,tabName):
        
        chapter = self.chaptersDict.get(tabName)
        
        if chapter:
            chapter.unselect()
        else:
            self.error('unselect: no such chapter: %s' % tabName)
            
    def updateChapterName(self,oldName,newName):
        
        self.nc.updateChapterName(oldName,newName)
        
    #@-node:ekr.20070320091806:Callbacks (chapter)
    #@+node:ekr.20070317085437.30:Chapter commands
    #@+node:ekr.20070317085437.31:cc.createChapter
    numberOfChapters = 0
    
    def createChapter (self,event=None,name=None):
    
        cc = self ; c = cc.c ; tt = cc.tt
    
        if name:
            tabName = name
        else:
            # The **immutable** chapter name is 'Chapter n'.
            self.numberOfChapters += 1
            tabName = 'Chapter %d' % self.numberOfChapters
            
        # g.trace(tabName)
    
        if name in ('trash','main',):
            tt.selectTab(tabName)
        else:
            root = self.nc.getChapterNode(tabName)
            self.chaptersDict[tabName] = chapter(c=c,chapterController=cc,name=tabName,p=root)
            tt.selectTab(tabName)
            tt.renameChapterHelper(cc,tabName)
            
        theChapter = self.chaptersDict.get(tabName)
        tt.makeTabMenu(tabName,theChapter)
            
        # tt.selectTab indirectly unselects the previous chapter.
        cc.selectChapter(tabName=tabName)
       
        c.bodyWantsFocusNow()
    #@-node:ekr.20070317085437.31:cc.createChapter
    #@+node:ekr.20070421092158:cc.forceMainChapter
    def forceMainChapter (self):
        
        cc = self
        
        tabName = cc.tt.nb.getcurselection()
    
        if tabName != 'main':
            cc.selectChapter('main')
    
        return tabName
    #@-node:ekr.20070421092158:cc.forceMainChapter
    #@+node:ekr.20070317085437.39:cc.makeNodeIntoChapter (TO DO)
    def makeNodeIntoChapter (self,p=None,redraw=True):
        
        return ###
        
        cc = self ; c = cc.c
        renum = p and p.copy()
        if not p: p = c.currentPosition()
        
        if p == c.rootPosition() and not p.next(): return
        
        c.beginUpdate()
        try:
            p.doDelete()
        finally:
            c.endUpdate(False)
        
        page,pageName = self.addPage()
        mnChapter = self.getChapter(pageName)
        oldChapter = cc.currentChapter
        mnChapter.makeCurrent()
        root = mnChapter.rp
        p.moveAfter(root)
        c.setRootPosition(p)
        oldChapter.makeCurrent()
       
        c.beginUpdate()
        try:
            c.selectPosition(oldChapter.rp)
        finally:
            c.endUpdate(redraw)
            if redraw: cc.nb.selectpage(pageName)
    #@nonl
    #@-node:ekr.20070317085437.39:cc.makeNodeIntoChapter (TO DO)
    #@+node:ekr.20070317085437.40:cc.removeChapter
    def removeChapter (self,event=None):
    
        cc = self ; c = self.c ; tt = cc.tt
        name = tt.getSelectedTabName()
    
        if name == 'trash':
            return self.error('Can not remove the trash')
        if name == 'main':
            return self.error('Can not remove the main chapter')
    
        self.nc.deleteChapter(name)
        tt.destroyTab(name)
    #@-node:ekr.20070317085437.40:cc.removeChapter
    #@+node:ekr.20070317085437.41:cc.renameChapter
    def renameChapter (self,event=None):
        
        '''Handle the rename chapter command.'''
        
        cc = self ; tt = cc.tt
        tabName = tt.getSelectedTabName()
    
        if tabName == 'trash':
            return self.error('Can not rename the trash')
        if tabName == 'main':
            return self.error('Can not rename the main chapter')
    
        tt.renameChapterHelper(cc,tabName)
    #@-node:ekr.20070317085437.41:cc.renameChapter
    #@+node:ekr.20070317130250:cc.selectChapter
    def selectChapter (self,event=None,tabName=None):
    
        chapter = self.chaptersDict.get(tabName)
    
        if chapter:
            chapter.select()
        else:
            self.error('select chapter: no such chapter: %s' % tabName)
    #@-node:ekr.20070317130250:cc.selectChapter
    #@-node:ekr.20070317085437.30:Chapter commands
    #@+node:ekr.20070317085437.49:Node commands
    #@+node:ekr.20070317085437.50:cc.cloneToChapter
    def cloneToChapter (self,event=None,toChapter=None):
    
        cc = self ; c = cc.c ; nc = cc.nc ; tt = cc.tt
        p = c.currentPosition() ; h = p.headString()
        fromChapter = cc.getSelectedChapter()
        toChapter = cc.getChapter(toChapter)
        if fromChapter.name == 'main' and h.startswith('@chapter'):
            return self.error('can not clone @chapter node')
        # g.trace('from',fromChapter.name,'to',toChapter)
        
        c.beginUpdate()
        try:
            parent = nc.getChapterNode(toChapter.name)
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
        
        cc = self ; c = cc.c ; nc = cc.nc ; tt = cc.tt
        p = c.currentPosition() ; h = p.headString()
        fromChapter = cc.getSelectedChapter()
        toChapter = cc.getChapter(toChapter)
        if fromChapter.name == 'main' and h.startswith('@chapter'):
            return self.error('can not copy @chapter node')
        # g.trace('from',fromChapter.name,'to',toChapter.name)
    
        c.beginUpdate()
        try:
            parent = nc.getChapterNode(toChapter.name)
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
        
        cc = self ; c = cc.c ; nc = cc.nc ; tt = cc.tt
        p = c.currentPosition() ; h = p.headString()
        fromChapter = cc.getSelectedChapter()
        toChapter = cc.getChapter(toChapter)
        if fromChapter.name == 'main' and h.startswith('@chapter'):
            return self.error('can not move @chapter node')
        # g.trace('from',fromChapter.name,'to',toChapter.name)
    
        c.beginUpdate()
        try:
            parent = nc.getChapterNode(toChapter.name)
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
        chapter = self.getChapter('trash')
    
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
    #@+node:ekr.20070320085610:cc.error
    def error (self,s):
        
        if self.inited:
            g.es_print(s,color='red')
    #@-node:ekr.20070320085610:cc.error
    #@+node:ekr.20070318124004:cc.getChapter
    def getChapter(self,name):
        
        return self.chaptersDict.get(name)
    #@-node:ekr.20070318124004:cc.getChapter
    #@+node:ekr.20070318122708:cc.getSelectedChapter
    def getSelectedChapter (self):
    
        cc = self
        if cc.selectedChapter:
            return cc.selectedChapter
        else:
            tabName = self.tt.nb.getcurselection()
            return self.chaptersDict.get(tabName)
    #@-node:ekr.20070318122708:cc.getSelectedChapter
    #@-node:ekr.20070317130648:Utils
    #@-others
#@nonl
#@-node:ekr.20070317085437:class chapterController
#@+node:ekr.20070325063303:class chapterNodesController
class chapterNodesController:

    '''A class that manages @chapters and @chapter nodes.'''

    #@    @+others
    #@+node:ekr.20070325063303.1: ctor (chapterNodes)
    def __init__ (self,c,cc):
    
        self.c = c
        self.cc = cc
    #@-node:ekr.20070325063303.1: ctor (chapterNodes)
    #@+node:ekr.20070325063303.2:createChapterNode
    def createChapterNode (self,chapterName):
    
        '''Create an @chapter node for the named chapter,
        creating an @chapters node if necessary.'''
    
        nc = self ; c = nc.c ; current = c.currentPosition()
        
        # g.trace(chapterName,'current',current)
    
        # Defensive code: cc.makeTrees should have made the @chapters node.
        if not nc.findChaptersNode():
            nc.createChaptersNode()
    
        c.beginUpdate()
        try:
            # Create the node with a postion method
            # so we don't involve the undo logic.
            p = current.insertAsLastChild()
            p.initHeadString('@chapter ' + chapterName)
            c.setBodyString(p,chapterName)
            p.moveToFirstChildOf(self.root)
        finally:
            c.endUpdate(False)
            
        return p
    #@-node:ekr.20070325063303.2:createChapterNode
    #@+node:ekr.20070325101652:createChaptersNode
    def createChaptersNode (self):
        
        nc = self ; c = nc.c ; cc = nc.cc ; root = c.rootPosition()
        
        # g.trace('root',root)
    
        c.beginUpdate()
        try:
            # Create the node with a postion method
            # so we don't involve the undo logic.
            p = root.insertAsLastChild()
            p.initHeadString('@chapters')
            p.moveToRoot(oldRoot=root)
            c.setRootPosition(p)
            self.cc.chaptersNode = p.copy()
        finally:
            c.endUpdate(False)
    #@nonl
    #@-node:ekr.20070325101652:createChaptersNode
    #@+node:ekr.20070325063303.3:deleteAllChapters
    def deleteAllChapters (self):
    
        '''Destroy the entire @chapters tree.'''
        
        nc = self
    
        if nc.root:
            c.beginUpdate()
            try:
                c.setCurrentPosition(nc.root)
                c.deleteOutline(event=None,op_name=None)
            finally:
                c.endUpdate(False)
    #@nonl
    #@-node:ekr.20070325063303.3:deleteAllChapters
    #@+node:ekr.20070325063303.4:deleteChapter
    def deleteChapter (self,chapterName):
    
        '''Delete the @chapter with the given name.'''
        
        nc = self
    
        if not nc.root:
             return
    
        c.beginUpdate()
        try:
            c.setCurrentPosition(nc.root)
            c.deleteOutline(event=None,op_name=None)
        finally:
            c.endUpdate(False)
    #@nonl
    #@-node:ekr.20070325063303.4:deleteChapter
    #@+node:ekr.20070425072438:error
    def error (self,s):
        
        self.cc.error(s)
    #@nonl
    #@-node:ekr.20070425072438:error
    #@+node:ekr.20070325093617:findChapterNode
    def findChapterNode (self,chapterName):
    
        '''Return the position of the @chapter node with the given name.'''
        
        nc = self ; cc = self.cc
        
        if not cc.chaptersNode:
            return # An error has already been given.
    
        s = '@chapter ' + chapterName
        for p in cc.chaptersNode.children_iter():
            if p.headString() == s:
                return p
    
        self.error('*** chapterSelectHelper: no @chapter node for: %s' % (name))
    
        return None
    #@-node:ekr.20070325093617:findChapterNode
    #@+node:ekr.20070325094401:findChaptersNode
    def findChaptersNode (self):
    
        '''Return the position of the @chapters node.'''
    
        nc = self ; c = nc.c ; cc = nc.cc
    
        if not cc.mainRoot:
            g.trace('setting cc.mainRoot',c.rootPosition())
            cc.mainRoot = c.rootPosition()
    
        root = cc and cc.mainRoot
    
        for p in root.self_and_siblings_iter():
            if p.headString() == '@chapters':
                cc.chaptersNode = p.copy()
                return p
                
        g.trace('*** no @chapters node','cc.mainRoot',cc.mainRoot)
        self.error('*** findChaptersNode: no @chapters node')
    
        return None
    #@-node:ekr.20070325094401:findChaptersNode
    #@+node:ekr.20070325115102:getChaperNode
    def getChapterNode (self,chapterName):
    
        '''Return the position of the @chapter node with the given name.'''
        
        nc = self ; c = nc.c ; cc = self.cc
    
        if chapterName == 'main':
            if not cc.mainRoot:
                g.trace('*** setting mainRoot',c.rootPosition())
                cc.mainRoot = c.rootPosition()
            # g.trace('mainRoot',cc.mainRoot,'c.rootPosition',c.rootPosition())
            return cc.mainRoot
        else:
            val = (
                nc.findChapterNode(chapterName) or
                nc.createChapterNode(chapterName))
            # g.trace('chapterName',chapterName,'val',val)
            return val
    #@-node:ekr.20070325115102:getChaperNode
    #@+node:ekr.20070325121800:updateChapterName
    def updateChapterName(self,oldName,newName):
        
        '''oldName is the immutable name of a chapter.
        Set the visible name of that chapter to newName.'''
        
    
        nc = self ; c = nc.c
        
        p = nc.findChapterNode(oldName)
        
        if p:
            c.setBodyString(p,newName)
        else:
            nc.cc.error('no such chapter: %s' % oldName)
      
    #@nonl
    #@-node:ekr.20070325121800:updateChapterName
    #@-others
#@nonl
#@-node:ekr.20070325063303:class chapterNodesController
#@+node:ekr.20070317085708:class chapter
class chapter:
    
    '''A class representing the non-gui data of a single chapter.'''
       
    #@    @+others
    #@+node:ekr.20070325155208:Birth
    #@+node:ekr.20070317085708.1: ctor: chapter
    def __init__ (self,c,chapterController,name,p,root):
    
        self.c = c 
        self.cc = chapterController
        self.hoistStack = []
        self.inited = False
        self.name = name # The immutable tabName.
        self.nc = chapterController.nc
        self.p = p.copy() # The current position...
        self.root = root and root.copy() # The immutable @chapter node (not used for the main chapter).
        self.selectLockout = False # True: in chapter.select logic.
        self.unlinkData = None # Used to link the @chapter node back into the outline.
    #@-node:ekr.20070317085708.1: ctor: chapter
    #@+node:ekr.20070317085708.2:__str__ and __repr__(chapter)
    def __str__ (self):
        
        return '<chapter id: %s name: %s p: %s>' % (
            id(self),
            self.name,
            self.p and self.p.headString() or '<no p>')
    
    __repr__ = __str__
    #@-node:ekr.20070317085708.2:__str__ and __repr__(chapter)
    #@-node:ekr.20070325155208:Birth
    #@+node:ekr.20070325155208.1:chapter.error
    def error (self,s):
    
        self.cc.error(s)
    #@nonl
    #@-node:ekr.20070325155208.1:chapter.error
    #@+node:ekr.20070420173354:chapter.link/unlink
    def link (self):
        
        '''Link the chapter's @chapter node back into the full outline.'''
    
        b = self.unlinkData ; c = self.c ; cc = self.cc
        assert(b)
        c.setRootPosition(cc.mainRoot) # Restore the main outline.
        parent = cc.chaptersNode
        n,root = b.childIndex,b.root
        root.linkAsNthChild(parent,n)
        self.unlinkData = None
        
    def unlink (self):
        
        '''Unlink the root node (the chapter's @chapter node) from the full outine.
        set unlinkData for later use by self.link.'''
        
        cc = self.cc ; name = self.name ; root = self.root
        assert(name != 'main')
        assert(cc.chaptersNode)
        assert(root)
    
        # Remember the data.
        self.unlinkData = g.Bunch(childIndex=root.childIndex(),root=self.root)
        root.moveToRoot(oldRoot=None)
       
    #@nonl
    #@-node:ekr.20070420173354:chapter.link/unlink
    #@+node:ekr.20070317131205.1:chapter.select & helpers
    def select (self):
        
        '''Restore chapter information and redraw the tree when a chapter is selected.'''
        
        if self.selectLockout: return
        
        try:
            self.selectLockout = True
            self.chapterSelectHelper()
        finally:
            self.selectLockout = False
    
    #@+node:ekr.20070423102603.1:chapterSelectHelper
    def chapterSelectHelper (self):
    
        c = self.c ; cc = self.cc ; nc = self.nc ; tt = cc.tt ; name = self.name
    
        # The big switcharoo.
        canvas = tt.getCanvas(name)
        c.frame.canvas = c.frame.tree.canvas = canvas
    
        # An even bigger switcharoo.
        if name == 'main':
            root = cc.mainRoot
            c.setRootPosition(root)
        else:
            root = self.root
            self.unlink()
            c.setRootPosition(root)
    
        cc.selectedChapter = self
        g.trace('*** ',name,root)
    
        # This must be done *after* switching roots.
        p = self.findPositionInChapter(self.p.v)
        if not p:
            self.error(
                '***** chapter:select: can not happen: lost %s in %s' % (
                    self.p.v.t.headString,name))
            self.p = p = c.rootPosition()
    
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
                    c.frame.tree.setCanvasBindings(canvas)
                    c.k.completeAllBindingsForWidget(canvas)
                    if name != 'main':
                        root.expand()
                    c.selectPosition(root)
                    c.hoistStack = []
                    c.hoist()
                    self.hoistStack = c.hoistStack[:]
            # g.trace('chapter',name,'p.v',id(p.v),p.headString())
            ###w = c.frame.body.bodyCtrl
            ###c.frame.body.selectEditor(w) # Switches text.
        finally:
            c.endUpdate()
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
                            g.trace('*** found outside @chapters','v',p2.v)
                            return p2
    
            # for p in cc.mainRoot.self_and_siblings_iter():
                # if p.headString().startswith('@chapters'):
                    # for p2 in p.self_and_subtree_iter():
                        # if p2.v == v:
                            # # g.trace('found in @chapters','v',p2.v)
                            # return p2
        else:
            # Search only the @chapter tree.
            for p in self.root.self_and_subtree_iter():
                if p.v == v:
                    g.trace('*** found in chapter',p)
                    return p
                    
        g.trace('*** not found',v.t.headString)
        return None
    #@nonl
    #@-node:ekr.20070317131708:chapter.findPositionInChapter
    #@-node:ekr.20070317131205.1:chapter.select & helpers
    #@+node:ekr.20070320091806.1:chapter.unselect
    def unselect (self):
    
        '''Remember chapter info when a chapter is about to be unselected.'''
        
        # g.trace(self.name)
    
        c = self.c ; cc = self.cc
    
        self.hoistStack = c.hoistStack[:]
        self.p = c.currentPosition()
        
        # Restore the entire outline and
        # link the chapter's @chapter node into the entire outline.
        if self.name == 'main':
            # g.trace('*** setting mainRoot',c.rootPosition())
            cc.mainRoot = c.rootPosition()
        else:
            self.link()
    #@-node:ekr.20070320091806.1:chapter.unselect
    #@-others
#@nonl
#@-node:ekr.20070317085708:class chapter
#@-others
#@nonl
#@-node:ekr.20070317085508.1:@thin leoChapters.py
#@-leo
