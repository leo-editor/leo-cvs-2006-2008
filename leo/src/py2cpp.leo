<?xml version="1.0" encoding="utf-8"?>
<?xml-stylesheet ekr_test?>
<leo_file>
<leo_header file_format="2" tnodes="0" max_tnode_index="0" clone_windows="0"/>
<globals body_outline_ratio="0.275510204082">
	<global_window_position top="92" left="269" height="686" width="870"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="ekr.20061203113554"><vh>Docs</vh>
<v t="ekr.20061203114036"><vh>Intro</vh></v>
<v t="ekr.20061203114036.1"><vh>Separating translated code</vh></v>
<v t="ekr.20061203114036.2"><vh>Type annotations</vh></v>
<v t="ekr.20061203114036.3"><vh>Lifetimes</vh></v>
<v t="ekr.20061203114036.4"><vh>py2cpp assertions</vh></v>
<v t="ekr.20061203114036.5"><vh>Exceptions</vh></v>
<v t="ekr.20061203114036.6"><vh>Conclusions</vh></v>
</v>
<v t="ekr.20061203123201"><vh>c2py  (reference)</vh>
<v t="ekr.20061203123201.1"><vh>&lt;&lt; what c2py does &gt;&gt;</vh></v>
<v t="ekr.20061203123201.2"><vh>&lt;&lt; theory of operation &gt;&gt;</vh></v>
<v t="ekr.20061203123201.3"><vh>&lt;&lt; specify user types &gt;&gt;</vh></v>
<v t="ekr.20061203123201.4"><vh>&lt;&lt; define testData &gt;&gt;</vh></v>
<v t="ekr.20061203123201.5"><vh>speedTest</vh></v>
<v t="ekr.20061203123201.6"><vh>leo1to2</vh>
<v t="ekr.20061203123201.7"><vh>leo1to2</vh></v>
<v t="ekr.20061203123201.8"><vh>convertLeo1to2</vh></v>
<v t="ekr.20061203123201.9"><vh>convertStringLeo1to2</vh></v>
<v t="ekr.20061203123201.10"><vh>convertCodeList1to2</vh></v>
</v>
<v t="ekr.20061203123201.11"><vh>c2py entry points</vh>
<v t="ekr.20061203123201.12"><vh>convertCurrentTree</vh></v>
<v t="ekr.20061203123201.13"><vh>convertLeoTree</vh></v>
<v t="ekr.20061203123201.14"><vh>convertCFileToPython</vh></v>
</v>
<v t="ekr.20061203123201.15"><vh>convertCStringToPython &amp; helpers (top level)</vh>
<v t="ekr.20061203123201.16"><vh>convertCodeList (main pattern function)</vh></v>
<v t="ekr.20061203123201.17"><vh>convertDocList</vh></v>
<v t="ekr.20061203123201.18"><vh>skipDocPart</vh></v>
<v t="ekr.20061203123201.19"><vh>skipCodePart</vh></v>
</v>
<v t="ekr.20061203123201.20"><vh>Scanning &amp; Replacing...</vh>
<v t="ekr.20061203123201.21"><vh>convertLeadingBlanks</vh></v>
<v t="ekr.20061203123201.22"><vh>mungeAllFunctions</vh>
<v t="ekr.20061203123201.23"><vh>handlePossibleFunctionHeader</vh></v>
<v t="ekr.20061203123201.24"><vh>massageFunctionArgs</vh></v>
<v t="ekr.20061203123201.25"><vh>massageFunctionHead (sets gClassName)</vh></v>
<v t="ekr.20061203123201.26"><vh>massageFunctionBody</vh>
<v t="ekr.20061203123201.27"><vh>massageIvars</vh></v>
<v t="ekr.20061203123201.28"><vh>removeCasts</vh></v>
<v t="ekr.20061203123201.29"><vh>removeTypeNames</vh></v>
</v>
</v>
<v t="ekr.20061203123201.30"><vh>handleAllKeywords</vh>
<v t="ekr.20061203123201.31"><vh>handleKeyword</vh></v>
</v>
<v t="ekr.20061203123201.32"><vh>isX...</vh>
<v t="ekr.20061203123201.33"><vh>isWs and isWOrNl</vh></v>
<v t="ekr.20061203123201.34"><vh>isSectionDef</vh></v>
<v t="ekr.20061203123201.35"><vh>isStringOrComment</vh></v>
</v>
<v t="ekr.20061203123201.36"><vh>find... &amp; match...</vh>
<v t="ekr.20061203123201.37"><vh>findInCode</vh></v>
<v t="ekr.20061203123201.38"><vh>findInList</vh></v>
<v t="ekr.20061203123201.39"><vh>match</vh></v>
<v t="ekr.20061203123201.40"><vh>matchWord</vh></v>
</v>
<v t="ekr.20061203123201.41"><vh>remove...</vh>
<v t="ekr.20061203123201.42"><vh>removeAllCComments</vh></v>
<v t="ekr.20061203123201.43"><vh>removeAllCSentinels</vh></v>
<v t="ekr.20061203123201.44"><vh>removeAllPythonComments</vh></v>
<v t="ekr.20061203123201.45"><vh>removeAllPythonSentinels</vh></v>
<v t="ekr.20061203123201.46"><vh>removeAtRoot</vh></v>
<v t="ekr.20061203123201.47"><vh>removeBlankLines</vh></v>
<v t="ekr.20061203123201.48"><vh>removeExcessWs</vh>
<v t="ekr.20061203123201.49"><vh>removeExessWsFromLine</vh></v>
</v>
<v t="ekr.20061203123201.50"><vh>removeLeadingAtCode</vh></v>
<v t="ekr.20061203123201.51"><vh>removeMatchingBrackets</vh></v>
<v t="ekr.20061203123201.52"><vh>removeSemicolonsAtEndOfLines</vh></v>
<v t="ekr.20061203123201.53"><vh>removeTrailingWs</vh></v>
</v>
<v t="ekr.20061203123201.54"><vh>replace... &amp; safeReplace</vh>
<v t="ekr.20061203123201.55"><vh>replace</vh></v>
<v t="ekr.20061203123201.56"><vh>replaceComments</vh></v>
<v t="ekr.20061203123201.57"><vh>replaceSectionDefs</vh></v>
<v t="ekr.20061203123201.58"><vh>safeReplace</vh></v>
</v>
<v t="ekr.20061203123201.59"><vh>skip... &amp; prev...</vh>
<v t="ekr.20061203123201.60"><vh>prevNonWsChar and prevNonWsOrNlChar</vh></v>
<v t="ekr.20061203123201.61"><vh>skipCBlockComment</vh></v>
<v t="ekr.20061203123201.62"><vh>skipPastLine</vh></v>
<v t="ekr.20061203123201.63"><vh>skipPastWord</vh></v>
<v t="ekr.20061203123201.64"><vh>skipString</vh></v>
<v t="ekr.20061203123201.65"><vh>skipStringOrComment</vh></v>
<v t="ekr.20061203123201.66"><vh>skipToMatchingBracket</vh></v>
<v t="ekr.20061203123201.67"><vh>skipWs and skipWsAndNl</vh></v>
</v>
<v t="ekr.20061203123201.68"><vh>stringToList &amp; listToString</vh>
<v t="ekr.20061203123201.69"><vh>stringToList</vh></v>
<v t="ekr.20061203123201.70"><vh>listToString</vh></v>
</v>
</v>
</v>
<v t="ekr.20061203123249" a="ETV"><vh>@button py2cpp</vh>
<v t="ekr.20061203131351"><vh>class controllerClass</vh>
<v t="ekr.20061203131351.1"><vh>ctor</vh></v>
<v t="ekr.20061203131351.2"><vh>findCode</vh></v>
<v t="ekr.20061203131636"><vh>tokenize</vh></v>
<v t="ekr.20061203131351.3"><vh>parse</vh></v>
<v t="ekr.20061203131351.4"><vh>gen</vh></v>
<v t="ekr.20061203131351.5"><vh>put</vh></v>
</v>
</v>
</vnodes>
<tnodes>
<t tx="ekr.20061203113554">@nocolor


