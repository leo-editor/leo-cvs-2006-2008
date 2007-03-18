#@+leo-ver=4-thin
#@+node:ekr.20070317085508.1:@thin leoChapters.py
'''Classes that manage chapters in Leo's core.'''

#@@language python
#@@tabwidth -4
#@@pagewidth 80

import leoGlobals as g

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
        self.tabNames = []
        self.tt = None # Set in finishCreate.
        
        # self.frame = frame
        # self.parentFrame = parentFrame
        
        # # Ivars for communication between cc.createCanvas and cc.treeInit.
        # # This greatly simplifies the init logic.
        # self.newCanvas = None
        # self.newPageName = None
        # self.newPage = None
        
        # # General ivars.
        # self.chapters = {} # Keys are tab names, values are Chapter objects.
        # self.currentChapter = None
        # self.editorBodies = {} # Keys are panes, values are leoTkinterBodies.
        # self.numberOfEditors = 0
        # self.panedBody = None # The present Tk.PanedWidget.
    
        # self.createNoteBook(parentFrame) # sets self.nb
    #@nonl
    #@-node:ekr.20070317085437.2: ctor: chapterController
    #@+node:ekr.20070318124624.1:finishCreate
    def finishCreate (self,treeTabController):
        
        cc = self
        cc.tt = treeTabController
        cc.createChapter(name='trash')
        cc.createChapter(name='main')
    #@-node:ekr.20070318124624.1:finishCreate
    #@-node:ekr.20070318124624:Birth
    #@+node:ekr.20070317085437.30:Chapter commands
    #@+node:ekr.20070317085437.31:createChapter
    numberOfChapters = 0
    
    def createChapter (self,event=None,name=None):
        
        cc = self ; c = cc.c ; tt = cc.tt
        
        if name == 'main':
            p = c.rootPosition()
        else:
            p = c.currentPosition()
        
        if not name:
            tabName = 'Chapter % d' % self.numberOfChapters
            self.numberOfChapters += 1
        else:
            tabName = name
        
        self.chaptersDict[tabName] = chapter(c=c,chapterController=cc,p=p)
        tt.selectTab(tabName)
        
        if name not in ('trash','main'):
            tt.renameChapterHelper(cc,tabName)
        c.bodyWantsFocusNow()
    #@-node:ekr.20070317085437.31:createChapter
    #@+node:ekr.20070317085437.39:makeNodeIntoChapter (TO BE REMOVED)
    def makeNodeIntoChapter (self,p=None,redraw=True):
        
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
            if not renum: self.renumber()
            c.selectPosition(oldChapter.rp)
        finally:
            c.endUpdate(redraw)
            if redraw: cc.nb.selectpage(pageName)
    #@nonl
    #@-node:ekr.20070317085437.39:makeNodeIntoChapter (TO BE REMOVED)
    #@+node:ekr.20070317085437.40:removeChapter (revise)
    def removeChapter (self,event=None):
    
        cc = self ; c = self.c ; nb = cc.tt.nb
        
        name = nb.getcurselection()
        if name == 'trash':
            return g.es('Can not remove the trash',color='red')
        if name == 'main':
            return g.es('Can not remove the main chapter',color='red')
    
        chapter = self.getSelectedChapter()
        
        # g.trace(name,chapter)
        p = chapter.rp
        tree = chapter.tree
        old_tree = cc.currentChapter.tree
        current = cc.currentChapter.cp
        c.beginUpdate()
        try:
            c.frame.tree = chapter.tree
            newNode = p and (p.visBack() or p.next()) # *not* p.visNext(): we are at the top level.
            if newNode:
                p.doDelete()
                c.selectPosition(newNode)
            c.frame.tree = old_tree
        finally:
            c.endUpdate()
        nb.delete(name)
    
        if tree == old_tree:
            pnames = nb.pagenames()
            nb.selectpage(pnames[0])
            c.selectPosition(c.currentPosition())
            c.redraw()
        else:
            c.selectPosition(current)
        self.renumber()
    #@nonl
    #@-node:ekr.20070317085437.40:removeChapter (revise)
    #@+node:ekr.20070317085437.41:renameChapter
    def renameChapter (self,event=None):
        
        '''Handle the rename chapter command.'''
        
        cc = self ; tt = cc.tt
        
        tabName = tt.getSelectedTabName()
    
        if tabName == 'trash':
            return g.es('Can not rename the trash',color='red')
        if tabName == 'main':
            return g.es('Can not rename the main chapter',color='red')
    
        tt.renameChapterHelper(cc,tabName)
    #@-node:ekr.20070317085437.41:renameChapter
    #@+node:ekr.20070317130250:selectChapter
    def selectChapter (self,event=None,tabName=None):
        
        self.root_p = self.findPositionAnywhere(self.root_v)
        self.p = self.findPositionInTree(self.v)
    #@-node:ekr.20070317130250:selectChapter
    #@-node:ekr.20070317085437.30:Chapter commands
    #@+node:ekr.20070317085437.49:Node commands
    #@+node:ekr.20070317085437.50:cloneToChapter
    def cloneToChapter (self,event=None):
    
        cc = self ; c = cc.c
        chapter = self.getSelectedChapter()
        
        p = c.currentPosition()
        back = p.back()
        if back:
            clone = p.clone(back)
            p2 = chapter.cp
            clone.unlink()
            clone.linkAfter(p2)
            chapter.makeCurrent()
        
            # Warning: c.begin/endUpdate not valid spanning chapter.makeCurrent()
            c.beginUpdate()
            try:
                c.selectPosition(clone)
                c.setChanged(True)
            finally:
                c.endUpdate()
    #@-node:ekr.20070317085437.50:cloneToChapter
    #@+node:ekr.20070317085437.51:copyToChapter
    def copyToChapter (self,event=None):
    
        cc = self ; c = cc.c
        chapter = self.getSelectedChapter()
    
        s = c.fileCommands.putLeoOutline()
        p = c.fileCommands.getLeoOutline(s)
        chapter.setVariables()
        p2 = chapter.cp
        p.moveAfter(p2)
        cc.currentChapter.setVariables()
        chapter.makeCurrent()
    
        # Warning: c.begin/endUpdate not valid spanning chapter.makeCurrent()
        c.beginUpdate()
        try:
            c.selectPosition(p)
            c.setChanged(True)
        finally:
            c.endUpdate()
    #@nonl
    #@-node:ekr.20070317085437.51:copyToChapter
    #@+node:ekr.20070317085437.52:moveToChapter
    def moveToChapter (self,event=None):
        
        cc = self ; c = cc.c
        chapter = cc.getSelectedChapter()
        
        p = c.currentPosition()
        if p.hasParent() or p.hasBack():
            p2 = chapter.cp
            p.unlink()
            p.linkAfter(p2)
            chapter.makeCurrent()
            
            # Warning: c.begin/endUpdate not valid spanning chapter.makeCurrent()
            c.beginUpdate()
            try:
                c.selectPosition(p)
                c.setChanged(True)
            finally:
                c.endUpdate()
    #@nonl
    #@-node:ekr.20070317085437.52:moveToChapter
    #@+node:ekr.20070317085437.29:emptyTrash
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
    #@-node:ekr.20070317085437.29:emptyTrash
    #@-node:ekr.20070317085437.49:Node commands
    #@+node:ekr.20070317130648:Utils
    #@+node:ekr.20070318124004:getChapter
    def getChapter(self,name):
        
        return self.chaptersDict.get(name)
    #@-node:ekr.20070318124004:getChapter
    #@+node:ekr.20070318122708:getSelectedChapter
    def getSelectedChapter (self):
    
        tabName = self.tt.nb.getcurselection()
        return self.chaptersDict.get(tabName)
    #@-node:ekr.20070318122708:getSelectedChapter
    #@+node:ekr.20070317130648.1:findPositionAnywhere
    def findPositionAnywhere (self,v):
        
        '''Return a valid position p such that p.v == v.'''
        
        for p in self.c.allNodes_iter():
            if p.v == v:
                return p
        else:
            return None
    #@nonl
    #@-node:ekr.20070317130648.1:findPositionAnywhere
    #@+node:ekr.20070317131708:findPositionInTree
    def findPositionInTree (self,v):
        
        '''Return a valid position p such that p.v == v.'''
        
        # self.root_p must be valid when this is called.
        assert (self.c.positionExists(self.root_p))
     
        for p in self.root_p.self_and_subtree_iter():
            if p.v == v:
                return p
        else:
            return None
    #@nonl
    #@-node:ekr.20070317131708:findPositionInTree
    #@-node:ekr.20070317130648:Utils
    #@-others
