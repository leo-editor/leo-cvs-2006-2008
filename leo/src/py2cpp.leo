<?xml version="1.0" encoding="utf-8"?>
<?xml-stylesheet ekr_test?>
<leo_file>
<leo_header file_format="2" tnodes="0" max_tnode_index="0" clone_windows="0"/>
<globals body_outline_ratio="0.5">
	<global_window_position top="12" left="473" height="927" width="783"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="ekr.20061203113554"><vh>Docs</vh>
<v t="ekr.20061204080441"><vh>Posting1: py2cpp</vh>
<v t="ekr.20061203114036"><vh>Intro</vh></v>
<v t="ekr.20061203114036.1"><vh>Separating translated code</vh></v>
<v t="ekr.20061203114036.2"><vh>Type annotations</vh></v>
<v t="ekr.20061203114036.3"><vh>Lifetimes</vh></v>
<v t="ekr.20061203114036.4"><vh>py2cpp assertions</vh></v>
<v t="ekr.20061203114036.5"><vh>Exceptions</vh></v>
<v t="ekr.20061203114036.6"><vh>Conclusions</vh></v>
</v>
<v t="ekr.20061204080441.1"><vh>ShedSkin speedup</vh></v>
<v t="ekr.20061204080441.2"><vh>Posting 2: Inside the bubble</vh></v>
<v t="ekr.20061204150444"><vh>Minimal overhead to cross the bubble</vh></v>
<v t="ekr.20061204151040"><vh>@url http://docs.python.org/ext/intro.html  (start of discussion about extending)</vh></v>
<v t="ekr.20061204163347"><vh>@url http://docs.python.org/ext/refcounts.html</vh></v>
<v t="ekr.20061204163347.1"><vh>Allocating objects dynamically</vh></v>
<v t="ekr.20061204163347.2"><vh>Minimal type</vh></v>
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
<v t="ekr.20061204183830"><vh>pypy compiler (reference)</vh></v>
<v t="ekr.20061204183908"><vh>Recursive import script</vh>
<v t="ekr.20061204183908.1"><vh>importFiles</vh></v>
<v t="ekr.20061204183908.2"><vh>importDir</vh></v>
<v t="ekr.20061204183908.3"><vh>createLastChildOf</vh></v>
</v>
<v t="ekr.20061203123249"><vh>@button py2cpp</vh>
<v t="ekr.20061203131351"><vh>class controllerClass</vh>
<v t="ekr.20061203131351.1"><vh>ctor</vh></v>
<v t="ekr.20061203131351.2"><vh>findCode</vh></v>
<v t="ekr.20061203131636"><vh>tokenize</vh></v>
<v t="ekr.20061203131351.3"><vh>parse</vh></v>
<v t="ekr.20061203131351.4"><vh>gen</vh></v>
<v t="ekr.20061203131351.5"><vh>put</vh></v>
</v>
</v>
<v t="ekr.20061205062741"><vh>@@button insert nodes</vh>
<v t="ekr.20061205064845"><vh>&lt;&lt; define s &gt;&gt;</vh></v>
<v t="ekr.20061205064845.1"><vh>mungeBody</vh></v>
</v>
<v t="ekr.20061204195153" a="V"><vh>@button ast</vh>
<v t="ekr.20061204195419" a="E"><vh>class ASTVisitor</vh>
<v t="ekr.20061204195419.2"><vh>__init__</vh></v>
<v t="ekr.20061205073149"><vh>push &amp; pop</vh></v>
<v t="ekr.20061204211633"><vh>trace</vh></v>
<v t="ekr.20061204205000"><vh>visitAdd</vh></v>
<v t="ekr.20061204205000.1"><vh>visitAnd</vh></v>
<v t="ekr.20061204205000.2"><vh>visitAssAttr</vh></v>
<v t="ekr.20061204205628.1"><vh>visitAssert</vh></v>
<v t="ekr.20061204205628.2"><vh>visitAssign</vh></v>
<v t="ekr.20061204205000.3"><vh>visitAssList</vh></v>
<v t="ekr.20061204205000.4"><vh>visitAssName</vh></v>
<v t="ekr.20061204205628"><vh>visitAssTuple</vh></v>
<v t="ekr.20061204205628.3"><vh>visitAugAssign</vh></v>
<v t="ekr.20061204205628.4"><vh>visitBackquote</vh></v>
<v t="ekr.20061204205628.5"><vh>visitBitand/or/xor</vh></v>
<v t="ekr.20061204205628.6"><vh>visitBreak</vh></v>
<v t="ekr.20061204205628.8"><vh>visitClass</vh></v>
<v t="ekr.20061204205628.7"><vh>visitCallFunc</vh></v>
<v t="ekr.20061204205628.9"><vh>visitCompare</vh></v>
<v t="ekr.20061204205628.10"><vh>visitConst</vh></v>
<v t="ekr.20061204205628.11"><vh>visitContinue</vh></v>
<v t="ekr.20061204214019.1"><vh>visitDecorators</vh></v>
<v t="ekr.20061205062426"><vh>visitDict</vh></v>
<v t="ekr.20061205062426.1"><vh>visitDiscard</vh></v>
<v t="ekr.20061205065240"><vh>visitDiv</vh></v>
<v t="ekr.20061205065240.1"><vh>visitEllipsis</vh></v>
<v t="ekr.20061205065240.2"><vh>visitExec</vh></v>
<v t="ekr.20061204211034"><vh>visitExpression</vh></v>
<v t="ekr.20061205065240.3"><vh>visitFloorDiv</vh></v>
<v t="ekr.20061204211034.1"><vh>visitFor</vh></v>
<v t="ekr.20061205065240.4"><vh>visitFrom</vh></v>
<v t="ekr.20061204203241.1"><vh>visitFunction</vh></v>
<v t="ekr.20061204213730.3"><vh>visitGenExpr</vh></v>
<v t="ekr.20061204213730.4"><vh>visitGenExprFor</vh></v>
<v t="ekr.20061204213730"><vh>visitGenExprIf</vh></v>
<v t="ekr.20061204213730.1"><vh>visitGenExprInner</vh></v>
<v t="ekr.20061204213730.2"><vh>visitGetattr</vh></v>
<v t="ekr.20061205065240.5"><vh>visitGlobal</vh></v>
<v t="ekr.20061204214019"><vh>visitIf</vh></v>
<v t="ekr.20061205065240.6"><vh>visitImport</vh></v>
<v t="ekr.20061205065240.7"><vh>visitInvert</vh></v>
<v t="ekr.20061205065240.8"><vh>visitKeyword</vh></v>
<v t="ekr.20061205065240.9"><vh>visitLambda</vh></v>
<v t="ekr.20061205065240.10"><vh>visitLeftShift</vh></v>
<v t="ekr.20061205065240.11"><vh>visitList</vh></v>
<v t="ekr.20061205065240.12"><vh>visitListComp</vh></v>
<v t="ekr.20061205065240.13"><vh>visitListCompFor</vh></v>
<v t="ekr.20061205065240.14"><vh>visitListCompIf</vh></v>
<v t="ekr.20061205065240.15"><vh>visitMod</vh></v>
<v t="ekr.20061205065240.16"><vh>visitModule</vh></v>
<v t="ekr.20061205065240.17"><vh>visitMul</vh></v>
<v t="ekr.20061205065240.18"><vh>visitName</vh></v>
<v t="ekr.20061205065240.19"><vh>visitNot</vh></v>
<v t="ekr.20061205065240.20"><vh>visitOr</vh></v>
<v t="ekr.20061205065240.21"><vh>visitPass</vh></v>
<v t="ekr.20061205065240.22"><vh>visitPower</vh></v>
<v t="ekr.20061205065240.23"><vh>visitPrint</vh></v>
<v t="ekr.20061205065240.24"><vh>visitPrintnl</vh></v>
<v t="ekr.20061205065240.25"><vh>visitRaise</vh></v>
<v t="ekr.20061204205000.5"><vh>visitReturn</vh></v>
<v t="ekr.20061205065240.26"><vh>visitRightShift</vh></v>
<v t="ekr.20061205065240.27"><vh>visitSlice</vh></v>
<v t="ekr.20061205065240.28"><vh>visitSliceobj</vh></v>
<v t="ekr.20061204202104"><vh>visitStmt</vh></v>
<v t="ekr.20061205065240.30"><vh>visitSub</vh></v>
<v t="ekr.20061205065240.31"><vh>visitSubscript</vh></v>
<v t="ekr.20061205065240.32"><vh>visitTryExcept</vh></v>
<v t="ekr.20061205065240.33"><vh>visitTryFinally</vh></v>
<v t="ekr.20061205065240.34"><vh>visitTuple</vh></v>
<v t="ekr.20061205065240.35"><vh>visitUnaryAdd</vh></v>
<v t="ekr.20061205065240.36"><vh>visitUnarySub</vh></v>
<v t="ekr.20061205065240.37"><vh>visitWhile</vh></v>
<v t="ekr.20061205065240.38"><vh>visitWith</vh></v>
</v>
</v>
<v t="ekr.20061204214019"><vh>visitIf</vh></v>
<v t="ekr.20061204205628.7"><vh>visitCallFunc</vh></v>
<v t="ekr.20061204211034.1"><vh>visitFor</vh></v>
<v t="ekr.20061204205628.9"><vh>visitCompare</vh></v>
<v t="ekr.20061204202104"><vh>visitStmt</vh></v>
<v t="ekr.20061204205628.2"><vh>visitAssign</vh></v>
<v t="ekr.20061204205628.8"><vh>visitClass</vh></v>
<v t="ekr.20061204203241.1"><vh>visitFunction</vh></v>
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
<t tx="ekr.20061204080441"></t>
<t tx="ekr.20061204080441.1">"The run-time performance of the generated code for our benchmarks typically
outperforms Psycho...by a factor of 2-40. The average speedups over Psycho and
[CPython] are about 12 and 45, respectively."
</t>
<t tx="ekr.20061204080441.2">py2cpp last thoughts for now