</t>
<t tx="ekr.20061203114036">My first python program was c2py, a program that did about 80% of the
transliteration drudgery in converting the C++ version of Leo to Python. This
program is in scripts.leo: Scripts--&gt;@file leoScripts.txt--&gt;Important--&gt;c2py
Convert C code to Python syntax

Following some pleasant off-line conversations with Michael Hudson of the pypy
project, I think it is time to do the reverse: create a program (py2cpp) that
will translate python code to C++. My thinking is this: The pypy project has
highly sophisticated tools (that take hours to run) that discover the types and
lifetimes of objects. But for the code *I* want to optimize, I already *know*
the types and lifetimes of all objects. Ever since lisp back in the early 60's,
garbage-collection languages have erected an impenetrable barrier between the
programmer and the allocator/garbage collector. In my case, I know a *lot* about
Leo's objects that I am *prohibited* from telling Python about. Thus, if I am
not mistaken (and I very well might be), the task of translating
(transliterating, really) from Python to C++ should be routine.

In Leo, the code to be translated are the node classes in leoNodes.py, the
read/write code in leoFileCommands.py and leoAtFile.py and the syntax coloring
code leoColor.py. Only parts of these modules would be translated, which makes
the job easier--hopefully *much* easier.

Please note, though, that *in general* the pypy way is the only way. For
example, Michael pointed me at:
http://webpages.charter.net/edreamleo/whitepapers.html#allocating-storage-using-lifetimes
This is a lovely paper. Very clear, and completely in alignment with my present
thinking. It shows, I think, the optimal way of discovering lifetimes in
general. But I know so much more about Leo that will *ever* be discovered by an
automatic tool!

I'm not willing to wait years for the pypy project to be completed. More
importantly, I do not want to run a tool that takes 2-3 hours to run every time
I change 'optimized' python code. Instead, I want a tool, written in Python of
course, that will translate my python code to C++ in a matter of seconds.
</t>
<t tx="ekr.20061203114036.1">By analogy with pypy's Restricted Python (RPython) language, py2cpp will
translate only a subset of Python. In particular, I definitely do not want to
translate import statements. We can enclose code to be transliterated in

if __py2cpp_compile: 
....&lt;&lt;define the python version of the code&gt;&gt;

py2cpp will create an *extension* module that will add the translated code
(including class defs?) back into the module from which they came. As I write
this, I see that this step could be tricky, but clearly it is doable.</t>
<t tx="ekr.20061203114036.2">To bypass pypy's type scanner (very expensive), some by-hand annotations will be
required. Maybe I'll call the resulting language: APython, for annotated Python.
The translator must know about Leo's coding conventions for c, p, g, w, d, etc.
Providing these coding conventions *once* (hard-coded in the py2cpp, or better,
in a config .leo file) eliminates the need for most annotations. One place where
annotations will be needed is in ctors. Something like:

def __init__ (self):
....self.x = 0 # type:i (integer)
....self.s = 'abc' # type:s (string)
....self.v = None # type:v (a vnode, as usual)

etc.  That is, the comments are the annotation.</t>
<t tx="ekr.20061203114036.3">We can't generate C++ code unless we can bypass Python's garbage collector (gc)
entirely. Fortunately, I know the lifetimes of all objects in the code I want to
translate. For vnodes and tnodes, the lifetime extends until the window
containing the outline closes. Call this the **window lifetime**. For the
colorizer, the lifetime is either permanent, the window lifetime, or
**temporary**, extending only until a (particular) method ends.

Again, Python provides no way for me to tell it about lifetimes. I'll probably
add __alloc__ and __dealloc__ methods (defined only if __py2cpp_compile is True)
that explicitly tell how to allocate and deallocate objects created by py2cpp.
That is, the __alloc__ tells how to allocate the 'self' object that is passed to
__init__. The __dealloc__ method (if it's really needed) will indicate the
**lifetime-point** (perhaps end-of-lifetime-point is a better term). This is the
place at which all methods having a particular lifetime will be reclaimed
en-mass. Since objects will be allocated in fixed-sized blocks, reclaiming can
be done extremely quickly. The actual deallocation will be done via a call (in
python) to a function in a py2cpp module. Or something like that. Anyway, the
essential idea is that the lifetime-point is indicated at a specific point in
the *Python* code.</t>
<t tx="ekr.20061203114036.4">The entire projects depends on the fact that I know (or think I know) what the
types and lifetimes of objects are. Clearly, hard crashes will happen if I am
wrong. Thus, a debugging mode (for the generated C++ code) is required to test
all relevant assertions implied by lifetimes and type allocations. I believe
that fixing the occasional failed assertions is *far* preferable to waiting for
pypy to verify the types 'from scratch' every time I add a Python statement :-)
Note that unit tests provide the obvious ways to test all important assertions.

The details of this part of the project are a bit fuzzy, but clearly vnodes and
tnodes are essentially immortal because of unlimited undo. That being so, we can
kill vnodes and tnodes *only* when their window closes. Conversely, when a
window closes, everything in it can go away, so we are safe. For other objects,
however, lifetime assertions may be harder to prove. If this becomes a big deal
(and it might) I think some kind of 'Gc viewer' tool might be good.
</t>
<t tx="ekr.20061203114036.5">C++ exception handling is not the same as Python exception handling. Don't know
exactly how I'll handle this, but some way will be found. Likely the pypy people
have already figured this out...
</t>
<t tx="ekr.20061203114036.6">My intuition is that **for sure** such a project is feasible.

py2cpp might be a useful test bed for pypy.

Now I know why I have always resisted hand-coding some of Leo's time-critical
code. It's hard to maintain two versions of code, but more importantly it's
wasted work (worse, misguided and error-producing work) if an automatic tool can
do the job instead.
</t>
<t tx="ekr.20061203123201">@first
@language python
@tabwidth -4

import string

@ When using c2py as a script to translate entire files, use convertCFileToPython().  When using c2py within Leo, use convertCurrentTree().

