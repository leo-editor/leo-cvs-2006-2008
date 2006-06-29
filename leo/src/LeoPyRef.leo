<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet ekr_stylesheet?>
<leo_file>
<leo_header file_format="2" tnodes="0" max_tnode_index="9759" clone_windows="0"/>
<globals body_outline_ratio="0.516324062878">
	<global_window_position top="34" left="399" height="817" width="796"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="EKR.20040430162943"><vh>Notes</vh>
<v t="ekr.20031218072017.329"><vh>@thin ../doc/leoNotes.txt</vh></v>
</v>
<v t="EKR.20040519090151.3"><vh>Projects</vh>
<v t="EKR.20040429143933"><vh>@thin leoProjects.txt</vh></v>
</v>
<v t="ekr.20060624072803"><vh>4.4.1 b3 projects</vh>
<v t="ekr.20060624072803.1"><vh>Bugs fixed</vh>
<v t="ekr.20060624080605"><vh>Fixed recent bug: Ctrl-g does not work in @mode nodes</vh>
<v t="ekr.20060119150624"><vh>createModeBindings</vh></v>
<v t="ekr.20060117202916.1"><vh>initMode</vh></v>
<v t="ekr.20060102103625.1"><vh>doMode (ParserBaseClass)</vh>
<v t="ekr.20060618110649"><vh>&lt;&lt; Compute modeName &gt;&gt;</vh></v>
</v>
</v>
<v t="ekr.20060625061210"><vh>Update column display when typing</vh>
<v t="ekr.20060625072145"><vh>Report</vh></v>
<v t="ekr.20050920085536.65"><vh>masterCommand &amp; helpers</vh>
<v t="ekr.20050920085536.67"><vh>&lt;&lt; add character to history &gt;&gt;</vh></v>
<v t="ekr.20050923172809.1"><vh>callStateFunction</vh></v>
<v t="ekr.20050923174229.3"><vh>callKeystrokeFunction (not used)</vh></v>
<v t="ekr.20051026083544"><vh>handleDefaultChar</vh></v>
</v>
</v>
<v t="ekr.20060107082929"><vh>Fixed problem reporting indentation errors</vh>
<v t="ekr.20060624085200.1"><vh>Report</vh></v>
<v t="ekr.20031218072017.2140"><vh>c.executeScript</vh>
<v t="ekr.20031218072017.2143"><vh>&lt;&lt; redirect output &gt;&gt;</vh></v>
<v t="EKR.20040627100424"><vh>&lt;&lt; unredirect output &gt;&gt;</vh></v>
</v>
<v t="ekr.20060624085200"><vh>g.handleScriptException</vh>
<v t="EKR.20040612215018"><vh>&lt;&lt; dump the lines near the error &gt;&gt;</vh></v>
</v>
<v t="ekr.20031218072017.3112"><vh>es_exception &amp; test</vh>
<v t="ekr.20050220030850"><vh>test_g_es_exception</vh></v>
</v>
<v t="ekr.20040731204831"><vh>getLastTracebackFileAndLineNumber</vh></v>
</v>
<v t="ekr.20051104152338"><vh>Fixed bug in Remove Sentinels command</vh>
<v t="ekr.20051104152338.1"><vh>Report</vh></v>
<v t="ekr.20031218072017.3300"><vh>removeSentinelsCommand</vh>
<v t="ekr.20031218072017.3301"><vh>&lt;&lt; Read file into s &gt;&gt;</vh></v>
<v t="ekr.20031218072017.3302"><vh>&lt;&lt; set delims from the header line &gt;&gt;</vh></v>
<v t="ekr.20031218072017.1149"><vh>&lt;&lt; Write s into newFileName &gt;&gt;</vh></v>
</v>
<v t="ekr.20031218072017.3303"><vh>removeSentinelLines</vh></v>
</v>
<v t="ekr.20051014152256"><vh>Fixed long-standing bugs in import code</vh>
<v t="ekr.20060625173330"><vh>Report</vh></v>
<v t="ekr.20040930075711"><vh>Handle underindented lines</vh></v>
<v t="ekr.20060627063640"><vh>Handle long signature lines</vh></v>
<v t="ekr.20031218072017.3189"><vh>skip_matching_python_delims</vh></v>
<v t="ekr.20031218072017.2256"><vh>Python scanners &amp; tests</vh>
<v t="ekr.20031218072017.2257"><vh>scanPythonClass &amp; helpers</vh>
<v t="ekr.20031218072017.2258"><vh>&lt;&lt; set class_name and headline &gt;&gt;</vh></v>
<v t="ekr.20060626100102"><vh>scanPythonClassHelper</vh></v>
<v t="ekr.20060626101103.1"><vh>createParentText</vh></v>
<v t="ekr.20060626103415"><vh>createClassNodeText</vh></v>
</v>
<v t="ekr.20031218072017.2263"><vh>scanPythonDef</vh>
<v t="ekr.20031218072017.2264"><vh>&lt;&lt; set headline or return i &gt;&gt;</vh></v>
<v t="ekr.20031218072017.2266"><vh>&lt;&lt; Create def node &gt;&gt;</vh></v>
</v>
<v t="ekr.20031218072017.2267"><vh>scanPythonDecls</vh>
<v t="ekr.20031218072017.2268"><vh>&lt;&lt; break on def or class &gt;&gt;</vh></v>
<v t="ekr.20031218072017.2269"><vh>&lt;&lt; Create a child node for declarations &gt;&gt;</vh></v>
</v>
<v t="ekr.20031218072017.2270"><vh>scanPythonText</vh>
<v t="ekr.20031218072017.2271"><vh>&lt;&lt; handle possible Python function or class &gt;&gt;</vh></v>
<v t="ekr.20031218072017.2272"><vh>&lt;&lt; Append a reference to the methods of this file &gt;&gt;</vh></v>
<v t="ekr.20031218072017.2273"><vh>&lt;&lt; Append any unused python text to the parent's body text &gt;&gt;</vh></v>
</v>
<v t="ekr.20060626083237.1"><vh>skipPythonDef</vh>
<v t="ekr.20060627062652"><vh>&lt;&lt; skip the entire signature &gt;&gt;</vh></v>
</v>
<v t="ekr.20060626083237.2"><vh>test_skipPythonDef</vh>
<v t="ekr.20060626083725"><vh>&lt;&lt; define s &gt;&gt;</vh></v>
</v>
<v t="ekr.20060627063313"><vh>test_skipPythonDef2</vh>
<v t="ekr.20060627063313.1"><vh>&lt;&lt; define s &gt;&gt;</vh></v>
</v>
<v t="ekr.20060626100102.1"><vh>test_scanPythonClass</vh>
<v t="ekr.20060626100102.2"><vh>&lt;&lt; define s &gt;&gt;</vh></v>
</v>
</v>
</v>
<v t="ekr.20060120084705"><vh>Overwrite mode now works in headllines</vh>
<v t="ekr.20051026083544.2"><vh>updateHead</vh></v>
<v t="ekr.20051125080855"><vh>selfInsertCommand &amp; helpers</vh>
<v t="ekr.20051026171121"><vh>&lt;&lt; handle newline &gt;&gt;</vh></v>
<v t="ekr.20060627083506"><vh>flashMatchingBracketsHelper</vh></v>
<v t="ekr.20060627091557"><vh>flashCharacter</vh></v>
<v t="ekr.20051027172949"><vh>updateAutomatchBracket</vh></v>
<v t="ekr.20051026171121.1"><vh>udpateAutoIndent</vh></v>
<v t="ekr.20051026092433"><vh>updateTab</vh></v>
</v>
</v>
<v t="ekr.20060627141422"><vh>Fixed crasher in masterCommand</vh>
<v t="ekr.20050920085536.65"><vh>masterCommand &amp; helpers</vh>
<v t="ekr.20050920085536.67"><vh>&lt;&lt; add character to history &gt;&gt;</vh></v>
<v t="ekr.20050923172809.1"><vh>callStateFunction</vh></v>
<v t="ekr.20050923174229.3"><vh>callKeystrokeFunction (not used)</vh></v>
<v t="ekr.20051026083544"><vh>handleDefaultChar</vh></v>
</v>
</v>
<v t="ekr.20060628094329.1"><vh>Improved view-lossage command</vh>
<v t="ekr.20050920084036.83"><vh>viewLossage</vh></v>
<v t="ekr.20050920084036.63"><vh>watchEscape (Revise)</vh></v>
<v t="ekr.20050920085536.65"><vh>masterCommand &amp; helpers</vh>
<v t="ekr.20050920085536.67"><vh>&lt;&lt; add character to history &gt;&gt;</vh></v>
<v t="ekr.20050923172809.1"><vh>callStateFunction</vh></v>
<v t="ekr.20050923174229.3"><vh>callKeystrokeFunction (not used)</vh></v>
<v t="ekr.20051026083544"><vh>handleDefaultChar</vh></v>
</v>
</v>
</v>
<v t="ekr.20060624072803.2"><vh>New features</vh>
<v t="ekr.20060623064600"><vh>Finished repeat-complex-command</vh></v>
<v t="ekr.20060625072145.1"><vh>Read leoSettings.leo from the directory containing the .leo file</vh>
<v t="ekr.20060625072145.2"><vh>Request</vh></v>
<v t="ekr.20041117093246"><vh>Scanning @settings (g.app.config)</vh>
<v t="ekr.20041117085625"><vh>g.app.config.openSettingsFile</vh></v>
<v t="ekr.20041120064303"><vh>g.app.config.readSettingsFiles</vh></v>
<v t="ekr.20041117083857.1"><vh>g.app.config.readSettings</vh></v>
<v t="ekr.20051013161232"><vh>g.app.config.updateSettings</vh></v>
</v>
<v t="ekr.20031218072017.1934"><vh>run &amp; allies</vh>
<v t="ekr.20041219072112"><vh>&lt;&lt; import leoGlobals and leoApp &gt;&gt;</vh></v>
<v t="ekr.20041219072416.1"><vh>&lt;&lt; import leoNodes and leoConfig &gt;&gt;</vh></v>
<v t="ekr.20040411081633"><vh>&lt;&lt; start psycho &gt;&gt;</vh></v>
<v t="ekr.20031218072017.1936"><vh>isValidPython</vh></v>
<v t="ekr.20041124083125"><vh>completeFileName (leo.py)</vh></v>
<v t="ekr.20031218072017.1624"><vh>createFrame (leo.py)</vh></v>
<v t="ekr.20031218072017.1938"><vh>createNullGuiWithScript (leo.py)</vh></v>
<v t="ekr.20031218072017.1939"><vh>getBatchScript</vh></v>
<v t="ekr.20041130093254"><vh>reportDirectories</vh></v>
</v>
</v>
<v t="ekr.20060627075911"><vh>Flash matching parens &amp; corresponding settings</vh>
<v t="ekr.20050920084036.54"><vh> ctor (editCommandsClass)</vh></v>
<v t="ekr.20060627080947"><vh>skip_matching_python_parens</vh></v>
<v t="ekr.20031218072017.3189"><vh>skip_matching_python_delims</vh></v>
<v t="ekr.20051125080855"><vh>selfInsertCommand &amp; helpers</vh>
<v t="ekr.20051026171121"><vh>&lt;&lt; handle newline &gt;&gt;</vh></v>
<v t="ekr.20060627083506"><vh>flashMatchingBracketsHelper</vh></v>
<v t="ekr.20060627091557"><vh>flashCharacter</vh></v>
<v t="ekr.20051027172949"><vh>updateAutomatchBracket</vh></v>
<v t="ekr.20051026171121.1"><vh>udpateAutoIndent</vh></v>
<v t="ekr.20051026092433"><vh>updateTab</vh></v>
</v>
</v>
</v>
<v t="ekr.20060624072803.3"><vh>New settings</vh>
<v t="ekr.20060628094329"><vh>Added standard bindings for Ctrl-y (yank) and Ctrl-k (kill-line)</vh></v>
<v t="ekr.20060624072803.4"><vh>Added @bool warn_about_redefined_shortcuts setting</vh></v>
<v t="ekr.20060627070101"><vh>Added @bool trace_bind_key_exceptions setting</vh></v>
<v t="ekr.20060627122419"><vh>Added bracket flash settings</vh></v>
</v>
</v>
<v t="EKR.20040519090151.2"><vh>To do</vh>
<v t="ekr.20040117181936"
expanded="ekr.20060628103226,"><vh>@thin ../doc/leoToDo.txt</vh></v>
<v t="ekr.20060207133601"><vh>@thin ../doc/leoToDoLater.txt</vh></v>
</v>
<v t="ekr.20060531161030" a="TV"><vh>To do: B4</vh>
<v t="ekr.20060628103226" a="E"><vh>Finish emacs commands</vh>
<v t="ekr.20060628103226.2"><vh>Alt-x handlers should add to lossage</vh></v>
<v t="ekr.20060628095110"><vh>Fix yank and kill-line commands</vh>
<v t="ekr.20050920084036.183"><vh>addToKillBuffer</vh></v>
<v t="ekr.20050920084036.174"><vh>class killBufferCommandsClass (add docstrings)</vh>
<v t="ekr.20050920084036.175"><vh> ctor &amp; finishCreate</vh></v>
<v t="ekr.20050920084036.176"><vh> getPublicCommands</vh></v>
<v t="ekr.20050920084036.183"><vh>addToKillBuffer</vh></v>
<v t="ekr.20050920084036.181"><vh>backwardKillSentence</vh></v>
<v t="ekr.20050920084036.180"><vh>backwardKillWord</vh></v>
<v t="ekr.20051216151811"><vh>clearKillRing</vh></v>
<v t="ekr.20050920084036.185"><vh>getClipboard</vh></v>
<v t="ekr.20050920084036.184"><vh>iterateKillBuffer</vh></v>
<v t="ekr.20050920084036.178"><vh>kill, killLine, killWord</vh></v>
<v t="ekr.20050920084036.182"><vh>killRegion &amp; killRegionSave &amp; helper</vh></v>
<v t="ekr.20050930095323.1"><vh>killSentence</vh></v>
<v t="ekr.20050930100733"><vh>killWs</vh></v>
<v t="ekr.20050930091642.1"><vh>yank</vh></v>
<v t="ekr.20050930091642.2"><vh>yankPop</vh></v>
<v t="ekr.20050920084036.128"><vh>zapToCharacter</vh></v>
</v>
</v>
<v t="ekr.20060628094329.2"><vh>Test/Fix macros</vh></v>
<v t="ekr.20060628103226.3"><vh>Make sure repeat counts work on basic editing commands</vh></v>
</v>
<v t="ekr.20060531161030.1"><vh>Make body editors persistant</vh></v>
<v t="ekr.20060527204444"><vh>Finish new colorizer plugin</vh></v>
</v>
<v t="ekr.20031218072017.2406"><vh>Code</vh>
<v t="ekr.20031218072017.2606"><vh>&lt;&lt; Import pychecker &gt;&gt;</vh></v>
<v t="ekr.20031218072017.2582"><vh> version &amp; signon stuff</vh>
<v t="ekr.20040629121554"><vh>getBuildNumber</vh></v>
<v t="ekr.20040629121554.1"><vh>getSignOnLine (Contains hard-coded version info)</vh></v>
<v t="ekr.20040629121554.2" a="M" labels="540801000032383634373033303061353332373632363536363666373236353230363336383631366536373635336132373061373033313061353636343635363632303639366536393734353636353732373336393666366532303238373336353663363632393361356337353330333033303631323032303230323036333230336432303733363536633636356337353330333033303631323032303230323036333265373636353732323033643230323232343532363537363639373336393666366533613230333132653332333233353230323432323230323332303433353635333230373537303634363137343635373332303734363836393733326530613730333230613733326571002e"><vh>initVersion</vh></v>
<v t="ekr.20040629121554.3"><vh>c.signOnWithVersion</vh></v>
</v>
<v t="ekr.20051031040240"><vh>Buttons and settings</vh>
<v t="ekr.20051027111215"><vh>@thin buttons.txt</vh></v>
<v t="ekr.20041119040438"><vh>@settings</vh>
<v t="ekr.20050420073615"><vh>@recent-files</vh></v>
<v t="ekr.20041119042418"><vh>@bool use_plugins = True</vh></v>
<v t="ekr.20041211042119"><vh>@int page_width = 80</vh></v>
</v>
</v>
<v t="ekr.20031218072017.2604"><vh>Core classes...</vh>
<v t="ekr.20031218072017.2605"><vh>@thin leo.py </vh></v>
<v t="ekr.20031218072017.2608"><vh>@thin leoApp.py</vh></v>
<v t="ekr.20041005105605.1"><vh>@thin leoAtFile.py</vh></v>
<v t="ekr.20031218072017.2794"><vh>@thin leoColor.py</vh></v>
<v t="ekr.20031218072017.2810"
marks="ekr.20040629121554.2,"><vh>@thin leoCommands.py</vh></v>
<v t="ekr.20041117062700"><vh>@thin leoConfig.py</vh></v>
<v t="ekr.20031218072017.3018"><vh>@thin leoFileCommands.py</vh></v>
<v t="ekr.20031218072017.3093"><vh>@thin leoGlobals.py</vh></v>
<v t="ekr.20031218072017.3206"><vh>@thin leoImport.py</vh></v>
<v t="ekr.20031218072017.3320"><vh>@thin leoNodes.py</vh></v>
<v t="ekr.20031218072017.3439"><vh>@thin leoPlugins.py</vh></v>
<v t="ekr.20031218072017.3446"><vh>@thin leoTangle.py</vh></v>
<v t="ekr.20051104075904" annotate="7d71002e"><vh>@thin leoTest.py</vh></v>
<v t="ekr.20031218072017.3603"><vh>@thin leoUndo.py</vh></v>
</v>
<v t="ekr.20031218072017.3625"><vh>Gui Base classes</vh>
<v t="ekr.20050721093241"><vh>&lt;&lt; about gui classes and gui plugins &gt;&gt;</vh></v>
<v t="ekr.20031218072017.3630"><vh>@thin leoCompare.py</vh></v>
<v t="ekr.20060123151617"
marks="ekr.20031218072017.3077,"><vh>@thin leoFind.py</vh></v>
<v t="ekr.20031218072017.3655"><vh>@thin leoFrame.py</vh></v>
<v t="ekr.20031218072017.3719"><vh>@thin leoGui.py</vh></v>
<v t="ekr.20031218072017.3749"><vh>@thin leoMenu.py</vh></v>
</v>
<v t="ekr.20031218072017.3821"><vh>Gui Tkinter classes</vh>
<v t="ekr.20031218072017.3838"><vh>@thin leoTkinterComparePanel.py</vh></v>
<v t="ekr.20031218072017.3858"><vh>@thin leoTkinterDialog.py</vh></v>
<v t="ekr.20031218072017.3897"><vh>@thin leoTkinterFind.py</vh></v>
<v t="ekr.20031218072017.3939"
marks="ekr.20060528170438,"><vh>@thin leoTkinterFrame.py</vh></v>
<v t="ekr.20031218072017.4047"><vh>@thin leoTkinterGui.py</vh></v>
<v t="ekr.20031218072017.4099"><vh>@thin leoTkinterKeys.py</vh></v>
<v t="ekr.20031218072017.4100"><vh>@thin leoTkinterMenu.py</vh></v>
<v t="ekr.20040803072955"
marks="ekr.20040803072955.58,"><vh>@thin leoTkinterTree.py</vh></v>
</v>
<v t="ekr.20031218072017.3748"
marks="ekr.20051010062551.1,ekr.20051008134059,ekr.20060321105403.2,ekr.20060104110233,"><vh>@thin leoKeys.py</vh></v>
<v t="ekr.20050710142719"
marks="ekr.20060613090701,"><vh>@thin leoEditCommands.py</vh></v>
</v>
</vnodes>
<tnodes>
<t tx="EKR.20040430162943"></t>
<t tx="EKR.20040519090151.2"></t>
<t tx="EKR.20040519090151.3"></t>
<t tx="EKR.20040612215018">if g.os_path_exists(fileName):
    f = file(fileName)
    lines = f.readlines()
    f.close()