The problem for me with compiler projects isn't just that they are hard, it's
that they tend to become all-consuming :-) In order to get on with Leo I shall
try to wrap up my present thoughts here.

If nothing else, the ShedSkin project shows that huge performance gains are
possible over psyco. This is an important result. The question is, are these
gains available when only part of the code is optimized? I believe the answer is
yes.

The Aha is to consider the boundary between optimized (C++) and python code. Let
us say that optimized code is **inside the bubble** and that regular Python code
is **outside the bubble**. The aha is this: **It is only at the bubble's
boundary that inefficiencies occur that are related to code inside the bubble.**
In other words, the more that executed code can stay inside the bubble, the more
efficient the code will be.

For example, all of Python's library code that implemented in C/C++ is inside a
bubble. This is a major reason why Python is so fast. We expect long-running
calls to Python's library to be very efficient, *provided* that the code in the
bubble doesn't make calls to code outside the bubble. For example, Python's xml
and dom libraries ought to give essentially optimal performance because all of
their code is (or could be, I don't know for sure) inside the bubble.

For py2cpp, keeping optimized code inside the bubble is absolutely crucial.
Consider, for example, the main read loop. This code **looks** like
transliterated C++ code, but appearances can be deceiving: it contains many
references to vnode and tnode ivars. If those references cross the bubble, most
performance gains will disappear. The problem is this: most of Leo's code that
references vnodes is *outside* the bubble (outside the code to be optimized). I
definitely will not consider any solution that moves a substantial part of Leo's
code inside the bubble: the bubble must contain only bottleneck code. So how can
we retain compatibility with code outside the bubble while making the code
inside the bubble fast?

At first I thought this was a show-stopper. Happily, I think the answer is
simple. The optimized code inside the bubble must provide two means of access:
the 'official' module-method table way (see
http://docs.python.org/ext/methodTable.html) for code outside the bubble, and a
**direct access** way for code inside the bubble. To make this work, all of the
code inside the bubble must be **in the same code space**, i.e., in a single
.cpp file. This eliminates all linking issues, though it does create some
namespace issues. These namespace issues are easily solved using prefixes
because all such prefixes are generated by code, i.e., by py2cpp.

So outside the bubble, an assignment like t = v.t results (as usual) in
something like 10-50 machine-language instructions in the interpreter and in
calls to __getattr__, and maybe even an indirection via the method table. Inside
the bubble, this should result in a single C statement, something like var_t =
var_v -&gt; vnode_ivar_t_offset. This assumes that leoNodes.py is inside the
bubble, which I think is essential.

So there it all is. py2cpp's code generators will emit dual-access code. They
will generate one or more module-method tables, that lead to 'official' module
code. They will also allow access (somehow) to equivalent, highly-optimized,
code for use only within the bubble. In this sense the 'bubble' becomes the unit
of global optimization, but in practice this optimization should be easy to do.
If ShedSkin can do it, py2cpp should be able to do it. py2cpp must generate
calls to Python's C-API as usual for all code outside the bubble. It will be up
to the programmer (me) to ensure that such calls do not exist inside
time-critical code. I believe this is feasible in the code I want to optimize.

In some ways all this is a hack. But a hack is all that is required for the code
that I want to optimize. Furthermore, the hack is made possible by Leo's coding
conventions, and I am willing to revise Leo's code as needed (mind you: only
within the optimized code) to follow those coding conventions. Naturally, pypy
has a much harder problem to solve, but that's their problem :-)

Edward

P.S. I forgot to mention that the only way to use lifetime-based storage
allocation is to move the vnode and tnode classes inside the bubble.

EKR
</t>
<t tx="ekr.20061204150444">@color
@language c

static PyObject *
spam_system(PyObject *self, PyObject *args)
{
    const char *command; int sts;
    if (!PyArg_ParseTuple(args, "s", &amp;command)) return NULL;
    sts = system(command);
    return Py_BuildValue("i", sts);
}

static PyMethodDef SpamMethods[] = {

    {"system",  spam_system, METH_VARARGS,"Execute a shell command."},
    {NULL, NULL, 0, NULL} // Sentinel
};

// Python calls initspam when importing module spam for the first time.
// The init function should be the only non-static item defined in the module file.
PyMODINIT_FUNC
initspam(void)
{
    (void) Py_InitModule("spam", SpamMethods);
}

@
The self argument is only used when the C function implements a built-in method,
not a function. In the example, self will always be a NULL pointer, since we are
defining a function, not a method. (This is done so that the interpreter doesn't
have to understand two different types of C functions.)

The args argument will be a pointer to a Python tuple object containing the
arguments. Each item of the tuple corresponds to an argument in the call's
argument list. The arguments are Python objects -- in order to do anything with
them in our C function we have to convert them to C values. The function
PyArg_ParseTuple() in the Python API checks the argument types and converts them
to C values. It uses a template string to determine the required types of the
arguments as well as the types of the C variables into which to store the
converted values. More about this later.

PyArg_ParseTuple() returns true (nonzero) if all arguments have the right type
and its components have been stored in the variables whose addresses are passed.
It returns false (zero) if an invalid argument list was passed. In the latter
case it also raises an appropriate exception so the calling function can return
NULL immediately (as we saw in the example).</t>
<t tx="ekr.20061204151040"></t>
<t tx="ekr.20061204163347"></t>
<t tx="ekr.20061204163347.1">@
Nobody ``owns'' an object; however, you can own a reference to an object. 

For lifetimes, we simple need to create a permanent reference to the object to ensure it is never deallocated.</t>
<t tx="ekr.20061204163347.2">@color
@language c

#include &lt;Python.h&gt;
#include "structmember.h"

typedef struct {
    PyObject_HEAD
    PyObject *first; /* first name */
    PyObject *last;  /* last name */
    int number;
} Noddy;

static void
Noddy_dealloc(Noddy* self)
{
    Py_XDECREF(self-&gt;first);
    Py_XDECREF(self-&gt;last);
    self-&gt;ob_type-&gt;tp_free((PyObject*)self);
}

static PyObject *
Noddy_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    Noddy *self;
    self = (Noddy *)type-&gt;tp_alloc(type, 0);
    if (self != NULL) {
        self-&gt;first = PyString_FromString("");
        if (self-&gt;first == NULL){ Py_DECREF(self); return NULL; }
        self-&gt;last = PyString_FromString("");
        if (self-&gt;last == NULL) { Py_DECREF(self); return NULL; }
        self-&gt;number = 0;
    }
    return (PyObject *)self;
}

