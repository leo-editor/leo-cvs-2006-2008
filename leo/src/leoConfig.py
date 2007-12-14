#@+leo-ver=4-thin
#@+node:ekr.20041117062700:@thin leoConfig.py
#@@language python
#@@tabwidth -4
#@@pagewidth 80

#@<< imports >>
#@+node:ekr.20041227063801:<< imports >>
import leoGlobals as g
import leoGui

import sys
#@-node:ekr.20041227063801:<< imports >>
#@nl

#@<< class parserBaseClass >>
#@+node:ekr.20041119203941.2:<< class parserBaseClass >>
class parserBaseClass:

    """The base class for settings parsers."""

    #@    << parserBaseClass data >>
    #@+node:ekr.20041121130043:<< parserBaseClass data >>
    # These are the canonicalized names.  Case is ignored, as are '_' and '-' characters.

    basic_types = [
        # Headlines have the form @kind name = var
        'bool','color','directory','int','ints',
        'float','path','ratio','shortcut','string','strings']

    control_types = [
        'abbrev','enabledplugins','font','if','ifgui','ifplatform','ignore','mode',
        'openwith','page','settings','shortcuts',
        'buttons','menus', # New in Leo 4.4.4.
        ]

    # Keys are settings names, values are (type,value) tuples.
    settingsDict = {}
    #@-node:ekr.20041121130043:<< parserBaseClass data >>
    #@nl

    #@    @+others
    #@+node:ekr.20041119204700: ctor (parserBaseClass)
    def __init__ (self,c):

        self.c = c
        self.recentFiles = [] # List of recent files.
        self.shortcutsDict = {}
            # Keys are cononicalized shortcut names, values are bunches.
        self.openWithList = []
            # A list of dicts containing 'name','shortcut','command' keys.

        # Keys are canonicalized names.
        self.dispatchDict = {
            'abbrev':       self.doAbbrev, # New in 4.4.1 b2.
            'bool':         self.doBool,
            'buttons':      self.doButtons, # New in 4.4.4
            'color':        self.doColor,
            'directory':    self.doDirectory,
            'enabledplugins': self.doEnabledPlugins,
            'font':         self.doFont,
            'if':           self.doIf,
            # 'ifgui':        self.doIfGui,  # Removed in 4.4 b3.
            'ifplatform':   self.doIfPlatform,
            'ignore':       self.doIgnore,
            'int':          self.doInt,
            'ints':         self.doInts,
            'float':        self.doFloat,
            'menus':        self.doMenus, # New in 4.4.4
            'mode':         self.doMode, # New in 4.4b1.
            'openwith':     self.doOpenWith, # New in 4.4.3 b1.
            'path':         self.doPath,
            'page':         self.doPage,
            'ratio':        self.doRatio,
            # 'shortcut':     self.doShortcut, # Removed in 4.4.1 b1.
            'shortcuts':    self.doShortcuts,
            'string':       self.doString,
            'strings':      self.doStrings,
        }
    #@-node:ekr.20041119204700: ctor (parserBaseClass)
    #@+node:ekr.20060102103625:createModeCommand
    def createModeCommand (self,name,modeDict):

        commandName = 'enter-' + name
        commandName = commandName.replace(' ','-')

        # g.trace(name,len(modeDict.keys()))

        # Save the info for k.finishCreate and k.makeAllBindings.
        d = g.app.config.modeCommandsDict

        # New in 4.4.1 b2: silently allow redefinitions of modes.
        d [commandName] = modeDict
    #@-node:ekr.20060102103625:createModeCommand
    #@+node:ekr.20041120103012:error
    def error (self,s):

        print s

        # Does not work at present because we are using a null Gui.
        g.es(s,color="blue")
    #@-node:ekr.20041120103012:error
    #@+node:ekr.20041120094940:kind handlers (parserBaseClass)
    #@+node:ekr.20060608221203:doAbbrev
    def doAbbrev (self,p,kind,name,val):

        d = {}
        s = p.bodyString()
        lines = g.splitLines(s)
        for line in lines:
            line = line.strip()
            if line and not g.match(line,0,'#'):
                name,val = self.parseAbbrevLine(line)
                if name: d [val] = name

        self.set (p,'abbrev','abbrev',d)
    #@-node:ekr.20060608221203:doAbbrev
    #@+node:ekr.20041120094940.1:doBool
    def doBool (self,p,kind,name,val):

        if val in ('True','true','1'):
            self.set(p,kind,name,True)
        elif val in ('False','false','0'):
            self.set(p,kind,name,False)
        else:
            self.valueError(p,kind,name,val)
    #@-node:ekr.20041120094940.1:doBool
    #@+node:ekr.20070925144337:doButtons
    def doButtons (self,p,kind,name,val):

        # __pychecker__ = '--no-argsused' # kind,name,val not used.

        aList = [] ; c = self.c ; tag = '@button'
        for p in p.subtree_iter():
            h = p.headString()
            if g.match_word(h,0,tag):
                # We can not assume that p will be valid when it is used.
                script = g.getScript(c,p,useSelectedText=False,forcePythonSentinels=True,useSentinels=True)
                aList.append((p.headString(),script),)

        # g.trace(g.listToString([h for h,script in aList]))

        # This setting is handled differently from most other settings,
        # because the last setting must be retrieved before any commander exists.
        g.app.config.buttonsList = aList
        g.app.config.buttonsFileName = c and c.shortFileName() or '<no settings file>'

    #@-node:ekr.20070925144337:doButtons
    #@+node:ekr.20041120094940.2:doColor
    def doColor (self,p,kind,name,val):

        # At present no checking is done.
        val = val.lstrip('"').rstrip('"')
        val = val.lstrip("'").rstrip("'")

        self.set(p,kind,name,val)
    #@-node:ekr.20041120094940.2:doColor
    #@+node:ekr.20041120094940.3:doDirectory & doPath
    def doDirectory (self,p,kind,name,val):

        # At present no checking is done.
        self.set(p,kind,name,val)

    doPath = doDirectory
    #@-node:ekr.20041120094940.3:doDirectory & doPath
    #@+node:ekr.20070224075914:doEnabledPlugins
    def doEnabledPlugins (self,p,kind,name,val):

        # __pychecker__ = '--no-argsused' # kind,name,val not used.

        c = self.c
        s = p.bodyString()

        # This setting is handled differently from all other settings,
        # because the last setting must be retrieved before any commander exists.

        # g.trace('len(s)',len(s))

        # Set the global config ivars.
        g.app.config.enabledPluginsString = s
        g.app.config.enabledPluginsFileName = c and c.shortFileName() or '<no settings file>'
    #@-node:ekr.20070224075914:doEnabledPlugins
    #@+node:ekr.20041120094940.6:doFloat
    def doFloat (self,p,kind,name,val):

        try:
            val = float(val)
            self.set(p,kind,name,val)
        except ValueError:
            self.valueError(p,kind,name,val)
    #@-node:ekr.20041120094940.6:doFloat
    #@+node:ekr.20041120094940.4:doFont
    def doFont (self,p,kind,name,val):

        # __pychecker__ = '--no-argsused' # kind not used.

        d = self.parseFont(p)

        # Set individual settings.
        for key in ('family','size','slant','weight'):
            data = d.get(key)
            if data is not None:
                name,val = data
                setKind = key
                self.set(p,setKind,name,val)
    #@-node:ekr.20041120094940.4:doFont
    #@+node:ekr.20041120103933:doIf
    def doIf(self,p,kind,name,val):

        # __pychecker__ = '--no-argsused' # args not used.

        g.trace("'if' not supported yet")
        return None
    #@-node:ekr.20041120103933:doIf
    #@+node:ekr.20041121125416:doIfGui
    #@+at 
    #@nonl
    # Alas, @if-gui can't be made to work. The problem is that plugins can set
    # g.app.gui, but plugins need settings so the leoSettings.leo files must 
    # be parsed
    # before g.app.gui.guiName() is known.
    #@-at
    #@@c

    if 0:

        def doIfGui (self,p,kind,name,val):

            # __pychecker__ = '--no-argsused' # args not used.

            # g.trace(repr(name))

            if not g.app.gui or not g.app.gui.guiName():
                s = '@if-gui has no effect: g.app.gui not defined yet'
                g.es_print(s,color='blue')
                return "skip"
            elif g.app.gui.guiName().lower() == name.lower():
                return None
            else:
                return "skip"
    #@-node:ekr.20041121125416:doIfGui
    #@+node:ekr.20041120104215:doIfPlatform
    def doIfPlatform (self,p,kind,name,val):

        # __pychecker__ = '--no-argsused' # args not used.

        # g.trace(sys.platform,repr(name))

        if sys.platform.lower() == name.lower():
            return None
        else:
            return "skip"
    #@-node:ekr.20041120104215:doIfPlatform
    #@+node:ekr.20041120104215.1:doIgnore
    def doIgnore(self,p,kind,name,val):

        return "skip"
    #@-node:ekr.20041120104215.1:doIgnore
    #@+node:ekr.20041120094940.5:doInt
    def doInt (self,p,kind,name,val):

        try:
            val = int(val)
            self.set(p,kind,name,val)
        except ValueError:
            self.valueError(p,kind,name,val)
    #@-node:ekr.20041120094940.5:doInt
    #@+node:ekr.20041217132253:doInts
    def doInts (self,p,kind,name,val):

        '''We expect either:
        @ints [val1,val2,...]aName=val
        @ints aName[val1,val2,...]=val'''

        name = name.strip() # The name indicates the valid values.
        i = name.find('[')
        j = name.find(']')

        # g.trace(kind,name,val)

        if -1 < i < j:
            items = name[i+1:j]
            items = items.split(',')
            name = name[:i]+name[j+1:].strip()
            # g.trace(name,items)
            try:
                items = [int(item.strip()) for item in items]
            except ValueError:
                items = []
                self.valueError(p,'ints[]',name,val)
                return
            kind = "ints[%s]" % (','.join([str(item) for item in items]))
            try:
                val = int(val)
            except ValueError:
                self.valueError(p,'int',name,val)
                return
            if val not in items:
                self.error("%d is not in %s in %s" % (val,kind,name))
                return

            # g.trace(repr(kind),repr(name),val)

            # At present no checking is done.
            self.set(p,kind,name,val)
    #@-node:ekr.20041217132253:doInts
    #@+node:ekr.20070925144337.2:doMenus & helper
    def doMenus (self,p,kind,name,val):

        # __pychecker__ = '--no-argsused' # kind,name,val not used.

        c = self.c ; aList = [] ; tag = '@menu'
        p = p.copy() ; after = p.nodeAfterTree()
        while p and p != after:
            h = p.headString()
            if g.match_word(h,0,tag):
                name = h[len(tag):].strip()
                if name:
                    for z in aList:
                        name2,junk,junk = z
                        if name2 == name:
                            self.error('Replacing previous @menu %s' % (name))
                            break
                    aList2 = []
                    kind = '%s %s' % (tag,name)
                    self.doItems(p,aList2)
                    aList.append((kind,aList2,None),)
                    p.moveToNodeAfterTree()
                else:
                    p.moveToThreadNext()
            else:
                p.moveToThreadNext()

        # This setting is handled differently from most other settings,
        # because the last setting must be retrieved before any commander exists.
        # self.dumpMenuList(aList)
        # g.trace(g.listToString(aList))
        # g.es_print('creating menu from %s' % (c.shortFileName()),color='blue')
        g.app.config.menusList = aList
        g.app.config.menusFileName = c and c.shortFileName() or '<no settings file>'
    #@+node:ekr.20070926141716:doItems
    def doItems (self,p,aList):

        p = p.copy() ; after = p.nodeAfterTree()
        p.moveToThreadNext()
        while p and p != after:
            h = p.headString()
            for tag in ('@menu','@item'):
                if g.match_word(h,0,tag):
                    itemName = h[len(tag):].strip()
                    if itemName:
                        if tag == '@menu':
                            aList2 = []
                            kind = '%s %s' % (tag,itemName)
                            self.doItems(p,aList2)
                            aList.append((kind,aList2,None),)
                            p.moveToNodeAfterTree()
                            break
                        else:
                            kind = tag
                            head = itemName
                            body = p.bodyString()
                            aList.append((kind,head,body),)
                            p.moveToThreadNext()
                            break
            else:
                # g.trace('***skipping***',p.headString())
                p.moveToThreadNext()
    #@nonl
    #@-node:ekr.20070926141716:doItems
    #@+node:ekr.20070926142312:dumpMenuList
    def dumpMenuList (self,aList,level=0):

        for z in aList:
            kind,val,val2 = z
            if kind == '@item':
                g.trace(level,kind,val,val2)
            else:
                print
                g.trace(level,kind,'...')
                self.dumpMenuList(val,level+1)
    #@nonl
    #@-node:ekr.20070926142312:dumpMenuList
    #@-node:ekr.20070925144337.2:doMenus & helper
    #@+node:ekr.20060102103625.1:doMode (ParserBaseClass)
    def doMode(self,p,kind,name,val):

        '''Parse an @mode node and create the enter-<name>-mode command.'''

        # __pychecker__ = '--no-argsused' # val not used.

        c = self.c ; k = c.k

        # g.trace('%20s' % (name),c.fileName())
        #@    << Compute modeName >>
        #@+node:ekr.20060618110649:<< Compute modeName >>
        name = name.strip().lower()
        j = name.find(' ')
        if j > -1: name = name[:j]
        if name.endswith('mode'):
            name = name[:-4].strip()
        if name.endswith('-'):
            name = name[:-1]
        modeName = name + '-mode'
        #@-node:ekr.20060618110649:<< Compute modeName >>
        #@nl

        # Create a local shortcutsDict.
        old_d = self.shortcutsDict
        d = self.shortcutsDict = {}

        s = p.bodyString()
        lines = g.splitLines(s)
        for line in lines:
            line = line.strip()
            if line and not g.match(line,0,'#'):
                name,bunch = self.parseShortcutLine(line)
                if not name:
                    # An entry command: put it in the special *entry-commands* key.
                    aList = d.get('*entry-commands*',[])
                    aList.append(bunch.entryCommandName)
                    d ['*entry-commands*'] = aList
                elif bunch is not None:
                    # A regular shortcut.
                    bunch.val = k.strokeFromSetting(bunch.val)
                    bunch.pane = modeName
                    bunchList = d.get(name,[])
                    # Important: use previous bindings if possible.
                    key2,bunchList2 = c.config.getShortcut(name)
                    bunchList3 = [b for b in bunchList2 if b.pane != modeName]
                    if bunchList3:
                        # g.trace('inheriting',[b.val for b in bunchList3])
                        bunchList.extend(bunchList3)
                    bunchList.append(bunch)
                    d [name] = bunchList
                    self.set(p,"shortcut",name,bunchList)
                    self.setShortcut(name,bunchList)

        # Restore the global shortcutsDict.
        self.shortcutsDict = old_d

        # Create the command, but not any bindings to it.
        self.createModeCommand(modeName,d)
    #@-node:ekr.20060102103625.1:doMode (ParserBaseClass)
    #@+node:ekr.20070411101643.1:doOpenWith (ParserBaseClass)
    def doOpenWith (self,p,kind,name,val):

        # g.trace('kind',kind,'name',name,'val',val,'c',self.c)

        d = self.parseOpenWith(p)
        d['name']=name
        d['shortcut']=val
        name = kind = 'openwithtable'
        self.openWithList.append(d)
        self.set(p,kind,name,self.openWithList)
    #@-node:ekr.20070411101643.1:doOpenWith (ParserBaseClass)
    #@+node:ekr.20041120104215.2:doPage
    def doPage(self,p,kind,name,val):

        pass # Ignore @page this while parsing settings.
    #@-node:ekr.20041120104215.2:doPage
    #@+node:ekr.20041121125741:doRatio
    def doRatio (self,p,kind,name,val):

        try:
            val = float(val)
            if 0.0 <= val <= 1.0:
                self.set(p,kind,name,val)
            else:
                self.valueError(p,kind,name,val)
        except ValueError:
            self.valueError(p,kind,name,val)
    #@-node:ekr.20041121125741:doRatio
    #@+node:ekr.20041120105609:doShortcuts (ParserBaseClass)
    def doShortcuts(self,p,kind,name,val,s=None):

        # __pychecker__ = '--no-argsused' # kind,val.

        # g.trace(self.c.fileName(),name)

        c = self.c ; d = self.shortcutsDict
        if s is None: s = p.bodyString()
        lines = g.splitLines(s)
        for line in lines:
            line = line.strip()
            if line and not g.match(line,0,'#'):
                name,bunch = self.parseShortcutLine(line)
                if bunch is not None:
                    # A regular shortcut.
                    bunchList = d.get(name,[])
                    bunchList.append(bunch)
                    d [name] = bunchList
                    self.set(p,"shortcut",name,bunchList)
                    self.setShortcut(name,bunchList)
    #@-node:ekr.20041120105609:doShortcuts (ParserBaseClass)
    #@+node:ekr.20041217132028:doString
    def doString (self,p,kind,name,val):

        # At present no checking is done.
        self.set(p,kind,name,val)
    #@-node:ekr.20041217132028:doString
    #@+node:ekr.20041120094940.8:doStrings
    def doStrings (self,p,kind,name,val):

        '''We expect one of the following:
        @strings aName[val1,val2...]=val
        @strings [val1,val2,...]aName=val'''

        name = name.strip()
        i = name.find('[')
        j = name.find(']')

        if -1 < i < j:
            items = name[i+1:j]
            items = items.split(',')
            items = [item.strip() for item in items]
            name = name[:i]+name[j+1:].strip()
            kind = "strings[%s]" % (','.join(items))
            # g.trace(repr(kind),repr(name),val)

            # At present no checking is done.
            self.set(p,kind,name,val)
    #@-node:ekr.20041120094940.8:doStrings
    #@-node:ekr.20041120094940:kind handlers (parserBaseClass)
    #@+node:ekr.20041124063257:munge
    def munge(self,s):

        return g.app.config.canonicalizeSettingName(s)
    #@-node:ekr.20041124063257:munge
    #@+node:ekr.20041119204700.2:oops
    def oops (self):
        print ("parserBaseClass oops:",
            g.callers(),
            "must be overridden in subclass")
    #@-node:ekr.20041119204700.2:oops
    #@+node:ekr.20041213082558:parsers
    #@+node:ekr.20041213083651:fontSettingNameToFontKind
    def fontSettingNameToFontKind (self,name):

        s = name.strip()
        if s:
            for tag in ('_family','_size','_slant','_weight'):
                if s.endswith(tag):
                    return tag[1:]

        return None
    #@-node:ekr.20041213083651:fontSettingNameToFontKind
    #@+node:ekr.20041213082558.1:parseFont & helper
    def parseFont (self,p):

        d = {
            'comments': [],
            'family': None,
            'size': None,
            'slant': None,
            'weight': None,
        }

        s = p.bodyString()
        lines = g.splitLines(s)

        for line in lines:
            self.parseFontLine(line,d)

        comments = d.get('comments')
        d['comments'] = '\n'.join(comments)

        return d
    #@+node:ekr.20041213082558.2:parseFontLine
    def parseFontLine (self,line,d):

        s = line.strip()
        if not s: return

        try:
            s = str(s)
        except UnicodeError:
            pass

        if g.match(s,0,'#'):
            s = s[1:].strip()
            comments = d.get('comments')
            comments.append(s)
            d['comments'] = comments
        else:
            # name is everything up to '='
            i = s.find('=')
            if i == -1:
                name = s ; val = None
            else:
                name = s[:i].strip()
                val = s[i+1:].strip()
                val = val.lstrip('"').rstrip('"')
                val = val.lstrip("'").rstrip("'")

            fontKind = self.fontSettingNameToFontKind(name)
            if fontKind:
                d[fontKind] = name,val # Used only by doFont.
    #@-node:ekr.20041213082558.2:parseFontLine
    #@-node:ekr.20041213082558.1:parseFont & helper
    #@+node:ekr.20041119205148:parseHeadline
    def parseHeadline (self,s):

        """Parse a headline of the form @kind:name=val
        Return (kind,name,val)."""

        kind = name = val = None

        if g.match(s,0,'@'):
            i = g.skip_id(s,1,chars='-')
            kind = s[1:i].strip()
            if kind:
                # name is everything up to '='
                j = s.find('=',i)
                if j == -1:
                    name = s[i:].strip()
                else:
                    name = s[i:j].strip()
                    # val is everything after the '='
                    val = s[j+1:].strip()

        # g.trace("%50s %10s %s" %(name,kind,val))
        return kind,name,val
    #@-node:ekr.20041119205148:parseHeadline
    #@+node:ekr.20070411101643.2:parseOpenWith & helper
    def parseOpenWith (self,p):

        d = {'command': None,}

        s = p.bodyString()
        lines = g.splitLines(s)

        for line in lines:
            self.parseOpenWithLine(line,d)

        return d
    #@+node:ekr.20070411101643.4:parseOpenWithLine
    def parseOpenWithLine (self,line,d):

        s = line.strip()
        if not s: return

        try:
            s = str(s)
        except UnicodeError:
            pass

        if not g.match(s,0,'#'):
            d['command'] = s
    #@-node:ekr.20070411101643.4:parseOpenWithLine
    #@-node:ekr.20070411101643.2:parseOpenWith & helper
    #@+node:ekr.20041120112043:parseShortcutLine (g.app.config)
    def parseShortcutLine (self,s):

        '''Parse a shortcut line.  Valid forms:

        --> entry-command
        settingName = shortcut
        settingName ! paneName = shortcut
        command-name -> mode-name = binding
        command-name -> same = binding
        '''

        name = val = nextMode = None ; nextMode = 'none'
        i = g.skip_ws(s,0)

        if g.match(s,i,'-->'): # New in 4.4.1 b1: allow mode-entry commands.
            j = g.skip_ws(s,i+3)
            i = g.skip_id(s,j,'-')
            entryCommandName = s[j:i]
            return None,g.Bunch(entryCommandName=entryCommandName)

        j = i
        i = g.skip_id(s,j,'-') # New in 4.4: allow Emacs-style shortcut names.
        name = s[j:i]
        if not name: return None,None

        # New in Leo 4.4b2.
        i = g.skip_ws(s,i)
        if g.match(s,i,'->'): # New in 4.4: allow pane-specific shortcuts.
            j = g.skip_ws(s,i+2)
            i = g.skip_id(s,j)
            nextMode = s[j:i]

        i = g.skip_ws(s,i)
        if g.match(s,i,'!'): # New in 4.4: allow pane-specific shortcuts.
            j = g.skip_ws(s,i+1)
            i = g.skip_id(s,j)
            pane = s[j:i]
            if not pane.strip(): pane = 'all'
        else: pane = 'all'

        i = g.skip_ws(s,i)
        if g.match(s,i,'='):
            i = g.skip_ws(s,i+1)
            val = s[i:]

        # New in 4.4: Allow comments after the shortcut.
        # Comments must be preceded by whitespace.
        comment = ''
        if val:
            i = val.find('#')
            if i > 0 and val[i-1] in (' ','\t'):
                # comment = val[i:].strip()
                val = val[:i].strip()

        # g.trace(pane,name,val,s)
        return name,g.bunch(nextMode=nextMode,pane=pane,val=val)
    #@-node:ekr.20041120112043:parseShortcutLine (g.app.config)
    #@+node:ekr.20060608222828:parseAbbrevLine (g.app.config)
    def parseAbbrevLine (self,s):

        '''Parse an abbreviation line:
        command-name = abbreviation
        return (command-name,abbreviation)
        '''

        i = j = g.skip_ws(s,0)
        i = g.skip_id(s,i,'-') # New in 4.4: allow Emacs-style shortcut names.
        name = s[j:i]
        if not name: return None,None

        i = g.skip_ws(s,i)
        if not g.match(s,i,'='): return None,None

        i = g.skip_ws(s,i+1)
        val = s[i:].strip()
        # Ignore comments after the shortcut.
        i = val.find('#')
        if i > -1: val = val[:i].strip()

        if val: return name,val
        else:   return None,None
    #@-node:ekr.20060608222828:parseAbbrevLine (g.app.config)
    #@-node:ekr.20041213082558:parsers
    #@+node:ekr.20041120094940.9:set (parseBaseClass)
    def set (self,p,kind,name,val):

        """Init the setting for name to val."""

        # __pychecker__ = '--no-argsused' # p used in subclasses, not here.

        c = self.c ; key = self.munge(name)
        # if kind and kind.startswith('setting'): g.trace("settingsParser %10s %15s %s" %(kind,val,name))
        d = self.settingsDict
        bunch = d.get(key)
        if bunch:
            # g.trace(key,bunch.val,bunch.path)
            path = bunch.path
            if g.os_path_abspath(c.mFileName) != g.os_path_abspath(path):
                g.es("over-riding setting: %s from %s" % (name,path))

        # N.B.  We can't use c here: it may be destroyed!
        d [key] = g.Bunch(path=c.mFileName,kind=kind,val=val,tag='setting')

    #@-node:ekr.20041120094940.9:set (parseBaseClass)
    #@+node:ekr.20041227071423:setShortcut (ParserBaseClass)
    def setShortcut (self,name,bunch):

        c = self.c

        # None is a valid value for val.
        key = c.frame.menu.canonicalizeMenuName(name)
        rawKey = key.replace('&','')
        self.set(c,rawKey,"shortcut",bunch)

        # g.trace(bunch.pane,rawKey,bunch.val)
    #@-node:ekr.20041227071423:setShortcut (ParserBaseClass)
    #@+node:ekr.20041119204700.1:traverse (parserBaseClass)
    def traverse (self):

        c = self.c

        p = g.app.config.settingsRoot(c)
        if not p:
            # g.trace('no settings tree for %s' % c)
            return None

        self.settingsDict = {}
        self.shortcutsDict = {}
        after = p.nodeAfterTree()
        while p and p != after:
            result = self.visitNode(p)
            # g.trace(result,p.headString())
            if result == "skip":
                if 0:
                    s = 'skipping settings in %s' % p.headString()
                    g.es_print(s,color='blue')
                p.moveToNodeAfterTree()
            else:
                p.moveToThreadNext()

        return self.settingsDict
    #@-node:ekr.20041119204700.1:traverse (parserBaseClass)
    #@+node:ekr.20041120094940.10:valueError
    def valueError (self,p,kind,name,val):

        """Give an error: val is not valid for kind."""

        # __pychecker__ = '--no-argsused' # p not used, but needed.

        self.error("%s is not a valid %s for %s" % (val,kind,name))
    #@-node:ekr.20041120094940.10:valueError
    #@+node:ekr.20041119204700.3:visitNode (must be overwritten in subclasses)
    def visitNode (self,p):

        # __pychecker__ = '--no-argsused' # p not used, but needed.

        self.oops()
    #@-node:ekr.20041119204700.3:visitNode (must be overwritten in subclasses)
    #@-others
