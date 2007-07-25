#@+leo-ver=4-thin
#@+node:mork.20041018204908.1:@thin multifile.py
#@<< docstring >>
#@+node:ekr.20050226114732:<< docstring >>
'''Multipath enables the ability to write a file to multiple locations.

It acts as a post-write mechanism, a file must be written to the filesystem for
it to work. At this point it is not a replacement for @path or an absolute path,
it works in tandem with them.

To use, place @multipath at the start of a line in the root node or an ancestor
of the node. The format is (On Unixy systems)::

    @multipath /machine/unit/:/machine/robot/:/machine/

New in version 0.6 of this plugin: the separator used above is ';' not ':',
for example:

    @multipath c:\prog\test;c:\prog\unittest

It will places copy of the written file in each of these directories.

There is an additional directive that simplifies common paths, it is called
@multiprefix. By typing @multiprefix with a path following it, before a
@multipath directive you set the beginning of the paths in the @multipath
directive.

For example: (note I put # in front of the directives here because I
dont want someone browsing this file to accidentilly save mulitple copies of
this file to their system :) )

#@verbatim
#@multiprefix /leo #@multipath /plugins 

or

#@verbatim
#@multiprefix /leo/
#@verbatim
#@multipath plugins: fungus : drain

copies a file to /leo/plugins /leo/fungus /leo/drain.

The @multiprefix stays in effect for the entire tree until reset with another
@multiprefix directive. @multipath is cumulitive, in that for each @multipath in
an ancestor a copy of the file is created. These directives must at the
beginning of the line and by themselves.
'''
#@nonl
#@-node:ekr.20050226114732:<< docstring >>
#@nl

#@@language python
#@@tabwidth -4

#@<< imports >>
#@+node:ekr.20050226114732.1:<< imports >>
import leoGlobals as g 

import leoAtFile
import leoPlugins

import os.path
import shutil
import sys

try:
    import tkFileDialog
    import weakref
    ok = True
except ImportError:
    ok = False
#@nonl
#@-node:ekr.20050226114732.1:<< imports >>
#@nl

__version__ = ".9"
#@<< version history >>
#@+node:ekr.20050226115130:<< version history >>
#@@killcolor
#@+at
# 0.3 EKR:
# - Added init method.
# - Minor code reorg.  The actual code is unchanged.
# 0.4 EKR: Changed 'new_c' logic to 'c' logic.
# 0.5 EKR: Use 'new' and 'open2' hooks to call addMenu.
# 0.6 EKR: Made it work with Leo 4.4.2.
# - Made all uses of leoAtFile explicit.
# - Simplified code by using g.funcToMethod in init code.
# - Renamed decoratedOpenFileForWriting to match openFileForWriting.
# - Rewrote stop and scanForMultiPath methods.
# 0.7 EKR: Use absolute filename for original file to avoid problems with 
# current directory.
# 0.8 EKR:
# * The path separator in @multipath directives is ';', not ':' as previously.
# - Fixed several bugs in scanForMultiPath.
# 0.9 EKR: add entries to g.globalDirectiveList so that this plugin will work 
# with the new colorizer.
#@-at
#@nonl
#@-node:ekr.20050226115130:<< version history >>
#@nl

multiprefix = '@multiprefix'   
multipath = '@multipath'
haveseen = {}   
files = {}

#@+others
#@+node:ekr.20050226115130.1:init & helpers
def init ():

    global ok
    if ok:
        if g.app.gui is None:
            g.app.createTkGui(__file__)
        ok = g.app.gui.guiName() == "tkinter"
        if ok:
            #import leoGlobals # Append to the module list, not to the g.copy.
            g.globalDirectiveList.append('multipath')
            g.globalDirectiveList.append('multiprefix')

            # Override all instances of leoAtFile.atFile.
            at = leoAtFile.atFile
            global originalOpenFileForWriting ; originalOpenFileForWriting = at.openFileForWriting
            g.funcToMethod(decoratedOpenFileForWriting,at,name='openFileForWriting')

            # leoPlugins.registerHandler('save1',start)
            leoPlugins.registerHandler('save2',stop)
            leoPlugins.registerHandler(('new','start2'),addMenu)
            g.plugin_signon(__name__)

    return ok