static int
Noddy_init(Noddy *self, PyObject *args, PyObject *kwds)
{
    PyObject *first=NULL, *last=NULL, *tmp;
    static char *kwlist[] = {"first", "last", "number", NULL};
    if (! PyArg_ParseTupleAndKeywords(args, kwds, "|OOi", kwlist, &amp;first, &amp;last, &amp;self-&gt;number))
        return -1;
    if (first) {
        tmp = self-&gt;first;   Py_INCREF(first);
        self-&gt;first = first; Py_XDECREF(tmp);
    }
    if (last) {
        tmp = self-&gt;last;  Py_INCREF(last);
        self-&gt;last = last; Py_XDECREF(tmp);
    }
    return 0;
}

//// Make ivars visible.
// Could we use thunks here?  
static PyMemberDef Noddy_members[] = {
    {"first",  T_OBJECT_EX, offsetof(Noddy, first), 0,"first name"},
    {"last",   T_OBJECT_EX, offsetof(Noddy, last),  0,"last name"},
    {"number", T_INT, offsetof(Noddy, number),      0,"noddy number"},
    {NULL}  /* Sentinel */
};

static PyObject *
Noddy_name(Noddy* self)
{
    static PyObject *format = NULL;
    PyObject *args, *result;
    if (format == NULL) {
        format = PyString_FromString("%s %s");
        if (format == NULL) return NULL;}
    if (self-&gt;first == NULL) { PyErr_SetString(PyExc_AttributeError, "first"); return NULL;}
    if (self-&gt;last  == NULL) { PyErr_SetString(PyExc_AttributeError, "last");  return NULL;}
    args = Py_BuildValue("OO", self-&gt;first, self-&gt;last);
    if (args == NULL) return NULL;
    result = PyString_Format(format, args);
    Py_DECREF(args);
    return result;
}