Please set user data in the &lt;&lt; specifying user types &gt;&gt; section.
@c

&lt;&lt; what c2py does &gt;&gt;
&lt;&lt; theory of operation &gt;&gt;
&lt;&lt; specify user types &gt;&gt;
tabWidth = 4 # how many blanks in a tab.
printFlag = False
doLeoTranslations = True ; dontDoLeoTranslations = False
&lt;&lt; define testData &gt;&gt;
@others

gClassName = "" # The class name for the present function.  Used to modify ivars.
gIvars = [] # List of ivars to be converted to self.ivar

def test():
    global printFlag ; printFlag = True
    for s in testData:
        convertCStringToPython(s, doLeoTranslations)
        
def go():
    test()

if __name__ == "__main__":
    speedTest(2)</t>
<t tx="ekr.20061203123201.1">@
c2py converts C or C++ text into python text. The conversion is not complete.
Nevertheless, c2py eliminates much of the tedious text manipulation that would
otherwise be required.

The following is a list of the translations performed by convertCodeList:

I.  Prepass

These translations happen before removing all curly braces.

Suppose we are translating:

    aTypeSpec aClass::aMethod(t1 v1,...,tn vn)
    {
        body
    }

1. Translates the function prototype, i.e., translates:

    aTypeSpec aClass::aMethod(t1 v1,...,tn vn)
to:
    def aMethod(v1,...vn):

As a special case, c2py translates:

    aTypeSpec aClass::aClass(t1 v1,...,tn vn)
to:
    aClass.__init__(t1 v1,...,tn vn)

Yes, I know, aClass.__init__ isn't proper Python, but retaining the class name is useful.

2. Let t denote any member of typeList or classList.

    a) Removes all casts of the form (t) or (t*) or (t**), etc.
    b) Converts t x, t *x, t **x, etc. to x.
    c) Converts x = new t(...) to x = t(...)
    d) For all i in ivarsDict[aClass] converts this -&gt; i to self.i
    e) For all i in ivarsDict[aClass] converts i to self.i

3. Converts &lt; &lt; x &gt; &gt; = to @c.  This Leo-specific translation is not done when translating files.

II.  Main Pass

This pass does the following simple translations everywhere except in comments and strings.

Changes all -&gt; to .
Changes all this.self to self (This corrects problems during the prepass.)
Removes all curly braces
Changes all #if to if
Changes all else if to elif
Changes all #else to else:
Changes all else to else:
Removes all #endif
Changes all &amp;&amp; to and
Changes all || to or
Changes all TRUE to True
Changes all FALSE to False
Changes all NULL to None
Changes all this to self
Changes all @code to @c.  This Leo-specific translation is not done when translating files.

III.  Complex Pass

This pass attempts more complex translations.

Converts if ( x ) to if x:
Converts elif ( x ) to elif x:
Converts while ( x ) to while x:
Converts for ( x ; y ; z ) to for x SEMI y SEMI z:

IV.  Final Pass

This pass completes the translation.

Removes all semicolons.
Removes @c if it starts the text.  This Leo-specific translation is not done when translating files.
Removes all blank lines.
Removes excess whitespace from all lines, leaving leading whitespace unchanged.
Replaces C/C++ comments by Python comments.
Removes trailing whitespace from all lines.
</t>
<t tx="ekr.20061203123201.2">@ Strategy and Performance

c2py is straightforward.  The speed of c2py is unimportant.  We don't care about the memory used because we translate only small pieces of text at a time.

We can do body[i:j] = x, regardless of len(x).  We can also do del body[i:j] to delete characters.

We scan repeatedly through the text.  Using many passes greatly simplifies the code and does not slow down c2py significantly.

No scans are done within strings or comments.  The idiom to handle such scans is the following:

def someScan(body):
    i = 0
    while i &lt; body(len):
        if isStringOrComment(body,i):
            i = skipStringOrComment(body,i)
        elif &lt;&lt; found what we are looking for ? &gt;&gt; :
            &lt;&lt; convert what we are looking for, setting i &gt;&gt;
        else: i += 1

That's about all there is to it.  The code was remarkably easy to write and seems clear to me.
</t>
<t tx="ekr.20061203123201.3">@ Please change the following lists so they contain the types and classes used by your program.

c2py removes all type definitions correctly; it converts
    new aType(...)
to
    aType(...)
@c

classList = [
    "vnode", "tnode", "Commands",
    "wxString", "wxTreeCtrl", "wxTextCtrl", "wxSplitterWindow" ]
    
typeList = ["char", "void", "short", "long", "int", "double", "float"]

@ Please change ivarsDict so it represents the instance variables (ivars) used by your program's classes.

ivarsDict is a dictionary used to translate ivar i of class c to self.i.  It also translates this-&gt;i to self.i.
@c
    
ivarsDict = {
    "atFile": [ "mCommands", "mErrors", "mStructureErrors",
        "mTargetFileName", "mOutputFileName", "mOutputStream",
        "mStartSentinelComment", "mEndSentinelComment", "mRoot"],

    "vnode": ["mCommands", "mJoinList", "mIconVal", "mTreeID", "mT", "mStatusBits"],

    "tnode": ["mBodyString", "mBodyRTF", "mJoinHead", "mStatusBits", "mFileIndex",
        "mSelectionStart", "mSelectionLength", "mCloneIndex"],
        
    "LeoFrame": ["mNextFrame", "mPrevFrame", "mCommands"],

    "Commands": [
        # public
        "mCurrentVnode", "mLeoFrame", "mInhibitOnTreeChanged", "mMaxTnodeIndex",
        "mTreeCtrl", "mBodyCtrl", "mFirstWindowAndNeverSaved",
        #private
        "mTabWidth", "mChanged", "mOutlineExpansionLevel", "mUsingClipboard",
        "mFileName", "mMemoryInputStream", "mMemoryOutputStream", "mFileInputStream",
        "mInputFile", "mFileOutputStream", "mFileSize", "mTopVnode", "mTagList",
        "mMaxVnodeTag",
        "mUndoType", "mUndoVnode", "mUndoParent", "mUndoBack", "mUndoN",
        "mUndoDVnodes", "mUndoLastChild", "mUndoablyDeletedVnode" ]}</t>