else:
    lines = g.splitLines(script)

s = '-' * 20
g.es_print(s)

# Print surrounding lines.
i = max(0,n-2)
j = min(n+2,len(lines))
while i &lt; j:
    ch = g.choose(i==n-1,'*',' ')
    s = "%s line %d: %s" % (ch,i+1,lines[i])
    g.es(s,newline=False)
    i += 1</t>
<t tx="EKR.20040627100424">if c.exists and c.config.redirect_execute_script_output_to_log_pane:

    g.restoreStderr()
    g.restoreStdout()</t>
<t tx="ekr.20031218072017.1149">try:
    mode = c.config.output_newline
    mode = g.choose(mode=="platform",'w','wb')
    theFile = open(newFileName,mode)
    s = g.toEncodedString(s,self.encoding,reportErrors=True)
    theFile.write(s)
    theFile.close()
    g.es("created: " + newFileName)
except:
    g.es("exception creating: " + newFileName)
    g.es_exception()</t>
<t tx="ekr.20031218072017.1624">def createFrame (fileName):
    
    """Create a LeoFrame during Leo's startup process."""
    
    import leoGlobals as g

    # Try to create a frame for the file.
    if fileName:
        if g.os_path_exists(fileName):
            ok, frame = g.openWithFileName(fileName,None)
            if ok:
                return frame.c,frame

    # Create a _new_ frame &amp; indicate it is the startup window.
    c,frame = g.app.newLeoCommanderAndFrame(fileName=fileName)
    frame.setInitialWindowGeometry()
    frame.resizePanesToRatio(frame.ratio,frame.secondary_ratio)
    frame.startupWindow = True
    # 3/2/05: Call the 'new' hook for compatibility with plugins.
    g.doHook("new",old_c=None,c=c,new_c=c)

    # Report the failure to open the file.
    if fileName:
        g.es("File not found: " + fileName)

    return c,frame</t>