static PyMethodDef Noddy_methods[] = {
    {"name", (PyCFunction)Noddy_name, METH_NOARGS,"Return the name"},
    {NULL}  /* Sentinel */
};

static PyTypeObject NoddyType = {
    PyObject_HEAD_INIT(NULL)
    0,                         /*ob_size: vestigial: should always be 0.*/
    "noddy.Noddy",             /*tp_name*/
    sizeof(Noddy),             /*tp_basicsize*/
    0,                         /*tp_itemsize*/
    (destructor)Noddy_dealloc, /*tp_dealloc*/
    0,                         /*tp_print*/
    0,                         /*tp_getattr*/
    0,                         /*tp_setattr*/
    0,                         /*tp_compare*/
    0,                         /*tp_repr*/
    0,                         /*tp_as_number*/
    0,                         /*tp_as_sequence*/
    0,                         /*tp_as_mapping*/
    0,                         /*tp_hash */
    0,                         /*tp_call*/
    0,                         /*tp_str*/
    0,                         /*tp_getattro*/
    0,                         /*tp_setattro*/
    0,                         /*tp_as_buffer*/
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE, /*tp_flags*/
    "Noddy objects",           /* tp_doc */
    0,		               /* tp_traverse */
    0,		               /* tp_clear */
    0,		               /* tp_richcompare */
    0,		               /* tp_weaklistoffset */
    0,		               /* tp_iter */
    0,		               /* tp_iternext */
    Noddy_methods,             /* tp_methods */
    Noddy_members,             /* tp_members */
    0,                         /* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    (initproc)Noddy_init,      /* tp_init */
    0,                         /* tp_alloc */
    Noddy_new,                 /* tp_new */
};

static PyMethodDef module_methods[] = {
    {NULL}  /* Sentinel */
};

#ifndef PyMODINIT_FUNC	/* declarations for DLL import/export */
#define PyMODINIT_FUNC void
#endif
PyMODINIT_FUNC
initnoddy2(void) 
{
    PyObject* m;
    if (PyType_Ready(&amp;NoddyType) &lt; 0) return;
    m = Py_InitModule3("noddy2", module_methods,"Example module that creates an extension type.");
    if (m == NULL) return;
    Py_INCREF(&amp;NoddyType);
    PyModule_AddObject(m, "Noddy", (PyObject *)&amp;NoddyType);
}
</t>
<t tx="ekr.20061204183830"></t>
<t tx="ekr.20061204183908"># An example of running this script:

@others

types = (".py",) #,".c",".html",".txt")

dir = "c:/Zope-2.6.2-src/lib/python"
dir = "c:/Zope-2.6.2-src/lib/Components"

importFiles(dir,types,recursive=True)

g.es("done",color="blue")
</t>
<t tx="ekr.20061204183908.1">def importFiles (dir,type=None,kind="@file",recursive=False):
    
    v = c.currentVnode()

    # Check the params.
    if kind != "@file" and kind != "@root":
        g.es("kind must be @file or @root: " + kind)
        return

    if not g.os_path_exists(dir):
        g.es("directory does not exist: " + dir)
        return
    
    c.beginUpdate()
    try:
        root = createLastChildOf(v,"imported files")
        try:
            importDir (dir,type,kind,recursive,root)
            root.contract()
        except:
            g.es_exception()
    finally:
        c.endUpdate()</t>
