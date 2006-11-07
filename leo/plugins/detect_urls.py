#@+leo-ver=4-thin
#@+node:ekr.20060506070443.1:@thin detect_urls.py
#@<< docstring >>
#@+node:vpe.20060426084738:<< docstring >>
"""
Colorizes URLs everywhere in node's body on node selection. 
Double click on any URL launches it in default browser.

URL regex:  (http|https|ftp)://[^\s'"]+[\w=/]

Related plugins:  color_markup.py; rClick.py
"""
#@nonl
#@-node:vpe.20060426084738:<< docstring >>
#@nl
#@@language python
#@@tabwidth -4
import leoGlobals as g
import leoPlugins
import re
url_regex = re.compile(r"""(http|https|ftp)://[^\s'"]+[\w=/]""")

#@+others
#@+node:vpe.20060305064323.5:openURL()
def openURL(tag,keywords):
    c = keywords.get("c")

    gui = g.app.gui ; w = c.frame.body.bodyCtrl
    s = gui.getAllText(w)
    ins = gui.getInsertPoint(w,python=True)
    row,col = g.convertPythonIndexToRowCol(s,ins)
    i,j = g.getLine(s,ins)
    line = s[i:j]
    
    for match in url_regex.finditer(line):
        if match.start() < col < match.end():
            url = match.group()
            if 0: # I have no idea why this code was present.
                start,end = match.start(), match.end()
                c.frame.body.setSelectionRange("%s.%s" %(row,start), "%s.%s" %(row,end))
                gui.setSelectionRange(w,start,end,python=True)
            if not g.app.unitTesting:
                try:
                    import webbrowser
                    webbrowser.open(url)
                except:
                    g.es("exception opening " + url)
                    g.es_exception()
            return url # force to skip word selection if url found
#@nonl
#@-node:vpe.20060305064323.5:openURL()
#@+node:vpe.20060426062042:colorizeURLs()
def colorizeURLs(tag,keywords):
    c = keywords.get("c")
    if not c: return

    c.frame.body.tag_configure("URL", underline=1, foreground="blue")
    gui = g.app.gui ; w = c.frame.body.bodyCtrl
    s = gui.getAllText(w)
    lines = s.split('\n')
    n = 0 # The number of characters before the present line.
    for line in lines:
        for match in url_regex.finditer(line):
            start, end = match.start(), match.end()
            i,j = gui.toGuiIndex(s,w,n+start),gui.toGuiIndex(s,w,n+end)
            c.frame.body.tag_add('URL',i,j)
        n += len(line) + 1
#@-node:vpe.20060426062042:colorizeURLs()
#@-others

if 1:
    leoPlugins.registerHandler("bodydclick1", openURL)
    leoPlugins.registerHandler("select2", colorizeURLs)
    g.plugin_signon(__name__)
#@-node:ekr.20060506070443.1:@thin detect_urls.py
#@-leo