<t tx="ekr.20061203123201.4">testData = [ "\n@doc\n\
This is a doc part: format, whilest, {};-&gt;.\n\
&lt;&lt;\
section def&gt;&gt;=\n\
LeoFrame::LeoFrame(vnode *v, char *s, int i)\n\
{\n\
    // test ; {} /* */.\n\
    #if 0 //comment\n\
        if(gLeoFrameList)gLeoFrameList -&gt; mPrevFrame = this ;\n\
        else\n\
            this -&gt; mNextFrame = gLeoFrameList ;\n\
    #else\n\
        \n\
        vnode *v = new vnode(a,b);\n\
        Commands *commander = (Commands) NULL ; // after cast\n\
        this -&gt; mPrevFrame = NULL ;\n\
    #endif\n\
    if (a==b)\n\
        a = 2;\n\
    else if (a ==c)\n\
        a = 3;\n\
    else return; \n\
    /* Block comment test:\n\
        if(2):while(1): end.*/\n\
    for(int i = 1; i &lt; limit; ++i){\n\
        mVisible = FALSE ;\n\
        mOnTop = TRUE ;\n\
    }\n\
    // trailing ws.	 \n\
    mCommands = new Commands(this, mTreeCtrl, mTextCtrl) ;\n\
    gActiveFrame = this ;\n\
}\n\
    ", "&lt;&lt;" +
"vnode methods &gt;&gt;=\n\
\n\
void vnode::OnCopyNode(wxCommandEvent&amp; WXUNUSED(event))\n\
{\n\
    mCommands -&gt; copyOutline();\n\
}\n\
\n@doc\n\
another doc part if, then, else, -&gt; \n&lt;&lt;" +
"vnode methods &gt;&gt;=\n\
void vnode::OnPasteNode(wxCommandEvent&amp; WXUNUSED(event))\n\
{\n\
    mCommands -&gt; pasteOutline();\n\
}\n" ]</t>
<t tx="ekr.20061203123201.5">def speedTest(passes):

    import time
    file = r"c:\prog\LeoPy\LeoPy.leo"
    f=open(file)
    if not f:
        print "not found: ", file
        return
    s=f.read()
    f.close()
    print "file:", file, " size:", len(s), " passes:", passes
    print "speedTest start"
    time1 = time.clock()
    p = passes
    while p &gt; 0:
        n = len(s) ; i = 0 ; lines = 0
        while -1 &lt; i &lt; n:
            if s[i] == '\n':
                lines += 1 ; i += 1
            else:
                i = s.find('\n',i) # _much_ faster than list-based-find.
            continue
            # match is about 9 times slower than simple test.
            if s[i]=='\n': # match(s,i,'\n'): # 
                i += 1
            else:
                i += 1
        p -= 1
    time2 = time.clock()
    print "lines:", lines
    print "speedTest done:"
    print "elapsed time:", time2-time1
    print "time/pass:", (time2-time1)/passes</t>
<t tx="ekr.20061203123201.6"></t>
<t tx="ekr.20061203123201.7">def leo1to2():

    import leo
    import leoGlobals
    c=leoGlobals.top()
    v=c.currentVnode()
    convertLeo1to2(v,c)
</t>
<t tx="ekr.20061203123201.8">def convertLeo1to2(v,c):

    after=v.nodeAfterTree()
    while v and v != after:
        s=v.bodyString()
        print "converting:", v.headString()
        s=convertStringLeo1to2(s)
        c.setBodyString(v,s)
        v=v.threadNext()

    c.Repaint() # for backward compatibility
    print "end of leo1to2"</t>
<t tx="ekr.20061203123201.9">def convertStringLeo1to2 (s):

    # print "convertStringLeo1to2:start\n", s
    codeList = stringToList(s) ; outputList = []
    i = 0
    while i &lt; len(codeList):
        j = skipCodePart(codeList,i)
        if j &gt; i:
            code = codeList[i:j]
            convertCodeList1to2(code)
            i = j
            #print "-----code:", listToString(code)
            for item in code:
                outputList.append(item)
        j = skipDocPart(codeList,i)
        if j &gt; i:
            doc = codeList[i:j]
            convertDocList(doc) # same as in c2py
            #print "-----doc:", listToString(doc)
            i = j
            for item in doc:
                outputList.append(item)
    
    result = listToString(outputList)
    global printFlag
    if printFlag: print "-----:\n", result
    return result</t>
<t tx="ekr.20061203123201.10">@ We do _not_ replace @root by @file or insert @others as needed.  Inserting @others can be done easily enough by hand, and may take more global knowledge than we can reasonably expect to have.
@c

def convertCodeList1to2(list):

    if 0: # There isn't much reason to do this.
        removeAtRoot(list)
    safeReplace(list, "@code", "@c")
    replaceSectionDefs(list)
    removeLeadingAtCode(list)
</t>
<t tx="ekr.20061203123201.11">@ We separate the processing into two parts,

1) a leo-aware driver that iterates over @file trees and
2) a text-based part that processes one or more files or strings.
</t>
<t tx="ekr.20061203123201.12">def convertCurrentTree():

    import c2py
    import leo
    import leoGlobals
    c=leoGlobals.top()
    v = c.currentVnode()
    c2py.convertLeoTree(v,c)</t>
<t tx="ekr.20061203123201.13">def convertLeoTree(v,c):

    after=v.nodeAfterTree()
    while v and v != after:
        s=v.bodyString()
        print "converting:", v.headString()
        s=convertCStringToPython(s, doLeoTranslations )
        c.setBodyString(v,s)
        v=v.threadNext()
    c.Repaint() # for backward compatibility.
    print "end of c2py"</t>
<t tx="ekr.20061203123201.14">def convertCFileToPython(file):

    f=open(file, 'r')
    if not f: return
    s = f.read()
    f.close();
    f=open(file + ".py", 'w')
    if not f: return
    s = convertCStringToPython(s, dontDoLeoTranslations )
    f.write(s)
    f.close()</t>
<t tx="ekr.20061203123201.15">def convertCStringToPython(s, leoFlag):

    # print "convertCStringToPython:start\n", s
    firstPart = True
    codeList = stringToList(s)
    
    if not leoFlag:
        convertCodeList(codeList, firstPart, dontDoLeoTranslations)
        return listToString(codeList)

    outputList = []
    i = 0
    while i &lt; len(codeList):
        j = skipCodePart(codeList,i)
        if j &gt; i:
            code = codeList[i:j]
            convertCodeList(code, firstPart, doLeoTranslations)
            i = j
            #print "-----code:", listToString(code)
            for item in code:
                outputList.append(item)
        firstPart = False # don't remove @c from here on.
        j = skipDocPart(codeList,i)
        if j &gt; i:
            doc = codeList[i:j]
            convertDocList(doc)
            #print "-----doc:", listToString(doc)
            i = j
            for item in doc:
                outputList.append(item)
    
    result = listToString(outputList)
    global printFlag
    if printFlag: print "-----:\n", result
    return result</t>