<t tx="ekr.20061204183908.2">def importDir (dir,types,kind,recursive,root):

    g.es("dir: " + dir,color="blue")
    
    try:
        files = os.listdir(dir)
        files2 = [] ; dirs =[]
        for f in files:
            path = g.os_path_join(dir,f)
            if g.os_path_isfile(path):
                name, ext = g.os_path_splitext(f)
                if not types or ext in types:
                    files2.append(path)
            elif recursive:
                dirs.append(path)
        if len(files2) &gt; 0 or len(dirs) &gt; 0:
            child = createLastChildOf(root,dir)
            c.selectVnode(child)
        if len(files2) &gt; 0:
            c.importCommands.importFilesCommand(files2,kind)
        if len(dirs) &gt; 0:
            dirs.sort()
            for dir in dirs:
                importDir(dir,types,kind,recursive,child)
    except:
        g.es("exception in importFiles script")
        g.es_exception()
</t>
<t tx="ekr.20061204183908.3">def createLastChildOf (v,headline):
    
    child = v.insertAsLastChild()
    child.initHeadString(headline)
    return child
</t>
<t tx="ekr.20061204195153">import compiler

@others

s = '''
class aClass:
    def spam(a):
        b = 2
        for i in xrange(0,2):
            a = 2+3
        return 'eggs' #comment
a = aClass()
b = a.spam(2)
if b == 4:
    c = 1
elif 6 &lt; b2 &gt; 4:
    c = 2
else:
    pass
'''

print '-' * 20
ast = compiler.parse(s)

# print 'ast',ast
visitor = ASTVisitor(verbose=3)
compiler.walk(ast,visitor,verbose=3) 
</t>
<t tx="ekr.20061204195419">class ASTVisitor:

	@others
</t>
<t tx="ekr.20061204195419.2">def __init__(self,verbose):

    self.node = None
    self.verbose = verbose
    self.classStack = []
    self.defStack = []
    self.stack = []
    self.indent = ''
</t>
<t tx="ekr.20061204202104">def visitStmt (self,node):

    self.push()

    result = []
    for z in node.nodes:
        s = self.visit(z) or '&lt;Stmt:Node:None&gt;'
        result.append(s)

    self.pop()
    
    result = [z.rstrip()+'\n' for z in result ]
    
    theStmt = ''.join(result) or '&lt;Stmt: None&gt;'
    
    # print 'Stmt',repr(theStmt)

    if not self.classStack and not self.defStack and not self.stack:
        print theStmt # Emit the module-level statement.
    
    return theStmt</t>
<t tx="ekr.20061204203241.1">def visitFunction(self,node):
    
    # self.trace(node.name)
        # 'decorators',node.decorators,
        # 'name',node.name,
        # 'argnames',node.argnames,
        # 'defaults',node.defaults,
        # 'flags',node.flags,
        # 'doc',node.doc,
        # 'code',node.code,
        
    self.push()
    self.defStack.append(node.name)

    result = []
    for z in node.code:
        s = self.visit(z)
        result.append(s)

    name = self.defStack.pop()
    assert name == node.name,'visitFunction: expected %s, got %s' % (node.name,name)
    self.pop()
    
    result = [z for z in result if z is not None]
    result = '\n'.join(result) or '&lt;Func:None&gt;'
    theFunc = '%sdef %s:\n%s' % (self.indent,node.name,result)
    if not self.classStack:
        print theFunc
    return theFunc</t>
<t tx="ekr.20061204205000">def visitAdd (self,node):

    # self.trace() # left/right operands
    self.push()
    rt = self.visit(node.right) or '&lt;None&gt;'
    lt = self.visit(node.right) or '&lt;None&gt;'
    self.pop()
    return '%s + %s' % (lt,rt)
</t>
<t tx="ekr.20061204205000.1">def visitAnd (node):

    self.trace()
    for z in node.nodes:
        self.visit(z)

</t>
<t tx="ekr.20061204205000.2">def visitAssAttr(self,node):  #attribute as target of assignment

    self.trace(node.attrname,node.flags)
    e = self.visit(node.expr) or '&lt;None&gt;'
    #expr expression on the left-hand side of the dot
    
    return '%s%s = %s' % (self.indent,node.attrname,e)

</t>
<t tx="ekr.20061204205000.3">def visitAssList(self,node):
    
    # self.trace()
    
    result = []
    for z in node.nodes:
        a = self.visit(z) or '&lt;None&gt;'
        result.append(a)
        
    return ''.join(result) or '&lt;assnList: None&gt;'
</t>
<t tx="ekr.20061204205000.4">def visitAssName(self,node):
    
    # name name being assigned to
    # self.trace(node.name,node.flags)
    
    return node.name
</t>
<t tx="ekr.20061204205000.5">def visitReturn (self,node):

    val = self.visit(node.value) or '&lt;ret:None&gt;'
    return '%sreturn %s ;' % (self.indent,val)</t>
<t tx="ekr.20061204205628">def visitAssTuple (self,node):
    
    self.trace()
    for z in node.nodes:
        self.visit(z)</t>
<t tx="ekr.20061204205628.1">def visitAssert (self,node):
    
    self.trace(node.test,node.fail)
        # test the expression to be tested 
        # fail the value of the AssertionError 
</t>
<t tx="ekr.20061204205628.2">def visitAssign (self,node):
    
    # self.trace()
    assignments = []
    e = self.visit(node.expr)
    for z in node.nodes:
        a = self.visit(z)
        assignments.append(a)  
    result = []
    for z in assignments:
        s = '%s%s = %s ;' % (self.indent,a,e)
        result.append(s)
        
    return ''.join(result)
        
    
    # nodes a list of assignment targets, one per equal sign 
    # expr the value being assigned 
