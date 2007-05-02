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
    
    '''A per-commander controller that manages chapters and related nodes.'''
    
    #@    @+others
    #@+node:ekr.20070317085437.2: ctor: chapterController
    def __init__ (self,c):
        
        self.c = c
        self.chaptersDict = {}
            # Keys are tabNames, values are chapters.
            # Important: tabNames never change, even if their button text changes.
        self.chaptersNode = None # Set later
        self.inited = False # Set in makeTrees.
        self.mainRoot = None # Set later
        self.selectedChapter = None
        self.tabNames = []
        self.tt = None # Set in finishCreate.
        
    #@nonl
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
            
    def updateChapterName(self,oldName,newName):
        
        cc = self
        cc.updateChapterName(oldName,newName)
    #@nonl
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
            assert(cc.chaptersNode)
    
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
                    tt.makeTabMenu(tabName,theChapter)
                    # tt.lowerTab(tabName)
        
        for tabName in ('trash',):
            if not cc.chaptersDict.get(tabName):
                p = cc.getChapterNode(tabName)
                cc.chaptersDict[tabName] = chapter(c=c,chapterController=cc,name=tabName,p=p,root=p)
                
        for tabName in ('main',):
            if not cc.chaptersDict.get(tabName):
                p = c.currentPosition()
                cc.chaptersDict[tabName] = chapter(c=c,chapterController=cc,name=tabName,p=p,root=None)
                
        cc.inited = True
    #@-node:ekr.20070325104904:cc.makeTrees
    #@+node:ekr.20070317085437.30:Chapter commands
    #@+node:ekr.20070317085437.31:cc.createChapter
    numberOfChapters = 0
    
    def createChapter (self,event=None,name=None):
    
        cc = self ; c = cc.c ; tt = cc.tt
    
        if name:
            tabName = name
        else:
            # The **immutable** chapter name is 'Chapter n'.
            cc.numberOfChapters += 1
            tabName = 'Chapter %d' % cc.numberOfChapters
            
        # g.trace(tabName)
    
        if name in ('trash','main',):
            tt.selectTab(tabName)
        else:
            root = cc.getChapterNode(tabName)
            cc.chaptersDict[tabName] = chapter(c=c,chapterController=cc,name=tabName,p=root)
            tt.selectTab(tabName)
            tt.renameChapterHelper(cc,tabName)
            
        theChapter = cc.chaptersDict.get(tabName)
        tt.makeTabMenu(tabName,theChapter)
            
        # tt.selectTab indirectly unselects the previous chapter.
        cc.selectChapter(tabName)
       
        c.bodyWantsFocusNow()
    #@-node:ekr.20070317085437.31:cc.createChapter
    #@+node:ekr.20070421092158:cc.forceMainChapter
    def forceMainChapter (self):
        
        cc = self
        oldChapter = cc.getSelectedChapter()
    
        if oldChapter.name != 'main':
            oldChapter.unselect()
            cc.selectChapter('main')
            
        # g.trace('-----',oldChapter.name)
    
        return oldChapter.name
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
        
        page,pageName = cc.addPage()
        mnChapter = cc.getChapter(pageName)
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
    #@+node:ekr.20070325063303:Node utils
    #@+node:ekr.20070317130250:cc.selectChapter
    def selectChapter (self,tabName):
    
        cc = self ; chapter = cc.chaptersDict.get(tabName)
    
        if chapter:
            chapter.select()
        else:
            cc.error('select chapter: no such chapter: %s' % tabName)
    #@-node:ekr.20070317130250:cc.selectChapter
    #@+node:ekr.20070325063303.2:createChapterNode
    def createChapterNode (self,chapterName):
    
        '''Create an @chapter node for the named chapter,
        creating an @chapters node if necessary.'''
    
        cc = self ; c = cc.c ; current = c.currentPosition()
        
        # g.trace(chapterName,'current',current)
    
        # Defensive code: cc.makeTrees should have made the @chapters node.
        if not cc.findChaptersNode():
            cc.createChaptersNode()
    
        c.beginUpdate()
        try:
            # Create the node with a postion method
            # so we don't involve the undo logic.
            p = current.insertAsLastChild()
            p.initHeadString('@chapter ' + chapterName)
            c.setBodyString(p,chapterName)
            p.moveToFirstChildOf(cc.chaptersNode)
        finally:
            c.endUpdate(False)
            
        return p
    #@-node:ekr.20070325063303.2:createChapterNode
    #@+node:ekr.20070325101652:createChaptersNode
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
        finally:
            c.endUpdate(False)
    #@nonl
    #@-node:ekr.20070325101652:createChaptersNode
    #@+node:ekr.20070325063303.4:deleteChapterNode
    def deleteChapterNode (self,chapterName):
    
        '''Delete the @chapter with the given name.'''
        
        cc = self
        
        chapter = cc.chaptersDict.get(chapterName)
    
        if chpater:
            c.beginUpdate()
            try:
                c.setCurrentPosition(chapter.root)
                c.deleteOutline(event=None,op_name=None)
            finally:
                c.endUpdate(False)
    #@nonl
    #@-node:ekr.20070325063303.4:deleteChapterNode
    #@+node:ekr.20070325093617:findChapterNode
    def findChapterNode (self,chapterName):
    
        '''Return the position of the @chapter node with the given name.'''
        
        cc = self
        
        if not cc.chaptersNode:
            return # An error has already been given.
    
        s = '@chapter ' + chapterName
        for p in cc.chaptersNode.children_iter():
            if p.headString() == s:
                return p
    
        cc.error('*** chapterSelectHelper: no @chapter node for: %s' % (chapterName))
    
        return None
    #@-node:ekr.20070325093617:findChapterNode
    #@+node:ekr.20070325094401:findChaptersNode
    def findChaptersNode (self):
    
        '''Return the position of the @chapters node.'''
    
        cc = self ; c = cc.c
    
        if not cc.mainRoot:
            # g.trace('setting cc.mainRoot',c.rootPosition())
            cc.mainRoot = c.rootPosition()
    
        root = cc and cc.mainRoot
    
        for p in root.self_and_siblings_iter():
            if p.headString() == '@chapters':
                cc.chaptersNode = p.copy()
                return p
                
        # g.trace('*** no @chapters node','cc.mainRoot',cc.mainRoot)
        # cc.error('*** findChaptersNode: no @chapters node')
    
        return None
    #@-node:ekr.20070325094401:findChaptersNode
    #@+node:ekr.20070325115102:getChaperNode
    def getChapterNode (self,chapterName):
    
        '''Return the position of the @chapter node with the given name.'''
        
        cc = self ; c = cc.c
    
        if chapterName == 'main':
            if not cc.mainRoot:
                g.trace('*** setting mainRoot',c.rootPosition())
                cc.mainRoot = c.rootPosition()
            # g.trace('mainRoot',cc.mainRoot,'c.rootPosition',c.rootPosition())
            return cc.mainRoot
        else:
            val = (
                cc.findChapterNode(chapterName) or
                cc.createChapterNode(chapterName))
            # g.trace('chapterName',chapterName,'val',val)
            return val
    #@-node:ekr.20070325115102:getChaperNode
    #@+node:ekr.20070325121800:updateChapterName
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
    #@-node:ekr.20070325121800:updateChapterName
    #@-node:ekr.20070325063303:Node utils
    #@+node:ekr.20070317130648:Utils
    #@+node:ekr.20070320085610:cc.error
    def error (self,s):
        
        cc = self
        
        if cc.inited:
            g.es_print(s,color='red')
    #@-node:ekr.20070320085610:cc.error
    #@+node:ekr.20070318124004:cc.getChapter
    def getChapter(self,name):
        
        cc = self
        
        return cc.chaptersDict.get(name)
    #@-node:ekr.20070318124004:cc.getChapter
    #@+node:ekr.20070318122708:cc.getSelectedChapter
    def getSelectedChapter (self):
    
        cc = self
    
        if cc.selectedChapter:
            return cc.selectedChapter
        else:
            tabName = cc.tt.nb.getcurselection()
            return cc.chaptersDict.get(tabName)
    #@-node:ekr.20070318122708:cc.getSelectedChapter
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
        self.unlinkData = g.Bunch(childIndex=root.childIndex(),root=root)
        root.moveToRoot(oldRoot=None)
       
    #@nonl
    #@-node:ekr.20070420173354:chapter.link/unlink
    #@+node:ekr.20070317131205.1:chapter.select & helpers
    def select (self,w=None):
        
        '''Restore chapter information and redraw the tree when a chapter is selected.'''
        
        if self.selectLockout: return
        
        try:
            self.selectLockout = True
            self.chapterSelectHelper(w)
        finally:
            self.selectLockout = False
    #@+node:ekr.20070423102603.1:chapterSelectHelper
    def chapterSelectHelper (self,w):
    
        c = self.c ; cc = self.cc ; tt = cc.tt ; name = self.name
    
        # The big switcharoo.
        c.frame.canvas = canvas = tt.getCanvas(name)
        c.frame.tree = tree = tt.getTree(name)
        
        if name == 'main':
            root = cc.mainRoot
            c.setRootPosition(root)
        else:
            root = self.root
            self.unlink()
            c.setRootPosition(root)
    
        cc.selectedChapter = self
    
        # Switch to the new editor.
        if w:
            assert w == c.frame.body.bodyCtrl
            assert w == c.frame.bodyCtrl
            p = self.findPositionInChapter(w.leo_p.v)
            if p != w.leo_p: g.trace('****** can not happen: lost p',w.leo_p,p)
        else:
             # This must be done *after* switching roots.
            p = self.findPositionInChapter(self.p.v)
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
                    g.trace('finish init',name)
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
                            # g.trace('*** found outside @chapters','v',p2.v)
                            return p2
        else:
            # Search only the @chapter tree.
            for p in self.root.self_and_subtree_iter():
                if p.v == v:
                    # g.trace('*** found in chapter',p)
                    return p
                    
        g.es_print('***** findPositionInChapter: lost %s in %s' % (v.t.headString,name))
        print 'cc.mainRoot',cc.mainRoot
        # print '******* top-level nodes *****'
        # for p in cc.mainRoot.self_and_siblings_iter():
            # print p.headStirng()
        return None
    #@nonl
    #@-node:ekr.20070317131708:chapter.findPositionInChapter
    #@+node:ekr.20070425175522:chapter.findEditorInChapter
    def findEditorInChapter (self,p):
        
        '''return w, an editor displaying position p.'''
        
        chapter = self ; c = self.c
    
        w = c.frame.body.findEditorForChapter(chapter,p)
        w.leo_chapter = chapter
        w.leo_p = p.copy()
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
        # g.trace('chapter','***',self.name,self.p.headString())
        
        # Restore the entire outline and
        # link the chapter's @chapter node into the entire outline.
        if self.name == 'main':
            # g.trace('*** setting mainRoot',c.rootPosition(),g.callers())
            cc.mainRoot = c.rootPosition()
        else:
            self.link()
            
        cc.selectedChapter = None
    #@-node:ekr.20070320091806.1:chapter.unselect
    #@-others
#@nonl
#@-node:ekr.20070317085708:class chapter
#@-others
#@nonl
#@-node:ekr.20070317085508.1:@thin leoChapters.py
#@-leo
