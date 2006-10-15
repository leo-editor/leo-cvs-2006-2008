#@+leo-ver=4-thin
#@+node:ekr.20031218072017.3749:@thin leoMenu.py
"""Gui-independent menu handling for Leo."""

#@@language python
#@@tabwidth -4
#@@pagewidth 80

import leoGlobals as g
import string
import sys

#@+others
#@+node:ekr.20031218072017.3750:class leoMenu
class leoMenu:
    
    """The base class for all Leo menus."""
    
    __pychecker__ = '--no-argsused' # base classes have many unused args.

    #@    @+others
    #@+node:ekr.20031218072017.3751: leoMenu.__init__
    def __init__ (self,frame):
        
        # g.trace('leoMenu',g.callers())
        
        self.c = c = frame.c
        self.frame = frame
        self.menus = {} # Menu dictionary.
        self.menuShortcuts = {}
        
        # To aid transition to emacs-style key handling.
        self.useCmdMenu = c.config.getBool('useCmdMenu')
        
        self.newBinding = True
            # True if using new binding scheme.
            # You can set this to False in an emergency to revert to the old way.
    
        if 0: # Must be done much later.
            self.defineMenuTables()
    #@-node:ekr.20031218072017.3751: leoMenu.__init__
    #@+node:ekr.20031218072017.3775:oops
    def oops (self):
    
        print "leoMenu oops:", g.callers(), "should be overridden in subclass"
    #@-node:ekr.20031218072017.3775:oops
    #@+node:ekr.20031218072017.3776:Gui-independent menu enablers
    #@+node:ekr.20031218072017.3777:updateAllMenus
    def updateAllMenus (self):
        
        """The Tk "postcommand" callback called when a click happens in any menu.
        
        Updates (enables or disables) all menu items."""
    
        # Allow the user first crack at updating menus.
        c = self.c
        
        if c and c.exists:
            c.setLog()
            p = c.currentPosition()
        
            if not g.doHook("menu2",c=c,p=p,v=p):
                self.updateFileMenu()
                self.updateEditMenu()
                self.updateOutlineMenu()
    #@nonl
    #@-node:ekr.20031218072017.3777:updateAllMenus
    #@+node:ekr.20061010070625:populateHelpMenu(not used)
    def populateHelpMenu (self):
        
        menus  = [self.getMenu(s) for s in ('File','Edit','Outline','Plugins','Cmds','Window')]
        
        try:
            topMenu = self.getMenu('top')
            g.trace(topMenu,g.dictToString(topMenu.__dict__))
            s  = topMenu._w + '.help'
            if 1:
                # Find the menu without any children.
                for key in topMenu.children.keys():
                    menu = topMenu.children.get(key)
                    print key,menu,'#children',len(menu.children)
                    if menu not in menus:
                        g.trace('found',menu)
                        self.setMenu('Help',menu)
                        self.createMenuEntries(menu,self.helpMenuTable)
                        return menu
            return None
            
        except Exception:
            g.trace('Can not get MacOS Help menu')
            g.es_exception()
            return None
    #@-node:ekr.20061010070625:populateHelpMenu(not used)
    #@+node:ekr.20031218072017.3778:updateFileMenu
    def updateFileMenu (self):
        
        c = self.c ; frame = c.frame
        if not c: return
    
        try:
            enable = frame.menu.enableMenu
            menu = frame.menu.getMenu("File")
            enable(menu,"Revert To Saved", c.canRevert())
            enable(menu,"Open With...", g.app.hasOpenWithMenu)
        except:
            g.es("exception updating File menu")
            g.es_exception()
    #@-node:ekr.20031218072017.3778:updateFileMenu
    #@+node:ekr.20031218072017.836:updateEditMenu
    def updateEditMenu (self):
    
        c = self.c ; frame = c.frame ; gui = g.app.gui
        if not c: return
        try:
            # Top level Edit menu...
            enable = frame.menu.enableMenu
            menu = frame.menu.getMenu("Edit")
            c.undoer.enableMenuItems()
            #@        << enable cut/paste >>
            #@+node:ekr.20040130164211:<< enable cut/paste >>
            if frame.body.hasFocus():
                data = frame.body.getSelectedText()
                canCut = data and len(data) > 0
            else:
                # This isn't strictly correct, but we can't get the Tk headline selection.
                canCut = True
            
            enable(menu,"Cut",canCut)
            enable(menu,"Copy",canCut)
            
            data = gui.getTextFromClipboard()
            canPaste = data and len(data) > 0
            enable(menu,"Paste",canPaste)
            #@-node:ekr.20040130164211:<< enable cut/paste >>
            #@nl
            if 0: # Always on for now.
                menu = frame.menu.getMenu("Find...")
                enable(menu,"Find Next",c.canFind())
                flag = c.canReplace()
                enable(menu,"Replace",flag)
                enable(menu,"Replace, Then Find",flag)
            # Edit Body submenu...
            menu = frame.menu.getMenu("Edit Body...")
            enable(menu,"Extract Section",c.canExtractSection())
            enable(menu,"Extract Names",c.canExtractSectionNames())
            enable(menu,"Extract",c.canExtract())
            enable(menu,"Match Brackets",c.canFindMatchingBracket())
        except:
            g.es("exception updating Edit menu")
            g.es_exception()
    #@-node:ekr.20031218072017.836:updateEditMenu
    #@+node:ekr.20031218072017.3779:updateOutlineMenu
    def updateOutlineMenu (self):
    
        c = self.c ; frame = c.frame
        if not c: return
    
        p = c.currentPosition()
        hasParent = p.hasParent()
        hasBack = p.hasBack()
        hasNext = p.hasNext()
        hasChildren = p.hasChildren()
        isExpanded = p.isExpanded()
        isCloned = p.isCloned()
        isMarked = p.isMarked()
    
        try:
            enable = frame.menu.enableMenu
            #@        << enable top level outline menu >>
            #@+node:ekr.20040131171020:<< enable top level outline menu >>
            menu = frame.menu.getMenu("Outline")
            enable(menu,"Cut Node",c.canCutOutline())
            enable(menu,"Delete Node",c.canDeleteHeadline())
            enable(menu,"Paste Node",c.canPasteOutline())
            enable(menu,"Paste Node As Clone",c.canPasteOutline())
            enable(menu,"Clone Node",c.canClone()) # 1/31/04
            enable(menu,"Sort Siblings",c.canSortSiblings())
            enable(menu,"Hoist",c.canHoist())
            enable(menu,"De-Hoist",c.canDehoist())
            #@-node:ekr.20040131171020:<< enable top level outline menu >>
            #@nl
            #@        << enable expand/contract submenu >>
            #@+node:ekr.20040131171020.1:<< enable expand/Contract submenu >>
            menu = frame.menu.getMenu("Expand/Contract...")
            enable(menu,"Contract Parent",c.canContractParent())
            enable(menu,"Contract Node",hasChildren and isExpanded)
            enable(menu,"Contract Or Go Left",(hasChildren and isExpanded) or hasParent)
            enable(menu,"Expand Node",hasChildren and not isExpanded)
            enable(menu,"Expand Prev Level",hasChildren and isExpanded)
            enable(menu,"Expand Next Level",hasChildren)
            enable(menu,"Expand To Level 1",hasChildren and isExpanded)
            enable(menu,"Expand Or Go Right",hasChildren)
            for i in xrange(2,9):
                frame.menu.enableMenu(menu,"Expand To Level " + str(i), hasChildren)
            #@-node:ekr.20040131171020.1:<< enable expand/Contract submenu >>
            #@nl
            #@        << enable move submenu >>
            #@+node:ekr.20040131171020.2:<< enable move submenu >>
            menu = frame.menu.getMenu("Move...")
            enable(menu,"Move Down",c.canMoveOutlineDown())
            enable(menu,"Move Left",c.canMoveOutlineLeft())
            enable(menu,"Move Right",c.canMoveOutlineRight())
            enable(menu,"Move Up",c.canMoveOutlineUp())
            enable(menu,"Promote",c.canPromote())
            enable(menu,"Demote",c.canDemote())
            #@-node:ekr.20040131171020.2:<< enable move submenu >>
            #@nl
            #@        << enable go to submenu >>
            #@+node:ekr.20040131171020.3:<< enable go to submenu >>
            menu = frame.menu.getMenu("Go To...")
            enable(menu,"Go Prev Visited",c.beadPointer > 1)
            enable(menu,"Go Next Visited",c.beadPointer + 1 < len(c.beadList))
            enable(menu,"Go To Prev Visible",c.canSelectVisBack())
            enable(menu,"Go To Next Visible",c.canSelectVisNext())
            if 0: # These are too slow.
                enable(menu,"Go To Next Marked",c.canGoToNextMarkedHeadline())
                enable(menu,"Go To Next Changed",c.canGoToNextDirtyHeadline())
            enable(menu,"Go To Next Clone",isCloned)
            enable(menu,"Go To Prev Node",c.canSelectThreadBack())
            enable(menu,"Go To Next Node",c.canSelectThreadNext())
            enable(menu,"Go To Parent",hasParent)
            enable(menu,"Go To Prev Sibling",hasBack)
            enable(menu,"Go To Next Sibling",hasNext)
            #@-node:ekr.20040131171020.3:<< enable go to submenu >>
            #@nl
            #@        << enable mark submenu >>
            #@+node:ekr.20040131171020.4:<< enable mark submenu >>
            menu = frame.menu.getMenu("Mark/Unmark...")
            label = g.choose(isMarked,"Unmark","Mark")
            frame.menu.setMenuLabel(menu,0,label)
            enable(menu,"Mark Subheads",hasChildren)
            if 0: # These are too slow.
                enable(menu,"Mark Changed Items",c.canMarkChangedHeadlines())
                enable(menu,"Mark Changed Roots",c.canMarkChangedRoots())
            enable(menu,"Mark Clones",isCloned)
            #@-node:ekr.20040131171020.4:<< enable mark submenu >>
            #@nl
        except:
            g.es("exception updating Outline menu")
            g.es_exception()
    #@-node:ekr.20031218072017.3779:updateOutlineMenu
    #@+node:ekr.20031218072017.3780:hasSelection
    # Returns True if text in the outline or body text is selected.
    
    def hasSelection (self):
        
        body = self.frame.body
    
        if body:
            first, last = body.getTextSelection()
            return first != last
        else:
            return False
    #@-node:ekr.20031218072017.3780:hasSelection
    #@-node:ekr.20031218072017.3776:Gui-independent menu enablers
    #@+node:ekr.20031218072017.3781:Gui-independent menu routines
    #@+node:ekr.20060926213642:capitalizeMinibufferMenuName
    def capitalizeMinibufferMenuName (self,s):
        
        result = []
        for i in xrange(len(s)):
            ch = s[i]
            prev = i > 0 and s[i-1] or ''
            prevprev = i > 1 and s[i-2] or ''
            if 1: # Just capitalize the start of each word.
                if (
                    i == 0 or
                    i == 1 and prev == '&' or
                    prev == '-' or
                    prev == '&' and prevprev == '-'
                ):
                    result.append(ch.capitalize())
                else:
                    result.append(ch)
            else: # Capitalizing accelerators in the middle of a word is dubious.
                next = i+1 < len(s) and s[i+1] or ''
                if (
                    i == 0 and next != '&' or
                    prev == '&' or
                    prev == '-' and next != '&'
                ):
                    result.append(ch.capitalize())
                else:
                    result.append(ch)
        return ''.join(result)
            
        
    #@nonl
    #@-node:ekr.20060926213642:capitalizeMinibufferMenuName
    #@+node:ekr.20031218072017.3785:createMenusFromTables & helpers
    def createMenusFromTables (self):
        
        c = self.c
        
        self.defineMenuTables()
        
        self.createFileMenuFromTable()
        self.createEditMenuFromTable()
        self.createOutlineMenuFromTable()
        
        g.doHook("create-optional-menus",c=c)
        
        if self.useCmdMenu:
            self.createCmndsMenuFromTable()
    
        self.createWindowMenuFromTable()
        self.createHelpMenuFromTable()
    #@+node:ekr.20031218072017.3790:createFileMenuFromTable
    def createFileMenuFromTable (self):
        
        c = self.c
        fileMenu = self.createNewMenu("&File")
        self.createMenuEntries(fileMenu,self.fileMenuTopTable)
        self.createNewMenu("Open &With...","File")
        self.createMenuEntries(fileMenu,self.fileMenuTop2Table)
        #@    << create the recent files submenu >>
        #@+node:ekr.20031218072017.3791:<< create the recent files submenu >>
        self.createNewMenu("Recent &Files...","File")
        c.recentFiles = c.config.getRecentFiles()
        
        if 0: # Not needed, and causes problems in wxWindows...
            self.createRecentFilesMenuItems()
        #@-node:ekr.20031218072017.3791:<< create the recent files submenu >>
        #@nl
        self.add_separator(fileMenu)
        #@    << create the read/write submenu >>
        #@+node:ekr.20031218072017.3792:<< create the read/write submenu >>
        readWriteMenu = self.createNewMenu("&Read/Write...","File")
        
        self.createMenuEntries(readWriteMenu,self.fileMenuReadWriteMenuTable)
        #@-node:ekr.20031218072017.3792:<< create the read/write submenu >>
        #@nl
        #@    << create the tangle submenu >>
        #@+node:ekr.20031218072017.3793:<< create the tangle submenu >>
        tangleMenu = self.createNewMenu("&Tangle...","File")
        
        self.createMenuEntries(tangleMenu,self.fileMenuTangleMenuTable)
        #@-node:ekr.20031218072017.3793:<< create the tangle submenu >>
        #@nl
        #@    << create the untangle submenu >>
        #@+node:ekr.20031218072017.3794:<< create the untangle submenu >>
        untangleMenu = self.createNewMenu("&Untangle...","File")
        
        self.createMenuEntries(untangleMenu,self.fileMenuUntangleMenuTable)
        #@-node:ekr.20031218072017.3794:<< create the untangle submenu >>
        #@nl
        #@    << create the import submenu >>
        #@+node:ekr.20031218072017.3795:<< create the import submenu >>
        importMenu = self.createNewMenu("&Import...","File")
        
        self.createMenuEntries(importMenu,self.fileMenuImportMenuTable)
        #@-node:ekr.20031218072017.3795:<< create the import submenu >>
        #@nl
        #@    << create the export submenu >>
        #@+node:ekr.20031218072017.3796:<< create the export submenu >>
        exportMenu = self.createNewMenu("&Export...","File")
        
        self.createMenuEntries(exportMenu,self.fileMenuExportMenuTable)
        #@-node:ekr.20031218072017.3796:<< create the export submenu >>
        #@nl
        self.add_separator(fileMenu)
        self.createMenuEntries(fileMenu,self.fileMenuTop3MenuTable)
    #@-node:ekr.20031218072017.3790:createFileMenuFromTable
    #@+node:ekr.20031218072017.3786:createEditMenuFromTable
    def createEditMenuFromTable (self):
    
        editMenu = self.createNewMenu("&Edit")
        self.createMenuEntries(editMenu,self.editMenuTopTable)
    
        #@    << create the edit body submenu >>
        #@+node:ekr.20031218072017.3787:<< create the edit body submenu >>
        editBodyMenu = self.createNewMenu("Edit &Body...","Edit")
        
        self.createMenuEntries(editBodyMenu,self.editMenuEditBodyTable)
        #@-node:ekr.20031218072017.3787:<< create the edit body submenu >>
        #@nl
        #@    << create the edit headline submenu >>
        #@+node:ekr.20031218072017.3788:<< create the edit headline submenu >>
        editHeadlineMenu = self.createNewMenu("Edit &Headline...","Edit")
        
        self.createMenuEntries(editHeadlineMenu,self.editMenuEditHeadlineTable)
        #@-node:ekr.20031218072017.3788:<< create the edit headline submenu >>
        #@nl
        #@    << create the find submenu >>
        #@+node:ekr.20031218072017.3789:<< create the find submenu >>
        findMenu = self.createNewMenu("&Find...","Edit")
        
        self.createMenuEntries(findMenu,self.editMenuFindMenuTable)
        #@-node:ekr.20031218072017.3789:<< create the find submenu >>
        #@nl
        
        self.createMenuEntries(editMenu,self.editMenuTop2Table)
    #@-node:ekr.20031218072017.3786:createEditMenuFromTable
    #@+node:ekr.20031218072017.3797:createOutlineMenuFromTable
    def createOutlineMenuFromTable (self):
    
        outlineMenu = self.createNewMenu("&Outline")
        
        self.createMenuEntries(outlineMenu,self.outlineMenuTopMenuTable)
        
        #@    << create check submenu >>
        #@+node:ekr.20040711140738.1:<< create check submenu >>
        checkOutlineMenu = self.createNewMenu("Chec&k...","Outline")
        
        self.createMenuEntries(checkOutlineMenu,self.outlineMenuCheckOutlineMenuTable)
        #@-node:ekr.20040711140738.1:<< create check submenu >>
        #@nl
        #@    << create expand/contract submenu >>
        #@+node:ekr.20031218072017.3798:<< create expand/contract submenu >>
        expandMenu = self.createNewMenu("E&xpand/Contract...","Outline")
        
        self.createMenuEntries(expandMenu,self.outlineMenuExpandContractMenuTable)
        #@-node:ekr.20031218072017.3798:<< create expand/contract submenu >>
        #@nl
        #@    << create move submenu >>
        #@+node:ekr.20031218072017.3799:<< create move submenu >>
        moveSelectMenu = self.createNewMenu("&Move...","Outline")
        
        self.createMenuEntries(moveSelectMenu,self.outlineMenuMoveMenuTable)
        #@-node:ekr.20031218072017.3799:<< create move submenu >>
        #@nl
        #@    << create mark submenu >>
        #@+node:ekr.20031218072017.3800:<< create mark submenu >>
        markMenu = self.createNewMenu("M&ark/Unmark...","Outline")
        
        self.createMenuEntries(markMenu,self.outlineMenuMarkMenuTable)
        #@-node:ekr.20031218072017.3800:<< create mark submenu >>
        #@nl
        #@    << create goto submenu >>
        #@+node:ekr.20031218072017.3801:<< create goto submenu >>
        gotoMenu = self.createNewMenu("&Go To...","Outline")
        
        self.createMenuEntries(gotoMenu,self.outlineMenuGoToMenuTable)
        #@-node:ekr.20031218072017.3801:<< create goto submenu >>
        #@nl
    #@-node:ekr.20031218072017.3797:createOutlineMenuFromTable
    #@+node:ekr.20050921103736:createCmndsMenuFromTable
    def createCmndsMenuFromTable (self):
        
        cmdsMenu = self.createNewMenu('&Cmds')
        
        if 0: # Now in the minibuffer table.
            # Used in top table: q,u,x
            self.createMenuEntries(cmdsMenu,self.cmdsMenuTopTable)
    
        for name,table in (
            # &: a,b,c,d,f,g,h,i,m,n,o,p,r,s,t
            ('&Abbrev...',          self.cmdsMenuAbbrevTable),
            ('Body E&ditors',       self.cmdsMenuBodyEditorsTable),
            ('&Buffers...',         self.cmdsMenuBuffersTable),
            ('&Cursor/Selection...',[]),
            ('&Focus...',           self.cmdsMenuFocusTable),
            ('&Macro...',           self.cmdsMenuMacroTable),
            ('M&inibuffer',         self.cmdsMenuMinibufferTable),
            ('&Panes...',           self.cmdsMenuPanesTable),
            ('Pic&kers...',         self.cmdsMenuPickersTable),
            ('&Rectangles...',      self.cmdsMenuRectanglesTable),
            ('Re&gisters...',       self.cmdsMenuRegistersTable),
            ('Scr&olling...',       self.cmdsMenuScrollTable),
            ('Spell C&heck...',     self.cmdsMenuSpellCheckTable),
            ('&Text Commands',      self.cmdsMenuTextTable),
            ('Toggle Setti&ngs',     self.cmdsMenuToggleTable),
        ):
            menu = self.createNewMenu(name,'&Cmds')
            self.createMenuEntries(menu,table)
    
        for name,table in (
            # &: b,e,f,s,t,x
            ('Cursor &Back...',                     self.cursorMenuBackTable),
            ('Cursor Back &Extend Selection...',    self.cursorMeuuBackExtendTable),
            ('Cursor Extend &To...',                self.cursorMenuExtendTable),
            ('Cursor &Forward...',                  self.cursorMenuForwardTable),
            ('Cursor Forward E&xtend Selection...', self.cursorMenuForwardExtendTable),
        ):
            menu = self.createNewMenu(name,'C&ursor/Selection...')
            self.createMenuEntries(menu,table)
    #@nonl
    #@-node:ekr.20050921103736:createCmndsMenuFromTable
    #@+node:ekr.20031218072017.3802:createWindowMenuFromTable
    def createWindowMenuFromTable (self):
    
        windowMenu = self.createNewMenu("&Window")
        
        self.createMenuEntries(windowMenu,self.windowMenuTopTable)
    #@-node:ekr.20031218072017.3802:createWindowMenuFromTable
    #@+node:ekr.20031218072017.3803:createHelpMenuFromTable
    def createHelpMenuFromTable (self):
        
        g.trace(sys.platform)
    
        if sys.platform == 'darwin':
            self.getMacHelpMenu()
        else:
            helpMenu = self.createNewMenu("&Help")
            self.createMenuEntries(helpMenu,self.helpMenuTable)
    #@nonl
    #@-node:ekr.20031218072017.3803:createHelpMenuFromTable
    #@-node:ekr.20031218072017.3785:createMenusFromTables & helpers
    #@+node:ekr.20031218072017.3752:defineMenuTables & helpers
    def defineMenuTables (self):
        
        c = self.c
        
        self.defineEditMenuTables()
        self.defineFileMenuTables()
        self.defineOutlineMenuTables()
        self.defineWindowMenuTables()
    
        if self.useCmdMenu:
            self.defineCmdsMenuTables()
    
        self.defineHelpMenuTables()
    
    #@+node:ekr.20031218072017.3753:defineEditMenuTables & helpers
    def defineEditMenuTables (self):
    
        self.defineEditMenuTopTable()
        self.defineEditMenuEditCursorTable()
        self.defineEditMenuEditBodyTable()
        self.defineEditMenuEditHeadlineTable()
        self.defineEditMenuFindMenuTable()
        self.defineEditMenuTop2Table()
    #@+node:ekr.20031218072017.839:defineEditMenuTopTable
    def defineEditMenuTopTable (self):
        
        __pychecker__ = 'no-unusednames=[f]' # We define 'f' just in case.
    
        c = self.c ; f = self.frame
        
        self.editMenuTopTable = [
            ("Can't Undo",c.undoer.undo), # &U reserved for Undo
            ("Can't Redo",c.undoer.redo), # &R reserved for Redo
            ("-",None),
            ("Cu&t",f.OnCutFromMenu), 
            ("Cop&y",f.OnCopyFromMenu),
            ("&Paste",f.OnPasteFromMenu),
            ("&Delete",c.editCommands.backwardDeleteCharacter),
            ("Select &All",f.body.selectAllText),
            ("-",None),
        ]
    
        # Top-level shortcuts here:  a,d,p,t,u,y,z
        # Top-level shortcuts later: e,g,n,v
    #@-node:ekr.20031218072017.839:defineEditMenuTopTable
    #@+node:ekr.20050711091931:defineEditMenuEditCursorTable (not ready yet)
    def defineEditMenuEditCursorTable (self):
        
        __pychecker__ = 'no-unusednames=c,f'
        
        c = self.c ; f = self.frame
    
        if 0: ### Not ready yet.
            # These should have Emacs names...
            self.editMenuEditCursorTable = [
                ('Delete Right',c.deleteRightChar), 
                ('Delete Left',c.deleteLeftChar), 
                # Moving the cursor.
                ('Start of Line',c.moveToStartOfLine), 
                ('End of Line',c.moveToEndOfLine), 
                ('Start of Node',c.moveToStartOfNode),
                ('End of Node',c.moveToEndOfNode), 
                ('-',None,None),
                # Extending the selection...
                ('Select Line',c.selectEntireLine),
                ('Extend To Start of Word',c.extendToStartOfWord),
                ('Extend To End of Word',c.extendToEndOfWord),
                ('Extend To Start Of Line',c.extendToStartOfLine), 
                ('Extend To End Of Line',c.extendToEndOfLine), 
                ('Extend To End of Node',c.extendToEndOfNode),
                # The mark...
            ]
    #@-node:ekr.20050711091931:defineEditMenuEditCursorTable (not ready yet)
    #@+node:ekr.20031218072017.3754:defineEditMenuEditBodyTable
    def defineEditMenuEditBodyTable (self):
        
        __pychecker__ = 'no-unusednames=c,f'
        
        c = self.c ; f = self.frame
    
        self.editMenuEditBodyTable = [
            ("Extract &Section",c.extractSection),
            ("Extract &Names",c.extractSectionNames),
            ("&Extract",c.extract),
            ("-",None,None),
            ("Convert All B&lanks",c.convertAllBlanks),
            ("Convert All T&abs",c.convertAllTabs),
            ("Convert &Blanks",c.convertBlanks),
            ("Convert &Tabs",c.convertTabs),
            ("Insert Body Time/&Date",c.insertBodyTime),
            ("&Reformat Paragraph",c.reformatParagraph),
            ("-",None,None),
            ("&Indent",c.indentBody),
            ("&Unindent",c.dedentBody),
            ("&Match Brackets",c.findMatchingBracket),
            ("Add Comments",c.addComments),
            ("Delete Comments",c.deleteComments),
        ]
        # Shortcuts a,b,d,e,i,l,m,n,r,s,t,u
    #@-node:ekr.20031218072017.3754:defineEditMenuEditBodyTable
    #@+node:ekr.20031218072017.3755:defineEditMenuEditHeadlineTable
    def defineEditMenuEditHeadlineTable (self):
        
        __pychecker__ = 'no-unusednames=c,f'
        
        c = self.c ; f = self.frame
        
        self.editMenuEditHeadlineTable = [
            ("Edit &Headline",c.editHeadline),
            ("&End Edit Headline",f.endEditLabelCommand),
            ("&Abort Edit Headline",f.abortEditLabelCommand),
            ("Insert Headline Time/&Date",f.insertHeadlineTime),
            ("Toggle Angle Brackets",c.toggleAngleBrackets),
        ]
    #@-node:ekr.20031218072017.3755:defineEditMenuEditHeadlineTable
    #@+node:ekr.20031218072017.3756:defineEditMenuFindMenuTable
    def defineEditMenuFindMenuTable (self):
        
        self.editMenuFindMenuTable = [
            # &: a,b,c,d,e,f,h,i,l,n,o,p,q,r,s,u,w,x
            '&open-find-tab',
            '&hide-find-tab',
            'search-&with-present-options',
            '-',
            'find-tab-find-&next',
            'find-tab-find-&prev',
            'find-tab-&change',
            'find-tab-find-&all',
            'clone-fi&nd-all',
            'find-tab-change-a&ll',
            '-',
            '&find-character',
            'find-character-extend-&selection',
            '&backward-find-character',
            'backward-find-character-&extend-selection',
            '-',
            '&isearch-forward',
            'isea&rch-backward',
            'isearch-forward-rege&xp',
            'isearch-backward-regex&p',
            '-',
            '&query-replace',
            'q&uery-replace-regex',
        ]
    
    # find-character-reverse            = Alt-P
    # isearch-with-present-options      = None
    #@nonl
    #@-node:ekr.20031218072017.3756:defineEditMenuFindMenuTable
    #@+node:ekr.20031218072017.3757:defineEditMenuTop2Table
    def defineEditMenuTop2Table (self):
        
        __pychecker__ = 'no-unusednames=c,f'
    
        c = self.c ; f = self.frame
    
        try:        show = c.frame.body.getColorizer().showInvisibles
        except:     show = False
        label = g.choose(show,"Hide In&visibles","Show In&visibles")
            
        self.editMenuTop2Table = [
            ("&Go To Line Number",c.goToLineNumber),
            ("&Execute Script",c.executeScript),
            (label,c.toggleShowInvisibles),
            ("Setti&ngs",c.preferences),
        ]
    
        # Top-level shortcuts earlier: a,d,p,t,u,y,z
        # Top-level shortcuts here: e,g,n,v
    #@-node:ekr.20031218072017.3757:defineEditMenuTop2Table
    #@-node:ekr.20031218072017.3753:defineEditMenuTables & helpers
    #@+node:ekr.20031218072017.3758:defineFileMenuTables & helpers
    def defineFileMenuTables (self):
    
        self.defineFileMenuTopTable()
        self.defineFileMenuTop2Table()
        self.defineFileMenuReadWriteMenuTable()
        self.defineFileMenuTangleMenuTable()
        self.defineFileMenuUntangleMenuTable()
        self.defineFileMenuImportMenuTable()
        self.defineFileMenuExportMenuTable()
        self.defineFileMenuTop3MenuTable()
    #@+node:ekr.20031218072017.3759:defineFileMenuTopTable
    def defineFileMenuTopTable (self):
        
        __pychecker__ = 'no-unusednames=c,f'
        
        c = self.c ; f = self.frame
    
        self.fileMenuTopTable = [
            ("&New",c.new),
            ("&Open...",c.open),
        ]
    #@-node:ekr.20031218072017.3759:defineFileMenuTopTable
    #@+node:ekr.20031218072017.3760:defineFileMenuTop2Table
    def defineFileMenuTop2Table (self):
        
        __pychecker__ = 'no-unusednames=c,f'
        
        c = self.c ; f = self.frame
    
        self.fileMenuTop2Table = [
            ("-",None),
            ("&Close",c.close),
            ("&Save",c.save),
            ("Save &As",c.saveAs),
            ("Save &To",c.saveTo), # &Tangle
            ("Re&vert To Saved",c.revert), # &Read/Write
        ]
    #@-node:ekr.20031218072017.3760:defineFileMenuTop2Table
    #@+node:ekr.20031218072017.3761:defineFileMenuReadWriteMenuTable
    def defineFileMenuReadWriteMenuTable (self):
        
        __pychecker__ = 'no-unusednames=c,f'
        
        c = self.c ; f = self.frame ; fc = c.fileCommands
    
        self.fileMenuReadWriteMenuTable = [
            ("&Read Outline Only",c.readOutlineOnly),
            ("Read @file &Nodes",c.readAtFileNodes),
            ("Write &Dirty @file Nodes",fc.writeDirtyAtFileNodes),
            ("Write &Missing @file Nodes",fc.writeMissingAtFileNodes),
            ("Write &Outline Only",fc.writeOutlineOnly),
            ("&Write @file Nodes",fc.writeAtFileNodes),
        ]
    #@-node:ekr.20031218072017.3761:defineFileMenuReadWriteMenuTable
    #@+node:ekr.20031218072017.3762:defineFileMenuTangleMenuTable
    def defineFileMenuTangleMenuTable (self):
        
        __pychecker__ = 'no-unusednames=c,f'
        
        c = self.c ; f = self.frame
    
        self.fileMenuTangleMenuTable = [
            ("Tangle &All",c.tangleAll),
            ("Tangle &Marked",c.tangleMarked),
            ("&Tangle",c.tangle),
        ]
    #@-node:ekr.20031218072017.3762:defineFileMenuTangleMenuTable
    #@+node:ekr.20031218072017.3763:defineFileMenuUntangleMenuTable
    def defineFileMenuUntangleMenuTable (self):
        
        __pychecker__ = 'no-unusednames=c,f'
        
        c = self.c ; f = self.frame
    
        self.fileMenuUntangleMenuTable = [
            ("Untangle &All",c.untangleAll),
            ("Untangle &Marked",c.untangleMarked),
            ("&Untangle",c.untangle),
        ]
    #@-node:ekr.20031218072017.3763:defineFileMenuUntangleMenuTable
    #@+node:ekr.20031218072017.3764:defineFileMenuImportMenuTable
    def defineFileMenuImportMenuTable (self):
        
        __pychecker__ = 'no-unusednames=c,f'
        
        c = self.c ; f = self.frame
    
        self.fileMenuImportMenuTable = [
            ("Import Derived File",c.importDerivedFile),
            ("Import To @&file",c.importAtFile),
            ("Import To @&root",c.importAtRoot),
            ("Import &CWEB Files",c.importCWEBFiles),
            ("Import &noweb Files",c.importNowebFiles),
            ("Import Flattened &Outline",c.importFlattenedOutline),
        ]
    #@-node:ekr.20031218072017.3764:defineFileMenuImportMenuTable
    #@+node:ekr.20031218072017.3765:defineFileMenuExportMenuTable
    def defineFileMenuExportMenuTable (self):
        
        __pychecker__ = 'no-unusednames=c,f'
        
        c = self.c ; f = self.frame
    
        self.fileMenuExportMenuTable = [
            ("Export &Headlines",c.exportHeadlines),
            ("Outline To &CWEB",c.outlineToCWEB),
            ("Outline To &Noweb",c.outlineToNoweb),
            ("&Flatten Outline",c.flattenOutline),
            ("&Remove Sentinels",c.removeSentinels),
            ("&Weave",c.weave),
        ]
    #@-node:ekr.20031218072017.3765:defineFileMenuExportMenuTable
    #@+node:ekr.20031218072017.3766:defineFileMenuTop3MenuTable
    def defineFileMenuTop3MenuTable (self):
        
        __pychecker__ = 'no-unusednames=c,f'
        
        c = self.c ; f = self.frame
    
        self.fileMenuTop3MenuTable = [
            ("E&xit",g.app.onQuit),
        ]
    #@-node:ekr.20031218072017.3766:defineFileMenuTop3MenuTable
    #@-node:ekr.20031218072017.3758:defineFileMenuTables & helpers
    #@+node:ekr.20031218072017.3767:defineOutlineMenuTables & helpers
    def defineOutlineMenuTables (self):
    
        self.defineOutlineMenuTopMenuTable()
        self.defineOutlineMenuCheckOutlineMenuTable()
        self.defineOutlineMenuExpandContractMenuTable()
        self.defineOutlineMenuMoveMenuTable()
        self.defineOutlineMenuMarkMenuTable()
        self.defineOutlineMenuGoToMenuTable()
    #@+node:ekr.20031218072017.3768:defineOutlineMenuTopMenuTable
    def defineOutlineMenuTopMenuTable (self):
        
        __pychecker__ = 'no-unusednames=c,f'
        
        c = self.c ; f = self.frame
    
        self.outlineMenuTopMenuTable = [
            ("C&ut Node",c.cutOutline),
            ("C&opy Node",c.copyOutline),
            ("&Paste Node",c.pasteOutline),
            ("Pas&te Node As Clone",c.pasteOutlineRetainingClones),
            ("&Delete Node",c.deleteOutline),
            ("-",None,None),
            ("&Insert Node",c.insertHeadline),
            ("&Clone Node",c.clone),
            ("Sort Childre&n",c.sortChildren), # Conflicted with Hoist.
            ("&Sort Siblings",c.sortSiblings),
            ("-",None),
            ("&Hoist",c.hoist),
            ("D&e-Hoist",f.c.dehoist),
            ("-",None),
        ]
        # Ampersand bindings:  a,b,c,d,e,h,i,n,o,p,t,s,y
        # Bindings for entries that go to submenus: a,g,k,m,x
    #@-node:ekr.20031218072017.3768:defineOutlineMenuTopMenuTable
    #@+node:ekr.20040711140738:defineOutlineMenuCheckOutlineMenuTable
    def defineOutlineMenuCheckOutlineMenuTable (self):
        
        __pychecker__ = 'no-unusednames=c,f'
        
        c = self.c ; f = self.frame
    
        self.outlineMenuCheckOutlineMenuTable = [
            ("Check &Outline",c.checkOutline),
            ("&Dump Outline",c.dumpOutline),
            ("-",None),
            ("Check &All Python Code",c.checkAllPythonCode),
            ("&Check Python &Code",c.checkPythonCode),
        ]
        # shortcuts used: a,c,d,o,p,r
    #@-node:ekr.20040711140738:defineOutlineMenuCheckOutlineMenuTable
    #@+node:ekr.20031218072017.3769:defineOutlineMenuExpandContractMenuTable
    def defineOutlineMenuExpandContractMenuTable (self):
        
        __pychecker__ = 'no-unusednames=c,f'
        
        c = self.c ; f = self.frame
    
        self.outlineMenuExpandContractMenuTable = [
            ("&Contract All",c.contractAllHeadlines),
            ("Contract &Node",c.contractNode),
            ("Contract &Parent",c.contractParent),
            ("Contract Or Go Left",c.contractNodeOrGoToParent),
            ("-",None),
            ("Expand P&rev Level",c.expandPrevLevel),
            ("Expand N&ext Level",c.expandNextLevel),
            ("Expand And Go Right",c.expandNodeAndGoToFirstChild),
            ("Expand Or Go Right",c.expandNodeOrGoToFirstChild),
            ("-",None),
            ("Expand To Level &1",c.expandLevel1),
            ("Expand To Level &2",c.expandLevel2),
            ("Expand To Level &3",c.expandLevel3),
            ("Expand To Level &4",c.expandLevel4),
            ("Expand To Level &5",c.expandLevel5),
            ("Expand To Level &6",c.expandLevel6),
            ("Expand To Level &7",c.expandLevel7),
            ("Expand To Level &8",c.expandLevel8),
            ("-",None),
            ("Expand &All",c.expandAllHeadlines),
            ("Expand N&ode",c.expandNode),
        ]
    #@-node:ekr.20031218072017.3769:defineOutlineMenuExpandContractMenuTable
    #@+node:ekr.20031218072017.3770:defineOutlineMenuMoveMenuTable
    def defineOutlineMenuMoveMenuTable (self):
        
        __pychecker__ = 'no-unusednames=c,f'
        
        c = self.c ; f = self.frame
    
        self.outlineMenuMoveMenuTable = [
            ("Move &Down",c.moveOutlineDown),
            ("Move &Left",c.moveOutlineLeft),
            ("Move &Right",c.moveOutlineRight),
            ("Move &Up",c.moveOutlineUp),
            ("-",None),
            ("&Promote",c.promote),
            ("&Demote",c.demote),
        ]
    #@-node:ekr.20031218072017.3770:defineOutlineMenuMoveMenuTable
    #@+node:ekr.20031218072017.3771:defineOutlineMenuMarkMenuTable
    def defineOutlineMenuMarkMenuTable (self):
        
        __pychecker__ = 'no-unusednames=c,f'
        
        c = self.c ; f = self.frame
    
        self.outlineMenuMarkMenuTable = [
            ("&Mark",c.markHeadline),
            ("Mark &Subheads",c.markSubheads),
            ("Mark Changed &Items",c.markChangedHeadlines),
            ("Mark Changed &Roots",c.markChangedRoots),
            ("Mark &Clones",c.markClones),
            ("&Unmark All",c.unmarkAll),
        ]
    #@-node:ekr.20031218072017.3771:defineOutlineMenuMarkMenuTable
    #@+node:ekr.20031218072017.3772:defineOutlineMenuGoToMenuTable
    def defineOutlineMenuGoToMenuTable (self):
        
        __pychecker__ = 'no-unusednames=c,f'
        
        c = self.c ; f = self.frame
    
        self.outlineMenuGoToMenuTable = [
            ("Go Prev Visited",c.goPrevVisitedNode), # Usually use buttons for this.
            ("Go Next Visited",c.goNextVisitedNode),
            ("Go To Prev Node",c.selectThreadBack),
            ("Go To Next Node",c.selectThreadNext),
            ("-",None),
            ("Go To Next Marked",c.goToNextMarkedHeadline),
            ("Go To Next Changed",c.goToNextDirtyHeadline),
            ("Go To Next Clone",c.goToNextClone),
            ("-",None),
            ("Go To First Node",c.goToFirstNode),
            ("Go To Prev Visible",c.selectVisBack),
            ("Go To Next Visible",c.selectVisNext),
            ("Go To Last Node",c.goToLastNode),
            ('Go To Last Visible',c.goToLastVisibleNode),
            ("-",None),
            ("Go To Parent",c.goToParent),
            ('Go To First Sibling',c.goToFirstSibling),
            ('Go To Last Sibling',c.goToLastSibling),
            ("Go To Prev Sibling",c.goToPrevSibling),
            ("Go To Next Sibling",c.goToNextSibling),
        ]
    #@-node:ekr.20031218072017.3772:defineOutlineMenuGoToMenuTable
    #@-node:ekr.20031218072017.3767:defineOutlineMenuTables & helpers
    #@+node:ekr.20050921103230:defineCmdsMenuTables & helpers
    def defineCmdsMenuTables (self):
        
        if 0: # Replaced by minibuffer submenu.
            self.defineCmdsMenuTopTable()
    
        self.defineCmdsMenuAbbrevTable()
        self.defineCmdsMenuBodyEditorsTable()
        self.defineCmdsMenuBuffersTable()
        self.defineCmdsMenuCursorTable()
        self.defineCmdsMenuFocusTable()
        self.defineCmdsMenuMacroTable()
        self.defineCmdsMenuMinibufferTable()
        self.defineCmdsMenuPanesTable()
        self.defineCmdsMenuPickersTable()
        self.defineCmdsMenuRectanglesTable()
        self.defineCmdsMenuRegistersTable()
        self.defineCmdsMenuScrollTable()
        self.defineCmdsMenuSpellCheckTable()
        self.defineCmdsMenuTextTable()
        self.defineCmdsMenuToggleTable()
    #@nonl
    #@+node:ekr.20060117094955.1:defineCmdsMenuAbbrevTable
    def defineCmdsMenuAbbrevTable (self):
        
        self.cmdsMenuAbbrevTable = [
            # &: a,e,i,k,l,r,w,v
            'abbre&v-mode',
            '-',
            '&list-abbrevs',
            '&read-abbrev-file',
            '&write-abbrev-file',
            '-',
            '&add-global-abbrev',
            '&inverse-add-global-abbrev',
            '&kill-all-abbrevs',
            '-',
            # 'expand-abbrev', # Not a command
            '&expand-region-abbrevs',
        ]
    #@-node:ekr.20060117094955.1:defineCmdsMenuAbbrevTable
    #@+node:ekr.20060912093104:defineCmdsMenuBodyEditorsTable
    def defineCmdsMenuBodyEditorsTable (self):
    
        self.cmdsMenuBodyEditorsTable = [
            # &: a,c,d
            '&add-editor',
            '&cycle-editor-focus',
            '&delete-editor',
        ]
    #@nonl
    #@-node:ekr.20060912093104:defineCmdsMenuBodyEditorsTable
    #@+node:ekr.20060117095212:defineCmdsMenuBufferTable
    def defineCmdsMenuBuffersTable (self):
    
        self.cmdsMenuBuffersTable = [
            '&append-to-buffer',
            '&kill-buffer',
            'list-&buffers',
            '&list-buffers-alphabetically',
            '&prepend-to-buffer',
            '&rename-buffer',
            '&switch-to-buffer',
        ]
    #@-node:ekr.20060117095212:defineCmdsMenuBufferTable
    #@+node:ekr.20060924124119:defineCmdsMenuCursorTable
    def defineCmdsMenuCursorTable (self):
    
        self.cursorMenuBackTable = [
            # &: b,c,l,p,s,v,w
            'back-&char',
            'back-&paragraph',
            'back-&sentence',
            'back-&word',
            '-',
            'beginning-of-&buffer',
            'beginning-of-&line',
            '-',
            'pre&vious-line',
        ]
        
        self.cursorMeuuBackExtendTable = [
            # &: b,c,l,p,s,v,w
            'back-&char-extend-selection',
            'back-&paragraph-extend-selection',
            'back-&sentence-extend-selection',
            'back-&word-extend-selection',
            '-',
            'beginning-of-&buffer-extend-selection',
            'beginning-of-&line-extend-selection',
            '-',
            'pre&vious-line-extend-selection',
        ]
        
        self.cursorMenuExtendTable = [
            # &: l,p,s,w
            'extend-to-&line',
            'extend-to-&paragraph',
            'extend-to-&sentence',
            'extend-to-&word',
        ]
        
        self.cursorMenuForwardTable = [
            # &: b,c,l,n,p,s,w
            'end-of-&buffer',
            'end-of-&line',
            '-',
            'forward-&char',
            'forward-&paragraph',
            'forward-&sentence',
            'forward-&word',
            '-',
            '&next-line',
        ]
        
        self.cursorMenuForwardExtendTable = [
            # &: b,c,l,n,p,s,w
            'end-of-&buffer-extend-selection',
            'end-of-&line-extend-selection',
            '-',
            'forward-&char-extend-selection',
            'forward-&paragraph-extend-selection',
            'forward-&sentence-extend-selection',
            'forward-&word-extend-selection',#
            '-',
            '&next-line-extend-selection',    
        ]
    #@nonl
    #@-node:ekr.20060924124119:defineCmdsMenuCursorTable
    #@+node:ekr.20060923060822:defineCmdsMenuFocusTable
    def defineCmdsMenuFocusTable (self):
    
        self.cmdsMenuFocusTable = [
            '&cycle-all-focus',
            'focus-to-&body',          
            'focus-to-&log',             
            'focus-to-&minibuffer',     
            'focus-to-&tree',             
        ]
    #@-node:ekr.20060923060822:defineCmdsMenuFocusTable
    #@+node:ekr.20060117114315:defineCmdsMenuMacroTable
    def defineCmdsMenuMacroTable (self):
    
        self.cmdsMenuMacroTable = [
            '&load-file',
            '-',
            '&start-kbd-macro',
            '&end-kbd-macro',
            '&name-last-kbd-macro',
            '-',
            '&call-last-keyboard-macro',
            '&insert-keyboard-macro',
        ]
    #@-node:ekr.20060117114315:defineCmdsMenuMacroTable
    #@+node:ekr.20061011084101.1:defineCmdsMenuMinibufferTable
    def defineCmdsMenuMinibufferTable (self):
        
        self.cmdsMenuMinibufferTable = [
            # &: f,h,i,q,r,s,v
            '&full-command',
            'keyboard-&quit',
            '&repeat-complex-command',
            '&view-lossage',
            '-',
            '&show-mini-buffer',
            'h&ide-mini-buffer',
            '-',
            '&help-for-minibuffer',
        ]
    #@-node:ekr.20061011084101.1:defineCmdsMenuMinibufferTable
    #@+node:ekr.20060924120752:defineCmdsMenuPanesTable
    def defineCmdsMenuPanesTable (self):
    
        self.cmdsMenuPanesTable = [
            # &: a,b,d,f,l,n,o,p,u,x,y
            'contract-&body-pane',
            'contract-&log-pane',
            'contract-&outline-pane',
            'contract-&pane',
            '-',
            'expand-bo&dy-pane',
            'expand-lo&g-pane',
            'expand-o&utline-pane',
            'expand-pa&ne',
            '-',
            '&fully-expand-body-pane',
            'full&y-expand-log-pane',
            'fully-e&xpand-outline-pane',
            'fully-exp&and-pane',
        ]
        
    #@nonl
    #@-node:ekr.20060924120752:defineCmdsMenuPanesTable
    #@+node:ekr.20061011085641:defineCmdsMenuPickersTable
    def defineCmdsMenuPickersTable (self):
        
        self. cmdsMenuPickersTable = [
            'show-&colors',
            'show-find-&options',
            'show-&fonts',
        ]
    #@nonl
    #@-node:ekr.20061011085641:defineCmdsMenuPickersTable
    #@+node:ekr.20060117095212.2:defineCmdsMenuRectanglesTable
    def defineCmdsMenuRectanglesTable (self):
    
        self.cmdsMenuRectanglesTable = [
            '&clear-rectangle',
            'c&lose-rectangle',
            '&delete-rectangle',
            '&kill-rectangle',
            '&open-rectangle',
            '&string-rectangle',
            '&yank-rectangle',
        ]
    #@-node:ekr.20060117095212.2:defineCmdsMenuRectanglesTable
    #@+node:ekr.20060117095212.1:defineCmdsMenuRegistersTable
    def defineCmdsMenuRegistersTable (self):
    
        self.cmdsMenuRegistersTable = [
            # &: a,c,e,i,j,n,p,r,v
            '&append-to-register',
            'copy-r&ectangle-to-register',
            '&copy-to-register',
            'i&ncrement-register',
            '&insert-register',
            '&jump-to-register',
            # 'number-to-register',
            '&point-to-register',
            'p&repend-to-register',
            '&view-register',
        ]
    #@-node:ekr.20060117095212.1:defineCmdsMenuRegistersTable
    #@+node:ekr.20060923060822.1:defineCmdsMenuScrollTable
    def defineCmdsMenuScrollTable (self):
    
        self.cmdsMenuScrollTable = [
            # &: c,d,e,f,l,o,p,r,v,x
            'scroll-outline-down-&line',
            'scroll-outline-down-&page',
            'scroll-outline-le&ft',
            'scroll-outline-&right',
            's&croll-outline-up-line',
            'scr&oll-outline-up-page',
            '-',
            'scroll-&down',
            'scroll-&up',
            '-',
            'scroll-down-&extend-selection',
            'scroll-up-e&xtend-selection',
        ]
    #@nonl
    #@-node:ekr.20060923060822.1:defineCmdsMenuScrollTable
    #@+node:ekr.20060117095212.7:defineCmdsMenuSpellCheckTable
    def defineCmdsMenuSpellCheckTable (self):
    
        self.cmdsMenuSpellCheckTable = [
            '&open-spell-tab',
            'spell-&change',
            'spell-change-&then-find',
            'spell-&find',
            'spell-&ignore',
        ]
    #@-node:ekr.20060117095212.7:defineCmdsMenuSpellCheckTable
    #@+node:ekr.20060924161901:defineCmdsMenuTextTable
    def defineCmdsMenuTextTable (self):
    
        self.cmdsMenuTextTable = [
            # &: b,c,d,e,f,g,i,l,m,n,o,p,r,s,u,y
            '&beautify-python-code',
            'beautify-all-p&ython-code',
            '-',
            'center-&line',
            'center-&region',
            '-',
            '&capitalize-word',
            '&downcase-word',
            '&upcase-word',
            '-',
            'd&owncase-region',
            'u&pcase-region',
            '-',
            '&indent-region',
            'indent-r&elative',
            'indent-ri&gidly',
            'u&nindent-region',
            '-',
            'sort-colu&mns',
            'sort-&fields',
            '&sort-lines',
        ]
    #@nonl
    #@-node:ekr.20060924161901:defineCmdsMenuTextTable
    #@+node:ekr.20060926161940:defineCmdsMenuToggleTable
    def defineCmdsMenuToggleTable (self):
    
        self.cmdsMenuToggleTable = [
            # &: d,e,m,s,t,u,v
            'toggle-a&utocompleter',
            'toggle-call&tips',
            'toggle-&extend-mode',
            'toggle-input-&state',
            'toggle-in&visibles',
            'toggle-&mini-buffer',
            'toggle-split-&direction',
            '-',
            # &: a,b,c,f,h,i,r,w,x
            'toggle-find-&ignore-case-option',
            'toggle-find-in-&body-option',
            'toggle-find-in-&headline-option',
            'toggle-find-mark-&changes-option',
            'toggle-find-mark-&finds-option',
            'toggle-find-rege&x-option',
            'toggle-find-&reverse-option',
            'toggle-find-&word-option',
            'toggle-find-wrap-&around-option',
        ]
    #@-node:ekr.20060926161940:defineCmdsMenuToggleTable
    #@-node:ekr.20050921103230:defineCmdsMenuTables & helpers
    #@+node:ekr.20031218072017.3773:defineWindowMenuTables
    def defineWindowMenuTables (self):
        
        __pychecker__ = 'no-unusednames=c,f'
        
        c = self.c ; f = self.frame
    
        self.windowMenuTopTable = [
            ("&Equal Sized Panes",f.equalSizedPanes),
            ("Toggle &Active Pane",f.toggleActivePane),
            ("Toggle &Split Direction",f.toggleSplitDirection),
            ("-",None),
            ("Resize To Screen",f.resizeToScreen),
            ("Casca&de",f.cascade),
            ("&Minimize All",f.minimizeAll),
            ("-",None),
            ("Open &Compare Window",c.openCompareWindow),
            ("Open &Python Window",c.openPythonWindow),
        ]
    #@-node:ekr.20031218072017.3773:defineWindowMenuTables
    #@+node:ekr.20031218072017.3774:defineHelpMenuTables
    def defineHelpMenuTables (self):
        
        self.helpMenuTable = [
            # &: a,b,c,d,f,h,l,m,n,o,p,r,s,t,u
            ("&About Leo...",           'about-leo'),
            ("Online &Home Page",       'open-online-home'),
            ("Open Online &Tutorial",   'open-online-tutorial'),
            ("Open &Users Guide",       'open-users-guide'),
            '-',
            ("Open Leo&Docs.leo",       'open-leoDocs-leo'),
            ("Open Leo&Plugins.leo",    'open-leoPlugins-leo'),
            ("Open Leo&Settings.leo",   'open-leoSettings-leo'),
            ("Open &myLeoSettings.leo", 'open-myLeoSettings-leo'),
            '-',
            'he&lp-for-minibuffer',
            'help-for-&command',
            '-',
            '&apropos-autocompletion',
            'apropos-&bindings',
            'apropos-&find-commands',
            '-',
            'pri&nt-bindings',
            'print-c&ommands',
        ]
    #@-node:ekr.20031218072017.3774:defineHelpMenuTables
    #@-node:ekr.20031218072017.3752:defineMenuTables & helpers
    #@+node:ekr.20051022053758.1:Helpers
    #@+node:ekr.20031218072017.3783:canonicalizeMenuName & cononicalizeTranslatedMenuName
    def canonicalizeMenuName (self,name):
        
        return ''.join([ch for ch in name.lower() if ch.isalnum()])
        
    def canonicalizeTranslatedMenuName (self,name):
        
        return ''.join([ch for ch in name.lower() if ch not in u'& \t\n\r'])
    
    #@-node:ekr.20031218072017.3783:canonicalizeMenuName & cononicalizeTranslatedMenuName
    #@+node:ekr.20051022044950:computeOldStyleShortcutKey
    def computeOldStyleShortcutKey (self,s):
        
        '''Compute the old-style shortcut key for @shortcuts entries.'''
        
        return ''.join([ch for ch in s.strip().lower() if ch.isalnum()])
    #@-node:ekr.20051022044950:computeOldStyleShortcutKey
    #@+node:ekr.20031218072017.1723:createMenuEntries
    def createMenuEntries (self,menu,table,dynamicMenu=False):
            
        '''Create a menu entry from the table.
        New in 4.4: this method shows the shortcut in the menu,
        but this method **never** binds any shortcuts.'''
        
        c = self.c ; f = c.frame ; k = c.k
        if g.app.unitTesting: return
        for data in table:
            #@        << get label & command or continue >>
            #@+node:ekr.20051021091958:<< get label & command or continue >>
            if type(data) == type(''):
                # New in Leo 4.4.2: Can use the same string for both the label and the command string.
                ok = True
                label = self.capitalizeMinibufferMenuName(data)
                command = data.replace('&','')
                if label == '-':
                    self.add_separator(menu)
                    continue # That's all.
            else:
                ok = type(data) in (type(()), type([])) and len(data) in (2,3)
                if ok:
                    if len(data) == 2:
                        # New in 4.4b2: command can be a minibuffer-command name (a string)
                        label,command = data
                    else:
                        # New in 4.4: we ignore shortcuts bound in menu tables.
                        label,junk,command = data
                        
                    if label in (None,'-'):
                        self.add_separator(menu)
                        continue # That's all.
                else:
                    g.trace('bad data in menu table: %s' % repr(data))
                    continue # Ignore bad data
            #@nonl
            #@-node:ekr.20051021091958:<< get label & command or continue >>
            #@nl
            #@        << compute commandName & accel from label & command >>
            #@+node:ekr.20031218072017.1725:<< compute commandName & accel from label & command >>
            # New in 4.4b2: command can be a minibuffer-command name (a string)
            minibufferCommand = type(command) == type('')
            accel = None
            if minibufferCommand:
                commandName = command 
                command = c.commandsDict.get(commandName)
                if command:
                    rawKey,bunchList = c.config.getShortcut(commandName)
                    # Pick the first entry that is not a mode.
                    for bunch in bunchList:
                        if not bunch.pane.endswith('-mode'):
                            # g.trace('1',bunch)
                            accel = bunch and bunch.val
                            if bunch.pane  == 'text': break # New in Leo 4.4.2: prefer text bindings.
                else:
                    if not g.app.unitTesting and not dynamicMenu:
                        # Don't warn during unit testing.
                        # This may come from a plugin that normally isn't enabled.
                        g.trace('No inverse for %s' % commandName)
                    continue # There is no way to make this menu entry.
            else:
                # First, get the old-style name.
                commandName = self.computeOldStyleShortcutKey(label)
                rawKey,bunchList = c.config.getShortcut(commandName)
                for bunch in bunchList:
                    if not bunch.pane.endswith('-mode'):
                        # g.trace('2',bunch)
                        accel = bunch and bunch.val ; break
                # Second, get new-style name.
                if not accel:
                    #@        << compute emacs_name >>
                    #@+node:ekr.20051021100806.1:<< compute emacs_name >>
                    #@+at 
                    #@nonl
                    # One not-so-horrible kludge remains.
                    # 
                    # The cut/copy/paste commands in the menu tables are not 
                    # the same as the methods
                    # actually bound to cut/copy/paste-text minibuffer 
                    # commands, so we must do a bit
                    # of extra translation to discover whether the user has 
                    # overridden their
                    # bindings.
                    #@-at
                    #@@c
                    
                    if command in (f.OnCutFromMenu,f.OnCopyFromMenu,f.OnPasteFromMenu):
                        emacs_name = '%s-text' % commandName
                    else:
                        try: # User errors in the table can cause this.
                            emacs_name = k.inverseCommandsDict.get(command.__name__)
                        except Exception:
                            emacs_name = None
                    #@-node:ekr.20051021100806.1:<< compute emacs_name >>
                    #@nl
                        # Contains the not-so-horrible kludge.
                    if emacs_name:
                        commandName = emacs_name
                        rawKey,bunchList = c.config.getShortcut(emacs_name)
                        # Pick the first entry that is not a mode.
                        for bunch in bunchList:
                            if not bunch.pane.endswith('-mode'):
                                accel = bunch.val ; break
                                # g.trace('2',bunch)
                    elif not dynamicMenu:
                        g.trace('No inverse for %s' % commandName)
            #@-node:ekr.20031218072017.1725:<< compute commandName & accel from label & command >>
            #@nl
            accelerator = stroke = k.shortcutFromSetting(accel) or ''
            accelerator = accelerator and g.stripBrackets(k.prettyPrintKey(accelerator))
            def masterMenuCallback (k=k,stroke=stroke,command=command,commandName=commandName):
                return k.masterMenuHandler(stroke,command,commandName)
            realLabel = self.getRealMenuName(label)
            amp_index = realLabel.find("&")
            realLabel = realLabel.replace("&","")
            if sys.platform == 'darwin':
                #@            << clear accelerator if it is a plain key >>
                #@+node:ekr.20060216110502:<< clear accelerator if it is a plain key >>
                for z in ('Alt','Ctrl','Command'):
                    if accelerator.find(z) != -1:
                        break # Found.
                else:
                    accelerator = ''
                #@-node:ekr.20060216110502:<< clear accelerator if it is a plain key >>
                #@nl
            self.add_command(menu,label=realLabel,
                accelerator=accelerator,
                command=masterMenuCallback,
                underline=amp_index)
    #@-node:ekr.20031218072017.1723:createMenuEntries
    #@+node:ekr.20031218072017.3784:createMenuItemsFromTable
    def createMenuItemsFromTable (self,menuName,table,dynamicMenu=False):
        
        try:
            menu = self.getMenu(menuName)
            if menu == None:
                print "menu does not exist: ",menuName
                g.es("menu does not exist: ",menuName)
                return
            self.createMenuEntries(menu,table,dynamicMenu=dynamicMenu)
        except:
            s = "exception creating items for %s menu" % menuName
            g.es_print(s)
            g.es_exception()
            
        g.app.menuWarningsGiven = True
    #@-node:ekr.20031218072017.3784:createMenuItemsFromTable
    #@+node:ekr.20031218072017.3804:createNewMenu
    def createNewMenu (self,menuName,parentName="top",before=None):
    
        try:
            parent = self.getMenu(parentName) # parent may be None.
            menu = self.getMenu(menuName)
            if menu:
                g.es("menu already exists: " + menuName,color="red")
            else:
                menu = self.new_menu(parent,tearoff=0)
                self.setMenu(menuName,menu)
                label = self.getRealMenuName(menuName)
                amp_index = label.find("&")
                label = label.replace("&","")
                if before: # Insert the menu before the "before" menu.
                    index_label = self.getRealMenuName(before)
                    amp_index = index_label.find("&")
                    index_label = index_label.replace("&","")
                    index = parent.index(index_label)
                    self.insert_cascade(parent,index=index,label=label,menu=menu,underline=amp_index)
                else:
                    self.add_cascade(parent,label=label,menu=menu,underline=amp_index)
                return menu
        except:
            g.es("exception creating " + menuName + " menu")
            g.es_exception()
            return None
    #@-node:ekr.20031218072017.3804:createNewMenu
    #@+node:ekr.20031218072017.4116:createOpenWithMenuFromTable & helper
    def createOpenWithMenuFromTable (self,table):
        
        '''Entries in the table passed to createOpenWithMenuFromTable are
    tuples of the form (commandName,shortcut,data).
    
    - command is one of "os.system", "os.startfile", "os.spawnl", "os.spawnv" or "exec".
    - shortcut is a string describing a shortcut, just as for createMenuItemsFromTable.
    - data is a tuple of the form (command,arg,ext).
    
    Leo executes command(arg+path) where path is the full path to the temp file.
    If ext is not None, the temp file has the given extension.
    Otherwise, Leo computes an extension based on the @language directive in effect.'''
    
        c = self.c
        g.app.openWithTable = table # Override any previous table.
        # Delete the previous entry.
        parent = self.getMenu("File")
        label = self.getRealMenuName("Open &With...")
        amp_index = label.find("&")
        label = label.replace("&","")
        try:
            index = parent.index(label)
            parent.delete(index)
        except:
            try:
                index = parent.index("Open With...")
                parent.delete(index)
            except: return
        # Create the Open With menu.
        openWithMenu = self.createOpenWithMenu(parent,label,index,amp_index)
        self.setMenu("Open With...",openWithMenu)
        # Create the menu items in of the Open With menu.
        for entry in table:
            if len(entry) != 3: # 6/22/03
                g.es("createOpenWithMenuFromTable: invalid data",color="red")
                return
        self.createOpenWithMenuItemsFromTable(openWithMenu,table)
        for entry in table:
            name,shortcut,data = entry
            c.k.bindOpenWith (shortcut,name,data)
    #@+node:ekr.20051022043608.1:createOpenWithMenuItemsFromTable
    def createOpenWithMenuItemsFromTable (self,menu,table):
        
        '''Create an entry in the Open with Menu from the table.
        
        Each entry should be a sequence with 2 or 3 elements.'''
        
        c = self.c ; k = c.k
    
        if g.app.unitTesting: return
    
        for data in table:
            #@        << get label, accelerator & command or continue >>
            #@+node:ekr.20051022043713.1:<< get label, accelerator & command or continue >>
            ok = (
                type(data) in (type(()), type([])) and
                len(data) in (2,3)
            )
                
            if ok:
                if len(data) == 2:
                    label,openWithData = data ; accelerator = None
                else:
                    label,accelerator,openWithData = data
                    accelerator = k.shortcutFromSetting(accelerator)
                    accelerator = accelerator and g.stripBrackets(k.prettyPrintKey(accelerator))
            else:
                g.trace('bad data in Open With table: %s' % repr(data))
                continue # Ignore bad data
            #@-node:ekr.20051022043713.1:<< get label, accelerator & command or continue >>
            #@nl
            realLabel = self.getRealMenuName(label)
            underline=realLabel.find("&")
            realLabel = realLabel.replace("&","")
            callback = self.defineOpenWithMenuCallback(openWithData)
        
            self.add_command(menu,label=realLabel,
                accelerator=accelerator or '',
                command=callback,underline=underline)
    #@-node:ekr.20051022043608.1:createOpenWithMenuItemsFromTable
    #@-node:ekr.20031218072017.4116:createOpenWithMenuFromTable & helper
    #@+node:ekr.20031218072017.2078:createRecentFilesMenuItems (leoMenu)
    def createRecentFilesMenuItems (self):
        
        c = self.c
        recentFilesMenu = self.getMenu("Recent Files...")
        
        # Delete all previous entries.
        self.delete_range(recentFilesMenu,0,len(c.recentFiles)+2)
        
        # Create the first two entries.
        table = (
            ("Clear Recent Files",None,c.clearRecentFiles),
            ("-",None,None))
        self.createMenuEntries(recentFilesMenu,table)
        
        # Create all the other entries.
        i = 3
        for name in c.recentFiles:
            def recentFilesCallback (event=None,c=c,name=name):
                __pychecker__ = '--no-argsused' # event not used, but must be present.
                c.openRecentFile(name)
            accel_ch = (string.digits + string.letters.upper()) # Not a unicode problem.
            label = "%s %s" % (accel_ch[i-2],g.computeWindowTitle(name))
            self.add_command(recentFilesMenu,label=label,command=recentFilesCallback,underline=0)
            i += 1
    #@-node:ekr.20031218072017.2078:createRecentFilesMenuItems (leoMenu)
    #@+node:ekr.20031218072017.4117:defineMenuCallback
    def defineMenuCallback(self,command,name,minibufferCommand):
        
        if minibufferCommand:
            
            # Create a dummy event as a signal to doCommand.
            event = g.Bunch(keysym='',char='',widget='')
            
            # The first parameter must be event, and it must default to None.
            def minibufferMenuCallback(event=event,self=self,command=command,label=name):
                __pychecker__ = '--no-argsused' # event not used, and must be present.
                
                c = self.c
                return c.doCommand(command,label,event)
        
            return minibufferMenuCallback
            
        else:
        
            # The first parameter must be event, and it must default to None.
            def legacyMenuCallback(event=None,self=self,command=command,label=name):
                __pychecker__ = '--no-argsused' # event not used, and must be present.
                
                c = self.c
                return c.doCommand(command,label)
        
            return legacyMenuCallback
    #@-node:ekr.20031218072017.4117:defineMenuCallback
    #@+node:ekr.20031218072017.4118:defineOpenWithMenuCallback
    def defineOpenWithMenuCallback(self,data):
        
        # The first parameter must be event, and it must default to None.
        def openWithMenuCallback(event=None,self=self,data=data):
            return self.c.openWith(data=data)
    
        return openWithMenuCallback
    #@-node:ekr.20031218072017.4118:defineOpenWithMenuCallback
    #@+node:ekr.20031218072017.3805:deleteMenu
    def deleteMenu (self,menuName):
    
        try:
            menu = self.getMenu(menuName)
            if menu:
                self.destroy(menu)
                self.destroyMenu(menuName)
            else:
                g.es("can't delete menu: " + menuName)
        except:
            g.es("exception deleting " + menuName + " menu")
            g.es_exception()
    #@-node:ekr.20031218072017.3805:deleteMenu
    #@+node:ekr.20031218072017.3806:deleteMenuItem
    def deleteMenuItem (self,itemName,menuName="top"):
        
        """Delete itemName from the menu whose name is menuName."""
    
        try:
            menu = self.getMenu(menuName)
            if menu:
                realItemName = self.getRealMenuName(itemName)
                self.delete(menu,realItemName)
            else:
                g.es("menu not found: " + menuName)
        except:
            g.es("exception deleting " + itemName + " from " + menuName + " menu")
            g.es_exception()
    #@-node:ekr.20031218072017.3806:deleteMenuItem
    #@+node:ekr.20031218072017.3782:get/setRealMenuName & setRealMenuNamesFromTable
    # Returns the translation of a menu name or an item name.
    
    def getRealMenuName (self,menuName):
    
        cmn = self.canonicalizeTranslatedMenuName(menuName)
        return g.app.realMenuNameDict.get(cmn,menuName)
        
    def setRealMenuName (self,untrans,trans):
    
        cmn = self.canonicalizeTranslatedMenuName(untrans)
        g.app.realMenuNameDict[cmn] = trans
    
    def setRealMenuNamesFromTable (self,table):
    
        try:
            for untrans,trans in table:
                self.setRealMenuName(untrans,trans)
        except:
            g.es("exception in setRealMenuNamesFromTable")
            g.es_exception()
    #@-node:ekr.20031218072017.3782:get/setRealMenuName & setRealMenuNamesFromTable
    #@+node:ekr.20031218072017.3807:getMenu, setMenu, destroyMenu
    def getMenu (self,menuName):
    
        cmn = self.canonicalizeMenuName(menuName)
        return self.menus.get(cmn)
        
    def setMenu (self,menuName,menu):
        
        cmn = self.canonicalizeMenuName(menuName)
        self.menus [cmn] = menu
        
    def destroyMenu (self,menuName):
        
        cmn = self.canonicalizeMenuName(menuName)
        del self.menus[cmn]
    #@-node:ekr.20031218072017.3807:getMenu, setMenu, destroyMenu
    #@-node:ekr.20051022053758.1:Helpers
    #@-node:ekr.20031218072017.3781:Gui-independent menu routines
    #@+node:ekr.20031218072017.3808:Must be overridden in menu subclasses
    #@+node:ekr.20031218072017.3809:9 Routines with Tk spellings
    def add_cascade (self,parent,label,menu,underline):
        self.oops()
        
    def add_command (self,menu,**keys):
        self.oops()
        
    def add_separator(self,menu):
        self.oops()
        
    def bind (self,bind_shortcut,callback):
        self.oops()
    
    def delete (self,menu,realItemName):
        self.oops()
        
    def delete_range (self,menu,n1,n2):
        self.oops()
    
    def destroy (self,menu):
        self.oops()
    
    def insert_cascade (self,parent,index,label,menu,underline):
        self.oops()
    
    def new_menu(self,parent,tearoff=0):
        self.oops()
    #@-node:ekr.20031218072017.3809:9 Routines with Tk spellings
    #@+node:ekr.20031218072017.3810:9 Routines with new spellings
    def activateMenu (self,menuName): # New in Leo 4.4b2.
        self.oops()
    
    def clearAccel (self,menu,name):
        self.oops()
    
    def createMenuBar (self,frame):
        self.oops()
        
    if 0: # Now defined in the base class
        def createOpenWithMenuFromTable (self,table):
            self.oops()
    
        def defineMenuCallback(self,command,name):
            self.oops()
            
        def defineOpenWithMenuCallback(self,command):
            self.oops()
        
    def disableMenu (self,menu,name):
        self.oops()
        
    def enableMenu (self,menu,name,val):
        self.oops()
        
    def getManuLabel (self,menu):
        __pychecker__ = '--no-argsused' # menu not used.
        self.oops()
        
    def setMenuLabel (self,menu,name,label,underline=-1):
        self.oops()
    #@-node:ekr.20031218072017.3810:9 Routines with new spellings
    #@-node:ekr.20031218072017.3808:Must be overridden in menu subclasses
    #@-others
#@-node:ekr.20031218072017.3750:class leoMenu
#@+node:ekr.20031218072017.3811:class nullMenu
class nullMenu(leoMenu):
    
    """A null menu class for testing and batch execution."""
    
    __pychecker__ = '--no-argsused' # This calss has many unused args.
    
    #@    @+others
    #@+node:ekr.20050104094308:ctor
    def __init__ (self,frame):
        
        # Init the base class.
        leoMenu.__init__(self,frame)
    #@-node:ekr.20050104094308:ctor
    #@+node:ekr.20050104094029:oops
    def oops (self):
    
        # g.trace("leoMenu", g.callers())
        pass
    #@-node:ekr.20050104094029:oops
    #@-others
#@-node:ekr.20031218072017.3811:class nullMenu
#@-others
#@-node:ekr.20031218072017.3749:@thin leoMenu.py
#@-leo