</t>
<t tx="ekr.20061204205628.3">def visitAugAssign (self,node):
    
    self.trace(node.op,node.expr)
    self.visit(node.node)
</t>
<t tx="ekr.20061204205628.4">def visitBackquote (self,node):
    
    self.trace(node.expr)
</t>
<t tx="ekr.20061204205628.5">def visitBitand (self,node):
    self.trace()
    for z in node.nodes:
        self.visit(z)

def visitBitor (self,node):
    self.trace()
    for z in node.nodes:
        self.visit(z)
        
def visitBitxor (self,node):
    self.trace()
    for z in node.nodes:
        self.visit(z)
</t>
<t tx="ekr.20061204205628.6">def visitBreak (self,node):
    
    self.trace()
</t>
<t tx="ekr.20061204205628.7">def visitCallFunc (self,node):

    # self.trace('args',node.args,'*args',node.star_args,'**args',node.dstar_args)
        #node expression for the callee 
        #args a list of arguments 
        #star_args the extended *-arg value 
        #dstar_args the extended **-arg value
    
    # g.trace('node',node.node)
    
    args = []
    if node.args:
        for z in node.args:
            s = self.visit(z) or '&lt;arg:None&gt;'
            args.append(s)
    star_args = []
    if node.star_args:
        for z in node.star_args:
            s = self.visit(z) or '&lt;*arg:None&gt;'
            star_args.append(s)
    dstar_args = []
    if node.dstar_args:
        for z in node.dstar_args:
            s = self.visit(z) or '&lt;**arg:None&gt;'
            dstar_args.append(s)
    all_args = []
    for aList in (args,star_args,dstar_args):
        all_args.extend(aList)
    all_args = ','.join(all_args)
    name = self.visit(node.node) or '&lt;call:None&gt;'
    theCall = '%s(%s)' % (name,all_args)
    return theCall
</t>
<t tx="ekr.20061204205628.8">def visitClass (self,node):

    # self.trace(node.name,'bases',node.bases)

    self.push()
    self.classStack.append(node.name)
    
    if node.doc:
        self.visit(node.doc)
        
    result = []
    for z in node.code:
        s = self.visit(z)
        result.append(s)

    name = self.classStack.pop()
    assert name == node.name,'visitClass: expected %s, got %s' % (node.name,name)
    self.pop()

    #doc doc string, a string or None 
    #code the body of the class statement
    
    result = ''.join(result) or '&lt;Class:None&gt;'
    theClass = '%sclass %s:\n%s' % (self.indent,node.name,result)
    # print theClass
    return theClass
</t>
<t tx="ekr.20061204205628.9">def visitCompare (self,node):

    #self.trace('ops',node.ops)
    #self.trace('expr',node.expr)
    
    e = self.visit(node.expr) or '&lt;comp:expr:None&gt;'
    
    result = ''
    for data in node.ops:
        op,val = data
        # g.trace(op,val)
        val = self.visit(val)
        if result:
            result = '%s &amp;&amp; %s %s %s' % (result,e,op,val)
            e = val
        else:
            result = '%s %s %s' % (e,op,val)
            e = val
            
    return result</t>
<t tx="ekr.20061204205628.10">def visitConst (self,node):
    
    return str(node.value)
</t>
<t tx="ekr.20061204205628.11">def visitContinue (self,node):
    
    self.trace()</t>
<t tx="ekr.20061204211034">def visitExpression (self,node):
    
    self.trace(node)</t>
<t tx="ekr.20061204211034.1">def visitFor (self,node):
    
    # self.trace()
    theAssn = self.visit(node.assign) or '&lt;for:assn:None&gt;'
    theList = self.visit(node.list) or '&lt;for:list:None&gt;'
    
    self.push()
    
    body = []
    for z in node.body:
        s = self.visit(z) or '&lt;for:None&gt;'
        body.append(s)
    body = ''.join(body).rstrip()+'\n'
    
    self.pop()
    
    theElse = node.else_ and self.visit(node.else_) or None
    theElseTrace = theElse or '&lt;for:else:None&gt;'
        
    # g.trace('assn',node.assign)
    # g.trace('list',node.list)
    # g.trace(body)
    # g.trace(theElse)

    theFor = '%sfor (%s in %s) {\n%s%s}' % (self.indent,theAssn,theList,body,self.indent)
    if theElse: theFor += '%selse {\n%s%s}' % (self.indent,theElse,self.indent)
    return theFor</t>
<t tx="ekr.20061204211633">def trace (self,*args,**keys):
    
    if 1:
        s = g.callers(3) + ':'
    else:
        s = '.' * len(self.stack) + g.callers(3) + ':'

    print '%-15s' % s,
    for arg in args:
        print arg,
    print
</t>
<t tx="ekr.20061204213730">def visitGenExprIf (self,node):
    
    self.trace()
    self.visit(node.test)
</t>
<t tx="ekr.20061204213730.1">def visitGenExprInner (self,node):
    
    g.trace(node.quals)
    self.visit(node.expr)
</t>
<t tx="ekr.20061204213730.2">def visitGetattr (self,node):
    
    if 0:
        self.trace(node.attrname)
    return self.visit(node.expr)
</t>
<t tx="ekr.20061204213730.3">def visitGenExpr (self,node):

    g.trace()
    
    self.push()

    result = []
    for z in node.code:
        s = self.visit(z)
        result.append(s)
        
    self.pop()

    result = ''.join(result) or '&lt;Expr:None&gt;'
    return result</t>
