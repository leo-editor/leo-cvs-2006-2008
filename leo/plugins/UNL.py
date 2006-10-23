#@+leo-ver=4-thin
#@+node:rogererens.20041013082304:@thin UNL.py
#@<< docstring >>
#@+node:ekr.20050119144617:<< docstring >>
'''This plugin supports Uniform Node Locators (UNL's). UNL's specify nodes within
Leo files. UNL's are not limited to nodes within the present Leo file; you can
use them to create cross-Leo-file links! UNL

This plugin consists of two parts:

1) Selecting a node shows the UNL in the status line at the bottom of the Leo
   window. You can copy from the status line and paste it into headlines, emails,
   whatever. 

2) Double-clicking @url nodes containing UNL's select the node specified in the
   UNL. If the UNL species in another Leo file, the other file will be opened.

Format of UNL's:

UNL's referring to nodes within the present outline have the form::

    headline1-->headline2-->...-->headlineN

headline1 is the headline of a top-level node, and each successive headline is
the headline of a child node.

UNL's of the form::

    file:<path>#headline1-->...-->headlineN

refer to a node specified in <path> For example, double clicking the following
headline will take you to Chapter 8 of Leo's Users Guide::

    @url file:c:/prog/leoCvs/leo/doc/leoDocs.leo#Users Guide-->Chapter 8: Customizing Leo
    
For example, suppose you want to email someone with comments about a Leo file.
Create a comments.leo file containing @url UNL nodes. That is, headlines are
@url followed by a UNL. The body text contains your comments about the nodes in
the _other_ Leo file! Send the comments.leo to your friend, who can use the
comments.leo file to quickly navigate to the various nodes you are talking
about. As another example, you can copy UNL's into emails. The recipient can
navigate to the nodes 'by hand' by following the arrows in the UNL.

**Notes**:

- At present, UNL's refer to nodes by their position in the outline. Moving a
  node will break the link.

- Don't refer to nodes that contain UNL's in the headline. Instead, refer to the
  parent or child of such nodes.

- You don't have to replace spaces in URL's or UNL's by '%20'.
'''
#@nonl
#@-node:ekr.20050119144617:<< docstring >>
#@nl

#@@language python
#@@tabwidth -4

__version__ = "0.8"
#@<< version history >>
#@+node:rogererens.20041014104353:<< version history >>
#@+at
# 
# - 0.1 rogererens: Initial version.
# - 0.2 ekr:  changes for new status line class.
# - 0.3 ekr: Added support for url keyword in '@url1' hook.
#            As a result, this plugin supports single and double quoted urls.
# - 0.4 ekr: Fixed crasher by adding c argument to g.findTopLevelNode and 
# g.findNodeInTree.
# - 0.5 EKR: Convert %20 to ' ' in url's.
# - 0.6 EKR: Made local UNL's work.
# - 0.7 EKR: Set c.doubleClickFlag to keep focus in newly-opened window.
# - 0.8 johnmwhite: Patch to onURl1 to handle @url file: headlines properly.
#@-at
#@nonl
#@-node:rogererens.20041014104353:<< version history >>
#@nl
#@<< imports >>
#@+node:rogererens.20041014110709.1:<< imports >>
import leoGlobals as g
import leoPlugins

Tk = g.importExtension('Tkinter',pluginName=__name__,verbose=True)

import os       
import urlparse 
#@nonl
#@-node:rogererens.20041014110709.1:<< imports >>
#@nl
#@<< globals >>
#@+node:rogererens.20041014111328:<< globals >>
#@+at
# 
#@-at
#@-node:rogererens.20041014111328:<< globals >>
#@nl

#@+others
#@+node:rogererens.20041013082304.1:createStatusLine
def createStatusLine(tag,keywords):

    """Create a status line.""" # Might already be done by another plugin. Checking needed?
    
    c = keywords.get("c")
    statusLine = c.frame.createStatusLine()
    statusLine.clear()
    statusLine.put("...")
#@nonl
#@-node:rogererens.20041013082304.1:createStatusLine
#@+node:rogererens.20041021091837:onUrl1
def onUrl1 (tag,keywords):
    """Redefine the @url functionality of Leo Core: allows jumping to URL _and UNLs_.
    Spaces are now allowed in URLs."""
    c = keywords.get("c")
    v = keywords.get("v")
    # The unl key is new in 4.3 beta 2.
    # The unl ends with the first blank, unless either single or double quotes are used.
    url = keywords.get('url')
    url = url.replace('%20',' ')

