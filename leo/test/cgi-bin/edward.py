#! c:\python25\python.exe
#@+leo-ver=4
#@+node:@file cgi-bin/edward.py
#@@first
# This is the cgi script called from hello.html when the user hits the button.
print "Content-type:text/html" ; print # This second print is required.
import sys
print "hi from edward.py"
print '<br> sys.argv:'
print sys.argv
#@nonl
#@-node:@file cgi-bin/edward.py
#@-leo