<t tx="ekr.20061204213730.4">def visitGenExprFor (self,node):
    
    g.trace()

    self.visit(node.assign)
    if node.iter:
        self.visit(node.iter)
    if node.ifs:
        self.visit(node.ifs)
</t>
<t tx="ekr.20061204214019">def visitIf (self,node):
    
    # self.trace()

    code = []
    for test,block in node.tests:
        test = self.visit(test) or '&lt;if:test:None&gt;'
        # self.trace(test)
        theBlock = self.visit(block) or '&lt;if:block:None&gt;'
        op = g.choose(len(code)&gt;0,'elif','if')
        s = '%s%s (%s) {\n%s%s}' % (self.indent,op,test,theBlock,self.indent)
        if code: s = '\n' + s
        code.append(s)

    theElse = node.else_ and self.visit(node.else_)
    if theElse:
        s = '\n%selse {\n%s%s}' % (self.indent,theElse,self.indent)
        code.append(s)
    theIf = ''.join(code)+'\n'
    return theIf
</t>
<t tx="ekr.20061204214019.1">def visitDecorators (self,node):
    
    for z in node.nodes:
        self.visit(z)
    
    # nodes List of function decorator expressions 

</t>
<t tx="ekr.20061205062426">def visitDict (self,node):
    
    g.trace()
    for z in node.items:
        self.visit(z)
</t>
<t tx="ekr.20061205062426.1">def visitDiscard (self,node):
    
    g.trace()
    self.visit(node.expr)

</t>
<t tx="ekr.20061205062741">&lt;&lt; define s &gt;&gt;

@others

p = g.findNodeAnywhere(c,'class ASTVisitor')
if p:
    print '-' * 40
    lines = g.splitlines(s)
    body = []
    for line in lines:
        if line.strip():
            body.append(line)
        elif body:
            head = body and body[0]
            i = head.find(' ')
            if i &gt; -1: head = head[:i]
            head = 'visit' + head
            print ('head',head)
            body = mungeBody(body)
            print('body',repr(body))
            if 0:
                p2 = p.insertAsLastChild()
                c.setHeadString(p2,head)
                c.setBodyString(p2,body)
            body = []</t>
<t tx="ekr.20061205064845">
s = '''
Div left  
 right  

Ellipsis   

Exec expr  
 locals  
 globals  

FloorDiv left  
 right  

From modname  
 names  

Global names  

Import names  

Invert expr  

Keyword name  
 expr  

Lambda argnames  
 defaults  
 flags  
 code  

LeftShift left  
 right  

List nodes  

ListComp expr  
 quals  

ListCompFor assign  
 list  
 ifs  

ListCompIf test  

Mod left  
 right  

Module doc doc string, a string or None 
 node body of the module, a Stmt 

Mul left  
 right  

Name name  

Not expr  

Or nodes  

Pass   

Power left  
 right  

Print nodes  
 dest  

Printnl nodes  
 dest  

Raise expr1  
 expr2  
 expr3   

RightShift left  
 right  

Slice expr  
 flags  
 lower  
 upper  

Sliceobj nodes list of statements 

Stmt nodes  

Sub left  
 right  

Subscript expr  
 flags  
 subs  

TryExcept body  
 handlers  
 else_  

TryFinally body  
 final  

Tuple nodes  

UnaryAdd expr  

UnarySub expr  

While test  
 body  
 else_  

With expr  
 vars  
 body  

Yield value
'''</t>
<t tx="ekr.20061205064845.1">def mungeBody (body):
    
    s = body[0]
    i = s.find(' ')
    if i &gt; -1:
        s = 'def visit' + s[:i] + ' (self,node):' + '# ' + s[i:]
    else:
        s = 'def visit' + s + ' (self,node):'
    body[0] = s + '\tg.trace()\n'
    
    for line in body:
        if line.find('nodes') &gt; -1:
            body.append('\tfor z in node.nodes:\n\t\tself.visit(z)\n')
            break
        elif line.find('body') &gt; -1:
            body.append('\tfor z in node.body:\n\t\tself.visit(z)\n')
            break
       
    return ''.join(body)
</t>
<t tx="ekr.20061205065240">def visitDiv (self,node):

	g.trace()
    self.visit(node.right)
    self.visit(node.left)
</t>
<t tx="ekr.20061205065240.1">def visitEllipsis (self,node):

	g.trace()
</t>
<t tx="ekr.20061205065240.2">def visitExec (self,node):
    
	g.trace(node.locals,node.globals)
    self.visit(node.expr)
</t>
<t tx="ekr.20061205065240.3">def visitFloorDiv (self,node):
    
	g.trace()
    self.visit(node.right)
    self.visit(node.left)
</t>
<t tx="ekr.20061205065240.4">def visitFrom (self,node):

	g.trace(node.modname,node.names)
</t>
<t tx="ekr.20061205065240.5">def visitGlobal (self,node):

	g.trace(node.names)
</t>
<t tx="ekr.20061205065240.6">def visitImport (self,node):

	g.trace(node.names)
</t>
<t tx="ekr.20061205065240.7">def visitInvert (self,node):

	g.trace()
    self.visit(node.expr)
</t>
<t tx="ekr.20061205065240.8">def visitKeyword (self,node):

	g.trace(node.name)
    self.visit(node.expr)
</t>
<t tx="ekr.20061205065240.9">def visitLambda (self,node):

	g.trace(node.flags,node.argnames)
    for z in node.defaults:
        self.visit(z)
    for z in node.code:
        self.visit(z)
 </t>