#@-node:ekr.20041119203941.2:<< class parserBaseClass >>
#@nl

#@+others
#@+node:ekr.20041119203941:class configClass
class configClass:
    """A class to manage configuration settings."""
    #@    << class data >>
    #@+node:ekr.20041122094813:<<  class data >>
    #@+others
    #@+node:ekr.20041117062717.1:defaultsDict
    #@+at 
    #@nonl
    # This contains only the "interesting" defaults.
    # Ints and bools default to 0, floats to 0.0 and strings to "".
    #@-at
    #@@c

    defaultBodyFontSize = g.choose(sys.platform=="win32",9,12)
    defaultLogFontSize  = g.choose(sys.platform=="win32",8,12)
    defaultMenuFontSize = g.choose(sys.platform=="win32",9,12)
    defaultTreeFontSize = g.choose(sys.platform=="win32",9,12)

    defaultsDict = {'_hash':'defaultsDict'}

    defaultsData = (
        # compare options...
        ("ignore_blank_lines","bool",True),
        ("limit_count","int",9),
        ("print_mismatching_lines","bool",True),
        ("print_trailing_lines","bool",True),
        # find/change options...
        ("search_body","bool",True),
        ("whole_word","bool",True),
        # Prefs panel.
        ("default_target_language","language","python"),
        ("target_language","language","python"), # Bug fix: 6/20,2005.
        ("tab_width","int",-4),
        ("page_width","int",132),
        ("output_doc_chunks","bool",True),
        ("tangle_outputs_header","bool",True),
        # Syntax coloring options...
        # Defaults for colors are handled by leoColor.py.
        ("color_directives_in_plain_text","bool",True),
        ("underline_undefined_section_names","bool",True),
        # Window options...
        ("allow_clone_drags","bool",True),
        ("body_pane_wraps","bool",True),
        ("body_text_font_family","family","Courier"),
        ("body_text_font_size","size",defaultBodyFontSize),
        ("body_text_font_slant","slant","roman"),
        ("body_text_font_weight","weight","normal"),
        ("enable_drag_messages","bool",True),
        ("headline_text_font_family","string",None),
        ("headline_text_font_size","size",defaultLogFontSize),
        ("headline_text_font_slant","slant","roman"),
        ("headline_text_font_weight","weight","normal"),
        ("log_text_font_family","string",None),
        ("log_text_font_size","size",defaultLogFontSize),
        ("log_text_font_slant","slant","roman"),
        ("log_text_font_weight","weight","normal"),
        ("initial_window_height","int",600),
        ("initial_window_width","int",800),
        ("initial_window_left","int",10),
        ("initial_window_top","int",10),
        ("initial_splitter_orientation","string","vertical"),
        ("initial_vertical_ratio","ratio",0.5),
        ("initial_horizontal_ratio","ratio",0.3),
        ("initial_horizontal_secondary_ratio","ratio",0.5),
        ("initial_vertical_secondary_ratio","ratio",0.7),
        ("outline_pane_scrolls_horizontally","bool",False),
        ("split_bar_color","color","LightSteelBlue2"),
        ("split_bar_relief","relief","groove"),
        ("split_bar_width","int",7),
    )
    #@-node:ekr.20041117062717.1:defaultsDict
    #@+node:ekr.20041118062709:define encodingIvarsDict
    encodingIvarsDict = {'_hash':'encodingIvarsDict'}

    encodingIvarsData = (
        ("default_derived_file_encoding","string","utf-8"),
        ("new_leo_file_encoding","string","UTF-8"),
            # Upper case for compatibility with previous versions.
        ("tkEncoding","string",None),
            # Defaults to None so it doesn't override better defaults.
    )
    #@-node:ekr.20041118062709:define encodingIvarsDict
    #@+node:ekr.20041117072055:ivarsDict
    # Each of these settings sets the corresponding ivar.
    # Also, the c.configSettings settings class inits the corresponding commander ivar.
    ivarsDict = {'_hash':'ivarsDict'}

    ivarsData = (
        ("at_root_bodies_start_in_doc_mode","bool",True),
            # For compatibility with previous versions.
        ("create_nonexistent_directories","bool",False),
        ("output_initial_comment","string",""),
            # "" for compatibility with previous versions.
        ("output_newline","string","nl"),
        ("page_width","int","132"),
        ("read_only","bool",True),
            # Make sure we don't alter an illegal leoConfig.txt file!
        ("redirect_execute_script_output_to_log_pane","bool",False),
        ("relative_path_base_directory","string","!"),
        ("remove_sentinels_extension","string",".txt"),
        ("save_clears_undo_buffer","bool",False),
        ("stylesheet","string",None),
        ("tab_width","int",-4),
        ("target_language","language","python"), # Bug fix: added: 6/20/2005.
        ("trailing_body_newlines","string","asis"),
        ("use_plugins","bool",True),
            # New in 4.3: use_plugins = True by default.
        # use_pysco can not be set by 4.3:  config processing happens too late.
            # ("use_psyco","bool",False),
        ("undo_granularity","string","word"),
            # "char","word","line","node"
        ("write_strips_blank_lines","bool",False),
    )
    #@-node:ekr.20041117072055:ivarsDict
    #@-others

    # List of dictionaries to search.  Order not too important.
    dictList = [ivarsDict,encodingIvarsDict,defaultsDict]

    # Keys are commanders.  Values are optionsDicts.
    localOptionsDict = {}

    localOptionsList = []

    # Keys are setting names, values are type names.
    warningsDict = {} # Used by get() or allies.
    #@-node:ekr.20041122094813:<<  class data >>
    #@nl
    #@    @+others
    #@+node:ekr.20041117083202:Birth... (g.app.config)
    #@+node:ekr.20041117062717.2:ctor (configClass)
    def __init__ (self):

        self.buttonsList = []
        self.buttonsFileName = ''
        self.configsExist = False # True when we successfully open a setting file.
        self.defaultFont = None # Set in gui.getDefaultConfigFont.
        self.defaultFontFamily = None # Set in gui.getDefaultConfigFont.
        self.enabledPluginsFileName = None
        self.enabledPluginsString = '' 
        self.globalConfigFile = None # Set in initSettingsFiles
        self.homeFile = None # Set in initSettingsFiles
        self.inited = False
        self.menusList = []
        self.menusFileName = ''
        self.modeCommandsDict = {} # For use by @mode logic. Keys are command names, values are g.Bunches.
        self.myGlobalConfigFile = None
        self.myHomeConfigFile = None
        self.recentFilesFiles = [] # List of g.Bunches describing .leoRecentFiles.txt files.
        self.write_recent_files_as_needed = False # Will be set later.
        self.silent = g.app.silentMode
        # g.trace('c.config.silent',self.silent)

        # Inited later...
        self.panes = None
        self.sc = None
        self.tree = None

        self.initDicts()
        self.initIvarsFromSettings()
        self.initSettingsFiles()
        self.initRecentFiles()
    #@-node:ekr.20041117062717.2:ctor (configClass)
    #@+node:ekr.20041227063801.2:initDicts
    def initDicts (self):

        # Only the settings parser needs to search all dicts.
        self.dictList = [self.defaultsDict]

        for key,kind,val in self.defaultsData:
            self.defaultsDict[self.munge(key)] = g.Bunch(
                setting=key,kind=kind,val=val,tag='defaults')

        for key,kind,val in self.ivarsData:
            self.ivarsDict[self.munge(key)] = g.Bunch(
                ivar=key,kind=kind,val=val,tag='ivars')

        for key,kind,val in self.encodingIvarsData:
            self.encodingIvarsDict[self.munge(key)] = g.Bunch(
                ivar=key,kind=kind,encoding=val,tag='encodings')
    #@-node:ekr.20041227063801.2:initDicts
    #@+node:ekr.20041117065611.2:initIvarsFromSettings & helpers
    def initIvarsFromSettings (self):

        for ivar in self.encodingIvarsDict.keys():
            if ivar != '_hash':
                self.initEncoding(ivar)

        for ivar in self.ivarsDict.keys():
            if ivar != '_hash':
                self.initIvar(ivar)
    #@+node:ekr.20041117065611.1:initEncoding
    def initEncoding (self,key):

        '''Init g.app.config encoding ivars during initialization.'''

        # N.B. The key is munged.
        bunch = self.encodingIvarsDict.get(key)
        encoding = bunch.encoding
        ivar = bunch.ivar
        # g.trace('g.app.config',ivar,encoding)
        setattr(self,ivar,encoding)

        if encoding and not g.isValidEncoding(encoding):
            g.es("g.app.config: bad encoding: %s: %s" % (ivar,encoding))
    #@-node:ekr.20041117065611.1:initEncoding
    #@+node:ekr.20041117065611:initIvar
    def initIvar(self,key):

        '''Init g.app.config ivars during initialization.

        This does NOT init the corresponding commander ivars.

        Such initing must be done in setIvarsFromSettings.'''

        # N.B. The key is munged.
        bunch = self.ivarsDict.get(key)
        ivar = bunch.ivar # The actual name of the ivar.
        val = bunch.val

        # g.trace('g.app.config',ivar,key,val)
        setattr(self,ivar,val)
    #@-node:ekr.20041117065611:initIvar
    #@-node:ekr.20041117065611.2:initIvarsFromSettings & helpers
    #@+node:ekr.20041117083202.2:initRecentFiles
    def initRecentFiles (self):

        self.recentFiles = []
    #@-node:ekr.20041117083202.2:initRecentFiles
    #@+node:ekr.20041117083857:initSettingsFiles
    def initSettingsFiles (self):

        """Set self.globalConfigFile, self.homeFile, self.machineConfigFile and self.myConfigFile."""

        settingsFile = 'leoSettings.leo'
        mySettingsFile = 'myLeoSettings.leo'
        machineConfigFile = self.getMachineName()

        for ivar,theDir,fileName in (
            ('globalConfigFile',    g.app.globalConfigDir,  settingsFile),
            ('homeFile',            g.app.homeDir,          settingsFile),
            ('myGlobalConfigFile',  g.app.globalConfigDir,  mySettingsFile),
            ('myHomeConfigFile',    g.app.homeDir,          mySettingsFile),
            ('machineConfigFile',   g.app.homeDir,          machineConfigFile),
        ):
            # The same file may be assigned to multiple ivars:
            # readSettingsFiles checks for such duplications.
            path = g.os_path_join(theDir,fileName)
            if g.os_path_exists(path):
                setattr(self,ivar,path)
            else:
                setattr(self,ivar,None)
        if 0:
            g.trace('global file:',self.globalConfigFile)
            g.trace('home file:',self.homeFile)
            g.trace('myGlobal file:',self.myGlobalConfigFile)
            g.trace('myHome file:',self.myHomeConfigFile)
    #@nonl
    #@+node:ekr.20071211112804:getMachineName
    def getMachineName (self):

        try:
            import os
            name = os.getenv('HOSTNAME')
            if not name:
                name = os.getenv('COMPUTERNAME')
            if not name:
                import socket
                name = socket.gethostname()
        except Exception:
            name = ''

        if name:
            name +='LeoSettings.leo'

        # g.trace(name)

        return name
    #@-node:ekr.20071211112804:getMachineName
    #@-node:ekr.20041117083857:initSettingsFiles
    #@-node:ekr.20041117083202:Birth... (g.app.config)
    #@+node:ekr.20041117081009:Getters... (g.app.config)
    #@+node:ekr.20041123070429:canonicalizeSettingName (munge)
    def canonicalizeSettingName (self,name):

        if name is None:
            return None

        name = name.lower()
        for ch in ('-','_',' ','\n'):
            name = name.replace(ch,'')

        return g.choose(name,name,None)

    munge = canonicalizeSettingName
    #@-node:ekr.20041123070429:canonicalizeSettingName (munge)
    #@+node:ekr.20041123092357:config.findSettingsPosition
    def findSettingsPosition (self,c,setting):

        """Return the position for the setting in the @settings tree for c."""

        munge = self.munge

        root = self.settingsRoot(c)
        if not root:
            return c.nullPosition()

        setting = munge(setting)

        for p in root.subtree_iter():
            h = munge(p.headString())
            if h == setting:
                return p.copy()

        return c.nullPosition()
    #@-node:ekr.20041123092357:config.findSettingsPosition
    #@+node:ekr.20041117083141:get & allies (g.app.config)
    def get (self,c,setting,kind):

        """Get the setting and make sure its type matches the expected type."""

        if c:
            d = self.localOptionsDict.get(c.hash())
            if d:
                val,junk = self.getValFromDict(d,setting,kind)
                if val is not None:
                    # g.trace(c.shortFileName(),setting,val)
                    return val

        for d in self.localOptionsList:
            val,junk = self.getValFromDict(d,setting,kind)
            if val is not None:
                kind = d.get('_hash','<no hash>')
                # g.trace(kind,setting,val)
                return val

        for d in self.dictList:
            val,junk = self.getValFromDict(d,setting,kind)
            if val is not None:
                kind = d.get('_hash','<no hash>')
                # g.trace(kind,setting,val)
                return val

        return None
    #@+node:ekr.20041121143823:getValFromDict
    def getValFromDict (self,d,setting,requestedType,warn=True):

        '''Look up the setting in d. If warn is True, warn if the requested type
        does not (loosely) match the actual type.
        returns (val,exists)'''

        bunch = d.get(self.munge(setting))
        if not bunch: return None,False

        # g.trace(setting,requestedType,bunch.toString())
        val = bunch.val
        if not self.typesMatch(bunch.kind,requestedType):
            # New in 4.4: make sure the types match.
            # A serious warning: one setting may have destroyed another!
            # Important: this is not a complete test of conflicting settings:
            # The warning is given only if the code tries to access the setting.
            if warn:
                s = (
                    'Warning: ignoring %s:%s not %s\n' +
                    'There may be conflicting settings!')
                g.es_print(s % (bunch.kind,setting,requestedType),color='red')
                # g.trace(g.callers())
            return None, False
        elif val in (u'None',u'none','None','none','',None):
            return None, True # Exists, but is None
        else:
            # g.trace(setting,val)
            return val, True
    #@-node:ekr.20041121143823:getValFromDict
    #@+node:ekr.20051015093141:typesMatch
    def typesMatch (self,type1,type2):

        '''
        Return True if type1, the actual type, matches type2, the requeseted type.

        The following equivalences are allowed:

        - None matches anything.
        - An actual type of string or strings matches anything.
        - Shortcut matches shortcuts.
        '''

        shortcuts = ('shortcut','shortcuts',)

        return (
            type1 == None or type2 == None or
            type1.startswith('string') or
            type1 == 'int' and type2 == 'size' or
            (type1 in shortcuts and type2 in shortcuts) or
            type1 == type2
        )
    #@-node:ekr.20051015093141:typesMatch
    #@-node:ekr.20041117083141:get & allies (g.app.config)
    #@+node:ekr.20051011105014:exists (g.app.config)
    def exists (self,c,setting,kind):

        '''Return true if a setting of the given kind exists, even if it is None.'''

        if c:
            d = self.localOptionsDict.get(c.hash())
            if d:
                junk,found = self.getValFromDict(d,setting,kind)
                if found: return True

        for d in self.localOptionsList:
            junk,found = self.getValFromDict(d,setting,kind)
            if found: return True

        for d in self.dictList:
            junk,found = self.getValFromDict(d,setting,kind)
            if found: return True

        # g.trace('does not exist',setting,kind)
        return False
    #@-node:ekr.20051011105014:exists (g.app.config)
    #@+node:ekr.20060608224112:getAbbrevDict
    def getAbbrevDict (self,c):

        """Search all dictionaries for the setting & check it's type"""

        d = self.get(c,'abbrev','abbrev')
        return d or {}
    #@-node:ekr.20060608224112:getAbbrevDict
    #@+node:ekr.20041117081009.3:getBool
    def getBool (self,c,setting,default=None):

        """Search all dictionaries for the setting & check it's type"""

        val = self.get(c,setting,"bool")

        if val in (True,False):
            return val
        else:
            return default
    #@-node:ekr.20041117081009.3:getBool
    #@+node:ekr.20070926082018:getButtons
    def getButtons (self):

        return g.app.config.buttonsList
    #@-node:ekr.20070926082018:getButtons
    #@+node:ekr.20041122070339:getColor
    def getColor (self,c,setting):

        """Search all dictionaries for the setting & check it's type"""

        return self.get(c,setting,"color")
    #@-node:ekr.20041122070339:getColor
    #@+node:ekr.20041117093009.1:getDirectory
    def getDirectory (self,c,setting):

        """Search all dictionaries for the setting & check it's type"""

        theDir = self.getString(c,setting)

        if g.os_path_exists(theDir) and g.os_path_isdir(theDir):
             return theDir
        else:
            return None
    #@-node:ekr.20041117093009.1:getDirectory
    #@+node:ekr.20070224075914.1:getEnabledPlugins
    def getEnabledPlugins (self):

        return g.app.config.enabledPluginsString
    #@-node:ekr.20070224075914.1:getEnabledPlugins
    #@+node:ekr.20041117082135:getFloat
    def getFloat (self,c,setting):

        """Search all dictionaries for the setting & check it's type"""

        val = self.get(c,setting,"float")
        try:
            val = float(val)
            return val
        except TypeError:
            return None
    #@-node:ekr.20041117082135:getFloat
    #@+node:ekr.20041117062717.13:getFontFromParams (config)
    def getFontFromParams(self,c,family,size,slant,weight,defaultSize=12):

        """Compute a font from font parameters.

        Arguments are the names of settings to be use.
        We default to size=12, slant="roman", weight="normal".

        We return None if there is no family setting so we can use system default fonts."""

        family = self.get(c,family,"family")
        if family in (None,""):
            family = self.defaultFontFamily

        size = self.get(c,size,"size")
        if size in (None,0): size = defaultSize

        slant = self.get(c,slant,"slant")
        if slant in (None,""): slant = "roman"

        weight = self.get(c,weight,"weight")
        if weight in (None,""): weight = "normal"

        # g.trace(g.callers(3),family,size,slant,weight,g.shortFileName(c.mFileName))

        return g.app.gui.getFontFromParams(family,size,slant,weight)
    #@-node:ekr.20041117062717.13:getFontFromParams (config)
    #@+node:ekr.20041117081513:getInt
    def getInt (self,c,setting):

        """Search all dictionaries for the setting & check it's type"""

        val = self.get(c,setting,"int")
        try:
            val = int(val)
            return val
        except TypeError:
            return None
    #@-node:ekr.20041117081513:getInt
    #@+node:ekr.20041117093009.2:getLanguage
    def getLanguage (self,c,setting):

        """Return the setting whose value should be a language known to Leo."""

        language = self.getString(c,setting)
        # g.trace(setting,language)

        return language
    #@-node:ekr.20041117093009.2:getLanguage
    #@+node:ekr.20070926070412:getMenusDict
    def getMenusList (self):

        return g.app.config.menusList
    #@nonl
    #@-node:ekr.20070926070412:getMenusDict
    #@+node:ekr.20070411101643:getOpenWith
    def getOpenWith (self,c):

        """Search all dictionaries for the setting & check it's type"""

        val = self.get(c,'openwithtable','openwithtable')

        return val
    #@-node:ekr.20070411101643:getOpenWith
    #@+node:ekr.20041122070752:getRatio
    def getRatio (self,c,setting):

        """Search all dictionaries for the setting & check it's type"""

        val = self.get(c,setting,"ratio")
        try:
            val = float(val)
            if 0.0 <= val <= 1.0:
                return val
            else:
                return None
        except TypeError:
            return None
    #@-node:ekr.20041122070752:getRatio
    #@+node:ekr.20041117062717.11:getRecentFiles
    def getRecentFiles (self):

        return self.recentFiles
    #@-node:ekr.20041117062717.11:getRecentFiles
    #@+node:ekr.20041117062717.14:getShortcut (config)
    def getShortcut (self,c,shortcutName):

        '''Return rawKey,accel for shortcutName'''

        key = c.frame.menu.canonicalizeMenuName(shortcutName)
        key = key.replace('&','') # Allow '&' in names.

        bunchList = self.get(c,key,"shortcut")
        if bunchList:
            bunchList = [bunch for bunch in bunchList
                if bunch.val and bunch.val.lower() != 'none']
            return key,bunchList
        else:
            return key,[]
    #@-node:ekr.20041117062717.14:getShortcut (config)
    #@+node:ekr.20041117081009.4:getString
    def getString (self,c,setting):

        """Search all dictionaries for the setting & check it's type"""

        return self.get(c,setting,"string")
    #@-node:ekr.20041117081009.4:getString
    #@+node:ekr.20041117062717.17:setCommandsIvars
    # Sets ivars of c that can be overridden by leoConfig.txt

    def setCommandsIvars (self,c):

        data = (
            ("default_tangle_directory","tangle_directory","directory"),
            ("default_target_language","target_language","language"),
            ("output_doc_chunks","output_doc_flag","bool"),
            ("page_width","page_width","int"),
            ("run_tangle_done.py","tangle_batch_flag","bool"),
            ("run_untangle_done.py","untangle_batch_flag","bool"),
            ("tab_width","tab_width","int"),
            ("tangle_outputs_header","use_header_flag","bool"),
        )

        for setting,ivar,theType in data:
            val = g.app.config.get(c,setting,theType)
            if val is None:
                if not hasattr(c,setting):
                    setattr(c,setting,None)
                    # g.trace(setting,None)
            else:
                setattr(c,setting,val)
                # g.trace(setting,val)
    #@-node:ekr.20041117062717.17:setCommandsIvars
    #@+node:ekr.20041120074536:settingsRoot
    def settingsRoot (self,c):

        # g.trace(c,c.rootPosition())

        for p in c.allNodes_iter():
            if p.headString().rstrip() == "@settings":
                return p.copy()
        else:
            return c.nullPosition()
    #@-node:ekr.20041120074536:settingsRoot
    #@-node:ekr.20041117081009:Getters... (g.app.config)
    #@+node:ekr.20041118084146:Setters (g.app.config)
    #@+node:ekr.20041118084146.1:set (g.app.config)
    def set (self,c,setting,kind,val):

        '''Set the setting.  Not called during initialization.'''

        # if kind.startswith('setting'): g.trace(val)

        found = False ;  key = self.munge(setting)
        if c:
            d = self.localOptionsDict.get(c.hash())
            if d: found = True

        if not found:
            theHash = c.hash()
            for d in self.localOptionsList:
                hash2 = d.get('_hash')
                if theHash == hash2:
                    found = True ; break

        if not found:
            d = self.dictList [0]

        d[key] = g.Bunch(setting=setting,kind=kind,val=val,tag='setting')

        if 0:
            dkind = d.get('_hash','<no hash: %s>' % c.hash())
            g.trace(dkind,setting,kind,val)
    #@-node:ekr.20041118084146.1:set (g.app.config)
    #@+node:ekr.20041118084241:setString
    def setString (self,c,setting,val):

        self.set(c,setting,"string",val)
    #@-node:ekr.20041118084241:setString
    #@+node:ekr.20041228042224:setIvarsFromSettings (g.app.config)
    def setIvarsFromSettings (self,c):

        '''Init g.app.config ivars or c's ivars from settings.

        - Called from readSettingsFiles with c = None to init g.app.config ivars.
        - Called from c.__init__ to init corresponding commmander ivars.'''

        # Ingore temporary commanders created by readSettingsFiles.
        if not self.inited: return

        # g.trace(c)
        d = self.ivarsDict
        for key in d:
            if key != '_hash':
                bunch = d.get(key)
                if bunch:
                    ivar = bunch.ivar # The actual name of the ivar.
                    kind = bunch.kind
                    val = self.get(c,key,kind) # Don't use bunch.val!
                    if c:
                        # g.trace("%20s %s = %s" % (g.shortFileName(c.mFileName),ivar,val))
                        setattr(c,ivar,val)
                    else:
                        # g.trace("%20s %s = %s" % ('g.app.config',ivar,val))
                        setattr(self,ivar,val)
    #@-node:ekr.20041228042224:setIvarsFromSettings (g.app.config)
    #@+node:ekr.20041201080436:appendToRecentFiles (g.app.config)
    def appendToRecentFiles (self,files):

        files = [theFile.strip() for theFile in files]

        # g.trace(files)

        def munge(name):
            name = name or ''
            return g.os_path_normpath(name).lower()

        for name in files:
            # Remove all variants of name.
            for name2 in self.recentFiles:
                if munge(name) == munge(name2):
                    self.recentFiles.remove(name2)

            self.recentFiles.append(name)
    #@-node:ekr.20041201080436:appendToRecentFiles (g.app.config)
    #@-node:ekr.20041118084146:Setters (g.app.config)
    #@+node:ekr.20041117093246:Scanning @settings (g.app.config)
    #@+node:ekr.20041120064303:g.app.config.readSettingsFiles & helpers
    def readSettingsFiles (self,fileName,verbose=True):

        seen = []
        self.write_recent_files_as_needed = False # Will be set later.
        #@    << define localDirectory, localConfigFile & myLocalConfigFile >>
        #@+node:ekr.20061028082834:<< define localDirectory, localConfigFile & myLocalConfigFile >>
        # This can't be done in initSettingsFiles because the local directory does not exits.
        localDirectory = g.os_path_dirname(fileName)

        #  Set the local leoSettings.leo file.
        localConfigFile = g.os_path_join(localDirectory,'leoSettings.leo')
        if not g.os_path_exists(localConfigFile):
            localConfigFile = None

        # Set the local myLeoSetting.leo file.
        myLocalConfigFile = g.os_path_join(localDirectory,'myLeoSettings.leo')
        if not g.os_path_exists(myLocalConfigFile):
            myLocalConfigFile = None
        #@nonl
        #@-node:ekr.20061028082834:<< define localDirectory, localConfigFile & myLocalConfigFile >>
        #@nl

        # Init settings from leoSettings.leo and myLeoSettings.leo files.
        for path,localFlag in (
            (self.globalConfigFile,False),
            (self.homeFile,False),
            (localConfigFile,False),
            (self.myGlobalConfigFile,False),
            (self.myHomeConfigFile,False),
            (self.machineConfigFile,False),
            (myLocalConfigFile,False),
            (fileName,True),
        ):
            if path and path.lower() not in seen:
                seen.append(path.lower())
                if verbose and not g.app.unitTesting and not self.silent and not g.app.batchMode:
                    s = 'reading settings in %s' % path
                    # This occurs early in startup, so use the following instead of g.es_print()
                    s = g.toEncodedString(s,'ascii')
                    print s
                    g.app.logWaiting.append((s+'\n','blue'),)

                c = self.openSettingsFile(path)
                if c:
                    self.updateSettings(c,localFlag)
                    g.app.destroyWindow(c.frame)
                    self.write_recent_files_as_needed = c.config.getBool('write_recent_files_as_needed')
                    self.setIvarsFromSettings(c)
        self.readRecentFiles(localConfigFile)
        self.inited = True
        self.setIvarsFromSettings(None)
    #@+node:ekr.20041117085625:g.app.config.openSettingsFile
    def openSettingsFile (self,path):

        theFile,isZipped = g.openLeoOrZipFile(path)
        if not theFile: return None

        # Similar to g.openWithFileName except it uses a null gui.
        # Changing g.app.gui here is a major hack.
        oldGui = g.app.gui
        g.app.gui = leoGui.nullGui("nullGui")
        c,frame = g.app.newLeoCommanderAndFrame(
            fileName=path,relativeFileName=None,
            initEditCommanders=False,updateRecentFiles=False)
        frame.log.enable(False)
        c.setLog()
        g.app.lockLog()
        ok = frame.c.fileCommands.open(
            theFile,path,readAtFileNodesFlag=False,silent=True) # closes theFile.
        g.app.unlockLog()
        frame.openDirectory = g.os_path_dirname(path)
        g.app.gui = oldGui
        return ok and c
    #@-node:ekr.20041117085625:g.app.config.openSettingsFile
    #@+node:ekr.20051013161232:g.app.config.updateSettings
    def updateSettings (self,c,localFlag):

        d = self.readSettings(c)

        if d:
            d['_hash'] = theHash = c.hash()
            if localFlag:
                self.localOptionsDict[theHash] = d
            else:
                self.localOptionsList.insert(0,d)

        if 0: # Good trace.
            if localFlag:
                g.trace(c.fileName())
                g.trace(d and d.keys())
    #@-node:ekr.20051013161232:g.app.config.updateSettings
    #@-node:ekr.20041120064303:g.app.config.readSettingsFiles & helpers
    #@+node:ekr.20041117083857.1:g.app.config.readSettings
    # Called to read all leoSettings.leo files.
    # Also called when opening an .leo file to read @settings tree.

    def readSettings (self,c):

        """Read settings from a file that may contain an @settings tree."""

        # g.trace(c.fileName())

        # Create a settings dict for c for set()
        if c and self.localOptionsDict.get(c.hash()) is None:
            self.localOptionsDict[c.hash()] = {}

        parser = settingsTreeParser(c)
        d = parser.traverse()

        return d
    #@-node:ekr.20041117083857.1:g.app.config.readSettings
    #@-node:ekr.20041117093246:Scanning @settings (g.app.config)
    #@+node:ekr.20050424114937.1:Reading and writing .leoRecentFiles.txt (g.app.config)
    #@+node:ekr.20070224115832:readRecentFiles & helpers
    def readRecentFiles (self,localConfigFile):

        '''Read all .leoRecentFiles.txt files.'''

        # The order of files in this list affects the order of the recent files list.
        seen = [] 
        localConfigPath = g.os_path_dirname(localConfigFile)
        for path in (
            g.app.homeDir,
            g.app.globalConfigDir,
            localConfigPath,
        ):
            if path and path not in seen:
                ok = self.readRecentFilesFile(path)
                if ok: seen.append(path)
        if not seen and self.write_recent_files_as_needed:
            self.createRecentFiles()
    #@nonl
    #@+node:ekr.20061010121944:createRecentFiles
    def createRecentFiles (self):

        '''Trye to reate .leoRecentFiles.txt in
        - the users home directory first,
        - Leo's config directory second.'''

        for theDir in (g.app.homeDir,g.app.globalConfigDir):
            if theDir:
                try:
                    fileName = g.os_path_join(theDir,'.leoRecentFiles.txt')
                    f = file(fileName,'w')
                    f.close()
                    g.es_print('created %s' % (fileName),color='red')
                    return
                except Exception:
                    g.es_print('can not create %s' % (fileName),color='red')
                    g.es_exception()
    #@nonl
    #@-node:ekr.20061010121944:createRecentFiles
    #@+node:ekr.20050424115658:readRecentFilesFile
    def readRecentFilesFile (self,path):

        fileName = g.os_path_join(path,'.leoRecentFiles.txt')
        ok = g.os_path_exists(fileName)
        if ok:
            if not g.unitTesting and not self.silent:
                print ('reading %s' % fileName)
            lines = file(fileName).readlines()
            if lines and self.munge(lines[0])=='readonly':
                lines = lines[1:]
            if lines:
                lines = [g.toUnicode(g.os_path_normpath(line),'utf-8') for line in lines]
                self.appendToRecentFiles(lines)

        return ok
    #@nonl
    #@-node:ekr.20050424115658:readRecentFilesFile
    #@-node:ekr.20070224115832:readRecentFiles & helpers
    #@+node:ekr.20050424114937.2:writeRecentFilesFile & helper
    recentFileMessageWritten = False

    def writeRecentFilesFile (self,c):

        '''Write the appropriate .leoRecentFiles.txt file.'''

        tag = '.leoRecentFiles.txt'

        if g.app.unitTesting:
            return

        localFileName = c.fileName()
        if localFileName:
            localPath,junk = g.os_path_split(localFileName)
        else:
            localPath = None

        written = False
        for path in (localPath,g.app.globalConfigDir,g.app.homeDir):
            if path:
                fileName = g.os_path_join(path,tag)
                if g.os_path_exists(fileName):
                    if not self.recentFileMessageWritten:
                        print ('wrote recent file: %s' % fileName)
                        written = True
                    self.writeRecentFilesFileHelper(fileName)
                    # Bug fix: Leo 4.4.6: write *all* recent files.

        if written:
            self.recentFileMessageWritten = True
        else:
            pass # g.trace('----- not found: %s' % g.os_path_join(localPath,tag))
    #@+node:ekr.20050424131051:writeRecentFilesFileHelper
    def writeRecentFilesFileHelper (self,fileName):
        # g.trace(fileName)

        # Don't update the file if it begins with read-only.
        theFile = None
        try:
            theFile = file(fileName)
            lines = theFile.readlines()
            if lines and self.munge(lines[0])=='readonly':
                # g.trace('read-only: %s' %fileName)
                return
        except IOError:
            # The user may have erased a file.  Not an error.
            if theFile: theFile.close()

        theFile = None
        try:
            # g.trace('writing',fileName)
            theFile = file(fileName,'w')
            if self.recentFiles:
                lines = [g.toEncodedString(line,'utf-8') for line in self.recentFiles]
                theFile.write('\n'.join(lines))
                # g.trace(fileName,'lines\n%s' % lines)
            else:
                theFile.write('\n')

        except IOError:
            # The user may have erased a file.  Not an error.
            pass

        except Exception:
            g.es('unexpected exception writing %s' % fileName,color='red')
            g.es_exception()

        if theFile:
            theFile.close()
    #@-node:ekr.20050424131051:writeRecentFilesFileHelper
    #@-node:ekr.20050424114937.2:writeRecentFilesFile & helper
    #@-node:ekr.20050424114937.1:Reading and writing .leoRecentFiles.txt (g.app.config)
    #@+node:ekr.20070418073400:g.app.config.printSettings & helper
    def printSettings (self,c):

        '''Prints the value of every setting, except key bindings and commands and open-with tables.
        The following letters indicate where the active setting came from:

        - D indicates default settings.
        - F indicates the file being loaded,
        - L indicates leoSettings.leo,
        - M indicates myLeoSettings.leo,
        '''

        settings = {} # Keys are setting names, values are (letter,val)

        if c:
            d = self.localOptionsDict.get(c.hash())
            self.printSettingsHelper(settings,d,letter='[F]')

        for d in self.localOptionsList:
            self.printSettingsHelper(settings,d)

        for d in self.dictList:
            self.printSettingsHelper(settings,d)

        keys = settings.keys() ; keys.sort()
        for key in keys:
            data = settings.get(key)
            letter,val = data
            print '%45s = %s %s' % (key,letter,val)
            g.es('%s %s = %s' % (letter,key,val))
    #@nonl
    #@+node:ekr.20070418075804:printSettingsHelper
    def printSettingsHelper(self,settings,d,letter=None):

        suppressKind = ('shortcut','shortcuts','openwithtable')
        suppressKeys = (None,'_hash','shortcut')

        if d:
            #@        << set letter >>
            #@+node:ekr.20070418084502:<< set letter >>
            theHash = d.get('_hash').lower()

            if letter:
                pass
            elif theHash.endswith('myleosettings.leo'):
                letter = '[M]'
            elif theHash.endswith('leosettings.leo'):
                letter = ' ' * 3
            else:
                letter = '[D]'

            # g.trace(letter,theHash)
            #@nonl
            #@-node:ekr.20070418084502:<< set letter >>
            #@nl
            for key in d.keys():
                if key not in suppressKeys and key not in settings.keys():
                    bunch = d.get(key)
                    if bunch.kind not in suppressKind:
                        settings[key] = (letter,bunch.val)
    #@nonl
    #@-node:ekr.20070418075804:printSettingsHelper
    #@-node:ekr.20070418073400:g.app.config.printSettings & helper
    #@-others
