# -*- coding: utf-8 -*-
#@+leo-ver=4-thin
#@+node:ekr.20031218072017.3206:@thin leoImport.py
#@@first
# The line above is required so non-ascii characters will be valid in unit tests.

#@@language python
#@@tabwidth -4
#@@pagewidth 80
#@@encoding utf-8
# The line above is required so the unit test that simulates an @auto leoImport.py will work!

# Minor to do: can leo determine the proper kind of import to do?  Should it?
# Minor to do: can @auto handle files containing Leo sentinels?

import leoGlobals as g
import leoTest # Support for unit tests.

import string

class baseLeoImportCommands:
    """The base class for Leo's import commands."""
    #@    @+others
    #@+node:ekr.20031218072017.3207:import.__init__
    def __init__ (self,c):

        self.c = c
        self._forcedGnxPositionList = []
        self.encoding = g.app.tkEncoding # 2/25/03: was "utf-8"
        self.errors = 0
        self.fileName = None # The original file name, say x.cpp
        self.fileType = None # ".py", ".c", etc.
        self.methodName = None # x, as in < < x methods > > =
        self.output_newline = g.getOutputNewline(c=c) # Value of @bool output_newline
        self.rootLine = "" # Empty or @root + self.fileName
        self.tabwidth = c.tab_width # The tab width in effect in the c.currentPosition.
        self.trace = c.config.getBool('trace_import')
        self.treeType = "@file" # "@root" or "@file"
        self.webType = "@noweb" # "cweb" or "noweb"
        self.web_st = [] # noweb symbol table.
    #@-node:ekr.20031218072017.3207:import.__init__
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
    def removeSentinelsCommand (self,paths,toString=False):

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
                if not toString: g.es("invalid @+leo sentinel in " + fileName)
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
            if toString:
                return s
            else:
                #@            << Write s into newFileName >>
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
                return None
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
    #@+node:ekr.20041126042730:getTabWidth
    def getTabWidth (self):

        d = g.scanDirectives(self.c)
        w = d.get("tabwidth")
        if w not in (0,None):
            return w
        else:
            return self.c.tab_width
    #@-node:ekr.20041126042730:getTabWidth
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
    #@+node:ekr.20031218072017.3311:massageComment
    def massageComment (self,s):

        '''Returns s with all runs of whitespace and newlines converted to a single blank.

        Also removes leading and trailing whitespace.'''

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
    def setEncoding (self,p=None):

        # scanDirectives checks the encoding: may return None.
        c = self.c
        if p is None: p = c.currentPosition()
        theDict = g.scanDirectives(c,p)
        encoding = theDict.get("encoding")
        if encoding and g.isValidEncoding(encoding):
            self.encoding = encoding
        else:
            self.encoding = g.app.tkEncoding # 2/25/03

        # print self.encoding
    #@-node:ekr.20031218072017.1463:setEncoding
    #@-node:ekr.20031218072017.3305:Utilities
    #@+node:ekr.20031218072017.3209:Import
    #@+node:ekr.20031218072017.3210:createOutline
    def createOutline (self,fileName,parent,atAuto=False,s=None,ext=None):

        c = self.c ; u = c.undoer ; s1 = s
        junk,self.fileName = g.os_path_split(fileName)
        self.methodName,self.fileType = g.os_path_splitext(self.fileName)
        self.setEncoding(p=parent)
        # g.trace(self.fileName,self.fileType)
        # All file types except the following just get copied to the parent node.
        if not ext: ext = self.fileType
        ext = ext.lower()
        if not s:
            #@        << Read file into s >>
            #@+node:ekr.20031218072017.3211:<< Read file into s >>
            try:
                fileName = g.os_path_normpath(fileName)
                theFile = open(fileName)
                s = theFile.read()
                s = g.toUnicode(s,self.encoding)
                theFile.close()
            except IOError:
                g.es("can not open %s%s" % (g.choose(atAuto,'@auto ',''),fileName),color='red')
                leoTest.fail()
                return None
            #@-node:ekr.20031218072017.3211:<< Read file into s >>
            #@nl

        # Create the top-level headline.
        if atAuto:
            p = parent.copy()
            c.beginUpdate()
            try:
                p.setTnodeText('')
            finally:
                c.endUpdate(False)
        else:
            undoData = u.beforeInsertNode(parent)
            p = parent.insertAsLastChild()
            if self.treeType == "@file" and not s1:
                p.initHeadString("@nosent " + fileName)
            else:
                p.initHeadString(fileName)
            u.afterInsertNode(p,'Import',undoData)

        self.rootLine = g.choose(self.treeType=="@file","","@root-code "+self.fileName+'\n')

        if ext in (".c", ".cpp", ".cxx"):
            self.scanCText(s,p,atAuto=atAuto)
        elif ext == '.c#':
            self.scanCSharpText(s,p,atAuto=atAuto)
        elif ext == ".el":
            self.scanElispText(s,p,atAuto=atAuto)
        elif ext == ".java":
            self.scanJavaText(s,p,atAuto=atAuto)
        elif ext == ".js":
            self.scanJavaScriptText(s,p,atAuto=atAuto)
        elif ext == ".pas":
            self.scanPascalText(s,p,atAuto=atAuto)
        elif ext in (".py", ".pyw"):
            self.scanPythonText(s,p,atAuto=atAuto)
        elif ext == ".php":
            self.scanPHPText(s,p,atAuto=atAuto)
        else:
            self.scanUnknownFileType(s,p,ext,atAuto=atAuto)

        p.contract()
        return p
    #@-node:ekr.20031218072017.3210:createOutline
    #@+node:ekr.20070806111212:readAtAutoNodes (importCommands) & helper
    def readAtAutoNodes (self):

        c = self.c
        p = c.currentPosition() ; after = p.nodeAfterTree()

        c.beginUpdate()
        try:
            found = False
            while p and p != after:
                if p.isAtAutoNode():
                    if p.isAtIgnoreNode():
                        g.es_print('ignoring %s' % (p.headString()),color='blue')
                        p.moveToThreadNext()
                    else:
                        self.readOneAtAutoNode(p)
                        found = True
                        p.moveToNodeAfterTree()
                else:
                    p.moveToThreadNext()
            g.es(g.choose(found,'finished','no @auto nodes in the selected tree'),color='blue')
        finally:
            c.endUpdate()

    #@+node:ekr.20070807084545:readOneAtAutoNode
    def readOneAtAutoNode(self,p):

        '''Read the @auto node at p'''

        c = self.c

        self.createOutline(
            fileName=p.atAutoNodeName(),
            parent=p.copy(),
            atAuto=True)

        # Force an update of the body pane.
        c.setBodyString(p,p.bodyString())
        c.frame.body.onBodyChanged(undoType=None)
    #@-node:ekr.20070807084545:readOneAtAutoNode
    #@-node:ekr.20070806111212:readAtAutoNodes (importCommands) & helper
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
    def importFilesCommand (self,files=None,treeType=None):
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
    #@+node:ekr.20031218072017.3241:Scanners for createOutline
    #@+node:ekr.20070703122141.65: class baseScannerClass
    class baseScannerClass:

        '''The base class for all import scanner classes.
        This class contains common utility methods.'''

        #@    @+others
        #@+node:ekr.20070703122141.66:baseScannerClass.__init__
        def __init__ (self,importCommands,atAuto,language):

            ic = importCommands

            self.atAuto = atAuto
            self.c = c = ic.c
            self.classId = None # The identifier containing the class tag: 'class', 'interface', 'namespace', etc.
            self.classIndent = 0 # The indentation of the start of the class.
            self.codeEnd = None
                # The character after the last character of the class, method or function.
                # An error will be given if this is not a newline.
            self.encoding = ic.encoding # g.app.tkEncoding
            self.errors = 0
            ic.errors = 0
            self.errorLines = []
            self.extraIdChars = ''
            self.fileName = ic.fileName # The original filename.
            self.fileType = ic.fileType # The extension,  '.py', '.c', etc.
            self.fullChecks = c.config.getBool('full_import_checks')
            self.importCommands = ic
            self.indentRefFlag = None # None, True or False.
            self.language = language
            self.methodName = ic.methodName # x, as in < < x methods > > =
            self.output_newline = ic.output_newline # = c.config.getBool('output_newline')
            self.output_indent = 0 # The minimum indentation presently in effect.
            self.root = None # The top-level node of the generated tree.
            self.rootLine = ic.rootLine # '' or @root + self.fileName
            self.sigEnd = None # The index of the end of the signature.
            self.sigId = None # The identifier contained in the signature, i.e., the function or method name.
            self.sigStart = None
                # The start of the line containing the signature.
                # An error will be given if something other than whitespace precedes the signature.
            self.startSigIndent = None
            self.tab_width = ic.getTabWidth() # The tab width in effect in the c.currentPosition.
            self.trace = False or ic.trace # = c.config.getBool('trace_import')
            self.treeType = ic.treeType # '@root' or '@file'
            self.webType = ic.webType # 'cweb' or 'noweb'  

            # Compute language ivars.
            delim1,delim2,delim3 = g.set_delims_from_language(language)
            self.comment_delim = delim1

            # Create the ws equivalent to one tab.
            if self.tab_width < 0:
                self.tab_ws = ' '*abs(self.tab_width)
            else:
                self.tab_ws = '\t'

            # May be overridden in subclasses.
            self.blockCommentDelim1 = None
            self.blockCommentDelim2 = None
            self.blockDelim1 = '{'
            self.blockDelim2 = '}'
            self.classTags = ['class',] # tags that start a tag.
            self.functionTags = []
            self.hasClasses = True
            self.hasFunctions = True
            self.lineCommentDelim = None
            self.lineCommentDelim2 = None
            self.outerBlockDelim1 = None
            self.outerBlockDelim2 = None
            self.sigHeadExtraTokens = [] # Extra tokens valid in head of signature.
            self.sigFailTokens = []
                # A list of strings that abort a signature when seen in a tail.
                # For example, ';' and '=' in C.

            self.strict = False # True if leading whitespace is very significant.
        #@-node:ekr.20070703122141.66:baseScannerClass.__init__
        #@+node:ekr.20070808115837:Checking
        #@+node:ekr.20070703122141.102:check
        def check (self,s,parent):

            '''Make sure the generated nodes are equivalent to the original file.

            1. Regularize and check leading whitespace.
            2. Check that a trial write produces the original file.

            Return True if the nodes are equivalent to the original file.
            '''

            if self.fullChecks and self.treeType == '@file':
                return self.checkTrialWrite()
            else:
                return True
        #@-node:ekr.20070703122141.102:check
        #@+node:ekr.20070703122141.104:checkTrialWrite & tests
        def checkTrialWrite (self,s1=None,s2=None):

            '''Return True if a trial write produces the original file.'''

            # s1 and s2 are for unit testing.

            c = self.c ; at = c.atFileCommands

            if s1 is None and s2 is None:
                at.write(self.root,
                    nosentinels=True,thinFile=False,
                    scriptWrite=False,toString=True,
                    write_strips_blank_lines=False)
                s1,s2 = self.file_s, at.stringOutput

            s1 = g.toUnicode(s1,self.encoding)
            s2 = g.toUnicode(s2,self.encoding)

            # Make sure we have a trailing newline in both strings.
            s1 = s1.replace('\r','')
            s2 = s2.replace('\r','')
            if not s1.endswith('\n'): s1 = s1 + '\n'
            if not s2.endswith('\n'): s2 = s2 + '\n'

            if s1 == s2: return True

            lines1 = g.splitLines(s1) ; n1 = len(lines1)
            lines2 = g.splitLines(s2) ; n2 = len(lines2)

            # g.trace('lines1',lines1)
            # g.trace('lines2',lines2)

            ok = True ; bad_i = 0
            for i in xrange(max(n1,n2)):
                ok = self.compareHelper(lines1,lines2,i,self.strict)
                if not ok:
                    bad_i = i + 1
                    break

            if g.app.unitTesting:
                d = g.app.unitTestDict
                ok = d.get('expectedMismatchLine') == d.get('actualMismatchLine')
                # Unit tests do not generate errors unless the mismatch line does not match.

            if not ok:
                self.reportMismatch(lines1,lines2,bad_i)

            return ok
        #@+node:ekr.20070816103348:@test checkTriailWrite
        if g.unitTesting:

            ic = c.importCommands
            runner = ic.baseScannerClass(ic,atAuto=True,language='python')
            runner.root = p.copy()

            g.app.unitTestDict ['expectedErrors'] = 1
            g.app.unitTestDict ['expectedMismatchLine'] = 2

            s1 = g.toUnicode('line1 Ä, ڱ,  궯, 奠\nline2\n',encoding='utf-8')
            s2 = g.toUnicode('line1 Ä, ڱ,  궯, 奠\nline2a\n',encoding='utf-8')
            runner.checkTrialWrite(s1=s1,s2=s2)
        #@-node:ekr.20070816103348:@test checkTriailWrite
        #@-node:ekr.20070703122141.104:checkTrialWrite & tests
        #@+node:ekr.20070730093735:compareHelper & tests
        def compareHelper (self,lines1,lines2,i,strict):

            '''Compare lines1[i] and lines2[i].
            strict is True if leading whitespace is very significant.'''

            def pr(*args,**keys): #compareHelper
                g.es_print(color='blue',*args,**keys)

            d = g.app.unitTestDict
            expectedMismatch = g.app.unitTesting and d.get('expectedMismatchLine')

            if i >= len(lines1):
                if i != expectedMismatch or not g.app.unitTesting:
                    pr('extra lines')
                    for line in lines2[i:]:
                        pr(repr(line))
                d ['actualMismatchLine'] = i
                return False

            if i >= len(lines2):
                if i != expectedMismatch or not g.app.unitTesting:
                    g.es_print('missing lines')
                    for line in lines2[i:]:
                        g.es_print(repr(line))
                d ['actualMismatchLine'] = i
                return False

            line1,line2 = lines1[i],lines2[i]
            if line1 == line2:
                return True # An exact match.
            elif not line1.strip() and not line2.strip():
                return True # Blank lines compare equal.
            elif not strict and line1.lstrip() == line2.lstrip():
                return True # A match excluding leading whitespace.
            else:
                if not g.app.unitTesting or i+1 != expectedMismatch:
                    # g.es_print('compareHelper')
                    g.es_print('*** first mismatch at line %d' % (i+1))
                    g.es_print('original line:  %s' % line1)
                    g.es_print('generated line: %s' % line2)
                d ['actualMismatchLine'] = i+1
                # g.trace('lines 1...\n',repr(lines1),'\nlines2...\n',repr(lines2))
                return False
        #@+node:ekr.20070816101019:@test compareHelper
        if g.unitTesting:

            ic = c.importCommands
            runner = ic.baseScannerClass(ic,atAuto=True,language='python')
            i = 0
            lines1 = ['abc',]
            lines2 = ['xyz',]

            g.app.unitTestDict ['expectedErrors'] = 1
            g.app.unitTestDict ['expectedMismatchLine'] = 1

            runner.compareHelper(lines1,lines2,i,strict=True)
        #@-node:ekr.20070816101019:@test compareHelper
        #@-node:ekr.20070730093735:compareHelper & tests
        #@+node:ekr.20070911110507:reportMismatch & test
        def reportMismatch (self,lines1,lines2,bad_i):

            def pr(*args,**keys): # reportMismatch
                g.es_print(color='blue',*args,**keys)

            kind = g.choose(self.atAuto,'@auto','import command')

            self.error(
                '%s did not import the file perfectly\nfirst mismatched line: %d\n%s' % (
                    kind,bad_i,repr(lines2[bad_i-1])))

            if len(lines1) < 100:
                pr('input...')
                for i in xrange(len(lines1)):
                    pr('%3d %s' % (i,lines1[i]),newline=False)
                pr('output...')
                for i in xrange(len(lines2)):
                    pr('%3d %s' % (i,lines2[i]),newline=False)

            return False
        #@+node:ekr.20070913084008:minitest of pr
        if False: # Don't clutter the unit tests.

            def pr(*args,**keys): # reportMismatch test
                g.es_print(color='blue',*args,**keys)

            pr('input...')
            pr('newline=False:',newline=False)
            pr('after')
            pr('done')
        #@-node:ekr.20070913084008:minitest of pr
        #@-node:ekr.20070911110507:reportMismatch & test
        #@-node:ekr.20070808115837:Checking
        #@+node:ekr.20070706084535:Code generation
        #@+at 
        #@nonl
        # None of these methods should ever need to be overridden in 
        # subclasses.
        # 
        #@-at
        #@+node:ekr.20070707073044.1:addRef
        def addRef (self,parent):

            '''Create an unindented @others or section reference in the parent node.'''

            c = self.c

            if self.treeType == '@file':
                c.appendStringToBody(parent,'@others\n')

            if self.treeType == '@root' and self.methodsSeen:
                c.appendStringToBody(parent,
                    g.angleBrackets(' ' + self.methodName + ' methods ') + '\n\n')
        #@-node:ekr.20070707073044.1:addRef
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
            if self.treeType == '@file':
                prefix = ''
            else:
                prefix = g.angleBrackets(' ' + headline + ' methods ') + '=\n\n'
                self.methodsSeen = True

            # Create the node.
            self.createHeadline(parent,prefix + body,headline)

        #@-node:ekr.20070707085612:createFunctionNode
        #@+node:ekr.20070703122141.77:createHeadline
        def createHeadline (self,parent,body,headline):

            # g.trace('parent,headline:',parent,headline)

            # Create the node.
            p = parent.insertAsLastChild()
            p.initHeadString(headline,self.encoding)

            # Set the body.
            if body:
                self.c.setBodyString(p,body,self.encoding)
            return p
        #@-node:ekr.20070703122141.77:createHeadline
        #@+node:ekr.20070703122141.79:getLeadingIndent
        def getLeadingIndent (self,s,i,ignoreComments=True):

            '''Return the leading whitespace of a line.
            Ignore blank and comment lines if ignoreComments is True'''

            width = 0
            i = g.find_line_start(s,i)
            if ignoreComments:
                while i < len(s):
                    # g.trace(g.get_line(s,i))
                    j = g.skip_ws(s,i)
                    if g.is_nl(s,j) or g.match(s,j,self.comment_delim):
                        i = g.skip_line(s,i) # ignore blank lines and comment lines.
                    else:
                        i, width = g.skip_leading_ws_with_indent(s,i,self.tab_width)
                        break      
            else:
                i, width = g.skip_leading_ws_with_indent(s,i,self.tab_width)

            # g.trace('returns:',width)
            return width
        #@-node:ekr.20070703122141.79:getLeadingIndent
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

            result = ''.join(result)
            return result
        #@-node:ekr.20070709094002:indentBody
        #@+node:ekr.20070705085335:insertIgnoreDirective
        def insertIgnoreDirective (self,parent):

            self.c.appendStringToBody(parent,'@ignore')

            if not g.unitTesting:
                g.es_print('inserting @ignore',color='blue')
        #@-node:ekr.20070705085335:insertIgnoreDirective
        #@+node:ekr.20070703122141.81:massageComment
        def massageComment (self,s):

            '''Return s with leading and trailing whitespace removed and all other
            runs of whitespace and newlines converted to a single blank.'''

            s = s.strip()
            s = s.replace('\n',' ')
            s = s.replace('\r',' ')
            s = s.replace('\t',' ')
            s = s.replace('  ',' ')
            s = s.strip()
            return s
        #@-node:ekr.20070703122141.81:massageComment
        #@+node:ekr.20070707113832.1:putClass & helpers
        def putClass (self,s,i,sigStart,sigEnd,codeEnd,start,parent):

            '''Creates a child node c of parent for the class, and a child of c for each def in the class.'''

            # Enter a new class 1: save the old class info.
            oldClassIndent = self.classIndent
            oldMethodName = self.methodName
            oldStartSigIndent = self.startSigIndent

            # Enter a new class 2: init the new class info.
            self.classIndent = self.getIndent(s,i)
            self.classLines = []
            self.indentRefFlag = None

            class_kind = self.classId
            class_name = self.sigId
            headline = '%s %s' % (class_kind,class_name)
            self.methodName = headline

            # Compute the starting lines of the class.
            prefix = self.createClassNodePrefix()
            if not self.sigId:
                g.trace('Can not happen: no sigId')
                sigId = 'Unknown class name'
            classHead = s[start:sigEnd]
            i = self.extendSignature(s,sigEnd)
            extend = s[sigEnd:i]
            if extend:
                classHead = classHead + extend

            # Create the class node.
            class_node = self.createHeadline(parent,'',headline)

            undentVal = self.getLeadingIndent(classHead,0)

            # Call the helper to parse the inner part of the class.
            putRef,indentFlag,classDelim,decls,trailing = self.putClassHelper(s,i,codeEnd,class_name,class_node)

            # g.trace(class_name,'indent',self.classIndent,'indentFlag',indentFlag)

            # Set the body of the class node.
            ref = putRef and self.getClassNodeRef(class_name,indentFlag) or ''

            # Remove the leading whitespace only from the classHead and trailing parts.
            result = (
                prefix +
                self.undentBy(classHead,undentVal) +
                self.undentBy(classDelim,undentVal) +
                ref +
                self.undentBy(trailing,undentVal))

            # Append the result to the class node.
            self.appendTextToClassNode(class_node,result)

            # Exit the new class: restore the previous class info.
            self.classIndent = oldClassIndent
            self.methodName = oldMethodName
            self.startSigIndent = oldStartSigIndent
        #@+node:ekr.20070703122141.106:appendRefToClassNode
        def getClassNodeRef (self,class_name,indentFlag):

            '''Insert the proper body text in the class_vnode.'''

            if self.treeType == '@file':
                s = '@others'
            else:
                s = g.angleBrackets(' class %s methods ' % (class_name))

            # Increase effective indentation by the width of self.tab_ws.
            # g.trace('class_name',class_name,indentFlag)

            if indentFlag:
                return '%s%s\n' % (self.tab_ws,s)
            else:
                return '%s\n' % (s)

            # if indentFlag:
                # self.appendTextToClassNode(class_node,'%s%s\n' % (self.tab_ws,s))
            # else:
                # self.appendTextToClassNode(class_node,'%s\n' % s)
        #@-node:ekr.20070703122141.106:appendRefToClassNode
        #@+node:ekr.20070707190351:appendTextToClassNode
        def appendTextToClassNode (self,class_node,s):

            c = self.c

            c.appendStringToBody(class_node,s) 
        #@-node:ekr.20070707190351:appendTextToClassNode
        #@+node:ekr.20070703122141.105:createClassNodePrefix
        def createClassNodePrefix (self):

            '''Create the class node prefix.'''

            if  self.treeType == '@file':
                prefix = ''
            else:
                prefix = g.angleBrackets(' ' + self.methodName + ' methods ') + '=\n\n'
                self.methodsSeen = True

            return prefix
        #@-node:ekr.20070703122141.105:createClassNodePrefix
        #@+node:ekr.20070707171329:putClassHelper
        def putClassHelper(self,s,i,end,class_name,class_node):

            '''s contains the body of a class, not including the signature.

            Parse s for inner methods and classes, and create nodes.'''

            # Increase the output indentation (used only in startsHelper).
            # This allows us to detect over-indented classes and functions.
            old_output_indent = self.output_indent
            self.output_indent += abs(self.tab_width)

            # Parse the decls.
            start = i = self.skipDecls(s,i,end,inClass=True)
            decls = s[start:i]

            # Parse the rest of the class.
            delim1, delim2 = self.outerBlockDelim1, self.outerBlockDelim2
            if g.match(s,i,delim1):
                # Do *not* use g.skip_ws_and_nl here!
                j = g.skip_ws(s,i + len(delim1))
                if g.is_nl(s,j): j = g.skip_nl(s,j)
                classDelim = s[i:j]
                end2 = self.skipBlock(s,i,delim1=delim1,delim2=delim2)
                start,putRef,indentFlag = self.scanHelper(s,j,end=end2,parent=class_node,kind='class')
            else:
                classDelim = ''
                start,putRef,indentFlag = self.scanHelper(s,i,end=end,parent=class_node,kind='class')

            # Restore the output indentation.
            self.output_indent = old_output_indent

            # Return the results.
            trailing = s[start:end]
            return putRef,indentFlag,classDelim,decls,trailing
        #@-node:ekr.20070707171329:putClassHelper
        #@-node:ekr.20070707113832.1:putClass & helpers
        #@+node:ekr.20070707082432:putFunction
        def putFunction (self,s,sigStart,codeEnd,start,parent):

            '''Create a node of parent for a function defintion.'''

            trace = False and self.trace

            # Enter a new function: save the old function info.
            oldStartSigIndent = self.startSigIndent

            if self.sigId:
                headline = self.sigId
            else:
                g.trace('Can not happen: no sigId')
                headline = 'unknown function'

            body1 = self.undentBody(s[start:sigStart],ignoreComments=False)

            body2 = self.undentBody(s[sigStart:codeEnd])
            body = body1 + body2
            if trace: g.trace('body\n%s' % body)

            if not body.endswith('\n'):
                self.error(
                    'function %s does not end with a newline; one will be added\n%s' % (
                        self.sigId,g.get_line(s,codeEnd)))
                g.trace(g.callers())

            self.createFunctionNode(headline,body,parent)

            # Exit the function: restore the function info.
            self.startSigIndent = oldStartSigIndent
        #@-node:ekr.20070707082432:putFunction
        #@+node:ekr.20070705094630:putRootText
        def putRootText (self,p):

            c = self.c

            c.appendStringToBody(p,'%s@language %s\n@tabwidth %d\n' % (
                self.rootLine,self.language,self.tab_width))
        #@-node:ekr.20070705094630:putRootText
        #@+node:ekr.20070703122141.88:undentBody & undentBy
        def undentBody (self,s,ignoreComments=True):

            '''Remove the first line's leading indentation from all lines of s.'''

            trace = False
            if trace: g.trace('before...\n',g.listToString(g.splitLines(s)))

            # Copy an @code line as is.
            # i = 0
            # if g.match(s,i,'@code'):
                # j = i ; i = g.skip_line(s,i) # don't use get_line: it is only for dumping.
                # result += s[j:i]

            # Calculate the amount to be removed from each line.
            undentVal = self.getLeadingIndent(s,0,ignoreComments=ignoreComments)
            if undentVal == 0:
                return s
            else:
                result = self.undentBy(s,undentVal)
                # result = ''.join([
                    # g.removeLeadingWhitespace(line,undent,self.tab_width)
                        # for line in g.splitLines(s)])
                if trace: g.trace('after...\n',g.listToString(g.splitLines(result)))
                return result

        def undentBy (self,s,undentVal):
            return ''.join(
                [g.removeLeadingWhitespace(line,undentVal,self.tab_width)
                    for line in g.splitLines(s)])
        #@-node:ekr.20070703122141.88:undentBody & undentBy
        #@+node:ekr.20070801074524:underindentedComment & underindentedLine
        def underindentedComment (self,line):

            self.error(
                'underindented python comments.\nExtra leading whitespace will be added\n' + line)

        def underindentedLine (self,line):

            self.error(
                'underindented line.\nExtra leading whitespace will be added\n' + line)
        #@-node:ekr.20070801074524:underindentedComment & underindentedLine
        #@-node:ekr.20070706084535:Code generation
        #@+node:ekr.20070703122141.78:error & oops
        def error (self,s):

            self.errors += 1
            self.importCommands.errors += 1
            if g.app.unitTesting:
                if self.errors == 1:
                    g.app.unitTestDict['actualErrorMessage'] = s
                g.app.unitTestDict['actualErrors'] = self.errors
                if 0: # For debugging unit tests.
                    g.es_print(s,color='red')
            else:
                g.es_print(s,color='red')

        def oops (self):
            print 'baseScannerClass oops: %s must be overridden in subclass' % g.callers()
        #@-node:ekr.20070703122141.78:error & oops
        #@+node:ekr.20070706084535.1:Parsing
        #@+at 
        #@nonl
        # Scan and skipDecls would typically not be overridden.
        #@-at
        #@+node:ekr.20070707150022:extendSignature
        def extendSignature(self,s,i):

            '''Extend the signature line if appropriate.
            The text *must* end with a newline.

            For example, the Python scanner appends docstrings if they exist.'''

            return i
        #@-node:ekr.20070707150022:extendSignature
        #@+node:ekr.20071017132056:getIndent
        def getIndent (self,s,i):

            j,j2 = g.getLine(s,i)
            junk,indent = g.skip_leading_ws_with_indent(s,j,self.tab_width)
            # g.trace('%d %s' % (indent,s[j:j2]))
            return indent
        #@nonl
        #@-node:ekr.20071017132056:getIndent
        #@+node:ekr.20070706101600:scan & scanHelper
        def scan (self,s,parent):

            '''A language independent scanner: it uses language-specific helpers.

            Create a child of self.root for:
            - Leading outer-level declarations.
            - Outer-level classes.
            - Outer-level functions.
            '''

            # Create the initial body text in the root.
            self.putRootText(parent)

            # Parse the decls.
            i = start = self.skipDecls(s,0,len(s),inClass=False)
            decls = s[:i]

            # Create the decls node.
            if decls: self.createDeclsNode(parent,decls)

            # Scan the rest of the file.
            start,junk,junk = self.scanHelper(s,i,end=len(s),parent=parent,kind='outer')

            # Finish adding to the parent's body text.
            self.addRef(parent)
            if start < len(s):
                self.c.appendStringToBody(parent,s[start:]) 
        #@+node:ekr.20071018084830:scanHelper
        def scanHelper(self,s,i,end,parent,kind):

            '''Common scanning code used by both scan and putClassHelper.'''

            assert kind in ('class','outer')
            start = i ; putRef = False ; indentFlag = None
            # if kind =='class' and g.match(s,i,self.outerBlockDelim1):
                # end = self.skipBlock(s,i,delim1=self.outerBlockDelim1,delim2=self.outerBlockDelim2)
                # start = i = i + len(self.outerBlockDelim1)
            while i < end:
                progress = i
                if s[i] in (' ','\t','\n'):
                    i += 1 # Prevent lookahead below, and speed up the scan.
                elif self.startsComment(s,i):
                    i = self.skipComment(s,i)
                elif self.startsString(s,i):
                    i = self.skipString(s,i)
                elif self.startsClass(s,i):  # Sets sigStart,sigEnd & codeEnd ivars.
                    putRef = True
                    if indentFlag is None: indentFlag = self.getIndent(s,i) > self.classIndent
                    end2 = self.codeEnd # putClass may change codeEnd ivar.
                    self.putClass(s,i,self.sigStart,self.sigEnd,self.codeEnd,start,parent)
                    i = start = end2
                elif self.startsFunction(s,i): # Sets sigStart,sigEnd & codeEnd ivars.
                    putRef = True ; indent = self.getIndent(s,i)
                    if indentFlag is None: indentFlag = indent > self.classIndent
                    self.putFunction(s,self.sigStart,self.codeEnd,start,parent)
                    i = start = self.codeEnd
                elif self.startsId(s,i):
                    i = self.skipId(s,i);
                elif kind == 'outer' and g.match(s,i,self.outerBlockDelim1): # Do this after testing for classes.
                    i = start = self.skipBlock(s,i,delim1=self.outerBlockDelim1,delim2=self.outerBlockDelim2)
                else: i += 1

                # if progress == i: g.pdb()
                assert progress < i,'i: %d, ch: %s' % (i,repr(s[i]))

            return start,putRef,indentFlag
        #@-node:ekr.20071018084830:scanHelper
        #@-node:ekr.20070706101600:scan & scanHelper
        #@+node:ekr.20070712075148:skipArgs
        def skipArgs (self,s,i,kind):

            '''Skip the argument or class list.  Return i, ok

            kind is in ('class','function')'''

            start = i
            i = g.skip_ws_and_nl(s,i)
            if not g.match(s,i,'('):
                return start,kind == 'class'

            i = self.skipParens(s,i)
            # skipParens skips the ')'
            if i >= len(s):
                return start,False
            else:
                return i,True 
        #@-node:ekr.20070712075148:skipArgs
        #@+node:ekr.20070707073859:skipBlock
        def skipBlock(self,s,i,delim1=None,delim2=None):

            '''Skip from the opening delim to *past* the matching closing delim.

            If no matching is found i is set to len(s)'''

            trace = False
            start = i
            if delim1 is None: delim1 = self.blockDelim1
            if delim2 is None: delim2 = self.blockDelim2
            match1 = g.choose(len(delim1)==1,g.match,g.match_word)
            match2 = g.choose(len(delim2)==1,g.match,g.match_word)
            assert match1(s,i,delim1)
            level = 0 ; start = i
            startIndent = self.startSigIndent
            if trace: g.trace('***','startIndent',startIndent,g.callers())
            while i < len(s):
                progress = i
                if g.is_nl(s,i):
                    backslashNewline = i > 0 and g.match(s,i-1,'\\\n')
                    i = g.skip_nl(s,i)
                    if not backslashNewline and not g.is_nl(s,i):
                        j, indent = g.skip_leading_ws_with_indent(s,i,self.tab_width)
                        line = g.get_line(s,j)
                        if trace: g.trace('indent',indent,line)
                        if indent < startIndent and line.strip():
                            # An non-empty underindented line.
                            # Issue an error unless it contains just the closing bracket.
                            if level == 1 and match2(s,j,delim2):
                                pass
                            else:
                                if j not in self.errorLines: # No error yet given.
                                    self.errorLines.append(j)
                                    self.underindentedLine(line)
                elif s[i] in (' ','\t',):
                    i += 1 # speed up the scan.
                elif self.startsComment(s,i):
                    i = self.skipComment(s,i)
                elif self.startsString(s,i):
                    i = self.skipString(s,i)
                elif match1(s,i,delim1):
                    level += 1 ; i += len(delim1)
                elif match2(s,i,delim2):
                    level -= 1 ; i += len(delim2)
                    if level <= 0:
                        if trace: g.trace('returns\n',repr(s[start:i]))
                        return i

                else: i += 1
                assert progress < i

            self.error('no block')
            if trace: g.trace('** no block')
            return start
        #@-node:ekr.20070707073859:skipBlock
        #@+node:ekr.20070712091019:skipCodeBlock
        def skipCodeBlock (self,s,i,kind):

            '''Skip the code block in a function or class definition.'''

            trace = False
            start = i
            i = self.skipBlock(s,i,delim1=None,delim2=None)

            if self.sigFailTokens:
                i = g.skip_ws(s,i)
                for z in self.sigFailTokens:
                    if g.match(s,i,z):
                        if trace: g.trace('failtoken',z)
                        return start,False

            if i > start:
                i = self.skipNewline(s,i,kind)

            if trace:
                g.trace(g.callers())
                g.trace('returns...\n',g.listToString(g.splitLines(s[start:i])))

            return i,True
        #@-node:ekr.20070712091019:skipCodeBlock
        #@+node:ekr.20070711104014:skipComment & helper
        def skipComment (self,s,i):

            '''Skip a comment and return the index of the following character.'''

            if g.match(s,i,self.lineCommentDelim) or g.match(s,i,self.lineCommentDelim2):
                return g.skip_to_end_of_line(s,i)
            else:
                return self.skipBlockComment(s,i)
        #@+node:ekr.20070707074541:skipBlockComment
        def skipBlockComment (self,s,i):

            '''Skip past a block comment.'''

            # Skip the opening delim.
            assert(g.match(s,i,self.blockCommentDelim1))
            start = i ; i += len(self.blockCommentDelim1)

            # Find the closing delim.
            k = string.find(s,self.blockCommentDelim2,i)
            if k == -1:
                self.error('Run on block comment: ' + s[start:i])
                return len(s)
            else:
                return k + len(self.blockCommentDelim2)
        #@-node:ekr.20070707074541:skipBlockComment
        #@-node:ekr.20070711104014:skipComment & helper
        #@+node:ekr.20070707080042:skipDecls & helper
        def skipDecls (self,s,i,end,inClass):

            '''Skip everything until the start of the next class or function.'''

            trace = False or self.trace
            start = i ; prefix = None
            classOrFunc = False
            while i < end:
                progress = i
                if s[i] in (' ','\t','\n'):
                    i += 1 # Prevent lookahead below, and speed up the scan.
                elif self.startsComment(s,i):
                    # Add the comment to the decl if it *doesn't* start the line.
                    i2,junk = g.getLine(s,i)
                    i2 = g.skip_ws(s,i2)
                    if i2 == i and prefix is None:
                        prefix = i2 # Bug fix: must include leading whitespace in the comment.
                    i = self.skipComment(s,i)
                elif self.startsString(s,i):
                    i = self.skipString(s,i)
                    prefix = None
                elif self.startsClass(s,i,quick=True):
                    # Important: do not include leading ws in the decls.
                    classOrFunc = True
                    i = self.adjustClassOrFunctionStart(s,i,self.classId) # 'class')
                    break
                elif self.startsFunction(s,i,quick=True):
                    # Important: do not include leading ws in the decls.
                    classOrFunc = True
                    i = self.adjustClassOrFunctionStart(s,i,'function')
                    break
                elif self.startsId(s,i):
                    i = self.skipId(s,i)
                    prefix = None
                # Don't skip outer blocks: they may contain classes.
                elif g.match(s,i,self.outerBlockDelim1):
                    break
                else:
                    i += 1 ;  prefix = None
                # if progress == i: g.pdb()
                assert(progress < i)

            if prefix is not None: i = prefix
            decls = s[start:i]
            if inClass and not classOrFunc:
                # Don't return decls if a class contains nothing but decls.
                if trace and decls.strip(): g.trace('**class is all decls...\n',decls)
                return start
            elif decls.strip(): 
                if trace or self.trace: g.trace('\n'+decls)
                return i
            else: # Ignore empty decls.
                return start
        #@+node:ekr.20070709084313:adjustClassOrFunctionStart
        def adjustClassOrFunctionStart(self,s,i,tag):

            '''
            s[i:] starts a class or function.
            Adjust i so it points at the start of the line.

            Issue a warning if anything except whitespace appears.
            '''

            j = g.find_line_start(s,i)
            return j

            # if s[j:i].strip():
                # self.error(
                    # '%s %s does not start a line. Leo must insert a newline\n%s' % (
                        # tag,self.sigId,g.get_line(s,j)))
                # return i
            # else:
                # return j
        #@-node:ekr.20070709084313:adjustClassOrFunctionStart
        #@-node:ekr.20070707080042:skipDecls & helper
        #@+node:ekr.20070707094858.1:skipId
        def skipId (self,s,i):

            return g.skip_id(s,i,chars=self.extraIdChars)
        #@nonl
        #@-node:ekr.20070707094858.1:skipId
        #@+node:ekr.20070730134936:skipNewline
        def skipNewline(self,s,i,kind):

            '''Skip whitespace and comments up to a newline, then skip the newline.
            Issue an error if no newline is found.'''

            while i < len(s):
                i = g.skip_ws(s,i)
                if self.startsComment(s,i):
                    i = self.skipComment(s,i)
                else: break

            if i >= len(s):
                return len(s)

            if g.match(s,i,'\n'):
                i += 1
            else:
                self.error(
                    '%s %s does not end in a newline; one will be added\n%s' % (
                        kind,self.sigId,g.get_line(s,i)))
                # g.trace(g.callers())

            return i
        #@-node:ekr.20070730134936:skipNewline
        #@+node:ekr.20070712081451:skipParens
        def skipParens (self,s,i):

            '''Skip a parenthisized list, that might contain strings or comments.'''

            return self.skipBlock(s,i,delim1='(',delim2=')')
        #@-node:ekr.20070712081451:skipParens
        #@+node:ekr.20070707073627.2:skipString
        def skipString (self,s,i):

            # Returns len(s) on unterminated string.
            return g.skip_string(s,i,verbose=False)
        #@-node:ekr.20070707073627.2:skipString
        #@+node:ekr.20070711132314:startsClass/Function (baseClass) & helpers
        # We don't expect to override this code, but subclasses may override the helpers.

        def startsClass (self,s,i,quick=False):
            '''Return True if s[i:] starts a class definition.
            Sets sigStart, sigEnd, sigId and codeEnd ivars.'''
            val = self.hasClasses and self.startsHelper(s,i,kind='class',quick=quick,tags=self.classTags)
            return val

        def startsFunction (self,s,i,quick=False):
            '''Return True if s[i:] starts a function.
            Sets sigStart, sigEnd, sigId and codeEnd ivars.'''
            val = self.hasFunctions and self.startsHelper(s,i,kind='function',quick=quick,tags=self.functionTags)
            return val
        #@+node:ekr.20070712112008:startsHelper
        def startsHelper(self,s,i,kind,quick,tags):
            '''return True if s[i:] starts a class or function.
            Sets sigStart, sigEnd, sigId and codeEnd ivars.'''

            # if not tags: return False

            trace = self.trace
            verbose = False # kind=='function'
            self.codeEnd = self.sigEnd = self.sigId = None
            self.sigStart = i

            # Underindented lines can happen in any language, not just Python.
            # The skipBlock method of the base class checks for such lines.
            self.startSigIndent = self.getLeadingIndent(s,i)

            # Run a quick check first.
            # Get the tag that starts the class or function.
            j = g.skip_ws_and_nl(s,i)
            i = self.skipId(s,j)
            self.sigId = theId = s[j:i] # Set sigId ivar 'early' for error messages.
            if not theId: return False

            if tags:
                if theId not in tags:
                    if trace and verbose: g.trace('**** %s theId: %s not in tags: %s' % (kind,theId,tags))
                    return False
                if quick: return True

            if trace and verbose: g.trace('kind',kind,'id',theId)

            # Get the class/function id.
            i, ids, classId = self.skipSigStart(s,j,kind,tags) # Rescan the first id.
            i, sigId = self.skipSigId(s,i,ids)
            if not sigId:
                if trace and verbose: g.trace('**no sigId',g.get_line(s,i))
                return False

            if self.output_indent < self.startSigIndent:
                if trace: g.trace('**over-indent',sigId)
                    #,'output_indent',self.output_indent,'startSigIndent',self.startSigIndent)
                return False

            # Skip the argument list.
            i, ok = self.skipArgs(s,i,kind)
            if not ok:
                if trace and verbose: g.trace('no args',g.get_line(s,i))
                return False
            i = g.skip_ws_and_nl(s,i)

            # Skip the tail of the signature
            i, ok = self.skipSigTail(s,i)
            if not ok:
                if trace and verbose: g.trace('no tail',g.get_line(s,i))
                return False
            sigEnd = i

            # A trick: make sure the signature ends in a newline,
            # even if it overlaps the start of the block.
            if not g.match(s,sigEnd,'\n') and not g.match(s,sigEnd-1,'\n'):
                if trace and verbose: g.trace('extending sigEnd')
                sigEnd = g.skip_line(s,sigEnd)

            if self.blockDelim1:
                i = g.skip_ws_and_nl(s,i)
                if not g.match(s,i,self.blockDelim1):
                    if trace and verbose: g.trace('no block',g.get_line(s,i))
                    return False

            i,ok = self.skipCodeBlock(s,i,kind)
            if not ok: return False
                # skipCodeBlock skips the trailing delim.

            # Success: set the ivars.
            self.codeEnd = i
            self.sigEnd = sigEnd
            self.sigId = sigId
            self.classId = classId

            # Note: backing up here is safe because
            # we won't back up past scan's 'start' point.
            # Thus, characters will never be output twice.
            k = self.sigStart
            if not g.match(s,k,'\n'):
                self.sigStart = g.find_line_start(s,k)

            # Isue this warning only if we have a real class or function.
            if 0: ### wrong.
                if s[self.sigStart:k].strip():
                    self.error('%s definition does not start a line\n%s' % (
                        kind,g.get_line(s,k)))

            if trace:
                if 1:
                    g.trace(kind,'returns\n'+s[self.sigStart:i])
                else:
                    g.trace(kind,'returns s[sigStart:i] = [%d:%d]' % (self.sigStart,i))
            return True
        #@-node:ekr.20070712112008:startsHelper
        #@+node:ekr.20070711140703:skipSigStart
        def skipSigStart (self,s,i,kind,tags):

            '''Skip over the start of a function/class signature.

            tags is in (self.classTags,self.functionTags).

            Return (i,ids) where ids is list of all ids found, in order.'''

            # __pychecker__ = '--no-argsused' # tags not used in the base class.

            trace = False and self.trace # or kind =='function'
            ids = [] ; classId = None
            if trace: g.trace('*entry',kind,i,s[i:i+20])
            start = i
            while i < len(s):
                j = g.skip_ws_and_nl(s,i)
                for z in self.sigFailTokens:
                    if g.match(s,j,z):
                        if trace: g.trace('failtoken',z,'ids',ids)
                        return start, [], None
                for z in self.sigHeadExtraTokens:
                    if g.match(s,j,z):
                        i += len(z) ; break
                else:
                    i = self.skipId(s,j)
                    theId = s[j:i]
                    if theId and theId in tags: classId = theId
                    if theId: ids.append(theId)
                    else: break

            if trace: g.trace('*exit ',kind,i,i < len(s) and s[i],ids,classId)
            return i, ids, classId
        #@-node:ekr.20070711140703:skipSigStart
        #@+node:ekr.20070712082913:skipSigTail
        def skipSigTail(self,s,i):

            '''Skip from the end of the arg list to the start of the block.'''

            trace = False and self.trace
            start = i
            i = g.skip_ws(s,i)
            for z in self.sigFailTokens:
                if g.match(s,i,z):
                    if trace: g.trace('failToken',z,'line',g.skip_line(s,i))
                    return i,False
            while i < len(s):
                if self.startsComment(s,i):
                    i = self.skipComment(s,i)
                elif g.match(s,i,self.blockDelim1):
                    if trace: g.trace(repr(s[start:i]))
                    return i,True
                else:
                    i += 1
            if trace: g.trace('no block delim')
            return i,False
        #@-node:ekr.20070712082913:skipSigTail
        #@+node:ekr.20070711134534:skipSigId
        def skipSigId (self,s,i,ids):

            '''Return (i, id) where id is the signature's id.

            By default, this is the last id in the ids list.'''

            return i, ids and ids[-1]
        #@-node:ekr.20070711134534:skipSigId
        #@-node:ekr.20070711132314:startsClass/Function (baseClass) & helpers
        #@+node:ekr.20070711104014.1:startsComment
        def startsComment (self,s,i):

            return (
                g.match(s,i,self.lineCommentDelim) or
                g.match(s,i,self.lineCommentDelim2) or
                g.match(s,i,self.blockCommentDelim1))
        #@-node:ekr.20070711104014.1:startsComment
        #@+node:ekr.20070707094858.2:startsId
        def startsId(self,s,i):

            return g.is_c_id(s[i:i+1])
        #@-node:ekr.20070707094858.2:startsId
        #@+node:ekr.20070707172732.1:startsString
        def startsString(self,s,i):

            return g.match(s,i,'"') or g.match(s,i,"'")
        #@-node:ekr.20070707172732.1:startsString
        #@-node:ekr.20070706084535.1:Parsing
        #@+node:ekr.20070707072749:run (baseScannerClass)
        def run (self,s,parent):

            scanner = self ; c = self.c
            scanner.root = root = parent.copy()
            scanner.file_s = s

            # Init the error/status info.
            self.errors = 0
            self.errorLines = []
            changed = c.isChanged()

            # Regularize leading whitespace for strict languages only.
            if self.strict:
                s = scanner.regularizeWhitespace(s)

            # Generate the nodes, including directive and section references.
            scanner.scan(s,parent)

            # Check the generated nodes.
            # Return True if the result is equivalent to the original file.
            ok = self.errors == 0 and scanner.check(s,parent)
            g.app.unitTestDict ['result'] = ok

            # Insert an @ignore directive if there were any serious problems.
            if not ok: scanner.insertIgnoreDirective(parent)

            if self.atAuto and ok:
                for p in root.self_and_subtree_iter():
                    p.clearDirty()
                c.setChanged(changed)
            else:
                root.setDirty(setDescendentsDirty=False)
                c.setChanged(True)
        #@+node:ekr.20070808115837.1:regularizeWhitespace
        def regularizeWhitespace (self,s):

            '''Regularize leading whitespace in s:
            Convert tabs to blanks or vice versa depending on the @tabwidth in effect.
            This is only called for strict languages.'''

            changed = False ; lines = g.splitLines(s) ; result = [] ; tab_width = self.tab_width

            if tab_width < 0: # Convert tabs to blanks.
                for line in lines:
                    i, w = g.skip_leading_ws_with_indent(line,0,tab_width)
                    s = g.computeLeadingWhitespace(w,-abs(tab_width)) + line [i:] # Use negative width.
                    if s != line: changed = True
                    result.append(s)
            elif tab_width > 0: # Convert blanks to tabs.
                for line in lines:
                    s = g.optimizeLeadingWhitespace(line,abs(tab_width)) # Use positive width.
                    if s != line: changed = True
                    result.append(s)

            if changed: self.regularizeError()

            return ''.join(result)
        #@+node:ekr.20070808121958:regularizeError
        def regularizeError (self):

            # Create the message.
            kind = g.choose(self.strict,'error','warning')
            s = g.choose(self.tab_width < 0,'tabs converted to blanks','blanks converted to tabs')
            message = '%s: inconsistent leading whitespace. %s' % (kind,s)

            # Issue an error or warning.
            if self.strict:
                self.error(message)
            else:
                print message
                g.es(message,color='red')

        #@-node:ekr.20070808121958:regularizeError
        #@-node:ekr.20070808115837.1:regularizeWhitespace
        #@-node:ekr.20070707072749:run (baseScannerClass)
        #@-others
    #@-node:ekr.20070703122141.65: class baseScannerClass
    #@+node:edreamleo.20070710110114.1:C scanner
    #@+node:edreamleo.20070710110153:scanCText
    def scanCText (self,s,parent,atAuto=False):

        scanner = self.cScanner(importCommands=self,atAuto=atAuto)

        scanner.run(s,parent)
    #@-node:edreamleo.20070710110153:scanCText
    #@+node:edreamleo.20070710093042:class cScanner (baseScannerClass)
    class cScanner (baseScannerClass):

        def __init__ (self,importCommands,atAuto):

            # Init the base class.
            importCommands.baseScannerClass.__init__(self,importCommands,
                atAuto=atAuto,language='c')

            # Set the parser delims.
            self.blockCommentDelim1 = '/*'
            self.blockCommentDelim2 = '*/'
            self.blockDelim1 = '{'
            self.blockDelim2 = '}'
            self.classTags = ['class',]
            self.extraIdChars = ':'
            self.functionTags = []
            self.lineCommentDelim = '//'
            self.lineCommentDelim2 = '#' # A hack: treat preprocess directives as comments(!)
            self.outerBlockDelim1 = '{'
            self.outerBlockDelim2 = '}'
            self.sigHeadExtraTokens = ['*']
            self.sigFailTokens = [';','=']
    #@-node:edreamleo.20070710093042:class cScanner (baseScannerClass)
    #@-node:edreamleo.20070710110114.1:C scanner
    #@+node:ekr.20071008130845:C# scanner
    #@+node:ekr.20071008130845.1:scanCSharpText
    def scanCSharpText (self,s,parent,atAuto=False):

        scanner = self.cSharpScanner(importCommands=self,atAuto=atAuto)

        scanner.run(s,parent)
    #@-node:ekr.20071008130845.1:scanCSharpText
    #@+node:ekr.20071008130845.2:class cSharpScanner (baseScannerClass)
    class cSharpScanner (baseScannerClass):

        def __init__ (self,importCommands,atAuto):

            # Init the base class.
            importCommands.baseScannerClass.__init__(self,importCommands,
                atAuto=atAuto,language='c')

            # Set the parser delims.
            self.blockCommentDelim1 = '/*'
            self.blockCommentDelim2 = '*/'
            self.blockDelim1 = '{'
            self.blockDelim2 = '}'
            self.classTags = ['class','interface','namespace',]
            self.extraIdChars = ':'
            self.functionTags = []
            self.lineCommentDelim = '//'
            self.lineCommentDelim2 = None
            self.outerBlockDelim1 = '{'
            self.outerBlockDelim2 = '}'
            self.sigHeadExtraTokens = []
            self.sigFailTokens = [';','='] # Just like C.
    #@-node:ekr.20071008130845.2:class cSharpScanner (baseScannerClass)
    #@-node:ekr.20071008130845:C# scanner
    #@+node:ekr.20070711060107:Elisp scanner
    #@+node:ekr.20070711060107.1:scanElispText
    def scanElispText (self,s,parent,atAuto=False):

        scanner = self.elispScanner(importCommands=self,atAuto=atAuto)

        scanner.run(s,parent)
    #@-node:ekr.20070711060107.1:scanElispText
    #@+node:ekr.20070711060113:class elispScanner (baseScannerClass)
    class elispScanner (baseScannerClass):

        #@    @+others
        #@+node:ekr.20070711060113.1: __init__
        def __init__ (self,importCommands,atAuto):

            # Init the base class.
            importCommands.baseScannerClass.__init__(self,importCommands,
                atAuto=atAuto,language='elisp')

            # Set the parser delims.
            self.blockCommentDelim1 = None
            self.blockCommentDelim2 = None
            self.lineCommentDelim = ';'
            self.lineCommentDelim2 = None
            self.blockDelim1 = '('
            self.blockDelim2 = ')'
            self.extraIdChars = '-'

        #@-node:ekr.20070711060113.1: __init__
        #@+node:ekr.20070711060113.2:Overrides
        # skipClass/Function/Signature are defined in the base class.
        #@nonl
        #@+node:ekr.20070711060113.3:startsClass/Function & skipSignature
        def startsClass (self,s,i):
            '''Return True if s[i:] starts a class definition.
            Sets sigStart, sigEnd, sigId and codeEnd ivars.'''
            return False

        def startsFunction(self,s,i):
            '''Return True if s[i:] starts a function.
            Sets sigStart, sigEnd, sigId and codeEnd ivars.'''

            self.sigStart = i
            self.codeEnd = self.sigEnd = self.sigId = None
            if not g.match(s,i,'('): return False
            end = self.skipBlock(s,i)
            if not g.match(s,end,')'): return False

            i = g.skip_ws(s,i+1)
            if not g.match_word(s,i,'defun'): return False

            i += len(key)
            sigEnd = i = g.skip_ws_and_nl(s,i)
            j = g.skip_id(s,i)
            word = s[i:j]
            if not word: return False

            self.codeEnd = end + 1
            self.sigEnd = sigEnd
            self.sigId = word
            return True
        #@-node:ekr.20070711060113.3:startsClass/Function & skipSignature
        #@+node:ekr.20070711063339:startsString
        def startsString(self,s,i):

            # Single quotes are not strings.
            return g.match(s,i,'"')
        #@-node:ekr.20070711063339:startsString
        #@-node:ekr.20070711060113.2:Overrides
        #@-others
    #@-node:ekr.20070711060113:class elispScanner (baseScannerClass)
    #@-node:ekr.20070711060107:Elisp scanner
    #@+node:edreamleo.20070710110114:Java scanner
    #@+node:edreamleo.20070710110114.2:scanJavaText
    def scanJavaText (self,s,parent,atAuto=False):

        scanner = self.javaScanner(importCommands=self,atAuto=atAuto)

        scanner.run(s,parent)
    #@-node:edreamleo.20070710110114.2:scanJavaText
    #@+node:edreamleo.20070710085115:class javaScanner (baseScannerClass)
    class javaScanner (baseScannerClass):

        #@    @+others
        #@+node:ekr.20071019171430:javaScanner.__init__
        def __init__ (self,importCommands,atAuto):

            # Init the base class.
            importCommands.baseScannerClass.__init__(self,importCommands,
                atAuto=atAuto,language='java')

            # Set the parser delims.
            self.blockCommentDelim1 = '/*'
            self.blockCommentDelim2 = '*/'
            self.lineCommentDelim = '//'
            self.lineCommentDelim2 = None
            self.outerBlockDelim1 = '{'
            self.classTags = ['class','interface']
            self.functionTags = []
            self.sigFailTokens = [';','='] # Just like c.
        #@-node:ekr.20071019171430:javaScanner.__init__
        #@+node:ekr.20071019170943:javaScanner.skipSigId
        def skipSigId (self,s,i,ids):

            '''Return (i, id) where id is the signature's id.

            By default, this is the last id in the ids list.'''

            # Remove 'public' and 'private'
            ids2 = [z for z in ids if z not in ('public','private','final',)]

            # Remove 'extends' and everything after it.
            ids = []
            for z in ids2:
                if z == 'extends': break
                ids.append(z)

            return i, ids and ids[-1]
        #@-node:ekr.20071019170943:javaScanner.skipSigId
        #@-others
    #@-node:edreamleo.20070710085115:class javaScanner (baseScannerClass)
    #@-node:edreamleo.20070710110114:Java scanner
    #@+node:ekr.20071027111225:JavaScript scanner
    #@+node:ekr.20071027111225.1:scanJavaScriptText
    def scanJavaScriptText (self,s,parent,atAuto=False):

        scanner = self.javaScriptScanner(importCommands=self,atAuto=atAuto)

        scanner.run(s,parent)
    #@-node:ekr.20071027111225.1:scanJavaScriptText
    #@+node:ekr.20071027111225.2:class javaScriptScanner (baseScannerClass)
    class javaScriptScanner (baseScannerClass):

        #@    @+others
        #@+node:ekr.20071027111225.3:javaScriptScanner.__init__
        def __init__ (self,importCommands,atAuto):

            # Init the base class.
            importCommands.baseScannerClass.__init__(self,importCommands,
                atAuto=atAuto,language='java') # Used to set comment delims.

            # Set the parser delims.
            self.blockCommentDelim1 = '/*'
            self.blockCommentDelim2 = '*/'
            self.blockDelim1 = '{'
            self.blockDelim2 = '}'
            self.hasClasses = False
            self.hasFunctions = True
            self.lineCommentDelim = '//'
            self.lineCommentDelim2 = None
            self.outerBlockDelim1 = None # For now, ignore outer blocks.
            self.outerBlockDelim2 = None
            self.classTags = []
            self.functionTags = ['function']
            self.sigFailTokens = [';',] # ','=',] # Just like Java.
        #@-node:ekr.20071027111225.3:javaScriptScanner.__init__
        #@-others
    #@-node:ekr.20071027111225.2:class javaScriptScanner (baseScannerClass)
    #@-node:ekr.20071027111225:JavaScript scanner
    #@+node:ekr.20070711104241:Pascal scanner
    #@+node:ekr.20070711104241.2:scanPascalText
    def scanPascalText (self,s,parent,atAuto=False):

        scanner = self.pascalScanner(importCommands=self,atAuto=atAuto)

        scanner.run(s,parent)
    #@nonl
    #@-node:ekr.20070711104241.2:scanPascalText
    #@+node:ekr.20070711104241.3:class pascalScanner (baseScannerClass)
    class pascalScanner (baseScannerClass):

        def __init__ (self,importCommands,atAuto):

            # Init the base class.
            importCommands.baseScannerClass.__init__(self,importCommands,
                atAuto=atAuto,language='pascal')

            # Set the parser delims.
            self.blockCommentDelim1 = '(*'
            self.blockCommentDelim2 = '*)'
            self.lineCommentDelim = '//'
            self.blockDelim1 = 'begin'
            self.blockDelim2 = 'end'
            self.classTags = []
            self.functionTags = ['function','procedure','constructor','destructor',]
    #@-node:ekr.20070711104241.3:class pascalScanner (baseScannerClass)
    #@-node:ekr.20070711104241:Pascal scanner
    #@+node:ekr.20070711090052:PHP scanner
    #@+node:ekr.20070711090122:scanPHPText
    def scanPHPText (self,s,parent,atAuto=False):

        scanner = self.phpScanner(importCommands=self,atAuto=atAuto)

        if scanner.isPurePHP(s):
            scanner.run(s,parent)
        else:
            fileName = scanner.fileName
            if not atAuto:
                g.es_print('%s seems to be mixed HTML and PHP.' % fileName)
            scanner.createHeadline(
                parent,body=s,headline=fileName)
    #@-node:ekr.20070711090122:scanPHPText
    #@+node:ekr.20070711090052.1:class phpScanner (baseScannerClass)
    class phpScanner (baseScannerClass):

        #@    @+others
        #@+node:ekr.20070711090052.2: __init__
        def __init__ (self,importCommands,atAuto):

            # Init the base class.
            importCommands.baseScannerClass.__init__(self,importCommands,
                atAuto=atAuto,language='php')

            # Set the parser delims.
            self.blockCommentDelim1 = '/*'
            self.blockCommentDelim2 = '*/'
            self.lineCommentDelim = '//'
            self.lineCommentDelim2 = '#'

            # The valid characters in an id
            self.chars = list(string.ascii_letters + string.digits)
            extra = [chr(z) for z in xrange(127,256)]
            self.chars.extend(extra)
        #@-node:ekr.20070711090052.2: __init__
        #@+node:ekr.20070711094850:isPurePHP
        def isPurePHP (self,s):

            '''Return True if the file begins with <?php or ends with ?>'''

            s = s.strip()

            return (
                s.startswith('<?') and
                s[2:3] in ('P','p','=','\n','\r',' ','\t') and
                s.endswith('?>'))

        #@-node:ekr.20070711094850:isPurePHP
        #@+node:ekr.20070711090052.3:Overrides
        # Does not create @first/@last nodes
        #@+node:ekr.20070711090807:startsString skipString
        def startsString(self,s,i):
            return g.match(s,i,'"') or g.match(s,i,"'") or g.match(s,i,'<<<')

        def skipString (self,s,i):
            if g.match(s,i,'"') or g.match(s,i,"'"):
                return self.skipString()
            else:
                return g.skip_heredoc_string(s,i)
        #@-node:ekr.20070711090807:startsString skipString
        #@-node:ekr.20070711090052.3:Overrides
        #@-others
    #@-node:ekr.20070711090052.1:class phpScanner (baseScannerClass)
    #@-node:ekr.20070711090052:PHP scanner
    #@+node:ekr.20070703123334.2:Python scanner
    #@+node:ekr.20070703122141.99:scanPythonText
    def scanPythonText (self,s,parent,atAuto=False):

        scanner = self.pythonScanner(importCommands=self,atAuto=atAuto)

        scanner.run(s,parent)
    #@-node:ekr.20070703122141.99:scanPythonText
    #@+node:ekr.20070703122141.100:class pythonScanner (baseScannerClass)
    class pythonScanner (baseScannerClass):

        #@    @+others
        #@+node:ekr.20070703122141.101: __init__
        def __init__ (self,importCommands,atAuto):

            # Init the base class.
            importCommands.baseScannerClass.__init__(self,importCommands,
                atAuto=atAuto,language='python')

            # Set the parser delims.
            self.lineCommentDelim = '#'
            self.classTags = ['class',]
            self.functionTags = ['def',]
            self.blockDelim1 = self.blockDelim2 = None
                # Suppress the check for the block delim.
                # The check is done in skipSigTail.
            self.strict = True

        #@-node:ekr.20070703122141.101: __init__
        #@+node:ekr.20070707113839:extendSignature
        def extendSignature(self,s,i):

            '''Extend the text to be added to the class node following the signature.

            The text *must* end with a newline.'''

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
        #@+node:ekr.20070707073627.4:skipString
        def skipString (self,s,i):

            # Returns len(s) on unterminated string.
            return g.skip_python_string(s,i,verbose=False)
        #@-node:ekr.20070707073627.4:skipString
        #@+node:ekr.20070712090019.1:skipCodeBlock (python) & helper
        def skipCodeBlock (self,s,i,kind):

            trace = False ; verbose = False
            # if trace: g.trace('***',g.callers())
            startIndent = self.startSigIndent
            assert startIndent is not None
            i = start = g.skip_ws_and_nl(s,i)
            parenCount = 0
            underIndentedStart = None # The start of trailing underindented blank or comment lines.
            while i < len(s):
                progress = i
                ch = s[i]
                if g.is_nl(s,i):
                    i = g.skip_nl(s,i)
                    j = g.skip_ws(s,i)
                    if g.is_nl(s,j):
                        pass # We have already made progress.
                    else:
                        if trace and verbose: g.trace(g.get_line(s,i))
                        backslashNewline = i > 0 and g.match(s,i-1,'\\\n')
                        if not backslashNewline:
                            i,underIndentedStart,breakFlag = self.pythonNewlineHelper(
                                s,i,parenCount,startIndent,underIndentedStart)
                            if breakFlag: break
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

            # The actual end of the block.
            if underIndentedStart is not None:
                i = underIndentedStart
                if trace: g.trace('***backtracking to underindent range')
                if trace: g.trace(g.get_line(s,i))

            if 0 < i < len(s) and not g.match(s,i-1,'\n'):
                g.trace('Can not happen: Python block does not end in a newline.')
                g.trace(g.get_line(s,i))
                return i,False
            if (trace or self.trace) and s[start:i].strip():
                g.trace('%s returns\n' % (kind) + s[start:i])
            return i,True
        #@+node:ekr.20070801080447:pythonNewlineHelper
        def pythonNewlineHelper (self,s,i,parenCount,startIndent,underIndentedStart):

            trace = False
            breakFlag = False
            j, indent = g.skip_leading_ws_with_indent(s,i,self.tab_width)
            if trace: g.trace('startIndent',startIndent,'indent',indent,'line',repr(g.get_line(s,j)))
            if indent <= startIndent and parenCount == 0:
                # An underindented line: it ends the block *unless*
                # it is a blank or comment line.
                if g.match(s,j,'#'):
                    if trace: g.trace('underindent: comment')
                    if underIndentedStart is None: underIndentedStart = i
                    i = j
                elif g.match(s,j,'\n'):
                    if trace: g.trace('underindent: blank line')
                    # Blank lines never start the range of underindented lines.
                    i = j
                else:
                    if trace: g.trace('underindent: end of block')
                    breakFlag = True # The actual end of the block.
            else:
                if underIndentedStart and g.match(s,j,'\n'):
                    # Add the blank line to the underindented range.
                    if trace: g.trace('properly indented blank line extends underindent range')
                elif underIndentedStart and g.match(s,j,'#'):
                    # Add the (properly indented!) comment line to the underindented range.
                    if trace: g.trace('properly indented comment line extends underindent range')
                elif underIndentedStart is None:
                    pass
                else:
                    # A properly indented non-comment line.
                    # Give a message for all underindented comments in underindented range.
                    if trace: g.trace('properly indented line generates underindent errors')
                    s2 = s[underIndentedStart:i]
                    lines = g.splitlines(s2)
                    for line in lines:
                        if line.strip():
                            junk, indent = g.skip_leading_ws_with_indent(line,0,self.tab_width)
                            if indent <= startIndent:
                                self.underindentedComment(line)
                    underIndentedStart = None
            if trace: g.trace('returns',i,'underIndentedStart',underIndentedStart)
            return i,underIndentedStart,breakFlag
        #@-node:ekr.20070801080447:pythonNewlineHelper
        #@-node:ekr.20070712090019.1:skipCodeBlock (python) & helper
        #@+node:ekr.20070803101619:skipSigTail
        # This must be overridden in order to handle newlines properly.

        def skipSigTail(self,s,i):

            '''Skip from the end of the arg list to the start of the block.'''

            while i < len(s):
                ch = s[i]
                if ch == '\n':
                    break
                elif ch in (' ','\t',):
                    i += 1
                elif self.startsComment(s,i):
                    i = self.skipComment(s,i)
                else:
                    break

            return i,g.match(s,i,':')
        #@-node:ekr.20070803101619:skipSigTail
        #@-others
    #@-node:ekr.20070703122141.100:class pythonScanner (baseScannerClass)
    #@-node:ekr.20070703123334.2:Python scanner
    #@+node:ekr.20070713075352:Default scanner
    def scanUnknownFileType (self,s,p,ext,atAuto=False):

        c = self.c
        changed = c.isChanged()
        body = g.choose(atAuto,'','@ignore\n')
        if ext in ('.html','.htm'): body += '@language html\n'
        if ext in ('.txt','.text'): body += '@nocolor\n'
        c.setBodyString(p,body + self.rootLine + s)
        if atAuto:
            for p in p.self_and_subtree_iter():
                p.clearDirty()
            if not changed:
                c.setChanged(False)

        g.app.unitTestDict = {'result':True}
    #@-node:ekr.20070713075352:Default scanner
    #@-node:ekr.20031218072017.3241:Scanners for createOutline
    #@+node:ekr.20070713075450:Unit tests
    # atAuto must be False for unit tests: otherwise the test gets wiped out.

    def cUnitTest(self,p,fileName=None,s=None,showTree=False):
        return self.scannerUnitTest(p,atAuto=False,fileName=fileName,s=s,showTree=showTree,ext='.c')

    def cSharpUnitTest(self,p,fileName=None,s=None,showTree=False):
        return self.scannerUnitTest(p,atAuto=False,fileName=fileName,s=s,showTree=showTree,ext='.c#')

    def elispUnitTest(self,p,fileName=None,s=None,showTree=False):
        return self.scannerUnitTest (p,atAuto=False,fileName=fileName,s=s,showTree=showTree,ext='.el')

    def htmlUnitTest(self,p,fileName=None,s=None,showTree=False):
        return self.scannerUnitTest (p,atAuto=False,fileName=fileName,s=s,showTree=showTree,ext='.htm')

    def javaUnitTest(self,p,fileName=None,s=None,showTree=False):
        return self.scannerUnitTest (p,atAuto=False,fileName=fileName,s=s,showTree=showTree,ext='.java')

    def javaScriptUnitTest(self,p,fileName=None,s=None,showTree=False):
        return self.scannerUnitTest (p,atAuto=False,fileName=fileName,s=s,showTree=showTree,ext='.js')

    def pascalUnitTest(self,p,fileName=None,s=None,showTree=False):
        return self.scannerUnitTest (p,atAuto=False,fileName=fileName,s=s,showTree=showTree,ext='.pas')

    def phpUnitTest(self,p,fileName=None,s=None,showTree=False):
        return self.scannerUnitTest (p,atAuto=False,fileName=fileName,s=s,showTree=showTree,ext='.php')

    def pythonUnitTest(self,p,fileName=None,s=None,showTree=False):
        return self.scannerUnitTest (p,atAuto=False,fileName=fileName,s=s,showTree=showTree,ext='.py')

    def textUnitTest(self,p,fileName=None,s=None,showTree=False):
        return self.scannerUnitTest (p,atAuto=False,fileName=fileName,s=s,showTree=showTree,ext='.txt')

    def defaultImporterUnitTest(self,p,fileName=None,s=None,showTree=False):
        return self.scannerUnitTest (p,atAuto=False,fileName=fileName,s=s,ext='.xxx')
    #@+node:ekr.20070713082220:scannerUnitTest
    def scannerUnitTest (self,p,atAuto=False,ext=None,fileName=None,s=None,showTree=False):

        '''Run a unit test of an import scanner,
        i.e., create a tree from string s at location p.'''

        c = self.c ; h = p.headString() ; old_root = p.copy()
        oldChanged = c.changed
        c.beginUpdate()
        try:
            d = g.app.unitTestDict
            expectedErrors = d.get('expectedErrors')
            expectedErrorMessage = d.get('expectedErrorMessage')
            expectedMismatchLine = d.get('expectedMismatchLine')
            g.app.unitTestDict = {
                'expectedErrors':expectedErrors,
                'expectedErrorMessage':expectedErrorMessage,
                'expectedMismatchLine':expectedMismatchLine,
            }
            if not fileName: fileName = p.headString()
            if not s: s = self.removeSentinelsCommand([fileName],toString=True)
            title = g.choose(h.startswith('@test'),h[5:],h)
            self.createOutline(title.strip(),p.copy(),atAuto=atAuto,s=s,ext=ext)
            d = g.app.unitTestDict
            ok = ((d.get('result') and expectedErrors in (None,0)) or
                (
                    # checkTrialWrite returns *True* if the following match.
                    # d.get('result') == False and
                    d.get('actualErrors') == d.get('expectedErrors') and
                    d.get('actualMismatchLine') == d.get('expectedMismatchLine') and
                    (expectedErrorMessage is None or d.get('actualErrorMessage') == d.get('expectedErrorMessage'))
                ))
            if not ok:
                g.trace('result',d.get('result'),
                    'actualErrors',d.get('actualErrors'),
                    'expectedErrors',d.get('expectedErrors'),
                    'actualMismatchLine',d.get('actualMismatchLine'),
                    'expectedMismatchLine', d.get('expectedMismatchLine'),
                    '\nactualErrorMessage  ',d.get('actualErrorMessage'),
                    '\nexpectedErrorMessage',d.get('expectedErrorMessage'),
                )
            if not showTree and ok:
                while old_root.hasChildren():
                    old_root.firstChild().doDelete()
                c.setChanged(oldChanged)

        finally:
            c.selectPosition(old_root)
            c.endUpdate()

        if g.app.unitTesting:
            assert ok

        return ok
    #@-node:ekr.20070713082220:scannerUnitTest
    #@-node:ekr.20070713075450:Unit tests
    #@-node:ekr.20031218072017.3209:Import
    #@-others

class leoImportCommands (baseLeoImportCommands):
    """A class that implements Leo's import commands."""
    pass
#@-node:ekr.20031218072017.3206:@thin leoImport.py
#@-leo