<t tx="ekr.20061205065240.10">def visitLeftShift (self,node):

	g.trace()
    self.visit(node.right)
    self.visit(node.left)
</t>
<t tx="ekr.20061205065240.11">def visitList (self,node):

	g.trace()
	for z in node.nodes:
		self.visit(z)
</t>
<t tx="ekr.20061205065240.12">def visitListComp (self,node):
 
	g.trace()
    self.visit(node.expr)
    for z in node.quals:
        self.visit(z)
</t>
<t tx="ekr.20061205065240.13">def visitListCompFor (self,node):

	g.trace()
    self.visit(node.assign)
    for z in node.list:
        self.visit(z)
    for z in node.ifs:
        self.visit(z)
</t>
<t tx="ekr.20061205065240.14">def visitListCompIf (self,node):  
	
    g.trace()
    self.visit(node.test)
</t>
<t tx="ekr.20061205065240.15">def visitMod (self,node):

	g.trace()
    self.visit(node.right)
    self.visit(node.left)
</t>
<t tx="ekr.20061205065240.16">if 0:
    def visitModule (self,node):
    
	    g.trace(node.doc)
	    # for z in node.body:
		    # self.visit(z)
</t>
<t tx="ekr.20061205065240.17">def visitMul (self,node):

	g.trace()
    self.visit(node.right)
    self.visit(node.left)</t>
<t tx="ekr.20061205065240.18">def visitName (self,node):
    
    # g.trace(node)
    
    if node.name:
        return str(node.name) or '&lt;Name:None&gt;'
    else:
        return '&lt;Name:None&gt;'
</t>
<t tx="ekr.20061205065240.19">def visitNot (self,node):

	g.trace()
    self.visit(node.expr)
</t>
<t tx="ekr.20061205065240.20">def visitOr (self,node):

	g.trace()
	for z in node.nodes:
		self.visit(z)
</t>
<t tx="ekr.20061205065240.21">def visitPass (self,node):
    
	return '%s;\n' % (self.indent)
</t>
<t tx="ekr.20061205065240.22">def visitPower (self,node):

	g.trace()
    self.visit(node.right)
    self.visit(node.left)
</t>
<t tx="ekr.20061205065240.23">def visitPrint (self,node):

	g.trace()
    if node.dest:
        self.visit(node.dest)
	for z in node.nodes:
		self.visit(z)
</t>
<t tx="ekr.20061205065240.24">def visitPrintnl (self,node):

	g.trace()
    if node.dest:
        self.visit(node.dest)
	for z in node.nodes:
		self.visit(z)
</t>
<t tx="ekr.20061205065240.25">def visitRaise (self,node):  
	
    g.trace()
    self.visit(expr1)
    self.visit(expr2)
    self.visit(expr3)
</t>
<t tx="ekr.20061205065240.26">def visitRightShift (self,node):
    
	g.trace()
    self.visit(node.right)
    self.visit(node.left)
 </t>
<t tx="ekr.20061205065240.27">def visitSlice (self,node):
    
	g.trace(flags)
    self.visit(node.expr)
    if node.lower:
        self.visit(node.lower)
    if node.upper:
        self.visit(node.upper)
</t>
<t tx="ekr.20061205065240.28">def visitSliceobj (self,node):

	g.trace()
	for z in node.nodes:
		self.visit(z)
</t>
<t tx="ekr.20061205065240.30">def visitSub (self,node):
 
	g.trace()
    self.visit(node.right)
    self.visit(node.left)
</t>
<t tx="ekr.20061205065240.31">def visitSubscript (self,node):
    
	g.trace(node.flags)
    self.visit(node.expr)
    for z in node.subs:
        self.visit(z)
</t>
<t tx="ekr.20061205065240.32">def visitTryExcept (self,node):

	g.trace()
	for z in node.body:
		self.visit(z)
    for z in node.handlers:
        self.visit(z)
    if node.else_:
        self.visit(node.else_)
</t>
<t tx="ekr.20061205065240.33">def visitTryFinally (self,node):

	g.trace()
	for z in node.body:
		self.visit(z)
    self.visit(node.final)
</t>
<t tx="ekr.20061205065240.34">def visitTuple (self,node):

	g.trace()
	for z in node.nodes:
		self.visit(z)
</t>
<t tx="ekr.20061205065240.35">def visitUnaryAdd (self,node):

	g.trace()
    self.visit(node.expr)
</t>
<t tx="ekr.20061205065240.36">def visitUnarySub (self,node):
    
	g.trace()
    self.visit(node.expr)
</t>
<t tx="ekr.20061205065240.37">def visitWhile (self,node):

	g.trace()
    
    self.push()

    self.visit(node.test)
	for z in node.body:
		self.visit(z)
    if node.else_:
        self.visit(node.else_)

    self.pop()</t>
<t tx="ekr.20061205065240.38">def visitWith (self,node):

	g.trace()
    for z in node.vars:
        self.visit(z)
    self.visit(node.expr)
	for z in node.body:
		self.visit(z)
</t>
<t tx="ekr.20061205073149">def push (self):
    
    name = g.callers(3)
    # g.trace('begin',name)
    self.stack.append(name)
    self.indent = ' ' * (4 *len(self.stack))
    
def pop (self):
    
    if self.stack:
        name = self.stack.pop()
        # g.trace('end',name)
    else:
        g.trace('can not happen')
    
    self.indent = ' ' * (4 *len(self.stack))</t>
</tnodes>
</leo_file>
