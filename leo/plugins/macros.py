#@+leo-ver=4-thin
#@+node:ekr.20040916084945:@thin macros.py
#@<< docstring >>
#@+node:ekr.20061102090532:<< docstring >>
'''
Creates new nodes containing parameterized section references.

For a discussion of this plugin, see:
http://sourceforge.net/forum/message.php?msg_id=2444117

This plugin adds nodes under the currently selected tree that are to act as
section references. To do so, go the Outline menu and select the
'Parameterize Section Reference' command. This plugin looks for a top level node called
'Parameterized Nodes'. If it finds a headline that matches the section reference
it adds a node/nodes to the current tree.

To see this in action, do the following:

0. **Important**: in the examples below, type << instead of < < and
   type >> instead of > >.  Docstrings can not contain section references!

1. Create a node called 'Parameterized Nodes', with a sub-node called < < Meow > >.
The body of < < Meow > > should have the text::

I mmmm sooo happy I could < < 1$ > >.  But I dont know if I have all the < < 2$ > >
money in the world.

2. In a node called A, type::

< < meow( purrrrrr, zzooot ) > > (leave the cursor at the end of the line)

3. In a node called B, type::

< < meow ( spit or puke, blinkin  ) > > (leave the cursor at the end of the line)

4. Leave the cursor in Node A at the designated point.

5. Go to Outline and select Parameterize Section Reference.

The plugin searches the outline, goes to level one and finds a Node with the Headline,
"Parameterized Nodes". It looks for nodes under that headline with the the headline
< < meow > >. It then creates this node structure under Node A:
    < < meow ( purrrrrr, zzooot ) > >
        < <2$> >
        < <1$> >

6. Examine the new subnodes of Node A.

< < meow ( purrrrrr, zzooot ) > > contains the body text of the < < meow > > node.
< < 1$ > > contains the word purrrrrr.
< < 2$ > > contains the word zzooot.

7. Go to Node B, and leave the cursor at the designated point.

Go to Outline Menu and select Parameterize Section Reference command.

8. Examine the new subnodes of Node B.

It's a lot easier to use than to explain!
'''
#@nonl
#@-node:ekr.20061102090532:<< docstring >>
#@nl

__version__ = "1.8"
#@<< version history >>
#@+node:ekr.20040916091520:<< version history >>
#@+at
# 
# 1.2 EKR:
# - Converted to outline.
# - Use g.angleBrackets to enclose lines with < < and > >.
# - Use new instead of start2 hook.
# - onCreate creates a new class for each commander.
# - Removed all globals.
# 1.3 EKR: Changed 'new_c' logic to 'c' logic.
# 1.4 EKR: Replaced tree.begin/endUpdate by c.beginEndUpdate.
# 1.5 EKR: Added event param to parameterize.
# 1.6 EKR: imported leoNodes and changed tnode to leoNodes.tnode.
# 1.7 Rich Ries: improved the docstring.
# 1.8 EKR: Add the menu only for the tkinter gui.
#@-at
#@nonl
#@-node:ekr.20040916091520:<< version history >>
#@nl

import leoGlobals as g
import leoNodes
import leoPlugins
import re

#@+others
#@+node:ekr.20070302121133:init
def init ():

    # Ok for unit testing: adds command to Outline menu.
    leoPlugins.registerHandler( ('new','open2') ,onCreate)
    g.plugin_signon(__name__)
#@nonl
#@-node:ekr.20070302121133:init
#@+node:ekr.20040916091520.1:onCreate
def onCreate(tag,keywords):

    c = keywords.get("c")
    if c:
        paramClass(c)
#@nonl
#@-node:ekr.20040916091520.1:onCreate
#@+node:ekr.20040916091520.2:class paramClass
class paramClass:

    #@    @+others
    #@+node:ekr.20040916091520.3:__init__
    def __init__ (self,c):

        self.c = c
        self.body = c.frame.body
        self.params = None
        self.pattern = g.angleBrackets(r'\w*?\(([^,]*?,)*?([^,])+?\)') + '$'
        self.regex = re.compile(self.pattern)

        if g.app.gui.guiName() == 'tkinter':
            self.addMenu()
    #@-node:ekr.20040916091520.3:__init__
    #@+node:ekr.20040916084945.1:macros.parameterize
    def parameterize (self,event=None):

        c = self.c
        tree = c.frame.tree
        body = c.frame.body
        w = body.bodyCtrl
        current = c.currentVnode()

        if not self.params:
            self.params = self.findParameters(current)
            if not self.params: return

        sr = body.getAllText()
        sr = sr.split('\n')

        t = str(g.app.gui.getInsertPoint(w)).split('.')
        sr = sr [int(t[0]) -1]
        sr = sr [: int(t[1])]
        sr = sr.rstrip()
        match = self.regex.search(sr)
        if not match: return

        sr = sr [match.start(): match.end()]
        for z in xrange(current.numberOfChildren()):
            child = current.nthChild(z)
            if child.headString == sr:
                return

        pieces = sr.split('(',1)
        searchline = pieces [0] + ">>"
        pieces [1] = pieces [1].rstrip('>')
        pieces [1] = pieces [1].rstrip(')')
        sections = pieces [1].split(',') ;

        node = None
        for z in xrange(self.params.numberOfChildren()):
            child = self.params.nthChild(z)
            if child.matchHeadline(searchline):
                node = child
                break
            return

        bodys = node.bodyString()
        tn = leoNodes.tnode(bodys,sr)
        c.beginUpdate()
        try:
            v = current.insertAsNthChild(0,tn)
            for z in xrange(0,len(sections)):
                head = g.angleBrackets(str(z+1)+"$")
                bod = sections [z]
                t = leoNodes.tnode(bod,head)
                v.insertAsNthChild(0,t)
        finally:
            c.endUpdate()
    #@nonl
    #@-node:ekr.20040916084945.1:macros.parameterize
    #@+node:ekr.20040916084945.2:findParameters
    def findParameters (self,v):

        tag = "Parameterized Nodes"

        if v.level() != 0:
            rnode = self.findParameters( v.parent())

        bnode = v
        while bnode:
            if bnode.headString() == tag:
                return bnode
            bnode = bnode.back()

        nnode = v
        while nnode:
            if nnode.headString() == tag:
                return nnode
            nnode = nnode.next()

        return None
    #@nonl
    #@-node:ekr.20040916084945.2:findParameters
    #@+node:ekr.20040916084945.3:addMenu
    def addMenu(self):

        c = self.c
        table = ("Parameterize Section Reference",None,self.parameterize),
        c.frame.menu.createMenuItemsFromTable("Outline",table,dynamicMenu=True)
    #@nonl
    #@-node:ekr.20040916084945.3:addMenu
    #@-others
#@nonl
#@-node:ekr.20040916091520.2:class paramClass
#@-others
#@-node:ekr.20040916084945:@thin macros.py
#@-leo
