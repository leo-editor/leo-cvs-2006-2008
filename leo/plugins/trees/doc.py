#@+leo-ver=4-thin
#@+node:ekr.20050329082101.165:@thin trees\doc.py
#@<< docstring >>
#@+node:ekr.20050329082101.166:<< docstring >>
"""A handler that documents a module

The parameter in the @auto-doc headline is the module to document.
    
"""
#@-node:ekr.20050329082101.166:<< docstring >>
#@nl

from autotrees import BaseTreeHandler, TreeNode
import inspect
import sets

import leoGlobals as g

__version__ = "0.1"
__plugin_requires__ = ["autotrees"]
__plugin_group__ = "Coding"

#@<< version history >>
#@+node:ekr.20050329082101.167:<< version history >>
#@+at
# 
# Version history
# 
# 0.1 - Paul Paterson:
#       Initial version
#@-at
#@-node:ekr.20050329082101.167:<< version history >>
#@nl


class Doc(BaseTreeHandler):
    """Handler for documentation nodes"""
        
    def initFrom(self, parameter):
        """Initialize the tree"""
        self.children = []
        self.done = sets.Set()
        try:
            module = __import__(parameter)
        except Exception, err:
            g.es("Failed: %s" % (err,), color="red")
        else:
            components = parameter.split('.')
            for comp in components[1:]:
                module = getattr(module, comp)
            self.children.extend(self.getDocsFor(module))
            
    def getDocsFor(self, object):
        """Return a list of child nodes documenting the object"""
        #print object
        children = []
        for name in dir(object):
            item = getattr(object, name)
            if not name.startswith("_") and not id(item) in self.done:
                self.done.add(id(item))
                if inspect.isclass(item):
                    #print "Class", item.__name__
                    grandchildren = self.getDocsFor(item)
                else:
                    #print "item", item
                    grandchildren = []
                children.append(
                    TreeNode(
                        name,
                        getattr(item, "__doc__", "No documentation for %s" % name),
                        grandchildren
                    )
                )
        return children
            
#@-node:ekr.20050329082101.165:@thin trees\doc.py
#@-leo
