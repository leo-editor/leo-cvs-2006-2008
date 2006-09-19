<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet ekr_stylesheet?>
<leo_file>
<leo_header file_format="2" tnodes="0" max_tnode_index="589" clone_windows="0"/>
<globals body_outline_ratio="0.5">
	<global_window_position top="91" left="387" height="816" width="848"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="ekr.20060918133516"><vh>(Native attributes)</vh>
<v t="ekr.20060904103412.7"><vh>__init__</vh></v>
<v t="ekr.20060916064339" a="M"><vh>vnodeAttributes</vh></v>
<v t="ekr.20060916115633" a="M"><vh>handleVnodeAttributes</vh></v>
<v t="ekr.20060918135304"><vh>restoreDescendentAttributes</vh></v>
</v>
<v t="ekr.20060918154842"><vh>Dump</vh></v>
<v t="ekr.20060904103412" a="E"
marks="ekr.20060904103412.6,ekr.20060916115633,ekr.20060916064339,"
expanded="ekr.20060904103412.6,ekr.20060904103721,ekr.20060904134958.179,"><vh>@thin __saxRead__.py</vh></v>
</vnodes>
<tnodes>
<t tx="ekr.20060904103412.7">def __init__ (self,c):
    
    self.c = c
    
    nativeTnodeAttributes = ('tx',)
    self.nativeVnodeAttributes = (
        'a','descendentTnodeUnknownAttributes',
        'expanded','marks','t','tnodeList',
        # 'vtag',
    )
    
    # Semantics
    self.currentVnode = None
    self.descendentExpandedList = []
    self.descendentMarksList = []
    self.descendentUnknownAttributesDictList = []
    self.topVnode = None
    self.txnToVnodeDict = {} # Keys are tnx's (strings).  Values are vnodes.</t>
<t tx="ekr.20060916064339"># The native attributes of &lt;v&gt; elements are a, t, vtag, tnodeList,
# marks, expanded and descendentTnodeUnknownAttributes.

def vnodeAttributes (self,attrs):
    
    node = self.node

    for bunch in self.attrsToList(attrs):
        name = bunch.name ; val = bunch.val
        if name == 't':
            aList = self.txnToNodesDict.get(val,[])
            aList.append(self.node)
            self.txnToNodesDict[val] = aList
            node.tnx = val
        else:
            node.attributes[name] = val
            # g.trace(name,len(val))</t>
<t tx="ekr.20060916115633"># The native attributes of &lt;v&gt; elements are a, t, vtag, tnodeList,
# marks, expanded and descendentTnodeUnknownAttributes.

def handleVnodeAttributes (self,node,v):
    
    d = node.attributes
    a = d.get('a')
    if a:
        # g.trace('a=%s %s' % (attrs,v.headString()))
        # 'C' (clone) and 'D' bits are not used.
        if 'M' in a: v.setMarked()
        if 'E' in a: v.expand()
        if 'O' in a: v.setOrphan()
        if 'T' in a: self.topVnode = v
        if 'V' in a: self.currentVnode = v

    s = d.get('tnodeList','')
    tnodeList = s and s.split(',')
    if tnodeList:
        # This tnode list will be resolved later.
        g.trace(v.headString(),len(tnodeList))
        v.tempTnodeList = tnodeList
        
    aDict = d.get('descendentTnodeUnknownAttributes')
    if aDict: self.descendentUnknownAttributesDictList.append(aDict)
    
    aList = d.get('expanded')
    if aList: self.descendentExpandedList.append(aList)
    
    aList = d.get('marks')
    if aList: self.descendentMarksList.append(aList)
        
    aDict = {}
    for key in d.keys():
        if key not in self.nativeVnodeAttributes:
            aDict[key] = d.get(key)
    if aDict: v.unknownAttributes = aDict</t>
<t tx="ekr.20060918133516">@