<t tx="ekr.20061203123201.16">def convertCodeList(list, firstPart, leoFlag):
    #first
    replace(list, "\r", None)
    convertLeadingBlanks(list)
    if leoFlag:
        replaceSectionDefs(list)
    mungeAllFunctions(list)
    #next
    safeReplace(list, " -&gt; ", '.')
    safeReplace(list, "-&gt;", '.')
    safeReplace(list, " . ", '.')
    safeReplace(list, "this.self", "self")
    safeReplace(list, "{", None)
    safeReplace(list, "}", None)
    safeReplace(list, "#if", "if")
    safeReplace(list, "#else", "else")
    safeReplace(list, "#endif", None)
    safeReplace(list, "else if", "elif")
    safeReplace(list, "else", "else:")
    safeReplace(list, "&amp;&amp;", "and")
    safeReplace(list, "||", "or")
    safeReplace(list, "TRUE", "True")
    safeReplace(list, "FALSE", "False")
    safeReplace(list, "NULL", "None")
    safeReplace(list, "this", "self")
    safeReplace(list, "try", "try:")
    safeReplace(list, "catch", "except:")
    if leoFlag:
        safeReplace(list, "@code", "@c")
    #next
    handleAllKeywords(list)
    # after processing for keywords
    removeSemicolonsAtEndOfLines(list)
    #last
    if firstPart and leoFlag: removeLeadingAtCode(list)
    removeBlankLines(list)
    removeExcessWs(list)
    # your taste may vary: in Python I don't like extra whitespace
    safeReplace(list, " :", ":") 
    safeReplace(list, ", ", ",")
    safeReplace(list, " ,", ",")
    safeReplace(list, " (", "(")
    safeReplace(list, "( ", "(")
    safeReplace(list, " )", ")")
    safeReplace(list, ") ", ")")
    replaceComments(list) # should follow all calls to safeReplace
    removeTrailingWs(list)
    safeReplace(list, "\t ", "\t") # happens when deleting declarations.</t>
<t tx="ekr.20061203123201.17">def convertDocList(docList):

    # print "convertDocList:", docList
    if matchWord(docList, 0, "@doc"):
        i = skipWs(docList, 4)
        if match(docList, i, "\n"):
            i += 1
        docList[0:i] = list("@ ")</t>
<t tx="ekr.20061203123201.18">def skipDocPart(list, i):
    
    # print "skipDocPart", i
    while i &lt; len(list):
        if matchWord(list, i, "@code") or matchWord(list, i, "@c"):
            break
        elif isSectionDef(list,i):
            break
        else: i = skipPastLine(list, i)
    return i</t>
<t tx="ekr.20061203123201.19">def skipCodePart(codeList, i):
    
    # print "skipCodePart", i
    if matchWord(codeList, i, "@doc") or matchWord(codeList, i, "@"):
        return i
    while i &lt; len(codeList):
        if match(codeList, i, "//"):
            i = skipPastLine(codeList,i)
        elif match(codeList, i, "/*"):
            i = skipCBlockComment(codeList,i)
        elif match(codeList, i, '"') or match(codeList, i, "'"):
            i = skipString(codeList,i)
        elif match(codeList, i, "\n"):
            i += 1
            if matchWord(codeList, i, "@doc") or matchWord(codeList, i, "@"):
                break
        else: i += 1
    return i</t>
<t tx="ekr.20061203123201.20"></t>
<t tx="ekr.20061203123201.21">def convertLeadingBlanks(list):

    global tabWidth
    if tabWidth &lt; 2: return
    i = 0
    while i &lt; len(list):
        n = 0
        while i &lt; len(list) and list[i] == ' ':
            n += 1 ; i += 1
            if n == tabWidth:
                list[i-tabWidth:i] = ['\t']
                i = i - tabWidth + 1
                n = 0
        i = skipPastLine(list, i)</t>
<t tx="ekr.20061203123201.22"># We scan for a '{' at the top level that is preceeded by ')'
# @code and &lt; &lt; x &gt; &gt; = have been replaced by @c
def mungeAllFunctions(codeList):

    prevSemi = 0 # Previous semicolon: header contains all previous text
    i = 0
    firstOpen = None
    while i &lt; len(codeList):
        if isStringOrComment(codeList,i):
            i = skipStringOrComment(codeList,i)
            prevSemi = i
        elif match(codeList, i, '('):
            if not firstOpen:
                firstOpen = i
            i += 1
        elif match(codeList, i, '#'):
            i = skipPastLine(codeList, i)
            prevSemi = i
        elif match(codeList, i, ';'):
            i += 1
            prevSemi = i
        elif matchWord(codeList, i, "@code"):
            i += 5
            prevSemi = i # restart the scan
        elif matchWord(codeList, i, "@c"):
            i += 2 ; prevSemi = i # restart the scan
        elif match(codeList, i, "{"):
            i = handlePossibleFunctionHeader(codeList,i,prevSemi,firstOpen)
            prevSemi = i ; firstOpen = None # restart the scan
        else: i += 1</t>
<t tx="ekr.20061203123201.23"># converts function header lines from c++ format to python format.
# That is, converts
# x1..nn w::y ( t1 z1,..tn zn) {
# to
# def y (z1,..zn): {

def handlePossibleFunctionHeader(codeList, i, prevSemi, firstOpen):

    assert(match(codeList,i,"{"))
    prevSemi = skipWsAndNl(codeList, prevSemi)
    close = prevNonWsOrNlChar(codeList, i)
    if close &lt; 0 or codeList[close] != ')':
        return 1 + skipToMatchingBracket(codeList, i)
    if not firstOpen:
        return 1 + skipToMatchingBracket(codeList, i)
    close2 = skipToMatchingBracket(codeList, firstOpen)
    if close2 != close:
        return 1 + skipToMatchingBracket(codeList, i)
    open = firstOpen
    assert(codeList[open]=='(')
    head = codeList[prevSemi:open]
    # do nothing if the head starts with "if", "for" or "while"
    k = skipWs(head,0)
    if k &gt;= len(head) or not head[k] in string.letters:
        return 1 + skipToMatchingBracket(codeList, i)
    kk = skipPastWord(head,k)
    if kk &gt; k:
        headString = listToString(head[k:kk])
        # C keywords that might be followed by '{'
        # print "headString:", headString
        if headString in [ "class", "do", "for", "if", "struct", "switch", "while"]:
            return 1 + skipToMatchingBracket(codeList, i)
    args = codeList[open:close+1]
    k = 1 + skipToMatchingBracket(codeList,i)
    body = codeList[i:k]
    #print "head:", listToString(head)
    #print "args:", listToString(args)
    #print "body:", listToString(body)
    #print "tot: ", listToString(codeList[prevSemi:k])
    head = massageFunctionHead(head)
    args = massageFunctionArgs(args)
    body = massageFunctionBody(body)
    #print "head2:", listToString(head)
    #print "args2:", listToString(args)
    #print "body2:", listToString(body)
    #print "tot2: ", listToString(codeList[prevSemi:k])
    result = []
    for item in head:
        result.append(item)
    for item in args:
        result.append(item)
    for item in body:
        result.append(item)
    codeList[prevSemi:k] = result
    return k</t>
<t tx="ekr.20061203123201.24">def massageFunctionArgs(args):
    global gClassName
    assert(args[0]=='(')
    assert(args[-1]==')')

    result = ['('] ; lastWord = []
    if gClassName:
        for item in list("self,"): result.append(item) #can put extra comma

    i = 1
    while i &lt; len(args):
        i = skipWsAndNl(args, i)
        c = args[i]
        if c in string.letters:
            j = skipPastWord(args,i)
            lastWord = args[i:j]
            i = j
        elif c == ',' or c == ')':
            for item in lastWord:
                result.append(item)
            if lastWord != [] and c == ',':
                result.append(',')
            lastWord = []
            i += 1
        else: i += 1
    if result[-1] == ',':
        del result[-1]
    result.append(')')
    result.append(':')
    # print "new args:", listToString(result)
    return result</t>