<t tx="ekr.20031218072017.1934">def run(fileName=None,*args,**keywords):
    
    """Initialize and run Leo"""
    
    __pychecker__ = '--no-argsused' # keywords not used.
    
    if not isValidPython(): return
    &lt;&lt; import leoGlobals and leoApp &gt;&gt;
    g.computeStandardDirectories()
    script, windowFlag = getBatchScript() # Do early so we can compute verbose next.
    verbose = script is None
    g.app.setLeoID(verbose=verbose) # Force the user to set g.app.leoID.
    &lt;&lt; import leoNodes and leoConfig &gt;&gt;
    g.app.nodeIndices = leoNodes.nodeIndices(g.app.leoID)
    g.app.config = leoConfig.configClass()
    fileName = completeFileName(fileName)
    reportDirectories(verbose)
    # Read settings *after* setting g.app.config.
    # Read settings *before* opening plugins.  This means if-gui has effect only in per-file settings.
    g.app.config.readSettingsFiles(fileName,verbose)
    g.app.setEncoding()
    if script:
        if windowFlag:
            g.app.createTkGui() # Creates global windows.
            g.app.gui.setScript(script)
            sys.args = []
        else:
            createNullGuiWithScript(script)
        fileName = None
    # Load plugins. Plugins may create g.app.gui.
    g.doHook("start1")
    if g.app.killed: return # Support for g.app.forceShutdown.
    # Create the default gui if needed.
    if g.app.gui == None:
        g.app.createTkGui() # Creates global windows.
    # Initialize tracing and statistics.
    g.init_sherlock(args)
    &lt;&lt; start psycho &gt;&gt;
    # New in 4.3: clear g.app.initing _before_ creating the frame.
    g.app.initing = False # "idle" hooks may now call g.app.forceShutdown.
    # Create the main frame.  Show it and all queued messages.
    c,frame = createFrame(fileName)
    if not frame: return
    g.app.trace_gc          = c.config.getBool('trace_gc')
    g.app.trace_gc_calls    = c.config.getBool('trace_gc_calls')
    g.app.trace_gc_verbose  = c.config.getBool('trace_gc_verbose')
    if g.app.disableSave:
        g.es("disabling save commands",color="red")
    g.app.writeWaitingLog()
    p = c.currentPosition()
    g.doHook("start2",c=c,p=p,v=p,fileName=fileName)
    if c.config.getBool('allow_idle_time_hook'):
        g.enableIdleTimeHook()
    if not fileName:
        c.redraw_now()
    c.bodyWantsFocus()
    g.app.gui.runMainLoop()</t>
<t tx="ekr.20031218072017.1936">def isValidPython():

    message = """\
Leo requires Python 2.2.1 or higher.
You may download Python from http://python.org/download/
"""
    try:
        # This will fail if True/False are not defined.
        import leoGlobals as g
    except ImportError:
        print "isValidPython: can not import leoGlobals"
        return 0
    except:
        print "isValidPytyhon: unexpected exception: import leoGlobals.py as g"
        import traceback ; traceback.print_exc()
        return 0
    try:
        ok = g.CheckVersion(sys.version, "2.2.1")
        if not ok:
            print message
            g.app.gui.runAskOkDialog(None,"Python version error",message=message,text="Exit")
        return ok
    except:
        print "isValidPython: unexpected exception: g.CheckVersion"
        import traceback ; traceback.print_exc()
        return 0</t>
<t tx="ekr.20031218072017.1938">def createNullGuiWithScript (script):
    
    import leoGlobals as g
    import leoGui
    
    g.app.batchMode = True
    g.app.gui = leoGui.nullGui("nullGui")
    if not g.app.root:
        g.app.root = g.app.gui.createRootWindow()
    g.app.gui.finishCreate()
    g.app.gui.setScript(script)
</t>
<t tx="ekr.20031218072017.1939">def getBatchScript ():
    
    import leoGlobals as g
    windowFlag = False
    
    name = None ; i = 1 # Skip the dummy first arg.
    while i + 1 &lt; len(sys.argv):
        arg = sys.argv[i].strip().lower()
        if arg in ("--script","-script"):
            name = sys.argv[i+1].strip() ; break
        if arg in ("--script-window","-script-window"):
            name = sys.argv[i+1].strip() ; windowFlag = True ; break
        i += 1

    if not name:
        return None, windowFlag
    name = g.os_path_join(g.app.loadDir,name)
    try:
        f = None
        try:
            f = open(name,'r')
            script = f.read()
            # g.trace("script",script)
        except IOError:
            g.es_print("can not open script file: " + name, color="red")
            script = None
    finally:
        if f: f.close()
        return script, windowFlag</t>
<t tx="ekr.20031218072017.2140">def executeScript(self,event=None,p=None,script=None,
    useSelectedText=True,define_g=True,define_name='__main__',silent=False):

    """This executes body text as a Python script.
    
    We execute the selected text, or the entire body text if no text is selected."""
    
    c = self ; script1 = script
    if not script:
        script = g.getScript(c,p,useSelectedText=useSelectedText)
    &lt;&lt; redirect output &gt;&gt;
    try:
        if script.strip():
            sys.path.insert(0,c.frame.openDirectory)
            script += '\n' # Make sure we end the script properly.
            try:
                p = c.currentPosition()
                d = g.choose(define_g,{'c':c,'g':g,'p':p},{})
                if define_name: d['__name__'] = define_name
                # g.trace(script)
                exec script in d
                if not script1 and not silent:
                    g.es("end of script",color="purple")
            except Exception:
                g.handleScriptException(c,p,script,script1)
            del sys.path[0]
        else:
            g.es("no script selected",color="blue")
    finally: # New in 4.3 beta 2: unredirect output last.
        &lt;&lt; unredirect output &gt;&gt;</t>
<t tx="ekr.20031218072017.2143">if c.config.redirect_execute_script_output_to_log_pane:

    g.redirectStdout() # Redirect stdout
    g.redirectStderr() # Redirect stderr</t>
<t tx="ekr.20031218072017.2256"></t>
<t tx="ekr.20031218072017.2257">def scanPythonClass (self,s,i,start,parent):

    """Creates a child node c of parent for the class, and children of c for each def in the class."""

    # g.trace(g.get_line(s,i))
    class_indent = self.getLeadingIndent(s,i)
    &lt;&lt; set class_name and headline &gt;&gt;
    if not class_name: return i
    i = g.skip_line(s,i) # Skip the class line.
    i,prefix,body = self.createClassNodeText(s,i,start)
    class_vnode = self.createHeadline(parent,prefix + body,headline)
    savedMethodName = self.methodName
    self.methodName = headline
    # Create a node for leading declarations of the class.
    i = self.scanPythonDecls(s,i,class_vnode,class_indent,indent_parent_ref_flag=True)
    start,i = self.scanPythonClassHelper(s,i,class_indent,class_name,class_vnode)
    s2 = s[start:i]
    if s2: class_vnode.appendStringToBody(s2)
    self.methodName = savedMethodName
    return i</t>
<t tx="ekr.20031218072017.2258"># Skip to the class name.
i = g.skip_ws(s,i)
i = g.skip_c_id(s,i) # skip "class"
i = g.skip_ws_and_nl(s,i)
if i &lt; len(s) and g.is_c_id(s[i]):
    j = i ; i = g.skip_c_id(s,i)
    class_name = s[j:i]
    headline = "class " + class_name
else:
    headline = ''
    class_name = ''</t>
<t tx="ekr.20031218072017.2263">def scanPythonDef (self,s,i,start,parent):

    """Creates a node of parent for the def."""

    # g.trace(g.get_line(s,i))
    &lt;&lt; set headline or return i &gt;&gt;
    i = self.skipPythonDef(s,i,start)
    # Create the def node.
    savedMethodName = self.methodName
    self.methodName = headline
    &lt;&lt; Create def node &gt;&gt;
    self.methodName = savedMethodName
    return i
</t>
<t tx="ekr.20031218072017.2264">i = g.skip_ws(s,i)
i = g.skip_c_id(s,i) # Skip the "def"
i = g.skip_ws_and_nl(s,i)
if i &lt; len(s) and g.is_c_id(s[i]):
    j = i ; i = g.skip_c_id(s,i)
    headline = s[j:i]
    # g.trace("headline:" + headline)
else: return i</t>
<t tx="ekr.20031218072017.2266"># Create the prefix line for @root trees.
if self.treeType == "@file":
    prefix = ""
else:
    prefix = g.angleBrackets(" " + savedMethodName + " methods ") + "=\n\n"
    self.methodsSeen = True

# Create body.
start = g.skip_blank_lines(s,start)
body = s[start:i]
body = self.undentBody(body)

# Create the node.
self.createHeadline(parent,prefix + body,headline)

</t>
<t tx="ekr.20031218072017.2267">def scanPythonDecls (self,s,i,parent,indent,indent_parent_ref_flag=True):
    
    done = False ; start = i
    while not done and i &lt; len(s):
        progress = i
        # g.trace(g.get_line(s,i))
        ch = s[i]
        if ch == '\n':
            backslashNewline = i &gt; 0 and g.match(s,i-1,"\\\n")
            i = g.skip_nl(s,i)
            # 2/14/03: break on lesser indention.
            j = g.skip_ws(s,i)
            if not g.is_nl(s,j) and not g.match(s,j,"#") and not backslashNewline:
                lineIndent = self.getLeadingIndent(s,i)
                if lineIndent &lt;= indent:
                    break
        elif ch == '#': i = g.skip_to_end_of_line(s,i)
        elif ch == '"' or ch == '\'':
            i = g.skip_python_string(s,i)
        elif g.is_c_id(ch):
            &lt;&lt; break on def or class &gt;&gt;
        else: i += 1
        assert(progress &lt; i)
    j = g.skip_blank_lines(s,start)
    if g.is_nl(s,j): j = g.skip_nl(s,j)
    if j &lt; i:
        &lt;&lt; Create a child node for declarations &gt;&gt;
    return i</t>
<t tx="ekr.20031218072017.2268">if g.match_c_word(s,i,"def") or g.match_c_word(s,i,"class"):
    i = g.find_line_start(s,i)
    done = True
    break
else:
    i = g.skip_c_id(s,i)</t>
<t tx="ekr.20031218072017.2269">headline = ref = g.angleBrackets(" " + self.methodName + " declarations ")
leading_tab = g.choose(indent_parent_ref_flag,"\t","")

# Append the reference to the parent's body.
parent.appendStringToBody(leading_tab + ref + "\n") # 7/6/02

# Create the node for the decls.
body = self.undentBody(s[j:i])
if self.treeType == "@root":
    body = "@code\n\n" + body
self.createHeadline(parent,body,headline)</t>
<t tx="ekr.20031218072017.2270"># See the comments for scanCText for what the text looks like.

def scanPythonText (self,s,parent):

    """Creates a child of parent for each Python function definition seen."""

    decls_seen = False ; start = i = 0
    self.methodsSeen = False
    while i &lt; len(s):
        progress = i
        # g.trace(g.get_line(s,i))
        ch = s[i]
        if ch == '\n' or ch == '\r': i = g.skip_nl(s,i)
        elif ch == '#': i = g.skip_to_end_of_line(s,i)
        elif ch == '"' or ch == '\'': i = g.skip_python_string(s,i)
        elif g.is_c_id(ch):
            &lt;&lt; handle possible Python function or class &gt;&gt;
        else: i += 1
        assert(progress &lt; i)
    if not decls_seen: # 2/17/03
        parent.appendStringToBody("@ignore\n" + self.rootLine + "@language python\n")
    &lt;&lt; Append a reference to the methods of this file &gt;&gt;
    &lt;&lt; Append any unused python text to the parent's body text &gt;&gt;</t>
<t tx="ekr.20031218072017.2271">if g.match_c_word(s,i,"def") or g.match_word(s,i,"class"):
    isDef = g.match_c_word(s,i,"def")
    if not decls_seen:
        parent.appendStringToBody("@ignore\n" + self.rootLine + "@language python\n")
        i = start = self.scanPythonDecls(s,start,parent,-1,indent_parent_ref_flag=False)
        decls_seen = True
        if self.treeType == "@file": # 7/29/02
            parent.appendStringToBody("@others\n") # 7/29/02
    if isDef:
        i = start = self.scanPythonDef(s,i,start,parent)
    else:
        i = start = self.scanPythonClass(s,i,start,parent)
else:
    i = g.skip_c_id(s,i)</t>
<t tx="ekr.20031218072017.2272">if self.treeType == "@root" and self.methodsSeen:
    parent.appendStringToBody(
        g.angleBrackets(" " + self.methodName + " methods ") + "\n\n")</t>
