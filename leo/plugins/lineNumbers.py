#@+leo-ver=4-thin
#@+node:ekr.20040419105219:@thin lineNumbers.py
'''Adds #line directives in perl and perlpod programs.

Over-rides two methods in leoAtFile.py to write #line directives after node
sentinels. This allows compilers to give locations of errors in relation to the
node name rather than the filename. Currently supports only perl and perlpod.
'''

# Use and distribute under the same terms as Leo.
# Original code by Mark Ng <markn@cs.mu.oz.au>

#@<< imports >>
#@+node:ekr.20050105150253:<< imports >>
import leoGlobals as g
import leoPlugins

import leoAtFile
import re
#@nonl
#@-node:ekr.20050105150253:<< imports >>
#@nl
__version__ = "0.3"
#@<< version history >>
#@+node:ekr.20050105150253.1:<< version history >>
#@@killcolor
#@+at
# 
# 0.1 Mark Ng
#     - Original code
# 0.2 EKR:
#     - Convert to new coding conventions.
# 0.3 EKR:
#     - Changed leoAtFile.newDerivedFile to leoAtFile.atFile when overriding 
# methods.
#       This is required because of changes in 4.3 to Leo's core code.
# 0.4 EKR:
#     - Used named sections to emphasize the dangerous nature of this code.
#@-at
#@nonl
#@-node:ekr.20050105150253.1:<< version history >>
#@nl

linere = re.compile("^#line 1 \".*\"$")

if not g.app.unitTesting: # Not safe for unit testing.  Changes core class.

    #@    << override write methods >>
    #@+node:ekr.20040419105219.1:<< override write methods >>
    oldOpenNodeSentinel = leoAtFile.atFile.putOpenNodeSentinel
    
    def putLineNumberDirective(self,v,inAtAll=False,inAtOthers=False,middle=False):
    
        oldOpenNodeSentinel(self,v,inAtAll,inAtOthers,middle)
    
        if self.language in ("perl","perlpod"):
            line = 'line 1 "node:%s (%s)"' % (self.nodeSentinelText(v),self.shortFileName)
            self.putSentinel(line)
            
    g.funcToMethod(putLineNumberDirective,	
        leoAtFile.atFile,"putOpenNodeSentinel")
    #@nonl
    #@-node:ekr.20040419105219.1:<< override write methods >>
    #@nl
    #@    << override read methods >>
    #@+node:ekr.20040419105219.2:<< override read methods >>
    readNormalLine = leoAtFile.atFile.readNormalLine
    
    def skipLineNumberDirective(self, s, i):
    
        if linere.search(s): 
            return  # Skipt the line.
        else:		
            readNormalLine(self,s,i)
    
    g.funcToMethod(skipLineNumberDirective,
        leoAtFile.atFile,"readNormalLine")
    #@nonl
    #@-node:ekr.20040419105219.2:<< override read methods >>
    #@nl
    g.plugin_signon(__name__)
#@nonl
#@-node:ekr.20040419105219:@thin lineNumbers.py
#@-leo
