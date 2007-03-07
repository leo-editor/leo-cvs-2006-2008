#@+leo-ver=4-thin
#@+node:ekr.20070227104713:@thin leoBridgeTest.py
'''A program to run unit tests with the leoBridge module.'''

#@+others
#@+node:ekr.20070227172826:main & helpers
def main ():
    
    tag = 'leoTestBridge'
    path = r'c:\prog\tigris-cvs\leo\test\test.leo'
    path = r'c:\prog\tigris-cvs\leo\test\unitTest.leo'

    import leoBridge

    # Setting verbose=True prints messages that would be sent to the log pane.
    bridge = leoBridge.controller(gui='nullGui',verbose=False)
    if bridge.isOpen():
        g = bridge.globals()
        c = bridge.openLeoFile(path)
        g.es('%s %s' % (tag,c.shortFileName()))
        runUnitTests(c,g)

    print tag,'done'
#@nonl
#@+node:ekr.20070227172648:runUnitTests
def runUnitTests (c,g):

    nodeName = 'All unit tests'
    
    import leoTest
    try:
        u = leoTest.testUtils(c)
        p = u.findNodeAnywhere(nodeName)
        if p:
            g.es('running unit tests in %s...' % nodeName)
            c.selectPosition(p)
            c.debugCommands.runUnitTests()
            g.es('unit tests complete')
        else:
            g.es('node not found:' % nodeName)
    except Exception:
        g.es('unexpected exception')
        g.es_exception()
        raise
#@nonl
#@-node:ekr.20070227172648:runUnitTests
#@-node:ekr.20070227172826:main & helpers
#@-others

main()
#@-node:ekr.20070227104713:@thin leoBridgeTest.py
#@-leo