Native xml attributes are the attributes of &lt;v&gt; and &lt;t&gt; elements that are known
(treated specially) by Leo's read/write code. The only native attribute of &lt;t&gt;
elements is tx. The native attributes of &lt;v&gt; elements are a, t, vtag, tnodeList,
marks, expanded and descendentTnodeUnknownAttributes.
</t>
<t tx="ekr.20060918135304">def restoreDescendentAttributes (self,c):

    for aDict in self.descendentUnknownAttributesDictList:
        for tnx in aDict.keys():
            v = self.txnToVnodeDict.get(tnx)
            if v:
                v.t.unknownAttributes = aDict[tnx]
                b.t._p_changed = 1
            else: g.trace("can not find tnode: tnx = %s" % tnx,color="red")
    
    marks = {} ; expanded = {}
    for tnx in self.descendentExpandedList:
        v = self.txnToVnodeDict.get(tnx)
        if v: expanded[v.t]=v.t
        else: g.trace("can not find tnode: tnx = %s" % tnx,color="red")
        
    for tnx in self.descendentMarksList:
        v = self.txnToVnodeDict.get(tnx)
        if v: marks[v.t]=v.t
        else: g.trace("can not find tnode: tnx = %s" % tnx,color="red")
    
    if marks or expanded:
        # g.trace("marks",len(marks),"expanded",len(expanded))
        for p in c.all_positions_iter():
            if marks.get(p.v.t):
                p.v.initMarkedBit()
                    # This was the problem: was p.setMark.
                    # There was a big performance bug in the mark hook in the Node Navigator plugin.
            if expanded.get(p.v.t):
                p.expand()</t>
