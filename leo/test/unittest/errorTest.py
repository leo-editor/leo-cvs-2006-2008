#@+leo-ver=4-thin
#@+node:ekr.20041012101944:@thin ../test/unittest/errorTest.py
# A file that contains functions with errors in them.
# This is used to test error reporting in scripts

#@@language python
#@@tabwidth -4

def testIndexError():
    
    a = []
    b = a[2]
#@nonl
#@-node:ekr.20041012101944:@thin ../test/unittest/errorTest.py
#@-leo
