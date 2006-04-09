#@+leo-ver=4-thin
#@+node:edream.110203113231.919:@thin override_commands.py
"""Override the Equal Sized Pane command"""

#@@language python
#@@tabwidth -4

import leoGlobals as g
import leoPlugins

#@+others
#@+node:edream.110203113231.920:onCommand
def onCommand (tag,keywords):

    if keywords.get("label")=="equalsizedpanes":
        g.es("over-riding Equal Sized Panes")
        return "override" # Anything other than None overrides.
#@nonl
#@-node:edream.110203113231.920:onCommand
#@-others

if not g.app.unitTesting: # Not for unit testing: overrides core methods.

    # Register the handlers...
    leoPlugins.registerHandler("command1", onCommand)
    
    __version__ = "1.2"
    g.plugin_signon(__name__)
#@nonl
#@-node:edream.110203113231.919:@thin override_commands.py
#@-leo