<t tx="ekr.20031218072017.2273"># Do nothing if only whitespace is left.
i = start ; i = g.skip_ws_and_nl(s,i)
if i &lt; len(s):
    parent.appendStringToBody(s[start:])</t>
<t tx="ekr.20031218072017.2406"> @tabwidth -4
@pagewidth 80

@ This section contains all the source code of leo.py.
 
Leo's code uses the following conventions throughout:

c:  a commander
ch: a character
d:  a dialog or a dict.
g:  the leoGlobal module.
i, j, k: indices into a string
p:  a position.
s:  a string
t:  a tnode or a text widget.
u:  an undoer
v:  a vnode
z:  a local temp.</t>
<t tx="ekr.20031218072017.2582"></t>
<t tx="ekr.20031218072017.2604"></t>
<t tx="ekr.20031218072017.2606">@color

# __pychecker__ = '--no-argsused'

# See pycheckrc file in leoDist.leo for a list of erroneous warnings to be suppressed.

if 0: # Set to 1 for lint-like testing.
      # Use t23.bat: only on Python 2.3.

    try:
        import pychecker.checker
        # This works.  We may want to set options here...
        # from pychecker import Config 
        # print pychecker
        print ; print "Warning (in leo.py): pychecker.checker running..." ; print
    except:
        print ; print 'Can not import pychecker' ; print</t>
<t tx="ekr.20031218072017.3112">def es_exception (full=True,c=None,color="red"):
    
    __pychecker__ = '--no-argsused' # c not used. retained for compatibility.

    typ,val,tb = sys.exc_info()

    # g.trace(full,typ,tb)
    
    fileName,n = g.getLastTracebackFileAndLineNumber()

    if full or g.app.debugSwitch &gt; 0:
        lines = traceback.format_exception(typ,val,tb)
    else:
        lines = traceback.format_exception_only(typ,val)
        if 0: # We might as well print the entire SyntaxError message.
            lines = lines[-1:] # Usually only one line, but more for Syntax errors!

    for line in lines:
        g.es_error(line,color=color)
        if not g.stdErrIsRedirected():
            print line

    if g.app.debugSwitch &gt; 1:
        import pdb # Be careful: g.pdb may or may not have been defined.
        pdb.set_trace()

    return fileName,n</t>
<t tx="ekr.20031218072017.3189">def skip_matching_python_delims(s,i,delim1,delim2,reverse=False):
    
    '''Skip from the opening delim to the matching delim2.
    
    Return the index of the matching ')', or -1'''
    
    level = 0 ; n = len(s)
    assert(g.match(s,i,delim1))
    if reverse:
         while i &gt;= 0:
            ch = s[i]
            if ch == delim1:
                level += 1 ; i -= 1
            elif ch == delim2:
                level -= 1
                if level &lt;= 0:  return i
                i -= 1
            # Doesn't handle strings and comments properly...
            else: i -= 1
    else:
        while i &lt; n:
            progress = i
            ch = s[i]
            if ch == delim1:
                level += 1 ; i += 1
            elif ch == delim2:
                level -= 1
                if level &lt;= 0:  return i
                i += 1
            elif ch == '\'' or ch == '"': i = g.skip_string(s,i)
            elif g.match(s,i,'#'):  i = g.skip_to_end_of_line(s,i)
            else: i += 1
            if i == progress: return -1
    return -1</t>
<t tx="ekr.20031218072017.3300">def removeSentinelsCommand (self,paths):
    
    c = self.c

    self.setEncoding()

    for fileName in paths:
        g.setGlobalOpenDir(fileName)
        path, self.fileName = g.os_path_split(fileName)
        &lt;&lt; Read file into s &gt;&gt;
        &lt;&lt; set delims from the header line &gt;&gt;
        # g.trace("line: '%s', start: '%s', end: '%s'" % (line_delim,start_delim,end_delim))
        s = self.removeSentinelLines(s,line_delim,start_delim,end_delim)
        ext = c.config.remove_sentinels_extension
        if not ext:
            ext = ".txt"
        if ext[0] == '.':
            newFileName = g.os_path_join(path,fileName+ext)
        else:
            head,ext2 = g.os_path_splitext(fileName) 
            newFileName = g.os_path_join(path,head+ext+ext2)
        &lt;&lt; Write s into newFileName &gt;&gt;</t>
<t tx="ekr.20031218072017.3301">try:
    theFile = open(fileName)
    s = theFile.read()
    s = g.toUnicode(s,self.encoding)
    theFile.close()
except IOError:
    g.es("can not open " + fileName, color="blue")
    leoTest.fail()
    return</t>
<t tx="ekr.20031218072017.3302"># Skip any non @+leo lines.
i = 0
while i &lt; len(s) and not g.find_on_line(s,i,"@+leo"):
    i = g.skip_line(s,i)

# Get the comment delims from the @+leo sentinel line.
at = self.c.atFileCommands
j = g.skip_line(s,i) ; line = s[i:j]

valid,new_df,start_delim,end_delim,derivedFileIsThin = at.parseLeoSentinel(line)
if not valid:
    g.es("invalid @+leo sentinel in " + fileName)
    return

if end_delim:
    line_delim = None
else:
    line_delim,start_delim = start_delim,None</t>
<t tx="ekr.20031218072017.3303"># This does not handle @nonl properly, but that's a nit...

def removeSentinelLines(self,s,line_delim,start_delim,end_delim):

    '''Properly remove all sentinle lines in s.'''

    delim = (line_delim or start_delim or '') + '@'
    verbatim = delim + 'verbatim' ; verbatimFlag = False
    result = [] ; lines = g.splitLines(s)
    for line in lines:
        i = g.skip_ws(line,0)
        if not verbatimFlag and g.match(line,i,delim):
            if g.match(line,i,verbatim):
                verbatimFlag = True # Force the next line to be in the result.
            # g.trace(repr(line))
        else:
            result.append(line)
            verbatimFlag = False
    result = ''.join(result)
    return result</t>
<t tx="ekr.20031218072017.3625">&lt;&lt; about gui classes and gui plugins &gt;&gt;</t>
<t tx="ekr.20031218072017.3821"></t>
<t tx="ekr.20040411081633">if g.app and g.app.use_psyco:
    try:
        import psyco
        if 0:
            theFile = r"c:\prog\test\psycoLog.txt"
            g.es("psyco now logging to",theFile,color="blue")
            psyco.log(theFile)
            psyco.profile()
        psyco.full()
        g.es("psyco now running",color="blue")
    except ImportError:
        pass
    except:
        print "unexpected exception importing psyco"
        g.es_exception()</t>
<t tx="ekr.20040629121554">def getBuildNumber(self):
    c = self
    return c.ver[10:-1] # Strip off "(dollar)Revision" and the trailing "$"</t>
<t tx="ekr.20040629121554.1">def getSignOnLine (self):
    c = self
    return "Leo 4.4.1 beta 2, build %s, June 23, 2006" % c.getBuildNumber()</t>
<t tx="ekr.20040629121554.2">def initVersion (self):
    c = self
    c.ver = "$Revision$" # CVS updates this.</t>
<t tx="ekr.20040629121554.3">def signOnWithVersion (self):

    c = self
    color = c.config.getColor("log_error_color")
    signon = c.getSignOnLine()
    n1,n2,n3,junk,junk=sys.version_info
    tkLevel = c.frame.top.getvar("tk_patchLevel")
    
    if sys.platform.startswith('win'):
        version = 'Windows '
        try:
            v = os.sys.getwindowsversion()
            version += ', '.join([str(z) for z in v])
        except Exception:
            pass
            
    else: version = sys.platform
    
    g.es("Leo Log Window...",color=color)
    g.es(signon)
    g.es("Python %d.%d.%d, Tk %s, Pmw %s\n%s" % (n1,n2,n3,tkLevel,Pmw.version(),version))
    g.enl()</t>
<t tx="ekr.20040731204831">def getLastTracebackFileAndLineNumber():
    
    typ,val,tb = sys.exc_info()
    
    if typ in (exceptions.SyntaxError,exceptions.IndentationError):
        # Syntax and indentation errors are a special case.
        # extract_tb does _not_ return the proper line number!
        # This code is similar to the code in format_exception_only(!!)
        try:
            msg,(filename, lineno, offset, line) = val
            return filename,lineno
        except:
            g.trace("bad line number")
            return None,0

    else:
        # The proper line number is the second element in the last tuple.
        data = traceback.extract_tb(tb)
        # g.trace(data)
        item = data[-1]
        filename = item[0]
        n = item[1]
        return filename,n</t>
<t tx="ekr.20040930075711">@nocolor

Leo can't represent some files using nodes!

I call this the "underindented blank line" problem.

Example:

@color

class aClass:
    def spam(): pass
# comment line
    def eggs(): pass
    
@nocolor

Leo's import code can't handle this:
    
- If the import code puts the comment line in a node, the line won't be output with the proper indentation!!

- Having the comment line stop the scanning of aClass is even worse.

- This usually shows up with an unindented blank line instead of the comment line.</t>
<t tx="ekr.20041117083857.1"># Called to read all leoSettings.leo files.
# Also called when opening an .leo file to read @settings tree.

def readSettings (self,c):
    
    """Read settings from a file that may contain an @settings tree."""
    
    # g.trace(c.fileName())
    
    # Create a settings dict for c for set()
    if c and self.localOptionsDict.get(c.hash()) is None:
        self.localOptionsDict[c.hash()] = {}

    parser = settingsTreeParser(c)
    d = parser.traverse()

    return d</t>
<t tx="ekr.20041117085625">def openSettingsFile (self,path):
    
    try:
        # Open the file in binary mode to allow 0x1a in bodies &amp; headlines.
        theFile = open(path,'rb')
    except IOError:
        g.es("can not open: " + path, color="blue")
        return None
        
    # Similar to g.openWithFileName except it uses a null gui.
    # Changing g.app.gui here is a major hack.
    oldGui = g.app.gui
    g.app.gui = leoGui.nullGui("nullGui")
    c,frame = g.app.newLeoCommanderAndFrame(path,updateRecentFiles=False)
    frame.log.enable(False)
    c.setLog()
    g.app.lockLog()
    ok = frame.c.fileCommands.open(
        theFile,path,readAtFileNodesFlag=False,silent=True) # closes theFile.
    g.app.unlockLog()
    frame.openDirectory = g.os_path_dirname(path)
    g.app.gui = oldGui
    return ok and c
</t>
<t tx="ekr.20041117093246"></t>
<t tx="ekr.20041119040438">@nocolor

This tree contains settings unique to this outline.</t>
<t tx="ekr.20041119042418">True: Leo loads plugins on startup.

Warning: Naive or hostile hooks may execute HOSTILE CODE contained in .leo files. See further warnings in LeoDocs.leo.
</t>
<t tx="ekr.20041120064303">def readSettingsFiles (self,fileName,verbose=True):
    
    seen = []
    localDirectory = g.os_path_dirname(fileName)
    localConfigFile = g.os_path_join(localDirectory,'leoSettings.leo')
    if not g.os_path_exists(localConfigFile): localConfigFile = None
    
    # Init settings from leoSettings.leo files.
    for path,localFlag in (
        (self.globalConfigFile,False),
        (self.homeFile,False),
        (localConfigFile,False), # New in 4.4.1.
        (fileName,True),
    ):
        if path and path.lower() not in seen:
            seen.append(path.lower())
            if verbose:
                g.es_print('reading settings in %s' % path)
            c = self.openSettingsFile(path)
            if c:
                self.updateSettings(c,localFlag)
                g.app.destroyWindow(c.frame)
            self.readRecentFilesFile(path)

    self.inited = True
    self.setIvarsFromSettings(None)</t>