<t tx="ekr.20060918154842">createVnode: tnx ekr.20041001211817     v 24745136 v.t 24745328 body 74   Buttons &amp; settings
createVnode: tnx ekr.20060809090106     v 24747152 v.t 24744912 body 167  @button scripts.leo
createVnode: tnx ekr.20060427103457     v 24826064 v.t 24826000 body 42   @button settings.leo
createVnode: tnx ekr.20051025070722     v 24826128 v.t 24826032 body 25   @button Beautify
createVnode: tnx ekr.20051025091355     v 24826224 v.t 24826096 body 31   @button Spell
createVnode: tnx ekr.20050911112310     v 24826288 v.t 24826256 body 44   @button Save
createVnode: tnx ekr.20051201090822     v 24826352 v.t 24826320 body 0    @settings
createVnode: tnx ekr.20060608223159     v 24826448 v.t 24826416 body 99   @abbrev
createVnode: tnx ekr.20060402133032     v 24826512 v.t 24826480 body 0    @page http plugin
createVnode: tnx ekr.20060402133032.1   v 24826608 v.t 24826576 body 0    @bool http_active = False
createVnode: tnx ekr.20060402133032.2   v 24826672 v.t 24826640 body 0    @int  port = 8080
createVnode: tnx ekr.20060402133032.3   v 24826736 v.t 24826704 body 0    @string rst_http_attributename = 'rst_http_attribute'
createVnode: tnx ekr.20060611121126     v 24826768 v.t 24826544 body 368  @shortcuts for buttons in test.leo
createVnode: tnx ekr.20060612072938     v 24826832 v.t 24826800 body 267  @mode extract
createVnode: tnx ekr.20060625074330     v 24826896 v.t 24826864 body 0    @bool use_syntax_coloring = True
createVnode: tnx ekr.20060626085228     v 24826928 v.t 24826384 body 106  @@button Unit Test
createVnode: tnx ekr.20060809084033     v 24826992 v.t 24826960 body 515  @@button cvt to g.et
createVnode: tnx ekr.20060809104405     v 24827088 v.t 24827056 body 95   &lt;&lt; version history &gt;&gt;
createVnode: tnx ekr.20060809092023     v 24827152 v.t 24827120 body 0    test
createVnode: tnx ekr.20060809103738     v 24827248 v.t 24827216 body 67   test1
createVnode: tnx ekr.20060809103738.1   v 24827312 v.t 24827280 body 47   test2
createVnode: tnx ekr.20060809090508     v 24827344 v.t 24827184 body 1138 replace
createVnode: tnx ekr.20060809091749.72  v 24827440 v.t 24827408 body 122  &lt;&lt; handle string &gt;&gt;
createVnode: tnx ekr.20060809091749.73  v 24827504 v.t 24827472 body 577  &lt;&lt; handle g.es &gt;&gt;
createVnode: tnx ekr.20060814111542     v 24827376 v.t 24827024 body 24   @@button add-ed
createVnode: tnx ekr.20060918083159     v 24827568 v.t 24827536 body 515  @@button Clear uAs
createVnode: tnx ekr.20060904193613     v 24827632 v.t 24827600 body 0    zodb get/put buttons
createVnode: tnx ekr.20060913093930     v 24827728 v.t 24827696 body 362  @@button zodb-get-tree
createVnode: tnx ekr.20060913094532     v 24827792 v.t 24827760 body 400  @@button zodb-get-node
createVnode: tnx ekr.20060913094124     v 24827856 v.t 24827824 body 257  @@button zodb-put-tree
createVnode: tnx ekr.20060913094301     v 24827920 v.t 24827888 body 356  @@button zodb-put-node
createVnode: tnx ekr.20051120173230     v 24827664 v.t 24745264 body 0    Prototypes
createVnode: tnx ekr.20051120173230.1   v 24828016 v.t 24827984 body 0    Server stuff
createVnode: tnx ekr.20051116122352     v 24828112 v.t 24828080 body 0    @thin c:\AppServ\www\php-test.php
createVnode: tnx ekr.20051116133640     v 24828176 v.t 24828144 body 0    @thin c:\AppServ\www\form.html
createVnode: tnx ekr.20051116133640.1   v 24828240 v.t 24828208 body 0    @thin c:\AppServ\www\welcome.php
createVnode: tnx ekr.20051120173230.2   v 24828272 v.t 24828048 body 0    Diff stuff
createVnode: tnx ekr.20051116222849     v 24828368 v.t 24828336 body 101  Tools/Scripts/diff.py
createVnode: tnx ekr.20051116222849.1   v 24828464 v.t 24828432 body 388  &lt;&lt; diff declarations &gt;&gt;
createVnode: tnx ekr.20051116222849.2   v 24828528 v.t 24828496 body 1580 main
createVnode: tnx ekr.20051116222016.1   v 24828560 v.t 24828400 body 105  difflib.py
createVnode: tnx ekr.20051116222016.2   v 24828656 v.t 24828624 body 1097 &lt;&lt; difflib declarations &gt;&gt;
createVnode: tnx ekr.20051116222016.3   v 24828720 v.t 24828688 body 107  _calculate_ratio
createVnode: tnx ekr.20051116222016.4   v 24828784 v.t 24828752 body 4377 class SequenceMatcher
createVnode: tnx ekr.20051116222016.5   v 24828880 v.t 24828848 body 2678 __init__
createVnode: tnx ekr.20051116222016.6   v 24828944 v.t 24828912 body 220  set_seqs
createVnode: tnx ekr.20051116222016.7   v 24829008 v.t 24828976 body 665  set_seq1
createVnode: tnx ekr.20051116222016.8   v 24829072 v.t 24829040 body 713  set_seq2
createVnode: tnx ekr.20051116222016.9   v 24829136 v.t 24829104 body 2877 __chain_b
createVnode: tnx ekr.20051116222016.10  v 24829200 v.t 24829168 body 4557 find_longest_match
createVnode: tnx ekr.20051116222016.11  v 24829264 v.t 24829232 body 741  get_matching_blocks
createVnode: tnx ekr.20051116222016.12  v 24829328 v.t 24829296 body 540  __helper
createVnode: tnx ekr.20051116222016.13  v 24829392 v.t 24829360 body 1972 get_opcodes
createVnode: tnx ekr.20051116222016.14  v 24829456 v.t 24829424 body 1884 get_grouped_opcodes
createVnode: tnx ekr.20051116222016.15  v 24829520 v.t 24829488 body 862  ratio
createVnode: tnx ekr.20051116222016.16  v 24829584 v.t 24829552 body 1038 quick_ratio
createVnode: tnx ekr.20051116222016.17  v 24829648 v.t 24829616 body 406  real_quick_ratio
createVnode: tnx ekr.20051116222016.18  v 24829680 v.t 24828816 body 1660 get_close_matches
createVnode: tnx ekr.20051116222016.19  v 24829744 v.t 24829712 body 254  _count_leading
createVnode: tnx ekr.20051116222016.20  v 24829808 v.t 24829776 body 56   class Differ
createVnode: tnx ekr.20051116222016.21  v 24829904 v.t 24829872 body 3156 &lt;&lt; class Differ declarations &gt;&gt;
createVnode: tnx ekr.20051116222016.22  v 25620528 v.t 24829936 body 1059 __init__
createVnode: tnx ekr.20051116222016.23  v 25620592 v.t 25620560 body 1234 compare
createVnode: tnx ekr.20051116222016.24  v 25620656 v.t 25620624 body 161  _dump
createVnode: tnx ekr.20051116222016.25  v 25620720 v.t 25620688 body 512  _plain_replace
createVnode: tnx ekr.20051116222016.26  v 25620784 v.t 25620752 body 3729 _fancy_replace
createVnode: tnx ekr.20051116222016.27  v 25620848 v.t 25620816 body 323  _fancy_helper
createVnode: tnx ekr.20051116222016.28  v 25620912 v.t 25620880 body 897  _qformat
createVnode: tnx ekr.20051116222016.29  v 25620944 v.t 24829840 body 1419 IS_LINE_JUNK
createVnode: tnx ekr.20051116222016.30  v 25621008 v.t 25620976 body 322  IS_CHARACTER_JUNK
createVnode: tnx ekr.20051116222016.31  v 25621072 v.t 25621040 body 2410 unified_diff
createVnode: tnx ekr.20051116222016.32  v 25621136 v.t 25621104 body 3029 context_diff
createVnode: tnx ekr.20051116222016.33  v 25621200 v.t 25621168 body 1136 ndiff
createVnode: tnx ekr.20051116222016.34  v 25621264 v.t 25621232 body 12801 _mdiff
createVnode: tnx ekr.20051116222016.35  v 25621328 v.t 25621296 body 2609 class HtmlDiff
createVnode: tnx ekr.20051116222016.36  v 25621424 v.t 25621392 body 123  &lt;&lt; class HtmlDiff declarations &gt;&gt;
createVnode: tnx ekr.20051116222016.37  v 25621488 v.t 25621456 body 677  __init__
createVnode: tnx ekr.20051116222016.38  v 25621552 v.t 25621520 body 1046 make_file
createVnode: tnx ekr.20051116222016.39  v 25621616 v.t 25621584 body 1083 _tab_newline_replace
createVnode: tnx ekr.20051116222016.40  v 25621680 v.t 25621648 body 1800 _split_line
createVnode: tnx ekr.20051116222016.41  v 25621744 v.t 25621712 body 1056 _line_wrapper
createVnode: tnx ekr.20051116222016.42  v 25621808 v.t 25621776 body 776  _collect_lines
createVnode: tnx ekr.20051116222016.43  v 25621872 v.t 25621840 body 869  _format_line
createVnode: tnx ekr.20051116222016.44  v 25621936 v.t 25621904 body 412  _make_prefix
createVnode: tnx ekr.20051116222016.45  v 25622000 v.t 25621968 body 1828 _convert_flags
createVnode: tnx ekr.20051116222016.46  v 25622064 v.t 25622032 body 3191 make_table
createVnode: tnx ekr.20051116222016.47  v 25622096 v.t 25621360 body 852  restore
createVnode: tnx ekr.20051116222016.48  v 25622160 v.t 25622128 body 77   _test
createVnode: tnx ekr.20051117095207     v 25622192 v.t 24828592 body 255  diff children
createVnode: tnx ekr.20051117095207.1   v 25622288 v.t 25622256 body 144  a
createVnode: tnx ekr.20051117095207.2   v 25622352 v.t 25622320 body 140  b
createVnode: tnx ekr.20051130182536     v 25622224 v.t 24828304 body 0    IronPython stuff
createVnode: tnx ekr.20051130182536.1   v 25622448 v.t 25622416 body 13   batch file
createVnode: tnx ekr.20051130182412     v 25622544 v.t 25622512 body 172  @@file ironPythonTest.bat
createVnode: tnx ekr.20051130181738     v 25622576 v.t 25622480 body 528  @@file ironPythonTest.py
createVnode: tnx ekr.20051214093711     v 25622608 v.t 25622384 body 429  redemo
createVnode: tnx ekr.20060103102234     v 25622704 v.t 25622672 body 2108 notes
createVnode: tnx ekr.20051214094526     v 25622768 v.t 25622736 body 517  createFrame
createVnode: tnx ekr.20060525151008     v 25622800 v.t 25622640 body 253  Idle
createVnode: tnx ekr.20060513224436     v 25622864 v.t 25622832 body 281  xcc Examples
createVnode: tnx ekr.20060513224436.1   v 25622960 v.t 25622928 body 15   @xcc OpenGl.h
createVnode: tnx ekr.20060513224436.2   v 25623056 v.t 25623024 body 47   USE_OPENGL
createVnode: tnx ekr.20060513224436.3   v 25623120 v.t 25623088 body 482  Data Types
createVnode: tnx ekr.20060513224436.4   v 25623184 v.t 25623152 body 35   1.1
createVnode: tnx ekr.20060513224436.5   v 25623280 v.t 25623248 body 25905 Defs
createVnode: tnx ekr.20060513224436.6   v 25623344 v.t 25623312 body 20613 Procs
createVnode: tnx ekr.20060513224436.7   v 25623376 v.t 25623216 body 35   1.2
createVnode: tnx ekr.20060513224436.8   v 25623472 v.t 25623440 body 2030 Defs
createVnode: tnx ekr.20060513224436.9   v 25623536 v.t 25623504 body 2844 Procs
createVnode: tnx ekr.20060513224436.10  v 25623568 v.t 25623408 body 35   1.3
createVnode: tnx ekr.20060513224436.11  v 25623664 v.t 25623632 body 4779 Defs
createVnode: tnx ekr.20060513224436.12  v 25623728 v.t 25623696 body 2927 Procs
createVnode: tnx ekr.20060513224436.13  v 25623760 v.t 25623600 body 35   1.4
createVnode: tnx ekr.20060513224436.14  v 25623856 v.t 25623824 body 1932 Defs
createVnode: tnx ekr.20060513224436.15  v 25623920 v.t 25623888 body 2367 Procs
createVnode: tnx ekr.20060513224436.16  v 25623952 v.t 25623792 body 35   1.5
createVnode: tnx ekr.20060513224436.17  v 25624048 v.t 25624016 body 2712 Defs
createVnode: tnx ekr.20060513224436.18  v 25624112 v.t 25624080 body 991  Procs
createVnode: tnx ekr.20060513224436.19  v 25624144 v.t 25623984 body 1161 WGL
createVnode: tnx ekr.20060513224436.20  v 25624176 v.t 25622992 body 14   @xcc cltest\testprog
createVnode: tnx ekr.20060513224436.21  v 25624272 v.t 25624240 body 0    program
createVnode: tnx ekr.20060513224436.22  v 25624368 v.t 25624336 body 122  Header Directives
createVnode: tnx ekr.20060513224436.23  v 25624432 v.t 25624400 body 251  int WINAPI WinMain(HINSTANCE hinstance,HINSTANCE hprevin
stance,LPSTR lpcmdline,int ncmdshow);!
createVnode: tnx ekr.20060513224436.24  v 25624304 v.t 25624208 body 71   @xcc gcctest\testprog
createVnode: tnx ekr.20060513224436.21  v 25624496 v.t 25624240 body 0    program
createVnode: tnx ekr.20060513182414     v 25624528 v.t 25624464 body 13   @xcc test.py
createVnode: tnx ekr.20060424075707     v 25624560 v.t 25622896 body 310  pymacs
createVnode: tnx ekr.20060601171501     v 25641040 v.t 25641008 body 477  @@button Ipython
createVnode: tnx ekr.20060804105327.2   v 25641104 v.t 25641072 body 237  @@button xbrl XML FILE
createVnode: tnx ekr.20060804105327.15  v 25641200 v.t 25641168 body 295  &lt;&lt;LogPrep&gt;&gt;
createVnode: tnx ekr.20060804105327.7   v 25641264 v.t 25641232 body 36   &lt;&lt; xml decl &gt;&gt;
createVnode: tnx ekr.20060804105327.8   v 25641328 v.t 25641296 body 23   &lt;&lt; start tag open = xbrl &gt;&gt;
createVnode: tnx ekr.20060804105327.3   v 25641392 v.t 25641360 body 102  &lt;&lt; instance items &gt;&gt;
createVnode: tnx ekr.20060804105327.4   v 25641488 v.t 25641456 body 91   &lt;&lt; Sales &gt;&gt;
createVnode: tnx ekr.20060804105327.5   v 25641520 v.t 25641424 body 102  &lt;&lt; context elements &gt;&gt;
createVnode: tnx ekr.20060804105327.6   v 25641584 v.t 25641552 body 48   &lt;&lt; units element USD &gt;&gt;
createVnode: tnx ekr.20060804105327.9   v 25641648 v.t 25641616 body 0    (NS)
createVnode: tnx ekr.20060804105327.10  v 25641744 v.t 25641712 body 99   &lt;&lt; ifrs-gp-typ (NS) &gt;&gt;
createVnode: tnx ekr.20060804105327.11  v 25641808 v.t 25641776 body 90   &lt;&lt; ifrs-gp       (NS) &gt;&gt;
createVnode: tnx ekr.20060804105327.12  v 25641840 v.t 25641680 body 0    (CHAR)
createVnode: tnx ekr.20060804105327.13  v 25641936 v.t 25641904 body 18   &lt;&lt; start tag close (CHAR) &gt;&gt;
createVnode: tnx ekr.20060804105327.14  v 25641968 v.t 25641872 body 23   &lt;&lt; close tag = xbrl &gt;&gt;
createVnode: tnx ekr.20060908132217     v 25642000 v.t 25641136 body 422  decoraters
createVnode: tnx ekr.20060813125022     v 25642032 v.t 24827952 body 0    Tests
createVnode: tnx ekr.20060813110008     v 25642128 v.t 25642096 body 53   Tests of components
createVnode: tnx ekr.20060813110008.24  v 25642224 v.t 25642192 body 0    Body...
createVnode: tnx ekr.20060813110008.25  v 25642320 v.t 25642288 body 195  Replace body
createVnode: tnx ekr.20060813110008.26  v 25642384 v.t 25642352 body 97   Restore body
createVnode: tnx ekr.20060813110008.27  v 25642416 v.t 25642256 body 0    Tree...
createVnode: tnx ekr.20060813110008.28  v 25642512 v.t 25642480 body 193  Replace tree
createVnode: tnx ekr.20060813110008.29  v 25642576 v.t 25642544 body 88   Restore  tree
createVnode: tnx ekr.20060813110008.30  v 25642608 v.t 25642448 body 0    Log...
createVnode: tnx ekr.20060813110008.31  v 25642704 v.t 25642672 body 192  Replace log
createVnode: tnx ekr.20060813110008.32  v 25642768 v.t 25642736 body 140  Restore log
createVnode: tnx ekr.20060813110008.33  v 25642800 v.t 25642640 body 0    Icon bar
createVnode: tnx ekr.20060813110008.34  v 25642896 v.t 25642864 body 22   Replace icon bar
createVnode: tnx ekr.20060813110008.35  v 25642960 v.t 25642928 body 22   Restore icon bar
createVnode: tnx ekr.20060813124952     v 25642992 v.t 25642832 body 0    Status Line
createVnode: tnx ekr.20060813124952.1   v 25643088 v.t 25643056 body 25   hide
createVnode: tnx ekr.20060813124952.2   v 25643152 v.t 25643120 body 25   show
createVnode: tnx ekr.20060814111542.1   v 25643024 v.t 25642160 body 237  word-forward test
createVnode: tnx ekr.20060823084124     v 25643216 v.t 25643184 body 55   Cloned node lost after saving
createVnode: tnx ekr.20060823084124.1   v 25643312 v.t 25643280 body 21   @@thin cloneTest.txt
createVnode: tnx ekr.20060823084124.3   v 25643408 v.t 25643376 body 12   Node 3
createVnode: tnx ekr.20060823084124.2   v 25643504 v.t 25643472 body 8    &lt;&lt; Node 6 &gt;&gt;
createVnode: tnx ekr.20060823084124.4   v 25643536 v.t 25643440 body 0    Node 4
createVnode: tnx ekr.20060823084124.5   v 25643632 v.t 25643600 body 12   Node 5
createVnode: tnx ekr.20060823084124.2   v 25643696 v.t 25643472 body 8    &lt;&lt; Node 6 &gt;&gt;
createVnode: tnx ekr.20060823085903     v 25643344 v.t 25643248 body 145  abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrst
uvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890
createVnode: tnx ekr.20060824113849     v 25643664 v.t 25643568 body 16   Problem with unicode in body pane (but not in headline)
Stéphane
createVnode: tnx ekr.20060829092342     v 25643760 v.t 25643728 body 0    Colorizer
createVnode: tnx ekr.20060629154158.30  v 25643856 v.t 25643824 body 246  PHP
createVnode: tnx ekr.20060629154158.47  v 25643920 v.t 25643888 body 534  Python2
createVnode: tnx ekr.20060629154158.7   v 25643984 v.t 25643952 body 415  C
createVnode: tnx ekr.20060831162537     v 25644016 v.t 25643792 body 224  Unicode characters
createVnode: tnx ekr.20060831164855     v 25644112 v.t 25644080 body 0    @url http://www.fileformat.info/tip/microsoft/enter_unic
ode.htm
createVnode: tnx ekr.20060905073703     v 25644144 v.t 25644048 body 844  message box example
createVnode: tnx ekr.20060829105608     v 25644208 v.t 25644176 body 176  python colorizer bug
createVnode: tnx ekr.20060905074910.1   v 25644272 v.t 25644240 body 482  code-block-regex
createVnode: tnx ekr.20060908135210     v 25644336 v.t 25644304 body 0    UNL's in @url nodes
createVnode: tnx ekr.20060908105059     v 25644432 v.t 25644400 body 0    @url 'ZODB--&gt;@button zodb-write'
createVnode: tnx ekr.20060908110506     v 25644496 v.t 25644464 body 89   @url 'file: ./../../plugins/leoPlugins.leo#Plugins--&gt;Ico
n and status areas--&gt;@thin UNL.py--&gt;To do'
createVnode: tnx ekr.20060913145850     v 25644528 v.t 25644368 body 96   Use gnx as a zodb key
createVnode: tnx ekr.20060916145616     v 25644592 v.t 25644560 body 0    Unicode tests
createVnode: tnx ekr.20060917124957     v 25644688 v.t 25644656 body 62   test unicode escapes
createVnode: tnx ekr.20060916143436     v 25644752 v.t 25644720 body 297  @@button put utf-8
createVnode: tnx ekr.20060917121048     v 25644848 v.t 25644816 body 7    out utf-8
createVnode: tnx ekr.20060916145230     v 25644880 v.t 25644784 body 273  @@button get utf-8
createVnode: tnx ekr.20060917053354     v 25644976 v.t 25644944 body 7    in utf-8
createVnode: tnx ekr.20060916145148     v 25645008 v.t 25644912 body 304  @@button put utf-16
createVnode: tnx ekr.20060917121713     v 25669712 v.t 25669680 body 7    out utf-16
createVnode: tnx ekr.20060916142718     v 25669744 v.t 25645040 body 276  @@button get utf-16
createVnode: tnx ekr.20060917053354.1   v 25669840 v.t 25669808 body 7    in utf-16
createVnode: tnx ekr.20060918095502     v 25669776 v.t 25644624 body 87   test hash(fileIndex)
createVnode: tnx ekr.20060902072410     v 25669872 v.t 25642064 body 30   word patch
createVnode: tnx ekr.20060904110922     v 25669936 v.t 25669904 body 0    OPML buttons
createVnode: tnx ekr.20060904111037.1   v 25670032 v.t 25670000 body 131  @button opml-write
createVnode: tnx ekr.20060904111037     v 25670096 v.t 25670064 body 129  @button opml-read
createVnode: tnx ekr.20060918153353     v 25670128 v.t 25669968 body 0    @thin c:\prog\test\atThinTest.txt
createVnode: tnx ekr.20060918105210     v 25670192 v.t 25670160 body 7    @file c:\prog\test\tnodeListTest.txt
handleVnodeAttributes: @file c:\prog\test\tnodeListTest.txt 3
createVnode: tnx ekr.20060918105210.1   v 25670288 v.t 25670256 body 11   node 1
createVnode: tnx ekr.20060918105210.2   v 25670352 v.t 25670320 body 11   node 2
createVnode: tnx ekr.20060915095508     v 25670384 v.t 25670224 body 274  @button sax-read
createVnode: tnx ekr.20060917181520     v 25670480 v.t 25670448 body 195  compareTrees
createVnode: tnx ekr.20060917174553     v 25670544 v.t 25670512 body 464  compareNodes
resolveTnodeLists: &lt;vnode 25670192:'@file c:\prog\test\tnodeListTest.txt'&gt; ekr.20060918105210 &lt;tnode 25670160&gt;
resolveTnodeLists: &lt;vnode 25670288:'node 1'&gt; ekr.20060918105210.1 &lt;tnode 25670256&gt;
resolveTnodeLists: &lt;vnode 25670352:'node 2'&gt; ekr.20060918105210.2 &lt;tnode 25670320&gt;
restoreDescendentAttributes: can not find tnode: tnx = ekr.20060918153353.1,

208 nodes checked, 0 errors
compareTrees --------------------
done
</t>
</tnodes>
</leo_file>