#@nonl
#@+node:mork.20041019091317:addMenu
haveseen = weakref.WeakKeyDictionary()

def addMenu (tag,keywords):

    c = keywords.get('c')
    if not c or haveseen.has_key(c):
        return
    haveseen [c] = None
    men = c.frame.menu
    men = men.getMenu('Edit')
    men.add_command(
        label = "Insert Directory String",
        command = lambda c = c: insertDirectoryString(c))
#@nonl
#@-node:mork.20041019091317:addMenu
#@+node:mork.20041019091524:insertDirectoryString
def insertDirectoryString (c):

    dir = tkFileDialog.askdirectory()
    if dir:
        w = c.frame.body.bodyCtrl
        w.insert('insert',dir)
        w.event_generate('<Key>')
        w.update_idletasks()
#@nonl
#@-node:mork.20041019091524:insertDirectoryString
#@-node:ekr.20050226115130.1:init & helpers
#@+node:mork.20041018204908.3:decoratedOpenFileForWriting
def decoratedOpenFileForWriting (self,root,fileName,toString):

    c = self.c

    # Call the original method.
    global originalOpenFileForWriting
    val = originalOpenFileForWriting(self,root,fileName,toString)

    # Save a pointer to the root for later.
    if root.isDirty(): files [fileName] = root.copy()

    # Return whatever the original method returned.
    return val 
#@-node:mork.20041018204908.3:decoratedOpenFileForWriting
#@+node:mork.20041018204908.6:stop
def stop (tag,keywords):

    c = keywords.get('c')
    if not c:
        g.trace('can not happen')
        return

    multi = scanForMultiPath(c)
    # g.trace(g.dictToString(multi))

    for fileName in multi.keys():
        paths = multi [fileName]
        for path in paths:
            try:
                if os.path.isdir(path):
                    shutil.copy2(fileName,path)
                    g.es("multifile:\nWrote %s to %s" % (fileName,path),color="blue")
                else:
                    g.es("multifile:\n%s is not a directory, not writing %s" % (path,fileName),color="red")
            except:
                g.es("multifile:\nCant write %s to %s" % (fileName,path),color="red")
                g.es_exception_type()
    files.clear()
#@nonl
#@-node:mork.20041018204908.6:stop
#@+node:mork.20041018204908.5:scanForMultiPath
def scanForMultiPath (c):

    '''Return a dictionary whose keys are fileNames and whose values are
    lists of paths to which the fileName is to be written.
    New in version 0.6 of this plugin: use ';' to separate paths in @multipath statements.'''

    global multiprefix, multipath
    at = c.atFileCommands ; sep = ';' ; d = {}
    for fileName in files.keys(): # Keys are fileNames, values are root positions.
        root = files[fileName]
        at.scanDefaultDirectory(root) # Using root here may be dubious.
        fileName = g.os_path_join(at.default_directory,fileName)
        # g.trace(fileName,at.default_directory)
        positions = [p.copy() for p in root.self_and_parents_iter()]
        positions.reverse()
        prefix = ''
        for p in positions:
            lines = p.bodyString().split('\n')
            # Calculate the prefix fisrt.
            for s in lines:
                if s.startswith(multiprefix):
                    prefix = s[len(multiprefix):].strip()
            # Handle the paths after the prefix is in place.
            for s in lines:
                if s.startswith(multipath):
                    s = s[len(multipath):].strip()
                    paths = s.split(sep)
                    paths = [z.strip() for z in paths]
                    if prefix:
                        paths = [g.os_path_join(at.default_directory,prefix,z) for z in paths]
                    else:
                        paths = [g.os_path_join(at.default_directory,z) for z in paths]
                    aList = d.get(fileName,[])
                    aList.extend(paths)
                    # g.trace(fileName,aList)
                    d[fileName] = aList
    return d
#@nonl
#@-node:mork.20041018204908.5:scanForMultiPath
#@-others
#@nonl
#@-node:mork.20041018204908.1:@thin multifile.py
#@-leo