<t tx="ekr.20041124083125">def completeFileName (fileName):
    
    import leoGlobals as g
    
    if not fileName:
        return None
        
    # This does not depend on config settings.
    fileName = g.os_path_join(os.getcwd(),fileName)

    head,ext = g.os_path_splitext(fileName)
    if not ext:
        fileName = fileName + ".leo"

    return fileName</t>
<t tx="ekr.20041130093254">def reportDirectories(verbose):
    
    import leoGlobals as g
   
    if verbose:
        for kind,theDir in (
            ("global config",g.app.globalConfigDir),
            ("home",g.app.homeDir),
        ):
            g.es("%s dir: %s" % (kind,theDir),color="blue")</t>
<t tx="ekr.20041211042119"></t>
<t tx="ekr.20041219072112"># Import leoGlobals, but do NOT set g.
try:
    import leoGlobals
except ImportError:
    print "Error importing leoGlobals.py"

# Create the application object.
try:
    import leoApp
    leoGlobals.app = leoApp.LeoApp()
except ImportError:
    print "Error importing leoApp.py"
    
# NOW we can set g.
g = leoGlobals
assert(g.app)</t>
<t tx="ekr.20041219072416.1">try:
    import leoNodes
except ImportError:
    print "Error importing leoNodes.py"
    import traceback ; traceback.print_exc()
try:
    import leoConfig
except ImportError:
    print "Error importing leoConfig.py"
    import traceback ; traceback.print_exc()</t>
<t tx="ekr.20050220030850">def test_g_es_exception():
    
    if c.config.redirect_execute_script_output_to_log_pane:
        return # Test doesn't work when redirection is on.

    try:
        import sys
        # Catch the output of g.es_exception.
        # We catch the AssertionError, so nothing gets written to stderr.
        sys.stdout = fo = g.fileLikeObject()
        try: # Create an exception to catch.
            assert False, 'Assert False in test_g_es_exception'
        except AssertionError:
            g.es_exception(color='suppress')
            result = fo.get()
            s1 = 'Traceback (most recent call last):'
            s2 = 'AssertionError: Assert False in test_g_es_exception'
            assert result.find(s1) &gt; -1, 'No traceback line: %s' % repr(result)
            assert result.find(s2) &gt; -1, 'No AssertionError line: %s' % repr(result)
    finally:
        # Not needed unless we execute this script as selected text.
        sys.stdout = sys.__stdout__</t>
<t tx="ekr.20050420073615">c:\prog\leoCVS\leo\doc\LeoDocs.leo
LeoPy.leo
C:\Documents and Settings\Ed\My Documents\ekr.leo
c:\prog\leoCVS\leo\config\leoSettings.leo</t>
<t tx="ekr.20050721093241">@nocolor

The following are notes for anyone who is interested in writing alternate gui's for Leo.

Rule 1: Leo's core is (or should be) free of gui-specific code.

Core code calls 'gui wrapper methods' defined by gui-specific classes.  The base classes for these gui-specific classes are in the node Code--&gt;Gui Base classes.

Rule 2: Gui-specific code should be localized.  

The @file nodes contained in the node 'Code--&gt;Gui Tkinter classes' in leoPy.leo contain all of Leo's Tkinter-specific code.  Gui plugins would typically put all similar code in a single file.

Rule 3: Gui-specific code can call gui methods directly.

There are no restrictions about the code in the gui-specific classes.

Rule 4:  Gui-specific classes must implement the 'gui wrapper methods' specified in the gui base classes.

This is the way that gui-specific classes provide gui-specific services to Leo's core.

The alternative would be to implement all gui-specific commands directly in the gui-specific code.  But this would be much more work than needed.  For example, only a few gui-specific wrappers are needed to implement all commands that deal with body text.  Implementing each of these commands 'from scratch' would duplicate a lot of code unnecessarily.

Using the gui wrapper methods is a bit messy for two reasons:

1.  It requires defining enough wrappers (both in the base gui classes and subclasses) so that all gui-specific services needed by Leo's core are available.   Adding a wrapper to a gui base class involves adding it to all gui-specific subclasses.  It's easy to forget to add a wrapper.  The gui base class defines all wrappers as a function that just calls oops().  This prints a warning that the wrapper should be defined in a subclass.

2. The original wrappers assumed Tkinter-like indices.  Wrappers that were defined later assume Python indices (see Rule 5 below).   The newer style wrappers that use Python indices have 'Python' in their name.   Having two sets of wrappers is one of the ugliest features of the present code.  I find it hard to remember which wrappers exist and what exactly they do :-)

Rule 5:  Leo's core should use Python indices, not gui-specific indices.

Leo's core mostly follows this rule: there may be a few exceptions.

A Python index is an int that runs from 0 (beginning of text) to len(s) (end of text s).  That is, there are exactly len(s) + 1 valid indices.  In contrast, Tkinter indices run from "1.0" to "x.y" where text s has x lines and where the length of the last line is y-1. 

Two (recently written) functions in leoGlobals.py support conversions from Python indices to the row/column indices used by Tkinter.

- g.convertPythonIndexToRowCol converts a Python index to a row/column index used by Tkinter.
- g.convertRowColToPythonIndex does the reverse.

Important:  the first Tkinter index is '1.0', not '0.0', but the row returned by g.convertPythonIndexToRowCol is zero based, so the code that actually creates Tkinter indices from row/col must add 1 to the row.  Similar remarks apply when going in the reverse direction.</t>
<t tx="ekr.20050920084036.54">def __init__ (self,c):

    baseEditCommandsClass.__init__(self,c) # init the base class.
    
    self.ccolumn = '0'   # For comment column functions.
    self.dynaregex = re.compile(r'[%s%s\-_]+'%(string.ascii_letters,string.digits))
        # For dynamic abbreviations
    self.extendMode = False # True: all cursor move commands extend the selection.
    self.fillPrefix = '' # For fill prefix functions.
    self.fillColumn = 70 # For line centering.
    self.moveSpotNode = None # A tnode.
    self.moveSpot = None # For retaining preferred column when moving up or down.
    self.moveCol = None # For retaining preferred column when moving up or down.
    self.store ={'rlist':[], 'stext':''} # For dynamic expansion.
    self.swapSpots = []
    self._useRegex = False # For replace-string
    self.widget = None # For use by state handlers.
    
    # Settings...
    self.autocompleteBrackets   = c.config.getBool('autocomplete-brackets')
    self.bracketsFlashBg        = c.config.getColor('flash-brackets-background-color')
    self.bracketsFlashCount     = c.config.getInt('flash-brackets-count')
    self.bracketsFlashDelay     = c.config.getInt('flash-brackets-delay')
    self.bracketsFlashFg        = c.config.getColor('flash-brackets-foreground-color')
    self.flashMatchingBrackets  = c.config.getBool('flash-matching-brackets')
    self.smartAutoIndent        = c.config.getBool('smart_auto_indent')</t>
<t tx="ekr.20050920084036.63">def watchEscape (self,event):

    k = self.k

    if not k.inState():
        k.setState('escape','start',handler=self.watchEscape)
        k.setLabelBlue('Esc ')
    elif k.getStateKind() == 'escape':
        state = k.getState('escape')
        # hi1 = k.keysymHistory [0]
        # hi2 = k.keysymHistory [1]
        data1 = keyHandlerClass.lossage[0]
        data2 = keyHandlerClass.lossage[1]
        ch1, stroke1 = data1
        ch2, stroke2 = data2
        
        if state == 'esc esc' and event.keysym == 'colon':
            self.evalExpression(event)
        elif state == 'evaluate':
            self.escEvaluate(event)
        # elif hi1 == hi2 == 'Escape':
        elif stroke1 == 'Escape' and stroke2 == 'Escape':
            k.setState('escape','esc esc')
            k.setLabel('Esc Esc -')
        elif event.keysym not in ('Shift_L','Shift_R'):
            k.keyboardQuit(event)</t>
<t tx="ekr.20050920084036.83">def viewLossage (self,event):
    
    '''Put the Emacs-lossage in the minibuffer label.'''

    k = self.k
    
    g.es('Lossage...')
    aList = leoKeys.keyHandlerClass.lossage
    aList.reverse()
    for data in aList:
        ch,stroke = data
        d = {' ':'Space','\t':'Tab','\b':'Backspace','\n':'Newline','\r':'Return'}
        ch = d.get(ch) or ch
        g.es(stroke or ch or 'None')</t>
<t tx="ekr.20050920084036.128">def zapToCharacter (self,event):
    
    '''Kill characters from the insertion point to a given character.'''

    k = self.k ; state = k.getState('zap-to-char')

    if state == 0:
        k.setLabelBlue('Zap To Character: ',protect=True)
        k.setState('zap-to-char',1,handler=self.zapToCharacter)
    else:
        c = k.c ; w = event.widget ; ch = event.char
        k.resetLabel()
        k.clearState()
        if (
            len(event.char) != 0 and
            ch in (string.ascii_letters + string.digits + string.punctuation)
        ):
            i = w.search(ch,'insert',stopindex='end')
            if i:
                t = w.get('insert','%s+1c' % i)
                self.addToKillBuffer(t)
                w.delete('insert','%s+1c' % i)</t>
<t tx="ekr.20050920084036.174">class killBufferCommandsClass (baseEditCommandsClass):
    
    '''A class to manage the kill buffer.'''

    @others</t>
<t tx="ekr.20050920084036.175">def __init__ (self,c):

    baseEditCommandsClass.__init__(self,c) # init the base class.

    self.killBuffer = [] # May be changed in finishCreate.
    self.kbiterator = self.iterateKillBuffer()
    self.last_clipboard = None # For interacting with system clipboard.
    self.reset = False
    try:
        self.widget = c.frame.body.bodyCtrl
    except AttributeError:
        self.widget = None

def finishCreate (self):
    
    baseEditCommandsClass.finishCreate(self)
        # Call the base finishCreate.
        # This sets self.k
    
    if self.k.useGlobalKillbuffer:
        self.killBuffer = leoKeys.keyHandlerClass.global_killbuffer</t>
<t tx="ekr.20050920084036.176">def getPublicCommands (self):
    
    return {
        'backward-kill-sentence':   self.backwardKillSentence,
        'backward-kill-word':       self.backwardKillWord,
        'clear-kill-ring':          self.clearKillRing,
        'kill-line':                self.killLine,
        'kill-word':                self.killWord,
        'kill-sentence':            self.killSentence,
        'kill-region':              self.killRegion,
        'kill-region-save':         self.killRegionSave,
        'yank':                     self.yank,
        'yank-pop':                 self.yankPop,
        'zap-to-character':         self.zapToCharacter,
    }</t>
<t tx="ekr.20050920084036.178">def kill (self,event,frm,to):

    k = self.k ; w = event.widget ; s = w.get(frm,to)
    self.addToKillBuffer(s)
    w.clipboard_clear()
    w.clipboard_append(s)
    w.delete(frm,to)

def killLine (self,event):
    '''Kill the line containing the cursor.'''
    self.kill(event,'insert linestart','insert lineend+1c')

def killWord (self,event):
    '''Kill the word containing the cursor.'''
    self.kill(event,'insert wordstart','insert wordend')
    self.killWs(event)
</t>
<t tx="ekr.20050920084036.180">def backwardKillWord (self,event):
    
    '''Kill the previous word.'''

    c = self.c
    c.editCommands.backwardWord(event)
    self.killWord(event)
    self.killWs(event)
    c.editCommands.backwardWord(event)</t>
