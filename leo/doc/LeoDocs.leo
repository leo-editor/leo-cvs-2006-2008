<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet ekr_stylesheet?>
<leo_file>
<leo_header file_format="2" tnodes="0" max_tnode_index="26108" clone_windows="0"/>
<globals body_outline_ratio="0.5">
	<global_window_position top="104" left="160" height="646" width="1021"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="ekr.20050404094627"><vh>Settings and buttons</vh>
<v t="ekr.20041226081019"><vh>@button Spell</vh></v>
<v t="ekr.20050812090111"><vh>@button rst3</vh></v>
<v t="ekr.20050407144417"><vh>@settings</vh>
<v t="ekr.20050407144342"><vh>@page http plugin</vh>
<v t="ekr.20050407144342.1"><vh>@bool http_active = False</vh></v>
<v t="ekr.20050407144342.2"><vh>@int  port = 8080</vh></v>
<v t="ekr.20050407144342.3"><vh>@string rst_http_attributename = rst_http_attribute</vh></v>
</v>
<v t="ekr.20050812123002"><vh>@page rst3 options</vh>
<v t="ekr.20050812123002.1"><vh>Http options...</vh>
<v t="ekr.20050812123002.2"><vh>@bool rst3_clear_http_attributes = False</vh></v>
<v t="ekr.20050812123002.3"><vh>@string rst3_http_attributename = 'rst_http_attribute'</vh></v>
<v t="ekr.20050812123002.4"><vh>@bool rst3_http_server_support = False</vh></v>
<v t="ekr.20050812123002.5"><vh>@string rst3_node_begin_marker = 'http-node-marker-'</vh></v>
</v>
<v t="ekr.20050812123002.6"><vh>@bool rst3_massage_body = False</vh></v>
<v t="ekr.20050812123002.7"><vh>@bool rst3_format_headlines = True</vh></v>
<v t="ekr.20050812123002.8"><vh>@bool rst3_write_intermediate_file = True</vh></v>
<v t="ekr.20051202072010"><vh>@string rst3_default_path =</vh></v>
</v>
</v>
<v t="ekr.20050901054622"><vh>@button Save</vh></v>
<v t="ekr.20050901055150"><vh>@@button promote</vh></v>
<v t="ekr.20050901060119"><vh>@@button def list</vh>
<v t="ekr.20050901061220"><vh>createDefList</vh></v>
</v>
<v t="ekr.20050901121617"><vh>@@button sentence</vh>
<v t="ekr.20050901121617.1"><vh>splitSentences</vh></v>
</v>
<v t="ekr.20050902080416"><vh>@@button reformat-paragraph</vh></v>
<v t="ekr.20060525104232"><vh>@@button rst-&gt;html</vh></v>
<v t="ekr.20060525110135"><vh>@@button rst-&gt;pdf</vh></v>
<v t="ekr.20060525110135.1"><vh>@@button rst-&gt;tex</vh></v>
<v t="ekr.20060525110217"><vh>@@button rst-&gt;rst</vh></v>
</v>
<v t="ekr.20050831195449"><vh>Read me first</vh></v>
<v t="edream.110203163054.46" a="E"><vh>Release Notes</vh>
<v t="edream.110203163054.117"><vh>Previous versions...</vh>
<v t="ekr.20060206111717"><vh>Ancient...</vh>
<v t="edream.110203163054.118"><vh>3.x...</vh>
<v t="edream.110203163054.119"><vh>3.12 final</vh>
<v t="edream.110203163054.120"><vh>Bug fixes (major)</vh>
<v t="edream.110203163054.121"><vh>Fixed major undo bug</vh></v>
<v t="edream.110203163054.122"><vh>Fixed huge performance bug when handling read errors</vh></v>
<v t="edream.110203163054.123"><vh>Fixed memory leaks: one minor, one huge</vh></v>
</v>
<v t="edream.110203163054.124"><vh>Bug fixes (minor)</vh>
<v t="edream.110203163054.125"><vh>Fixed bug affecting encoding in headlines</vh></v>
<v t="edream.110203163054.126"><vh>Fixed bug affecting log pane</vh></v>
<v t="edream.110203163054.127"><vh>Fixed bug importing files with upper case extensions</vh></v>
<v t="edream.110203163054.128"><vh>Fixed bug involving log messages during Open commands</vh></v>
<v t="edream.110203163054.129"><vh>Fixed bug that caused some log messages to disappear</vh></v>
<v t="edream.110203163054.130"><vh>Fixed bug that disabled double-clicking when when windows were first opened</vh></v>
<v t="edream.110203163054.131"><vh>Fixed bug that forced body_pane_wraps setting to 1</vh></v>
<v t="edream.110203163054.132"><vh>Fixed bug when deleting trailing newlines in the body pane</vh></v>
<v t="edream.110203163054.133"><vh>Fixed colorizer exception when undoing paste</vh></v>
<v t="edream.110203163054.134"><vh>Fixed Go To Line Number bug</vh></v>
<v t="edream.110203163054.135"><vh>Fixed line-break bug with @nosent files</vh></v>
<v t="edream.110203163054.136"><vh>Fixed new Open With problems</vh></v>
<v t="edream.110203163054.137"><vh>Fixed problems with Convert tabs to blanks preference panel setting</vh></v>
<v t="edream.110203163054.138"><vh>Fixed problems with the code that destroys Leo windows</vh></v>
<v t="edream.110203163054.139"><vh>Fixed recent bug in the Reformat Paragraph command</vh></v>
<v t="edream.110203163054.140"><vh>Fixed refresh problem after Read @file Node command</vh></v>
<v t="edream.110203163054.141"><vh>Fixed several problems with the Open With command</vh></v>
<v t="edream.110203163054.142"><vh>Fixed Sort bug</vh></v>
<v t="edream.110203163054.143"><vh>Leo now updates ow/col numbers when plugins not enabled</vh></v>
<v t="edream.110203163054.144"><vh>Made dragging nodes more robust</vh></v>
<v t="edream.110203163054.145"><vh>Removed improper clones from LeoPy.leo</vh></v>
<v t="edream.110203163054.146"><vh>Removed unused fractional widths from leoFind code</vh></v>
<v t="edream.110203163054.147"><vh>updateRecentFiles now handles Null filenames properly</vh></v>
</v>
<v t="edream.110203163054.148"><vh>Code improvements</vh>
<v t="edream.110203163054.149"><vh>New functions in leoGlobals.py</vh></v>
<v t="edream.110203163054.150"><vh>New scripts</vh></v>
<v t="edream.110203163054.151"><vh>Rewrote dialog code</vh></v>
<v t="edream.110203163054.152"><vh>Reorganized vnodes and tnodes</vh></v>
<v t="edream.110203163054.153"><vh>Simplified startup code</vh></v>
<v t="edream.110203163054.154"><vh>Replaced exec with getattr/setattr throughout the code</vh></v>
</v>
<v t="edream.110203163054.155"><vh>Features</vh>
<v t="edream.110203163054.156"><vh>Added @wrap and @nowrap directives</vh></v>
<v t="edream.110203163054.157"><vh>Added apply button to Font panel</vh></v>
<v t="edream.110203163054.158"><vh>Added Icon &amp; Status areas to Leo window</vh></v>
<v t="edream.110203163054.159"><vh>Added minimal support for Rebol and activescript languages</vh></v>
<v t="edream.110203163054.160"><vh>Added Write Dirty @file Nodes command</vh></v>
<v t="edream.110203163054.161"><vh>Changed OnIconDoubleClick to allow @url url comments</vh></v>
<v t="edream.110203163054.162"><vh>Hyperlinks are now enabled by default</vh></v>
<v t="edream.110203163054.163"><vh>Improved how headlines are highlighted</vh></v>
<v t="edream.110203163054.164"><vh>Improved startup logic so only one frame ever gets opened</vh></v>
<v t="edream.110203163054.165"><vh>Improved the reporting of characters that do not exist in the present encoding</vh></v>
<v t="edream.110203163054.166"><vh>Leo now correctly remembers the sizes of windows</vh></v>
<v t="edream.110203163054.167"><vh>Removed toggle &lt;&lt; &gt;&gt; command</vh></v>
<v t="edream.110203163054.168"><vh>Undo now restores cursor</vh></v>
<v t="edream.110203163054.169"><vh>Updated Marks window in Mark Find and Mark Changes commands</vh></v>
<v t="edream.110203163054.170"><vh>Use "file in directory" format for entries in Recent Files list</vh></v>
</v>
<v t="edream.110203163054.171"><vh>Hooks</vh>
<v t="edream.110203163054.172"><vh>About hooks</vh></v>
<v t="edream.110203163054.173"><vh>Added "clear-mark" and "set-mark" hooks</vh></v>
<v t="edream.110203163054.174"><vh>Added hooks to customize popup menus</vh></v>
<v t="edream.110203163054.175"><vh>Added new hooks so that plugins may extend popup menus </vh></v>
</v>
<v t="edream.110203163054.176"><vh>Plugins</vh>
<v t="edream.110203163054.177"><vh>Added add_directives.py plugin</vh></v>
<v t="edream.110203163054.178"><vh>Added color_markup.py plugin</vh></v>
<v t="edream.110203163054.179"><vh>Added nav_buttons.py plugin</vh></v>
<v t="edream.110203163054.180"><vh>Added plugins_menu.py plugin</vh></v>
<v t="edream.110203163054.181"><vh>Added scripts_menu.py plugin</vh></v>
<v t="edream.110203163054.182"><vh>Improved how Leo loads plugins</vh></v>
</v>
<v t="edream.110203163054.183"><vh>Reorganized Leo folder: big change to cvs</vh>
<v t="edream.110203163054.184"><vh>Added scripts for Linux</vh></v>
</v>
</v>
<v t="edream.110203163054.185"><vh>3.11.1</vh></v>
<v t="edream.110203163054.186"><vh>3.11</vh>
<v t="edream.110203163054.187"><vh>New in 3.11 final</vh>
<v t="edream.110203163054.188"><vh>Bug fixes</vh>
<v t="edream.110203163054.189"><vh>Added call to c.redraw() in fileCommands.readAtFileNodes</vh></v>
<v t="edream.110203163054.190"><vh>Added getpreferredencoding to leoGlobals.py</vh></v>
<v t="edream.110203163054.191"><vh>Eliminated caught exception in frame.setTabWidth</vh></v>
<v t="edream.110203163054.192"><vh>Fixed bug in skip_long</vh></v>
<v t="edream.110203163054.193"><vh>Fixed bug that prevented email line in About Leo from working</vh></v>
<v t="edream.110203163054.194"><vh>Fixed unicode bugs when Tangling and Untangling</vh></v>
<v t="edream.110203163054.195"><vh>Fixed various bugs reported by Pychecker</vh></v>
<v t="edream.110203163054.196"><vh>Removed all __del__ methods</vh></v>
</v>
<v t="edream.110203163054.197"><vh>New and improved features and commands</vh>
<v t="edream.110203163054.198"><vh>Added patch by Davide Salomoni to OnIconDoubleClick</vh></v>
<v t="edream.110203163054.199"><vh>@lineending directive specifies line endings</vh></v>
<v t="edream.110203163054.200"><vh>Added thin_at_file_trees &amp; load_derived_files_immediately options</vh></v>
</v>
</v>
<v t="edream.110203163054.201"><vh>** Leo now uses unicode internally</vh>
<v t="edream.110203163054.202"><vh>Added calls to toEncodedString before all calls to write</vh></v>
<v t="edream.110203163054.203"><vh>Check for valid encoding when setting app().tkEncoding</vh></v>
<v t="edream.110203163054.204"><vh>How Leo handles unicode</vh></v>
<v t="edream.110203163054.205"><vh>Unicode settings</vh></v>
<v t="edream.110203163054.206"><vh>Unicode theory of operation</vh></v>
<v t="edream.110203163054.207"><vh>Use app().tkEncoding when writing to log pane</vh></v>
</v>
<v t="edream.110203163054.208"><vh>** Improved hooks &amp; a new plugin architecture</vh>
<v t="edream.110203163054.217"><vh>Major reorganization of hooks</vh>
<v t="edream.110203163054.218"><vh>About hooks</vh></v>
</v>
<v t="edream.110203163054.219"><vh>Added several new plugins</vh></v>
<v t="edream.110203163054.220"><vh>Improved Open With plugin</vh></v>
<v t="edream.110203163054.221"><vh>Added logic to retain log output until a log exists</vh></v>
</v>
<v t="edream.110203163054.222"><vh>New configuration options &amp; plugins</vh>
<v t="edream.110203163054.223"><vh>Plugins</vh></v>
<v t="edream.110203163054.205"><vh>Unicode settings</vh></v>
<v t="edream.110203163054.224"><vh>Colors for Show Invisibibles command</vh></v>
<v t="edream.110203163054.225"><vh>look_for_control_drag_on_mouse_down option</vh></v>
<v t="edream.110203163054.226"><vh>body_insertion_cursor_color setting</vh></v>
<v t="edream.110203163054.227"><vh>time/date settings</vh></v>
</v>
<v t="edream.110203163054.228"><vh>New commands</vh>
<v t="edream.110203163054.229"><vh>Toggle Angle Brackets</vh></v>
<v t="edream.110203163054.230"><vh>Insert Body/Headline Time/Date</vh></v>
<v t="edream.110203163054.231"><vh>Go To First/last Node</vh></v>
<v t="edream.110203163054.232"><vh>Go To Parent</vh></v>
<v t="edream.110203163054.233"><vh>Go To Next/Previous Sibling</vh></v>
<v t="edream.110203163054.234"><vh>Write Missing @file Nodes</vh></v>
</v>
<v t="edream.110203163054.235"><vh>Improved commands</vh>
<v t="edream.110203163054.236"><vh>Added support for body/headline_gmt_time settings</vh></v>
<v t="edream.110203163054.237"><vh>Tangle now supports output_newline option</vh></v>
<v t="edream.110203163054.238"><vh>Major improvements to expand/contract commands</vh></v>
<v t="edream.110203163054.239"><vh>Leo now allows multiple writes of cloned nodes</vh></v>
<v t="edream.110203163054.240"><vh>The Sort Siblings command can now sort top-level nodes</vh></v>
<v t="edream.110203163054.241"><vh>Changed locks on customizeLeo.py</vh></v>
</v>
<v t="edream.110203163054.242"><vh>Other improvements</vh>
<v t="edream.110203163054.243"><vh>Allow color param when queuing messages to log pane</vh></v>
<v t="edream.110203163054.244"><vh>Improved scrolling when moving right</vh></v>
<v t="edream.110203163054.245"><vh>Put file name first in window title</vh></v>
<v t="edream.110203163054.246"><vh>Leo scrolls partially visible headlines into full view</vh></v>
<v t="edream.110203163054.247"><vh>Allowed @comment with @language plain</vh></v>
<v t="edream.110203163054.248"><vh>The Find button is now default button in the Find panel</vh></v>
<v t="edream.110203163054.249"><vh>Improved syntax coloring for html and xml</vh>
</v>
<v t="edream.110203163054.251"><vh>Improved Prefs panel</vh></v>
<v t="edream.110203163054.252"><vh>Removed setup.py from distributed files</vh></v>
</v>
<v t="edream.110203163054.253"><vh>Bug fixes</vh>
<v t="edream.110203163054.254"><vh>Eliminated potential hang in Open With command</vh></v>
<v t="edream.110203163054.255"><vh>Fixed 2 line number bugs</vh></v>
<v t="edream.110203163054.256"><vh>Fixed bug involving nested comments in sentinel lines</vh></v>
<v t="edream.110203163054.257"><vh>Fixed bugs in promote/demote</vh></v>
<v t="edream.110203163054.258"><vh>Fixed configuration bug.</vh></v>
<v t="edream.110203163054.259"><vh>Fixed crasher in undo logic</vh></v>
<v t="edream.110203163054.260"><vh>Fixed drag problem</vh></v>
<v t="edream.110203163054.261"><vh>Fixed huge performance bug in v.unjoinNode</vh></v>
<v t="edream.110203163054.262"><vh>Fixed long-standing control-v bug on Linux</vh></v>
<v t="edream.110203163054.263"><vh>Fixed minor import bugs</vh></v>
<v t="edream.110203163054.264"><vh>Fixed problem with block comments</vh></v>
<v t="edream.110203163054.265"><vh>Fixed several problems revealed by French plugin</vh></v>
<v t="edream.110203163054.266"><vh>Fixed several problems with noweb mode</vh></v>
<v t="edream.110203163054.267"><vh>Fixed syntax coloring bugs</vh></v>
<v t="edream.110203163054.268"><vh>Full recolor after paste</vh></v>
<v t="edream.110203163054.269"><vh>Installer now creates plugins directory</vh></v>
<v t="edream.110203163054.270"><vh>Removed duplicate redraws when renaming nodes</vh></v>
<v t="edream.110203163054.271"><vh>Udated recent files menu when saving a new .leo file</vh></v>
<v t="edream.110203163054.272"><vh>Worked around bugs in Python 2.3 a1</vh></v>
</v>
</v>
<v t="edream.110203163054.273"><vh>3.10</vh>
<v t="edream.110203163054.274"><vh>Fixed bugs</vh>
<v t="edream.110203163054.275"><vh>Allowed abbreviated xml tags.</vh></v>
<v t="edream.110203163054.276"><vh>Changed shortcut to Find Previous so Alt - F4 closes Leo</vh></v>
<v t="edream.110203163054.277"><vh>Changed url of help file</vh></v>
<v t="edream.110203163054.278"><vh>Fixed @nsf bug reported by Travers A. Hough</vh></v>
<v t="edream.110203163054.279"><vh>Fixed a bug in Untangle</vh></v>
<v t="edream.110203163054.280"><vh>Fixed bug in Python importer</vh></v>
<v t="edream.110203163054.281"><vh>Fixed bug involving redrawing screen initially</vh></v>
<v t="edream.110203163054.282"><vh>Fixed bugs involving @nosentinelsfile</vh></v>
<v t="edream.110203163054.283"><vh>Fixed crashers in colorizeAnyLanguage</vh></v>
<v t="edream.110203163054.284"><vh>Fixed environment bug in Execute Script command</vh></v>
<v t="edream.110203163054.285"><vh>Fixed major memory leak</vh></v>
<v t="edream.110203163054.286"><vh>Fixed path problem in paths passed to tangle_done.py</vh></v>
<v t="edream.110203163054.287"><vh>Fixed problems with Open With code in customizeLeo.py</vh></v>
<v t="edream.110203163054.288"><vh>Fixed Recent Files command</vh></v>
<v t="edream.110203163054.289"><vh>Fixed reversion involving @comment &amp; @language together</vh></v>
<v t="edream.110203163054.290"><vh>Fixed undo bug</vh></v>
</v>
<v t="edream.110203163054.291"><vh>Added features</vh>
<v t="edream.110203163054.292"><vh>New Mark Clones and Go To Next Clone commands.</vh></v>
<v t="edream.110203163054.293"><vh>New Export Headlines command</vh></v>
<v t="edream.110203163054.294"><vh>Control-dragging a node now clones it</vh></v>
<v t="edream.110203163054.295"><vh>New "Node Only checkbox in the Find/Change panel</vh></v>
<v t="edream.110203163054.296"><vh>@root options</vh></v>
<v t="edream.110203163054.297"><vh>Converted leoConfig.py to use @root-code</vh></v>
<v t="edream.110203163054.298"><vh>Added @file options</vh></v>
<v t="edream.110203163054.299"><vh>Added support for underlined menu items</vh></v>
<v t="edream.110203163054.300"><vh>Improved Leo's window icon</vh></v>
<v t="edream.110203163054.301"><vh>Added easy way of replacing any Leo code</vh></v>
<v t="edream.110203163054.302"><vh>Added convenience routines to redirect stderr and stdout</vh></v>
<v t="edream.110203163054.303"><vh>Added "event1" and "event2" hooks</vh></v>
<v t="edream.110203163054.304"><vh>Added  contributed code to support @read-only nodes</vh></v>
</v>
<v t="edream.110203163054.305"><vh>Known bugs</vh>
<v t="edream.110203163054.306"><vh>Bugs in undoReplace logic</vh></v>
</v>
</v>
<v t="edream.110203163054.307"><vh>leo.py 3.9</vh>
<v t="edream.110203163054.308"><vh>Fixed bugs</vh>
<v t="edream.110203163054.309"><vh>Fixed bug involving @language</vh></v>
<v t="edream.110203163054.310"><vh>Correctly colors Pascal's "private" and "uses" keywords</vh></v>
<v t="edream.110203163054.311"><vh>Fixed a major bug in top()</vh></v>
<v t="edream.110203163054.312"><vh>Fixed bugs when importing Java files.</vh></v>
<v t="edream.110203163054.313"><vh>Convert All Blanks/Tabs  commands honor @tabwidth directives</vh></v>
</v>
<v t="edream.110203163054.314"><vh>New documentation for leo.py 3.9</vh>
<v t="edream.110203163054.315"><vh>Major performance improvements</vh>
<v t="edream.110203163054.316"><vh>Incremental syntax coloring speeds redraws</vh></v>
<v t="edream.110203163054.317"><vh>Incremental undo reduces memory usages significantly</vh></v>
</v>
<v t="edream.110203163054.318"><vh>Major configuration improvements</vh>
<v t="edream.110203163054.319"><vh>Chapter 8: Customizing Leo</vh>
<v t="ekr.20050122084954"><vh>Using leoSettings.leo and @settings trees</vh></v>
<v t="edream.110203163054.320"><vh>Obsolete: Using leoConfig.leo and leoConfig.txt</vh></v>
<v t="edream.110203163054.321"><vh>Using plugins and hooks</vh>
<v t="edream.110203163054.322"><vh>Overview of plugins and hooks</vh></v>
<v t="edream.110203163054.323"><vh>New plugin architecture</vh></v>
<v t="edream.110203163054.172"><vh>About hooks</vh></v>
<v t="edream.110203163054.331"><vh>SECURITY WARNINGS</vh>
<v t="edream.110203163054.332"><vh>The danger of trusting code in shared .leo files</vh></v>
<v t="edream.110203163054.333"><vh>NEVER use this kind of code in a hook!!</vh></v>
<v t="edream.110203163054.334"><vh>Don't use rexec !!</vh>
<v t="edream.110203163054.335"><vh>&lt;&lt; change all instances of rexec to exec in v's body &gt;&gt;</vh></v>
<v t="edream.110203163054.336"><vh>&lt;&lt; delete thisNode &gt;&gt;</vh></v>
<v t="edream.110203163054.337"><vh>&lt;&lt; clear the undo stack &gt;&gt;</vh></v>
</v>
</v>
<v t="edream.110203163054.338"><vh>Convenience routines for plugins</vh>
<v t="edream.110203163054.339"><vh>Convenience functions to enable and disable the "idle" hook</vh></v>
<v t="edream.110203163054.340"><vh>Convenience methods to create, destroy and modify menus</vh>
<v t="edream.110203163054.341"><vh>createMenuItemsFromTable</vh></v>
<v t="edream.110203163054.342"><vh>createNewMenu</vh></v>
<v t="edream.110203163054.343"><vh>createOpenWithMenuFromTable</vh></v>
<v t="edream.110203163054.344"><vh>deleteMenu</vh></v>
<v t="edream.110203163054.345"><vh>deleteMenuItem</vh></v>
<v t="edream.110203163054.346"><vh>Example: how to create a menu</vh></v>
</v>
</v>
<v t="edream.110203163054.347"><vh>Translating menus into other languages</vh></v>
<v t="edream.121403162622"><vh>Support for unit testing</vh></v>
</v>
<v t="edream.110203163054.61"><vh>Putting the Leo icon in Leo windows</vh></v>
<v t="edream.110203163054.348"><vh>Extending the format of .leo files</vh></v>
<v t="edream.120703073611"><vh>Attaching temporary attributes to vnodes and tnodes</vh></v>
<v t="edream.120703073611.1"><vh>Recommended conventions for plugins</vh></v>
<v t="edream.110603190322.6"><vh> Script Find and Script Change</vh>
<v t="edream.111803060152.1"><vh>How it works</vh></v>
<v t="ekr.20040201113232"><vh>Using the initScriptFind script</vh></v>
<v t="edream.111803060152.2"><vh>Ideas for using scripts</vh></v>
</v>
<v t="ekr.20050219093156"><vh>How do I add a new menu item from a plugin?</vh>
<v t="ekr.20050219093156.1"><vh>@url http://www.pythonware.com/library/tkinter/introduction/index.htm</vh></v>
<v t="ekr.20050219093156.2"><vh>@url http://www.tcl.tk/man/tcl8.4/TkCmd/contents.htm</vh></v>
</v>
</v>
<v t="edream.110203163054.349"><vh>More flexible creation of non-existent directories</vh></v>
</v>
<v t="edream.110203163054.350"><vh>New commands &amp; features</vh>
<v t="edream.110203163054.351"><vh>@url</vh></v>
<v t="edream.110203163054.352"><vh>Execute Script command</vh></v>
<v t="edream.110203163054.353"><vh>Go To Line Number command</vh></v>
<v t="edream.110203163054.349"><vh>More flexible creation of non-existent directories</vh></v>
<v t="edream.110203163054.354"><vh>Much better support for cweb</vh>
<v t="edream.110203163054.355"><vh>About cweb mode </vh></v>
</v>
<v t="edream.110203163054.356"><vh>Open With command</vh>
<v t="edream.110203163054.343"><vh>createOpenWithMenuFromTable</vh></v>
</v>
<v t="edream.110203163054.357"><vh>Optional Emacs-style auto-indent</vh></v>
<v t="edream.110203163054.61"><vh>Putting the Leo icon in Leo windows</vh></v>
<v t="edream.110203163054.358"><vh>Reformat Paragraph command</vh></v>
</v>
<v t="edream.110203163054.359"><vh>Appendix 1 to Chapter 4: Using @rawfile, @silentfile and @nosentinlefile trees</vh></v>
</v>
</v>
<v t="edream.110203163054.360"><vh>leo.py 3.8</vh>
<v t="edream.110203163054.361"><vh>Fixed bugs</vh>
<v t="edream.110203163054.362"><vh>Crashers</vh>
<v t="edream.110203163054.363"><vh>Fixed another crasher in scanAllDirectives</vh></v>
</v>
<v t="edream.110203163054.366"><vh>Bugs involving paths &amp; derived files</vh>
<v t="edream.110203163054.368"><vh>Fixed @delims "round trip" bug</vh></v>
<v t="edream.110203163054.369"><vh>Fixed cweb sentinel bug</vh></v>
<v t="edream.110203163054.370"><vh>Fixed import to @root problems</vh></v>
<v t="edream.110203163054.371"><vh>Leo generates @@ sentinels only for real Leo directives</vh></v>
</v>
<v t="edream.110203163054.372"><vh>Minor syntax coloring bugs</vh>
<v t="edream.110203163054.373"><vh>Colorizer now recognizes comments after preprocessor directives</vh></v>
<v t="edream.110203163054.374"><vh>Syntax color perl's alarm function</vh></v>
<v t="edream.110203163054.375"><vh>Fixed block-comment bug in Java and HTML</vh></v>
</v>
<v t="edream.110203163054.376"><vh>Minor user interface bugs</vh>
<v t="edream.110203163054.377"><vh>Worked around Control-T bug</vh></v>
<v t="edream.110203163054.378"><vh>Fixed bug involving menu pastes in headlines</vh></v>
</v>
<v t="edream.110203163054.379"><vh>fixed Unicode bug in setBodyStringOrPane</vh></v>
</v>
<v t="edream.110203163054.380"><vh>New &amp; changed features</vh>
<v t="edream.110203163054.381"><vh>New @rawfile &amp; @silentfile trees</vh>
<v t="edream.110203163054.359"><vh>Appendix 1 to Chapter 4: Using @rawfile, @silentfile and @nosentinlefile trees</vh></v>
</v>
<v t="edream.110203163054.382"><vh>New @raw, @end_raw and @quiet directives</vh>
<v t="edream.110203163054.383"><vh>@raw and @end_raw directives delimit raw text</vh></v>
<v t="edream.110203163054.384"><vh>@verbose, @terse, @quiet and @silent directives control comments in @root trees</vh></v>
</v>
<v t="edream.110203163054.385"><vh>Much better support for CWEB</vh>
<v t="edream.110203163054.355"><vh>About cweb mode </vh></v>
</v>
<v t="edream.110203163054.386"><vh>Allow @comment and @language to coexist</vh></v>
<v t="edream.110203163054.387"><vh>Configuration settings and commands</vh>
<v t="edream.110203163054.388"><vh>Added stylesheet option to support &lt;?xml-stylesheet...?&gt; line</vh></v>
<v t="edream.110203163054.389"><vh>Added Configuration Commands to help menu</vh></v>
<v t="edream.110203163054.390"><vh>Added output_initial_comment option</vh></v>
<v t="edream.110203163054.391"><vh>Added output_newline option</vh></v>
<v t="edream.110203163054.392"><vh>Changed path_directive_creates_directories to create_nonexistent_directories</vh></v>
</v>
<v t="edream.110203163054.393"><vh>Minor changes</vh>
<v t="edream.110203163054.394"><vh>Added support for forth language comments</vh></v>
<v t="edream.110203163054.395"><vh>All export commands now use output_newline option</vh></v>
<v t="edream.110203163054.396"><vh>Changed names of commands in help menu and corresponding entries in leoConfig.leo</vh></v>
<v t="edream.110203163054.397"><vh>Created es_exception</vh></v>
<v t="edream.110203163054.398"><vh>Created reloadAll in leoGlobals.py</vh></v>
<v t="edream.110203163054.399"><vh>Forced focus to body pane after ending headline edit</vh></v>
<v t="edream.110203163054.400"><vh>Use // as single-line comment in Java</vh></v>
<v t="edream.110203163054.401"><vh>wrote "finished" after write @file nodes command</vh></v>
</v>
</v>
<v t="edream.110203163054.402"><vh>Coming soon: Leo 4.0, a major improvement</vh></v>
</v>
<v t="edream.110203163054.403"><vh>leo.py 3.7</vh>
<v t="edream.110203163054.404"><vh>Fixed Bugs</vh>
<v t="edream.110203163054.405"><vh>Language and syntax coloring bugs</vh>
<v t="edream.110203163054.406"><vh>Fixed @comment bug</vh></v>
<v t="edream.110203163054.407"><vh>Fixed colorizing for "while" in C</vh></v>
<v t="edream.110203163054.408"><vh>Fixed @language plain # bug</vh></v>
<v t="edream.110203163054.409"><vh>Fixed @language plain single-quote bug</vh></v>
</v>
<v t="edream.110203163054.410"><vh>Bugs in Edit body commands</vh></v>
<v t="edream.110203163054.411"><vh>Bugs relating to tangling and derived files</vh>
<v t="edream.110203163054.412"><vh>Fixed major bug in @file read code</vh></v>
<v t="edream.110203163054.413"><vh>Fixed minor read bug</vh></v>
<v t="edream.110203163054.406"><vh>Fixed @comment bug</vh></v>
<v t="edream.110203163054.414"><vh>Fixed a bug that affected wrapping in doc parts</vh></v>
</v>
<v t="edream.110203163054.415"><vh>Other bugs</vh>
<v t="edream.110203163054.416"><vh>Fixed reversion in Tangle/Untangle code</vh></v>
<v t="edream.110203163054.417"><vh>Fixed undo cloned headline bug</vh></v>
<v t="edream.110203163054.418"><vh>Fixed Find previous bug</vh></v>
<v t="edream.110203163054.419"><vh>Fixed tab problems</vh></v>
<v t="edream.110203163054.420"><vh>Leo now remembers insert point always</vh></v>
<v t="edream.110203163054.421"><vh>Removed setup.py from binary distribution</vh></v>
</v>
</v>
<v t="edream.110203163054.422"><vh>Improvements</vh>
<v t="edream.110203163054.423"><vh>Many new user options</vh>
<v t="edream.110203163054.424"><vh>General configuration options</vh>
<v t="edream.110203163054.425"><vh>path_directive_creates_directories</vh></v>
<v t="edream.110203163054.426"><vh>relative_path_base_directory</vh></v>
<v t="edream.110203163054.427"><vh>remove_sentinels_extension</vh></v>
<v t="edream.110203163054.428"><vh>write_clone_indices</vh></v>
</v>
<v t="edream.110203163054.429"><vh>Secondary pane ratios</vh></v>
<v t="edream.110203163054.430"><vh>User-configurable colors</vh></v>
<v t="edream.110203163054.431"><vh>User-configurable shortcuts for commands</vh></v>
</v>
<v t="edream.110203163054.432"><vh>Improved support for Unicode</vh></v>
<v t="edream.110203163054.433"><vh>End of cursed newlines</vh></v>
<v t="edream.110203163054.434"><vh>Code is now compatible with Python 2.1</vh></v>
<v t="edream.110203163054.435"><vh>Better file and path handling</vh></v>
<v t="edream.110203163054.436"><vh>Better support for Perl+pod</vh></v>
<v t="edream.110203163054.437"><vh>New End Edit Headline and Abort Edit Headline commands</vh></v>
<v t="edream.110203163054.438"><vh>Allow reads and writes of cloned @file nodes</vh></v>
<v t="edream.110203163054.439"><vh>Leo now closes an empty window when opening a recent file</vh></v>
<v t="edream.110203163054.440"><vh>Improved derived files</vh></v>
<v t="edream.110203163054.441"><vh>Improved enabling of menu items in popup menus</vh></v>
<v t="edream.110203163054.442"><vh>About Leo dialog is now non-modal</vh></v>
</v>
</v>
<v t="edream.110203163054.443"><vh>leo.py 3.6</vh>
<v t="edream.110203163054.444"><vh>Known bug: problems with Python window</vh></v>
<v t="edream.110203163054.445"><vh>Bug fixes</vh>
<v t="edream.110203163054.446"><vh>Fixed problems with opening and writing leoConfig.txt on Linux</vh></v>
<v t="edream.110203163054.447"><vh>Fixed problems renaming files on Linux</vh></v>
<v t="edream.110203163054.448"><vh>Fixed missing headline bug on startup</vh></v>
<v t="edream.110203163054.449"><vh>Improved call to os.path.join in leoApp.finishCreate</vh></v>
<v t="edream.110203163054.450"><vh>Improved how directories are handled in @root trees</vh></v>
<v t="edream.110203163054.451"><vh>Dave Hein: fixed Tk 8.4 problem in Prefs Panel</vh></v>
<v t="edream.110203163054.452"><vh>Dave Hein: added CheckVersion to leoUtils.py</vh></v>
<v t="edream.110203163054.453"><vh>Dave Hein: the Python window now works on Linux.</vh></v>
<v t="edream.110203163054.454"><vh>Steven P. Schaefer: Improved handling of directives in @root trees</vh></v>
<v t="edream.110203163054.455"><vh>Steven P. Schaefer: Fixed cursed newline bug for Linux</vh></v>
</v>
<v t="edream.110203163054.456"><vh>Improvements to existing features</vh>
<v t="edream.110203163054.457"><vh>Leo now remembers scrollbar position and insert point of previously visited nodes</vh></v>
<v t="edream.110203163054.458"><vh>Body pane now gets focus after Go Back/Next</vh></v>
<v t="edream.110203163054.459"><vh>Improved all commands in Help menu</vh></v>
<v t="edream.110203163054.460"><vh>Removed most error messages in atFile::read logic</vh></v>
<v t="edream.110203163054.461"><vh>Added shortcuts for Read/Write @file Nodes commands</vh></v>
<v t="edream.110203163054.462"><vh>Tomaz Ficko: Added support for MouseWheel (Linux only)</vh></v>
</v>
<v t="edream.110203163054.463"><vh>New features</vh>
<v t="edream.110203163054.464"><vh>Added Match Brackets command</vh></v>
<v t="edream.110203163054.465"><vh>Added PHP support</vh></v>
<v t="edream.110203163054.466"><vh>Added LaTex support</vh></v>
</v>
</v>
<v t="edream.110203163054.467"><vh>leo.py 3.5</vh>
<v t="edream.110203163054.468"><vh>Bug fixes</vh>
<v t="edream.110203163054.469"><vh>Called cf.flush in leoConfig.update</vh></v>
<v t="edream.110203163054.470"><vh>Fixed crasher in leoFileCommands.readOutlineOnly</vh></v>
<v t="edream.110203163054.471"><vh>Fixed crasher when leoConfig.txt did not exist</vh></v>
<v t="edream.110203163054.472"><vh>Fixed cursed newline bug in leoAtFile</vh></v>
<v t="edream.110203163054.473"><vh>Rewrote scanAllDirectives routines to handle relative paths</vh></v>
<v t="edream.110203163054.474"><vh>Suppressed erroneous tangle warning about relative paths</vh></v>
</v>
<v t="edream.110203163054.475"><vh>Improvements</vh>
<v t="edream.110203163054.476"><vh>Added configuration settings for horizontal scrollbars</vh></v>
<v t="edream.110203163054.477"><vh>Added commands to the help menu</vh></v>
<v t="edream.110203163054.478"><vh>Added logic to test for read-only files</vh></v>
<v t="edream.110203163054.479"><vh>Added importFiles script</vh></v>
</v>
</v>
<v t="edream.110203163054.480"><vh>leo.py 3.4</vh>
<v t="edream.110203163054.481"><vh>Configuration settings and leoConfig.leo</vh>
<v t="edream.110203163054.482"><vh>Added comments to leoConfig.txt about split direction and ratio</vh></v>
<v t="edream.110203163054.483"><vh>Added save_clears_undo_buffer config option</vh></v>
<v t="edream.110203163054.484"><vh>Corrected spelling of limit_directory_search_extenstion </vh></v>
<v t="edream.110203163054.485"><vh>Created leoConfig.leo</vh></v>
<v t="edream.110203163054.486"><vh>Fixed a major config bug. This fixes font problems</vh></v>
<v t="edream.110203163054.487"><vh>Improved Recent Files menu</vh></v>
<v t="edream.110203163054.488"><vh>Leo honors pane ratio stored in .leo files</vh></v>
<v t="edream.110203163054.489"><vh>Leo writes prefs if leoConfig.txt is read-only</vh></v>
<v t="edream.110203163054.490"><vh>Made leoConfig.txt be read/write by default</vh></v>
<v t="edream.110203163054.491"><vh>Toggle Split Direction now updates leoConfig.txt</vh></v>
</v>
<v t="edream.110203163054.492"><vh>Documentation for code in leo.py that may be of wider interest</vh>
<v t="edream.110203163054.493"><vh>Code hidden in leo.py</vh>
<v t="edream.110203163054.494"><vh>c2py.py</vh></v>
<v t="edream.110203163054.495"><vh>disStats.py</vh></v>
<v t="edream.110203163054.496"><vh>Tkinter utilities</vh></v>
<v t="edream.110203163054.497"><vh>Font dialog</vh></v>
<v t="edream.110203163054.498"><vh>Syntax coloring code</vh></v>
<v t="edream.110203163054.499"><vh>Tree code</vh></v>
</v>
</v>
<v t="edream.110203163054.500"><vh>Fixed bugs</vh>
<v t="edream.110203163054.501"><vh>Fixed another clone bug: created setAncestorsOfClonedNodesInTreeDirty</vh></v>
<v t="edream.110203163054.502"><vh>Fixed bugs that delayed writing of find and prefs panels</vh></v>
<v t="edream.110203163054.503"><vh>Fixed revert problems in font panel</vh></v>
<v t="edream.110203163054.504"><vh>Fixed several unicode bugs</vh></v>
<v t="edream.110203163054.505"><vh>Fixed wandering insertion point bug</vh></v>
</v>
<v t="edream.110203163054.506"><vh>Minor improvements</vh>
<v t="edream.110203163054.507"><vh>Syntax colorer now honors @comment</vh></v>
<v t="edream.110203163054.508"><vh>Added @ignore to "raw" imported files</vh></v>
<v t="edream.110203163054.509"><vh>Added log message for Remove Sentinels command</vh></v>
<v t="edream.110203163054.510"><vh>Improved highlighting of whitespace</vh></v>
<v t="edream.110203163054.511"><vh>Remove Sentinels command now uses .txt extension instead of .tmp</vh></v>
</v>
</v>
<v t="edream.110203163054.512"><vh>leo.py 3.3</vh>
<v t="edream.110203163054.513"><vh>Added support for Unicode</vh></v>
<v t="edream.110203163054.514"><vh>Improved the Import commands &amp; fixed Javadoc problem</vh></v>
<v t="edream.110203163054.515"><vh>Fixed crasher when Tangling</vh></v>
<v t="edream.110203163054.516"><vh>Fixed problems with negative tab widths</vh></v>
<v t="edream.110203163054.517"><vh>Fixed numerous problems related to configuration settings</vh></v>
</v>
<v t="edream.110203163054.518"><vh>leo.py 3.2</vh>
<v t="edream.110203163054.519"><vh>Nested @others directives now valid</vh>
</v>
<v t="edream.110203163054.527"><vh>Improved Import command</vh></v>
<v t="edream.110203163054.528"><vh>Reassigned shortcuts in the Outline-Move/Select menu</vh></v>
<v t="edream.110203163054.529"><vh>Fixed crasher in the Preferences Panel</vh></v>
<v t="edream.110203163054.530"><vh>Improved syntax coloring of continued C strings</vh></v>
<v t="edream.110203163054.531"><vh>Made many changes to Color Panel</vh></v>
<v t="edream.110203163054.532"><vh>Added email address &amp; URL to About Leo dialog</vh></v>
<v t="edream.110203163054.533"><vh>added disStats.py</vh></v>
</v>
<v t="edream.110203163054.534"><vh>leo.py 3.1</vh>
<v t="edream.110203163054.535"><vh>Added compare panel</vh></v>
<v t="edream.110203163054.536"><vh>Added new settings to leoConfig.txt</vh></v>
<v t="edream.110203163054.537"><vh>Changed precedence scheme for preferences</vh></v>
<v t="edream.110203163054.538"><vh>Fixed @tabwidth, @pagewidth and @language directives</vh></v>
<v t="edream.110203163054.539"><vh>Flatten Outline now escapes only the first non-blank character of each line.</vh></v>
<v t="edream.110203163054.540"><vh>Open Python Window command adds path to IDLE automatically</vh></v>
<v t="edream.110203163054.541"><vh>Python 2.2 required dialog tells where to download Python 2.2 and Tk 8.3</vh></v>
</v>
<v t="edream.110203163054.542"><vh>leo.py 3.0</vh>
<v t="edream.110203163054.543"><vh>Optional new file format</vh></v>
<v t="edream.110203163054.544"><vh>New features (in approximate order of importance)</vh>
<v t="edream.110203163054.545"><vh>Added many settings to leoConfig.txt file</vh>
<v t="edream.110203163054.546"><vh>New windows now open using config params.</vh></v>
</v>
<v t="edream.110203163054.547"><vh>Added autoscrolling in the outline pane</vh></v>
<v t="edream.110203163054.548"><vh>Color panel</vh></v>
<v t="edream.110203163054.549"><vh>Font panel</vh></v>
<v t="edream.110203163054.550"><vh>Leo now opens windows at the position in which they were saved</vh></v>
<v t="edream.110203163054.551"><vh>Added Toggle Split Direction</vh></v>
<v t="edream.110203163054.552"><vh>Improved syntax coloring for @comment directives</vh></v>
<v t="edream.110203163054.553"><vh>Leo warns and aborts if not Python 2.2 or above</vh></v>
<v t="edream.110203163054.554"><vh>All panels now have labeled frames and grooved borders</vh></v>
<v t="edream.110203163054.555"><vh>Leo directives are now colored green by default</vh></v>
<v t="edream.110203163054.556"><vh>Print a traceback message for all serious exceptions</vh></v>
<v t="edream.110203163054.557"><vh>@comment supports comments starting with REM</vh></v>
</v>
<v t="edream.110203163054.558"><vh>Fixed bugs (one crasher)</vh>
<v t="edream.110203163054.559"><vh>Fixed crasher in atFile.scanAllDirectives</vh></v>
<v t="edream.110203163054.560"><vh>Fixed syntax coloring bug involving Leo directives</vh></v>
<v t="edream.110203163054.561"><vh>Windows now open without visual problems</vh></v>
<v t="edream.110203163054.562"><vh>Made Convert Tabs, Convert All Blanks and Convert All Tabs undoable</vh></v>
<v t="edream.110203163054.563"><vh>Made Prefs panel non-modal</vh></v>
</v>
</v>
</v>
<v t="edream.110203163054.564"><vh>2.x...</vh>
<v t="edream.110203163054.565"><vh>leo.py 2.5.1 Many improvements</vh>
<v t="edream.110203163054.566"><vh>New &amp; improved commands</vh>
<v t="edream.110203163054.567"><vh>Tabs and spaces</vh>
<v t="edream.110203163054.568"><vh>Added Convert All Blanks and Convert All Tabs commands</vh></v>
<v t="edream.110203163054.569"><vh>Added Convert Tabs command</vh></v>
<v t="edream.110203163054.570"><vh>Tab widths work</vh></v>
<v t="edream.110203163054.571"><vh>Negative tab width converts tabs to spaces</vh></v>
</v>
<v t="edream.110203163054.572"><vh>Improved Preferences panel</vh></v>
<v t="edream.110203163054.320"><vh>Obsolete: Using leoConfig.leo and leoConfig.txt</vh></v>
<v t="edream.110203163054.573"><vh>Cut and Paste now works properly in all situations</vh></v>
<v t="edream.110203163054.574"><vh>Added Recent Files menu</vh></v>
<v t="edream.110203163054.575"><vh>All Extract and Import commands are now undoable</vh></v>
<v t="edream.110203163054.576"><vh>Made Cascade and Minimize All commands functional</vh></v>
</v>
<v t="edream.110203163054.577"><vh>Significant bug fixes</vh>
<v t="edream.110203163054.578"><vh>Fixed several bugs in the Import commands</vh></v>
<v t="edream.110203163054.579"><vh>Invalid directories no longer cause read errors</vh></v>
</v>
<v t="edream.110203163054.580"><vh>Fixed crashers</vh>
<v t="edream.110203163054.581"><vh>Fixed crasher when saving a new file</vh></v>
<v t="edream.110203163054.582"><vh>Fixed crashers in Remove Sentinels command</vh></v>
<v t="edream.110203163054.583"><vh>Fixed crasher in Import commands</vh></v>
</v>
<v t="edream.110203163054.584"><vh>Fixed minor bugs &amp; improvements</vh>
<v t="edream.110203163054.585"><vh>Recolored body text after extract commands</vh></v>
<v t="edream.110203163054.586"><vh>Fixed bug involving missing clone mark after Move Right command</vh></v>
<v t="edream.110203163054.587"><vh>Changed defaultextension from "x" to ".x" in dialogs.</vh></v>
<v t="edream.110203163054.588"><vh>Fixed minor bug in Save and Save As commands</vh></v>
<v t="edream.110203163054.589"><vh>Fixed minor problems with documentation</vh></v>
<v t="edream.110203163054.590"><vh>Renamed Font to Set Font... and Syntax Coloring... to Set Colors...</vh></v>
</v>
</v>
<v t="edream.110203163054.591"><vh>leo.py 2.4</vh>
<v t="edream.110203163054.592"><vh>Fixed several bugs</vh></v>
<v t="edream.110203163054.593"><vh>Added better error recovery when writing .leo files</vh></v>
<v t="edream.110203163054.594"><vh>Dragging headlines</vh></v>
<v t="edream.110203163054.60"><vh>How to associate Leo with .leo files on Windows</vh></v>
</v>
<v t="edream.110203163054.595"><vh>leo.py 2.3</vh></v>
<v t="edream.110203163054.596"><vh>leo.py 2.2 Bug fixes and documentation revised</vh></v>
<v t="edream.110203163054.597"><vh>2.1 Import &amp; Export commands</vh>
<v t="edream.110203163054.598"><vh>Import and Export commands</vh></v>
<v t="edream.110203163054.599"><vh>Fixed moves up to root position</vh></v>
<v t="edream.110203163054.600"><vh>Improved the syntax colorer</vh></v>
</v>
<v t="edream.110203163054.601"><vh>2.0 Untangle, Unlimited Undo/Redo, Syntax Coloring, etc.</vh>
<v t="edream.110203163054.602"><vh>Format change: no blank lines between sentinels in derived files</vh></v>
<v t="edream.110203163054.603"><vh>Unlimited Undo and Redo</vh></v>
<v t="edream.110203163054.604"><vh>Drawing and syntax coloring</vh>
<v t="edream.110203163054.605"><vh>Syntax coloring works for all languages</vh></v>
<v t="edream.110203163054.606"><vh>Fixed minor syntax coloring bugs</vh></v>
<v t="edream.110203163054.607"><vh>Headlines given more space</vh></v>
<v t="edream.110203163054.608"><vh>Suppressed auto-indent for Python in @nocolor mode</vh></v>
</v>
<v t="edream.110203163054.609"><vh>Tangle/Untangle</vh>
<v t="edream.110203163054.610"><vh>Fixed old bugs in Untangle</vh></v>
<v t="edream.110203163054.611"><vh>@c now is the same as @code</vh></v>
<v t="edream.110203163054.612"><vh>Untangle only trims trailing lines from updated nodes</vh></v>
</v>
<v t="edream.110203163054.613"><vh>Fixed Linux-specific bugs</vh></v>
</v>
<v t="edream.110203163054.614"><vh>1.0 New commands and bug fixes</vh>
<v t="edream.110203163054.615"><vh>Unfinished commands</vh></v>
<v t="edream.110203163054.616"><vh>How to copy an outline from Borland Leo to Leo.py</vh></v>
<v t="edream.110203163054.617"><vh>Fixed bugs</vh></v>
<v t="edream.110203163054.618"><vh>Remaining minor problems</vh></v>
</v>
<v t="edream.110203163054.619"><vh>0.08 Find, Change and Tangle commands &amp; major bugs fixed</vh>
<v t="edream.110203163054.620"><vh>About the Find and Change commands</vh></v>
<v t="edream.110203163054.621"><vh>About the Tangle command</vh></v>
<v t="edream.110203163054.622"><vh>About hyperlinking</vh></v>
<v t="edream.110203163054.623"><vh>Fixed significant bugs</vh></v>
<v t="edream.110203163054.624"><vh>Other improvements</vh></v>
<v t="edream.110203163054.625"><vh>Improved memory management</vh></v>
<v t="edream.110203163054.626"><vh>The trace function (Sherlock tracing)</vh></v>
<v t="edream.110203163054.627"><vh>Improved directory and file name handling</vh></v>
<v t="edream.110203163054.628"><vh>Improvements that will be propagated back to LeoCB</vh></v>
</v>
<v t="edream.110203163054.629"><vh>0.07 Stability and scripting</vh>
<v t="edream.110203163054.630"><vh>Thorough testing</vh></v>
<v t="edream.110203163054.631"><vh>Removed many irritations.  Some remain</vh></v>
<v t="edream.110203163054.632"><vh>Fixed bug that can drop data</vh></v>
<v t="edream.110203163054.633"><vh>Added Python window and scripting support</vh></v>
<v t="edream.110203163054.634"><vh>Added Script to convert from Leo 1 to Leo 2</vh></v>
<v t="edream.110203163054.635"><vh>Added Leo Documentation command</vh></v>
<v t="edream.110203163054.636"><vh>Added Auto indent</vh></v>
</v>
<v t="edream.110203163054.637"><vh>0.06 Minor changes for Linux</vh></v>
<v t="edream.110203163054.638"><vh>0.05 The first functional version</vh>
<v t="edream.110203163054.639"><vh>Testing &amp; Performance</vh></v>
<v t="edream.110203163054.640"><vh>Installing and Running leo.py</vh></v>
<v t="edream.110203163054.641"><vh>Files &amp; Folders</vh></v>
<v t="edream.110203163054.642"><vh>Functional Commands and Features</vh></v>
<v t="edream.110203163054.643"><vh>Non-Functional Commands and Features</vh></v>
<v t="edream.110203163054.644"><vh>Bugs, Problems and Code Quality</vh></v>
<v t="edream.110203163054.645"><vh>New Things To Do</vh></v>
</v>
</v>
<v t="edream.110203163054.646"><vh>Borland PC versions...</vh>
<v t="edream.110203163054.647"><vh>Borland 2.7 Major bug fix: please upgrade</vh></v>
<v t="edream.110203163054.648"><vh>Borland 2.6 Major changes: please upgrade</vh>
<v t="edream.110203163054.649"><vh>Format change: no blank lines between sentinels in derived files</vh></v>
<v t="edream.110203163054.650"><vh>Eliminated spurious read errors</vh></v>
<v t="edream.110203163054.651"><vh>@c now is the same as @code</vh></v>
<v t="edream.110203163054.652"><vh>Fixed old bugs in Untangle</vh></v>
<v t="edream.110203163054.653"><vh>Compatibility with leo.py v2.0</vh></v>
<v t="edream.110203163054.654"><vh>Changed "Batch" check box to "Show Context"</vh></v>
<v t="edream.110203163054.655"><vh>Can not ensure .leo extension</vh></v>
</v>
<v t="edream.110203163054.656"><vh>version 2.5: Fixed several serious bugs</vh></v>
<v t="edream.110203163054.657"><vh>version 2.4: The new Leo2 (Do not use this version)</vh>
<v t="edream.110203163054.658"><vh>Fixed clone bugs</vh></v>
<v t="edream.110203163054.659"><vh>.leo files now contain all data</vh></v>
<v t="edream.110203163054.660"><vh>Replaced archive command</vh></v>
<v t="edream.110203163054.661"><vh>Automatic update of @file trees</vh></v>
<v t="edream.110203163054.662"><vh>Errors while reading</vh></v>
<v t="edream.110203163054.663"><vh>Errors while writing</vh></v>
<v t="edream.110203163054.664"><vh>Drawbacks of @file trees</vh></v>
</v>
<v t="edream.110203163054.665"><vh>version 2.3: Do not use this version</vh>
<v t="edream.110203163054.666"><vh>@first directive</vh></v>
<v t="edream.110203163054.667"><vh>Archive Entire Outline command</vh></v>
<v t="edream.110203163054.668"><vh>Fixed @c syntax coloring</vh></v>
<v t="edream.110203163054.669"><vh>Fixed bugs in the find command</vh></v>
<v t="edream.110203163054.670"><vh>Fixed bug involving @file dirty bits</vh></v>
<v t="edream.110203163054.671"><vh>The Log window is now part of the Leo window</vh></v>
</v>
<v t="edream.110203163054.672"><vh>version 2.2 (beta)</vh></v>
<v t="edream.110203163054.673"><vh>version 2.1 (beta)</vh></v>
<v t="edream.110203163054.674"><vh>1.x versions</vh>
<v t="edream.110203163054.675"><vh>Changes made in version 1.15</vh></v>
<v t="edream.110203163054.676"><vh>Changes made in version 1.14</vh></v>
<v t="edream.110203163054.677"><vh>Changes made in version 1.13</vh></v>
<v t="edream.110203163054.678"><vh>Changes made in version 1.12</vh></v>
<v t="edream.110203163054.679"><vh>Changes made in version 1.11</vh>
<v t="edream.110203163054.680"><vh>Multiple parts not allowed for &lt;&lt; section name &gt;&gt;</vh></v>
<v t="edream.110203163054.681"><vh>Untangling: updating an outline</vh></v>
</v>
<v t="edream.110203163054.682"><vh>Changes made in version 1.10</vh></v>
<v t="edream.110203163054.683"><vh>Changes made in version 1.9</vh>
<v t="edream.110203163054.684"><vh>New Execute Script command</vh></v>
<v t="edream.110203163054.685"><vh>Python window improved</vh></v>
</v>
<v t="edream.110203163054.686"><vh>Changes made in version 1.8</vh></v>
<v t="edream.110203163054.687"><vh>Changes made in version 1.7</vh></v>
<v t="edream.110203163054.688"><vh>Changes made in version 1.6</vh></v>
<v t="edream.110203163054.689"><vh>Changes made in version 1.5</vh></v>
<v t="edream.110203163054.690"><vh>Changes made in version 1.4</vh>
<v t="edream.110203163054.691"><vh>Outline To Noweb command</vh></v>
<v t="edream.110203163054.692"><vh>find/change Python scripts</vh></v>
<v t="edream.110203163054.693"><vh>v.commands() Python method</vh></v>
</v>
<v t="edream.110203163054.694"><vh>Changes made in version 1.3</vh></v>
<v t="edream.110203163054.695"><vh>Changes made in version 1.2</vh></v>
<v t="edream.110203163054.696"><vh>Changes made in version 1.1</vh></v>
<v t="edream.110203163054.697"><vh>Changes made in version 1.0</vh></v>
<v t="edream.110203163054.698"><vh>Changes made in version 0.19</vh>
<v t="edream.110203163054.699"><vh>Fixed directory bug</vh></v>
<v t="edream.110203163054.700"><vh>Added @language HTML, perl and perlpod</vh></v>
<v t="edream.110203163054.701"><vh>Eliminated @noweb &amp; replaced @cweb with @language cweb</vh></v>
<v t="edream.110203163054.355"><vh>About cweb mode </vh></v>
<v t="edream.110203163054.702"><vh>Improved syntax coloring</vh></v>
<v t="edream.110203163054.703"><vh>Improved Print command</vh></v>
<v t="edream.110203163054.704"><vh>Improved how Untangle handles block comments</vh></v>
<v t="edream.110203163054.705"><vh>Eliminated clone windows (but not clone nodes!)</vh></v>
<v t="edream.110203163054.706"><vh>Eliminated Extended noweb Syntax</vh></v>
</v>
<v t="edream.110203163054.707"><vh>Changes made in version 0.18</vh>
<v t="edream.110203163054.708"><vh>File format extended</vh></v>
<v t="edream.110203163054.709"><vh>Fixed bug in languages without block comments</vh></v>
<v t="edream.110203163054.710"><vh>Added @header and @noheader directives</vh></v>
<v t="edream.110203163054.711"><vh>Added @language fortran90</vh></v>
<v t="edream.110203163054.712"><vh>Added @language perlpod</vh></v>
</v>
<v t="edream.110203163054.713"><vh>Changes made in version 0.17</vh>
<v t="edream.110203163054.714"><vh>Support for noweb &lt;&lt;*&gt;&gt; convention</vh></v>
<v t="edream.110203163054.715"><vh>new @cweb, @noweb, @path, @tabwidth and @pagewidth directives</vh></v>
<v t="edream.110203163054.716"><vh>CWEB mode now has a chance of working</vh></v>
<v t="edream.110203163054.717"><vh>Reduced default screen size</vh></v>
</v>
<v t="edream.110203163054.718"><vh>Changes made in version 0.16</vh>
<v t="edream.110203163054.719"><vh>Bug fixes</vh></v>
<v t="edream.110203163054.720"><vh>Fixed crasher involving switching windows</vh></v>
<v t="edream.110203163054.721"><vh>new @language directive</vh></v>
<v t="edream.110203163054.722"><vh>@language and @comment directives can be inherited</vh></v>
<v t="edream.110203163054.723"><vh>Untangle can now handle non-C files</vh></v>
<v t="edream.110203163054.724"><vh>Untangle now removes trailing blank lines</vh></v>
<v t="edream.110203163054.725"><vh>new @verbose, @terse and @silent directives</vh></v>
<v t="edream.110203163054.726"><vh>Default directories</vh></v>
<v t="edream.110203163054.727"><vh>Import Files command now handles Pascal , Python and Java files.</vh></v>
<v t="edream.110203163054.728"><vh>Toggle Active Pane command</vh></v>
<v t="edream.110203163054.729"><vh>Path delimiters are now '\' instead of '/'</vh></v>
<v t="edream.110203163054.730"><vh>Cleaned up code</vh></v>
<v t="edream.110203163054.731"><vh>Fixed crasher involving empty section names</vh></v>
<v t="edream.110203163054.732"><vh>Untangle warns about sections not in the outline</vh></v>
<v t="edream.110203163054.733"><vh>A limitations involving Untangle</vh></v>
</v>
<v t="edream.110203163054.734"><vh>Known Bugs &amp; Limitations</vh></v>
</v>
</v>
</v>
<v t="ekr.20050210102358"><vh>4.0... New read logic eliminates read errors, eliminated child indices</vh>
<v t="edream.110203163054.66"><vh>4.0.1 through 4.0.4</vh></v>
<v t="edream.110203163054.67"><vh>4.0 final</vh>
<v t="edream.110203163054.68"><vh>4.0 beta 4</vh></v>
<v t="edream.110203163054.69"><vh>4.0 beta 3</vh>
<v t="edream.110203163054.70"><vh>Fixed bugs</vh>
<v t="edream.110203163054.71"><vh>Fixed bug that caused some clones not to be marked as clones</vh></v>
<v t="edream.110203163054.72"><vh>Corrected problems with setting icons on Linux</vh></v>
<v t="edream.110203163054.73"><vh>Fixed crasher in sentinelName</vh></v>
<v t="edream.110203163054.74"><vh>Reenabled orphans &amp; ignored test in new write logic</vh></v>
</v>
<v t="edream.110203163054.75"><vh>New features</vh>
<v t="edream.110203163054.76"><vh>Added support for unknown tnode and vnode attributes</vh></v>
<v t="edream.110203163054.77"><vh>Added build number to signon</vh></v>
<v t="edream.110203163054.78"><vh>Added better error message in setDefaultIcon</vh></v>
</v>
</v>
<v t="edream.110203163054.79"><vh>4.0 beta 2</vh>
<v t="edream.110203163054.80"><vh>To-do for 4.0 final</vh></v>
<v t="edream.110203163054.81"><vh>Fixed Bugs</vh>
<v t="edream.110203163054.82"><vh>Added crucial defensive checks in v.headString() and v.bodySting()</vh></v>
<v t="edream.110203163054.83"><vh>Ensured newlines before all sentinels in @rawfile</vh></v>
<v t="edream.110203163054.84"><vh>Fixed bugs involving find params</vh></v>
<v t="edream.110203163054.85"><vh>Fixed Python Import bug</vh></v>
<v t="edream.110203163054.86"><vh>Fixed several more unicode bugs</vh></v>
<v t="edream.110203163054.87"><vh>Fixed crasher in Go To Outline command.</vh></v>
<v t="edream.110203163054.88"><vh>Fixed @rawfile write problem</vh></v>
</v>
<v t="edream.110203163054.89"><vh>Improved commands</vh>
<v t="edream.110203163054.90"><vh>Finished Import Derived File command and made it undoable</vh></v>
<v t="edream.110203163054.91"><vh>Moved Clear Recent Files menu item into Recent Files menu</vh></v>
<v t="edream.110203163054.92"><vh>Added better log message for Convert All Tabs/Blanks commands</vh></v>
<v t="edream.110203163054.93"><vh>Marked changed nodes &amp; make the @file node and the outline dirty.</vh></v>
<v t="edream.110203163054.94"><vh>Rewrote icon code so it doesn't use PIL or tkIcon in Python 2.3</vh></v>
<v t="edream.110203163054.95"><vh>Created leoGui base class for tkinterGui class</vh></v>
</v>
<v t="edream.110203163054.96"><vh>New and improved settings</vh>
<v t="edream.110203163054.97"><vh>Added support for two new settings affecting drags</vh></v>
<v t="edream.110203163054.98"><vh>changed default for config.write_old_format_derived_files</vh></v>
</v>
</v>
<v t="edream.110203163054.99"><vh>4.0 beta 1</vh>
<v t="edream.110203163054.100"><vh>4.0 Theory of operation</vh></v>
<v t="edream.110203163054.101"><vh>New commands &amp; options</vh>
<v t="edream.110203163054.102"><vh>New write_old_format_derived_files option</vh></v>
<v t="edream.110203163054.103"><vh>New Clear Recent Files command</vh></v>
<v t="edream.110203163054.104"><vh>New Import Derived File command</vh></v>
<v t="edream.110203163054.105"><vh>New Write 3.x/4.x Derived Files &amp; autosave</vh></v>
</v>
<v t="edream.110203163054.106"><vh>New plugins</vh></v>
<v t="edream.110203163054.107"><vh>New read logic and greatly inproved error recovery</vh>
<v t="edream.110203163054.108"><vh>Added test for unvisited nodes in read logic</vh></v>
<v t="edream.110203163054.109"><vh>Error recovery is _much_ better than before</vh></v>
</v>
<v t="edream.110203163054.110"><vh>Improvements &amp; bug fixes</vh>
<v t="edream.110203163054.111"><vh>Added horizontal scrollbar in body pane when @nowrap in effect</vh></v>
<v t="edream.110203163054.112"><vh>Added support for Python 2.3</vh></v>
<v t="edream.110203163054.113"><vh>Leo recycles window objects only if more than one window open</vh></v>
<v t="edream.110203163054.114"><vh>Removed "not undoable" message from Read @file Nodes command</vh></v>
<v t="edream.110203163054.115"><vh>Removed Open Python Window command</vh></v>
<v t="edream.110203163054.116"><vh>Simplified read and write code</vh></v>
</v>
</v>
</v>
</v>
<v t="ekr.20050210102150.1"><vh>4.1... gnx's</vh>
<v t="ekr.20040216151748"><vh>4.1 final</vh>
<v t="ekr.20040217085036"><vh>Added several new plugins</vh></v>
<v t="ekr.20040216152948"><vh>Added Toggle Angle Brackets command</vh></v>
<v t="ekr.20040216153725"><vh>Changed Undo/Redo messages</vh></v>
<v t="ekr.20040217075627"><vh>Fixed clone bug when pasting nodes</vh></v>
<v t="ekr.20040217085036.1"><vh>Investigated encoding problem: it's a Python 2.3 bug</vh></v>
</v>
<v t="ekr.20040131040356"><vh>4.1 rc4</vh>
<v t="ekr.20040201114855"><vh>New plugins in 4.1 rc4</vh>
<v t="ekr.20040201114855.42"><vh>mod_http.py plugin: Bernhard Mulder</vh></v>
<v t="ekr.20040201114855.91"><vh>newButtons.py plugin: Paul Paterson</vh></v>
<v t="ekr.20040201114855.29"><vh>nodenavigator.py plugin: Paul Paterson</vh></v>
<v t="ekr.20040201114855.36"><vh>rowcol.py: EKR</vh></v>
<v t="ekr.20040201114855.13"><vh>searchbox.py plugin: Paul Paterson</vh></v>
<v t="ekr.20040201120903"><vh>status_line.py plugin: EKR</vh></v>
</v>
<v t="ekr.20040131041015"><vh>New features in 4.1 rc4</vh>
<v t="ekr.20040131040544.10"><vh>Leo no longer automatically draws the status area</vh></v>
<v t="ekr.20040131040544.21"><vh>Esc and enter key now work in the find panel</vh></v>
<v t="ekr.20040131040544.55"><vh>Improved message for orphan nodes</vh></v>
<v t="ekr.20040131040544.178"><vh>Eliminated marking nodes dirty unnecessarily</vh></v>
<v t="ekr.20040131040544.222"><vh>Execute Script command now ends all nodes with a newline</vh></v>
<v t="ekr.20040131040544.2"><vh>Added message when plugins are disabled</vh></v>
<v t="ekr.20040201061329"><vh>Created status_line.py plugin</vh></v>
<v t="ekr.20040201114855.105"><vh>Simplified operation of script-find/change &amp; improved documentation</vh>
<v t="edream.110603190322.6"><vh> Script Find and Script Change</vh>
<v t="edream.111803060152.1"><vh>How it works</vh></v>
<v t="ekr.20040201113232"><vh>Using the initScriptFind script</vh></v>
<v t="edream.111803060152.2"><vh>Ideas for using scripts</vh></v>
</v>
</v>
<v t="ekr.20040201114855.106"><vh>Added done message to Mark Changed commands</vh></v>
</v>
<v t="ekr.20040131040356.1"><vh>Bugs fixed in 4.1 rc4</vh>
<v t="ekr.20040131044727"><vh>Fixed several bugs when writing derived files</vh></v>
<v t="ekr.20040131040754"><vh>Fixed several crashers</vh></v>
<v t="ekr.20040131040544.5"><vh>Fixed "bad leo file" when reading some 3.x .leo files</vh></v>
<v t="ekr.20040131040544.18"><vh>Fixed huge performance bug in cut/copy node commands</vh></v>
<v t="ekr.20040131040544.32"><vh>Leo now properly re-enables drawing after exceptions</vh></v>
<v t="ekr.20040201114855.107"><vh>Fixed major bug in tkFind.init</vh></v>
<v t="ekr.20040131040544.73"><vh>Fixed bug in Move Up command</vh></v>
<v t="ekr.20040131040544.81"><vh>Fixed bug in Import Derived File</vh></v>
<v t="ekr.20040131040544.146"><vh>Fixed bugs related to saving read-only files</vh></v>
<v t="ekr.20040131040544.169"><vh>Fixed bug in Import Python Window command when using Python 2.2</vh></v>
<v t="ekr.20040131040544.228"><vh>Fixed bugs in Convert All BlanksTabs commands</vh></v>
<v t="ekr.20040131040544.258"><vh>Fixed crashes in open_shell.py plugin</vh></v>
<v t="ekr.20040131044136"><vh>Fixed several bugs involving cut &amp; paste</vh></v>
<v t="ekr.20040131040544.227"><vh>Fixed whitespace problem in leoTkinterGui.py</vh></v>
<v t="ekr.20040131100557"><vh>Fixed glitches when inserting node in hoisted outline</vh></v>
<v t="ekr.20040203084228"><vh>Fixed bugs in search command</vh></v>
</v>
<v t="ekr.20040131040356.2"><vh>Bug fixed in previous 4.1 releases</vh></v>
<v t="ekr.20040131040356.3"><vh>New code-level features</vh></v>
<v t="ekr.20040131040356.4"><vh>New configuration settings</vh></v>
<v t="ekr.20040131040356.5"><vh>New features</vh></v>
</v>
<v t="edream.121403160546"><vh>4.1 rc3</vh>
<v t="edream.121403165221"><vh>Bugs fixed in this release</vh></v>
<v t="edream.121403161017"><vh>Bug fixed in previous 4.1 releases</vh></v>
<v t="edream.121403161017.1"><vh>New code-level features</vh></v>
<v t="edream.121403161017.2"><vh>New configuration settings</vh></v>
<v t="edream.121403161340"><vh>New features</vh></v>
</v>
<v t="edream.110603185805"><vh>4.1 beta 5</vh>
<v t="edream.120403174147"><vh>Changes made in 4.1 beta 5</vh>
<v t="edream.120403180443"><vh>New and improved features</vh>
<v t="edream.120403174147.105"><vh>Honor outline/body pane ratio when opening files</vh></v>
<v t="edream.120403174147.112"><vh>Leo now adjusts newly opened windows so they fit on the screen</vh></v>
<v t="edream.120403174147.119"><vh>Tested support for Unicode file &amp; directory names</vh></v>
<v t="edream.120403174147.128"><vh>Added code so @url nodes may open .leo files</vh></v>
<v t="edream.120403174147.56"><vh>Fixed problems with @lineending platform</vh></v>
</v>
<v t="edream.120403174241"><vh>Bugs fixed</vh>
<v t="edream.120403174147.30"><vh>Fixed crasher in Apply Settings command</vh></v>
<v t="edream.120403174147.102"><vh>Fixed crasher in Toggle Angle Brackets command</vh></v>
<v t="edream.120403174147.109"><vh>Fixed crasher when setting Icon in Linux)</vh></v>
<v t="edream.120403174147.33"><vh>Fixed Find panel bug on the Mac</vh></v>
<v t="edream.120403174147.36"><vh>Fixed Import backslash-newline bug</vh></v>
<v t="edream.120403174147.61"><vh>Fixed Linux import problem</vh></v>
<v t="edream.120403174147.63"><vh>Fixed Recent files crasher</vh></v>
<v t="edream.120403174147.65"><vh>Fixed Replace Blanks command</vh></v>
<v t="edream.110603190322.8"><vh>Fixed Serious Undo Change All bugs</vh></v>
<v t="edream.120403174147.94"><vh>Fixed several long-standing bugs related to Extract commands</vh></v>
</v>
</v>
<v t="edream.120403180443.1"><vh>Changes made in earlier 4.1 betas</vh>
<v t="edream.110603190234.1"><vh>Code-level features</vh>
<v t="edream.110603190125.3"><vh>Regression tests started</vh></v>
<v t="edream.110603190125.4"><vh>Code reorganized to support other guis</vh></v>
<v t="edream.110303182253.39"><vh>Made app.forceShutdown work in "idle" hook</vh></v>
</v>
<v t="edream.110603190404"><vh>Fixed bugs</vh>
<v t="edream.110603190322.13"><vh>Fixed bug involving 0x1a characters in body text.</vh></v>
<v t="edream.110603190322.11"><vh>Fixed first node-only find bug</vh></v>
<v t="edream.110603190322.3"><vh>Fixed bug in idle_body_key</vh></v>
<v t="edream.111803060643"><vh>Fixed LaTeX syntax coloring bug</vh></v>
</v>
<v t="edream.110603192009"><vh>Improved format of .leo files</vh>
<v t="edream.110603190322.9"><vh>Leo now ignores unknown prefs and find prefs</vh></v>
<v t="edream.110603190322.10"><vh>Leo now writes node_only find prefs</vh></v>
<v t="edream.110603190125.1"><vh>.leo files are now cvs-friendly</vh></v>
</v>
<v t="edream.110603192009.1"><vh>New &amp; improved commands</vh>
<v t="edream.112303173638"><vh>Running Leo in batch mode</vh></v>
<v t="edream.110203163054.833"><vh>Executing Python scripts in body text</vh></v>
<v t="edream.110603190322.14"><vh>Added Check Outline command</vh></v>
<v t="edream.110603190322.15"><vh>Added Hoist/De-Hoist commands</vh></v>
<v t="edream.111803060152"><vh>Added script-based find/change commands</vh>
<v t="edream.110603190322.6"><vh> Script Find and Script Change</vh>
<v t="edream.111803060152.1"><vh>How it works</vh></v>
<v t="ekr.20040201113232"><vh>Using the initScriptFind script</vh></v>
<v t="edream.111803060152.2"><vh>Ideas for using scripts</vh></v>
</v>
</v>
<v t="edream.110303182253.3"><vh>Leo now does an auto-save only if files have actually been changed.</vh></v>
<v t="edream.111803062437"><vh>Shift commands now shift single line if no selection</vh></v>
</v>
<v t="edream.110303182719"><vh>New config settings</vh></v>
</v>
</v>
<v t="edream.110203163054.64"><vh>4.1 alpha 1</vh></v>
</v>
<v t="ekr.20050210102150"><vh>4.2... @file-thin, shared tnodes</vh>
<v t="ekr.20040922074200"><vh>4.2 final</vh></v>
<v t="ekr.20040914103359"><vh>4.2 rc1</vh>
<v t="ekr.20040914103743.1"><vh>Added new features</vh>
<v t="ekr.20040914103359.137"><vh>Added c.frame.openDirectory to sys.path when executing scripts</vh></v>
<v t="ekr.20040914103359.37"><vh>Added expanded_click_area option to disable left click logic in outline pane</vh></v>
<v t="ekr.20040914103359.2"><vh>Restored the "iconclick1/2" hooks</vh></v>
<v t="ekr.20040914103359.19"><vh>(Allow longer headlines for to support long url's)</vh>
<v t="ekr.20040914103359.20"><vh>Report</vh></v>
</v>
</v>
<v t="ekr.20040914103743"><vh>Fixed bugs</vh>
<v t="ekr.20040914103359.47"><vh>Disabled perfect import</vh></v>
<v t="ekr.20040914103359.127"><vh>Fixed bugs in Tangle/Untangle</vh></v>
<v t="ekr.20040914103359.12"><vh>Fixed Import Derived Files command</vh></v>
<v t="ekr.20040914103359.15"><vh>Fixed parsing of minimal &lt;preferences&gt; tag</vh></v>
<v t="ekr.20040914103359.7"><vh>Fixed problem with tabs on MacOs</vh></v>
<v t="ekr.20040914103359.28"><vh>Fixed read errors with @language html</vh></v>
<v t="ekr.20040914103359.4"><vh>Made sure a proper message is given with invalid versions of Python</vh></v>
<v t="ekr.20040914103359.110"><vh>Removed failed assert from colorizer</vh></v>
<v t="ekr.20040914103359.31"><vh>Removed spurious "Warning: updating changed text" messages</vh></v>
<v t="ekr.20040914103359.129"><vh>Shifted all Alt-shortcuts to Ctrl shortcuts on the Mac</vh></v>
</v>
</v>
<v t="ekr.20040713110718"><vh>4.2 beta 3</vh>
<v t="ekr.20040804165258.1"><vh>Bug fixes</vh>
<v t="ekr.20040804164600.16"><vh>Leo gives the user a chance to save read-only files</vh></v>
<v t="ekr.20040804164600.36"><vh>Fixed some unit-test bugs</vh></v>
<v t="ekr.20040804164600.56"><vh>Added 3 .cascading style sheets to the distribution list</vh></v>
<v t="ekr.20040804164600.98"><vh>Fixed some bugs in g.importFromPath</vh></v>
<v t="ekr.20040804164600.102"><vh>Fixed major bug in write logic</vh></v>
<v t="ekr.20040804164600.265"><vh>Fixed bug in p.isAncestorOf</vh></v>
<v t="ekr.20040804164600.275"><vh>Leo now writes only the currently selected tree when pasting to the clipboard</vh></v>
<v t="ekr.20040804164600.377"><vh>Fixed performance bug when reading .leo files</vh></v>
<v t="ekr.20040804170846"><vh>Leo now reports problems with bad directories more clearly</vh></v>
<v t="ekr.20040804164600.394"><vh>Leo reads collapsed xml tags properly in .leo files</vh></v>
<v t="ekr.20040804164600.406"><vh>Leo makes brings the confirm save box to the front</vh></v>
<v t="ekr.20040804164600.419"><vh>Improved how es_exception gets line number of errors</vh></v>
<v t="ekr.20040804164600.421"><vh>Fixed major bug: changing headline now marks subnodes dirty</vh></v>
<v t="ekr.20040804164600.470"><vh>Leo now gives update warning only once per derived file</vh></v>
<v t="ekr.20040804164600.471"><vh>Leo updates tnodeLists properly in all situations</vh></v>
<v t="ekr.20040804164600.515"><vh>Fixed several leaks of positions</vh></v>
<v t="ekr.20040804171818"><vh>Fixed all unit tests so they work with both Python 2.2 and Python 2.3</vh></v>
</v>
<v t="ekr.20040804165258.2"><vh>Features</vh>
<v t="ekr.20040804172113"><vh>@test and @suite greatly aid unit testing</vh></v>
<v t="ekr.20040804172113.1"><vh>New scripts in test.leo make it very easy to use the gc, profile and timeit modules</vh></v>
<v t="ekr.20040804165258.3"><vh>Import dialogs allow multiple selections</vh></v>
<v t="ekr.20040804165258.4"><vh>New Check menu and commands</vh></v>
<v t="ekr.20040804170531"><vh>Perfect Import feature automatically corrects imported files</vh></v>
<v t="ekr.20040804170657"><vh>Improved performance of outline pane</vh></v>
<v t="ekr.20040804164600.424"><vh>The Go To Line Number command ignores all @all nodes</vh></v>
</v>
</v>
<v t="EKR.20040628095213"><vh>4.2 beta 1 &amp; beta 2</vh>
<v t="EKR.20040628095213.311"><vh>New coding conventions</vh></v>
<v t="EKR.20040524104904.242"><vh>Extending the format of .leo files</vh></v>
<v t="ekr.20040705111716"><vh>in 4.2 b2</vh>
<v t="ekr.20040705111716.1"><vh>Savedmarks and expantion state in &lt;v&gt; elements for @thin nodes</vh></v>
<v t="ekr.20040705111716.45"><vh>Marked all related @thin nodes dirty when a node changesd</vh></v>
<v t="ekr.20040705111716.126"><vh>Fixed bug when reading  4.1 files with topology errors</vh></v>
<v t="ekr.20040705150130"><vh>Leo passes all important pychecker tests</vh></v>
</v>
<v t="ekr.20040705112148"><vh>in 4.2 b1</vh>
<v t="EKR.20040628095213.513"><vh>Changed *nix install script</vh></v>
<v t="EKR.20040628100535"><vh>Fixed bugs</vh>
<v t="EKR.20040628095213.3"><vh>Made "end1" and "ilde"events work again</vh></v>
<v t="EKR.20040628095213.23"><vh>Put drawing hooks back in</vh></v>
<v t="EKR.20040628095213.56"><vh>Fixed syntax colouring Bug in html mode</vh></v>
<v t="EKR.20040628095213.60"><vh>Colorizing fixes</vh></v>
<v t="EKR.20040628095213.113"><vh>Fixed Select All bug</vh></v>
<v t="EKR.20040628095213.121"><vh>Fixed bugs in @tab_width: support backspace with negative tab width</vh></v>
<v t="EKR.20040628095213.143"><vh>Fixed bugs in Remove Sentinel command</vh></v>
<v t="EKR.20040628095213.160"><vh>Eliminated spurious error messages in Import Derived File command</vh></v>
<v t="EKR.20040628095213.192"><vh>Removed gnx in headlines when importing thin derived files</vh></v>
<v t="EKR.20040628095213.202"><vh>Fixed bugs reading 4.1 files</vh></v>
<v t="EKR.20040628095213.213"><vh>Fixed Open With bug</vh></v>
<v t="EKR.20040628095213.225"><vh>Fixed Go To Line Number command</vh></v>
<v t="EKR.20040628095213.246"><vh>Fixed crash when importing Borland wstring.cpp</vh></v>
<v t="EKR.20040628095213.279"><vh>Fixed bug in insertBodyTime</vh></v>
<v t="EKR.20040628095213.297"><vh>Fixed bug when pasting large text into headlines</vh></v>
<v t="EKR.20040628095213.308"><vh>Fixed bug in delete command</vh></v>
<v t="EKR.20040628095213.312"><vh>Fixed oops: nullGui setIdleTimeHook</vh></v>
<v t="EKR.20040628095213.324"><vh>Fixed problems with trailing newlines and spurious changed bit</vh></v>
<v t="EKR.20040628095213.346"><vh>Fixed headline key handling</vh></v>
<v t="EKR.20040628095213.348"><vh>Fixed Problems executing script</vh></v>
<v t="EKR.20040628095213.354"><vh>Fixed problem with PHP and @last</vh></v>
<v t="EKR.20040628095213.366"><vh>Fixed bug when writing unknownAttributes</vh></v>
<v t="EKR.20040628095213.368"><vh>Fixed bugs opening a second file</vh></v>
<v t="EKR.20040628095213.404"><vh>Fixed bug: @last silently failed when extra lines exist</vh></v>
<v t="EKR.20040628095213.407"><vh>Fixed hang when dragging from one clone copy to another</vh></v>
<v t="EKR.20040628095213.412"><vh>Fixed crash in Write Missing</vh></v>
<v t="EKR.20040628095213.442"><vh>Fixed bug in getScript</vh></v>
<v t="EKR.20040628095213.444"><vh>Fixed problems with @all</vh></v>
<v t="EKR.20040628095213.499"><vh>Fixed double print in Execute Script command</vh></v>
<v t="EKR.20040628095213.512"><vh>Fixed bug reading leo.nsi</vh></v>
</v>
<v t="EKR.20040628100535.1"><vh>Added new features</vh>
<v t="EKR.20040628095213.52"><vh>Allowed &lt;/leo_header&gt; tag</vh></v>
<v t="EKR.20040628095213.109"><vh>Replaced the word "Leo" with Leo icon in Find/Compare/Prefs windows</vh></v>
<v t="EKR.20040628095213.110"><vh>Improved Import command slightly</vh></v>
<v t="EKR.20040628095213.197"><vh>Added 3 files to distribution lists</vh></v>
<v t="EKR.20040628095213.198"><vh>Supported @tabwidth in indent/dedent</vh></v>
<v t="EKR.20040628095213.264"><vh>Import now creates absolute path</vh></v>
<v t="EKR.20040628095213.269"><vh>Created @killcolor directive</vh></v>
<v t="EKR.20040628095213.282"><vh>Added Paste Retaining Clones command</vh></v>
<v t="EKR.20040628095213.314"><vh>Added readLineGenerator &amp; readLineClass to leoGlobals</vh></v>
<v t="EKR.20040628095213.334"><vh>Much better error handling in executeScript</vh></v>
<v t="EKR.20040628095213.377"><vh>Recovered nodes when reading .leo files containing topology errors</vh></v>
<v t="EKR.20040628095213.391"><vh>Generalized write-to-string logic</vh></v>
<v t="EKR.20040628095213.408"><vh>Added case_sensitiveLanguage to colorizer</vh></v>
<v t="EKR.20040628095213.425"><vh>Write entire @thin tree on write errors</vh></v>
<v t="EKR.20040628095213.485"><vh>Handled inner @language and @comment properly</vh></v>
<v t="EKR.20040628095213.490"><vh>Better reporting of body text conflicts</vh></v>
<v t="EKR.20040628095213.493"><vh>Improved error handling for unknownAttributes</vh></v>
<v t="EKR.20040628095213.501"><vh>Read and write all t.unknownAttributes in top vnode of an @thin tree</vh></v>
</v>
</v>
</v>
<v t="EKR.20040601084317"><vh>4.2 a3</vh>
<v t="EKR.20040601084317.2"><vh>Bug fixes</vh>
<v t="EKR.20040601101118"><vh>Fixed copy/paste operations involving @thin trees</vh></v>
<v t="EKR.20040601101430"><vh>Fixed Change Headline command</vh></v>
<v t="EKR.20040601084317.99"><vh>Eliminated spurious "Not written x.tmp" message after write errors</vh></v>
<v t="EKR.20040601084317.142"><vh>Fixed problems saving unknownAttribute field</vh></v>
<v t="EKR.20040601102115"><vh>Fixed unicode problem in the Dump Outline command</vh></v>
</v>
<v t="EKR.20040601101227"><vh>New Features</vh>
<v t="EKR.20040601101227.1"><vh>Leo ignores all directives in @all trees</vh></v>
<v t="EKR.20040601101430.1"><vh>@+-middle sentinels allow sections to be defined in grandchildren</vh></v>
<v t="EKR.20040601101510"><vh>@clone sentinel allows siblings to be cloned</vh></v>
<v t="EKR.20040601101547"><vh>Created @thin, @nosent, @noref and @asis abbreviations</vh>
<v t="EKR.20040524104904.92"><vh>Appendix 1 to Chapter 4: Using @asis, @noref and @nosent trees</vh></v>
</v>
<v t="EKR.20040601084317.102"><vh>Made undo extensible</vh></v>
<v t="EKR.20040601102703"><vh>Started work on simple new undo scheme</vh></v>
<v t="EKR.20040601084317.161"><vh>Created new c, p, v iterators</vh></v>
</v>
<v t="EKR.20040601102808"><vh>Known bugs</vh></v>
</v>
<v t="EKR.20040518070558"><vh>4.2 a2</vh>
<v t="EKR.20040518070940.5"><vh>Implemented @file-thin</vh></v>
<v t="EKR.20040518070824"><vh>Fixed bugs</vh>
<v t="EKR.20040518071415"><vh>Fixed clone bug that caused parts of outlines to disappear</vh></v>
<v t="EKR.20040518070940.156"><vh>Fixed long-standing problem with the outline-only command</vh></v>
<v t="EKR.20040518070824.1"><vh>Made sure file indices are always assigned when writing files.</vh></v>
<v t="EKR.20040518070940"><vh>Fixed problems with missing tnodeList with @file-noref</vh></v>
<v t="EKR.20040518070940.164"><vh>Added t.writeBit</vh></v>
</v>
<v t="EKR.20040518075457"><vh>Dangers of @file-thin</vh></v>
</v>
</v>
<v t="ekr.20060206111600"><vh>4.3...@settings</vh>
<v t="ekr.20050917092557"><vh>4.3.3 final</vh>
<v t="ekr.20050917105646"><vh>Fixes made in 4.3.3</vh></v>
<v t="ekr.20050917092557.1"><vh>Rewrote documentation</vh></v>
<v t="ekr.20050917092557.2"><vh>Bug fixes...</vh>
<v t="ekr.20050917092557.3"><vh>Fixed various unicode bugs</vh></v>
<v t="ekr.20050917092557.4"><vh>Fixed bugs relating to recent files</vh></v>
<v t="ekr.20050917092557.5"><vh>Fixed minor crasher in colorizer</vh></v>
<v t="ekr.20050917092557.6"><vh>Protected several methods used by plugin manager</vh></v>
<v t="ekr.20050917092557.7"><vh>Added test files to distribution list and cvs</vh></v>
</v>
<v t="ekr.20050917092557.8"><vh>New and improved  plugins</vh>
<v t="ekr.20050917092557.9"><vh>New rst3 plugin</vh></v>
<v t="ekr.20050917092557.10"><vh>Improved spellpyx plugin</vh></v>
<v t="ekr.20050917092557.11"><vh>Improved vim and openWith plugins</vh></v>
</v>
<v t="ekr.20050917092557.12"><vh>New &amp; improved features...</vh>
<v t="ekr.20050917092557.13"><vh>Added g.es_print, g.es_trace function</vh></v>
<v t="ekr.20050917092557.14"><vh>Improved PrettyPrinting</vh></v>
</v>
</v>
<v t="ekr.20050913131848"><vh>4.3.2 final</vh>
<v t="ekr.20050906104918.1"><vh>Rewrote documentation</vh></v>
<v t="ekr.20050906104931.1"><vh>Bug fixes...</vh>
<v t="ekr.20050909082711"><vh>Fixed various unicode bugs</vh></v>
<v t="ekr.20050906104931.15"><vh>Fixed bugs relating to recent files</vh></v>
<v t="ekr.20050906104931.38"><vh>Fixed minor crasher in colorizer</vh></v>
<v t="ekr.20050906104931.42"><vh>Protected several methods used by plugin manager</vh></v>
<v t="ekr.20050906104931.43"><vh>Added test files to distribution list and cvs</vh></v>
</v>
<v t="ekr.20050908164150"><vh>New and improved  plugins</vh>
<v t="ekr.20050908164150.1"><vh>New rst3 plugin</vh></v>
<v t="ekr.20050908164150.2"><vh>Improved spellpyx plugin</vh></v>
<v t="ekr.20050910143326"><vh>Improved vim and openWith plugins</vh></v>
</v>
<v t="ekr.20050906104931.48"><vh>New &amp; improved features...</vh>
<v t="ekr.20050906104931.49"><vh>Added g.es_print, g.es_trace function</vh></v>
<v t="ekr.20050906104931.56"><vh>Improved PrettyPrinting</vh></v>
</v>
</v>
<v t="ekr.20050906104918"><vh>4.3.2 beta 1</vh></v>
<v t="ekr.20050620144052"><vh>4.3.1</vh>
<v t="ekr.20050620144052.2"><vh>Bug fixes...</vh>
<v t="ekr.20050620144052.3"><vh>Fixed bug in @ratio setting</vh></v>
<v t="ekr.20050620144052.6"><vh>Fixed crasher footprint plugin</vh></v>
<v t="ekr.20050620144052.8"><vh>Fixed invalid position bug)</vh></v>
<v t="ekr.20050620144052.48"><vh>Fixed undo problems in unit tests</vh></v>
<v t="ekr.20050620144052.112"><vh>Made sure same case is used in all recent files entries</vh></v>
<v t="ekr.20050620144052.114"><vh>Made sure all dialogs gets focus when they are run</vh></v>
<v t="ekr.20050620144052.116"><vh>Improved Resize To Screen command</vh></v>
<v t="ekr.20050620144052.119"><vh>Made sure comments are always visible in setting dialog even for non-@ nodes</vh></v>
<v t="ekr.20050620144052.154"><vh>Fixed problem with leading @ in body text</vh></v>
<v t="ekr.20050620144052.166"><vh>Fixed several  crashers while undoing a move involving clones</vh></v>
<v t="ekr.20050620144052.182"><vh>Fixed Unicode encoding problem</vh></v>
<v t="ekr.20050620144052.185"><vh>Fixed problem with coloring @language plain</vh></v>
<v t="ekr.20050620144602"><vh>Fixed bug: Mark Clones command did not work</vh></v>
</v>
<v t="ekr.20050620144052.207"><vh>New features...</vh>
<v t="ekr.20050620144052.208"><vh>Created separate helpers for idle_body_key</vh></v>
<v t="ekr.20050620144052.210"><vh>Made all Mark commands undoable</vh></v>
<v t="ekr.20050620144052.222"><vh>Removed dependence on profile and pstats modules from leoTest.py</vh></v>
<v t="ekr.20050620144052.231"><vh>Added support for tk resource files</vh></v>
<v t="ekr.20050620144425"><vh>Added support for coloring the PL/SQL language</vh></v>
</v>
</v>
<v t="ekr.20050523092026"><vh>4.3-final</vh>
<v t="ekr.20050523092056.1"><vh>Fixed crasher when pie-menu plugin enabled</vh></v>
<v t="ekr.20050523092056.4"><vh>Fixed crasher in Extract Section Command</vh></v>
</v>
<v t="ekr.20050513141852"><vh>4.3-beta 2</vh>
<v t="ekr.20050513141913.1"><vh>Fixed bugs...</vh>
<v t="ekr.20050513141913.16"><vh>Fixed nodenavagator bug</vh></v>
<v t="ekr.20050513141913.17"><vh>Fixed LaTex Coloring bug</vh></v>
<v t="ekr.20050513141913.22"><vh>Error messages in scripts are now redirected properly.</vh></v>
<v t="ekr.20050513141913.30"><vh>Fixed 2 crashers in nav_buttons plugin</vh></v>
<v t="ekr.20050513141913.57"><vh>Fixed crasher in yoffsetTree</vh></v>
<v t="ekr.20050513141913.60"><vh>Fixed crasher in undo</vh></v>
<v t="ekr.20050513141913.82"><vh>Fixed  several problems with Extract and Extract Section</vh></v>
<v t="ekr.20050513141913.91"><vh>Fixed bug with Delete in headlines</vh></v>
<v t="ekr.20050513141913.127"><vh>Fixed bugs re initial_splitter_orientation &amp; @strings &amp; @ints generally</vh></v>
<v t="ekr.20050513141913.140"><vh>Fixed bug with hoist + insert</vh></v>
<v t="ekr.20050513141913.145"><vh>Fixed problem with settings dialog position when panes split horizontally</vh></v>
<v t="ekr.20050513141913.149"><vh>Fixed problem changing shortcut &amp; redid shortcuts widget</vh></v>
</v>
<v t="ekr.20050513141913.187"><vh>New Features...</vh>
<v t="ekr.20050513141913.97"><vh>Marking any node sets the outline changed</vh></v>
<v t="ekr.20050513141913.188"><vh>Allow quoted urls in  @urls nodes</vh></v>
<v t="ekr.20050513141913.194"><vh>Moved executeFile into core</vh></v>
<v t="ekr.20050513141913.197"><vh>Rewrote g.getScript using at.writeFromString</vh></v>
<v t="ekr.20050513141913.233"><vh>Added define_name arg to c.executeScript</vh></v>
</v>
</v>
<v t="ekr.20050429094215"><vh>4.3-beta 1</vh>
<v t="ekr.20050429094215.2"><vh>Fixed bugs...</vh>
<v t="ekr.20050429094215.3"><vh>Made sure NameErrors are reported with tracebacks in scripts</vh></v>
<v t="ekr.20050429094215.22"><vh>Finally! fixed .leoID problem!</vh></v>
<v t="ekr.20050429094215.31"><vh>Investigated problem with LeoPluginsRef.leo</vh></v>
<v t="ekr.20050429094215.41"><vh>Fixed conflicts in menu shortcuts</vh></v>
<v t="ekr.20050429094215.113"><vh>Fixed bug in p.initStatus caught by pychecker</vh></v>
<v t="ekr.20050429094215.116"><vh>Fixed crasher in import logic (leoAtFile)</vh></v>
<v t="ekr.20050429094215.120"><vh>Put in protections against unbounded recursion in idle_scrollTo</vh></v>
</v>
<v t="ekr.20050429094215.130"><vh>New features...</vh>
<v t="ekr.20050429094215.131"><vh>Created stand-alone leoGlobals.py module</vh></v>
<v t="ekr.20050429094215.139"><vh>Leo now ignores problems opening settings file for chapters plugin</vh></v>
<v t="ekr.20050429094215.145"><vh>Improved write logic</vh></v>
<v t="ekr.20050429094215.173"><vh>Rewrote the undo code</vh></v>
<v t="ekr.20050429094215.286"><vh>Implemented undo/redo for Paste Retaining clones</vh></v>
<v t="ekr.20050429094215.316"><vh>Added support for 'str_' uA's</vh></v>
<v t="ekr.20050429094215.347"><vh>Removed unused params from leoAtFile.py</vh></v>
<v t="ekr.20050429094215.353"><vh>Leo  saves recent files info in .leoRecentFiles.txt files</vh>
<v t="ekr.20050429094215.354"><vh>What I did</vh></v>
<v t="ekr.20050429094215.355"><vh>New plan</vh></v>
</v>
<v t="ekr.20050429095849"><vh>Finished all @settings coding</vh></v>
</v>
</v>
<v t="ekr.20050313101229"><vh>4.3-a4</vh>
<v t="ekr.20050313101229.2"><vh>Fixed bugs...</vh>
<v t="ekr.20050313101229.69"><vh>Fix colorizer bug for initial @nocolor in @root nodes</vh></v>
<v t="ekr.20050313101229.74"><vh>Fixed @wrap bug</vh></v>
<v t="ekr.20050313101229.77"><vh>Fixed change-all bug</vh></v>
</v>
<v t="ekr.20050313103448"><vh>New features...</vh>
<v t="ekr.20050313101229.95"><vh>Created Add Comments and Delete Comments commands</vh></v>
<v t="ekr.20050313101229.94"><vh>Deprecated new_c key in hooks, added c key</vh></v>
<v t="ekr.20050313103448.1"><vh>Added the 'before-create-leo-frame' hook</vh></v>
<v t="ekr.20050313101229.101"><vh>Added support for mod_labels plugin</vh></v>
</v>
<v t="ekr.20050313101229.100"><vh>Revised plugins for the 4.3 code base</vh></v>
</v>
<v t="ekr.20050221104844"><vh>4.3-a3</vh>
<v t="ekr.20050221104844.2"><vh>Bugs</vh>
<v t="ekr.20050221104844.3"><vh>Fixed crasher in Tangle</vh></v>
<v t="ekr.20050221104844.12"><vh>Applied patch to rst2 plugin</vh></v>
<v t="ekr.20050221104844.14"><vh>Revised searchbox plugin so it works with Leo 4.3</vh></v>
<v t="ekr.20050221104844.27"><vh>Fixed bugs in nav_buttons and nodenavigator plugins</vh></v>
<v t="ekr.20050221104844.45"><vh>Made sure Leo asks for leoID at most once</vh></v>
<v t="ekr.20050221104844.54"><vh>Fixed botch in g.pdb</vh></v>
<v t="ekr.20050222100936"><vh>Fixed crasher when executing a script if the script was selected text in a new window</vh></v>
</v>
<v t="ekr.20050221104844.57"><vh>New features</vh>
<v t="ekr.20050221104844.58"><vh>Added sets.py to distribution</vh></v>
<v t="ekr.20050221104844.59"><vh>Added color='suppress' hack to g.es</vh></v>
</v>
</v>
<v t="ekr.20050126100405"><vh>4.3-a2</vh>
<v t="ekr.20050130112336.1"><vh>To do: Improve how Leo handles recent files</vh></v>
<v t="ekr.20050209141626.3"><vh>Bugs fixed...</vh>
<v t="ekr.20050209141626.4"><vh>Fixed very old bug in Undo Insert Node </vh></v>
<v t="ekr.20050209141626.8"><vh>Made sure to remove duplicates from recent files</vh></v>
<v t="ekr.20050209141626.12"><vh>Fixed indentation problems in leoTkinterFind.py</vh></v>
<v t="ekr.20050209141626.13"><vh>Changed leoConfig.txt to leoSettings.leo in Help menu, etc.</vh></v>
<v t="ekr.20050209141626.16"><vh>Investigated recent files problems</vh></v>
<v t="ekr.20050209141626.23"><vh>Improved queuing of log messages</vh></v>
<v t="ekr.20050209141626.42"><vh>Fixed crasher in Change All command</vh></v>
<v t="ekr.20050209141626.43"><vh>Fixed crasher in script button</vh></v>
<v t="ekr.20050209141626.46"><vh>Fixed print problems on the Mac</vh></v>
<v t="ekr.20050209141626.53"><vh>leoTest.runTests now makes copies of all positions</vh></v>
<v t="ekr.20050209141626.54"><vh>Fixed problems with unit test file paths</vh></v>
<v t="ekr.20050209141626.55"><vh>Made local config settings work again</vh></v>
<v t="ekr.20050209141626.91"><vh>Fix problems searching for nothing but whitespace</vh></v>
<v t="ekr.20050210101318"><vh>Fixed problems with typing return in the Find panel</vh></v>
<v t="ekr.20050209141626.101"><vh>Buttons no longer work in toolbars when settings dialog is open</vh></v>
<v t="ekr.20050209141626.102"><vh>Fixed bug in delayed focus logic</vh></v>
<v t="ekr.20050209141626.105"><vh>Made sure Leo asks for leoID at most once</vh></v>
<v t="ekr.20050209141626.113"><vh>Leo now prints unicode characters properly in the log pane</vh></v>
<v t="ekr.20050209141626.114"><vh>Fixed various problems with opening files with Unicode filenames</vh></v>
<v t="ekr.20050211095754"><vh>Fixed bug reading encoding field in derived files</vh></v>
<v t="ekr.20050212054743"><vh>Allow indented code blocks to be run using Execute Script command</vh></v>
<v t="ekr.20050212144116"><vh>Fixed problems found by pychecker</vh></v>
</v>
<v t="ekr.20050209141626.150"><vh>New features...</vh>
<v t="ekr.20050126100405.1"><vh>Added undo granularity</vh>
<v t="EKR.20040524104904.48"><vh>Undoing operations</vh></v>
</v>
<v t="ekr.20050209141626.185"><vh>Added support for top-level init function in plugins</vh></v>
<v t="ekr.20050209141626.190"><vh>Changed name of Paste Retaining Clones to Paste Node As Clone</vh></v>
<v t="ekr.20050209141626.193"><vh>Added leoPlugins.leo to Help menu</vh></v>
<v t="ekr.20050209141626.194"><vh>Script buttons can request to be removed</vh></v>
<v t="ekr.20050209141626.195"><vh>Improved documentation in several nodes in leoSettings.leo</vh></v>
<v t="ekr.20050209141626.196"><vh>Predefined c,g &amp; p in scripts, unit tests &amp; test routines</vh></v>
<v t="ekr.20050209141626.198"><vh>Changed name of Preferences command to Settings</vh></v>
</v>
</v>
<v t="ekr.20050122090311"><vh>4.3-a1</vh>
<v t="ekr.20050123112834"><vh>Defining features of 4.3</vh>
<v t="ekr.20050123110009"><vh>Using @settings trees and leoSettings.leo</vh>
<v t="ekr.20050122084954"><vh>Using leoSettings.leo and @settings trees</vh></v>
<v t="ekr.20050122091036"><vh>Unfinished configuration features</vh></v>
</v>
<v t="ekr.20050123092834.520"><vh>Rewrote Leo's read/write logic</vh></v>
<v t="ekr.20050123115804"><vh>Added Plugins Manager plugin</vh></v>
<v t="ekr.20050123115804.1"><vh>You can install third-party extensions in Leo's extensions directory</vh></v>
</v>
<v t="ekr.20050123092834.1"><vh>Fixed bugs...</vh>
<v t="ekr.20050123101208"><vh> Major bugs: these bugs corrupted derived files!</vh>
<v t="ekr.20050123092834.432"><vh>Fixed double doc part bug</vh></v>
<v t="ekr.20050123092834.497"><vh>Fixed bug in how Leo writes thin derived files</vh></v>
</v>
<v t="ekr.20050123092834.2"><vh>Commands</vh>
<v t="ekr.20050123092834.6"><vh>Fixed problems with spawnv option of openWith</vh></v>
<v t="ekr.20050123092834.19"><vh>Fixed bug in  Remove Sentinels command</vh></v>
<v t="ekr.20050123092834.27"><vh>Fixed bug re Paste Node As Clone</vh></v>
<v t="ekr.20050123092834.42"><vh>Fixed Pretty Print commands for Python 2.4</vh></v>
<v t="ekr.20050123092834.71"><vh>Fixed crasher in Import Derived Files command</vh></v>
<v t="ekr.20050123092834.510"><vh>Search commands are now restricted to hoisted area</vh></v>
</v>
<v t="ekr.20050123100706.1"><vh>Distribution</vh>
<v t="ekr.20050123092834.491"><vh>Fixed file association in leoDist.leo</vh></v>
</v>
<v t="ekr.20050123092834.165"><vh>Files</vh>
<v t="ekr.20050123092834.492"><vh>g.import wrappers return module if it is in sys.modules</vh></v>
<v t="ekr.20050123092834.166"><vh>Disabled changes to comment delims in @@language and @@comment sentinels</vh></v>
<v t="ekr.20050123092834.176"><vh>Made sure files that differ only in line ending get written if @lineending is in effect</vh></v>
<v t="ekr.20050123092834.196"><vh>Fixed bug:  @nosent wrote sentinels!</vh></v>
<v t="ekr.20050123092834.422"><vh>Fixed bug in replaceTargetFileIfDifferent</vh></v>
<v t="ekr.20050123092834.424"><vh>Made sure that @ignore forces writing of inner @thin trees</vh></v>
<v t="ekr.20050123092834.431"><vh>Fixed crasher when attempting to write a derived file to an invalid path</vh></v>
<v t="ekr.20050123092834.434"><vh>Fixed Python 2.4 deprecation warning when saving .leo files</vh></v>
<v t="ekr.20050123092834.499"><vh>Fixed crasher in getOutputNewline</vh></v>
<v t="ekr.20050123092834.544"><vh>Always use os.rename in utils_rename</vh></v>
<v t="ekr.20050123151338"><vh>Fixed bugs handling @language &amp; @comment in atFile.scanAllDirectives &amp; g.scanDirectives)</vh></v>
</v>
<v t="ekr.20050123103303"><vh>Gui</vh>
<v t="ekr.20050123092834.502"><vh>Put the scrollWheel workaround in createTkTreeCanvas</vh></v>
</v>
<v t="ekr.20050123100706.2"><vh>Menus</vh>
<v t="ekr.20050123092834.81"><vh>Fixed problems with Control-E</vh></v>
<v t="ekr.20050123092834.490"><vh>Better handling of duplicate menu shortcuts</vh></v>
</v>
<v t="ekr.20050123092834.159"><vh>Nodes</vh>
<v t="ekr.20050123092834.160"><vh>Fixed crash after cutting an imported node</vh></v>
<v t="ekr.20050123092834.163"><vh>Removed invalid assert in lastVisible</vh></v>
<v t="ekr.20050123093854.1"><vh>Fixed bugs in tnodes_iter and unique_tnodes_iter</vh></v>
</v>
<v t="ekr.20050123111723"><vh>Plugins</vh>
<v t="ekr.20050123092834.1047"><vh>Fixed two bugs in Plugins Manager plugin</vh></v>
<v t="ekr.20050123092834.1052"><vh>Fixed bug re referencing destroyed ivars</vh></v>
<v t="ekr.20050123092834.1057"><vh>Fixed bug in registerOneHandler</vh></v>
<v t="ekr.20050123092834.506"><vh>Fixed conflict between settings panel and chapters plugin</vh></v>
</v>
<v t="ekr.20050123092834.526"><vh>Pychecker</vh></v>
<v t="ekr.20050123092834.438"><vh>Scripting</vh>
<v t="ekr.20050123092834.439"><vh>Fixed unbounded recursion with --script and redirected output</vh></v>
<v t="ekr.20050123092834.474"><vh>Script buttons now execute the entire script</vh></v>
<v t="ekr.20050123092834.480"><vh>Fixed error reporting in executeScript when the error happens outside the script</vh></v>
</v>
<v t="ekr.20050123092834.486"><vh>Startup</vh>
<v t="ekr.20050123092834.487"><vh>Non-existent command-line file becomes name of new Leo wiindow</vh></v>
<v t="ekr.20050123092834.1011"><vh>computeHomeDir now handles references to other vars</vh></v>
</v>
</v>
<v t="ekr.20050123092834.896"><vh>New or improved features...</vh>
<v t="ekr.20050123110009"><vh>Using @settings trees and leoSettings.leo</vh>
<v t="ekr.20050122084954"><vh>Using leoSettings.leo and @settings trees</vh></v>
<v t="ekr.20050122091036"><vh>Unfinished configuration features</vh></v>
</v>
<v t="ekr.20050123103303.1"><vh>Code</vh>
<v t="ekr.20050123092834.520"><vh>Rewrote Leo's read/write logic</vh></v>
<v t="ekr.20050123092834.173"><vh>Added g.cantImport</vh></v>
<v t="ekr.20050123092834.901"><vh>Added g.fileLikeObject.readline</vh></v>
<v t="ekr.20050123092834.928"><vh>Added support for g.app.debugSwitch in es_exception</vh></v>
<v t="ekr.20050123092834.984"><vh>Restored drawing/event hooks</vh></v>
<v t="ekr.20050123092834.1004"><vh>Added p=p param to all hooks containing v=v</vh></v>
<v t="ekr.20050123092834.565"><vh>Implemented delayed focus scheme</vh></v>
</v>
<v t="ekr.20050123103521"><vh>Commands</vh>
<v t="ekr.20050123092834.897"><vh>Added 'Expand Or Go Right' and 'Contract or Go Left' commands</vh></v>
<v t="ekr.20050123092834.908"><vh>Added keyboard shortcuts to find panel</vh></v>
<v t="ekr.20050123092834.1005"><vh>Find panels are now associated with individual Leo windows</vh></v>
<v t="ekr.20050123105026"><vh>Find panels are now inited from @settings nodes</vh></v>
<v t="ekr.20050123092834.961"><vh>Improved Go To Line Number and Execute Script commands</vh></v>
<v t="ekr.20050123092834.1018"><vh>Improved support for relative path names</vh></v>
<v t="ekr.20050123092834.1043"><vh>Implemented 'Undo Clear Recent Files'</vh></v>
<v t="ekr.20050123092834.517"><vh>Removed old-style write commands</vh></v>
</v>
<v t="ekr.20050123092834.1044"><vh>Plugins &amp; extensions</vh>
<v t="ekr.20050123115804"><vh>Added Plugins Manager plugin</vh></v>
<v t="ekr.20050123115804.1"><vh>You can install third-party extensions in Leo's extensions directory</vh></v>
<v t="ekr.20050123112151"><vh>Improved doHandlersForTag</vh></v>
<v t="ekr.20050123092834.1013"><vh>Leo now associates modules with hook handlers</vh></v>
</v>
<v t="ekr.20050123103753"><vh>Syntax Coloring &amp; languages</vh>
<v t="ekr.20050123092834.903"><vh>Added support for Ada</vh></v>
<v t="ekr.20050123092834.929"><vh>Added support for Forth</vh></v>
</v>
</v>
</v>
</v>
<v t="ekr.20060206111717.1"><vh>4.4 minibuffer, keys, autocompletion, multiple log panes</vh>
<v t="ekr.20051219150602"><vh>4.4 alpha 5</vh>
<v t="ekr.20051219150602.2"><vh>Fixed bugs</vh>
<v t="ekr.20051219150602.3"><vh>Made sure focus doesn't go to log during tab completion or after writes to log</vh></v>
<v t="ekr.20051219150602.7"><vh>Fixed problem with getScript in batch mode</vh></v>
<v t="ekr.20051219150602.10"><vh>Text box is now selected in goto-line-number command</vh></v>
<v t="ekr.20051219150602.13"><vh>Restored headkey  &amp; bodykey hooks</vh></v>
<v t="ekr.20051219150602.28"><vh>Fixed ancient bug in read error logic that hung Leo</vh></v>
<v t="ekr.20051219150602.75"><vh>Fixed many headline problems</vh></v>
<v t="ekr.20051219150602.81"><vh>Fixed problem in reformatParagraph</vh></v>
<v t="ekr.20051219150602.85"><vh>Installed LeoUsers patch </vh></v>
<v t="ekr.20060105182648.376"><vh>Improved Import Derived Files command.</vh></v>
<v t="ekr.20060105182648.377"><vh>Fixed crasher in backwardDeleteCharacter</vh></v>
<v t="ekr.20060105182648.378"><vh>Fixed recent bug: dialogs now get focus properly when first opened.</vh></v>
<v t="ekr.20060105182648.379"><vh>Made sure shortcuts are printed clearly by k.registerCommand</vh></v>
<v t="ekr.20060105182648.382"><vh>Suppressed crash undoing a clone followed by a drag</vh></v>
</v>
<v t="ekr.20051219150602.100"><vh>New features</vh>
<v t="ekr.20051219150602.101"><vh>created ut.leo, ut.py and ut.bat</vh></v>
<v t="ekr.20051219150602.102"><vh>Added modes/*.xml to distribution</vh></v>
<v t="ekr.20051219150602.105"><vh>Revised cursor movement commands and added selection-extension commands</vh></v>
<v t="ekr.20051219151926"><vh>Added classic key bindings in leoSettings.leo</vh></v>
<v t="ekr.20060105182648.432"><vh>Allow multiple key bindings to the same command</vh></v>
<v t="ekr.20060105182648.469"><vh>Settings command now opens leoSettings.leo</vh></v>
</v>
</v>
<v t="ekr.20051028051444"><vh>4.4 alpha 4</vh>
<v t="ekr.20051028051444.1"><vh>Quick Start</vh></v>
<v t="ekr.20051028051444.2"><vh>The 'key' features of 4.4</vh>
<v t="ekr.20051101161405"><vh>Leo's minibuffer works like the Emacs mini-buffer</vh></v>
<v t="ekr.20051101161405.1"><vh>@shortcuts nodes in leoSettings.leo allow per-pane bindings</vh></v>
<v t="ekr.20051101161405.2"><vh>The scripting plugin allows key bindings</vh></v>
<v t="ekr.20051101161405.3"><vh>EKR shortcuts</vh></v>
<v t="ekr.20051101162123"><vh>Leo now ignores key bindings in menu tables</vh></v>
</v>
<v t="ekr.20051205091625"><vh>Status of minibuffer commands</vh></v>
<v t="ekr.20051028051616"><vh>New in alpha 1...</vh>
<v t="ekr.20051028051444.4"><vh>New options</vh>
<v t="ekr.20051028051444.5"><vh>The @bool useMinibuffer option</vh></v>
<v t="ekr.20051028051444.6"><vh>The @bool useCmdMenu option</vh></v>
<v t="ekr.20051028051444.7"><vh>Options for selected body text</vh></v>
</v>
<v t="ekr.20051028051444.8"><vh>New mini-buffer commands</vh></v>
<v t="ekr.20051028051444.9"><vh>New code-level features</vh>
<v t="ekr.20051028051444.10"><vh>Dictionaries of keys and commands</vh></v>
<v t="ekr.20051028051444.11"><vh>Functions that return the present key bindings</vh></v>
<v t="ekr.20051028051444.12"><vh>The registerCommand helper</vh></v>
</v>
<v t="ekr.20051028051444.13"><vh>Bugs fixed (in 4.3 code base)</vh>
<v t="ekr.20051028051444.14"><vh>Leo protects c.endUpdate with a 'finally' clause</vh></v>
<v t="ekr.20051028051444.15"><vh>Added kludge to solve infamous control-v problems</vh></v>
<v t="ekr.20051028051444.16"><vh>Fixed bug in Leo's read logic</vh></v>
<v t="ekr.20051028051444.17"><vh>Fixed bug in goto-last-node.</vh></v>
<v t="ekr.20051028051444.18"><vh>Leo now reads @settings trees when opening a .leo file from another outline.</vh></v>
<v t="ekr.20051028051444.19"><vh>Improved g.removeExtraLws</vh></v>
</v>
</v>
<v t="ekr.20051028051616.1"><vh>New in alpha 2</vh>
<v t="ekr.20051101162123.1"><vh>The tabbed log</vh>
<v t="ekr.20051028051616.172"><vh>Programming the tabbed log</vh></v>
</v>
<v t="ekr.20051028061322"><vh>New minibuffer commands</vh></v>
<v t="ekr.20051028051616.299"><vh>Optional generation of closing brackets</vh></v>
<v t="ekr.20051101182739"><vh>New settings in leoSettings.leo</vh></v>
<v t="ekr.20051101161949"><vh>Improved and retired plugins</vh>
<v t="ekr.20051028051616.160"><vh>Improved the scripting plugin</vh></v>
<v t="ekr.20051101162947"><vh>Retired the TabbedLog plugin</vh></v>
</v>
<v t="ekr.20051101163145"><vh>Many code-level improvements</vh></v>
<v t="ekr.20051101163404"><vh>Fixed minor bugs</vh></v>
</v>
<v t="ekr.20051109112610"><vh>New in alpha 3</vh>
<v t="ekr.20051109112826"><vh>The New and Newer World Orders</vh></v>
<v t="ekr.20051109141223"><vh>Bugs fixed...</vh>
<v t="ekr.20051109112826.217"><vh>Fix crasher in Open logic</vh></v>
<v t="ekr.20051109112826.227"><vh>(Undo ends editing</vh></v>
<v t="ekr.20051109112826.257"><vh>Disabled minibuffer when not in use</vh></v>
<v t="ekr.20051109112826.315"><vh>Fixed bug in Find Backward</vh></v>
<v t="ekr.20051109112826.265"><vh>Improved Spell tab</vh></v>
</v>
<v t="ekr.20051109141524"><vh>New features</vh>
<v t="ekr.20051109112826.222"><vh>Created scripts.leo and unitTest.leo</vh></v>
<v t="ekr.20051109112826.254"><vh>c.executeMinibufferCommand executes a minibuffer command by name</vh></v>
<v t="ekr.20051109112826.310"><vh>Improved perl entries in language dicts</vh></v>
</v>
<v t="ekr.20051109141524.1"><vh>Code-level changes</vh>
<v t="ekr.20051109112826.223"><vh>Changed  edit_text to edit_widget everywhere</vh></v>
<v t="ekr.20051109112826.224"><vh>Removed tree ivars</vh></v>
<v t="ekr.20051109142920"><vh>Removed frame.begin/endUpdate</vh></v>
</v>
</v>
<v t="ekr.20051128181229"><vh>New in alpha 4</vh>
<v t="ekr.20051128181351"><vh>Bugs fixed</vh>
<v t="ekr.20051128181302.148"><vh>Changed scripting plugin so files opened with buttons stay in front</vh></v>
<v t="ekr.20051128181302.183"><vh>Fixed undo/redo bugs</vh></v>
<v t="ekr.20051128181302.192"><vh>Fixed focus problem with tab completion</vh></v>
<v t="ekr.20051128181302.193"><vh>Fixed minor Save bug</vh></v>
<v t="ekr.20051128181302.231"><vh>Fixed long-standing problem with Plugins Manager plugin</vh></v>
<v t="ekr.20051128181302.244"><vh>Fixed 2 outline editing bugs</vh></v>
<v t="ekr.20051205090923.13"><vh>Fixed crasher in deleteNextChar</vh></v>
<v t="ekr.20051205090923.16"><vh>Fixed new headline bug</vh></v>
<v t="ekr.20051205090923.22"><vh>Fix problems applying settings</vh></v>
<v t="ekr.20051128181302.204"><vh>Fixed several bugs in rst3 plugin</vh></v>
</v>
<v t="ekr.20051128181651"><vh>Code changes</vh>
<v t="ekr.20051128181302.149"><vh>Removed later arg from c.frame.xWantsFocus</vh></v>
<v t="ekr.20051128181302.196"><vh>Created enableTclTraces</vh></v>
<v t="ekr.20051128181302.208"><vh>Eliminated w.update in g.app.gui.set_focus</vh></v>
</v>
<v t="ekr.20051128181651.1"><vh>New &amp; improved features and files</vh>
<v t="ekr.20051128181302.147"><vh>Moved all scripts into scripts.leo</vh></v>
<v t="ekr.20051128181302.150"><vh>Improved how the New Tab and Rename Tab commands work in the log pane</vh></v>
<v t="ekr.20051128181302.151"><vh>Improved the appearance of the Spell tab</vh></v>
<v t="ekr.20051128181302.156"><vh>Added Clone-find checkbox to the Find tab</vh></v>
<v t="ekr.20051128181302.171"><vh>Improved find tab</vh></v>
<v t="ekr.20051128181302.211"><vh>Improved formatting of shortcuts in print-commands and print-bindings</vh></v>
<v t="ekr.20051128181302.213"><vh>Added settings for vim plugin</vh></v>
<v t="ekr.20051128181302.214"><vh>Put up a dialog if can't import Pmw</vh></v>
<v t="ekr.20051128181302.229"><vh>Bound &lt;Return&gt; to end-edit-headline</vh></v>
</v>
</v>
</v>
<v t="ekr.20060116174906"><vh>4.4 beta 1</vh>
<v t="ekr.20060116174906.2"><vh>Bugs fixed</vh>
<v t="ekr.20060116174906.3"><vh>Fixed minor headline problems</vh></v>
<v t="ekr.20060116174906.63"><vh>Fixed undo problems</vh></v>
<v t="ekr.20060116174906.86"><vh>Improved word-export plugin</vh></v>
<v t="ekr.20060116174906.87"><vh>Removed a bad use of g.app.log in the find panel</vh></v>
<v t="ekr.20060116174906.88"><vh>Fix crash: tab in minibuffer</vh></v>
<v t="ekr.20060116174906.90"><vh>Installed patch for headline width</vh></v>
<v t="ekr.20060116174906.97"><vh>Redraw screen properly after Move To Next Dirty</vh></v>
<v t="ekr.20060116174906.100"><vh>Fixed focus bug</vh></v>
<v t="ekr.20060116174906.103"><vh>Made sure to bring proper window on top in settings.leo button</vh></v>
<v t="ekr.20060116174906.104"><vh>Arrow keys now clear the text selection</vh></v>
<v t="ekr.20060116174906.113"><vh>Fixed several minor bugs</vh></v>
<v t="ekr.20060116174906.118"><vh>Fixed problems with plugins</vh></v>
<v t="ekr.20060116174906.122"><vh>Fixed old file handling bug</vh></v>
<v t="ekr.20060116174906.125"><vh>Use shutil.move in g.utils_rename</vh></v>
<v t="ekr.20060116174906.130"><vh>Simplified k.copyBindingsToWidget and eliminated k.onTextWidgetKey</vh></v>
<v t="ekr.20060116174906.160"><vh>Made sure that focus stays in body during tab completion</vh></v>
<v t="ekr.20060116174906.163"><vh>Leo now puts focus in body pane after deleting a window</vh></v>
<v t="ekr.20060116174906.164"><vh>Fixed many binding problems</vh></v>
<v t="ekr.20060116174906.185"><vh>Fixed extend-selection problems</vh></v>
<v t="ekr.20060116174906.187"><vh>Fixed per-pane bindings!</vh></v>
<v t="ekr.20060116174906.194"><vh>Always redraw the screen after editing a label</vh></v>
</v>
<v t="ekr.20060116174906.195"><vh>Code level changes</vh>
<v t="ekr.20060116174906.198"><vh>Removed g.top from Leo's core and all plugins</vh></v>
<v t="ekr.20060116174906.199"><vh>Created c.exists ivar and related logic</vh></v>
<v t="ekr.20060116174906.213"><vh>Call c.setLog in all entries into code</vh></v>
<v t="ekr.20060116174906.255"><vh>Generalized doCommand</vh></v>
</v>
<v t="ekr.20060116174906.258"><vh>New features</vh>
<v t="ekr.20060116174906.259"><vh>Installed many standard bindings to leoSettings.leo</vh></v>
<v t="ekr.20060116174906.262"><vh>Added Check Bindings script in leoSettings.leo</vh></v>
<v t="ekr.20060116174906.263"><vh>Scripts now maintain original focus</vh></v>
<v t="ekr.20060116174906.267"><vh>Added scroll-up/down-extend-selection commands</vh></v>
<v t="ekr.20060116174906.272"><vh>Improved cursor move/extend commands</vh></v>
<v t="ekr.20060116174906.296"><vh>Added support for @mode nodes</vh></v>
<v t="ekr.20060116174906.306"><vh>keyboard-quit restores default input mode</vh></v>
</v>
<v t="ekr.20060116174906.257"><vh>Added discusion to FAQ about when deleting a node is 'dangerous'</vh>
<v t="ekr.20060111192108"><vh>When is deleting a node dangerous?</vh></v>
</v>
</v>
<v t="ekr.20060206111508"><vh>4.4 beta 2</vh>
<v t="ekr.20060206111508.2"><vh>Bugs fixed</vh>
<v t="ekr.20060206111508.3"><vh>Fixed crasher in Save button</vh></v>
<v t="ekr.20060206111508.4"><vh>Fixed minor bugs &amp; made minor improvements</vh>
<v t="ekr.20060206111508.5"><vh>Fixed two annoying headline glitches</vh></v>
<v t="ekr.20060206111508.14"><vh>Insert headline didn't redraw headline properly in vim mode</vh></v>
<v t="ekr.20060206111508.40"><vh>Improved printBindings, printCommands &amp; modeHelp</vh></v>
</v>
<v t="ekr.20060206111508.48"><vh>Fixed crasher re BackSpace in log window</vh></v>
<v t="ekr.20060206111508.49"><vh>Fixed crashers in cut/copy/paste commands</vh></v>
<v t="ekr.20060206111508.54"><vh>Fixed crasher when clicking the close box during a long command</vh></v>
<v t="ekr.20060206111508.58"><vh>cloneFindAll now honor present find settings</vh></v>
<v t="ekr.20060206111508.63"><vh>Double-click didn't work in the body pane.</vh></v>
<v t="ekr.20060206111508.74"><vh>Improved body.makeInsertPointVisible</vh></v>
<v t="ekr.20060206111508.75"><vh>Fixed cut/copy/paste from menu</vh></v>
<v t="ekr.20060206111508.553"><vh>Fixed major blunder: tree.onHeadChanged sets focus only if there was a real change</vh></v>
<v t="ekr.20060206111508.97"><vh>Disabled plain-key bindings in insert/overwrite modes</vh></v>
<v t="ekr.20060206111508.103"><vh>Disabled auto-scrolling in outline pane on clicks</vh></v>
<v t="ekr.20060206111508.136"><vh>move-outline and find commands force a screen scroll</vh></v>
<v t="ekr.20060211104746.2"><vh>Fixed undo problem in headlines</vh></v>
<v t="ekr.20060214085054"><vh>Found the cause of 'sticking focus' problem</vh></v>
<v t="ekr.20060211104746.162"><vh>Fixed tree icon bug</vh></v>
<v t="ekr.20060211104746.177"><vh>Set remembered column properly in prev-line and next-line</vh></v>
<v t="ekr.20060211104746.208"><vh>Fixed focus problems in spell tab</vh></v>
<v t="ekr.20060214074035.9"><vh>Fixed problem with body_gmt_time setting</vh></v>
<v t="ekr.20060214074035.20"><vh>Made sure save updates the open directory</vh></v>
<v t="ekr.20060214074035.41"><vh>Fixed sort-lines problems</vh></v>
<v t="ekr.20060214074035.101"><vh>Fixed bug: paste outline lost headline editing</vh></v>
</v>
<v t="ekr.20060206111508.547"><vh>Code improvements</vh>
<v t="ekr.20060206111508.550"><vh>Removed code in c.begin/EndUpdate and c.endEditLabel that tried to save/restore focus</vh></v>
<v t="ekr.20060206111508.596"><vh>Improved tree allocation</vh></v>
<v t="ekr.20060211104746.12"><vh>Created c.masterFocusHandler</vh></v>
<v t="ekr.20060211104746.168"><vh>Added unit tests for key dicts</vh></v>
<v t="ekr.20060211104746.346"><vh>Special-cased commands for minibuffer</vh></v>
<v t="ekr.20060214074035.6"><vh>Made sure yield works with Python 2.2</vh></v>
<v t="ekr.20060214074035.12"><vh>Use os.getenv('User") if it exists to get initial cvs name</vh></v>
</v>
<v t="ekr.20060206112001"><vh>Improved commands</vh>
<v t="ekr.20060212102459.4"><vh>Minibuffer-oriented find commands</vh></v>
<v t="ekr.20060214074035.67"><vh>Leo remembers the previous open directory</vh></v>
</v>
<v t="ekr.20060214090742"><vh>Improved plugins</vh>
<v t="ekr.20060214074035.65"><vh>Fixed problem with view plugin</vh></v>
<v t="ekr.20060214074035.66"><vh>Installed cleo patch</vh></v>
</v>
<v t="ekr.20060214083808"><vh>New commands</vh>
<v t="ekr.20060212102459.4"><vh>Minibuffer-oriented find commands</vh></v>
</v>
<v t="ekr.20060214083647"><vh>New settings</vh></v>
<v t="ekr.20060214092741"><vh>User input modes</vh></v>
</v>
<v t="ekr.20060215112429"><vh>4.4 experimental 1</vh>
<v t="ekr.20060215112429.9"><vh>Fixed (maybe) problems with unicode characters &amp; caps lock</vh></v>
<v t="ekr.20060215112429.2"><vh>Restored some legacy bindings</vh></v>
<v t="ekr.20060215112429.3"><vh>Fixed crasher in Go To Line command</vh></v>
<v t="ekr.20060215112429.6"><vh>Fixed menu problem on Linux</vh></v>
</v>
<v t="ekr.20060217071505"><vh>4.4 a6</vh>
<v t="ekr.20060217071505.1"><vh>Fixed urgent compatibility problems</vh></v>
<v t="ekr.20060217072324"><vh>Minor bugs fixed</vh></v>
<v t="ekr.20060217072647"><vh>New debugging options in leoSettings.leo</vh></v>
</v>
<v t="ekr.20060227102028"><vh>4.4 a7</vh>
<v t="ekr.20060227102028.2"><vh>Bugs Fixed</vh>
<v t="ekr.20060227102028.3"><vh>Fixed binding bug</vh></v>
<v t="ekr.20060227102028.14"><vh>Fixed bug in open-find-dialog</vh></v>
<v t="ekr.20060227102028.15"><vh>Ensure dialogs properly get focus</vh></v>
<v t="ekr.20060227102028.16"><vh>Disabled autocompleter in headlines</vh></v>
<v t="ekr.20060227102028.17"><vh>Removed horrible g.app.dialogs hack</vh></v>
<v t="ekr.20060227102028.18"><vh>Fix crasher in plugin</vh></v>
</v>
<v t="ekr.20060227102028.111"><vh>Autocompletion and calltips</vh></v>
</v>
<v t="ekr.20060328171518"><vh>4.4 b3</vh>
<v t="ekr.20060328171518.1"><vh>New features</vh>
<v t="ekr.20060328171518.10"><vh>Added scroll outline pane commands</vh></v>
<v t="ekr.20060328171518.11"><vh>Improved registerCommand</vh></v>
<v t="ekr.20060328171518.15"><vh>Suppressed autocompletion after numbers</vh></v>
<v t="ekr.20060328171518.16"><vh>Added colorizing support for Lua language</vh></v>
<v t="ekr.20060328171518.45"><vh>Added run-unit-test command</vh></v>
</v>
<v t="ekr.20060328171518.47"><vh>Bugs</vh>
<v t="ekr.20060328171518.48"><vh>Fixed problem with left &amp; right arrows in outline mode</vh></v>
<v t="ekr.20060328171518.57"><vh>Fixed undo problem with clones</vh></v>
<v t="ekr.20060328171518.83"><vh>Investigated setting descendant @file nodes dirty when changing body text</vh></v>
<v t="ekr.20060328171518.85"><vh>Work around newline problems on the Mac</vh></v>
<v t="ekr.20060328171518.101"><vh>Got rid of settings messages</vh></v>
<v t="ekr.20060328171518.108"><vh>Clicks outside minibuffer no longer rip focus</vh></v>
<v t="ekr.20060328171518.111"><vh>Handled missing leoSettings.leo files more gracefully</vh></v>
<v t="ekr.20060328171518.119"><vh>Converted all shortcuts to unicode</vh></v>
<v t="ekr.20060328171518.135"><vh>Made Open With shortcuts work again</vh></v>
<v t="ekr.20060328171518.151"><vh>Made sure autocompleter and calltip text stick</vh></v>
<v t="ekr.20060328171518.152"><vh>Fixed a bug in c.openWith</vh></v>
<v t="ekr.20060328171518.169"><vh>Import/export commands now set directory for next open</vh></v>
<v t="ekr.20060328171518.190"><vh>Investigated colorizer problems: can not reproduce</vh></v>
<v t="ekr.20060328171518.248"><vh>Removed support @ifgui: it doesn't and can't work</vh></v>
<v t="ekr.20060328171518.249"><vh>Removed autocompletion for self</vh></v>
<v t="ekr.20060414071350.1"><vh>Rewrote g.importExtension to simplify startup logic</vh></v>
<v t="ekr.20060414071350.8"><vh>Removed calls to lstrip and rstrip for compatibility with Python 2.2.1</vh></v>
<v t="ekr.20060414071350.39"><vh>Fixed crash in string.startswith and string.endswith</vh></v>
<v t="ekr.20060414071350.47"><vh>Fixed Crash after undoing clearRecentFiles command</vh></v>
<v t="ekr.20060414071350.58"><vh>Fixed minor problems reported by Pychecker</vh></v>
</v>
<v t="ekr.20060328171518.191"><vh>Plugins</vh>
<v t="ekr.20060328171518.238"><vh>Changed path to stylesheet in the rst3 plugin</vh></v>
<v t="ekr.20060328171518.240"><vh>Fixed problems with chapters plugin</vh></v>
<v t="ekr.20060328171518.244"><vh>Improved groupoperations plugin</vh></v>
<v t="ekr.20060328171518.245"><vh>Fixed crasher in Word (and other) plugins</vh></v>
<v t="ekr.20060328171518.246"><vh>Fixed problem with labels plugin</vh></v>
</v>
</v>
<v t="ekr.20060417092536"><vh>4.4 b4</vh>
<v t="ekr.20060421070409.1"><vh>Bugs</vh>
<v t="ekr.20060421070602"><vh>Fixed rename-buffer command</vh></v>
<v t="ekr.20060421070409.2"><vh>Investigated problems with legacy bindings</vh></v>
<v t="ekr.20060421070409.3"><vh>Fixed bug when cutting text in headline</vh>
<v t="ekr.20060421070409.4"><vh>Report</vh></v>
</v>
<v t="ekr.20060421070409.9"><vh>Fixed crasher in open-find-dialog</vh>
<v t="ekr.20060421070409.10"><vh>Report</vh></v>
<v t="ekr.20060421070409.11"><vh>Traceback</vh></v>
</v>
<v t="ekr.20060421070409.33"><vh>Don't do typing completion for numbers</vh></v>
<v t="ekr.20060421070409.36"><vh>Fixed crash in undo</vh></v>
</v>
<v t="ekr.20060421070409.37"><vh>New features</vh>
<v t="ekr.20060417092825.1"><vh>Added script to update new copies of leoSettting.leo from previous copies</vh></v>
<v t="ekr.20060421070409.41"><vh>Added new commands</vh></v>
<v t="ekr.20060421070409.40"><vh>Made all edit command undoable</vh></v>
</v>
</v>
<v t="ekr.20060428084553"><vh>4.4 rc1</vh>
<v t="ekr.20060428084553.2"><vh>Bugs</vh>
<v t="ekr.20060428084957"><vh>Fixed rename-buffer command</vh></v>
<v t="ekr.20060428084553.4"><vh>Fixed bug when cutting text in headline</vh></v>
<v t="ekr.20060428084553.10"><vh>Fixed crasher in open-find-dialog</vh></v>
<v t="ekr.20060428084553.34"><vh>Suppressed typing completion for numbers</vh></v>
<v t="ekr.20060428084553.37"><vh>Fixed crash in undo</vh></v>
<v t="ekr.20060428084711"><vh>Fixed crash in datenodes plugin</vh></v>
</v>
<v t="ekr.20060428084553.38"><vh>New features</vh>
<v t="ekr.20060428084553.39"><vh>Added clear-selection command</vh></v>
<v t="ekr.20060428084553.41"><vh>Made all edit command undoable</vh></v>
<v t="ekr.20060428084553.42"><vh>Added new commands</vh></v>
<v t="ekr.20060428084553.273"><vh>Added filename completion</vh></v>
</v>
</v>
<v t="ekr.20060511074853"><vh>4.4 final</vh></v>
</v>
<v t="ekr.20060822140418"><vh>4.4.1...</vh>
<v t="ekr.20060830141224"><vh>4.4.1 final</vh>
<v t="ekr.20060830141224.2"><vh>Removed warning about changed nodes</vh></v>
<v t="ekr.20060830141224.13"><vh>Bugs fixed</vh>
<v t="ekr.20060830141224.14"><vh>Fixed serious bug in Paste Node as Clone</vh>
<v t="ekr.20060830141224.15"><vh>Report</vh></v>
<v t="ekr.20060830141224.16"><vh>What I did</vh></v>
</v>
<v t="ekr.20060830141224.37"><vh>Fixed minor .leoID.txt bug</vh>
<v t="ekr.20060830141224.38"><vh>Report</vh></v>
</v>
<v t="ekr.20060830141224.45"><vh>Improved speed of unmark-all and corresponding undo/redo</vh>
<v t="ekr.20060830141224.46"><vh>Report</vh></v>
</v>
</v>
</v>
<v t="ekr.20060822140418.1"><vh>4.4.1 b4</vh>
<v t="ekr.20060822140418.3"><vh>Bugs fixed</vh>
<v t="ekr.20060822140418.4"><vh>Added bindings to text panes for show-font command</vh></v>
<v t="ekr.20060822140418.26"><vh>Fixed kill-line, kill-word, kill-sentence, etc</vh></v>
<v t="ekr.20060822140418.29"><vh>Fixed minor scrolling problem</vh></v>
<v t="ekr.20060822140418.36"><vh>Fixed bug in backward-kill-word</vh></v>
<v t="ekr.20060822140418.39"><vh>Fixed unicode bug in forward-word and backward-word commands</vh></v>
<v t="ekr.20060822140418.41"><vh>Fixed problem setting body background color</vh></v>
<v t="ekr.20060822140418.49"><vh>Disabled incremental colorizing in new colorizer when there are multiple editors</vh></v>
<v t="ekr.20060822140418.97"><vh>Removed component classes</vh></v>
</v>
<v t="ekr.20060822140418.69"><vh>New features</vh>
<v t="ekr.20060822140418.76"><vh>Added scroll-outline-left/right commands</vh></v>
<v t="ekr.20060822140418.77"><vh>Generalized bracket flasher</vh></v>
<v t="ekr.20060822140418.88"><vh>Leo *already* supports Python decorators</vh></v>
<v t="ekr.20060822140418.92"><vh>Wrote script to convert g.es to g.et where appropriate</vh></v>
<v t="ekr.20060822140418.70"><vh>Created menu font settings</vh></v>
</v>
</v>
<v t="ekr.20060601101643"><vh>4.4.1 b1</vh>
<v t="ekr.20060601101958.1"><vh>Fixed bugs</vh>
<v t="ekr.20060601101958.56"><vh>The Open Python Window command runs Idle in a separate process</vh></v>
<v t="ekr.20060601101958.2"><vh>Fixed crasher in searchbox plugin</vh></v>
<v t="ekr.20060601101958.6"><vh>Fixed binding problems in leoSettings.leo reported by Check bindings script.</vh></v>
<v t="ekr.20060601101958.13"><vh>Fixed crasher in macros plugin</vh></v>
<v t="ekr.20060601101958.14"><vh>Fixed crasher in  UNL plugin</vh></v>
<v t="ekr.20060601101958.16"><vh>Suppressed traceback in g.callers when the call stack isn't deep enough</vh></v>
<v t="ekr.20060603082009"><vh>Fixed long-standing bug involving @comment and @language</vh></v>
</v>
<v t="ekr.20060601102802"><vh>New features, commands &amp; plugins</vh>
<v t="ekr.20060601101958.245"><vh>Support for multiple editors in the body pane</vh></v>
<v t="ekr.20060601101958.70"><vh>Improved searches</vh></v>
<v t="ekr.20060601101958.52"><vh>Added debug command</vh></v>
<v t="ekr.20060601101958.58"><vh>Added Debug button to scripting plugin</vh></v>
<v t="ekr.20060603072938"><vh>Added python-help command</vh></v>
<v t="ekr.20060601101958.277"><vh>Added toggle-invisibles and hide-invisibles commands</vh></v>
<v t="ekr.20060601101958.172"><vh>Added run-unit-test command</vh></v>
<v t="ekr.20060601101958.234"><vh>The help-for-command command now works for almost all commands</vh></v>
<v t="ekr.20060603081537"><vh>Added shortcut_button plugin</vh></v>
</v>
<v t="ekr.20060601102802.2"><vh>New and improved settings</vh>
<v t="ekr.20060601101958.174"><vh>Added @bool idle_redraw setting</vh></v>
<v t="ekr.20060601101958.264"><vh>Added autoindent_in_nocolor_mode setting</vh></v>
<v t="ekr.20060601101958.244"><vh>Added warnings about the expanded_click_area setting</vh></v>
<v t="ekr.20060601101958.276"><vh>Removed support for @shortcut (@shortcuts remains)</vh></v>
</v>
<v t="ekr.20060601101958.28"><vh>Minor improvements</vh>
<v t="ekr.20060601101958.218"><vh>Finished Cmds menu</vh></v>
<v t="ekr.20060601101958.235"><vh>Improved show-fonts command</vh></v>
<v t="ekr.20060601101958.238"><vh>Strip quotes from color, font settings.</vh></v>
<v t="ekr.20060601101958.239"><vh>Warn about invalid Enter and Leave key bindings</vh></v>
</v>
</v>
<v t="ekr.20060620094645"><vh>4.4.1 b2</vh>
<v t="ekr.20060620094645.34"><vh>Bugs fixed</vh>
<v t="ekr.20060620094645.35"><vh>Made sure calltip always adds '('</vh></v>
<v t="ekr.20060620094645.43"><vh>word matches now succeed if first character of the pattern is not in word-chars.</vh></v>
<v t="ekr.20060620094645.44"><vh>Dialogs now bring the Leo window back to the front</vh></v>
<v t="ekr.20060620094645.45"><vh>Fixed unit test: ensure that body gets focus after ending editing</vh></v>
<v t="ekr.20060620094645.46"><vh>Remember scrolling postion, insert point and selection range in multiple editors</vh></v>
<v t="ekr.20060620094645.50"><vh>Fix crasher in kill-region command</vh></v>
<v t="ekr.20060620094645.52"><vh>Fixed bug: cycle-editor hung Leo</vh></v>
<v t="ekr.20060620094645.64"><vh>Fixed crasher in init code</vh></v>
<v t="ekr.20060620094645.68"><vh>use g.stripBrackets instead of lstrip and rstrip</vh></v>
<v t="ekr.20060620094645.76"><vh>Restore cursor when changing focus in editors</vh></v>
<v t="ekr.20060620094645.77"><vh>Undo restores focus again</vh></v>
<v t="ekr.20060622130815"><vh>Updated row/col indicators when using arrow keys</vh></v>
<v t="ekr.20060622130815.3"><vh>Fixed show-invisibles crasher</vh></v>
</v>
<v t="ekr.20060620094645.78"><vh>Code level</vh>
<v t="ekr.20060620094645.79"><vh>Simplified gui bindings</vh></v>
<v t="ekr.20060622130815.9"><vh>Created g.makeScriptButton</vh></v>
</v>
<v t="ekr.20060620094645.85"><vh>New &amp; improved features</vh>
<v t="ekr.20060620094645.86"><vh>Improved filename completion</vh></v>
<v t="ekr.20060620094645.96"><vh>Added support for --&gt; command-name in @mode nodes</vh></v>
<v t="ekr.20060620094645.97"><vh>Better listings for print-commands and print-bindings &amp; mode-help commands</vh></v>
<v t="ekr.20060620094645.103"><vh>Fixed find-character &amp; find-word commands</vh></v>
<v t="ekr.20060620094645.106"><vh>Better printing of bindings (period -&gt; .) etc</vh></v>
<v t="ekr.20060620094645.107"><vh>Added support for !command, !insert and !overwrite bindings</vh></v>
<v t="ekr.20060620094645.108"><vh>Improved check bindings script in leoSettings.leo</vh></v>
<v t="ekr.20060620094645.109"><vh>Improved isearch &amp; added isearch-with-present-options command</vh></v>
<v t="ekr.20060620094645.194"><vh>Use last shortcut defined</vh></v>
<v t="ekr.20060620094645.225"><vh>selfInsertCommand sets the column used by up/down arrows</vh></v>
<v t="ekr.20060620094645.231"><vh>Added toggle-autocompleter and toggle-calltips commands</vh></v>
<v t="ekr.20060620094645.232"><vh>Script buttons now create press-xxx-button commands</vh></v>
<v t="ekr.20060620094645.233"><vh>print-bindings command now properly sorts bindings</vh></v>
<v t="ekr.20060620094645.234"><vh>Allow @shortcuts bindings to apply to press-xxx-commands</vh></v>
<v t="ekr.20060620094645.242"><vh>Added support for @abbrev nodes in leoSettings.leo</vh></v>
<v t="ekr.20060620094645.243"><vh>Created open-users-guide command</vh></v>
<v t="ekr.20060620094645.252"><vh>scroll-up/down commands now scroll the outline if focus is in outline pane</vh></v>
<v t="ekr.20060620094645.258"><vh>Cycle-focus command cycles through tabs and editors</vh></v>
<v t="ekr.20060620094645.286"><vh>Allow @mode outside of leoSettings.leo</vh></v>
<v t="ekr.20060622130553"><vh>Added section about upgrading settings</vh></v>
<v t="ekr.20060622130553.2"><vh>Documented how to turn @buttons into plugins</vh></v>
</v>
<v t="ekr.20060620094645.302"><vh>Plugins</vh>
<v t="ekr.20060620094645.303"><vh>Added doc-only option to rst3</vh></v>
<v t="ekr.20060620094645.304"><vh>Fixed bug in rst doc_only_mode</vh></v>
<v t="ekr.20060620094645.305"><vh>Support show_headlines options in doc-only mode in rst3 plugin</vh></v>
<v t="ekr.20060620094645.306"><vh>Fixed bug in UNL plugin</vh></v>
<v t="ekr.20060620094645.307"><vh>Improved image plugin</vh></v>
<v t="ekr.20060620094645.308"><vh>Fixed path problem with rst3 plugin</vh></v>
<v t="ekr.20060620094645.309"><vh>Fixed crashers in scheduler plugin</vh></v>
</v>
<v t="ekr.20060622132524"><vh>Settings</vh>
<v t="ekr.20060620094645.299"><vh>Added editor_orientation setting</vh></v>
</v>
</v>
<v t="ekr.20060629083400.1"><vh>4.4.1 b3</vh>
<v t="ekr.20060629083935.2"><vh>Bugs fixed</vh>
<v t="ekr.20060629083935.3"><vh>Fixed recent bug: Ctrl-g does not work in @mode nodes</vh></v>
<v t="ekr.20060629083935.8"><vh>Update column display when typing</vh></v>
<v t="ekr.20060629083935.15"><vh>Fixed long-standing problem reporting indentation errors</vh></v>
<v t="ekr.20060629083935.25"><vh>Fixed long-standing bug in Remove Sentinels command</vh></v>
<v t="ekr.20060629083935.32"><vh>Fixed long-standing bugs in import code</vh></v>
<v t="ekr.20060629083935.61"><vh>Overwrite mode now works in headllines</vh></v>
<v t="ekr.20060629083935.70"><vh>Fixed crasher in masterCommand</vh></v>
<v t="ekr.20060629083935.71"><vh>Improved view-lossage command</vh></v>
</v>
<v t="ekr.20060629083935.74"><vh>New features</vh>
<v t="ekr.20060629083935.75"><vh>Finished repeat-complex-command</vh></v>
<v t="ekr.20060629083935.76"><vh>Read leoSettings.leo from the directory containing the .leo file</vh></v>
<v t="ekr.20060629083935.93"><vh>Flash matching parens &amp; corresponding settings</vh></v>
</v>
<v t="ekr.20060629083935.96"><vh>New settings</vh>
<v t="ekr.20060629083935.97"><vh>Added standard bindings for Ctrl-y (yank) and Ctrl-k (kill-line)</vh></v>
<v t="ekr.20060629083935.98"><vh>Added @bool warn_about_redefined_shortcuts setting</vh></v>
<v t="ekr.20060629083935.99"><vh>Added @bool trace_bind_key_exceptions setting</vh></v>
<v t="ekr.20060629083935.100"><vh>Added bracket flash settings</vh></v>
</v>
</v>
<v t="ekr.20060903102158"><vh>4.4.1.1 final</vh></v>
</v>
</v>
<v t="edream.110203163054.63" a="E"><vh>Latest version</vh>
<v t="ekr.20060928172040"><vh>4.4.2 beta 1</vh>
<v t="ekr.20060928172525.81"><vh>The 'big reorg':  vnode, tnode and position classes are independent of the rest of Leo</vh></v>
<v t="ekr.20060928195040"><vh>New features</vh>
<v t="ekr.20060928194633.1"><vh>myLeoSettings.leo</vh></v>
<v t="ekr.20060928172525.195"><vh>Created simple support for ZODB databases</vh>
<v t="ekr.20060928172525.197"><vh>Scripting using zodb</vh></v>
</v>
<v t="ekr.20060928172525.172"><vh>Improved help-for-command</vh></v>
<v t="ekr.20060928172525.180"><vh>Improved  quick-find commands</vh></v>
<v t="ekr.20060928172525.198"><vh>Improved how Leo works w/o the mousre</vh></v>
<v t="ekr.20060928172525.237"><vh>Increased speed of arrow keys</vh></v>
<v t="ekr.20060928172525.240"><vh>Find command now collapses nodes during searches</vh></v>
<v t="ekr.20060928172525.252"><vh>Added support  -- comments in @url nodes</vh></v>
<v t="ekr.20060928172525.167"><vh>Added many new commands to Cmds menu</vh></v>
</v>
<v t="ekr.20060928195040.1"><vh>New plugins</vh></v>
</v>
</v>
</v>
</vnodes>
<tnodes>
<t tx="EKR.20040518070558">Leo 4.2 alpha 2           May 18, 2004

This is an important milestone in Leo's history; the two defining features of the 4.2 code base are complete:

1. This is the first stable version using the "shared nodes" code base.

Shared nodes dramatically improve the time needed to insert, delete, and move nodes.  Moreover, the new code base is code compatible with the old.  Indeed, much of Leo still uses the old code base.  See Chapter 7 for full details of how to script Leo with the 4.2 code base.

2. This is the first version to use @file-thin for most derived files.

@file-thin makes it possible to use Leo effectively in a cvs environment.  Indeed, cvs now contains only a "dummy" version of LeoPy.leo.  The idea is that:

- LeoPyRef.leo hardly ever changes.  Developers will download LeoPyRef.leo once from cvs, then rename LeoPyRef.leo to be LeoPy.leo.  LeoPy.leo is private to each developer.

- Developers will commit and update to cvs only thin derived files.  There is no longer any need to keep .leo files and the files derived from them "in synch".

- Similar remarks apply to LeoPlugins.leo.  Cvs contains only LeoPluginsRef.leo, and contributors will need only to submit thin derived files.

I have been using the new code base without incident for weeks now, and I am fairly confident that it is safe to use.  Nevertheless, I would suggest routine caution when dealing with this version until more people have tested it.

Known bugs

- Cutting and pasting an @file-thin node does not work properly.  This will be easy to fix, I think.

- The present algorithm for reading thin derived files probably does not handle properly the situation in which a named node is some kind of grand child of the referencing node rather than being an immediate child of the referencing node.  This is a rare situation, easily avoided, and it doesn't happen at all in LeoPy.leo.  Nevertheless, something must be done.

Other improvements:

- Fixed a number of problems with using Leo on MacOS X.  In particular, Leo now uses the clover key as is usual on the Mac.  More Mac and *nix specific improvements are coming.

Still to do:

- Perfect import and @import.
- Make the Go To Line Number command work with @file-thin files.
- Fix minor bugs and add new features
  See the "To Do: 4.2" node in the leoToDo.txt node in LeoPy.leo.</t>
<t tx="EKR.20040518070824"></t>
<t tx="EKR.20040518070824.1">- Moved call to assignFileIndices into write_Leo_file.
- Called assignFileIndices in writeAtFileNodes, writeDirtyAtFileNodes, writeMissingAtFileNodes</t>
<t tx="EKR.20040518070940"></t>
<t tx="EKR.20040518070940.5">What I did:

File format

Added -thin field to @+leo sentinel

Recognizers

- Added vnode recognizers for @file-thin option.
- Added position proxies for vnode recognizers.

Directives &amp; sentinels
- Added support for @all.

Writing

- Added top-level atFile code to write @file-thin tree.
- DO write @file-thin vnodes if there was an error writing the derived file.
	- No autosave for @file-thin.
 	- Leo writes @file nodes first, so this is not a problem.
	- putVnode checks orphan bit, which gets set if there was an error.
- Don't write vnodes (or related tnodes) for @file-thin trees. (fileCommands).
- Do write empty nodes in @thin trees.
- Don't generate close node sentinels until all children have been generated.

Reading

- Set at.thinFile when reading thin files.
- Suppressed changed message and related items for thin files.
- Modified scanText4 and allies to read thin derived files.
	- Don't look for tnodeList for thin files.
	- Initially, at.lastThinNode is at.root.v
	- readStartNode calls createThinChild
	- createThinChild makes a child of at.lastThinNode if needed and sets at.lastThinNode.
- Updated fc.tnodesDict in at.createThinChild.
	Otherwise clones existing only in two thin files won't be linked properly.</t>
<t tx="EKR.20040518070940.156">After a match, the find-next command searched only in the suboutline where the first match occurred.
To fix this, we call g.app.findFrame.handleUserClick in various Tk event handlers.</t>
<t tx="EKR.20040518070940.164">@nocolor


p.v.t.visitedBit was used for two purposes:

- To mark the nodes to be written.
- To mark nodes that are not orphan.

What I did:

- Added t.is/set/clearWriteBit.
- Call t.setWriteBit in putVnode unless we are in a thin node.
- putTnodes tests for t.writeBit rather than t.visitedBit.</t>
<t tx="EKR.20040518071415">Leo did not handle moving a node to the root position of the outline correctly.</t>
<t tx="EKR.20040518075457">Using @ignore with @file-thin is asking for trouble.
If you remove the @ignore and then save, you will lose data.

How to recover the data:
	- Read Outline.
	- Remove @ignore
	- Import derived file... </t>
<t tx="EKR.20040524104904.48">Leo supports unlimited undo for all typing and all commands. The
'undo_granularity' setting controls the granularity of undo. There are four
possible values:

``node``
    Starts a new undo unit when typing moves to a new node.

``line`` (default)
    Starts a new undo unit when typing moves to new line.

``word``
    Starts a new undo unit when typing starts a new word.

``char`` (not recommended)
    Starts a new undo unit for each character typed.
    This wastes lots of computer memory.

``setUndoTypingParams`` calls ``recognizeStartOfTypingWord`` to recognize the
start of words. Plugins can modify ``recognizeStartOfTypingWord``. It should
return ``True`` if the typing indicated by the params starts a new 'word' for the
purposes of undo with 'word' granularity. ``setUndoTypingParams`` calls this
method only when the typing could possibly continue a previous word. In other
words, undo will work safely regardless of the value returned. See the actual
code for ``recognizeStartOfTypingWord`` for more details.</t>
<t tx="EKR.20040524104904.92">An @asis tree is a tree whose root headline starts with @asis &lt;filename&gt;.  Similarly, for @noref and @nosent trees.

New in 4.2:  The following terms are equivalent.  The first form is preferred in each case.

@asis, @file-asis, @silent
@nosent, @file-nosent and @nosentinelsfile
@noref, @file-noref and @rawfile

You can get any combination of sentinels/no sentinels and references/no references using @file, @nosent, @noref and @asis trees:

                 Derived files        Sections and 
Type of tree   contain sentinels?   @others expanded?
------------   ------------------   -----------------
       @asis   no                   no
       @file   yes                  yes
      @noref   yes                  no
     @nosent   no                   yes
     
       

Leo can not update the outline from changes made from derived files unless those files contain sentinels.  The primary source for @nosent and @asis trees are the outlines from which those files were derived.

Leo creates files derived from @noref and @asis trees by writing the body text of all nodes of the tree in outline order.  Leo writes the body text _as is_, without recognizing section definitions, without expanding section references, and without treating directives specially in any way.  In particular, Leo copies all directives, including @space or @c directives, to the derived file as text. However, Leo recognizes the @ignore directive in the _ancestors_ of @noref or @asis nodes, so you may use the @ignore directive as usual to prevent Leo from writing @rawfile and @silentfile trees.

Notes:

1. When writing @noref trees, Leo writes only the @+leo, @-leo, @+node, @-node, @+body and @-body sentinels.

2. Within @asis trees only, if a headline starts with @@, Leo writes everything in the headline following the @@ just before the corresponding body text.

3. Files derived from @asis trees contain _nothing_ not contained in body text (or @@ headlines).  In particular, if body text does not end in a newline, the first line from the next node will concatenated to the last line of the preceding node.</t>
<t tx="EKR.20040524104904.242">Leo reads and writes "foreign" attributes in ``&lt;v&gt;`` and ``&lt;t&gt;`` elements in .leo files as follows:

- When reading a .leo file, Leo will create ``t.unknownAttributes`` or ``v.unknownAttributes`` ivars for
  any ``tnode`` or ``vnode`` whose corresponding ``&lt;v&gt;`` or ``&lt;t&gt;`` element in the .leo file contains a foreign attribute.

- The ``unknownAttributes`` ivars are dictionaries whose keys are the attribute names and whose values are strings.

- When writing a file, Leo will write "foreign" attributes if a ``vnode`` or ``tnode`` contains an ``unknownAttributes`` ivar.

- The only native attribute of ``&lt;t&gt;`` elements is ``tx``.

- The native attributes of ``&lt;v&gt;`` elements are ``a``, ``t``, ``vtag`` and ``tnodeList``.

- The native attributes of ``&lt;v&gt;`` elements are ``marks``, ``expanded`` and ``descendentTnodeUnknownAttributes``.

- Non-native attributes are called **foreign** attributes.

- Leo performs the usual xml escapes on these strings when reading or writing the ``unknownAttributes`` ivars.

Plugins may cause Leo to write such foreign attributes simply by attaching unknownAttributes ivars to a vnode or tnode.
Like this::

	if hasattr(v,"unknownAttributes"):
		v.unknownAttributes ["vnodeIcon"] = pathToIcon
	else:
		v.unknownAttributes = {"vnodeIcon" : pathToIcon}

See the section called "Recommended conventions for plugins" for advice about
how to avoid potential conflicts in naming new attributes.

All members of these dictionaries should be "pickleable". That is, Leo uses
Python's Pickle module to encode all values in these dictionaries. Leo will
discard any attributes that can not be pickled. This should not be a major
problem to plugins. For example, instead of putting a tnode into these
dictionaries, a plugin could put the tnode's gnx (a string) in the dictionary.

Leo writes only ``t.unknownAttributes`` when writing ``@thin`` trees to the .leo
file. Leo puts (the encoding of) these elements into an attribute called
``descendentTnodeUnknownAttributes``. This attribute is part of the ``&lt;v&gt;``
element representing the ``@thin`` node. Leo does _not_ write
``v.unknownAttributes`` in ``@thin`` trees because *only tnodes have gnx's in
thin derived files*. In effect, vnodes are anonymous. We could attempt to get
around this by identifying vnodes by their corresponding tnodes, but that's not
a general solution and it is, in effect, equivalent to writing only
``t.unknownAttributes``. So it seems pointless to "pretend" to be writing
``v.unknownAttributes``.

The effect of this is to make all vnodes identical, as far as using
unknownAttributes is concerned. This won't work in all cases. For example, a
plugin that creates an arbitrary directed graph between vnodes must distinguish
between joined vnodes. In that case, the plugin should confine itself to @file
trees, or just vnodes in .leo files, for that matter.</t>
<t tx="EKR.20040601084317">Leo 4.2 alpha 3           June 1, 2004

This version fixes completes the essential features of version 4.2.  All known incompletions and bugs involving shared nodes and Leo's new file format have been fixed.  BTW, this version of Leo completes Leaps 201 and 202.

It should be safe to use this version for collaboration between Leo's developers.  I hereby encourage people to start using cvs for collaboration.  Only by doing so will we discover any possible problems.

The only item that must be completed before releasing 4.2 beta is fixing the Go To Line Number command so it supports thin derived files.

There are many known bugs in this version: most are minor bugs that have been around for a long time.  All known bugs will be fixed by the first release candidate.  See the to-do list in LeoPy.leo for the complete list.

The highlights of this version:

- All features of @file-thin are now complete and appear to be stable.
	- All .leo files in the distribution use @thin files where possible.
	- Leo ignores all directives within the range of the @all directive.
	- The @+middle and @-middle sentinels allow sections to be defined in any descendant node.
	- The @clone sentinel marks duplicate cloned siblings.
- The beginnings of a new undo scheme are in place.
- @thin, @nosent, @noref and @asis are abbreviations for @file-thin, @file-nosent, @file-noref and @file-asis.
- Created new iterators that return lists of vnodes and tnodes, including iterators that remove all duplicates from those lists.</t>
<t tx="EKR.20040601084317.2"></t>
<t tx="EKR.20040601084317.99">This happened after write errors such as orphan nodes.</t>
<t tx="EKR.20040601084317.102">Added u.registerUndoHandlers.

This will become largely unnecessary in the new undo scheme.  It's good to have though.</t>
<t tx="EKR.20040601084317.142">When writing .leo files Leo now pickle's and hexlify's all data in the v.unknownAttribute and t.unknownAttribute dictionaries.  When reading .leo files Leo does the reverse.

Leo ignores all elements in these dictionaries if some element can not be pickled.</t>
<t tx="EKR.20040601084317.161">I have fallen madly in love with generators.  The following new iterators are defined with generators.

c.all_positions_iter
c.all_tnodes_iter
c.all_vnodes_iter
c.all_unique_tnodes_iter
c.all_unique_vnodes_iter

p.tnodes_iter
p.vnodes_iter
p.unique_tnodes_iter
p.unique_vnodes_iter

v.self_and__subtree_iter
v.self_and_unique_subtree_iter</t>
<t tx="EKR.20040601101118">If the copied node was an @thin or @file-thin node node only the root node was copied.</t>
<t tx="EKR.20040601101227"></t>
<t tx="EKR.20040601101227.1"></t>
<t tx="EKR.20040601101430">This bug exists in 4.1 final.  Leo did not properly show the found text in headlines.  The fix was in the code that redraws the screen, not in the find/change code itself.</t>
<t tx="EKR.20040601101430.1"></t>
<t tx="EKR.20040601101510"></t>
<t tx="EKR.20040601101547"></t>
<t tx="EKR.20040601102115"></t>
<t tx="EKR.20040601102703">The new scheme simply saves all information in one or more vnodes and their associated tnodes.  This is a general scheme that can be used by almost any command.

At present only the u.saveTree method exists.  Coming soon, u.saveNode, u.saveNodeAndChildren and u.saveListOfNodes.</t>
<t tx="EKR.20040601102808">See the to-do list in LeoPy.leo for a list of known bugs in this version.

None of these bugs is serious:  I consider this version to be suitable for day-to-day work.</t>
<t tx="EKR.20040628095213">Leo 4.2 beta 2           July 5, 2004
Leo 4.2 beta 1           June 30, 2004

The highlights of 4.2 beta 2:

- Leo now writes the entire contents of @ignore'd @thin trees to the .leo file.
This change ensures that users can create and remove @ignore directives without
any chance of losing data inadvertently.

- Leo now saves and restores marks and the expansion state of nodes in @thin trees.

- Leo marks @thin nodes as dirty whenever they become "newly unignored", i.e.,
when an @thin node no longer falls in the range of an @ignore directive.

Beta 1 completes all fundamental work in the 4.2 code base. All essential code
is complete. Dozens of bugs have been fixed since the Alpha 3 release about a
month ago.

Known bugs in 4.2 beta 2:

- Not all plugins work correctly.
- Some plugins leak memory very slightly.

The highlights of Leo 4.2:

- @thin trees make Leo much more friendly to cvs. Files derived from @thin can
be committed to cvs and updated from cvs without having to commit or update the
corresponding .leo file. There is no longer any need to keep .leo files and
derived files in synch.

- Leo's data structures have been reorganized. As a result, all outline
operations are much faster. To support this organization, scripts that traverse
Leo's data structures must now use a positions rather than vnodes. Old scripts
that appear to use vnodes will still work because methods like c.currentVnode
that appear to return vnodes actually return positions.

Other features of 4.2:

- Leo is now much more friendly to using spaces instead of tabs.
- The Execute Script command reports erroneous lines more clearly.
- The usual assortment of bug features and minor features.

Coming soon in 4.2:

- Perfect Import will guarantee that Leo imports file perfectly.
- @import will allow you to study files using Leo without changing those files.</t>
<t tx="EKR.20040628095213.3">@nocolor

- Leo calls g.enableIdleTimeHook at end of startup code.
	- This means that g.idleTimeHookHandler gets called periodically, even if no hooks have been defined.
	- g.enableIdleTime hook now calls g.app.gui.setIdleTimeHook at most once.

- app.forceShutdown now calls "end1" hook before calling app.finishQuit.
	- This ensures that the "end1" hook always gets called once.
	- app.finishQuit calls doHook("end1",...) only if it hasn't been called before.
		- This isn't necessary, but it makes traces in doHook less confusing.

- idleTimeHookHandler now calls the idle-time hook for all open windows.
	- So having multiple windows open should not affect idle-time hooks.

** Warning: new convention required to workaround apparent Tk problems.
	- "idle" hooks should return if g.app.killed is True.</t>
<t tx="EKR.20040628095213.23">@color

Added the following hooks:

tag argument                                               keys in keywords
(hook name)           overrides    when called           dictionary argument
---------             ---------    -----------           -------------------

"draw-outline-box"       yes   start of drawBox          tree,p,v,x,y (note 6)
"draw-outline-icon"      yes   start of tree.drawIcon    tree,p,v,x,y (note 6)
"draw-outline-node"      yes   start of tree.drawNode    tree,p,v,x,y (note 6)
"draw-outline-text-box"  yes   start of tree.drawText    tree,p,v,x,y (note 6)
"draw-sub-outline"       yes   start of tree.drawTree    tree,p,v,x,y,h,level,hoistFlag (note 6)</t>
<t tx="EKR.20040628095213.52"></t>
<t tx="EKR.20040628095213.56"></t>
<t tx="EKR.20040628095213.60">Added support for RapidQ, css, shell scripts and PHP.</t>
<t tx="EKR.20040628095213.109">http://sourceforge.net/forum/message.php?msg_id=2429098
By: nobody

The Leo icon can eliminate the need for the word Leo.

What I did:

- Eliminate Leo in name of Find panel.
- Derived leoTkinterPrefs from leoTkinterDialog: creates icon.
- Derived leoComparePanel from leoTkinterDialog: creates icon.
- Eliminated the -t option when opening Idle: the idle window is now called "Python Shell"</t>
<t tx="EKR.20040628095213.110">- Added @language html when importing ".htm" and ".html" files.
- Added @nocolor when importing ".txt" and ".text" files
</t>
<t tx="EKR.20040628095213.113">When in headline, the Select All command selected the body text.</t>
<t tx="EKR.20040628095213.121">- idle_body_key must call g.scanDirectives in order to support @tab_width.
	- This must be done for tabs and newlines.

- Fixed bug in g.scanDirectives that was rejecting negative tabwidth values.
	- This bug did not exist in the other versions of scanDirectives.

- With a negative tabwidth, a backspace now computes what spaces are equivalent to a tab and delete all of those.  This is easy to do!
</t>
<t tx="EKR.20040628095213.143"></t>
<t tx="EKR.20040628095213.160"></t>
<t tx="EKR.20040628095213.192"></t>
<t tx="EKR.20040628095213.197">doc\leoUsersGuide.txt
doc\leoFAQ.txt
doc\leoLeaps.txt</t>
<t tx="EKR.20040628095213.198">The old code used at c.tab_width.  It should also look for @tabwidth directives.

This was not good when @tabwidth -4 was in effect.</t>
<t tx="EKR.20040628095213.202">atFile.scanHeader was not handling -encoding fields properly.</t>
<t tx="EKR.20040628095213.213"></t>
<t tx="EKR.20040628095213.225"></t>
<t tx="EKR.20040628095213.246"># namespace not handled very well.</t>
<t tx="EKR.20040628095213.264"></t>
<t tx="EKR.20040628095213.269"></t>
<t tx="EKR.20040628095213.279">I inserted "import time", and while I was at it I improved the error checking.</t>
<t tx="EKR.20040628095213.282">- By default, finishPaste command reassigns all indices in copied nodes.
- Created pasteOutlineRetainingClones.
- Added reassignIndices arg to pasteOutline, getLeoOutline and finishPaste.
- Added &lt;&lt; recreate tnodesDict &gt;&gt; in getLeoOutline.
- Simplified getTnode slightly: the "if t" code is the same for both kinds of reads.</t>
<t tx="EKR.20040628095213.297">The code now limits what can be pasted to a maximum of one line or a about 250 characters.</t>
<t tx="EKR.20040628095213.308"></t>
<t tx="EKR.20040628095213.311">@nocolor

- Leo now uses True and False everywhere instead of true and false.

- All of Leo's code uses spaces instead of tabs for indentation.</t>
<t tx="EKR.20040628095213.312"></t>
<t tx="EKR.20040628095213.314"></t>
<t tx="EKR.20040628095213.324">- Set removeTrailing to True unless ch is a newline.

This allows Alt-f to work properly.

- Return "break" after the "final" text has been computed if nothing has changed.

This suppresses spurious newlines.

A new idea:  Make sure the text _does_ have a newline at all times.  I'm not sure this will work...

- ALWAYS set the text in select.  This prevents some weird problems with trailing newlines.</t>
<t tx="EKR.20040628095213.334">- The string passed to exec now includes sentinels.

goToLineNumber needs sentinels to work properly.

- es_exception now gets the error line number from the traceback.

- Added new keyword arguments to goToLineNumber.

- Created goToScriptLineNumber, which just calls goToLineNumber.</t>
<t tx="EKR.20040628095213.346">Hitting return in middle of a headline didn't work.</t>
<t tx="EKR.20040628095213.348"></t>
<t tx="EKR.20040628095213.354"></t>
<t tx="EKR.20040628095213.366"></t>
<t tx="EKR.20040628095213.368"></t>
<t tx="EKR.20040628095213.377">Changed getVnode so it checks for v = None after calling getExistingVnode.  Creating the node seems to work in this case: I wouldn't bet my life that it works in all cases.</t>
<t tx="EKR.20040628095213.391">- Added toString to most write methods.
- Retained scriptFile option for compatibility with plugins.</t>
<t tx="EKR.20040628095213.404"></t>
<t tx="EKR.20040628095213.407"></t>
<t tx="EKR.20040628095213.408"></t>
<t tx="EKR.20040628095213.412"></t>
<t tx="EKR.20040628095213.425"></t>
<t tx="EKR.20040628095213.442">This only happened after previous write error.

The fix was to init self.errors in openWriteFile.

The whole atFile logic is pretty gruesome.  It's got to be cleaned up.</t>
<t tx="EKR.20040628095213.444">- Allow indented @all.
    - Changed to g.is_special
    - Changed leoColor.doAtKeyword
    
- Fixed bug in is_special that broke p.isAtAllNode.</t>
<t tx="EKR.20040628095213.485">There was a small hole in the format of derived files.  Leo assumed that comment delimiters do not change within any particular derived file.  This assumption is not necessarily true in files like leoProjects.txt.

What I did:

- putDirective and readDirective now check for @langauge and @comment, and change comment delims appropriately.

This is slightly dubious: after all, an @langauge directive in the middle of most derived files will cause havoc.  However, one could say that this is the users problem :-)

BTW, this doesn't really solve all problems in @all trees: Leo can still get mightily confused about comment delims if the user doesn't put proper @language directives in @all trees.
</t>
<t tx="EKR.20040628095213.490">readEndNode uses the existing tempBodyString attribute to determine if the body text has changed.  If so, we mark the tnode dirty.  The code in 

top_df.read.&lt;&lt; copy all tempBodyStrings to tnodes &gt;&gt;

propagates the dirty marks to all ancestor @file nodes.  This can't be done in readEndNode because no positions are available at that time.</t>
<t tx="EKR.20040628095213.493"></t>
<t tx="EKR.20040628095213.499"></t>
<t tx="EKR.20040628095213.501">Leo now writes t.unknownAttributes to the .leo file when writing the &lt;v&gt; element corresponding to the root of an @thin tree.  Leo will do this by writing a new xml attribute, descendentTnodeUnknownAttributes, in &lt;v&gt; element.

Leo will only write t.unknownAttributes, not v.unknownAttributes.  This is because only tnodes have gnx's in thin derived files.  In effect, vnodes are anonymous.  We could attempt to get around this by identifying vnodes by their corresponding tnodes, but that's not a general solution and it is, in effect, equivalent to writing only t.unknownAttributes.  This being so, it seems pointless to "pretend" to be writing v.unknownAttributes.

The effect of this is to make all vnodes identical, as far as using unknownAttributes is concerned.  As I've stated in the past, this won't do if, for example, a plugin is trying create an arbitrary directed graph between vnodes.  In that case, the plugin should confine itself to @file trees, or just vnodes in .leo files, for that matter.</t>
<t tx="EKR.20040628095213.512">The problem was setting endSentinelComment to None instead of "" in readDirective.

The code is pretty fragile; it should handle either None or "", but in fact it requires "".</t>
<t tx="EKR.20040628095213.513"></t>
<t tx="EKR.20040628100535">@killcolor</t>
<t tx="EKR.20040628100535.1"></t>
<t tx="edream.110203163054.46">@nocolor</t>
<t tx="edream.110203163054.60">Leo will open .leo files automatically provided that you associate leo.py with .leo files.
Here is how to open Leo when double-clicking a .leo file on Windows 2K or XP:


-   In Windows 2K or XP, go to ``Start-&gt;Settings-&gt;Control panel``, open the ``Folder Options`` tab.
-   Select the ``file types`` tab. Press the ``New`` button.
-   Enter ``Leo`` into the ``Create New File Extension`` field. Press OK.
-   With ``Leo`` still highlighted in the ``Registered File Types`` list box, press the ``Advanced`` button.
-   Change the default file type field to something like ``Leo Literate Outline``.
-   Press the ``Icon`` button and browse to the ``LeoDoc`` icon in Leo's ``Icons`` folder.
-   Click OK. This gets the icons right and registers the description of the .leo file.

You now have to tell windows what to do to open the file properly:

-   Press the new button to open the ``New Action`` window.
-   In the ``Action`` field type ``Open``, then type **one** of the following lines::

    [python install dir]\pythonw.exe   [leo install dir]\leo.py %1
    [python install dir]\python.exe -i [leo install dir]\leo.py %1

The first  line opens Leo files with no console window.
The second line opens Leo files with a console window and leaves the window open after Leo exits.
You should now be able to double click on a leo file in explorer with Leo.</t>
<t tx="edream.110203163054.61">Leo will draw a Leo icon in all Leo windows without PIL or tkIcon.
For versions of Leo before 4.0 and for versions of Python before 2.3,
Leo will draw a Leo icon in Leo windows only if you have installed Fredrik Lundh's PIL and tkIcon packages.

-   Download PIL from http://www.pythonware.com/downloads/index.htm#pil

-   Download tkIcon from http://www.effbot.org/downloads/#tkIcon</t>
<t tx="edream.110203163054.63"></t>
<t tx="edream.110203163054.64">Leo 4.1 alpha 1                   November 3, 2003

*** Alpha quality code:  Please make full backups before playing with this code!

This release marks another significant milestone in Leo's history:

- Leo's 4.x file code is complete.  At present I have no plans to change the format of .leo files or derived files.  I am eating my own dog food: I do all my editing with the 4.1 code base.

- Leo uses immutable gnx's (id:timestamp:n) by default to associate tnodes with vnodes in .leo files.  This makes Leo as cvs friendly as possible.  From now on .leo files will be checked in to cvs with the -ko (text/keywords off) option.

- The use_gnx setting in leoConfig.txt determines whether uses gnx's (cvs friendly) or ints.  No version of Leo before 4.1 can read .leo files containing gnx.   Only gnx's are immutable.  Leo recomputes all non-gnx indices from scratch whenever writing a .leo file. It is possible to convert between 3.x and 4.1 file formats by changing the use_gnx setting.

- The 4.1 code base has been reorganized to support gui's other than tkinter.  Leo's src directory contains several new source files.

- The file test.leo in the test directory contains real regression tests for syntax coloring.   Regression testing scripts create regression tests dynamically from data in Leo's outline.  Very cool, very easy, very general.  In particular, regression tests may use temporary nodes in test.leo rather than creating separate Tk windows for testing.

Known bugs:

- The Extract commands eat one character too much.

- The __wx_gui.py plugin is only partly functional.</t>
<t tx="edream.110203163054.66">Leo 4.0.4                         October 29, 2003

- Fixed a problem with the titles in Font and Color panels.
- Worked around a Unicode assert failure in the colorizer.
- Fixed crasher in OnEndEditHeadline.
- Fixed import problems in leoPlugins.leo.
- @first and @last sentinels no longer contain corresponding text.
  This fixes a problem that affected PHP comment delimiters.

Leo 4.0.3                         October 25, 2003

- Fixes several problems with the auto_save and plugin menu plugins.
- Fixes a problem with the Go To Line Number command.

Note: This version does _not_ support Unicode file names or directory names.

Leo 4.0.2                         October 23, 2003

- Fixes a crasher in reportBadChars when a .leo file contains a character that
  can not be represented in the encoding specified in the first line of the
  .leo file.
- Leo now sends full tracebacks to the log window when Leo takes an unexpected
 exception.
- Leo now issues a more informative message when the @comment directive
  inhibits the Untangle command.

Leo 4.0.1                         October 22, 2003

- Fixes several crashers, one of which may prevent Leo from starting.
- Fixes indentation for section references that are preceded by something
  other than whitespace.
- Removes debugging traces when reading and writing unknown attributes.
- Removes some improperly cloned nodes from LeoDocs.leo.
- Adds the checkTopologyOfAllClones script.
- Fixes some problems with plugins.</t>
<t tx="edream.110203163054.67">Leo 4.0 final                     October 17, 2003

More than a year in the making, Leo 4.0 is finally here.

Highlights of 4.0 final:
-----------------------

** Improved and simplified format of derived files.
	- Eliminated child indices, extraneous blank lines and @body sentinels.
	- Eliminated @node sentinels that indicate outline structure.
	- New @nl and @nonl sentinels indicate where newlines are and aren't.
	- These changes will largely eliminate unwanted cvs conflicts.

** Greatly improved error handling.
	- Reading derived files _never_ alter outline structure or links.
	- Read errors leave the outline completely unchanged.
	- Broken clone links are gone forever.
	- As a result, 4.0 is much safer than all previous versions.

** Full compatibility will previous versions of Leo.
	- Leo 4.0 reads all derived files properly, regardless of version.
	- Leo writes new-format derived files by default, and this default may be changed.
	- New commands in the read/write menu allow you to explicitly specify the format of derived files.

* New commands:
	- Write 3.x Derived File and Write 4.x Derived File.
	- Import Derived File.
	- Clear Recent Files.

* Dozens of other improvements, including:
	- Better Unicode support.
	- New configuration settings.
	- Several new plugins.

See the notes for the various beta releases for full details.</t>
<t tx="edream.110203163054.68">Leo 4.0 beta 4                      October 13, 2003

This is the third public release of Leo 4.0. There are no known serious bugs in
this version of Leo.  This will be the last beta release before 4.0 final.

Changes made in 4.0 beta 4
--------------------------

- Changed all instances of string.letters to string.ascii_letters.
  string.letters can cause crashes in some locales (Unicode environments).
- Fixed several bugs that caused clone marks not to be set properly.</t>
<t tx="edream.110203163054.69">Leo 4.0 beta 3                      October 9, 2003

This is the third public release of Leo 4.0. There are no known serious bugs in
this version of Leo.

Highlights of 4.0 beta 3
------------------------

- Fixed problems with setting Leo's window icons.
- Plugins may now save their own information in &lt;v&gt; and &lt;t&gt; elements in .leo files.
- The usual assortment of bug fixes and minor improvements.

See the children of this node for full details.</t>
<t tx="edream.110203163054.70"></t>
<t tx="edream.110203163054.71">This was a long-standing bug.  It's effect was cosmetic, and it was important to fix.</t>
<t tx="edream.110203163054.72"></t>
<t tx="edream.110203163054.73">This could happen when the derived file was corrupted.</t>
<t tx="edream.110203163054.74"></t>
<t tx="edream.110203163054.75"></t>
<t tx="edream.110203163054.76">Leo can now read and write "foreign" attributes in &lt;v&gt; and &lt;t&gt; elements in .leo files:

- When reading a .leo file, Leo will create t.unknownAttributes or v.unknownAttributes ivars for any tnode and vnode object whose corresponding &lt;v&gt; or &lt;t&gt; element in the .leo file contains a foreign attribute.

- The unknownAttributes ivars are a dictionary whose keys are the attribute names and whose values are strings.

- When writing a file, Leo will write "foreign" attributes if  a vnode or tnode contains an unknownAttributes ivar.

- The only "native" attributes that Leo expects to find are the "tx" attribute in &lt;t&gt; elements and the "a", "t", "vtag" and "tnodeList" attributes of &lt;v&gt; elements.  Everything else is a foreign attribute.

- Leo performs the usual xml escapes on these strings when reading or writing the unknownAttributes ivars.

Plugins may cause Leo to write such foreign attributes simply by attaching unknownAttributes ivars to a vnode or tnode.  For example:

	v.unknownAttributes = {"vnodeIcon" : pathToIcon}

It would be best not to delete other foreign attributes, so the following would be preferred:

	if hasattr(v,"unknownAttributes"):
		v.unknownAttributes["vnodeIcon"] = pathToIcon
	else:
		v.unknownAttributes = {"vnodeIcon" : pathToIcon}

Another way:

	try:
		v.unknownAttributes["vnodeIcon"] = pathToIcon
	except AttributeError:
		v.unknownAttributes = {"vnodeIcon" : pathToIcon}</t>
<t tx="edream.110203163054.77"></t>
<t tx="edream.110203163054.78">Leo now warns if it can't find either the Icons directory or the LeoApp16.ico icon in that directory.</t>
<t tx="edream.110203163054.79">Leo 4.0 beta 2                      October 3, 2003

This is the second public release of Leo 4.0. There are no known serious bugs
in this version of Leo. Version 4.0 is the culmination of over a year of
collaborative design work and several months of actual implementation.

Highlights of 4.0 beta 2
------------------------
* Fixed several bugs:
  - Fixed several problems with reading and writing 4.0 derived files.
  - Fixed several Unicode-related bugs.
  - Fixed a crasher in the Go To Line Number command.
  - Fixed a problem with Importing Python files.
* Important improvements:
  - Added allow_clone_drags setting.  N.B. Allows Leo to be used with Aqua.
  - When running Python 2.3 Leo can now create window icons without third-party packages.
- The usual minor improvements and bug fixes.

See the children of this node for full details.

Highlights of 4.0 beta 1
------------------------
* Improved and simplified format of derived files.
* Greatly improved error handling.
* Full compatibility will previous versions of Leo.</t>
<t tx="edream.110203163054.80">- Fix undo/redo bug for all commands that change body text in multiple nodes without changing outline structure.
	- This is a long-standing bug that came to light when trying to make Read @file Nodes undoable.

- Make Read @file Nodes command undoable.

- Fix small bugs in the Go To Line Number command.</t>
<t tx="edream.110203163054.81"></t>
<t tx="edream.110203163054.82">The new code prints a warning if Leo's key internal strings are not Unicode.</t>
<t tx="edream.110203163054.83"></t>
<t tx="edream.110203163054.84">There were bugs involving saving the "Pattern Match" and "Subroutine Only" find settings.</t>
<t tx="edream.110203163054.85">@nocolor

Class level-code after the method definitions was dropped.  For example:

@color

class someclass:
	def __init__(self):
		pass

	# this code is dropped
	class_var = None

def some_proc():
	pass</t>
<t tx="edream.110203163054.86">The new code ensures that Leo creates and uses only Unicode strings internally.</t>
<t tx="edream.110203163054.87">Fixed Go To Outline command so it doesn't crash on 4.0 files.  More work is needed.</t>
<t tx="edream.110203163054.88">Under certain conditions the no sentinels at all were written when writing @rawfile trees.</t>
<t tx="edream.110203163054.89"></t>
<t tx="edream.110203163054.90"></t>
<t tx="edream.110203163054.91">This is much more natural and less cluttered.</t>
<t tx="edream.110203163054.92"></t>
<t tx="edream.110203163054.93"></t>
<t tx="edream.110203163054.94">Leo will create the Leo icon in Leo windows automatically when using Python 2.3.  The Python Imaging Library and the tkIcon package are only used when using previous versions of Python.</t>
<t tx="edream.110203163054.95">This is the foundation for "foreign" guis.</t>
<t tx="edream.110203163054.96"></t>
<t tx="edream.110203163054.97">allow_clone_drags

This is a workaround so that Leo may be used on Aqua.  When this setting is zero Leo always moves nodes when dragging.  The default is to enable clone-drags.

enable_drag_messages

Allows the user to suppress the message telling whether dragging nodes will move them or clone them.  The default is to enable those messages.</t>
<t tx="edream.110203163054.98">After the 4.0 beta 1 release I changed the default so that _new_ format derived files are written if leoConfig.txt does not exist.</t>
<t tx="edream.110203163054.99">leo.py 4.0 beta 1                      September 26, 2003

This is the first public release of Leo 4.0.  Version 4.0 is the culmination of over a year of collaborative design work and several months of actual implementation.

Please use caution when using this beta version of Leo.  It appears very solid and it has been tested by only a few people.

Highlights of 4.0:

** Improved and simplified format of derived files.
	- Eliminated child indices, extraneous blank lines and @body sentinels.
	- Eliminated @node sentinels that indicate outline structure.
	- New @nl and @nonl sentinels indicate where newlines are and aren't.
	- These changes will largely eliminate unwanted cvs conflicts.

** Greatly improved error handling.
	- Reading derived files _never_ alter outline structure or links.
	- Read errors leave the outline completely unchanged.
	- Broken clone links are gone forever.
	- As a result, using 4.0 is much safer than all previous versions.

** Full compatibility will previous versions of Leo.
	- Leo reads all derived files properly, regardless of version.
	- Leo writes new-format derived files by default, and this default may be changed.
	- New commands in the read/write menu allow you to explicitly specify the format of derived files.

* New commands:
	- Write 3.x Derived File.
	- Write 4.x Derived File.
	- Import Derived File.
	- Clear Recent Files.

- Several new plugins.
- Several minor bug fixes.

See the children of this node for full details.</t>
<t tx="edream.110203163054.100">The Synchronization Principle simplifies everything and at long last puts Leo on a firm theoretical foundation.  This principle states that the "smallest unit of meaning" of any Leo outline is the entire outline itself.  In particular, individual derived files have meaning only in the context of a particular outline.

The Synchronization Principle has the following happy consequences:

1. We may assume that all derived files are in synch with the outline that wrote them.  This assumption allows Leo to use "hidden machinery" in the outline to associate nodes in the derived file with nodes in the outline.  This "hidden" machinery consists of a list of tnodes associated with @file vnodes in the outline.  When writing a derived file Leo creates a list of tnodes in the order they were written to the derived file.  When reading the derived file, Leo uses this list to associate nodes in the derived file with nodes in the outline.

2. Derived files must get their structure from the .leo file that wrote them.  As we have seen, this is done using the hidden machinery in the .leo file.  Consequently, there is no further need to represent outline structure in derived files.  There is no need any longer either for child indices or for sentinels to represent outline structure.  As a result, we can eliminate @+body and @-body nodes entirely because all @+node sentinels are followed by body text.

3. All .leo files must contain full outline structure.  Even "thin" outline will contain the full representation of the outline as vnodes.

4. Reading _never_ alters outline structure in the outline.  No vnodes are ever created or destroyed and reading never alters clone links.  This is true whether or not read errors occur.  The read code sets a temporary attribute of tnodes while reading.  These attributes are copied to the permanent t.bodyString attribute only if no read errors were encountered.

4. Error recovery is now trivial:  Read errors indicate that the .leo files and one or more derived files are out-of-synch.  No error recovery is attempted: the @file tree in which the error occurred reverts back to its original state.

5. The new Import Derived File command is the _only_ way to recover data from mismatched derived file.</t>
<t tx="edream.110203163054.101"></t>
<t tx="edream.110203163054.102">The write_old_format_derived_files option in leoConfig.leo and leoConfig.txt determines which format of derived file Leo's Write and Save commands write by default.  If this option is 0 (recommended) Leo writes 4.x format derived files.  Otherwise Leo writes 3.x derived files.

Note that you can use the Write 3.x/4.x Derived Files commands in the File:Read/Write menu to write derived files in an explicitly specified format.</t>
<t tx="edream.110203163054.103">This command deletes all entries in the Recent Files submenu except the most recent file.  The files themselves are not affected, just the menu entries.</t>
<t tx="edream.110203163054.104">The Import Derived File command imports all the nodes in a derived file into the outline.  Unlike the read commands, no outline structure is preserved.  This command can import either 3.x or 4.x derived files.

This command is necessary in version 4.0 because there is no other way to read derived files that are out-of-synch with a .leo file.</t>
<t tx="edream.110203163054.105">The Write 4.x Derived Files command and Write 3.x Derived Files command work just like the Write @file Nodes command, except that they write the indicated format off derived file.  In contrast, the Write @file Nodes command writes 3.x format derived files if and only if the write_old_format_derived_files = 1 in leoConfig.txt.

All three of these commands automatically save the outline (the .leo file) if any derived file was actually written.  This is necessary so that information in the .leo file always remains in synch with all derived files.</t>
<t tx="edream.110203163054.106">Paul Paterson contributed the following new plugins:

mod_autosave.py

Autosaves the Leo document every so often.

mod_timestamp.py

Timestamps all save operations to show when they occur.

word_export.py

Exports an outline to a word document.  Clicking "plugins ... word export ... export" exports the selected outline to Word.  Word should be running with an open (empty) document before executing this command.</t>
<t tx="edream.110203163054.107"></t>
<t tx="edream.110203163054.108">Leo's read code now warns if any non-empty node is unvisited.  This check, and the check that headlines match pretty much guarantees that out-of-synch outlines will generate errors.  Thus, there is no need a gnx timestamp in @+leo sentinels!</t>
<t tx="edream.110203163054.109">Version 4.0 is a major advance in Leo's error handling.  Using 4.0 is much safer than all previous versions.  This new error handling applies to all derived files, both 3.x and 4.x format.  

Leo's read code never alters the structure of an outline, regardless of whether read errors are encountered. This means that clone links, marks, and all other information in the outline except body text remains completely unchanged during reads.  Broken clone links (the dreaded read errors) are gone forever.  
Also, the new read code makes no changes to any body text until it is known that no read errors have occured.  This ensures that absolutely no changes at all are made to the outline if there are read errors.

Leo's read code now writes a message to the log pane whenever it sees that the body text in the derived file does not match the body text in the outline.  These messages do not indicate errors, only that the body text has been changed outside of Leo, say in an external editor or by cvs.</t>
<t tx="edream.110203163054.110"></t>
<t tx="edream.110203163054.111"></t>
<t tx="edream.110203163054.112">Added encoding comments to leoGlobals.py and French plugins

This removes a warning new in Python 2.3.
</t>
<t tx="edream.110203163054.113">There is no need to recycle Python objects when the last outline window is being closed.</t>
<t tx="edream.110203163054.114">This is too annoying during testing.  The Read @file Nodes command will in fact be made undoable for the 4.0 final release.</t>
<t tx="edream.110203163054.115">This has been changed in Python 2.3 and it probably wasn't ever a good idea...</t>
<t tx="edream.110203163054.116">The read code has much simplified using look-behind rather than look-ahead.  Both the read and write code write the file line-by-line without recursion.</t>
<t tx="edream.110203163054.117"></t>
<t tx="edream.110203163054.118"></t>
<t tx="edream.110203163054.119">leo.py 3.12 Final                       July 17, 2003

Window sizes are now in pixels rather than grid units.
You will need to resize existing outlines (.leo files).  Don't panic!

Highlights of this version:

* Plugged a huge memory leak.
* Fixed a major bug involving undo.
* Added Icon &amp; Status areas to Leo window for use by plugins.
* Important new plugins:
  - The file leoPlugins.leo now contains all plugins.
  - add_directives.py allows plugins to define new directives.
  - color_markup.py supports wiki-styled markup.
  - mod_spelling.py checks spelling (requires aspell to be installed).
  - nav_buttons.py creates browser-style navigation plugins in the icon area.
  - plugins_menu.py creates a Plugins menu items for all loaded plugins.
  - scripts_menu.py creates a Scripts menu for all scripts in scripts folder.
  - spell
  - trace_gc traces all changes to memory at idle time.
* Other enhancements:
  - Redesigned the Find panel.   Non-functional options are dimmed.
  - Added @wrap and @nowrap directives.
  - Added Write Dirty @file Nodes command.
  - Added several new "stub hooks".
  - Hyperlinks are now enabled by default.
  - Leo now loads plugins in alphabetical order.
  - Leo now remembers the size and location of Leo windows.
  - Undo now restores the insert point or the selection range after most commands.
  - Added apply button to Font panel.
  - Improved the reporting of characters that do not exist in the present encoding.
* The usual assortment of bug fixes and minor improvements.
  - There are no known bugs in this version of Leo.

See the children of this node for full details.</t>
<t tx="edream.110203163054.120"></t>
<t tx="edream.110203163054.121">Undoing the following commands could corrupt outlines:

Convert All Blanks, Convert All Tabs, Extract, Extract Names, Extract Section.</t>
<t tx="edream.110203163054.122">v.nodeAfterTree was being called way too often when handling read errors.</t>
<t tx="edream.110203163054.123">- Leo wasn't properly recycling Tk widgets when redrawing the outline pane.  This was a _huge_ leak.

- Leo now recycles all objects used by a window when that window closes.

The app.destroyAllWindowObjects() routine calls o.__dict__.clear for all objects o in a window.

- Leo now longer needs destroy() methods in each major class.</t>
<t tx="edream.110203163054.124"></t>
<t tx="edream.110203163054.125">c:\prog\leoCVS\leo\src\leoNodes.py:1174: Parameter (encoding) not used

This may have been the cause of some "unicode" problems.</t>
<t tx="edream.110203163054.126">c:\prog\leoCVS\leo\src\leoFrame.py:976: No global (a) found

This may have been the cause of some problems with the log panel.</t>
<t tx="edream.110203163054.127">Leo didn't properly import .cxx files or files with upper case extensions.</t>
<t tx="edream.110203163054.128">The messages "reading: @file x" were not always showing up during Open commands.</t>
<t tx="edream.110203163054.129">Symptom: Sometimes the "reading" messages would not appear when reading an outline.

Cause: Several event handlers are called at unpredictable times during the load process.  These may try to reset the log.

Solution:
- create app.setLog, app.lockLog and app.unlocklog methods.
- call app.lockLog before opening an outline.</t>
<t tx="edream.110203163054.130"></t>
<t tx="edream.110203163054.131">The body_pane_wraps setting is now handled properly.
</t>
<t tx="edream.110203163054.132">The body keystroke handler wasn't handling the delete character properly.</t>
<t tx="edream.110203163054.133"></t>
<t tx="edream.110203163054.134">Methods with the same name confused this command.

The Go To Line Number command will be rewritten for 4.0.</t>
<t tx="edream.110203163054.135">The following was improperly indented in @nosentinel files.  The expansion of &lt;&lt; class shape declarations &gt;&gt; was indented twice.

class shape(object):
  	&lt;&lt; class shape declarations &gt;&gt;
  	# after decls</t>
<t tx="edream.110203163054.136">- Added code to check for errors in the table passed to createOpenWithMenuFromTable.

- Revised code that checks to see whether a temp file has already been created.  The old code didn't properly take into account of file extensions when checking for already opened temp files.</t>
<t tx="edream.110203163054.137">Leo now converts all tabs to blanks as you type, not just leading blanks.</t>
<t tx="edream.110203163054.138">- Moved the code into the app class.</t>
<t tx="edream.110203163054.139">This was due to a recent change in getTextSelection.</t>
<t tx="edream.110203163054.140"></t>
<t tx="edream.110203163054.141">- Several parts of the code looped on lists that were altered in the loop.
- Fixed several bugs in the code that handled shortcuts to Open With menu items.</t>
<t tx="edream.110203163054.142">- Leo's various sort commands did not work properly if two headlines were identical.

- Eliminated the unnecessary and buggy sortSequence routine.</t>
<t tx="edream.110203163054.143"></t>
<t tx="edream.110203163054.144">Recent changes interfered with dragging nodes.</t>
<t tx="edream.110203163054.145">Here are the results from running checkClones2Links script on this file:

multipleTargetsInDerivedFiles: 8

(fixed) class nodeIndices      (improperly duplicated in leoAtFile.py)
(fixed) frame.OpenWithFileName (improperly duplicated in Recent Files submenu)
(fixed) recentButtonCallback   (improperly duplicated in Mark/Goto submenu)

-- Used several times in same derived file.  Will this be valid in LeoN?

&lt;&lt; Append any unused text to the parent's body text &gt;&gt; (used several times in leoImport.py)
&lt;&lt; Check both parts for @ comment conventions &gt;&gt; (used several times in leoTangle.py)
&lt;&lt; Compare single characters &gt;&gt; (used several times in leoTangle.py)
&lt;&lt; Set the default directory &gt;&gt; (used several times in leoAtFile.py)

-- Used (properly) in two different derived files:

replacePatterns (used on purpose in setup.py and postSetup.py)

clonedAtFileNodes: 9

@file ../plugins/add_directives.py
@file ../plugins/french_fm.py
@file ../plugins/open_with.py
@file ../plugins/vim.py
@file ../plugins/xemacs.py
@file c:\prog\test\multiple.txt
@file-nosent nosentCloneTest.txt
@silentfile ../doc/PKG-INFO.TXT
@silentfile ../doc/README.TXT
</t>
<t tx="edream.110203163054.146">Fractions cause problems in some locales.  The height/width params weren't used anyway!
</t>
<t tx="edream.110203163054.147"></t>
<t tx="edream.110203163054.148"></t>
<t tx="edream.110203163054.149">- createTopologyList creates a list containing a description of a tree.  Used by several of the new scripts.

- importFromPath encapsulates a lot of details of custom importing, and makes it unnecessary to alter sys.path.

- funcToMethod allows users to add methods to any class.  Such methods immediately become available to all objects, including existing objects!

- Added do-nothing flush method to redirect class.  This routine was added to support LeoN.</t>
<t tx="edream.110203163054.150">- The checkForPossiblyBrokenLinks script does just what it says.

- The checkClones2Links script warns if nodes are used by several derived files.</t>
<t tx="edream.110203163054.151">The new code uses a common base class for all dialogs.</t>
<t tx="edream.110203163054.152">- The new code uses proper Python lists to represent join lists.  This greatly clarifies the relevant sections of code, and may even provide a performance boost.  

- tnodes now contain both headline and body text. This change creates an important invariant:  vnodes with the same vnx's always point to tnodes with the same tnx's.  This invariant is vital to resolving conflicts properly.

- rewrote joinList code and move joinLists to tnodes.</t>
<t tx="edream.110203163054.153">- There is now only a single entry point into Leo: the run() routine.

This routine uses an optional fileName arg.

- Created runMainLoop function in leo.py so the call to mainloop() is in a separate function.

This routine was added to support LeoN.</t>
<t tx="edream.110203163054.154"></t>
<t tx="edream.110203163054.155"></t>
<t tx="edream.110203163054.156">The body_pane_wraps setting is used if neither of these directives is in effect.
</t>
<t tx="edream.110203163054.157">This make the Font panel a bit less intimidating to use.</t>
<t tx="edream.110203163054.158">- Added an "icon area" at the top of each Leo frame.  Plugins may add buttons to the Icon area at the top of each Leo frame.  See the nav_buttons.py plugin for an example of how to use this area.

- Added a "status area" at the bottom of each Leo frame.  This area reports the line and column number of the cursor.  Plugins may send status messages to this this area.

- Added convenience routines for the icon and status areas to the LeoFrame class.  Plugins may use these convenience routines to create, update, manage and destroy fields in the icon and status areas.</t>
<t tx="edream.110203163054.159">These aren't quite ready for prime time.</t>
<t tx="edream.110203163054.160"></t>
<t tx="edream.110203163054.161"></t>
<t tx="edream.110203163054.162">Hypertext links now enabled by default.  Control-click any section reference to go to its definition.  I changed the colorer so that it does _not_ underline active hyperlinks in section reference.  If a section reference is underlined, it means the definition does _not_ exist.  Otherwise the section reference _does_ exist and control-clicking the reference takes you to the defining node in one of its descendants.</t>
<t tx="edream.110203163054.163">The new code is substantially more robust than the old.</t>
<t tx="edream.110203163054.164"></t>
<t tx="edream.110203163054.165"></t>
<t tx="edream.110203163054.166">Leo was not honoring the requested size of Leo windows.

As the result of this change Leo will open old .leo files much smaller than expected.  Do not panic!  Simply resize the Leo window and save it.  The next time you open the window all will be well.</t>
<t tx="edream.110203163054.167">I have found this command to be highly annoying and unwanted.</t>
<t tx="edream.110203163054.168">This is very important for the spell-checking plugin, and is quite useful in all other situations.</t>
<t tx="edream.110203163054.169"></t>
<t tx="edream.110203163054.170"></t>
<t tx="edream.110203163054.171">- Added the following stub hooks:

"after-create-leo-frame"
"close-frame"
"create-optional-menus"
"destroy-all-global-windows"
"init-color-markup"
"new"
"redraw-entire-outline"
"scan-directives"

See the section called "About hooks" for full details.

- Changed handleLeoHook to doHook.  This simplifies the code a bit.
</t>
<t tx="edream.110203163054.172">@nowrap

At startup time Leo looks all files of the form mod_*.py in the plugins
directory. Leo assumes that these files are "plugins" containing Python modules
that customizes Leo's operation. Leo attempts to import each file.

Each module should register routines that are called at various times during
execution. Such times are identified by strings known as "tags". The code in in
one or more plugins corresponding to each tag are known as the "hook" routines
for that tag. Leo catches exceptions (including syntax errors) in hook
routines, so it is safe to hack away on this code.

Leo passes two argument to all hook routines: the tag and a keywords dictionary
containing additional information. For example, keywords["label"] indicates the
kind of command for "command1" and "command2" hooks.

For some hooks, returning anything other than None "overrides" Leo's default
action. Hooks have full access to all of Leo's source code. Just import the
relevant file. For example, top() returns the commander for the topmost Leo
window.

The following table summarizes the arguments passed to hooks: ( Overrides is
"yes" if returning anything other than None overrides Leo's normal command or
event processing.)

tag argument                                              keys in keywords
(hook name)  overrides       when called                  dictionary argument
---------    ---------       -----------                  -------------------
"bodyclick1"   yes      before normal click in body       c,v,event
"bodyclick2"            after  normal click in body       c,v,event
"bodydclick1"  yes      before double click in body       c,v,event
"bodydclick2"           after  double click in body       c,v,event
"bodykey1"     yes      before body keystrokes            c,v,ch,oldSel,undoType
"bodykey2"              after  body keystrokes            c,v,ch,oldSel,undoType
"bodyrclick1"  yes      before right click in body        c,v,event
"bodyrclick2"           after  right click in body        c,v,event
"boxclick1"    yes      before click in +- box            c,v,event
"boxclick2"             after  click in +- box            c,v,event
"command1"     yes      before each command               c,v,label (note 2)
"command2"              after  each command               c,v,label (note 2)
"drag1"        yes      before start of drag              c,v,event
"drag2"                 after  start of drag              c,v,event
"dragging1"    yes      before continuing to drag         c,v,event
"dragging2"             after  continuing to drag         c,v,event
"end1"                  start of app.quit()
"enddrag1"     yes      before end of drag                c,v,event
"enddrag2"              after  end of drag                c,v,event
"headclick1"   yes      before normal click in headline   c,v,event
"headclick2"            after  normal click in headline   c,v,event
"headrclick1"  yes      before right click in headline    c,v,event
"headrclick2"           after  right click in headline    c,v,event
"headkey1"     yes      before headline keystrokes        c,v,ch
"headkey2"              after  headline keystrokes        c,v,ch
"hypercclick1" yes      before control click in hyperlink c,v,event
"hypercclick2"          after  control click in hyperlink c,v,event
"hyperenter1"  yes      before entering hyperlink         c,v,event
"hyperenter2"           after  entering hyperlink         c,v,event
"hyperleave1"  yes      before leaving  hyperlink         c,v,event
"hyperleave2"           after  leaving  hyperlink         c,v,event
"iconclick1"   yes      before single click in icon box   c,v,event
"iconclick2"            after  single click in icon box   c,v,event
"iconrclick1"  yes      before right click in icon box    c,v,event
"iconrclick2"           after  right click in icon box    c,v,event
"icondclick1"  yes      before double click in icon box   c,v,event
"icondclick2"           after  double click in icon box   c,v,event
"idle"                  periodically (at idle time)       c,v
"menu1"        yes      before creating menus             c,v        (note 3)
"menu2"        yes      before updating menus             c,v
"open1"        yes      before opening any file           old_c,new_c,fileName (note 4)
"open2"                 after  opening any file           old_c,new_c,fileName (note 4)
"openwith1"    yes      before Open With command          c,v,openType,arg,ext
"openwith2"             after  Open With command          c,v,openType,arg,ext
"recentfiles1" yes      before Recent Files command       c,v,fileName,closeFlag
"recentfiles2"          after  Recent Files command       c,v,fileName,closeFlag
"save1"        yes      before any Save command           c,v,fileName
"save2"                 after  any Save command           c,v,fileName
"select1"      yes      before selecting a vnode          c,new_v,new_v
"select2"               after  selecting a vnode          c,new_v,old_v
"select3"               after  selecting a vnode          c,new_v,old_v
"set-mark"     no       when a mark is set                c,v           (new)
"start1"       no       after app.finishCreate()
"start2"                after opening first Leo window    c,v,fileName
"unselect1"    yes      before unselecting a vnode        c,new_v,old_v
"unselect2"             after  unselecting a vnode        c,old_v,old_v
"@url1"        yes      before double-click @url node     c,v           (note 5)
"@url2"                 after  double-click @url node     c,v           (note 5)

Notes:

(1) "activate" and "deactivate" hooks: These have been removed because they do
not work as expected.

(2) "commands" hooks: The label entry in the keywords dict contains the
"canonicalized" form of the command, that is, the lowercase name of the command
with all non-alphabetic characters removed.

Commands hooks now set the label for undo and redo commands "undo" and "redo"
rather than "cantundo" and "cantredo".

(3) "menu1" hook: Setting app().realMenuNameDict in this hook is an easy way of
translating menu names to other languages. Note: the "new" names created this
way affect only the actual spelling of the menu items, they do _not_ affect how
you specify shortcuts in leoConfig.txt, nor do they affect the "official"
command names passed in app().commandName. For example, suppose you set
app().realMenuNameDict["Open..."] = "Ouvre".

(4) "open1" and "open2" hooks: These are called with a keywords dict containing
the following entries:

old_c: The commander of the previously open window.
new_c: The commander of the newly opened window.
fileName: The name of the file being opened.

You can use old_c.currentVnode() and new_c.currentVnode() to get the current
vnode in the old and new windows.

Leo calls the "open1" and "open2" hooks only if the file is already open. Leo
will also call the "open1" and "open2" hooks if: a) a file is opened using the
Recent Files menu and b) the file is not already open.

(5) "@url1" and "@url2" hooks are only executed if "icondclick1" hook returns None.


New in version 3.12:

The following hooks are a new breed of hook, called "stub hooks". Conceptually,
these hooks are like calls to stub routines that can be filled in by code in
plugins.

tag argument                                                       keys in keywords
(hook name)               overrides        when called           dictionary argument
---------                 ---------        -----------           -------------------
"after-create-leo-frame"     no   before calling f.finishCreate  c
"after-redraw-outline"       no        end of tree.redraw        c (note 6)
"before-create-leo-frame"    no    after calling f.finishCreate  c
"clear-mark"                 no        when mark is set          c,v
"close-frame"                no        in app.closeLeoWindow     c
"color-optional-markup"      yes *     (note 7)                  colorer,v (note 7)
"create-optional-menus"      no        (note 8)                  (note 8)
"create-popup-menu-items"    no        in tree.OnPopup           c,v,event (new)
"destroy-all-global-windows" no        (note 12)                 None
"draw-outline-box"           yes       start of drawBox          tree,p,v,x,y (note 6)
"draw-outline-icon"          yes       start of tree.drawIcon    tree,p,v,x,y (note 6)
"draw-outline-node"          yes       start of tree.drawNode    tree,p,v,x,y (note 6)
"draw-outline-text-box"      yes       start of tree.drawText    tree,p,v,x,y (note 6)
"draw-sub-outline"           yes       start of tree.drawTree    tree,p,v,x,y,h,level (note 6)
"enable-popup-menu-items"    no        in tree.OnPopup           c,v,event (new)
"init-color-markup"          no        (note 7)                  colorer,v,s,i,j,colortag (note 7)
"new"                        no        start of New command      old_c,new_c (note 9)
"redraw-entire-outline"      yes       start of tree.redraw      c (note 6)
"scan-directives"            no        in scanDirectives         c,v,s,old_dict,dict,pluginsList (note 10)
"set-mark"                   no        when mark is set          c,v
"show-popup-menu"            no        in tree.OnPopup           c,v,event

Notes:

(6) These hooks are useful for testing.

(7) These stub hooks allow plugins to parse and handle markup withing doc
parts, comments and Python """ strings. Note that these hooks are _not_ called
in Python ''' strings. See the color_markup plugin for a complete example of
how to use these hooks.

(8) The "create-optional-menus" stub hook is called when Leo is creating menus,
at the place at which creating new menus is appropriate. Therefore, this hook
need only create new menus in the correct order, without worrying about the
placement of the menus in the menu bar. See the plugins_menu and scripts_menu
plugins for examples of how to use this hook. Leo now executes hooks in
alphabetical order, so that the Plugins menu will be created before the Scripts
menu.

(9) The "new" stub hook is called at the beginning of the code that implements
the New command. This provides a much easier way of recognizing when Leo is
about to create a new Leo window.

(10) The "scan-directives" stub hooks is called inside the scanDirectives
global function. The dictionary returned by scanDirectives now contains an item
whose key is "pluginsList". The value of this item is a list of tuples
(d,v,s,k) where:

- d is the spelling of the @directive, without the leading @.
- v is the vnode containing the directive, _not_ the original vnode.
- s[k:] is a string containing whatever follows the @directive. k has already
been moved past any whitespace that follows the @directive.

See the add_directives plugins directive for a complete example of how to use
the "scan-directives" stub hook.

(11) The "close-frame" stub hook is called in app.closeLeoWindow just before
removing the window from app.windowList. The hook code may remove the window
from app.windowList to prevent app.closeLeoWindow from destroying the window.

(12) Leo calls the "destroy-all-global-windows" hook in app.destroyAllGlobalWindows().
This hook gives plugins the chance to clean up after themselves when Leo shuts down.</t>
<t tx="edream.110203163054.173">Leo now supports two new stub hooks: "clear-mark" and "set-mark".  Both fully update the marks window, so it is important that they not be called "too often", and they aren't.

As a side effect, it is no longer necessary to update the marks window after every command that affects marks, a nice simplification and generalization of the code.

While I was at it, I moved the two dialog classes used only by the nav_buttons plugin out of leoDialog.py and into nav_buttons.py where they belong.</t>
<t tx="edream.110203163054.174">Added the "create-popup-menu", "enable-popup-menu-items" and "show-popup-menu" hooks.</t>
<t tx="edream.110203163054.175">Added the "create-popup-menu", "enable-popup-menu-items" and "show-popup-menu" hooks.</t>
<t tx="edream.110203163054.176"></t>
<t tx="edream.110203163054.177">This plugin allows users to create new directives.

As an example, this plugin creates a new @markup wiki directive.</t>
<t tx="edream.110203163054.178">This plugin supports coloring for markup in doc parts and Python triple-double-quoted strings.

At present, this plugin supports wiki-style markup, and it would be easy to change the style of markup.</t>
<t tx="edream.110203163054.179">This plugin adds 4 new buttons to the icon area at the top of each Leo window:

- Back and Forward arrows that work like a typical web browser.  Clicking the back arrow button takes you to the last node in the tree you visited.  Clicking the forward arrow button moves you forward.  The forward arrow button is dimmed unless you have clicked the back arrow button recently.

- The Recent button opens a non-modal dialog showing all the nodes you have visited recently.  This dialog is updated cleanly by the tree.select method.  You will see this entries change dynamically.  There are buttons in this dialog for clearing individual entries or clearing all entries.  Double-clicking any entry in this dialog takes you to that node, as does clicking the Go button.

The entries in the Recent Nodes pane do _not_ correspond to the order implied by the Forward and Back arrows.  Rather, the most recently visited node is on top, followed by the next most recently visited node, and so on, with the additional feature that nodes appear only once in the list.

- The Marks button opens a non-modal dialog showing all marked nodes in the tree.  Marking or unmarking nodes in the tree adds or deletes entries from this dialog.  Double-clicking any entry in this dialog takes you to that node, as does clicking the Go button.</t>
<t tx="edream.110203163054.180">This creates a plugins menu describing each loaded plugin.</t>
<t tx="edream.110203163054.181">The scripts_menu.py plugin creates a Scripts menu for all scripts in scripts folder.</t>
<t tx="edream.110203163054.182">- Leo now scans all .py files in the plugins folder when looking for plugins.

Filenames need not start with mod_, and Leo scans only the plugins folder.

- Leo loads plugins in alphabetical order.

- Leo now prints only a brief summary of the number of files loaded &amp; examined to the log file.</t>
<t tx="edream.110203163054.183">1. Created config, doc, examples, plugins, scripts, src, test &amp; tools folders.

2. Removed the following files:

- nsi.leo file.  This was a duplicate of code in LeoPy.leo.  
- bdist.bat, go.bat, help.bat, sdist.bat.
- leo.rc and leo.res.  These were resource files used by the Delphi classes.</t>
<t tx="edream.110203163054.184">These were written by Frank Merenda.</t>
<t tx="edream.110203163054.185">leo.py 3.11.1                       May 1, 2003

This version fixes two bugs:
	
- Version 3.11 had startup problems on some Linux systems.

- Creating clones by control dragging did not always work.
  This bug has existed in Leo for a long time.</t>
<t tx="edream.110203163054.186">leo.py requires Python 2.1 or above and tcl/tk 8.3 or above.
leo.py will work on Linux, Windows and MacOs X Jaguar.

leo.py 3.11.1                       May 1, 2003

This version fixes the following bugs:

- Leo would crash on startup on some Linux systems due to a problem
  with Leo's local copy of getpreferredencoding.

- Leo sometimes did not set clone bits properly after creating a clone
  by control-dragging a node.  This bug has existed for about 6 months!

leo.py 3.11                         April 27, 2003

This version of Leo contains many important improvements since 3.10,
especially support for unicode and a new plugin architecture.

The Highlights of 3.11:

** Leo supports unicode.
	- New @encoding directives specifies encoding for derived files.
	- New settings specify default encodings for .leo and derived files.
	- Derived files specify encodings used to create them.
** A new plugin architecture for customizing Leo. (A major improvement.)
- New commands:
	- Toggle Angle Brackets.
	- Insert Time/Date (in headline or body text).
	- Go To First/Last Node, Parent, Next/Previous Sibling.
	- Write Missing @file Nodes.
	- Expand/Contract Node.
- Improved commands:
	- Fixed a huge performance bug that slowed moving nodes left.
	- Expand/Contract commands now operate on the selected tree.
	  ( A major improvement)
	- Sort Siblings command can now sort top-level nodes.
	- Leo now allows multiple writes of cloned nodes.
	  (Useful when different @path directives are in effect.)
- Other improvements:
	- New @lineending directive specifies line endings.
	- Improved syntax coloring for html and xml.
	- Leo scrolls partially visible headlines into full view.
	- Added "Replace tabs with spaces" checkbox in Prefs panel.
- New settings in leoConfig.leo/.txt.
	- Added "tk_encoding" setting and related logic.
	- Colors for Show Invisibles command and body_insertion_cursor
	- Settings affecting when control-drags start.
	- Defaults for unicode (see above).
- Many other bug fixes and improvements.

See the children of this node for full details.</t>
<t tx="edream.110203163054.187"></t>
<t tx="edream.110203163054.188"></t>
<t tx="edream.110203163054.189">This ensures that the outline is redrawn properly after the Read @file Nodes command.</t>
<t tx="edream.110203163054.190">Browsing the comp.lang.python yesterday I found that there are serious problems with Python's getdefaultlocale() routine.  Martin v. Löwis says "getdefaultlocale() is broken, and cannot be fixed", though he does suggest the following workaround:

leoGlobals.py uses locale.getpreferredencoding to define getpreferredencoding if locale.getpreferredencoding exists (it is new in Python 2.3alpha).  Otherwise, Leo uses the code copied from the 2.3a2 version of Python to define getpreferredencoding.  Either way, leoGlobals.py now defines getpreferredencoding and Leo uses getpreferredencoding rather than getdefaultlocale.</t>
<t tx="edream.110203163054.191">After opening the Python window the call to tkFont() threw a (caught) exception on every call to frame.setTabWidth.  The fix was to add the optional root param.</t>
<t tx="edream.110203163054.192">skip_long was throwing an exception if there were no valid digits following a + or - sign.</t>
<t tx="edream.110203163054.193"></t>
<t tx="edream.110203163054.194">- tangle.scanAllDirectives was not setting self.encoding when handling @encoding.
- tangle.scanAllDirectives wasn't scanning the @encoding line properly.
- fixed crashers in Tangle and Untangle logic.</t>
<t tx="edream.110203163054.195">Fixed bug in handleLinesFollowingSentinel:
c:\prog\LeoCVS\leo\leoAtFile.py:482: No global (i) found
Removed i arg from rfind.

Fixed bug in definition of BadLeoFile:
c:\prog\LeoCVS\leo\leoFileCommands.py:27: Base class (exceptions.Exception) __init__() not called
Added call to Exception.__init__(self,message)

Fixed bug in askYesNoCancel
c:\prog\LeoCVS\leo\leoDialog.py:283: Variable (no) used before being set.
Disabled defaultButton logic.  New code would have to be thoroughly tested.

Removing unused routine: setDefaultLoc.
c:\prog\LeoCVS\leo\leoNodes.py:2581: No class attribute (defaultLoc) found

Fixed bug in put: changed a to app()
c:\prog\leoCvs\leo\leoFrame.py:4973: No global (a) found
</t>
<t tx="edream.110203163054.196">I had completely misunderstood __del__ methods!  __del__ methods disable the gc's ability to collect circular garbage (!!) and so __del__ methods will _never_ be called (!!)

BTW, when deleting an entire Leo window Leo calls various destroy methods to unlink items.  This allows the garbage collector to collect all data structures.  Because of unlimited undo only these destroy methods have the potential for creating "real" garbage.</t>
<t tx="edream.110203163054.197"></t>
<t tx="edream.110203163054.198">This adds http:\\ to url's if needed.</t>
<t tx="edream.110203163054.199">New in version 3.11.  The @lineending directive allows you to specify the line endings for individual derived files.  This directive will override the output_newline setting in leoConfig.txt.  Note that @lineending _never_ affects the line endings in .leo files themselves:  we must have consistent line endings in .leo files!  See below for more details.

The valid forms of the new @lineending directive are:

@lineending nl       (the default, Linux)
@lineending cr       (Mac)
@lineending crlf     (Windows)
@lineending lf       (same as nl, not recommended)
@lineending platform (same as platform value for output_newline setting in leoConfig.txt)</t>
<t tx="edream.110203163054.200">This will have no effect until version 4.0.</t>
<t tx="edream.110203163054.201">Leo now uses unicode internally for most strings.  This solves a lot of problems.  The children of this node discuss all the details...</t>
<t tx="edream.110203163054.202">This fixes several bugs.</t>
<t tx="edream.110203163054.203">In particular, the locale returned by locale.getdefaultlocale()[1] need not be a valid unicode encoding.
</t>
<t tx="edream.110203163054.204">Leo now uses unicode internally for most strings.  The highlights:

1. Leo converts headline and body text to unicode when reading .leo files and derived files.  Both .leo files and derived files may specify their encoding, with "utf-8" being used by default.  If the encoding used in a derived file is not "utf-8" it is represented in the @+leo sentinel line.  For example:

#@+leo-encoding=iso-8859-1.

The "utf-8" encoding is a "lossless" encoding (it can represent all unicode code points), so encoding and decoding to and from utf-8 plain strings will never cause a problem.  When reading or writing a character not in a "lossy" encoding, Leo converts such characters to '?' and issues a warning. 

2. When writing .leo files and derived files Leo uses the same encoding used to read the file, again with "utf-8" used as a default.

3. leoConfig.py contains two settings used to specify the default encoding used for .leo and derived files:

default_derived_file_encoding = UTF-8 
new_leo_file_encoding = UTF-8 

I do not recommend changing new_leo_file_encoding (see the comments in leoConfig.leo) and you may set 
default_derived_file_encoding to anything that makes sense for you.

4. You may use the @encoding directive to specify the encoding used in a derived file.  You can't mix encodings in a single derived file.

This is all should need to know to use extended character sets on Leo.</t>
<t tx="edream.110203163054.205">leoConfig.py now contains two new settings, with the defaults shown below: 

default_derived_file_encoding = UTF-8 
new_leo_file_encoding = UTF-8 

These control the default encodings used when writing derived files and .leo files.

I do not recommend changing new_leo_file_encoding (see the comments in leoConfig.leo)

You may set default_derived_file_encoding to anything that makes sense for you.
</t>
<t tx="edream.110203163054.206">The following paragraphs discuss code-level details.  You should not need to read this section in order to use Leo.

1. Leo uses unicode objects in vnodes and tnodes to denote headline and body text.  Note that unicode strings have no encoding; only plain strings have encodings. This means that once an (encoded) plain string has been converted to a unicode string it doesn't matter how the unicode string was created.  This is the key that makes Leo's new code robust. 

So internally Leo never has to worry about encodings. The only times encoding matter is when encoded strings are converted to and from unicode when Leo reads or writes files (or when the passing strings to and from Tk.Text widgets, but the idea is the same).

2. Python expressions that mix unicode strings u and plain strings s, like:

	u + s 
or 
	u == s 
or 
	u[5] == s[2:]

are promoted to unicode objects using the "system encoding". This encoding should never be changed, but we can't assume that we know what it is, so for safety we should assume the most restrictive encoding, namely "ascii".  With this assumption, Leo's code can't throw an exception during these promotions provided that: 

- All strings are converted to unicode when Leo reads files or gets text from Tk.Text widgets. 
- All string literals in Leo's code have only ascii characters.</t>
<t tx="edream.110203163054.207"></t>
<t tx="edream.110203163054.208">It is now much easier to customize Leo.  The new scheme is based on plugins (files in the plugins directory) rather than modifying customizeLeo.py.  Many thanks to Paul Paterson for suggesting this scheme and for doing the first implementation.
</t>
<t tx="edream.110203163054.217">Simplified and regularized hooks:

- replaced "event1" and "event2" hooks with 'regular' hooks.
	* Much easier to understand.
- added "iconrclick" hooks.
- added "bodyrclick" hooks.
- added "save1" and "save2" hooks
- added "dragging" hooks.
	* These are called when drag hook called while already dragging.
- added "hyperenter" and "hyperleave" hooks.
	* These only fire if use_hyperlinks = 1 in leoConfig.txt.
- removed "activate" and "deactivate" hooks.
	* These were not reliable.
- almost all hooks now have c,v arguments.
- "command" hooks now return "undo" and "redo" rather than "cantundo" and "cantredo"

Improved code:

- improved the tracing of hooks.
- the tracing code also checks to make sure that most hooks have c,v keywords.
- created es_event_exception().
- put all event handlers in try/except blocks that call es_event_exception on errors.</t>
<t tx="edream.110203163054.218">At startup time Leo looks all files of the form mod_*.py in the plugins
directory. Leo assumes that these files are "plugins" containing Python modules
that customizes Leo's operation. Leo attempts to import each file.

Each module should register routines that are called at various times during
execution. Such times are identified by strings known as "tags". The code in in
one or more plugins corresponding to each tag are known as the "hook" routines
for that tag. Leo catches exceptions (including syntax errors) in hook
routines, so it is safe to hack away on this code.

Leo passes two argument to all hook routines: the tag and a keywords dictionary
containing additional information. For example, keywords["label"] indicates the
kind of command for "command1" and "command2" hooks.

For some hooks, returning anything other than None "overrides" Leo's default
action. Hooks have full access to all of Leo's source code. Just import the
relevant file. For example, top() returns the commander for the topmost Leo
window.

The following table summarizes the arguments passed to hooks: ( Overrides is
"yes" if returning anything other than None overrides Leo's normal command or
event processing.)

tag argument                                              keys in keywords
(hook name)  overrides       when called                  dictionary argument
---------    ---------       -----------                  -------------------
"bodyclick1"   yes      before normal click in body       c,v,event (new)
"bodyclick2"            after  normal click in body       c,v,event (new)
"bodydclick1"  yes      before double click in body       c,v,event (new)
"bodydclick2"           after  double click in body       c,v,event (new)
"bodykey1"     yes      before body keystrokes            c,v,ch,oldSel,undoType
"bodykey2"              after  body keystrokes            c,v,ch,oldSel,undoType
"bodyrclick1"  yes      before right click in body        c,v,event (new)
"bodyrclick2"           after  right click in body        c,v,event (new)
"boxclick1"    yes      before click in +- box            c,v,event (new)
"boxclick2"             after  click in +- box            c,v,event (new)
"command1"     yes      before each command               c,v,label (note 2)
"command2"              after  each command               c,v,label (note 2)
"drag1"        yes      before start of drag              c,v,event (new)
"drag2"                 after  start of drag              c,v,event (new)
"dragging1"    yes      before continuing to drag         c,v,event (new)
"dragging2"             after  continuing to drag         c,v,event (new)
"end1"                  start of app.quit()
"enddrag1"     yes      before end of drag                c,v,event (new)
"enddrag2"              after  end of drag                c,v,event (new)
"headclick1"   yes      before normal click in headline   c,v,event (new)
"headclick2"            after  normal click in headline   c,v,event (new)
"headrclick1"  yes      before right click in headline    c,v,event (new)
"headrclick2"           after  right click in headline    c,v,event (new)
"headkey1"     yes      before headline keystrokes        c,v,ch
"headkey2"              after  headline keystrokes        c,v,ch
"hypercclick1" yes      before control click in hyperlink c,v,event (new)
"hypercclick2"          after  control click in hyperlink c,v,event (new)
"hyperenter1"  yes      before entering hyperlink         c,v,event (new)
"hyperenter2"           after  entering hyperlink         c,v,event (new)
"hyperleave1"  yes      before leaving  hyperlink         c,v,event (new)
"hyperleave2"           after  leaving  hyperlink         c,v,event (new)
"iconclick1"   yes      before single click in icon box   c,v,event (new)
"iconclick2"            after  single click in icon box   c,v,event (new)
"iconrclick1"  yes      before right click in icon box    c,v,event (new)
"iconrclick2"           after  right click in icon box    c,v,event (new)
"icondclick1"  yes      before double click in icon box   c,v,event (new)
"icondclick2"           after  double click in icon box   c,v,event (new)
"idle"                  periodically (at idle time)       c,v
"menu1"        yes      before creating menus             c,v (note 3)
"menu2"        yes      before updating menus             c,v
"open1"        yes      before opening any file           old_c,new_c,fileName (note 4)
"open2"                 after  opening any file           old_c,new_c,fileName (note 4)
"openwith1"    yes      before Open With command          c,v,openType,arg,ext
"openwith2"             after  Open With command          c,v,openType,arg,ext
"recentfiles1" yes      before Recent Files command       c,v,fileName,closeFlag
"recentfiles2"          after  Recent Files command       c,v,fileName,closeFlag
"save1"        yes      before any Save command           c,v,fileName
"save2"                 after  any Save command           c,v,fileName
"select1"      yes      before selecting a vnode          c,new_v,new_v
"select2"               after  selecting a vnode          c,new_v,old_v
"start1"       no       after app.finishCreate()
"start2"                after opening first Leo window    c,v,fileName
"unselect1"    yes      before unselecting a vnode        c,new_v,old_v (new)
"unselect2"             after  unselecting a vnode        c,old_v,old_v (new)
"@url1"        yes      before double-click @url node     c,v (note 5)
"@url2"                 after  double-click @url node     c,v (note 5)

Notes:

(1) "activate" and "deactivate" hooks: These have been removed because they do
not work as expected.

(2) "commands" hooks: The label entry in the keywords dict contains the
"canonicalized" form of the command, that is, the lowercase name of the command
with all non-alphabetic characters removed.

Commands hooks now set the label for undo and redo commands "undo" and "redo"
rather than "cantundo" and "cantredo".

(3) "menu1" hook: Setting app().realMenuNameDict in this hook is an easy way of
translating menu names to other languages. Note: the "new" names created this
way affect only the actual spelling of the menu items, they do _not_ affect how
you specify shortcuts in leoConfig.txt, nor do they affect the "official"
command names passed in app().commandName. For example, suppose you set
app().realMenuNameDict["Open..."] = "Ouvre".

(4) "open1" and "open2" hooks: These are called with a keywords dict containing
the following entries:

old_c: The commander of the previously open window.
new_c: The commander of the newly opened window.
fileName: The name of the file being opened.

You can use old_c.currentVnode() and new_c.currentVnode() to get the current
vnode in the old and new windows.

Leo calls the "open1" and "open2" hooks only if the file is already open.
Leo will also call the "open1" and "open2" hooks if:
a) a file is opened using the Recent Files menu and
b) the file is not already open.

(5) "@url1" and "@url2" hooks are only executed if "icondclick1" hook returns
None.</t>
<t tx="edream.110203163054.219">See the Code:Customizing Leo:Plugins folder in LeoPy.leo for full details of all plugins.

- Added disabled support for @folder.

- Demoted up/down arrow stuff to a disabled plugin for now.</t>
<t tx="edream.110203163054.220">The idle-time hook now checks for dirty @file nodes that have been modified in an external editor since the last check.  An alert is raised when such conflicting changes are found.

Improved sanitize_filename utility (in leoGlobals.py) so that it converts all characters used to denote filenames to underscores.</t>
<t tx="edream.110203163054.221">This allows output from registering hooks to appear in the log pane.</t>
<t tx="edream.110203163054.222"></t>
<t tx="edream.110203163054.223">The following new plugins are now in LeoPy.leo.

- mod_script_io_to_body.py
	Redirect output from scripts to end of body pane.

- mod_vim.py
	Adds support for VIM editor.

- mod_french_fm.py
	Full translation of all Leo's menus into French.</t>
<t tx="edream.110203163054.224">Added support for the following options:

show_invisibles_space_background_color
show_invisibles_tab_background_color
</t>
<t tx="edream.110203163054.225">This option controls when the control key is considered to start a control-drag.

If look_for_control_drag_on_mouse_down = 1 the the control key must be down when dragging starts.  Otherwise, the control key must be down when dragging ends.</t>
<t tx="edream.110203163054.226">This allows Leo to be used with a black background.</t>
<t tx="edream.110203163054.227">Two new settings in leoConfig.leo/.txt specify the format of the time/date
strings inserted by the Insert Body Time/Date and Insert Headline Time/Date
commands:

body_time_format_string
headline_time_format_string

These settings are really the format string passed to time.strftime(format).

See http://www.python.org/doc/current/lib/module-time.html for a complete list
of the format options. The "%m/%d/%Y %H:%M:%S" format is used by default,
resulting in a time/date format such as: 1/30/2003 8:31:55

</t>
<t tx="edream.110203163054.228"></t>
<t tx="edream.110203163054.229">- if the headline is bracketed (named) then the &lt;&lt; &gt;&gt; are removed.
- if the headline is not bracketed (unnamed) then the &lt;&lt; &gt;&gt; are inserted. 
</t>
<t tx="edream.110203163054.230">The Insert Body Time/Date and Insert Headline Time/Date commands are in the
Edit Body and Edit Headline menus respectively. They insert the formatted time
&amp; date into the body or headline text. You must be editing a headline to be
able to insert the time/date into the headline. If you aren't Leo will say:
"Edit headline to append date/time"

Two new settings in leoConfig.leo/.txt specify the time/date format:

body_time_format_string
headline_time_format_string

These settings are really the format string passed to time.strftime(format).

See http://www.python.org/doc/current/lib/module-time.html for a complete list
of the format options. The "%m/%d/%Y %H:%M:%S" format is used by default,
resulting in a time/date format such as: 1/30/2003 8:31:55</t>
<t tx="edream.110203163054.231">These commands select the first or last node of an outline and make that node visible.</t>
<t tx="edream.110203163054.232">This command selects the parent of the previously selected node and makes that node visible.</t>
<t tx="edream.110203163054.233">These commands select the previous or following sibling of a node and make the newly selected node visible.</t>
<t tx="edream.110203163054.234">This command writes any files (in the presently selected outline) that do not exist.</t>
<t tx="edream.110203163054.235"></t>
<t tx="edream.110203163054.236">This allows time to be expressed as local time or gmttime.</t>
<t tx="edream.110203163054.237"></t>
<t tx="edream.110203163054.238">The Expand To Level n commands now expand only the nodes in the presently selected outline.  This makes these commands much more useful.

With these changes there is no longer any need for the Expand Subheads command.</t>
<t tx="edream.110203163054.239">This can be useful when clones are in the range of different @path directives.</t>
<t tx="edream.110203163054.240"></t>
<t tx="edream.110203163054.241">1. Leo now longer warns when writing customizeLeo.py.

2. Inserted a lock that prevents customizeLeo.py from being written unless use_customize_leo_dot_py = 1 in leoConfig.txt.  Leo writes a message to the log if customizeLeo.py is dirty but was not written because of the setting in leoConfig.txt.
</t>
<t tx="edream.110203163054.242"></t>
<t tx="edream.110203163054.243"></t>
<t tx="edream.110203163054.244"></t>
<t tx="edream.110203163054.245">This makes the file name easier to see in the Windows task bar.
</t>
<t tx="edream.110203163054.246"></t>
<t tx="edream.110203163054.247">This allows Leo to syntax color comments with @language plain.
The @comment directive must follow the @langauge directive.</t>
<t tx="edream.110203163054.248">In other words, the Pressing the Enter key in the Find panel executes the Find Next command.
</t>
<t tx="edream.110203163054.249">The syntax colorer now colors all element tags.  See the example in the child of this node.</t>
<t tx="edream.110203163054.251">- Added "Replace tabs with spaces" checkbox.

- The close button is equivalent to the "Cancel" button rather than the "Ok" button.</t>
<t tx="edream.110203163054.252">This was causing great confusion.</t>
<t tx="edream.110203163054.253"></t>
<t tx="edream.110203163054.254"></t>
<t tx="edream.110203163054.255">- There was a bug that prevented the command from working properly if the line number preceded the present line.

- The goto line number option only works on full path names in @file nodes. 
It does not work for relative paths or in combination with an @path directive.</t>
<t tx="edream.110203163054.256">This problem only arose with languages such as html that have no single-line comment delimiter.
</t>
<t tx="edream.110203163054.257"></t>
<t tx="edream.110203163054.258">Leo did not properly handle configuration settings containing the % character.
</t>
<t tx="edream.110203163054.259"></t>
<t tx="edream.110203163054.260">Double-clicking the icon box used to set the cursor to the hand.
</t>
<t tx="edream.110203163054.261">Every call to v.unjoinNode was calling c.clearAllVistied.

Fixing this bug will allow me not to use inodes &amp; locations for the foreseeable future.</t>
<t tx="edream.110203163054.262"></t>
<t tx="edream.110203163054.263"></t>
<t tx="edream.110203163054.264">In the unusual case that a language has no single-line comment delimiter, Leo will remove the block delimiters from the headline text in node sentinels.  createNthChild must take this into account by doing a second comparison of headlines if the normal comparison fails.  If the second comparison of headlines succeeds we assume that we should use the headline from the outline instead of the derived file.  I believe some kind of kludge like this will also be required for 4.0.</t>
<t tx="edream.110203163054.265">- Translating the "Tangle..." label differently from the "Tangle" one was 
impossible without modifying leo's source code (same thing for "Untangle..." 
and "Untangle").

- Couldn't translate either "Show Invisibles" and "Hide Invisibles". First 
toggle is OK then an error occurs after the second...</t>
<t tx="edream.110203163054.266">- changed copyPart so it returns on @code as well as @c.

- changed convertVnodeToWeb so that it takes account of the "at_root_bodies_start_in_doc_mode" setting.

- For the most part, directives other than @c, @code, @space, @doc, @others get written to the file as @@directive.  There are minor differences between how this is handled in @root and @file trees. This might be considered a bug, and I am not going to do anything unless someone complains loudly.
</t>
<t tx="edream.110203163054.267">Enabling or disabling @language or @comment now recolors entire text.</t>
<t tx="edream.110203163054.268"></t>
<t tx="edream.110203163054.269">I had forgotten to compile leo.nsi.</t>
<t tx="edream.110203163054.270"></t>
<t tx="edream.110203163054.271"></t>
<t tx="edream.110203163054.272">Python 2.3a1 contains a bug in the tkinter code.  This bug has been fixed on Python's cvs site.  Until this bug is fixed in an official Python release Leo must use:

true,false = 1,0

rather than:

true,false = True,False</t>
<t tx="edream.110203163054.273">leo.py 3.10                             December 14, 2002

This version of Leo corrects bugs, improves Leo's documentation and adds many new features:

- Rewrote the Scripting Chapter in Leo's Users Guide.
- Improved the Customization Chapter of the Users Guide.
- Adds several customizations contributed by Leo's users.
  Among these: @read-only nodes. Reading empty .leo files.
  Redirecting stderr and stdout to Leo's log pane.
- New Mark Clones and Go To Next Clone commands.
- New Export Headlines command.
- Control-dragging a node now clones it.
- New "Node Only checkbox in the Find/Change panel.
- @root-code trees start in code mode by default.
  This allows @root trees to work like @file trees.
- @root-doc  trees start in doc  mode by default.
- Converted leoConfig.py to use @root-code
- New at_root_bodies_start_in_doc_mode option in leoConfig.py.
  Specifies whether @root trees work like @root-code or @root-doc.
- New synonyms: @file-asis = @silentfile
  @file-nosent = @nosentinelsfile ; @file-noref = @rawfile.
- Leo now supports navigation of menus using underlined menus.
- Added an easy way to replace any Leo method by a function.
  The code in customizeLeo.py can now override any part of Leo's code!
- Added routines to redirect stderr and stdout to Leo's log pane.
  These routines can be called from customizeLeo.py.
- Added "event1" and "event2" hooks for customize event handling.
- Improved Leo's window icon, and improved how that icon is loaded.
- The usual assortment of bug fixes and minor improvements.
  Actually, this release fixes more than the usual number of bugs.

See the children of this node for full details.

The quote of the month:

I must say I am very impressed. I have been absolutely seduced by Leo over the
past few days. I tell you, I can not put it down. I feel like a kid with a
shiny new bike...I'm already bursting with new ways I'd like to use the tool in
the future -- Lyn Adams Headley</t>
<t tx="edream.110203163054.274"></t>
<t tx="edream.110203163054.275">The old code did not allow &lt;tag /&gt; in many cases.  The new code reads minimal.leo without complaint.  It is:

&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;leo_file&gt;
&lt;leo_header file_format="2" /&gt;
&lt;globals /&gt;
&lt;preferences /&gt;
&lt;find_panel_settings /&gt;
&lt;vnodes /&gt;
&lt;tnodes /&gt;
&lt;/leo_file&gt;
</t>
<t tx="edream.110203163054.276">Apparently the F4 shortcuts interferes with the Alt-F4 shortcut.</t>
<t tx="edream.110203163054.277">The content formerly on evisa.com, including the Leo tutorials is now on 3dtree.com.</t>
<t tx="edream.110203163054.278">Leo improperly added extra blank lines and tabs in @file-nosent trees.</t>
<t tx="edream.110203163054.279">Untangle was warning about a missing section if the section had only an @doc part.</t>
<t tx="edream.110203163054.280">Leo was not handling the class keyword properly.</t>
<t tx="edream.110203163054.281">When leo.py was launched from the command line specifying a non-existent file the message "file not found" was displayed but the outline pane was not drawn properly.</t>
<t tx="edream.110203163054.282">@nosentinelsfile nodes were not being marked dirty properly.

Also, the message in atFile.writeAll about "no @file node found"  did not include these nodes.  The message was generalized.</t>
<t tx="edream.110203163054.283">While scanning for the initial state we must make sure that i &lt; old_len and i &lt; new_len.

Leo was not handling Python ''' strings properly.</t>
<t tx="edream.110203163054.284">It is not correct to do:

	exec s in __builtins__

because that pollutes the namespaces of the __builtin__ module.  Correct is simply:

  exec s in {}</t>
<t tx="edream.110203163054.285">Previous versions of Leo did not properly recycle bindings in the outline pane.

This was reported by David LeBlanc and fixed with major hints from Chad Netzer.
</t>
<t tx="edream.110203163054.286"></t>
<t tx="edream.110203163054.287"></t>
<t tx="edream.110203163054.288">The lambda functions for callbacks were not working properly.</t>
<t tx="edream.110203163054.289">The fix was made to atFile.scanAllDirectives() and leoGlobals.scanDirectives()
tangle.scanAllDirectives() was not affected.

# Reversion fix: 12/06/02: We must use elif here, not if.
elif not old.has_key("language") and dict.has_key("language"):</t>
<t tx="edream.110203163054.290">This bug was created recently by the new underline/realMenuName logic.  We must not set the undo/redoRealMenuName ivars in clearUndoState: that should only be done when actually setting the menu names.</t>
<t tx="edream.110203163054.291"></t>
<t tx="edream.110203163054.292">Both command are enabled only if the presently selected node is a clone.  Mark Clones marks all nodes that are clones of the present node.  Go To Next Clone goes to the next node that is a clone of the present node. A little experimentation convinced me that this command should wrap.  So this command endlessly cycles among the nodes.  Trying to end the this endless cycling would not be easy, as my experience with the Find command shows.

These are straightforward (and surprisingly useful) commands.  Please report any problems immediately.</t>
<t tx="edream.110203163054.293">This works just like the Flatten Outline command except it writes only headlines.</t>
<t tx="edream.110203163054.294">How did I ever live without this.

Also improved messages and fixed a major performance bug: tree.numberOfVisibleNodes was being called repeatedly!</t>
<t tx="edream.110203163054.295">The Node Only checkbox takes precedence over Suboutline Only if they are both checked.</t>
<t tx="edream.110203163054.296">New in Leo 3.10:  Leo allows you to choose whether body text in @root trees will start in code mode or doc mode by default.

@root-doc filename and @root-code filename specify that body text is assumed to start in doc mode or code mode respectively.  The options (-doc and -code) must follow @root immediately with no intervening whitespace.  In effect, @root-code and @root-doc are two new directives.

These @root options override the new at_root_bodies_start_in_doc_mode option in leoConfig.py.  This option affects only @root trees without options.  Such "plain" @root trees are now deprecated, which only means that it is now better style to use either @root-code or @root-doc.  The reason is simple: the meaning of plain @root trees will depend on the at_root_bodies_start_in_doc_mode option, and that isn't good.

By default, at_root_bodies_start_in_doc_mode = 1 for compatibility for old @root trees.  I actually don't think this option is good for much; I created it before I created @root-doc and @root-code, and I decided it wouldn't hurt to leave it in.  Anyway, you now have complete flexibility about how @root works, and in particular you can make @root work just like @file.</t>
<t tx="edream.110203163054.297"></t>
<t tx="edream.110203163054.298">@file-asis is a synonym for @silentfile.
@file-nosent is a synonym for @nosentinelsfile.
@file-noref is a synonym for @norefsfile.</t>
<t tx="edream.110203163054.299">Completed a major revision of the menu handling code to handle underlined menus.  As is typical on Windows, you specify the underlined character by preceding it with an ampersand character.</t>
<t tx="edream.110203163054.300">Created a new icon and improved the code that loads it.</t>
<t tx="edream.110203163054.301">This is the funcToMethod function in customizeLeo.py.</t>
<t tx="edream.110203163054.302">See the relevant section of customizeLeo.py</t>
<t tx="edream.110203163054.303">"event1" and "event2" are generated for many Leo events. keywords.get("kind") returns one of the following for "event1" and "event2" hooks:

"activate",             activate window event   (not uniform across window managers).
"deactivate"            deactivate window event (not uniform across window managers).
"boxClick"              The +- box has been clicked.
"drag"                  Generated repeated while dragging nodes.
"endDrag"               mouseUp that ends a drag.
"headClick"             Left-click in a headline.
"headPopup"             Right-click in a headline.
"headKey"               A keypress in a headline.
"hyperLinkControlClick" Control-click on a hyperlink.
"hyperLinkEnter"        Mouse moves over a hyperlink.       Disabled at present.
"hyperLinkLeave"        Mouse moves away from a hyperlink.  Disabled at present.
"iconDoubleClick"       The icon box has been double-clicked.</t>
<t tx="edream.110203163054.304"></t>
<t tx="edream.110203163054.305"></t>
<t tx="edream.110203163054.306">The present code properly handles undo/redo for operations that copy trees, but copying trees itself causes problems for further undoes.  I've disabled further undos, as was done previously, but this is a pity.

To fix this, we may have to hack on the beads to indicated that a copy has been made.  No doubt about it: copying trees is tricky.</t>
<t tx="edream.110203163054.307">leo.py 3.9                               Nov 23, 2002

This is one of the most interesting versions of Leo ever released:

* Major performance improvements:
  - Incremental syntax coloring speeds response when typing.
  - Incremental undo drastically reduces memory used.

* Major improvements in customizing Leo:
  - Leo looks in the file customizeLeo.py for user-specific customizations.
  - Leo calls "hook routines" in customizeLeo.py for all commands and events.
    These hook routines can modify or replace any command or event.
  - New convenience routines simplify creating and modifying menus.
  - Easy translation of menus to other languages using customizeLeo.py.

* Better integration with other tools:
  - The Open With command allows you to communicate back and forth to other editors.
  - The Go To Line Number command converts lines numbers in derived files
    to locations in the outline.
  - Double-clicking the icon of a @url node launches any url in your web browser.
  - The Execute Script command executes Python code in any body pane.
    This is much more convenient than opening Leo's Idle window.
  - Much better support for cweb. At last, Leo has a power user of cweb.
    By default, @space, @* and @** sections are colored as latex text.
    Leo properly generates @q..@&gt; sentinels.
  - @nosentinelfile is like @file except Leo writes no sentinel lines.

* Other improvements:
  - Optional Emacs-style auto-indent.
  - Reformat Paragraph command.
  - Leo will optionally create nonexistent directories specified in
    @file, @root or @path, including all nonexistent parent directories.
  - Leo will place its own icon in Leo windows provided that you have
    installed Fredrik Lundh's PIL and tkIcon packages.
  - The usual assortment of bug fixes.

See the children of this node for full details.

P.S. Here is what Travers A. Hough recently said about Leo:

"When first I opened Leo, it was out of curiosity.  But having used it...I'LL NEVER GO BACK. THEY'LL HAVE TO PRY LEO OUT OF MY COLD, DEAD FINGERS! Seriously, it should be renamed "Crack Cocaine" because it's that addictive. I'm ready to start a 12-Step group."
</t>
<t tx="edream.110203163054.308"></t>
<t tx="edream.110203163054.309">The cweb prefs panel setting was overriding @language python (!)</t>
<t tx="edream.110203163054.310">@language pascal
@color

private
uses</t>
<t tx="edream.110203163054.311">app().log is now set correctly when there are multiple windows.  Previously, app().log depended on activate events, and was not reliable.  The following routines now set app().log:

- frame.doCommand
- frame.OnMenuClick

Thus, top() will be reliable after any command is executed.  Creating a new window and opening a .leo file also set app().log correctly, so it appears that all holes have now been plugged.

Note: The value of top() may change during a new or open command, which may change the routine used to execute the "command1" and "command2" hooks.  This is not a bug, and hook routines must be aware of this fact.
</t>
<t tx="edream.110203163054.312">Leo no longer massages comments when importing Java files.

There was a bug in massageBody that prevented text from being indented properly.  There was a bug in find_line_start (!!) that caused the start of the previous line to be found if s[i] was a newline.  It's amazing that these bugs were undiscovered for so long.

Treat interface like class.</t>
<t tx="edream.110203163054.313"></t>
<t tx="edream.110203163054.314">Version 3.9 contains many new features and commands.  The children of this node document them.</t>
<t tx="edream.110203163054.315"></t>
<t tx="edream.110203163054.316">Undo now uses incremental syntax coloring.  This speed up undo tremendously.</t>
<t tx="edream.110203163054.317">Previous versions of Leo stored the complete body text whenever any change was made to the body text.  The present version of undo stores only enough information to undo or redo the typing: typically two lines of text.  This results in about a 90% reduction in the memory used by undo.
</t>
<t tx="edream.110203163054.318">These are discussed in the child of this node.</t>
<t tx="edream.110203163054.319">@nocolor

You may customize Leo in several ways:

I.  Using leoSettings.leo

The following information discusses how Leo 4.3 and all later versions handle user configuration settings. For all previous versions, see the node called 'Obsolete: Using leoConfig.leo and leoConfig.txt'

Leo stores options in @settings trees, that is, parts of Leo outlines whose root node has the headline @settings.  When opening a .leo file, Leo looks for @settings trees in the following places:

- The file called leoSettings.leo in the leo/config directory.
- The file called leoSettings.leo in the users home directory.
- The file being loaded.

Settings that later in the above list override settings found earlier. For example, any setting specified in an @settings tree in the file being loaded overrides any setting seen in any leoSettings.leo file.

II. Using plugins and hooks

During startup, Leo looks for plugins, i.e., .py files in the plugins directory.  These plugins register functions called "hooks" to be called a various times during execution.  Full details are provided below.

Plugins provide the following advantages:

- Any time you see a nice hook handler that someone has written you can just copy it to a plugin file and it runs next time you start Leo.
- You don't have to keep updating a large and growing customizeLeo.py file.
- You can disable and enable hooks by renaming the relevant plugin file.
  (or by enabling or disabling the code in the plugin that registers hook functions).
- You don't have to merge code from hooks pertaining to the same Leo event.

When executing any command or handling any event, Leo calls hook routines registered from the plugin files.  The arguments to hooks are:

- "tag", a string telling the kind of command or event about to be executed, and
- "keywords", a Python dictionary whose keys depend on the specific command or event.

This is a very simple, powerful and general mechanism for customizing Leo as you see fit.  There are dozens of kinds of hooks, including the "command1" and "command2" hooks that are called before and after each of Leo's menu commands.  Leo will allow you to override most commands and event handling.  In many cases, if a hook returns any value except None Leo will assume that the hook has completely handled the command or event and will take no further action.  The details will be explained in full below.

Leo catches all exceptions raised in hook code, so you can modify hooks without worry.

SECURITY WARNINGS: Using hooks naively can create the potential for virus-like behavior.  Please read the section called SECURITY WARNINGS for full details.

III. Using convenience routines called from hooks.

Hook routines can import any file in Leo's source code and execute routines in that file.  Leo's contains a number of convenience routines designed to make common customization tasks easier.  Hooks can use these routines to create your own menus, to translate menus into other languages, and to create entries in the Open With menu.  These convenience routines are discussed in detail below.

IV. Setting app().realMenuNameDict inside hooks to translate menus into other languages.

This is discussed below.</t>
<t tx="edream.110203163054.320">@nocolor

Leo will override settings in .leo files if it finds a file called leoConfig.txt in the config subdirectory.  Leo works just as before if it does not find a leoConfig.txt file.

You should make changes to leoConfig.txt by changing leoConfig.leo and then executing the Tangle All command.  There are two advantages to changing leoConfig.txt in this manner.  First, it is just easier to change leoConfig.leo.  Second, all comments are lost in leoConfig.txt when Leo updates it, so using leoConfig.leo as the primary data file means you will always have the comments available.

Leo looks for leoConfig.txt first in the directory specified by the Python variable sys.leo_config_directory.  You would typically set this variable in Python's sitecustomize.py file.  If this variable does not exist, Leo looks in the directory from which Leo was loaded.

The child of this node contains an example of leoConfig.txt that shows all the options that may be set.

Settings in leoConfig.txt overrides preferences in .leo files, but only for those items actually in leoConfig.txt, so you can choose which settings you want to override.  Also, a Leo ignores any setting in leoConfig.txt whose value is "ignore" (without the quotes). For example:

[prefs panel options]
tab_width = ignore

If a setting is overridden, it is _not_ written to the .leo file when the outline is saved.  Note that this does not change the file format: all previous versions of Leo will be able to read such .leo files.

The preceding is probably all you need to know to use leoConfig.txt.  The following discuss some minor details: 

1. When reading a .leo file, if a setting is found neither in leoConfig.txt nor in the .leo file, Leo uses a default, hard-coded value.  In leo.py 3.0 and later these default settings are found in tables that appear in the section called:

	&lt;&lt; define default tables for settings &gt;&gt;

in the file leoConfig.py. So it is now convenient to change settings in leo.py itself as well as in leoConfig.txt.

2. Leo will update leoConfig.txt unless the read_only option is on in leoConfig.txt.  

WARNING: there are problems when Leo does write leoConfig.txt: all comments are lost and options and sections are written in a random order.  This is due to problems in Python's ConfigParser module and will not be changed any time soon.

3. Provided the read_only option is off, Leo updates leoConfig.txt whenever it saves a .leo file or whenever the Preferences panel is closed without being canceled.  When updating leoConfig.txt, Leo will write only existing settings whose value is not "ignore".

4. When Leo saves a .leo file, Leo will write a Preferences setting to the .leo file only if the setting will not be written when updating leoConfig.txt.  In particular, changes made in the Preferences Panel will become permanent immediately if Leo the read_only option is off.  Otherwise the change will become permanent when any .leo file is saved.</t>
<t tx="edream.110203163054.321">Beginning with version 3.11, you may use plugins to customize how Leo works.  You can

- override or modify any command
- add or customize menus or
- translate menus into any language.

Plugins have full access to all of Leo's source code.  In particular, several convenience methods have been added to make customizing menus and commands easier.

Plugins are permanent: they will not go away when Leo is updated.  You can take
advantage of the latest CVS updates _without_ having to throw away your modifications.

Important warning: plugins must avoid blindly executing scripts in .leo files.  Doing so could expose all parts of your computer to malicious Python code.  The section called "Security warnings and precautions" discusses how to customize Leo safely and how to avoid several pitfalls.</t>
<t tx="edream.110203163054.322">What is a plugin?

A plugin is a .py file that appears in Leo's plugin subdirectory. Leo tries to
import all such files while starting up. This is done at "start1" time, that
is, in the call to doHook("start1") in the run function in leo.py. Plugins
exist to define "hook code".

New in 3.11: Leo looks in the plugins folder for .py files. Leo tries to
import all such files at startup ("start2") time.

New in 4.1: Leo enables only plugins whose name appears in pluginsManager.txt.
Leo loads plugins in the order in which they appear in pluginsManager.txt. Leo
loads no plugins if pluginsManager.txt does not exist in the plugins directory.

What is hook code?

Leo automatically calls hook code at various times during Leo's execution.
Typical hooks are:

- "start2", called at the end of Leo's startup process,
- "command1", called before executing any of Leo's commands
- "idle", called at Tk's idle time, when nothing else is happening,

See the documentation for hooks in this file for full details.

N.B. Plugins can use "start2" hooks to override any of Leo's classes. See
"Overriding functions, methods &amp; classes" in leoPlugins.leo for several
examples of how to do this.

How do plugins work?

Plugins register themselves when Leo imports them using the following code,
which should appear as the outer level of the .py file:

@color

"""A description of this plugin"""

registerHandler("xxx", onXXX)
__version__ = "1.2"
plugin_signon(__name__)
	
@nocolor

Line by line:

1) """A description of this plugin"""

This is a Python doc string describing the plugin. This string becomes the
value of the __name__ attribute for the module (.py file).

2) registerHandler("xxx", onXXX)

This line registers a handler called onXXX for the hook called "xxx". See the
documentation for hooks for a complete list of hook names that you can use
instead of "xxx". onXXX is the name of a function or method, presumably defined
in the plugin file, that Leo will call at "xxx" time. For example:

registerHandler("idle",onIdle)

will cause Leo to call the onIdle function at "idle" time.

You can pass a list of hook names as the first argument to registerHandler. For
example:

registerHandler(("bodykey1","bodykey2","headkey1","headkey2"), onKey)

3) __version__ = "1.2"

This assigns a version attribute to module. At present this attribute is used
by the plugin code that creates Leo's Plugins menu.

4) plugin_signon(__name__)

This line increases the count of loaded modules. The present code for
plugin_signon does not actually print separate signons--it seems to verbose.

About hook handlers

See the "About hooks" section of leoPlugins.leo for full documentation about
how to write hook handler routines, like onXXX or onKey in the examples above.
Basically, each hook should have this pattern:
	
@color

def onXXX (tag,keywords):
	c = keywords.get("c")
	otherKeyword = keywords.get("otherKeyword")
	&lt;&lt; do something with c and otherKeyword, etc. &gt;&gt;
	
@nocolor

In other words, keywords is a Python dictionary containing the keyword
arguments passed to the hook handler. See the See the "About hooks" section of
leoPlugins.leo for a list of the keywords passed to each hook handler.

The tag is the name of the hook. For example, tag would one of
"bodykey1","bodykey2","headkey1","headkey2", for the onKey hook handler in the
example above.

What's next?

It's one thing to know how to create a plugin. It's another to know how to
actually change Leo. Obviously, some study is needed. The place to start your
study is LeoPy.leo. In particular, study very carefully the section called
"Overview of code". Leo is a highly modular program, and Python is ideally
suited to this style of programming.</t>
<t tx="edream.110203163054.323">@nocolor

New in 3.11: Leo looks in the plugins folder for .py files. Leo tries to
import all such files at startup ("start2") time.

New in 4.1: Leo enables only plugins whose name appears in pluginsManager.txt.
Leo loads no plugins if pluginsManager.txt does not exist in the plugins directory.

The child of this node gives an example of the code that creates the Open With
menu. The following code, appearing at the end of mod_open_with.py, registers
two different hook functions. The on_idle function is the "idle" hook. The
create_open_with_menu is the "start2","open2" and "command2" hooks.

@color

# Register the handlers... 
registerHandler("idle", on_idle) 
registerHandler(("start2","open2","command2"), create_open_with_menu) 
es("...open with")
	
@nocolor
Plugins may call registerHandler with a hook name like "idle" or a list of hook
names like ("start2","open2","command2"). Also, you can use the "all" hook name
to indicate that code will be called for all hooks. This is useful for tracing
hooks. Plugins may also call registerExclusiveHandler for hooks that should not
be redefined in other plugins.

mod_open_with.py also contains the on_idle and create_open_with functions that
actually handle the hook. Such functions have two arguments: tag and keywords.
You will find many examples of this in LeoPy.leo.

About error checking:

At present Leo will disable all hooks if any hook throws an exception. In
practice this isn't a big deal, but something better could be done.

How to send me your plugins:

It should now be _much_ easier to submit a plugin for inclusion in LeoPy.leo.
Just send me a .leo file containing @file mod_your_plugin.py. Please have this
@file node be @ignored: this is more convenient for me. Ideally, your .leo file
should contain _only_ your plugin code.</t>
<t tx="edream.110203163054.331">Naively using hooks can expose you and your .leo files to malicious attacks.  You will be safe as long as you follow these basic principles:

1. Hooks should _never_ blindly execute Python scripts in .leo files. Blindly executing scripts in .leo files runs the extreme risk of executing malicious code if you ever share any .leo file with someone else.  Moreover, using rexec instead of exec WILL NOT PROTECT YOU.  See the children of this node for further discussion of this important topic.

2. Hooks can execute any code safely _provided_ that all code is contained entirely within the plugin file. If you have a nifty customization that you want to do on a particular .leo file, put that code into a plugin.

3. Use only authentic copies of Leo that come from Leo's SourceForge site.</t>
<t tx="edream.110203163054.332">I'd like to thank Stephen Schaefer for gently insisting that we must guard against malicious code in shared .leo files.  Here is a little story Stephen told on Leo's SourceForge site that makes clear what the danger is:

"I foresee a future in which the majority of leo projects come from marginally trusted sources...I see a world of leo documents sent hither and yon - resumes, project proposals, textbooks, magazines, contracts - and as a race of Pandora's, we cannot resist wanting to see "What's in the box?" And are we going to fire up a text editor to make a detailed examination of the ASCII XML? Never! We're going to double click on the cute leo file icon, and leo will fire up in all its raging glory. Just like Word (and its macros) or Excel (and its macros)."

This succinctly illustrates the fundamental problem: when we share "our" .leo files we can _not_ assume that we know what is our "own" documents.  So hooks that naively searches through .leo files looking for scripts to execute is looking for big trouble.

The following node contains an example of the kind of code that is extremely dangerous.</t>
<t tx="edream.110203163054.333">@color
@ WARNING ***** Using the following routine exposes you to malicious code in .leo files! *****

Do not EVER use code that blindly executes code in .leo files!
Someone could send you malicious code embedded in the .leo file.

WARNING 1: Changing "@onloadpythonscript" to something else will NOT protect
           you if you EVER share either your files with anyone else.

WARNING 2: Replacing exec by rexec below provides NO additional protection!
           A malicious rexec script could trash your .leo file in subtle ways.
@c
if 0: # WRONG: This blindly execute scripts found in an .leo file! NEVER DO THIS!
	def onLoadFile():
		v = top().rootVnode()
		while v:
			h = v.headString().lower()
			if match_word(h,0,"@onloadpythonscript"):
				s = v.bodyString()
				if s and len(s) &gt; 0:
					try: # SECURITY BREACH: s may be malicious!
						exec(s + '\n',__builtins__,__builtins__)
					except:
						es_exception()
			v = v.threadNext()
</t>
<t tx="edream.110203163054.334">@color
@ It would be most foolish to expect rexec to protect you against malicious code contained in .leo files.  Remember that Leo is a repository of source code, so any text operation is potentially malicious.

For example, consider the following script.  This script is valid in rexec mode:
@c

c = top()
thisNode = c.currentVnode()
v = c.rootVnode()
while v:
	&lt;&lt; change all instances of rexec to exec in v's body &gt;&gt;
	v = v.threadNext()
&lt;&lt; delete thisNode &gt;&gt;
&lt;&lt; clear the undo stack &gt;&gt;

@ This script will introduce a security hole the .leo file without doing anything prohibited by rexec, and without leaving any traces of the perpetrating script behind.  The damage will become permanent _outside_ this script when the user saves the .leo file.
</t>
<t tx="edream.110203163054.335">pass</t>
<t tx="edream.110203163054.336">pass</t>
<t tx="edream.110203163054.337">pass</t>
<t tx="edream.110203163054.338">Hooks have full access to all of Leo's source code simply by importing it.

Moreover, several convenience methods have been added to make customizing menus and commands easier.  The following paragraphs discuss these routines and how to use them.

</t>
<t tx="edream.110203163054.339">The following routines enable and disable "idle" hooks.  They are defined in leoGlobals.py.

enableIdleTimeHook(idleTimeDelay=100)

Enables the "idle" hook. After this routine is called Leo will call the "idle" hook approximately every idleTimeDelay milliseconds.  Leo will continue to call the "idle" hook periodically until disableIdleTimeHook() is called.

disableIdleTimeHook()

Disables the "idle" hook.</t>
<t tx="edream.110203163054.340">The following convenience routines make creating menus easier.

These are methods of the leoFrame class.  Use top().frame to get the frame object for the presently active Leo window.

The plugins node in LeoPy.leo gives examples of how to use these routines to create custom menus and to add items to the Open With menu.

These convenience methods all do complete error checking and write messages to the log pane and to the console if errors are encountered.</t>
<t tx="edream.110203163054.341">@nocolor
createMenuItemsFromTable (self,menuName,table,openWith=0)

This method adds items to the menu whose name is menuName.  The table argument describes the entries to be created.  This table is a sequence of items of the form (name,shortcut,command).

- name is the command name
- shortcut is the shortcut, or None to indicate no shortcut.
- command is the routine to execute when the menu item is selected.

An entry of the form ("-",None,None) indicates a separator line between menu items.

For example:
@color
table =
	("Toggle Active Pane","Ctrl-T",self.OnToggleActivePane),
	("-",None,None),
	("Toggle Split Direction",None,self.OnToggleSplitDirection))

top().frame.createMenuItemsFromTable("Window",table)
@nocolor

If the openWith keyword argument is 1 the items are added to a submenu of the Open With menu.  However, it will be more convenient to use the createOpenWithMenuFromTable method to create the Open With menu.
</t>
<t tx="edream.110203163054.342">createNewMenu (self,menuName,parentName="top")

This method creates a new menu:

- menuName is the name of the menu to be created.
- parentName is the name of the parent menu, or "top" if the menu is to created in the menu bar.

This method returns the menu object that was created, or None if there was a problem.  Your code need not remember the value returned by this method.  Instead, your code will refer to menus by name.
</t>
<t tx="edream.110203163054.343">createOpenWithMenuFromTable (self,table)

This method adds items to submenu of the Open With menu item in the File menu.

The table argument describes the entries to be created.  This table is a sequence of items of the form (name,shortcut,data).

- name is the command name
- shortcut is the shortcut, or None to indicate no shortcut.
- data is a tuple of the form (command,arg,ext)
- command is one of "os.system", "os.startfile", "os.spawnl", "os.spawnv" or "exec".
- arg is an argument to be passed to the given command.
- ext is a file extension or None.

When the user selects the Open With item corresponding to the table item Leo executes command(arg).
If ext is not None, the temp file has the given extension.
Otherwise, Leo computes an extension based on what @language directive is in effect.

For example:

table = (
	("Idle",   "Alt+Shift+I",("os.system",idle_arg,".py")),
	("Word",   "Alt+Shift+W",("os.startfile",None,".doc")),
	("Wordpad","Alt+Shift+T",("os.startfile",None,".txt")))

top().frame.createOpenWithMenuFromTable(table)
	</t>
<t tx="edream.110203163054.344">deleteMenu (self,menuName)

Deletes the menu whose name is given, including all entries in the menu.</t>
<t tx="edream.110203163054.345">deleteMenuItem (self,itemName,menuName="top")

Deletes the item whose name is itemName from the menu whose name is menuName.  To delete a menu in the menubar, specify menuName="top".</t>
<t tx="edream.110203163054.346">@nocolor
The leoFrame class creates the Window menu as follows:
@color

windowMenu = self.createNewMenu("&amp;Window")

table = (
	("&amp;Equal Sized Panes","Ctrl-E",self.OnEqualSizedPanes),
	("Toggle &amp;Active Pane","Ctrl-T",self.OnToggleActivePane),
	("Toggle &amp;Split Direction",None,self.OnToggleSplitDirection),
	("-",None,None),
	("Casca&amp;de",None,self.OnCascade),
	("&amp;Minimize All",None,self.OnMinimizeAll),
	("-",None,None),
	("Open &amp;Compare Window",None,self.OnOpenCompareWindow),
	("Open &amp;Python Window","Alt+P",self.OnOpenPythonWindow))

self.createMenuEntries(windowMenu,table)
</t>
<t tx="edream.110203163054.347">@nocolor

It is easy for hooks to translate menus into another language.  For example, code similar to the following code would typically be found in the "start2" hook:

@color

table = (
	("Open...","&amp;Ouvre"),
	("OpenWith","O&amp;uvre Avec..."),
	("close","&amp;Ferme"),
	("Undo Typing","French &amp;Undo Typing"), # Shows you how much French I know ;-)
	("Redo Typing","French &amp;Redo Typing"),
	("Can't Undo", "French Can't Undo"),
	("Can't Redo", "French Can't Redo"))
# Call the convenience routine to do the work.
app().setRealMenuNamesFromTable(table)</t>
<t tx="edream.110203163054.348">New in 4.0: Leo can now read and write "foreign" attributes in &lt;v&gt; and &lt;t&gt; elements in .leo files:

- When reading a .leo file, Leo will create t.unknownAttributes or v.unknownAttributes ivars for any tnode and vnode object whose corresponding &lt;v&gt; or &lt;t&gt; element in the .leo file contains a foreign attribute.

- The unknownAttributes ivars are a dictionary whose keys are the attribute names and whose values are strings.

- When writing a file, Leo will write "foreign" attributes if  a vnode or tnode contains an unknownAttributes ivar.

- The only "native" attributes that Leo expects to find are the "tx" attribute in &lt;t&gt; elements and the "a", "t", "vtag" and "tnodeList" attributes of &lt;v&gt; elements.  Everything else is a foreign attribute.

- Leo performs the usual xml escapes on these strings when reading or writing the unknownAttributes ivars.

Plugins may cause Leo to write such foreign attributes simply by attaching unknownAttributes ivars to a vnode or tnode.  For example:

	v.unknownAttributes = {"vnodeIcon" : pathToIcon}

It would be best not to delete other foreign attributes, so the following would be preferred:

	if hasattr(v,"unknownAttributes"):
		v.unknownAttributes["vnodeIcon"] = pathToIcon
	else:
		v.unknownAttributes = {"vnodeIcon" : pathToIcon}

Another way:

	try:
		v.unknownAttributes["vnodeIcon"] = pathToIcon
	except AttributeError:
		v.unknownAttributes = {"vnodeIcon" : pathToIcon}

See the section called "Recommended conventions for plugins" for advice about how to avoid potential conflicts in naming new attributes.</t>
<t tx="edream.110203163054.349">Leo creates nonexistent directories only if create_nonexistent_directories = 1 in leoConfig.txt.

Previous versions of Leo created a new directory only if its parent directory already existed.  Now, Leo will create all non-existing directories as required.

For example.  Suppose neither dir1 nor dir2 exists.  Leo will create both dir1 and dir1 when it writes the following @file \root\dir1\dir2\spam.py.</t>
<t tx="edream.110203163054.350"></t>
<t tx="edream.110203163054.351">Double-clicking the icon box of a node whose headline has the form:

@url &lt;any url&gt;

executes the url in your default web browser.

Leo checks that the url is valid before doing so. A valid url is:

-- 3 or more lowercase alphas,
-- followed by one ':',
-- followed by one or more of: $%&amp;'()*+,-./0-9:=?@A-Z_a-z{}~
-- followed by one of:         $%&amp;'()*+/0-9:=?@A-Z_a-z}~

Url's should contain no spaces: use %20 to indicate spaces.

You may use any type of url that your browser supports: http,mailto,ftp,file,etc.
</t>
<t tx="edream.110203163054.352"></t>
<t tx="edream.110203163054.353">The present version should be quite usable for its main purpose: tracking
down lines corresponding to error messages. In particular, except for possible
pathological cases, Leo should always put the cursor in the node containing the
referenced line. Possible pathologies involve asking Leo to "go to" a sentinel
line. It won't always be clear what node contains the sentinel.

I am well aware that Leo may not put the cursor on the proper line within
the vnode, but human beings being the excellent pattern matchers that we are,
we should be easily be able to find a line within a node.

Notes in LeoPy.leo, in the node called (Go to line number), discuss a variety
of issues that may cause the cursor not to go to the "proper" line. It also
discusses a better way to position the cursor.

Internally, there are two main versions of this command: one for @silentfile
trees, and one for @rawfile and @file trees. In the first case, there are no
sentinels in the derived file, so Leo just steps through the outline. This is
the easy case, and should work well. In the second case (@rawfile and @file
trees), the derived file contains sentinels, and Leo uses those sentinels to
determine in what vnode the given line occurs.

In this second case, Leo can almost always position the cursor within the
proper node, because Leo just scans back in the derived file looking for the
proper @+node sentinel. However, in order to "count" lines in the derived file
(to place the cursor properly _within_ the body text) Leo must recreate exactly
the logic used by the atFile.read logic, and that isn't easy. Moreover, there
is _no_ guarantee that the derived file is unchanged from when it was written;
after all, if you get syntax errors you tend to want to fix them ;-)

Please do not report bugs in this command, unless the bug involves a
crash, which would be reported both in Leo's log pane and in the console
window. This command will probably be improved in 3.10.</t>
<t tx="edream.110203163054.354">At last Leo has a power user of cweb.  Cweb mode is now fully tested and fully functional.  The following improvements have been made to cweb mode:

1. Corrected sentinels used in cweb mode.

Leo must double _all_ @ signs following the @q@. For example, an @@color sentinel gets turned into @q@@@@@color@&gt;.

2. Leo colors cweb doc parts and C comments in LaTex mode by default.

In cweb mode Leo colors @space, @* and @** sections using LaTeX coloring by default.  The color_cweb_doc_parts_with_latex option in leoConfig.py/.txt affects this default.

Similarly, Leo colors C comments in cweb mode using LaTeX coloring by default. The color_cweb_comments_with_latex option in leoConfig.py/.txt affects this default.

3. Cweb mode works similarly in @file and @root trees.

See the child of this node for full details about cweb mode.
</t>
<t tx="edream.110203163054.355">Cweb mode refers to how Leo tangles an outline when @language cweb is in effect or the cweb option in the Settings Panel is in effect.

Leo treats _all_ cweb code in cweb mode as unevaluated text.  That is, Leo treats cweb control codes, including @&lt;...@&gt;, @&lt;...@&gt;=, @c, @space, @* and @** as "raw" text within cweb mode.  Leo does _not_ expand _cweb_ section references when writing derived files in cweb mode.  However, Leo _does_ expand _noweb_ section references, so you may use noweb sections to organize cweb files! You can create _noweb_ code and doc sections using the @code and @doc directives in place of @c and @space directives.

By default, cweb colors @space, @* and @** sections using the same syntax coloring as for LaTeX.  In addition, cweb colors C // and /*..*/ comments using LaTeX coloring by default.  You may change these defaults using the color_cweb_doc_parts_with_latex and color_cweb_comments_with_latex options in leoConfig.py.</t>
<t tx="edream.110203163054.356">The Open With command allows you to communicate with external editor.  When you select this command Leo creates a temporary file and invokes an external program.  Leo periodically checks whether this temporary file has changed; Leo changes the corresponding node in the outline if so.

You must create the entries in the Open With submenu. This would typically be done in a hook routine, using the createOpenWithMenuFromTable routine described in the child of this node.

The @file mod_open_with.py node in LeoPy.leo gives a complete example of handling the Open With menu.</t>
<t tx="edream.110203163054.357">Leo now supports optional Emacs-style auto-indent.  This style of auto-indent aligns newly created lines with unmatched ( [ or { brackets in the previous line. This feature is enabled only if smart_auto_indent = 1 in leoConfig.txt.

This code was contributed by David McNab, david@rebirthing.co.nz.</t>
<t tx="edream.110203163054.358">New in leo.py v3.9

Whether importing text from an outside source, typing in text, or modifying text, eventually you end up with a block of text in which some lines are too long and some are too short.  The Reformat Paragraph command will rearrange the words in a text paragraph to fill each line as full as possible, up to the @pagewidth setting.

A paragraph is delimited by blank lines, Leo directives, and (of course) start and end of text in a node.  The width of the line used by the reformatting operation is governed by @pagewidth and the indentation that would be applied to the node when tangled (as part of a @root) or written (as part of a @file).

The command operates on the paragraph containing the insert cursor.  If the insert cursor is on a blank line or directive, nothing happens.  If the cursor is on a line containing text, then the paragraph containing that text line is reformatted and the insert cursor is moved to the next paragraph.

Be careful that you don't do this on source code!  Of course, if you do reformat something that should have been left alone, then just Undo.

NOTE: Lines with hanging indentation are handled so that the hanging indentation is preserved.  This is most useful for bulleted or numbered lists, such as:

  1. This is the first paragraph, and
     it has a hanging indentation.

  2. This is the second paragraph, and
     it too has a hanging indentation.</t>
<t tx="edream.110203163054.359">An @rawfile tree is a tree whose root headline starts with @rawfile &lt;filename&gt;.  Similarly, for @silentfile and @nosentinelsfile trees.

Leo creates files derived from @file and @nosentinelsfile trees in exactly the same way.  The _only_ difference is that files derived from @file trees contain sentinels, while files derived from @nosentinelsfile trees do not.  Therefore, Leo can not update outlines from changed made from files derived from @nosentinelfile trees.

Leo creates files derived from @rawfile and @silentfile trees by writing the body text of all nodes of the tree in outline order.  Leo writes the body text _as is_, without recognizing section definitions, without expanding section references, and without treating directives specially in any way.  In particular, Leo copies all directives, including @space or @c directives, to the derived file as text. However, Leo recognizes the @ignore directive in the _ancestors_ of @rawfile or @silentfile nodes, so you may use the @ignore directive as usual to prevent Leo from writing @rawfile and @silentfile trees.

There are several difference between @rawfile and @silentfile trees:

1. Leo writes no sentinel lines when writing @silentfile trees.  When writing @rawfile trees, Leo writes only the @+leo, @-leo, @+node, @-node, @+body and @-body sentinels. Therefore, Leo can update @rawfile trees, but _not_ @silentfile trees from changes made in derived files. Unlike @file and @rawfile trees, the primary source of information for an @silentfile tree is the outline containing it.

2. Within @silentfile trees only, if a headline starts with @@, Leo writes everything in the headline following the @@ just before the corresponding body text.

3. Files derived from @silentfile trees contain _nothing_ not contained in body text (or @@ headlines).  In particular, if body text does not end in a newline, the first line from the next node will concatenated to the last line of the preceding node.

In short, you can get any combination of sentinels/no sentinels and references/no references using @file, @nosentinelsfile, @rawfile and @silentfile trees.  This is shown in the following table:

                     Derived files        Sections and 
    Type of tree   contain sentinels?   @others expanded?
    ------------   ------------------   -----------------
           @file   yes                  yes
@nosentinelsfile   no                   yes
        @rawfile   yes                  no
     @silentfile   no                   no

New in Leo 3.10:

@file-asis is a synonym for @silentfile.
@file-nosent is a synonym for @nosentinelsfile.
@file-noref is a synonym for @rawfile.
</t>
<t tx="edream.110203163054.360">leo.py 3.8                               October 29, 2002

Many major improvements have been made to Leo, all made as the result of user requests:

- New @rawfile and @silentfile trees complement @file trees.
  @rawfile and @silentfile trees create derived files without using sections.
  @rawfile files contain only those sentinels needed to automatically untangle them.
  @silentfile trees contain no sentinels at all.
- New @raw and @end_raw directives allow unformatted code within @file trees.
- Much better support for CWEB.  You may organize .w files using noweb!
- The @comment and @language directives may now apply simultaneously.
- Leo can now read, remember and write &lt;?xml-stylesheet...?&gt; lines,
  under control of the new stylesheet option.
- The new output_newline option specifies the line endings used when writing files.
- The new output_initial_comment option specifies the text to appear
  in an @comment sentinel at the start of each derived file.
- New commands in the help menu make it much easier to change configuration options.
- Dozens of minor improvements and bug fixes.

This month Dave Hein and I discovered how to uniquely and permanently identify nodes, regardless of where those nodes are located and regardless of how many people are working simultaneously on them.  This discovery will greatly improve Leo, and will simplify how people use Leo with CVS.  Leo 4.0, due out in a month or two, will be the first version of Leo to use this breakthrough.

See the children of this node for full details.
</t>
<t tx="edream.110203163054.361"></t>
<t tx="edream.110203163054.362"></t>
<t tx="edream.110203163054.363">The warning for "unknown language" had an unbound var.</t>
<t tx="edream.110203163054.366"></t>
<t tx="edream.110203163054.368">Leo now properly handles @delims directives in @file trees.</t>
<t tx="edream.110203163054.369">Leo now properly recognizes all sentinel lines when @language cweb is in effect.</t>
<t tx="edream.110203163054.370">Fixed a bug that caused Leo to say "methods" rather than "functions" when importing C code.

Leo now adds @root &lt;filename&gt; statement when importing to @root nodes.</t>
<t tx="edream.110203163054.371"></t>
<t tx="edream.110203163054.372"></t>
<t tx="edream.110203163054.373"></t>
<t tx="edream.110203163054.374"></t>
<t tx="edream.110203163054.375">Previously, Java only had block comments, and the ending delim wasn't being removed from doc parts.</t>
<t tx="edream.110203163054.376"></t>
<t tx="edream.110203163054.377">The present code explicitly eliminates control-T processing in headlines, which means that control-T does not switch panes when editing headline text.  Control-T _does_ switch panes in all other cases.

This appears to be another Tk bug.</t>
<t tx="edream.110203163054.378">Only shortcut pastes worked before.</t>
<t tx="edream.110203163054.379"></t>
<t tx="edream.110203163054.380">Leo 3.7 significantly offers you several new ways to create derived files.</t>
<t tx="edream.110203163054.381">@rawfile and @silentfile trees are important new additions to Leo.  They work like @file trees, but are simpler to use.  See the child of this node for full details.</t>
<t tx="edream.110203163054.382">The @raw and @end_raw directives delimit a region of "raw" text.  No section references are recognized within "raw" text, and no additional leading whitespace is generated within "raw" text when writing the derived file.

The @quiet directive is valid only within @root trees.  It suppresses all sentinels except the @+node sentinels used to mark headlines.

See the children of this node for full details.</t>
<t tx="edream.110203163054.383">The @raw and @end_raw directives are valid only within @file trees.  The @raw directive starts a section of "raw" text.  The @end_raw directive ends such a section, as does the end of body text. No section references are recognized within "raw" text, and no additional leading whitespace is generated within "raw" text when writing the derived file.
</t>
<t tx="edream.110203163054.384">The @verbose, @terse, @quiet and @silent directives determine how the Tangle command outputs comments in @root trees.  Comments written by the user in code sections are always output: these directives control only: a) the comments containing doc sections and b) sentinel comments that delimit the beginning and end of code sections.

When @verbose is in effect Tangle outputs all comments. When @terse is in effect, Tangle outputs only those comments necessary for Untangle to work. When @silent is in effect Tangle adds no additional comments.  The @quiet directive is like @silent except that it does output leading sentinels as comments. Like @silent, @quiet inhibits untangling. 

@verbose is the default. If more than one of these directives appear in the same body text the "most verbose" of these options will be in effect.</t>
<t tx="edream.110203163054.385">It is now possible to create CWEB (.w) files from @file trees.  When @language cweb is in effect the following happen:

1. Leo does not recognize @space and @c directives.

2. The colorizer now recognizes both cweb and noweb section definitions and references.

3. Leo uses @q@ and @&gt; for comment delimiters in files derived from @file or @rawfile trees, and Leo replaces @ by @@ within such comments.

4. Leo now properly warns about orphan nodes when @langauge cweb was in effect.

See the child of this node for the new documentation that applies to cweb mode.</t>
<t tx="edream.110203163054.386">It is now possible to have both the @comment and @language directives to be in effect at the same time.  To do this, both directives must appear in the same node, and the @comment directive must follow the @language directive.</t>
<t tx="edream.110203163054.387"></t>
<t tx="edream.110203163054.388">Leo preserves the &lt;?xml-stylesheet...?&gt; line if it is already present in the .leo file.

Otherwise, Leo writes a &lt;?xml-stylesheet...?&gt; line only if the stylesheet option is present in the configuration file.  The stylesheet option specifies s in &lt;?xml-stylesheet s?&gt;</t>
<t tx="edream.110203163054.389">The Open LeoConfig.leo command opens the configuration file.  The apply setting command applies any changes to settings made as the result of changing leoConfig.leo.</t>
<t tx="edream.110203163054.390">This option allows a comment to be inserted in derived files just after the initial @+leo line.  The comment will appear in an @comment sentinel.  See leoConfig.leo for full details.</t>
<t tx="edream.110203163054.391">This option allows you to specify the line endings to be used when writing derived files and when exporting files.  See leoConfig.leo for full details.</t>
<t tx="edream.110203163054.392">Changed the path_directive_creates_directories option in leoConfig.leo to create_nonexistent_directories.

The old name was too misleading.  Indeed, this option applies not just to @path directives, but to all situations in which the path name specified in @path directives or @root, @file, @rawfile or @silentfile nodes does not exist.

</t>
<t tx="edream.110203163054.393"></t>
<t tx="edream.110203163054.394"></t>
<t tx="edream.110203163054.395"></t>
<t tx="edream.110203163054.396">The new names are less cluttered than the old.</t>
<t tx="edream.110203163054.397">Leo now prints a summary of any exception taken to the log window, and a full traceback to the console window.</t>
<t tx="edream.110203163054.398">This is taken from Python Cookbook.

This may be of use to people developing Leo, though it's not clear how useful this is with Tk programs.</t>
<t tx="edream.110203163054.399">A small convenience that is actually quite nice to have.</t>
<t tx="edream.110203163054.400">Sentinel lines in Java files now start with //@.</t>
<t tx="edream.110203163054.401">It wasn't always completely clear when the command was complete.</t>
<t tx="edream.110203163054.402">Recently I have discovered a way of creating true, immutable global identifiers (called global tnode indices or gti's for short).  Version 4.0, due late this year or early next, will be the first version of Leo to take full advantage of the opportunities created by gti's.

Gti's will be a way of permanently and uniquely identifying every node (headline and body text) ever created by Leo, even when many people are working on the same .leo and derived files.  For the first time, Leo will be able reliably to associate nodes in .leo files with nodes in derived files.

No previous version of Leo, including 3.7, has this ability, although that may not be so apparent to the casual user.  As a work around in all previous versions of Leo, .leo files contain copies of all information in derived files.  This "mirroring scheme" is needed so that clones in .leo files can be associated with their cloned counterparts in derived files.

While the mirroring scheme usually works well, it has some significant problems:

1. .leo files are much larger than they need to be.

2. Read errors occur if the derived files get out-of-synch with the information in the .leo file.  All clone links get broken when read errors occur, which basically ruins the resulting .leo file.  The only real way to recover is to use the Read Outline Only command.

3. Because out-of-synch conditions are so serious, it becomes a dicey proposition to save .leo files as backups; to create a reliable backup one must save the leo file along with all derived files.

Gti's solve all these problems:

1. .leo files no longer need to save a copy of all information in all derived files.  Leo will write only the root node of @file trees to the outline, secure in the knowledge that it can reliably recreate the outline from the derived file.

2. The dreaded read errors will be impossible because there is no longer any data in the .leo file that can become out-of-synch with data in the derived files.

3. Because .leo files can never become out-of-synch with derived files, we can, for the first time, safely backup a project by creating a "fat" .leo file that contains all information in all derived files.  Most .leo files will be "thin."  Saving "fat" .leo files will only happen as the result of a new Save Backup
command. 

I am excited about Leo 4.0.  It promises to revolutionize how people use Leo.</t>
<t tx="edream.110203163054.403">leo.py 3.7                                 October 9, 2002

Many improvements have been made to Leo.  The highlights:

- Now works with Python 2.1.  Previous versions required Python 2.2.
- Many new user options, including user-definable shortcuts for all commands
  and colors for all parts of Leo's windows.
  As a result, it is now possible to use arrow keys as you desire.
- Minimal support for Unicode Latin-1 (iso-8859-1) encoding. Better support is coming.
- Improved handling of relative path names.
- The @first directive allows lines to precede the opening @+leo sentinel line.
- The @last  directive allows lines to follow  the closing @-leo sentinel line.
- Better support for Perl+pod.
- Leo now ends all lines with '\n' regardless of platform.
- Leo is now compatible with Python 2.1.
- Simplified sentinels reduce spurious CVS diffs.
- Many other minor improvements and bug fixes.

Warning: Leo expects that all characters in derived files and .leo files are contained in the encoding specified by the xml_version_string option in leoConfig.txt.  Characters will be garbled if this restriction is not followed.  This restriction will be removed in the next release.

See the children of this node for full details.</t>
<t tx="edream.110203163054.404"></t>
<t tx="edream.110203163054.405"></t>
<t tx="edream.110203163054.406">The old code did not handle @comment /* */ in C mode because the */ given in the comment improperly terminated the scanning.

Changed find to rfind when scanning @@ sentinels.</t>
<t tx="edream.110203163054.407"></t>
<t tx="edream.110203163054.408">Under certain circumstances # was not properly colored when coloring plain text.</t>
<t tx="edream.110203163054.409">single quote colorized text in plain text mode.  This was due to missing parentheses.</t>
<t tx="edream.110203163054.410">The old code did not properly set the text selection in all cases.

This bug affected the Indent, Unindent, Extract and Extract Section.</t>
<t tx="edream.110203163054.411"></t>
<t tx="edream.110203163054.412">Body text was being cleared in a node in an @file tree if the node contained a reference to a section defined in a grandchild.  This was the first serious bug ever reported in the @file read logic.

The problem: Body text was being updated as the result of @+node sentinels rather than @+body sentinels.
This was wrong, as extra @+node sentinels are often generated when no body text is generated. The result is
that the body text was being cleared. 

The fix: I simply moved the code that creates body text from the @+node logic to the @+body logic in
scanText.</t>
<t tx="edream.110203163054.413">The new code resets the error count when reading each derived file, so errors in one file do not cascade to following derived files.</t>
<t tx="edream.110203163054.414"></t>
<t tx="edream.110203163054.415"></t>
<t tx="edream.110203163054.416">st_enter was not returning part numbers, which would have affected the Untangle command.</t>
<t tx="edream.110203163054.417">The old code undid the changes to only one headline of a group of cloned nodes. This was a serious bug because it would destroy the assumed equality between all cloned headlines.</t>
<t tx="edream.110203163054.418">The Find Previous command would get stuck once it found a match.</t>
<t tx="edream.110203163054.419">The original bug report:

"If you set the @tabwidth to something other than the Preference value, you'll see the body displayed appropriately. However, if you do a Ctrl-s to save the leo file, the body is redisplayed using the Preferences setting--of course, clicking on another node and then back to the original node displays with the correct tab setting again."</t>
<t tx="edream.110203163054.420">The old code remembered the insertion point only if it were set as the result of a keystroke.
</t>
<t tx="edream.110203163054.421">This was too confusing to users.  setup.py is intended only to create official distributions.</t>
<t tx="edream.110203163054.422">These improvements are listed in the approximate order of importance.</t>
<t tx="edream.110203163054.423"></t>
<t tx="edream.110203163054.424"></t>
<t tx="edream.110203163054.425">path_directive_creates_directories

Specifies whether to create a directory mentioned in an @file, @root node or @path directive if it does not exist.</t>
<t tx="edream.110203163054.426">relative_path_base_directory 

The directory to be used as a prefix for &lt;filename&gt; in @path &lt;filename&gt; and @file &lt;filename&gt; and @root &lt;filename&gt; when &lt;filename&gt; is a relative path.

Valid values for this option:

"!" means relative to the location leo.py (the default).
"." means relative to the location of the .leo file in the top window.
An absolute path (in platform-dependent format).

Relative paths are not allowed: such paths would be dangerous because their meaning would depend on the changing value of the current working directory.</t>
<t tx="edream.110203163054.427">remove_sentinels_extension

Sets the string to be appended to file names resulting from the Remove Sentinels command.  If the value starts with . the extension is appended to the original file name. Otherwise, the extension is appended before the file extension.

Example 1:
	File name x.y
	remove_sentinels_extension = _ns
	Result: x_ns.y

Example 2:
	File name x.y
	remove_sentinels_extension = .txt
	Result: x.y.txt
</t>
<t tx="edream.110203163054.428">write_clone_indices 

Indicates whether derived files will contain clone indices.

Please specify no clone indices if you are going to submit files to Leo's CVS site.</t>
<t tx="edream.110203163054.429">The following options now exist in the &lt;&lt; Options for newly opened windows &gt;&gt; section of LeoConfig.leo.

initial_horizontal_secondary_ratio

Sets the ratio of outline pane size to log pane size when splitting the primary panes horizontally.
The primary panes are the body pane and the secondary pane.

initial_vertical_secondary_ratio

Sets the ratio of tree pane size to body pane size when splitting the primary panes vertically.
The primary panes are the body pane and the secondary pane.


</t>
<t tx="edream.110203163054.430">The following options now exist in the &lt;&lt; Window options &gt;&gt; section of LeoConfig.leo.

body_text_foreground_color
body_text_background_color

The foreground and background colors of body text.

body_cursor_foreground_color
body_cursor_background_color

The foreground and background colors for the cursor in body text.

headline_text_unselected_foreground_color
headline_text_unselected_background_color

The foreground and background colors of unselected headline text.
Both must be specified for either to take effect.

headline_text_selected_foreground_color 
headline_text_selected_background_color

The foreground and background colors of selected headline text that is not being edited.
Both must be specified for either to take effect.

headline_text_editing_foreground_color
headline_text_editing_background_color

The foreground and background colors of unselected headline text in a headline that is being edited.
Both must be specified for either to take effect.

headline_text_editing_selection_foreground_color
headline_text_editing_selection_background_color

The foreground and background colors of selected text headline text in a headline that is being edited.
Both must be specified for either to take effect.

outline_pane_background_color

The background color of outline pane itself.

log_text_foreground_color
log_text_background_color

The foreground and background colors of log text.</t>
<t tx="edream.110203163054.431">The &lt;&lt; Keyboard shortcuts settings &gt;&gt; section of leoConfig.leo allows the user to specify keyboard shortcuts for all commands.

Notes:

1. There is one option for every command in Leo's menus; they won't be listed separately here.

2. For full documentation, see the

&lt;&lt; Keyboard shortcuts settings &gt;&gt; and
&lt;&lt; About keyboard shortcuts &gt;&gt;

sections of leoConfig.leo.  The gist of this documentation is that you must use names known to Tk, and Leo also provides a few other names.

3. At most one shortcut may be associated with a command.  If one really wanted to have two shortcuts, one would have to use two different command names. In particular, there is now only one shortcut for the Find Next command.
</t>
<t tx="edream.110203163054.432">Leo checks all characters that are entered (via typing or via paste) into headline and body text to see whether they can be represented in the encoding specified by the xml_version_string setting in leoConfig.txt.  Leo issues a message and disallows the entry of the character if it can't be represented in that encoding.

This draconian behavior shouldn't be too much of a nuisance, at least temporarily. Note that _all_ characters are valid in the UTF-8 encoding, so the present version of Leo will allow you to specify all characters if you must. But the Latin-1 (iso-8859-1) encoding, being a one-byte encoding, limits you to at most 256 separate characters. 

In 3.8 I plan to allow you to use all Unicode characters, regardless of encoding, by using character references.  This will require some reorganization of the present code, and I don't want to delay 3.7 to handle them.

Warning: The present code does not handle well files (.leo or derived files) that contain characters outside the specified encoding.  At present, your best bet is to remove such characters for now.  Hopefully 3.8 will do a much better job handling characters "foreign" to the specified encoding.</t>
<t tx="edream.110203163054.433">Leo now writes only \n (Linux newlines) in derived files and .leo files.  This was done simply by opening derived files and .leo files in "wb" mode.</t>
<t tx="edream.110203163054.434"></t>
<t tx="edream.110203163054.435">1. Leo now supports relative_path_base_directory and path_directive_creates_directories user options.  See the discussion of those options in this document.

2. Leo now retains file modes when tangling and writing derived files.</t>
<t tx="edream.110203163054.436">Blank lines now precede and follow =pod and =cut.

Improvements made to @first and @last directives.</t>
<t tx="edream.110203163054.437">These were added so to resolve the debate about what the Esc key should do.  The user can now bind Esc to either of these commands.</t>
<t tx="edream.110203163054.438">Leo no longer gives an error message when reading or writing cloned @file nodes.</t>
<t tx="edream.110203163054.439"></t>
<t tx="edream.110203163054.440">Leo writes derived files a bit differently than before.  These changes are compatible with the Borland version of Leo, provided that xml_version_string = UTF-8 in leoConfig.txt.

The changes:

1. Eliminated writing clone indices in derived files.  This reduces the number of spurious changes reported by CVS.  Leo now relies solely on information in .leo files to recreate clone indices.  This is safe because read errors clear clone indices anyway.  You can force clone indices to be written using the write_clone_indices user option in leoConfig.txt.

2. Removed extra newline following @+leo directive.  This is part of an unfinished plan to eliminate all extra blank lines in derived files.  It's not clear whether this plan will ever succeed.</t>
<t tx="edream.110203163054.441">Leo enables the Tangle and Untangle items in popup menus if any descendant of the selected node contains an @root node.  Similarly, Leo enables the Read @file nodes and Write @file nodes items in popup menus if any descendant of the selected node contains an @file node.</t>
<t tx="edream.110203163054.442"></t>
<t tx="edream.110203163054.443">leo.py 3.6                                 September 11, 2002

Highlights:

- Fixed a large number of bugs, especially bugs that appear only on Linux.
- Leo now remembers the previous insertion point and location of the scrollbar when switching between nodes.
- Added Match Brackets command.
- Added support for MouseWheel (Linux only).
- Added support for LaTex and PHP.
- Improved all aspects of the Help menu.
- Discovered a minor bug involving the Python (Idle) window and documented a workaround.

See the children of this node for full details.</t>
<t tx="edream.110203163054.444">The following minor bug can not easily be fixed because it involves an interaction between Leo and Idle.

After opening Idle with the Open Python Window command, opening another Leo window shows both the Leo window and a blank, square window.  Closing either of the new windows may cause exceptions, either immediately or later.

The best workaround is simply not to open any new Leo windows after using the Open Python Window command.</t>
<t tx="edream.110203163054.445"></t>
<t tx="edream.110203163054.446"></t>
<t tx="edream.110203163054.447">os.rename can fail on some Linux systems.</t>
<t tx="edream.110203163054.448">When starting Leo with no arguments the 'NewHeadline' node was not displayed. </t>
<t tx="edream.110203163054.449">Changed:

bitmap_name = os.path.join(self.loadDir,"Icons\LeoApp.ico") 

to:

bitmap_name = os.path.join(self.loadDir,"Icons","LeoApp.ico") 
</t>
<t tx="edream.110203163054.450">There were problems handling relative path names in @root and @path directives.</t>
<t tx="edream.110203163054.451">With Tk/Tcl 8.4, the Preferences window is empty (no buttons, fields, labels). 

Tcl 8.4 complains about using "col" in the grid() calls.</t>
<t tx="edream.110203163054.452">This routine does a better job of checking the Tk version than the old code in leoApp.py</t>
<t tx="edream.110203163054.453"></t>
<t tx="edream.110203163054.454">Only the last directive was in effect in @root trees.  The new code allows node-by-node control.</t>
<t tx="edream.110203163054.455">This involved calling readlineForceUnixNewline instead of readline in the atFile:read logic.</t>
<t tx="edream.110203163054.456"></t>
<t tx="edream.110203163054.457">How did I ever live without this?</t>
<t tx="edream.110203163054.458"></t>
<t tx="edream.110203163054.459">The cursor now changes to an arrow when it moves over a link in the About Leo dialog.

The About Leo dialog now includes a build revision number.

Fixed problems with the Leo icon in the About Leo dialog.

Improved download dialog in Tutorial command.</t>
<t tx="edream.110203163054.460">CVS conflict files produce so many error messages that these errors are useless.</t>
<t tx="edream.110203163054.461"></t>
<t tx="edream.110203163054.462"></t>
<t tx="edream.110203163054.463"></t>
<t tx="edream.110203163054.464">The Match Brackets command is enabled if the cursor is next to one of the following characters in the body pane:

( ) [ ] { } &lt; &gt;

This command looks for the matching character, searching backwards through the body text if the cursor is next to ) ] } or &gt; and searching forward through the text otherwise.  If the cursor is between two brackets the search is made for the bracket matching the leftmost bracket.

If a match is found, the entire range of characters delimited by the brackets is highlighted and the cursor is placed just to the left of the matching characters.  Thus, executing this command twice highlights the range of matched characters without changing the cursor.</t>
<t tx="edream.110203163054.465">This code is due to Dave Hein.

Leo understands the following PHP keywords:

&lt;?php, ?&gt;, __CLASS__, __FILE__, __FUNCTION__, __LINE__, and,	as, break, case, cfunction, class, const, continue, declare, default, do, else, elseif,  enddeclare, endfor, endforeach, endif, endswitch, endwhile, eval,  extends, for, foreach, function, global, if, new, old_function, or, static, switch, unset(), use, var, while, xor,

Leo does not yet color the following keywords containing():

array(), die(), echo(), empty(), exit(), include(), include_once(), isset(), list(), print(), require(), require_once(), return()</t>
<t tx="edream.110203163054.466">This code is due to Marcus A. Martin.

Leo understands the following LaTex keywords: capitalization is significant.  For example, \vert produces a single vertical line and \Vert produces a double vertical line.

\@, \(, \), \{, \},

\acute, \addcontentsline, \addtocontents, \addtocounter, \address,
\addtolength, \addvspace, \AE, \ae, \aleph, \alph, \angle, \appendix, 
\approx,\arabic, \arccos, \arcsin, \arctan, \ast, \author,

\b, \backmatter, \backslash, \bar, \baselineskip, \baselinestretch,
\begin, \beta, \bezier, \bf, \bfseries, \bibitem, \bigcap, 
\bigcup, \bigodot, \bigoplus, \bigotimes, \bigskip, \biguplus, 
\bigvee, \bigwedge,\bmod, \boldmath, \Box, \breve, \bullet,

\c, \cal, \caption, \cdot, \cdots, \centering, \chapter, 
\check, \chi, \circ, \circle, \cite, \cleardoublepage, \clearpage, 
\cline,\closing, \clubsuit, \coprod, \copywright, \cos, \cosh, 
\cot, \coth,csc,

\d, \dag, \dashbox, \date, \ddag, \ddot, \ddots, \decl, 
\deg, \Delta, \delta, \depthits, \det, 
\DH, \dh, \Diamond, \diamondsuit, \dim, \div, \DJ, \dj, 
\documentclass, \documentstyle, \dot, \dotfil, \downarrow,

\ell, \em, \emph, \end, \enlargethispage, \ensuremath, 
\enumi, \enuii, \enumiii, \enuiv, \epsilon, \equation, \equiv,
\eta, \example, \exists, \exp,

\fbox, \figure, \flat, \flushbottom, \fnsymbol, \footnote, 
\footnotemark, \fotenotesize, 
\footnotetext, \forall, \frac, \frame, \framebox, \frenchspacing, 
\frontmatter,

\Gamma, \gamma, \gcd, \geq, \gg, \grave, \guillemotleft, 
\guillemotright,\guilsinglleft, \guilsinglright,

\H, \hat, \hbar, \heartsuit, \heightits, \hfill, \hline, \hom, \hrulefill,\hspace, \huge,\Huge,\hyphenation

\Im, \imath, \include, includeonly, indent, \index, \inf, \infty, \input, \int, \iota,\it, \item, \itshape,

\jmath, \Join,

\k, \kappa, \ker, \kill,

\label, \Lambda, \lambda, \langle, \large, \Large, \LARGE, 
\LaTeX, \LaTeXe, 
\ldots, \leadsto, \left, \Leftarrow, \leftarrow, \lefteqn, \leq,
\lg, \lhd, \lim, \liminf, \limsup, \line, \linebreak, 
\linethickness, \linewidth,\listfiles,
\ll, \ln, \location, \log, \Longleftarrow, \longleftarrow, 
\Longrightarrow,longrightarrow,

\mainmatter, \makebox, \makeglossary, \makeindex,\maketitle, \markboth, \markright,
\mathbf, \mathcal, \mathit, \mathnormal, \mathop,
\mathrm, \mathsf, \mathtt, \max, \mbox, \mdseries, \medskip,
\mho, \min, \mp, \mpfootnote, \mu, \multicolumn, \multiput,

\nabla, \natural, \nearrow, \neq, \newcommand, \newcounter, 
\newenvironment, \newfont,
\newlength,\newline, \newpage, \newsavebox, \newtheorem, \NG, \ng,
\nocite, \noindent, \nolinbreak, \nopagebreak, \normalsize,
\not, \nu, nwarrow,

\Omega, \omega, \onecolumn, \oint, \opening, \oval, 
\overbrace, \overline,

\P, \page, \pagebreak, \pagenumbering, \pageref, \pagestyle, 
\par, \parbox,\paragraph, \parindent, \parskip, \part, 
\partial, \per, \Phi, \phi,\Pi, \pi, \pm, 
\pmod, \pounds, \prime, \printindex, \prod, \propto, \protext, 
\providecomamnd, \Psi,\psi, \put,

\qbezier, \quoteblbase, \quotesinglbase,

\r, \raggedbottom, \raggedleft, \raggedright, \raisebox, \rangle, 
\Re, \ref, \renewcommand, \renewenvironment, \rhd, \rho, \right, 
\Rightarrow,\rightarrow, \rm, \rmfamily,
\Roman, \roman, \rule, 

\s, \samepage, \savebox, \sbox, \sc, \scriptsize, \scshape, 
\searrow, \sec, \section,
\setcounter, \setlength, \settowidth, \settodepth, \settoheight, 
\settowidth, \sf, \sffamily, \sharp, \shortstack, \Sigma, \sigma, 
\signature, \sim, \simeq, \sin, \sinh, \sl, \SLiTeX,
\slshape, \small, \smallskip, \spadesuit, \sqrt, \sqsubset,
\sqsupset, \SS,
\stackrel, \star, \subsection, \subset, 
\subsubsection, \sum, \sup, \supressfloats, \surd, \swarrow,

\t, \table, \tableofcontents, \tabularnewline, \tan, \tanh, 
\tau, \telephone,\TeX, \textbf,
\textbullet, \textcircled, \textcompworkmark,\textemdash, 
\textendash, \textexclamdown, \textheight, \textquestiondown, 
\textquoteblleft, \textquoteblright, \textquoteleft,
\textperiod, \textquotebl, \textquoteright, \textmd, \textit, \textrm, 
\textsc, \textsl, \textsf, \textsuperscript, \texttt, \textup,
\textvisiblespace, \textwidth, \TH, \th, \thanks, \thebibligraphy,
\Theta, theta, 
\tilde, \thinlines, 
\thispagestyle, \times, \tiny, \title,\today, \totalheightits, 
\triangle, \tt, 
\ttfamily, \twocoloumn, \typeout, \typein,

\u, \underbrace, \underline, \unitlength, \unlhd, \unrhd, \Uparrow,
\uparrow,\updownarrow, \upshape, \Upsilon, \upsilon, \usebox,
\usecounter, \usepackage, 

\v, \value, \varepsilon, \varphi, \varpi, \varrho, \varsigma, 
\vartheta, \vdots, \vec, \vector, \verb, \Vert, \vert, \vfill,
\vline, \vphantom, \vspace,

\widehat, \widetilde, \widthits, \wp,

\Xi, \xi,

\zeta</t>
<t tx="edream.110203163054.467">leo.py 3.5                                  August 14, 2002

Highlights:

- Added new entries in the help menu.
 (Including a link to Joe Orr's excellent ScreenBook tutorial).
- Added the importFiles script in leoImport.py.
- Added configuration options for horizontal scrollbars.
- Added better warnings for read-only files.
- Removed all '\r' when reading derived files.
- Fixed crasher in Read Outline Only command.
- Fixed crasher when leoConfig.txt did not exist.
- Many small improvements and bug fixes.</t>
<t tx="edream.110203163054.468"></t>
<t tx="edream.110203163054.469">This may be the cause of truncated leoConfig.txt files on Linux.</t>
<t tx="edream.110203163054.470"></t>
<t tx="edream.110203163054.471"></t>
<t tx="edream.110203163054.472">Removed '\r' characters when reading.  The write logic is unchanged.</t>
<t tx="edream.110203163054.473">Relative paths should not set the global default paths.  Instead, the relative path is concatenated to the global default path when the file is opened.</t>
<t tx="edream.110203163054.474"></t>
<t tx="edream.110203163054.475"></t>
<t tx="edream.110203163054.476">Added log_pane_wraps and outline_pane_scrolls_horizontally configuration settings.</t>
<t tx="edream.110203163054.477"></t>
<t tx="edream.110203163054.478">Note: b4 contains a fix to b3 in this area:  for writing, we must first test whether the file exists.  Otherwise we may get a false indication that the (non-existent) file is read-only.</t>
<t tx="edream.110203163054.479">Added the importFiles script in leoImport.py. Use this script as follows:

- Select the node under which you want the imported files to appear.
- Open the Python window within Leo.
- Type the following in the Python window:

import leoImport
dir = "c:/prog/test"  # or some other directory
type = ".py"  # Type of files you want to import.
leoImport.importFiles(dir,type)

If you want to import all files in a directory, replace the last line with:

leoImport.importFiles(dir)</t>
<t tx="edream.110203163054.480">leo.py 3.4                                     August 11, 2002

This release contains many small improvements and bug fixes.  The highlights:

- Fixed several crashers involving Unicode.
- The Show Invisibles command now makes blanks and tabs look much better.
- Created leoConfig.leo, from which leoConfig.txt is now derived.
- Added save_clears_undo_buffer configuration option.
- Fixed a large number of problems with the configuration code.
- The usual minor improvements and bug fixes.

See the children of this node for full details.</t>
<t tx="edream.110203163054.481"></t>
<t tx="edream.110203163054.482">The problem is that the ratio is saved in the .leo file and the split direction is not. So if leoConfig.txt is read-only you the Toggle Split Direction command will permanently change the body-outline ratio _without_ permanently changing the split direction itself.

This basically sucks, and here are my reasons: 

1. I do not want to be adding more options to .leo files; the whole idea of leoConfig.txt is to move in the opposite direction. 

2. You can make everything work more like you would expect by making leoConfig.txt read-write. 

3. Especially in the case of the split direction, I expect people to have strong preferences one way or the other, so even if leoConfig.txt is read-only it shouldn't be too odious to pick a split direction and live with it.</t>
<t tx="edream.110203163054.483">The undo buffer creates a lot of strings.  On some system this may be a problem.  If save_clears_undo_buffer = 1 the Save command (and only the Save command) will clear the undo buffer.</t>
<t tx="edream.110203163054.484">The new spelling is to limit_directory_search_extension.  Note that this affects the valid entries in leoConfig.txt.</t>
<t tx="edream.110203163054.485">This allows us to create leoConfig.txt more easily, and provides a safe place to permanently store comments when read-write mode is on.</t>
<t tx="edream.110203163054.486">If a setting was missing or "ignore" it could never be set!  This no doubt could have caused a wide variety of symptoms.  In particular, in the distributed leoConfig.txt file it meant that settings for "default" fonts and sizes were never updated!</t>
<t tx="edream.110203163054.487">The new code properly deletes previous entries regardless of case or path separators.</t>
<t tx="edream.110203163054.488">There were a couple of bugs here.

Note that the ratio (whichever the direction) is stored in the .leo file.  The initial_splitter_orientation setting in leoConfig.txt applies to _all_ files.  The initial_vertical_ratio and the corresponding initial_horizontal_ratio  apply only to new files, so are essentially useless.

Yes, this is pretty stupid; it's the result of not wanting to add more stuff to Leo's file format.</t>
<t tx="edream.110203163054.489"></t>
<t tx="edream.110203163054.490"></t>
<t tx="edream.110203163054.491"></t>
<t tx="edream.110203163054.492"></t>
<t tx="edream.110203163054.493">leo.py 3.1 contains Python code that may be of interest to some Python programmers.  All Python files are derived from LeoPy.leo.

See the children of this node for details.</t>
<t tx="edream.110203163054.494">This script does much of the grunt work of converting from C/C++ syntax to Python syntax.  It was surprisingly effective in converting Leo from C++ to Python.  These scripts don't need to be perfect to save a _lot_ of work.  And of course you can always add your own improvements...

As written, the script converts an entire Leo tree.  It would be easy to write an entry that would convert plain text files, but it's probably best to import the files to be converted into Leo first.  That way the slow algorithms in c2py.py will work on smaller pieces of text.</t>
<t tx="edream.110203163054.495">This code gathers and prints static statistics about Python bytecode.</t>
<t tx="edream.110203163054.496">The file leoUtils.py contains some small Tkinter utilities:

w,h,x,y = get_window_info(top) returns the width, height, x and y positions of the Tkinter window top.

center_dialog(top) centers the Tkinter window top on the screen.

w,f = create_labeled_frame(parent...) creates a labeled Tkinter window as a child of parent.  The caller packs widgets into f to create the frame.

leoUtils.py contains many other routines including an Python version of the Sherlock tracing package.</t>
<t tx="edream.110203163054.497">leoFontPanel.py puts up a Font dialog.  This dialog dispenses with the typical "sample" pane and instead changes text immediately directly on the screen.  Comes with Ok, Cancel and Revert buttons.  IMO, this dialog is much better than the sample Tk/Tkinter font dialogs available on the web.</t>
<t tx="edream.110203163054.498">leoColor.py contains code to syntax color Tk.Text widgets for a variety of languages.  Supporting a new language here is mostly a matter of adding another table of keywords.</t>
<t tx="edream.110203163054.499">Leo supports powerful outlining features, including clones.  Clones are challenging to implement, to say the least.  The vnode and tnode classes, defined in leoNodes.py, represent the underlying data.  vnodes represent nodes on the screen.  vnodes may share text, the tnode class is the "unit of sharing" of such text.  The leoTree class draws the tree and handles events, including dragging nodes around the screen.  The Commands class calls the vnode, tnode and leoTree classes to handle menu commands.  In Smalltalk's model/view/controller terminology, the vnode and tnode classes are model class, the leoTree class is a view class, and the Commands class is a controller class.</t>
<t tx="edream.110203163054.500"></t>
<t tx="edream.110203163054.501">Now at last it is clear why Leo hasn't been writing derived files affected by clones.  It's not enough to mark v dirty.  We must mark all the cloned nodes of v's tree dirty as well.

However, we only need do this when a node is deleted, and we definitely do _not_ want to do this otherwise, for that would mark far too many nodes dirty.  To get around this, we leave v.setDirty() as it was, and use the new code only in v.setDirtyDeleted.

Note that the undo and redo cases handle this automatically because they call c.doDelete.

So now we can state a rule that should not ever be broken: after doing a Save command, a Write @file Nodes command should always report "unchanged" for all files.</t>
<t tx="edream.110203163054.502"></t>
<t tx="edream.110203163054.503">Added setRevertVars to update revert settings.  This is called from __init__ and onOk.</t>
<t tx="edream.110203163054.504">Changed idle_body_key and idle_head_key, leoTangle::os and tnode::setTnodeText.

We must remove backticks from messages that might contain unicode characters so they will print properly.  There were only a few instances, and they are all error messages that hardly ever get executed, so I hope I was careful putting them in.  I should be able to find them all by looking for '"'.</t>
<t tx="edream.110203163054.505">Repeated double-clicking (without intervening single-click) caused the selection to move to the left.</t>
<t tx="edream.110203163054.506"></t>
<t tx="edream.110203163054.507"></t>
<t tx="edream.110203163054.508">This is consistent with what the Import commands do for the other file types.  It's also much safer.</t>
<t tx="edream.110203163054.509"></t>
<t tx="edream.110203163054.510">This makes selected text look much better and makes Show Invisibles look much better as well.  

This was not easy to do.  Apparently tag settings interfere with the Tk.Text settings.  I have not found a way to specify the selectbackground color for tags.  The only way I could get things to work is define whitespace tags only when in showInvisibles mode.</t>
<t tx="edream.110203163054.511">.tmp files disappear On Windows XP after Leo exits!</t>
<t tx="edream.110203163054.512">leo.py 3.3                                     August 3, 2002

This version of Leo:

- Added support for Unicode.
- Improved the Import commands.
- Fixed numerous bugs related to configuration settings.
- Fixed the "Javadoc" bug and several latent bugs related to it.

See the children of this node for details.

Edward K. Ream</t>
<t tx="edream.110203163054.513">It is now possible to use non-Ascii characters in Leo!

Leo uses the xml_version_string setting to encode Unicode characters in .leo files.  This will be UTF-8 by default.  I've also very briefly tested ISO-8859-1.

I am a complete Unicode ignoramus.  It seemed trivial to add Unicode support to Leo, and if there are any fine points that should have been considered I no doubt did not consider them...</t>
<t tx="edream.110203163054.514">The Import command now does a better job of removing excess leading whitespace.

When importing .java files, Leo now preserves newlines in leading block comments.  This makes the typical weird Java comments look better.  For example,

/**  This is a typical,
  * brain-dead,
  * Java comment.
  */

Now gets rendered as

@ * This is a typical
 * brain-dead,
 * Java comment.
@c

The comment will be reconstituted properly when rewritten.
</t>
<t tx="edream.110203163054.515">This never happened before because all languages had either 1 or 3 delims.  But Java now has only 2 delims to force block comments.</t>
<t tx="edream.110203163054.516">Leo should now handle negative tab widths properly.</t>
<t tx="edream.110203163054.517">- Negative tab widths are now honored properly.

- Made 'additional_body_text_border' setting functional.

- Made 'body_pane_wraps' setting functional.

- There was a bug that made the following non-functional.

	"read_only"
	"xml_version_string"
	"limit_count"
	"body_pane_wraps"

That is, only the default settings in leoConfig.py were used, not the settings in leoConfig.txt.

- The old code did not use the "page_width" and "tab_width" settings from leoConfig.txt.</t>
<t tx="edream.110203163054.518">leo.py 3.2                                     July 30, 2002

This version generalizes the @others directive, improves the Import command and fixes several bugs.  See the children of this node for full details.

The highlights:

- Nested @others directives are now valid, an important improvement.
  This simplifies files that define more than one class.
- Improved the Import command and squashed several bugs lurking there.
- Made the various Go commands in the Outline-Move/Select menu functional
  by reassigning keyboard shorts
- Fixed a crasher in the Prefs Panel.
- Fixed numerous bugs in the Set Colors command.
- Fixed syntax coloring of C strings that span multiple lines.
- The usual minor improvements and bug fixes.

Edward K. Ream</t>
<t tx="edream.110203163054.519">Nested @others directives are now valid, even when no named node intervenes.  This is a significant enhancement to Leo because it is now easier to define multiple classes in a single file.  The leoNode.py file also uses nested @others directives.

The outline shown in the child of this node shows the general idea.

The Import command uses nested @others to great effect in Python files containing many classes.  For example, try importing the file Python/Lib/Compiler/ast.py.</t>
<t tx="edream.110203163054.527">The Import command creates nested @others directives when parsing Python classes.

Fixed two bugs in the Import command:

1. The Import command now properly places the first @others directive of Python files.  Previously the @others directive was placed before section references, so code could be rearranged.

2. The Import command now properly handles all C preprocessor directives.  Previously there were problems handling the #ifndef directive which could ruin imports.

Two other minor improvements:

1. This is reasonable: we don't wan't people generating files from imported files unless they take some positive action.

2. The Import command now checks that different branches of #if, #else, #endif directives have the same net number of braces, and warns if they do not.  This logic was inserted while trying to fix bug #2 above.</t>
<t tx="edream.110203163054.528">It's too confusing to have arrow keys mean different things in different panes.

For one thing, we want to leave the focus in the body pane after the first click in the outline pane, but that means that the arrow keys must still be functional in the body pane!

Alas, all the various combinations of key bindings of arrow keys appear to do something; there are none left to use for moving around in the outline pane.  So we are stuck with poor shortcuts.</t>
<t tx="edream.110203163054.529">Leo could sometimes crash when the user selected Cancel in the Preferences panel.</t>
<t tx="edream.110203163054.530"></t>
<t tx="edream.110203163054.531">There were too many problems in the old color panel.

- Completely revised the Revert logic in the main Color panel.
- The color name picker now reverts properly.
- Color names and color swatches are now properly updated in all cases,
  so there is no need to write color values to the log window.
- Eliminate quotation marks around color names and values.
- The color picker now shows the value of the present color, not the revert color.
- Increased the width of name buttons to handle long color names.
</t>
<t tx="edream.110203163054.532">Thanks to Thomas Guettler for suggesting this.</t>
<t tx="edream.110203163054.533">This script uses the dis module to print static statistics about Python bytecode.  Of no use to anyone but me.</t>
<t tx="edream.110203163054.534">leo.py 3.1                                     July 20, 2002

This version fixes a blunder that affects only leo.py 3.0.  I recommend that all users of 3.0 upgrade to this version.

With this release Leo's to-do list is now empty! I shall fix bugs as they are reported. I'll add new features only if convinced that they contribute significantly to Leo.

The highlights:

- Fixed a blunder: Leo 3.0 did nothing when it was opened directly from leo.py.
  (Opening leo using openLeo.py did work.)
- Created a compare panel to control scripts in leoCompare.py.
- Added many new settings in leoConfig.txt to initialize the compare panel.
- The FAQ tells how to add support for new languages.
  (These instructions also appear in the "Notes/How To" section in LeoPy.leo)
- The usual minor improvements and bug fixes.

Edward K. Ream</t>
<t tx="edream.110203163054.535">The file comparison window helps people verify that imported files are, in fact, precisely equivalent to the original files.</t>
<t tx="edream.110203163054.536">Here are the new settings in leoCompare.txt:

# Initial settings of the Compare panel.
# 	These correspond to the keyword parameters of the leoCompare constructor.
# 	Exception: there are no keywords for compare file names in the constructor.

[compare options]

# ----- Options specifying files for the Compare panel.

compare_file_1 = c:/prog/test/compareTest1/file1.txt
#	Path to the first file or directory to be compared.
#	Directory compares ignore a filename part of the path, if present.
#	E.g., c:/directory1/spam.py is valid for directory compares.

compare_file_2 = c:/prog/test/compareTest2/file2.txt
#	Path to the second file or directory to be compared.
#	Directory compares ignore a filename part of the path, if present.
#	E.g., c:/directory2/spam.py is valid for directory compares

output_file = c:/prog/test/compareResults.txt
#	Path to the output file.
#	Leo will silently write to this file, regardless of whether it already exists.
#	Leo will write to the log pane if this path is empty or invalid.

append_output_to_output_file = 0
#	0: Replace output file with results of compare.
#	1: Append output to output file.

# ----- Options related to directory compares.
#	These options has no effect when comparing files.

limit_directory_search_extenstion = .py
#	Limit directory searches to files with the given file extension.
# 	Examples:
#		None	Compare all files when comparing directories.
#		.py  	Compare .py files when comparing directories.

# ----- Options related to file compares.
#	These options have no effect when comparing directories.

ignore_blank_lines = 1
#	1: Ignore blanks lines when comparing files.

ignore_first_line_of_file_1 = 0
#	1: Ignore the first line of compare_file_1 when comparing files.

ignore_first_line_of_file_2 = 0
#	1: Ignore the first line of compare_file_2 when comparing files.

ignore_interior_whitespace = 0
#	1: Ignore whitespace after the leading whitespace of a line when comparing files.

ignore_leading_whitespace = 0
#	1: Ignore leading whitespace of each line when comparing files.
#	Not recommended when comparing .py files.

ignore_sentinel_lines = 0
#	1: Ignore sentinel lines when comparing files.
#	Leo sets sentinel comment delimiters from the first line of each file.
#	This option has no effect if the first line is not a @+leo line.

# ----- Options affecting how Leo shows the results of file compares.
#	(Leo gathers statistics regardless of these options.)

limit_count = 9
#	0: Show lines regardless of the number of mismatches.
#	n: Stop showing lines after n mismatches.

make_whitespace_visible = 0
#	1: Show blanks as [ ] and tabs as [t]

print_both_lines_for_matches = 0
#	0: Print only the line of compare_file_1 when showing matching lines.
#	1: Print lines of both files when showing matching lines.

print_matching_lines = 0
#	1: Print lines that match using the print_both_lines_for_matches option.

print_mismatching_lines = 1
#	1: Print lines that do not compare equal to each other.

print_trailing_lines = 1
#	1: Print lines all lines in one file after an end-of-file is seen on the other file.</t>
<t tx="edream.110203163054.537">The new rules allow leo.py 3.1 to read and write .leo files more like leo.py 2.x when there is no leoConfig.txt file.  The scheme used in leo.py 3.0 meant that preferences were _never_ written to .leo files.  It's advantage was that all defaults were specified in:

	leoConfig.&lt;&lt; define default tables for settings &gt;&gt;

I think the present scheme is more natural, but we shall see...

In effect, Leo sets and gets various options in the following order of precedence:

1. Use explicit settings in leoConfig.txt if they exist.

2. Use defaults for leoConfig.txt, but only if leoConfig.txt exists.  These defaults are found in:

	leoConfig.&lt;&lt; define default tables for settings &gt;&gt;

3. Use settings in .leo files if leoConfig.txt does not exist.

4. If leoConfig.txt does not exist, and the .leo file does not specify a setting, use hard-coded settings in the various classes, just as leo.py 2.x did.</t>
<t tx="edream.110203163054.538">The @pagewidth, @tabwidth and @language directives could not have worked while tangling. Apparently nobody has every used these directives in @root trees!</t>
<t tx="edream.110203163054.539">The Flatten Outline command must use an escape convention so that it can distinguish between the "+" and "-" characters that denote a headline and any "+" and "-" characters that start a line of body text.

The old version of Flatten Outline inserted a backspace before _all_ "+", "-" and backspace characters.  The new version of Flatten Outline inserts a backspace before such characters only if they are the first non-whitespace character of a line.

This change affects the "file format" used by the Import Flattened Outline command.  If you import a file flattened with the old version of Flatten Outline, the new Import Flattened Outline will remove the inserted backspace only if it is the first non-whitespace character of the line.  In practice, this is unlikely to be a problem: you could just manually convert "\\", "\+" and "\-" to "\", "+" and "-" throughout the imported file.</t>
<t tx="edream.110203163054.540">The Open Python Window command now attempts to add IDLE's location to sys.path if import idle fails.

Bernhard Mulder contributed the code that made this improvement possible.

</t>
<t tx="edream.110203163054.541"></t>
<t tx="edream.110203163054.542">leo.py 3.0                                     July 16, 2002

This version is called 3.0 because it can optionally produce files that can NOT be read by the leo.py 2.x or the Borland version of Leo.  However, by default, leo.py 3.0 DOES produce files that all previous versions of Leo can read.

See the children of this node for full details.  The highlights:

- Support for many user options stored in leoConfig.txt, including, among others,
  fonts in all panes, colors for syntax coloring and default window size and position.
- Support for .leo files with XML types like "ISO-8859-1", controlled by a user option.
  Note: by default, Leo writes files compatible with previous versions of Leo.
- Powerful new Color and Font pickers, fully connected to user options.
- Added Toggle Split Direction command, under control of user options.
- Added autoscrolling in the outline pane.
- Windows open at the position in which they were saved.
- The size and position of new windows can be controlled with user options.
- Eliminated drawing problems while opening files.
- Improved syntax coloring for @comment plain.
- The Convert All Blanks and Convert All Tabs commands are now undoable.
- Leo warns and aborts if Python 2.2 or above is not running.
- The usual bug fixes.

At least one more version of leo.py is planned.</t>
<t tx="edream.110203163054.543">You now have a choice: you can configure Leo to please previous versions of Leo or to please XML parsers:

Leo now uses the xml_version_string configuration setting, if present, to override the UTF-8 setting used in all previous versions of Leo.  The default value of this setting is UTF-8, so by default leo.py will write files that may be read by any previous version of leo.py or the Borland version of Leo.

However, xml_version_string = ISO-8859-1 will produce .leo files that are more acceptable to XML parsers when those .leo files contain Unicode characters that are not found in the UTF-8 (Ascii) character set.  In any event, the choice of whether to please previous versions of Leo or XML parser is completely up to you. 

If the setting does not exist, whatever value is present in the .leo file will be written when the .leo file is written.  For new files, a value of UTF-8 will be used when this setting is not present.

Notice that this also affects what is written to the clipboard.</t>
<t tx="edream.110203163054.544"></t>
<t tx="edream.110203163054.545">This version supports many more options than before.  See leoConfig.txt for the full list.

Leo looks for leoConfig.txt in the same places as in leo.py 2.5.  If Leo does not find leoConfig.txt, This version will use defaults specified in tables defined in the section
	&lt;&lt; define default tables for settings &gt;&gt;
in leoConfig.py.  So it is now convenient to change settings in leo.py itself as well as in leoConfig.txt.</t>
<t tx="edream.110203163054.546">Including the split direction and split ration.

Leo now uses all configuration settings from leoConfig.txt.</t>
<t tx="edream.110203163054.547">If you drag a headline above or below the outline pane the outline pane will scroll automatically.  As before, Leo will cancel the drag if you release a headline anywhere but over another headline's icon.</t>
<t tx="edream.110203163054.548">You can specify colors for each syntax coloring construct using a color wheel or by choosing one of the standard Tk color names.  When a color becomes active Leo writes its value or color name to the log pane for your reference.  This is useful when setting coloring options in leoConfig.txt.</t>
<t tx="edream.110203163054.549">Using this panel should be self-explanatory (what you see is what you get) with the following exceptions:

1.  When a font becomes "active", the new font appears in the panes whose check boxes are selected.  A font becomes active when you double-click its name, or check or uncheck any checkbox.

It would be much better to have a font become active if you just select its name.  Alas, that is not possible due to a well-known gap in the Tk.Listbox class.

2. Font sizes must be greater than 0 and less than 100 for them to become in effect.

3. Choosing very _small_ values for font sizes may cause Leo's window to _expand_ its width.

4. When you choose OK or Cancel Leo writes the fonts presently active in each pane to the log pane for your reference.  This is useful when setting font options in leoConfig.txt.</t>
<t tx="edream.110203163054.550">This was a supremely irritating bug.</t>
<t tx="edream.110203163054.551">This command switches between vertical and horizontal orientations of the Leo window.  In the vertical orientation, the body pane appears below the pane containing the outline and log panes.  In the horizontal orientation, the body pane appears to the left the pane containing the outline and log panes.

leoConfig.txt specifies the default direction.  If leoConfig.txt does not exist, or does not specify the direction, the "vertical" orientation is used, just as in previous versions.

By default, the ratio of pane outline pane to the body pane is 0.5 in the vertical orientation and 0.3 in the horizontal orientation.  These two ratios may be changed using leoConfig.txt.</t>
<t tx="edream.110203163054.552">The @comment directive no longer suppresses syntax coloring.  Leo directives (but not doc parts) are colored when @language plain is in effect.  The user can, as always, suppress all coloring by using @nocolor.  The new rules are much more natural than the old, and much less confusing.</t>
<t tx="edream.110203163054.553"></t>
<t tx="edream.110203163054.554"></t>
<t tx="edream.110203163054.555">The old colorer colored all Leo directives blue, the same color as keywords in whatever language is current. I think the distinction between Leo directives and language keywords is useful.  Of course, you can control syntax coloring yourself by altering leoConfig.txt.</t>
<t tx="edream.110203163054.556">This message is printed to the console, not the log pane.  On windows, this may not always be visible.</t>
<t tx="edream.110203163054.557">Leo will convert underscores in the @comment directives to significant spaces.  For example,

@comment REM_

causes the comment delimiter to be "REM " (Note the trailing space).</t>
<t tx="edream.110203163054.558"></t>
<t tx="edream.110203163054.559">This happened sometimes when using @comment.</t>
<t tx="edream.110203163054.560">Leo directives were mostly being colored using the colors for keywords.  This didn't show up because both were colored blue.</t>
<t tx="edream.110203163054.561">Only one window now appears when opening a .leo file, and the window is completely drawn before anything gets written to the log pane.</t>
<t tx="edream.110203163054.562">Added new code for Convert All Blanks and Convert All Tabs.

Fixed a bug that resulted in Convert Tabs being undoable.</t>
<t tx="edream.110203163054.563">This makes the panel much more convenient to use.</t>
<t tx="edream.110203163054.564"></t>
<t tx="edream.110203163054.565">leo.py version 2.5.1                            July 7, 2002

2.5.1 This version corrects crashers that affect undo/redo move commands.
Version 2.5 has been withdrawn.
Anyone using 2.5 should use 2.5.1 instead.

This is a major step forward to completing leo.py.  It adds significant new features and corrects many bugs.  Full details are found in the children of this node.  Here are the highlights, in approximate order of importance:

1. Leo supports tab widths properly, and negative tab widths cause Leo to convert tabs to blanks as you type.  Three new commands appear in the Edit Body menu: Convert Tabs, Convert All Tabs and Convert All Blanks.  Convert All Tabs and Convert All Spaces convert the entire selected tree.

2. Leo now allows you to override selected preferences using a configuration file called leoConfig.txt. Leo acts as before if this file does not exist.  An option in leoConfig.txt specifies whether leoConfig.txt is read-only.

3. The Preferences panel is now a modal dialog containing Ok, Cancel and Revert buttons.  This makes it clear what preferences are being set.

4. At long last, cut and paste work properly in all situations.  You can cut and paste between Leo and other applications, or between two different copies of Leo.

5. Added the Recent Files submenu to the File menu.  Very nice to have.

6. Fixed a number of bugs, including several crashers.  Fixed several bugs in the Import commands.  Leo will no longer abort reading if it detects an invalid directory name in the Default Tangle Directory in the Preferences panel.

leo.py is almost complete.  The only remaining tasks on my list are:

1. Make the Set Font... and Set Colors... commands functional.  This will be easy now that leoConfig.txt exists.
2. Fix the Javadoc bug.</t>
<t tx="edream.110203163054.566">The following are listed in the approximate order of their importance.  The marked nodes are particularly important.</t>
<t tx="edream.110203163054.567">Gary Herron suggested this changes.</t>
<t tx="edream.110203163054.568">These commands convert an entire tree.</t>
<t tx="edream.110203163054.569">This command converts leading tabs to blanks in a single node.</t>
<t tx="edream.110203163054.570">Previous versions of Leo ignored the tab width field!  This field is now fully functional.  </t>
<t tx="edream.110203163054.571">Leo converts tabs to blanks as you type when a negative tab width is specified.</t>
<t tx="edream.110203163054.572">The Preferences panel is now a modal dialog.  This solves a number of problems, both for the implementation and for the user.  It is now completely clear which preferences are being set, viz., the preferences for the window on top.  In addition, the Prefs panel now shows the name of the window whose preferences are to be set.

The Prefs panel now contains OK, Cancel and Revert buttons.  These are useful, and they are possible only because we have a modal dialog.</t>
<t tx="edream.110203163054.573">You may now cut and paste between Leo and other apps, or between two different copies of Leo.</t>
<t tx="edream.110203163054.574">The elements of this submenu are saved in leoConfig.txt, if present.

Leo adds files to this submenu even if leoConfig.txt is missing or read-only, but those additions will not be remembered unless leoConfig.txt is present and writable.</t>
<t tx="edream.110203163054.575"></t>
<t tx="edream.110203163054.576"></t>
<t tx="edream.110203163054.577"></t>
<t tx="edream.110203163054.578">1. Importing the following script

class C:
    def __init__(self):
        pass

created an outline with class C appearing in two nodes.

2. Importing the following file created orphan nodes for declaration.

import sys # This line becomes an orphaned node
class C:
    xyz = 'xyz' # This line becomes an orphaned node
    def __init__(self):
        pass

3. Importing a Python file containing classes without methods resulted in nested classes. There is still a minor problem:  The following

class A:
	pass

puts the "pass" in a section called &lt;&lt; class A declarations &gt;&gt;.  This is not easy to fix: you will have to correct it by hand.

4. Improved the Import to @root command.  Added @root &lt;filename&gt; to the body text of the root of tree and eliminated @language and @others directives.</t>
<t tx="edream.110203163054.579">This is important, because it means that invalid entries in, say, the Default Tangle Directory preference will no longer abort an attempted read.</t>
<t tx="edream.110203163054.580"></t>
<t tx="edream.110203163054.581">This would happen if the Default Tangle Directory did not exist in the Prefs panel.</t>
<t tx="edream.110203163054.582">This command always crashed, perhaps due to a reversion.</t>
<t tx="edream.110203163054.583">The crash happened if the Import command was executed in a new, unsaved file.

The fix was to the directory logic in import.scanAllDirectives.</t>
<t tx="edream.110203163054.584"></t>
<t tx="edream.110203163054.585"></t>
<t tx="edream.110203163054.586">The bug involves only the clone mark itself: nodes have always been properly joined.</t>
<t tx="edream.110203163054.587">Gary Herron reported this bug and told me how to fix it. This change is to the default file extension field of file dialogs.  It seems to have no effect on Windows. Apparently this makes a difference in Linux...</t>
<t tx="edream.110203163054.588">These commands no longer change the file name associated with a window if the user cancels the Save or Save As dialog.</t>
<t tx="edream.110203163054.589">This involved changing the documentation for the Demote, Insert Headline, Extract Headline, Syntax Coloring... and Font... commands.  Removed documentation for the Open/Close Log Window command.</t>
<t tx="edream.110203163054.590"></t>
<t tx="edream.110203163054.591">leo.py version 2.4                             June 20, 2002

This version fixes some annoying bugs and adds some nice features.  The children of this node contain full details.

1. Leo now properly highlights the headline of a newly created node.  Similarly, the Edit Headline command (control-H) now works.  Double-clicking in a headline now does what you would expect: it selects the word under the cursor.  Similarly, triple-clicking now selects the entire headline.  Also fixes several other minor bugs.

2. Drag and drop.  You can now reorganize outlines by dragging nodes around.  You must drag from a node's headline and release on another node's headline.  See a child of this node for complete details.

3. You can now open .leo files in leo.py by double clicking on .leo files.  You must associate leo.py with .leo files.  See a child of this node for detailed instructions about how to do this.

4. Improves error recovery when there are errors writing .leo files.

5. Updates this file to match the documentation of Leo's web site.  At long last, Leo's documentation is complete.</t>
<t tx="edream.110203163054.592">1. Fixed a bug in app.finishCreate that caused Leo to take an exception on MacOS X.

2. Leo now properly highlights the headline of a newly created node.  Similarly, the Edit Headline command (control-H) now works properly.

3. Removed a useless assert in st_enter_root_name that could fail under unusual circumstances.</t>
<t tx="edream.110203163054.593">When writing a .leo file, say f.leo, Leo now attempts to create a backup file called f.leo.back.  If there is an error while writing f.leo, Leo will restore f.leo from f.leo.back.  Note that Leo will write derived files correctly even when there is an error writing the .leo file.</t>
<t tx="edream.110203163054.594">New in leo.py v2.4: You may drag an node (including all its descendents) from one place to another in an outline.  To start a drag, press the main (left) mouse button while the cursor is over the icon for a node.  The cursor will change to a hand icon. If you release the mouse button while the hand cursor is above the icon for another node, Leo will move the dragged node after that node.  If you release the mouse button when the hand cursor is not over an icon, Leo will print "not moved" and leave the outline pane as it is.  This can result in the dragged node not being visible on the screen, but it seems less alarming not to force the current node to become visible as that would undo any scrolling that has just been done.

New in leo.py 3.0: If you drag outside the outline pane, the outline pane will scroll automatically.

Leo scrolls the outline pane as the result of mouse-moved events, so to continue scrolling you must keep moving the mouse.  I experimented with scrolling the outline pane whenever the cursor is dragged outside it, but the results were not good.  There was a noticeable delay between releasing the cursors and halting the scrolling.  The present code is simpler and more likely to work on all platforms.

Leo only allows dragging from one icon to another.  In particular, you can't move a node to the first child of another node unless that node is already expanded.   I experimented with automatically open nodes when the cursor moves over an unexpanded node with children.  However, this was confusing and alarming.  It seems best to expand and contract nodes explicitly.</t>
<t tx="edream.110203163054.595">leo.py version 2.3                             June 5, 2002

This version fixes a minor problem with Leo.

1.  The code that reads and writes @file nodes now uses the directory containing the .leo file as a default when the Default Tangle Directory setting is empty in the Preferences panel.  This is a reasonable default because derived files are most often created in the same directory as the .leo file.  BTW, the Tangle and Untangle commands have used this convention for a long time.

Note: This default allows us to distribute LeoPy.leo without specifying a directory in the Preferences Panel.</t>
<t tx="edream.110203163054.596">leo.py version 2.2                             June 1, 2002

The version fixes two bugs that happen rarely and can cause loss of data when they do happen.

1.  In certain circumstances leo.py v2.1 would delete most of an outline when a node was moved in front of the previous root node!

2.  All previous versions of leo.py will crash when saving body text containing unicode characters.  This could occur as the result of cutting and pasting text from another application into the body pane.  Leo.py now writes body text containing unicode characters using Python's u-prefixed notation.  That is, the body text is written as: u'escaped_text'  where escaped text replaces unicode characters not in the ascii character set by escape sequences of the form \uxxxx.  The result contains nothing but ascii characters, so leo.py will have no problem reading it.  Naturally, compilers and other tools may not understand Python's notation, so you may have to convert escaped text to something that your tools can understand.

3.  This file, LeoDocs.leo, now more closely matches the documentation on Leo's web site.</t>
<t tx="edream.110203163054.597">leo.py version 2.1                             May 16, 2002

This version of Leo adds Import and Export commands and fixes several bugs:

1. All Import and Export commands now work. Several of these commands are found only in Leo.py.  Some of these commands may be of beta quality.

I use Import commands mainly for studying other people's code.  Be wary of generating source files from trees generated by the Import commands.

2. Fixed a bug that caused Leo to crash when a node was moved up in front of the previous root node.

3. Fixed several bugs in the syntax colorer.  One of these bugs caused Leo to crash when handling CWEB.

4. Leo now colors strings green.</t>
<t tx="edream.110203163054.598">I use Import commands mainly for studying other people's code.  Be wary of generating source files from trees generated by the Import commands.

The Remove Sentinels command can "clean" files for publication or walk-throughs.  You can also use the Remove Sentinels command to prepare files for comparisons.  For example, one could study a file, say f.py, as follows:

1. Use the Import Files command to create an @file tree, say @file f2.py, for study.  Changing the name to f2.py ensures that saving the .leo file won't destroy the original file.

2. Use the Remove Sentinels command to create a file f3.py.  Use a file comparison program to ensure that f1.py is identical to f3.py.</t>
<t tx="edream.110203163054.599">Fixed several bugs that caused Leo to hang when moving an outline up before the previous root node.</t>
<t tx="edream.110203163054.600">Fixed a bug that caused Leo to hang when syntax coloring noweb code with the CWEB syntax colorer.

The syntax colorizer now handles Python triple strings and C preprocessor directives properly.

Leo now colors strings with the same green used by IDLE.  I think this color looks very good.

Improved the syntax coloring for CWEB.</t>
<t tx="edream.110203163054.601">leo.py version 2.0                             March 4, 2002

leo.py v2.0 and Borland Leo v2.6 are being released simultaneously.  I urge all users of Leo to upgrade to one or both of these versions.  Note: the Untangle commands of both v2.0 and v2.6 should be considered beta quality.  Please report any problems with Untangle ASAP.

This is an important milestone in Leo's history, for several reasons:

1. For the first time, leo.py (v2.0) and the Borland Leo (v2.6) are functionally identical.  In particular, their respective Tangle commands produce identical output.

2. All "mission critical" aspects of leo.py are now complete: only the Import commands remain unfinished. leo.py v2.0 adds unlimited Undo/Redo, Untangle and full syntax coloring.  Unlimited Undo/Redo are reason enough to upgrade to v2.0.

3. leo.py v2.0 and Borland Leo v2.6 introduce an optimized format for derived files: both versions remove blank lines from between sentinel lines.  This is an upward compatible change in the format of derived files: leo.py v2.0 and Borland Leo v2.6 can read derived files from all previous versions of Leo, but previous versions of Leo can not read derived files without blanks lines between sentinels.

See the children of this node for full details.</t>
<t tx="edream.110203163054.602">leo.py v2.0 optionally can remove blanks from between sentinel lines in derived files.  This is an upward compatible change in the format of derived files: leo.py v2.0 can read derived files from all previous versions of Leo, but previous versions of Leo can not read derived files without blanks lines.

Removing blank lines requires a new kind of sentinel, the "verbatimAfterRef" sentinel.  This allows Leo to handle comments following section references that would otherwise be treated as sentinels themselves.  For example:
   
   &lt;&lt; section &gt;&gt; #+others
   
Leo removes blanks lines between sentinels by default.  To cause Leo not to remove blank lines do the following.  In the section called &lt;&lt; initialize atFile ivars &gt;&gt; in leoAtFile.py, change:

	self.suppress_newlines = true
to
	self.suppress_newlines = false

Note: leo.py v2.0 can read derived files without blank lines between sentinels regardless of the setting of self.suppress_newlines.
</t>
<t tx="edream.110203163054.603">leo.py supports unlimited Undo and Redo.  All outline operations and all typing operations may be undone and redone.  Undo state persists even after Saves.  Even the Change All command is undoable.  Only the "Read @file Nodes" command is undoable; it clears the entire undo state. This command raises a dialog to allow the user to cancel.

Think of the actions that may be Undone or Redone as a string of beads.  A "bead pointer" points to the present bead.  Performing an operation creates a new bead after the present bead and removes all following beads.  Undoing an operation moves the bead pointer backwards; redoing an operation moves the bead pointer forwards.  The Undo command is disabled when the bead pointer moves in front of the first bead; the Redo command is disabled when the bead pointer points to the last bead.

</t>
<t tx="edream.110203163054.604"></t>
<t tx="edream.110203163054.605">leo.py syntax colors all languages mentioned in the Preferences Panel.</t>
<t tx="edream.110203163054.606">1. Show Invisibles command works in @nocolor mode.

2. @unit, @root, @nocolor and @color now terminate doc parts.

3. Three characters were colored blue at the start of a section def in:

  &lt;&lt;name&gt;&gt;=
  
This didn't show up if there is a space after the &lt;&lt;.</t>
<t tx="edream.110203163054.607">Leo adds extra space at the end of headlines so that headlines now have enough room to show all text.  This works around an apparent Tk bug.</t>
<t tx="edream.110203163054.608"></t>
<t tx="edream.110203163054.609">The Untangle command is beta quality. Please make backups before untangling.</t>
<t tx="edream.110203163054.610">leo.py v2.0 fixes two bugs present in Borland v2.5 and fixed in Borland v2.6:

1. Untangle did not work properly for languages like Perl and Python that do not have block comments. 

2. Untangle did not recognize @ on a line by itself as the start of a doc part.</t>
<t tx="edream.110203163054.611">@c now works the same as @code.  This makes the syntax colorers agree with what the Tangle commands actually do.  Previously, the syntax colorers indicated that everything following an @c was code, while the Tangle commands placed everything following an @c in the doc part!</t>
<t tx="edream.110203163054.612">Previous versions of untangle silently trimmed trailing lines from all nodes, which seems rude.</t>
<t tx="edream.110203163054.613">The font size for code text is now 12 on Linux.

Changed code so that the path to the Icons folder is computed correctly on all platforms.</t>
<t tx="edream.110203163054.614">leo.py version 1.0                             February 10, 2002

Version 1.0 adds many new features and fixes several bugs.  I recommend that all users of leo.py upgrade to this version.  This version deserves the number 1.0; it has no known bugs.

Here are the highlights of this release.  See the children of this node for details.

1. Fixed bugs: the Tangle All and Tangle Marked commands didn't work at all. Fixed several bugs in the Find and Change commands.  The "Suboutline Only" option now applies to the Search All and Change All commands.  Settings in the Preferences Panel now "stick" properly to the currently selected window.  Fixed many minor bugs.

2. leo.py now re-marks @file trees as dirty if errors are found while writing those trees.  This makes it difficult to write derived files that will be out-of-synch when read again.

3. New commands and features:  Added the Revert, Select All, Delete, Sort Children, Sort Siblings, Contract Parent (very useful!) and Toggle Active Pane commands, and all commands in the Edit Body menu, and all the Go To commands in the Move/Select menu. The Show Invisibles commands is ugly, and useful nonetheless.

The Edit Body commands work much more reliably than the similar commands in the Borland version of Leo.  You may now specify Python scripts rather than .bat files in the Preferences panel. Added a way, albeit clumsy, to cut and paste nodes between Borland Leo and leo.py.  When syntax coloring Python text, leo.py increments the auto-indentation by one tab after a trailing colon.  This provides a subtle reminder to add such colons.

4. leo.py handles events and shortcuts properly.  The shortcut for the Insert Node command is now Control-I, as it is in the Borland version of Leo.  Worked around a TK bug that prevented double-clicks from properly selecting words.  leo.py enables and disables all menu items properly.</t>
<t tx="edream.110203163054.615">Removed the Print and Page setup commands because Tk provides no support for printing.  This is not significant: we can use the export commands to create text files.  These text files can then be formatted and printed as desired.

The following commands remain unfinished.  They will be finished in this order:

1. Untangle commands. 
	
2. Import/Export commands.

3. Unlimited Undo and Redo.

4. Toggle Split Direction, Cascade and Recent Windows commands.

5. Font Panel and Syntax Coloring commands.</t>
<t tx="edream.110203163054.616">It should be possible to cut a node or tree in Borland Leo and paste it using the Copy Node command in leo.py.  At present, cutting and pasting trees between applications can only be done indirectly.  Do this:

1. Copy the tree in Borland Leo using the Copy Node or Cut Node command.
2. Paste the tree into empty body text of leo.py using the Paste command from the Edit menu, _not_ the Paste Node command from the Outline menu.
3. Select all the body text and choose Copy or Cut from the Edit menu.
4. Move to the tree view, and choose Paste Node.

I hope to make this unpleasantness go away soon.</t>
<t tx="edream.110203163054.617">1. Fixed the Tangle All and Tangle Marked commands.  They always crashed.

2. The Change command did not work in headlines because of a reversion in how headline text is selected.

3. All event handlers now return "break".  This prevents further event handling and allows leo.py to handle events properly.  This cleared up the last major mystery in leo.py.

4. Settings in the Prefs Panel now "stick" to windows.  That is, they change when the user selects a new Leo window.  In particular, the Default Tangle Directory is restored properly.  This is important, as otherwise the Tangle commands might write files to the wrong place.

5. Removed calls to trace during shutdown.  In general, it is not possible to call app() during shutdown because the app object may no longer exist.

6. @others was not syntax colored properly if it was indented.</t>
<t tx="edream.110203163054.618">1. Adding trailing whitespace to a line in body text does not set the file-dirty mark.  This can never cause a derived file to become "out-of-synch" because the read code does not compare body text.

Apparently there is no way to fix this bug because of holes in Tk's event mechanism.  Specifically, tree.idle_body_key has no way to tell directly what keystroke caused it to be entered.

2. Cutting and pasting between applications can only be done indirectly.  See the node called
"How to copy an outline from Borland Leo to Leo.py".</t>
<t tx="edream.110203163054.619">leo.py version 0.08                             February 3, 2002

Version 0.08 adds important new features and fixes several bugs.  All users of version 0.07 should upgrade to this version.  This code seems solid, and significant bugs may remain.  Note: this code has been tested only on Windows XP.  Please report any problems with Linux or Macintosh.

This is the first version of Leo to feel as smooth as the Borland v2.5. leo.py is now less buggy than v2.5; the Borland version will soon be upgraded to match leo.py.

Here is a summary of new features.  See the children of this node for full details.

1. The Find and Change commands are fully functional.  These commands support Tk's "advanced regular expressions" when the "pattern match" option is checked.  Tk's regular expressions are documented at:

  http://tcl.activestate.com/man/tcl8.4/TclCmd/regexp.htm

2. The Tangle commands work; leo.py now supports @root trees.  The next release will support the Untangle commands.  Converting the Untangle code to Python is almost complete.

3. Leo now ensures that the currently selected headline is always visible, scrolling the outline pane as needed.

4. Improved Leo's memory management and eliminated several serious bugs.  One bug caused errors while reading @file trees.  Eliminating this is a huge step forward.  This bug exists in the Borland version of Leo and will be fixed soon.

5. Leo now underlines undefined section references.  Added support for hyperlinking, but disabled hyperlinking because it is not very useful without browser navigation buttons.</t>
<t tx="edream.110203163054.620">leo.py handles Find and Change commands much more smoothly than does the Borland version of Leo.  Indeed, I plan to rewrite the Borland code to match the code in leo.py.

In general, leo.py handles the Find and Change commands more smoothly than does the Borland version of Leo.  Note: the node that "anchors" wrapped searches is the current node when any change is made to the Find panel.  The anchor is recomputed after a wrapped search fails.

Changed the meaning of a Find panel setting from "batch" to "context".  This will be changed in a future Borland version.  In the meantime, setting the "context" option in leo.py will set the "batch" option in the Borland version.

The "context" option affects only the "Find All" and "Change All" commands.  When this option is in effect, more context information is printed when matches are found.

The "reverse" option affects all Searches and Changes, both those initiated from the Find Panel itself, and those initiated from menu commands.  In particular, F3 will find the previous search if the "reverse" option is in effect.</t>
<t tx="edream.110203163054.621">The Tangle command has passed significant tests, and bugs may remain.  Be warned.

leo.py's Tangle command produces output that is slightly different from Leo v2.5. The differences are insignificant; here is the complete list:

1. The header line, i.e., the first comment line of the tangled file: leo.py produces forward slashes in the path name, Leo v2.5 produces back slashes.

2. Leading whitespace: leo.py produces "optimized" leading whitespace.  leo.py removes blanks if they do not affect the visual appearance of whitespace; this depends on the tab width specified in the Preferences Panel.  Leo v2.5 copies leading whitespace exactly.  The leo.py way is preferable; it will produce output acceptable to Python's tabnanny regardless of tab width used while running Python.

3. Trailing blanks lines in body text: leo.py removes all trailing whitespace.  Leo v2.5 does not.  Conceivably, leo.py might have to change to make the Untangle command work properly.  More likely the leo.py way is just better.</t>
<t tx="edream.110203163054.622">Underlining "live" links clutters the screen too much, and hyperlinks from section references to section definitions isn't very useful without the standard "back" and "forward" buttons typically found in web browsers.  For these reasons, I have disabled hyperlinking.

To enable hyperlinking, just set:

	self.use_hyperlinks = true
	
in color.__init__ in the @file leoColor.py tree.</t>
<t tx="edream.110203163054.623">1. Fixed several bugs involving cloned headlines.  One bug caused cloned headlines not to be updated in synch.  Another bug caused @file trees not to be marked as dirty under certain conditions.

Both bugs could have caused read errors while reading @file trees, so fixing these bugs is a big step forward.  I have experienced no read errors since fixing these bugs.  A huge step forward.  This bug exists in the Borland versions of Leo and should be fixed ASAP.

2. There was a big performance bug lurking in the tree code that became apparent during testing of the Find and Change commands.  Closing a window could take almost a minute if the tree had been redrawn many times.  Old widgets were never deleted until the window was closed.  This may be a problem with tkinter, and the workaround was straightforward.

3. Fixed a bug in the "Save To" command.  After doing a Save To, a following Save command used the Save To file name!  This explains why some saves "didn't take".

4. Fixed a bug in the Save commands.  Cancelling a Save dialog did not work: instead it wrote a file called ".leo".  I am not sure whether this bug occurred in previous releases. 

5. All Save commands now always recompute file indices.  This old logic accomplished very little, and introduced needless differences between the various kinds of Save commands.

6. Made file and path name processing more portable.  Removed all calls to os.chdir().

7. Fixed a bug that caused a control-d to delete a character in the body pane when the Move Down command didn't do anything, i.e., when the presently selected node was the bottom node on the screen.</t>
<t tx="edream.110203163054.624">1. Used Tk.Text widgets in headlines rather than Tk.Entry widgets.  This allows the Find/Change commands to search headlines.  Control-k no longer deletes text following the cursor in headlines.

2. Improved the performance of screen updates and markedly reduced flicker in the body pane.

3. Found a way to handle keystrokes without knowing the status of the control and alt keys.  The idle event handlers now ignore the actual keystrokes in most cases, and take action solely based on whether the headline or body text has actually changed as the result of those keystrokes.  If not, we can assume that a command has been entered and we do not set the dirty or changed bits.

4. Replaced es_newline global with app().log.es_newline, i.e., frame.es_newline.  This is better than before because each log stream now has its own newline count.

5. Reduced width of the log pane to give more space to the tree pane.

6. The LeoPy folder now contains a dummy file called __init__.py.  This file marks the LeoPy folder as a potential package.

7. Added several new functions to the file leo.py.  These are useful for invoking leo.py from a Python interpreter.  See the section "How to Install &amp; Run Leo" for details.</t>
<t tx="edream.110203163054.625">Previous version of leo.py did not release memory when windows close.  This version does.

Memory management is remarkably easy in Python/Tk.  Added __del__ routines and corresponding destroy routines to the frame, vnode and tree classes.  The destroy routines eliminate circular references between objects. The __del__ routines do nothing except print debugging traces; we know that all references to an object have been removed when its __del__ routine is called.

Added app.deleteOnClose ivar to control memory management.  When true, Leo deletes all frame objects when a frame closes.  This is always true at present.

Fixed a memory botch: previously a dummy vnode was allocated for every vnode created while reading files.</t>
<t tx="edream.110203163054.626">Starting with this release, you will see trace statements throughout the code.  The trace function is defined in leoUtils.py; trace implements much of the functionality of my Sherlock tracing package.  Traces are more convenient than print statements for two reasons: 1) you don't need explicit trace names and 2) you can disable them without recompiling.

In the following examples, suppose that the call to trace appears in function f.

trace(string) prints string if tracing for f has been enabled.  For example, the following statement prints from s[i] to the end of the line if tracing for f has been enabled.

	j = skip_line(s,i) ; trace(s[i:j])

trace(function) executes the function if tracing for f has been enabled.  For example,

	trace(self.f2)

You enable and disable tracing by calling init_trace(args).  Examples:

	init_trace("+*")         # enable all traces
	init_trace("+a","+b")    # enable traces for a and b
	init_trace(("+a","+b"))  # enable traces for a and b
	init_trace("-a")         # disable tracing for a
	traces = init_trace("?") # return the list of enabled traces

If two arguments are supplied to trace, the first argument is the "tracepoint name" and the second argument is the "tracepoint action" as shown in the examples above.  If tracing for the tracepoint name is enabled, the tracepoint action is printed (if it is a string) or executed (if it is a function name).

"*" will not match an explicit tracepoint name that starts with a minus sign.  For example,

	trace("-nocolor", self.disable_color)</t>
<t tx="edream.110203163054.627">Rewrote the code that computes file names.  This should have two beneficial effects:

Note:  This code has only been tested on Windows XP.

1. The code should be more portable.  I've used os.path.join throughout to concatenate parts of filenames, and this should handle differences involving path separators on different platforms.

2. The code no longer calls os.chdir().  The "current application directory" changes only as the result of completing file open and save dialogs.  In particular, @path, @root and @file do not change the current application directory.

3. Used leo.__file__ to get the directory from which leo.py was loaded.  This seems to be reliable, though it has only been tested on Windows XP.</t>
<t tx="edream.110203163054.628">The following features of leo.py will be incorporated into the Borland version 2.6 of Leo:

1. Improve leading whitespace handling in Tangle.

2. Fix clone bugs (rewrite vnode::setDirty).  These bugs can cause errors while reading @file nodes.

3. Improve Find/Change commands. Change "batch" to "context".  This will make the Preferences Panel work identically in both programs.

4. Always recompute file indices and compute file indices.  This will make derived files produced by v2.6 identical to the files produced by leo.py.

5. Make sure all file names end in .leo.</t>
<t tx="edream.110203163054.629">I urge anyone using leo.py upgrade to this version.  This is the first version of leo.py that has been thoroughly tested.

See the children of this node details about this release.  Here are the highlights:

1. Fixed many bugs, including a bug that can cause body text to be lost when creating a new headline.

2. The Python window now works. You can now run Python scripts from within leo.py!

3. Added a script to convert Leo files from Leo 1 to Leo 2 format.

4. @nocolor and @color are now inherited properly from ancestor nodes.

5. Added Leo Documentation to Help menu.  This command opens LeoDocs.leo.
	
6. Added auto indent to body pane.

For even more details, see the diary entries for January 6-9 in LeoPy.leo.

See the To Do lists in LeoPy.leo for a list of unfinished features.  The primary unfinished features are the Find/Change commands, preferences settings and the Tangle/Untangle commands.</t>
<t tx="edream.110203163054.630">This is the first version of leo.py that has been heavily tested.  About 70 percent of my work on leo.py has been done using leo.py itself.   I know of no remaining bugs that can cause data to be lost.</t>
<t tx="edream.110203163054.631">I have concentrated on removing all significant irritations encountered while using leo.py.  Far fewer still remain than before.  Among the remaining irritations:

1. Syntax coloring happens at "idle time", that is, after all events have been handled.  This means that characters are initially colored black, then changed to another couple after an obvious delay.  The obvious event-handling code does not work.  Perhaps using a "virtual event" may work.

2. Keystrokes that should initiate commands _also_ get passed to widgets.  I am hoping to find a way around this, and it may take a bit of work.  The two biggest offender:  Control-k while editing a headline deletes from the cursor to the end of the headline (in addition to creating a new node!)  Control-i gets passed to the body pane as a tab.

3. The border around the tree pane gets over-written by headlines.  I'm not sure how to fix this: it is certainly a Tk bug.</t>
<t tx="edream.110203163054.632">Fixed a bug that can cause body text to be lost when creating a new node.</t>
<t tx="edream.110203163054.633">Choosing Open Python Window brings up IDLE, the standard Python IDE, from which scripts may be run and debugged.

Note: The path to idle.py must exist in sys.paths.  For Python2.1 on windows, this path will typically be \Python21\Tools\idle  If this path does not exist, a message will be sent to the log pane.  The usual way to add a path to sys.paths is to modify the sitecustomize.py file.

Changed names of several vnode and commands methods to make them compatible with the scripting documentation on Leo's web site.   You may now run any script that runs on Borland Leo on leo.py.

When running scripts from leo.py, you may refer to any method or instance variable (attribute) in the code for leo.py.  If you want to run those scripts on Borland Leo you should restrict yourself to the methods documented in the Scripting chapter of Leo's online documentation.</t>
<t tx="edream.110203163054.634">To convert an @root tree to an @file tree, choose the root of the tree to be converted, then do the following in the Python window:

	import c2py
	c2py.leo1to2()
	
This script makes numerous changes throughout the tree.  It does not, however, change @root to @file, or insert the needed @others directives.  You must do that by hand.</t>
<t tx="edream.110203163054.635">At long last it is possible to open this file, LeoDocs.leo, from the help menu.

This command will work only if LeoDocs.leo is located in the directory in which leo.py exists.</t>
<t tx="edream.110203163054.636">The body pane now has auto-indent on at all times.</t>
<t tx="edream.110203163054.637">leo.py version 0.06 (alpha)                     December 20, 2001

This version fixes several minor problems that prevented leo.py from running on Linux.  There is no need to upgrade to this version if leo.py works on your system.  This version is neither more nor less stable than version 0.05.  This file, LeoDocs.leo, has also been improved substantially.

There still may be problems running leo.py on Linux.  You may be able to fix those problems yourself after reading this file... I'll be on vacation until about January 8.  I may be able to answer questions on Leo's SourceForge site, and I'll make no code changes until then.

Problems fixed:

1.  Removed call to print_stack() in es() logic.  If there are problems during initialization this logic printed "Null log" and then printed a stack dump.  This dump was more confusing than helpful.

2.  Changed "darkblue" to "DarkBlue".  The standard colors known to Tk are listed at
	http://tcl.activestate.com/man/tcl8.4/TkCmd/colors.htm
	
If you have more problems with unknown colors, please use a color listed above.

3.  Eliminated some accelerators (Linux only).  You may take an exception in createAccelerators() in leoFrame.py if Linux does not support the accelerators defined in one of the following sections:

  &lt;&lt; control key bindings &gt;&gt;
  &lt;&lt; alt key bindings &gt;&gt;
  
Just comment out the relevant entry.  Please let me know which accelerators don't work.  I can add platform-specific code to deal with them.

4.  Added loaddir code to leo.py.  Leo tries to guess where leo.py was loaded from.  If this doesn't work leo may take an exception in leo.py.

As a temporary hack, please set loaddir correctly in the following code at the start of leo.py:

  # loaddir should be the directory that contains leo.py
  if sys.platform=="win32":
    loaddir = "c:\\prog\\LeoPy\\"
  else:
    loaddir = "LeoPy"
	
5. Removed bullet 0x95 characters from this file. They don't show up well on Linux.

6. In leoTree.py, changed the filenames from x.gif to x.GIF.  Linux is more picky about case in filenames than Windows.

Edward K. Ream
December 20, 2001</t>
<t tx="edream.110203163054.638">leo.py version 0.05 (alpha)                      December 17, 2001

This version of Leo marks a major milestone in Leo's history.  leo.py is the first functional version of Leo written completely in Python and Tkinter, Python's interface to the tcl/Tk system.

leo.py is quite useable. leo.py should work on any machine with recent Python and tcl/Tk interpreters.  This version of Leo was created using Windows XP, Python 2.1 and tcl/Tk 8.3.

Warning: This version is alpha quality.  Use extreme caution: please save your work often and make full backups of all .leo files and derived files.

Please read this node's children before sending bug reports or feature requests.  Send all bug reports to Leo's SourceForge web site at: http://sourceforge.net/projects/leo/

Edward K. Ream</t>
<t tx="edream.110203163054.639">I have been happily using leo.py to develop itself for the last three days without serious problems.  leo.py reads and writes all its source files exactly as does the Borland version.  This is an important test, and significant errors may remain.

Performance on a 1.2 Ghz Pentium is good to excellent.  Drawing the screen happens quickly, smoothly and without flicker.  Expanding and contracting nodes is usually excellent, and slows when a many nodes have been expanded.  Syntax coloring appears instantaneous, even with an unsophisticated algorithm.  Loading LeoPy.leo files takes about 3 seconds. This could be improved by using Python's XML classes.</t>
<t tx="edream.110203163054.640">You must have recent versions of Python and tcl/Tk installed on your machine.
Download Python from http://python.org/
Download tcl/Tk from http://tcl.activestate.com/software/tcltk/

After installing Python and Tk, run Leo double clicking the file leo.py in the LeoPy folder.  On Windows this will bring up a Leo window and a black Python interpreter window.

The LeoPy folder contains all files in this distribution.  leo.py is the main source file; run Leo by double clicking leo.py.  The Python interpreter will create corresponding .pyc files as .py files are imported by leo.py.

LeoPy.leo is the master source code file; all .py files were derived from LeoPy.leo.  c2py.py and leoCompare.py are tools that should be run from a Python interpreter.
</t>
<t tx="edream.110203163054.641"></t>
<t tx="edream.110203163054.642">Functional Commands and Features

    Open, Save, Save As, Save To commands.
    Read @file Nodes command.
    Read Outline Only command.
    Write Outline Only command. Warning: this has not been tested thoroughly.
    Insert Node, Delete Node and Clone commands.
    Move Node Right/Left/Up/Down commands.
    Cut Node, Copy Node, Paste Node commands.
    Syntax coloring for Python only.
    The @color and @nocolor directives, but these are not inherited yet.</t>
<t tx="edream.110203163054.643">Unfinished Commands and Features:

	Revert.
	All Tangle and Untangle commands.
	All Import commands.
	All Find and Change commands.
	Sort Children command.
	Toggle Split Direction, Toggle Active Pane and Cascade commands.
	Auto indent in the body pane.
	The Preferences panel is semi-functional: see note one below.
	The Find panel is non-functional.
	The Python scripting window is non-functional.
	Syntax Coloring Options and Font Options windows are not ready yet.
	@color and @nocolor directives are not inherited yet.

Notes:

1. The Preferences panel is partly functional.  The default target language option has no effect: syntax coloring is for Python only.  Tab width can not be changed; tabs are 8 characters wide.

2. Menu items are not yet dynamically dimmed and undimmed.  Some non-functional commands have undimmed menus.  Keyboard accelerators work even for dimmed menus.

3. Scripting Leo is not possible yet.  You can't control Leo from the Python interpreter because control passes to the Tk event loop.

4. Leo's Save commands do not yet save the information about which node was visible at the top of the tree.

5. The Save/SaveAs/SaveTo dialogs don't handle shortcuts to folders properly; they try to replace the shortcut with the .leo file.

6. Initialization code in leo.py computes the directory from which Leo was loaded using argv[0].  I am not sure this is proper, though I have had no problems recently.  Tree icons will not load properly if argv[0] does not specify this directory.  If the path is invalid Leo will print: os.chdir failed: `dir`

7. The tree class does not automatically ensure that the current node is visible after an outline operation.

8. The font used in the body pane is not great.  I hope to improve it.

9. Headline text is sometimes obscured.
</t>
<t tx="edream.110203163054.644">leo.py already feels less buggy than the wxWindows versions of Leo.  Rewriting Leo in Python and Tkinter has greatly improved the code. Further improvements are possible.  BTW, work began in earnest on this version of Leo in late October, 2001.  It's been a great month.

The following problems have resisted my initial attempts at solving them.  Any help from Tk experts would be appreciated:

1. Window icons are the Tk icon, not the nifty Leo icon.  Really, there _must_ be a way to do this!

2. Can variable-width tabs can be done in Tk?  If not, Leo may have to convert tabs to blanks as specified by the preferences panel.

3. Cut, copy and paste work in the log and body panes using Control-X, Control-C and Control-V keys.  However, there are no Cut, Copy or Paste menu items in the Edit menu.  Is it possible to send simulated keystrokes to a text widget?

4. Some menu accelerators do not seem to be available in Tk.  In particular, many of the items in the submenus of the Outline menu have no accelerators yet.  These commands are useful only if they can be chosen from the keyboard rather than the menu.

5. The border of the tree control is gray.  It can be overwritten by large headlines.  This appears to be a Tk or Tkinter bug; I haven't found any way to eliminate the border or color it white.

6. There doesn't seem to be a way to select all the headline text when editing starts.  The click that starts editing always clears the selection.

7. Changing the type of leo.py to .pyw doesn't seem to work.

8. A message flash briefly on the screen when leo.py exits, too fast to read. These messages do not appear when invoking leo.py from the Python interpreter.  They probably would be visible in a Linux window.</t>
<t tx="edream.110203163054.645">It will be much easier to make such improvements to leo.py than to previous versions of Leo. Here is my list of new things to do:

1. Create "hyperlinks" from section references to section definitions.  This will happen in the next release.

2. Add automatic "tab nanny" checking and full syntax checking of Python body text.

3. Build a file/directory comparison window using code in leoCompare.py.

4. Build a Python debugger into Leo.  Python provides excellent hooks for debugging and tracing.  Python's stand-alone IDLE debugger doesn't seem to work well with the Tk command loop.

5. Expand Leo's file format to take advantage of the power of Tk text widgets.
</t>
<t tx="edream.110203163054.646"></t>
<t tx="edream.110203163054.647">Leo Borland version 2.6                             May 15, 2002

This version fixes a bug that can cause errors while reading derived files.  Earlier versions do not ensure that clone indices in derived files are distinct.

I recommend that all users of the Windows version of Leo upgrade to this version.</t>
<t tx="edream.110203163054.648">Leo Borland version 2.6                             March 4, 2002

leo.py v2.0 and Borland Leo v2.6 are being released simultaneously.  I urge all users of Leo to upgrade to one or both of these versions.  This is an important milestone in Leo's history,  For the first time, leo.py (v2.0) and the Borland Leo (v2.6) are functionally identical.  In particular, their respective Tangle commands produce identical output.

Borland version 2.6 fixes major problems and contains numerous changes to make it fully compatible with leo.py v2.0.  Highlights of Borland v2.6:

1. Fixes bugs that caused spurious errors while reading @file trees.  Such errors can destroy clone links.

2. Supports an improved format for derived files.  This format is used by leo.py 2.0.  This is an upward compatible change: previous versions of Leo can not read the new format, and this version of Leo can read all previous derived files.

3. Fixes two long-standing bugs in the Untangle command.

4. As mentioned above, the Tangle commands are byte-for-byte compatible with leo.py v2.0.  Also, @c is now equivalent to @code.

5. Adds two very useful commands: Sort Siblings and Contract Parent.

See the Children of this node for full details.</t>
<t tx="edream.110203163054.649">This version of Leo removes blanks from between sentinel lines in derived files.  This version of Leo is fully compatible with leo.py v2.0 in this regard.

This is an upward compatible change in the format of derived files: Borland Leo v2.6 can read derived files from all previous versions of Leo, but previous versions of Leo can not read derived files without blanks lines.

Removing blank lines requires a new kind of sentinel, the "verbatimAfterRef" sentinel.  This allows Leo to handle comments following section references that would otherwise be treated as sentinels themselves.  For example:
   
   &lt;&lt; section &gt;&gt; #+others</t>
<t tx="edream.110203163054.650">Whenever a node changes, Leo now ensures that all nodes cloned to it, and all ancestor @file nodes are marked dirty.  This is the cause of spurious read errors.

As a side effect, nodes now become dirty when they move.

This change was made in leo.py v0.8.

It is also vital that @file nodes remain dirty until they are written without errors.  Otherwise, a Save command will succeed without warning, and a later read may cause the dreaded "clones have been cleared" message.

This change was made in leo.py v1.0.</t>
<t tx="edream.110203163054.651">@c now works the same as @code.  This makes the syntax colorers agree with what the Tangle commands actually do.  Previously, the syntax colorers indicated that everything following an @c was code, while the Tangle commands placed everything following an @c in the doc part!</t>
<t tx="edream.110203163054.652">This version fixes two long-standing bugs:

1. Untangle did not work properly for languages like Perl and Python that do not have block comments. 

2. Untangle did not recognize @ on a line by itself as the start of a doc part.</t>
<t tx="edream.110203163054.653">The Tangle commands are now byte-for-byte compatible with leo.py 2.0.  Tangle outputs "optimized" leading whitespace just as leo.py does.  This can be important in Python programs.

All the Save commands now recompute clone indices just as in leo.py 2.0.</t>
<t tx="edream.110203163054.654">The "Show Context" checkbox in the Find Panel is presently non-functional.  (In leo.py it affects the messages produced by the Find All and Change All commands.)</t>
<t tx="edream.110203163054.655">Unlike leo.py, the Borland version of Leo can not ensure that saved outlines have .leo extensions.

There are two problems:

1.  The ensureExtension routine is called after the dialog closes.  If this routine changes the file name we could overwrite an existing file!

2.  There appears to be problems with the Borland DefaultExt field.  Setting this field causes crashes.</t>
<t tx="edream.110203163054.656">This version fixes several serious bugs.  All users of Leo2 should upgrade to version 2.5 immediately.

1. Eliminated the ill-fated automatic updating feature.  This turns out to be very dangerous and disconcerting.  If one makes changes to the .leo file and does not save those changes, a later update could erase those unsaved changes!

2. Removing automatic updating also fixed another bug:  The current outline node was not being selected properly when a .leo file was read, so that in some cases the body text did not correspond to the selected outline node.  This never caused loss of data, and was disconcerting.

3. Fixed a bug that caused Find/Change settings to be saved to a file only if a find or change command was actually executed.

4. Restored several parts of Leo2(cb).leo that were inadvertently erased due to earlier bugs.  In particular, the outlines for xbuf.c and xbuf.h have now been restored.

One bug remains.  On Windows XP, the cursor is obscured in the Find/Change dialog when it is at the far left of the Find or Change text areas.  This may be a botch in the XP text control itself.  The solution would be to create a border in the text areas, and there is no obvious way to do this using the Borland classes.</t>
<t tx="edream.110203163054.657">Version 2.4 is a major improvement in Leo2.  I urge all users of Leo2 to upgrade to this version.  See the children of this node for full details.

The "old" Leo2 tried to save space by not writing all information in @file trees.  This was a serious mistake.  The "new" Leo2 saves all information in an outline to the .leo file, including all information in @file trees.
Once again you may back up a project merely by backing up the project's .leo file.  There is no Archive command, and no need for one.  All .leo files are now safe archives.

As the result of the change in file formats, Leo 2.4 may clear clone links when loading derived files created with previous versions of Leo.  Leo 2.4 will issue detailed messages when that happens.

The new Leo2 is much safer and more convenient to use than the old Leo2.  Error messages and error recovery have been improved.

Leo2 updates @file trees automatically when Leo2 is activated.  For example, suppose you change a derived file in another editor, say in an IDE.  Leo2 will update the @file tree when you switch to Leo, provided that you have saved the file in the IDE.  Warning: due to several apparent bugs in the Delphi code, this feature only works if the main Leo window is at least partially visible on the screen (!)
</t>
<t tx="edream.110203163054.658">Version 2.4 fixes several bugs involving clones.

1. Version 2.4 rewrites clone indices when writing derived filed, so node sentinels accurately reflect the clone status of the node.  The node sentinel for the root node no longer contains the maximum clone index.  Leo2 clears the root's clone index on reading and writing so that the root node is not mistakenly joined so another node!

2. Version 2.4 takes more care to recreate clone links properly when reading derived files.  A derived file can be read into a .leo file different from the .leo that wrote the derived file, so Leo2 makes sure that clone links are proper in the .leo file being opened.  A minor drawback: .leo files now are "big", so reading them is a little slower.

Note: Clone links into @file trees work only if the .leo file is "in synch" with the files derived from the @file trees.  Clone links will break if the .leo file and derived files are not in synch.  Typically "backup" .leo files will be out-of-synch with present derived files, so it's best to use "backup" .leo files only in emergencies, for example to revert a project to a previous state.</t>
<t tx="edream.110203163054.659">The "old" Leo2 tried to save space by not writing all information in @file trees.  This was a serious mistake.  The "new" Leo2 saves all information in an outline to the .leo file, including all information in @file trees.  It is once again possible to back up a project merely by backing up the project's .leo file.</t>
<t tx="edream.110203163054.660">The archive command was a backup disaster waiting to happen.  It has been replaced by the following four file commands are located in the File:Read/Write submenu.

Read Outline Only: reads an outline using only the .leo file, not any files derived from @file nodes.  This command is useful for reverting a project to a previously saved state.

Read @file Nodes: updates all @file nodes in an outline.  This ensures that the state of an outline matches all files derived from @file nodes.  Included for completeness.  This happens automatically when a .leo file is first read, and it also happens automatically when Leo2 is reactivated.

Write Outline Only: saves an outline without writing any @file trees.  Useful for inserting an @file node into an outline without modifying a derived file with the same name.

Write @file Nodes: forces an update of all @file trees.  Surprisingly useful.</t>
<t tx="edream.110203163054.661">Leo2 updates @file trees automatically when Leo2 is activated.  For example, suppose you change a derived file in another editor, say in an IDE.  Leo2 will update the @file tree when you switch to Leo, provided that you have saved the file in the IDE.

Warning: due to several apparent bugs in the Delphi code, this feature only works if the main Leo window is at least partially visible on the screen (!)</t>
<t tx="edream.110203163054.662">Revised for version 2.4

Loading and saving .leo files usually keeps the .leo file and derived files "in synch".  However, if you create backup .leo files, it can easily happen that the structure of @file nodes in the backup .leo files no longer matches that structure in the derive files.  Leo2 will detect this condition the next time you next open the old .leo file.  When that happens, Leo2 discards the entire out-of-synch @file tree, and recreates it solely using the derived file.  In the process all marks and clone links from outside the file are lost. Leo2 issues the messages:

	Error reading @file &lt;filename&gt;
	-- Rereading file.  Clone links into this file will be lost.

to remind you that the .leo file you are using is out-of-date.  Saving the .leo file will bring it up to date.

If one or more sentinel lines in a derived file have been corrupted in some way, by inserting, deleting, altering or moving a sentinel, Leo issues these messages:

	Error reading @file &lt;filename&gt;
	&lt;An error message about a bad sentinel&gt;
	-- Rereading file.  Clone links into this file will be lost.
	&lt;An error message about a bad sentinel&gt; (again)
	----- File may have damaged sentinels!

Data may not actually be lost, and the outline structure will be seriously damaged.  The most sensible thing to do is to restore the derived file from a .leo file using the Read Outline Only command.

No error recovery is attempted when automatically updating @file trees.  If an error is found the update is canceled (leaving the outline unchanged) and the following message is given:

    -- Update canceled due to structure errors
	
We don't attempt error recovery because error recovery would clear clone links.  For example, suppose we are editing a .leo file, and for some reason we also edit a derived file _without_ saving the .leo file.  Now the files could be out of synch!  So it is best not to press on with an automatic update.
	</t>
<t tx="edream.110203163054.663">Revised for version 2.4

If Leo2 detects orphan or ignored nodes while writing an @file node it saves all information in the @file tree in the outline (.leo) file.  No information is lost.  When the .leo file is read again Leo2 will load the information in the @file tree from the .leo file, not the derived file.

As a reminder, Leo2 marks the erroneous @file node as dirty so that saving the .leo file will attempt to rewrite the @file node.  Version 2.4 no longer marks the @file node as "stuck on dirty".  If you save the .leo file the dirty mark will be cleared.  However, the @file node will be dirty every time the file is read until all errors are corrected.
</t>
<t tx="edream.110203163054.664">@file trees are less flexible than @root trees:

1.  You can not use section definitions in more than one file.  For example, you can't define declarations in one file to be used in another file.  If you need all the features of noweb you must use @root trees.

2. @file trees use no escape conventions whatever.  A code part in an @file tree contains a section reference if &lt;&lt; precedes &gt;&gt; on the line, regardless of whether &lt;&lt; or &gt;&gt; are contained in strings or comments.  In practice, such "false references" occur infrequently, and the workaround is simply to split the offending line.  Moreover, noweb's escape conventions (@&lt;&lt; and @&gt;&gt;) cause problems in @root trees, so this "drawback" is very minor.

3. Clone links into @file trees work only if the .leo file is "in synch" with the files derived from the @file trees.  In particular, backup .leo files will usually be out of synch with derived files.  Clone links will break otherwise.  To recover from such errors, simply use the "Read Outline Only" command.</t>
<t tx="edream.110203163054.665">Note: 10/19/01: I recommend that all users upgrade to version 2.4.  There are some serious problems with version 2.3.

This version of Leo contains some significant improvements.  See the children of this node for details:

1. The new @first directive allows you to place lines at the very start of files derived from @file nodes. For example, @first #!/usr/bin/env python

2. The log window is now part of the Leo window.  Very handy.

3. Fixed several bugs involving the Find command.

4. A new Archive command saves an entire outline (including all @file trees) to a .leo file.  Use this command with caution.  Loading and then saving a .leo file created with the Archive command will revert an entire project to the state it had when the archived .leo file was created.</t>
<t tx="edream.110203163054.666">The @first directive allows you to place lines at the very start of files derived from @file nodes. For example, the body text of @file spam.py might be:

@first #! /usr/bin/env python

The body text of @file foo.perl might be:

@first #/usr/bin/perl

@first directives are recognized only at the start of the body text of @file nodes.  No text may precede @first directives.  More than one @first directive may exist, like this:

@first #! /usr/bin/env python
@first # more comments.</t>
<t tx="edream.110203163054.667">The Archive command writes all nodes of an outline to a .leo file, including all parts of @file trees.  All @file trees are marked in such a way that when the archived .leo file is read 1) all @file trees will be restored from the archived outline rather from derived files and 2) all @file trees will be marked dirty so that when the archived .leo file is written all @file nodes will be updated.

Use the Archive command (and the files written by it) with caution: loading and then saving an archived .leo file will back up an entire project to its state when the archive was originally written!</t>
<t tx="edream.110203163054.668">Added support for @c in syntax colorers for Python, Pascal, Perl, Java and HTML.</t>
<t tx="edream.110203163054.669">Fixed a bug in the Change, Then Find command.  The Change, Then Find command would rescan the newly changed text if the "change text" contained the "find text" preceded by other text of length greater or equal to the length of the original "find text".

For example, changing "blah" to "const blah" would result in rescanning the newly inserted "blah".  This would cause the "Change All" command to hang.

The old code advanced the search point by the length of the "find text."  The new code advances the insertion point by the length of the "change text".

Fixed the Find/Change panel: some captions were cut off.</t>
<t tx="edream.110203163054.670">@file nodes are now marked dirty whenever any change is made in the @file tree, including changes made as the result of changing cloned nodes outside the @file tree.</t>
<t tx="edream.110203163054.671">Made the log window part of the Leo window.  Having the log be part of the leo window is very convenient.</t>
<t tx="edream.110203163054.672">Leo2 readme file
Borland version 2.2, 9/16/01

This version fixes several bugs in Leo2:

1. Fixed a bug that causes all data in an @file tree to be lost under the following conditions:

A. The @file tree was erroneous, i.e., it contained orphan or ignored nodes.
B. The .leo file containing the erroneous tree was saved twice.

Leo2 now marks an erroneous @file node as "stuck on dirty" until the tree is fixed.  Recall that dirty nodes have icons with a black border rather than a gray border.  Whenever a file Save operation occurs, Leo2 will attempt to write all dirty @file trees, thereby reminding you that errors remain.  However, the .leo file itself is not "stuck on unsaved", so you won't be prompted to save the .leo file endlessly.

While fixing this bug I also improved error and warning messages relating to reading and writing @file nodes.  This should make it clear that a) data in erroneous @file trees is saved to the .leo file and b) data is recovered from the .leo file when reading erroneous @file nodes.

2. Fixed a bug relating to clones that could cause loss of data.  Leo2 now marks all clones dirty when any clone changes, and makes sure to mark @file nodes dirty that contain changed clones.

3.  Changed the code that writes @file trees to end lines with "\r\n" rather than "\n".  I hope this will improve matters, though I have my doubts.  Please report any problems with the new scheme immediately.

4. Added Write @file Nodes command.  The command writes all @file nodes in the selected tree, regardless of whether they have been changed.

5. Made the commands in the Main Leo2 window functional.</t>
<t tx="edream.110203163054.673">Version 2.1 is the first public release of Leo2.  This version appears stable, and should be used with caution.

The major feature of Leo2 is that tangling and untangling happen automatically for all code derived from @file nodes.  

Remember to back up all files derived from @file nodes; such files are original source files!  It is no longer possible to back up an entire project by backing up a single .leo file.</t>
<t tx="edream.110203163054.674"></t>
<t tx="edream.110203163054.675">Version 1.15 can read @file trees.  Leo warns when reading @file files, and changing @file trees in Leo v1.15 is not recommended.</t>
<t tx="edream.110203163054.676">This version corrects a problem with double-clicking Leo icons under Windows Me.  You may now launch Leo by double-click the icon for any .leo file and you may open any .leo file by double-clicking on it.</t>
<t tx="edream.110203163054.677">This version of Leo corrects a problem with how whitespace was handled in @silent mode.</t>
<t tx="edream.110203163054.678">Barring serious bugs, version 1.12 is likely to be the last Borland/Windows version of Leo for a while.  The wxWindows versions of Leo are usable enough to justify putting all further work into them.

There are several important improvements in version 1.12:

1. Added the Sort command to the Outline menu.  This command sorts all the children of a node into alphabetical order.

2. A major improvement to Tangle.  In @silent mode, Tangle now outputs derived files with "verbatim" whitespace, that is, without any extra blanks, tabs and newlines.  This makes Tangle much more useful for Python, and in other applications.  For example, it is now possible to do the following in Python:

if &lt;&lt;condition1&gt;&gt; &amp;&amp; &lt;&lt;condition2&gt;&gt;:
	print &lt;&lt;list of vars&gt;&gt;

In the derived file, expansions of the sections will be placed on the lines in which the reference appears.  This works in Python as long as the expansions themselves appear on a single logical line.

This "verbatim" expansion only happens in @silent mode, so these kinds of derived files can not be Untangled.

3. Tangle now reports errors more fully and less redundantly.  Errors involving missing or erroneous path names (specified in @root directives, @path directives or the Preferences Panel) are more specific.  These errors are reported only once per Tangle command, and these errors terminate the Tangle command immediately.  This is wise; we don't want to write files to the wrong directory!  Finally, Tangle no longer prints the actual text of a section when giving the "possibly duplicate section definition" error.  This should be helpful: no longer are huge error messages generated.  It should be easy enough to find the relevant section definitions using Leo's find command.</t>
<t tx="edream.110203163054.679">This version corrects a problem that can cause the Import CWEB Files command to hang in an endless loop.

This file also contains improved documentation (see the children of this node) in two sections:

1.  Added an explanation of the following error message given by the Tangle command: "Multiple parts not allowed for &lt;&lt; section name &gt;&gt;"

2.  Added a warning about using Untangle to update cloned nodes.
(See the last paragraph of the node.)</t>
<t tx="edream.110203163054.680">Sections can be defined in several parts in two ways:

1.  Using &lt;&lt; section name &gt;&gt;= in several places with the same section name.

2.  Using several @code directives within the _same_ body text.

As a precaution against mistakenly defining a section in more than one place, it is invalid to use @code in different nodes to define multiple parts for the same section.  In particular, this error may arise when using cloned nodes.

This error may always be eliminated by using &lt;&lt; section name &gt;&gt;= instead of @code.
	
</t>
<t tx="edream.110203163054.681">The Untangle, Untangle All and Untangle Marked commands are the reverse of the corresponding Tangle commands.  They update an outline based on changes made to one or more derived files.  These are exceptionally useful commands.

For example, suppose you create a new part of the outline and Tangle it for the first time.  When you compile the resulting derived files for the first time, you are likely to get many syntax errors.  You could fix those errors in the outline and Tangle the outline again, but there is a much easier way:  you fix the errors in the derived files using the compiler's editor, then run the untangle command on the part of the outline that created the derived file.  The Untangle command updates the selected outline to match the changes in the derived files.  It's as simple as that.  By the way, the Untangle command marks all the nodes in the outline that it updates, and you can examine all such nodes with the Go To Next Marked command in the Outline menu.

You cannot use Untangle to update doc parts, or leading comments in code parts or "trivial" whitespace in code parts.  This is a limitation of the Untangle command that cannot be fixed; Untangle has no way of knowing whether leading comments came from doc parts or are just leading comments.

Untangle never changes the structure of an outline;  it never inserts, deletes or moves nodes.  Don't attempt to change the structure of an outline by modifying derived files; it won't work.  Also, never delete, move or alter the sentinel lines in derived files written by the Tangle command.  Such lines start with /// followed by a section name.

If you change the section name in a sentinel line Untangle will not update the code in the outline (with the old name) that generated the renamed section.  Untangle now warns about sections that appear in a derived file but not in the outline.  Untangle has no trouble with changed section references in derived files; it is only changed sentinel lines that cause problems.

Cloned nodes that generate code in several files may cause problems for Untangle if not all the code is changed the same way in derived files.  If Untangle is run separately on these derived files, Untangle will update all cloned nodes each time it is run, so only the code in the last Untangle run will take effect.  Therefore, the only reliable way to update text in cloned nodes is to make the change in the .leo file rather than the derived files.</t>
<t tx="edream.110203163054.682">Version 1.10 incorporates the following changes:

1. The Untangle command no longer updates @doc chunks under any circumstances.  This makes Untangle safe to use when the "Tangle outputs doc chunks" preferences is not selected.  In previous versions the Untangle command would delete all @doc chunks in the outline when a derived file had been Tangled without "Tangle outputs doc chunks".

The new version of Untangle is experimental; only one line of code has been added.  I welcome any comments about this change.  This change also fixes (or rather bypasses) a crasher reported in Untangle.

2. The shortcut for the Execute Script command has been changed from Alt-E to Shift-Alt-E to avoid conflicting with the shortcut that brings up the edit menu.

</t>
<t tx="edream.110203163054.683">Version 1.9 contains several improvements that make Leo more Python-friendly:

1. The Execute Script command (Alt-E) in the Edit menu allows you to execute Python scripts directly from body text.

2. Several small changes make the Python window significantly easier to use.

Also, considerable reference (study-only) code has been removed from leo(CB).leo.</t>
<t tx="edream.110203163054.684">It is now possible to execute any Python script directly from any body text.  Just select the script in the body text (including a trailing newline) and use the Execute Script (Alt-E) command from the edit menu.  The script is copied to the Python window and executed as usual.
</t>
<t tx="edream.110203163054.685">Several small changes make the Python window significantly easier to use:

1. The paste command now works in the Python window whenever the Python window is visible.  This fixes a bug that required a mouse click in either pane before paste would work.

2. It is now possible to execute scripts multi-line scripts pasted into the input pane.  Other changes make it easier (or possible) to terminate continued code.</t>
<t tx="edream.110203163054.686">Fixed a crasher that makes it impossible to tangle outlines containing doc parts in languages like HTML that have no single-line comment delimiter.</t>
<t tx="edream.110203163054.687">Leo v 1.7 accepts a slightly more general file format so that it can read XML generated from external XML tools.  Leo v 1.7 can read all previous .leo files.  Leo's Save commands remain unchanged.

Leo still only understands Leo files.  However, Leo now understands a slightly generalized form of Leo files. Specifically:

1.  Attributes may now appear in any order.  (Leo writes attributes in a fixed order, but some XSLT tools rewrite Leo files with attributes in a different order.)

2.  Leo will now accept &lt;tag/&gt; instead of &lt;tag&gt;stuff&lt;/tag&gt; when "stuff" is empty.
</t>
<t tx="edream.110203163054.688">This version corrects a small bug: the wrong text is selected when the syntax colorer changes.  This is a cosmetic bug only; the selected text will not be replaced when further typing occurs.

Unless major bugs are found, this will be the last version of Leo for several months.  I want to freeze the code so that I can work on the wxWindows version.</t>
<t tx="edream.110203163054.689">This version is a major milestone in Leo's code.  Improvements were made throughout Leo's code in an attempt to correct an extremely hard-to-find bug that can cause data in body panes to be lost.  Only time will tell if the bug has, in fact, finally been eradicated.

This version also corrects a minor bug; icons in a newly cloned tree were not always drawn properly.  Also, the currently selected headline no longer changes if you click on the + or - icons that expand and contract headlines.  This new behavior is a result of simplifying the event handlers; I won't consider changing this behavior until it is clear that the data loss bug has finally been fixed.

Use this version of Leo with caution until the new code has been thoroughly tested.  New asserts will guard against silent data loss and other unexpected events.  I don't expect these asserts to fail, but then one never does...

The following lists the changes that were made the code.  You don't need to read the following details; they are provided only for completeness.

1.  Greatly simplified the event handlers.  This should have been done long ago.

The event handlers now handle _all_ aspects of switching tree nodes and updating data structures when the body pane changes.  In particular, this guarantees that tnodes are "synched" when the body pane changes.  This is a major simplification and a major improvement: it should no longer be possible to lose data once it appears in the body pane.

The reverse is not true: the code must still take care that the body pane is updated if tnodes are changed "by hand."  (This is typically done when new nodes are being created.  Such nodes are never the current node and so are not shown in the body pane.)  I re-checked all code to make sure this constraint is satisfied.

Removed synchVnodes and updateBodyPane methods.  These have always been the most error-prone methods in Leo.  Removing them was made possible because the global constraint that tnodes are up-to-date is now guaranteed by the event handlers.

Created a new updateSyntaxColorer routine, which is called when moving a node or changing its text might affect syntax coloring.  This routine can never affect tnodes.

2.  Removed reference counting from tnodes.  The new code deletes tnodes only during the read process.  After that, tnodes are never deleted.  This could be called a memory leak, but it ensures that tnodes can never be deleted out from under a vnode.  I don't this was ever the problem with losing data, and the new code makes sure that it can't be.

3.  Improved how icons are redrawn.  Event handlers now set the dirty bit when text changes, which simplifies matters.

4.  Added asserts to guard against silent data loss, unexpected calls to event handlers, and mismatches between vnodes and their commanders.

6.  Added the mCommands data member to vnodes.  This member ensures that the correct commander is returned by vnode::commands().  The old code got the commander by looking for the current window.  Conceivably this could have caused the wrong commander to be used in some cases.</t>
<t tx="edream.110203163054.690">This version adds the following features:

1. Outline to noweb command.
2. Python scripts for finding and changing text in Leo outlines.
3. A Python method of the vnode class returning the commander corresponding to a vnode.
4. Documentation for Leo's import/export commands.

This may be the last version of Leo for a while; I am about to start work on a cross-platform wxWindows version of Leo.  However, bug reports and requests for new features are always welcome.

Edward K. Ream
September 19, 2000
</t>
<t tx="edream.110203163054.691">The "Outline To Noweb" command converts the selected outline to a flat file containing noweb text.  The name of the root section is taken from the @root directive.  &lt;&lt;*&gt;&gt; is used if the @root directive is not followed by any file name.</t>
<t tx="edream.110203163054.692">Leo's Python scripting does not support Leo's Find and Replace commands directly because these commands are interactive.  Calling these commands from a Python script would be clumsy.

Instead you can use the new find and change scripts to search and replace text.  These scripts use Python's powerful re module.</t>
<t tx="edream.110203163054.693">The commands() method has been added to the Python vnode class.

c=v.commands()

This method returns the commander for the window containing v.  This method can be used to avoid passing commanders as arguments to vnode methods.  For example, given just v, we can call either of the following:

	v.commands().synchNode()
	v.commands().Repaint()</t>
<t tx="edream.110203163054.694">This version corrects a problem with the Save As command;  it worked only once!  That is, after the Save As command was executed the window's title would change, but a later Save command would change the file specified before the Save As command was executed.</t>
<t tx="edream.110203163054.695">This version of Leo introduces Python scripting.  This is a major new addition to Leo.  See the new Chapter 7 of this documentation.  Python support still has rough edges; the next release will be cleaner.  Any suggestions for improvements to Leo's support for Python would be appreciated.

Alt-V now toggles the "View All Characters" option.  This is especially useful when editing Python code.

Besides Python support, a number of minor bug fixes have been made:

Added syntax coloring for try and catch to the C parsers.

Control-K, I now indents blocks of text uniformly, regardless of the language being syntax colored, and regardless of @nocolor and @color directives.  Similarly, Control-K, U now undents blocks of text.  The old keys, control-[ and control-] only worked when the current language was C and syntax coloring was enabled.

Removed the menu items that had the enter key as a shortcut.  The only way to create a new node now is with Control-I.  Using the enter key for a shortcut is not a good idea: it causes problems throughout the code.

Fixed a bug in forgiving compare.  The code that was calling compare_comments wasn't handling mismatched whitespace properly.

Got the Import command for Python working.  I found a bug in Tangle: in @silent mode we must always output a newline in the place of the function name.  Otherwise the Python indentation will be wrong.

The Untangle is now disabled when in @silent mode.  Nothing good can happen in that case!

Fixed a minor problem with the @path directive:  ff a _new_ file has not been saved we issue a warning, not an error if no path has been specified.  We can't really test the @root command for a path because the @root command may be found much later.  Fortunately, this warning will happen very rarely.  It's important, however, to warn that the file may be written to the standard directory if no path is specified in the @root command.  Otherwise, Leo's behavior would be quite confusing.</t>
<t tx="edream.110203163054.696">This version corrects an oversight in the Flatten Outline command.  In order to recreate the outline structure it is not enough to know whether each node has children; you must also know how many children each node has.

The new version of the Flatten Outline command represents the outline the same way the Export MORE Text does:  a child headline is indented one tab more than its parent headline.</t>
<t tx="edream.110203163054.697">The Tangle commands now examine all nodes, including cloned nodes that have previously been visited.  Previously, such nodes were skipped during tangling.  The new logic allows clones to represent code common to more than one unit. You can always insert an @ignore directive in an ancestor of a cloned node to prevent the node from being processed during tangling.
</t>
<t tx="edream.110203163054.698">Version 0.19 fixes some bugs and eliminates some problematic features of Leo.  Also, the role of CWEB mode has been documented more thoroughly.

The PC version of PC is feature complete.  I will release version 1.0 after people have played with this version for a while.

As always, I'll be happy to fix bugs or add urgently needed features.
</t>
<t tx="edream.110203163054.699">Fixed a bug that could result in Tangle outputting derived files in the wrong directory.

Tangle and Untangle now set the current directory using @path directive if it exists, otherwise the directory specified in the Preferences panel if it exists, otherwise the directory set by the Load or Save commands if it exists.  (The Save As and Save To never alter this directory.) Finally, a check to see if the @root directive specifies a full path.  If so, the current directory is not changed.

If none of these directories exists an error is raised so that no Tangling or Untangling is done.  This error can only occur if Tangling or Untangling a file that has just been created by the New command and never saved with the Save command.</t>
<t tx="edream.110203163054.700">Added the @language html, @language perl and @language perlpod directives, and added HTML, Perl and Perl + POD items in the Preferences panel.

The HTML script is rudimentary at present.  Suggestions for improvement are welcome.</t>
<t tx="edream.110203163054.701">The @cweb and @noweb commands are no longer functional.  The new @language cweb directive replaces @cweb, and the other @language directives effectively replace @noweb.  There is an new CWEB option in the Preference panel.
</t>
<t tx="edream.110203163054.702">Leo now parses the @language directive as you type, so if you change the language specified by the @language directive you will see the effect immediately.

There is no longer a limit of 6 languages that can be syntax colored. Let me know if you would like Leo to support another language.</t>
<t tx="edream.110203163054.703">The Print command is now much more flexible and convenient: it will print any node and all its descendents, whether or not the node contains @unit, @root or @ignore directives.  
</t>
<t tx="edream.110203163054.704">Modified massage_block_comment so that it converts the first of a series of newlines to a blank and deletes the rest; Untangle no longer mangles modified @doc sections.

A more complete solution would be for Tangle to insert a flag for inserted newlines ( say backslash newline) so that Untangle could know which newlines to remove.  I'd like to wait until all Tangle/Untangle code is converted to C++ before doing a more thorough job.
</t>
<t tx="edream.110203163054.705">Leo no longer supports clone _windows_.  Cloned outlines, however, will remain with Leo forever.  

Clone windows were never very useful and were buggy.  Eliminating clone windows has made it possible to handle events more smoothly and powerfully.</t>
<t tx="edream.110203163054.706">The Extended Noweb Syntax option in the Preferences panel is gone.  This option has always been deprecated.</t>
<t tx="edream.110203163054.707"></t>
<t tx="edream.110203163054.708">Version 0.18 changes the file format in an upward compatible way.  That is, version 0.18 can read all previous versions of Leo files, but you must have version 0.18 of Leo to read files written by version 0.18.</t>
<t tx="edream.110203163054.709">Fixed a bug that caused @doc section not to be output properly for those languages like Fortran and Perl that do not have block comments.</t>
<t tx="edream.110203163054.710">The @noheader directive suppresses the header line normal written by Tangle at the start of each derived file.  The @noheader directive is especially useful in Perl.  Also added the corresponding "Tangle outputs header line" checkbox in the preferences panel.  This checkbox sets the default which may be over-ridden by the @header or @noheader directives.</t>
<t tx="edream.110203163054.711">@language fortran specifies that comments start with C.
@language fortran90 specifies that comments start with !.</t>
<t tx="edream.110203163054.712">@language perlpod specifies the Perl language with block comments being delimited by =pod and =cut</t>
<t tx="edream.110203163054.713">Version 0.17 fixes some bugs and puts some finishing touches on Leo.

The Borland C++ Builder version of Leo is now feature complete; there are no further items on the to-do list.  Yes, I'll be happy to fix bugs or add urgently needed features.
</t>
<t tx="edream.110203163054.714">Tangle and Untangle now treat &lt;&lt;*&gt;&gt;= as a synonym for @root filename if the _headline_ starts with text of the form @root filename.  This convention allows full compatibility with noweb.
</t>
<t tx="edream.110203163054.715">The @path, @tabwidth and @pagewidth directives are new.

These directives allow the user to override the defaults specified in the Prefs panel on a file-by-file basis.   For the first time, every option in the Preferences panel may be overridden by a directive.</t>
<t tx="edream.110203163054.716">I fixed several severe bugs involving CWEB mode.  It is now possible to tangle and untangle files when in CWEB mode, though CWEB mode has still not been tested thoroughly.</t>
<t tx="edream.110203163054.717">Reduced the default size of Leo windows so that they can be more easily resized on a small screen.</t>
<t tx="edream.110203163054.718">Version 0.16 is a significant new release of Leo.  All users of the PC version of Leo should upgrade to version 0.16.

Significant changes have been made to Tangle and Untangle:  these commands should now be able to handle code in almost any language.  The new @language directive specifies the comment and string conventions used when Tangling and Untangling.

The @verbose, @terse and @silent directives are new:  they control how Tangle outputs comments.

The Import Files command now handles Pascal, Python and Java files in addition to C and C++ files.

Besides the major changes a number of bug fixes and other minor features have been added.

Acknowledgements:  Thanks to Zak Greant for numerous suggestions and bug fixes, and to Garold Johnson for improving this file.</t>
<t tx="edream.110203163054.719">Version 0.16 fixes all bugs mentioned on the SourceForge site as of April 27, 2000.  These bugs involved problems with

@comment &lt;empty&gt;
@comment 2 delims
Not inheriting @comment properly
non-delimited filenames in @root directives
Crashes while Tangling
Problems with Untangle with languages other than C.

Later sections discuss some of these in more detail.</t>
<t tx="edream.110203163054.720">Version 0.16 fixes a crasher related to changing windows.

This _may_ have been the source of crashes when cutting and pasting outlines, but don't count on it!  Make sure you back up files _before_ cutting and pasting outlines!</t>
<t tx="edream.110203163054.721">The @language directive is new.  The @language directive actually specifies the comment delimiters and string types used by the Tangle and Untangle.

The form of this directive is

@language x

where x is one of the following: c,c++,html,java,objective-c,pascal,perl,python and shell.  Shell files have comments that start with #.  Case is ignored in the language specifiers, but not in the @language itself.  Thus, the following are equivalent:

@language html
@language HTML
@language hTmL

but the following is invalid:

@LANGUAGE html

The @comment directive is now officially deprecated: you should use the @language directive whenever possible.  At present Untangle will not process an @root or @unit node if an @comment directive is in effect.  Why?  Because Untangle can't be sure of properly parsing a derived file if the language of the derived file isn't known.  It might be possible to assume some defaults in this case, but that is not done at present and is not a high priority.</t>
<t tx="edream.110203163054.722">Scanning for @directives is now much faster.  As a result, the @language and @comment directives will be recognized anywhere in an outline.  This means

1) child nodes will "inherit" @language or @comment directives from ancestors unless over-ridden in the child node and

2) @language and @comment directives need not be placed in @unit or @root nodes.  This is a much more intuitive and powerful way of handling these directives.</t>
<t tx="edream.110203163054.723">Key parts of the untangle logic have been generalized so that they can handle essentially any computer language. The following routines no longer have any C-specific code and have essentially been completely rewritten:

scan_derived_file (formerly scan_c_file)
forgiving_compare (formerly c_compare)

Tangle now will properly output comments using the present comment delimiters as specified by either the @language directive or the @comment directive.  As mentioned before, you should use @language instead of @comment wherever possible.</t>
<t tx="edream.110203163054.724">As a side effect of the Untangle command, Leo now removes trailing blank lines from the body text of all nodes being untangled.  This finally crushes a long-standing bug.  If the body text ends with one or more blank lines, the altered body text contains exactly one trailing newline.

Nodes that are altered in this way are not marked, nor is the file-changed mark set.  This seems to be the most appropriate action to take:  it would be confusing to prompt the user to save a changed file if the only changes involve trailing whitespace.</t>
<t tx="edream.110203163054.725">The @verbose, @terse and @silent directives determine how Tangle outputs comments.  When @verbose is in effect Tangle outputs all comments.  When @terse is in effect, Tangle outputs only those comments necessary for Untangle to work.  When @silent is in effect Tangle no additional comments.  Note: comments written by the user in code sections are always output: these directives control only:

1.  The comments containing doc chunks and
2.  Sentinel comments that delimit the beginning and end of code chunks.

@verbose is the default.  If more than one of these directives appear in the same body text the "most verbose" of these options will be in effect.</t>
<t tx="edream.110203163054.726">At long last Leo has a useful notion of default directory.  By default, the default directory is the directory containing the .leo file.  This may be over-ridden using the "Tangle Default Directory" option in the Preferences panel.

The default directory is used whenever a file name in an @root directive contains no path component.
</t>
<t tx="edream.110203163054.727">The Import Files command looks at the file extension to see how it should handle files.

Extension	Language
.c			C
.cpp		C++
.java		Java
.pas		Pascal
.py			Python

If the extension is not one of the above the Import files commands merely puts the entire file into the body text of a single node.

The Import Files command probably needs quite a bit of work.</t>
<t tx="edream.110203163054.728">Control-T now changes the pane that is currently active.  If the outline pane was active, the body pane becomes active, and vice versa.  This command makes it possible to switch between panes without using the mouse.</t>
<t tx="edream.110203163054.729">In previous versions of leo.leo I used slash instead of backslash as path delimiters.  This should never have worked, but somehow it did.  The present code uses the correct backslash in all @root directives.</t>
<t tx="edream.110203163054.730">Many improvements were made to the code.  See the diary section of leo.leo if you are interested.  In particular, I created args.h and args.c to define arguments.  This cleans up the code quite a bit.</t>
<t tx="edream.110203163054.731">Changed Tangle and Untangle so that empty section names like &lt;&lt; &gt;&gt; and &lt;&lt; &gt;&gt;= are treated as ordinary characters.  No warning is issued, which is debatable.</t>
<t tx="edream.110203163054.732">As mentioned in the main documentation, you must not change sentinel lines in derived files in any way.  In particular, if you change the section name in a sentinel line Untangle will not update the code in the outline (with the old name) that generated the renamed section.  Untangle now warns about sections that appear in a derived file but not in the outline.  Untangle has no trouble with changed section references in derived files; it is only changed sentinel lines that cause problems.
</t>
<t tx="edream.110203163054.733">Leo is being used to develop HTML files for web sites.  In this context it is natural to define sections that are shared between files.  Don't expect Untangle to update such sections if you make changes to them in derived files.  The natural place to change sections shared by several roots is in the outline, not in the files derived from the outline.

If you do change code in a derived file that appears in several derived files, and try to use Untangle to update the code in the outline one of two things will happen:

1) You untangle an @root node.  Untangle will never compare examine the common section of code for changes, as the common section appear under a @unit node, not the @root node. Untangle will complain about an orphan node.
 
2) You untangle an @unit node.  Untangle will examine each @root node under the @unit node.  Unless the change is made in the last root examined, Untangle will propagate the change when it first sees it, then go right ahead and undo the change when it sees the next expansion of the node in a derived file.
 
Untangle tests for inconsistent expansions of a section only within a single derived file.  Such tests are not done between different derived files because we do not want disallow sections with the same names in different roots.</t>
<t tx="edream.110203163054.734">Known bugs and limitations in all versions of Leo.

1. Untangle has no way of updating a section(chunk) whose name has been changed in the derived file.  Because of the @unit directive, there is not even a way to issue a meaningful warning.

2. Tangle treats @c like @code when in CWEB mode.
I recommend changing @c to @&lt; c @&gt;= throughout your CWEB sources and adding a reference
to @&lt; c @&gt; in all roots of CWEB files.

Known bugs and limitations of the PC version of Leo.

Syntax coloring options are not saved to the file.

The Log window has a limited capacity. This mainly affects debugging traces but could affect the output from the Tangle or Untangle commands if you tangled or untangled a large number of files.
</t>
<t tx="edream.110203163054.833">The Execute Script command executes body text as a Python script.  Leo execute the selected text, or the entire body text if no text is selected.

Scripts are executed in a "pristine" environment, that is, with __builtins__ as both the local and global environments.

New in version 4.1:  Body text may now contain @directives and section references. This is a major step forward: you can now use all of Leo's features to organize scripts that you execute interactively.

Section definitions must appear in the node containing the script or in descendant nodes.  Leo "preprocesses" all scripts by simulating the writing of a derived file to a string.

The Execute Script command sets app.scriptDict["script1"] to the value of the script before preprocessing, and sets app.scriptDict["script2"] to the value of the script after preprocessing.  Scripts may examine and change app.scriptDict as they please.</t>
<t tx="edream.110303182253.3">Leo does an auto-save only if something has actually been changed.</t>
<t tx="edream.110303182253.39"></t>
<t tx="edream.110303182719">The config_encoding setting controls the encoding of non-ascii characters in leoConfig.txt.

The use_gnx setting in leoConfig.txt determines whether uses gnx's (cvs friendly) or ints.  No version of Leo before 4.1 can read .leo files containing gnx.   Only gnx's are immutable.  Leo recomputes all non-gnx indices from scratch whenever writing a .leo file. It is possible to convert between 3.x and 4.1 file formats by changing the use_gnx setting.
</t>
<t tx="edream.110603185805">Leo 4.1 beta 5                   December 5, 2003

This is the fifth release of the reorganized 4.1 code base.

For the first time in months there are no serious bugs outstanding.

Warning: By default Leo 4.1 creates .leo files that can not be read by older versions of Leo.

Warning: Use the __wx_gui.py plugin with extreme caution until further notice:
bugs in this plugin could cause body text to be cleared improperly when changing nodes.

Beta 5:
  * Leo runs in batch mode when invoked with --script aScriptFile.py
    - Created "null gui" classes that do not use any gui code.
  * Leo supports Unicode characters (e.g. Chinese) in path and file names.
  * Fixed several long-standing bugs:
    - Fixed several minor problems with the Extract Section and Import commands.
    - Fixed problem that prevent the Find panel from working on the Mac.
    - Improved @url handling so that @url file:\\path\x.leo works properly.
    - Improved support for @lineending platform.
    - Leo honors outline/body pane ratio when opening .leo files.
    - Leo now ensures that newly-opened windows fit entirely on the screen.
    - Fixed a crasher when Undoing a Change All command when searching headlines.
  - Fixed other bugs resulting from the 4.1 reorg:
    - Fixed problem loading plugins on Linux.
    - Fixed crashers in the Extract Section and Extract commands.
    - Fixed a crasher when writing a file containing an undefined section.
    - Removed duplicate bindings in popup menus.
    - Made sure to show Leo's windows in wx gui plugin.

Beta 4:
  - Fixed several "reorg" bugs, some of which affected plugins.
  - Allow @directives and section references when executing scripts!
  - More than one section reference may now appear on the same line.
  - Use "utf-8" encoding for filenames under MacOS (Darwin)
  - Allow command or cmnd prefix for menu shortcuts under Darwin.
	  
Beta 3:
  - Completed the reorg, making many changes to the code base.
  - Fixed a LaTeX coloring bug

Beta 2:
  - Fixed a startup problem on Linux: the "mbcs" text encoding is not valid on Linux.

Beta 1:
  * Script-based find/change commands.
  - Hoist &amp; DeHoist commands for viewing parts of an outline.
  - Check Outline command finds user clone mistakes.
  * New configuration settings:
    - use_gnx specifies whether .leo files use integers as indices:
      use_gnx = 0 makes .leo files compatible with previous versions of Leo.
      use_gnx = 1 makes .leo files cvs-friendly
    - config_encoding specifies the encoding of leoConfig.txt.
  * Several significant code-level changes:
    - The 4.1 code base has been reorganized to support gui plugins.
    - An example wx_gui plugin is partly functional.
    - Created a flexible framework for creating &amp; running regression tests.
    - app.forceShutdown now works when called from plugins.</t>
<t tx="edream.110603190125.1">Leo 4.1 uses immutable gnx's (id:timestamp:n) by default to associate tnodes with vnodes in .leo files.  This makes Leo as cvs friendly as possible.  From now on .leo files will be checked in to cvs with the -ko (text/keywords off) option.</t>
<t tx="edream.110603190125.3">The file test.leo in the test directory contains real regression tests for syntax coloring.   Regression testing scripts create regression tests dynamically from data in Leo's outline.  Very cool, very easy, very general.  In particular, regression tests may use temporary nodes in test.leo rather than creating separate Tk windows for testing.</t>
<t tx="edream.110603190125.4">The 4.1 code base has been reorganized to support gui's other than tkinter.  Leo's src directory contains several new source files.

This reorg affects almost all plugins.  Considerably more work and testing will be done before 4.1 final.

The __wx_gui.py plugin is uses the newly reorganized code.  It is functional except for gui-dependent commands like Toggle-Split Direction.  WARNING: treat the this plugin with extreme caution until further notice.  The possibility exists that bugs in the code could cause body text to be cleared improperly when changing nodes.</t>
<t tx="edream.110603190234.1"></t>
<t tx="edream.110603190322.3">This involved fixing a bug in idle_body_key so that the oldText param is honored if present.</t>
<t tx="edream.110603190322.6">@nocolor

New in 4.1: Leo now supports scripts in Leo's Find/Change dialog.

Leo's find panel now contains the Script Search radio button and the Script
Change checkbox. When the Script Search radio button is selected Leo treats the
contents of the Search Text as a script to execute whenever any kind of Find
command is executed. Similarly, when the Script Change checkbox is selected Leo
treats the context of the Change Text as a script to execute whenever any kind
of Change command is executed. See below for just how this works.

Script-based find-change is extremely powerful. In effect, Leo's Find/Change
panel becomes a new platform for running scripts interactively. Leo now has all
the find/change capability of pattern matching languages like Snobol and Icon,
just by using the capabilities of the plain Python language. Moreover, Leo can
deliver these capabilities interactively or not depending which buttons you push
in Leo's Find/Change panel.

Script-based find/change frees the user from having to control script-based
searches interactively. Rather than forcing find/change scripts to implement
their own interactive controls, it is much easier to use what Leo already has.</t>
<t tx="edream.110603190322.8">Undoing Change All cleared the body pane or the headline pane.

The fix was simple: call setUndoParams instead of setUndoTypingParams in batchChange.</t>
<t tx="edream.110603190322.9"></t>
<t tx="edream.110603190322.10"></t>
<t tx="edream.110603190322.11">The node-only option wasn't working due to a bug in createFrame.

There still may be a problem with the interaction between Node-only,Change All and Undo.</t>
<t tx="edream.110603190322.13">The fix was to open files with 'rb' instead of 'r'.  This probably should be done in more places.</t>
<t tx="edream.110603190322.14">This command checks for unused tnodeLists and checks the topology of all clones.</t>
<t tx="edream.110603190322.15">The Hoist command redraws the screen so presently selected tree becomes the only visible part of the outline.  Leo prevents the you from moving nodes outside the hoisted outline.  The De-hoist command restores the outline.  Hoist commands may be nested.</t>
<t tx="edream.110603190404"></t>
<t tx="edream.110603192009"></t>
<t tx="edream.110603192009.1"></t>
<t tx="edream.111803060152"></t>
<t tx="edream.111803060152.1">Leo dedicates a Python dictionary called app.searchDict for communication
between Leo and the search and change scripts. The search and change scripts may
also use app.searchDict for communication between themselves. Leo sets
app.searchDict["type"] to "find", "change", "findAll" or "changeAll" to indicate
the kind of command being executed. Scripts may use all other entries in
app.searchDict as they please.

Leo executes the find script once when you press the Find button (or the Change
then Find button) in Leo's Find/Change dialog. Typically, the find script would
traversing the tree and highlight the found text or otherwise indicate to the
user that the find operation has succeeded. However, the script can do anything
it pleases.

Leo executes the the find script repeatedly when you press the Find All button.
Leo keeps executing the find script until app.searchDict["continue"] evaluates
to false. Initially there is no entry for app.searchDict["continue"], so the
find script must set app.searchDict["continue"] = true if it wants Leo to keep
executing it.

Leo executes the change script once when you press the Change button. Typically,
the change script would change the selected text. Usually the change script will
compute the new value of body text and call c.setBodyString(p,newText) to
make that change permanent. 

The change script also may handle undo, typically by calling
c.frame.onBodyChanged(v,"Change",oldText=oldText). Leo does not handle undo
automatically. Indeed, Leo makes no assumptions whatever about what the change
script really does.

Leo executes the the change script repeatedly when you press the Change All
button. Just as with the Find All command, Leo keeps executing the change script
until app.searchDict["continue"] evaluates to false.

Most find and change scripts will ignore settings in the Find Panel like "whole
word", "pattern match", and "reverse". However, these settings are available to
the scripts via ivars such as c.whole_word_flag, etc. if desired.</t>
<t tx="edream.111803060152.2">@nocolor

Some ideas for using scripts:
	
Either the find and change scripts may use Python's re module.  For
example, the find script could set app.searchDict["m"] to the match object
returned by re's match method.  The change script would then compute the
result, change the text and set the undo info as usual.

There is no reason to confine find/change scripts to operate on data only
within a Leo outline. These scripts could as easily traverse your file system
as the Leo outline. But notice: scripts could pull data from the file system
into the outline so that you can see the effects of changes as the scripts
operate. Again, this can all happen interactively if you like.</t>
<t tx="edream.111803060643"></t>
<t tx="edream.111803062437"></t>
<t tx="edream.112303173638">@color
@  New in version 4.1: On startup, Leo looks for two arguments of the form --script scriptFile.  If found, Leo enters batch mode.

In batch mode Leo does not show any windows.  Leo assumes the scriptFile contains a Python script and executes the contents of that file using Leo's Execute Script command.  By default, Leo sends all output to Leo's log pane to the console window.  Scripts in the scriptFile may disable or enable this output by calling app.log.disable() or app.log.enable()

Scripts in the scriptFile may execute any of Leo's commands except the Edit Body and Edit Headline commands.  Those commands require interaction with the user.

For example, the following batch script reads a Leo file and prints all the headlines in that file.
@c

import leoGlobals as g

path = r"c:\prog\leoCVS\leo\test\test.leo"

g.app.log.disable() # disable reading messages while opening the file
flag,newFrame = g.openWithFileName(path,None)
g.app.log.enable() # re-enable the log.

for p in newFrame.c.allNodes_iter():
	g.es(g.toEncodedString(p.headString(),"utf-8"))</t>
<t tx="edream.120403174147"></t>
<t tx="edream.120403174147.30">Another 4.1 reorg bug.</t>
<t tx="edream.120403174147.33">This was due to a missing activate event.</t>
<t tx="edream.120403174147.36">Continuation lines caused the import command to terminate functions, methods and classes prematurely.</t>
<t tx="edream.120403174147.56"></t>
<t tx="edream.120403174147.61">This was causing Leo not to load plugins properly on Linux.  The problem was that the imp module does not handle Unicode file names properly.</t>
<t tx="edream.120403174147.63">This was a reorg bug.</t>
<t tx="edream.120403174147.65">Another bug caused by the 4.1 reorg.</t>
<t tx="edream.120403174147.94">- Leo now properly enables and disables the Extract Section menu item.
- Leo no longer removes leading forward slashes in section names in headlines.
- Corrected the documentation for the Extract Section command.</t>
<t tx="edream.120403174147.102">Another 4.1 reorg bug.</t>
<t tx="edream.120403174147.105">This bug has been around for a long time.</t>
<t tx="edream.120403174147.109">The new code attempts to use bitmap files only on Windows.</t>
<t tx="edream.120403174147.112">Leo makes sure that opened files or newly-created outlines fit entirely on the screen.  The Cascade commands leaves the sizes of windows unchanged: it merely ensures that the top left corner of a window is visible on the screen.</t>
<t tx="edream.120403174147.119"></t>
<t tx="edream.120403174147.128">@ A problem: the new window gets put behind the old.  This is probably because Tk thinks that the mouse-down event should select then new window...</t>
<t tx="edream.120403174241"></t>
<t tx="edream.120403180443"></t>
<t tx="edream.120403180443.1"></t>
<t tx="edream.120703073611">Plugins may create (or add to) v.tempAttributes (for vnodes) or t.tempAttributes (for tnodes).  These will work just like the corresponding unknownAttributes dicts except that Leo will _not_ read or write these dictionaries when reading or writing files.  Note: nothing needs to change in Leo to support this convention.</t>
<t tx="edream.120703073611.1">@nocolor

We wish to avoid the possibility that two plugins might unwittingly choose the same name for attributes in the unknownAttributes or tempAttributes dictionaries.  The following convention eliminates that possibility.

Each plugin should create its own dictionary _inside_ any tempAttributes or unknownAttributes dictionaries that it intends to create or modify.  Something like this:

@color

# Create the tempAttributes dict for this vnode.
if not v.hasattr("tempAttributes"):
	v.tempAttributes = {}

# Create a subdictionary for the private use of my plugin.
d = v.tempAttributes.get("myPluginName")
if d is None:
	v.tempAttributes["myPluginName"] = d = {}

@nocolor

Now the plugin can set and get fields in d.  Similar code would be used for the t.tempAttributes, v.unknownAttributes and t.unknownAttributes dictionaries.</t>
<t tx="edream.121403160546">Leo 4.1 Release Candidate 3              December 19, 2003

This release fixes a serious bug in the logic that reads old-style derived files.

There are no known bugs in this version of Leo.

The highlights of this release:

- Leo runs in batch mode when invoked with --script aScriptFile.py
- Leo supports Unicode characters (e.g. Chinese) in path and file names.
- @directives and section references are now valid when executing scripts.
- @ignored and orphan nodes now valid in @file-nosent trees.
- Script-based find/change commands.
- Check Outline command.
- Hoist &amp; DeHoist commands.
- A new gui-agnostic architecture: useful for batch mode and unit tests.
- Several new configuration settings.
- Many new unit tests.
- A host of bug fixes.</t>
<t tx="edream.121403161017">See previous release notes for more details:

- Fixed several minor problems with the Extract Section and Import commands.
- Fixed problem that prevent the Find panel from working on the Mac.
- Improved @url handling so that @url file:\\path\x.leo works properly.
- Improved support for @lineending platform.
- Leo honors outline/body pane ratio when opening .leo files.
- Leo now ensures that newly-opened windows fit entirely on the screen.
- Fixed a crasher when Undoing a Change All command when searching headlines.
- Fixed other bugs resulting from the 4.1 reorg:
- Fixed problem loading plugins on Linux.
- Fixed crashers in the Extract Section and Extract commands.
- Fixed a crasher when writing a file containing an undefined section.
- Removed duplicate bindings in popup menus.
- Made sure to show Leo's windows in wx gui plugin.
- More than one section reference may now appear on the same line.
- Use "utf-8" encoding for filenames under MacOS (Darwin)
- Allow command or cmnd prefix for menu shortcuts under Darwin.
- Fixed a LaTeX coloring bug
</t>
<t tx="edream.121403161017.1">- The 4.1 code base has been reorganized to support gui plugins.
- Created a flexible framework for creating &amp; running regression tests.
- app.forceShutdown now works when called from plugins.
- Created app.unitTestDict for communication between tests and between tests and code.

- An example wx_gui plugin is partly functional.

	Warning: Use the __wx_gui.py plugin with extreme caution until further notice:
	bugs in this plugin could cause body text to be cleared improperly when changing nodes.
</t>
<t tx="edream.121403161017.2">- use_gnx specifies whether .leo files use integers as indices:
  
	use_gnx = 0 makes .leo files compatible with previous versions of Leo.
	use_gnx = 1 makes .leo files cvs-friendly

- config_encoding specifies the encoding of leoConfig.txt.</t>
<t tx="edream.121403161340">- Import Derived File command now uses a file dialog.

	This is much more natural than using @file nodes.

- Leo now loads all plugins listed in pluginsManager.text.

	It is no longer necessary to edit plugin files to enable or disable plugins.</t>
<t tx="edream.121403162622">New in 4.1: The plugins test suite creates a new convention: if a plugin has a
function at the outer (module) level called unitTest, Leo will call that
function when doing unit testing for plugins. So it would be good if writers of
plugins would create such a unitTest function. The unitTest function should run
some tests. All unitTest needs to do to indicate failure is throw an exception
or cause an assert to fail. Leo's plugins test suite takes care of the rest.</t>
<t tx="edream.121403165221">- Corrected counts when replacing tabs/blanks.
- Don't write tnodeList when executing scripts.
- Fixed long-standing clone-drag bug.
- Fixed inconsistency between how 4.x and 3.x handle @others.
  The code now works as it did in all 3.x versions, namely
  @others does not terminate doc parts.
- Leo now properly sets clone marks when when cutting and pasting nodes.
- Only double-quotes delimit strings in html files.
  This bug prevented Leo from untangling some valid html/xml files.
- Leo now puts class docstrings in class nodes when importing .py files.
- Fixed several reorg bugs.</t>
<t tx="ekr.20040131040356">Leo 4.1 Release Candidate 4              February 3, 2004

This release fixes numerous bugs reported since 4.1 rc3 and makes several other
minor improvements, including several nifty new plugins.

The highlights of Leo 4.1:

- Leo runs in batch mode when invoked with --script aScriptFile.py
- Leo supports Unicode characters (e.g. Chinese) in path and file names.
- @directives and section references are now valid when executing scripts.
- @ignored and orphan nodes now valid in @file-nosent trees.
- Script-based find/change commands.
- Check Outline command.
- Hoist &amp; DeHoist commands.
- A new gui-agnostic architecture: useful for batch mode and unit tests.
- Several new configuration settings.
- Many new unit tests.
- Excellent new plugins.
- A host of bug fixes.</t>
<t tx="ekr.20040131040356.1"></t>
<t tx="ekr.20040131040356.2">See previous release notes for more details:

4.1 rc3:

- Corrected counts when replacing tabs/blanks.
- Don't write tnodeList when executing scripts.
- Fixed long-standing clone-drag bug.
- Fixed inconsistency between how 4.x and 3.x handle @others.
  The code now works as it did in all 3.x versions, namely
  @others does not terminate doc parts.
- Leo now properly sets clone marks when when cutting and pasting nodes.
- Only double-quotes delimit strings in html files.
  This bug prevented Leo from untangling some valid html/xml files.
- Leo now puts class docstrings in class nodes when importing .py files.
- Fixed several reorg bugs.

4.1 rc2, rc1, betas, alphas:

- Fixed several minor problems with the Extract Section and Import commands.
- Fixed problem that prevent the Find panel from working on the Mac.
- Improved @url handling so that @url file:\\path\x.leo works properly.
- Improved support for @lineending platform.
- Leo honors outline/body pane ratio when opening .leo files.
- Leo now ensures that newly-opened windows fit entirely on the screen.
- Fixed a crasher when Undoing a Change All command when searching headlines.
- Fixed other bugs resulting from the 4.1 reorg:
- Fixed problem loading plugins on Linux.
- Fixed crashers in the Extract Section and Extract commands.
- Fixed a crasher when writing a file containing an undefined section.
- Removed duplicate bindings in popup menus.
- Made sure to show Leo's windows in wx gui plugin.
- More than one section reference may now appear on the same line.
- Use "utf-8" encoding for filenames under MacOS (Darwin)
- Allow command or cmnd prefix for menu shortcuts under Darwin.
- Fixed a LaTeX coloring bug
</t>
<t tx="ekr.20040131040356.3">- The 4.1 code base has been reorganized to support gui plugins.
- Created a flexible framework for creating &amp; running regression tests.
- app.forceShutdown now works when called from plugins.
- Created app.unitTestDict for communication between tests and between tests and code.

- An example wx_gui plugin is partly functional.

	Warning: Use the __wx_gui.py plugin with extreme caution until further notice:
	bugs in this plugin could cause body text to be cleared improperly when changing nodes.
</t>
<t tx="ekr.20040131040356.4">- use_gnx specifies whether .leo files use integers as indices:
  
	use_gnx = 0 makes .leo files compatible with previous versions of Leo.
	use_gnx = 1 makes .leo files cvs-friendly

- config_encoding specifies the encoding of leoConfig.txt.</t>
<t tx="ekr.20040131040356.5">- Import Derived File command now uses a file dialog.

	This is much more natural than using @file nodes.

- Leo now loads all plugins listed in pluginsManager.text.

	It is no longer necessary to edit plugin files to enable or disable plugins.</t>
<t tx="ekr.20040131040544.2"></t>
<t tx="ekr.20040131040544.5"></t>
<t tx="ekr.20040131040544.10">This allows plugins to draw the status area in the icon area.</t>
<t tx="ekr.20040131040544.18">The old code was concatenating strings; the new code uses list.append.</t>
<t tx="ekr.20040131040544.21">- ESC closes the Find panel.

- Hitting the Return key is now equivalent to hitting the Find button.</t>
<t tx="ekr.20040131040544.32"></t>
<t tx="ekr.20040131040544.55">Leo now reports the parent of the orphan node.</t>
<t tx="ekr.20040131040544.73">This bug happened when a move up command would cause a node to become the sibling of (a clone of) itself.  In such cases, Leo simply selects the other cloned copy of the moved node.</t>
<t tx="ekr.20040131040544.81">The bug was causing Leo not to remember the comment delimiters in the @+leo sentinel.  As a result, Leo was recognizing no sentinels and the command complained about missing @-leo sentinels.</t>
<t tx="ekr.20040131040544.146">- Leo now does a better job of checking and reporting read-only violations.

- Leo now clears the file-dirty mark only if the file was successfully saved.

</t>
<t tx="ekr.20040131040544.169"></t>
<t tx="ekr.20040131040544.178">Leo sets only ancestor @file nodes dirty (not nodes themselves) when altering outline structure, i.e., when moving, inserting, deleting, cloning and sorting nodes.</t>
<t tx="ekr.20040131040544.222">That is, when preprocessing the script (expanding section references, etc.) Leo now ensures that child nodes effectively end in a newline.  This prevents unintended concatenation of lines.</t>
<t tx="ekr.20040131040544.227">A contained a space before a tab in the leading whitespace of the line.</t>
<t tx="ekr.20040131040544.228">- These commands did not properly count the number of changed nodes.
- These commands now mark only changed nodes as dirty.</t>
<t tx="ekr.20040131040544.258"></t>
<t tx="ekr.20040131040754">Fixed crashers in:

- Insert Headline Time/Date commands.
- Change headline command.
- Write Dirty/Missing @file Nodes commands.
- Batch mode.</t>
<t tx="ekr.20040131041015"></t>
<t tx="ekr.20040131044136">- Fixed a bug that caused cut and paste operations in headlines to revert when those commands were chosen from the Edit menu.

- Extended control-v bug fix to "darwin","freebsd4","freebsd5"

- Cut and paste are now always enabled when not editing the body pane.  This isn't perfect, and is an improvement.</t>
<t tx="ekr.20040131044727">1. Fixed a bug that caused improper indentation of sections.

The bug happened in some cases when a section reference occurred following non-whitespace.

2. Leo ensures that leading whitespace is not added when writing empty lines.

This might fix the "Zope Sprint" bug: "blank" lines in the expansion of @others got leading whitespace.</t>
<t tx="ekr.20040131100557">Previously, if you hoist a node with no children and then insert a node (CTRL-I)
then the child is created as a sibling of the hoisted node and consequently is
not displayed.

Leo now creates the new node as the first child of the hoisted node. 

Also, Leo disables the Clone command when the presently selected node is the root of a hoist.</t>
<t tx="ekr.20040201061329">This creates a status area at the bottom of the Leo Window.  Plugins may write to this area using the status area convenience routines in leoTkinterFrame.py.</t>
<t tx="ekr.20040201113232">@nocolor

The Scripts node in LeoPy.leo contains a script called initScriptFind.  This script makes it easy to set up script based searches as follows:

1. Put the following code in the root of a tree that will contain your script search:

@color
# Initialize Leo's find panel using the named children of this node.
from leoGlobals import *
initScriptFind("Find script","Change script") # Second argument is optional.
# Start searching at the top.
top().selectVnode(c.rootVnode())
@nocolor

2. Put the search script in a child node called "Find script" (no quotes).

3. (Optional) Put the change script in a child node called "Change script"

4.  Execute the code above.  Leo does the following:

- Puts the body of the "Find script" into the find text of Leo's Find/Change dialog.
- Puts the body of the "Change script" into the change text of Leo's Find/Change dialog.
- Selects the Script Find radio button.
- Selects the Script Change checkbox if the change script exists.
- Selects the root of the entire outline.

Presto!  Leo is ready for a script search.</t>
<t tx="ekr.20040201114855"></t>
<t tx="ekr.20040201114855.13">Adds a quick search to the toolbar in Leo.

A search box which behaves like a web site search is added, along with a "GO"
button to do quick searches right from the main Leo window. All the current
search options are retained except that "search body text" is explicitly set -
mainly because this is by far the most common use case.

Pressing &lt;CR&gt; while editing the text automatically does a search. Repeated
searches can be done by clicking the "GO" button.

The combo box also stores a list of previous searches, which can be selected to
quickly repeat a search. When activating a previous search the original search
mode is used.

Still to do:

- incremental search
- reverse search
- persist recent searches across Leo sessions
- use INI file to set options for list size, etc.</t>
<t tx="ekr.20040201114855.29">Adds a node navigator to the toolbar. The navigator allows quick access to
marked nodes. You can either go to the marked node or hoist the marked node.</t>
<t tx="ekr.20040201114855.36">Adds row/column indicators to the toolbar at the top of Leo Windows.</t>
<t tx="ekr.20040201114855.42">A minimal http plugin for LEO, based on AsyncHttpServer.py.

Use this plugin is as follows:

1. Start Leo with the plugin enabled. You will see a purple message that says
something like: "http serving enabled on port 8080, version 0.9"

2. Start a web browser, and enter the following url: http://localhost:8080/
You will see a a "top" level page containing one link for every open .leo file.
Start clicking :-)

You can use the browser's refresh button to update the top-level view in the
browser after you have opened or closed files.</t>
<t tx="ekr.20040201114855.91">Automatically add nodes for common tasks. This can be used to generate boiler
plate code to quickly build an outline.</t>
<t tx="ekr.20040201114855.105"></t>
<t tx="ekr.20040201114855.106"></t>
<t tx="ekr.20040201114855.107">This bug happened when executing the initScriptFind script.  This bug could cause Leo not to be able to save files.</t>
<t tx="ekr.20040201120903">Adds a status line to the bottom of Leo windows.</t>
<t tx="ekr.20040203084228">The Change All command was looping when the find pattern was '\n'.</t>
<t tx="ekr.20040216151748">Leo 4.1 Final              February 20, 2004

Leo 4.1 Final is the culmination of four months of work. No significant bugs
have been reported since 4.1 rc4. Several people have contributed nifty plugins
recently. See leoPlugins.leo for full details.

The highlights of Leo 4.1:

- Leo runs in batch mode when invoked with --script aScriptFile.py
- Leo supports Unicode characters (e.g. Chinese) in path and file names.
- @directives and section references are now valid when executing scripts.
- @ignored and orphan nodes now valid in @file-nosent trees.
- Script-based find/change commands.
- Check Outline command.
- Hoist &amp; DeHoist commands.
- A new gui-agnostic architecture: useful for batch mode and unit tests.
- Several new configuration settings.
- Many new unit tests.
- Excellent new plugins.
- A host of bug fixes.</t>
<t tx="ekr.20040216152948"></t>
<t tx="ekr.20040216153725">Changed Undo/Redo messages:

- Insert Outline to Insert Node.
- Delete Outline to Delete Node.
- Clone to Clone Node.

This is a real code change: it affects the undo/redo logic.</t>
<t tx="ekr.20040217075627">Clone bits could be improperly set in some cases.  This bug would not have caused serious long-term problems.

Steps to reproduce:

1. Create a parent node (named 'cloned').
2. Create two children nodes (one named 'dummy' and another named 'bottom') under the parent node 'cloned'.
3. Move the 'bottom' node below the 'dummy' node.
4. Clone node 'cloned'.
5. Copy node 'dummy'.
6. Paste node 'dummy' in between 'dummy' and 'bottom'.
7. After pasting you'll see that 'bottom' is now marked as a cloned node.</t>
<t tx="ekr.20040217085036">See leoPlugins.leo for full details.</t>
<t tx="ekr.20040217085036.1">Here is the bug report I submitted to Python:

The documentation for encoding lines at

C:\Python23\Doc\Python-Docs-2.3.1\whatsnew\section-encodings.html

states:

"Encodings are declared by including a specially formatted comment in the
first or second line of the source file."

In fact, contrary to the implication, the Python 2.3 parser does not look
for lines of the form:

# -*- coding: &lt;encoding&gt; -*-

For example, Python improperly scans the following line for an encoding

#@+leo-ver=4-encoding=iso-8859-1.

and reports that iso-8859-1. (note trailing dot) is an invalid encoding!

The workaround for my app is to precede this line with the following line:

# -*- coding: iso-8859-1 -*-

This makes Python 2.3 happy.

To make myself perfectly clear: Python has absolutely no right to complain
about comment lines that do not have the form:

# -*- coding: &lt;encoding&gt; -*-</t>
<t tx="ekr.20040705111716"></t>
<t tx="ekr.20040705111716.1">Leo will write only t.unknownAttributes to the .leo file when writing the &lt;v&gt; element corresponding to the root of an @thin tree.  Leo will do this by writing a new xml attribute, say descendentTnodeUnknownAttributes, in &lt;v&gt; element.

The reason that Leo will only write t.unknownAttributes and not v.unknownAttributes is that only tnodes have gnx's in thin derived files.  In effect, vnodes are anonymous.  We could attempt to get around this by identifying vnodes by their corresponding tnodes, but that's not a general solution and it is, in effect, equivalent to writing only t.unknownAttributes.  This being so, it seems pointless to "pretend" to be writing v.unknownAttributes.

The effect of this is to make all vnodes identical, as far as using unknownAttributes is concerned.  As I've stated in the past, this won't do if, for example, a plugin is trying create an arbitrary directed graph between vnodes.  In that case, the plugin should confine itself to @file trees, or just vnodes in .leo files, for that matter.

7/1/04:

- Leo now writes "marks" and "expanded" attributes in the root &lt;v&gt; element for @thin trees.

- VERY IMPORTANT.  Leo now writes entire tree of @ignored @thin nodes.  This fixes a major bug.</t>
<t tx="ekr.20040705111716.45">Leo marks as dirty all @file nodes when they become "newly unignored".</t>
<t tx="ekr.20040705111716.126"></t>
<t tx="ekr.20040705112148"></t>
<t tx="ekr.20040705150130">Leo now generates no warnings with all significant tests enabled.  Some tests have been disabled in bases classes, and in a few cases pychecker gives erroneous warnings that have been suppressed directly in the source code using the __pychecker__ = arg syntax.</t>
<t tx="ekr.20040713110718">Leo 4.2 beta 3           August 10, 2004

This version of Leo is feature complete.  Leo's core code has been stable for several months.

To do: most plugins work with the new code base, but other plugins need some more work.

The highlights of Leo 4.2:

- @thin trees make Leo much more friendly to cvs. Files derived from @thin can
be committed to cvs and updated from cvs without having to commit or update the
corresponding .leo file. There is no longer any need to keep .leo files and
derived files in synch.

- Leo's data structures have been reorganized. As a result, all outline
operations are much faster. To support this organization, scripts that traverse
Leo's data structures must now use a positions rather than vnodes. Old scripts
that appear to use vnodes will still work because methods like c.currentVnode
that appear to return vnodes actually return positions.

- A new mod_scripting plugin is a big advance in scripting and testing.
test.leo now uses @test and @script nodes to define unit tests without
explicitly creating subclasses of unittest.TestCase. Converting scripts to unit
tests now takes a few seconds!

- A much faster and more robust spell checker plugin. (requires Python 2.3)

- Leo is now much more friendly to using spaces instead of tabs.

- The Execute Script command reports erroneous lines more clearly.

- The Perfect Import feature guarantee that Leo imports file exactly.</t>
<t tx="ekr.20040804164600.16">Leo now vetoes the shutdown logic if saving a dirty file fails.

Leo prints in red the warning about not being able save the read-only file. The
user can use the Save To command to save the file. The Save To command does not
clear the file's dirty bit, so Leo will prompt again to save the file. The user
will have to ignore this prompt in order to exit. This is correct: the
_original_ file has not been saved.</t>
<t tx="ekr.20040804164600.36">- g.getScript implicitly assumed that p == c.currentPosition.
  I removed that assumption.

- The scriptButton callback in the scripting.py plugin no longer calls c.executeScript.
  It's simpler and easier to call exec directly.

- Improved c.checkOutline:
    - Added full keyword arg.
    - Print more if verbose is on.</t>
<t tx="ekr.20040804164600.56"></t>
<t tx="ekr.20040804164600.98"></t>
<t tx="ekr.20040804164600.102">Spurious entries in a tnodeList for @thin trees wiped out all the headlines in the @thin tree.</t>
<t tx="ekr.20040804164600.265"></t>
<t tx="ekr.20040804164600.275"># The new code only writes tnodes for the current tree when pasting to the clipboard.</t>
<t tx="ekr.20040804164600.377">There was a big performance bug in the nodenavigator plugin.</t>
<t tx="ekr.20040804164600.394">@nocolor

As a result, the minimal .leo file is:

@color
@language html

&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;leo_file&gt;
&lt;leo_header/&gt;
&lt;globals/&gt;
&lt;preferences/&gt;
&lt;find_panel_settings/&gt;
&lt;vnodes/&gt;
&lt;tnodes/&gt;
&lt;/leo_file&gt;

@nocolor

The empty_leo_file plugin now uses this code. The minimal .leo file that Leo
might actually write is more like this:

@color

&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;leo_file&gt;
&lt;leo_header/&gt;
&lt;globals/&gt;
&lt;preferences/&gt;
&lt;find_panel_settings&gt;
    &lt;find_string/&gt;
    &lt;change_string/&gt;
&lt;/find_panel_settings&gt;
&lt;vnodes/&gt;
&lt;tnodes/&gt;
&lt;/leo_file&gt;</t>
<t tx="ekr.20040804164600.406"></t>
<t tx="ekr.20040804164600.419"></t>
<t tx="ekr.20040804164600.421">This is required to make @thin work properly.</t>
<t tx="ekr.20040804164600.424">This makes the command more useful.</t>
<t tx="ekr.20040804164600.470"></t>
<t tx="ekr.20040804164600.471">A major change: putVnode doesn't put tnodeLists for @thin nodes.

Instead it issues an informational message and deletes the tnodeList.</t>
<t tx="ekr.20040804164600.515">Leo used to allocate more positions than necessary.  This unnecessarily stressed the garbage collector.</t>
<t tx="ekr.20040804165258.1"></t>
<t tx="ekr.20040804165258.2"></t>
<t tx="ekr.20040804165258.3">Leo now allows you to select multiple files in the dialogs for all Import
commands. This fixes a major annoyance. However, you must be running Python 2.3
or above to get this feature.
</t>
<t tx="ekr.20040804165258.4">Added the Check submenu of the Outline menu. This contains the Check Outline and
Dump Outline commands, as well as four new commands:

The Check All Python Code and Check Python Code commands report any syntax errors or tabnanny errors.  These commands mark erroneous nodes.  These commands work on the selected Node and its descendants.  These commands ignore any nodes for which a) @ignore is in effect or b) @language python is in not effect.

The Check Python Code and Pretty Print Python Code commands replace nodes with their pretty-printed alternative.  No doubt everyone will have their own favorite style.  You could implement alternate pretty printers in a plugin merely by overriding the following methods of class prettyPrinter in leoCommands.py:
    
---- putOperator:      puts whitespace around operators.
---- putNormalToken:   puts whitespace around everything else.</t>
<t tx="ekr.20040804170531"></t>
<t tx="ekr.20040804170657">Leo now reuses all widgets used to draw the outline pane.  This improves performance and ends leaks of bindings and widgets.</t>
<t tx="ekr.20040804170846">@thin bad-directory caused excessive and confusing tracebacks.</t>
<t tx="ekr.20040804171818"></t>
<t tx="ekr.20040804172113"></t>
<t tx="ekr.20040804172113.1"></t>
<t tx="ekr.20040914103359">Leo 4.2 release candidate 1        September 14, 2004

This version fixes a number of minor bugs reported since the last release. See
the children of this node for details.

The highlights of Leo 4.2:

- @thin trees make Leo much more friendly to cvs. Files derived from @thin can
be committed to cvs and updated from cvs without having to commit or update the
corresponding .leo file. There is no longer any need to keep .leo files and
derived files in synch.

- Leo's data structures have been reorganized. As a result, all outline
operations are much faster. To support this organization, scripts that traverse
Leo's data structures must now use a positions rather than vnodes. Old scripts
that appear to use vnodes will still work because methods like c.currentVnode
that appear to return vnodes actually return positions.

- A new mod_scripting plugin is a big advance in scripting and testing.
test.leo now uses @test and @script nodes to define unit tests without
explicitly creating subclasses of unittest.TestCase. Converting scripts to unit
tests now takes a few seconds!

- A much faster and more robust spell checker plugin. (requires Python 2.3)

- Leo is now much more friendly to using spaces instead of tabs.

- The Execute Script command reports erroneous lines more clearly.

- The Perfect Import feature guarantee that Leo imports file exactly.</t>
<t tx="ekr.20040914103359.2"></t>
<t tx="ekr.20040914103359.4"></t>
<t tx="ekr.20040914103359.7">With TclTkAqua on the Mac (but *not* with tcltk installed via Fink), the tab
problem doesn't exist there), the tab, return, and backspace keys did not generate
ASCII codes, i.e. event.char is an empty string. So when I press the tab key,
Tk inserts a tab character and Leo isn't even aware of it.</t>
<t tx="ekr.20040914103359.12">If only one file was specified Leo gave an error for every character of the file name!
</t>
<t tx="ekr.20040914103359.15"></t>
<t tx="ekr.20040914103359.19"></t>
<t tx="ekr.20040914103359.20">@killcolor

From Dan Winkler:

On a couple of occasions, I tried to paste in a long @url node and got 
this message:

	Truncating headline to 250 characters

I wonder if the 250 character limit on headline length should be 
rethought in light of the @url directive and long web addresses.</t>
<t tx="ekr.20040914103359.28"></t>
<t tx="ekr.20040914103359.31"></t>
<t tx="ekr.20040914103359.37"></t>
<t tx="ekr.20040914103359.47">There were too many problems with this feature.  In the future Leo will have a Check Import command.</t>
<t tx="ekr.20040914103359.110"></t>
<t tx="ekr.20040914103359.127">Leo wasn't always traversing the outline correctly when looking for @root nodes.</t>
<t tx="ekr.20040914103359.129">http://sourceforge.net/forum/message.php?msg_id=2742238
By: hinsen

The shortcut definitions in Leo are quite inconvenient on the Mac, as those
using the Alt key don't work. Alt is used for entry of additional characters.
On the other hand, ctrl is available for shortcuts but not used in Leo, since
the ctrl-based shortcuts are shifted to the command key (following standard
Mac practice).

The patch at the end of this message simply shifts all Alt-shortcuts to Ctrl
on the Mac.

That leaves one minor clash: Command-` is used for CloneNode in Leo, although
it canonical MacOS function (switching between the windows of an application)
would be very useful in Leo as well. Removing the CloneNode binding is easy
enough, but it seems that I must implement a window switching function myself.
Not today :-)

Konrad.
</t>
<t tx="ekr.20040914103359.137"></t>
<t tx="ekr.20040914103743"></t>
<t tx="ekr.20040914103743.1"></t>
<t tx="ekr.20040922074200">Leo 4.2 Final       September 20, 2004

The highlights of Leo 4.2:

- @thin trees make Leo much more friendly to cvs. Files derived from @thin can
be committed to cvs and updated from cvs without having to commit or update the
corresponding .leo file. There is no longer any need to keep .leo files and
derived files in synch.

- Leo's data structures have been reorganized. As a result, all outline
operations are much faster. To support this organization, scripts that traverse
Leo's data structures must now use a positions rather than vnodes. Old scripts
that appear to use vnodes will still work because methods like c.currentVnode
that appear to return vnodes actually return positions.

- A new mod_scripting plugin is a big advance in scripting and testing.
test.leo now uses @test and @script nodes to define unit tests without
explicitly creating subclasses of unittest.TestCase. Converting scripts to unit
tests now takes a few seconds!

- A much faster and more robust spell checker plugin. (requires Python 2.3)

- Leo is now much more friendly to using spaces instead of tabs.

- The Execute Script command reports erroneous lines more clearly.</t>
<t tx="ekr.20041226081019">c.spellCommands.openSpellTab()</t>
<t tx="ekr.20050122084954">Leo stores options in @settings trees, that is, parts of Leo outlines whose root node has the headline @settings.  When opening a .leo file, Leo looks for @settings trees in the following places:

- The file called leoSettings.leo in the leo/config directory.
- The file called leoSettings.leo in the users home directory.
- The file being loaded.

Settings that later in the above list override settings found earlier. For example, any setting specified in an @settings tree in the file being loaded overrides any setting seen in any leoSettings.leo file.

The Settings command temporarily replaces the outline pane with an outline showing all the @settings trees in effect. The Settings command also replaces the body pane with a "settings dialog" pane. This settings dialog pane
allows you to change the settings selected in the outline pane using standard gui widgets.

The format of nodes in @settings trees are as follows:

1. "Simple settings nodes" have headlines of the form:

@&lt;type&gt; name = val

set the value of name to val, with the indicated type.

&lt;type&gt; may be one of the following, with valid values shown:

&lt;type&gt;          Valid values
-----           ------------
\@bool           True, False, 0, 1
\@color          A Tk color name or value, such as 'red' or 'xf2fddff' (without the quotes)

For a list of Tk color specifiers see:

- http://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm
- http://www.tcl.tk/man/tcl8.4/TkLib/GetColor.htm

\@directory      A path to a directory
\@float          A floating point number of the form nn.ff.
\@int            An integer
\@ints[list]     An integer (must be one of the ints in the list).
                 Example: @ints meaningOfLife[0,42,666]=42
\@path           A path to a directory or file
\@ratio          A floating point number between 0.0 and 1.0, inclusive.
\@string         A string
\@strings[list]  A string (must be one of the strings in the list).
                 Example: @strings tk_relief['flat','groove','raised']='groove'

2. "Complex settings nodes" have headlines of the form:

\@&lt;type&gt; description

The actual settings are specified in the body text.  At present, there are two such kinds of complex settings nodes:

- @font

The body text contains a list of settings for a font.  For example:

body_text_font_family = Courier New
body_text_font_size = None
body_text_font_slant = None
body_text_font_weight = None

- @recentFiles

The body text contains a list of paths of recently opened files, one path per line.

Warning: The following features of @recentfiles nodes are confusing and probably
will be changed:

- Leo does not save recent file information unless the open .leo file has an
@settings tree and an @recentfiles node within the @settings tree. That is, Leo
does not save recent files information in leoSettings.leo files.

- Changing the @rencentfiles node doesn't mark the Leo file as dirty, so if you
don't save the .leo file the recent files information will not be updated.

3. "Page nodes" have headlines of the form @page &lt;description&gt;

Such nodes have the effect of gathering all descendant settings nodes into a single settings page.

4.  All other nodes are "Organizer" nodes.  Such nodes have no effect on the settings shown in the dialog.  You may use them as you please to organize settings.

Notes:

A.  At present, you can not change @settings trees while executing the Settings command.  You can, however, change any @settings tree normally when not executing the Settings command.

B. Other kinds of settings nodes are planned for future releases.</t>
<t tx="ekr.20050122090311">Leo 4.3 alpha 1                 January 24, 2005

Leo 4.3 is the culmination of more than four months of work. 

The defining features of Leo 4.3:

1. Leo now stores options in @settings trees, that is, outlines whose headline
is '@settings'. When opening a .leo file, Leo looks for @settings trees not only
in the outline being opened but also in various leoSettings.leo files.

The key design goal of @settings trees was that Leo's user options must be
infinitely flexible. That goal has been accomplished. Indeed, users can create
arbitrarily complex user options with @settings trees. Leo settings outlines
are, in fact, infinitely more flexible and powerful than any scheme based on
flat text.  Readers of Python's configParser shootout take note!

2. The Settings command temporarily replaces the outline pane with an outline
showing all the @settings trees in effect. The Settings command also replaces
the body pane with a "settings pane". This settings pane allows you to change
the settings selected in the outline pane using standard gui widgets. The
settings pane is dynamically created from nodes in the settings tree; it is as
extensible as the @settings tree itself.

3. Leo's read/write code in leoAtFile.py has been rewritten to support user-
defined tangling and untangling.  This is a major cleanup of Leo's core.

4. Leo now boasts a wonderful new Plugins Manager plugin. This plugin enables
and disables plugins automatically. You never have to mess with
pluginsManager.txt again! This plugin also tells you everything you need to know
about each plugin. Finally, this plugin also lets you download plugins from
Leo's cvs site! Many thanks to Paul Patterson for this excellent work.

5. You can install third-party extensions in Leo's extensions directory. Leo
will attempt to import such extensions from the extensions directory if normal
imports fail.</t>
<t tx="ekr.20050122091036">The essential features of @settings trees and the settings dialog appear to be stable.  However, many improvements can be imagined, including the following:

- Allow searching for nodes while in the settings dialog.

- Allow adding, deleting, rearranging nodes while in the settings dialog.

- Allow adding, deleting, rearranging recent files while in the settings dialog.

These will be added as time permits and people request.</t>
<t tx="ekr.20050123092834.1"></t>
<t tx="ekr.20050123092834.2"></t>
<t tx="ekr.20050123092834.6">The Open With logic in createOpenWithMenuFromTable for the 'spawnv' case  now actually calls os.spawnv (rather than spawnl) and it allows a variable length list of parameters.</t>
<t tx="ekr.20050123092834.19">The old code wasn't handling single file selections properly.  The new code works around an apparent bug in Tk.askopenfilename.</t>
<t tx="ekr.20050123092834.27">The new code forbids Paste Node As Clone if the paste would result in a node being a clone of itself.</t>
<t tx="ekr.20050123092834.42">The '@' sign is an operator in Python 2.4, not an error token.</t>
<t tx="ekr.20050123092834.71">What I did:
    
- Created a new top-level method: scanHeaderForThin.

This sets self.encoding temporarily. The actual value of self.encoding does not
really matter: no errors will be given by readLine and its helpers even if there
are unicode encoding errors.

- We must _not_ set self.encoding in scanHeader: that would interfere with
normal initialization.</t>
<t tx="ekr.20050123092834.81">- Restored non Pmw code in resizePanesToRatio.  This code got deleted by mistake.  The Equal Sized Panes works again.

- Added many do-nothing methods to nullMenu class.

This should prevent the startup logic from messing with shortcuts in any way.  It's also the right thing to do.

- Added an entry for EqualSizedPanes to leoSettings.leo.  This overrides the default (Ctrl-E) and thereby prevents the default from overriding the entry for ExecuteScript!

- Re-enabled code in createMenuEntries that warns when shortcuts have been redefined.  Not sure if this is a wise idea, or indeed if it actually does anything :-)

I am tempted to remove all the default entries entirely.  This would simplify error reporting, but then Leo would hardly work at all if leoSettings.leo were not present.</t>
<t tx="ekr.20050123092834.159"></t>
<t tx="ekr.20050123092834.160">p.moveToParent now just returns if p is a null position.</t>
<t tx="ekr.20050123092834.163"># Leo looped after this assert failed.</t>
<t tx="ekr.20050123092834.165"></t>
<t tx="ekr.20050123092834.166">he readDirective method was changing the comment delimiters as the result of
seeing the sentinels corresponding to @language or @comment directives. But in
general this makes no sense! Comment delimiters should be set once and for all
in the @+leo sentinel: there is no compiler in the world that tolerates mixed
comment delimiters.

BTW, the way to set javascript "inner" comments is to use @delims, not @comment.
N.B. The @language and @comment delimiters _will_ have an effect, and that
effect is in the _write_ logic, not the read logic. The effect is to set the
comment delims in the @+leo sentinel.

The quick fix is to comment out code in readDirective.</t>
<t tx="ekr.20050123092834.173"></t>
<t tx="ekr.20050123092834.176">The old code did not honor the @lineending directive if the two files would otherwise be identical.

What I did:

- Added self.explicitLineEnding to remember whether an explicit @lineending directive is in effect.

- Make sure the user knows why an otherwise identical file was written.

- Changed name of compareFilesIgnoringNewlines to compareFiles.

- Added ignoreLineEndings arg to compareFiles.</t>
<t tx="ekr.20050123092834.196">The fix was to add nosentinels=nosentinels in the call to initWriteIvars in atFile.write.</t>
<t tx="ekr.20050123092834.422">This method now does nothing if at.toString is True.</t>
<t tx="ekr.20050123092834.424"></t>
<t tx="ekr.20050123092834.431"></t>
<t tx="ekr.20050123092834.432">Leo did not correctly write adjacent @doc parts in @file trees.  Leo could not read the resulting derived files!

The bug happened if any node in an @file tree contains adjacent @doc parts, like this:

@  first doc part
...
@ second doc part
...

Leo failed to write the closing #@-at sentinel that would finish the first @doc part.</t>
<t tx="ekr.20050123092834.434">The new code uses protocol=1 instead of the deprecated bin argument to Pickler.</t>
<t tx="ekr.20050123092834.438"></t>
<t tx="ekr.20050123092834.439">The problem was that nullLog.write calls print, and if print is redirected the
code ends up calling nullLog.write again.

What I did:

- g.redirectClass.redirect does nothing if g.app.batchMode is True.
- added g.rawPrint.
- Changed self.old.write(s) to self.old.write(s+'\n') throughout.</t>
<t tx="ekr.20050123092834.474">It makes no sense to use only the selected text.</t>
<t tx="ekr.20050123092834.480">The old code assumed that the error is always in the script itself. Not true!
The error could happen in methods called by the script.

This code works with Python 2.3.4 and Python 2.4.  It may be version dependent.</t>
<t tx="ekr.20050123092834.486"></t>
<t tx="ekr.20050123092834.487">Leo now sets the name of the frame to the requested file name on the command line even if the file name does not exist.</t>
<t tx="ekr.20050123092834.490">The code now clears previous shortcut, and tells what the previous entry was.</t>
<t tx="ekr.20050123092834.491">Changed the open command associated with .leo files on Windows from:

pythonw.exe "&lt;leodir&gt;\src\leo.py" %1

to:

"pythonw.exe" "&lt;leodir&gt;\src\leo.py" "%1"

The difference is in quotes.  Especially quotes around "%1" seem to matter.</t>
<t tx="ekr.20050123092834.492">This is an important difference. imp.load_module is equivalent to a reload, so
we must not call this if the module already exists!</t>
<t tx="ekr.20050123092834.497">Leo did not properly write derived files that contained section references to grand-children.

For example:

&lt;&lt; current level&gt;&gt;
  reference to &lt;&lt; 3. level&gt;&gt;
    &lt;&lt; 1.level&gt;&gt;
        &lt;&lt; 2.level &gt;&gt;
            &lt;&lt; 3.level&gt;&gt;

The fix was simply to reverse the order in which putRefAt puts +middle and -middle sentinels.</t>
<t tx="ekr.20050123092834.499">In some cases g.app.config.output_newline was None.  The new code sets the default to '', and then assigns a valid default to ''.</t>
<t tx="ekr.20050123092834.502">This binds scroll-wheel events to Button-4 and Button-5
</t>
<t tx="ekr.20050123092834.506">chapters.py requires that the canvas have a name ivar.

Added treeCanvas.name = '1' in:
    
&lt;&lt; replace tree pane with settings tree &gt;&gt;</t>
<t tx="ekr.20050123092834.510"></t>
<t tx="ekr.20050123092834.517">Leo can still read such files, but old-style file formats are now deprecated</t>
<t tx="ekr.20050123092834.520">The new code greatly simplifies the class structure. The intention is to allow plugins to override methods of this file more easily.

The highlights:

- Plugins may now override methods in this file much more easily.
    - All code is now in a single class.
    - Resolved the few name conflicts by renaming x to x3 or x4.
    - The new code generally uses methods instead of sections.
    - Initialiation is now simple and sane, and is done in dedicated methods.
    - All constants are class constants: no more module-level constants.

- All top-level methods support toString or fromString arguments.</t>
<t tx="ekr.20050123092834.526">Fixed shawdow warnings.  The following are all Python global functions:

cmp -&gt; compare
dict -&gt; theDict
dir -&gt; theDir
file -&gt; theFile
id -&gt; theId
type -&gt; theType
input  (suppressed the warning)
iter -&gt; theIter</t>
<t tx="ekr.20050123092834.544">Apparently distutils.file_util is not present in all Python distributions!

New approaches:
    - Fall back on code in distutils.file_util if import fails.
    - Make sure the src and dst volumes are the same (so Linux os.rename will always work)
    - Simplify replaceTargetFileIfDifferent by creating new routines.

What I did:
    - Rewrote replaceTargetFileIfDifferent in terms of atFile.rename, atFile.remove, etc.
    - Rewrote update_file_if_changed in terms of g.utils_rename, g.utils_remove, etc.</t>
<t tx="ekr.20050123092834.565">Leo's code now contains an important simplification to Leo's gui code. This
arose because of a problem in the UNL plugin. The window that opened when double
clicking an @url UNL node wasn't staying on top.

It turns out that this was essentially impossible to fix with the old code. The
proximate cause of the original problem button-1 was bound to OnActivateTree,
which called g.app.gui.set_focus after the new window was visible, thereby
bringing the old tree to the front.

Further investigation revealed other problems. For example, the idle-time code
in the status line logic was also messing with the focus. It turns out that
repeatedly calling g.app.gui.set_focus is a very bad idea, for lots of reasons
which I won't go into in detail here.

The old code called g.app.gui.set_focus explicitly whenever it wanted focus to
change. But there is a much better way, namely to have routines that _indicate_
where they want the focus to be "after the dust settles", that is, when all gui
calls have been completed. I call this a "delayed focus" scheme.

So I rewrote all the code that sets the focus. The new code replaces direct
calls to g.app.gui.set_focus with calls to the following methods in
leoTkinterFrame class: bodyWantsFocus, statusLineWantsFocus, treeWantsFocus and
logWantsFocus. Actually, these xWantsFocus methods all do the same thing, but
using different methods improves traces.

This is an excellent pattern. Again, rather than setting the focus directly,
these xWantsFocus methods merely signal their intension to set the focus. This
allows very complex logic to be hidden in leoTkinterFrame.set_focus.

leoTkinterFrame.set_focus is indeed complex. It took me several hours this
morning to get it just right. It queues up a 'one-shot' callback. That is, at
most one copy of the callback is ever waiting to be executed. Furthermore, the
callback is only queued for execution at the result of a call to xWantsFocus; it
is never run automatically at idle time. Finally, even when executed, the
callback does nothing if the last requested commander (in the new ivar,
g.app.wantedFocus) does not match the commander to which the callback was bound.

These checks allow the UNL plugin to open a window properly and keep it topmost.

This is a big step forward for Leo, for the following reasons:

- Delayed focus ensures that the body pane always has focus unless the code has
a specific, positive reason for the focus to be elsewhere. This was difficult
(or rather impossible) to do with the old code: there are _many_ Tk calls that
can affect the focus.

- Delayed focus minimizes calls to g.app.gui.set_focus. Unlike the old code,
many seconds may elapse between calls. The stress on Tk is much less, and I
believe this may cure some flakiness in how focus changes, especially in
headlines.

- There are some cases where focus must change immediately. The xWantsFocus
methods all support a 'later' keyword argument. By default it is True, but when
it is False leoTkinterFrame.set_focus calls g.app.gui.set_focus immediately.

- The xWantsFocus methods all support a 'tag' keyword argument that tells what
routine the method is called from. It is a big help in making sense of traces.
BTW, extensive traces are the _only_ possible way of tracking down
focus/selection problems.</t>
<t tx="ekr.20050123092834.896"></t>
<t tx="ekr.20050123092834.897">These commands work as do the similar commands in Windows Explorer. How did we
ever live without them?</t>
<t tx="ekr.20050123092834.901">This supports the fromString option in read commands.</t>
<t tx="ekr.20050123092834.903">Thanks to Bernhard Mulder for the new code.</t>
<t tx="ekr.20050123092834.908">- Tab toggles between the Search to the Replace areas.

- Control-Tab inserts a tab.

- Added hot keys for all settings.  Use Alt-x to activate hot key x.
  The Enter key activates the Find button.

- As usual, Alt-F4 dismisses the Find panel.</t>
<t tx="ekr.20050123092834.928">It's not clear that this support is so useful for debugging scripts.

If g.app.debugSwitch is True es_exception gives a full traceback.</t>
<t tx="ekr.20050123092834.929">Thanks to David McNab &lt;david@freenet.org.nz&gt; for this work.</t>
<t tx="ekr.20050123092834.961">- Go To Line Number command now assumes the presently selected node is a script if there is no ancestor @file node.

- Execute Script command uses this new logic to select the proper node and line in a script if there is an error.

How did we ever live without these features?</t>
<t tx="ekr.20050123092834.984">Restored the following hooks:
    
"boxclick1"     before click in +- box            c,p,v,event
"boxclick2"     after  click in +- box            c,p,v,event
"drag1"         before start of drag              c,p,v,event
"drag2"         after  start of drag              c,p,v,event
"dragging1"     before continuing to drag         c,p,v,event
"dragging2"     after  continuing to drag         c,p,v,event
"enddrag1"      before end of drag                c,p,v,event
"enddrag2"      after  end of drag                c,p,v,event

The following already existed.  I added v=p keyword params:

"iconclick1"    before single click in icon box   c,p,v,event
"iconclick2"    after  single click in icon box   c,p,v,event
"iconrclick1"   before right click in icon box    c,p,v,event
"iconrclick2"   after  right click in icon box    c,p,v,event
"icondclick1"   before double click in icon box   c,p,v,event
"icondclick2"   after  double click in icon box   c,p,v,event</t>
<t tx="ekr.20050123092834.1004">Changed these hooks:

"bodyclick1", "bodyclick2",
"bodydclick1", "bodydclick2",
"bodyrclick1", "bodyrclick2",
"bodykey1", "bodykey2",
"command1", "command2",
"headclick1", "headclick2",
"headrclick1", "headrclick2",
"headkey1", "headkey2", 
"hyperclick1", "hyperclick2",
"hyperenter1", "hyperenter2",
"hyperleave1", "hyperleave2", 
"openwith1", "openwith2",
"menu1", "menu2", 
"recentfiles1", "recentfiles2",
"save1", "save2",
"select1", "select2", "select3",
"start2",
"unselect1", "unselect2",
"url1", "url2", 

"clear-mark", "set-mark", 
"color-optional-markup",
"create-popup-menu", 
"draw-outline-icon",
"draw-outline-node",
"draw-outline-text-box",
"draw-sub-outline", 
"init-color-markup",
"scan-directives", 
"draw-outline-box",
"enable-popup-menu-items",
"show-popup-menu",</t>
<t tx="ekr.20050123092834.1005">Leo no loner has any global windows!

- Each commander has its own find window.
    - It's title tells to what commander it applies.
</t>
<t tx="ekr.20050123092834.1011">computeHomeDir() now test the first retrieval of the %HOME% var and grab it's
results if it is in fact another environment variable.</t>
<t tx="ekr.20050123092834.1013"></t>
<t tx="ekr.20050123092834.1018">Actually, support already existed for them in getBaseDirectly!

What I did.

- Added a c keyword to getBaseDirectory.
- Added similar logic to os_path_join.

- Changed some stupid code in g.openWithFileName (called by @url logic):
    changed: fileName = g.os_path_join(os.getcwd(),fileName)
    to:      fileName = g.os_path_abspath(fileName)

MAYBE g.os_path_abspath should force '.' to mean c.openDir, but I kinda doubt
it. This could be asking for trouble.

OTOH, the various flavors of scanAllDirectives already do this.  Hmmmmmm.</t>
<t tx="ekr.20050123092834.1043"></t>
<t tx="ekr.20050123092834.1044"></t>
<t tx="ekr.20050123092834.1047">- This plugin now handles both kinds of triple-quotes correctly so that both
kinds of docstrings are recognized.

- This plugin now is controlled by the first reference to a plugin in
pluginsManager.txt. All other references are ignored.</t>
<t tx="ekr.20050123092834.1052">Created callTagHandler. This checks 'idle' hooks to make sure that any commander
referenced by the 'c','new_c' or 'old_c' keywords still exists.</t>
<t tx="ekr.20050123092834.1057">leoPlugins.registerOneHandler wasn't working properly at all. In effect, only
the last registered hook was ever being remembered!</t>
<t tx="ekr.20050123093854.1">tnodes_iter and unique_tnodes_iter were returning vnodes, not tnodes!</t>
<t tx="ekr.20050123100706.1"></t>
<t tx="ekr.20050123100706.2"></t>
<t tx="ekr.20050123101208"></t>
<t tx="ekr.20050123103303"></t>
<t tx="ekr.20050123103303.1"></t>
<t tx="ekr.20050123103521"></t>
<t tx="ekr.20050123103753"></t>
<t tx="ekr.20050123105026">- Leo now ignores all find settings in .leo files.  Instead, Leo inits find settings from @settings entries.

- Removed all c ivars corresponding to leoFind ivars.
    - This eliminates the ugliest code in Leo.
    - Inits all leoFind ivars from @settings in init, a helper of the ctor.
    - Updates all the leoFind ivars in update_ivars, called just before doing any find.

- Removed the _flag suffix from leoFind ivars.
    - Another major mess cleaned up.

- Renamed find/change_text to find/change_ctrl to avoid name conflict.</t>
<t tx="ekr.20050123110009">Leo now stores options in @settings trees, that is, outlines whose headline is '@settings'. When opening a .leo file, Leo looks for @settings trees not only in the outline being opened but also in various leoSettings.leo files.

The key design goal of @settings trees was that Leo's user options must be infinitely flexible. That goal has been accomplished. Indeed, users can create arbitrarily complex user options with @settings trees. Leo settings outlines are, in fact, infinitely more flexible and powerful than any scheme based on flat text.

The Settings command temporarily replaces the outline pane with an outline showing all the @settings trees in effect. The Settings command also replaces the body pane with a "settings pane". This settings pane allows you to change the settings selected in the outline pane using standard gui widgets. The settings pane is dynamically created from nodes in the settings tree; it is as extensible as the @settings tree itself.

For full details, see the children of this node.</t>
<t tx="ekr.20050123111723"></t>
<t tx="ekr.20050123112151">- leoPlugins.doHandlersForTag now executes the list of hook handlers for a
particular tag (hook name) until one of the handlers returns a non-None result.
doHandersForTag no longer tries to "sort" handlers, so the order that the
handlers are executed is the order in which they were registered.

I finally understand the concerns people have raised several times about hooks
interfering with each other. If two handlers try to return a non-None result
only one of them will ever execute. doHandlersForTag can't do much about this: a
better solution would require more conceptual framework. Not now...</t>
<t tx="ekr.20050123112834"></t>
<t tx="ekr.20050123115804">Leo now boasts a wonderful new Plugins Manager plugin.  This plugin enables and disables plugins automatically.  You never have to mess with pluginsManager.txt again!  This plugin also tells you everything you need to know about each plugin.  Finally, this plugin also lets you download plugins from Leo's cvs site!  Many thanks to Paul Patterson for this excellent work.

Note.  The Plugins Manager plugin requires Pmw.  You can install Pmw in Leo's extensions directory if you like.</t>
<t tx="ekr.20050123115804.1">You can can import any extension to Leo by putting the extension in the 'extensions' directory and using g.importExtension to import it.

- created the 'extensions' directory and g.app.extensionsDir

- created g.importModule and g.importExtension</t>
<t tx="ekr.20050123151338">Changed scanDirectives and atFile.scanDirectives so they work like tangle.scanAllDirectives.  Also added a few clarifying words in LeoDocs.leo.

This should have worked, but didn't:

+ Code 
  @language python 
  + @file sql_create.sql 
    @comment -- 
 
So I rearranged the outline (probably more logical anyway) to  
+Code 
  + Python 
  ... 
+ SQL 
  ... </t>
<t tx="ekr.20050126100405">Leo 4.3 alpha 2                 February 14, 2005

Leo 4.3 is the culmination of more than four months of work. This alpha 2
release corrects various bugs and distribution problems.

a2 also adds several new features:

- Adds 'word', 'line' and 'node' undo granularities.
- Predefines 'c','g', and 'p' in scripts and unit tests.
- Added support for top-level init functions in plugins.
- Buttons can remove themselves when their scripts fail.

The defining features of Leo 4.3:

1. Leo now stores options in @settings trees, that is, outlines whose headline
is '@settings'. When opening a .leo file, Leo looks for @settings trees not only
in the outline being opened but also in various leoSettings.leo files.

The key design goal of @settings trees was that Leo's user options must be
infinitely flexible. That goal has been accomplished. Indeed, users can create
arbitrarily complex user options with @settings trees. Leo settings outlines
are, in fact, infinitely more flexible and powerful than any scheme based on
flat text.  Readers of Python's configParser shootout take note!

2. The Settings command temporarily replaces the outline pane with an outline
showing all the @settings trees in effect. The Settings command also replaces
the body pane with a "settings pane". This settings pane allows you to change
the settings selected in the outline pane using standard gui widgets. The
settings pane is dynamically created from nodes in the settings tree; it is as
extensible as the @settings tree itself.

3. Leo's read/write code in leoAtFile.py has been rewritten to support user-
defined tangling and untangling.  This is a major cleanup of Leo's core.

4. Leo now boasts a wonderful new Plugins Manager plugin. This plugin enables
and disables plugins automatically. You never have to mess with
pluginsManager.txt again! This plugin also tells you everything you need to know
about each plugin. Finally, this plugin also lets you download plugins from
Leo's cvs site! Many thanks to Paul Patterson for this excellent work.

5. You can install third-party extensions in Leo's extensions directory. Leo
will attempt to import such extensions from the extensions directory if normal
imports fail.  Leo is distributed with Pmw (Python Mega Widgets) in this directory.</t>
<t tx="ekr.20050126100405.1"></t>
<t tx="ekr.20050130112336.1">Warning: The following features of @recentfiles nodes are confusing and probably
will be changed:

- Leo does not save recent file information unless the open .leo file has an
@settings tree and an @recentfiles node within the @settings tree. That is, Leo
does not save recent files information in leoSettings.leo files.

- Changing the @rencentfiles node doesn't mark the Leo file as dirty, so if you
don't save the .leo file the recent files information will not be updated.</t>
<t tx="ekr.20050209141626.3"></t>
<t tx="ekr.20050209141626.4">http://sourceforge.net/forum/message.php?msg_id=2795653

1. Select a node in the tree
2. Hit CTRL-I to insert a node
3. Hit CTRL-Z to undo the insert
4. There is no longer a node selected in the tree so keyboard tree navigation etc commands don't work until you click on something with the mouse

-----

http://sourceforge.net/forum/message.php?msg_id=2795656

1. Select a node in the tree
2. Hit CTRL-I to insert a node
3. Hit CTRL-Z to undo the insert
4. Hit Hoist before clicking on anything

Now you are hoisted on the recently removed node! The node is dead but his memory lives on ...</t>
<t tx="ekr.20050209141626.8"></t>
<t tx="ekr.20050209141626.12"></t>
<t tx="ekr.20050209141626.13"></t>
<t tx="ekr.20050209141626.16">http://sourceforge.net/forum/message.php?msg_id=2966541

---- Report:

"Recent Files"  is not remembering files after one closes all open leo sessions.

But it does update the "Recent Files" list while leo is open in the same session.
If one opens more files it adds them to the list. But close all files and Leo
forgets them all.

---- Added to @recentfile documentation: 

Warning: The following features of @recentfiles nodes are confusing and probably
will be changed:

- Leo does not save recent file information unless the open .leo file has an
@settings tree and an @recentfiles node within the @settings tree. That is, Leo
does not save recent files information in leoSettings.leo files.

- Changing the @rencentfiles node doesn't mark the Leo file as dirty, so if you
don't save the .leo file the recent files information will not be updated.</t>
<t tx="ekr.20050209141626.23">http://sourceforge.net/forum/message.php?msg_id=2960328

Symptom

Can not import messages were not being sent to the console, even though there is a call to es in g.cantImport.

What I did

- The code in g.es now checks for nullLog as well as log == None when deciding when to queue messages.

- g.openWithFileName now calls g.app.writeWaitingLog immediately after enabling the new log.

This writes the queued log messages in the proper order: a major advance in clarity.

- Added silent param to two methods.

This allows the 'reading settings from' message to be sent to the log instead of the default 'reading' message.</t>
<t tx="ekr.20050209141626.42"></t>
<t tx="ekr.20050209141626.43">The new code no longer requires that the present node have a tnodeList.

File "/Users/edream/leoCVS/leo/src/leoAtFile.py", line 3830, in putOpenNodeSentinel
    at.root.v.t.tnodeList.append(p.v.t)
    
AttributeError: 'tnode' object has no attribute 'tnodeList'</t>
<t tx="ekr.20050209141626.46">The message 'command for widget 5' was a message from Tk saying in effect that no command was bound to the button.

Indeed, this was so: a recent botch in a change in mod_scripting.py prevented the binding.

Moreover, there were some extra print statments in the g.es logic for the Mac.</t>
<t tx="ekr.20050209141626.53">This makes the test more robust in case of failure.</t>
<t tx="ekr.20050209141626.54">Changed the setup code for the import/export test cases so that it uses os.path.sep when it sees \\ in the test nodes.

With this change all unit tests pass on the Mac as well as on XP.</t>
<t tx="ekr.20050209141626.55">*None* of the local settings were working(!!)

The old init code in the configSettings class had no chance of working. We must
use the full g.app.config.get logic.

Added some very simple unit tests to make sure the basics will never break
again so easily.</t>
<t tx="ekr.20050209141626.91">There were problems searching for whitespace.

Note: it just ran slowly &amp; silently.</t>
<t tx="ekr.20050209141626.101"></t>
<t tx="ekr.20050209141626.102">http://sourceforge.net/forum/message.php?msg_id=2958470

I opened a new .leo file, and the cursor was flashing in the text box. I started
typing "@language", and found that the first character is in the text box, and
the rest is in the headline!

What I did:

This was the result of a race condition in the new scheme for setting focus. I
rewrote set_focus so the delayed callback always sets the last requested focus.
The new code also takes care to clear the last request after fulfilling it.</t>
<t tx="ekr.20050209141626.105">http://sourceforge.net/forum/message.php?msg_id=2958470

All changes were to g.app.leoID():

- Fixed bug:  set g.app.leoID in &lt;&lt; put up a dialog requiring a valid id &gt;&gt;.
- Improved signon message.
- Better error handling and reporting. </t>
<t tx="ekr.20050209141626.113">This now works: g.es('ﺻﺱ',color='red')

g.es must send the original unicode string to the log pane widget, NOT an encoded string.</t>
<t tx="ekr.20050209141626.114">http://sourceforge.net/forum/message.php?msg_id=2983923

- Replaced string.+ with string.% in numerous places.
- Simplified g.openWithFileName and corrected problems in error-reporting logic.</t>
<t tx="ekr.20050209141626.150"></t>
<t tx="ekr.20050209141626.185">When loading plugins, the Leo checks to see if the plugin has an init function
at the top level (the module level). If so, Leo calls the init function. This
function should return True (or equivalent) if the module loaded correctly.

If the top-level init function does not exist, Leo assumes the module loaded
correctly.</t>
<t tx="ekr.20050209141626.190"></t>
<t tx="ekr.20050209141626.193"></t>
<t tx="ekr.20050209141626.194">A script in an @button node or script node can now request to be removed by
setting g.app.scriptDict['removeMe'] = True. Leo checks this value after
executing the script in the button.</t>
<t tx="ekr.20050209141626.195"></t>
<t tx="ekr.20050209141626.196">@nocolor

Added define_p keyword arg in executeScript. When True (the default), the script
or unit test is run in an environment in which ``c``, ``p`` and ``g`` are all defined.
``c`` is the commander for the outline in which the script appears.
``p`` is the same as ``c.currentPosition`` and ``g`` is the leoGlobals module.

Therefore, the following lines need never appear in scripts or unit tests!

@color

import leoGlobals as g
p = c.currentPosition()</t>
<t tx="ekr.20050209141626.198"></t>
<t tx="ekr.20050210101318">Typing return now correctly invokes the Find button, without adding a newline in the find string.</t>
<t tx="ekr.20050210102150"></t>
<t tx="ekr.20050210102150.1"></t>
<t tx="ekr.20050210102358"></t>
<t tx="ekr.20050211095754">@nocolor
http://sourceforge.net/forum/message.php?msg_id=2990951
Milan Melena

I think, I found two bugs:

1) leoAtFile.py:
&lt;&lt; read optional encoding param &gt;&gt;
changed first instance of i = j + 1 to i = j + 2

2) leoGlobals.py
g.getScript now returns with

if at.output_newline == 'crlf':
    return script.replace("\r\n","\n")
else:
    return script</t>
<t tx="ekr.20050212054743">At present, such indented blocks may not contain Leo directives or section references.  This will be fixed in 4.3a3.</t>
<t tx="ekr.20050212144116">1. (fixed) C:\prog\leoCVS\leo\src\leoCommands.py:4539: No global (loadDir) found
    # Would cause leoSettings.leo in Window menu to crash.
    
2. (fixed) C:\prog\leoCVS\leo\src\leoGlobals.py:3426: No global (local) found
    
    # Local --&gt; locale
    # Might cause getpreferredencoding to fail on *nix.
    
3. (fixed) C:\prog\leoCVS\leo\src\leoGlobals.py:4152: No global (testing) found
    # Should be self.testing.
    
4. (fixed) mu problems:
    - Changed x to self.x:
        - C:\prog\leoCVS\leo\src\leoGlobals.py:3795: No global (removeSentinelsFromLines) found
        - C:\prog\leoCVS\leo\src\leoGlobals.py:3838: No global (getSentinelsFromLines) found
    - Changed self.x to g.x:
        C:\prog\leoCVS\leo\src\leoGlobals.py:3854: No class attribute (comment_delims_from_extension) found
    - pull_source has been renamed, I don not know to what.
        C:\prog\leoCVS\leo\src\leoGlobals.py:4170: Object (mu) has no attribute (pull_source)
        (commented out the code that contains this)
        
5. (removed code) from &lt;&lt; create a node p for  kind &amp; root2 &gt;&gt;
    - last_p is None at first, so last_p.insertAfter does not make sense.</t>
<t tx="ekr.20050219093156">@nocolor

c.frame.menu.createMenuItemsFromTable will append items to the end of an existing menu.  For example, the following script will add a new item at the end of the 'File' menu. 
@color

def callback(*args,**keys):
    g.trace()

table = (("Test1",None,callback),)

c.frame.menu.createMenuItemsFromTable('File',table)

@nocolor
Plugins can do anything that can be done with Tk using the menu returned by c.frame.menu.getMenu.  For example, here is a script that adds a Test menu item after the 'Open With' menu item in the File menu.
@color

def callback(*args,**keys):
    g.trace()

fileMenu = c.frame.menu.getMenu('File')

# 3 is the position in the menu.  Other kinds of indices are possible.
fileMenu.insert(3,'command',label='Test2',command=callback)</t>
<t tx="ekr.20050219093156.1"></t>
<t tx="ekr.20050219093156.2">The authoritative source for information.</t>
<t tx="ekr.20050221104844">Leo 4.3 alpha 3                 February 24, 2005

Leo 4.3 is the culmination of more than five months of work. This alpha 3
release corrects various bugs in Leo's core and in plugins. This is the first
release that include an installer for MacOSX.

The defining features of Leo 4.3:

1. Leo now stores options in @settings trees, that is, outlines whose headline
is '@settings'. When opening a .leo file, Leo looks for @settings trees not only
in the outline being opened but also in various leoSettings.leo files.

The key design goal of @settings trees was that Leo's user options must be
infinitely flexible. That goal has been accomplished. Indeed, users can create
arbitrarily complex user options with @settings trees. Leo settings outlines
are, in fact, infinitely more flexible and powerful than any scheme based on
flat text.  Readers of Python's configParser shootout take note!

2. The Settings command temporarily replaces the outline pane with an outline
showing all the @settings trees in effect. The Settings command also replaces
the body pane with a "settings pane". This settings pane allows you to change
the settings selected in the outline pane using standard gui widgets. The
settings pane is dynamically created from nodes in the settings tree; it is as
extensible as the @settings tree itself.

3. Leo's read/write code in leoAtFile.py has been rewritten to support user-
defined tangling and untangling.  This is a major cleanup of Leo's core.

4. Leo now boasts a wonderful new Plugins Manager plugin. This plugin enables
and disables plugins automatically. You never have to mess with
pluginsManager.txt again! This plugin also tells you everything you need to know
about each plugin. Finally, this plugin also lets you download plugins from
Leo's cvs site! Many thanks to Paul Patterson for this excellent work.

5. You can install third-party extensions in Leo's extensions directory. Leo
will attempt to import such extensions from the extensions directory if normal
imports fail. Leo is distributed with Pmw (Python Mega Widgets), path.py and
sets.py in this directory.</t>
<t tx="ekr.20050221104844.2"></t>
<t tx="ekr.20050221104844.3">http://sourceforge.net/forum/message.php?msg_id=2998446
By: djsg

g.create_temp_name() calls tempfile.mktemp or mkstemp(), but these return different values!

mktemp returns the filename(a string); mkstemp returns a tuple (handle,filename)

What I did:

- Changed g.create_temp_name to g.create_temp_file.
- Removed the file open logic in tangle.put_all_roots (now done in g.create_temp_file)
- Rewrote g.create_temp_file so it works in both cases.
- Create test routine for g.create_temp_file
- Created very simple unit tests in test.leo for tangle and untangle.</t>
<t tx="ekr.20050221104844.12">http://sourceforge.net/forum/message.php?msg_id=2999651

I was pleasantly surprised to discover the reST2 plug-in working under 4.3a2
(this is one the first thing I try as I'd like to use Leo as an editor
for that).

As mentioned in early threads, it still needs @rst for each node to be included
in the reST rendering process. So I put @rst test.html and then a child with
@rst and some reST code and it worked !!

Then I tried to to get a simple rst file using @rst test but the plugin complained:

[snip]

  File "C:\dn_apps\Leo\plugins\rst2.py", line 164, in onIconDoubleClick
    writeTreeAsRst(rstFile,fname,p,c)
TypeError: writeTreeAsRst() takes exactly 5 arguments (4 given)

So I looked at the rst2.py and found a way to get it working but I would need
someone to verify it :

line 164, replaced   writeTreeAsRst(rstFile,fname,p,c)  by

syntax = False
writeTreeAsRst(rstFile,fname,p,c,syntax)

And it worked!
</t>
<t tx="ekr.20050221104844.14"></t>
<t tx="ekr.20050221104844.27">http://sourceforge.net/forum/message.php?msg_id=3005140
By: ktenney

- perform a search which marks a number of nodes
- select "Outline -&gt; Mark/Unmark -&gt; Unmark All"
- Several marks are still listed in in the nodenavigator "Marks" list.
  (They are not marked in the outline.)

What I did:

- The p.set/clearMark methods now call the hook _after_ changing the marked status.
  This fixes the apparent bug in nodenavigator.py.
- Rewrote nav_buttons.py.  The old code was a mess; the new code is clean.
- Changed the vnodeList ivar in leoTkinterDialog to positionList.
- Rewrote c.unmarkAll to make clear that it is using positions.
    - Added test_c_unmark_all test routine.</t>
<t tx="ekr.20050221104844.45">http://sourceforge.net/forum/message.php?msg_id=2958470
From: Rich

Leo 4.3 alpha 1, build  1.208 , January 24, 2005
Python 2.3.4, Tk 8.4.3, win32

Opened a new .leo file. It asked for an ID, and said it saved it. Closed the
new leo file &amp; tried opening "Leo\config\leoSettings.leo". _It_ is asking for
a leoID!

What I did

All changes were to g.app.leoID():
    - Fixed bug:  set g.app.leoID in &lt;&lt; put up a dialog requiring a valid id &gt;&gt;.
    - Improved signon message.
    - Better error handling and reporting. </t>
<t tx="ekr.20050221104844.54">g.pdb wasn't working because pdb wasn't imported inside the function.</t>
<t tx="ekr.20050221104844.57"></t>
<t tx="ekr.20050221104844.58">This allows plugins such as plugin_manager.py to work on Python 2.2.x.</t>
<t tx="ekr.20050221104844.59">g.es does nothing if color=='suppress'.  This can be useful in unit tests.</t>
<t tx="ekr.20050222100936">http://sourceforge.net/forum/message.php?msg_id=3008045

Leo crashed when executing a script if the script was selected text in a new window.

What I did:

- g.getScript now calls g.getOutputNewline(c=c) rather than look at atFile.output_newline.

atFile.output_newline may not exist if a) the file is new and b) g.getScript
doesn't call atfile.write.

- Set scripting=scriptWrite in call to atFile.scanAllDirectives in atFile.write.

This suppresses the following irrelevant message when executing scripts:

    "No absolute directory specified anywhere."</t>
<t tx="ekr.20050313101229">Leo 4.3 alpha 4                 March 15, 2005

Leo 4.3 is the culmination of more than five months of work. This alpha 4
focuses on plugins: all known plugins are now in leoPlugins.leo. Most plugins
now work with the 4.3 code base. Warning: not all plugins have been tested
thorougly.

This alpha 4 release also adds the requently-requested Add Comments and Delete
Comments commands to Leo's Edit Body menu.

The defining features of Leo 4.3:

1. Leo now stores options in @settings trees, that is, outlines whose headline
is '@settings'. When opening a .leo file, Leo looks for @settings trees not only
in the outline being opened but also in various leoSettings.leo files.

The key design goal of @settings trees was that Leo's user options must be
infinitely flexible. That goal has been accomplished. Indeed, users can create
arbitrarily complex user options with @settings trees. Leo settings outlines
are, in fact, infinitely more flexible and powerful than any scheme based on
flat text.  Readers of Python's configParser shootout take note!

2. The Settings command temporarily replaces the outline pane with an outline
showing all the @settings trees in effect. The Settings command also replaces
the body pane with a "settings pane". This settings pane allows you to change
the settings selected in the outline pane using standard gui widgets. The
settings pane is dynamically created from nodes in the settings tree; it is as
extensible as the @settings tree itself.

3. Leo's read/write code in leoAtFile.py has been rewritten to support user-
defined tangling and untangling.  This is a major cleanup of Leo's core.

4. Leo now boasts a wonderful new Plugins Manager plugin. This plugin enables
and disables plugins automatically. You never have to mess with
pluginsManager.txt again! This plugin also tells you everything you need to know
about each plugin. Finally, this plugin also lets you download plugins from
Leo's cvs site! Many thanks to Paul Patterson for this excellent work.

5. You can install third-party extensions in Leo's extensions directory. Leo
will attempt to import such extensions from the extensions directory if normal
imports fail. Leo is distributed with Pmw (Python Mega Widgets), path.py and
sets.py in this directory.</t>
<t tx="ekr.20050313101229.2"></t>
<t tx="ekr.20050313101229.69">Nodes containing the @root directive did not honor @nocolor directives.</t>
<t tx="ekr.20050313101229.74">http://sourceforge.net/forum/message.php?msg_id=3035471

Leo was not inserting a visible horizontal scrollbar when @nowrap was in effect.</t>
<t tx="ekr.20050313101229.77">http://sourceforge.net/forum/message.php?msg_id=3042593

Leo now properly redraws the screen after a Change All command.</t>
<t tx="ekr.20050313101229.94">Several hooks use the 'new_c' key in the keywords dictionary. Plugin writers had
to remember whether to get the commander using keywords.get('c') or
keywords.get('new_c') or both. This was needlessly confusing.

All hooks that use the 'new_c' key now use also include the 'c' key. The 'new_c'
key is deprectated; plugins should use the 'c' key instead. 

None of the plugins presently in leoPlugins.leo use the 'new_c' key, but the
'new_c' key still exists for compatibility.

The following plugins were affected by this change:

ConceptualSort.py
URLloader.py
UASearch.py
arrows.py
autocompleter.py
base64Packager.py
cleo.py
dyna_menu.py
macros.py
mod_read_dir_outline.py
mod_scripting.py
multifile.py
nodebar.py
nodenavigator.py
open_with.py
scheduler.py
read_only_nodes.py
templates.py</t>
<t tx="ekr.20050313101229.95">The Add Comments command puts comments around a block of code. This command uses
single-line comments if the language in effect for the node supports single-line
comments.

The Delete Comments command deletes the comments specified by the Add Comments command.</t>
<t tx="ekr.20050313101229.100">Fixed problems in the following plugins. See the &lt;&lt; version history &gt;&gt; section
in each plugin for details.

autocompleter.py
cleo.py
mod_scripting.py
mod_tempfname.py
templates.py
vim.py
xemacs.py

Replaced the 'new_c' key by the 'c' key in the following plugins:

ConceptualSort.py
URLloader.py
UASearch.py
arrows.py
autocompleter.py
base64Packager.py
cleo.py
dyna_menu.py
macros.py
mod_read_dir_outline.py
mod_scripting.py
multifile.py
nodebar.py
nodenavigator.py
open_with.py
scheduler.py
read_only_nodes.py
templates.py

Replaced the 'start2' hook by the 'new' hook in the following plugins: (This was
made possible now that 'new' is called when opening a new window if the
'open1/2' hooks are not called.

URLloader.py
UASearch.py
at_produce.py
autocompleter.py
color_markup.py
fastGotoNode.py
groupOperations.py
import_cisco_config.py
multifile.py
nodebar.py
open_with.py
read_only_nodes.py
scheduler.py
table.py
usetemacs.py
xsltWithNodes.py</t>
<t tx="ekr.20050313101229.101">atFile.copyAllTempBodyStringsToTnodes calls:

    c.mod_label_controller.add_label(p,"before change:",old_body)</t>
<t tx="ekr.20050313103448"></t>
<t tx="ekr.20050313103448.1">Leo calls the 'before-create-leo-frame' hook just before calling frame.onCreate.
Similarly, Leo calls the 'after-create-leo-frame' just after calling
frame.onCreate.</t>
<t tx="ekr.20050404094627"></t>
<t tx="ekr.20050407144342"> 
        
        
        </t>
<t tx="ekr.20050407144342.1"></t>
<t tx="ekr.20050407144342.2"></t>
<t tx="ekr.20050407144342.3"></t>
<t tx="ekr.20050407144417"></t>
<t tx="ekr.20050429094215">Leo 4.3 beta 1                 April 30, 2005

Leo 4.3 beta 1 completes all major features of Leo 4.3. There are no known
significant bugs remaining.

The defining features of Leo 4.3:
---------------------------------
1. Leo now stores options in @settings trees, that is, outlines whose headline
is '@settings'. When opening a .leo file, Leo looks for @settings trees not only
in the outline being opened but also in various leoSettings.leo files.

The key design goal of @settings trees was that Leo's user options must be
infinitely flexible. That goal has been accomplished. Indeed, users can create
arbitrarily complex user options with @settings trees. Leo settings outlines
are, in fact, infinitely more flexible and powerful than any scheme based on
flat text.  Readers of Python's configParser shootout take note!

2. The Settings command temporarily replaces the outline pane with an outline
showing all the @settings trees in effect. The Settings command also replaces
the body pane with a "settings pane". This settings pane allows you to change
the settings selected in the outline pane using standard gui widgets. The
settings pane is dynamically created from nodes in the settings tree; it is as
extensible as the @settings tree itself.

3. Leo now stores recent files information in .leoRecentFiles.txt files.

4. Leo's read/write code in leoAtFile.py has been rewritten to support user-
defined tangling and untangling.  This is a major cleanup of Leo's core.

5. Leo now boasts a wonderful new Plugins Manager plugin. This plugin enables
and disables plugins automatically. You never have to mess with
pluginsManager.txt again! This plugin also tells you everything you need to know
about each plugin. Finally, this plugin also lets you download plugins from
Leo's cvs site! Many thanks to Paul Patterson for this excellent work.

6. You can install third-party extensions in Leo's extensions directory. Leo
will attempt to import such extensions from the extensions directory if normal
imports fail. Leo is distributed with Pmw (Python Mega Widgets), path.py and
sets.py in this directory.</t>
<t tx="ekr.20050429094215.2"></t>
<t tx="ekr.20050429094215.3">The initial bug report:

http://sourceforge.net/forum/message.php?msg_id=3048149

The problem arose from a misguided attempt to eliminate non-useful information
from traces. Alas, the baby got thrown out with the bath water.

Here are the changes I made:

 - c.executeScript now calls g.es_exception(full=True) to ensure that a full
 stack trace always gets produced. This is especially important when the
 exception happens in a module (file) called by the script.

- c.executeScript now always executes the section &lt; &lt; dump the lines near the
error &gt; &gt;, regardless of context. The lines are printed (in black) in the log.
This is useful information in almost all cases.

- After much experimentation, g.es_exception is basically unchanged. Note: If
the error occurs in your script itself (as contrasted with an exception thrown
from a file called by your script) Leo always has properly put the cursor on the
offending line. I made no changes in this logic.

BTW, calling pdb.set_trace() in your scripts may cause more problems than it is
worth. Indeed.pdb.set_trace() uses only the information on the stack, and that
may not be enough information to be useful. I usually use g.trace to find out
what is happening. This works well.</t>
<t tx="ekr.20050429094215.22">Initial bug report:

http://sourceforge.net/forum/message.php?msg_id=3053699

There were three similar bugs, all arising from the fact that g.os_path_abs and
g.os_path_join return the _working_ directory if the initial path is None!

I removed my HOME directory for testing. This was essential.

- Compute home directory must return None, rather than the working directory if
the HOME variable is None.

- app.setLeoId must be careful (in two sections) to do nothing if any of
(homeDir,globalConfigDir,loadDir) is None.</t>
<t tx="ekr.20050429094215.31">The problem is that newButtons must use @nosent, so any changes to newButtons
must be accompanied by a change to LeoPluginsRef.py. There is nothing more that
needs to be done.</t>
<t tx="ekr.20050429094215.41">The De-hoist command conflicted with the Expand/Contract submenu.

The Paste Node As Clone conflicted with the Mark submenu.</t>
<t tx="ekr.20050429094215.113">The status bits weren't being passed to v.initStatus!</t>
<t tx="ekr.20050429094215.116">Traceback (most recent call last):
  File "c:\prog\leoCVS\leo\src\leoCommands.py", line 174, in doCommand
    command()
  File "c:\prog\leoCVS\leo\src\leoCommands.py", line 863, in importDerivedFile
    c.importCommands.importDerivedFiles(v,names)
  File "C:\prog\leoCVS\leo\src\leoImport.py", line 137, in importDerivedFiles
    isThin = at.scanHeaderForThin(theFile,fileName)
  File "C:\prog\leoCVS\leo\src\leoAtFile.py", line 570, in scanHeaderForThin
    junk,junk,isThin = at.scanHeader(theFile,fileName)
  File "C:\prog\leoCVS\leo\src\leoAtFile.py", line 2616, in scanHeader
    at.error("Bad @+leo sentinel in: %s" % fileName)
  File "C:\prog\leoCVS\leo\src\leoAtFile.py", line 4500, in error
    self.printError(message)
  File "C:\prog\leoCVS\leo\src\leoAtFile.py", line 4509, in printError
    if self.errors == 0:
AttributeError: atFile instance has no attribute 'errors'
</t>
<t tx="ekr.20050429094215.120">Traceback (most recent call last):
  File "C:\prog\leoCVS\leo\src\leoTkinterTree.py", line 1409, in idle_scrollTo
    h1 = self.yoffset(p)
  File "C:\prog\leoCVS\leo\src\leoTkinterTree.py", line 1488, in yoffset
    h, flag = self.yoffsetTree(root,v1)
  File "C:\prog\leoCVS\leo\src\leoTkinterTree.py", line 1506, in yoffsetTree
    h2, flag = self.yoffsetTree(child,p1)
  
# Maximum recursion depth exceeded.

It is still not completely clear why this happened.</t>
<t tx="ekr.20050429094215.130"></t>
<t tx="ekr.20050429094215.131">- Moved computeGlobalConfigDir, computeHomeDir, computeLoadDir and startupEncoding from leo.py to leoGlobals.py.

- Created g.computeStandardDirectories and used it in leo.py.

- Created g.createStandAloneApp using the above functions.  This function was based on the 'Standalone Operation' classed in the plugin_manager plugin.  g.createStandAloneApp doesn't actually use any of these classes because the nullGui class is basically a clumsier version of the BlackHole class.

- Added a do-nothing attachLeoIcon method to nullGui class to suppress a warning.  As I said, the nullGui class is not as elegant as Paul's BlackHole class.

- Added &lt;&lt;importLeoGlobals&gt;&gt; button to newButtons plugin.  This creates a node named
  &lt;&lt; define importLeoGlobals &gt;&gt; whose body text defines an importLeoGlobals function.

The idea is that importing leoGlobals from a stand-alone plugin is a bit tricky.  The importLeoGlobals handles these details.  Note that we don't want to define importLeoGlobals in a node included by @others, because this function must be available to the code in the &lt;&lt; imports &gt;&gt; section.  So we use a named section and reference it in before referencing the &lt;&lt; imports &gt;&gt; section.  See the plugin_manager plugin for an example.

- Changed the plugin_manager plugin as follows:
    - Used the newButtons plugin to add an &lt;&lt; define importLeoGlobals &gt;&gt; section.
    - Simplified the import logic using importLeoGlobals function.
    - Commented out the Standalone Operation classes.
    - Called g.createStandAloneApp in the '__name__ == "__main__"' code.</t>
<t tx="ekr.20050429094215.139">- config.openSettingsFile returns None if there is a read error.

- leoFileCommand.open gives no BadLeoFile message if silent is True.</t>
<t tx="ekr.20050429094215.145">- Simplified write_Leo_file using new leoFileCommand.deleteFileWithMessage and g.utils_rename.

- Eliminated outputList var.
    - The code that writes to a clipboard sets self.outputFile to g.fileLikeObject.

- Speeded up put routine: it always writes to self.outputFile.

- self.outputFile is now a cStringIo object.  However, the heart of the put routine is:

    s = g.toEncodedString(s,self.leo_file_encoding,reportErrors=True)
    self.outputFile.write(s)

and it appears that the call to g.toEncodedString is the limiting factor.</t>
<t tx="ekr.20050429094215.173">- Use g.Bunch to simplify code.
- Added 'before' &amp; 'after' methods
- Added entries to optionalIvars dynamically in bead methods.
- Eliminated 'case-itis' by making it unnessesary ever to add more cases.
- Removed 'v' key in undoer:  replaced it with 'p'.
- Replaced u.v by u.p and v by p in find code (It's too confusing).
- p.setDirty and p.setAllAncestorAtFileNodesDirty  return list of nodes that were marked dirty.
- Create new top-level before/after methods &amp; helpers:
- Changed setUndoTypingParams to use new dispatch method.
- Removed makeBeadDict.
- Removed updateSetChangedFlag.
- Added new methods to nullUndoer class.
- Moved undo methods from leoNodes.py to leoUndo.py
- Added dirtyVnodeList param to afterChangeNodeContents.</t>
<t tx="ekr.20050429094215.286"></t>
<t tx="ekr.20050429094215.316">The only changes concern how Leo encodes and decodes items in
t.unknownAttributes and v.unknownAttributes.

Without changing the file format, the only way to tell Leo how to write
attributes is to use naming conventions. When writing attributes, Leo now does
the following:

- Do nothing except apply xml escapes if the attribute name (in
t.unknownAttributes or v.unknownAttributes) starts with str_ and the attribute
is, in fact, a string. If the string is a Unicode string Leo converts the
Unicode string to an encoded string.

- Use the present pickling/hexlifying scheming otherwise. In particular, issue a
warning and ignore the attribute if the attribute can not be pickled. BTW, there
is no need for separate base64 support: hexlifying guarantees that the result is
valid in any xml environment.

Leo now does the reverse when reading.

BTW, plugins could add their own naming conventions in an emergency. Indeed, the
conventions will be confined to code in atFile.putUa and atFile.getUa, so a
plugin would only need to override these two methods.</t>
<t tx="ekr.20050429094215.347">Removed inAtOthers  param from putOpen/CloseNodeSentinel.
Removed inAtAll param from putCloseNodeSentinel.
Removed putCloseSentinel param from putAtAllBody
Removed putCloseSentinel param from putBody

Removed toString param from openFileForWritingHelper
Removed toString param from v.putUnknownAttributes

Note: most(all?) top-level atFile.write methods pass toString to initWriteIvars.</t>
<t tx="ekr.20050429094215.353">Leo stores recent files information as follows.

1. Leo stores recent files info in files called .leoRecentFiles.txt. These will
be a plain text files with one line per recent files entry. An Easter egg: if
the file starts with read-only, read_only, readonly, etc. Leo will never update
the file and will not remember changes to the Recent Files menu.

2. On startup, Leo searches for the .leoRecentFiles.txt files in the user's home
directory, if it exists. Leo looks in Leo's config directory next, but only if
the home directory does not exist, or does not contain a .leoRecentFiles.txt
file. In other words, Leo will use at most one .leoRecentFiles.txt file on
startup.

3. When opening a .leo file, Leo looks for .leoRecentFiles.txt in the directory
containing the file.

4. At no time after installation does Leo create any .leoRecentFiles.txt file.
This will allow users (or their managers) to set policy regarding where to store
this information (if anywhere).

5. Leo writes at most one .leoRecentFiles.txt file when saving a .leo file,
namely the file read in item 3 if it exists, or the file read in item 2
otherwise.

This is a flexible scheme that should meet most needs without having to resolve
thorny questions about exactly where recent files info belongs.</t>
<t tx="ekr.20050429094215.354">@killcolor

- Properly implemented undo/redo Clear Recent Files.

- readSettingsFiles now reads @recentfiles nodes from all settings files.

- Created @settings nodes and @recent-files nodes if they do not exist.</t>
<t tx="ekr.20050429094215.355">@killcolor

You all have convinced me that storing recent files data in .leo files is a dubious idea. My new plan is as follows:

1. Leo will store recent files info in files called .leoRecentFiles.txt.  These will be a plain text files with one line per recent files entry.  These will be local files, so problems concerning directory structure and path specifications should go away.

2.  On startup, Leo will search for the .leoRecentFiles.txt files in the user's home directory, if it exists.  Leo will look in Leo's config directory next, but only if the home directory does not exist, or does not contain a .leoRecentFiles.txt file.  In other words, Leo will use at most one .leoRecentFiles.txt file on startup.

3.  When opening a .leo file, Leo will look for .leoRecentFiles.txt in the directory containing the file.

4.  At no time after installation will Leo create any .leoRecentFiles.txt file.  This will allow users (or their managers) to set policy regarding where to store this information (if anywhere).

5.  Leo will write at most one .leoRecentFiles.txt file when saving a .leo file, namely the file read in item 3 if it exists, or the file read in item 2 otherwise.

6.  Leo will have settings to tell which .leoRecentFiles.txt files may be written.

7. Leo will never create @settings nodes or @recent-files nodes automatically.  Moreover, I shall remove the @recent-files panel from the settings dialog and the corresponding @recent-files code from the config classes.

I believe this will address everyone's concerns without the need for resolving thorny questions about exactly where recent files info belongs.

</t>
<t tx="ekr.20050429095849">- Saved expansion state of @settings trees when the user hits the OK button.

- Added support for UNL's in the status line when the settings dialog is active.

- Debugged @if-platform, @if-gui, @ints &amp; @strings.

- Reloaded settings files when opening the settings dialog.

- Removed support for @recent-files nodes.  This is now handled by .leoRecentFiles.txt files.</t>
<t tx="ekr.20050513141852">Leo 4.3 beta 2                 May 15, 2005

Leo 4.3 beta 2 completes all major features of Leo 4.3 and fixes all bugs
reported since the beta 1 release.

The defining features of Leo 4.3:
---------------------------------
1. Leo now stores options in @settings trees, that is, outlines whose headline
is '@settings'. When opening a .leo file, Leo looks for @settings trees not only
in the outline being opened but also in various leoSettings.leo files.

The key design goal of @settings trees was that Leo's user options must be
infinitely flexible. That goal has been accomplished. Indeed, users can create
arbitrarily complex user options with @settings trees. Leo settings outlines
are, in fact, infinitely more flexible and powerful than any scheme based on
flat text.  Readers of Python's configParser shootout take note!

2. The Settings command temporarily replaces the outline pane with an outline
showing all the @settings trees in effect. The Settings command also replaces
the body pane with a "settings pane". This settings pane allows you to change
the settings selected in the outline pane using standard gui widgets. The
settings pane is dynamically created from nodes in the settings tree; it is as
extensible as the @settings tree itself.

3. Leo now stores recent files information in .leoRecentFiles.txt files.

4. Leo's read/write code in leoAtFile.py has been rewritten to support user-
defined tangling and untangling.  This is a major cleanup of Leo's core.

5. Leo now boasts a wonderful new Plugins Manager plugin. This plugin enables
and disables plugins automatically. You never have to mess with
pluginsManager.txt again! This plugin also tells you everything you need to know
about each plugin. Finally, this plugin also lets you download plugins from
Leo's cvs site! Many thanks to Paul Patterson for this excellent work.

6. You can install third-party extensions in Leo's extensions directory. Leo
will attempt to import such extensions from the extensions directory if normal
imports fail. Leo is distributed with Pmw (Python Mega Widgets), path.py and
sets.py in this directory.</t>
<t tx="ekr.20050513141913.1"></t>
<t tx="ekr.20050513141913.16">http://sourceforge.net/forum/message.php?msg_id=3133917

'Recent' and 'Marked' button now appear in new windows.</t>
<t tx="ekr.20050513141913.17">http://sourceforge.net/forum/message.php?msg_id=3133915

The colorizer now correctly handles the following:
    
\@, \(, \), \{, \}

And also constructs like \documentclass{report}.</t>
<t tx="ekr.20050513141913.22">http://sourceforge.net/forum/message.php?msg_id=3051870</t>
<t tx="ekr.20050513141913.30">http://sourceforge.net/forum/message.php?msg_id=3138608

The nav_buttons plugin was using self.c rather than keywords.get('c') in a hook
handler. The general rule is that hook handlers should do nothing if self.c !-
keywords.get('c').  This was an old bug, arising from the rewrite of the plugin.

I added a warning to that effect in the plugin template.

It would perhaps be better to specify an optional commander in registerHandler
and only call the handler if the commander matches. However, this isn't so easy
or clean to do.I

http://sourceforge.net/forum/forum.php?thread_id=1282631&amp;forum_id=10226
 
The plugin was failing to set the positionList ivar (in the base
tkinterListBoxDialog class). This was a fairly recent blunder: I saw that
positionList wasn't used in the plugin directly, so I 'improved' the code by
using a local var instead of self.positionList. This illustrates a hazard of
using subclassing.</t>
<t tx="ekr.20050513141913.57">This happened when creating a new chapter with chapters.py enabled.</t>
<t tx="ekr.20050513141913.60">http://sourceforge.net/forum/forum.php?thread_id=1281868&amp;forum_id=10226

The fix was to recompute newSel in &lt;&lt; handle backspace with negative tab_width &gt;&gt; in idle_body_key.</t>
<t tx="ekr.20050513141913.82">- The section name lost its indentation.
- The created section had extra indentation.
- Undoing did not remove the inserted section node.

The unit tests now properly test indentation.</t>
<t tx="ekr.20050513141913.91">http://sourceforge.net/forum/message.php?msg_id=3143895

The Edit-&gt;Delete command did nothing when the selected text was in a headline.</t>
<t tx="ekr.20050513141913.97">The following methods changed:

- markAllAtFileNodesDirty
- markAtFileNodesDirty
- markClones
- markHeadline
- markSubheads

I also rewrote the code using explicit positions.</t>
<t tx="ekr.20050513141913.127">http://sourceforge.net/forum/forum.php?thread_id=1281868&amp;forum_id=10226

doStrings now accepts either:

@strings[values]name=value
@strings name[values]=value

Similarly, doInts accepts:

@ints[values]name=value
@ints name[values]=value</t>
<t tx="ekr.20050513141913.140">http://sourceforge.net/forum/message.php?msg_id=3149604

Changed c.hoistStack[-1].current to c.hoistStack[-1].p in c.insertHeadline.</t>
<t tx="ekr.20050513141913.145">http://sourceforge.net/forum/forum.php?thread_id=1281868&amp;forum_id=10226

The code now calls frame.resizePanesToRatio in createFrame in Leo.

Not only does this fix this bug, it honors the following settings:

- initial_horizontal_ratio
- initial_horizontal_secondary_ratio
- initial_vertical_ratio
- initial_vertical_secondary_ratio</t>
<t tx="ekr.20050513141913.149">http://sourceforge.net/forum/message.php?msg_id=3138608

Replaced individual shortcuts widget with a single text widget. This allows the
user to add or delete shortcuts.</t>
<t tx="ekr.20050513141913.187"></t>
<t tx="ekr.20050513141913.188">http://sourceforge.net/forum/message.php?msg_id=3135170</t>
<t tx="ekr.20050513141913.194">For a test of this, see the script in test.leo at:
    
Scripts--&gt;Script to execute @test, @suite or file

Read the documentation in that node before running the script.</t>
<t tx="ekr.20050513141913.197">g.getScript now fully processes all scripts, regardless of where they came from.

- Changed g.getScript:
    - p arg is now required.
    - Removed unused script arg.
    - Added forcePythonSentinels arg (default is True).
    - g.getScript no longer temporarily alters any body text.
        - atFile.writeFromString gets the initial text using the fromString arg.
    - g.getScript now always calls atFile.writeFromString to handle all Leo directives.

- Added forcePythonSentinels to atFile.initWriteIvars and atFile.scanAllDirectives.
    - Default is None, in which case the code sets forcePythonSentinels to the scriptWrite arg.

- Added forcePythonSentinels to atFile.scanAllDirectives.
    - Default is False.

- Created atFile.putAtFirstLines and atFile.putAtLastLines.
    - These replace the corresonding sections in writeOpenFile.
    - It was not actually necessary to define these, but it cleans up the code.

- Created atFile.writeFromString.
    - This handles all the details of simulating a write _from_ a string _to_ a string.

- atFile.initWriteIvars and atFile.openFileForWriting now allow root to be None.
    - This is not used at present: root is always defined.

- Added fromString arg to atFile.writeOpenFile and atFile.putBody.</t>
<t tx="ekr.20050513141913.233">http://sourceforge.net/forum/forum.php?thread_id=1281640&amp;forum_id=10228

The default is ''.  It define_name exists c.executeScript executes the script in an environment containing
__name__ = define_name.</t>
<t tx="ekr.20050523092026">Leo 4.3 final                 May 23, 2005

Leo 4.3 is here after almost five months of work.

The defining features of Leo 4.3:
---------------------------------
1. Leo now stores options in @settings trees, that is, outlines whose headline
is '@settings'. When opening a .leo file, Leo looks for @settings trees not only
in the outline being opened but also in various leoSettings.leo files.

The key design goal of @settings trees was that Leo's user options must be
infinitely flexible. That goal has been accomplished. Indeed, users can create
arbitrarily complex user options with @settings trees. Leo settings outlines
are, in fact, infinitely more flexible and powerful than any scheme based on
flat text.  Readers of Python's configParser shootout take note!

2. The Settings command temporarily replaces the outline pane with an outline
showing all the @settings trees in effect. The Settings command also replaces
the body pane with a "settings pane". This settings pane allows you to change
the settings selected in the outline pane using standard gui widgets. The
settings pane is dynamically created from nodes in the settings tree; it is as
extensible as the @settings tree itself.

3. Leo now stores recent files information in .leoRecentFiles.txt files.

4. Leo's read/write code in leoAtFile.py has been rewritten to support user-
defined tangling and untangling.  This is a major cleanup of Leo's core.

5. Leo now boasts a wonderful new Plugins Manager plugin. This plugin enables
and disables plugins automatically. You never have to mess with
pluginsManager.txt again! This plugin also tells you everything you need to know
about each plugin. Finally, this plugin also lets you download plugins from
Leo's cvs site! Many thanks to Paul Patterson for this excellent work.

6. You can install third-party extensions in Leo's extensions directory. Leo
will attempt to import such extensions from the extensions directory if normal
imports fail. Leo is distributed with Pmw (Python Mega Widgets), path.py and
sets.py in this directory.</t>
<t tx="ekr.20050523092056.1">http://sourceforge.net/forum/message.php?msg_id=3155657

Enabling the Pie Menu plug-in caused Leo to quit when opening .leo files.</t>
<t tx="ekr.20050523092056.4">This fixed a recent bug.
The crash happened if not section text was specified.
Added new checks and new error messages.</t>
<t tx="ekr.20050620144052">Leo 4.3.1                    June 20, 2005

- Added support for Tk resource files.
- Added support for coloring the PL/SQL language.
- All Mark commands are now undoable.
- Improved Resize To Screen command.
- The usual assortment of minor bug fixes.</t>
<t tx="ekr.20050620144052.2"></t>
<t tx="ekr.20050620144052.3">http://sourceforge.net/forum/message.php?msg_id=3166883
By: rogererens

I swear I didn't wait for the release to be the first to report a bug! I just
didn't try this in the alfa/beta versions:

Leo 4.3 final, build  1.262 , May 23, 2005
Python 2.4.1, Tk 8.4.7, win32

Changing
Global settings: C:\Leo\config\leoSettings.leo--&gt;Window options--&gt;@page Options
for new windows--&gt;@ratio initial_horizontal_ratio = 0.3
or any of the other ratios, does not save them to leoSettings.leo. So after
restarting I still have the old settings in use.
</t>
<t tx="ekr.20050620144052.6">http://sourceforge.net/forum/message.php?msg_id=3167166

The fix was to add the following line to the init function:

    global click_registry, coloured_nodes</t>
<t tx="ekr.20050620144052.8">Modifying outlines can invalidate existing positions!  This rarely happens.  At present it affects the atFile.read logic when reading an outline whose initial current position is a clone outside an @thin tree with another clone inside the @thin tree.  So the read logic computes the expected current position before reading all derived files, and this expected current position becomes invalid.

What I did:

1.  Moved &lt;&lt; set current and top positions &gt;&gt; from getVnodes to end of getLeoFile.
This ensures that the outline won't change after computing the position.

2. Unit tests will have to be revised to make sure that only valid positions get used.</t>
<t tx="ekr.20050620144052.48">- Fixed bugs in convertAllBlanks and convertAllTabs.

These must always call afterChangeGroup to match beforeChangeGroup, even if
nothing has changed.

- Added u.getMark and u.rollbackToMark.

These allow unit tests to cut the undo stack back to an initial position in the
tearDown method. This should be done for all tests that use u.undo and u.redo
methods. The bug was probably the result of changing the outline in the tearDown
method.

Both the Reformat Paragraph and Edit Body unit tests now roll back the undo stack.

- Added traces for unexpected conditions in u.undo, u.redo and tree.select.

- Call u.setUndoTypes() in u.setUndoTypingParams when returning early.

- Corrected Edit Body unit tests.

These tests should not call undo/redo when nothing is expected to change. Doing
so may trigger the new 'cant undo' traces in u.undo.

- doTest in leoTest.py now makes copies of both p and p1.

It's not clear that this is needed, it can't hurt, and it may have been important.</t>
<t tx="ekr.20050620144052.112">The problem was that leo.__file__ returns a randomly upper or lower cased drive letter.</t>
<t tx="ekr.20050620144052.114"># The About Leo dialog was not getting focus.</t>
<t tx="ekr.20050620144052.116"></t>
<t tx="ekr.20050620144052.119">http://sourceforge.net/forum/message.php?msg_id=3176499

5) am I missing text in the Settings panels?  the outline shows that certain
nodes have text (e.g., "About keyboard shortcuts" has the blue rectangle), yet
the body pane is empty; heck, even the title suggests that something should
be there...
</t>
<t tx="ekr.20050620144052.154">http://sourceforge.net/forum/message.php?msg_id=3190593

As luck would have it, I need to put an @ character at the beginning of a line
in source code (windows registry file format) and can't figure out how to do
it. 
</t>
<t tx="ekr.20050620144052.166"></t>
<t tx="ekr.20050620144052.182">http://sourceforge.net/forum/message.php?msg_id=3186385

I just tried 4.3-final, and it seems it does not work with Chinese LC_CTYPE:</t>
<t tx="ekr.20050620144052.185">http://sourceforge.net/forum/message.php?msg_id=3175553

When I set default_target_language to plain in 4.2., no words in any body text
is colored. This behavior seems to have changed in 4.3. Is it right, that I
now have to write @nocolor on top of *every* body text to get rid of randomly
colored words?
 
What I did:

- Added entries for target_language to ivarsDic and defaultsDict in leoConfig.py.
- Added @language target_language = Python to leoSettings.leo.
- Convert c.target_language to lowercase in several places.</t>
<t tx="ekr.20050620144052.207"></t>
<t tx="ekr.20050620144052.208">idle_body_key now calls doAutoIndent and convertBlanksToTabs.  The idea is that plugins could override these methods if desired.</t>
<t tx="ekr.20050620144052.210"># I also fixed a bug: the Mark Clones command did not work!</t>
<t tx="ekr.20050620144052.222">Some non-standard distributions don't include the profile and pstats modules.</t>
<t tx="ekr.20050620144052.231">Leo will now look for a file called .leo_xresources in the users home directory.
If found, Leo will pass that file to Tk's option_readfile method for the top
widget. This allows users to set Tk options.</t>
<t tx="ekr.20050620144425"></t>
<t tx="ekr.20050620144602"></t>
<t tx="ekr.20050812090111">import leoPlugins

rst3 = leoPlugins.getPluginModule('rst3')

if rst3:
    controller = rst3.controllers.get(c)
    if controller:
        controller.processTopTree(p)
else:
    rst3 = leoPlugins.loadOnePlugin('rst3',verbose=True)
    if rst3:
        g.es('rst3 loaded')
        rst3.onCreate('tag',{'c':c})
    else:
        # Ask to be removed.
        g.app.scriptDict['removeMe'] = True</t>
<t tx="ekr.20050812123002"></t>
<t tx="ekr.20050812123002.1"></t>
<t tx="ekr.20050812123002.2">Deletes p.v.rst2_http_attributename from all nodes after writing.

Deletes p.v.unknownAttributes if it then becomes empty.</t>
<t tx="ekr.20050812123002.3"></t>
<t tx="ekr.20050812123002.4">@nocolor

If False, add_node_marker and http_support_main  do nothing.  Otherwise add_node_marker does the following:
    
1. add_node_marker writes a string using generate_node_marker.

Generates 'http-node-marker-'+str(number), where number is config.node_counter
(incremented each time add_node_marker is called.

2. Enables the following code in :
@color

    if config.tag == 'open2':
        http_map = self.http_map
    else:
        http_map = {}
        config.anchormap = {}
        # maps v nodes to markers.
        config.node_counter = 0
    # [snip] code to write the tree
    if config.rst2_http_server_support:
        self.http_map = http_map</t>
<t tx="ekr.20050812123002.5"></t>
<t tx="ekr.20050812123002.6">True: call body_filter to massage text.

Removes @ignore, @nocolor, @wrap directives.
</t>
<t tx="ekr.20050812123002.7">Used differently.  See rst2_pure_document.</t>
<t tx="ekr.20050812123002.8"></t>
<t tx="ekr.20050831195449">@nocolor

For instruction about installing Leo see:
http://webpages.charter.net/edreamleo/install.html

For everything a beginner needs to know about Leo see:
http://webpages.charter.net/edreamleo/intro.html

For help installing or using Leo please ask questions at:
http://sourceforge.net/forum/?group_id=3458</t>
<t tx="ekr.20050901054622">c.save()</t>
<t tx="ekr.20050901055150">@color
# Script to promote headlines and body text

root = p.copy()
body = [root.bodyString()+'\n']
for p in root.subtree_iter():
    body.append(p.headString())
    body.append(p.bodyString().rstrip()+'\n')

body = '\n'.join(body)
root.setBodyString(body)
</t>
<t tx="ekr.20050901060119">@color

# Converts text selection to def list.

@others

createDefList(c,p)</t>
<t tx="ekr.20050901061220">def createDefList(c,p):
    
    undoType = 'Create Def List'
    head,lines,tail,oldSel,oldYview = c.getBodyLines()
    if not lines: return
    
    result = ['``%s``\n' % lines[0].strip()]
    
    for line in lines[1:]:
        result.append('    %s' % line.lstrip()+'\n')
    lines = ''.join(result).rstrip()

    c.updateBodyPane(head,lines,tail,undoType,oldSel,oldYview)</t>
<t tx="ekr.20050901121617">@color

# Puts each sentence on a separate line
# Not as useful as I had hoped.  The Reformat Paragraph command is better.

@others

splitSentences(c,p)</t>
<t tx="ekr.20050901121617.1">def splitSentences(c,p):
    
    undoType = 'Split Sentences'
    head,lines,tail,oldSel,oldYview = c.getBodyLines()
    s = p.bodyString()
    if not s.strip(): return
    
    i = 0 ; line = [] ; result = [] ; nl = False
    while i &lt; len(s):
        ch = s[i] ; i += 1 ; ch2 = '.'
        if i &lt; len(s): ch2 = s[i]
        if ch in ('.',';') and ch2 in (' ','\t','\n'):
            line.append(ch)
            r = ''.join(line)+'\n'
            if nl and ch == '.': r = r + '\n'
            result.append(r)
            line = [] ; nl = False
            while i &lt; len(s):
                ch2 = s[i]
                if ch2 == '\n' and ch == '.':
                    nl = True
                if ch2 in (' ','\t','\n'):
                    i += 1
                else:
                    break
        else: line.append(ch)

    result.append(''.join(line)+'\n') # Add the last line.
    result = ''.join(result)
    c.updateBodyPane('',result,'',undoType,oldSel,oldYview)</t>
<t tx="ekr.20050902080416"># Start at the top.
b = c.frame.body.bodyCtrl
b.mark_set('insert','1.0')
b.tag_remove('sel','1.0','end')
b.tag_add('sel','1.0','1.0')
b.update_idletasks()

# Format until the end.
count = 0 # Guard against loops.
while count &lt; 100:
    count += 1
    s = p.bodyString()
    if not s.strip():
        break
    c.reformatParagraph()
    s2 = p.bodyString()
    
    index = b.index('insert')
    if b.compare(index,'&gt;=','end-1c'):
        break</t>
<t tx="ekr.20050906104918">Leo 4.3.2 beta 1                  September 10, 2005

To learn about Leo, see: http://webpages.charter.net/edreamleo/intro.html

The highlights of 4.3.2:
-----------------------

- Improved Leo's documentation:
    - A tutorial introduction to Leo:
      http://webpages.charter.net/edreamleo/intro.html
    - A 5-minute guide to programming with Leo:
      http://webpages.charter.net/edreamleo/intro.html#quick-start-for-programmers

- The new rst3 plugin creates .html and .tex files from reStructuredText
  embedded in Leo files. Any node of the source outline may contain options for
  the rst3 plugin, which makes this plugin much more useful and flexible than
  the previous rst plugins. All of Leo's documentation was created using this
  plugin from sources in LeoDocs.leo. For full documentation for rst3 see:
  http://webpages.charter.net/edreamleo/rstplugin3.html.

- The spellpyx (spell checking) plugin is now much easier to use.

- The vim and openWith plugins now use Python's subprocess module if it is present.
 
- Improved the Pretty Printing command.

- The usual assortment of bug fixes.</t>
<t tx="ekr.20050906104918.1">Here is a summary of the changes:

- General:  All chapters created with rst3 plugin.  This ensures a uniform look.  The source is in LeoDocs.leo.  Removed all references to older versions of Leo, except when discussing old file formats in the Appendices.  Corrected all text so it discusses present version.

- rst3 plugin itself:  Correct bug that caused chapters to be formatted differently when processing multiple @rst trees.  

- rst3 button in LeoDocs.leo:  The script first looks *up* the tree, looking for an @rst node.  If found, it processes just that tree.  If not found, it processes all @rst nodes *below* the originally selected node.  The button is now much more convenient to use.

- Preface: Shorter, no history.  No longer a dead end.

- What People are Saying About Leo: No longer a dead end.

- FAQ: Reorganized, simplified, revised.  Added entries for running Leo in a console window and debugging docutils.  Improved entry for using cvs.

- Chapter 1: Installation: Now the first chapter.  Revised.

- Chapter 2: Tutorial: Completely rewritten.  Like Python's tutorial, this chapter contains everything a beginner needs to understand and use Leo.  The `Quickstart for programmers` section is the heart of this chapter.  All terms used have links either to their definition in the tutorial or in the Glossary.  Newbies should be able to digest this chapter easily.  This chapter should make Leo comprehensible to many more people.

- Chapter 3: Using Outlines: Revised per general remarks above.

- Chapter 4: Writing Programs in Leo.  Completely rewritten.  The old chapter was an embarrassment. The new chapter is a reference guide, properly organized as such.  The introduction warns newbies away.

- Chapter 5: Using Leo's Commands.  'Minor' revisions and corrections create a substantially better result.

- Chapter 6: Leo and literate programming: Reformatting helps.  New words about rST markup and other improvements over traditional LP.

- Chapter 7: Scripting Leo with Python: Rewritten, simplified, updated and corrected.  The sources in LeoDocs.leo are directly executable.  rST sources use literal blocks instead of code-blocks so that the sources are simplified. (Important when executing examples).  Properly discusses positions, including 'supremely important' section on copying positions.

- Chapter 8: Customizing Leo.  Heavily revised.  Discusses leoSettings.leo, not leoConfig.txt.  Security warnings are more reasonable.  Section on script buttons. Rewrote section on uA's (Adding extensible attributes to nodes and .leo files).

- Chapter 9: History of Leo.  Rewritten.  Much shorter and more useful.  Discusses the major milestones, concentrating on explaining the major differences between versions.  Gone are details of how discoveries came to be.  They are in LeoPostings.leo, which will be included in the distribution.

- Chapter 10: Theory of Operation.  Largely rewritten.  Discusses positions properly.  Omits discussion of how clones were implemented before 4.2.

- Chapter 11: White Papers.  A new chapter.  This is a slightly-edited version of writing that had been buried in the appendices.

- Appendices.  Heavily revised and reformatted.  Rewrote sections on file formats.

- Glossary: A separate chapter.  All terms have links to their definition.  All definitions are rST targets so other chapters may refer to them.  Added several new entries.
</t>
<t tx="ekr.20050906104931.1"></t>
<t tx="ekr.20050906104931.15">http://sourceforge.net/forum/message.php?msg_id=3218558</t>
<t tx="ekr.20050906104931.38">The fix was to add an entry of 'unknown' state to state_dict. This fixes the
crash by brute force, but may not be strictly correct. However, this is pretty
much moot: we shall soon be moving to the new colorizer.</t>
<t tx="ekr.20050906104931.42">The code gets c = keywords.get('c') in several places.
The protection is to return if c is None.
This affects the following files: plugins_menu.py, pluginsTest.py, plugin_manager.py</t>
<t tx="ekr.20050906104931.43">http://sourceforge.net/forum/message.php?msg_id=3231597

test.leo had some non-@ignore'd @thin nodes for files not in the distribution.

- Only files used by unit tests should be on cvs and the distribution.
    - test\unittest\batchTest.py and test\unittest\errorTest.py were already on cvs.
    - Added these files to the distribution.

- Other test files should be distributed in @ignore nodes.

- Leo's distribution checklist now has an item to check that the distributed test.leo can be opened without errors.</t>
<t tx="ekr.20050906104931.48"></t>
<t tx="ekr.20050906104931.49">Calling print directly is dangerous: it will fail for unicode characters.</t>
<t tx="ekr.20050906104931.56">The new Pretty Print code has the following improvements:

- Strip trailing blanks in get.
- Many improvement to doOp.
- Improved DoMultiline:
    - Added special case logic to ensure '#' is preceded by space except at start of line.
    - Added blank after multi-line string if needed.
- Added lastName token for special-case handling depending on previous token.
- No change to put, putArray or doName.</t>
<t tx="ekr.20050908164150"></t>
<t tx="ekr.20050908164150.1">See http://webpages.charter.net/edreamleo/rstplugin3.html for full documentation
of this plugin.

The rst3 plugin creates output files from Leo outlines containing
reStructuredText (rST) ReStructuredText is a simple and powerful text formatting
markup language. Outlines are a natural way to organize rST (or any text).

This plugin adds the Write Restructured Text command to Leo's Edit menu. The
Write Restructured Text command searches the selected outline looking for rst
root nodes whose headline have the form @rst &lt;filename&gt;. The plugin then creates
the named file in various ways depending which rst3 options are in effect.

By default, the rst3 plugin creates rST headings automatically from outlines, so
the higher-level nodes in the outline correspond to higher-level sections in the
output. Creating rST headings automatically relieves you from one of the most
tedious chores in creating rST markup.

To use this plugin effectively, Python's docutils module must be installed. The
rst3 plugin will use the SilverCity syntax coloring package if it installed.

This plugin sends .htm, .html or .tex files to the docutils module for further
processing. Docutils generates HTML files or LaTeX files depending on the file's
extension. HTML files generated by docutils refer to three .css (cascading style
sheet) files that should exist in the same directory as the generated HTML file.
You can control the formatting of the HTML file by altering these .css files.</t>
<t tx="ekr.20050908164150.2">This plugin now allows quotes within words, but strips quotes and other cruft
from the beginning and end of words. As a result, using the spellpyx spell
checker is much easier than before.

Leo's extensions folder now contains aspell23.pyd and aspell24.pyd. These are
Python dll's compiled for Python 2.3 and 2.4 respectively. You must rename one
of these files to be aspell.pyd and move aspell.pyd to the aspell folder. For
more details, see the installation nodes in the docstring for the spellpyx
plugin.</t>
<t tx="ekr.20050909082711">- Fixed bug with non-unicode characters in file name

    http://sourceforge.net/forum/message.php?msg_id=3224635
    
    Leo crashed try to read .leo files whose name contained non-ascii characters.

- Fixed bug with non-unicode characters in settings value

    http://sourceforge.net/forum/message.php?msg_id=3222750
    
    Leo crashed try to write settings whose values contained non-ascii characters.

- Fixed bug tangling sections with non-unicode characters.

    http://sourceforge.net/forum/message.php?msg_id=3307318</t>
<t tx="ekr.20050910143326">These plugins now use Python's subprocess module if it is present. The
subprocess module comes standard with Python 2.4. For Linux systems, Leo will
use subprocess.py in Leo's extensions folder if necessary.

For Windows systems you can install Python's subprocess module in Python 2.2 or
2.3 as follows:
    
    - Go to http://www.effbot.org/downloads/#subprocess

    - Download and execute one of the following installers, depending on your version of Python:
        subprocess-0.1-20041012.win32-py2.3.exe 
        subprocess-0.1-20041012.win32-py2.2.exe
        
This installer installs the subprocess sources and also _subprocess.pyd in Python's site-packages folder.
</t>
<t tx="ekr.20050913131848">Leo 4.3.2 final                 September 16, 2005

To learn about Leo, see: http://webpages.charter.net/edreamleo/intro.html

The highlights of 4.3.2:
-----------------------

- Improved Leo's documentation:
    - A tutorial introduction to Leo:
      http://webpages.charter.net/edreamleo/intro.html
    - A 5-minute guide to programming with Leo:
      http://webpages.charter.net/edreamleo/intro.html#quick-start-for-programmers

- The new rst3 plugin creates .html and .tex files from reStructuredText
  embedded in Leo files. Any node of the source outline may contain options for
  the rst3 plugin, which makes this plugin much more useful and flexible than
  the previous rst plugins. All of Leo's documentation was created using this
  plugin from sources in LeoDocs.leo. For full documentation for rst3 see:
  http://webpages.charter.net/edreamleo/rstplugin3.html.

- The spellpyx (spell checking) plugin is now much easier to use.

- The vim and openWith plugins now use Python's subprocess module if it is present.
 
- Improved the Pretty Printing command.

- The usual assortment of bug fixes.</t>
<t tx="ekr.20050917092557">Leo 4.3.3 final                 September 17, 2005

Leo 4.3.3 fixes several bugs reported in Leo 4.3.2 final in the last several days.

To learn about Leo, see: http://webpages.charter.net/edreamleo/intro.html

The highlights of 4.3.3 (and 4.3.2)
-----------------------------------

- Improved Leo's documentation:
    - A tutorial introduction to Leo:
      http://webpages.charter.net/edreamleo/intro.html
    - A 5-minute guide to programming with Leo:
      http://webpages.charter.net/edreamleo/intro.html#quick-start-for-programmers

- The new rst3 plugin creates .html and .tex files from reStructuredText
  embedded in Leo files. Any node of the source outline may contain options for
  the rst3 plugin, which makes this plugin much more useful and flexible than
  the previous rst plugins. All of Leo's documentation was created using this
  plugin from sources in LeoDocs.leo. For full documentation for rst3 see:
  http://webpages.charter.net/edreamleo/rstplugin3.html.

- The spellpyx (spell checking) plugin is now much easier to use.

- The vim and openWith plugins now use Python's subprocess module if it is present.
 
- Improved the Pretty Printing command.

- The usual assortment of bug fixes.</t>
<t tx="ekr.20050917092557.1">Here is a summary of the changes:

- General:  All chapters created with rst3 plugin.  This ensures a uniform look.  The source is in LeoDocs.leo.  Removed all references to older versions of Leo, except when discussing old file formats in the Appendices.  Corrected all text so it discusses present version.

- rst3 plugin itself:  Correct bug that caused chapters to be formatted differently when processing multiple @rst trees.  

- rst3 button in LeoDocs.leo:  The script first looks *up* the tree, looking for an @rst node.  If found, it processes just that tree.  If not found, it processes all @rst nodes *below* the originally selected node.  The button is now much more convenient to use.

- Preface: Shorter, no history.  No longer a dead end.

- What People are Saying About Leo: No longer a dead end.

- FAQ: Reorganized, simplified, revised.  Added entries for running Leo in a console window and debugging docutils.  Improved entry for using cvs.

- Chapter 1: Installation: Now the first chapter.  Revised.

- Chapter 2: Tutorial: Completely rewritten.  Like Python's tutorial, this chapter contains everything a beginner needs to understand and use Leo.  The `Quickstart for programmers` section is the heart of this chapter.  All terms used have links either to their definition in the tutorial or in the Glossary.  Newbies should be able to digest this chapter easily.  This chapter should make Leo comprehensible to many more people.

- Chapter 3: Using Outlines: Revised per general remarks above.

- Chapter 4: Writing Programs in Leo.  Completely rewritten.  The old chapter was an embarrassment. The new chapter is a reference guide, properly organized as such.  The introduction warns newbies away.

- Chapter 5: Using Leo's Commands.  'Minor' revisions and corrections create a substantially better result.

- Chapter 6: Leo and literate programming: Reformatting helps.  New words about rST markup and other improvements over traditional LP.

- Chapter 7: Scripting Leo with Python: Rewritten, simplified, updated and corrected.  The sources in LeoDocs.leo are directly executable.  rST sources use literal blocks instead of code-blocks so that the sources are simplified. (Important when executing examples).  Properly discusses positions, including 'supremely important' section on copying positions.

- Chapter 8: Customizing Leo.  Heavily revised.  Discusses leoSettings.leo, not leoConfig.txt.  Security warnings are more reasonable.  Section on script buttons. Rewrote section on uA's (Adding extensible attributes to nodes and .leo files).

- Chapter 9: History of Leo.  Rewritten.  Much shorter and more useful.  Discusses the major milestones, concentrating on explaining the major differences between versions.  Gone are details of how discoveries came to be.  They are in LeoPostings.leo, which will be included in the distribution.

- Chapter 10: Theory of Operation.  Largely rewritten.  Discusses positions properly.  Omits discussion of how clones were implemented before 4.2.

- Chapter 11: White Papers.  A new chapter.  This is a slightly-edited version of writing that had been buried in the appendices.

- Appendices.  Heavily revised and reformatted.  Rewrote sections on file formats.

- Glossary: A separate chapter.  All terms have links to their definition.  All definitions are rST targets so other chapters may refer to them.  Added several new entries.
</t>
<t tx="ekr.20050917092557.2"></t>
<t tx="ekr.20050917092557.3">- Fixed bug with non-unicode characters in file name

    http://sourceforge.net/forum/message.php?msg_id=3224635
    
    Leo crashed try to read .leo files whose name contained non-ascii characters.

- Fixed bug with non-unicode characters in settings value

    http://sourceforge.net/forum/message.php?msg_id=3222750
    
    Leo crashed try to write settings whose values contained non-ascii characters.

- Fixed bug tangling sections with non-unicode characters.

    http://sourceforge.net/forum/message.php?msg_id=3307318</t>
<t tx="ekr.20050917092557.4">http://sourceforge.net/forum/message.php?msg_id=3218558</t>
<t tx="ekr.20050917092557.5">The fix was to add an entry of 'unknown' state to state_dict. This fixes the
crash by brute force, but may not be strictly correct. However, this is pretty
much moot: we shall soon be moving to the new colorizer.</t>
<t tx="ekr.20050917092557.6">The code gets c = keywords.get('c') in several places.
The protection is to return if c is None.
This affects the following files: plugins_menu.py, pluginsTest.py, plugin_manager.py</t>
<t tx="ekr.20050917092557.7">http://sourceforge.net/forum/message.php?msg_id=3231597

test.leo had some non-@ignore'd @thin nodes for files not in the distribution.

- Only files used by unit tests should be on cvs and the distribution.
    - test\unittest\batchTest.py and test\unittest\errorTest.py were already on cvs.
    - Added these files to the distribution.

- Other test files should be distributed in @ignore nodes.

- Leo's distribution checklist now has an item to check that the distributed test.leo can be opened without errors.</t>
<t tx="ekr.20050917092557.8"></t>
<t tx="ekr.20050917092557.9">See http://webpages.charter.net/edreamleo/rstplugin3.html for full documentation
of this plugin.

The rst3 plugin creates output files from Leo outlines containing
reStructuredText (rST) ReStructuredText is a simple and powerful text formatting
markup language. Outlines are a natural way to organize rST (or any text).

This plugin adds the Write Restructured Text command to Leo's Edit menu. The
Write Restructured Text command searches the selected outline looking for rst
root nodes whose headline have the form @rst &lt;filename&gt;. The plugin then creates
the named file in various ways depending which rst3 options are in effect.

By default, the rst3 plugin creates rST headings automatically from outlines, so
the higher-level nodes in the outline correspond to higher-level sections in the
output. Creating rST headings automatically relieves you from one of the most
tedious chores in creating rST markup.

To use this plugin effectively, Python's docutils module must be installed. The
rst3 plugin will use the SilverCity syntax coloring package if it installed.

This plugin sends .htm, .html or .tex files to the docutils module for further
processing. Docutils generates HTML files or LaTeX files depending on the file's
extension. HTML files generated by docutils refer to three .css (cascading style
sheet) files that should exist in the same directory as the generated HTML file.
You can control the formatting of the HTML file by altering these .css files.</t>
<t tx="ekr.20050917092557.10">This plugin now allows quotes within words, but strips quotes and other cruft
from the beginning and end of words. As a result, using the spellpyx spell
checker is much easier than before.

Leo's extensions folder now contains aspell23.pyd and aspell24.pyd. These are
Python dll's compiled for Python 2.3 and 2.4 respectively. You must rename one
of these files to be aspell.pyd and move aspell.pyd to the aspell folder. For
more details, see the installation nodes in the docstring for the spellpyx
plugin.</t>
<t tx="ekr.20050917092557.11">These plugins now use Python's subprocess module if it is present. The
subprocess module comes standard with Python 2.4. For Linux systems, Leo will
use subprocess.py in Leo's extensions folder if necessary.

For Windows systems you can install Python's subprocess module in Python 2.2 or
2.3 as follows:
    
    - Go to http://www.effbot.org/downloads/#subprocess

    - Download and execute one of the following installers, depending on your version of Python:
        subprocess-0.1-20041012.win32-py2.3.exe 
        subprocess-0.1-20041012.win32-py2.2.exe
        
This installer installs the subprocess sources and also _subprocess.pyd in Python's site-packages folder.
</t>
<t tx="ekr.20050917092557.12"></t>
<t tx="ekr.20050917092557.13">Calling print directly is dangerous: it will fail for unicode characters.</t>
<t tx="ekr.20050917092557.14">The new Pretty Print code has the following improvements:

- Strip trailing blanks in get.
- Many improvement to doOp.
- Improved DoMultiline:
    - Added special case logic to ensure '#' is preceded by space except at start of line.
    - Added blank after multi-line string if needed.
- Added lastName token for special-case handling depending on previous token.
- No change to put, putArray or doName.</t>
<t tx="ekr.20050917105646">- Fixed bug that caused the Open With command to crash if the subprocess module was not installed.

- Fixed problems in the niceNocent and fastGotoNode plugins.</t>
<t tx="ekr.20051028051444">Leo 4.4 alpha 4                                         December 5, 2005

Leo 4.4 a4 introduces the 'Newer World Order' for redrawing the screen,
corrects numerous bugs in the 4.4 code base, and introduces several new features.

You should be able to use this version safely. There are no known serious bugs,
but several minibuffer commands are not ready for primve time. All the major
features of 4.4 are in place.

To learn about Leo, see: http://webpages.charter.net/edreamleo/intro.html

The highlights of Leo 4.4:
----------------------------------
- An Emacs-like mini-buffer: you can now execute any command by typing its long
name. Support for tab completion.

- A tabbed log pane. The Find and Spell Check commands now use tabs instead of
dialogs, making those commands much easier to use. Plugins or scripts can easily
create new tabs. The Completion tab shows possible typing completions.

- Support for almost all commands in the Emacs Cmds menu, including cursor
and screen movement, basic character, word and paragraph manipulation, and
commands to manipulate buffers, the kill ring, regions and rectangles.

- Per-pane key bindings. You can bind shortcuts to multiple commands depending
on which of Leo's panes presently has focus. For example, you can use arrow keys
to move nodes in the outline pane, while retaining their defaults in Leo's body
pane. Per-pane key bindings are essential for mouseless Leo.

- @command nodes create minibuffer commands. You can bind key shortcuts to
@button and @command nodes.

- A rewrite of Leo's keystroke handling. In particular, Leo handles key events
immediately rather than queuing them for idle time.

- Leo recovers from crashes much more reliably than in any prevsios version.

- Leo updates the screen immediately rather than waiting for idle time.
This 'Newer World Order' simplifies the code and improves performance.

Known bugs in Leo 4.4a4
-----------------------
- Several minibuffer commands do not work.  See the release notes for details.

Coming in later releases of Leo 4.4:
------------------------------------
- An auto-complete command that shows class members in the Completion tab.

- More support for mouseless Leo. There will be commands to manipulate all
aspects of Leo using commands, so your fingers will never have to leave the
keyboard.

- Support for Vim and other 'plain-key' input modes.</t>
<t tx="ekr.20051028051444.1">Here are the default bindings relating to the minibuffer. Any of
these may be changed by changing @shortcuts nodes in leoSettings.leo.

Alt-x: Just like Emacs: starts minibuffer. The prompt is 'full-command' Type a
full command name, then hit &lt;Return&gt; to execute the command. Tab completion
works, but not for file names.

Alt-c: Like Emacs Control-C: (Ctrl-C conflicts with XP cut). starts minibuffer.
The prompt is 'quick-command'. This mode is not completed, but stuff like
`Ctrl-C r` and `Ctrl r r` do work.

Alt-u: Like Emacs Ctrl-u: (Ctrl-u conflicts with move-outline-up). Add a repeat
count for later command. Ctrl-u 999 a adds 999 a's, but many features remain
unfinished.

Ctrl-g: Just like Emacs Ctrl-g: Closes the mini-buffer.

The @bool useMinibuffer setting in leoSettings.leo just controls whether the
minibuffer is visible. The minibuffer exists (and you can type into it) even if
it isn't visible! You can use the show-mini-buffer, hide-mini-buffer and
toggle-mini-buffer commands to show or hide the minibuffer.</t>
<t tx="ekr.20051028051444.2">The most important new features of Leo 4.4 have to do with key bindings.

See the children of this node for details.


</t>
<t tx="ekr.20051028051444.4"></t>
<t tx="ekr.20051028051444.5">1. The minibuffer exists regardless of this setting, but will not be shown
   initially if it is False.

2. Hiding the minibuffer does not change any bindings or the operation of Leo in
   any other way. Therefore, if you do hide the minibuffer initially, and never
   want to use it, you should not bind shortcuts to any commands that use the
   minibuffer.

3. You can execute the show-mini-buffer, hide-mini-buffer and toggle-mini-buffer
   commands (or any other minibuffer command!) if the minibuffer is hidden.
   Indeed, the following will work even if the minibuffer is hidden.

       &lt;alt-x&gt;show-mini-buffer&lt;return&gt;</t>
<t tx="ekr.20051028051444.6">This options controls whether Leo creates a Cmds menu.

This menu is not ready yet, though nothing bad happens if this option is True.</t>
<t tx="ekr.20051028051444.7">http://sourceforge.net/forum/message.php?msg_id=3355954

'body_text_selection_background_color'  Default is 'Gray80'
'body_text_selection_foreground_color'  Default is 'white'</t>
<t tx="ekr.20051028051444.8">- The contract-and-go-right command moves to the parent node and collapses the
parent node.

- The goto-first-sibling and goto-last-sibling commands allow rapid movement
through an ouline without collapsing nodes.

- The print-bindings and print-commands show what commands exist and what keys
are bound to them.

- The help command gives a brief quick start introduction to Leo's Emacs-like
features.</t>
<t tx="ekr.20051028051444.9"></t>
<t tx="ekr.20051028051444.10">Leo maintains the following dictionaries.  As usual, k refers to c.keyHandler:

- c.keyHandler.registerCommand can be called from scripts to register new alt-x
  commands. It probably won't work from plugins yet.

New dictionaries and methods make it easier to customize and extend Leo:

- c.commandsDict describes all commands. Keys are full Emacs command names;
values are functions f.

- k.inverseCommandsDict: keys are f.__name__, values are emacs command names.

- k.leoCallbackDict: keys are leoCallback functions, values are called
functions.

- k.bindingsDict: keys are shortcuts, values are g.bunches with the following
    members: func, name, warningGiven, fromMenu.</t>
<t tx="ekr.20051028051444.11">The following helper functions make it easy to discover the binding presently in
effect for a command:

- k.getShortcutForCommandName(self,commandName) returns the shortcut given
  f.__name__.

- k.getShortcutForCommand(self,f) returns the shortcut for f.</t>
<t tx="ekr.20051028051444.12">@nocolor

c.keyHandlerregisterCommand (self,commandName,shortcut,func)

This function make the func available as a minibuffer command, and optionally
binds a shortcut to func. You can wrap any method in a function, so the
restriction to functions is not significant.

Here is an example take from an @button node::

@color

k = c.keyHandler

def f (event):
    g.es_print('Hello',color='purple')

k.registerCommand('print-hello','Alt-Ctrl-Shift-p',f)
k.registerCommand('print-hello2',None,f)</t>
<t tx="ekr.20051028051444.13">The following bugs exist in 4.3 final.</t>
<t tx="ekr.20051028051444.14">This makes it much harder to hang Leo after taking an exception. Leo 4.4a1 is
*much* more robust than Leo 4.3 final in this regard.</t>
<t tx="ekr.20051028051444.15">Added big kludge to menu.createMenuEntries so that f.OnCut/Copy/PasteFromMenu get called
**only** when explicitly selected from the menu (rather than from a shortcut).
This allows the code in cut/copy/paste-text to be different as needed.

Users can override the shortcut by assigning shortcuts to cut/copy/paste-text commands.
The shortcut will appear in the menu, but does **not** get bound to c.frame.menu.

This is an essential step in solving the infamous Control-V problem.
The code appears to work properly on XP.  Not tested other places.

This is the last best hope to solve this problem: the code interacts as little as possible with Tk.</t>
<t tx="ekr.20051028051444.16">http://sourceforge.net/forum/message.php?msg_id=3351985

Leo did not read empty tnodes like &lt;t/&gt; properly.</t>
<t tx="ekr.20051028051444.17"></t>
<t tx="ekr.20051028051444.18">http://sourceforge.net/forum/message.php?msg_id=3376527</t>
<t tx="ekr.20051028051444.19">It now computes the minimum leading whitespace of all non-blank lines. The old
code computed the leading whitespace of the *first* non-blank line. This would
give the wrong results if the first line were indented.</t>
<t tx="ekr.20051028051616"></t>
<t tx="ekr.20051028051616.1"></t>
<t tx="ekr.20051028051616.160">@nocolor

The scripting plugin has been improved as follows:

1. You can bind shortcuts in @button nodes.  Like this:

@button name @key=shortcut

This binds the shortcut to the script in the script button.  The button's name is 'name', but you can see the full headline in the status line when you move the mouse over the button.  This is a clean and simple way of discovering the shortcut.

2. You can create your own minibuffer commands with @command nodes.

A node whose headline has the form:

@command command-name

a new minibuffer command whose name is 'command-name'.

A node whose headline has the form:

@command command-name @key=shortcut

creates new minibuffer command and binds shortcut to it.

3.  The scripting plugin no longer contains the 'bindLate' code-level option.  The scripts for all @button or @command nodes are computed 'dynamically', that is, when the button is pushed or the command is executed from the minibuffer.  This is the most useful way, and the most intuitive.

Previously, scripts for @button nodes were never dynamic, while scripts in @button nodes created by the 'Script button' button were dynamic only if bindLate was True.  You could call this a bug: it was unhelpful, annoying and confusing.

4. The scripting plugin no longer prints an 'end of script' message.  This allows scripts to select tabs in the log pane</t>
<t tx="ekr.20051028051616.172">@color

# Plugins and scripts can easily create new tabs in the log panel.
# Important: you can run any of these examples using the 'Run Script' button.

# To create a tab named "Test" or make it visible if it already exists:
 
c.frame.log.selectTab('Test')

# When first created, a tab contains a text widget.
# To write to this widget, add the tabName argument to g.es:

g.es('Test',color='blue',tabName='Test')

# Plugins and scripts can easily replace the default Text widget with other Tk widgets.
# c.frame.log.tabFrame contains the Tk.Frame that contains all the other widgets of the frame.
# c.frame.log.logCtrl contains the Tk.Text widget that is initially the only widget in this frame.
# So to remove this text widget just do:
    
c.frame.log.logCtrl.pack_forget()

# Now you can pack any other widgets into c.frame.log.tabFrame.

import Tkinter as Tk ; log = c.frame.log
log.selectTab('Test')
log.logCtrl.pack_forget()
f = Tk.Frame(log.tabFrame,bg='red',height='1inch',width='2inch')
f.pack(side='left',expand=0,fill='none')</t>
<t tx="ekr.20051028051616.299">Leo can optionally generate matching brackets depending on the setting:

@bool autocomplete-brackets = TrueOrFalse

If True, Leo will immediately type the corresponding closing bracket whenever
you type a '(', '[' or '{' character. You can use the forward-char command to
move past the closing bracket, and Leo will move past any closing bracket if you
type the closing bracket with the cursor just to the left of a closing bracket.</t>
<t tx="ekr.20051028061322">**Important**: The print-bindings and print-commands commands (new in a1) show
what commands exist and what keys are bound to them.

- The help command tells how to use the minibuffer.

- The show-minibuffer, hide-minibuffer and toggle-mini-buffer commands show and hide the minibuffer.

It *is* possible to execute these command even if the minibuffer isn't presently
visible. For example, typing 

&lt;alt-x&gt;toggle-mini-buffer&lt;return&gt;

should always work.

- The open-find-tab command opens the Find tab. The Find tab replaces the old
Find panel. The Find panel is deprecated.

- The open-spell-tab command opens the Spell-checking tab.

- The show-colors command creates the 'Colors' tab in the log pane. This tab allows you to
experiment with picking fonts.

- The show-fonts command creates the 'Fonts' tab in the log pane. This tab allows you to
experiment with picking colors.</t>
<t tx="ekr.20051101161405">At the bottom of Leo's window you will now see an area labelled the mini-buffer.
You can't type in it directly, you activate the buffer by typing Alt-x or Alt-c.
Typing Alt-x takes you to 'full-command' mode. Type the full name of a command,
followed by a 'return'. 

- To get help, type Alt-x help.
- For a list of commands, type Alt-x print-commands.
- For a list of present key bindings, type Alt-x print-bindings.
- To leave the mini-buffer at any time type Ctrl-g.

Note: you can redefine any of these keys as you wish.

Important: you can execute any of Leo's 'legacy' commands from the mini-buffer.
For example, Alt-x about-leo or Alt-x open-find-dialog. Note: Leo's Find
*dialog* is deprecated. You will find it much more convenient to use Leo's new
Find *tab*. Use the open-find-tab command.

You can use tab-completion in the minibuffer to cycle through the list of
commands that start with what is in the buffer. Typing backspace takes you back
to the what you previously typed (less on character.) The 'Completion' tab shows
all possible completions. This tab appears automatically when you type a tab in
the minibuffer.

The mini-buffer reduces the need for shortcuts dramatically. For example, none
of Leo's import commands need a shortcut because it is easy enough to execute
them from the minibuffer. In particular, executing commands from the minibuffer
is much easier than executing commands by hand from a menu. </t>
<t tx="ekr.20051101161405.1">leoSettings.leo contains one functional @shortcuts node and one disabled
@@shortcuts node. These node contain entries for every command.

You can assign key shortcuts to any command, as discussed in the comments in
that file. You can leave the nodes as they are, use them as base for
modifications, or roll your own. You should define a binding for every function,
even if that binding is 'None'. If you don't, Leo will issue a warning.

Leo now supports per-pane bindings.  Bindings of the form:

command-name ! pane = shortcut

bind the shortcut to the command only withing a single pane. The possible values
for 'pane' are:

pane    affected panes
----    --------------
all     body,log,tree
body    body
log     log
mini    minibuffer
text    body,log
tree    tree</t>
<t tx="ekr.20051101161405.2">The scripting plugin has been improved in two ways:

1. You can specify key bindings in @button nodes as follows:

@button name @key=shortcut

This binds the shortcut to the script in the script button. The button's name is
'name', but you can see the full headline in the status line when you move the
mouse over the button.

2. You can create new minibuffer commands with @command nodes:

@command name @key=shortcut

This creates a new minibuffer command and binds shortcut to it.</t>
<t tx="ekr.20051101161405.3">Abbreviations may not work at present. A new kind of abbreviation is presently
hard coded in add_ekr_altx_commands in leoKeys.py. For example, one ekr-shortcut
is: 'f', which is bound to leo-find-panel. Typing Alt-x f Return executes
leo-find-panel. These may be quicker than Emacs abbreviations, or not.</t>
<t tx="ekr.20051101161949"></t>
<t tx="ekr.20051101162123">These 'hard-coded' bindings are no longer needed and interfere with per-pane bindings.</t>
<t tx="ekr.20051101162123.1">- The open-find-tab command opens the Find tab.

- The open-spell-tab command opens the Spell-checking tab.

The Find and Spell *tabs* replace the corresponding legacy *dialogs*. Using tabs
eliminates previous problems with dialogs obscuring Leo's main window.

Two essential components of the settings dialog now are implemented in the tabbed log:

- The show-colors command creates the 'Colors' tab in the log pane.

- The show-fonts command creates the 'Fonts' tab in the log pane.

These two tabs allow you to pick color or font names without using the @settings dialog.

Important: scripts and plugins can easily create new tabs in the Log pane. See
Chapter 7 of the Users Guide for details.</t>
<t tx="ekr.20051101162947">Leo's core now supports tabs in the log pane.</t>
<t tx="ekr.20051101163145">Leo 4.4a2 contains a large number of code-level improvements--some very
significant. For full details, see the (Projects) section of LeoPy.leo.</t>
<t tx="ekr.20051101163404">The following bugs existed in the 4.4a1 code base and have now been fixed:

- Removed warnings from compare dialog.</t>
<t tx="ekr.20051101182739">- The node::

    @shortcuts traditional Leo shortcuts with important emacs bindings

contains Leo key bindings.

- The settings in @page Spell tab replace the settings in spellpyx.ini.

- You can specify the background of tabs using the following pattern::

    @color log_pane_XXX_tab_background_color = aColor

For example::

    @color log_pane_Find_tab_background_color = #d6c7d3

- The @bool autocomplete-brackets setting controls whether Leo types a matching
closing bracket immediately when you type '(', '[' or '{'.</t>
<t tx="ekr.20051109112610"></t>
<t tx="ekr.20051109112826">@nocolor

The New World Order means that drawing happens immediately, not at idle time.

The Newer World Order means that c.endUpdate is equivalent to c.redraw_now.</t>
<t tx="ekr.20051109112826.217">http://sourceforge.net/forum/message.php?msg_id=3411030

The fix was to add guards so the code does not assume w._name exists for all widgets w.</t>
<t tx="ekr.20051109112826.222">Scripts.leo contains general-purpose scripts.

unitTest.leo contains all of Leo's unit tests.

test.leo is now for recent tests.  Its small size speeds up my workflow.</t>
<t tx="ekr.20051109112826.223">Changed the following plugins:

cleo.py, footprints.py,__wx_gui.py, zodb.py</t>
<t tx="ekr.20051109112826.224">Removed tree.redrawScheduled, tree.updateCount and tree.disableRedraw

Three major complications are gone.</t>
<t tx="ekr.20051109112826.227"></t>
<t tx="ekr.20051109112826.254">http://sourceforge.net/forum/message.php?msg_id=3412644

You can invoke minibuffer commands by name.  For example:

c.executeMinibufferCommand('open-outline')

Note: c.keyHandler.funcReturn contains the value returned from the command. In
many cases, as above, this value is simply 'break'.</t>
<t tx="ekr.20051109112826.257">For now, I just set c.useTextMinibuffer = False,
so Leo uses a Tk.Label rather than a Tk.Text widget.

This will cause less confusion than always having the minibuffer enabled.</t>
<t tx="ekr.20051109112826.265">http://sourceforge.net/forum/message.php?msg_id=3415021

The code now uses the settings in @page Spell tab in leoSettings.leo.</t>
<t tx="ekr.20051109112826.310">@nocolor
http://sourceforge.net/forum/message.php?msg_id=3414639

The entries for Perl and Perlpod are now as follows:

@color

self.language_extension_dict = {
    "perl" : "pl",
    "perlpod" : "pod",
}

self.extension_dict = {
    "pl"    : "perl",
    "pod"   : "perlpod",
}</t>
<t tx="ekr.20051109112826.315">http://sourceforge.net/forum/message.php?msg_id=3418304

Fixed an edge effect when backward searching for a match that occurs at the very
end of body text. In the process I removed an ancient hack.</t>
<t tx="ekr.20051109141223"></t>
<t tx="ekr.20051109141524"></t>
<t tx="ekr.20051109141524.1"></t>
<t tx="ekr.20051109142920">This code should never have existed.  It was used only in the macro plugin.</t>
<t tx="ekr.20051128181229"></t>
<t tx="ekr.20051128181302.147"></t>
<t tx="ekr.20051128181302.148">The plugin can not call bodyWantsFocus.</t>
<t tx="ekr.20051128181302.149">Later may never come in the Newer World Order, so everything must happen immediately.</t>
<t tx="ekr.20051128181302.150">This ensures that the widget is always visible.</t>
<t tx="ekr.20051128181302.151"></t>
<t tx="ekr.20051128181302.156">http://sourceforge.net/forum/message.php?msg_id=3425070

This code was contributed by Roger Erens.

When the Clone Find All checkbox is checked, the Find All command creates a new
root node called Found: &lt;your search pattern&gt;

This node contains clones of the nodes found by the Find All command. It is your
own responsibility to navigate to this new node and to clean it up when it's no
longer needed.</t>
<t tx="ekr.20051128181302.171">The tab now scrolls properly.</t>
<t tx="ekr.20051128181302.183">http://sourceforge.net/forum/message.php?msg_id=3434727

- Added calls to c.frame.body.onBodyChanged in cut/paste handlers.

- Added call to c.selectPosition(c.currentPosition()) in undo/redo.
    This is essential because previous calls to c.selectPosition may have had redraw_flag = False.</t>
<t tx="ekr.20051128181302.192"></t>
<t tx="ekr.20051128181302.193">http://sourceforge.net/forum/message.php?msg_id=3425967

When creating a new Leo outline (no leo file created yet), the Save As command
created the file Test4.leo instead of the expected Test4.3.leo</t>
<t tx="ekr.20051128181302.196"></t>
<t tx="ekr.20051128181302.204">http://sourceforge.net/forum/message.php?msg_id=3427809

Allowed relative path to stylesheets.

http://sourceforge.net/forum/message.php?msg_id=3433717

The rst3 plugin now traverses the tree as was done previously in the @button rst3 nodes.

http://sourceforge.net/forum/message.php?msg_id=3456419

The rst3 plugin now looks up and down the tree for settings doc parts.

The rst3 plugin now supports the default_path option.</t>
<t tx="ekr.20051128181302.208">@nocolor

- The focusIn/Out trace is a great tool.

- doTabCompletion now calls w.update before calling bodyWantsFocus.

- Eliminated w.update from g.app.gui.set_focus.  It is now called only in
those places where it is truly essential, such as in k.doTabCompletion and
wherever else it might be required.

- Pmw.Notebook does a *lot* when it switches panes (e.g., the _layout method)
and potentially any of the things it does could result in focus shifting to
widget. Rather than trying to make sense of it all, Leo will simply call
w.update as necessary to force completion of the Pmw.Notebook work before trying
to set focus.</t>
<t tx="ekr.20051128181302.211"></t>
<t tx="ekr.20051128181302.213">http://sourceforge.net/forum/message.php?msg_id=3440420

Added @string vim_cmd and @string vim_exe settings. The defaults now correspond
to default installations of vim.</t>
<t tx="ekr.20051128181302.214">http://sourceforge.net/forum/message.php?msg_id=3436726

The dialog warns about the extensions folder not containing Pmw. This can happen
when getting files from cvs.</t>
<t tx="ekr.20051128181302.229">http://sourceforge.net/forum/message.php?msg_id=3437089

The new default binding causes focus to move to the body pane when the user hits
&lt;Return&gt; to end editing in a headline.</t>
<t tx="ekr.20051128181302.231">http://sourceforge.net/forum/message.php?msg_id=3442064

This was not, in fact, a problem with the plugins manager plugin.

The bug was in &lt;&lt; put up a dialog requiring a valid id &gt;&gt; in app.setLeoID.
The code set g.app.gui to None after calling g.app.gui.runAskLeoIDDialog the code set!

While I was at it, Leo's core now always inits Pmw when creating Tk.Tk. This
removes the necessity for Plugins to do this.</t>
<t tx="ekr.20051128181302.244">1: Outline not marked dirty during editing

https://sourceforge.net/forum/message.php?msg_id=3447570

2: Inserting a headline didn't save previous edits of headlines</t>
<t tx="ekr.20051128181351"></t>
<t tx="ekr.20051128181651">Leo 4.4a4 completes the transition to the 'Newer World Order'.</t>
<t tx="ekr.20051128181651.1"></t>
<t tx="ekr.20051202072010"></t>
<t tx="ekr.20051205090923.13"></t>
<t tx="ekr.20051205090923.16">http://sourceforge.net/forum/message.php?msg_id=3450435</t>
<t tx="ekr.20051205090923.22">http://sourceforge.net/forum/message.php?msg_id=3389810</t>
<t tx="ekr.20051205091625">- The abbreviation and buffer commands are not ready yet.

- repeat-complex-command does not work.

- Moving the cursor when the 'mark' has been defined does not expand the visibly
selected text.

- Yanking and killing have not been well tested.

- C-u 5 &lt;return&gt; works but is not undone properly. Also, the kill-line command
does not work as in Emacs.

- Many new commands must be generalized to handle the more complex environment
Leo offers. For example, search commands must be told whether to limit the
search a single node, or a node or and its descendants, or the entire outline.
We need a set-variable command that sets a (Python) variable using an
emacs-style variable name.

- The notion of the 'point' must be expanded so it indicates a node as well as
text location.
    
- New commands are needed to support 'mouseless-Leo'. The user must be able to
drive all dialogs from the keyboard, or to get the same effect without using a
dialog at all. Examples: dismiss-top-dialog, scroll-outline-up/down. We also
need commands to change focus and to manage menus. Examples: focus-in-body,
focus-in-tree, etc, activate-edit-menu, etc.</t>
<t tx="ekr.20051219150602">Leo 4.4 alpha 5                                             January 6, 2006

This release completes the last major features of Leo 4.4:

- User-specified key-binding modes.
- Support for multiple key-bindings for individual minibuffer commands.

This will be the last alpha version of Leo 4.4. Beta 1 is coming in about a
week. You should be able to use this version safely; there are no known serious
bugs.

To learn about Leo, see: http://webpages.charter.net/edreamleo/intro.html

The highlights of Leo 4.4:
----------------------------------
- An Emacs-like mini-buffer: you can now execute any command by typing its long
name. Support for tab completion.

- A tabbed log pane. The Find and Spell Check commands now use tabs instead of
dialogs, making those commands much easier to use. Plugins or scripts can easily
create new tabs. The Completion tab shows possible typing completions.

- Support for most commands in the Emacs Cmds menu, including cursor and screen
movement, basic character, word and paragraph manipulation, and commands to
manipulate buffers, the kill ring, regions and rectangles.

- Per-pane key bindings. You can bind shortcuts to multiple commands depending
on which of Leo's panes presently has focus. For example, you can use arrow keys
to move nodes in the outline pane, while retaining their defaults in Leo's body
pane.

- User-specified key-binding modes. This feature makes it possible to emulate all
aspects of Emacs and Vim as far as key bindings are concerned.

- @command nodes create minibuffer commands. You can bind key shortcuts to
@button and @command nodes.

- Leo recovers from crashes much more reliably than in any previous version.

- Leo handles keystrokes and updates the screen immediately rather than waiting
for idle time.</t>
<t tx="ekr.20051219150602.2"></t>
<t tx="ekr.20051219150602.3"></t>
<t tx="ekr.20051219150602.7"></t>
<t tx="ekr.20051219150602.10">http://sourceforge.net/forum/message.php?msg_id=3464874</t>
<t tx="ekr.20051219150602.13">http://sourceforge.net/forum/message.php?msg_id=3466412

New in Leo 4.4: Leo calls the 'headkey1' and 'headkey2' hooks only when the user
completes the editing of a headline, and ch is always '\r', regardless of
platform.

http://sourceforge.net/forum/message.php?msg_id=3462294</t>
<t tx="ekr.20051219150602.28">http://sourceforge.net/forum/message.php?msg_id=3467558

What I did:

- atFile.readError deletes root's entire subtree.
- atFile.read only warns about unvisited node if there is no error.
</t>
<t tx="ekr.20051219150602.75">http://sourceforge.net/forum/message.php?msg_id=3461068

And a recent bug: clicking in the expand/contract box didn't save the headline.</t>
<t tx="ekr.20051219150602.81">The problem was caused by the recent change to g.app.gui.setTextSelection.

The default for the new 'insert' keyword must be sel.end for compatibility with old code.</t>
<t tx="ekr.20051219150602.85">Read @file Nodes and Import Derived File commands no longer create copies of the root node.</t>
<t tx="ekr.20051219150602.100"></t>
<t tx="ekr.20051219150602.101">The provide batch-mode unit testing.</t>
<t tx="ekr.20051219150602.102"></t>
<t tx="ekr.20051219150602.105">Leo now supports the following commands, shown below with their present bindings:

back-char ! text = LtArrow
back-char-extend-selection ! text = Shift-LtArrow
back-paragraph ! text = Alt-braceleft 
back-paragraph-extend-selection ! text = Alt-Shift-braceleft
back-sentence ! text = Alt-a 
back-sentence-extend-selection  = None
back-word ! text = Alt-b  # No conflict   
back-word-extend-selection  ! text = Alt-Shift-b
beginning-of-buffer ! text = Alt-less # Note: same as Alt-Shift-less
beginning-of-buffer-extend-selection  = None
beginning-of-line ! text = Ctrl-a
beginning-of-line-extend-selection = None
exchange-point-mark = None
forward-char ! text = RtArrow
forward-char-extend-selection ! text = Shift-RtArrow
forward-paragraph ! text = Alt-braceright
forward-paragraph-extend-selection ! text = Alt-Shift-braceright
forward-sentence ! text = Alt-e
forward-sentence-extend-selection ! text = Alt-Shift-e
forward-word ! text = Alt-f
forward-word-extend-selection ! text = Alt-Shift-f
next-line ! text = DnArrow
next-line-extend-selection  ! text = Shift-DnArrow
previous-line ! text = Uparrow
previous-line-extend-selection ! text = Shift-UpArrow

The -extend-selection variants move the cursor and also extend the selection
from the insert point in the indicated direction. As usual exchange-point-mark
switches the insert point from one side of the selection to the other: which
side of the selection the insert point is on does make a difference.

I also added three commands that implement so-called 'extend mode':

clear-extend-mode = None
set-extend-mode = None
toggle-extend-mode = None

When extend mode is on (it is off at first), all cursor movement commands listed
above extend the selection. Very handy. Thanks to Brian for this suggestion.

This is the start of mouseless Leo. For the first time all the common Emacs
cursor-movement commands exist. These commands should work in any text widget.</t>
<t tx="ekr.20051219151926">leoSettings.leo now contains a node called:

@@shortcuts traditional Leo bindings

This node contains the 'classic' Leo key bindings that appeared in Leo 4.3. I
have proofed these settings carefully, but some errors may remain. Please report
any errors or any other suggestions for these settings.</t>
<t tx="ekr.20060105182648.376">Leo no longer creates a duplicate root node when importing derived files.

The code is due to LeoUser.</t>
<t tx="ekr.20060105182648.377"></t>
<t tx="ekr.20060105182648.378"></t>
<t tx="ekr.20060105182648.379"></t>
<t tx="ekr.20060105182648.382">The reason for this assert is unclear.</t>
<t tx="ekr.20060105182648.432"></t>
<t tx="ekr.20060105182648.469">This is the end of the ill-fated settings dialog.

Important: you can use the show-colors and show-fonts commands to help set
colors and fonts in leoSettings.leo.</t>
<t tx="ekr.20060111192108">A **dangerous** delete is a deletion of a node so that all the data in the node is deleted *everywhere* in an outline.  The data is gone, to be retrieved only via undo or via backups.  It may not be obvious which deletes are dangerous in an outline containing clones.  Happily, there is a very simple rule of thumb::

    Deleting a non-cloned node is *always* dangerous.
    Deleting a cloned node is *never* dangerous.

We could also consider a delete to be dangerous **if it results in a node being omitted from a derived file.**  This can happen as follows.  Suppose we have the following outline (As usual, A' indicates that A is marked with a clone mark)::

    - @thin spam.py
        - A'
            - B
    - Projects
        - A'
            - B

Now suppose we clone B, and move the clone so the tree looks like this::

    - @thin spam.py
        - A'
            - B'
    - Projects
        - A'
            - B'
        - B'

If (maybe much later), we eliminate B' as a child of A will get::

    - @thin spam.py
        - A'
    - Projects
        - A'
        - B

B has not been destroyed, but B is gone from @thin spam.py! So in this sense deleting a clone node can also be called dangerous.</t>
<t tx="ekr.20060116174906">Leo 4.4 beta 1                                             January 17, 2006

The code is stable; there are no known serious bugs. Some features are
incomplete.

Leo is a text editor, data organizer, project manager and much more. See:
http://webpages.charter.net/edreamleo/intro.html

The highlights of Leo 4.4:
--------------------------
- An Emacs-like mini-buffer: you can now execute any command by typing its long
name, with tab completion.

- Many new commands, including cursor and screen movement, basic character, word
and paragraph manipulation, and commands to manipulate buffers, the kill ring,
regions and rectangles. You can use Leo without using a mouse.

- Flexible key bindings and input modes. You can emulate the operation of Emacs,
Vim, or any other editor.

- A tabbed log pane. The Find and Spell Check commands now use tabs instead of
dialogs, making those commands much easier to use. Plugins or scripts can easily
create new tabs. The Completion tab shows possible typing completions.

- Dozens of other new features and bug fixes since Leo 4.3.3.

Links:
------
Leo:      http://webpages.charter.net/edreamleo/front.html
Home:     http://sourceforge.net/projects/leo/
Download: http://sourceforge.net/project/showfiles.php?group_id=3458
CVS:      http://sourceforge.net/cvs/?group_id=3458
Quotes:   http://webpages.charter.net/edreamleo/testimonials.html</t>
<t tx="ekr.20060116174906.2"></t>
<t tx="ekr.20060116174906.3">A 'backward' delete at the start of a headline deletes the first character.
delete-char did not work in headlines.</t>
<t tx="ekr.20060116174906.63">http://sourceforge.net/forum/message.php?msg_id=3465251</t>
<t tx="ekr.20060116174906.86">http://sourceforge.net/forum/message.php?msg_id=3495741

The plugin now uses sys.getdefaultencoding() to set the encoding.</t>
<t tx="ekr.20060116174906.87">This could have been the source of weird find behavior.</t>
<t tx="ekr.20060116174906.88">The fix was to have x.getSelectedText return '' instead of None.</t>
<t tx="ekr.20060116174906.90">http://sourceforge.net/forum/message.php?msg_id=3510983</t>
<t tx="ekr.20060116174906.97"></t>
<t tx="ekr.20060116174906.100">https://sourceforge.net/forum/message.php?msg_id=3514627

c.endUpdate now restores the previous focus by default.</t>
<t tx="ekr.20060116174906.103"></t>
<t tx="ekr.20060116174906.104">http://sourceforge.net/forum/message.php?msg_id=3514755
</t>
<t tx="ekr.20060116174906.113">http://sourceforge.net/forum/message.php?msg_id=3515341</t>
<t tx="ekr.20060116174906.118">http://sourceforge.net/forum/message.php?msg_id=3509141

Problems with cleo.  Installed patch: http://sourceforge.net/forum/message.php?msg_id=3517080

https://sourceforge.net/forum/message.php?msg_id=3515025

Problems with fastgotonode and and groupOperations.</t>
<t tx="ekr.20060116174906.122">http://sourceforge.net/forum/message.php?msg_id=3518722

To generate HTML file I entered the outline header "@file bbb.xml" under which
I put the following body text:

//////////////// beginning of excerpt
@first &lt;?xml version="1.0" encoding="windows-1250" ?&gt;
@language html
@
comment line
@c
@others
//////////////// end of excerpt

This works OK.
But, if I put a space after the sole @ above "comment line",  save and close
the .leo file and then open it, Leo protests in log pane on the right:

//////////////// beginning of excerpt
----- error reading @file: bbb.xml
Missing open block comment
//////////////// end of excerpt</t>
<t tx="ekr.20060116174906.125">This corrects a problem that shows up as 'Invalid cross-device link' messages on Linux.

http://sourceforge.net/forum/message.php?msg_id=3519803</t>
<t tx="ekr.20060116174906.130">These should be considered bug fixes.

- copyBindingsToWidget now binds keys in priority order. This also simplifies
and clarifies the code.

- Removed k.onTextWidgetKey.  Added a callback that invokes k.masterCommand.</t>
<t tx="ekr.20060116174906.160">Hitting Backspace immediately put the focus in the log. Another backspace put
the focus in the body pane.

The problem was in log.clearTab.  It must do call t.update().</t>
<t tx="ekr.20060116174906.163"></t>
<t tx="ekr.20060116174906.164"></t>
<t tx="ekr.20060116174906.185">extensionHelper resets movePoint any time there is no selection.</t>
<t tx="ekr.20060116174906.187"></t>
<t tx="ekr.20060116174906.194">The fix was to call endUpdate() rather than endUpdate(changed) in onHeadChanged.</t>
<t tx="ekr.20060116174906.195"></t>
<t tx="ekr.20060116174906.198">g.top and the associated g.app.log logic is inherently unreliable.</t>
<t tx="ekr.20060116174906.199">This allows code to determine in a standard way whether a window is in the process of being destroyed.</t>
<t tx="ekr.20060116174906.213">This includes k.masterCommand and all event handlers.
</t>
<t tx="ekr.20060116174906.255">Leo now calls doCommand on all commands, so the 'command' hooks and error
processing always get done.</t>
<t tx="ekr.20060116174906.257"></t>
<t tx="ekr.20060116174906.258"></t>
<t tx="ekr.20060116174906.259">@nocolor</t>
<t tx="ekr.20060116174906.262"></t>
<t tx="ekr.20060116174906.263">http://sourceforge.net/forum/message.php?msg_id=3518792

EKR: The change in focus happened in c.endEditing in at.writeFromString.

I added a new restoreFocus keyword arg to c.endEditing.</t>
<t tx="ekr.20060116174906.267"></t>
<t tx="ekr.20060116174906.272">http://sourceforge.net/forum/message.php?msg_id=3515616

Could we have a visible-line-up and visible-line-down command? (I.e. to move
the cursor up or down by a visible rather than a logical line).  With these
commands, the arrows plugin could be permanently retired!

What I did:

- next-line and prev-line now work as requested.  This obsoletes the arrow plugin.
    - Removed the redundant tree.OnUpKey and tree.OnDownKey
    - Retired the arrows plugin.

- Created the extendHelper method.
    This creates and maintains the moveSpot, moveCol an moveSpotNode ivars,
    and is responsible for extending the selection range.</t>
<t tx="ekr.20060116174906.296">Still to do:

Specify what mode to enter after each command:

- command-name -&gt; mode-name = binding

will specify what mode to enter after each command.
At present, all commands exit to the top-level mode.

- Add @string active-keyset setting?</t>
<t tx="ekr.20060116174906.306"></t>
<t tx="ekr.20060206111508">Leo 4.4 beta 2                                              February 14, 2006

This version fixes dozens of bugs, improves performance and polishes the user
interface. The code is stable; there are no known serious bugs.

Leo is a text editor, data organizer, project manager and much more. See:
http://webpages.charter.net/edreamleo/intro.html

The highlights of Leo 4.4b2:
----------------------------
- Much better 'fit and finishes'.
- New commands that support mouseless Leo.
- Minibuffer search commands provide all features of Leo's legacy search commands.
- User modes are fully functional and you can create special bindings for the minibuffer.
- New master key and click handlers and improved allocation of screen widgets.

Coming in Leo 4.4b3:
--------------------
- A revived chapters plugin.
- Autocompleter Tab.
- Improved incremental searches.

The highlights of Leo 4.4:
--------------------------
- An Emacs-like mini-buffer: you can now execute any command by typing its long
name, with tab completion.

- Many new commands, including cursor and screen movement, basic character, word
and paragraph manipulation, and commands to manipulate buffers, the kill ring,
regions and rectangles. You can use Leo without using a mouse.

- Flexible key bindings and input modes. You can emulate the operation of Emacs,
Vim, or any other editor.

- A tabbed log pane. The Find and Spell Check commands now use tabs instead of
dialogs, making those commands much easier to use. Plugins or scripts can easily
create new tabs. The Completion tab shows possible typing completions.

- Dozens of other new features and bug fixes since Leo 4.3.3.

Links:
------
Leo:      http://webpages.charter.net/edreamleo/front.html
Home:     http://sourceforge.net/projects/leo/
Download: http://sourceforge.net/project/showfiles.php?group_id=3458
CVS:      http://sourceforge.net/cvs/?group_id=3458
Quotes:   http://webpages.charter.net/edreamleo/testimonials.html</t>
<t tx="ekr.20060206111508.2"></t>
<t tx="ekr.20060206111508.3">@nocolor

Must check for c.exists in c.executeScript after executing the script.</t>
<t tx="ekr.20060206111508.4">@nocolor

- keyboard-quit now ends editing.

- print-bindings shows plain keys only in 'ignore' mode.

- Removed k.add_ekr_altx_commands and k.makeHardBindings.

- Added binding to vim plain shortcuts: mode-help = h

- Print the initial mode when first creating a window.
  The change had to be made in g.openWithFileName because of the UNL plugin.

- Improved print-bindings &amp; mode help.

- endMode retains the widget on entry, so e.g., inserting a new node retaings the headline editing state.

@color
</t>
<t tx="ekr.20060206111508.5">@nocolor

- Added initialClickExpandsOrContractsNode settings.  Clicking an node expands or contracts the node if this setting is True.  EKR much prefers False. 

- Selecting a headline should not select text in it.

@color
</t>
<t tx="ekr.20060206111508.14">@nocolor

What I did:
    
- endMode must not change focus.

- modeHelp calls c.endEditing(retainFocus=True)

@color</t>
<t tx="ekr.20060206111508.40"></t>
<t tx="ekr.20060206111508.48">
</t>
<t tx="ekr.20060206111508.49">Traceback (most recent call last):

  File "c:\prog\leoCVS\leo\src\leoCommands.py", line 250, in doCommand
    val = command() # Call legacy command

  File "C:\prog\leoCVS\leo\src\leoTkinterFrame.py", line 1777, in cutText
    oldText = w.get('1.0','end')

AttributeError: Canvas instance has no attribute 'get'</t>
<t tx="ekr.20060206111508.54"></t>
<t tx="ekr.20060206111508.58"></t>
<t tx="ekr.20060206111508.63"></t>
<t tx="ekr.20060206111508.74">Call w.see('insert'), not w.see('insert-5L')</t>
<t tx="ekr.20060206111508.75"></t>
<t tx="ekr.20060206111508.97"></t>
<t tx="ekr.20060206111508.103">The outline jumps around too much when expanding/contracting nodes
</t>
<t tx="ekr.20060206111508.136"># This is required now that scrolling is disabled by default.</t>
<t tx="ekr.20060206111508.547">- Replaced frame.xWantsFocus with c.xWantsFocus.
- Added event arg to all legacy commands.
- Replaced k.tkBindingFromSetting by k.shortcutFromSetting.
- Replaced k.canonicalizeShortcut by k.shortcutFromSetting.
- Replaced k.bindShortcut with bindKey.
- k.makeBindingsFromCommandsDict does not call k.bindKey for mode bindings.
- Call update_idletasks when writing to the log.
- Updated selection point immediately in masterKeyHandler.
  Otherwise, updateStatusLine would be one click behind.</t>
<t tx="ekr.20060206111508.550">@nocolor

This is logically and practically dubious.
True, a screen redraw shouldn't mess with the focus,
but there are the following problems:

1. c.endUpdate can happen anytime, and it could interfere with other efforts to set focus.
2. g.app.get_focus might get the 'wrong' or a 'bad' focus.</t>
<t tx="ekr.20060206111508.553"></t>
<t tx="ekr.20060206111508.596">A *major* improvement to the tree allocation code:

1.  Use p.key() to as keys to tree.visibleText.
 This greatly speeds up tree.findEditWidget

2. Eliminated the brain-dead requirement that previously-allocated widgets must match the position.
   - The allocation code just gets *any* previously allocated widget.
     This eliminates an n**2 search!
   - The ancient problem was that theId refers to the *window* not its Text widget:
     the *window* must be moved to the right spot.

3. recycleWidgets is simpler and a bit faster.

4. destroyWidgets now works: (the bug was not clearing tree.ids).</t>
<t tx="ekr.20060206111600"></t>
<t tx="ekr.20060206111717"></t>
<t tx="ekr.20060206111717.1"></t>
<t tx="ekr.20060206112001">- Improved format of print-commands and print-bindings commands.

- Eliminated clone-find-all, selection-only, show-context checkboxes
  when show_only_find_tab_options setting is True.

- All minibuffer find commands copy the find string from the Find tab into the minibuffer.

- The replace-string command sets up arguments for Tab find. This is different
  from the normal Emacs replace-string command, but it works well in Leo.

- Leo doesn't abort the minibuffer if the command does not exist.
  This is much more convenient.
</t>
<t tx="ekr.20060211104746.2">In the new drawing scheme, tree.redraw_now always calls c.endEditing, which
calls tree.onHeadChanged. The effect of this was to reverse the action of
undo/redoNodeContents.

The solution was to change the edit widget directly before calling
tree.redraw_now. To do this, I created the new tree.setHeadline method.</t>
<t tx="ekr.20060211104746.12">* Found the reason why focus was *still* sticking in the outline pane:
    - The click handlers must return 'break', not continue.
    - However, OnActivateHeadline must return 'continue' when the headline is active
      so that Tk will handle the click properly.

- UNL does not seem to be causing problems.

- No need to save/restore focus in status line.

- Added several new traces to tkTree class.

* tree.redraw_now now ends editing properly. This fixes lots of bugs. In
particular, it avoid any chance that p.edit_widget won't correspond to the
present position.

- k.masterClickHandler calls tree.OnDeactivate() if there is no callback function.
  This solves most headline focus problems, provided that all panes bind clicks to k.masterClickHandler.

- toggle-active-pane now ends editing properly.

- insert-headline now calls c.editPosition after calling c.endUpdate().</t>
<t tx="ekr.20060211104746.162">Backspace in empty body text sometimes moved focus to canvas, and sometimes
improperly drew icon.

Made several fixes to onBodyChanged. There was no test for unchanged text! This
could have created all sorts of problems for undo.</t>
<t tx="ekr.20060211104746.168">@ This revealed several problems:
    
- Most find dialog commands do not actually exist. All find commands except
open-find-dialog actuall refer to the find tab.

- Severl other minor shortcut problems.</t>
<t tx="ekr.20060211104746.177">http://sourceforge.net/forum/message.php?msg_id=3549737

for extend selection,
with binding to arrow keys,
if you switch from up to dn arrow,
the selection restarts again.
this should just change extend direction
while still using the same selection.
</t>
<t tx="ekr.20060211104746.208"></t>
<t tx="ekr.20060211104746.346">select-all-text, move back/forward line/char, start/end-of-line.</t>
<t tx="ekr.20060212102459.4">All minibuffer search commands, with the exception of the isearch (incremental) commands, simply provide a minibuffer interface to Leo's legacy find commands.  This means that all the powerful features of Leo's legacy commands are available to the minibuffer search commands.

Note: all bindings shown are the default bindings for these commands.  You may change any of these bindings using @shortcuts nodes in leoSettings.leo.

Settings

leoSettings.leo now contains several settings related to the Find tab:

- @bool show_only_find_tab_options = True

When True (recommended), the Find tab does not show the 'Find', 'Change', 'Change, Then Find', 'Find All' and 'Change All' buttons.

- @bool minibufferSearchesShowFindTab = True

When True, Leo shows the Find tab when executing most of the commands discussed below.  It's not necessary for it to be visible, but I think it provides good feedback about what search-with-present-options does.  YMMY.  When True, the sequence Control-F, Control-G is one way to show the Find Tab.

Basic find commands

- The open-find-tab command makes the Find tab visible.  The Find tab does **not** need to be visible to execute any search command discussed below.

- The hide-find-tab commands hides the Find tab, but retains all the present settings.

- The search-with-present-options command (Control-F) prompts for a search string.  Typing the &lt;Return&gt; key puts the search string in the Find tab and executes a search based on all the settings in the Find tab.   This command is my 'workhorse' search command.

- The show-search-options command shows the present search options in the status line.  At present, this command also shows the Find tab.

Search again commands

- The find-tab-find command (F3) is the same as the search-with-present-options command, except that it uses the search string in the find-tab.  This is what I use as my default 'search again' command.

- Similarly, the find-tab-find-previous command (F2) repeats the command specified by the Find tab, but in reverse.

- The find-again command a combination of the search-with-present-options and find-tab-find command.  It is the same as the find-tab-find command if a search pattern other than '&lt;find pattern here&gt;' exists in the Find tab.  Otherwise, the find-again is the same as the search-with-present-options command.

Setting find options

- Several minibuffer commands toggle the checkboxes and radio buttons in the Find tab, and thus affect the operation of the search-with-present-options command. Some may want to bind these commands to keys. Others, will prefer to toggle options in a mode.


Here are the commands that toggle checkboxes: toggle-find-ignore-case-option, toggle-find-in-body-option, toggle-find-in-headline-option, toggle-find-mark-changes-option, toggle-find-mark-finds-option, toggle-find-regex-option, toggle-find-reverse-option, toggle-find-word-option, and toggle-find-wrap-around-option.

Here are the commands that set radio buttons: set-find-everywhere, set-find-node-only, and set-find-suboutline-only.

- The enter-find-options-mode (Ctrl-Shift-F) enters a mode in which you may change all checkboxes and radio buttons in the Find tab with plain keys.  As always, you can use the mode-help (Tab) command to see a list of key bindings in effect for the mode.

Search commands that set options as a side effect

The following commands set an option in the Find tab, then work exactly like the search-with-present-options command.

- The search-backward and search-forward commands set the 'Whole Word' checkbox to False.

- The word-search-backward and word-search-forward set the 'Whole Word' checkbox to True.

- The re-search-forward and re-search-backward set the 'Regexp' checkbox to True.

Find all commands

- The find-all command prints all matches in the log pane.

- The clone-find-all command replaces the previous 'Clone Find' checkbox.  It prints all matches in the log pane, and creates a node at the beginning of the outline containing clones of all nodes containing the 'find' string.  Only one clone is made of each node, regardless of how many clones the node has, or of how many matches are found in each node.

Note: the radio buttons in the Find tab (Entire Outline, Suboutline Only and Node only) control how much of the outline is affected by the find-all and clone-find-all commands.

Search and replace commands

The replace-string prompts for a search string.  Type &lt;Return&gt; to end the search string.  The command will then prompt for the replacement string.  Typing a second &lt;Return&gt; key will place both strings in the Find tab and executes a **find** command, that is, the search-with-present-options command.

So the only difference between the replace-string and search-with-present-options commands is that the replace-string command has the side effect of setting 'change' string in the Find tab.  However, this is an extremely useful side effect, because of the following commands...

- The find-tab-change command (Ctrl-=) replaces the selected text with the 'change' text in the Find tab.

- The find-tab-change-then-find (Ctrl--) replaces the selected text with the 'change' text in the Find tab, then executes the find command again.

The find-tab-find, find-tab-change and find-tab-change-then-find commands can simulate any kind of query-replace command.  **Important**: Leo presently has separate query-replace and query-replace-regex commands, but they are buggy and 'under-powered'.  Fixing these commands has low priority.

- The find-tab-change-all command changes all occurrences of the 'find' text with the 'change' text.  Important: the radio buttons in the Find tab (Entire Outline, Suboutline Only and Node only) control how much of the outline is affected by this command.

Incremental search commands

Leo's incremental search commands are completely separate from Leo's legacy search commands.  At present, incremental search commands do not cross node boundaries: they work only in the body text of single node.

Coming in Leo 4.4b3: the incremental commands will maintain a list of previous matches.  This allows for

a) support for backspace and
b) an incremental-search-again command.

Furthermore, this list makes it easy to detect the end of a wrapped incremental search.

Here is the list of incremental find commands: isearch-backward, isearch-backward-regexp, isearch-forward and
isearch-forward-regexp.'''</t>
<t tx="ekr.20060214074035.6">@nocolor
http://sourceforge.net/forum/message.php?msg_id=3549737

\src\leoEditCommands.py:340: 
Warning: 'yield' will become a reserved keyword 

for python2.2 leoEditCommands.py needs
from __future__ import generators

Also changed the following plugins:

at_produce.py
fastGotoNode.py
rst3.py
zodb.py</t>
<t tx="ekr.20060214074035.9">http://sourceforge.net/forum/message.php?msg_id=3549737

The fix was to call getBool rather than getString.</t>
<t tx="ekr.20060214074035.12">http://sourceforge.net/forum/message.php?msg_id=3237845

On startup, it asked me for a unique id, "possibly your CVS username".
As a non-windows-user, that made no sense at all to me - at very least, it should
fill in os.getenv("USER") as a default, because it's right on non-windows systems,
isn't it?  (If it isn't, there's no explanation at that point that would tell
me otherwise, that's the value I used anyway...)  Just an out-of-box-experience
issue.</t>
<t tx="ekr.20060214074035.20">http://sourceforge.net/forum/message.php?msg_id=3534349
By: edcdave

Saving the Leo file is not sufficient - I have to exit the document and open
it again before the rst destination directory is set correctly.

The fix was to set c.frame.openDirectory in save.</t>
<t tx="ekr.20060214074035.41">The problem: event.widget is the minibuffer.  It must be the body text.

- k.fullCommand saves the initial event and passes it on to callAltXFunction.

- There was a bug in c.masterFocusHandler.  The correct test for 'no change' is:

    if c.hasFocusWidget and c.requestedFocusWidget == c.hasFocusWidget:

** Important: the 'extra' calls to set_focus are correct. The minibuffer messes
with the tab pane, and so we *must* be careful to yank the focus back to the
body.</t>
<t tx="ekr.20060214074035.65">http://sourceforge.net/forum/message.php?msg_id=3538274

It's not clear that there were serious problems with the plugin, but I improved the code and error messages.  All features work for me.

Several plugins use the icon-double-click hook.  The reported problems could have been due to plugin conflicts.
</t>
<t tx="ekr.20060214074035.66">http://sourceforge.net/forum/message.php?msg_id=3517080

Patch for CLeo to allow check-marks:
-----------------------------------------------------
Line 412 in def draw_arrow:
replace 
............canvas.create_line(v.iconx-10,v.icony+7,v.iconx+5,v.icony+7,fill
= 'Gray50',width=1)

with
............#@........&lt;&lt; Blank Check &gt;&gt;
............#@+node:rjries.20060113114142:&lt;&lt; Blank Check &gt;&gt;
............#@&lt;&lt; Point Setter &gt;&gt;
............#@+node:rjries.20060113114350:&lt;&lt; Point Setter &gt;&gt;
............# Define the 3 points of a check mark to allow quick adjustment
............XpointA = v.iconx  -15+3
............YpointA = v.icony  +8-2
............XpointB = v.iconx  -7
............YpointB = v.icony  +13
............XpointC = v.iconx  +5
............YpointC = v.icony  -2
............#@nonl
............#@-node:rjries.20060113114350:&lt;&lt; Point Setter &gt;&gt;
............#@nl
............# "white-out" the check mark
............canvas.create_line(XpointA, YpointA, XpointB, YpointB,
fill=colour,width=2)
............canvas.create_line(XpointB, YpointB, XpointC, YpointC,
fill=colour,width=2)
............#@nonl
............#@-node:rjries.20060113114142:&lt;&lt; Blank Check &gt;&gt;
............#@nl
............# restore line 
............canvas.create_line(v.iconx-12,v.icony+7,v.iconx+6,v.icony+7,fill
= 'Gray50',width=1)

-----------------------------------------------------
Line 421-422 in def draw_tick (**not draw_arrow):
replace 
........canvas.create_line(v.iconx+13-5,v.icony+8,v.iconx+13,v.icony+13,fill=colour,width=2)
........canvas.create_line(v.iconx+13,v.icony+13,v.iconx+13+12,v.icony-2,fill=colour,width=2)

with

........#@....&lt;&lt; Point Setter &gt;&gt;
........#@+node:rjries.20060113114350:&lt;&lt; Point Setter &gt;&gt;
........# Define the 3 points of a check mark to allow quick adjustment
........XpointA = v.iconx  -15+3
........YpointA = v.icony  +8-2
........XpointB = v.iconx  -7
........YpointB = v.icony  +13
........XpointC = v.iconx  +5
........YpointC = v.icony  -2
........#@nonl
........#@-node:rjries.20060113114350:&lt;&lt; Point Setter &gt;&gt;
........#@nl
........# draw the check-mark
........canvas.create_line(XpointA, YpointA, XpointB, YpointB,
fill=colour,width=2)
........canvas.create_line(XpointB, YpointB, XpointC, YpointC,
fill=colour,width=2)

-----------------------------------------------------
Line 598 in def priority_menu
replace
............# (self.donePriority,'Done'),
with
............(self.donePriority,'Done'),
</t>
<t tx="ekr.20060214074035.67">http://sourceforge.net/forum/message.php?msg_id=3571431
By: ktenney

To reiterate a request:

When doing File-&gt;Open the default directory should the directory which
was navigated to for previous 'Open'

What I did:

- Defined g.app.globalOpenDir # The directory last used to open a file.</t>
<t tx="ekr.20060214074035.101"></t>
<t tx="ekr.20060214083647">New settings:

- @int max_undo_stack_size
- @bool minibufferSearchesShowFindTab
- @bool show_only_find_tab_options

New debugging settings:

@bool allow_idle_time_hook
@bool gc_before_redraw
@bool show_tree_stats
@bool trace_bindings
@bool trace_doCommand
@bool trace_f.set_focus
@bool trace_focus = False
@bool trace_g.app.gui.set_focus
@bool trace_gc
@bool trace_gc_calls
@bool trace_gc_verbose
@bool trace_masterClickHandler
@bool trace_masterCommand
@bool trace_masterFocusHandler
@bool trace_masterKeyHandler
@bool trace_modes
@bool trace_redraw_now
@bool trace_select
@bool trace_tree
@bool trace_tree_alloc
@bool trace_tree_edit
@bool use_syntax_coloring
@string trace_bindings_filter
@string trace_bindings_pane_filter</t>
<t tx="ekr.20060214083808">Debugging commands:

- dump-all-objects, ump-new-objects, verbose-dump-objects.
- free-text-widgets.

Find commands:

See the child of this node for details.

- find-again.
- find-all and clone-find-all.
- find-tab-find command, find-tab-find-previous.
- find-tab-change, find-tab-change-all, find-tab-change-then-find.
- hide-find-tab, open-find-tab.
- re-search-forward and re-search-backward.
- replace-string.
- search-with-present-options.
- search-backward and search-forward.
- show-search-options.
- word-search-backward and word-search-forward.

Search options:

- set-find-everywhere, set-find-node-only, and set-find-suboutline-only.
- toggle-find-ignore-case-option, toggle-find-in-body-option,
  toggle-find-in-headline-option, toggle-find-mark-changes-option,
  toggle-find-mark-finds-option, toggle-find-regex-option,
  toggle-find-reverse-option, toggle-find-word-option, 
  toggle-find-wrap-around-option.

Mouseless Leo:

- activate-cmds-menu, activate-edit-menu, activate-file-menu activate-help-menu,
  activate-outline-menu, activate-plugins-menu, activate-window-menu.
- contract-body-pane, contract-log-pane, contract-outline-pane, contract-pane.
- expand-body-pane, expand-log-pane, expand-outline-pane, expand-pane.
- fully-expand-body-pane, fully-expand-log-pane, fully-expand-outline-pane, fully-expand-pane.
- hide-body-pane, hide-log-pane, hide-outline-pane, hide-pane.
- click-click-box, click-headline, click-icon-box, double-click-headline,
  double-click-icon-box, simulate-begin-drag, simulate-end-drag.
  (These commands trigger event hooks. In particular, double-click-icon-box will
  invoke the vim or xemacs plugins if they are enabled.)</t>
<t tx="ekr.20060214085054">The problem with focus 'sticking' in the Pmw.Notebook was due to a call to
bringToFront. Apparently, the side effect was to assign a focus to the widget
that had it previously. This makes sense, and can not be considered a Tk bug.

Remove almost all calls to w.update in Leo.

No more calls to w.after that were used to draw the status line. The master key
and click handlers now call the label update method directly. This may ease a
major stress on Tk.</t>
<t tx="ekr.20060214090742"></t>
<t tx="ekr.20060214092741">- @mode nodes in leoSettings.leo allow you to specify input modes with separate key bindings.

See the child of this node for full details.

- All key bindings specified with !mini pane specifier apply to all modes.

</t>
<t tx="ekr.20060215112429">Leo 4.4 experimental 1                                      February 15, 2006

This version is an emergency measure.  It's goals:

1.  To fix some of the key-handling issues in Leo 4.4 b2.
2.  To allow further experimentation with key handling.
3.  To allow easy reporting of any other key handling problems.

Please do not use this version (or Leo 4.4b2) unless you are ready to report bugs.

My apologies for the key handling problems in Leo 4.4 b2.  I hope this version will
be all that is necessary to fix those problems.

Here are the details of the key-handling changes:

- Added support for trace_key_event setting.
- Added support for ignore_caps_lock setting.
- Added Caps_Lock and Num_Lock to k.tkNamesList and in the list of
  special keys in k.masterCommand and k.masterKeyHandlerHelper.
- Added support for k.ignore_unbound_non_ascii_keys logic in masterKeyHandlerHelper.
- Disabled unknown keysym trace in k.strokeFromEvent.
- Enabled the international keyboard on XP as an aid to testing.
- Added support for swap_mac_keys setting in k.shortcutFromSetting.</t>
<t tx="ekr.20060215112429.2">extract                             = Shift-Ctrl-D
extract-names                       = Shift-Ctrl-N
extract-section                     = Shift-Ctrl-S  # Shift-Ctrl-E: end-of-line-extend-selection

write-at-file-nodes                 = Shift-Ctrl-W # Was enter-file-mode.
write-dirty-at-file-nodes           = Shift+Ctrl+Q

# Removed definitions of find and file modes.  I never used them.</t>
<t tx="ekr.20060215112429.3">http://sourceforge.net/forum/message.php?msg_id=3545403</t>
<t tx="ekr.20060215112429.6">The patch was reported at:

http://sourceforge.net/forum/message.php?msg_id=3577681

Thanks to caugm.</t>
<t tx="ekr.20060215112429.9">http://sourceforge.net/forum/message.php?msg_id=3573470

What I did:

- Added support for trace_key_event setting.
- Added support for ignore_caps_lock setting.
- Added Caps_Lock and Num_Lock to k.tkNamesList and in the list of
  special keys in k.masterCommand and k.masterKeyHandlerHelper.
- Added support for k.ignore_unbound_non_ascii_keys logic in masterKeyHandlerHelper.
- Disabled unknown keysym trace in k.strokeFromEvent.
- Enabled the international keyboard on XP as an aid to testing.
- Added support for swap_mac_keys setting in k.shortcutFromSetting.</t>
<t tx="ekr.20060217071505">Leo 4.4 alpha 6                                         February 17, 2006

Leo 4.4 b2 was broken on some platforms.  Leo 4.4 a6 should fix those problems
forever.  However, only wider distribution will verify that for certain.

Besides fixing the fatal problems with Leo 4.4b2, this version fixes two minor bugs
and adds some new settings in leoSettings.leo.

Leo is a text editor, data organizer, project manager and much more. See:
http://webpages.charter.net/edreamleo/intro.html

The highlights of Leo 4.4 b2 and a6:
----------------------------
- Smoother user interface.
- New commands that support mouseless Leo.
- Minibuffer search commands provide all features of Leo's legacy search commands.
- User modes are fully functional; you can create special bindings for the minibuffer.
- New master key and click handlers and improved allocation of screen widgets.

Coming in Leo 4.4b3:
--------------------
- A revived chapters plugin.
- Autocompleter Tab.
- Improved incremental searches.

The highlights of Leo 4.4:
--------------------------
- An Emacs-like mini-buffer: you can now execute any command by typing its long
name, with tab completion.

- Many new commands, including cursor and screen movement, basic character, word
and paragraph manipulation, and commands to manipulate buffers, the kill ring,
regions and rectangles. You can use Leo without using a mouse.

- Flexible key bindings and input modes. You can emulate the operation of Emacs,
Vim, or any other editor.

- A tabbed log pane. The Find and Spell Check commands now use tabs instead of
dialogs, making those commands much easier to use. Plugins or scripts can easily
create new tabs. The Completion tab shows possible typing completions.

- Dozens of other new features and bug fixes since Leo 4.3.3.

Links:
------
Leo:      http://webpages.charter.net/edreamleo/front.html
Home:     http://sourceforge.net/projects/leo/
Download: http://sourceforge.net/project/showfiles.php?group_id=3458
CVS:      http://sourceforge.net/cvs/?group_id=3458
Quotes:   http://webpages.charter.net/edreamleo/testimonials.html</t>
<t tx="ekr.20060217071505.1">The new scheme binds to keystrokes, not commands.  This should be as portable
and robust as all previous versions (except b2, which was broken).

- Created k.completeAllBindings, called last in k.makeAllBindings. This binds
all keystrokes in k.bindingsDict to k.masterKeyHandler with an optional stroke
argument. This allows k.masterKeyhandler to dispense with the problematic call
to k.strokeFromEvent. This is all that is really required. 

- Added code to menu.createMenuEntries that clears the accelerator on MacOS for
any key that isn't a control, alt or command key. This solves the recurring
problems with the Return key. The only effect is that the menu won't mention a
binding that is actually in effect, but apparently that cannot be helped.

- Added g.safeCompareStrings, which may, or may not, fix the crasher when
comparing k.abortAllModesKey to the incoming keystroke in k.masterKeyHandler.
It's a bit tricky to test.

- The ignore_caps_lock is no longer functional. Sigh. This depends on knowing
the Caps_Lock bit in key events. I may put this back later, but I can't delay a6
even a minute for this.</t>
<t tx="ekr.20060217072324">- Fixed crasher in k.masterCommand.

- Arrow keys no longer destroy UNL line
</t>
<t tx="ekr.20060217072647">- @bool trace_autocompleter # The autocompleter itself is not ready yet.
- @bool trace_key_event
- @bool trace_minibuffer
- @bool trace_status_line</t>
<t tx="ekr.20060227102028">Leo 4.4 alpha 7                                             February 28, 2006

This version fixes some minor problems with Leo 4.4a6 and adds autocompletion
and calltips.

Leo is a text editor, data organizer, project manager and much more. See:
http://webpages.charter.net/edreamleo/intro.html

The highlights of Leo 4.4:
--------------------------
- An Emacs-like mini-buffer: you can now execute any command by typing its long
name, with tab completion.

- Many new commands, including cursor and screen movement, basic character, word
and paragraph manipulation, and commands to manipulate buffers, the kill ring,
regions and rectangles. You can use Leo without using a mouse.

- Flexible key bindings and input modes. You can emulate the operation of Emacs,
Vim, or any other editor.

- A tabbed log pane. The Find and Spell Check commands now use tabs instead of
dialogs, making those commands much easier to use. Plugins or scripts can easily
create new tabs. The Completion tab shows possible typing completions.

- Autocompletion and calltips.  Autocompletion works much like tab completion.

- Dozens of other new features and bug fixes since Leo 4.3.3.

Links:
------
Leo:      http://webpages.charter.net/edreamleo/front.html
Home:     http://sourceforge.net/projects/leo/
Download: http://sourceforge.net/project/showfiles.php?group_id=3458
CVS:      http://sourceforge.net/cvs/?group_id=3458
Quotes:   http://webpages.charter.net/edreamleo/testimonials.html</t>
<t tx="ekr.20060227102028.2"></t>
<t tx="ekr.20060227102028.3"># http://sourceforge.net/forum/message.php?msg_id=3583335
</t>
<t tx="ekr.20060227102028.14">@nocolor

http://sourceforge.net/forum/message.php?msg_id=3586962
By: bwmulder

the open-find-dialog is broken. 
 
Error: 4 
TypeError Exception in Tk callback 
Function: &lt;function findButtonCallback at 0x04E219F0&gt; (type: &lt;type 'function'&gt;) 
Args: () 
Traceback (innermost last): 
File "C:\Python24\lib\site-packages\Pmw\Pmw_1_2\lib\PmwBase.py", line 1747, in __call__ 
return apply(self.func, args) 
TypeError: findButtonCallback() takes at least 1 argument (0 given) 
</t>
<t tx="ekr.20060227102028.15"></t>
<t tx="ekr.20060227102028.16"># This was causing problems.  It may be an easy fix, but I kinda doubt it.</t>
<t tx="ekr.20060227102028.17">
</t>
<t tx="ekr.20060227102028.18">@nocolor

http://sourceforge.net/forum/message.php?msg_id=3597694
By: tfer

Template Plug-in (maybe others tooo) co,plain when activated:
exception executing command
Traceback (most recent call last):
  File "leoCommands.py", line 265, in doCommand
    val = command(event)
  File "c:\Leo_Cvs\Leo\plugins\plugins_menu.py", line 350, in about
    PluginAbout(self.name, self.version, self.doc)
  File "c:\Leo_Cvs\Leo\plugins\plugins_menu.py", line 576, in __init__
    g.app.dialogs += 1
AttributeError: LeoApp instance has no attribute 'dialogs'</t>
<t tx="ekr.20060227102028.111">Typing a period when @language python is in effect starts autocompletion. Typing
'(' during autocompletion shows the calltip. Typing Return or Control-g
(keyboard-quit) exits autocompletion or calltips.

Autocompletion

Autocompletion shows what may follow a period in code. (Actually you can specify
any character using the auto-complete shortcut setting.) For example, after
typing g. Leo will show a list of all the global functions in leoGlobals.py.
Autocompletion works much like tab completion in the minibuffer. Unlike the
minibuffer, the presently selected completion appears directly in the body
pane.

A leading period brings up 'Autocomplete Modules'. (The period goes away.) You
can also get any module by typing its name. If more than 25 items would appear
in the Autocompleter tab, Leo shows only the valid starting characters. At this
point, typing an exclamation mark shows the complete list. Thereafter, typing
further exclamation marks toggles between full and abbreviated modes.

If x is a list 'x.!' shows all its elements, and if x is a Python dictionary,
'x.!' shows x.keys(). For example, 'sys.modules.!' Again, further exclamation
marks toggles between full and abbreviated modes.

During autocompletion, typing a question mark shows the docstring for the
object. For example: 'g.app?' shows the docstring for g.app. This doesn't work
(yet) directly for Python globals, but '__builtin__.f?' does. Example:
'__builtin__.pow?' shows the docstring for pow.

Autocompletion works in the Find tab; you can use &lt;Tab&gt; to cycle through the
choices. The 'Completion' tab appears while you are doing this; the Find tab
reappears once the completion is finished.

Calltips

Calltips appear after you type an open parenthesis in code. Calltips shows the
expected arguments to a function or method. Calltips work for any Python
function or method, including Python's global function. Examples:

a)  'g.toUnicode('  gives 'g.toUnicode(s, encoding, reportErrors=False'
b) 'c.widgetWantsFocusNow' gives 'c.widgetWantsFocusNow(w'
c) 'reduce(' gives 'reduce(function, sequence[, initial]) -&gt; value'

The calltips appear directly in the text and the argument list is highlighted so
you can just type to replace it. The calltips appear also in the status line for
reference after you have started to replace the args.

Options

Both autocompletion and calltips are initially enabled or disabled by the
enable_autocompleter and enable_calltips settings in leoSettings.leo. You may
enable or disable these features at any time with these commands:
enable-auto-completer-command, enable-calltips-command,
disable-auto-completer-command and disable-calltips-command.</t>
<t tx="ekr.20060328171518">Leo 4.4 beta 3                                             April 14, 2006

This version fixes some minor problems and adds various features.  This code
has been in use for several weeks without any major problems reported.

Leo is a text editor, data organizer, project manager and much more. See:
http://webpages.charter.net/edreamleo/intro.html

The highlights of Leo 4.4:
--------------------------
- An Emacs-like mini-buffer: you can now execute any command by typing its long
name, with tab completion.

- Many new commands, including cursor and screen movement, basic character, word
and paragraph manipulation, and commands to manipulate buffers, the kill ring,
regions and rectangles. You can use Leo without using a mouse.

- Flexible key bindings and input modes. You can emulate the operation of Emacs,
Vim, or any other editor.

- A tabbed log pane. The Find and Spell Check commands now use tabs instead of
dialogs, making those commands much easier to use. Plugins or scripts can easily
create new tabs. The Completion tab shows possible typing completions.

- Autocompletion and calltips.  Autocompletion works much like tab completion.

- Dozens of other new features and bug fixes since Leo 4.3.3.

Links:
------
Leo:      http://webpages.charter.net/edreamleo/front.html
Home:     http://sourceforge.net/projects/leo/
Download: http://sourceforge.net/project/showfiles.php?group_id=3458
CVS:      http://sourceforge.net/cvs/?group_id=3458
Quotes:   http://webpages.charter.net/edreamleo/testimonials.html</t>
<t tx="ekr.20060328171518.1"></t>
<t tx="ekr.20060328171518.10">http://sourceforge.net/forum/message.php?msg_id=3608246

Added the following commands:

scroll-outline-down-line       
scroll-outline-down-page       
scroll-outline-up-line       
scroll-outline-up-page</t>
<t tx="ekr.20060328171518.11">It now properly creates bindings.</t>
<t tx="ekr.20060328171518.15"></t>
<t tx="ekr.20060328171518.16">http://sourceforge.net/forum/message.php?msg_id=3572598</t>
<t tx="ekr.20060328171518.45">This is equivalent to the Unit Test script button in unitTest.leo</t>
<t tx="ekr.20060328171518.47"></t>
<t tx="ekr.20060328171518.48">http://sourceforge.net/forum/message.php?msg_id=3619340

Just tried out CVS today, and on Linux left/right and L/R in outline mode
(Ctrl-Shift-O) seem to do nothing, whereas they should expand/contract parent
nodes.</t>
<t tx="ekr.20060328171518.57">http://sourceforge.net/forum/message.php?msg_id=3639193

The dirty bits were not updated properly in several undo/redo operations.</t>
<t tx="ekr.20060328171518.83">http://sourceforge.net/forum/message.php?msg_id=3642892

The present code is probably the best compromise between strict accuracy and marking too many nodes dirty.</t>
<t tx="ekr.20060328171518.85">http://sourceforge.net/forum/message.php?msg_id=3606515

Added insert-newline command and fixed some related commands.</t>
<t tx="ekr.20060328171518.101">Apparently g.app.unitTesting isn't set properly for the new-window test.</t>
<t tx="ekr.20060328171518.108">The bug: Hit control-f, then select the text that doesn't have focus.</t>
<t tx="ekr.20060328171518.111">http://sourceforge.net/forum/message.php?msg_id=3641107

ConfigSettings.initEncoding now uses the g.app.config settings if no other settings are available.

In particular, this causes at.encoding to be inited to a reasonable value.</t>
<t tx="ekr.20060328171518.119">- onBodyChanged now converts everything to unicode, either directly or by calling g.app.gui.getAllText.

- Replaced all calls to g.safeStringCompare by g.app.gui.getAllText which calls g.toUnicode.

- Converted all shortcuts to unicode in shortcutFromSetting (a.k.a strokeFromSetting)

- Removed g.safeStringCompare.  This function was a bad idea.

Important: Leo is supposed to convert all characters to unicode, so there should
never be a need for safeStringCompare. The proper way to avoid UnicodeError's is
to call g.toUnicode(s,g.app.tkEncoding).</t>
<t tx="ekr.20060328171518.135">http://sourceforge.net/forum/message.php?msg_id=3607355</t>
<t tx="ekr.20060328171518.151"></t>
<t tx="ekr.20060328171518.152">http://sourceforge.net/forum/message.php?msg_id=3573148

c.openWith now dcalls g.enableIdleTimeHook</t>
<t tx="ekr.20060328171518.169">These commands now set g.app.globalOpenDir.</t>
<t tx="ekr.20060328171518.190">http://sourceforge.net/forum/message.php?msg_id=3585710</t>
<t tx="ekr.20060328171518.191"></t>
<t tx="ekr.20060328171518.238">http://sourceforge.net/forum/message.php?msg_id=3637393

I'm trying to set up a default stylesheet for a project and want this to be
held relative to the project directory (where the .leo file is). The default
is to place it in the same directory as the output, which is a couple of levels
down.

http://sourceforge.net/forum/message.php?msg_id=3639216

g.os_path_dirname(self.outputFileName) with self.c.frame.openDirectory. This
makes the path relative to the project. Not 100% as the stylesheet filename
would need a path embedded in it to move the location down the tree. However,
it is consistent with the way the output file is named.</t>
<t tx="ekr.20060328171518.240">See the chapters2 in leoPlugins.leo.

See also:

http://sourceforge.net/forum/message.php?msg_id=3626542

https://sourceforge.net/forum/message.php?msg_id=3629055

http://sourceforge.net/forum/message.php?msg_id=3632004</t>
<t tx="ekr.20060328171518.244">Cleaned up the code and added support minibuffer commands:

group-operations-clear-marked       = Alt-Ctrl-Shift-l
group-operations-mark-for-copy      = Alt-Ctrl-Shift-c
group-operations-mark-for-move      = Alt-Ctrl-Shift-m
group-operations-mark-for-clone     = Alt-Ctrl-`
group-operations-mark-target        = Alt-Ctrl-Shift-t
group-operations-operate-on-marked  = Alt-Ctrl-Shift-o
group-operations-transfer           = Alt-Ctrl-Shift-d

This code has not been tested with the chapters2 plugin.</t>
<t tx="ekr.20060328171518.245">http://sourceforge.net/forum/message.php?msg_id=3617936

The fix was to plugins_menu.py: the cmd_callback must have an event argument.
</t>
<t tx="ekr.20060328171518.246">The fix: all menu commands now have event=None in their argument list.</t>
<t tx="ekr.20060328171518.248">Alas, @if-gui can't be made to work. The problem is that plugins can set
g.app.gui, but plugins need settings so the leoSettings.leo files must be parsed
before g.app.gui.guiName() is known.</t>
<t tx="ekr.20060328171518.249">It's not ready for prime time.</t>
<t tx="ekr.20060414071350.1"></t>
<t tx="ekr.20060414071350.8">@nocolor
http://sourceforge.net/forum/message.php?msg_id=3671350

Change aString.lstrip and aString.rstrip to the aString.replace.
@color</t>
<t tx="ekr.20060414071350.39">leoID = ekr (in c:\Documents and Settings\Ed)
reading settings in C:\prog\leoCVS\leo\config\leoSettings.leo
reading settings in C:\prog\leoCVS\leo\src\LeoPy.leo
rst3 plugin: SilverCity not loaded
AttributeError Exception in Tk callback
  Function: &lt;function bindKeyCallback at 0x016F2E70&gt; (type: &lt;type 'function'&gt;)
  Args: (&lt;Tkinter.Event instance at 0x03510288&gt;,)
  Event type: KeyPress (type num: 2)
Traceback (innermost last):
  File "C:\prog\leoCVS\leo\extensions\Pmw\Pmw_1_2\lib\PmwBase.py", line 1752, in __call__
    return apply(self.func, args)
  File "C:\prog\leoCVS\leo\src\leoKeys.py", line 2002, in bindKeyCallback
    return k.masterKeyHandler(event,stroke=stroke)
  File "C:\prog\leoCVS\leo\src\leoKeys.py", line 2928, in masterKeyHandler
    val = self.masterKeyHandlerHelper(event,stroke)
  File "C:\prog\leoCVS\leo\src\leoKeys.py", line 2992, in masterKeyHandlerHelper
    val = k.callStateFunction(event) # Calls end-command.
  File "C:\prog\leoCVS\leo\src\leoKeys.py", line 2219, in callStateFunction
    val = k.state.handler(event)
  File "C:\prog\leoCVS\leo\src\leoKeys.py", line 348, in autoCompleterStateHandler
    self.insertNormalChar(ch,keysym)
  File "C:\prog\leoCVS\leo\src\leoKeys.py", line 856, in insertNormalChar
    self.calltip(obj)
  File "C:\prog\leoCVS\leo\src\leoKeys.py", line 455, in calltip
    obj = getattr(string,obj.__name__)
AttributeError: 'module' object has no attribute 'startswith'</t>
<t tx="ekr.20060414071350.47">exception executing command
Traceback (most recent call last):
  File "C:\prog\leoCVS\leo\src\leoCommands.py", line 264, in doCommand
    val = command(event)
  File "C:\prog\leoCVS\leo\src\leoCommands.py", line 884, in clearRecentFiles
    u.afterClearRecentFiles(bunch)
  File "C:\prog\leoCVS\leo\src\leoUndo.py", line 621, in afterClearRecentFiles
    u.pushBead(bunch)
  File "C:\prog\leoCVS\leo\src\leoUndo.py", line 192, in pushBead
    u.setUndoTypes()
  File "C:\prog\leoCVS\leo\src\leoUndo.py", line 341, in setUndoTypes
    u.cutStack()
  File "C:\prog\leoCVS\leo\src\leoUndo.py", line 136, in cutStack
    if bunch.kind == 'beforeGroup':
AttributeError: 'Bunch' object has no attribute 'kind'</t>
<t tx="ekr.20060414071350.58"># No change for now
C:\prog\tigris-cvs\leo\src\leoKeys.py:1050: Parameter (thread) not used

# Fixed
C:\prog\tigris-cvs\leo\src\leoTkinterFrame.py:1428: Function returns a value and also implicitly returns None
C:\prog\tigris-cvs\leo\src\leoTkinterTree.py:1222: Local variable (delta) not used
C:\prog\tigris-cvs\leo\src\leoKeys.py:1931: Local variable (f) not used
C:\prog\tigris-cvs\leo\src\leoGlobals.py:5246: Local variable (buttonList) not used
C:\prog\tigris-cvs\leo\src\leoCommands.py:493: No global (enableIdleTimeHook) found</t>
<t tx="ekr.20060417092536">Leo 4.4 beta 4                                             April 21, 2006

This version fixes a long-standing MacOS bug.  It is likely to be the last
beta release before 4.4 final.  This release also adds several new commands
and contains a script for updating leoSettings.leo.

Warning: The previous beta was not widely distributed. Please do some testing in
your environment before recommending this version of Leo to others, (such as
your students).

Leo is a text editor, data organizer, project manager and much more. See:
http://webpages.charter.net/edreamleo/intro.html

The highlights of Leo 4.4:
--------------------------
- An Emacs-like mini-buffer: you can now execute any command by typing its long
name, with tab completion.

- Many new commands, including cursor and screen movement, basic character, word
and paragraph manipulation, and commands to manipulate buffers, the kill ring,
regions and rectangles. You can use Leo without using a mouse.

- Flexible key bindings and input modes. You can emulate the operation of Emacs,
Vim, or any other editor.

- A tabbed log pane. The Find and Spell Check commands now use tabs instead of
dialogs, making those commands much easier to use. Plugins or scripts can easily
create new tabs. The Completion tab shows possible typing completions.

- Autocompletion and calltips.  Autocompletion works much like tab completion.

- Dozens of other new features and bug fixes since Leo 4.3.3.

Links:
------
Leo:      http://webpages.charter.net/edreamleo/front.html
Home:     http://sourceforge.net/projects/leo/
Download: http://sourceforge.net/project/showfiles.php?group_id=3458
CVS:      http://sourceforge.net/cvs/?group_id=3458
Quotes:   http://webpages.charter.net/edreamleo/testimonials.html</t>
<t tx="ekr.20060417092825.1">See the (presently disabled) script button in scripts.leo at:

Buttons--&gt;@@button updateSettings

From the docstring:

Here is a **preliminary** script that updates a new leoSettings.leo file
(path2) from the settings in a previous leoSettings.leo file (path1).
Presumably, the path2 file is the leoSettings.leo file from a new distribution,
and the path1 file a leoSettings.leo file containing settings that you have
modified.  You must specify the full path of both files in the top-level @button node.

**Warning**: This script modifies the path2 file. Make sure that you don't mind
modifying this file.

**Warning**: This script is unsophisticated in its update algorithm. If if finds
corresponding nodes (node with the same settings name) in both outlines it simply
replaces the node in the path2 file with the node in the path1 file. In
particular, it does not keep track of individual shortcuts: it repaces the body
of one @shortcuts node with the body of the corresponding @shortcuts node.

**Note**: If the path1 file contains a settings node not in the path2 file it
attempts to create a new node in the corresponding place in the path2 file. If
this is not possible, say because the structures of the files are different, the
script places the new node as the last child of the @settings node in the path2
file.</t>
<t tx="ekr.20060421070409.1"></t>
<t tx="ekr.20060421070409.2">@nocolor
http://sourceforge.net/forum/message.php?msg_id=3688804
By: paulpaterson

It seems that copying and pasting nodes with CTRL-SHIFT-C, V is not working.
- (legacy bindings)
- select a node
- CTRL-SHIFT-C
- CTRL-SHIFT-V
- Vim opens up! I expect to paste the node. The clipboard doesn't seem to contain
any XML
- The menu items show that these keys are bound to the copy and paste node
commands

*** Also on legacy bindings the arrow keys don't seem to move the cursor in the
body.</t>
<t tx="ekr.20060421070409.3"></t>
<t tx="ekr.20060421070409.4">@nocolor
http://sourceforge.net/forum/message.php?msg_id=3692247
By: vpe

After cutting selection in the headline, headline area shrinks too much.  Example:
headline is 'NewHeadline', select last 'e', ctrl-x, it shrinks to 'Ne'

To fix by hand: add

s=g.app.gui.getAllText(w)

Just before

w.configure(width=f.tree.headWidth(s=s))

in cutText in leoTkFrame.py</t>
<t tx="ekr.20060421070409.9"></t>
<t tx="ekr.20060421070409.10">@nocolor
http://sourceforge.net/forum/message.php?msg_id=3692247

Find panel cannot be re-opened. Run open-find-dialog. Close it. Run open-find-dialog
again -- crash.

The fix was to move the line:

self.top.protocol("WM_DELETE_WINDOW", self.onCloseWindow)

from createBindings to createFrame in the leoTkinterFind class.</t>
<t tx="ekr.20060421070409.11">TclError Exception in Tk callback
  Function: &lt;function bindKeyCallback at 0x0169B170&gt; (type: &lt;type 'function'&gt;)
  Args: (&lt;Tkinter.Event instance at 0x01865EB8&gt;,)
  Event type: KeyPress (type num: 2)
Traceback (innermost last):
  File "C:\prog\tigris-cvs\leo\extensions\Pmw\Pmw_1_2\lib\PmwBase.py", line 1752, in __call__
    return apply(self.func, args)
  File "c:\prog\tigris-cvs\leo\src\leoKeys.py", line 1991, in bindKeyCallback
    return k.masterKeyHandler(event,stroke=stroke)
  File "c:\prog\tigris-cvs\leo\src\leoKeys.py", line 2931, in masterKeyHandler
    val = self.masterKeyHandlerHelper(event,stroke)
  File "c:\prog\tigris-cvs\leo\src\leoKeys.py", line 2990, in masterKeyHandlerHelper
    val = k.callStateFunction(event) # Calls end-command.
  File "c:\prog\tigris-cvs\leo\src\leoKeys.py", line 2208, in callStateFunction
    val = k.state.handler(event)
  File "c:\prog\tigris-cvs\leo\src\leoKeys.py", line 2289, in fullCommand
    k.callAltXFunction(k.mb_event)
  File "c:\prog\tigris-cvs\leo\src\leoKeys.py", line 2327, in callAltXFunction
    func(event)
  File "C:\prog\tigris-cvs\leo\src\leoCommands.py", line 2801, in showFindPanel
    c.frame.findPanel.bringToFront()
  File "C:\prog\tigris-cvs\leo\src\leoTkinterFind.py", line 469, in bringToFront
    self.top.withdraw() # Helps bring the window to the front.
  File "c:\python24\lib\lib-tk\Tkinter.py", line 1562, in wm_withdraw
    return self.tk.call('wm', 'withdraw', self._w)
TclError: bad window path name ".25637872"

================================================
  Event contents:
    char:
    delta: 13
    height: ??
    keycode: 13
    keysym: Return
    keysym_num: 65293
    num: ??
    serial: 1486
    state: 0
    time: 1717970
    type: 2
    widget: .17570752.17571352.19882152.minibuffer
    width: ??
    x: 183
    x_root: 576
    y: -62
    y_root: 859

</t>
<t tx="ekr.20060421070409.33"># getLeadinWord must clear self.membersList to disable completion.</t>
<t tx="ekr.20060421070409.36">leoID = ekr (in c:\Documents and Settings\Ed)
reading settings in C:\prog\tigris-cvs\leo\config\leoSettings.leo
reading settings in C:\Documents and Settings\Ed\My Documents\ekr.leo
rst3 plugin: SilverCity not loaded
exception executing command
Traceback (most recent call last):

  File "C:\prog\tigris-cvs\leo\src\leoCommands.py", line 264, in doCommand
    val = command(event)

  File "C:\prog\tigris-cvs\leo\src\leoCommands.py", line 2969, in pasteOutline
    u.afterInsertNode(pasted,undoType,undoData)

  File "C:\prog\tigris-cvs\leo\src\leoUndo.py", line 750, in afterInsertNode
    u.pushBead(bunch)

  File "C:\prog\tigris-cvs\leo\src\leoUndo.py", line 182, in pushBead
    if bunch2 and bunch2.kind == 'beforeGroup':

AttributeError: 'Bunch' object has no attribute 'kind'</t>
<t tx="ekr.20060421070409.37"></t>
<t tx="ekr.20060421070409.40"></t>
<t tx="ekr.20060421070409.41">New commands:

add-space-to-lines,
add-tab-to-lines
clean-lines
clear-selected-text
goto-global-line
help-for-command
open-outline-by-name (filename completion)
remove-space-from-lines
remove-tab-from-lines</t>
<t tx="ekr.20060421070602"></t>
<t tx="ekr.20060428084553">Leo 4.4 release candidate 1                                 April 28, 2006

This version fixes a few minor bug reported in 4.4b4 and adds 9 new commands.
The open-outline-by-name command supports filename completion.

Leo is a text editor, data organizer, project manager and much more. See:
http://webpages.charter.net/edreamleo/intro.html

The highlights of Leo 4.4:
--------------------------
- An Emacs-like mini-buffer: you can now execute any command by typing its long
name, with tab completion.

- Many new commands, including cursor and screen movement, basic character, word
and paragraph manipulation, and commands to manipulate buffers, the kill ring,
regions and rectangles. You can use Leo without using a mouse.

- Flexible key bindings and input modes. You can emulate the operation of Emacs,
Vim, or any other editor.

- A tabbed log pane. The Find and Spell Check commands now use tabs instead of
dialogs, making those commands much easier to use. Plugins or scripts can easily
create new tabs. The Completion tab shows possible typing completions.

- Autocompletion and calltips.  Autocompletion works much like tab completion.

- Dozens of other new features and bug fixes since Leo 4.3.3.

Links:
------
Leo:      http://webpages.charter.net/edreamleo/front.html
Home:     http://sourceforge.net/projects/leo/
Download: http://sourceforge.net/project/showfiles.php?group_id=3458
CVS:      http://leo.tigris.org/source/browse/leo/
Quotes:   http://webpages.charter.net/edreamleo/testimonials.html</t>
<t tx="ekr.20060428084553.2"></t>
<t tx="ekr.20060428084553.4">http://sourceforge.net/forum/message.php?msg_id=3692247

After cutting selection in the headline, headline area shrank too much.  </t>
<t tx="ekr.20060428084553.10">http://sourceforge.net/forum/message.php?msg_id=3692247

Find panel cannot be re-opened. Run open-find-dialog. Close it. Run open-find-dialog
again -- crash.</t>
<t tx="ekr.20060428084553.34"># getLeadinWord must clear self.membersList to disable completion.</t>
<t tx="ekr.20060428084553.37">Traceback (most recent call last):

  File "C:\prog\tigris-cvs\leo\src\leoCommands.py", line 264, in doCommand
    val = command(event)

  File "C:\prog\tigris-cvs\leo\src\leoCommands.py", line 2969, in pasteOutline
    u.afterInsertNode(pasted,undoType,undoData)

  File "C:\prog\tigris-cvs\leo\src\leoUndo.py", line 750, in afterInsertNode
    u.pushBead(bunch)

  File "C:\prog\tigris-cvs\leo\src\leoUndo.py", line 182, in pushBead
    if bunch2 and bunch2.kind == 'beforeGroup':

AttributeError: 'Bunch' object has no attribute 'kind'</t>
<t tx="ekr.20060428084553.38"></t>
<t tx="ekr.20060428084553.39">Useful, e.g., after a find.</t>
<t tx="ekr.20060428084553.41">self.beginCommand(undoType='xxx')
...
self.endCommand(changed=True,setLabel=True)</t>
<t tx="ekr.20060428084553.42">New commands:

add-space-to-lines
add-tab-to-lines
clean-lines
clear-selected-text
goto-global-line
help-for-command
remove-space-from-lines
remove-tab-from-lines</t>
<t tx="ekr.20060428084553.273">At present, only the open-outline-by-name command supports filename completion.</t>
<t tx="ekr.20060428084711">https://sourceforge.net/forum/message.php?msg_id=3699799</t>
<t tx="ekr.20060428084957"></t>
<t tx="ekr.20060511074853">Leo 4.4 Final                                                     May 11, 2006

Leo 4.4 Final is available at:
http://sourceforge.net/project/showfiles.php?group_id=3458&amp;package_id=29106

Leo is a text editor, data organizer, project manager and much more. See:
http://webpages.charter.net/edreamleo/intro.html

The highlights of Leo 4.4:
--------------------------
- An Emacs-like mini-buffer: you can now execute any command by typing its long
name, with tab completion.

- Many new commands, including cursor and screen movement, basic character, word
and paragraph manipulation, and commands to manipulate buffers, the kill ring,
regions and rectangles. You can use Leo without using a mouse.

- Flexible key bindings and input modes. You can emulate the operation of Emacs,
Vim, or any other editor.

- A tabbed log pane. The Find and Spell Check commands now use tabs instead of
dialogs, making those commands much easier to use. Plugins or scripts can easily
create new tabs. The Completion tab shows possible typing completions.

- Autocompletion and calltips.  Autocompletion works much like tab completion.
  To enable autocompletion, bind a key to the auto-complete command.

- Dozens of other new features and bug fixes since Leo 4.3.3.

Links:
------
Leo:      http://webpages.charter.net/edreamleo/front.html
Home:     http://sourceforge.net/projects/leo/
Download: http://sourceforge.net/project/showfiles.php?group_id=3458
CVS:      http://leo.tigris.org/source/browse/leo/
Quotes:   http://webpages.charter.net/edreamleo/testimonials.html</t>
<t tx="ekr.20060525104232">import leoPlugins

rst3 = leoPlugins.getPluginModule('rst3')

if rst3:
    controller = rst3.controllers.get(c)
    if controller:
        p,s = controller.writeNodeToString(ext='.html')
        print '*' * 40,p
        print s
else:
    rst3 = leoPlugins.loadOnePlugin('rst3',verbose=True)
    if rst3:
        g.es('rst3 loaded')
        rst3.onCreate('tag',{'c':c})
    else:
        # Ask to be removed.
        g.app.scriptDict['removeMe'] = True</t>
<t tx="ekr.20060525110135"># Problems with pdf files.

import leoPlugins

rst3 = leoPlugins.getPluginModule('rst3')

if rst3:
    controller = rst3.controllers.get(c)
    if controller:
        p,s = controller.writeNodeToString(ext='.pdf')
        print '*' * 40,p
        print s
else:
    rst3 = leoPlugins.loadOnePlugin('rst3',verbose=True)
    if rst3:
        g.es('rst3 loaded')
        rst3.onCreate('tag',{'c':c})
    else:
        # Ask to be removed.
        g.app.scriptDict['removeMe'] = True</t>
<t tx="ekr.20060525110135.1">import leoPlugins

rst3 = leoPlugins.getPluginModule('rst3')

if rst3:
    controller = rst3.controllers.get(c)
    if controller:
        p,s = controller.writeNodeToString(ext='.tex')
        print '*' * 40,p
        print s
else:
    rst3 = leoPlugins.loadOnePlugin('rst3',verbose=True)
    if rst3:
        g.es('rst3 loaded')
        rst3.onCreate('tag',{'c':c})
    else:
        # Ask to be removed.
        g.app.scriptDict['removeMe'] = True</t>
<t tx="ekr.20060525110217">import leoPlugins

rst3 = leoPlugins.getPluginModule('rst3')

if rst3:
    controller = rst3.controllers.get(c)
    if controller:
        p,s = controller.writeNodeToString(ext=None) # Convert rst nodes to rst text.
        print '*' * 40,p
        print s
else:
    rst3 = leoPlugins.loadOnePlugin('rst3',verbose=True)
    if rst3:
        g.es('rst3 loaded')
        rst3.onCreate('tag',{'c':c})
    else:
        # Ask to be removed.
        g.app.scriptDict['removeMe'] = True</t>
<t tx="ekr.20060601101643">Leo 4.4.1 beta 1                                            June 3, 2006

Leo 4.4.1 beta 1 is available at:
http://sourceforge.net/project/showfiles.php?group_id=3458&amp;package_id=29106

Leo is a text editor, data organizer, project manager and much more. See:
http://webpages.charter.net/edreamleo/intro.html

The highlights of Leo 4.4.1:
----------------------------
- A new colorizer plugin controlled by jEdit language description files.
  At present this plugin only reliably colors @language python code.
- Multiple editors in Leo's body pane.
- Search commands now support regex replace patterns: \1, \2, etc.
- Support for external debuggers: see http://webpages.charter.net/edreamleo/debuggers.html
- The scripting plugin now creates a Debug Script button.
- Several new commands including run-unit-test, python-help and toggle-invisibles.
- The help-for-command commands now contains information for almost all commands.
- A new shortcut_button plugin.

Links:
------
Leo:      http://webpages.charter.net/edreamleo/front.html
Home:     http://sourceforge.net/projects/leo/
Download: http://sourceforge.net/project/showfiles.php?group_id=3458
CVS:      http://leo.tigris.org/source/browse/leo/
Quotes:   http://webpages.charter.net/edreamleo/testimonials.html</t>
<t tx="ekr.20060601101958.1"></t>
<t tx="ekr.20060601101958.2">http://sourceforge.net/forum/message.php?msg_id=3729858

Fixed crasher in Leo 4.4 by initing self.p in Quickfind ctor.</t>
<t tx="ekr.20060601101958.6">http://sourceforge.net/forum/message.php?msg_id=3737879</t>
<t tx="ekr.20060601101958.13">http://sourceforge.net/forum/message.php?msg_id=3737745

- Added event keyword argument to parameterize function.</t>
<t tx="ekr.20060601101958.14">http://sourceforge.net/forum/message.php?msg_id=3737745

The fix was to add a c argument to g.findTopLevelNode and g.findNodeInTree.
</t>
<t tx="ekr.20060601101958.16"></t>
<t tx="ekr.20060601101958.28"></t>
<t tx="ekr.20060601101958.52">This runs the winpdb debugger in a separate process.

The winpdb debugger must be installed for this command to work.

For more details, see: http://webpages.charter.net/edreamleo/debuggers.html</t>
<t tx="ekr.20060601101958.56">This fixes all conflicts between Leo and Idle.</t>
<t tx="ekr.20060601101958.58"></t>
<t tx="ekr.20060601101958.70">- Allow \1, \2, etc. replacements in re searches.

- Allow \n and \t in plain searches.

- The shortcut for the replace-string command now changes from the find command
to the replace command.</t>
<t tx="ekr.20060601101958.172">@nocolor

http://sourceforge.net/forum/message.php?msg_id=3575014

Actually, the run-unit-tests command first appeared in Leo 4.4, but it never got
properly announced.</t>
<t tx="ekr.20060601101958.174">http://sourceforge.net/forum/message.php?msg_id=3729823

This is intended to help with redraw problems on Linux.</t>
<t tx="ekr.20060601101958.218"></t>
<t tx="ekr.20060601101958.234"></t>
<t tx="ekr.20060601101958.235">It is now clearer what the selected values are.</t>
<t tx="ekr.20060601101958.238"></t>
<t tx="ekr.20060601101958.239"></t>
<t tx="ekr.20060601101958.244">@nocolor

http://sourceforge.net/forum/message.php?msg_id=3737745

Added warnings in various places that the setting:

@bool expanded_click_area = True

interferes with the  Universal Scrolling plugin.</t>
<t tx="ekr.20060601101958.245">The add-editor command adds a new editor, the delete-editor command deletes the
presently selected editor, and the cycle-editor-focus command cycles focus
between editors in the body text.</t>
<t tx="ekr.20060601101958.264">@nocolor

leoSettings.leo now contains the following setting, with default as shown:

@bool autoindent_in_nocolor_mode = True


True:  auto-indent regardless of how text is colored.
False: disable auto-indenting if in range @nocolor or @kill.

This will make the default action work as Roger Erens requested, and will allow
you to make Leo work exactly as before if you want.</t>
<t tx="ekr.20060601101958.276">@shortcut nodes never worked and apparently nobody ever used them.</t>
<t tx="ekr.20060601101958.277"></t>
<t tx="ekr.20060601102802"></t>
<t tx="ekr.20060601102802.2"></t>
<t tx="ekr.20060603072938">This prompts for a string s, then puts the result of help(s) in Leo's log pane.</t>
<t tx="ekr.20060603081537">This plugin creates a 'Shortcut' button in the icon area. Pressing the Shortcut
button creates *another* button which when pressed will select the presently
selected node at the time the button was created.</t>
<t tx="ekr.20060603082009">http://sourceforge.net/forum/message.php?msg_id=3761285

There were actually two bugs:
    
- parseLeoSentinel was not recognizing the closing comment delim (!!)

- putDirective was incorrectly setting delims for @language and @comment delims.
  This is wrong: the init code calls scanAllDirectives, and the comment delims
  **must not change** in the file (except as the result of @delims.)</t>
<t tx="ekr.20060620094645">Leo 4.4.1 beta 2                                            June 23, 2006

Leo 4.4.1 beta 2 is available at:
http://sourceforge.net/project/showfiles.php?group_id=3458&amp;package_id=29106

Leo is a text editor, data organizer, project manager and much more. See:
http://webpages.charter.net/edreamleo/intro.html

The highlights of Leo 4.4.1:
----------------------------
- A new colorizer plugin controlled by jEdit language description files.
  At present this plugin only reliably colors @language python code.
- Multiple editors in Leo's body pane.
- Search commands now support regex replace patterns: \1, \2, etc.
- Support for external debuggers: see http://webpages.charter.net/edreamleo/debuggers.html
- The scripting plugin now creates a Debug Script button.
- Several new commands including run-unit-test, python-help and toggle-invisibles.
- The help-for-command commands now contains information for almost all commands.
- A new shortcut_button plugin.

Links:
------
Leo:      http://webpages.charter.net/edreamleo/front.html
Home:     http://sourceforge.net/projects/leo/
Download: http://sourceforge.net/project/showfiles.php?group_id=3458
CVS:      http://leo.tigris.org/source/browse/leo/
Quotes:   http://webpages.charter.net/edreamleo/testimonials.html</t>
<t tx="ekr.20060620094645.34"></t>
<t tx="ekr.20060620094645.35"></t>
<t tx="ekr.20060620094645.43"></t>
<t tx="ekr.20060620094645.44">Called c.bringToFront() after open/save/import dialogs.</t>
<t tx="ekr.20060620094645.45">FAIL: @test return ends editing of headline

----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\prog\tigris-cvs\leo\src\leoTest.py", line 155, in runTest
    exec script + '\n' in {'c':c,'g':g,'p':p}
  File "&lt;string&gt;", line 14, in ?
AssertionError: oops2

----------------------------------------------------------------------
Ran 438 tests in 193.628s

FAILED (failures=1)
&gt;&gt;&gt;
</t>
<t tx="ekr.20060620094645.46">http://sourceforge.net/forum/message.php?msg_id=3764077</t>
<t tx="ekr.20060620094645.50"></t>
<t tx="ekr.20060620094645.52">@nocolor

http://sourceforge.net/forum/message.php?msg_id=3771032
By: paulpaterson

The cycle-editor-focus command causes Leo to lock up  on my machine (WinXP,
Python 2.4).

@color
</t>
<t tx="ekr.20060620094645.64">http://sourceforge.net/forum/message.php?msg_id=3771014</t>
<t tx="ekr.20060620094645.68">lstrip and rstrip do not exist in Python 2.2.1.</t>
<t tx="ekr.20060620094645.76">@nocolor

http://sourceforge.net/forum/message.php?msg_id=3778764
By: davidmcnab

When I hit my 'change-editor-focus' binding, the cursor jumps
to unpredictable places within the next editor pane.
</t>
<t tx="ekr.20060620094645.77"></t>
<t tx="ekr.20060620094645.78"></t>
<t tx="ekr.20060620094645.79">Added makeMasterGuiBinding.</t>
<t tx="ekr.20060620094645.85"></t>
<t tx="ekr.20060620094645.86"></t>
<t tx="ekr.20060620094645.96"></t>
<t tx="ekr.20060620094645.97"></t>
<t tx="ekr.20060620094645.103"></t>
<t tx="ekr.20060620094645.106"></t>
<t tx="ekr.20060620094645.107">Leo now supports bindings of the form:

command-name !command = shortcut

You will find examples in leoSettings.leo in the node

@keys EKR bindings: vim mode bindings--&gt;Shortcuts--&gt;@shortcuts top-level keys

Such bindings are essential for all plain key bindings that are *only* to be executed in command mode.  Most, but *not* all plain key bindings should be bound in the !command 'pane'.  The two exceptions presently are '.' which *always* invokes the autocompleter code and '(' which *always* invokes the calltips code.

It is now possible to have a *single* set of key bindings be 'Emacs-like' and
'Vim-like' at the same time. See the node EKR bindings: vim mode bindings in
leoSettings.leo.

One setting switches between emacs-like operation and vim-like operation:

For emacs, use:
@strings  [ignore,insert,overwrite] top_level_unbound_key_action = insert

For vim, use:
@strings  [ignore,insert,overwrite] top_level_unbound_key_action = ignore

Vim-like modes are made possible by two new features:

1. Entry commands in @mode nodes. In the body of @mode nodes, lines of the form

--&gt; command-name

tell Leo to execute the command when entering the mode. More than one such lines
may exist; Leo executes them in the order they appear. Entry commands are
potentially a very powerful feature. To avoid chaos, entry commands should not
alter the minibuffer :-)

2. Silent modes. In order to keep the selected text visible, Leo must *not* move
focus into the minibuffer for editing commands. The set-silent-mode command
tells Leo to treat the mode described in the @mode node as a silent mode. A true
mode is created, but it only affects key bindings and the minibuffer never
becomes active.

Thus, all @mode nodes for vim-like modes contain the following line:

--&gt; set-silent-mode.</t>
<t tx="ekr.20060620094645.108">All sets of key bindings in leoSettings.leo now start with @keys in the headline
of the root node. The @keys convention is used *only* by the Check Bindings
script. So now, instead of having a static list of key bindings sets (which is
guaranteed to get out-of-date), the Check Bindings script can scan all of
leoSettings.leo for sets of key bindings.

Another improvement to the Check Bindings script. Besides doing a better job of
checking, you may now specify optional commands, such as commands defined in
plugins. The Check Bindings will not complain if the commands don't presently
exists in k.commandsDict. You specify such commands by adding items to the
following lists in the root node of the Check Bindings script, i.e., the node
Buttons--&gt;@button Check Bindings.

optionalCommandPrefixes = ['group-operations']
optionalCommandNames = []</t>
<t tx="ekr.20060620094645.109">- added isearch-with-present-options.
- many small improvements to isearch code.
- regex searches now highlighted properly.
- isearches are (and should be) confined to a single body text.
- Backspace now handled properly.

A small glitch. Starting a regexp pattern with '.' will cause the entire pattern
to turn red initially, which is technically correct but perhaps a bit
confusing.</t>
<t tx="ekr.20060620094645.194">http://sourceforge.net/forum/message.php?msg_id=3767016</t>
<t tx="ekr.20060620094645.225"></t>
<t tx="ekr.20060620094645.231">The commands that enable and disable calltips now update the status line.</t>
<t tx="ekr.20060620094645.232">Creating a script button creates the press-xxx-button command,
and you can specify settings for such commands using @shortcuts nodes.</t>
<t tx="ekr.20060620094645.233"></t>
<t tx="ekr.20060620094645.234">@nocolor

The scripting plugin now creates a press-x-button command for each scripting button named x.
You can bind shortcuts to such commands by placing @shortcuts nodes in an @setting tree in the outline containing the @button nodes.  test.leo shows an example.

What I did:
    
- The scripting plugin now defines button bindings with the 'button' pane specifier.
  This takes precedence over all other specifiers.

- k.bindKeyToDict now does a better job of detecting and warning about redefinitions.

- k.printBindings now properly sorts entries.
  This was causing me a great deal of confusion.

- k.registerCommand now properly gets shortcuts from settings if possible,
  and makes bindings in the new 'button' pane specifier.

- masterKeyHandlerHelper now supports the 'button' pane specifier,
  which overrides all others.

@color</t>
<t tx="ekr.20060620094645.242"></t>
<t tx="ekr.20060620094645.243">@nocolor

http://sourceforge.net/forum/message.php?msg_id=3772475

Maybe put a link to the html TOC into the Help Menu,
"%leodir%/doc/html/leo_TOC.html".

This is more intuitive (to newbies) than the LeoDocs.leo link.  I found this
very confusing in the begining.

What I did:
    
- Created open-users-guide command.
- Created Open Users Guide menu item.
- Removed Open Offline Tutorial menu item.

@color</t>
<t tx="ekr.20060620094645.252"># Important: this can be done better using per-pane bindings as in the default leoSettings.leo.</t>
<t tx="ekr.20060620094645.258"></t>
<t tx="ekr.20060620094645.286"></t>
<t tx="ekr.20060620094645.299">http://sourceforge.net/forum/message.php?msg_id=3778744

Added editor_orientation setting: valid values are vertical and horizontal.</t>
<t tx="ekr.20060620094645.302"></t>
<t tx="ekr.20060620094645.303">@nocolor

http://sourceforge.net/forum/message.php?msg_id=3767601
http://sourceforge.net/forum/message.php?msg_id=3768413
Craig

I have an @thin file with @Doc and @Code sections scattered though out the tree,
where each node has one or more doc and code sections.

I would like to be able to use the rst3 pluging to produce an html file containing
only info from the doc sections, ignoring the code sections.

I added the </t>
<t tx="ekr.20060620094645.304">@nocolor
http://sourceforge.net/forum/message.php?msg_id=3770732
By: ktenney

In &lt;&lt; Theory of operation of find/change &gt;&gt; 
the opening paragraph does not appear in the html,
</t>
<t tx="ekr.20060620094645.305">@nocolor

http://sourceforge.net/forum/message.php?msg_id=3780216
Craig

In Doc_Only_Mode the rst3 plugin outputs headlines irrespective of the show_headlines
setting.  The other modes do honour thi setting.

I scratched around and managed to fix this by changing the node: rst3.py--&gt;class
rstClass--&gt;write methods--&gt;writeBody &amp; helpers--&gt;handleDocOnlyMode

In Line 25 I added a new statement:
     if showHeadlines:
and indented the following 3 lines to make them conditional on this if:
        if result or showThisHeadline or showOrganizers or p == self.topNode:
            # g.trace(len(result),p.headString())
            self.writeHeadlineHelper(p)</t>
<t tx="ekr.20060620094645.306">@nocolor
http://sourceforge.net/forum/message.php?msg_id=3785400
By: craigj3


I have a @url node pointing to a Leo file which has a filename with %20 in it.
When I double-click this node I get:

"can not open: \\\Documents%20and%20Settings\tftcj1.EDCON\My%20Documents\Proj\RI
CAA\PcasCellLink.leo"

Taking a look with a debugger, I see that Plugins--&gt;Enhancing the icon and status
areas--&gt;@thin UNL.py--&gt;onUrl1 line 29ish does not covert %20 to spaces before
calling openWithFileName.</t>
<t tx="ekr.20060620094645.307">@nocolor
http://sourceforge.net/forum/message.php?msg_id=3783225
Craig

I am looking at the image pluging for organising photos, and discovered that
it is limited to gif files only.  I found this a bit silly as installing the
ImageTk module from the Python Imaging Library and making a two line change
to the pluging enables it to be used on practically any image type.

The two line are:
1.  a new import:-
import ImageTk

2. In &lt;&lt;select image&gt;&gt; line 9 change 
photo = Tk.PhotoImage(master=a.root, file=filename)

to

photo = ImageTk.PhotoImage(master=a.root, file=filename)</t>
<t tx="ekr.20060620094645.308">@nocolor
http://sourceforge.net/forum/message.php?msg_id=3779706
By: mstarzyk

My point was not about not found CSS, but that .html files are written to
default_path directory, but .txt files are not written to default_path
directory.</t>
<t tx="ekr.20060620094645.309">@nocolor

http://sourceforge.net/forum/message.php?msg_id=3784636
By: craigj3

I note that the scheduler plugin is currently broken.

The problem was that all commands now get an event arg.

The Begin Recording and End Recording commands do not seem to work...</t>
<t tx="ekr.20060622130553">
http://sourceforge.net/forum/message.php?msg_id=3784292

http://webpages.charter.net/edreamleo/install.html#updating-settings-from-previous-versions-of-leo</t>
<t tx="ekr.20060622130553.2">http://sourceforge.net/forum/message.php?msg_id=3778946

http://webpages.charter.net/edreamleo/writingPlugins.html#turning-script-buttons-into-plugins</t>
<t tx="ekr.20060622130815">http://sourceforge.net/forum/message.php?msg_id=3790857</t>
<t tx="ekr.20060622130815.3">http://sourceforge.net/forum/message.php?msg_id=3790814</t>
<t tx="ekr.20060622130815.9"></t>
<t tx="ekr.20060622132524"></t>
<t tx="ekr.20060629083400.1">Leo 4.4.1 beta 3                                            June 29, 2006

Leo 4.4.1 beta 3 is available at:
http://sourceforge.net/project/showfiles.php?group_id=3458&amp;package_id=29106

Leo is a text editor, data organizer, project manager and much more. See:
http://webpages.charter.net/edreamleo/intro.html

The highlights of Leo 4.4.1:
----------------------------
- A new colorizer plugin controlled by jEdit language description files.
  At present this plugin only reliably colors @language python code.
- Multiple editors in Leo's body pane.
- Search commands now support regex replace patterns: \1, \2, etc.
- Support for external debuggers: see http://webpages.charter.net/edreamleo/debuggers.html
- The scripting plugin now creates a Debug Script button.
- Several new commands including run-unit-test, python-help and toggle-invisibles.
- The help-for-command commands now contains information for almost all commands.
- A new shortcut_button plugin.

Links:
------
Leo:      http://webpages.charter.net/edreamleo/front.html
Home:     http://sourceforge.net/projects/leo/
Download: http://sourceforge.net/project/showfiles.php?group_id=3458
CVS:      http://leo.tigris.org/source/browse/leo/
Quotes:   http://webpages.charter.net/edreamleo/testimonials.html</t>
<t tx="ekr.20060629083935.2"></t>
<t tx="ekr.20060629083935.3"></t>
<t tx="ekr.20060629083935.8">http://sourceforge.net/forum/message.php?msg_id=3795258

The column display doesn't change while typing.

</t>
<t tx="ekr.20060629083935.15">http://sourceforge.net/forum/message.php?msg_id=3510448

The fix was to getLastTracebackFileAndLineNumber.

I also created handleScriptException.</t>
<t tx="ekr.20060629083935.25">http://sourceforge.net/forum/message.php?msg_id=3413805</t>
<t tx="ekr.20060629083935.32">- Underindented comments do not end the scan of Python classes or methods.
- Handles continued signature lines properly.</t>
<t tx="ekr.20060629083935.61">Note: Editing headline text will happen in insert mode unless

@strings top_level_unbound_key_action = overwrite</t>
<t tx="ekr.20060629083935.70">After executing a command we must be careful to test c.exists.
</t>
<t tx="ekr.20060629083935.71">- A better trace, and the trace goes to the log pane.

- Eliminated k.keysymHistory: Tk keysyms are pretty useless.
</t>
<t tx="ekr.20060629083935.74"></t>
<t tx="ekr.20060629083935.75">@nocolor

- Improved prompt.
- Added message if no previous complex command.
- Added mode entries.</t>
<t tx="ekr.20060629083935.76">http://sourceforge.net/forum/message.php?msg_id=3794854</t>
<t tx="ekr.20060629083935.93">@killcolor

Here are the relevant settings:
    
@bool flash_matching_brackets: True: flash matching bracket when typing (, ), [, ], { or }.

@color flash_brackets_background_color and @color flash_brackets_foreground_color.

@int flash_brackets_count: The number of times to flash matching brackets.

@int flash-brackets-delay: One half the total cycle time of bracket flashes, in milliseconds.
</t>
<t tx="ekr.20060629083935.96"></t>
<t tx="ekr.20060629083935.97"># Ctrl-k is no longer needed by the match-brackets command now that brackets flash automatically.</t>
<t tx="ekr.20060629083935.98"></t>
<t tx="ekr.20060629083935.99">When True, this provides a full traceback for all exceptions taken when binding keyboard shortcuts.</t>
<t tx="ekr.20060629083935.100">@killcolor

@bool flash_matching_brackets: True: flash matching bracket when typing (, ), [, ], { or }.

@color flash_brackets_background_color and @color flash_brackets_foreground_color.

@int flash_brackets_count: The number of times to flash matching brackets.

@int flash-brackets-delay: One half the total cycle time of bracket flashes, in milliseconds.</t>
<t tx="ekr.20060822140418"></t>
<t tx="ekr.20060822140418.1">Leo 4.4.1 beta 4                                            August 24, 2006

Leo 4.4.1 beta 4 is available at:
http://sourceforge.net/project/showfiles.php?group_id=3458&amp;package_id=29106

Leo is a text editor, data organizer, project manager and much more. See:
http://webpages.charter.net/edreamleo/intro.html

The highlights of Leo 4.4.1:
----------------------------
- Leo outputs decorators correctly, provided that the decorator is not a Leo directive.
- A new colorizer plugin controlled by jEdit language description files.
- A new shadow files plugin that allows derived files not to have sentinel lines.
- Multiple editors in Leo's body pane.
- Search commands now support regex replace patterns: \1, \2, etc.
- Support for external debuggers: see http://webpages.charter.net/edreamleo/debuggers.html
- The scripting plugin now creates a Debug Script button.
- Several new commands including run-unit-test, python-help, toggle-invisibles,
  and scroll-outline-left/right.
- The help-for-command commands now contains information for almost all commands.
- A new shortcut_button plugin.

Links:
------
Leo:      http://webpages.charter.net/edreamleo/front.html
Home:     http://sourceforge.net/projects/leo/
Download: http://sourceforge.net/project/showfiles.php?group_id=3458
CVS:      http://leo.tigris.org/source/browse/leo/
Quotes:   http://webpages.charter.net/edreamleo/testimonials.html</t>
<t tx="ekr.20060822140418.3"></t>
<t tx="ekr.20060822140418.4">http://sourceforge.net/forum/forum.php?thread_id=1542384&amp;forum_id=10228</t>
<t tx="ekr.20060822140418.26">http://sourceforge.net/forum/message.php?msg_id=3839322</t>
<t tx="ekr.20060822140418.29">http://sourceforge.net/forum/message.php?msg_id=3805745</t>
<t tx="ekr.20060822140418.36">http://sourceforge.net/forum/message.php?msg_id=3841115

There is still some doubt about what the best operation of this command should be.</t>
<t tx="ekr.20060822140418.39">http://leo.zwiki.org/9RussianUnicodeWordsAreNotDetectedProperlyInBodyPane</t>
<t tx="ekr.20060822140418.41">http://sourceforge.net/forum/message.php?msg_id=3874380

Setting a value for background color in the body pane had no effect.

There were several problems, amoung which conflicting and confusing settings.
In particular, the insert_mode_bg_color setting overrides the body_text_background_color setting.

I changed the code so that insert_mode_bg_color defaults to
body_text_background_color, and put all the settings for the body text in one
place.</t>
<t tx="ekr.20060822140418.49"></t>
<t tx="ekr.20060822140418.69"></t>
<t tx="ekr.20060822140418.70">http://sourceforge.net/forum/message.php?msg_id=3802624

Added @font menu font setting</t>
<t tx="ekr.20060822140418.76">http://sourceforge.net/forum/message.php?msg_id=3834645</t>
<t tx="ekr.20060822140418.77">http://sourceforge.net/forum/message.php?msg_id=3802513

Added these settings:
    
@string open_flash_brackets = ([{
@string close_flash_brackets = )]}</t>
<t tx="ekr.20060822140418.88">Leo *already* outputs decorators correctly, assuming the decorator does not conflict with a Leo directive.</t>
<t tx="ekr.20060822140418.92">http://sourceforge.net/forum/message.php?msg_id=3858363</t>
<t tx="ekr.20060822140418.97">These were overly complicated an not useful.</t>
<t tx="ekr.20060830141224">Leo 4.4.1 final                                            August 30, 2006

Leo 4.4.1 final is available at:
http://sourceforge.net/project/showfiles.php?group_id=3458&amp;package_id=29106

Leo is a text editor, data organizer, project manager and much more. See:
http://webpages.charter.net/edreamleo/intro.html

The highlights of Leo 4.4.1:
----------------------------
- Leo outputs decorators correctly, provided that the decorator is not a Leo directive.
- A new colorizer plugin controlled by jEdit language description files.
- A new shadow files plugin that allows derived files not to have sentinel lines.
- Multiple editors in Leo's body pane.
- Search commands now support regex replace patterns: \1, \2, etc.
- Support for external debuggers: see http://webpages.charter.net/edreamleo/debuggers.html
- The scripting plugin now creates a Debug Script button.
- Several new commands including run-unit-test, python-help, toggle-invisibles,
  and scroll-outline-left/right.
- The help-for-command commands now contains information for almost all commands.
- A new shortcut_button plugin.

Links:
------
Leo:      http://webpages.charter.net/edreamleo/front.html
Home:     http://sourceforge.net/projects/leo/
Download: http://sourceforge.net/project/showfiles.php?group_id=3458
CVS:      http://leo.tigris.org/source/browse/leo/
Quotes:   http://webpages.charter.net/edreamleo/testimonials.html</t>
<t tx="ekr.20060830141224.2"># Possibly a less intrusive warning should be used.</t>
<t tx="ekr.20060830141224.13"></t>
<t tx="ekr.20060830141224.14"></t>
<t tx="ekr.20060830141224.15">@nocolor
http://sourceforge.net/forum/message.php?msg_id=3885494
By: mikecrowe

OK, I found out how to duplicate this one.  This caused me a lot of grief until
I found out what is causing it.

NodeA:
...Child1
...Child2
...Child3

NodeB:
...CloneChild1
...CloneChild2
...CloneChild3

Now, put cursor on NodaA.  Ctrl-Shift-C (copy node).
Next, put cursor on CloneChild3.  Paste Node as Clone
You should get an invalid paste clone message.

Now, first cursor move (for me) puts NodeB as top node, ERASING all other nodes.
Warning:  DO NOT SAVE NOW.  It will erase all other nodes.
</t>
<t tx="ekr.20060830141224.16">@nocolor

- Created getLeoOutlineHelper.  This simplifies the code.
- Init self.checking in getLeoFile and getLeoOutline.
- Use self.checking in getVnodes, getVnode and createVnode.
  Using self.checking in getVnode complicates an already way-too-complex method, but it can't be helped.</t>
<t tx="ekr.20060830141224.37"></t>
<t tx="ekr.20060830141224.38">@nocolor

http://sourceforge.net/forum/message.php?msg_id=3886250
By: znafets

A .leoID.txt with a \n behind the idstring creates a problem. 
It will be read in g.app.leoID and being used as is when writing the Leo file.

The fix is in app.setLeoID -&gt; &lt;&lt; return if we can set leoID from "leoID.txt" &gt;&gt;</t>
<t tx="ekr.20060830141224.45"></t>
<t tx="ekr.20060830141224.46">@nocolor

http://sourceforge.net/forum/message.php?msg_id=3890031
By: terry_n_brown

I have a tree of some 2500 nodes, run a script that marks
probably 1500-2000 of them, and that's quick (2-3 seconds max.).

I can clear all the marks with:

for p in c.allNodes_iter():
    p.v.clearMarked()

and that also is quick (2-3 seconds max.).  But when I use the menu option Unmark
All, that takes forever (1-2 minutes :-) running 100% CPU all the while.</t>
<t tx="ekr.20060903102158">Leo 4.4.1.1 final                                       September 3, 2006

Leo 4.4.1.1 final is available at:
http://sourceforge.net/project/showfiles.php?group_id=3458&amp;package_id=29106

Leo 4.4.1.1 corrects a serious last-minute unicode bug in Leo 4.4.1.
This version also adds the new slideshow plugin.

Leo is a text editor, data organizer, project manager and much more. See:
http://webpages.charter.net/edreamleo/intro.html

The highlights of Leo 4.4.1:
----------------------------
- Leo outputs decorators correctly, provided that the decorator is not a Leo directive.
- A new colorizer plugin controlled by jEdit language description files.
- A new shadow files plugin that allows derived files not to have sentinel lines.
- A new slide show plugin allows you to use Leo outlines as slide shows.
- Multiple editors in Leo's body pane.
- Search commands now support regex replace patterns: \1, \2, etc.
- Support for external debuggers: see http://webpages.charter.net/edreamleo/debuggers.html
- The scripting plugin now creates a Debug Script button.
- Several new commands including run-unit-test, python-help, toggle-invisibles,
  and scroll-outline-left/right.
- The help-for-command commands now contains information for almost all commands.
- A new shortcut_button plugin.

Links:
------
Leo:      http://webpages.charter.net/edreamleo/front.html
Home:     http://sourceforge.net/projects/leo/
Download: http://sourceforge.net/project/showfiles.php?group_id=3458
CVS:      http://leo.tigris.org/source/browse/leo/
Quotes:   http://webpages.charter.net/edreamleo/testimonials.html</t>
<t tx="ekr.20060928172040">Leo 4.4.2 beta 1                                  September 29, 2006

Leo 4.4.2 beta 1 is available at:
http://sourceforge.net/project/showfiles.php?group_id=3458&amp;package_id=29106

Leo is a text editor, data organizer, project manager and much more. See:
http://webpages.charter.net/edreamleo/intro.html

The highlights of Leo 4.4.2:
----------------------------
- You can now store settings in myLeoSettings.leo without fear of those settings
  being changed by cvs updates or in future versions of Leo.
- Leo's vnode and tnode classes are now completely independent of the rest of Leo.
  Some api's have been changed.  This 'big reorg' and may affect scripts and plugins.
- Leo's vnode and tnode classes can optionally be compatible with ZODB databases,
  i.e., they can optionally derive from ZODB.Persistence.Persistent.
  See Chapter 17: Using ZODB with Leo for details.
- The leoOPML plugin defines commands to read and write OPML files.
- The slideshow plugin allows Leo to run slideshows defined by @slideshow and @slide nodes.
- The leo_to_rtf and leo_to_html plugins create rtf and html files from Leo outlines.
- Much faster navigation through the outline using Alt-arrow keys.
- When focus is in the outline pane, you can move to headlines by typing the first letter of headlines.
- The find command now closes nodes not needed to show the node containing the present match.
- Numerous changes that make Leo easier to use without using a mouse.
- Many new minibuffer commands now appear in the Cmds menu.

Links:
------
Leo:      http://webpages.charter.net/edreamleo/front.html
Home:     http://sourceforge.net/projects/leo/
Download: http://sourceforge.net/project/showfiles.php?group_id=3458
CVS:      http://leo.tigris.org/source/browse/leo/
Quotes:   http://webpages.charter.net/edreamleo/testimonials.html</t>
<t tx="ekr.20060928172525.81">What I did:
    
- Removed c argument from t, v and p ctors.
- Removed c argument from most position methods.
    - In particular, p.link, p.unlink, v.link and v.unlink no longer update c.currentPosition()
    - Moved all position methods that still had a c argument to the Commands class.
- Removed p.allNodes_iter.
- Added c.findRootPosition and c.findRootVnode.
- c.rootPosition now returns c.findRootPosition(c.currentPosition())

As a result:
    
- The tnode, vnode and position classes are *completely* independent of Leo.
  In particular, no tnode, vnode or position method gets a c argument.
- The p.link, p.unlink, v.link and v.unlink are significantly simpler.
- The machinery for keeping the root position up-to-date is
  simple and confined to one place in the Commands class.</t>
<t tx="ekr.20060928172525.167"></t>
<t tx="ekr.20060928172525.172">It now prints the binding for the command.</t>
<t tx="ekr.20060928172525.180">Rewrote moveWordHelper. It now avoids Tk and regexes.  *Much* simpler.</t>
<t tx="ekr.20060928172525.195">@nocolor

My present thinking is that scripts should be able to store/retrieve persistent
objects to/from the zodb. That is, the zodb plugin is likely to be retired.

Leo's vnode and tnode classes now derive from ZODB.Persistence.Persistent if
leoNodes.use_zodb is True. It remains to be seen whether having use_zodb = True
will cause any serious problems.

See the posting below (Scripting using zodb) for latest details.

See the node 'zodb get/put buttons' in test.leo for examples of how scripts can access zodb easily.

Created g.init_zodb and v.detach.</t>
<t tx="ekr.20060928172525.197">&gt; Do you see zodb as persisting Leo files or Leo nodes?

Interesting question.  I now see the zodb plugin as a proof-of-concept for *user-defined* scripts.  The zodb plugin is probably going to go away.

Let us suppose that db is a ZODB.DB instance. (To see how to create such an instance, see the init_zodb method in the zodb plugin.  Perhaps I'll defines something like g.openZodb to make this easier.)  Then the statements:

connection = db.open()
root = connection.root()
root[aKey] = v
get_transaction().commit()
connection.close()

will write all of v's data (all vnodes and tnodes) to the zodb.  This is true whatever v is: it can be the root of an entire outline, or any suboutline.  If you want to write a single node, you would have to 'detach' that node from the outline.  You can do this by copying the node and then unlinking the node from its descendents. Perhaps I could add a convenience method to the vnode class to make this easier.

&gt;Do you see zodb work as providing enhanced access to nodes across multiple files?

Scripts could do so easily.  Happily, the distinction between 'long-lived' and 'short-lived' connections is not important for scripts: a script should hold a connection open only for as long as needed.  So it would be easy to write any number of vnode trees to the zodb.  Later, another script could access any of the data in the zodb by zodb key.  Like this:

connection = db.open()
root = connection.root()
v = root.get(aKey)
p = leoNodes.position(v,[])

After running this script, p is a position representing the root of the tree of 'imported' vnodes.  The script above does not 'connect' the imported trees to an outline, nor should it do so.  As I write this, I realize that the position ctor should make the second argument optional, so that leoNodes.position(v) would be equivalent to leoNodes.position(v,[]).

Each script should open at most connection at a time and be sure to close any zodb connection it creates.  The proper way to do this is in a finally statement, like this:

try:
....connection = db.open()
....root = connection.root()
....v = root.get(aKey)
....p = leoNodes.position(v,[])
....&lt;&lt; do something with the nodes in p's tree&gt;&gt;
finally:
....get_transaction().commit()
....connection.close()

In short, the recent changes to Leo's vnode and tnode classes give scripts the ability to save/retrieve Leo data to/from the zodb in any way a script wants, without any further support from Leo, or from me.

I shall spend an hour or two more with the zodb plugin, but it looks to me that the plugin has served its purpose.  Rather than trying to guess how people will want to use the zodb, it will be simpler and more general to have people write scripts that do exactly what they want.  In particular, such scripts can easily sidestep the problems with multiple open connections.

Edward

P.S. Please note that the scripts shown above could not have been written without all the recent work with the zodb plugin and the big code reorg.

P.P.S. A couple of unit tests involving the new v/t.__hash__ methods just failed, so it may be just a little bit longer before the code on cvs is truly zodb ready.  I'll also be working on example scripts and the convenience methods described above.

EKR
</t>
<t tx="ekr.20060928172525.198">- Removed all modes except Alt-C mode.
- Use Shift-arrows for outline moves when focus is in outline pane.
- Put help / apropos commands in help menu.
- Put focus commands in Cmds menu.
- When focus is in outline, normal character navagates like Windows explorer.
- Put Scrolling commands in Cmds menu.
- Screened out(some) unwanted characters from affecting outline navigation.More work is needed.
- Esc character is never inserted into text.
- Replaced @button clones-tab with @command clones-tab.
- Scripting plugins now sets verbose=True so @commands get shown.
* Alt keys (outline move commands) should set focus to outline even if nothing else happens.
- Closing a window no longer puts focus in limbo: added force argument to c.set_focus.
- New gui bindings: (I should actually be able to remember these).
    cycle-all-focus                     = Alt-Y
    contract-pane                       = Alt+Ctrl+-
    expand-pane                         = Alt+Ctrl-=
    focus-to-tree                       = Alt-space
    scroll-outline-down-page            = Alt-PageDn
    scroll-outline-down-page            ! tree = PageDn
    scroll-outline-up-page              = Alt-PageUp
    scroll-outline-up-page              ! tree = PageUp
    scroll-outline-left                 = Alt+Ctrl+LtArrow
    scroll-outline-right                = Alt+Ctrl+RtArrow
- Put find-character and back-find-character in Edit:Find menu.
- Use Alt-S,Alt-R for incremental searches.
- Created find-character-extend-selection and back-find-character-extend-selection.
- Added binding (Ctrl-W) and entry in Cmds menu for select-word-at-cursor.
- Added binding (Ctrl-P) for repeat-complex-command.
- Added binding (Ctrl-B) for execute-script.
* Fixed bug in extend mode.
- Added binding (Ctrl-space) for toggle extend mode.
- Removed most cursor move bindings involving ctrl keys. Exception: ctrl-a and ctrl-e.
    ** The idea is that I'll use extend mode instead.
- Stay in outline mode: added @bool stayInTreeAfterEditHeadline setting.
- Added Cmds:Toggle Settings submenu.
- Use emacs names in Cmds menu (and in some other places): allow single item in menu tables.</t>
<t tx="ekr.20060928172525.237">http://sourceforge.net/forum/message.php?msg_id=3935368</t>
<t tx="ekr.20060928172525.240">http://sourceforge.net/forum/message.php?msg_id=3935780

This greatly speeds searches that used to open many nodes.</t>
<t tx="ekr.20060928172525.252">http://sourceforge.net/forum/message.php?msg_id=3935981

@url nodes of the form::

    @url -- aComment
    
now get the actual url from the entire first line of body text.
Such url's need not be quoted if they contain spaces.

</t>
<t tx="ekr.20060928194633.1">The myLeoSettings.leo file is a way of ensuring that your customized settings are not altered when updating Leo from cvs or while installing a new version of Leo.  The myLeoSettings.leo acts much like Python's site-customize.py file.  The myLeoSettings.leo file will never be part of any Leo distribution, and it will never exist in Leo's cvs repository.  This solution is *much* better than tring to update leoSettings.leo with scripts.

Leo loads settings from myLeoSettings.leo *after* loading settings from leoSettings.leo files but *before* loading settings from the .leo file being opened.</t>
<t tx="ekr.20060928195040"></t>
<t tx="ekr.20060928195040.1">The following plugins are new in Leo 4.4.2 b2:
    
leo_to_rtf
leo_to_html
leoOPML  (At present, contained in leoOPML.leo instead of leoPlugins.leo)
paste_as_headlines
slideshow
word_count

The __saxRead__.py plugin is an **experimental** for use by EKR.
It will be folded into Leo's core in the near future.</t>
</tnodes>
</leo_file>
