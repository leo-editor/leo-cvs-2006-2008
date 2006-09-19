#@+leo-ver=4-thin
#@+node:ekr.20031218072017.3018:@thin leoFileCommands.py
#@@language python
#@@tabwidth -4
#@@pagewidth 80

use_sax = False # For transition to sax-based read code.

#@<< imports >>
#@+node:ekr.20050405141130:<< imports >>
import leoGlobals as g

if g.app and g.app.use_psyco:
    # print "enabled psyco classes",__file__
    try: from psyco.classes import *
    except ImportError: pass
    
import leoNodes

import binascii
import cStringIO
import os
import pickle
import string
import xml.sax
import xml.sax.saxutils
#@nonl
#@-node:ekr.20050405141130:<< imports >>
#@nl

#@<< define exception classes >>
#@+node:ekr.20060918164811:<< define exception classes >>
class BadLeoFile(Exception):
    def __init__(self, message):
        self.message = message
        Exception.__init__(self,message) # Init the base class.
    def __str__(self):
        return "Bad Leo File:" + self.message
        
class invalidPaste(Exception):
    pass
#@nonl
#@-node:ekr.20060918164811:<< define exception classes >>
#@nl

class baseFileCommands:
    """A base class for the fileCommands subcommander."""
    #@    @+others
    #@+node:ekr.20031218072017.3019:leoFileCommands._init_
    def __init__(self,c):
    
        # g.trace("__init__", "fileCommands.__init__")
        self.c = c
        self.frame = c.frame
        self.nativeTnodeAttributes = ('tx',)
        self.nativeVnodeAttributes = (
            'a','descendentTnodeUnknownAttributes',
            'expanded','marks','t','tnodeList',
            # 'vtag',
        )
        self.initIvars()
    
    def initIvars(self):
    
        # General
        c = self.c
        self.maxTnodeIndex = 0
        self.numberOfTnodes = 0
        self.mFileName = ""
        self.fileDate = -1
        self.leo_file_encoding = c.config.new_leo_file_encoding
        # g.trace('self.leo_file_encoding',self.leo_file_encoding)
        # For reading
        self.checking = False # True: checking only: do *not* alter the outline.
        self.descendentExpandedList = []
        self.descendentMarksList = []
        self.fileFormatNumber = 0
        self.forbiddenTnodes = []
        self.descendentUnknownAttributesDictList = []
        self.ratio = 0.5
        self.fileBuffer = None ; self.fileIndex = 0
        if not use_sax:
            self.currentVnodeStack = [] # A stack of vnodes giving the current position.
            self.topVnodeStack     = [] # A stack of vnodes giving the top position.
            self.topPosition = None
        # For writing
        self.read_only = False
        self.outputFile = None
        self.openDirectory = None
        self.topVnode = None
        self.usingClipboard = False
        self.currentPosition = None
        # New in 3.12
        self.copiedTree = None
        self.tnodesDict = {}
            # keys are gnx strings as returned by canonicalTnodeIndex.
            # Values are gnx's.
    #@nonl
    #@-node:ekr.20031218072017.3019:leoFileCommands._init_
    #@+node:ekr.20031218072017.3020:Reading
    #@+node:ekr.20060919104836: Top-level
    #@+node:ekr.20031218072017.1559:getLeoOutlineFromClipboard & helpers
    def getLeoOutlineFromClipboard (self,s,reassignIndices=True):
        
        '''Read a Leo outline from string s in clipboard format.'''
    
        try:
            v = self.getLeoOutlineHelper(s,reassignIndices,checking=True)
            v = self.getLeoOutlineHelper(s,reassignIndices,checking=False)
        except invalidPaste:
            v = None
            g.es("Invalid Paste As Clone",color="blue")
        except BadLeoFile:
            v = None
            g.es("The clipboard is not valid ",color="blue")
    
        return v
        
    getLeoOutline = getLeoOutlineFromClipboard # for compatibility
    #@nonl
    #@+node:ekr.20031218072017.1557:finishPaste
    def finishPaste(self,reassignIndices=True):
        
        """Finish pasting an outline from the clipboard.
        
        Retain clone links if reassignIndices is False."""
    
        c = self.c
        current = c.currentPosition()
        if reassignIndices:
            #@        << reassign tnode indices >>
            #@+node:ekr.20031218072017.1558:<< reassign tnode indices >>
            #@+at 
            #@nonl
            # putLeoOutline calls assignFileIndices (when copying nodes) so 
            # that vnode can be associated with tnodes.
            # However, we must _reassign_ the indices here so that no "False 
            # clones" are created.
            #@-at
            #@@c
            
            current.clearVisitedInTree()
            
            for p in current.self_and_subtree_iter():
                t = p.v.t
                if not t.isVisited():
                    t.setVisited()
                    self.maxTnodeIndex += 1
                    t.setFileIndex(self.maxTnodeIndex)
            #@-node:ekr.20031218072017.1558:<< reassign tnode indices >>
            #@nl
        c.selectPosition(current)
        return current
    #@-node:ekr.20031218072017.1557:finishPaste
    #@+node:ekr.20060826052453.1:getLeoOutlineHelper
    def getLeoOutlineHelper (self,s,reassignIndices,checking):
        
        self.checking = checking
        self.usingClipboard = True
        self.fileBuffer = s ; self.fileIndex = 0
        self.descendentUnknownAttributesDictList = []
        v = None
    
        self.tnodesDict = {}
        if not reassignIndices:
            #@        << recreate tnodesDict >>
            #@+node:EKR.20040610134756:<< recreate tnodesDict >>
            nodeIndices = g.app.nodeIndices
            
            self.tnodesDict = {}
            
            for t in self.c.all_unique_tnodes_iter():
                tref = t.fileIndex
                if nodeIndices.isGnx(tref):
                    tref = nodeIndices.toString(tref)
                self.tnodesDict[tref] = t
                
            if 0:
                print '-'*40
                for key in self.tnodesDict.keys():
                    print key,self.tnodesDict[key]
            #@-node:EKR.20040610134756:<< recreate tnodesDict >>
            #@nl
        try:
            self.getXmlVersionTag()
            self.getXmlStylesheetTag()
            self.getTag("<leo_file>")
            self.getClipboardHeader()
            self.getVnodes(reassignIndices)
            self.getTnodes()
            self.getTag("</leo_file>")
            if not checking:
                v = self.finishPaste(reassignIndices)
        finally:
            self.fileBuffer = None ; self.fileIndex = 0
            self.usingClipboard = False
            self.tnodesDict = {}
        return v
    #@nonl
    #@-node:ekr.20060826052453.1:getLeoOutlineHelper
    #@+node:ekr.20031218072017.3022:getClipboardHeader
    def getClipboardHeader (self):
    
        if self.getOpenTag("<leo_header"):
            return # <leo_header> or <leo_header/> has been seen.
    
        while 1:
            if self.matchTag("file_format="):
                self.getDquote() ; self.fileFormatNumber = self.getLong() ; self.getDquote()
            elif self.matchTag("tnodes="):
                self.getDquote() ; self.getLong() ; self.getDquote() # no longer used
            elif self.matchTag("max_tnode_index="):
                self.getDquote() ; self.getLong() ; self.getDquote() # no longer used
            elif self.matchTag("></leo_header>"): # new in 4.2: allow this form.
                break
            else:
                self.getTag("/>")
                break
    #@-node:ekr.20031218072017.3022:getClipboardHeader
    #@-node:ekr.20031218072017.1559:getLeoOutlineFromClipboard & helpers
    #@+node:ekr.20031218072017.1553:getLeoFile
    # The caller should enclose this in begin/endUpdate.
    
    def getLeoFile (self,fileName,readAtFileNodesFlag=True,silent=False):
    
        c = self.c
        c.setChanged(False) # May be set when reading @file nodes.
        #@    << warn on read-only files >>
        #@+node:ekr.20031218072017.1554:<< warn on read-only files >>
        # os.access may not exist on all platforms.
        
        try:
            self.read_only = not os.access(fileName,os.W_OK)
        except AttributeError:
            self.read_only = False
        except UnicodeError:
            self.read_only = False
                
        if self.read_only:
            g.es("read only: " + fileName,color="red")
        #@-node:ekr.20031218072017.1554:<< warn on read-only files >>
        #@nl
        self.checking = False
        self.mFileName = c.mFileName
        self.initReadIvars()
        c.loading = True # disable c.changed
        
        try:
            ok = True
            if use_sax:
                self.readSaxFile(fileName=fileName,silent=silent)
            else:
                self.getAllLeoElements(fileName=fileName,silent=silent)
        except BadLeoFile, message:
            if not silent:
                g.es_exception()
                g.alert(self.mFileName + " is not a valid Leo file: " + str(message))
            ok = False
    
        if ok and readAtFileNodesFlag:
            # Redraw before reading the @file nodes so the screen isn't blank.
            # This is important for big files like LeoPy.leo.
            c.redraw_now()
            c.atFileCommands.readAll(c.rootVnode(),partialFlag=False)
        
        # New in 4.3.1: do this after reading derived files.
        if use_sax:
            self.resolveTnodeLists(c)
            self.restoreDescendentAttributes(c)
            setPositionsFromVnodes()
        else:
            if not self.usingClipboard:
                self.setPositionsFromStacks()
            if not c.currentPosition():
                c.setCurrentPosition(c.rootPosition())
    
        c.selectVnode(c.currentPosition()) # load body pane
        c.loading = False # reenable c.changed
        c.setChanged(c.changed) # Refresh the changed marker.
        if not use_sax:
            self.restoreDescendentAttributes()
        self.initReadIvars()
        return ok, self.ratio
    #@nonl
    #@-node:ekr.20031218072017.1553:getLeoFile
    #@+node:ekr.20031218072017.2009:newTnode
    def newTnode(self,index):
    
        if self.tnodesDict.has_key(index):
            g.es("bad tnode index: %s. Using empty text." % str(index))
            return leoNodes.tnode()
        else:
            # Create the tnode.  Use the _original_ index as the key in tnodesDict.
            t = leoNodes.tnode()
            self.tnodesDict[index] = t
        
            if type(index) not in (type(""),type(u"")):
                g.es("newTnode: unexpected index type:",type(index),index,color="red")
            
            # Convert any pre-4.1 index to a gnx.
            theId,time,n = gnx = g.app.nodeIndices.scanGnx(index,0)
            if time != None:
                t.setFileIndex(gnx)
    
            return t
    #@-node:ekr.20031218072017.2009:newTnode
    #@+node:ekr.20031218072017.3029:readAtFileNodes (leoAtFile)
    def readAtFileNodes (self):
    
        c = self.c ; p = c.currentPosition()
        
        c.beginUpdate()
        try:
            c.atFileCommands.readAll(p,partialFlag=True)
        finally:
            c.endUpdate()
        
        # Force an update of the body pane.
        c.setBodyString(p,p.bodyString())
        c.frame.body.onBodyChanged(undoType=None)
    #@-node:ekr.20031218072017.3029:readAtFileNodes (leoAtFile)
    #@+node:ekr.20031218072017.2297:open (leoFileCommands)
    def open(self,theFile,fileName,readAtFileNodesFlag=True,silent=False):
    
        c = self.c ; frame = c.frame
        if not use_sax: # Read the entire file into the buffer
            self.fileBuffer = theFile.read() ; theFile.close()
            self.fileIndex = 0
        #@    << Set the default directory >>
        #@+node:ekr.20031218072017.2298:<< Set the default directory >>
        #@+at 
        #@nonl
        # The most natural default directory is the directory containing the 
        # .leo file that we are about to open.  If the user has specified the 
        # "Default Directory" preference that will over-ride what we are about 
        # to set.
        #@-at
        #@@c
        
        theDir = g.os_path_dirname(fileName)
        
        if len(theDir) > 0:
            c.openDirectory = theDir
        #@-node:ekr.20031218072017.2298:<< Set the default directory >>
        #@nl
        self.topPosition = None
        ok, ratio = self.getLeoFile(
            fileName,
            readAtFileNodesFlag=readAtFileNodesFlag,
            silent=silent)
        frame.resizePanesToRatio(ratio,frame.secondary_ratio)
        if 0: # 1/30/04: this is useless.
            if self.topPosition: 
                c.setTopVnode(self.topPosition)
        if not use_sax: # Delete the file buffer
            self.fileBuffer = ""
        return ok
    #@nonl
    #@-node:ekr.20031218072017.2297:open (leoFileCommands)
    #@+node:ekr.20031218072017.3030:readOutlineOnly
    def readOutlineOnly (self,theFile,fileName):
    
        c = self.c
        # Read the entire file into the buffer
        self.fileBuffer = theFile.read() ; theFile.close()
        self.fileIndex = 0
        #@    << Set the default directory >>
        #@+node:ekr.20031218072017.2298:<< Set the default directory >>
        #@+at 
        #@nonl
        # The most natural default directory is the directory containing the 
        # .leo file that we are about to open.  If the user has specified the 
        # "Default Directory" preference that will over-ride what we are about 
        # to set.
        #@-at
        #@@c
        
        theDir = g.os_path_dirname(fileName)
        
        if len(theDir) > 0:
            c.openDirectory = theDir
        #@-node:ekr.20031218072017.2298:<< Set the default directory >>
        #@nl
        c.beginUpdate()
        try:
            ok, ratio = self.getLeoFile(fileName,readAtFileNodesFlag=False)
        finally:
            c.endUpdate()
        c.frame.deiconify()
        vflag,junk,secondary_ratio = self.frame.initialRatios()
        c.frame.resizePanesToRatio(ratio,secondary_ratio)
        if 0: # 1/30/04: this is useless.
            # This should be done after the pane size has been set.
            if self.topPosition:
                c.frame.tree.setTopPosition(self.topPosition)
                c.redraw_now()
        # delete the file buffer
        self.fileBuffer = ""
        return ok
    #@-node:ekr.20031218072017.3030:readOutlineOnly
    #@-node:ekr.20060919104836: Top-level
    #@+node:ekr.20060919133249:Common
    # Methods common to both the sax and non-sax code.
    #@nonl
    #@+node:ekr.20060919142200.1:initReadIvars
    def initReadIvars (self):
    
        self.descendentUnknownAttributesDictList = []
        self.descendentExpandedList = []
        self.descendentMarksList = []
        self.tnodesDict = {}
    #@nonl
    #@-node:ekr.20060919142200.1:initReadIvars
    #@+node:ekr.20031218072017.2004:canonicalTnodeIndex
    def canonicalTnodeIndex(self,index):
        
        """Convert Tnnn to nnn, leaving gnx's unchanged."""
    
        # index might be Tnnn, nnn, or gnx.
        theId,time,n = g.app.nodeIndices.scanGnx(index,0)
        if time == None: # A pre-4.1 file index.
            if index[0] == "T":
                index = index[1:]
    
        return index
    #@-node:ekr.20031218072017.2004:canonicalTnodeIndex
    #@+node:EKR.20040627120120:restoreDescendentAttributes
    def restoreDescendentAttributes (self):
        
        c = self.c
    
        for resultDict in self.descendentUnknownAttributesDictList:
            for gnx in resultDict.keys():
                tref = self.canonicalTnodeIndex(gnx)
                t = self.tnodesDict.get(tref)
                if t:
                    t.unknownAttributes = resultDict[gnx]
                    t._p_changed = 1
                # else: g.trace("can not find tnode: gnx = %s" % gnx,color="red")
        
        marks = {} ; expanded = {}
        for gnx in self.descendentExpandedList:
            t = self.tnodesDict.get(gnx)
            if t: expanded[t]=t
            # else: g.trace("can not find tnode: gnx = %s" % gnx,color="red")
            
        for gnx in self.descendentMarksList:
            t = self.tnodesDict.get(gnx)
            if t: marks[t]=t
            # else: g.trace("can not find tnode: gnx = %s" % gnx,color="red")
        
        if marks or expanded:
            # g.trace("marks",len(marks),"expanded",len(expanded))
            for p in c.all_positions_iter():
                if marks.get(p.v.t):
                    p.v.initMarkedBit()
                        # This was the problem: was p.setMark.
                        # There was a big performance bug in the mark hook in the Node Navigator plugin.
                if expanded.get(p.v.t):
                    p.expand()
    #@nonl
    #@-node:EKR.20040627120120:restoreDescendentAttributes
    #@+node:ekr.20060919110638.11:resolveTnodeLists (SAX)
    def resolveTnodeLists (self,c):
        
        for p in c.allNodes_iter():
            if hasattr(p.v,'tempTnodeList'):
                result = []
                for tnx in p.v.tempTnodeList:
                    index = self.canonicalTnodeIndex(tnx)
                    t = self.tnodesDict.get(index)
                    if t:
                        g.trace(v,tnx,t)
                        result.append(t)
                    else:
                        g.trace('No tnode for %s' % tnx)
                p.v.t.tnodeList = result
                delattr(p.v,'tempTnodeList')
    #@nonl
    #@-node:ekr.20060919110638.11:resolveTnodeLists (SAX)
    #@+node:ekr.20060919110638.13:setPositionsFromVnodes (Sax)
    def setPositionsFromVnodes (self,c):
        
        v = self.currentVnode
        if not v: return
    
        for p in c.allNodes_iter():
            if p.v == v:
                c.selectPosition(p)
                break
    #@nonl
    #@-node:ekr.20060919110638.13:setPositionsFromVnodes (Sax)
    #@-node:ekr.20060919133249:Common
    #@+node:ekr.20031218072017.3021:Non-sax
    if not use_sax:
        #@    @+others
        #@+node:ekr.20040326054052:setPositionsFromStacks (silly)
        def setPositionsFromStacks (self):
            
            c = self.c
        
            current = self.convertStackToPosition(self.currentVnodeStack)
            
            if current:
                # g.trace('using convertStackToPosition',current)
                c.setCurrentPosition(current)
            else:
                # g.trace(self.currentVnodeStack)
                c.setCurrentPosition(c.rootPosition())
                
            # At present this is useless: the drawing code doesn't set the top position properly.
            if 0:
                top = self.convertStackToPosition(self.topVnodeStack)
                if top:
                    c.setTopPosition(top)
        #@nonl
        #@-node:ekr.20040326054052:setPositionsFromStacks (silly)
        #@+node:ekr.20040326052245:convertStackToPosition (silly)
        def convertStackToPosition (self,stack):
        
            c = self.c ; p2 = None
            if not stack: return None
        
            for p in c.allNodes_iter():
                if p.v == stack[0]:
                    p2 = p.copy()
                    for n in xrange(len(stack)):
                        if not p2: break
                        # g.trace("compare",n,p2.v,stack[n])
                        if p2.v != stack[n]:
                            p2 = None
                        elif n + 1 == len(stack):
                            break
                        else:
                            p2.moveToParent()
                    if p2:
                        return p
        
            return None
        #@-node:ekr.20040326052245:convertStackToPosition (silly)
        #@+node:ekr.20031218072017.1243:get, match & skip (basic)
        #@+node:ekr.20031218072017.1244:get routines (basic)
        #@+node:EKR.20040526204706:getBool
        def getBool (self):
        
            self.skipWs() # guarantees at least one more character.
            ch = self.fileBuffer[self.fileIndex]
            if ch == '0':
                self.fileIndex += 1 ; return False
            elif ch == '1':
                self.fileIndex += 1 ; return True
            else:
                raise BadLeoFile("expecting bool constant")
        #@-node:EKR.20040526204706:getBool
        #@+node:EKR.20040526204706.1:getDouble
        def getDouble (self):
        
            self.skipWs()
            i = self.fileIndex ; buf = self.fileBuffer
            floatChars = string.digits + 'e' + 'E' + '.' + '+' + '-'
            n = len(buf)
            while i < n and buf[i] in floatChars:
                i += 1
            if i == self.fileIndex:
                raise BadLeoFile("expecting float constant")
            val = float(buf[self.fileIndex:i])
            self.fileIndex = i
            return val
        #@-node:EKR.20040526204706.1:getDouble
        #@+node:EKR.20040526204706.2:getDqBool
        def getDqBool (self):
        
            self.getDquote()
            val = self.getBool()
            self.getDquote()
            return val
        #@-node:EKR.20040526204706.2:getDqBool
        #@+node:EKR.20040526204706.3:getDqString
        def getDqString (self):
        
            self.getDquote()
            i = self.fileIndex
            self.fileIndex = j = string.find(self.fileBuffer,'"',i)
            if j == -1: raise BadLeoFile("unterminated double quoted string")
            s = self.fileBuffer[i:j]
            self.getDquote()
            return s
        #@-node:EKR.20040526204706.3:getDqString
        #@+node:EKR.20040526204706.4:getDquote
        def getDquote (self):
        
            self.getTag('"')
        #@-node:EKR.20040526204706.4:getDquote
        #@+node:ekr.20031218072017.3024:getEscapedString
        def getEscapedString (self):
        
            # The next '<' begins the ending tag.
            i = self.fileIndex
            self.fileIndex = j = string.find(self.fileBuffer,'<',i)
            if j == -1:
                print self.fileBuffer[i:]
                raise BadLeoFile("unterminated escaped string")
            else:
                # Allocates memory
                return self.xmlUnescape(self.fileBuffer[i:j])
        #@-node:ekr.20031218072017.3024:getEscapedString
        #@+node:EKR.20040526204706.5:getIndex
        def getIndex (self):
        
            val = self.getLong()
            if val < 0: raise BadLeoFile("expecting index")
            return val
        #@-node:EKR.20040526204706.5:getIndex
        #@+node:EKR.20040526204706.6:getLong
        def getLong (self):
        
            self.skipWs() # guarantees at least one more character.
            i = self.fileIndex
            if self.fileBuffer[i] == '-':
                i += 1
            n = len(self.fileBuffer)
            while i < n and self.fileBuffer[i] in string.digits:
                i += 1
            if i == self.fileIndex:
                raise BadLeoFile("expecting int constant")
            val = int(self.fileBuffer[self.fileIndex:i])
            self.fileIndex = i
            return val
        #@-node:EKR.20040526204706.6:getLong
        #@+node:EKR.20040526204706.7:getOpenTag
        def getOpenTag (self,tag):
            
            """
            Look ahead for collapsed tag: tag may or may not end in ">"
            Skips tag and /> if found, otherwise does not alter index.
            Returns True if the closing part was found.
            Throws BadLeoFile if the tag does not exist.
            """
        
            if tag[-1] == ">":
                # Only the tag itself or a collapsed tag are valid.
                if self.matchTag(tag):
                    return False # Not a collapsed tag.
                elif self.matchTag(tag[:-1]):
                    # It must be a collapsed tag.
                    self.skipWs()
                    if self.matchTag("/>"):
                        return True
                print "getOpenTag(", tag, ") failed:"
                raise BadLeoFile("expecting" + tag)
            else:
                # The tag need not be followed by "/>"
                if self.matchTag(tag):
                    old_index = self.fileIndex
                    self.skipWs()
                    if self.matchTag("/>"):
                        return True
                    else:
                        self.fileIndex = old_index
                        return False
                else:
                    print "getOpenTag(", tag, ") failed:"
                    raise BadLeoFile("expecting" + tag)
        #@-node:EKR.20040526204706.7:getOpenTag
        #@+node:EKR.20040526204706.8:getStringToTag
        def getStringToTag (self,tag):
        
            buf = self.fileBuffer
            blen = len(buf) ; tlen = len(tag)
            i = j = self.fileIndex
            while i < blen:
                if tag == buf[i:i+tlen]:
                    self.fileIndex = i
                    return buf[j:i]
                else: i += 1
            raise BadLeoFile("expecting string terminated by " + tag)
            return ""
        #@-node:EKR.20040526204706.8:getStringToTag
        #@+node:EKR.20040526204706.9:getTag
        def getTag (self,tag):
            
            """
            Look ahead for closing />
            Return True if found.
            """
            
            if self.matchTag(tag):
                return
            else:
                print "getTag(", tag, ") failed:"
                raise BadLeoFile("expecting" + tag)
        #@-node:EKR.20040526204706.9:getTag
        #@+node:EKR.20040526204036:getUnknownTag
        def getUnknownTag(self):
            
            self.skipWsAndNl() # guarantees at least one more character.
            tag = self.getStringToTag('=')
            if not tag:
                print "getUnknownTag failed"
                raise BadLeoFile("unknown tag not followed by '='")
        
            self.fileIndex += 1
            val = self.getDqString()
            # g.trace(tag,val)
            return tag,val
        #@-node:EKR.20040526204036:getUnknownTag
        #@-node:ekr.20031218072017.1244:get routines (basic)
        #@+node:ekr.20031218072017.1245:match routines
        def matchChar (self,ch):
            self.skipWs() # guarantees at least one more character.
            if ch == self.fileBuffer[self.fileIndex]:
                self.fileIndex += 1 ; return True
            else: return False
        
        # Warning: does not check for end-of-word,
        # so caller must match prefixes first.
        def matchTag (self,tag):
            self.skipWsAndNl() # guarantees at least one more character.
            i = self.fileIndex
            if tag == self.fileBuffer[i:i+len(tag)]:
                self.fileIndex += len(tag)
                return True
            else:
                return False
        
        def matchTagWordIgnoringCase (self,tag):
            self.skipWsAndNl() # guarantees at least one more character.
            i = self.fileIndex
            tag = string.lower(tag)
            j = g.skip_c_id(self.fileBuffer,i)
            word = self.fileBuffer[i:j]
            word = string.lower(word)
            if tag == word:
                self.fileIndex += len(tag)
                return True
            else:
                return False
        #@-node:ekr.20031218072017.1245:match routines
        #@+node:ekr.20031218072017.3027:skipWs
        def skipWs (self):
        
            while self.fileIndex < len(self.fileBuffer):
                ch = self.fileBuffer[self.fileIndex]
                if ch == ' ' or ch == '\t':
                    self.fileIndex += 1
                else: break
        
            # The caller is entitled to get the next character.
            if  self.fileIndex >= len(self.fileBuffer):
                raise BadLeoFile("")
        #@-node:ekr.20031218072017.3027:skipWs
        #@+node:ekr.20031218072017.3028:skipWsAndNl
        def skipWsAndNl (self):
        
            while self.fileIndex < len(self.fileBuffer):
                ch = self.fileBuffer[self.fileIndex]
                if ch == ' ' or ch == '\t' or ch == '\r' or ch == '\n':
                    self.fileIndex += 1
                else: break
        
            # The caller is entitled to get the next character.
            if  self.fileIndex >= len(self.fileBuffer):
                raise BadLeoFile("")
        #@-node:ekr.20031218072017.3028:skipWsAndNl
        #@+node:ekr.20031218072017.3031:xmlUnescape
        def xmlUnescape(self,s):
        
            if s:
                s = string.replace(s, '\r', '')
                s = string.replace(s, "&lt;", '<')
                s = string.replace(s, "&gt;", '>')
                s = string.replace(s, "&amp;", '&')
            return s
        #@-node:ekr.20031218072017.3031:xmlUnescape
        #@-node:ekr.20031218072017.1243:get, match & skip (basic)
        #@+node:ekr.20031218072017.1555:getAllLeoElements
        def getAllLeoElements (self,fileName,silent):
            c = self.c
        
            self.getXmlVersionTag()
            self.getXmlStylesheetTag()
        
            self.getTag("<leo_file>") # Must match exactly.
            self.getLeoHeader()
            self.getGlobals()
            self.getPrefs()
            self.getFindPanelSettings()
            
            # Causes window to appear.
            c.frame.resizePanesToRatio(c.frame.ratio,c.frame.secondary_ratio)
            if not silent:
                g.es("reading: " + fileName)
            
            self.getVnodes()
            self.getTnodes()
            self.getCloneWindows()
            self.getTag("</leo_file>")
        #@nonl
        #@-node:ekr.20031218072017.1555:getAllLeoElements
        #@+node:ekr.20031218072017.3023:getCloneWindows
        # For compatibility with old file formats.
        
        def getCloneWindows (self):
        
            if not self.matchTag("<clone_windows>"):
                return # <clone_windows/> seen.
        
            while self.matchTag("<clone_window vtag=\"V"):
                self.getLong() ; self.getDquote() ; self.getTag(">")
                if not self.getOpenTag("<global_window_position"):
                    self.getTag("<global_window_position")
                    self.getPosition()
                    self.getTag("/>")
                self.getTag("</clone_window>")
            self.getTag("</clone_windows>")
        #@-node:ekr.20031218072017.3023:getCloneWindows
        #@+node:ekr.20031218072017.2064:getFindPanelSettings
        def getFindPanelSettings (self):
            
            if self.getOpenTag("<find_panel_settings"):
                return # <find_panel_settings/> seen.
            
            # New in 4.3: ignore all pre-4.3 find settings.
            while 1:
                if   self.matchTag("batch="):           self.getDqBool()
                elif self.matchTag("ignore_case="):     self.getDqBool()
                elif self.matchTag("mark_changes="):    self.getDqBool()
                elif self.matchTag("mark_finds="):      self.getDqBool()
                elif self.matchTag("node_only="):       self.getDqBool()
                elif self.matchTag("pattern_match="):   self.getDqBool()
                elif self.matchTag("reverse="):         self.getDqBool()
                elif self.matchTag("script_change="):   self.getDqBool()
                elif self.matchTag("script_search="):   self.getDqBool()
                elif self.matchTag("search_headline="): self.getDqBool()
                elif self.matchTag("search_body="):     self.getDqBool()
                elif self.matchTag("selection_only="):  self.getDqBool()
                elif self.matchTag("suboutline_only="): self.getDqBool()
                elif self.matchTag("whole_word="):      self.getDqBool()
                elif self.matchTag("wrap="):            self.getDqBool()
                elif self.matchTag(">"): break
                else: self.getUnknownTag() # Ignore all other tags.
            # Allow only <find_string> or <find_string/>
            if self.getOpenTag("<find_string>"): 
                pass
            else:
                self.getEscapedString() ; self.getTag("</find_string>")
            # Allow only <change_string> or <change_string/>
            if self.getOpenTag("<change_string>"): 
                pass
            else:
                self.getEscapedString() ; self.getTag("</change_string>")
            self.getTag("</find_panel_settings>")
        #@-node:ekr.20031218072017.2064:getFindPanelSettings
        #@+node:ekr.20031218072017.2306:getGlobals
        def getGlobals (self):
        
            if self.getOpenTag("<globals"):
                # <globals/> seen: set reasonable defaults:
                self.ratio = 0.5
                y,x,h,w = 50,50,500,700
            else:
                self.getTag("body_outline_ratio=\"")
                self.ratio = self.getDouble() ; self.getDquote() ; self.getTag(">")
        
                self.getTag("<global_window_position")
                y,x,h,w = self.getPosition()
                self.getTag("/>")
        
                self.getTag("<global_log_window_position")
                self.getPosition()
                self.getTag("/>") # no longer used.
        
                self.getTag("</globals>")
        
            # Redraw the window before writing into it.
            self.frame.setTopGeometry(w,h,x,y)
            self.frame.deiconify()
            self.frame.lift()
            self.frame.update()
        #@-node:ekr.20031218072017.2306:getGlobals
        #@+node:ekr.20031218072017.1970:getLeoHeader
        def getLeoHeader (self):
        
            # Set defaults.
            self.maxTnodeIndex = 0
            self.numberOfTnodes = 0
        
            if self.getOpenTag("<leo_header"):
                return # <leo_header/> seen.
        
            # New in version 1.7: attributes may appear in any order.
            while 1:
                if self.matchTag("file_format="):
                    self.getDquote() ; self.fileFormatNumber = self.getLong() ; self.getDquote()
                elif self.matchTag("tnodes="):
                    self.getDquote() ; self.numberOfTnodes = self.getLong() ; self.getDquote()
                elif self.matchTag("max_tnode_index="):
                    self.getDquote() ; self.maxTnodeIndex = self.getLong() ; self.getDquote()
                    # g.trace("max_tnode_index:",self.maxTnodeIndex)
                elif self.matchTag("clone_windows="):
                    self.getDquote() ; self.getLong() ; self.getDquote() # no longer used.
                elif self.matchTag("></leo_header>"): # new in 4.2: allow this form.
                    break
                else:
                    self.getTag("/>")
                    break
        #@-node:ekr.20031218072017.1970:getLeoHeader
        #@+node:ekr.20031218072017.3025:getPosition
        def getPosition (self):
        
            top = left = height = width = 0
            # New in version 1.7: attributes may appear in any order.
            while 1:
                if self.matchTag("top=\""):
                    top = self.getLong() ; self.getDquote()
                elif self.matchTag("left=\""):
                    left = self.getLong() ; self.getDquote()
                elif self.matchTag("height=\""):
                    height = self.getLong() ; self.getDquote()
                elif self.matchTag("width=\""):
                    width = self.getLong() ; self.getDquote()
                else: break
            return top, left, height, width
        #@-node:ekr.20031218072017.3025:getPosition
        #@+node:ekr.20031218072017.2062:getPrefs
        # Note: Leo 4.3 does not write these settings to local .leo files.
        # Instead, corresponding settings are contained in leoConfig.leo files.
        
        def getPrefs (self):
        
            c = self.c
            
            if self.getOpenTag("<preferences"):
                return # <preferences/> seen
        
            table = (
                ("allow_rich_text",None,None), # Ignored.
                ("tab_width","tab_width",self.getLong),
                ("page_width","page_width",self.getLong),
                ("tangle_bat","tangle_batch_flag",self.getBool),
                ("untangle_bat","untangle_batch_flag",self.getBool),
                ("output_doc_chunks","output_doc_flag",self.getBool),
                ("noweb_flag",None,None), # Ignored.
                ("extended_noweb_flag",None,None), # Ignored.
                ("defaultTargetLanguage","target_language",self.getTargetLanguage),
                ("use_header_flag","use_header_flag",self.getBool))
            
            done = False
            while 1:
                found = False
                for tag,var,f in table:
                    if self.matchTag("%s=" % tag):
                        if var:
                            self.getDquote() ; val = f() ; self.getDquote()
                            setattr(c,var,val)
                            # g.trace(var,val)
                        else:
                            self.getDqString()
                        found = True ; break
                if not found:
                    if self.matchTag("/>"):
                        done = True ; break
                    if self.matchTag(">"):
                        break
                    else: # New in 4.1: ignore all other tags.
                        self.getUnknownTag()
        
            if not done:
                while 1:
                    if self.matchTag("<defaultDirectory>"):
                        # New in version 0.16.
                        c.tangle_directory = self.getEscapedString()
                        self.getTag("</defaultDirectory>")
                        if not g.os_path_exists(c.tangle_directory):
                            g.es("default tangle directory not found:" + c.tangle_directory)
                    elif self.matchTag("<TSyntaxMemo_options>"):
                        self.getEscapedString() # ignored
                        self.getTag("</TSyntaxMemo_options>")
                    else: break
                self.getTag("</preferences>")
        #@+node:ekr.20031218072017.2063:getTargetLanguage
        def getTargetLanguage (self):
            
            # Must match longer tags before short prefixes.
            for name in g.app.language_delims_dict.keys():
                if self.matchTagWordIgnoringCase(name):
                    language = name.replace("/","")
                    # self.getDquote()
                    return language
                    
            return "c" # default
        #@-node:ekr.20031218072017.2063:getTargetLanguage
        #@-node:ekr.20031218072017.2062:getPrefs
        #@+node:ekr.20031218072017.3026:getSize
        def getSize (self):
        
            # New in version 1.7: attributes may appear in any order.
            height = 0 ; width = 0
            while 1:
                if self.matchTag("height=\""):
                    height = self.getLong() ; self.getDquote()
                elif self.matchTag("width=\""):
                    width = self.getLong() ; self.getDquote()
                else: break
            return height, width
        #@-node:ekr.20031218072017.3026:getSize
        #@+node:ekr.20031218072017.1561:getTnode (changed for 4.4)
        def getTnode (self):
        
            # we have already matched <t.
            index = -1 ; attrDict = {}
        
            # New in Leo 4.4: support collapsed tnodes.
            if self.matchTag('/>'): # A collapsed tnode.
                return
        
            # Attributes may appear in any order.
            while 1:
                if self.matchTag("tx="):
                    # New for 4.1.  Read either "Tnnn" or "gnx".
                    index = self.getDqString()
                elif self.matchTag("rtf=\"1\""): pass # ignored
                elif self.matchTag("rtf=\"0\""): pass # ignored
                elif self.matchTag(">"):         break
                else: # New for 4.0: allow unknown attributes.
                    # New in 4.2: allow pickle'd and hexlify'ed values.
                    attr,val = self.getUa("tnode")
                    if attr: attrDict[attr] = val
                    
            # index might be Tnnn, nnn, or gnx.
            theId,time,n = g.app.nodeIndices.scanGnx(index,0)
            if time == None: # A pre-4.1 file index.
                if index[0] == "T":
                    index = index[1:]
        
            index = self.canonicalTnodeIndex(index)
            t = self.tnodesDict.get(index)
            #@    << handle unknown attributes >>
            #@+node:ekr.20031218072017.1564:<< handle unknown attributes >>
            keys = attrDict.keys()
            if keys:
                t.unknownAttributes = attrDict
                t._p_changed = 1
                if 0: # For debugging.
                    s = "unknown attributes for tnode"
                    g.es_print(s, color = "blue")
                    for key in keys:
                        s = "%s = %s" % (key,attrDict.get(key))
                        g.es_print(s)
            #@-node:ekr.20031218072017.1564:<< handle unknown attributes >>
            #@nl
            if t:
                s = self.getEscapedString()
                t.setTnodeText(s,encoding=self.leo_file_encoding)
            else:
                g.es("no tnode with index: %s.  The text will be discarded" % str(index))
            self.getTag("</t>")
        #@-node:ekr.20031218072017.1561:getTnode (changed for 4.4)
        #@+node:ekr.20031218072017.2008:getTnodeList (4.0,4.2)
        def getTnodeList (self,s):
        
            """Parse a list of tnode indices in string s."""
            
            # Remember: entries in the tnodeList correspond to @+node sentinels, _not_ to tnodes!
            
            fc = self ; 
        
            indexList = s.split(',') # The list never ends in a comma.
            tnodeList = []
            for index in indexList:
                index = self.canonicalTnodeIndex(index)
                t = fc.tnodesDict.get(index)
                if not t:
                    # Not an error: create a new tnode and put it in fc.tnodesDict.
                    # g.trace("not allocated: %s" % index)
                    t = self.newTnode(index)
                tnodeList.append(t)
                
            # if tnodeList: g.trace(len(tnodeList))
            return tnodeList
        #@-node:ekr.20031218072017.2008:getTnodeList (4.0,4.2)
        #@+node:ekr.20031218072017.1560:getTnodes
        def getTnodes (self):
        
            # A slight change: we require a tnodes element.  But Leo always writes this.
            if self.getOpenTag("<tnodes>"):
                return # <tnodes/> seen.
            
            while self.matchTag("<t"):
                    self.getTnode()
        
            self.getTag("</tnodes>")
        #@-node:ekr.20031218072017.1560:getTnodes
        #@+node:EKR.20040526204036.1:getUa
        # changed for 4.3.
        
        def getUa(self,nodeType):
            
            """Parse an unknown attribute in a <v> or <t> element."""
            
            __pychecker__ = '--no-argsused' # nodeType not used: good for debugging.
            
            # New in 4.2.  The unknown tag has been pickled and hexlify'd.
            attr,val = self.getUnknownTag()
            if not attr:
                return None,None
                
            # New in 4.3: leave string attributes starting with 'str_' alone.
            if attr.startswith('str_') and type(val) == type(''):
                # g.trace(attr,val)
                return attr,val
                
            # New in 4.3: convert attributes starting with 'b64_' using the base64 conversion.
            if 0: # Not ready yet.
                if attr.startswith('b64_'):
                    try: pass
                    except Exception: pass
                
            try:
                binString = binascii.unhexlify(val) # Throws a TypeError if val is not a hex string.
            except TypeError:
                # Assume that Leo 4.1 wrote the attribute.
                # g.trace('4.1 val:',val2)
                return attr,val
            try:
                # No change needed to support protocols.
                val2 = pickle.loads(binString)
                # g.trace('v.3 val:',val2)
                return attr,val2
            except (pickle.UnpicklingError,ImportError):
                return attr,val
        #@-node:EKR.20040526204036.1:getUa
        #@+node:ekr.20031218072017.1566:getVnode & helpers
        # changed for 4.2 & 4.4
        def getVnode (self,parent,back,skip,appendToCurrentStack,appendToTopStack):
        
            v = None
            setCurrent = setExpanded = setMarked = setOrphan = setTop = False
            tref = -1 ; headline = '' ; tnodeList = None ; attrDict = {}
        
            # we have already matched <v.
            
            # New in Leo 4.4: support collapsed tnodes.
            if self.matchTag('/>'): # A collapsed vnode.
                v,skip2 = self.createVnode(parent,back,tref,headline,attrDict)
                if self.checking: return None
                else: return v
            
            while 1:
                if self.matchTag("a=\""):
                    #@            << Handle vnode attribute bits >>
                    #@+node:ekr.20031218072017.1567:<< Handle vnode attribute bits  >>
                    # The a=" has already been seen.
                    while 1:
                        if   self.matchChar('C'): pass # Not used: clone bits are recomputed later.
                        elif self.matchChar('D'): pass # Not used.
                        elif self.matchChar('E'): setExpanded = True
                        elif self.matchChar('M'): setMarked = True
                        elif self.matchChar('O'): setOrphan = True
                        elif self.matchChar('T'): setTop = True
                        elif self.matchChar('V'): setCurrent = True
                        else: break
                    
                    self.getDquote()
                    #@-node:ekr.20031218072017.1567:<< Handle vnode attribute bits  >>
                    #@nl
                elif self.matchTag("t="):
                    # New for 4.1.  Read either "Tnnn" or "gnx".
                    tref = index = self.getDqString()
                    if self.usingClipboard:
                        #@                << raise invalidPaste if the tnode is in self.forbiddenTnodes >>
                        #@+node:ekr.20041023110111:<< raise invalidPaste if the tnode is in self.forbiddenTnodes >>
                        # Bug fix in 4.3 a1: make sure we have valid paste.
                        theId,time,n = g.app.nodeIndices.scanGnx(index,0)
                        if not time and index[0] == "T":
                            index = index[1:]
                            
                        index = self.canonicalTnodeIndex(index)
                        t = self.tnodesDict.get(index)
                        
                        if t in self.forbiddenTnodes:
                            # g.trace(t)
                            raise invalidPaste
                        #@-node:ekr.20041023110111:<< raise invalidPaste if the tnode is in self.forbiddenTnodes >>
                        #@nl
                elif self.matchTag("vtag=\"V"):
                    self.getIndex() ; self.getDquote() # ignored
                elif self.matchTag("tnodeList="):
                    s = self.getDqString()
                    tnodeList = self.getTnodeList(s) # New for 4.0
                elif self.matchTag("descendentTnodeUnknownAttributes="):
                    # New for 4.2, deprecated for 4.3?
                    s = self.getDqString()
                    theDict = self.getDescendentUnknownAttributes(s)
                    if theDict:
                        self.descendentUnknownAttributesDictList.append(theDict)
                elif self.matchTag("expanded="): # New in 4.2
                    s = self.getDqString()
                    self.descendentExpandedList.extend(self.getDescendentAttributes(s,tag="expanded"))
                elif self.matchTag("marks="): # New in 4.2.
                    s = self.getDqString()
                    self.descendentMarksList.extend(self.getDescendentAttributes(s,tag="marks"))
                elif self.matchTag(">"):
                    break
                else: # New for 4.0: allow unknown attributes.
                    # New in 4.2: allow pickle'd and hexlify'ed values.
                    attr,val = self.getUa("vnode")
                    if attr: attrDict[attr] = val
            # Headlines are optional.
            if self.matchTag("<vh>"):
                headline = self.getEscapedString() ; self.getTag("</vh>")
            # g.trace("skip:",skip,"parent:",parent,"back:",back,"headline:",headline)
            if skip:
                v = self.getExistingVnode(tref,headline)
                if v: # Bug fix: 4/18/05: The headline may change during paste as clone.
                    v.initHeadString(headline,encoding=self.leo_file_encoding)
            if v is None:
                v,skip2 = self.createVnode(parent,back,tref,headline,attrDict)
                if not self.checking:
                    skip = skip or skip2
                    if tnodeList:
                        v.t.tnodeList = tnodeList # New for 4.0, 4.2: now in tnode.
                    
            if not self.checking:
                #@        << Set the remembered status bits >>
                #@+node:ekr.20031218072017.1568:<< Set the remembered status bits >>
                if setCurrent:
                    self.currentVnodeStack = [v]
                
                if setTop:
                    self.topVnodeStack = [v]
                    
                if setExpanded:
                    v.initExpandedBit()
                    
                if setMarked:
                    v.initMarkedBit() # 3/25/03: Do not call setMarkedBit here!
                
                if setOrphan:
                    v.setOrphan()
                #@-node:ekr.20031218072017.1568:<< Set the remembered status bits >>
                #@nl
        
            # Recursively create all nested nodes.
            parent = v ; back = None
            while self.matchTag("<v"):
                append1 = appendToCurrentStack and len(self.currentVnodeStack) == 0
                append2 = appendToTopStack and len(self.topVnodeStack) == 0
                back = self.getVnode(parent,back,skip,
                    appendToCurrentStack=append1,appendToTopStack=append2)
            
            if not self.checking:
                #@        << Append to current or top stack >>
                #@+node:ekr.20040326055828:<< Append to current or top stack >>
                if not setCurrent and len(self.currentVnodeStack) > 0 and appendToCurrentStack:
                    #g.trace("append current",v)
                    self.currentVnodeStack.append(v)
                    
                if not setTop and len(self.topVnodeStack) > 0 and appendToTopStack:
                    #g.trace("append top",v)
                    self.topVnodeStack.append(v)
                #@-node:ekr.20040326055828:<< Append to current or top stack >>
                #@nl
        
            # End this vnode.
            self.getTag("</v>")
            return v
        #@nonl
        #@+node:ekr.20031218072017.1860:createVnode
        # (changed for 4.2) sets skip
        
        def createVnode (self,parent,back,tref,headline,attrDict):
            
            # g.trace(parent,headline)
            v = None ; c = self.c
            # Shared tnodes are placed in the file even if empty.
            if tref == -1:
                t = leoNodes.tnode()
            else:
                tref = self.canonicalTnodeIndex(tref)
                t = self.tnodesDict.get(tref)
                if not t:
                    t = self.newTnode(tref)
                    
            if self.checking: return None,False
            
            if back: # create v after back.
                v = back.insertAfter(t)
            elif parent: # create v as the parent's first child.
                v = parent.insertAsNthChild(0,t)
            else: # create a root vnode
                v = leoNodes.vnode(t)
                v.moveToRoot(oldRoot=None)
                c.setRootVnode(v) # New in Leo 4.4.2.
        
            if v not in v.t.vnodeList:
                v.t.vnodeList.append(v) # New in 4.2.
        
            skip = len(v.t.vnodeList) > 1
            v.initHeadString(headline,encoding=self.leo_file_encoding)
            #@    << handle unknown vnode attributes >>
            #@+node:ekr.20031218072017.1861:<< handle unknown vnode attributes >>
            keys = attrDict.keys()
            if keys:
                v.unknownAttributes = attrDict
                v._p_changed = 1
            
                if 0: # For debugging.
                    s = "unknown attributes for " + v.headString()
                    g.es_print(s,color="blue")
                    for key in keys:
                        s = "%s = %s" % (key,attrDict.get(key))
                        g.es_print(s)
            #@-node:ekr.20031218072017.1861:<< handle unknown vnode attributes >>
            #@nl
            # g.trace(skip,tref,v,v.t,len(v.t.vnodeList))
            return v,skip
        #@nonl
        #@-node:ekr.20031218072017.1860:createVnode
        #@+node:ekr.20040701065235.1:getDescendentAttributes
        def getDescendentAttributes (self,s,tag=""):
            
            '''s is a list of gnx's, separated by commas from a <v> or <t> element.
            Parses s into a list.
            
            This is used to record marked and expanded nodes.
            '''
            
            __pychecker__ = '--no-argsused' # tag used only for debugging.
        
            gnxs = s.split(',')
            result = [gnx for gnx in gnxs if len(gnx) > 0]
            # g.trace(tag,result)
            return result
        #@-node:ekr.20040701065235.1:getDescendentAttributes
        #@+node:EKR.20040627114602:getDescendentUnknownAttributes
        # Only @thin vnodes have the descendentTnodeUnknownAttributes field.
        # The question is: what are we to do about this?
        
        def getDescendentUnknownAttributes (self,s):
            
            try:
                bin = binascii.unhexlify(s) # Throws a TypeError if val is not a hex string.
                val = pickle.loads(bin)
                return val
        
            except (TypeError,pickle.UnpicklingError,ImportError):
                g.trace('oops: getDescendentUnknownAttributes')
                return None
        #@-node:EKR.20040627114602:getDescendentUnknownAttributes
        #@+node:ekr.20040326063413:getExistingVnode
        def getExistingVnode (self,tref,headline):
        
            assert(tref > -1)
            tref = self.canonicalTnodeIndex(tref)
            t = self.tnodesDict.get(tref)
            try:
                return t.vnodeList[0]
            except (IndexError,AttributeError):
                g.es("Missing vnode:",headline,color="red")
                g.es("Probably an outline topology error.")
                return None
        #@-node:ekr.20040326063413:getExistingVnode
        #@-node:ekr.20031218072017.1566:getVnode & helpers
        #@+node:ekr.20031218072017.1565:getVnodes
        def getVnodes (self,reassignIndices=True):
        
            c = self.c
        
            if self.getOpenTag("<vnodes>"):
                return # <vnodes/> seen.
                
            self.forbiddenTnodes = []
            back = parent = None # This routine _must_ work on vnodes!
            self.currentVnodeStack = []
            self.topVnodeStack = []
                
            if self.usingClipboard:
                oldRoot = c.rootPosition()
                oldCurrent = c.currentPosition()
                if not reassignIndices:
                    #@            << set self.forbiddenTnodes to tnodes than must not be pasted >>
                    #@+node:ekr.20041023105832:<< set self.forbiddenTnodes to tnodes than must not be pasted >>
                    self.forbiddenTnodes = []
                    
                    for p in oldCurrent.self_and_parents_iter():
                        if p.v.t not in self.forbiddenTnodes:
                            self.forbiddenTnodes.append(p.v.t)
                            
                    # g.trace("forbiddenTnodes",self.forbiddenTnodes)
                    #@-node:ekr.20041023105832:<< set self.forbiddenTnodes to tnodes than must not be pasted >>
                    #@nl
        
            while self.matchTag("<v"):
                append1 = not self.usingClipboard and len(self.currentVnodeStack) == 0
                append2 = not self.usingClipboard and len(self.topVnodeStack) == 0
                back = self.getVnode(parent,back,skip=False,
                    appendToCurrentStack=append1,appendToTopStack=append2)
        
            if self.usingClipboard and not self.checking:
                # Link in the pasted nodes after the current position.
                newRoot = c.rootPosition()
                c.setRootPosition(oldRoot)
                newRoot.v.linkAfter(oldCurrent.v)
                newCurrent = oldCurrent.copy()
                newCurrent.v = newRoot.v
                c.setCurrentPosition(newCurrent)
        
            self.getTag("</vnodes>")
        #@-node:ekr.20031218072017.1565:getVnodes
        #@+node:ekr.20031218072017.1249:getXmlStylesheetTag
        def getXmlStylesheetTag (self):
        
            """Parses the optional xml stylesheet string, and sets the corresponding config option.
            
            For example, given: <?xml_stylesheet s?> the config option is s."""
            
            c = self.c
            tag = "<?xml-stylesheet "
        
            if self.matchTag(tag):
                s = self.getStringToTag("?>")
                # print "reading:", tag + s + "?>"
                c.frame.stylesheet = s
                self.getTag("?>")
        #@-node:ekr.20031218072017.1249:getXmlStylesheetTag
        #@+node:ekr.20031218072017.1468:getXmlVersionTag
        # Parses the encoding string, and sets self.leo_file_encoding.
        
        def getXmlVersionTag (self):
        
            self.getTag(g.app.prolog_prefix_string)
            encoding = self.getDqString()
            self.getTag(g.app.prolog_postfix_string)
        
            if g.isValidEncoding(encoding):
                self.leo_file_encoding = encoding
                # g.trace('self.leo_file_encoding:',encoding, color="blue")
            else:
                g.es("invalid encoding in .leo file: " + encoding, color="red")
        #@-node:ekr.20031218072017.1468:getXmlVersionTag
        #@-others
    #@nonl
    #@-node:ekr.20031218072017.3021:Non-sax
    #@+node:ekr.20060919104530:Sax
    if use_sax:
        #@    @+others
        #@+node:ekr.20060919110638.2:dumpSaxTree
        def dumpSaxTree (self,root,dummy):
            
            if not root:
                print 'dumpSaxTree: empty tree'
                return
            if not dummy:
                root.dump()
            for child in root.children:
                self.dumpSaxTree(child,dummy=False)
        #@nonl
        #@-node:ekr.20060919110638.2:dumpSaxTree
        #@+node:ekr.20060919110638.3:readSaxFile
        def readSaxFile (self,fileName,silent=False):
        
            c = self.c
        
            # Pass one: create the intermediate nodes.
            self.dummyRoot = dummyRoot = self.parse_leo_file(fileName,silent=silent)
            # self.dumpSaxTree(dummyRoot,dummy=True)
        
            # Pass two: create the tree of vnodes and tnodes from the intermediate nodes.
            v = dummyRoot and self.createVnodes(dummyRoot)
            if 0:  #########  Much of this is presently in getLeoFile
                c2 = c.new()
                c2.setRootVnode(v)
                self.resolveTnodeLists(c2)
                self.restoreDescendentAttributes(c2)
                c2.checkOutline() 
                self.setCurrentPosition(c2)
        #@nonl
        #@-node:ekr.20060919110638.3:readSaxFile
        #@+node:ekr.20060919110638.4:createVnodes & helpers
        def createVnodes (self, dummyRoot):
            
            '''**Important**: this method and its helpers are low-level code
            corresponding to link/unlink methods in leoNodes.py.
            Modify this with extreme care.'''
            
            if 0: # inited by top-level methods...
                self.descendentExpandedList = []
                self.descendentMarksList = []
                self.descendentUnknownAttributesDictList = {}
                self.tnodesDict = {} # Keys are tnx's (strings).  Values are tnodes.
        
            children = self.createChildren(dummyRoot,parent_v = None)
            firstChild = children and children[0]
        
            return firstChild
        #@nonl
        #@+node:ekr.20060919110638.5:createChildren
        # node is a saxNodeClass object, parent_v is a vnode.
        
        def createChildren (self, node, parent_v):
            
            result = []
            
            for child in node.children:
                tnx = child.tnx
                t = self.txnToVnodeDict.get(tnx)
                if t:
                    # A clone.  Create a new clone node, but share the subtree, i.e., the tnode.
                    # g.trace('clone',child.headString,v.t,v.t.bodyString)
                    v = self.createVnode(child,parent_v,t=t)
                else:
                    v = self.createVnodeTree(child,parent_v)
                result.append(v)
                
            self.linkSiblings(result)
            if parent_v: self.linkParentAndChildren(parent_v,result)
            return result
        #@nonl
        #@-node:ekr.20060919110638.5:createChildren
        #@+node:ekr.20060919110638.6:createVnodeTree
        def createVnodeTree (self,node,parent_v):
        
            v = self.createVnode(node,parent_v)
            
            # To do: create the children only if v is not a clone.
            self.createChildren(node,v)
        
            return v
        #@nonl
        #@-node:ekr.20060919110638.6:createVnodeTree
        #@+node:ekr.20060919110638.7:createVnode
        def createVnode (self,node,parent_v,t=None):
            
            h = node.headString
            b = node.bodyString
        
            if not t:
                t = leoNodes.tnode(bodyString=b,headString=h)
            v = leoNodes.vnode(t)
            v.t.vnodeList.append(v)
            v._parent = parent_v
        
            index = self.canonicalTnodeIndex(node.tnx)
            self.tnodesDict [index] = t
            
            g.trace('tnx','%-22s' % (index),'v',id(v),'v.t',id(v.t),'body','%-4d' % (len(b)),h)
            
            self.handleVnodeAttributes(node,v)
            
            return v
        #@nonl
        #@+node:ekr.20060919110638.8:handleVnodeAttributes
        # The native attributes of <v> elements are a, t, vtag, tnodeList,
        # marks, expanded and descendentTnodeUnknownAttributes.
        
        def handleVnodeAttributes (self,node,v):
            
            d = node.attributes
            a = d.get('a')
            if a:
                # g.trace('a=%s %s' % (attrs,v.headString()))
                # 'C' (clone) and 'D' bits are not used.
                if 'M' in a: v.setMarked()
                if 'E' in a: v.expand()
                if 'O' in a: v.setOrphan()
                if 'T' in a: self.topVnode = v
                if 'V' in a: self.currentVnode = v
        
            s = d.get('tnodeList','')
            tnodeList = s and s.split(',')
            if tnodeList:
                # This tnode list will be resolved later.
                g.trace(v.headString(),len(tnodeList))
                v.tempTnodeList = tnodeList
                
            aDict = d.get('descendentTnodeUnknownAttributes')
            if aDict: self.descendentUnknownAttributesDictList.append(aDict)
            
            aList = d.get('expanded')
            if aList: self.descendentExpandedList.append(aList)
            
            aList = d.get('marks')
            if aList: self.descendentMarksList.append(aList)
                
            aDict = {}
            for key in d.keys():
                if key not in self.nativeVnodeAttributes:
                    aDict[key] = d.get(key)
            if aDict: v.unknownAttributes = aDict
        #@nonl
        #@-node:ekr.20060919110638.8:handleVnodeAttributes
        #@-node:ekr.20060919110638.7:createVnode
        #@+node:ekr.20060919110638.9:linkParentAndChildren
        def linkParentAndChildren (self, parent_v, children):
            
            # if children: g.trace(parent_v,len(children))
            
            firstChild_v = children and children[0] or None
        
            parent_v.t._firstChild = firstChild_v
            
            for child in children:
                child._parent = parent_v
            
            v = parent_v
            if v not in v.t.vnodeList:
                v.t.vnodeList.append(v)
        #@nonl
        #@-node:ekr.20060919110638.9:linkParentAndChildren
        #@+node:ekr.20060919110638.10:linkSiblings
        def linkSiblings (self, sibs):
            
            '''Set the v._back and v._next links for all vnodes v in sibs.'''
            
            n = len(sibs)
        
            for i in xrange(n):
                v = sibs[i]
                v._back = (i-1 >= 0 and sibs[i-1]) or None
                v._next = (i+1 <  n and sibs[i+1]) or None
        #@nonl
        #@-node:ekr.20060919110638.10:linkSiblings
        #@-node:ekr.20060919110638.4:createVnodes & helpers
        #@+node:ekr.20060919110638.14:parse_leo_file
        def parse_leo_file (self,theFile,inputFileName,silent):
            
            c = self.c
        
            try:
                node = None
                parser = xml.sax.make_parser()
                # Do not include external general entities.
                # The actual feature name is "http://xml.org/sax/features/external-general-entities"
                parser.setFeature(xml.sax.handler.feature_external_ges,0)
                # Hopefully the content handler can figure out the encoding from the <?xml> element.
                handler = saxContentHandler(c,inputFileName,silent)
                parser.setContentHandler(handler)
                parser.parse(theFile)
                node = handler.getNode()
            except xml.sax.SAXParseException:
                g.es_print('Error parsing %s' % (inputFileName),color='red')
                g.es_exception()
            except Exception:
                g.es_print('Unexpected exception parsing %s' % (inputFileName),color='red')
                g.es_exception()
                
            return node
        #@nonl
        #@-node:ekr.20060919110638.14:parse_leo_file
        #@+node:ekr.20060919110638.19:class saxContentHandler (XMLGenerator)
        class saxContentHandler (xml.sax.saxutils.XMLGenerator):
            
            '''A sax content handler class that reads Leo files.'''
        
            #@    @+others
            #@+node:ekr.20060919110638.20: __init__ & helpers
            def __init__ (self,c,fileName,silent):
            
                self.c = c
                self.fileName = fileName
                self.silent = silent
            
                # Init the base class.
                xml.sax.saxutils.XMLGenerator.__init__(self)
                
                #@    << define dispatch dict >>
                #@+node:ekr.20060919110638.21:<< define dispatch dict >>
                # There is no need for an 'end' method if all info is carried in attributes.
                
                self.dispatchDict = {
                    'find_panel_settings':         (None,None),
                    'globals':                     (self.startGlobals,None),
                    'global_log_window_position':  (None,None), # The position of the log window is no longer used.
                    'global_window_position':      (self.startWinPos,None),
                    'leo_file':                    (None,None),
                    'leo_header':                  (self.startLeoHeader,None),
                    'preferences':                 (None,None),
                    't':                           (self.startTnode,self.endTnode),
                    'tnodes':                      (None,None),
                    'v':                           (self.startVnode,self.endVnode),
                    'vh':                          (self.startVH,self.endVH),
                    'vnodes':                      (self.startVnodes,None), # Causes window to appear.
                }
                #@nonl
                #@-node:ekr.20060919110638.21:<< define dispatch dict >>
                #@nl
                
                # Global attributes of the .leo file...
                self.body_outline_ratio = None
                self.global_window_position = {}
                self.encoding = 'utf-8' 
            
                # Semantics...
                self.content = None
                self.currentNode = None
                self.elementStack = []
                self.errors = 0
                self.txnToNodesDict = {} # Keys are tnx's (strings), values are *lists* of saxNodeClass objects.
                self.level = 0
                self.node = None
                self.nodeList = [] # List of saxNodeClass objects with the present tnode.
                self.nodeStack = []
                self.rootNode = None
                self.topNode = None
            #@nonl
            #@-node:ekr.20060919110638.20: __init__ & helpers
            #@+node:ekr.20060919110638.29: Do nothing
            def endElementNS(self,name,qname):
                g.trace(name)
                
            def endDocument(self):
                pass
            
            def ignorableWhitespace(self):
                pass
            
            def processingInstruction (self,target,data):
                pass # For <?xml-stylesheet ekr_stylesheet?>
            
            def skippedEntity(self,name):
                g.trace(name)
            
            def startElementNS(self,name,qname,attrs):
                g.trace(name)
                
            def startDocument(self):
                pass
            #@nonl
            #@-node:ekr.20060919110638.29: Do nothing
            #@+node:ekr.20060919134313: Utils
            #@+node:ekr.20060919110638.23:attrsToList
            def attrsToList (self,attrs):
                
                '''Convert the attributes to a list of g.Bunches.
                
                attrs: an Attributes item passed to startElement.'''
                
                if 1:
                    for name in attrs.getNames():
                        val = attrs.getValue(name)
                        if type(val) != type(u''):
                            g.trace('Non-unicode attribute',name,val)
            
                # g.trace(g.listToString([repr() for name in attrs.getNames()]))
                
                return [
                    g.Bunch(name=name,val=attrs.getValue(name))
                        for name in attrs.getNames()]
            #@nonl
            #@-node:ekr.20060919110638.23:attrsToList
            #@+node:ekr.20060919110638.26:error
            def error (self, message):
                
                print
                print
                print 'XML error: %s' % (message)
                print
                
                self.errors += 1
            #@nonl
            #@-node:ekr.20060919110638.26:error
            #@+node:ekr.20060919110638.27:inElement
            def inElement (self,name):
                
                return self.elementStack and name in self.elementStack
            #@nonl
            #@-node:ekr.20060919110638.27:inElement
            #@+node:ekr.20060919110638.28:printStartElement
            def printStartElement(self,name,attrs):
                
                indent = '\t' * self.level or ''
            
                if attrs.getLength() > 0:
                    print '%s<%s %s>' % (
                        indent,
                        self.clean(name).strip(),
                        self.attrsToString(attrs,sep=' ')),
                else:
                    print '%s<%s>' % (
                        indent,
                        self.clean(name).strip()),
            
                if name.lower() in ['v','t','vnodes','tnodes',]:
                    print
            #@nonl
            #@+node:ekr.20060919110638.24:attrsToString
            def attrsToString (self,attrs,sep='\n'):
                
                '''Convert the attributes to a string.
                
                attrs: an Attributes item passed to startElement.
                
                sep: the separator charater between attributes.'''
            
                result = [
                    '%s="%s"' % (bunch.name,bunch.val)
                    for bunch in self.attrsToList(attrs)
                ]
            
                return sep.join(result)
            #@nonl
            #@-node:ekr.20060919110638.24:attrsToString
            #@+node:ekr.20060919110638.25:clean
            def clean(self,s):
            
                return g.toEncodedString(s,"ascii")
            #@nonl
            #@-node:ekr.20060919110638.25:clean
            #@-node:ekr.20060919110638.28:printStartElement
            #@-node:ekr.20060919134313: Utils
            #@+node:ekr.20060919110638.30:characters
            def characters(self,content):
                
                if content and type(content) != type(u''):
                    g.trace('Non-unicode content',repr(content))
            
                content = content.replace('\r','')
                if not content: return
            
                elementName = self.elementStack and self.elementStack[-1].lower() or '<no element name>'
                
                if elementName in ('t','vh'):
                    # if elementName == 'vh': g.trace(elementName,repr(content))
                    self.content.append(content)
            
                elif content.strip():
                    print 'unexpected content:',elementName,repr(content)
            #@nonl
            #@-node:ekr.20060919110638.30:characters
            #@+node:ekr.20060919110638.31:endElement & helpers
            def endElement(self,name):
                
                name = name.lower()
                if name in printElements or 'all' in printElements:
                    indent = '\t' * (self.level-1) or ''
                    print '%s</%s>' % (indent,self.clean(name).strip())
                
                data = self.dispatchDict.get(name)
            
                if data is None:
                    g.trace('unknown element',name)
                else:
                    junk,func = data
                    if func:
                        func()
            
                name2 = self.elementStack.pop()
                assert name == name2
            #@nonl
            #@+node:ekr.20060919110638.32:endTnode
            def endTnode (self):
                
                for node in self.nodeList:
                    node.bodyString = ''.join(self.content)
            
                self.content = []
            #@nonl
            #@-node:ekr.20060919110638.32:endTnode
            #@+node:ekr.20060919110638.33:endVnode
            def endVnode (self):
                
                self.level -= 1
                self.node = self.nodeStack.pop()
            #@nonl
            #@-node:ekr.20060919110638.33:endVnode
            #@+node:ekr.20060919110638.34:endVH
            def endVH (self):
                  
                if self.node:
                    self.node.headString = ''.join(self.content)
            
                self.content = []
            #@nonl
            #@-node:ekr.20060919110638.34:endVH
            #@-node:ekr.20060919110638.31:endElement & helpers
            #@+node:ekr.20060919110638.45:getters
            def getCurrentNode (self):
                return self.currentNode
                
            def getRootNode (self):
                return self.rootNode
                
            def getTopNode (self):
                return self.topNode
            #@nonl
            #@-node:ekr.20060919110638.45:getters
            #@+node:ekr.20060919110638.35:startElement & helpers
            def startElement(self,name,attrs):
                
                name = name.lower()
                if name in printElements or 'all' in printElements:
                    self.printStartElement(name,attrs)
            
                self.elementStack.append(name)
                
                data = self.dispatchDict.get(name)
            
                if data is None:
                    g.trace('unknown element',name)
                else:
                    func,junk = data
                    if func:
                        func(attrs)
            #@nonl
            #@+node:ekr.20060919110638.36:getPositionAttributes
            def getPositionAttributes (self,attrs):
                
                d = {}
                
                for bunch in self.attrsToList(attrs):
                    name = bunch.name ; val = bunch.val
                    if name in ('top','left','width','height'):
                        try:
                            d[name] = int(val)
                        except ValueError:
                            d[name] = 100 # A reasonable emergency default.
                    else:
                        g.trace(name,len(val))
                        
                return d
            #@nonl
            #@-node:ekr.20060919110638.36:getPositionAttributes
            #@+node:ekr.20060919110638.37:startGlobals
            def startGlobals (self,attrs):
                
                for bunch in self.attrsToList(attrs):
                    name = bunch.name ; val = bunch.val
                    
                    if name == 'body_outline_ratio':
                        self.body_outline_ratio = val
                        # g.trace(name,val)
                    else:
                        g.trace(name,len(val))
            #@nonl
            #@-node:ekr.20060919110638.37:startGlobals
            #@+node:ekr.20060919110638.38:startWinPos
            def startWinPos (self,attrs):
                
                self.global_window_position = self.getPositionAttributes(attrs)
                # g.trace(self.global_window_position)
            #@nonl
            #@-node:ekr.20060919110638.38:startWinPos
            #@+node:ekr.20060919110638.39:startLeoHeader
            def startLeoHeader (self,attrs):
                
                self.txnToNodesDict = {}
            #@nonl
            #@-node:ekr.20060919110638.39:startLeoHeader
            #@+node:ekr.20060919112118:startVnodes
            def startVnodes (self,attrs):
                
                c = self.c
            
                # Causes window to appear.
                c.frame.resizePanesToRatio(c.frame.ratio,c.frame.secondary_ratio)
                if not self.silent:
                    g.es("reading: " + self.fileName)
            #@nonl
            #@-node:ekr.20060919112118:startVnodes
            #@+node:ekr.20060919110638.40:startVH
            def startVH (self,attrs):
            
                self.content = []
            #@nonl
            #@-node:ekr.20060919110638.40:startVH
            #@+node:ekr.20060919110638.41:startTnode
            def startTnode (self,attrs):
                
                if not self.inElement('tnodes'):
                    self.error('<t> outside <tnodes>')
                    
                self.content = []
                
                self.tnodeAttributes(attrs)
            #@nonl
            #@+node:ekr.20060919110638.42:tnodeAttributes
            def tnodeAttributes (self,attrs):
                
                # The tnode must have a tx attribute to associate content with the proper node.
                    
                self.nodeList = []
            
                for bunch in self.attrsToList(attrs):
                    name = bunch.name ; val = bunch.val
                    if name == 'tx':
                        self.nodeList = self.txnToNodesDict.get(val,[])
                        if not self.nodeList:
                            self.error('Bad leo file: no node for <t tx=%s>' % (val))
                    else:
                        # Do **not** set any saxNodeClass attributes here!
                        self.error('Unexpected tnode attribute %s = %s' % (name,val))
                        
                if not self.nodeList:
                    self.error('Bad leo file: no tx attribute for tnode')
            #@nonl
            #@-node:ekr.20060919110638.42:tnodeAttributes
            #@-node:ekr.20060919110638.41:startTnode
            #@+node:ekr.20060919110638.43:startVnode
            def startVnode (self,attrs):
                
                if not self.inElement('vnodes'):
                    self.error('<v> outside <vnodes>')
            
                if self.rootNode:
                    parent = self.node
                else:
                    self.rootNode = parent = saxNodeClass() # The dummy parent node.
                    parent.headString = 'dummyNode'
            
                self.node = saxNodeClass()
            
                parent.children.append(self.node)
                self.vnodeAttributes(attrs)
                self.nodeStack.append(parent)
                    
                return parent
            #@nonl
            #@+node:ekr.20060919110638.44:vnodeAttributes
            # The native attributes of <v> elements are a, t, vtag, tnodeList,
            # marks, expanded and descendentTnodeUnknownAttributes.
            
            def vnodeAttributes (self,attrs):
                
                node = self.node
            
                for bunch in self.attrsToList(attrs):
                    name = bunch.name ; val = bunch.val
                    if name == 't':
                        aList = self.txnToNodesDict.get(val,[])
                        aList.append(self.node)
                        self.txnToNodesDict[val] = aList
                        node.tnx = val
                    else:
                        node.attributes[name] = val
                        # g.trace(name,len(val))
            #@nonl
            #@-node:ekr.20060919110638.44:vnodeAttributes
            #@-node:ekr.20060919110638.43:startVnode
            #@-node:ekr.20060919110638.35:startElement & helpers
            #@-others
        #@nonl
        #@-node:ekr.20060919110638.19:class saxContentHandler (XMLGenerator)
        #@+node:ekr.20060919110638.15:class saxNodeClass
        class saxNodeClass:
            
            '''A class representing one <v> element.
            
            Use getters to access the attributes, properties and rules of this mode.'''
            
            #@    @+others
            #@+node:ekr.20060919110638.16: node.__init__
            def __init__ (self):
            
                self.attributes = {}
                self.bodyString = ''
                self.headString = ''
                self.children = []
                self.tnodeList = []
                self.tnx = None
            #@nonl
            #@-node:ekr.20060919110638.16: node.__init__
            #@+node:ekr.20060919110638.17: node.__str__ & __repr__
            def __str__ (self):
            
                return '<v: %s>' % self.headString
            
            __repr__ = __str__
            #@nonl
            #@-node:ekr.20060919110638.17: node.__str__ & __repr__
            #@+node:ekr.20060919110638.18:node.dump
            def dump (self):
                 
                print
                print 'node: tnx: %s body: %d %s' % (self.tnx,len(self.bodyString),self.headString)
                print 'children:',g.listToString([child for child in self.children])
                print 'attrs:',self.attributes.values()
            #@nonl
            #@-node:ekr.20060919110638.18:node.dump
            #@-others
        #@nonl
        #@-node:ekr.20060919110638.15:class saxNodeClass
        #@-others
    #@nonl
    #@-node:ekr.20060919104530:Sax
    #@-node:ekr.20031218072017.3020:Reading
    #@+node:ekr.20031218072017.3032:Writing
    #@+node:ekr.20031218072017.1570:assignFileIndices & compactFileIndices
    def assignFileIndices (self):
        
        """Assign a file index to all tnodes"""
        
        c = self.c ; nodeIndices = g.app.nodeIndices
    
        nodeIndices.setTimestamp() # This call is fairly expensive.
    
        # Assign missing gnx's, converting ints to gnx's.
        # Always assign an (immutable) index, even if the tnode is empty.
        for p in c.allNodes_iter():
            try: # Will fail for None or any pre 4.1 file index.
                theId,time,n = p.v.t.fileIndex
            except TypeError:
                # Don't convert to string until the actual write.
                p.v.t.fileIndex = nodeIndices.getNewIndex()
    
        if 0: # debugging:
            for p in c.allNodes_iter():
                g.trace(p.v.t.fileIndex)
    
    # Indices are now immutable, so there is no longer any difference between these two routines.
    compactFileIndices = assignFileIndices
    #@-node:ekr.20031218072017.1570:assignFileIndices & compactFileIndices
    #@+node:ekr.20050404190914.2:deleteFileWithMessage
    def deleteFileWithMessage(self,fileName,kind):
        
        __pychecker__ = '--no-argsused' # kind unused: retained for debugging.
    
        try:
            os.remove(fileName)
    
        except Exception:
            if self.read_only:
                g.es("read only",color="red")
            g.es("exception deleting backup file:" + fileName)
            g.es_exception(full=False)
            return False
    #@+node:ekr.20050404212949:test_fc_deleteFileWithMessage
    def test_fc_deleteFileWithMessage(self):
    
        fc=c.fileCommands # Self is a dummy argument.
        fc.deleteFileWithMessage('xyzzy','test')
        
    if 0: # one-time test of es statements.
        fileName = 'fileName' ; kind = 'kind'
        g.es("read only",color="red")
        g.es("exception deleting %s file: %s" % (fileName,kind))
        g.es("exception deleting backup file:" + fileName)
    #@-node:ekr.20050404212949:test_fc_deleteFileWithMessage
    #@-node:ekr.20050404190914.2:deleteFileWithMessage
    #@+node:ekr.20031218072017.1470:put
    def put (self,s):
        '''
        Put string s to self.outputFile.
        All output eventually comes here.
        '''
        # Improved code: self.outputFile (a cStringIO object) always exists.
        if s:
            s = g.toEncodedString(s,self.leo_file_encoding,reportErrors=True)
            self.outputFile.write(s)
    
    def put_dquote (self):
        self.put('"')
            
    def put_dquoted_bool (self,b):
        if b: self.put('"1"')
        else: self.put('"0"')
            
    def put_flag (self,a,b):
        if a:
            self.put(" ") ; self.put(b) ; self.put('="1"')
            
    def put_in_dquotes (self,a):
        self.put('"')
        if a: self.put(a) # will always be True if we use backquotes.
        else: self.put('0')
        self.put('"')
    
    def put_nl (self):
        self.put("\n")
        
    def put_tab (self):
        self.put("\t")
        
    def put_tabs (self,n):
        while n > 0:
            self.put("\t")
            n -= 1
    #@nonl
    #@-node:ekr.20031218072017.1470:put
    #@+node:ekr.20031218072017.3034:putEscapedString
    # Surprisingly, the call to xmlEscape here is _much_ faster than calling put for each characters of s.
    
    def putEscapedString (self,s):
    
        if s and len(s) > 0:
            self.put(self.xmlEscape(s))
    #@-node:ekr.20031218072017.3034:putEscapedString
    #@+node:ekr.20040324080819.1:putLeoFile & helpers
    def putLeoFile (self):
    
        self.putProlog()
        self.putHeader()
        self.putGlobals()
        self.putPrefs()
        self.putFindSettings()
        #start = g.getTime()
        self.putVnodes()
        #start = g.printDiffTime("vnodes ",start)
        self.putTnodes()
        #start = g.printDiffTime("tnodes ",start)
        self.putPostlog()
    #@nonl
    #@+node:ekr.20031218072017.3035:putFindSettings
    def putFindSettings (self):
        
        # New in 4.3:  These settings never get written to the .leo file.
        self.put("<find_panel_settings/>")
        self.put_nl()
    #@-node:ekr.20031218072017.3035:putFindSettings
    #@+node:ekr.20031218072017.3037:putGlobals
    # Changed for Leo 4.0.
    
    def putGlobals (self):
    
        c = self.c
        self.put("<globals")
        #@    << put the body/outline ratio >>
        #@+node:ekr.20031218072017.3038:<< put the body/outline ratio >>
        # Puts an innumerate number of digits
        
        self.put(" body_outline_ratio=")
        self.put_in_dquotes(str(c.frame.ratio))
        #@-node:ekr.20031218072017.3038:<< put the body/outline ratio >>
        #@nl
        self.put(">") ; self.put_nl()
        #@    << put the position of this frame >>
        #@+node:ekr.20031218072017.3039:<< put the position of this frame >>
        width,height,left,top = c.frame.get_window_info()
        
        self.put_tab()
        self.put("<global_window_position")
        self.put(" top=") ; self.put_in_dquotes(str(top))
        self.put(" left=") ; self.put_in_dquotes(str(left))
        self.put(" height=") ; self.put_in_dquotes(str(height))
        self.put(" width=") ; self.put_in_dquotes(str(width))
        self.put("/>") ; self.put_nl()
        #@-node:ekr.20031218072017.3039:<< put the position of this frame >>
        #@nl
        #@    << put the position of the log window >>
        #@+node:ekr.20031218072017.3040:<< put the position of the log window >>
        top = left = height = width = 0 # no longer used
        self.put_tab()
        self.put("<global_log_window_position")
        self.put(" top=") ; self.put_in_dquotes(str(top))
        self.put(" left=") ; self.put_in_dquotes(str(left))
        self.put(" height=") ; self.put_in_dquotes(str(height))
        self.put(" width=") ; self.put_in_dquotes(str(width))
        self.put("/>") ; self.put_nl()
        #@-node:ekr.20031218072017.3040:<< put the position of the log window >>
        #@nl
        self.put("</globals>") ; self.put_nl()
    #@-node:ekr.20031218072017.3037:putGlobals
    #@+node:ekr.20031218072017.3041:putHeader
    def putHeader (self):
    
        tnodes = 0 ; clone_windows = 0 # Always zero in Leo2.
    
        self.put("<leo_header")
        self.put(" file_format=") ; self.put_in_dquotes("2")
        self.put(" tnodes=") ; self.put_in_dquotes(str(tnodes))
        self.put(" max_tnode_index=") ; self.put_in_dquotes(str(self.maxTnodeIndex))
        self.put(" clone_windows=") ; self.put_in_dquotes(str(clone_windows))
        self.put("/>") ; self.put_nl()
    #@-node:ekr.20031218072017.3041:putHeader
    #@+node:ekr.20031218072017.3042:putPostlog
    def putPostlog (self):
    
        self.put("</leo_file>") ; self.put_nl()
    #@-node:ekr.20031218072017.3042:putPostlog
    #@+node:ekr.20031218072017.2066:putPrefs
    def putPrefs (self):
        
        # New in 4.3:  These settings never get written to the .leo file.
        self.put("<preferences/>")
        self.put_nl()
    #@-node:ekr.20031218072017.2066:putPrefs
    #@+node:ekr.20031218072017.1246:putProlog & helpers
    def putProlog (self):
    
        c = self.c
        
        self.putXMLLine()
        
        if c.config.stylesheet or c.frame.stylesheet:
            self.putStyleSheetLine()
    
        self.put("<leo_file>") ; self.put_nl()
    #@+node:ekr.20031218072017.1247:putXMLLine
    def putXMLLine (self):
        
        '''Put the **properly encoded** <?xml> element.'''
    
        # Use self.leo_file_encoding encoding.
        self.put(g.app.prolog_prefix_string)
        
        self.put_dquote()
        self.put(self.leo_file_encoding)
        self.put_dquote()
    
        self.put(g.app.prolog_postfix_string)
        self.put_nl()    
    #@nonl
    #@-node:ekr.20031218072017.1247:putXMLLine
    #@+node:ekr.20031218072017.1248:putStyleSheetLine
    def putStyleSheetLine (self):
        
        c = self.c
        
        # The stylesheet in the .leo file takes precedence over the default stylesheet.
        self.put("<?xml-stylesheet ")
        self.put(c.frame.stylesheet or c.config.stylesheet)
        self.put("?>")
        self.put_nl()
    #@nonl
    #@-node:ekr.20031218072017.1248:putStyleSheetLine
    #@-node:ekr.20031218072017.1246:putProlog & helpers
    #@+node:ekr.20031218072017.1577:putTnode
    def putTnode (self,t):
    
        self.put("<t")
        self.put(" tx=")
    
        gnx = g.app.nodeIndices.toString(t.fileIndex)
        self.put_in_dquotes(gnx)
    
        if hasattr(t,"unknownAttributes"):
            self.putUnknownAttributes(t)
    
        self.put(">")
    
        # g.trace(t)
        if t.bodyString:
            self.putEscapedString(t.bodyString)
    
        self.put("</t>") ; self.put_nl()
    #@-node:ekr.20031218072017.1577:putTnode
    #@+node:ekr.20031218072017.1575:putTnodes 
    def putTnodes (self):
        
        """Puts all tnodes as required for copy or save commands"""
    
        c = self.c
    
        self.put("<tnodes>") ; self.put_nl()
        #@    << write only those tnodes that were referenced >>
        #@+node:ekr.20031218072017.1576:<< write only those tnodes that were referenced >>
        if self.usingClipboard: # write the current tree.
            theIter = c.currentPosition().self_and_subtree_iter()
        else: # write everything
            theIter = c.allNodes_iter()
        
        # Populate tnodes
        tnodes = {}
        
        for p in theIter:
            index = p.v.t.fileIndex
            assert(index)
            tnodes[index] = p.v.t
        
        # Put all tnodes in index order.
        keys = tnodes.keys() ; keys.sort()
        for index in keys:
            # g.trace(index)
            t = tnodes.get(index)
            assert(t)
            # Write only those tnodes whose vnodes were written.
            if t.isWriteBit(): # 5/3/04
                self.putTnode(t)
        #@nonl
        #@-node:ekr.20031218072017.1576:<< write only those tnodes that were referenced >>
        #@nl
        self.put("</tnodes>") ; self.put_nl()
    #@-node:ekr.20031218072017.1575:putTnodes 
    #@+node:EKR.20040526202501:putUnknownAttributes & helper
    def putUnknownAttributes (self,torv):
        
        """Put pickleable values for all keys in torv.unknownAttributes dictionary."""
        
        attrDict = torv.unknownAttributes
        if type(attrDict) != type({}):
            g.es("ignoring non-dictionary unknownAttributes for",torv,color="blue")
            return
    
        for key in attrDict.keys():
            val = attrDict[key]
            self.putUaHelper(torv,key,val)
    #@nonl
    #@+node:ekr.20050418161620.2:putUaHelper
    def putUaHelper (self,torv,key,val):
        
        '''Put attribute whose name is key and value is val to the output stream.'''
        
        # New in 4.3: leave string attributes starting with 'str_' alone.
        if key.startswith('str_'):
            if type(val) == type(''):
                attr = ' %s="%s"' % (key,self.xmlEscape(val))
                self.put(attr)
            else:
                g.es("ignoring non-string attribute %s in %s" % (
                    key,torv),color="blue")
            return
        try:
            try:
                # Protocol argument is new in Python 2.3
                # Use protocol 1 for compatibility with bin.
                s = pickle.dumps(val,protocol=1)
            except TypeError:
                s = pickle.dumps(val,bin=True)
            attr = ' %s="%s"' % (key,binascii.hexlify(s))
            self.put(attr)
    
        except pickle.PicklingError:
            # New in 4.2 beta 1: keep going after error.
            g.es("ignoring non-pickleable attribute %s in %s" % (
                key,torv),color="blue")
    #@-node:ekr.20050418161620.2:putUaHelper
    #@-node:EKR.20040526202501:putUnknownAttributes & helper
    #@+node:ekr.20031218072017.1579:putVnodes & helpers
    def putVnodes (self):
    
        """Puts all <v> elements in the order in which they appear in the outline."""
    
        c = self.c
        c.clearAllVisited()
    
        self.put("<vnodes>") ; self.put_nl()
    
        # Make only one copy for all calls.
        self.currentPosition = c.currentPosition() 
        self.topPosition     = c.topPosition()
    
        if self.usingClipboard:
            self.putVnode(self.currentPosition) # Write only current tree.
        else:
            for p in c.rootPosition().self_and_siblings_iter():
                self.putVnode(p) # Write the next top-level node.
    
        self.put("</vnodes>") ; self.put_nl()
    #@+node:ekr.20031218072017.1863:putVnode (3.x and 4.x)
    def putVnode (self,p):
    
        """Write a <v> element corresponding to a vnode."""
    
        fc = self ; c = fc.c ; v = p.v
        isThin = p.isAtThinFileNode()
        # Must check all parents.
        isIgnore = False
        for p2 in p.self_and_parents_iter():
            if p2.isAtIgnoreNode():
                isIgnore = True ; break
        isOrphan = p.isOrphan()
        forceWrite = isIgnore or not isThin or (isThin and isOrphan)
    
        fc.put("<v")
        #@    << Put tnode index >>
        #@+node:ekr.20031218072017.1864:<< Put tnode index >>
        if v.t.fileIndex:
            gnx = g.app.nodeIndices.toString(v.t.fileIndex)
            fc.put(" t=") ; fc.put_in_dquotes(gnx)
        
            # g.trace(v.t)
            if forceWrite or self.usingClipboard:
                v.t.setWriteBit() # 4.2: Indicate we wrote the body text.
        else:
            g.trace(v.t.fileIndex,v)
            g.es("error writing file(bad v.t.fileIndex)!")
            g.es("try using the Save To command")
        #@-node:ekr.20031218072017.1864:<< Put tnode index >>
        #@nl
        #@    << Put attribute bits >>
        #@+node:ekr.20031218072017.1865:<< Put attribute bits >>
        attr = ""
        if p.v.isExpanded(): attr += "E"
        if p.v.isMarked():   attr += "M"
        if p.v.isOrphan():   attr += "O"
        
        if 1: # No longer a bottleneck now that we use p.equal rather than p.__cmp__
            # Almost 30% of the entire writing time came from here!!!
            if p.equal(self.topPosition):   attr += "T" # was a bottleneck
            if c.isCurrentPosition(p):      attr += "V" # was a bottleneck
        
        if attr: fc.put(' a="%s"' % attr)
        #@-node:ekr.20031218072017.1865:<< Put attribute bits >>
        #@nl
        #@    << Put tnodeList and unKnownAttributes >>
        #@+node:ekr.20040324082713:<< Put tnodeList and unKnownAttributes >>
        # Write the tnodeList only for @file nodes.
        # New in 4.2: tnode list is in tnode.
        
        if 0: # Debugging.
            if v.isAnyAtFileNode():
                if hasattr(v.t,"tnodeList"):
                    g.trace(v.headString(),len(v.t.tnodeList))
                else:
                    g.trace(v.headString(),"no tnodeList")
        
        if hasattr(v.t,"tnodeList") and len(v.t.tnodeList) > 0 and v.isAnyAtFileNode():
            if isThin:
                if g.app.unitTesting:
                    g.app.unitTestDict["warning"] = True
                g.es("deleting tnode list for %s" % p.headString(),color="blue")
                # This is safe: cloning can't change the type of this node!
                delattr(v.t,"tnodeList")
            else:
                fc.putTnodeList(v) # New in 4.0
        
        if hasattr(v,"unknownAttributes"): # New in 4.0
            self.putUnknownAttributes(v)
            
        if p.hasChildren() and not forceWrite and not self.usingClipboard:
            # We put the entire tree when using the clipboard, so no need for this.
            self.putDescendentUnknownAttributes(p)
            self.putDescendentAttributes(p)
        #@-node:ekr.20040324082713:<< Put tnodeList and unKnownAttributes >>
        #@nl
        fc.put(">")
        #@    << Write the head text >>
        #@+node:ekr.20031218072017.1866:<< Write the head text >>
        headString = p.v.headString()
        
        if headString:
            fc.put("<vh>")
            fc.putEscapedString(headString)
            fc.put("</vh>")
        #@-node:ekr.20031218072017.1866:<< Write the head text >>
        #@nl
        
        if not self.usingClipboard:
            #@        << issue informational messages >>
            #@+node:ekr.20040702085529:<< issue informational messages >>
            if p.isAtThinFileNode and p.isOrphan():
                g.es("Writing erroneous: %s" % p.headString(),color="blue")
                p.clearOrphan()
            
            if 0: # For testing.
                if p.isAtIgnoreNode():
                     for p2 in p.self_and_subtree_iter():
                            if p2.isAtThinFileNode():
                                g.es("Writing @ignore'd: %s" % p2.headString(),color="blue")
            #@-node:ekr.20040702085529:<< issue informational messages >>
            #@nl
    
       # New in 4.2: don't write child nodes of @file-thin trees (except when writing to clipboard)
        if p.hasChildren():
            if forceWrite or self.usingClipboard:
                fc.put_nl()
                # This optimization eliminates all "recursive" copies.
                p.moveToFirstChild()
                while 1:
                    fc.putVnode(p)
                    if p.hasNext(): p.moveToNext()
                    else:           break
                p.moveToParent()
    
        fc.put("</v>") ; fc.put_nl()
    #@-node:ekr.20031218072017.1863:putVnode (3.x and 4.x)
    #@+node:ekr.20031218072017.2002:putTnodeList (4.0,4.2)
    def putTnodeList (self,v):
        
        """Put the tnodeList attribute of a tnode."""
        
        # g.trace(v)
        
        # Remember: entries in the tnodeList correspond to @+node sentinels, _not_ to tnodes!
    
        fc = self ; nodeIndices = g.app.nodeIndices
        tnodeList = v.t.tnodeList
        if tnodeList:
            # g.trace("%4d" % len(tnodeList),v)
            fc.put(" tnodeList=") ; fc.put_dquote()
            for t in tnodeList:
                try: # Will fail for None or any pre 4.1 file index.
                    theId,time,n = t.fileIndex
                except:
                    g.trace("assigning gnx for ",v,t)
                    gnx = nodeIndices.getNewIndex()
                    v.t.setFileIndex(gnx) # Don't convert to string until the actual write.
            s = ','.join([nodeIndices.toString(t.fileIndex) for t in tnodeList])
            fc.put(s) ; fc.put_dquote()
    #@nonl
    #@-node:ekr.20031218072017.2002:putTnodeList (4.0,4.2)
    #@+node:ekr.20040701065235.2:putDescendentAttributes
    def putDescendentAttributes (self,p):
        
        nodeIndices = g.app.nodeIndices
    
        # Create a list of all tnodes whose vnodes are marked or expanded
        marks = [] ; expanded = []
        for p in p.subtree_iter():
            if p.isMarked() and not p in marks:
                marks.append(p.copy())
            if p.hasChildren() and p.isExpanded() and not p in expanded:
                expanded.append(p.copy())
    
        for theList,tag in ((marks,"marks="),(expanded,"expanded=")):
            if theList:
                sList = []
                for p in theList:
                    gnx = p.v.t.fileIndex
                    sList.append("%s," % nodeIndices.toString(gnx))
                s = string.join(sList,'')
                # g.trace(tag,[str(p.headString()) for p in theList])
                self.put('\n' + tag)
                self.put_in_dquotes(s)
    #@-node:ekr.20040701065235.2:putDescendentAttributes
    #@+node:EKR.20040627113418:putDescendentUnknownAttributes
    def putDescendentUnknownAttributes (self,p):
    
        # Create a list of all tnodes having a valid unknownAttributes dict.
        tnodes = []
        for p2 in p.subtree_iter():
            t = p2.v.t
            if hasattr(t,"unknownAttributes"):
                if t not in tnodes :
                    tnodes.append((p,t),)
        
        # Create a list of pairs (t,d) where d contains only pickleable entries.
        data = []
        for p,t in tnodes:
            if type(t.unknownAttributes) != type({}):
                 g.es("ignoring non-dictionary unknownAttributes for",p,color="blue")
            else:
                # Create a new dict containing only entries that can be pickled.
                d = dict(t.unknownAttributes) # Copy the dict.
                for key in d.keys():
                    try: pickle.dumps(d[key],bin=True)
                    except pickle.PicklingError:
                        del d[key]
                        g.es("ignoring bad unknownAttributes key %s in %s" % (
                            key,p),color="blue")
                data.append((t,d),)
                
        # Create resultDict, an enclosing dict to hold all the data.
        resultDict = {}
        nodeIndices = g.app.nodeIndices
        for t,d in data:
            gnx = nodeIndices.toString(t.fileIndex)
            resultDict[gnx]=d
        
        if 0:
            print "resultDict"
            for key in resultDict:
                print ; print key,resultDict[key]
            
        # Pickle and hexlify resultDict.
        if resultDict:
            try:
                tag = "descendentTnodeUnknownAttributes"
                s = pickle.dumps(resultDict,bin=True)
                field = ' %s="%s"' % (tag,binascii.hexlify(s))
                self.put(field)
            except pickle.PicklingError:
                g.trace("can't happen",color="red")
    #@-node:EKR.20040627113418:putDescendentUnknownAttributes
    #@-node:ekr.20031218072017.1579:putVnodes & helpers
    #@-node:ekr.20040324080819.1:putLeoFile & helpers
    #@+node:ekr.20031218072017.1573:putLeoOutline (to clipboard) & helper
    # Writes a Leo outline to s in a format suitable for pasting to the clipboard.
    
    def putLeoOutline (self):
    
        self.outputFile = g.fileLikeObject()
        self.usingClipboard = True
        self.assignFileIndices() # 6/11/03: Must do this for 3.x code.
        self.putProlog()
        self.putClipboardHeader()
        self.putVnodes()
        self.putTnodes()
        self.putPostlog()
        s = self.outputFile.getvalue()
        self.outputFile = None
        self.usingClipboard = False
        return s
    #@+node:ekr.20031218072017.1971:putClipboardHeader
    def putClipboardHeader (self):
    
        c = self.c ; tnodes = 0
        #@    << count the number of tnodes >>
        #@+node:ekr.20031218072017.1972:<< count the number of tnodes >>
        c.clearAllVisited()
        
        for p in c.currentPosition().self_and_subtree_iter():
            t = p.v.t
            if t and not t.isWriteBit():
                t.setWriteBit()
                tnodes += 1
        #@-node:ekr.20031218072017.1972:<< count the number of tnodes >>
        #@nl
        self.put('<leo_header file_format="1" tnodes=')
        self.put_in_dquotes(str(tnodes))
        self.put(" max_tnode_index=")
        self.put_in_dquotes(str(tnodes))
        self.put("/>") ; self.put_nl()
    #@-node:ekr.20031218072017.1971:putClipboardHeader
    #@-node:ekr.20031218072017.1573:putLeoOutline (to clipboard) & helper
    #@+node:ekr.20060919064401:putToOPML & helpers
    def putToOPML (self):
        
        self.putXMLLine()
        self.putOPMLProlog()
        self.putOPMLHeader()
        self.putOPMLNodes()
        self.putOPMLPostlog()
    #@nonl
    #@+node:ekr.20060919064401.1:putOPMLProlog
    def putOPMLProlog (self):
    
        self.put('<opml version="1.0">\n')
    #@nonl
    #@-node:ekr.20060919064401.1:putOPMLProlog
    #@+node:ekr.20060919064401.2:putOPMLHeader
    def putOPMLHeader (self):
        
        '''Put the OPML header, including attributes for globals, prefs and  find settings.'''
        
        self.put('<head>\n')
        
        self.put('</head>\n')
    #@nonl
    #@-node:ekr.20060919064401.2:putOPMLHeader
    #@+node:ekr.20060919064401.3:putOPMLNodes
    def putOPMLNodes (self):
        
        c = self.c ; root = c.rootPosition()
        
        self.put('<body>\n')
        
        for p in root.self_and_siblings_iter():
            self.putOPMLNode(p)
        
        self.put('</body>\n')
    #@nonl
    #@-node:ekr.20060919064401.3:putOPMLNodes
    #@+node:ekr.20060919064401.4:putOPMLNode
    #@+at 
    #@nonl
    # Native xml attributes are the attributes of <v> and <t> elements that
    # are known (treated specially) by Leo's read/write code. The only native
    # attribute of <t> elements is tx. The native attributes of <v> elements 
    # are: a,
    # t, vtag, tnodeList, marks, expanded and 
    # descendentTnodeUnknownAttributes.
    #@-at
    #@@c
    
    def putOPMLNode (self,p):
        
        c = self.c ; indent = '\t' * p.level()
        body = p.bodyString() or '' ; head = p.headString() or ''
        
        a = self.aAttributes(p)
        uA = self.uAAttributes(p)
        tnodeList = self.tnodeListAttributes(p)
        
        self.put('%s<outline tx="%s" %s%s%s' % (
            indent,
            g.app.nodeIndices.toString(p.v.t.fileIndex),
            g.choose(a,'a="%s" ' % (a),''),
            g.choose(tnodeList,'tnodeList="%s" ' % (tnodeList),''),
            uA
        ))
        
        # python's xml.sax.saxutils.
        for tag,val in (('head',head),('body',body)):
            self.put(' %s="%s" ' % (tag,self.attributeEscape(val)))
        
        if p.hasChildren():
            self.put('>\n')
            for p2 in p.children_iter():
                self.putOPMLNode(p2)
            self.put('%s</outline>\n' % indent)
        else:
            self.put('/>\n')
    #@nonl
    #@+node:ekr.20060919085443:attributeEscape
    def attributeEscape(self,s):
    
        # Unlike xmlEscape, replace " by &quot; and replace newlines by character reference.
        s = s or ''
        return (
            s.replace('&','&amp;')
            .replace('<','&lt;')
            .replace('>','&gt;')
            .replace('"','&quot;')
            .replace('\n','&#10;\n')
        )
    #@-node:ekr.20060919085443:attributeEscape
    #@+node:ekr.20060919064401.5:aAttributes
    def aAttributes (self,p):
        
        c = self.c
        attr = []
    
        if p.isExpanded():          attr.append('E')
        if p.isMarked():            attr.append('M')
        if c.isCurrentPosition(p):  attr.append('V')
    
        #if p.v.isOrphan():              attr.append('O')
        #if p.equal(self.topPosition):   attr.append('T')
    
        return ''.join(attr)
    #@nonl
    #@-node:ekr.20060919064401.5:aAttributes
    #@+node:ekr.20060919064401.6:tnodeListAttributes
    # Based on fileCommands.putTnodeList.
    
    def tnodeListAttributes (self,p):
        
        '''Put the tnodeList attribute of p.v.t'''
    
        # Remember: entries in the tnodeList correspond to @+node sentinels, _not_ to tnodes!
        
        if not hasattr(p.v.t,'tnodeList') or not p.v.t.tnodeList:
            return ''
            
        # g.trace('tnodeList',p.v.t.tnodeList)
    
        # Assign fileIndices.
        for t in p.v.t.tnodeList:
            try: # Will fail for None or any pre 4.1 file index.
                theId,time,n = p.v.t.fileIndex
            except:
                g.trace("assigning gnx for ",p.v.t)
                gnx = g.app.nodeIndices.getNewIndex()
                p.v.t.setFileIndex(gnx) # Don't convert to string until the actual write.
    
        s = ','.join([g.app.nodeIndices.toString(t.fileIndex) for t in p.v.t.tnodeList])
    #@nonl
    #@-node:ekr.20060919064401.6:tnodeListAttributes
    #@+node:ekr.20060919064401.7:uAAttributes (Not yet, and maybe never)
    def uAAttributes (self,p):
        
        return ''
    #@nonl
    #@-node:ekr.20060919064401.7:uAAttributes (Not yet, and maybe never)
    #@-node:ekr.20060919064401.4:putOPMLNode
    #@+node:ekr.20060919064401.8:putOPMLPostlog
    def putOPMLPostlog (self):
        
        self.put('</opml>\n')
    #@nonl
    #@-node:ekr.20060919064401.8:putOPMLPostlog
    #@-node:ekr.20060919064401:putToOPML & helpers
    #@+node:ekr.20031218072017.1720:save
    def save(self,fileName):
    
        c = self.c ; v = c.currentVnode()
    
        # New in 4.2.  Return ok flag so shutdown logic knows if all went well.
        ok = g.doHook("save1",c=c,p=v,v=v,fileName=fileName)
        if ok is None:
            c.beginUpdate()
            try:
                c.endEditing()# Set the current headline text.
                self.setDefaultDirectoryForNewFiles(fileName)
                ok = self.write_Leo_file(fileName,False) # outlineOnlyFlag
                if ok:
                    c.setChanged(False) # Clears all dirty bits.
                    g.es("saved: " + g.shortFileName(fileName))
                    if c.config.save_clears_undo_buffer:
                        g.es("clearing undo")
                        c.undoer.clearUndoState()
            finally:
                c.endUpdate()
        g.doHook("save2",c=c,p=v,v=v,fileName=fileName)
        return ok
    #@-node:ekr.20031218072017.1720:save
    #@+node:ekr.20031218072017.3043:saveAs
    def saveAs(self,fileName):
    
        c = self.c ; v = c.currentVnode()
    
        if not g.doHook("save1",c=c,p=v,v=v,fileName=fileName):
            c.beginUpdate()
            try:
                c.endEditing() # Set the current headline text.
                self.setDefaultDirectoryForNewFiles(fileName)
                if self.write_Leo_file(fileName,False): # outlineOnlyFlag
                    c.setChanged(False) # Clears all dirty bits.
                    g.es("saved: " + g.shortFileName(fileName))
            finally:
                c.endUpdate()
        g.doHook("save2",c=c,p=v,v=v,fileName=fileName)
    #@-node:ekr.20031218072017.3043:saveAs
    #@+node:ekr.20031218072017.3044:saveTo
    def saveTo (self,fileName):
    
        c = self.c ; v = c.currentVnode()
    
        if not g.doHook("save1",c=c,p=v,v=v,fileName=fileName):
            c.beginUpdate()
            try:
                c.endEditing()# Set the current headline text.
                self.setDefaultDirectoryForNewFiles(fileName)
                if self.write_Leo_file(fileName,False): # outlineOnlyFlag
                    g.es("saved: " + g.shortFileName(fileName))
            finally:
                c.endUpdate()
        g.doHook("save2",c=c,p=v,v=v,fileName=fileName)
    #@-node:ekr.20031218072017.3044:saveTo
    #@+node:ekr.20031218072017.3045:setDefaultDirectoryForNewFiles
    def setDefaultDirectoryForNewFiles (self,fileName):
        
        """Set c.openDirectory for new files for the benefit of leoAtFile.scanAllDirectives."""
        
        c = self.c
    
        if not c.openDirectory or len(c.openDirectory) == 0:
            theDir = g.os_path_dirname(fileName)
    
            if len(theDir) > 0 and g.os_path_isabs(theDir) and g.os_path_exists(theDir):
                c.openDirectory = theDir
    #@-node:ekr.20031218072017.3045:setDefaultDirectoryForNewFiles
    #@+node:ekr.20031218072017.3046:write_Leo_file
    def write_Leo_file(self,fileName,outlineOnlyFlag,toString=False,toOPML=False):
    
        c = self.c
        self.assignFileIndices()
        if not outlineOnlyFlag or toOPML:
            # Update .leoRecentFiles.txt if possible.
            g.app.config.writeRecentFilesFile(c)
            #@        << write all @file nodes >>
            #@+node:ekr.20040324080359:<< write all @file nodes >>
            try:
                # Write all @file nodes and set orphan bits.
                c.atFileCommands.writeAll()
            except Exception:
                g.es_error("exception writing derived files")
                g.es_exception()
                return False
            #@-node:ekr.20040324080359:<< write all @file nodes >>
            #@nl
        #@    << return if the .leo file is read-only >>
        #@+node:ekr.20040324080359.1:<< return if the .leo file is read-only >>
        # self.read_only is not valid for Save As and Save To commands.
        
        if g.os_path_exists(fileName):
            try:
                if not os.access(fileName,os.W_OK):
                    g.es("can not create: read only: " + fileName,color="red")
                    return False
            except:
                pass # os.access() may not exist on all platforms.
        #@-node:ekr.20040324080359.1:<< return if the .leo file is read-only >>
        #@nl
        try:
            theActualFile = None
            if not toString:
                #@            << create backup file >>
                #@+node:ekr.20031218072017.3047:<< create backup file >>
                # rename fileName to fileName.bak if fileName exists.
                if g.os_path_exists(fileName):
                    backupName = g.os_path_join(g.app.loadDir,fileName)
                    backupName = fileName + ".bak"
                    if g.os_path_exists(backupName):
                        g.utils_remove(backupName)
                    ok = g.utils_rename(fileName,backupName)
                    if not ok:
                        if self.read_only:
                            g.es("read only",color="red")
                        return False
                else:
                    backupName = None
                #@-node:ekr.20031218072017.3047:<< create backup file >>
                #@nl
            self.mFileName = fileName
            if toOPML:
                #@            << ensure that filename ends with .opml >>
                #@+node:ekr.20060919070145:<< ensure that filename ends with .opml >>
                if not self.mFileName.endswith('opml'):
                    self.mFileName = self.mFileName + '.opml'
                fileName = self.mFileName
                #@nonl
                #@-node:ekr.20060919070145:<< ensure that filename ends with .opml >>
                #@nl
            self.outputFile = cStringIO.StringIO()
            if not toString:
                theActualFile = open(fileName, 'wb')
            if toOPML:
                self.putToOPML()
            else:
                self.putLeoFile()
            s = self.outputFile.getvalue()
            if toString:
                # For support of chapters plugin.
                g.app.write_Leo_file_string = s
            else:
                theActualFile.write(s)
                theActualFile.close()
                #@            << delete backup file >>
                #@+node:ekr.20031218072017.3048:<< delete backup file >>
                if backupName and g.os_path_exists(backupName):
                
                    self.deleteFileWithMessage(backupName,'backup')
                #@-node:ekr.20031218072017.3048:<< delete backup file >>
                #@nl
            self.outputFile = None
            return True
        except Exception:
            g.es("exception writing: " + fileName)
            g.es_exception(full=False)
            if theActualFile: theActualFile.close()
            self.outputFile = None
            #@        << delete fileName >>
            #@+node:ekr.20050405103712:<< delete fileName >>
            if fileName and g.os_path_exists(fileName):
                self.deleteFileWithMessage(fileName,'')
            #@-node:ekr.20050405103712:<< delete fileName >>
            #@nl
            #@        << rename backupName to fileName >>
            #@+node:ekr.20050405103712.1:<< rename backupName to fileName >>
            if backupName:
                g.es("restoring " + fileName + " from " + backupName)
                g.utils_rename(backupName,fileName)
            #@-node:ekr.20050405103712.1:<< rename backupName to fileName >>
            #@nl
            return False
    
    write_LEO_file = write_Leo_file # For compatibility with old plugins.
    #@nonl
    #@-node:ekr.20031218072017.3046:write_Leo_file
    #@+node:ekr.20031218072017.2012:writeAtFileNodes
    def writeAtFileNodes (self,event=None):
        
        '''Write all @file nodes in the selected outline.'''
    
        c = self.c
    
        self.assignFileIndices()
        changedFiles = c.atFileCommands.writeAll(writeAtFileNodesFlag=True)
        assert(changedFiles != None)
        if changedFiles:
            g.es("auto-saving outline",color="blue")
            c.save() # Must be done to set or clear tnodeList.
    #@-node:ekr.20031218072017.2012:writeAtFileNodes
    #@+node:ekr.20031218072017.1666:writeDirtyAtFileNodes
    def writeDirtyAtFileNodes (self,event=None):
    
        '''Write all changed @file Nodes.'''
        
        c = self.c
    
        self.assignFileIndices() # 4/3/04
        changedFiles = c.atFileCommands.writeAll(writeDirtyAtFileNodesFlag=True)
        if changedFiles:
            g.es("auto-saving outline",color="blue")
            c.save() # Must be done to set or clear tnodeList.
    #@-node:ekr.20031218072017.1666:writeDirtyAtFileNodes
    #@+node:ekr.20031218072017.2013:writeMissingAtFileNodes
    def writeMissingAtFileNodes (self,event=None):
        
        '''Write all missing @file nodes.'''
    
        c = self.c ; v = c.currentVnode()
    
        if v:
            at = c.atFileCommands
            self.assignFileIndices() # 4/3/04
            changedFiles = at.writeMissing(v)
            assert(changedFiles != None)
            if changedFiles:
                g.es("auto-saving outline",color="blue")
                c.save() # Must be done to set or clear tnodeList.
    #@-node:ekr.20031218072017.2013:writeMissingAtFileNodes
    #@+node:ekr.20031218072017.3050:writeOutlineOnly
    def writeOutlineOnly (self,event=None):
        
        '''Write the entire outline without writing any derived files.'''
    
        c = self.c
        c.endEditing()
        self.write_Leo_file(self.mFileName,True) # outlineOnlyFlag
    #@-node:ekr.20031218072017.3050:writeOutlineOnly
    #@+node:ekr.20031218072017.3051:xmlEscape
    # Surprisingly, this is a time critical routine.
    
    def xmlEscape(self,s):
    
        assert(s and len(s) > 0) # check is made in putEscapedString
        s = string.replace(s, '\r', '')
        s = string.replace(s, '&', "&amp;")
        s = string.replace(s, '<', "&lt;")
        s = string.replace(s, '>', "&gt;")
        return s
    #@-node:ekr.20031218072017.3051:xmlEscape
    #@-node:ekr.20031218072017.3032:Writing
    #@-others
    
class fileCommands (baseFileCommands):
    """A class creating the fileCommands subcommander."""
    pass
#@nonl
#@-node:ekr.20031218072017.3018:@thin leoFileCommands.py
#@-leo