<t tx="ekr.20061203123201.25">def massageFunctionHead(head):

    # print "head:", listToString(head)
    result = []
    prevWord = []
    global gClassName ; gClassName = []
    i = 0
    while i &lt; len(head):
        i = skipWsAndNl(head, i)
        if i &lt; len(head) and head[i] in string.letters:
            result = []
            j = skipPastWord(head,i)
            prevWord = head[i:j]
            i = j
            # look for ::word2
            i = skipWs(head,i)
            if match(head,i,"::"):
                # Set the global to the class name.
                gClassName = listToString(prevWord)
                # print "class name:", gClassName
                i = skipWs(head, i+2)
                if i &lt; len(head) and (head[i]=='~' or head[i] in string.letters):
                    j = skipPastWord(head,i)
                    if head[i:j] == prevWord:
                        for item in list("__init__"): result.append(item)
                    elif head[i]=='~' and head[i+1:j] == prevWord:
                        for item in list("__del__"): result.append(item)
                    else:
                        # for item in "::": result.append(item)
                        for item in head[i:j]: result.append(item)
                    i = j
            else:
                for item in prevWord:result.append(item)
        else: i += 1
        
    finalResult = list("def ")
    for item in result: finalResult.append(item)
    # print "new head:", listToString(finalResult)
    return finalResult</t>
<t tx="ekr.20061203123201.26">def massageFunctionBody(body):

    body = massageIvars(body)
    body = removeCasts(body)
    body = removeTypeNames(body)
    return body</t>
<t tx="ekr.20061203123201.27">def massageIvars(body):

    if gClassName and ivarsDict.has_key(gClassName):
        ivars = ivarsDict [ gClassName ]
    else:
        ivars = []
    # print "key:ivars=", gClassName, ':', `ivars`

    i = 0
    while i &lt; len(body):
        if isStringOrComment(body,i):
            i = skipStringOrComment(body,i)
        elif body[i] in string.letters:
            j = skipPastWord(body,i)
            word = listToString(body[i:j])
            # print "looking up:", word
            if word in ivars:
                # replace word by self.word
                # print "replacing", word, " by self.", word
                word = "self." + word
                word = list(word)
                body[i:j] = word
                delta = len(word)-(j-i)
                i = j + delta
            else: i = j
        else: i += 1
    return body</t>
<t tx="ekr.20061203123201.28">def removeCasts(body):

    i = 0
    while i &lt; len(body):
        if isStringOrComment(body,i):
            i = skipStringOrComment(body,i)
        elif match(body, i, '('):
            start = i
            i = skipWs(body, i+1)
            if body[i] in string.letters:
                j = skipPastWord(body,i)
                word = listToString(body[i:j])
                i = j
                if word in classList or word in typeList:
                    i = skipWs(body, i)
                    while match(body,i,'*'):
                        i += 1
                    i = skipWs(body, i)
                    if match(body,i,')'):
                        i += 1
                        # print "removing cast:", listToString(body[start:i])
                        del body[start:i]
                        i = start
        else: i += 1
    return body</t>
<t tx="ekr.20061203123201.29"># Do _not_ remove type names when preceeded by new.

def removeTypeNames(body):

    i = 0
    while i &lt; len(body):
        if isStringOrComment(body,i):
            i = skipStringOrComment(body,i)
        elif matchWord(body, i, "new"):
            i = skipPastWord(body,i)
            i = skipWs(body,i)
            # don't remove what follows new.
            if body[i] in string.letters:
                i = skipPastWord(body,i)
        elif body[i] in string.letters:
            j = skipPastWord(body,i)
            word = listToString(body[i:j])
            if word in classList or word in typeList:
                k = skipWs(body, j)
                while match(body,k,'*'):
                    k += 1 ; j = k
                # print "Deleting type name:", listToString(body[i:j])
                del body[i:j]
            else:
                i = j
        else: i += 1
    return body</t>
<t tx="ekr.20061203123201.30"># converts if ( x ) to if x:
# converts while ( x ) to while x:
def handleAllKeywords(codeList):

    # print "handAllKeywords:", listToString(codeList)
    i = 0
    while i &lt; len(codeList):
        if isStringOrComment(codeList,i):
            i = skipStringOrComment(codeList,i)
        elif ( matchWord(codeList,i,"if") or
            matchWord(codeList,i,"while") or
            matchWord(codeList,i,"for") or
            matchWord(codeList,i,"elif") ):
            i = handleKeyword(codeList,i)
        else:
            i += 1
    # print "handAllKeywords2:", listToString(codeList)</t>
<t tx="ekr.20061203123201.31">def handleKeyword(codeList,i):

    isFor = False
    if (matchWord(codeList,i,"if")):
        i += 2
    elif (matchWord(codeList,i,"elif")):
        i += 4
    elif (matchWord(codeList,i,"while")):
        i += 5
    elif (matchWord(codeList,i,"for")):
        i += 3
        isFor = True
    else: assert(0)
    # Make sure one space follows the keyword
    k = i
    i = skipWs(codeList,i)
    if k == i:
        c = codeList[i]
        codeList[i:i+1] = [ ' ', c ]
        i += 1
    # Remove '(' and matching ')' and add a ':'
    if codeList[i] == "(":
        j = removeMatchingBrackets(codeList,i)
        if j &gt; i and j &lt; len(codeList):
            c = codeList[j]
            codeList[j:j+1] = [":", " ", c]
            j = j + 2
        return j
    return i</t>
<t tx="ekr.20061203123201.32"></t>
<t tx="ekr.20061203123201.33">def isWs(c):
    return c == ' ' or c == '\t'
    
def isWsOrNl(c):
    return c == ' ' or c == '\t' or c == '\n'</t>
<t tx="ekr.20061203123201.34"># returns the ending index if i points to &lt; &lt; x &gt; &gt; =
def isSectionDef(list, i):

    i = skipWs(list,i)
    if not match(list,i,"&lt;&lt;"): return False
    while i &lt; len(list) and list[i] != '\n':
        if match(list,i,"&gt;&gt;="): return i+3
        else: i += 1
    return False</t>
<t tx="ekr.20061203123201.35">def isStringOrComment(list, i):

    return match(list,i,"'") or match(list,i,'"') or match(list,i,"//") or match(list,i,"/*")</t>
<t tx="ekr.20061203123201.36"></t>
<t tx="ekr.20061203123201.37">def findInCode(codeList, i, findStringOrList):

    findList = stringToList(findStringOrList)
    
    while i &lt; len(codeList):
        if isStringOrComment(codeList,i):
            i = skipStringOrComment(codeList,i)
        elif match(codeList, i, findList):
            return i
        else: i += 1
    return -1</t>
<t tx="ekr.20061203123201.38">def findInList(list, i, findStringOrList):

    findList = stringToList(findStringOrList)
    
    while i &lt; len(list):
        if match(list, i, findList): return i
        else: i += 1
    return -1</t>
