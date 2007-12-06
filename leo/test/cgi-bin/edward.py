#! c:\python25\python.exe
#@+leo-ver=4
#@+node:@file cgi-bin/edward.py
#@@first
# This is the cgi script called from hello.html when the user hits the button.

#@+others
#@+node:print_css
def print_css():

    print '<style type="text/css">'
    print 'body{'
    print '  font: 10pt Verdana,sans-serif;'
    print '  color: navy;'
    print '}'
    print '.node{'
    print '  cursor: pointer;'
    print '  cursor: hand;'
    print '}'
    print '.branch{'
    print '  display: none;'
    print '  margin-left: 16px;'
    print '}'
    print '</style>'
#@-node:print_css
#@+node:print_node
def print_node (p):

    gnx = g.app.nodeIndices.toString(p.v.t.fileIndex)

    print '<div class="node">'
    print '<img src="closed.gif" alt="-" border="0" id="%s">' % gnx
    print p.headString()
    print '<p>'
    print p.bodyString() or '<b>no body</b>'
    print '</div>'

    # <span class="branch" id="branch1">
         # <img src="doc.gif">Tags, Tags, Tags<br>
         # <img src="doc.gif">Hyperlinks</a><br>
         # <img src="doc.gif">Images<br>
         # <img src="doc.gif">Tables<br>
         # <img src="doc.gif">Forms<br>
     # </span>
#@-node:print_node
#@+node:class nullFileObject
class nullFileObject:

    '''A class used to discard all output to stdout, etc.'''

    def write (self,s):
        pass
#@-node:class nullFileObject
#@-others

import os
import sys
path = r'c:\prog\tigris-cvs\leo\test\test.leo'

# Kill all output from the bridge so it doesn't become part of the page.
sys.stdout = nullFileObject()
import leoBridge
controller = leoBridge.controller(gui='nullGui',verbose=False)
g = controller.globals()
c = controller.openLeoFile(path)
p = c.rootPosition()
# Restore sys.stdout.
sys.stdout = sys.__stdout__

# This line is required (with extra newline), but does not show on the page.
print "Content-type:text/html\n"

print '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2//EN">'
print '<html>'
print '<head>'
print '<title></title>'
print_css()
print '</head>'
print '<body>'
print '<p> This is the page returned by edward.py'
print '<p> It is a placeholder, to be replaced by css representing a tree.'
print 'sys.argv:',sys.argv

print_node(p)
print '</body>'
print '</html>'
#@-node:@file cgi-bin/edward.py
#@-leo
