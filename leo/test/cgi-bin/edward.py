#! c:\python25\python.exe
#@+leo-ver=4
#@+node:@file cgi-bin/edward.py
#@@first
# This is the cgi script called from hello.html when the user hits the button.

# This line is required (with extra newline), but does not show on the page.
print "Content-type:text/html\n"

import sys
print '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2//EN">'
print '<html>'
print '<head>'
print '<title></title>'
print '</head>'
print '<body>'
print '<p> This is the page returned by edward.py'
print '<p> It is a placeholder, to be replaced by css representing a tree.'
print 'sys.argv:',sys.argv
print '</body>'
print '</html>'
#@-node:@file cgi-bin/edward.py
#@-leo