#@+at 
#@nonl
# Most browsers should handle the following urls:
#   ftp://ftp.uu.net/public/whatever.
#   http://localhost/MySiteUnderDevelopment/index.html
#   file://home/me/todolist.html
#@-at
#@@c

    try:
        try:
            urlTuple = urlparse.urlsplit(url)
            #@            << log url-stuff >>
            #@+node:rogererens.20041125015212:<<log url-stuff>>
            if 0:
                g.es("scheme  : " + urlTuple[0])
                g.es("network : " + urlTuple[1])
                g.es("path    : " + urlTuple[2])
                g.es("query   : " + urlTuple[3])
                g.es("fragment: " + urlTuple[4])
            #@nonl
            #@-node:rogererens.20041125015212:<<log url-stuff>>
            #@nl
        except:
            g.es("exception interpreting the url " + url)
            g.es_exception()
       
        if not urlTuple[0]:
            urlProtocol = "file" # assume this protocol by default
        else:
            urlProtocol = urlTuple[0]
        
        if urlProtocol == "file":
            if urlTuple[2].endswith(".leo"):
                c.frame.top.update_idletasks() # Clear remaining events, so they don't interfere.
                ok,frame = g.openWithFileName(urlTuple[2], c)
                if ok:
                    #@                    << go to the node>>
                    #@+node:rogererens.20041125015212.1:<<go to the node>>
                    c2 = frame.c
                    
                    if urlTuple [4]: # we have a UNL!
                        nodeList = urlTuple [4].split("-->")
                        p = g.findTopLevelNode(c2,nodeList[0])
                        for headline in nodeList [1:]:
                            p = g.findNodeInTree(c2,p,headline)
                        if p:
                            c2.beginUpdate()
                            try:
                                c2.frame.tree.expandAllAncestors(p)
                                c2.selectPosition(p)
                            finally:
                                c2.endUpdate()
                                
                    # Disable later call to c.onClick so the focus stays in c2.
                    c.doubleClickFlag = True
                    #@nonl
                    #@-node:rogererens.20041125015212.1:<<go to the node>>
                    #@nl
            elif urlTuple[0] == "":
                #@                << go to node in present outline >>
                #@+node:ekr.20060908105814:<< go to node in present outline >>
                if urlTuple [2]:
                    nodeList = urlTuple [2].split("-->")
                    p = g.findTopLevelNode(c,nodeList[0])
                    if p:
                        for headline in nodeList [1:]:
                            p = g.findNodeInTree(c,p,headline)
                            if not p: break
                    if p:
                        c.frame.tree.expandAllAncestors(p)
                        c.selectPosition(p)
                        c.redraw()
                #@nonl
                #@-node:ekr.20060908105814:<< go to node in present outline >>
                #@nl
            else:
                #@                <<invoke external browser>>
                #@+node:ekr.20061023141204:<<invoke external browser>>
                import webbrowser
                             
                # Mozilla throws a weird exception, then opens the file!
                try:
                    webbrowser.open(url)
                except:
                    pass
                #@nonl
                #@-node:ekr.20061023141204:<<invoke external browser>>
                #@nl
        else:
            #@            <<invoke external browser>>
            #@+node:ekr.20061023141204:<<invoke external browser>>
            import webbrowser
                         
            # Mozilla throws a weird exception, then opens the file!
            try:
                webbrowser.open(url)
            except:
                pass
            #@nonl
            #@-node:ekr.20061023141204:<<invoke external browser>>
            #@nl
        return True
            # PREVENTS THE EXECUTION OF LEO'S CORE CODE IN
            # Code-->Gui Base classes-->@thin leoFrame.py-->class leoTree-->tree.OnIconDoubleClick (@url)
    except:
        g.es("exception opening " + url)
        g.es_exception()
#@nonl
#@-node:rogererens.20041021091837:onUrl1
#@+node:rogererens.20041013084119:onSelect2
def onSelect2 (tag,keywords):

    """Shows the UNL in the status line whenever a node gets selected."""

    c = keywords.get("c")

    # c.currentPosition() is not valid while using the settings panel.
    new_p = keywords.get('new_p')
    
    # g.trace(new_p)
    
    if new_p:
        c.frame.clearStatusLine()
        myList = [p.headString() for p in new_p.self_and_parents_iter()]
        myList.reverse()

        # Rich has reported using ::
        # Any suggestions for standardization?
        s = "-->".join(myList)
        c.frame.putStatusLine(s)
#@nonl
#@-node:rogererens.20041013084119:onSelect2
#@-others

if Tk: # Ok for unit testing.
    if g.app.gui is None:
        g.app.createTkGui(__file__)

    if g.app.gui.guiName() == "tkinter":
        leoPlugins.registerHandler("after-create-leo-frame", createStatusLine)
        leoPlugins.registerHandler("select2", onSelect2)    # show UNL
        leoPlugins.registerHandler("@url1", onUrl1)         # jump to URL or UNL
                
        g.plugin_signon(__name__)
#@nonl
#@-node:rogererens.20041013082304:@thin UNL.py
#@-leo
