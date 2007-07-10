#@+leo-ver=4-thin
#@+node:ekr.20031218072017.3206:@thin leoImport.py
#@@language python
#@@tabwidth -4
#@@pagewidth 80

import leoGlobals as g
import leoTest # Support for unit tests.

import parser
import re
import string
import tabnanny
import tokenize

class baseLeoImportCommands:
    """The base class for Leo's import commands."""
    #@    @+others
    #@+node:ekr.20031218072017.3207:import.__init__
    def __init__ (self,c):

        self.c = c

        # New in 4.3: honor any tabwidth directive in effect when importing files.
        self.tabwidth = c.tab_width

        # Set by ImportFilesFommand.
        self.treeType = "@file" # "@root" or "@file"
        # Set by ImportWebCommand.
        self.webType = "@noweb" # "cweb" or "noweb"

        # Set by create_outline.
        self.fileName = None # The original file name, say x.cpp
        self.methodName = None # x, as in < < x methods > > =
        self.fileType = None # ".py", ".c", etc.
        self.rootLine = "" # Empty or @root + self.fileName

        # Support of output_newline option
        self.output_newline = g.getOutputNewline(c=c)

        # Used by Importers.
        self.web_st = []
        self.encoding = g.app.tkEncoding # 2/25/03: was "utf-8"
        self._forcedGnxPositionList = []
    #@-node:ekr.20031218072017.3207:import.__init__
    #@+node:ekr.20031218072017.3209:Import
    #@+node:ekr.20031218072017.3210:createOutline
    def createOutline (self,fileName,parent):

        c = self.c ; u = c.undoer
        junk,self.fileName = g.os_path_split(fileName)
        self.methodName,ext = g.os_path_splitext(self.fileName)
        self.fileType = ext
        self.setEncoding()
        # g.trace(self.fileName,self.fileType)
        # All file types except the following just get copied to the parent node.
        ext = ext.lower()
        appendFileFlag = ext not in (
            ".c", ".cpp", ".cxx", ".el", ".java", ".lua", ".pas", ".py", ".pyw", ".php")
        #@    << Read file into s >>
        #@+node:ekr.20031218072017.3211:<< Read file into s >>
        try:
            theFile = open(fileName)
            s = theFile.read()
            s = g.toUnicode(s,self.encoding)
            theFile.close()
        except IOError:
            g.es("can not open " + fileName)
            leoTest.fail()
            return None
        #@-node:ekr.20031218072017.3211:<< Read file into s >>
        #@nl
        # Create the top-level headline.
        undoData = u.beforeInsertNode(parent)
        p = parent.insertAsLastChild()
        if self.treeType == "@file":
            p.initHeadString("@file " + fileName)
        else:
            p.initHeadString(fileName)
        u.afterInsertNode(p,'Import',undoData)

        self.rootLine = g.choose(self.treeType=="@file","","@root-code "+self.fileName+'\n')

        if appendFileFlag:
            body = "@ignore\n"
            if ext in (".html",".htm"): body += "@language html\n"
            if ext in (".txt",".text"): body += "@nocolor\n"
            c.setBodyString(p,body + self.rootLine + s)
        elif ext in (".c", ".cpp", ".cxx"):
            self.scanCText(s,p)
        elif ext == ".el":
            self.scanElispText(s,p)
        elif ext in (".fs", ".fi"):
            self.scanForthText(s,p)
        elif ext == ".java":
            self.scanJavaText(s,p,True) #outer level
        elif ext == ".lua":
            self.scanLuaText(s,p)
        elif ext == ".pas":
            self.scanPascalText(s,p)
        elif ext in (".py", ".pyw"):
            self.scanPythonText(s,p)
        elif ext == ".php":
            self.scanPHPText(s,p) # 08-SEP-2002 DTHEIN
        else:
            g.es("createOutline: can't happen")
        return p
    #@-node:ekr.20031218072017.3210:createOutline
    #@+node:ekr.20041126042730:getTabWidth
    def getTabWidth (self):

        d = g.scanDirectives(self.c)
        w = d.get("tabwidth")
        if w not in (0,None):
            return w
        else:
            return self.c.tab_width
    #@-node:ekr.20041126042730:getTabWidth
    #@+node:ekr.20031218072017.1810:importDerivedFiles
    def importDerivedFiles (self,parent=None,paths=None):
        # Not a command.  It must *not* have an event arg.

        c = self.c ; u = c.undoer ; command = 'Import'
        at = c.atFileCommands ; current = c.currentPosition()
        self.tab_width = self.getTabWidth()
        if not paths: return
        c.beginUpdate()
        try:
            u.beforeChangeGroup(current,command)
            for fileName in paths:
                g.setGlobalOpenDir(fileName)
                #@            << set isThin if fileName is a thin derived file >>
                #@+node:ekr.20040930135204:<< set isThin if fileName is a thin derived file >>
                fileName = g.os_path_normpath(fileName)

                try:
                    theFile = open(fileName,'rb')
                    isThin = at.scanHeaderForThin(theFile,fileName)
                    theFile.close()
                except IOError:
                    isThin = False
                #@-node:ekr.20040930135204:<< set isThin if fileName is a thin derived file >>
                #@nl
                undoData = u.beforeInsertNode(parent)
                p = parent.insertAfter()
                if isThin:
                    at.forceGnxOnPosition(p)
                    p.initHeadString("@thin " + fileName)
                    at.read(p,thinFile=True)
                else:
                    p.initHeadString("Imported @file " + fileName)
                    at.read(p,importFileName=fileName)
                p.contract()
                u.afterInsertNode(p,command,undoData)
            current.expand()
            c.selectPosition(current)
            c.setChanged(True)
            u.afterChangeGroup(p,command)
        finally:
            c.endUpdate()
    #@+node:ekr.20051208100903.1:forceGnxOnPosition
    def forceGnxOnPosition (self,p):

        self._forcedGnxPositionList.append(p.v)
    #@-node:ekr.20051208100903.1:forceGnxOnPosition
    #@-node:ekr.20031218072017.1810:importDerivedFiles
    #@+node:ekr.20031218072017.3212:importFilesCommand
    def importFilesCommand (self,files=None,treeType=None,
        perfectImport=True,testing=False,verbose=False):
            # Not a command.  It must *not* have an event arg.

        c = self.c
        if c == None: return
        v = current = c.currentVnode()
        if current == None: return
        if len(files) < 1: return
        self.tab_width = self.getTabWidth() # New in 4.3.
        self.treeType = treeType
        c.beginUpdate()
        try: # range of update...
            if len(files) == 2:
                #@            << Create a parent for two files having a common prefix >>
                #@+node:ekr.20031218072017.3213:<< Create a parent for two files having a common prefix >>
                #@+at 
                #@nonl
                # The two filenames have a common prefix everything before the 
                # last period is the same.  For example, x.h and x.cpp.
                #@-at
                #@@c

                name0 = files[0]
                name1 = files[1]
                prefix0, junk = g.os_path_splitext(name0)
                prefix1, junk = g.os_path_splitext(name1)
                if len(prefix0) > 0 and prefix0 == prefix1:
                    current = current.insertAsLastChild()
                    junk, nameExt = g.os_path_split(prefix1)
                    name,ext = g.os_path_splitext(prefix1)
                    current.initHeadString(name)
                #@-node:ekr.20031218072017.3213:<< Create a parent for two files having a common prefix >>
                #@nl
            for fileName in files:
                g.setGlobalOpenDir(fileName)
                v = self.createOutline(fileName,current)
                if v: # createOutline may fail.
                    perfectImport = False ###
                    testing = True; verbose = True
                    if perfectImport and treeType == "@file": # Can't correct @root trees.
                        self.perfectImport(fileName,v,testing=testing,verbose=verbose,verify=False)
                    else:
                        if not g.unitTesting:
                            g.es("imported " + fileName,color="blue")
                    v.contract()
                    v.setDirty()
                    c.setChanged(True)
            c.validateOutline()
            current.expand()
        finally:
            c.endUpdate()
        c.selectVnode(current)
    #@-node:ekr.20031218072017.3212:importFilesCommand
    #@+node:ekr.20031218072017.3214:importFlattenedOutline & allies
    #@+node:ekr.20031218072017.3215:convertMoreString/StringsToOutlineAfter
    # Used by paste logic.

    def convertMoreStringToOutlineAfter (self,s,firstVnode):
        s = string.replace(s,"\r","")
        strings = string.split(s,"\n")
        return self.convertMoreStringsToOutlineAfter(strings,firstVnode)

    # Almost all the time spent in this command is spent here.

    def convertMoreStringsToOutlineAfter (self,strings,firstVnode):

        __pychecker__ = '--no-objattrs' # suppress bad warnings re lastVnode.

        c = self.c
        if len(strings) == 0: return None
        if not self.stringsAreValidMoreFile(strings): return None
        c.beginUpdate()
        try: # range of update...
            firstLevel, junk = self.moreHeadlineLevel(strings[0])
            lastLevel = -1 ; theRoot = lastVnode = None
            index = 0
            while index < len(strings):
                progress = index
                s = strings[index]
                level, newFlag = self.moreHeadlineLevel(s)
                level -= firstLevel
                if level >= 0:
                    #@                << Link a new vnode v into the outline >>
                    #@+node:ekr.20031218072017.3216:<< Link a new vnode v into the outline >>
                    assert(level >= 0)
                    if lastVnode is None:
                        # g.trace(firstVnode)
                        theRoot = v = firstVnode.insertAfter()
                    elif level == lastLevel:
                        v = lastVnode.insertAfter()
                    elif level == lastLevel + 1:
                        v = lastVnode.insertAsNthChild(0)
                    else:
                        assert(level < lastLevel)
                        while level < lastLevel:
                            lastLevel -= 1
                            lastVnode = lastVnode.parent()
                            assert(lastVnode)
                            assert(lastLevel >= 0)
                        v = lastVnode.insertAfter()
                    lastVnode = v
                    lastLevel = level
                    #@-node:ekr.20031218072017.3216:<< Link a new vnode v into the outline >>
                    #@nl
                    #@                << Set the headline string, skipping over the leader >>
                    #@+node:ekr.20031218072017.3217:<< Set the headline string, skipping over the leader >>
                    j = 0
                    while g.match(s,j,'\t'):
                        j += 1
                    if g.match(s,j,"+ ") or g.match(s,j,"- "):
                        j += 2

                    v.initHeadString(s[j:])
                    #@-node:ekr.20031218072017.3217:<< Set the headline string, skipping over the leader >>
                    #@nl
                    #@                << Count the number of following body lines >>
                    #@+node:ekr.20031218072017.3218:<< Count the number of following body lines >>
                    bodyLines = 0
                    index += 1 # Skip the headline.
                    while index < len(strings):
                        s = strings[index]
                        level, junk = self.moreHeadlineLevel(s)
                        level -= firstLevel
                        if level >= 0:
                            break
                        # Remove first backslash of the body line.
                        if g.match(s,0,'\\'):
                            strings[index] = s[1:]
                        bodyLines += 1
                        index += 1
                    #@-node:ekr.20031218072017.3218:<< Count the number of following body lines >>
                    #@nl
                    #@                << Add the lines to the body text of v >>
                    #@+node:ekr.20031218072017.3219:<< Add the lines to the body text of v >>
                    if bodyLines > 0:
                        body = ""
                        n = index - bodyLines
                        while n < index:
                            body += strings[n]
                            if n != index - 1:
                                body += "\n"
                            n += 1
                        v.setTnodeText(body)
                    #@-node:ekr.20031218072017.3219:<< Add the lines to the body text of v >>
                    #@nl
                    v.setDirty()
                else: index += 1
                assert progress < index
            if theRoot:
                theRoot.setDirty()
                c.setChanged(True)
        finally:
            c.endUpdate()
        return theRoot
    #@-node:ekr.20031218072017.3215:convertMoreString/StringsToOutlineAfter
    #@+node:ekr.20031218072017.3220:importFlattenedOutline
    def importFlattenedOutline (self,files): # Not a command, so no event arg.

        c = self.c ; u = c.undoer ; current = c.currentPosition()
        if current == None: return
        if len(files) < 1: return

        self.setEncoding()
        fileName = files[0] # files contains at most one file.
        g.setGlobalOpenDir(fileName)
        #@    << Read the file into array >>
        #@+node:ekr.20031218072017.3221:<< Read the file into array >>
        try:
            theFile = open(fileName)
            s = theFile.read()
            s = string.replace(s,"\r","")
            s = g.toUnicode(s,self.encoding)
            array = string.split(s,"\n")
            theFile.close()
        except IOError:
            g.es("Can not open " + fileName, color="blue")
            leoTest.fail()
            return
        #@-node:ekr.20031218072017.3221:<< Read the file into array >>
        #@nl

        # Convert the string to an outline and insert it after the current node.
        undoData = u.beforeInsertNode(current)
        p = self.convertMoreStringsToOutlineAfter(array,current)
        if p:
            c.endEditing()
            c.validateOutline()
            c.editPosition(p)
            p.setDirty()
            c.setChanged(True)
            u.afterInsertNode(p,'Import',undoData)
        else:
            g.es(fileName + " is not a valid MORE file.")
    #@-node:ekr.20031218072017.3220:importFlattenedOutline
    #@+node:ekr.20031218072017.3222:moreHeadlineLevel
    # return the headline level of s,or -1 if the string is not a MORE headline.
    def moreHeadlineLevel (self,s):

        level = 0 ; i = 0
        while g.match(s,i,'\t'):
            level += 1
            i += 1
        plusFlag = g.choose(g.match(s,i,"+"),True,False)
        if g.match(s,i,"+ ") or g.match(s,i,"- "):
            return level, plusFlag
        else:
            return -1, plusFlag
    #@-node:ekr.20031218072017.3222:moreHeadlineLevel
    #@+node:ekr.20031218072017.3223:stringIs/stringsAreValidMoreFile
    # Used by paste logic.

    def stringIsValidMoreFile (self,s):

        s = string.replace(s,"\r","")
        strings = string.split(s,"\n")
        return self.stringsAreValidMoreFile(strings)

    def stringsAreValidMoreFile (self,strings):

        if len(strings) < 1: return False
        level1, plusFlag = self.moreHeadlineLevel(strings[0])
        if level1 == -1: return False
        # Check the level of all headlines.
        i = 0 ; lastLevel = level1
        while i < len(strings):
            s = strings[i] ; i += 1
            level, newFlag = self.moreHeadlineLevel(s)
            if level > 0:
                if level < level1 or level > lastLevel + 1:
                    return False # improper level.
                elif level > lastLevel and not plusFlag:
                    return False # parent of this node has no children.
                elif level == lastLevel and plusFlag:
                    return False # last node has missing child.
                else:
                    lastLevel = level
                    plusFlag = newFlag
        return True
    #@-node:ekr.20031218072017.3223:stringIs/stringsAreValidMoreFile
    #@-node:ekr.20031218072017.3214:importFlattenedOutline & allies
    #@+node:ekr.20031218072017.3224:importWebCommand & allies
    #@+node:ekr.20031218072017.3225:createOutlineFromWeb
    def createOutlineFromWeb (self,path,parent):

        c = self.c ; u = c.undoer
        junk,fileName = g.os_path_split(path)

        undoData = u.beforeInsertNode(parent)

        # Create the top-level headline.
        p = parent.insertAsLastChild()
        p.initHeadString(fileName)
        if self.webType=="cweb":
            c.setBodyString(p,"@ignore\n" + self.rootLine + "@language cweb")

        # Scan the file, creating one section for each function definition.
        self.scanWebFile(path,p)

        u.afterInsertNode(p,'Import',undoData)

        return p
    #@-node:ekr.20031218072017.3225:createOutlineFromWeb
    #@+node:ekr.20031218072017.3226:importWebCommand
    def importWebCommand (self,files,webType):

        c = self.c ; current = c.currentVnode()
        if current == None: return
        if not files: return
        self.tab_width = self.getTabWidth() # New in 4.3.
        self.webType = webType

        c.beginUpdate()
        try:
            for fileName in files:
                g.setGlobalOpenDir(fileName)
                v = self.createOutlineFromWeb(fileName,current)
                v.contract()
                v.setDirty()
                c.setChanged(True)
            c.selectVnode(current)
        finally:
            c.endUpdate()
    #@-node:ekr.20031218072017.3226:importWebCommand
    #@+node:ekr.20031218072017.3227:findFunctionDef
    def findFunctionDef (self,s,i):

        # Look at the next non-blank line for a function name.
        i = g.skip_ws_and_nl(s,i)
        k = g.skip_line(s,i)
        name = None
        while i < k:
            if g.is_c_id(s[i]):
                j = i ; i = g.skip_c_id(s,i) ; name = s[j:i]
            elif s[i] == '(':
                if name: return name
                else: break
            else: i += 1
        return None
    #@-node:ekr.20031218072017.3227:findFunctionDef
    #@+node:ekr.20031218072017.3228:scanBodyForHeadline
    #@+at 
    #@nonl
    # This method returns the proper headline text.
    # 
    # 1. If s contains a section def, return the section ref.
    # 2. cweb only: if s contains @c, return the function name following the 
    # @c.
    # 3. cweb only: if s contains @d name, returns @d name.
    # 4. Otherwise, returns "@"
    #@-at
    #@@c

    def scanBodyForHeadline (self,s):

        if self.webType == "cweb":
            #@        << scan cweb body for headline >>
            #@+node:ekr.20031218072017.3229:<< scan cweb body for headline >>
            i = 0
            while i < len(s):
                i = g.skip_ws_and_nl(s,i)
                # line = g.get_line(s,i) ; g.trace(line)
                # Allow constructs such as @ @c, or @ @<.
                if self.isDocStart(s,i):
                    i += 2 ; i = g.skip_ws(s,i)
                if g.match(s,i,"@d") or g.match(s,i,"@f"):
                    # Look for a macro name.
                    directive = s[i:i+2]
                    i = g.skip_ws(s,i+2) # skip the @d or @f
                    if i < len(s) and g.is_c_id(s[i]):
                        j = i ; g.skip_c_id(s,i) ; return s[j:i]
                    else: return directive
                elif g.match(s,i,"@c") or g.match(s,i,"@p"):
                    # Look for a function def.
                    name = self.findFunctionDef(s,i+2)
                    return g.choose(name,name,"outer function")
                elif g.match(s,i,"@<"):
                    # Look for a section def.
                    # A small bug: the section def must end on this line.
                    j = i ; k = g.find_on_line(s,i,"@>")
                    if k > -1 and (g.match(s,k+2,"+=") or g.match(s,k+2,"=")):
                        return s[j:k+2] # return the section ref.
                i = g.skip_line(s,i)
            #@-node:ekr.20031218072017.3229:<< scan cweb body for headline >>
            #@nl
        else:
            #@        << scan noweb body for headline >>
            #@+node:ekr.20031218072017.3230:<< scan noweb body for headline >>
            i = 0
            while i < len(s):
                i = g.skip_ws_and_nl(s,i)
                # line = g.get_line(s,i) ; g.trace(line)
                if g.match(s,i,"<<"):
                    k = g.find_on_line(s,i,">>=")
                    if k > -1:
                        ref = s[i:k+2]
                        name = string.strip(s[i+2:k])
                        if name != "@others":
                            return ref
                else:
                    name = self.findFunctionDef(s,i)
                    if name:
                        return name
                i = g.skip_line(s,i)
            #@-node:ekr.20031218072017.3230:<< scan noweb body for headline >>
            #@nl
        return "@" # default.
    #@-node:ekr.20031218072017.3228:scanBodyForHeadline
    #@+node:ekr.20031218072017.3231:scanWebFile (handles limbo)
    def scanWebFile (self,fileName,parent):

        theType = self.webType
        lb = g.choose(theType=="cweb","@<","<<")
        rb = g.choose(theType=="cweb","@>",">>")

        try: # Read the file into s.
            f = open(fileName)
            s = f.read()
        except:
            g.es("Can not import " + fileName, color="blue")
            return

        #@    << Create a symbol table of all section names >>
        #@+node:ekr.20031218072017.3232:<< Create a symbol table of all section names >>
        i = 0 ; self.web_st = []

        while i < len(s):
            progress = i
            i = g.skip_ws_and_nl(s,i)
            # line = g.get_line(s,i) ; g.trace(line)
            if self.isDocStart(s,i):
                if theType == "cweb": i += 2
                else: i = g.skip_line(s,i)
            elif theType == "cweb" and g.match(s,i,"@@"):
                i += 2
            elif g.match(s,i,lb):
                i += 2 ; j = i ; k = g.find_on_line(s,j,rb)
                if k > -1: self.cstEnter(s[j:k])
            else: i += 1
            assert (i > progress)

        # g.trace(self.cstDump())
        #@-node:ekr.20031218072017.3232:<< Create a symbol table of all section names >>
        #@nl
        #@    << Create nodes for limbo text and the root section >>
        #@+node:ekr.20031218072017.3233:<< Create nodes for limbo text and the root section >>
        i = 0
        while i < len(s):
            progress = i
            i = g.skip_ws_and_nl(s,i)
            if self.isModuleStart(s,i) or g.match(s,i,lb):
                break
            else: i = g.skip_line(s,i)
            assert(i > progress)

        j = g.skip_ws(s,0)
        if j < i:
            self.createHeadline(parent,"@ " + s[j:i],"Limbo")

        j = i
        if g.match(s,i,lb):
            while i < len(s):
                progress = i
                i = g.skip_ws_and_nl(s,i)
                if self.isModuleStart(s,i):
                    break
                else: i = g.skip_line(s,i)
                assert(i > progress)
            self.createHeadline(parent,s[j:i],g.angleBrackets(" @ "))

        # g.trace(g.get_line(s,i))
        #@-node:ekr.20031218072017.3233:<< Create nodes for limbo text and the root section >>
        #@nl
        while i < len(s):
            outer_progress = i
            #@        << Create a node for the next module >>
            #@+node:ekr.20031218072017.3234:<< Create a node for the next module >>
            if theType=="cweb":
                assert(self.isModuleStart(s,i))
                start = i
                if self.isDocStart(s,i):
                    i += 2
                    while i < len(s):
                        progress = i
                        i = g.skip_ws_and_nl(s,i)
                        if self.isModuleStart(s,i): break
                        else: i = g.skip_line(s,i)
                        assert (i > progress)
                #@    << Handle cweb @d, @f, @c and @p directives >>
                #@+node:ekr.20031218072017.3235:<< Handle cweb @d, @f, @c and @p directives >>
                if g.match(s,i,"@d") or g.match(s,i,"@f"):
                    i += 2 ; i = g.skip_line(s,i)
                    # Place all @d and @f directives in the same node.
                    while i < len(s):
                        progress = i
                        i = g.skip_ws_and_nl(s,i)
                        if g.match(s,i,"@d") or g.match(s,i,"@f"): i = g.skip_line(s,i)
                        else: break
                        assert (i > progress)
                    i = g.skip_ws_and_nl(s,i)

                while i < len(s) and not self.isModuleStart(s,i):
                    progress = i
                    i = g.skip_line(s,i)
                    i = g.skip_ws_and_nl(s,i)
                    assert (i > progress)

                if g.match(s,i,"@c") or g.match(s,i,"@p"):
                    i += 2
                    while i < len(s):
                        progress = i
                        i = g.skip_line(s,i)
                        i = g.skip_ws_and_nl(s,i)
                        if self.isModuleStart(s,i):
                            break
                        assert (i > progress)
                #@-node:ekr.20031218072017.3235:<< Handle cweb @d, @f, @c and @p directives >>
                #@nl
            else:
                assert(self.isDocStart(s,i)) # isModuleStart == isDocStart for noweb.
                start = i ; i = g.skip_line(s,i)
                while i < len(s):
                    progress = i
                    i = g.skip_ws_and_nl(s,i)
                    if self.isDocStart(s,i): break
                    else: i = g.skip_line(s,i)
                    assert (i > progress)

            body = s[start:i]
            body = self.massageWebBody(body)
            headline = self.scanBodyForHeadline(body)
            self.createHeadline(parent,body,headline)
            #@-node:ekr.20031218072017.3234:<< Create a node for the next module >>
            #@nl
            assert(i > outer_progress)
    #@nonl
    #@-node:ekr.20031218072017.3231:scanWebFile (handles limbo)
    #@+node:ekr.20031218072017.3236:Symbol table
    #@+node:ekr.20031218072017.3237:cstCanonicalize
    # We canonicalize strings before looking them up, but strings are entered in the form they are first encountered.

    def cstCanonicalize (self,s,lower=True):

        if lower:
            s = string.lower(s)
        s = string.replace(s,"\t"," ")
        s = string.replace(s,"\r","")
        s = string.replace(s,"\n"," ")
        s = string.replace(s,"  "," ")
        s = string.strip(s)
        return s
    #@-node:ekr.20031218072017.3237:cstCanonicalize
    #@+node:ekr.20031218072017.3238:cstDump
    def cstDump (self):

        self.web_st.sort()
        s = "Web Symbol Table...\n\n"
        for name in self.web_st:
            s += name + "\n"
        return s
    #@-node:ekr.20031218072017.3238:cstDump
    #@+node:ekr.20031218072017.3239:cstEnter
    # We only enter the section name into the symbol table if the ... convention is not used.

    def cstEnter (self,s):

        # Don't enter names that end in "..."
        s = string.rstrip(s)
        if s.endswith("..."): return

        # Put the section name in the symbol table, retaining capitalization.
        lower = self.cstCanonicalize(s,True)  # do lower
        upper = self.cstCanonicalize(s,False) # don't lower.
        for name in self.web_st:
            if string.lower(name) == lower:
                return
        self.web_st.append(upper)
    #@-node:ekr.20031218072017.3239:cstEnter
    #@+node:ekr.20031218072017.3240:cstLookup
    # This method returns a string if the indicated string is a prefix of an entry in the web_st.

    def cstLookup (self,target):

        # Do nothing if the ... convention is not used.
        target = string.strip(target)
        if not target.endswith("..."): return target
        # Canonicalize the target name, and remove the trailing "..."
        ctarget = target[:-3]
        ctarget = self.cstCanonicalize(ctarget)
        ctarget = string.strip(ctarget)
        found = False ; result = target
        for s in self.web_st:
            cs = self.cstCanonicalize(s)
            if cs[:len(ctarget)] == ctarget:
                if found:
                    g.es("****** " + target + ": is also a prefix of: " + s)
                else:
                    found = True ; result = s
                    # g.es("replacing: " + target + " with: " + s)
        return result
    #@-node:ekr.20031218072017.3240:cstLookup
    #@-node:ekr.20031218072017.3236:Symbol table
    #@-node:ekr.20031218072017.3224:importWebCommand & allies
    #@+node:EKR.20040506075328.2:perfectImport
    def perfectImport (self,fileName,p,testing=False,verbose=False,convertBlankLines=True,verify=True):

        __pychecker__ = 'maxlines=500'

        #@    << about this algorithm >>
        #@+node:ekr.20040717112739:<< about this algorithm >>
        #@@nocolor
        #@+at
        # 
        # This algorithm corrects the result of an Import To @file command so 
        # that it is guaranteed that the result of writing the imported file 
        # will be identical to the original file except for any sentinels that 
        # have been inserted.
        # 
        # On entry, p points to the newly imported outline.
        # 
        # We correct the outline by applying Bernhard Mulder's algorithm.
        # 
        # 1.  We use the atFile.write code to write the newly imported outline 
        # to a string s.  This string contains represents a thin derived file, 
        # so it can be used to recreate then entire outline structure without 
        # any other information.
        # 
        # Splitting s into lines creates the fat_lines argument to mu methods.
        # 
        # 2. We make corrections to fat_lines using Mulder's algorithm.  The 
        # corrected fat_lines represents the corrected outline.  To do this, 
        # we set the arguments as follows:
        # 
        # - i_lines: fat_lines stripped of sentinels
        # - j_lines to the lines of the original imported file.
        # 
        # The algorithm updates fat_lines using diffs between i_lines and 
        # j_lines.
        # 
        # 3. Mulder's algorithm doesn't specify which nodes have been 
        # changed.  In fact, it Mulder's algorithm doesn't really understand 
        # nodes at all.  Therefore, if we want to mark changed nodes we do so 
        # by comparing the original version of the imported outline with the 
        # corrected version of the outline.
        #@-at
        #@-node:ekr.20040717112739:<< about this algorithm >>
        #@nl
        c = self.c
        root = p.copy()
        at = c.atFileCommands
        if testing:
            #@        << clear all dirty bits >>
            #@+node:ekr.20040716065356:<< clear all dirty bits >>
            for p2 in p.self_and_subtree_iter():
                p2.clearDirty()
            #@-node:ekr.20040716065356:<< clear all dirty bits >>
            #@nl
        #@    << Assign file indices >>
        #@+node:ekr.20040716064333:<< Assign file indices  >>
        nodeIndices = g.app.nodeIndices

        nodeIndices.setTimestamp()

        for p2 in root.self_and_subtree_iter():
            try: # Will fail for None or any pre 4.1 file index.
                theId,time,n = p2.v.t.fileIndex
            except TypeError:
                p2.v.t.fileIndex = nodeIndices.getNewIndex()
        #@-node:ekr.20040716064333:<< Assign file indices  >>
        #@nl
        #@    << Write root's tree to to string s >>
        #@+node:ekr.20040716064333.1:<< Write root's tree to to string s >>
        at.write(root,thinFile=True,toString=True)
        s = at.stringOutput
        if not s: return
        #@-node:ekr.20040716064333.1:<< Write root's tree to to string s >>
        #@nl

        # Set up the data for the algorithm.
        mu = g.mulderUpdateAlgorithm(testing=testing,verbose=verbose)
        delims = g.comment_delims_from_extension(fileName)
        fat_lines = g.splitLines(s) # Keep the line endings.
        i_lines,mapping = mu.create_mapping(fat_lines,delims)
        j_lines = file(fileName).readlines()

        # Correct write_lines using the algorihm.
        if i_lines != j_lines:
            if verbose:
                g.es("Running Perfect Import",color="blue")
            write_lines = mu.propagateDiffsToSentinelsLines(i_lines,j_lines,fat_lines,mapping)
            if 1: # For testing.
                #@            << put the corrected fat lines in a new node >>
                #@+node:ekr.20040717132539:<< put the corrected fat lines in a new node >>
                write_lines_node = root.insertAfter()
                write_lines_node.initHeadString("write_lines")
                s = ''.join(write_lines)
                write_lines_node.scriptSetBodyString(s,encoding=g.app.tkEncoding)
                #@-node:ekr.20040717132539:<< put the corrected fat lines in a new node >>
                #@nl
            #@        << correct root's tree using write_lines >>
            #@+node:ekr.20040717113036:<< correct root's tree using write_lines >>
            #@+at 
            #@nonl
            # Notes:
            # 1. This code must overwrite the newly-imported tree because the 
            # gnx's in
            # write_lines refer to those nodes.
            # 
            # 2. The code in readEndNode now reports when nodes change during 
            # importing. This
            # code also marks changed nodes.
            #@-at
            #@@c

            try:
                at.correctedLines = 0
                at.targetFileName = "<perfectImport string-file>"
                at.inputFile = fo = g.fileLikeObject()
                at.file = fo # Strange, that this is needed.  Should be cleaned up.
                for line in write_lines:
                    fo.write(line)
                firstLines,junk,junk = c.atFileCommands.scanHeader(fo,at.targetFileName)
                # To do: pass params to readEndNode.
                at.readOpenFile(root,fo,firstLines,perfectImportRoot=root)
                n = at.correctedLines
                if verbose:
                    g.es("%d marked node%s corrected" % (n,g.choose(n==1,'','s')),color="blue")
            except:
                g.es("Exception in Perfect Import",color="red")
                g.es_exception()
                s = None
            #@-node:ekr.20040717113036:<< correct root's tree using write_lines >>
            #@nl
        if verify:
            #@        << verify that writing the tree would produce the original file >>
            #@+node:ekr.20040718035658:<< verify that writing the tree would produce the original file >>
            try:
                # Read the original file into before_lines.
                before = file(fileName)
                before_lines = before.readlines()
                before.close()

                # Write the tree into after_lines.
                at.write(root,thinFile=True,toString=True)
                after_lines1 = g.splitLines(at.stringOutput)

                # Strip sentinels from after_lines and compare.
                after_lines = mu.removeSentinelsFromLines(after_lines1,delims)

                # A major kludge: Leo can not represent unindented blank lines in indented nodes!
                # We ignore the problem here by stripping whitespace from blank lines.
                # We shall need output options to handle such lines.
                if convertBlankLines:
                    mu.stripWhitespaceFromBlankLines(before_lines)
                    mu.stripWhitespaceFromBlankLines(after_lines)
                if before_lines == after_lines:
                    if verbose:
                        g.es("Perfect Import verified",color="blue")
                else:
                    leoTest.fail()
                    if verbose:
                        g.es("Perfect Import failed verification test!",color="red")
                        #@            << dump the files >>
                        #@+node:ekr.20040718045423:<< dump the files >>
                        print len(before_lines),len(after_lines)

                        if len(before_lines)==len(after_lines):
                            for i in xrange(len(before_lines)):
                                extra = 3
                                if before_lines[i] != after_lines[i]:
                                    j = max(0,i-extra)
                                    print '-' * 20
                                    while j < i + extra + 1:
                                        leader = g.choose(i == j,"* ","  ")
                                        print "%s%3d" % (leader,j), repr(before_lines[j])
                                        print "%s%3d" % (leader,j), repr(after_lines[j])
                                        j += 1
                        else:
                            for i in xrange(min(len(before_lines),len(after_lines))):
                                if before_lines[i] != after_lines[i]:
                                    extra = 5
                                    print "first mismatch at line %d" % i
                                    print "printing %d lines after mismatch" % extra
                                    print "before..."
                                    for j in xrange(i+1+extra):
                                        print "%3d" % j, repr(before_lines[j])
                                    print
                                    print "after..."
                                    for k in xrange(1+extra):
                                        print "%3d" % (i+k), repr(after_lines[i+k])
                                    print
                                    print "with sentinels"
                                    j = 0 ; k = 0
                                    while k < i + 1 + extra:
                                        print "%3d" % k,repr(after_lines1[j])
                                        if not g.is_sentinel(after_lines1[j],delims):
                                            k += 1
                                        j += 1
                                    break
                        #@-node:ekr.20040718045423:<< dump the files >>
                        #@nl
            except IOError:
                g.es("Can not reopen %s!" % fileName,color="red")
                leoTest.fail()
            #@-node:ekr.20040718035658:<< verify that writing the tree would produce the original file >>
            #@nl
    #@-node:EKR.20040506075328.2:perfectImport
    #@+node:ekr.20031218072017.3241:Scanners for createOutline
    #@+node:ekr.20070703122141.65:class baseScannerClass
    class baseScannerClass:

        '''
        The base class for all import scanner classes.
        This class contains common utility methods.
        '''

        #@    @+others
        #@+node:ekr.20070703122141.66:baseScannerClass.__init__
        def __init__ (self,importCommands,atAuto,language,strict):

            # Copy arguments.
            self.atAuto = atAuto
            self.language = language
            self.strict = strict

            # Copy ivars from the importCommands class.
            self.importCommands = ic = importCommands
            self.c = ic.c
            self.encoding = ic.encoding
            self.fileName = ic.fileName
            self.fileType = ic.fileType
            # self._forcedGnxPositionList = []
            self.methodName = ic.methodName
            self.output_newline = ic.output_newline
            self.root = None # The top-level node of the generated tree.
            self.rootLine = ic.rootLine
            self.tab_width = ic.getTabWidth()
            self.treeType = ic.treeType
            # self.web_st = []
            self.webType = ic.webType

            # Compute language ivars.
            delim1,delim2,delim3 = g.set_delims_from_language(language)
            self.comment_delim = delim1

            # Create the ws equivalent to one tab.
            if self.tab_width < 0:
                self.tab_ws = ' '*abs(self.tab_width)
            else:
                self.tab_ws = '\t'

            # For communication between scan and startsClass/Function...
            self.end = None
                # If not none, what scanClass/Function would return.
                # This allows startsClass/Function to do all the work.
            self.sigEnd = None

            # May be overridden in subclasses.
            self.lineCommentDelim = None
            self.blockCommentDelim1 = None
            self.blockCommentDelim2 = None

        #@-node:ekr.20070703122141.66:baseScannerClass.__init__
        #@+node:ekr.20070707072749:run
        def run (self,s,parent):

            scanner = self
            scanner.root = parent
            scanner.file_s = s

            # Step 1: generate the nodes,
            # including all directive and section references.
            scanner.scan(s,parent)

            # Step 2: check the generated nodes.
            # Return True if the result is equivalent to the original file.
            ok = scanner.check(parent)

            # Step 3: insert an @ignore directive if there are any problems.
            if not ok:
                scanner.insertIgnoreDirectives(parent)
        #@-node:ekr.20070707072749:run
        #@+node:ekr.20070703122141.102:check & helpers
        def check (self,parent):

            '''
            Make sure the generated nodes are equivalent to the original file.

            1. Regularize and check leading whitespace.
            2. Check that a trial write produces the original file.

            Return True if the nodes are equivalent to the original file.
            '''

            return self.checkWhitespace(parent) and self.checkTrialWrite()
        #@+node:ekr.20070705085126:checkTab
        # Similar to c.tabNannyNode

        def checkTab (self,p):

            """Check indentation using tabnanny."""

            h = p.headString() ; body = p.bodyString()

            try:
                readline = g.readLinesClass(body).next
                tabnanny.process_tokens(tokenize.generate_tokens(readline))
                return True

            except IndentationError, err:
                # Instances of this class have attributes filename, lineno, offset and text.
                g.es_print("IndentationError in %s at line %d" % (h,err.lineno),color="blue")
                # g.es_print(str(err)) # str(err.text))

            except parser.ParserError, msg:
                g.es_print("ParserError in %s" % h,color="blue")
                g.es_print(str(msg))

            except tokenize.TokenError, msg:
                g.es_print("TokenError in %s" % h,color="blue")
                g.es_print(str(msg))

            except tabnanny.NannyNag, nag:
                badline = nag.get_lineno()
                line    = nag.get_line()
                message = nag.get_msg()
                g.es_print("Indentation error in %s, line %d" % (h, badline),color="blue")
                g.es_print(message)
                g.es_print("offending line:\n%s" % repr(str(line))[1:-1])

            except:
                g.trace("unexpected exception")
                g.es_exception()

            return False
        #@-node:ekr.20070705085126:checkTab
        #@+node:ekr.20070703122141.103:checkWhitespace
        def checkWhitespace(self,parent):

            '''Check and normalize the leading whitespace of all nodes.

            - The original sources may fail Python's tabNanny checks.  

            - Leading whitespace in the original sources may be inconsistent with the
              @tabwidth setting in effect in the @auto tree.

            - The original sources may contain underindented comments. 

            If an indentation problem is found, issue a warning and return False.
            Otherwise, normalize the indentation of all pieces so that it is indeed
            consistent with the indentation specified by the present @tabwidth setting.
            Normalizing underindented comments means shifting the comments right.
            '''

            # Check that whitespace passes TabNanny.
            # Check that whitespace is compatible with @tabwidth.
            # Check for underindented lines.
            g.trace(self.tab_width)
            ok = True
            for p in parent.self_and_subtree_iter():
                ok = ok and self.checkTab(p)
            return ok
        #@nonl
        #@-node:ekr.20070703122141.103:checkWhitespace
        #@+node:ekr.20070703122141.104:checkTrialWrite
        def checkTrialWrite (self):

            '''Return True if a trial write produces the original file.'''

            c = self.c ; at = c.atFileCommands

            at.write(self.root,
                nosentinels=True,thinFile=False,
                scriptWrite=False,toString=True,
                write_strips_blank_lines=False,
            )
            s1 = self.file_s
            s2 = at.stringOutput
            ok = s1 == s2
            if ok:
                g.es_print('@auto ***success***')
            else:
                g.es_print('@auto ***failure***')
                lines1 = g.splitLines(s1)
                lines2 = g.splitLines(s2)
                if not self.strict: # ignore blank lines.
                    lines1 = [z for z in lines1 if z.strip()]
                    lines2 = [z for z in lines2 if z.strip()]
                if len(lines1) != len(lines2):
                    g.trace('***different number of lines:',
                        'lines1',len(lines1),'lines2',len(lines2))
                g.trace('***mismatch',
                    'len(s1)',len(s1),'len(s2)',len(s2))
                n = min(len(lines1),len(lines2))
                for i in xrange(n):
                    if lines1[i] != lines2[i]:
                        print 'first mismatch at line %d' % (i)
                        print 'original line: ', repr(lines1[i])
                        print 'generated line:', repr(lines2[i])
                        break
                else:
                    if len(lines2) < len(lines1):
                         print 'missing lines'
                         i = n
                         while i < len(lines1):
                             print repr(lines1[i])
                             i += 1
                    else:
                        print 'extra lines'
                        i = n
                        while i < len(lines2):
                            print repr(lines1[2])
                            i += 1
                if 0:
                    print
                    for i in xrange(len(lines2)):
                        print '%3d: %s' % (i,repr(lines2[i]))
            return ok
        #@-node:ekr.20070703122141.104:checkTrialWrite
        #@-node:ekr.20070703122141.102:check & helpers
        #@+node:ekr.20070707071124:utils
        #@+node:ekr.20070703122141.78:error & scanError
        def error (self,s):
            g.es_print(s,color='red')

        scanError = error
        #@nonl
        #@-node:ekr.20070703122141.78:error & scanError
        #@+node:ekr.20070703122141.79:getLeadingIndent
        def getLeadingIndent (self,s,i):

            """Return the leading whitespace of a line, ignoring blank and comment lines."""

            width = 0 ; i = g.find_line_start(s,i)
            while i < len(s):
                # g.trace(g.get_line(s,i))
                j = g.skip_ws(s,i)
                if g.is_nl(s,j) or g.match(s,j,self.comment_delim):
                    i = g.skip_line(s,i) # ignore blank lines and comment lines.
                else:
                    i, width = g.skip_leading_ws_with_indent(s,i,self.tab_width)
                    break

            # g.trace("returns:",width)
            return width
        #@-node:ekr.20070703122141.79:getLeadingIndent
        #@+node:ekr.20070703122141.80:isDocStart and isModuleStart
        # The start of a document part or module in a noweb or cweb file.
        # Exporters may have to test for @doc as well.

        def isDocStart (self,s,i):

            if not g.match(s,i,"@"):
                return False

            j = g.skip_ws(s,i+1)
            if g.match(s,j,"%defs"):
                return False
            elif self.webType == "cweb" and g.match(s,i,"@*"):
                return True
            else:
                return g.match(s,i,"@ ") or g.match(s,i,"@\t") or g.match(s,i,"@\n")

        def isModuleStart (self,s,i):

            if self.isDocStart(s,i):
                return True
            else:
                return self.webType == "cweb" and (
                    g.match(s,i,"@c") or g.match(s,i,"@p") or
                    g.match(s,i,"@d") or g.match(s,i,"@f"))
        #@-node:ekr.20070703122141.80:isDocStart and isModuleStart
        #@+node:ekr.20070707073627:oops
        def oops (self):
            print ("baseScannerClass oops:",
                g.callers(),
                "must be overridden in subclass")
        #@-node:ekr.20070707073627:oops
        #@+node:ekr.20070703122141.82:setEncoding
        def setEncoding (self):

            # scanDirectives checks the encoding: may return None.
            theDict = g.scanDirectives(self.c)
            encoding = theDict.get("encoding")
            if encoding and g.isValidEncoding(encoding):
                self.encoding = encoding
            else:
                self.encoding = g.app.tkEncoding # 2/25/03

            # print self.encoding
        #@-node:ekr.20070703122141.82:setEncoding
        #@-node:ekr.20070707071124:utils
        #@+node:ekr.20070706084535.1:Parsing
        #@+node:ekr.20070707075646:Must be defined in base class
        #@+node:ekr.20070706101600:scan & helper
        def scan (self,s,parent):

            '''A language independent scanner: it uses language-specific helpers.

            Create a child of self.root for:
            - Leading outer-level declarations.
            - Outer-level classes.
            - Outer-level functions.
            '''
            i = start = self.skipDecls(s,0,len(s))
            decls = s[:i]
            if decls: self.createDeclsNode(parent,decls)
            needRef = False
            while i < len(s):
                progress = i
                if g.match(s,i,self.lineCommentDelim):
                    i = g.skip_line(s,i)
                elif g.match(s,i,self.blockCommentDelim1):
                    i = self.skipBlockComment(s,i)
                elif self.startsString(s,i):
                    i = self.skipString(s,i)
                elif self.startsClass(s,i):
                    end2 = self.skipClass(s,i)
                    self.putClass(s,i,end2,start,parent)
                    i = start = end2
                    needRef = True
                elif self.startsFunction(s,i):
                    end2 = self.skipFunction(s,i)
                    self.putFunction(s,i,end2,start,parent)
                    i = start = end2
                elif self.startsId(s,i):
                    i = self.skipId(s,i);
                else: i += 1
                assert(progress < i)
            self.addRef(parent)
        #@+node:ekr.20070707073044.1:addRef
        def addRef (self,parent):

            '''Create an unindented the @others or section reference in the parent node.'''

            c = self.c

            if self.treeType == "@file":
                c.appendStringToBody(parent,"@others\n")

            if self.treeType == "@root" and self.methodsSeen:
                c.appendStringToBody(parent,
                    g.angleBrackets(" " + self.methodName + " methods ") + "\n\n")
        #@-node:ekr.20070707073044.1:addRef
        #@-node:ekr.20070706101600:scan & helper
        #@+node:ekr.20070707080042:skipDecls & helper
        def skipDecls (self,s,i,end):

            '''
            Carefully skip everything until the start of the next class or function.
            '''

            while i < end:
                progress = i
                if g.match(s,i,self.lineCommentDelim):
                    i = g.skip_line(s,i)
                elif g.match(s,i,self.blockCommentDelim1):
                    i = self.skipBlockComment(s,i)
                elif self.startsString(s,i):
                    i = self.skipString(s,i)
                elif self.startsClass(s,i):
                    # Important: do not include leading ws in the decls.
                    i = self.adjustClassOrFunctionStart(s,i,'class')
                    break
                elif self.startsFunction(s,i):
                    # Important: do not include leading ws in the decls.
                    i = self.adjustClassOrFunctionStart(s,i,'function')
                    break
                elif self.startsId(s,i):
                    i = self.skipId(s,i);
                else: i += 1
                assert(progress < i)

            return min(i,end)
        #@+node:ekr.20070709084313:adjustClassOrFunctionStart
        def adjustClassOrFunctionStart(self,s,i,tag):

            '''
            s[i:] starts a class or function.
            Adjust i so it points at the start of the line.

            Issue a warning if anything except whitespace appears.
            '''

            j = g.find_line_start(s,i)
            if s[j:i].strip():
                message = '% definition does not start a line. Leo must insert a newline.' % tag
                self.error(message)
                return i
            else:
                return j
        #@-node:ekr.20070709084313:adjustClassOrFunctionStart
        #@-node:ekr.20070707080042:skipDecls & helper
        #@-node:ekr.20070707075646:Must be defined in base class
        #@+node:ekr.20070707075646.1:May be defined in subclasses
        #@+node:ekr.20070707150022:extendSignature
        def extendSignature(self,s,i,start):

            '''
            Extend the signature line if appropriate.
            The text *must* end with a newline.

            For example, the Python scanner appends docstrings if they exist.
            '''

            return i
        #@-node:ekr.20070707150022:extendSignature
        #@+node:ekr.20070707073859:skipBlock
        def skipBlock(self,s,i,delim1='{',delim2='}'):

            """Skips from the opening delim to the matching closing delim.

            If no matching is found i is set to len(s)"""

            # start = g.get_line(s,i)
            assert g.match(s,i,delim1)
            level = 0 ; n = len(s)
            while i < n:
                c = s[i]
                if c == delim1:
                    level += 1 ; i += 1
                elif c == delim2:
                    level -= 1 ; i += 1
                    if level <= 0: return i
                elif g.match(s,i,self.lineCommentDelim):
                    i = g.skip_line(s,i)
                elif g.match(s,i,self.blockCommentDelim1):
                    i = self.skipBlockComment(s,i)
                elif self.startsString(s,i):
                    i = self.skipString(s,i)
                # Only for C++.
                # elif g.match_word(s,i,"#if") or g.match_word(s,i,"#ifdef") or g.match_word(s,i,"#ifndef"):
                    # i,delta = g.skip_pp_if(s,i)
                    # level += delta
                else: i += 1
            return i
        #@-node:ekr.20070707073859:skipBlock
        #@+node:ekr.20070707074541:skipBlockComment
        def skipBlockComment (self,s,i):

            '''Skip past a block comment.'''

            # Skip the opening delim.
            assert(g.match(s,i,self.blockCommentDelim1))
            start = i ; i += len(self.blockCommentDelim1)

            # Find the closing delim.
            k = string.find(s,self.blockCommentDelim2,i)
            if k == -1:
                self.scanError("Run on block comment: " + s[start:i])
                return len(s)
            else:
                return k + len(self.blockCommentDelim2)
        #@-node:ekr.20070707074541:skipBlockComment
        #@+node:edreamleo.20070710105410:skipClass/Function/Signature
        # startsClass and startsFunction must do all the work anyway,
        # so they set the ending points and we just return it.

        def skipClass (self,s,i):
            return self.end

        def skipFunction (self,s,i):
            return self.end

        def skipSignature (self,s,i):
            return self.sigEnd
        #@-node:edreamleo.20070710105410:skipClass/Function/Signature
        #@+node:ekr.20070707094858.1:skipId
        def skipId (self,s,i):

            return g.skip_c_id(s,i)
        #@-node:ekr.20070707094858.1:skipId
        #@+node:ekr.20070707073627.2:skipString
        def skipString (self,s,i):

            # Returns len(s) on unterminated string.
            return g.skip_string(s,i,verbose=False)
        #@-node:ekr.20070707073627.2:skipString
        #@+node:ekr.20070707094858.2:startsId
        def startsId(self,s,i):

            return g.is_c_id(s[i])
        #@-node:ekr.20070707094858.2:startsId
        #@+node:ekr.20070707172732.1:startsString
        def startsString(self,s,i):

            return g.match(s,i,'"') or g.match(s,i,"'")
        #@-node:ekr.20070707172732.1:startsString
        #@-node:ekr.20070707075646.1:May be defined in subclasses
        #@+node:ekr.20070707073627.3:Must be defined in subclasses
        def putClass (self,s,i,end,start,parent):
            self.oops()

        def putFunction (self,s,i,end,start,parent):
            self.oops()

        def skipClass (self,s,i):
            self.oops()

        def skipFunction (self,s,i):
            self.oops()

        def skipSignature (self,s,i):
            self.oops()

        def startsClass (self,s,i):
            self.oops()

        def startsFunction (self,s,i):
            self.oops()
        #@-node:ekr.20070707073627.3:Must be defined in subclasses
        #@-node:ekr.20070706084535.1:Parsing
        #@+node:ekr.20070706084535:Semantics (must be defined in base class)
        #@+node:ekr.20070705144309:createDeclsNode
        def createDeclsNode (self,parent,s):

            '''Create a child node of parent containing s.'''

            # Create the node for the decls.
            headline = self.methodName + ' declarations'
            body = self.undentBody(s)
            self.createHeadline(parent,body,headline)
        #@-node:ekr.20070705144309:createDeclsNode
        #@+node:ekr.20070707085612:createFunctionNode
        def createFunctionNode (self,headline,body,parent):

            # Create the prefix line for @root trees.
            if self.treeType == "@file":
                prefix = ""
            else:
                prefix = g.angleBrackets(" " + headline + " methods ") + "=\n\n"
                self.methodsSeen = True

            body = self.undentBody(body)

            # Create the node.
            self.createHeadline(parent,prefix + body,headline)

        #@-node:ekr.20070707085612:createFunctionNode
        #@+node:ekr.20070703122141.77:createHeadline
        def createHeadline (self,parent,body,headline):

            # g.trace("parent,headline:",parent,headline)

            # Create the vnode.
            p = parent.insertAsLastChild()
            p.initHeadString(headline,self.encoding)

            # Set the body.
            if body:
                self.c.setBodyString(p,body,self.encoding)
            return p
        #@-node:ekr.20070703122141.77:createHeadline
        #@+node:ekr.20070705085335:insertIgnoreDirectives
        def insertIgnoreDirectives (self,parent):

            g.trace(parent)
        #@-node:ekr.20070705085335:insertIgnoreDirectives
        #@+node:ekr.20070703122141.81:massageComment
        def massageComment (self,s):

            """Returns s with all runs of whitespace and newlines converted to a single blank.

            Also removes leading and trailing whitespace."""

            s = s.strip()
            s = s.replace("\n"," ")
            s = s.replace("\r"," ")
            s = s.replace("\t"," ")
            s = s.replace("  "," ")
            s = s.strip()
            return s
        #@-node:ekr.20070703122141.81:massageComment
        #@+node:ekr.20070707113832.1:putClass & helpers
        def putClass (self,s,i,end,start,parent):

            """Creates a child node c of parent for the class, and children of c for each def in the class."""

            # g.trace('start',start,'i',i,g.get_line(s,i))
            c = self.c
            classStart = g.find_line_start(s,i)
            prefix = self.createClassNodePrefix()

            i = self.skipSignature(s,i)
            if not self.sigID:
                g.trace('Can not happen: no sigID')
                sigID = 'Unknown class name'
            class_name = self.sigID # May be set in skipSignature.
            headline = "class " + class_name
            body = s[start:i]
            body = self.undentBody(body)
            j = i ; i = self.extendSignature(s,i)
            extend = s[j:i]
            if extend:
                extend = self.undentBody(extend)
                extend = self.indentBody(extend)
                body = body + extend

            class_node = self.createHeadline(parent,prefix + body,headline)

            savedMethodName = self.methodName
            self.methodName = headline

            self.putClassHelper(s,i,end,class_name,class_node)
            self.methodName = savedMethodName
        #@+node:ekr.20070703122141.106:appendRefToClassNode
        def appendRefToClassNode (self,class_name,class_node):

            '''Insert the proper body text in the class_vnode.'''

            if self.treeType == "@file":
                s = '@others'
            else:
                s = g.angleBrackets(' class %s methods ' % (class_name))

            self.appendTextToClassNode(class_node,'%s%s\n' % (self.tab_ws,s))
        #@-node:ekr.20070703122141.106:appendRefToClassNode
        #@+node:ekr.20070707190351:appendTextToClassNode
        def appendTextToClassNode (self,class_node,s):

            c = self.c
            c.appendStringToBody(class_node,s) 
        #@-node:ekr.20070707190351:appendTextToClassNode
        #@+node:ekr.20070703122141.105:createClassNodePrefix
        def createClassNodePrefix (self):

            '''Create the class node prefix.'''

            if  self.treeType == "@file":
                prefix = ""
            else:
                prefix = g.angleBrackets(" " + self.methodName + " methods ") + "=\n\n"
                self.methodsSeen = True

            return prefix
        #@-node:ekr.20070703122141.105:createClassNodePrefix
        #@+node:ekr.20070707171329:putClassHelper
        def putClassHelper(self,s,i,end,class_name,class_node):

            assert(i <= end)
            # Put any leading decls in the class node.
            start = i
            i = self.skipDecls(s,i,end)
            decls = s[start:i]
            if decls:
                # We must regularize the indentation to match the @others
                decls = self.undentBody(decls)
                decls = self.indentBody(decls)
                # g.trace(class_name,'decls',repr(decls))
                self.appendTextToClassNode(class_node,decls)
            start = i ; putRef = False
            while i < end:
                progress = i
                if g.match(s,i,self.lineCommentDelim):
                    i = g.skip_line(s,i)
                elif g.match(s,i,self.blockCommentDelim1):
                    i = self.skipBlockComment(s,i)
                elif self.startsString(s,i):
                    i = self.skipString(s,i)
                elif self.startsClass(s,i):
                    putRef = True
                    end2 = self.skipClass(s,i)
                    self.putClass(s,i,end2,start,class_node)
                    i = start = end2
                elif self.startsFunction(s,i):
                    putRef = True
                    end2 = self.skipFunction(s,i)
                    self.putFunction(s,i,end2,start,class_node)
                    i = start = end2
                elif self.startsId(s,i):
                    i = self.skipId(s,i);
                else: i += 1
                assert(progress < i)

            if putRef:
                self.appendRefToClassNode(class_name,class_node)

            if start < end:
                trailing = s[start:end]
                self.appendTextToClassNode(class_node,trailing)
        #@-node:ekr.20070707171329:putClassHelper
        #@-node:ekr.20070707113832.1:putClass & helpers
        #@+node:ekr.20070707082432:putFunction
        def putFunction (self,s,i,end,start,parent):

            '''
            Create a node of parent for a function defintion.
            '''

            if self.sigID:
                headline = self.sigID
            else:
                g.trace('Can not happen: no sigID')
                headline = 'unknown function'
            body = s[start:end]
            self.createFunctionNode(headline,body,parent)
        #@-node:ekr.20070707082432:putFunction
        #@+node:ekr.20070705094630:putRootText
        def putRootText (self,p):

            c = self.c

            if self.atAuto:
                c.appendStringToBody(p,self.rootLine + '@language python\n')
            else:
                c.appendStringToBody(p,'@ignore\n' + self.rootLine + '@language python\n')
        #@-node:ekr.20070705094630:putRootText
        #@+node:ekr.20070703122141.88:undentBody
        def undentBody (self,s):

            '''Remove the leading indentation of line 1 from all lines of s.'''

            i = 0 ; result = ''

            # Copy an @code line as is.
            if g.match(s,i,"@code"):
                j = i ; i = g.skip_line(s,i) # don't use get_line: it is only for dumping.
                result += s[j:i]

            # Calculate the amount to be removed from each line.
            undent = self.getLeadingIndent(s,i)
            if undent == 0: return s

            result = []
            for line in g.splitLines(s):
                line = g.removeLeadingWhitespace(line,undent,self.tab_width)
                result.append(line)
            return ''.join(result)
        #@-node:ekr.20070703122141.88:undentBody
        #@+node:ekr.20070709094002:indentBody
        def indentBody (self,s,lws=None):

            '''Add whitespace equivalent to one tab for all non-blank lines of s.'''

            result = []
            if not lws: lws = self.tab_ws

            for line in g.splitLines(s):
                if line.strip():
                    result.append(lws + line)
                elif line.endswith('\n'):
                    result.append('\n')

            return ''.join(result)
        #@-node:ekr.20070709094002:indentBody
        #@-node:ekr.20070706084535:Semantics (must be defined in base class)
        #@-others
    #@-node:ekr.20070703122141.65:class baseScannerClass
    #@+node:ekr.20070703123618.2:Python tests
    #@+node:ekr.20070703181153:@mark-for-unit-tests @auto tests
    #@+node:ekr.20070703122141.128:@test scanPythonText
    if g.unitTesting:

        ic = c.importCommands
        c,p = g.getTestVars()

        if 1:
            fileName = g.os_path_abspath(g.os_path_join(g.app.loadDir,'leoTest.py'))
            # print '@test scanPythonText: path',path
            f = file(fileName)
            s = f.read()
            f.close()
        else:
            s = '''\
    def spam():
        pass
    '''

        # Duplicate processing in ic command
        junk,ic.fileName = g.os_path_split(fileName)
        ic.methodName,ic.fileType = g.os_path_splitext(ic.fileName)
        ic.setEncoding()

        ic.scanPythonText (s=s,parent=p.copy(),atAuto=True)

        if 1:
            nodes = [z for z in p.subtree_iter()]
            print 'Generated tree has %d nodes' % len(nodes)
        else:
            g.trace('***** generated tree...')
            for z in p.subtree_iter():
                print '.'*z.level(),z.headString()
    #@-node:ekr.20070703122141.128:@test scanPythonText
    #@-node:ekr.20070703181153:@mark-for-unit-tests @auto tests
    #@+node:ekr.20070703181153.1:Not ready
    #@+node:ekr.20070703123618.3:@@test skipPythonDef
    if g.unitTesting:

        c,p = g.getTestVars()
        self = c.importCommands
        scanner = pythonScanner(self,atAuto)

        # global c # Get syntax warning if this is not first.
        # if self: c = self.c             # Run from @test node: c not global
        # else: self = c.importCommands   # Run from @suite: c *is* global
        d = g.scanDirectives(c)
        self.tab_width = d.get("tabwidth")
        verbose = False
        #@    << define s >>
        #@+node:ekr.20070703123618.4:<< define s >>
        s = '''\
        def test1():
            aList = (a,
        b,c)
        # underindented comment.
            return 1

        def test2():
        # underindented comment.
            pass
        '''

        s = g.adjustTripleString(s,self.tab_width)
        #@-node:ekr.20070703123618.4:<< define s >>
        #@nl
        start = 0
        i = self.skipPythonDef(s,i=0,start=start)
        result = s[start:i].strip()
        if verbose: g.trace(result)
        assert result.startswith('def test1') and result.endswith('return 1'),'result:\n%s' % result
        start = i
        i = self.skipPythonDef(s,i=i,start=start)
        result = s[start:i].strip()
        if verbose: g.trace(result)
        assert result.startswith('def test2') and result.endswith('pass'),'result:\n%s' % result
    #@-node:ekr.20070703123618.3:@@test skipPythonDef
    #@+node:ekr.20070703123618.5:@@test skipPythonDef (long lines)
    if g.unitTesting:

        c,p = g.getTestVars()
        self = c.importCommands
        scanner = pythonScanner(self,atAuto)

        # global c # Get syntax warning if this is not first.
        # if self: c = self.c             # Run from @test node: c not global
        # else: self = c.importCommands   # Run from @suite: c *is* global

        d = g.scanDirectives(c)
        self.tab_width = d.get("tabwidth")
        verbose = False
        #@    << define s >>
        #@+node:ekr.20070703123618.6:<< define s >>
        s = '''\
        def test1(
                a=2):
            return 1

        def test2(
        a=3):
            return 2
        '''

        s = g.adjustTripleString(s,self.tab_width)
        #@-node:ekr.20070703123618.6:<< define s >>
        #@nl
        start = 0
        i = self.skipPythonDef(s,i=0,start=start)
        result = s[start:i].strip()
        if verbose: g.trace(result)
        assert result.startswith('def test1') and result.endswith('return 1'),'result:\n%s' % result
        start = i
        i = self.skipPythonDef(s,i=i,start=start)
        result = s[start:i].strip()
        if verbose: g.trace(result)
        assert result.startswith('def test2') and result.endswith('return 2'),'result:\n%s' % result
    #@-node:ekr.20070703123618.5:@@test skipPythonDef (long lines)
    #@+node:ekr.20070703123618.7:@@test scanPythonClass
    if g.unitTesting:

        c,p = g.getTestVars()
        self = c.importCommands
        scanner = pythonScanner(self,atAuto)

        # global c # Get syntax warning if this is not first.
        # if self: c = self.c             # Run from @test node: c not global
        # else: self = c.importCommands   # Run from @suite: c *is* global

        d = g.scanDirectives(c)
        self.tab_width = d.get("tabwidth")
        verbose = False
        #@    << define s >>
        #@+node:ekr.20070703123618.8:<< define s >>
        s = '''\
        class aClass:
            def spam():
                return 'spam'
        # underindented comment line
            def eggs():
                return 'eggs'

        class aClass2:
            def twit():
                return 'twit'
        '''

        s = g.adjustTripleString(s,self.tab_width)
        #@-node:ekr.20070703123618.8:<< define s >>
        #@nl
        start = 0
        i = self.skipPythonDef(s,i=0,start=start)
        result = s[start:i].strip()
        if verbose: g.trace(result)
        assert result.startswith('class aClass') and result.endswith("'eggs'"),'result:\n%s' % result
        start = i
        i = self.skipPythonDef(s,i=i,start=start)
        result = s[start:i].strip()
        if verbose: g.trace(result)
        assert result.startswith('class aClass2') and result.endswith("'twit'"),'result:\n%s' % result
    #@-node:ekr.20070703123618.7:@@test scanPythonClass
    #@-node:ekr.20070703181153.1:Not ready
    #@-node:ekr.20070703123618.2:Python tests
    #@+node:ekr.20070703123618:Unchanged scanners
    #@+node:ekr.20031218072017.3265:scanElispText & allies
    def scanElispText(self,s,p):

        c = self.c
        c.appendStringToBody(p,"@ignore\n@language elisp\n")
        i = 0 ; start = 0
        while i < len(s):
            progress = i
            ch = s[i] ; # g.trace(g.get_line(s,i))
            if ch == ';':
                i = g.skip_line(s,i)
            elif ch == '(':
                j = self.skipElispParens(s,i)
                k = g.skip_ws(s,i+1)
                if g.match_word(s,k,"defun") or g.match_word(s,k,"defconst") or g.match_word(s,k,"defvar"):
                    data = s[start:i]
                    if data.strip():
                        self.createElispDataNode(p,data)
                    self.createElispFunction(p,s[i:j+1])
                    start = j+1
                i = j
            else:
                i += 1
            assert(progress < i)
        data = s[start:len(s)]
        if data.strip():
            self.createElispDataNode(p,data)
    #@+node:ekr.20031218072017.3266:skipElispParens
    def skipElispParens (self,s,i):

        level = 0 ; n = len(s)
        assert(g.match(s,i,'('))

        while i < n:
            c = s[i]
            if c == '(':
                level += 1 ; i += 1
            elif c == ')':
                level -= 1
                if level <= 0:
                    return i
                i += 1
            elif c == '"': i = g.skip_string(s,i) # Single-quotes are not strings.
            elif g.match(s,i,";"):  i = g.skip_line(s,i)
            else: i += 1
        return i
    #@-node:ekr.20031218072017.3266:skipElispParens
    #@+node:ekr.20031218072017.3267:skipElispId
    def skipElispId (self,s,i):

        n = len(s)
        while i < n and g.isWordChar(s[i]):
            i += 1
        return i
    #@-node:ekr.20031218072017.3267:skipElispId
    #@+node:ekr.20031218072017.3268:createElispFunction
    def createElispFunction (self,p,s):

        body = s
        i = 1 # Skip the '('
        i = g.skip_ws(s,i)

        # Set the prefix in the headline.
        assert(g.match(s,i,"defun") or g.match_word(s,i,"defconst") or g.match_word(s,i,"defvar"))
        if g.match_word(s,i,"defconst"):
            prefix = "const "
        elif g.match_word(s,i,"defvar"):
            prefix = "var "
        else:
            prefix = ""

        # Skip the "defun" or "defconst" or "defvar"
        i = self.skipElispId(s,i)

        # Get the following id.
        i = g.skip_ws(s,i)
        j = self.skipElispId(s,i)
        theId = prefix + s[i:j]

        self.createHeadline(p,body,theId)
    #@-node:ekr.20031218072017.3268:createElispFunction
    #@+node:ekr.20031218072017.3269:createElispDataNode
    def createElispDataNode (self,p,s):

        data = s
        # g.trace(len(data))

        # Skip blank lines and comment lines.
        i = 0
        while i < len(s):
            i = g.skip_ws_and_nl(s,i)
            if g.match(s,i,';'):
                i = g.skip_line(s,i)
            else: break

        # Find the next id, probably prefixed by an open paren.
        if g.match(s,i,"("):
            i = g.skip_ws(s,i+1)
        j = self.skipElispId(s,i)
        theId = s[i:j]
        if not theId:
            theId = "unnamed data"

        self.createHeadline(p,data,theId)
    #@-node:ekr.20031218072017.3269:createElispDataNode
    #@-node:ekr.20031218072017.3265:scanElispText & allies
    #@+node:ekr.20041107094641:scanForthText
    def scanForthText (self,s,parent):

        """Minimal forth scanner - leave it to user to create nodes as they see fit."""

        self.c.setBodyString(parent,"@ignore\n" + "@language forth\n" + self.rootLine + s)
    #@-node:ekr.20041107094641:scanForthText
    #@+node:ekr.20060328112327:scanLuaText
    def scanLuaText (self,s,parent):

        """Minimal Lua scanner - leave it to user to create nodes as they see fit."""

        self.c.setBodyString(parent,"@ignore\n" + "@language lua\n" + self.rootLine + s)
    #@-node:ekr.20060328112327:scanLuaText
    #@+node:ekr.20031218072017.3281:scanPascalText
    # Creates a child of parent for each Pascal function definition seen.

    def scanPascalText (self,s,parent):

        c = self.c
        method_seen = False ; methodKind = "methods"
        scan_start = function_start = i = 0
        name = None
        while i < len(s):
            # line = g.get_line(s,i) ; g.trace(line)
            ch = s[i]
            if ch == '{': i = g.skip_pascal_braces(s,i)
            elif ch == '"' or ch == '\'': i = g.skip_pascal_string(s,i)
            elif g.match(s,i,"//"): i = g.skip_to_end_of_line(s,i)
            elif g.match(s,i,"(*"): i = g.skip_pascal_block_comment(s,i)
            elif g.is_c_id(s[i]):
                #@            << handle possible Pascal function >>
                #@+node:ekr.20031218072017.3282:<< handle possible Pascal function >>
                if g.match_c_word(s,i,"begin"):
                    i = g.skip_pascal_begin_end(s,i)
                    if g.match_c_word(s,i,"end"):
                        i = g.skip_c_id(s,i)
                elif (g.match_c_word(s,i,"function")  or g.match_c_word(s,i,"procedure") or
                    g.match_c_word(s,i,"constructor") or g.match_c_word(s,i,"destructor")):

                    # line = g.get_line(s,i) ; g.trace(line)

                    start = i
                    i = g.skip_c_id(s,i)
                    i = g.skip_ws_and_nl(s,i)
                    #@    << remember the function name, or continue >>
                    #@+node:ekr.20031218072017.3285:<< remember the function name, or continue >>
                    if i < len(s) and g.is_c_id(s[i]):
                        j = i ; i = g.skip_c_id(s,i)
                        while i + 1 < len(s) and s[i] == '.' and g.is_c_id(s[i+1]):
                            i += 1 ; j = i
                            i = g.skip_c_id(s,i)
                        name = s[j:i]
                    else: continue
                    #@-node:ekr.20031218072017.3285:<< remember the function name, or continue >>
                    #@nl
                    #@    << skip the function definition, or continue >>
                    #@+node:ekr.20031218072017.3286:<< skip the function definition, or continue >>
                    #@<< skip past the semicolon >>
                    #@+node:ekr.20031218072017.3287:<< skip past the semicolon >>
                    while i < len(s) and s[i] != ';':
                        # The paremeter list may contain "inner" semicolons.
                        if s[i] == '(':
                            i = g.skip_parens(s,i)
                            if g.match(s,i,')'):
                                i += 1
                            else: break
                        else: i += 1
                    if g.match(s,i,';'):
                        i += 1
                    i = g.skip_ws_and_nl(s,i)

                    if g.match_c_word(s,i,"var"):
                        # Skip to the next begin.
                        i = g.skip_c_id(s,i)
                        done = False
                        while i < len(s) and not done:
                            ch = s[i]
                            if ch == '{': i = g.skip_pascal_braces(s,i)
                            elif g.match(s,i,"//"): i = g.skip_to_end_of_line(s,i)
                            elif g.match(s,i,"(*"): i = g.skip_pascal_block_comment(s,i)
                            elif g.is_c_id(ch):
                                if g.match_c_word(s,i,"begin"): done = True
                                else: i = g.skip_c_id(s,i)
                            elif ch == '"' or ch == '\'': i = g.skip_pascal_string(s,i)
                            else: i += 1
                    #@-node:ekr.20031218072017.3287:<< skip past the semicolon >>
                    #@nl

                    if not g.match_c_word(s,i,"begin"):
                        continue
                    # Skip to the matching end.
                    i = g.skip_pascal_begin_end(s,i)
                    if g.match_c_word(s,i,"end"):
                        i = g.skip_c_id(s,i)
                        i = g.skip_ws_and_nl(s,i)
                        if g.match(s,i,';'):
                            i += 1
                        i = g.skip_ws(s,i)
                        if g.is_nl(s,i):
                            i = g.skip_nl(s,i)
                    else: continue
                    #@-node:ekr.20031218072017.3286:<< skip the function definition, or continue >>
                    #@nl
                    if not method_seen:
                        method_seen = True
                        #@        << create a child node for leading declarations >>
                        #@+node:ekr.20031218072017.3283:<< create a child node for leading declarations >>
                        save_ip = i
                        i = scan_start
                        while i < start and g.is_ws_or_nl(s,i):
                            i += 1
                        if i < start:
                            c.appendStringToBody(parent,"@ignore\n" + self.rootLine + "@language pascal\n")
                            headline = g.angleBrackets(self.methodName + " declarations ")
                            # Append the headline to the parent's body.
                            c.appendStringToBody(parent,headline + "\n")
                            if self.treeType == "@file":
                                body = s[scan_start:start]
                            else:
                                body = "@code\n\n" + s[scan_start:start]
                            body = self.undentBody(body)
                            self.createHeadline(parent,body,headline)
                        i = save_ip
                        scan_start = i
                        #@-node:ekr.20031218072017.3283:<< create a child node for leading declarations >>
                        #@nl
                        #@        << append noweb method reference to the parent node >>
                        #@+node:ekr.20031218072017.3288:<< append noweb method reference to the parent node >>
                        # Append the headline to the parent's body.
                        if self.treeType == "@file":
                            c.appendStringToBody(parent,"@others\n")
                        else:
                            c.appendStringToBody(parent,
                                g.angleBrackets(" " + self.methodName + " methods ") + "\n")
                        #@-node:ekr.20031218072017.3288:<< append noweb method reference to the parent node >>
                        #@nl
                        function_start = start
                    else: function_start = scan_start
                    #@    << create a child node for the function >>
                    #@+node:ekr.20031218072017.3284:<< create a child node for the function >>
                    # Point i _after_ the last character of the function.
                    i = g.skip_ws(s,i)
                    if g.is_nl(s,i):
                        i = g.skip_nl(s,i)
                    function_end = i
                    headline = name
                    body = s[function_start:function_end]
                    body = self.massageBody(body,methodKind)
                    self.createHeadline(parent,body,headline)
                    scan_start = i
                    #@-node:ekr.20031218072017.3284:<< create a child node for the function >>
                    #@nl
                else: i = g.skip_c_id(s,i)
                #@-node:ekr.20031218072017.3282:<< handle possible Pascal function >>
                #@nl
            else: i += 1
        #@    << Append any unused text to the parent's body text >>
        #@+node:ekr.20031218072017.3264:<< append any unused text to the parent's body text >>
        # Used by the Java and Pascal scanners.

        i = g.skip_ws_and_nl(s,scan_start)
        if i < len(s):
            c.appendStringToBody(parent,s[scan_start:])
        #@-node:ekr.20031218072017.3264:<< append any unused text to the parent's body text >>
        #@nl
    #@-node:ekr.20031218072017.3281:scanPascalText
    #@+node:ekr.20031218072017.3242:scanPHPText (Dave Hein)
    # 08-SEP-2002 DTHEIN: Added for PHP import support.
    #
    # PHP uses both # and // as line comments, and /* */ as block comments

    def scanPHPText (self,s,parent):

        __pychecker__ = 'maxlines=500'

        """Creates a child of parent for each class and function definition seen."""

        #@    << define scanPHPText vars >>
        #@+node:ekr.20031218072017.3244:<< define scanPHPText vars >>
        c = self.c
        scan_start = 0
        class_start = 0
        function_start = 0
        i = 0
        class_body = ""
        class_node = ""
        phpClassName = re.compile("class\s+([a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*)")
        phpFunctionName = re.compile("function\s+([a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*)")

        # 14-SEP-2002 DTHEIN: added these 2 variables to allow use of @first/last
        startOfCode = s.find("\n") + 1 # this should be the line containing the initial <?php
        endOfCode = s.rfind("?>") # this should be the line containing the last ?>
        #@-node:ekr.20031218072017.3244:<< define scanPHPText vars >>
        #@nl
        #@    << Append file if not pure PHP >>
        #@+node:ekr.20031218072017.3243:<< Append file if not pure PHP >>
        # If the file does not begin with <?php or end with ?> then
        # it is simply appended like a generic import would do.

        s.strip() # Remove inadvertent whitespace.

        if (
            not (
                s.startswith("<?P") or
                s.startswith("<?p") or
                s.startswith("<?=") or
                s.startswith("<?\n") or
                s.startswith("<?\r") or
                s.startswith("<? ") or
                s.startswith("<?\t")
            ) or not (
                s.endswith("?>\n") or
                s.endswith("?>\r") or
                s.endswith("?>\r\n")
            )
        ):
            g.es("File seems to be mixed HTML and PHP; importing as plain text file.")
            c.setBodyString(parent,"@ignore\n" + self.rootLine + s)
            return
        #@-node:ekr.20031218072017.3243:<< Append file if not pure PHP >>
        #@nl

        # 14-SEP-2002 DTHEIN: Make leading <?php use the @first directive
        c.appendStringToBody(parent,"@first ")
        c.appendStringToBody(parent,s[:startOfCode])
        scan_start = i = startOfCode
        while i < endOfCode:
            # line = g.get_line(s,i) ; g.trace(line)
            ch = s[i]
            # These cases skip tokens.
            if ch == '/' or ch == '#':
                #@            << handle possible PHP comments >>
                #@+node:ekr.20031218072017.3246:<< handle possible PHP comments >>
                if g.match(s,i,"//"):
                    i = g.skip_line(s,i)
                elif g.match(s,i,"#"):
                    i = g.skip_line(s,i)
                elif g.match(s,i,"/*"):
                    i = g.skip_block_comment(s,i)
                else:
                    i += 1
                #@-node:ekr.20031218072017.3246:<< handle possible PHP comments >>
                #@nl
            elif ch == '<':
                #@            << handle possible heredoc string >>
                #@+node:ekr.20031218072017.3245:<< handle possible heredoc string >>
                if g.match(s,i,"<<<"):
                    i = g.skip_heredoc_string(s,i)
                else:
                    i += 1
                #@-node:ekr.20031218072017.3245:<< handle possible heredoc string >>
                #@nl
            elif ch == '"' or ch == '\'':
                i = g.skip_string(s,i)
            # These cases help determine where functions start.
            # FIXME: probably want to capture 'var's as class member data
            elif ch == 'f' or ch =='c':
                #@            << handle possible class or function >>
                #@+node:ekr.20031218072017.3247:<< handle possible class or function >>
                #@+at 
                #@nonl
                # In PHP, all functions are typeless and start with the 
                # keyword "function;  all classes start with the keyword 
                # class.
                # 
                # Functions can be nested, but we don't handle that right now 
                # (I don't think it is a common practice anyway).
                #@-at
                #@@c
                if g.match(s,i,"function "):
                    #we want to make the function a subnode of either the @file node or a class node
                    # 1. get the function name
                    # 2. make a reference in the parent
                    # 3. create the child node, and dump the function in it.
                    function_start = i
                    m = phpFunctionName.match(s[i:])
                    if (None == m): # function keyword without function name
                        i += len("function ")
                    else:
                        headline = g.angleBrackets(" function " + m.group(1) + " ")
                        # find the end of the function
                        openingBrace = s.find('{',i)
                        function_end = g.skip_php_braces(s,openingBrace)
                        function_end = g.skip_to_end_of_line(s,function_end - 1) + 1 # include the line end
                        # Insert skipped text into parent's body.
                        if class_start:
                            class_body += s[scan_start:function_start]
                        else:
                            c.appendStringToBody(parent,s[scan_start:function_start])
                        # Append the headline to the parent's body.
                        if class_start:
                            class_body += (headline + "\n")
                        else:
                            c.appendStringToBody(parent,headline + "\n")
                        # Backup to capture leading whitespace (for undent purposes)
                        while (function_start > 0) and (s[function_start - 1] in [" ", "\t"]):
                            function_start -= 1
                        # Get the body and undent it
                        function_body = s[function_start:function_end]
                        function_body = self.undentBody(function_body)
                        if self.treeType != "@file":
                            function_body = "@code\n\n" + function_body
                        # Create the new node
                        if class_start:
                            self.createHeadline(class_node,function_body,headline)
                        else:
                            self.createHeadline(parent,function_body,headline)
                        i = function_end
                        scan_start = i
                        function_end = 0
                        function_start = 0 #done with this function
                        function_body = ""

                elif g.match(s,i,"class "):
                    # we want to make the class a subnode of the @file node
                    # 1. get the class name
                    # 2. make a reference in the parent
                    # 3. create the child node and dump the function in it
                    class_start = i
                    class_body = ""
                    m = phpClassName.match(s[i:])
                    if (None == m): # class keyword without class name
                        i += len("class ")
                    else:
                        # Insert skipped text into parent's body.
                        c.appendStringToBody(parent,s[scan_start:class_start])
                        # create the headline name
                        headline = g.angleBrackets(" class " + m.group(1) + " ")
                        # find the place to start looking for methods (functions)
                        openingBrace = s.find('{',i)
                        # find the end of the class
                        class_end = g.skip_php_braces(s,openingBrace)
                        class_end = g.skip_to_end_of_line(s,class_end - 1) + 1 # include the line end
                        # Append the headline to the parent's body.
                        c.appendStringToBody(parent,headline + "\n")
                        # Backup to capture leading whitespace (for undent purposes)
                        while (class_start > 0) and (s[class_start - 1] in [" ", "\t"]):
                            class_start -= 1
                        scan_start = class_start
                        # Create the new node
                        class_node = self.createHeadline(parent,"",headline)
                        i = openingBrace

                else:
                    i += 1
                #@-node:ekr.20031218072017.3247:<< handle possible class or function >>
                #@nl
            elif class_start and (ch == '}'):
                #@            << handle end of class >>
                #@+node:ekr.20031218072017.3248:<< handle end of class >>
                # Capture the rest of the body
                class_body += s[scan_start:class_end]
                # insert the class node's body
                if self.treeType != "@file":
                    class_body = "@code\n\n" + class_body
                class_body = self.undentBody(class_body)
                c.appendStringToBody(class_node,class_body)
                # reset the indices
                i = class_end
                scan_start = i
                class_end = 0
                class_start = 0 #done with this class
                class_body=""
                #@-node:ekr.20031218072017.3248:<< handle end of class >>
                #@nl
            else: i += 1
        #@    << Append any unused text to the parent's body text >>
        #@+node:ekr.20031218072017.3249:<< Append any unused text to the parent's body text >>
        c.appendStringToBody(parent,s[scan_start:endOfCode])
        #@-node:ekr.20031218072017.3249:<< Append any unused text to the parent's body text >>
        #@nl
        # 14-SEP-2002 DTHEIN: Make leading <?php use the @first directive
        c.appendStringToBody(parent,"@last ")
        c.appendStringToBody(parent,s[endOfCode:])
    #@-node:ekr.20031218072017.3242:scanPHPText (Dave Hein)
    #@-node:ekr.20070703123618:Unchanged scanners
    #@+node:ekr.20070703123334.2:Python scanner & helpers
    #@+node:ekr.20070705091716:pythonUnitTest
    def pythonUnitTest (self,p,s,fileName,atAuto=False,strict=False):

        '''
        Run a unit test of the Python parser,
        i.e., create a tree from string s at location p.
        The caller is responsible for asserting properties of the tree.
        '''

        # Duplicate processing in ic command
        ic = self ; c = ic.c
        if fileName.startswith('@test'):
            fileName = fileName[5:].strip()
        junk,ic.fileName = g.os_path_split(fileName)
        ic.methodName,ic.fileType = g.os_path_splitext(ic.fileName)
        ic.setEncoding()

        c.beginUpdate()
        try:
            # Create a child
            child = p.insertAsLastChild()
            assert child
            h = g.choose(atAuto,'@auto ' + fileName,fileName)
            child.initHeadString(h)
            ic.scanPythonText (s=s,parent=child.copy(),atAuto=atAuto,strict=strict)
        finally:
            c.endUpdate()
        if 0:
            g.trace('***** generated tree...')
            for z in p.subtree_iter():
                print '.'*z.level(),z.headString()

        return child
    #@-node:ekr.20070705091716:pythonUnitTest
    #@+node:ekr.20070703122141.99:scanPythonText
    def scanPythonText (self,s,parent,atAuto=False,strict=False):

        scanner = self.pythonScanner(
            importCommands=self,
            atAuto=atAuto,
            strict=strict)

        scanner.run(s,parent)
    #@-node:ekr.20070703122141.99:scanPythonText
    #@+node:ekr.20070703122141.100:class pythonScanner (baseScannerClass)
    class pythonScanner (baseScannerClass):

        #@    @+others
        #@+node:ekr.20070703122141.101: __init__
        def __init__ (self,importCommands,atAuto,strict):

            importCommands.baseScannerClass.__init__(self,importCommands,
                atAuto=atAuto,
                language='python',
                strict=strict,
            )

            # Set the parser delims.
            self.blockCommentDelim1 = None
            self.blockCommentDelim2 = None
            self.lineCommentDelim = '#'

        #@-node:ekr.20070703122141.101: __init__
        #@+node:ekr.20070707073723:Overrides
        #@+at 
        #@nonl
        # skipClass/Function/Signature are usually defined in the base class,
        # but for Python it is convenient to override them all.
        #@-at
        #@nonl
        #@+node:ekr.20070707113839:extendSignature
        def extendSignature(self,s,i):

            '''
            Extend the text to added to the class node following the signature.

            The text *must* end with a newline.
            '''

            # Add a docstring to the class node,
            # And everything on the line following it
            j = g.skip_ws_and_nl(s,i)
            if g.match(s,j,'"""') or g.match(s,j,"'''"):
                j = g.skip_python_string(s,j)
                if j < len(s): # No scanning error.
                    # Return the docstring only if nothing but whitespace follows.
                    j = g.skip_ws(s,j)
                    if g.is_nl(s,j):
                        return j + 1

            return i
        #@-node:ekr.20070707113839:extendSignature
        #@+node:ekr.20070707082226:skipClass/Function & helper
        def skipClass (self,s,i):
            return self.skipHelper(s,i)

        def skipFunction (self,s,i):
            return self.skipHelper(s,i)
        #@+node:ekr.20070707111805:skipHelper (pythonScanner)
        def skipHelper (self,s,i):

            # g.trace(g.get_line(s,i))

            startIndent = self.getLeadingIndent(s,i)
            i = self.skipSignature(s,i)
            i = g.skip_ws_and_nl(s,i)
            parenCount = 0
            underIndentedStart = None
            while i < len(s):
                progress = i
                ch = s[i]
                if g.is_nl(s,i):
                    backslashNewline = i > 0 and g.match(s,i-1,"\\\n")
                    i = g.skip_nl(s,i)
                    if not backslashNewline:
                        j, indent = g.skip_leading_ws_with_indent(s,i,self.tab_width)
                        underIndented = indent <= startIndent and parenCount == 0
                        if underIndented:
                            if g.match(s,j,'#') or g.match(s,j,'\n'):
                                # Dont stop immediately for underindented comment or blank lines.
                                # Extend the range of underindented lines.
                                if underIndentedStart is None:
                                    underIndentedStart = i
                                i = j
                            else:
                                # The actual end of the function.
                                return g.choose(underIndentedStart is None,i,underIndentedStart)
                        else:
                            underIndentedStart = None
                elif ch == '#':
                    i = g.skip_to_end_of_line(s,i)
                elif ch == '"' or ch == '\'':
                    i = g.skip_python_string(s,i)
                elif ch in '[{(':
                    i += 1 ; parenCount += 1
                    # g.trace('ch',ch,parenCount)
                elif ch in ']})':
                    i += 1 ; parenCount -= 1
                    # g.trace('ch',ch,parenCount)
                else: i += 1
                assert(progress < i)

            return i
        #@-node:ekr.20070707111805:skipHelper (pythonScanner)
        #@-node:ekr.20070707082226:skipClass/Function & helper
        #@+node:ekr.20070707115247:skipSignature
        def skipSignature (self,s,i):

            '''Skip the signature line of a class or function.
            The text must end with a newline.'''

            start = i
            message = 'Warning: improper signature: %s' % g.get_line(s,start)

            # g.trace(g.getLine(s,i))

            # Skip the def or class.
            for tag in ('def','class'):
                if g.match_word(s,i,tag):
                    i += len(tag)
                    break
            else:
                self.error(message)
                return start

            # Skip the class or function name.
            i = g.skip_ws_and_nl(s,i)
            j = g.skip_c_id(s,i)
            if j == i:
                self.error(message)
                return start

            # Skip the optional argument or base-class list.
            i = g.skip_ws_and_nl(s,j)
            if g.match(s,i,'('):
                i = self.skipBlock(s,i,delim1='(',delim2=')')
                i = g.skip_ws_and_nl(s,i)

            if g.match(s,i,':'):
                return g.skip_line(s,i+1)
            else:
                self.error(message)
                return start
        #@-node:ekr.20070707115247:skipSignature
        #@+node:ekr.20070707073627.4:skipString
        def skipString (self,s,i):

            # Returns len(s) on unterminated string.
            return g.skip_python_string(s,i,verbose=False)
        #@-node:ekr.20070707073627.4:skipString
        #@+node:ekr.20070707080005:startsClass/Function
        def startsClass (self,s,i):
            '''Return the class id if s[i:] starts a class definition.'''
            return self.startsHelper(s,i,'class')

        def startsFunction (self,s,i):
            '''Return the function id if s[i:] starts a function definition.'''
            return self.startsHelper(s,i,'def')

        def startsHelper(self,s,i,tag):

            if g.match_word(s,i,tag):
                i += len(tag)
                i = g.skip_ws_and_nl(s,i)
                j = g.skip_c_id(s,i)
                self.sigID = s[i:j]
                return True
            else:
                return False
        #@-node:ekr.20070707080005:startsClass/Function
        #@-node:ekr.20070707073723:Overrides
        #@-others
    #@-node:ekr.20070703122141.100:class pythonScanner (baseScannerClass)
    #@-node:ekr.20070703123334.2:Python scanner & helpers
    #@+node:edreamleo.20070710110114:Java scanner & helpers
    #@+node:edreamleo.20070710110114.2:scanJavaText
    def scanJavaText (self,s,parent,atAuto=False,strict=False):

        scanner = self.javaScanner(
            importCommands=self,
            atAuto=atAuto,
            strict=strict)

        scanner.run(s,parent)
    #@-node:edreamleo.20070710110114.2:scanJavaText
    #@+node:edreamleo.20070710085115:class javaScanner (baseScannerClass)
    class javaScanner (baseScannerClass):

        #@    @+others
        #@+node:edreamleo.20070710085115.1: __init__
        def __init__ (self,importCommands,atAuto,strict):

            importCommands.baseScannerClass.__init__(self,importCommands,
                atAuto=atAuto,
                language='python',
                strict=strict,
            )

            # Set the parser delims.
            self.blockCommentDelim1 = '/*'
            self.blockCommentDelim2 = '*/'
            self.lineCommentDelim = '//'

        #@-node:edreamleo.20070710085115.1: __init__
        #@+node:edreamleo.20070710085115.2:Overrides
        # skipClass/Function/Signature are defined in the base class.
        #@nonl
        #@+node:edreamleo.20070710085115.8:startsClass/Function & skipSignature
        def startsClass (self,s,i):
            '''Return True if s[i:] starts a class definition.
            Sets self.end, self.sigEnd and self.sigID.'''
            return self.startsHelper(s,i,classFlag=True)

        def startsFunction (self,s,i):
            '''Return True if s[i:] starts a function.
            Sets self.end, self.sigEnd and self.sigID.'''
            return self.startsHelper(s,i,classFlag=False)

        def startsHelper(self,s,i,classFlag):
            '''Return index of end of signature if sig is True,
            otherwise return True if s[i:] starts a class or function.'''

            self.end = self.sigEnd = self.sigID = None
            if not g.is_c_id(s[i]): return False
            word1 = g.skip_c_id(s,i)
            if classFlag is not None:
                classStart = word1 in ('class','interface')
                if classFlag != classStart: return False

            # Skip one or more id's.
            while i < len(s) and g.is_c_id(s[i]):
                j = g.skip_c_id(s,i)
                word = s[i:j]
                i = g.skip_ws_and_nl(s,j)

            # Skip the argument list.
            if not g.match(s,i,'('): return False
            i = g.skip_parens(s,i)
            if not g.match(s,i,')') : return False

            # Skip the block.
            i = g.skip_ws_and_nl(s,i+1)
            if g.match(s,i,'{'):
                sigEnd = g.skip_ws_and_nl(s,i+1)
                i = g.skip_braces(s,i)
                ok = g.match(s,i,'}')
                if ok:
                    i = g.skip_ws_and_nl(s,i+1)
                    self.end = i
                    self.sigEnd = sigEnd
                    self.sigID = word
                return ok
            else:
                return False

        #@-node:edreamleo.20070710085115.8:startsClass/Function & skipSignature
        #@-node:edreamleo.20070710085115.2:Overrides
        #@-others
    #@-node:edreamleo.20070710085115:class javaScanner (baseScannerClass)
    #@-node:edreamleo.20070710110114:Java scanner & helpers
    #@+node:edreamleo.20070710110114.1:C scanner & helpers
    #@+node:edreamleo.20070710110153:scanCText
    def scanCText (self,s,parent,atAuto=False,strict=False):

        scanner = self.cScanner(
            importCommands=self,
            atAuto=atAuto,
            strict=strict)

        scanner.run(s,parent)
    #@-node:edreamleo.20070710110153:scanCText
    #@+node:edreamleo.20070710093042:class cScanner (baseScannerClass)
    class javaScanner (baseScannerClass):

        #@    @+others
        #@+node:edreamleo.20070710093042.1: __init__
        def __init__ (self,importCommands,atAuto,strict):

            importCommands.baseScannerClass.__init__(self,importCommands,
                atAuto=atAuto,
                language='python',
                strict=strict,
            )

            # Set the parser delims.
            self.blockCommentDelim1 = '/*'
            self.blockCommentDelim2 = '*/'
            self.lineCommentDelim = '//'

        #@-node:edreamleo.20070710093042.1: __init__
        #@+node:edreamleo.20070710093042.2:Overrides
        # skipClass/Function/Signature are defined in the base class.
        #@nonl
        #@+node:edreamleo.20070710093042.6:startsClass/Function & skipSignature
        def startsClass (self,s,i):
            '''Return True if s[i:] starts a class definition.
            Sets self.end, self.sigEnd and self.sigID.'''
            return self.startsHelper(s,i,classFlag=True)

        def startsFunction (self,s,i):
            '''Return True if s[i:] starts a function.
            Sets self.end, self.sigEnd and self.sigID.'''
            return self.startsHelper(s,i,classFlag=False)

        def startsHelper(self,s,i,classFlag):
            '''Return index of end of signature if sig is True,
            otherwise return True if s[i:] starts a class or function.'''

            self.end = self.sigEnd = self.sigID = None
            # Skip one or more id's.
            words = []
            if not g.is_c_id(s[i]): return False
            while i < len(s) and g.is_c_id(s[i]):
                j = g.skip_c_id(s,i)
                word = s[i:j]
                words.append(word)
                i = g.skip_ws_and_nl(s,j)

            classStart = 'class' in words
            if classFlag != classStart: return False

            # Skip one or more lists: casts can cause multiple parens.
            if not g.match(s,i,'('): return False
            while g.match(s,i,'('):
                i = g.skip_parens(s,i)
                if not g.match(s,i,')') : return False
                i = g.skip_ws_and_nl(s,i+1)

            if g.match(s,i,'{'):
                sigEnd = g.skip_ws_and_nl(s,i+1)
                i = g.skip_braces(s,i)
                ok = g.match(s,i,'}')
                if ok:
                    i = g.skip_ws_and_nl(s,i+1)
                    self.end = i
                    self.sigEnd = sigEnd
                    self.sigID = word
                return ok
            else:
                return False
        #@-node:edreamleo.20070710093042.6:startsClass/Function & skipSignature
        #@-node:edreamleo.20070710093042.2:Overrides
        #@-others
    #@-node:edreamleo.20070710093042:class cScanner (baseScannerClass)
    #@-node:edreamleo.20070710110114.1:C scanner & helpers
    #@-node:ekr.20031218072017.3241:Scanners for createOutline
    #@-node:ekr.20031218072017.3209:Import
    #@+node:ekr.20031218072017.3289:Export
    #@+node:ekr.20031218072017.3290:convertCodePartToWeb
    # Headlines not containing a section reference are ignored in noweb and generate index index in cweb.

    def convertCodePartToWeb (self,s,i,v,result):

        # g.trace(g.get_line(s,i))
        c = self.c ; nl = self.output_newline
        lb = g.choose(self.webType=="cweb","@<","<<")
        rb = g.choose(self.webType=="cweb","@>",">>")
        h = string.strip(v.headString())
        #@    << put v's headline ref in head_ref >>
        #@+node:ekr.20031218072017.3291:<< put v's headline ref in head_ref>>
        #@+at 
        #@nonl
        # We look for either noweb or cweb brackets. head_ref does not include 
        # these brackets.
        #@-at
        #@@c

        head_ref = None
        j = 0
        if g.match(h,j,"<<"):
            k = string.find(h,">>",j)
        elif g.match(h,j,"<@"):
            k = string.find(h,"@>",j)
        else:
            k = -1

        if k > -1:
            head_ref = string.strip(h[j+2:k])
            if len(head_ref) == 0:
                head_ref = None
        #@-node:ekr.20031218072017.3291:<< put v's headline ref in head_ref>>
        #@nl
        #@    << put name following @root or @file in file_name >>
        #@+node:ekr.20031218072017.3292:<< put name following @root or @file in file_name >>
        if g.match(h,0,"@file") or g.match(h,0,"@root"):
            line = h[5:]
            line = string.strip(line)
            #@    << set file_name >>
            #@+node:ekr.20031218072017.3293:<< Set file_name >>
            # set j & k so line[j:k] is the file name.
            # g.trace(line)

            if g.match(line,0,"<"):
                j = 1 ; k = string.find(line,">",1)
            elif g.match(line,0,'"'):
                j = 1 ; k = string.find(line,'"',1)
            else:
                j = 0 ; k = string.find(line," ",0)
            if k == -1:
                k = len(line)

            file_name = string.strip(line[j:k])
            if file_name and len(file_name) == 0:
                file_name = None
            #@-node:ekr.20031218072017.3293:<< Set file_name >>
            #@nl
        else:
            file_name = line = None
        #@-node:ekr.20031218072017.3292:<< put name following @root or @file in file_name >>
        #@nl
        if g.match_word(s,i,"@root"):
            i = g.skip_line(s,i)
            #@        << append ref to file_name >>
            #@+node:ekr.20031218072017.3294:<< append ref to file_name >>
            if self.webType == "cweb":
                if not file_name:
                    result += "@<root@>=" + nl
                else:
                    result += "@(" + file_name + "@>" + nl # @(...@> denotes a file.
            else:
                if not file_name:
                    file_name = "*"
                result += lb + file_name + rb + "=" + nl
            #@-node:ekr.20031218072017.3294:<< append ref to file_name >>
            #@nl
        elif g.match_word(s,i,"@c") or g.match_word(s,i,"@code"):
            i = g.skip_line(s,i)
            #@        << append head_ref >>
            #@+node:ekr.20031218072017.3295:<< append head_ref >>
            if self.webType == "cweb":
                if not head_ref:
                    result += "@^" + h + "@>" + nl # Convert the headline to an index entry.
                    result += "@c" + nl # @c denotes a new section.
                else: 
                    escaped_head_ref = string.replace(head_ref,"@","@@")
                    result += "@<" + escaped_head_ref + "@>=" + nl
            else:
                if not head_ref:
                    if v == c.currentVnode():
                        head_ref = g.choose(file_name,file_name,"*")
                    else:
                        head_ref = "@others"

                result += lb + head_ref + rb + "=" + nl
            #@-node:ekr.20031218072017.3295:<< append head_ref >>
            #@nl
        elif g.match_word(h,0,"@file"):
            # Only do this if nothing else matches.
            #@        << append ref to file_name >>
            #@+node:ekr.20031218072017.3294:<< append ref to file_name >>
            if self.webType == "cweb":
                if not file_name:
                    result += "@<root@>=" + nl
                else:
                    result += "@(" + file_name + "@>" + nl # @(...@> denotes a file.
            else:
                if not file_name:
                    file_name = "*"
                result += lb + file_name + rb + "=" + nl
            #@-node:ekr.20031218072017.3294:<< append ref to file_name >>
            #@nl
            i = g.skip_line(s,i) # 4/28/02
        else:
            #@        << append head_ref >>
            #@+node:ekr.20031218072017.3295:<< append head_ref >>
            if self.webType == "cweb":
                if not head_ref:
                    result += "@^" + h + "@>" + nl # Convert the headline to an index entry.
                    result += "@c" + nl # @c denotes a new section.
                else: 
                    escaped_head_ref = string.replace(head_ref,"@","@@")
                    result += "@<" + escaped_head_ref + "@>=" + nl
            else:
                if not head_ref:
                    if v == c.currentVnode():
                        head_ref = g.choose(file_name,file_name,"*")
                    else:
                        head_ref = "@others"

                result += lb + head_ref + rb + "=" + nl
            #@-node:ekr.20031218072017.3295:<< append head_ref >>
            #@nl
        i,result = self.copyPart(s,i,result)
        return i, string.strip(result) + nl

    #@+at 
    #@nonl
    # %defs a b c
    #@-at
    #@-node:ekr.20031218072017.3290:convertCodePartToWeb
    #@+node:ekr.20031218072017.3296:convertDocPartToWeb (handle @ %def)
    def convertDocPartToWeb (self,s,i,result):

        nl = self.output_newline

        # g.trace(g.get_line(s,i))
        if g.match_word(s,i,"@doc"):
            i = g.skip_line(s,i)
        elif g.match(s,i,"@ ") or g.match(s,i,"@\t") or g.match(s,i,"@*"):
            i += 2
        elif g.match(s,i,"@\n"):
            i += 1
        i = g.skip_ws_and_nl(s,i)
        i, result2 = self.copyPart(s,i,"")
        if len(result2) > 0:
            # Break lines after periods.
            result2 = string.replace(result2,".  ","." + nl)
            result2 = string.replace(result2,". ","." + nl)
            result += nl+"@"+nl+string.strip(result2)+nl+nl
        else:
            # All nodes should start with '@', even if the doc part is empty.
            result += g.choose(self.webType=="cweb",nl+"@ ",nl+"@"+nl)
        return i, result
    #@-node:ekr.20031218072017.3296:convertDocPartToWeb (handle @ %def)
    #@+node:ekr.20031218072017.3297:convertVnodeToWeb
    #@+at 
    #@nonl
    # This code converts a vnode to noweb text as follows:
    # 
    # Convert @doc to @
    # Convert @root or @code to < < name > >=, assuming the headline contains 
    # < < name > >
    # Ignore other directives
    # Format doc parts so they fit in pagewidth columns.
    # Output code parts as is.
    #@-at
    #@@c

    def convertVnodeToWeb (self,v):

        c = self.c
        if not v or not c: return ""
        startInCode = not c.config.at_root_bodies_start_in_doc_mode
        nl = self.output_newline
        s = v.bodyString()
        lb = g.choose(self.webType=="cweb","@<","<<")
        i = 0 ; result = "" ; docSeen = False
        while i < len(s):
            progress = i
            # g.trace(g.get_line(s,i))
            i = g.skip_ws_and_nl(s,i)
            if self.isDocStart(s,i) or g.match_word(s,i,"@doc"):
                i,result = self.convertDocPartToWeb(s,i,result)
                docSeen = True
            elif (g.match_word(s,i,"@code") or g.match_word(s,i,"@root") or
                g.match_word(s,i,"@c") or g.match(s,i,lb)):
                #@            << Supply a missing doc part >>
                #@+node:ekr.20031218072017.3298:<< Supply a missing doc part >>
                if not docSeen:
                    docSeen = True
                    result += g.choose(self.webType=="cweb",nl+"@ ",nl+"@"+nl)
                #@-node:ekr.20031218072017.3298:<< Supply a missing doc part >>
                #@nl
                i,result = self.convertCodePartToWeb(s,i,v,result)
            elif self.treeType == "@file" or startInCode:
                #@            << Supply a missing doc part >>
                #@+node:ekr.20031218072017.3298:<< Supply a missing doc part >>
                if not docSeen:
                    docSeen = True
                    result += g.choose(self.webType=="cweb",nl+"@ ",nl+"@"+nl)
                #@-node:ekr.20031218072017.3298:<< Supply a missing doc part >>
                #@nl
                i,result = self.convertCodePartToWeb(s,i,v,result)
            else:
                i,result = self.convertDocPartToWeb(s,i,result)
                docSeen = True
            assert(progress < i)
        result = string.strip(result)
        if len(result) > 0:
            result += nl
        return result
    #@-node:ekr.20031218072017.3297:convertVnodeToWeb
    #@+node:ekr.20031218072017.3299:copyPart
    # Copies characters to result until the end of the present section is seen.

    def copyPart (self,s,i,result):

        # g.trace(g.get_line(s,i))
        lb = g.choose(self.webType=="cweb","@<","<<")
        rb = g.choose(self.webType=="cweb","@>",">>")
        theType = self.webType
        while i < len(s):
            progress = j = i # We should be at the start of a line here.
            i = g.skip_nl(s,i) ; i = g.skip_ws(s,i)
            if self.isDocStart(s,i):
                return i, result
            if (g.match_word(s,i,"@doc") or
                g.match_word(s,i,"@c") or
                g.match_word(s,i,"@root") or
                g.match_word(s,i,"@code")): # 2/25/03
                return i, result
            elif (g.match(s,i,"<<") and # must be on separate lines.
                g.find_on_line(s,i,">>=") > -1):
                return i, result
            else:
                # Copy the entire line, escaping '@' and
                # Converting @others to < < @ others > >
                i = g.skip_line(s,j) ; line = s[j:i]
                if theType == "cweb":
                    line = string.replace(line,"@","@@")
                else:
                    j = g.skip_ws(line,0)
                    if g.match(line,j,"@others"):
                        line = string.replace(line,"@others",lb + "@others" + rb)
                    elif g.match(line,0,"@"):
                        # Special case: do not escape @ %defs.
                        k = g.skip_ws(line,1)
                        if not g.match(line,k,"%defs"):
                            line = "@" + line
                result += line
            assert(progress < i)
        return i, string.rstrip(result)
    #@-node:ekr.20031218072017.3299:copyPart
    #@+node:ekr.20031218072017.1462:exportHeadlines
    def exportHeadlines (self,fileName):

        c = self.c ; nl = self.output_newline
        p = c.currentPosition()
        if not p: return
        self.setEncoding()
        firstLevel = p.level()
        mode = c.config.output_newline
        mode = g.choose(mode=="platform",'w','wb')
        try:
            theFile = open(fileName,mode)
        except IOError:
            g.es("Can not open " + fileName,color="blue")
            leoTest.fail()
            return
        for p in p.self_and_subtree_iter():
            head = p.moreHead(firstLevel,useVerticalBar=True)
            head = g.toEncodedString(head,self.encoding,reportErrors=True)
            theFile.write(head + nl)
        theFile.close()
    #@-node:ekr.20031218072017.1462:exportHeadlines
    #@+node:ekr.20031218072017.1147:flattenOutline
    def flattenOutline (self,fileName):

        c = self.c ; nl = self.output_newline
        p = c.currentVnode()
        if not p: return
        self.setEncoding()
        firstLevel = p.level()

        # 10/14/02: support for output_newline setting.
        mode = c.config.output_newline
        mode = g.choose(mode=="platform",'w','wb')
        try:
            theFile = open(fileName,mode)
        except IOError:
            g.es("Can not open " + fileName,color="blue")
            leoTest.fail()
            return

        for p in p.self_and_subtree_iter():
            head = p.moreHead(firstLevel)
            head = g.toEncodedString(head,self.encoding,reportErrors=True)
            theFile.write(head + nl)
            body = p.moreBody() # Inserts escapes.
            if len(body) > 0:
                body = g.toEncodedString(body,self.encoding,reportErrors=True)
                theFile.write(body + nl)
        theFile.close()
    #@-node:ekr.20031218072017.1147:flattenOutline
    #@+node:ekr.20031218072017.1148:outlineToWeb
    def outlineToWeb (self,fileName,webType):

        c = self.c ; nl = self.output_newline
        current = c.currentPosition()
        if not current: return
        self.setEncoding()
        self.webType = webType
        # 10/14/02: support for output_newline setting.
        mode = c.config.output_newline
        mode = g.choose(mode=="platform",'w','wb')
        try:
            theFile = open(fileName,mode)
        except IOError:
            g.es("Can not open " + fileName,color="blue")
            leoTest.fail()
            return

        self.treeType = "@file"
        # Set self.treeType to @root if p or an ancestor is an @root node.
        for p in current.parents_iter():
            flag,junk = g.is_special(p.bodyString(),0,"@root")
            if flag:
                self.treeType = "@root"
                break
        for p in current.self_and_subtree_iter():
            s = self.convertVnodeToWeb(p)
            if len(s) > 0:
                s = g.toEncodedString(s,self.encoding,reportErrors=True)
                theFile.write(s)
                if s[-1] != '\n': theFile.write(nl)
        theFile.close()
    #@-node:ekr.20031218072017.1148:outlineToWeb
    #@+node:ekr.20031218072017.3300:removeSentinelsCommand
    def removeSentinelsCommand (self,paths):

        c = self.c

        self.setEncoding()

        for fileName in paths:
            g.setGlobalOpenDir(fileName)
            path, self.fileName = g.os_path_split(fileName)
            #@        << Read file into s >>
            #@+node:ekr.20031218072017.3301:<< Read file into s >>
            try:
                theFile = open(fileName)
                s = theFile.read()
                s = g.toUnicode(s,self.encoding)
                theFile.close()
            except IOError:
                g.es("can not open " + fileName, color="blue")
                leoTest.fail()
                return
            #@-node:ekr.20031218072017.3301:<< Read file into s >>
            #@nl
            #@        << set delims from the header line >>
            #@+node:ekr.20031218072017.3302:<< set delims from the header line >>
            # Skip any non @+leo lines.
            i = 0
            while i < len(s) and not g.find_on_line(s,i,"@+leo"):
                i = g.skip_line(s,i)

            # Get the comment delims from the @+leo sentinel line.
            at = self.c.atFileCommands
            j = g.skip_line(s,i) ; line = s[i:j]

            valid,new_df,start_delim,end_delim,derivedFileIsThin = at.parseLeoSentinel(line)
            if not valid:
                g.es("invalid @+leo sentinel in " + fileName)
                return

            if end_delim:
                line_delim = None
            else:
                line_delim,start_delim = start_delim,None
            #@-node:ekr.20031218072017.3302:<< set delims from the header line >>
            #@nl
            # g.trace("line: '%s', start: '%s', end: '%s'" % (line_delim,start_delim,end_delim))
            s = self.removeSentinelLines(s,line_delim,start_delim,end_delim)
            ext = c.config.remove_sentinels_extension
            if not ext:
                ext = ".txt"
            if ext[0] == '.':
                newFileName = g.os_path_join(path,fileName+ext)
            else:
                head,ext2 = g.os_path_splitext(fileName) 
                newFileName = g.os_path_join(path,head+ext+ext2)
            #@        << Write s into newFileName >>
            #@+node:ekr.20031218072017.1149:<< Write s into newFileName >>
            try:
                mode = c.config.output_newline
                mode = g.choose(mode=="platform",'w','wb')
                theFile = open(newFileName,mode)
                s = g.toEncodedString(s,self.encoding,reportErrors=True)
                theFile.write(s)
                theFile.close()
                if not g.unitTesting:
                    g.es("created: " + newFileName)
            except:
                g.es("exception creating: " + newFileName)
                g.es_exception()
            #@-node:ekr.20031218072017.1149:<< Write s into newFileName >>
            #@nl
    #@-node:ekr.20031218072017.3300:removeSentinelsCommand
    #@+node:ekr.20031218072017.3303:removeSentinelLines
    # This does not handle @nonl properly, but that's a nit...

    def removeSentinelLines(self,s,line_delim,start_delim,end_delim):

        '''Properly remove all sentinle lines in s.'''

        __pychecker__ = '--no-argsused' # end_delim.

        delim = (line_delim or start_delim or '') + '@'
        verbatim = delim + 'verbatim' ; verbatimFlag = False
        result = [] ; lines = g.splitLines(s)
        for line in lines:
            i = g.skip_ws(line,0)
            if not verbatimFlag and g.match(line,i,delim):
                if g.match(line,i,verbatim):
                    verbatimFlag = True # Force the next line to be in the result.
                # g.trace(repr(line))
            else:
                result.append(line)
                verbatimFlag = False
        result = ''.join(result)
        return result
    #@-node:ekr.20031218072017.3303:removeSentinelLines
    #@+node:ekr.20031218072017.1464:weave
    def weave (self,filename):

        c = self.c ; nl = self.output_newline
        p = c.currentPosition()
        if not p: return
        self.setEncoding()
        #@    << open filename to f, or return >>
        #@+node:ekr.20031218072017.1150:<< open filename to f, or return >>
        try:
            # 10/14/02: support for output_newline setting.
            mode = c.config.output_newline
            mode = g.choose(mode=="platform",'w','wb')
            f = open(filename,mode)
            if not f: return
        except:
            g.es("exception opening:" + filename)
            g.es_exception()
            return
        #@-node:ekr.20031218072017.1150:<< open filename to f, or return >>
        #@nl
        for p in p.self_and_subtree_iter():
            s = p.bodyString()
            s2 = string.strip(s)
            if s2 and len(s2) > 0:
                f.write("-" * 60) ; f.write(nl)
                #@            << write the context of p to f >>
                #@+node:ekr.20031218072017.1465:<< write the context of p to f >>
                # write the headlines of p, p's parent and p's grandparent.
                context = [] ; p2 = p.copy() ; i = 0
                while i < 3:
                    i += 1
                    if not p2: break
                    context.append(p2.headString())
                    p2.moveToParent()

                context.reverse()
                indent = ""
                for line in context:
                    f.write(indent)
                    indent += '\t'
                    line = g.toEncodedString(line,self.encoding,reportErrors=True)
                    f.write(line)
                    f.write(nl)
                #@-node:ekr.20031218072017.1465:<< write the context of p to f >>
                #@nl
                f.write("-" * 60) ; f.write(nl)
                s = g.toEncodedString(s,self.encoding,reportErrors=True)
                f.write(string.rstrip(s) + nl)
        f.flush()
        f.close()
    #@-node:ekr.20031218072017.1464:weave
    #@-node:ekr.20031218072017.3289:Export
    #@+node:ekr.20031218072017.3305:Utilities
    #@+node:ekr.20031218072017.3306:createHeadline
    def createHeadline (self,parent,body,headline):

        # g.trace("parent,headline:",parent,headline)
        # Create the vnode.
        v = parent.insertAsLastChild()
        v.initHeadString(headline,self.encoding)
        # Set the body.
        if len(body) > 0:
            self.c.setBodyString(v,body,self.encoding)
        return v
    #@-node:ekr.20031218072017.3306:createHeadline
    #@+node:ekr.20031218072017.3307:error
    def error (self,s): g.es(s)
    #@-node:ekr.20031218072017.3307:error
    #@+node:ekr.20031218072017.3308:getLeadingIndent
    def getLeadingIndent (self,s,i):

        """Return the leading whitespace of a line, ignoring blank and comment lines."""

        i = g.find_line_start(s,i)
        while i < len(s):
            # g.trace(g.get_line(s,i))
            j = g.skip_ws(s,i) # Bug fix: 2/14/03
            if g.is_nl(s,j) or g.match(s,j,"#"): # Bug fix: 2/14/03
                i = g.skip_line(s,i) # ignore blank lines and comment lines.
            else:
                i, width = g.skip_leading_ws_with_indent(s,i,self.tab_width)
                # g.trace("returns:",width)
                return width
        # g.trace("returns:0")
        return 0
    #@-node:ekr.20031218072017.3308:getLeadingIndent
    #@+node:ekr.20031218072017.3309:isDocStart and isModuleStart
    # The start of a document part or module in a noweb or cweb file.
    # Exporters may have to test for @doc as well.

    def isDocStart (self,s,i):

        if not g.match(s,i,"@"):
            return False

        j = g.skip_ws(s,i+1)
        if g.match(s,j,"%defs"):
            return False
        elif self.webType == "cweb" and g.match(s,i,"@*"):
            return True
        else:
            return g.match(s,i,"@ ") or g.match(s,i,"@\t") or g.match(s,i,"@\n")

    def isModuleStart (self,s,i):

        if self.isDocStart(s,i):
            return True
        else:
            return self.webType == "cweb" and (
                g.match(s,i,"@c") or g.match(s,i,"@p") or
                g.match(s,i,"@d") or g.match(s,i,"@f"))
    #@-node:ekr.20031218072017.3309:isDocStart and isModuleStart
    #@+node:ekr.20031218072017.3310:massageBody & helper
    def massageBody (self,s,methodKind):

        # g.trace(s)
        # g.trace(g.get_line(s,0))
        c = self.c
        if self.treeType == "@file":
            if self.fileType == ".py": # 7/31/02: was "py"
                return self.undentBody(s)
            else:
                newBody, comment = self.skipLeadingComments(s)
                newBody = self.undentBody(newBody)
                newLine = g.choose(g.is_nl(newBody,0),"\n","\n\n")
                if len(comment) > 0:
                    return comment + "\n@c" + newLine + newBody
                else:
                    return newBody
        else:
            # Inserts < < self.methodName methodKind > > =
            cweb = self.fileType == "c" and not c.use_noweb_flag
            lb = g.choose(cweb,"@<","<<")
            rb = g.choose(cweb,"@>=",">>=")
            intro = lb + " " + self.methodName + " " + methodKind + " " + rb
            if self.fileType == ".py": # 7/31/02: was "py"
                newBody = self.undentBody(s)
                newLine = g.choose(g.is_nl(newBody,0),"\n","\n\n")
                return intro + newLine + newBody
            else:
                newBody, comment = self.skipLeadingComments(s)
                newBody = self.undentBody(newBody)
                newLine = g.choose(g.is_nl(newBody,0),"\n","\n\n")
                if len(comment) > 0:
                    return comment + "\n" + intro + newLine + newBody
                else:
                    return intro + newLine + newBody
    #@+node:ekr.20031218072017.3315:skipLeadingComments
    def skipLeadingComments (self,s):

        """Skips all leading comments in s, returning the remaining body text and the massaged comment text.

        Returns (body, comment)"""

        # g.trace(g.get_line(s,0))
        s_original = s
        s = s.lstrip()
        i = 0 ; comment = ""
        if self.fileType in [".c", ".cpp"]: # 11/2/02: don't mess with java comments.
            #@        << scan for C-style comments >>
            #@+node:ekr.20031218072017.3316:<< scan for C-style comments >>
            while i < len(s):
                if g.match(s,i,"//"): # Handle a C++ comment.
                    while g.match(s,i,'/'):
                        i += 1
                    j = i ; i = g.skip_line(s,i)
                    comment = comment + self.massageComment(s[j:i]) + "\n"
                    # 8/2/02: Preserve leading whitespace for undentBody
                    i = g.skip_ws(s,i)
                    i = g.skip_blank_lines(s,i)
                elif g.match(s,i,"/*"): # Handle a block C comment.
                    j = i + 2 ; i = g.skip_block_comment (s,i)
                    k = g.choose(g.match(s,i-2,"*/"),i-2,i)
                    if self.fileType == ".java":
                        # 8/2/02: a hack: add leading whitespace then remove it.
                        comment = self.undentBody(comment)
                        comment2 = ' ' * 2 + s[j:k]
                        comment2 = self.undentBody(comment2)
                        comment = comment + comment2 + "\n"
                    else:
                        comment = comment + self.massageComment(s[j:k]) + "\n"
                    # 8/2/02: Preserve leading whitespace for undentBody
                    i = g.skip_ws(s,i)
                    i = g.skip_blank_lines(s,i)
                else: break
            #@-node:ekr.20031218072017.3316:<< scan for C-style comments >>
            #@nl
        elif self.fileType == ".lua":
            #@        << scan for Lua comments >>
            #@+node:ekr.20060328112327.1:<< scan for Lua comments >>
            while i < len(s):
                if g.match(s,i,"--"): # Handle a Lua line comment.
                    while g.match(s,i,'/'):
                        i += 1
                    j = i ; i = g.skip_line(s,i)
                    comment = comment + self.massageComment(s[j:i]) + "\n"
                    # 8/2/02: Preserve leading whitespace for undentBody
                    i = g.skip_ws(s,i)
                    i = g.skip_blank_lines(s,i)
                else: break
            #@-node:ekr.20060328112327.1:<< scan for Lua comments >>
            #@nl
        elif self.fileType == ".pas":
            #@        << scan for Pascal comments >>
            #@+node:ekr.20031218072017.3317:<< scan for Pascal comments >>
            while i < len(s):
                if g.match(s,i,"//"): # Handle a Pascal line comment.
                    while g.match(s,i,'/'):
                        i += 1
                    j = i ; i = g.skip_line(s,i)
                    comment = comment + self.massageComment(s[j:i]) + "\n"
                    # 8/2/02: Preserve leading whitespace for undentBody
                    i = g.skip_ws(s,i)
                    i = g.skip_blank_lines(s,i)
                elif g.match(s,i,'(*'):
                    j = i + 1 ; i = g.skip_pascal_block_comment(s,i)
                    comment = comment + self.massageComment(s[j:i]) + "\n"
                    # 8/2/02: Preserve leading whitespace for undentBody
                    i = g.skip_ws(s,i)
                    i = g.skip_blank_lines(s,i)
                else: break
            #@-node:ekr.20031218072017.3317:<< scan for Pascal comments >>
            #@nl
        elif self.fileType == ".py":
            #@        << scan for Python comments >>
            #@+node:ekr.20031218072017.3318:<< scan for Python comments >>
            while i < len(s) and g.match(s,i,'#'):
                j = i + 1 ; i = g.skip_line(s,i)
                comment = self.undentBody(comment)
                comment = comment + self.massageComment(s[j:i]) + "\n"
                # 8/2/02: Preserve leading whitespace for undentBody
                i = g.skip_ws(s,i)
                i = g.skip_blank_lines(s,i)
            #@-node:ekr.20031218072017.3318:<< scan for Python comments >>
            #@nl
        comment = string.strip(comment)
        if len(comment) == 0:
            return s_original, "" # Bug fix: 11/2/02: don't skip leading whitespace!
        elif self.treeType == "@file":
            return s[i:], "@ " + comment
        else:
            return s[i:], "@ " + comment + "\n"
    #@-node:ekr.20031218072017.3315:skipLeadingComments
    #@-node:ekr.20031218072017.3310:massageBody & helper
    #@+node:ekr.20031218072017.3311:massageComment
    def massageComment (self,s):

        """Returns s with all runs of whitespace and newlines converted to a single blank.

        Also removes leading and trailing whitespace."""

        # g.trace(g.get_line(s,0))
        s = string.strip(s)
        s = string.replace(s,"\n"," ")
        s = string.replace(s,"\r"," ")
        s = string.replace(s,"\t"," ")
        s = string.replace(s,"  "," ")
        s = string.strip(s)
        return s
    #@-node:ekr.20031218072017.3311:massageComment
    #@+node:ekr.20031218072017.3312:massageWebBody
    def massageWebBody (self,s):

        theType = self.webType
        lb = g.choose(theType=="cweb","@<","<<")
        rb = g.choose(theType=="cweb","@>",">>")
        #@    << Remove most newlines from @space and @* sections >>
        #@+node:ekr.20031218072017.3313:<< Remove most newlines from @space and @* sections >>
        i = 0
        while i < len(s):
            progress = i
            i = g.skip_ws_and_nl(s,i)
            if self.isDocStart(s,i):
                # Scan to end of the doc part.
                if g.match(s,i,"@ %def"):
                    # Don't remove the newline following %def
                    i = g.skip_line(s,i) ; start = end = i
                else:
                    start = end = i ; i += 2
                while i < len(s):
                    progress2 = i
                    i = g.skip_ws_and_nl(s,i)
                    if self.isModuleStart(s,i) or g.match(s,i,lb):
                        end = i ; break
                    elif theType == "cweb": i += 1
                    else: i = g.skip_to_end_of_line(s,i)
                    assert (i > progress2)
                # Remove newlines from start to end.
                doc = s[start:end]
                doc = string.replace(doc,"\n"," ")
                doc = string.replace(doc,"\r","")
                doc = string.strip(doc)
                if doc and len(doc) > 0:
                    if doc == "@":
                        doc = g.choose(self.webType=="cweb", "@ ","@\n")
                    else:
                        doc += "\n\n"
                    # g.trace("new doc:",doc)
                    s = s[:start] + doc + s[end:]
                    i = start + len(doc)
            else: i = g.skip_line(s,i)
            assert (i > progress)
        #@-node:ekr.20031218072017.3313:<< Remove most newlines from @space and @* sections >>
        #@nl
        #@    << Replace abbreviated names with full names >>
        #@+node:ekr.20031218072017.3314:<< Replace abbreviated names with full names >>
        i = 0
        while i < len(s):
            progress = i
            # g.trace(g.get_line(s,i))
            if g.match(s,i,lb):
                i += 2 ; j = i ; k = g.find_on_line(s,j,rb)
                if k > -1:
                    name = s[j:k]
                    name2 = self.cstLookup(name)
                    if name != name2:
                        # Replace name by name2 in s.
                        # g.trace("replacing %s by %s" % (name,name2))
                        s = s[:j] + name2 + s[k:]
                        i = j + len(name2)
            i = g.skip_line(s,i)
            assert (i > progress)
        #@-node:ekr.20031218072017.3314:<< Replace abbreviated names with full names >>
        #@nl
        s = string.rstrip(s)
        return s
    #@-node:ekr.20031218072017.3312:massageWebBody
    #@+node:ekr.20031218072017.1463:setEncoding
    def setEncoding (self):

        # scanDirectives checks the encoding: may return None.
        theDict = g.scanDirectives(self.c)
        encoding = theDict.get("encoding")
        if encoding and g.isValidEncoding(encoding):
            self.encoding = encoding
        else:
            self.encoding = g.app.tkEncoding # 2/25/03

        # print self.encoding
    #@-node:ekr.20031218072017.1463:setEncoding
    #@+node:ekr.20031218072017.3319:undentBody
    # We look at the first line to determine how much leading whitespace to delete.

    def undentBody (self,s):

        """Removes extra leading indentation from all lines."""

        # g.trace(s)
        i = 0 ; result = ""
        # Copy an @code line as is.
        if g.match(s,i,"@code"):
            j = i ; i = g.skip_line(s,i) # don't use get_line: it is only for dumping.
            result += s[j:i]
        # Calculate the amount to be removed from each line.
        undent = self.getLeadingIndent(s,i)
        if undent == 0: return s
        while i < len(s):
            j = i ; i = g.skip_line(s,i) # don't use get_line: it is only for dumping.
            line = s[j:i]
            # g.trace(line)
            line = g.removeLeadingWhitespace(line,undent,self.tab_width)
            result += line
        return result
    #@-node:ekr.20031218072017.3319:undentBody
    #@-node:ekr.20031218072017.3305:Utilities
    #@-others

class leoImportCommands (baseLeoImportCommands):
    """A class that implements Leo's import commands."""
    pass
#@-node:ekr.20031218072017.3206:@thin leoImport.py
#@-leo