<t tx="ekr.20050920084036.181">def backwardKillSentence (self,event):
    
    '''Kill the previous sentence.'''
    
    w = event.widget
    i = w.search('.','insert',backwards=True,stopindex='1.0')

    if i:
        i2 = w.search('.',i,backwards=True,stopindex='1.0')
        i2 = g.choose(i2=='','1.0',i2+'+1c ')
        self.kill(event,i2,'%s + 1c' % i)</t>
<t tx="ekr.20050920084036.182">def killRegion (self,event):
    '''Kill the text selection.'''
    self.killRegionHelper(event,deleteFlag=True)
    
def killRegionSave (self,event):
    '''Add the selected text to the kill ring, but do not delete it.'''
    self.killRegionHelper(event,deleteFlag=False)

def killRegionHelper (self,event,deleteFlag):

    w = event.widget

    if g.app.gui.isTextWidget(w):
        theRange = w.tag_ranges('sel')
        if theRange:
            s = w.get(theRange[0],theRange[-1])
            if deleteFlag:
                w.delete(theRange[0],theRange[-1])
            self.addToKillBuffer(s)
            w.clipboard_clear()
            w.clipboard_append(s)
            self.removeRKeys(w)</t>
<t tx="ekr.20050920084036.183">def addToKillBuffer (self,text):
    
    killKeys =(
        '&lt;Control-k&gt;', '&lt;Control-w&gt;',
        '&lt;Alt-d&gt;', '&lt;Alt-Delete', '&lt;Alt-z&gt;', '&lt;Delete&gt;',
        '&lt;Control-Alt-w&gt;')

    k = self.k
    self.reset = True

    # g.trace(repr(text))

    if self.killBuffer and k.stroke in killKeys:
        self.killBuffer [0] = self.killBuffer [0] + text
    else:
        self.killBuffer.insert(0,text)</t>
<t tx="ekr.20050920084036.184">def iterateKillBuffer (self):

    while 1:
        if self.killBuffer:
            self.last_clipboard = None
            for z in self.killBuffer:
                if self.reset:
                    self.reset = False
                    break
                yield z
</t>
<t tx="ekr.20050920084036.185">def getClipboard (self,w):

    try:
        ctxt = w.selection_get(selection='CLIPBOARD')
        if not self.killBuffer or ctxt != self.last_clipboard:
            self.last_clipboard = ctxt
            if not self.killBuffer or self.killBuffer [0] != ctxt:
                return ctxt
    except: pass

    return None</t>
<t tx="ekr.20050920085536.65">def masterCommand (self,event,func,stroke,commandName=None):

    '''This is the central dispatching method.
    All commands and keystrokes pass through here.'''

    k = self ; c = k.c
    c.setLog()
    trace = c.config.getBool('trace_masterCommand')
  
    c.startRedrawCount = c.frame.tree.redrawCount
    k.stroke = stroke # Set this global for general use.
    keysym = event and event.keysym or ''
    ch = event and event.char or ''
    w = event and event.widget
    state = event and hasattr(event,'state') and event.state or 0
    k.func = func
    k.funcReturn = None # For unit testing.
    commandName = commandName or func and func.__name__ or '&lt;no function&gt;'
    special = keysym in (
        'Caps_Lock','Num_Lock','Control_L','Alt_L','Shift_L','Control_R','Alt_R','Shift_R')
    interesting = func is not None
    inserted = not special

    if trace and interesting:
        g.trace(
            # 'stroke: ',stroke,'state:','%x' % state,'ch:',repr(ch),'keysym:',repr(keysym),
            'w:',w and c.widget_name(w),'func:',func and func.__name__
        )

    if inserted:
        # g.trace(stroke,keysym)
        &lt;&lt; add character to history &gt;&gt;
        
    # We *must not* interfere with the global state in the macro class.
    if c.macroCommands.recordingMacro:
        done = c.macroCommands.startKbdMacro(event)
        if done: return 'break'
        
    # g.trace(stroke,k.abortAllModesKey)

    if k.abortAllModesKey and stroke == k.abortAllModesKey: # 'Control-g'
        k.keyboardQuit(event)
        k.endCommand(event,commandName)
        return 'break'
        
    if special: # Don't pass these on.
        return 'break' 

    if 0: # *** This is now handled by k.masterKeyHandler.
        if k.inState():
            val = k.callStateFunction(event) # Calls end-command.
            if val != 'do-func': return 'break'
            g.trace('Executing key outside of mode')

    if k.regx.iter:
        try:
            k.regXKey = keysym
            k.regx.iter.next() # EKR: next() may throw StopIteration.
        finally:
            return 'break'

    if k.abbrevOn:
        expanded = c.abbrevCommands.expandAbbrev(event)
        if expanded: return 'break'

    if func: # Func is an argument.
        if trace: g.trace('command',commandName)
        if commandName.startswith('specialCallback'):
            # The callback function will call c.doCommand
            val = func(event)
            # k.simulateCommand uses k.funcReturn.
            k.funcReturn = k.funcReturn or val # For unit tests.
        else:
            # Call c.doCommand directly
            c.doCommand(func,commandName,event=event)
        if c.exists:
            k.endCommand(event,commandName)
            c.frame.updateStatusLine()
        return 'break'
    elif k.inState():
        return 'break' #Ignore unbound keys in a state.
    else:
        val = k.handleDefaultChar(event)
        if c.exists:
            c.frame.updateStatusLine()
        return val</t>
<t tx="ekr.20050920085536.67">if stroke or len(ch) &gt; 0:
    if len(keyHandlerClass.lossage) &gt; 99:
        keyHandlerClass.lossage.pop()
    keyHandlerClass.lossage.insert(0,(ch,stroke),)</t>
<t tx="ekr.20050923172809.1">def callStateFunction (self,event):
    
    k = self ; val = None
    
    # g.trace(k.state.kind)
    
    if k.state.kind:
        if k.state.handler:
            val = k.state.handler(event)
            if val != 'continue':
                k.endCommand(event,k.commandName)
        else:
            g.es_print('no state function for %s' % (k.state.kind),color='red')
            
    return val</t>
<t tx="ekr.20050923174229.3">def callKeystrokeFunction (self,event):
    
    '''Handle a quick keystroke function.
    Return the function or None.'''
    
    k = self
    numberOfArgs, func = k.keystrokeFunctionDict [k.stroke]

    if func:
        func(event)
        commandName = k.inverseCommandsDict.get(func) # Get the emacs command name.
        k.endCommand(event,commandName)
    
    return func</t>
<t tx="ekr.20050930091642.1">def yank (self,event):
    
    '''Insert the next entry in the kill ring at the insert point.'''

    k = self.k ; w = self.w
    i = w.index('insert')
    clip_text = self.getClipboard(w)

    if self.killBuffer or clip_text:
        self.reset = True
        s = clip_text or self.kbiterator.next()
        w.tag_delete('kb')
        w.insert('insert',s,('kb'))
        w.mark_set('insert',i)</t>
<t tx="ekr.20050930091642.2">def yankPop (self,event):
    
    '''Replaces the just-yanked kill buffer with the contents of the previous kill buffer.'''

    k = self.k ; w = event.widget
    i = w.index('insert') ; t, t1 = i.split('.')
    clip_text = self.getClipboard(w)

    if self.killBuffer or clip_text:
        if clip_text: s = clip_text
        else:         s = self.kbiterator.next()
        t1 = str(int(t1)+len(s))
        r = w.tag_ranges('kb')
        if r and r [0] == i:
            w.delete(r[0],r[-1])
        w.tag_delete('kb')
        w.insert('insert',s,('kb'))
        w.mark_set('insert',i)</t>
<t tx="ekr.20050930095323.1">def killSentence (self,event):
    
    '''Kill the sentence containing the cursor.'''

    w = event.widget
    i  = w.search('.','insert',stopindex='end')
    if i:
        i2 = w.search('.','insert',backwards=True,stopindex='1.0')
        i2 = g.choose(i2=='','1.0',i2+'+1c ')
        self.kill(event,i2,'%s + 1c' % i)</t>
<t tx="ekr.20050930100733">def killWs (self,event):
    
    ws = '' ; w = event.widget

    while 1:
        s = w.get('insert')
        if s in (' ','\t'):
            w.delete('insert')
            ws = ws + s
        else:
            break
            
    if ws:
        self.addToKillBuffer(ws)</t>
<t tx="ekr.20051013161232">def updateSettings (self,c,localFlag):

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
            g.trace(d and d.keys())</t>
<t tx="ekr.20051014152256"></t>
<t tx="ekr.20051026083544">def handleDefaultChar(self,event):
    
    k = self ; c = k.c
    w = event and event.widget
    name = c.widget_name(w)

    if name.startswith('body'):
        action = k.unboundKeyAction
        if action in ('insert','overwrite'):
            c.editCommands.selfInsertCommand(event,action=action)
        else: pass # Ignore the key.
        return 'break'
    elif name.startswith('head'):
        c.frame.tree.onHeadlineKey(event)
        return 'break'
    else:
        # Let tkinter handle the event.
        # ch = event and event.char ; g.trace('to tk:',name,repr(ch))
        return None</t>
<t tx="ekr.20051026083544.2">def updateHead (self,event,w):
    
    '''Update a headline from an event.
    
    The headline officially changes only when editing ends.'''
    
    c = self.c ; k = c.k
    ch = event and event.char or ''
    i,j = g.app.gui.getTextSelection(w)
    
    if ch == '\b':
        if i != j:  w.delete(i,j)
        else:       w.delete('insert-1c')
    elif ch and ch not in ('\n','\r'):
        if i != j:                              w.delete(i,j)
        elif k.unboundKeyAction == 'overwrite': w.delete(i,'%s+1c' % i)
        i = w.index('insert')
        w.insert(i,ch)

    s = w.get('1.0','end')
    if s.endswith('\n'):
        s = s[:-1]
    w.configure(width=self.headWidth(s=s))

    if ch in ('\n','\r'):
        self.endEditLabel() # Now calls self.onHeadChanged.
</t>
<t tx="ekr.20051026092433">def updateTab (self,p,w):

    c = self.c ; d = g.scanDirectives(c,p)
    tab_width = d.get("tabwidth",c.tab_width)
    
    i,j = g.app.gui.getTextSelection(w)
    if i != j:
        w.delete(i,j)
    if tab_width &gt; 0:
        w.insert("insert",'\t')
    else:
        # Get the preceeding characters.
        s = w.get("insert linestart","insert")
    
        # Compute n, the number of spaces to insert.
        width = g.computeWidth(s,tab_width)
        n = abs(tab_width) - (width % abs(tab_width))
        w.insert("insert",' ' * n)</t>
<t tx="ekr.20051026171121">i,j = oldSel

if i != j:
    # No auto-indent if there is selected text.
    w.delete(i,j)
    w.insert(i,ch)
else:
    w.insert(i,ch)
    allow_in_nocolor = c.config.getBool('autoindent_in_nocolor_mode')
    if (
        (allow_in_nocolor or c.frame.body.colorizer.useSyntaxColoring(p)) and
        undoType != "Change"
    ):
        # No auto-indent if in @nocolor mode or after a Change command.
        self.updateAutoIndent(p,w)</t>