<t tx="ekr.20061203123201.39"># returns True if findList matches starting at codeList[i]

def match (codeList, i, findStringOrList):

    findList = stringToList(findStringOrList)
    n = len(findList)
    j = 0
    while i+j &lt; len(codeList) and j &lt; len(findList):
        if codeList[i+j] != findList[j]:
            return False
        else:
            j += 1
            if j == n:
                return i+j
    return False</t>
<t tx="ekr.20061203123201.40">def matchWord (codeList, i, findStringOrList):

    j = match(codeList,i,findStringOrList)
    if not j:
        return False
    elif j &gt;= len(codeList):
        return True
    else:
        c = codeList[j]
        return not (c in string.letters or c in string.digits or c == '_')</t>
<t tx="ekr.20061203123201.41"></t>
<t tx="ekr.20061203123201.42">def removeAllCComments(list, delim):

    i = 0
    while i &lt; len(list):
        if match(list,i,"'") or match(list,i,'"'):
            i = skipString(list,i)
        elif match(list,i,"//"):
            j = skipPastLine(list,i)
            print "deleting single line comment:", listToString(list[i:j])
            del list[i:j]
        elif match(list,i,"/*"):
            j = skipCBlockComment(list,i)
            print "deleting block comment:", listToString(list[i:j])
            del list[i:j]
        else:
            i += 1</t>
<t tx="ekr.20061203123201.43">def removeAllCSentinels(list, delim):

    i = 0
    while i &lt; len(list):
        if match(list,i,"'") or match(list,i,'"'):
            # string starts a line.
            i = skipString(list,i)
            i = skipPastLine(list,i)
        elif match(list,i,"/*"):
            # block comment starts a line
            i = skipCBlockComment(list,i)
            i = skipPastLine(line,i)
        elif match(list,i,"//@"):
            j = skipPastLine(list,i)
            print "deleting sentinel:", listToString(list[i:j])
            del list[i:j]
        else:
            i = skipPastLine(list,i)</t>
<t tx="ekr.20061203123201.44">def removeAllPythonComments(list, delim):

    i = 0
    while i &lt; len(list):
        if match(list,i,"'") or match(list,i,'"'):
            i = skipString(list,i)
        elif match(list,i,"#"):
            j = skipPastLine(list,i)
            print "deleting comment:", listToString(list[i:j])
            del list[i:j]
        else:
            i += 1</t>
<t tx="ekr.20061203123201.45">def removeAllPythonSentinels(list, delim):

    i = 0
    while i &lt; len(list):
        if match(list,i,"'") or match(list,i,'"'):
            # string starts a line.
            i = skipString(list,i)
            i = skipPastLine(list,i)
        elif match(list,i,"#@"):
            j = skipPastLine(list,i)
            print "deleting sentinel:", listToString(list[i:j])
            del list[i:j]
        else:
            i = skipPastLine(list,i)</t>
<t tx="ekr.20061203123201.46">def removeAtRoot (codeList):

    i = skipWs(codeList, 0)
    if matchWord(codeList,i,"@root"):
        j = skipPastLine(codeList,i)
        del codeList[i:j]

    while i &lt; len(codeList):
        if isStringOrComment(codeList,i):
            i = skipStringOrComment(codeList,i)
        elif match(codeList,i,"\n"):
            i = skipWs(codeList, i+1)
            if matchWord (codeList,i,"@root"):
                j = skipPastLine(codeList,i)
                del codeList[i:j]
        else: i += 1
</t>
<t tx="ekr.20061203123201.47">def removeBlankLines(codeList):

    i = 0
    while i &lt; len(codeList):
        j = i
        while j &lt; len(codeList) and (codeList[j]==" " or codeList[j]=="\t"):
            j += 1
        if j== len(codeList) or codeList[j] == '\n':
            del codeList[i:j+1]
        else:
            oldi = i
            i = skipPastLine(codeList,i)</t>
<t tx="ekr.20061203123201.48">def removeExcessWs(codeList):

    i = 0
    i = removeExcessWsFromLine(codeList,i)
    while i &lt; len(codeList):
        if isStringOrComment(codeList,i):
            i = skipStringOrComment(codeList,i)
        elif match(codeList,i,'\n'):
            i += 1
            i = removeExcessWsFromLine(codeList,i)
        else: i += 1</t>
<t tx="ekr.20061203123201.49">def removeExcessWsFromLine(codeList,i):

    assert(i==0 or codeList[i-1] == '\n')
    i = skipWs(codeList,i)
    while i &lt; len(codeList):
        if isStringOrComment(codeList,i): break # safe
        elif match(codeList, i, '\n'): break
        elif match(codeList, i, ' ') or match(codeList, i, '\t'):
            # Replace all whitespace by one blank.
            k = i
            i = skipWs(codeList,i)
            codeList[k:i] = [' ']
            i = k + 1 # make sure we don't go past a newline!
        else: i += 1
    return i</t>
<t tx="ekr.20061203123201.50">def removeLeadingAtCode(codeList):

    i = skipWsAndNl(codeList,0)
    if matchWord(codeList,i,"@code"):
        i = skipWsAndNl(codeList,5)
        del codeList[0:i]
    elif matchWord(codeList,i,"@c"):
        i = skipWsAndNl(codeList,2)
        del codeList[0:i]</t>
<t tx="ekr.20061203123201.51">def removeMatchingBrackets(codeList, i):

    j = skipToMatchingBracket(codeList, i)
    if j &gt; i and j &lt; len(codeList):
        # print "del brackets:", listToString(codeList[i:j+1])
        c = codeList[j]
        if c == ')' or c == ']' or c == '}':
            del codeList[j:j+1]
            del codeList[i:i+1]
            # print "returning:", listToString(codeList[i:j])
            return j - 1
        else: return j + 1
    else: return j</t>
<t tx="ekr.20061203123201.52">def removeSemicolonsAtEndOfLines(list):

    i = 0
    while i &lt; len(list):
        if isStringOrComment(list,i):
            i = skipStringOrComment(list,i)
        elif list[i] == ';':
            j = skipWs(list,i+1)
            if j &gt;= len(list) or match(list,j,'\n') or match(list,j,'#') or match(list,j,"//"):
                del list[i]
            else: i += 1
        else: i += 1</t>
<t tx="ekr.20061203123201.53">def removeTrailingWs(list):

    i = 0
    while i &lt; len(list):
        if isWs(list[i]):
            j = i
            i = skipWs(list,i)
            assert(j &lt; i)
            if i &gt;= len(list) or list[i] == '\n':
                # print "removing trailing ws:", `i-j`
                del list[j:i]
                i = j
        else: i += 1</t>
<t tx="ekr.20061203123201.54"></t>
<t tx="ekr.20061203123201.55"># Replaces all occurances of findString by changeString.
# Deletes all occurances if change is None
def replace(codeList, findString, changeString):

    if len(findString)==0: return
    findList = stringToList(findString)
    changeList = stringToList(changeString)

    i = 0
    while i &lt; len(codeList):
        if match(codeList, i, findList):
            codeList[i:i+len(findList)] = changeList
            i += len(changeList)
        else: i += 1</t>