#@nonl
#@-node:ekr.20070317085437:class chapterController
#@+node:ekr.20070317085708:class chapter
class chapter:
    
    '''A class representing the non-gui data of a single chapter.'''
       
    #@    @+others
    #@+node:ekr.20070317085708.1: ctor: chapter
    def __init__ (self,c,chapterController,p):
    
        # Set the ivars.
        self.c = c 
        self.cc = chapterController
        self.p = p.copy() # The current position.
        self.v = p.v # The current vnode.
        self.root_p = p.copy()
        self.root_v = p.v
        
        # self.canvas = canvas
        # self.frame = frame
        # self.pageName = pageName
        # self.page = page # The Pmw.NoteBook page.
        # self.tree = tree
        # self.treeBar = frame.treeBar
        
        # # The name of the page.
        # self.sv = Tk.StringVar()
        # self.sv.set(pageName)
        
        # self.initTree()
        # self.init()
    #@nonl
    #@-node:ekr.20070317085708.1: ctor: chapter
    #@+node:ekr.20070317085708.2:__str__ and __repr__: Chapter
    def __str__ (self):
        
        return '<chapter id: %s p: %s>' % (
            id(self),self.p and self.p.headString() or '<no p>')
        
    __repr__ = __str__
    #@nonl
    #@-node:ekr.20070317085708.2:__str__ and __repr__: Chapter
    #@+node:ekr.20070317131205.1:select (TO DO)
    def select (self):
        
        pass
    #@nonl
    #@-node:ekr.20070317131205.1:select (TO DO)
    #@-others
#@nonl
#@-node:ekr.20070317085708:class chapter
#@-others
#@nonl
#@-node:ekr.20070317085508.1:@thin leoChapters.py
#@-leo