<t tx="ekr.20051026171121.1"># By David McNab:
def updateAutoIndent (self,p,w):

    c = self.c ; d = g.scanDirectives(c,p)
    tab_width = d.get("tabwidth",c.tab_width) # Get the previous line.
    s = w.get("insert linestart - 1 lines","insert linestart -1c")
    # Add the leading whitespace to the present line.
    junk, width = g.skip_leading_ws_with_indent(s,0,tab_width)
    if s and len(s) &gt; 0 and s [ -1] == ':':
        # For Python: increase auto-indent after colons.
        if c.frame.body.colorizer.scanColorDirectives(p) == "python":
            width += abs(tab_width)
    if self.smartAutoIndent:
        # Determine if prev line has unclosed parens/brackets/braces
        bracketWidths = [width] ; tabex = 0
        for i in range(0,len(s)):
            if s [i] == '\t':
                tabex += tab_width-1
            if s [i] in '([{':
                bracketWidths.append(i+tabex+1)
            elif s [i] in '}])' and len(bracketWidths) &gt; 1:
                bracketWidths.pop()
        width = bracketWidths.pop()
    ws = g.computeLeadingWhitespace(width,tab_width)
    if ws:
        w.insert("insert",ws)</t>
<t tx="ekr.20051027172949">def updateAutomatchBracket (self,p,w,ch,oldSel):

    # assert ch in ('(',')','[',']','{','}')
    
    c = self.c ; d = g.scanDirectives(c,p) ; i,j = oldSel
    language = d.get('language')
    
    if ch in ('(','[','{',):
        automatch = language not in ('plain',)
        if automatch:
            ch = ch + {'(':')','[':']','{':'}'}.get(ch)
        if i != j:
            w.delete(i,j)
        w.insert(i,ch)
        if automatch:
            w.mark_set('insert','insert-1c')
    else:
        ch2 = w.get('insert')
        if ch2 in (')',']','}'):
            w.mark_set('insert','insert+1c')
        else:
            if i != j:
                w.delete(i,j)
            w.insert(i,ch)</t>
<t tx="ekr.20051031040240"></t>
<t tx="ekr.20051104152338"></t>
<t tx="ekr.20051104152338.1">@nocolor

http://sourceforge.net/forum/message.php?msg_id=3413805
By: nobody

I thought this might be for 4.4a2, but I see the same effect w/ 
Leo 4.3.3, build  1.282 , September 17, 2005
Python 2.3.5, Tk 8.4.7, win32

I haven't used Leo for code, but just started to try to re-organize some Perl I inherited.

Leo apears to remove sentinels, AND preceding newlines, so the effect is something
like this:

.... some code....

   next line;
}
#@ leo sentinel here...
#

    If  ( something ) {
      more code;
......

becomes:

.... some code....

   next line;
} If  ( something ) {
      more code;
......

Now, that may be annoying, but mildly so - it still runs.
When this:

#
#@ sentinel
if () {

turns to this:

# if() {

code just breaks.</t>
<t tx="ekr.20051125080855">def selfInsertCommand(self,event,action='insert'):
    
    '''Insert a character in the body pane.
    This is the default binding for all keys in the body pane.'''
    
    c = self.c ; p = c.currentPosition()
    ch = event and event.char or ''
    if event and event.keysym == 'Return': ch = '\n' # This fixes the MacOS return bug.
    w = event and event.widget
    name = c.widget_name(w)
    oldSel =  name.startswith('body') and g.app.gui.getTextSelection(w)
    oldText = name.startswith('body') and p.bodyString()
    undoType = 'Typing'
    trace = c.config.getBool('trace_masterCommand')
    brackets = ('(',')','[',']','{','}')
    
    if trace: g.trace(name,repr(ch),ch in brackets)
    
    if g.doHook("bodykey1",c=c,p=p,v=p,ch=ch,oldSel=oldSel,undoType=undoType):
        return "break" # The hook claims to have handled the event.
        
    if ch == '\t':
        self.updateTab(p,w)
    elif ch == '\b':
        # This is correct: we only come here if there no bindngs for this key. 
        self.backwardDeleteCharacter(event)
    elif ch in ('\r','\n'):
        ch = '\n'
        &lt;&lt; handle newline &gt;&gt;
    elif ch in brackets and self.autocompleteBrackets:
        self.updateAutomatchBracket(p,w,ch,oldSel)
    elif ch: # Null chars must not delete the selection.
        i,j = oldSel
        if i != j:                  w.delete(i,j)
        elif action == 'overwrite': w.delete(i,'%s+1c' % i)
        w.insert(i,ch)
        if ch in brackets and self.flashMatchingBrackets: # New in 4.4.1.
            self.flashMatchingBracketsHelper(w,i,ch)               
    else:
        return 'break' # New in 4.4a5: this method *always* returns 'break'
        
    # New in 4.4.1: Set the column for up and down keys.
    spot = w.index('insert')
    c.editCommands.setMoveCol(spot)

    # Update the text and handle undo.
    newText = g.app.gui.getAllText(w) # New in 4.4b3: converts to unicode.
    # g.trace(repr(newText))
    w.see(w.index('insert'))
    if newText != oldText:
        c.frame.body.onBodyChanged(undoType=undoType,
            oldSel=oldSel,oldText=oldText,oldYview=None)
            
    g.doHook("bodykey2",c=c,p=p,v=p,ch=ch,oldSel=oldSel,undoType=undoType)
    return 'break'</t>
<t tx="ekr.20051216151811">def clearKillRing (self,event=None):
    
    '''Clear the kill ring.'''
    
    self.killBuffer = []</t>
<t tx="ekr.20060102103625.1">def doMode(self,p,kind,name,val):
    
    '''Parse an @mode node and create the enter-&lt;name&gt;-mode command.'''
    
    __pychecker__ = '--no-argsused' # val not used.
    
    c = self.c ; k = c.k
    
    # g.trace('%20s' % (name),c.fileName())
    &lt;&lt; Compute modeName &gt;&gt;
    
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
    self.createModeCommand(modeName,d)</t>
<t tx="ekr.20060107082929"></t>
<t tx="ekr.20060117202916.1">def initMode (self,event,modeName):
    
    k = self ; c = k.c
    trace = c.config.getBool('trace_modes')
    if trace: g.trace(modeName)

    if not modeName:
        g.trace('oops: no modeName')
        return

    d = g.app.config.modeCommandsDict.get('enter-'+modeName)
    if not d:
        self.badMode(modeName)
        return
    else:
        k.modeBindingsDict = d
        
    k.inputModeName = modeName
    k.silentMode = False

    entryCommands = d.get('*entry-commands*',[])
    if entryCommands:
        for commandName in entryCommands:
            if trace: g.trace('entry command:',commandName)
            k.simulateCommand(commandName)
            
    # Create bindings after we know whether we are in silent mode.
    w = g.choose(k.silentMode,k.modeWidget,k.widget)
    k.createModeBindings(modeName,d,w)
        
    if k.silentMode:
        k.showStateAndMode()
    else:
        k.setLabelBlue(modeName+': ',protect=True)
        k.showStateAndMode()
        if k.useTextWidget:
            c.minibufferWantsFocus()
        else:
            pass # Do *not* change the focus here!</t>
<t tx="ekr.20060119150624">def createModeBindings (self,modeName,d,w):
    
    '''Create mode bindings for the named mode using dictionary d for widget w.'''
    
    __pychecker__ = '--no-argsused' # w not used (except for debugging).
    
    k = self ; c = k.c
        
    # g.trace(g.listToString(d.keys()))

    for commandName in d.keys():
        if commandName == '*entry-commands*': continue
        func = c.commandsDict.get(commandName)
        if not func:
            g.es_print('No such command: %s. Referenced from %s' % (
                commandName,modeName))
            continue
        bunchList = d.get(commandName,[])
        for bunch in bunchList:
            stroke = bunch.val
            # Important: bunch.val is a stroke returned from k.strokeFromSetting.
            # Do not call k.strokeFromSetting again here!
            if stroke and stroke not in ('None','none',None):
                if 0:
                    g.trace(
                        g.app.gui.widget_name(w), modeName,
                        '%10s' % (stroke),
                        '%20s' % (commandName),
                        bunch.nextMode)
                        
                k.makeMasterGuiBinding(stroke)
               
                # Create the entry for the mode in k.masterBindingsDict.
                # Important: this is similar, but not the same as k.bindKeyToDict.
                # Thus, we should **not** call k.bindKey here!
                d2 = k.masterBindingsDict.get(modeName,{})
                d2 [stroke] = g.Bunch(
                    commandName=commandName,
                    func=func,
                    nextMode=bunch.nextMode,
                    stroke=stroke)
                k.masterBindingsDict [ modeName ] = d2</t>
<t tx="ekr.20060120084705">@nocolor

Note: Editing headline text will happen in insert mode unless

@strings top_level_unbound_key_action = overwrite


@color</t>
<t tx="ekr.20060527204444">- Add all features used by Php.

- Add all other features.</t>
<t tx="ekr.20060531161030"></t>
<t tx="ekr.20060531161030.1"></t>
<t tx="ekr.20060618110649">name = name.strip().lower()
j = name.find(' ')
if j &gt; -1: name = name[:j]
if name.endswith('mode'):
    name = name[:-4].strip()
if name.endswith('-'):
    name = name[:-1]
modeName = name + '-mode'</t>
<t tx="ekr.20060623064600">@nocolor

- Improved prompt.
- Added message if no previous complex command.
- Added mode entries.</t>
<t tx="ekr.20060624072803"></t>
<t tx="ekr.20060624072803.1"></t>
<t tx="ekr.20060624072803.2"></t>
<t tx="ekr.20060624072803.3"></t>
<t tx="ekr.20060624072803.4"></t>
<t tx="ekr.20060624080605"></t>
<t tx="ekr.20060624085200">def handleScriptException (c,p,script,script1):

    g.es("exception executing script",color='blue')

    fileName, n = g.es_exception(full=True,c=c)
    
    g.trace(fileName,n)

    if p and not script1 and fileName == "&lt;string&gt;":
        c.goToScriptLineNumber(p,script,n)

    &lt;&lt; dump the lines near the error &gt;&gt;</t>
<t tx="ekr.20060624085200.1">@nocolor

http://sourceforge.net/forum/message.php?msg_id=3510448

The fix was to getLastTracebackFileAndLineNumber.

I also created handleScriptException.</t>
<t tx="ekr.20060625061210"></t>
<t tx="ekr.20060625072145">@nocolor

http://sourceforge.net/forum/message.php?msg_id=3795258

The column display doesn't change while typing.

</t>
<t tx="ekr.20060625072145.1"></t>
<t tx="ekr.20060625072145.2">@nocolor

http://sourceforge.net/forum/message.php?msg_id=3794854
By: ktenney

I see what happened, I changed my 'home' setting
to please other apps.

Any chance Leo could add a 4th location to look for
leoSettings.leo, namely the directory which the 
current Leo file came from?

I haul my files around on a usb key, and it would
be great if the settings could live in the same
dir as the Leo files.</t>
<t tx="ekr.20060625173330">Improve import code so it handles stufff like this from Ipyton/iplib

### This should *not* terminate the function!

    self.LOGHEAD = Itpl(
"""#log# Automatic Logger file. *** THIS MUST BE THE FIRST LINE ***
#log# DO NOT CHANGE THIS LINE OR THE TWO BELOW
#log# opts = $self.rc.opts
#log# args = $self.rc.args
#log# It is safe to make manual edits below here.
#log#-----------------------------------------------------------------------
""")

- Handle blanks better in imports:
    - Add tab_width keyword arg to import command.
    - Convert tabs to blanks if tab width &lt; 0.
- Ignore position of blank lines wrt sentinels.
- Ignore (optionally?) underindented blank lines.
- Use pyclbr to parse Python imports?</t>
<t tx="ekr.20060626083237.1">def skipPythonDef (self,s,i,start):
    
    # g.trace(g.get_line(s,i))

    # Set defIndent to the indentation of the def line.
    defIndent = self.getLeadingIndent(s,start)
    parenCount = 0
    &lt;&lt; skip the entire signature &gt;&gt;
    indent = self.getLeadingIndent(s,i)
    while i &lt; len(s): # and indent &gt; defIndent
        progress = i
        ch = s[i]
        if g.is_nl(s,i):
            backslashNewline = i &gt; 0 and g.match(s,i-1,"\\\n")
            i = g.skip_nl(s,i)
            if not backslashNewline:
                # New in Leo 4.4.1: don't set indent for comment lines.
                j = g.skip_ws(s,i)
                if not g.match(s,j,'#'):
                    indent = self.getLeadingIndent(s,i)
                    if indent &lt;= defIndent and parenCount == 0:
                        break
        elif ch == '#':
            i = g.skip_to_end_of_line(s,i)
        elif ch == '"' or ch == '\'':
            i = g.skip_python_string(s,i)
        elif ch in '[{(':
            i += 1 ; parenCount += 1
            # g.trace('ch',ch,parenCount)
        elif ch in ']})':
            i += 1 ; parenCount -= 1
            # g.trace('ch',ch,parenCount)
        else: i += 1
        assert(progress &lt; i)
        
    return i</t>
<t tx="ekr.20060626083237.2">def test_skipPythonDef (self):

    global c # Get syntax warning if this is not first.
    if self: c = self.c             # Run from @test node: c not global
    else: self = c.importCommands   # Run from @suite: c *is* global

    d = g.scanDirectives(c)
    self.tab_width = d.get("tabwidth")
    verbose = False
    &lt;&lt; define s &gt;&gt;
    start = 0
    i = self.skipPythonDef(s,i=0,start=start)
    result = s[start:i].strip()
    if verbose: g.trace(result)
    assert result.startswith('def test1') and result.endswith('return 1'),'result:\n%s' % result
    start = i
    i = self.skipPythonDef(s,i=i,start=start)
    result = s[start:i].strip()
    if verbose: g.trace(result)
    assert result.startswith('def test2') and result.endswith('pass'),'result:\n%s' % result</t>
<t tx="ekr.20060626083725">s = '''\
def test1():
    aList = (a,
b,c)
# underindented comment.
    return 1

def test2():
# underindented comment.
    pass
'''

s = g.adjustTripleString(s,self.tab_width)</t>
<t tx="ekr.20060626100102">def scanPythonClassHelper(self,s,i,class_indent,class_name,class_vnode):
    
    indent =  self.getLeadingIndent(s,i)
    start = i = g.skip_blank_lines(s,i)
    parent_vnode = None
    while i &lt; len(s):
        progress = i
        # New in Leo 4.4.1: ignore comment lines, whatever their indentation.
        if indent &lt;= class_indent:
            j = g.skip_ws(s,i)
            if g.match(s,j,'#'):
                i = g.skip_to_end_of_line(s,j)
            else: break
        if g.is_nl(s,i):
            backslashNewline = i &gt; 0 and g.match(s,i-1,"\\\n")
            j = g.skip_nl(s,i)
            if not backslashNewline:
                indent = self.getLeadingIndent(s,j)
                if indent &gt; class_indent: i = j
                else: break
            else: i = j
        elif g.match_c_word(s,i,"def"):
            if not parent_vnode:
                self.createParentText(class_vnode,class_name)
                parent_vnode = class_vnode
            i = start = self.scanPythonDef(s,i,start,parent_vnode)
            indent = self.getLeadingIndent(s,i)
        elif g.match_c_word(s,i,"class"):
            if not parent_vnode:
                self.createParentText(class_vnode,class_name)
                parent_vnode = class_vnode
            i = start = self.scanPythonClass(s,i,start,parent_vnode)
            indent = self.getLeadingIndent(s,i)
        elif s[i] == '#': i = g.skip_to_end_of_line(s,i)
        elif s[i] == '"' or s[i] == '\'': i = g.skip_python_string(s,i)
        else: i += 1
        assert(progress &lt; i)
    return start,i
</t>
<t tx="ekr.20060626100102.1">def test_scanPythonClass (self):

    global c # Get syntax warning if this is not first.
    if self: c = self.c             # Run from @test node: c not global
    else: self = c.importCommands   # Run from @suite: c *is* global

    d = g.scanDirectives(c)
    self.tab_width = d.get("tabwidth")
    verbose = False
    &lt;&lt; define s &gt;&gt;
    start = 0
    i = self.skipPythonDef(s,i=0,start=start)
    result = s[start:i].strip()
    if verbose: g.trace(result)
    assert result.startswith('class aClass') and result.endswith("'eggs'"),'result:\n%s' % result
    start = i
    i = self.skipPythonDef(s,i=i,start=start)
    result = s[start:i].strip()
    if verbose: g.trace(result)
    assert result.startswith('class aClass2') and result.endswith("'twit'"),'result:\n%s' % result</t>
<t tx="ekr.20060626100102.2">s = '''\
class aClass:
    def spam():
        return 'spam'
# underindented comment line
    def eggs():
        return 'eggs'
        
class aClass2:
    def twit():
        return 'twit'
'''

s = g.adjustTripleString(s,self.tab_width)</t>
<t tx="ekr.20060626101103.1">def createParentText (self,class_vnode,class_name):

    '''Insert the proper body text in the class_vnode.'''
    
    # This must be done after the declaration reference is generated.
    if self.treeType == "@file":
        class_vnode.appendStringToBody("\t@others\n")
    else:
        ref = g.angleBrackets(' class %s methods ' % (class_name))
        class_vnode.appendStringToBody("\t" + ref + "\n\n")</t>
<t tx="ekr.20060626103415">def createClassNodeText (self,s,i,start):
    
    # Create the section name using the old value of self.methodName.
    if  self.treeType == "@file":
        prefix = ""
    else:
        prefix = g.angleBrackets(" " + self.methodName + " methods ") + "=\n\n"
        self.methodsSeen = True
    
    # i points just after the class line.
    
    # Add a docstring to the class node.
    docStringSeen = False
    j = g.skip_ws_and_nl(s,i)
    if g.match(s,j,'"""') or g.match(s,j,"'''"):
        j = g.skip_python_string(s,j)
        if j != len(s): # No scanning error.
            i = j ; docStringSeen = True
    
    body = s[start:i]
    body = self.undentBody(body)
    if docStringSeen: body = body + '\n'
    
    return i,prefix,body</t>
<t tx="ekr.20060627062652"># Now that we count parens, we must be careful to skip the entire signature.

j = s.find('(',i)
if j != -1:
    j = g.skip_matching_python_parens(s,j)

if j == -1 or not g.match(s,j+1,':'):
    g.es_print('Warning: improper signature: %s' % g.get_line(s,i))
    return i
else:
    i = g.skip_line(s,j) # Still not quite 100% correct.</t>
<t tx="ekr.20060627063313">def test_skipPythonDef2 (self):
    
    '''Tests of long signature lines.'''

    global c # Get syntax warning if this is not first.
    if self: c = self.c             # Run from @test node: c not global
    else: self = c.importCommands   # Run from @suite: c *is* global

    d = g.scanDirectives(c)
    self.tab_width = d.get("tabwidth")
    verbose = False
    &lt;&lt; define s &gt;&gt;
    start = 0
    i = self.skipPythonDef(s,i=0,start=start)
    result = s[start:i].strip()
    if verbose: g.trace(result)
    assert result.startswith('def test1') and result.endswith('return 1'),'result:\n%s' % result
    start = i
    i = self.skipPythonDef(s,i=i,start=start)
    result = s[start:i].strip()
    if verbose: g.trace(result)
    assert result.startswith('def test2') and result.endswith('return 2'),'result:\n%s' % result</t>
<t tx="ekr.20060627063313.1">s = '''\
def test1(
        a=2):
    return 1

def test2(
a=3):
    return 2
'''

s = g.adjustTripleString(s,self.tab_width)</t>
<t tx="ekr.20060627063640">Definitions such as the following caused problems:
    
@color

def __init__(self, parent, id=-1, title="", pos=wx.DefaultPosition,
        size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):

    wx.Frame.__init__(self, parent, id, title, pos, size, style)
    
@nocolor

The import code wasn't skipping the entire signature, so the indentation wasn't computed properly.</t>
<t tx="ekr.20060627070101">When True, this provides a full traceback for all exceptions taken when binding keyboard shortcuts.</t>
<t tx="ekr.20060627075911">@nocolor

Here are the relevant settings:
    
@bool flash_matching_brackets: True: flash matching bracket when typing (, ), [, ], { or }.

\@color flash_brackets_background_color and @color flash_brackets_foreground_color.

@int flash_brackets_count: The number of times to flash matching brackets.

@int flash-brackets-delay: One half the total cycle time of bracket flashes, in milliseconds.

@color</t>
<t tx="ekr.20060627080947">def skip_matching_python_parens(s,i):

    '''Skip from the opening ( to the matching ).
    
    Return the index of the matching ')', or -1'''
    
    return skip_matching_python_delims(s,i,'(',')')</t>
<t tx="ekr.20060627083506">def flashMatchingBracketsHelper (self,w,index,ch):

    s = g.app.gui.getAllText(w)
    i = g.app.gui.toPythonIndex(s,w,index)
    # g.trace(index,i,ch)

    if ch in ('(','{','['):
        d = {'(': ')', '{': '}', '[': ']'}
        reverse = False # Search forward
    else:
        d = {')': '(', '}': '{', ']': '['}
        reverse = True # Search backward

    delim2 = d.get(ch)
    j = g.skip_matching_python_delims(s,i,ch,delim2,reverse=reverse)
    if j != -1:
        j = g.app.gui.toGuiIndex(s,w,j)
        self.flashCharacter(w,j)</t>
<t tx="ekr.20060627091557">def flashCharacter(self,w,i):
    
    bg      = self.bracketsFlashBg or 'DodgerBlue1'
    fg      = self.bracketsFlashFg or 'white'
    flashes = self.bracketsFlashCount or 2
    delay   = self.bracketsFlashDelay or 75

    def addFlashCallback(w,count,index):
        w.tag_add('flash',index,'%s+1c' % (index))
        w.after(delay,removeFlashCallback,w,count-1,index)
    
    def removeFlashCallback(w,count,index):
        w.tag_remove('flash','1.0','end')
        if count &gt; 0:
            w.after(delay,addFlashCallback,w,count,index)

    try:
        w.tag_configure('flash',foreground=fg,background=bg)
        addFlashCallback(w,flashes,i)
    except Exception:
        pass</t>
<t tx="ekr.20060627122419">@killcolor

@bool flash_matching_brackets: True: flash matching bracket when typing (, ), [, ], { or }.

@color flash_brackets_background_color and @color flash_brackets_foreground_color.

@int flash_brackets_count: The number of times to flash matching brackets.

@int flash-brackets-delay: One half the total cycle time of bracket flashes, in milliseconds.</t>
<t tx="ekr.20060627141422">@nocolor

After executing a command we must be careful to test c.exists.

@color</t>
<t tx="ekr.20060628094329"># Ctrl-k is no longer needed by the match-brackets command now that brackets flash automatically.</t>
<t tx="ekr.20060628094329.1">@nocolor

- A better trace, and the trace goes to the log pane.

- Eliminated k.keysymHistory: Tk keysyms are pretty useless.

@color</t>
<t tx="ekr.20060628094329.2"></t>
<t tx="ekr.20060628095110">Blank lines: deletes the newline.
Non-blank lines: deletes up to the newline.</t>
<t tx="ekr.20060628103226"></t>
<t tx="ekr.20060628103226.2"></t>
<t tx="ekr.20060628103226.3"></t>
</tnodes>
</leo_file>