<t tx="ekr.20061203123201.56"># For Leo we expect few block comments; doc parts are much more common.

def replaceComments(codeList):

    i = 0
    if match(codeList, i, "//"):
        codeList[0:2] = ['#']
    while i &lt; len(codeList):
        if match(codeList, i, "//"):
            codeList[i:i+2] = ['#']
            i = skipPastLine(codeList,i)
        elif match(codeList, i, "/*"):
            j = skipCBlockComment(codeList,i)
            del codeList[j-2:j]
            codeList[i:i+2] = ['#']
            j -= 2 ; k = i ; delta = -1
            while k &lt; j + delta :
                if codeList[k]=='\n':
                    codeList[k:k+1] = ['\n', '#', ' ']
                    delta += 2 ; k += 3 # progress!
                else: k += 1
            i = j + delta
        elif match(codeList, i, '"') or match(codeList, i, "'"):
            i = skipString(codeList,i)
        else: i += 1</t>
<t tx="ekr.20061203123201.57"># Replaces &lt; &lt; x &gt; &gt; = by @c (at the start of lines).
def replaceSectionDefs(codeList):

    i = 0
    j = isSectionDef(codeList,i)
    if j &gt; 0: codeList[i:j] = list("@c ")

    while i &lt; len(codeList):
        if isStringOrComment(codeList,i):
            i = skipStringOrComment(codeList,i)
        elif match(codeList,i,"\n"):
            i += 1
            j = isSectionDef(codeList,i)
            if j &gt; i: codeList[i:j] = list("@c ")
        else: i += 1</t>
<t tx="ekr.20061203123201.58"># Replaces occurances of findString by changeString outside of C comments and strings.
# Deletes all occurances if change is None.
def safeReplace(codeList, findString, changeString):

    if len(findString)==0: return
    findList = stringToList(findString)
    changeList = stringToList(changeString)
    i = 0
    if findList[0] in string.letters: #use matchWord
        while i &lt; len(codeList):
            if isStringOrComment(codeList,i):
                i = skipStringOrComment(codeList,i)
            elif matchWord(codeList, i, findList):
                codeList[i:i+len(findList)] = changeList
                i += len(changeList)
            else: i += 1
    else: #use match
        while i &lt; len(codeList):
            if match(codeList, i, findList):
                codeList[i:i+len(findList)] = changeList
                i += len(changeList)
            else: i += 1</t>
<t tx="ekr.20061203123201.59"></t>
<t tx="ekr.20061203123201.60">def prevNonWsChar(list, i):

    i -= 1
    while i &gt;= 0 and isWs(list[i]):
        i -= 1
    return i

def prevNonWsOrNlChar(list, i):

    i -= 1
    while i &gt;= 0 and isWsOrNl(list[i]):
        i -= 1
    return i</t>
<t tx="ekr.20061203123201.61">def skipCBlockComment(codeList, i):

    assert(match(codeList, i, "/*"))
    i += 2

    while i &lt; len(codeList):
        if match(codeList, i, "*/"): return i + 2
        else: i += 1
    return i</t>
<t tx="ekr.20061203123201.62">def skipPastLine(codeList, i):

    while i &lt; len(codeList) and codeList[i] != '\n':
        i += 1
    if i &lt; len(codeList) and codeList[i] == '\n':
        i += 1
    return i</t>
<t tx="ekr.20061203123201.63">def skipPastWord(list, i):

    assert(list[i] in string.letters or list[i]=='~')
    
    # Kludge: this helps recognize dtors.
    if list[i]=='~':
        i += 1
    
    while i &lt; len(list) and (
        list[i] in string.letters or
        list[i] in string.digits or
        list[i]=='_'):
        i += 1
    return i</t>
<t tx="ekr.20061203123201.64">def skipString(codeList, i):

    delim = codeList[i] # handle either single or double-quoted strings
    assert(delim == '"' or delim == "'")
    i += 1

    while i &lt; len(codeList):
        if codeList[i] == delim: return i + 1
        elif codeList[i] == '\\': i += 2
        else: i += 1
    return i</t>
<t tx="ekr.20061203123201.65">def skipStringOrComment(list,i):

    if match(list,i,"'") or match(list,i,'"'):
        return skipString(list,i)
    if match(list, i, "//"):
        return skipPastLine(list,i)
    elif match(list, i, "/*"):
        return skipCBlockComment(list,i)
    else: assert(0)</t>
<t tx="ekr.20061203123201.66">def skipToMatchingBracket(codeList, i):

    c = codeList[i]
    if   c == '(': delim = ')'
    elif c == '{': delim = '}'
    elif c == '[': delim = ']'
    else: assert(0)

    i += 1
    while i &lt; len(codeList):
        c = codeList[i]
        if isStringOrComment(codeList,i):
            i = skipStringOrComment(codeList,i)
        elif c == delim:
            return i
        elif c == '(' or c == '[' or c == '{':
            i = skipToMatchingBracket(codeList,i)
            i += 1 # skip the closing bracket.
        else: i += 1
    return i</t>
<t tx="ekr.20061203123201.67">def skipWs(list, i):

    while i &lt; len(list):
        c = list[i]
        if c == ' ' or c == '\t':
            i += 1
        else: break
    return i
    
def skipWsAndNl(list, i):

    while i &lt; len(list):
        c = list[i]
        if c == ' ' or c == '\t' or c == '\n':
            i += 1
        else: break
    return i</t>
<t tx="ekr.20061203123201.68"></t>
<t tx="ekr.20061203123201.69"># converts a string to a list containing one item per character of the list.
# converts None to the empty string and leaves other types alone.

# list(string) does not work on none.
def stringToList(string):

    if string:
        return list(string)
    else:
        return []</t>
<t tx="ekr.20061203123201.70">def listToString(list):

    return string.join(list,"")</t>
<t tx="ekr.20061203123249"># py2cpp: translate python code to C++ code.
# Works on body of `if __py2cpp__` trees.

@others

controller = controllerClass(c,p)
s = controller.findCode()
if s:
    tokens = controller.tokenize(s)
    tree   = controller.parse(tokens)
    code   = controller.gen(tree)
    controller.put(code)
</t>
<t tx="ekr.20061203131351">class controllerClass:
    
    @others</t>
<t tx="ekr.20061203131351.1">def __init__ (self,c,p):
    
    self.c = c
    self.p = p
</t>
<t tx="ekr.20061203131351.2">def findCode (self):
    
    g.trace()
    return 'test'</t>
<t tx="ekr.20061203131351.3">def parse (self,tokens):
    
    g.trace()</t>
<t tx="ekr.20061203131351.4">def gen (self,tree):
    
    g.trace()</t>
<t tx="ekr.20061203131351.5">def put (self,output):
    
    g.trace()</t>
<t tx="ekr.20061203131636">def tokenize (self,s):
    
    g.trace(repr(s))</t>
</tnodes>
</leo_file>
