#@+leo-ver=4-thin
#@+node:edream.110203113231.669:@thin import_cisco_config.py
#@<< docstring >>
#@+node:ekr.20050912180321:<< docstring >>
'''This plugin adds a menu item under the File->Import menu to import
Cisco configuration files.

The plugin will:

1)  Create a new node, under the current node, where the configuration will be
    written. This node will typically have references to several sections (see below).

2)  Create sections (child nodes) for the indented blocks present in the original
    config file. These child nodes will have sub-nodes grouping similar blocks (e.g.
    there will be an 'interface' child node, with as many sub-nodes as there are real
    interfaces in the configuration file).

3)  Create sections for the custom keywords specified in the customBlocks[] list in
    importCiscoConfig(). You can modify this list to specify different keywords. DO
    NOT put keywords that are followed by indented blocks (these are taken care of by
    point 2 above). The negated form of the keywords (for example, if the keyword is
    'service', the negated form is 'no service') is also included in the sections.
    
    
4)  Not display consecutive empty comment lines (lines with only a '!').

All created sections are alphabetically ordered.
'''
#@nonl
#@-node:ekr.20050912180321:<< docstring >>
#@nl

#@@language python
#@@tabwidth -4

#@<< imports >>
#@+node:ekr.20050111085909:<< imports >>
import leoGlobals as g
import leoPlugins

tkFileDialog = g.importExtension('tkFileDialog',pluginName=__name__,verbose=True)
#@nonl
#@-node:ekr.20050111085909:<< imports >>
#@nl
__version__ = "1.5"
#@<< version history >>
#@+node:ekr.20050311102853:<< version history >>
#@@killcolor
#@+at
# 
# 1.4 EKR:
# - Added init function.
# - Use only 'new' and 'open2' hooks.
# 1.5 EKR:
# - Removed all calls to g.top().
# - Fixed bug: return ok in init.
#@-at
#@nonl
#@-node:ekr.20050311102853:<< version history >>
#@nl

#@+others
#@+node:ekr.20050311102853.1:init
def init ():
    
    ok = tkFileDialog is not None
    
    if ok:
        if g.app.gui is None:
            g.app.createTkGui(__file__)
    
        if g.app.gui.guiName() == "tkinter":
            leoPlugins.registerHandler(('new','open2'),create_import_cisco_menu)
            g.plugin_signon(__name__)
            
    return ok
#@nonl
#@-node:ekr.20050311102853.1:init
#@+node:edream.110203113231.671:create_import_cisco_menu
def create_import_cisco_menu (tag,keywords):

    c = keywords.get('c')
    if not c or not c.exists: return
    
    importMenu = c.frame.menu.getMenu('import')
    
    def importCiscoConfigCallback(event=None,c=c):
        importCiscoConfig(c)

    newEntries = (
        ("-",None,None),
        ("Import C&isco Configuration","Shift+Ctrl+I",importCiscoConfigCallback))

    c.frame.menu.createMenuEntries(importMenu,newEntries,dynamicMenu=True)
#@nonl
#@-node:edream.110203113231.671:create_import_cisco_menu
#@+node:edream.110203113231.672:importCiscoConfig
def importCiscoConfig(c):

    if not c or not c.exists: return
    current = c.currentPosition()
    #@    << open file >>
    #@+node:edream.110203113231.673:<< open file >>
    name = tkFileDialog.askopenfilename(
        title="Import Cisco Configuration File",
        filetypes=[("All files", "*")]
        )
    if name == "":	return
    
    p = current.insertAsNthChild(0)
    c.beginUpdate()
    p.setHeadString("cisco config: %s" % name)
    c.endUpdate()
    
    try:
        fh = open(name)
        g.es("importing: %s" % name)
        linelist = fh.read().splitlines()
        fh.close()
    except IOError,msg:
        g.es("error reading %s: %s" % (name, msg))
        return
    #@nonl
    #@-node:edream.110203113231.673:<< open file >>
    #@nl

    # define which additional child nodes will be created
    # these keywords must NOT be followed by indented blocks
    customBlocks = ['aaa','ip as-path','ip prefix-list','ip route',
                    'ip community-list','access-list','snmp-server','ntp',
                    'boot','service','logging']
    out = []
    blocks = {}
    children = []
    lines = len(linelist)
    i = 0
    skipToNextLine = 0
    # create level-0 and level-1 children
    while i<(lines-1):
        for customLine in customBlocks:
            if (linelist[i].startswith(customLine) or
                linelist[i].startswith('no %s' % customLine)):
                #@                << process custom line >>
                #@+node:edream.110203113231.674:<< process custom line >>
                if not blocks.has_key(customLine):
                    blocks[customLine] = []
                    out.append(g.angleBrackets(customLine))
                    # create first-level child
                    child = p.insertAsNthChild(0)
                    child.setHeadStringOrHeadline(g.angleBrackets(customLine))
                    children.append(child)
                
                blocks[customLine].append(linelist[i])
                #@nonl
                #@-node:edream.110203113231.674:<< process custom line >>
                #@nl
                skipToNextLine = 1
                break
        if skipToNextLine:
            skipToNextLine = 0
        else:
            if linelist[i+1].startswith(' '):
                #@                << process indented block >>
                #@+node:edream.110203113231.675:<< process indented block >>
                space = linelist[i].find(' ')
                if space == -1:
                    space = len(linelist[i])
                key = linelist[i][:space]
                if not blocks.has_key(key):
                    blocks[key] = []
                    out.append(g.angleBrackets(key))
                    # create first-level child
                    child = p.insertAsNthChild(0)
                    child.setHeadStringOrHeadline(g.angleBrackets(key))
                    children.append(child)
                
                value = [linelist[i]]
                # loop through the indented lines
                i = i+1
                try:
                    while linelist[i].startswith(' '):
                        value.append(linelist[i])
                        i = i+1
                except:
                    # EOF
                    pass
                i = i-1 # restore index
                # now add the value to the dictionary
                blocks[key].append(value)
                #@nonl
                #@-node:edream.110203113231.675:<< process indented block >>
                #@nl
            else:
                out.append(linelist[i])
        i=i+1
    # process last line
    out.append(linelist[i])
    
    #@    << complete outline >>
    #@+node:edream.110203113231.676:<< complete outline >>
    # first print the level-0 text
    outClean = []
    prev = ''
    for line in out:
        if line=='!' and prev=='!':
            pass # skip repeated comment lines
        else:
            outClean.append(line)
        prev = line
    p.setBodyStringOrPane('\n'.join(outClean))
    
    # scan through the created outline and add children
    for child in children:
        # extract the key from the headline. Uhm... :)
        key = child.headString().split('<<'
            )[1].split('>>')[0].strip()
        if blocks.has_key(key):
            if type(blocks[key][0]) == type(''):
                # it's a string, no sub-children, so just print the text
                child.setBodyStringOrPane('\n'.join(blocks[key]))
            else:
                # it's a multi-level node
                for value in blocks[key]:
                    # each value is a list containing the headline and then the text
                    subchild = child.insertAsNthChild(0)
                    subchild.setHeadStringOrHeadline(value[0])
                    subchild.setBodyStringOrPane('\n'.join(value))
            child.sortChildren()
        else:
            # this should never happen
            g.es("Unknown key: %s" % key)
    p.sortChildren()
    #@nonl
    #@-node:edream.110203113231.676:<< complete outline >>
    #@nl
#@nonl
#@-node:edream.110203113231.672:importCiscoConfig
#@-others
#@nonl
#@-node:edream.110203113231.669:@thin import_cisco_config.py
#@-leo