#@-node:ekr.20041119203941:class configClass
#@+node:ekr.20041119203941.3:class settingsTreeParser (parserBaseClass)
class settingsTreeParser (parserBaseClass):

    '''A class that inits settings found in an @settings tree.

    Used by read settings logic.'''

    #@    @+others
    #@+node:ekr.20041119204103:ctor
    def __init__ (self,c):

        # Init the base class.
        parserBaseClass.__init__(self,c)
    #@-node:ekr.20041119204103:ctor
    #@+node:ekr.20041119204714:visitNode (settingsTreeParser)
    def visitNode (self,p):

        """Init any settings found in node p."""

        # g.trace(p.headString())

        munge = g.app.config.munge

        kind,name,val = self.parseHeadline(p.headString())
        kind = munge(kind)

        if kind is None: # Not an @x node. (New in Leo 4.4.4)
            pass
        if kind == "settings":
            pass
        elif kind in self.basic_types and val in (u'None',u'none','None','none','',None):
            # None is valid for all basic types.
            self.set(p,kind,name,None)
        elif kind in self.control_types or kind in self.basic_types:
            f = self.dispatchDict.get(kind)
            try:
                return f(p,kind,name,val)
            except TypeError:
                g.es_exception()
                print "*** no handler",kind

        return None
    #@-node:ekr.20041119204714:visitNode (settingsTreeParser)
    #@-others
#@-node:ekr.20041119203941.3:class settingsTreeParser (parserBaseClass)
#@+node:ekr.20070627082044.906:Unit tests
#@+node:ekr.20070627082044.903:@@test ifgui
if g.unitTesting:
    guiname = g.app.gui.guiName()

    tkinter = c.config.getBool('test_tkinter_setting')
    wx      = c.config.getBool('test_wxWindows_setting')

    print guiname

    if guiname == 'tkinter':
        assert(tkinter)
        assert(not wx)

    if guiname == 'wxWindows':
        assert(not tkinter)
        assert(wx)
#@nonl
#@-node:ekr.20070627082044.903:@@test ifgui
#@-node:ekr.20070627082044.906:Unit tests
#@-others
#@-node:ekr.20041117062700:@thin leoConfig.py
#@-leo
