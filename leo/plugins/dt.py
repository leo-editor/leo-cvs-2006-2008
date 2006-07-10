#@+leo-ver=4-thin
#@+node:ekr.20060710092959:@thin dt.py
#@<< docstring >>
#@+node:ekr.20060710093300:<< docstring >>
'''Sends code to the doctest module and reports the result.'''
#@nonl
#@-node:ekr.20060710093300:<< docstring >>
#@nl
#@<< imports >>
#@+node:ekr.20060710092959.1:<<imports >>
import leoPlugins
from leoPlugins import baseLeoPlugin
import doctest
import os
import leoGlobals as g
#@-node:ekr.20060710092959.1:<<imports >>
#@nl
#@<< version history >>
#@+node:ekr.20060710093300.1:<< version history >>
#@@nocolor

#@+at
# v 0.1 EKR: modified slightly from original by ktenney.
#@-at
#@nonl
#@-node:ekr.20060710093300.1:<< version history >>
#@nl

#@+others
#@+node:ekr.20060710093300.2:init
def init ():
    
    leoPlugins.registerHandler('after-create-leo-frame', DT)
    
    return True
#@nonl
#@-node:ekr.20060710093300.2:init
#@+node:ekr.20060710092959.2:class DT
class DT(baseLeoPlugin):

    """Sends code to the doctest module and reports the result
    If text is selected, tests only the selection
    """

    #@    @+others
    #@+node:ekr.20060710092959.3:__init__
    def __init__(self, tag, keywords):
        
        """Init doctest plugin
        """
        baseLeoPlugin.__init__(self, tag, keywords)
        self.setCommand('dtest', self.dtest)
    
    #    self.setMenuItem('Cmds')
    #    self.setButton()
    #@-node:ekr.20060710092959.3:__init__
    #@+node:ekr.20060710092959.4:dtest
    def dtest(self, event):
        """The handler
        """
        
        # get a valid temporary filename
        createfile, tempfilename = g.create_temp_file()
        createfile.close()
        
        selected = False
        
        # if text is selected, only test selection
        if self.c.frame.body.hasTextSelection():
            selected = True
            selection = self.c.frame.body.getSelectedText()
            tempfile = open(tempfilename, 'w')
            tempfile.write(selection)
            tempfile.close()
        
        # test this subtree
        else:
            self.c.importCommands.flattenOutline(tempfilename)
            
        tempfile = open(tempfilename)
        text = tempfile.readlines()
        tempfile.close()    
        # strip trailing whitespace, an annoying source of doctest failures
        text = [line.strip() for line in text]
        text = "\n".join(text)
        tempfile = open(tempfilename, 'w')
        tempfile.write(text)
        tempfile.close()
        
        # run doctest on temporary file
        failures, tests = doctest.testfile(tempfilename, module_relative = False)
        
        # report summary of results in Leo
        if selected:
            g.es('Result of running doctest on selected text;')
        else:
            g.es('Result of running doctest on this subtree;')        
        if failures == 0:
            g.es("%s tests run successfully" % tests, color="blue")
        if failures == 1:
            g.es("There was one failure in %s tests" % tests, color="red")    
        if failures > 1:
            g.es("%s failures in %s tests" % (failures, tests), color="red")
         
        os.remove(tempfilename)
    #@nonl
    #@-node:ekr.20060710092959.4:dtest
    #@+node:ekr.20060710092959.5:onCreate
    def onCreate(tag, keywords):
    
        DT.dt(tag, keywords)
    #@nonl
    #@-node:ekr.20060710092959.5:onCreate
    #@-others
#@nonl
#@-node:ekr.20060710092959.2:class DT
#@-others
#@nonl
#@-node:ekr.20060710092959:@thin dt.py
#@-leo
