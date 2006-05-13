#@+leo-ver=4-thin
#@+node:ekr.20060513122450:@thin xcc_nodes.py

"""Integrate C/C++ compiler and debugger in a node."""

#@<< About this plugin >>
#@+node:ekr.20060513122450.1:<< About this plugin >>
#@@nocolor
#@+at 			
#@nonl
# X C++ Compiler nodes----
# PLEASE SEE http://xccnode.sourceforge.net/
#  The xcc_nodes.py plugins simplify the c++ syntaxe and integrate compiling
#  and debuging tools.
#  creation:
#  	The name of the headline is set to:
#  	@xcc projectname
#  	or
#  	@xcc projectname.ext
#  	As soon as "@xcc" is written in the headline a blank configuration is
#  written in the node.
#  	The optional extension (*.ext) set the kind of project the node will 
# build.
#  	Empty extension is equivalent to the "exe" extension.
#  		if ext == cpp,
#  			inflate name.cpp
#  			the node will attempt to build an executable
#  		if ext == h,
#  			inflate name.h
#  			the node will attempt to check the syntaxe of the header
#  		if ext == exe,
#  			this is equivalent to no ext at all
#  			inflate name.h and name.cpp
#  			the node will attempt to build an executable
#  		if ext == dll,
#  			inflate name.h and name.cpp
#  			the node will attempt to build a dynamic link library
#  		if ext == lib,
#  			inflate name.h and name.cpp
#  			the node will attempt to build a static link library
#  usage:
#  	The "@xcc" node support Leo's @others syntax but _NOT_ the sections
#  reference.
#  	The actual code is written in the childs of the main node and the code 
# generation is
#  	affected by headlines.
#  	Here are the rules:             (see examples for good understanding)
#  	- The "At" rule:
#  		if headline start with "@", the node and its childs are ignored.
#  	- The "Semicolon" rule:
#  		if a headline end with ";" and an other compatible rule is trigered in 
# the
#  same headline,
#  		the rule will be written in the source if there is one.
#  	- The "Comment" rule:
#  		if a headline start with "//", all its body and childs are commented out
#  in the form:
#  			/*headline
#  				body text
#  				and
#  				childs
#  				*/
#  		This rule is compatible with the semicolon rule
#  	- The "Function" rule:
#  		if a headline end with ")", the headline is used as funtion prototype, 
# the body and childs are encased automatically in the opening and closing 
# curly brace.
#  		"Class" and "Function" rules are disabled while in a "Function" rule. 
# This rule is compatible with the semicolon rule, except that if there is a
#  header
#  		in the project the function will always be declared in the header and
#  defined in the	source,appending "!" prevent declaration in header for 
# global function.
#  	- The "Class" rule:
#  		if a headline start with "class", a class is declared and opening and
#  closing curly brace
#  		automatically written, all the childs from this node are class members,
#  the functions are
#  		correctly dispatched between header and source (access specifier is
#  appended if it need to).
#  	- The "Default" rule:
#  		if a headline doesnt triger any of the preceeding rules, its headline is
#  written as a comment
#  		and the body and childs written "as is" in the form:
#  			//headline
#  				body text
#  				and
#  				childs
#  		This rule is compatible with the semicolon rule
# -> Config Panel reference :
# 	-> options : generally the most used options.
# 		-> Create files : Request that files should be inflated.
# 		-> Compile : Request that the project should be built using the configured 
# compiler.
# 			-> Seek first error : Attempt to locate the first error encountered.
# 		-> Execute : Request to run the built exe.
# 			-> Connect to pipe : Interface the built exe pipe to the node interface, 
# exe is simply spwned if unchecked.
# 		-> Debug : Request to run the built exe with the configured debugger 
# (overide the "Execute" option).
# 			-> Seek breapoints : Detect and "Goto" encountered breakpoints.
# 		-> Xcc verbose : Special verbose mode usefull to config the debugger and 
# widely used when coding the plugin
#  		-> Filter output : Filter compiler and debugger ouput, showing only error 
# and warning
# 		-> Colorize log : Colorize the output if checked, allowing easyer 
# browsing.
# - by Alexis Gendron Paquette
#@-at
#@nonl
#@-node:ekr.20060513122450.1:<< About this plugin >>
#@nl
#@<< version history >>
#@+node:ekr.20060513183934:<< version history >>
#@@nocolor
#@+at
# 
# v 0.1: Pierre Bidon, et. al.
# 
# v 0.2 EKR:
# - Add per-node controller class.  This required many changes.
# - Many stylistic changes.  Many more are coming.
#@-at
#@nonl
#@-node:ekr.20060513183934:<< version history >>
#@nl
#@<< imports >>
#@+node:ekr.20060513122450.4:<< imports >>
# from leoPlugins import *
# from leoGlobals import *
import leoPlugins
import leoGlobals as g

# from Tkinter import *
import Tkinter as Tk
from winsound import Beep as beep
import traceback
import os,sys,thread,threading,time,string,re
import tkFileDialog,tkMessageBox,tkSimpleDialog
import pickle,base64,zlib
#@nonl
#@-node:ekr.20060513122450.4:<< imports >>
#@nl

controllers = {}

if 1: # To be replaced by ivars
    #@    << globals >>
    #@+node:ekr.20060513122450.5:<< globals >>
    #@+others
    #@+node:ekr.20060513122450.9:Write Info
    FILE_HDR = ""
    FILE_FTR = ""
    
    CLASS_HDR = "//"+5*"------------------"+"\n"
    CLASS_OPN = ""
    CLASS_END = ""
    CLASS_FTR = ""
    
    FUNC_HDR = "//"+5*"------------------"+"\n"
    FUNC_OPN = ""
    FUNC_END = ""
    FUNC_FTR = ""
    #@nonl
    #@-node:ekr.20060513122450.9:Write Info
    #@+node:ekr.20060513122450.6:Process
    if os.name == "dos" or os.name == "nt":
        Encoding = "mbcs"
    else:
    	Encoding = "ascii"
    	
    #--------------------------
    ProcessList = []
    #@nonl
    #@-node:ekr.20060513122450.6:Process
    #@+node:ekr.20060513122450.16:Icons
    #@+node:ekr.20060513122450.17:Go
    Go_e = "S\'x\\xdam\\x8e\\xcbn\\x830\\x14D\\xf7\\xfcLk \\xb2\\xbc\\xe8\\xe2\\xda@\\xc4\\xd32\\xe0\\x90.!J\\xa1\\x04\\x02\\x04K\\x80\\xbf\\xbeV\\xd6\\x1d\\xe9\\xe8\\x8cf5\\xf9\\xe7p\\xe6\\xde\\xd0\\xf9\\x00\\x02R\\x01\\xc0\\x9b\\xbb\\xa3\\xf0\\xfdd@\\nWH5\\x95\\xe9\\x956\\xd6+\\xe6\\x844\\xdcl|\\xbf]\\x03\\xfd\\xb2\\t\\xc16r\\x96j \\xa7\\xe3f\\xe9\\xb9\\x90\\xea\\xfbH\\xb1[\\xf8\\xfa\\xa90v2\\xadG\\xf5\\xc2v\\xd6\\x7f\\x18\\x88\\x01\\x8d\\xaa\\xef\\x83\\xb9v\\x1es\\xdc\\xc1?a\\xdb[\\xd6\\xfb\\x11@X\\t(\\x19\\xdd\\xc35\\xa6\\xd4\\x83)\\x8d\\x1fG\\xeb\\x8a\\x98uB\\xa2K\\xd2\\xb5\\xc0#\\xf8\\xcd\\xe5xI\\x8ap\\x95\\xb1\\xdf\\x8b\\x15_\\x9eT\\xf8\\xac\\xf4X\\\'\\xd7\\xf9,\\xc0\\x92u\\x11\\xc0\\x81\\xf2i\\xd8\\xdbtIR\\xdaJw\\x9aD\\xbb\\xf1(b%\"\\xf5\\x02b\\x8b\\x7f\\x80n\\xa2E]\\xe1f~\\x00\\xe0\\xad_\\xd6\\x1f\\x96\\x88[)\'\np0\n."
    #@nonl
    #@-node:ekr.20060513122450.17:Go
    #@+node:ekr.20060513122450.18:StepIn
    StepIn_e = "S\'x\\xda\\x95\\xd0Ms\\x820\\x10\\x06\\xe0;\\x7f\\xa5\\x17\\x15\\xa6\\x0e\\x87\\x1e6\\x100|\\x9a\\xa4\\x0c\\xda\\x9bP\\x0b\\x02\\x82\"\\x18\\xf0\\xd77\\xe1\\xdaS3\\xf3dg\\x92\\xec\\xbb3a\\xab\\xc6\\x8d\\xed\\xa6\\xc4\\x00\\x14\\xa2\\x04 \\xce\\xae\\xfa\\x98\\x9d\\xf5a{^\\x0f\\xdbTy\\r\\x99\\x12+S\\xbe\\x95R\\xf3)\\r\\xd9\\xc6|J\\xb2\\xae\\xe5\\x93\\xb5\\xa6\\xb6\\xfe\\xb4\\x19n\\xa7\\xb4QZo\\xce\\x95\\xc6\\xe3\\x89Ry<\\xac\\xc8\\xac\\xe0\\x92\\xf0\\xc52I\\xca\\xf5\\xe1\\x95\\xeb\\xd1\\xe2\\xa4G\\xbd&sTV\\x7f\\xdcD\\x95\\x92\\xaa\\x84\\xfa\\xe6\\xf3\\xfaf\\xd1\\xda\\xb3h\\x85\\xa7\\x90\\xab\\x03\\x99\\xc3\\xea/\\x97\\x01\\xc5P\\x10\\x0b\\xfe.\\r\\xfe\\xb3,\\xb1\\x94\\xe5K\\x00H\\x05\\xb0\\xb7\\xd0D\\x1e>\\x02{\\xee\\xb8v\\x7f \\x01\\xc4A\\x05\\x159\\x8f^\\xd4\\xe8\\xb8+\\xef\\xcfQ5O\\x06\\xd0\\x10\\x17yq\\xddU\\xc4H(B(\\x19-\\x87N\\x82\\xcb\\x8e\\x82\\xf8c\\x8f\\x8aU\\xe8\\x072\\x9b\\x89\\x1d\\x08m\\x15\\xbb\\xc8f\\xc2\\xb7\\xf6\\xcc\\xeb.\\x07\\x84\\xcb\\x90\\xec\\x03Q\\xd0\\xb1\\xa4\\x989\\xf7\\x9f\\x16\\xdek,\\x1b>\\x9b\\xef\\xc0\\xb6\\x8f\\x1d=\\xc4\\xed\\xe5M\\x0e\\xe1\\x8c^Z\\xe4|\\xd2 j\\x10\\x1a\\xf8.\\xd3J\\xd1\\xcd\\x1e\\xb2\\rJb\\xd4\\x82i:\\x85 `?>\\xb4_\\xa4j\\x9b\\xc9\'\np0\n."
    #@nonl
    #@-node:ekr.20060513122450.18:StepIn
    #@+node:ekr.20060513122450.19:StepOver
    StepOver_e = "S\'x\\xda\\x95\\xd0Mo\\x830\\x0c\\x06\\xe0;\\xbf\\xa6|hh\\x87\\x1e\\x9c\\x10h`@\\x03\\xed(\\xbbA\\x86\\xc2\\x97J\\x05l\\x01~\\xfdHw\\x9f\\xb4Wz\\xec\\x8b-YN\\x0e\\xbd\\x17;}M\\x00\\x18DW\\x80\\xc8\\xae\\xf4\\xd9\\xce\\x94m.\\x95XY\\xb8\\xad\\xb8\\xca7\\xbf\\xed\\xb2We.\\rE\\xdfGuM\\x95\\xb1\\xccf\\xe5Q\\x18\\xf3\\xb8{\\x14Y\\xaf\\xdc\\x83\\x8c\\xdf\\xfd\\x95\\xf7\\xfez\\xed\\xe9\\x1a\\xb6t%5M\\x9f*s\\xb6+3\\xda\\xf8\\xae0#\\xb56j\\xb9\\xfe\\xbbz\\xed\\xfdTI\\xbbG\\x90v>f\\xed\\xf0\\x12\\xb7d\\t\\x93\\xee\\xc3K\\x80\\x11\\x10\\x14\\xc3\\xdf\\xd1\\xe0?\\xc1\\xf2\\xd9\\x9e/\\x01\\xa0\\x8d\\x847\\x8c\\x16:\\x05\\x08\\xe1uJ\\xb5\\xb1\\xc3IN]$\\x98\\x90\\\'\\x1f\\xa4\\xcc\\xc3\\xc0\\x850\\x8c\\x9a\\xba\\xa6A\\xec\\x92U\\xcf\\xc0At\\x10\\x11r\\x93\\xeb\\x019\\xc8bS\\x02\\x08\\x1f\\x863\\x96\\xcc\\xea.\\x1e\\x08\\xbd8a4hy\\x00\\x143\\xdf\\xee\\xef\\xb5\\xe0\\xd4\\xa3h\\xab\\x9c\\xf2\\xaba\\xef\\x1e\\xc6\\x84I\\xcag!\\xac\\x98\\x9cH\\xcbo\\x13\\x069Y\\xa9?b\\x03\\xce\\xedV[\\xc5%\\xac\\x97O\\xc2\\xb1!)\\xb9]4Q\\x87\\xab\\xe77\\xc2\\xca\\xf4\\xb30\\xf9\\xdb~\"\\xc4\\xf2x\\xd4~\\x00\\\'\\xed\\x9a\\xd0\'\np0\n."
    #@nonl
    #@-node:ekr.20060513122450.19:StepOver
    #@+node:ekr.20060513122450.20:StepOut
    StepOut_e = "S\"x\\xda\\x95\\xd0\\xddn\\x820\\x14\\xc0\\xf1{\\x9eF\\xc5\\x8c\\xedb\\x17\\xa7\\xa5`a\\x80\\x05;\\xd4;As\\xca\\x87\\x9bQ\\x94\\x8f\\xa7_\\xcb\\x1b\\xac\\xc9/\'9i\\xfeM\\x9a.Z?q[\\xc5\\x00\\x04\\xc4\\x12 )\\xae\\xf6\\xb3\\xb8\\xd8\\x9dsYvNnL]a$\\xc6P:\\xda\\xde{\\x95\\xf9\\x87\\xd1\\x15\\xab\\x8f\\x97\\xa6\\xe7\\xd2\\xd2\\xf7\\x96\\xc6\\xbd\\xc8;\\xe3vZiy\\xab\\x95?\\xc18k\\x83L\\xd6A\\x16\\xd5|\\x8c\\x14\\x1f\\x99\\xe2\\xd9\\xec\\xb2N\\x9d\\xf9U\\xad\\xb4\\xbb\\xc9*\\xedx2Nv|\\xd7\\x9d\\xd9a\\x15\\xd7F~\\x8duV\\x97\\x9a[\\x985\\x01\\x15\\xf5\\xef[R\\xb3!\\xca\\xccB\\xf7\\xd2\\xe6\\xe8\\xa7 \\x18 \\xa7\\x00`\\xc1\\x7f\\x0e\\xed\\xe71\\x7f\\t\\x00o\\x01\\xb6\\x94\\x0c\\\\\\xfa\\xd4E\\xc4\\xad\\xa5\\xb7\\x04\\x9b\\xfc\\x8b\\x02\\xde7A\\x8f\\xb8\\x90\\xa17E\\xef\\x8ce=6\\x8c\\xd0\\x1d[\\xec<\\xa2\\xb8\\xdc\\x10w|\\x84\\x02\\xf0\\xb6\\xe0\\xd2S4F\\xeaUp8\\xd1\\xe8\\x8ar\\x98\\xa0\\xea\\xad\\xa6<\\xb9(\\x90\\x9d_J\\x08\\xdf\\x150\\x9e/\\xacI\\x15J\\x97\\xba4\\x0f\\xfdjI c>\\xfb\\xe6\\x9b\\xfd/\\x0e\\x870\\x8a\\x08*2$\\x10\\x9c\\xf91\\xc3*>$t\\xbf\\x86\\xeaL,2\\xae\\xc6M\\xa3{O\\x07H\\xfa\\x90\\x94\\xef\\xa0/]_\\xb1\\xf2\\x8b\\xa0\\x80\\xa4\\xff\\xfc\\xb4\\xfe\\x00\\xd4\\xc7\\xa1 \"\np0\n."
    #@nonl
    #@-node:ekr.20060513122450.20:StepOut
    #@+node:ekr.20060513122450.21:Pause
    Pause_e = "S\'x\\xda\\x95\\xceKn\\x830\\x18\\x04\\xe0=\\x97i\\xf3t\\xba\\xc8\\xe2\\xb7\\t\\xc6N\\xb0e\\x08\\x02\\x96\\x85\\x02\\x86:\\x84\\x14Wn9}Q{\\x82\\x8e\\xf4I\\xb3\\x19i\\xe2gC\\xa5o\\xf4\\t@A\\xa4\\x00\\x04\\xaa7\\x16e+[f\\xbb\\xc5f1\\xdbR.]\\xce\\x13Z\\xe4\\xc1\\xcb!\\x0f\\xd0>3\\x03OR\\xc3\\x92\\x93\\t-\\xeaC1{\\x9a\\x8a\\xfeim?\\xea\\xb5\\xedM\\xc0\\x93\\xda\\xc1\\xffC\\xfeF\\xde\\xef#\\x00V(\\x10\\x04\\x7f\\xb1\\xe9\\xec\\xe3\\xd6U\\xb9\\x0c}\\xd82B\\xb4\\xdaJ\\xca\\xaf\\xeeN\\x19&8m8\\xef\\x8aT\\xf9\\xb4\\xd3\\xd3%}\\xcc\\xf7(\\x13\\xac\\xed\\xa2\\xc6\\x80\\xday\\xef\\xcc\\x07\\x03\\xac\\xba\\xc9\\x98\\x1d\\x1e\\x82\\xde\\xba\\xd1\\x0e\\xda\\xb1\\xf4\\xbb\\x91\\xe6Z]\\xe2\\xcf\\xbe(h\\x89\\xc1\\x9d\\x13\\xdc\\xb7N\\x91\\x81\\x8c\\x8e\\xbf\\xd11~\\x8d\\x08\\x80t\\xc7\\xa3\\xf7\\x03\\xce\\xc7^\\x95\'\np0\n."
    #@nonl
    #@-node:ekr.20060513122450.21:Pause
    #@+node:ekr.20060513122450.22:Stop
    Stop_e = "S\'x\\xda-\\x8c\\xc1\\x8e\\x820\\x14E\\xf7\\xfc\\x8c\\xa2\\x18\\xdc\\xb8x\\x14h\\x0b%\\x0e4LSv`\\xb4O@t\\xa4\\x19\\x18\\xbe~&d\\xee\\xe2\\x9c\\xe4,n\\xb1\\xed\\xe99\\xec1\\x02\\xc8Ad\\x00\\xe7\\xe6\\xb1\\xb7\\xfe\\xd5\\xb5\\xbeZl\\xa3\\x96\\xaf\\x9d}\\xd5\\xaal\\xd9_\\xdc\\xdb\\xb7>\\x1eR~\\xf9$\\xb4q\\t\\xbdx3\\x88\\xed\\x0b\\xfe\\xe7\\xac$\\xd3\\xaa\\xf5\\x10\\x80\\xab\\x1c\\x18\\tf>\\xa6a`&\\x9d\\xb0\\xb8\\xe5\\x1d\\xa5\\x811Z\\x8b\\x04y\\xa78\\x18\\x8c\\xde\\xb5\\x91P\\xd6\\t\\xbd\\xe3\\xc4\\xaa\\xef\\xc9s\\xb2Z\\x02\\xc8l\\xb8\\xde\\x97\\xaa\\x93\\x85\\xe8\\xe4\\xb8A\\x94\\xba|T\\xa2_2\\x16\\xc5$\\x7f\\xa6\\xb7\\x8f\\xc1\\xe0\\x0f13X\\x8a\\x05F&\\x1eZ\\xe9Y\\x1a\\x00\\x84\\xe3\\xc9\\xf9\\x05\\x1a\\x01HO\'\np0\n."
    #@nonl
    #@-node:ekr.20060513122450.22:Stop
    #@+node:ekr.20060513122450.23:Watch
    WatchData = "S\"x\\xda\\x95\\x90\\xdbr\\x820\\x10@\\xdf\\xf9\\x1a\\xc1Z\\xea\\xe3&\\x86\\x8b\\x96\\x8bf\\x18\\x8coBk \\xa4B!\\x8a\\xc9\\xd77\\xfa\\x07\\xdd\\x99\\xb3g\\xf7ewg\\x0f\\x0b\\x19f\\x1b\\xd9\\x10\\x80=\\xa4\\x05@Z\\x95\\xae\\xaaJ\\xa3\\xaa\\xec\\xc9\\xa3\\xf633\\xf9\\xd6\\xc7\\xcc\\x9d\\xfc\\xc0:p\\xa7c`,\\xf7\\xca\\xd6\\xa3\\xb7\\xbeW\\xdeZ\\x9d\\xbd\\xb5\\xb3\\xfc-\\xd7\\x16w5h\\x0bu\\xfdwO\\x8d\'\\xad\\xcco)\\x07F\\xe5\\xaa\\xd7\\xd2\\xf4T.\\x07Z\\x8fL\\xd7\\x8a\\xd1\\xfa~\\xd2\\x85\\xdc\\xd2\\xe2j\\x11\\xb1NDL\\x9f\\x10\\xe7\\x99\\x9a\\xe8Fd\\x94\\x91\\xe1x#\\xc2\\xfaj\\xfb&R~\\x13\\xa5\\xbe\\xb0X\\x9b\\xefejjO\\x99&T\\xe3\\xd9\\x1d\\x04\\xf3\\xd2\\xb3]g\\xb1\\x13\\xbbaG9\\x80\\x03\\xff\\t<\\xbf\\xf4z\\t@\\xdc\\x00D\\x18=\\x18\\xdbm\\x10\\x9f\\x07\\xe2\\xf4\\xb8El\\xda\\xda\\xe6\\xab,\\x82\\x16b\\x12F\\x98\\x7f\\x04|\\x143#\\x04\\x03\\x97\\x19N\\xda>\\xee>\\xa3\\x96s\\x9d$-\\xdbw1A\\xb3j\\xcfR\\xac\\x12\\xa0!\\xc6\\xec\\x92#~p\\xdeB\\x84\\x10]L\\xb7X\\xf3\\xbe\\xc8s\\x01\\x8f\\xe2\\x07o\\x0eo\\xfdq#`\\x9f\\x07!\\x1cz\\x8d\\n>\\xbb\\xdd\\xe5\\xb3y\\xef\\x92,Ar\\xde\\xdez\\xd4\\xa4\\xa5)\\xc7\\x92\\x04\\xdfWx\\xd4\\x1d:9\\xdcey\\x84\\x16{{\\xba\\xef\\xfc\\x01\\xdb\\xb2\\x9a\\xfc\"\np0\n."
    #@nonl
    #@-node:ekr.20060513122450.23:Watch
    #@+node:ekr.20060513122450.24:Config
    ConfigData = "S\'x\\xdaU\\xce\\xc1r\\x820\\x14\\x85\\xe1=O\\x03\\xd6\\x11\\xbb\\xbc\\t\\x84\\x06\\x0c\\x99@-\\xda\\x1d\\xa4N\\x10(j\\xc9\\x10\\xe0\\xe9k\\xd8yg\\xbe\\xb9\\x9b\\x7fq2\\xb7\\x8bx\\xd0\\xd5!\\x80\\x00&\\x00R\\xff\\xe2i\\xbf\\xf0tU,\\xba\\xe2\\xd6$}\\x8b\\x8c\\xf2D\\xa6\\xa7Q\\x16\\xefc\\xb5\\xb1l\\xe6\\xfd\\x95\\x1bm9\\xf7\\xb2\\xe8\\xfa\\xa4\\x90}<\\xaf::\\xb3\\x86\\xcea\\xfd\\xa1\\xfd\\xcb[\\xba\\xc8\\xb5K\\x9b\\xb3g\\xcb8?\\xb6\\xf7$W\\xf0z\\xd8\\xac\\xcfY\\x17\\x01\\xd0\\n \\xc68S7\\x16\\x802\\x8a\\xd0\\x01\\x1b\\x8a\\tF\\x8aR\\xce@\\x18N\\x00+\\x97\\x8a\\x14\\xc0$1\\xa0\\xba\\x1d\\xcaC-\\xdc\\x9c#\\x04\\xfbG\\x19\\xd57\\xe7\\xf8\\x0b(@\\xed\\x105\\x0b=3\\x1ev\\x8a\\xf5\\x15\\xc1\\xd0\\xee\\xd1!\\x80t\\xc74R\\xe2Hq\\x8f\\x94\\xfb\\xc5\\xae`\"\\x81\\x82O\\xd3d\\xd1\\xf5[\\xe5\\x12=\\xa6\\xed\\xcf)\\x84m\\xbb\\x1b\\x03\\xe7\\xb9\\xd8w\\xfe\\x01*\\x83e%\'\np0\n."
    #@nonl
    #@-node:ekr.20060513122450.24:Config
    #@+node:ekr.20060513122450.25:Prompt
    Prompt_e = "S\'x\\xda\\xad\\x90\\xcdn\\xab0\\x14\\x84\\xf7\\xbcJ\\x16\\xb9I\\xdbp\\xbb\\xe8\\xe2p\\xb0\\x8d\\xe1\\xf2\\xe3:\\xb4%;\\x12r\\r\\x86\\x14Zh\\x0cy\\xfa\\x92\\xf6\\t*\\xf5\\x93F\\xa3\\x91F\\xb3\\x98\\xc7?\\r\\x8b\\xdd\\xa6d\\x02\\x04D)@\\xb2\\x9c\\xf9\\x7fs\\xbfX\\x9e\\xed\\xc5\\xfet7\\xd8\\xc7\\x9ba\\xff\\xbc\\x9au\\xe9\\xed\\xf8\\xd2\\xbf\\xd0\\xf1\\x1a\\xf3\\xe7\\xa6\\xdbM\\x87W\\x7f:4|\\n5\\x97\\xc4*\\xbdk;\\xba\\x1c\\xd6\\xc3{>+[\\x0f:[G:[us\\xdd\\x97i\\xdd\\x05\\xb2\\xf6Q\\xe8v\\x13W\\xd7@J.\\x00\\x96c\\xbdc\\x8f \\x08(\\x8e\\xf0\\x8d\\x05\\xbf\\xc8\\xcf\\xc6\\xd0|\\xd9\\xd7%\\x00\\xfcm>\\x86\\xc5\\x0e\\xf4\\x81\\xeb(\\xa3\\xa8\\x85\\xf5\\x96\\xf7\\x01E\\x18y%\\xbb\\x91\\xf7G\\xdfE\\tSq\\xaeD\\x9f\\\'\\x9e\\x1e\\xf9G\\xd1\\x18q\\x9b\\\'\\xbe\\xae\\xc8S\\xd6Om\\x9b\\xba\\x1e:w\\xf1\\xae6\\x1da\\xa1\\x87\\x08\\xe2%\\xacn-\\x11\"\\xbaXli\\x0b\\xdc\\xb4\\x1c\\xdc1\\x13E\"D{@\\x07+\\x88\\\\L\\x03\\xf5\\x11zP\\xf6\\x9b\\xfd+(Ch\\xdaH\\xf8k\\xc3vl\\x81q45\\x8bC\\xbd\\x19d\\xce-TNU\\x94\\xda@J\\xa8\\xae)U\\\'\\xf8\\x97)BOR\\xaf\\xa0\\xdb\\xf9\\xf5\\xe2]\\x9d\\x19$|\\xb4\\x03\\xc5\\x02R\\x95\\xfc\\xb8]\\x0b\\x15I\\x80\\xd8<<X\\x9fJ\\x0f\\xa2\\xed\'\np0\n."
    #@nonl
    #@-node:ekr.20060513122450.25:Prompt
    #@-node:ekr.20060513122450.16:Icons
    #@+node:ekr.20060513122450.26:Colors
    ErrorColor = "#%02x%02x%02x" % (255,200,200)
    BreakColor = "#%02x%02x%02x" % (200,200,255)
    LineNumColor = "#%02x%02x%02x" % (200,200,255)
    RegExpFgColor = "#%02x%02x%02x" % (0,0,255)
    VarSupBgColor = "#%02x%02x%02x" % (255,230,230)
    #@nonl
    #@-node:ekr.20060513122450.26:Colors
    #@-others
    #@nonl
    #@-node:ekr.20060513122450.5:<< globals >>
    #@nl

#@@language python
#@@tabwidth -4

__version__ = "0.2"

#@+others
#@+node:ekr.20060513153648:Documentation
#@+node:ekr.20060513122450.2:Known Flaws
#@@nocolor
#@+at 
# 
# *** Most flaw can be worked around by using "default" node(or rule) and 
# writing all	code inside it.
#  (default rule -> comment out headline & write body "as is")
# - the currently selected node Info is refreshed in a leasy way when editing 
# headline or body.
# - line number refresh isnt 100% accurate when editing text in the body.
# - Breakpoints can only be Added/deleted, Enabling/Disabling isnt supported 
# yet.
# - code auto dispath feature wont work as expected with template class and 
# function.
# - class is the only structural keyword supported in the tree to date, union, 
# struct and enum dont trigger any rule.
# - DLL debugging is untested to date, it surely dont work.
# - Untested on Linux, see linPause and aPause functions.
#@-at
#@nonl
#@-node:ekr.20060513122450.2:Known Flaws
#@+node:ekr.20060513122450.3:Future Features
#@@nocolor
#@+at
# 
# - C/C++ code/project importer/merger
# - "Document" rule -> auto inflating/compiling html(possibly .chm) 
# documentation for the project.
# - Display external files if needed.(external error or similar)
# - "Browse Info" management allowing declaration/references to be searched 
# and displayed.
# - Automation of precompiled headers, possibly using a "#PCH" node.
# - in the debugger regular expression/task list:
#     reg exp:
#         if a group named "FOO" is returned by the regular
#         expression, then the "_FOO_" variable is supported
#         by the corresponding "Task" line.
#     Task:
#         Apart from those defined by the corresponding regular	expression,
#@-at
#@-node:ekr.20060513122450.3:Future Features
#@-node:ekr.20060513153648:Documentation
#@+node:ekr.20060513142641:Module level
#@+node:ekr.20060513123144:init
def init ():
    
    data = (
        (("new","open2"), OnCreate),
        # ("start2",      OnStart2),
        ("select2",     OnSelect2),
        ("idle",        OnIdle),
        ("command2",    OnCommand2),
        ("bodydclick2", OnBodyDoubleClick),
        ("bodykey2",    OnBodyKey2),
        ("headkey2",    OnHeadKey2),
        ("end1",        OnQuit),
    )
    
    for hook,f in data:
        leoPlugins.registerHandler(hook,f)

    g.plugin_signon(__name__)

    return True


#@-node:ekr.20060513123144:init
#@+node:ekr.20060513122450.395:Module-level event handlers
#@+node:ekr.20060513122450.397:OnCreate
def OnCreate(tag,keywords):
    
    g.trace(keywords)
    c = keywords.get("c")
    if c:
        controllers [c] = controllerClass(c)
#@nonl
#@-node:ekr.20060513122450.397:OnCreate
#@+node:ekr.20060513122450.396:OnStart2 (No longer used)
if 0:
    def OnStart2(tag,keywords):
        try:
            if XCC_INITED == False:
                c = keywords.get("c")
                InitXcc(c)
                n = c.currentPosition()
                h = n.headString()	
                
        except Exception,e:
            TraceBack()
#@nonl
#@-node:ekr.20060513122450.396:OnStart2 (No longer used)
#@+node:ekr.20060513122450.398:OnSelect2
def OnSelect2(tag,keywords):
    
    global controllers
    c = keywords.get("c")
    controller = controllers.get(c)
    controller and controller.onSelect()
#@nonl
#@-node:ekr.20060513122450.398:OnSelect2
#@+node:ekr.20060513122450.399:OnIdle
def OnIdle(tag,keywords):
    
    global controllers
    c = keywords.get("c")
    controller = controllers.get(c)
    controller and controller.onIdle()
#@nonl
#@-node:ekr.20060513122450.399:OnIdle
#@+node:ekr.20060513122450.400:OnCommand2
def OnCommand2(tag,keywords):
    
    global controllers
    c = keywords.get("c")
    controller = controllers.get(c)
    controller and controller.onCommand2(keywords)
#@nonl
#@-node:ekr.20060513122450.400:OnCommand2
#@+node:ekr.20060513122450.401:OnBodyDoubleClick
def OnBodyDoubleClick(tag,keywords):
    
    global controllers
    c = keywords.get("c")
    controller = controllers.get(c)
    controller and controller.onBodyDoubleClick()
#@nonl
#@-node:ekr.20060513122450.401:OnBodyDoubleClick
#@+node:ekr.20060513122450.402:OnBodyKey2
def OnBodyKey2(tag,keywords):
    
    global controllers
    c = keywords.get("c")
    controller = controllers.get(c)
    controller and controller.onBodyKey2(keywords)
#@nonl
#@-node:ekr.20060513122450.402:OnBodyKey2
#@+node:ekr.20060513122450.403:OnHeadKey2
def OnHeadKey2(tag,keywords):
    
    global controllers
    c = keywords.get("c")
    controller = controllers.get(c)
    controller and controller.onHeadKey2(keywords)
#@nonl
#@-node:ekr.20060513122450.403:OnHeadKey2
#@+node:ekr.20060513122450.404:OnQuit
def OnQuit(tag,keywords):
    
    global controllers
    for key in controllers.keys():
        controller = controllers.get(key)
        controller.onQuit()
#@nonl
#@-node:ekr.20060513122450.404:OnQuit
#@-node:ekr.20060513122450.395:Module-level event handlers
#@+node:ekr.20060513122450.27:OS Specific Funcs
#@+node:ekr.20060513122450.28:winPause
def winPause(pid):
    
	import ctypes

	hp = ctypes.windll.Kernel32.OpenProcess(0x1F0FFF,0,int(pid))
	if hp == 0:
		Error("xcc: ","can't open process: "+str(long(ctypes.windll.Kernel32.GetLastError())))
		return
	
	if ctypes.windll.Kernel32.DebugBreakProcess(hp) == 0:
		Warning("xcc: ","Unable to break into the target!")
		return
#@nonl
#@-node:ekr.20060513122450.28:winPause
#@+node:ekr.20060513122450.29:linPause
def linPause(pid):	# theorical way to do it, untested!

	import signal
	os.kill(pid,signal.SIGINT)
#@nonl
#@-node:ekr.20060513122450.29:linPause
#@-node:ekr.20060513122450.27:OS Specific Funcs
#@+node:ekr.20060513142641.1:Helpers
#@+node:ekr.20060513122450.32:GetNodePath
def GetNodePath(node,as="->"):

	path = []
	for p in node.parents_iter():
		path.insert(0,p.headString()+as)

	path.append(node.headString())
	return ''.join(path)
#@nonl
#@-node:ekr.20060513122450.32:GetNodePath
#@+node:ekr.20060513122450.33:AddText
def AddText(text,node):

	node.setBodyTextOrPane(node.bodyString()+text)
	l,c = LeoBody.index("end").split(".")
	LeoBody.see(l+".0")
#@nonl
#@-node:ekr.20060513122450.33:AddText
#@+node:ekr.20060513122450.34:Error
def Error(module,error):
	g.es(module,newline = False,color = "blue")
	g.es(error,color = "red")
#@-node:ekr.20060513122450.34:Error
#@+node:ekr.20060513122450.35:Warning
def Warning(module,warning):

	g.es(module,newline = False,color = "blue")
	g.es(warning,color = "orange")
#@nonl
#@-node:ekr.20060513122450.35:Warning
#@+node:ekr.20060513122450.36:Message
def Message(module,warning):

	g.es(module,newline = False,color = "blue")
	g.es(warning)
#@-node:ekr.20060513122450.36:Message
#@+node:ekr.20060513122450.37:GetUnknownAttributes
def GetUnknownAttributes(vnode,create = False):

	if hasattr(vnode,"unknownAttributes") != True:
		if create == True:
			vnode.unknownAttributes = {}
		else:
			return None
	return vnode.unknownAttributes
#@nonl
#@-node:ekr.20060513122450.37:GetUnknownAttributes
#@+node:ekr.20060513122450.38:GetDictKey (not used)
if 0:
    def GetDictKey(dic,key,create=False,init=""):
        if key in dic:
            return dic[key]
        else:
            if create == True:
                dic[key] = init
                return dic[key]
            else:
                return None
#@nonl
#@-node:ekr.20060513122450.38:GetDictKey (not used)
#@+node:ekr.20060513122450.39:TraceBack
if 0:
    def TraceBack():
        typ,val,tb = sys.exc_info()
        lines = traceback.format_exception(typ,val,tb)
        for line in lines:
            # g.es(line,color = "red")
            print line
            
TraceBack = g.es_exception
#@nonl
#@-node:ekr.20060513122450.39:TraceBack
#@+node:ekr.20060513122450.40:DecompressIcon
def DecompressIcon(data):
	try:
		#unpickle
		zdata = pickle.loads(data)	
		#unzip
		return zlib.decompress(zdata)	#return a base64
	except Excetion:
		Traceback()
#@-node:ekr.20060513122450.40:DecompressIcon
#@+node:ekr.20060513122450.41:CompressIcon
#@+at
# # Encode to base64, zip the data in a string and finally pickle it to be 
# free from illegal char
# #the inflated file is a literal(without the quote)
# #to be embeded in code and passed to DecompressIcon func before use.
# 
# #to use:
# 	# remove "@" at the top
# 	# ctrl+e (execute script)
# 	# choose the file to translate, press save
# 	# open choosedfile.lit in notepade, select all(ctrl+a), copy(ctrl+c), close 
# notepade
# 	# paste(ctrl+v) where you needed your literal (dont forget to add the 
# quote)
# 
# from leoGlobals import *
# import tkFileDialog
# from pickle import *
# from base64 import *
# from zlib import *
# import os
# 
# 
# try:
# 	ft = ('All Files', '.*'),
# 	s = tkFileDialog.askopenfilename(filetypes=ft,title="Select file to 
# convert...")
# 	if s != None and s != "":
# 		f = file(s,"rb")
# 		data = f.read()
# 		f.close()
# 		b64data = encodestring(data)
# 		zdata = compress(b64data,9)
# 		pdata = dumps(zdata)
# 		pdata = pdata.replace("\\","\\\\")
# 		pdata = pdata.replace("\'","\\\'")
# 		pdata = pdata.replace("\"","\\\"")
# 		pdata = pdata.replace("\n","\\n")
# 		name,ext = os.path.splitext(s)
# 		f = file(name+".lit","wb")
# 		f.write(pdata)
# 		f.close()
# except Exception,e:
# 	g.es(str(e))
#@-at
#@nonl
#@-node:ekr.20060513122450.41:CompressIcon
#@-node:ekr.20060513142641.1:Helpers
#@+node:ekr.20060513122450.388:Xcc Funcs
#@+node:ekr.20060513122450.389:GetXccNode
def GetXccNode(node):

	for p in node.parents_iter():
		h = p.headString()
		if (h[0:5] == "@xcc "):
			return p
	
	return None
#@-node:ekr.20060513122450.389:GetXccNode
#@+node:ekr.20060513122450.390:IsXcc
def IsXcc(node):

	if node.headString()[0:5] == "@xcc ":
		return True
	else:
		return False
#@-node:ekr.20060513122450.390:IsXcc
#@+node:ekr.20060513122450.392:UpdateProcess
def UpdateProcess():
	global ProcessList
	if len(ProcessList) != 0:
		p = ProcessList[0]
		if p.Update() == True:
			return
		else:
			if p.Close() != None:
				ProcessList = []		#reset 
			else:
				ProcessList.pop(0)
				if len(ProcessList) != 0:					
					if ProcessList[0].Open() != True:	#load next
						ProcessList = []		#reset
#@-node:ekr.20060513122450.392:UpdateProcess
#@+node:ekr.20060513122450.393:ReplaceVars
def ReplaceVars(exp):
	exp = exp.replace("_NAME_",NAME)
	exp = exp.replace("_EXT_",EXT)
	exp = exp.replace("_ABSPATH_",ABS_PATH)#.replace("\\","\\\\"))
	exp = exp.replace("_RELPATH_",REL_PATH)#.replace("\\","\\\\"))
	exp = exp.replace("_SRCEXT_",SRC_EXT)
	
	return exp
	
#@nonl
#@-node:ekr.20060513122450.393:ReplaceVars
#@+node:ekr.20060513122450.394:ImportFiles
def ImportFiles():

	Warning("TODO: ","Add import code in ImportFiles function!")
#@nonl
#@-node:ekr.20060513122450.394:ImportFiles
#@-node:ekr.20060513122450.388:Xcc Funcs
#@-node:ekr.20060513142641:Module level
#@+node:ekr.20060513122450.42:Classes
#@+node:ekr.20060513141418:class controllerClass
class controllerClass:

    #@    @+others
    #@+node:ekr.20060513142641.2:controller.ctor
    def __init__ (self,c):
        
        self.c = c
        
        #@    @+others
        #@+node:ekr.20060513122450.7:Xcc Core
        self.XCC_INITED = False
        
        self.ACTIVE_NODE = None
        self.ACTIVE_DICT = None
        self.ACTIVE_PROCESS = None
        
        self.SELECTED_NODE = None
        self.SELECTED_DICT = None
        
        self.LOCATE_CHILD = True
        self.CHILD_NODE = None
        self.CHILD_DICT = None
        self.CHILD_LINE = None
        self.CHILD_EXT = None
        
        self.Parser = None
        #@nonl
        #@-node:ekr.20060513122450.7:Xcc Core
        #@+node:ekr.20060513122450.8:Browse Info
        self.NAME = ""
        self.EXT = ""
        self.SRC_EXT = ""
        self.ABS_PATH = ""
        self.REL_PATH = ""
        self.CWD = ""
        self.PARSE_ERROR = ""
        self.PARSE_ERROR_NODE = None
        #@nonl
        #@-node:ekr.20060513122450.8:Browse Info
        #@+node:ekr.20060513122450.10:Compile Info
        self.FIRST_ERROR = False
        self.CPL = None
        #@nonl
        #@-node:ekr.20060513122450.10:Compile Info
        #@+node:ekr.20060513122450.11:Debug Info
        self.DBG = None
        
        self.DEBUGGER = ""
        self.TARGET_PID = ""
        
        self.DBG_RUNNING = False
        self.DBG_PROMPT = False
        
        self.DBG_TASK = []
        self.DBG_SD = []
        self.DBG_RD = []
        self.PROMPT_RD = []
        
        self.DBG_STEPPING = False
        self.WATCH_TASK = None
        
        #	pipe char buffering
        self.OutBuff = ""
        self.ErrBuff = ""
        #@nonl
        #@-node:ekr.20060513122450.11:Debug Info
        #@+node:ekr.20060513122450.12:Execute Info
        self.EXE = None
        #@nonl
        #@-node:ekr.20060513122450.12:Execute Info
        #@+node:ekr.20060513122450.13:Options
        self.FILTER_OUTPUT = "False"
        self.VERBOSE = "False"
        self.OPTS = {}
        #@nonl
        #@-node:ekr.20060513122450.13:Options
        #@+node:ekr.20060513122450.14:Widgets
        self.ToolBar = None
        self.BreakBar = None
        self.Watcher = None
        self.Config = None
        #@nonl
        #@-node:ekr.20060513122450.14:Widgets
        #@-others
        
        self.initXcc(c)
    #@nonl
    #@-node:ekr.20060513142641.2:controller.ctor
    #@+node:ekr.20060513122450.391:initXcc
    def initXcc(self,c):
    
        self.CWD = os.getcwd()
        self.LeoTop = c
        self.LeoFrame = c.frame	
    
        self.LeoBodyText = self.LeoFrame.body.bodyCtrl
        self.LeoYBodyBar = self.LeoFrame.body.bodyBar
        self.LeoXBodyBar = self.LeoFrame.body.bodyXBar
        
        g.trace(c,self.LeoBodyText)
    
        self.LeoFont = self.LeoBodyText["font"]
        self.LeoWrap = self.LeoBodyText["wrap"]
    
        self.Config = ConfigClass(self)
        self.BreakBar = BreakbarClass(self)
        self.Watcher = WatcherClass(self)
        self.ToolBar = ToolbarClass(self) # must init after breakbar cos use bg color
    #@nonl
    #@-node:ekr.20060513122450.391:initXcc
    #@+node:ekr.20060513152023:controller event handlers
    #@+node:ekr.20060513152032.3:onSelect
    def onSelect(self):
        
        c = self.c ; p = c.currentPosition()
        
        if IsXcc(p):
            self.sSelect(p)
            self.cSelect()
        else:
            p2 = GetXccNode(p)
            if p2:
                if p2 != self.SELECTED_NODE:
                    self.sSelect(p2)
                self.cSelect(p)			
            else:
                self.sSelect()
                self.cSelect()
    #@nonl
    #@-node:ekr.20060513152032.3:onSelect
    #@+node:ekr.20060513152032.4:onIdle
    def onIdle(self):
    
        crash = None
        try:
            self.UpdateProcess()
            self.BreakBar.IdleUpdate()
        except Exception:
            if crash:
                TraceBack()
                crash.do(None)
    #@nonl
    #@-node:ekr.20060513152032.4:onIdle
    #@+node:ekr.20060513152032.5:onCommand2
    def onCommand2(self,keywords):
    
        if keywords.get("label") in ["undo","redo"]:
            if self.SELECTED_NODE != None:
                self.BreakBar.bodychanged = True
    #@nonl
    #@-node:ekr.20060513152032.5:onCommand2
    #@+node:ekr.20060513152032.6:onBodyDoubleClick
    def onBodyDoubleClick(self):
        
        c = self.c ; p = c.currentPosition()
    
        if self.SELECTED_NODE == p:
            self.sGoToError()
    #@nonl
    #@-node:ekr.20060513152032.6:onBodyDoubleClick
    #@+node:ekr.20060513152032.7:onBodyKey2
    def onBodyKey2(self,keywords):
       
        ch = keywords.get("ch")
        self.LeoBodyText.tag_delete("xcc_error")
        if self.CHILD_NODE != None and ch in ["\r","",str(chr(8))]:
            self.BreakBar.BreaksFromTags()
    #@nonl
    #@-node:ekr.20060513152032.7:onBodyKey2
    #@+node:ekr.20060513152032.8:onHeadKey2
    def onHeadKey2(self,keywords):
       
        # g.trace(keywords,g.callers())
        
        c = self.c ; p = c.currentPosition()
        
        if IsXcc(p):
            if self.SELECTED_NODE == None:
                self.sSelect(p)
                self.sInitDict()
            else:
                self.sGetBrowseInfo()
        else:
            ch = keywords.get("ch")
            if self.CHILD_NODE != None and ch == "\r":
                self.cSelect(self.CHILD_NODE)
    #@nonl
    #@-node:ekr.20060513152032.8:onHeadKey2
    #@+node:ekr.20060513152032.9:onQuit
    def onQuit(self):
      
        if self.ACTIVE_NODE != None:
            self.GoToNode(self.ACTIVE_NODE)
            self.aStop()
            while self.ACTIVE_NODE != None:
                self.UpdateProcess()
    #@nonl
    #@-node:ekr.20060513152032.9:onQuit
    #@-node:ekr.20060513152023:controller event handlers
    #@+node:ekr.20060513160819:pause
    def pause (self,pid):
        
        if os.name == "nt":
            winPause(pid)
        else:
            linPause(pid)
    #@nonl
    #@-node:ekr.20060513160819:pause
    #@+node:ekr.20060513122450.31:GoToNode
    def GoToNode(self,node,index=None,tagcolor=None):
        
        if not node: return
        c = self.c ; w = self.LeoBodyText
    	
        c.beginUpdate()
        if not node.isVisible():
            for p in node.parents_iter():
                p.expand()
        c.selectPosition(node)
        c.endUpdate()
    
        if index is None: return
        w.mark_set("insert",index)
        w.see(index)
    
        if tagcolor is None: return 
        l,c = w.index("insert").split(".")
        w.tag_add("xcc_error",l+".0",l+".end")
        w.tag_config("xcc_error",background=tagcolor)
        w.tag_raise("xcc_error")
    #@nonl
    #@-node:ekr.20060513122450.31:GoToNode
    #@+node:ekr.20060513122450.322:Child Node Funcs
    #@+node:ekr.20060513122450.323:cIs
    def cIs(self,node):
        for p in node.parents_iter():
            if p.headString()[0:5] == "@xcc ":
                return True	
        return False
    #@-node:ekr.20060513122450.323:cIs
    #@+node:ekr.20060513122450.324:cSet
    def cSet(self,name,value):
        self.CHILD_DICT[name] = value
    #@-node:ekr.20060513122450.324:cSet
    #@+node:ekr.20060513122450.325:cGet
    def cGet(self,name,init=""):
        if name not in self.CHILD_DICT:
            self.cSet(name,init)	
        return self.CHILD_DICT[name]
    #@-node:ekr.20060513122450.325:cGet
    #@+node:ekr.20060513122450.326:cSelect
    def cSelect(self,node=None):
        # global CHILD_NODE,CHILD_DICT,CHILD_LINE,CHILD_EXT
        # try:
        if node != None:
            self.Config.Hide()
            #if CHILD_NODE != None:
            #	BreakBar.Hide()
            self.CHILD_NODE = node
            self.CHILD_DICT = self.cGetDict()
            if self.LOCATE_CHILD == True:
                loc = LOCATOR(CHILD_NODE,1)
                self.CHILD_EXT = loc.FOUND_FILE_EXT
                self.CHILD_LINE = loc.FOUND_FILE_LINE								
                self.BreakBar.Show()
                if loc.FOUND_FILE_EXT != None:
                    self.ToolBar.SyncDisplayToChild(loc)
                else:
                    self.ToolBar.SyncDisplayToError()
        elif self.CHILD_NODE != None:
            self.BreakBar.Hide()
            self.CHILD_NODE = None
            self.CHILD_DICT = None
            self.CHILD_LINE = None
            self.CHILD_EXT = None
        # except Exception:
            # TraceBack()
    #@nonl
    #@-node:ekr.20060513122450.326:cSelect
    #@+node:ekr.20060513122450.327:cGetDict
    def cGetDict(self,node=None):#Get xcc child dict alias "xcc_child_cfg" in ua	
    
        if node == None:
            node =	self.CHILD_NODE
        if node == None:
            return None
            
        v = node.v
        if hasattr(v,"unknownAttributes") != True:
            v.unknownAttributes = {}		
        
        if "xcc_child_cfg" not in v.unknownAttributes:
            v.unknownAttributes["xcc_child_cfg"] = d = {}
            return d		
        else:
            return v.unknownAttributes["xcc_child_cfg"]
    #@nonl
    #@-node:ekr.20060513122450.327:cGetDict
    #@-node:ekr.20060513122450.322:Child Node Funcs
    #@+node:ekr.20060513122450.295:Selected Node Funcs
    #@+node:ekr.20060513122450.296:sGatherInfo
    def sGatherInfo(self):
    
        if self.SELECTED_NODE:
            self.sExtractHeadInfo()
            
            #@        @+others
            #@+node:ekr.20060513122450.297:Head
            # global REL_PATH,NAME,EXT,REL_PATH,ABS_PATH,CWD
            
            self.NAME = sGet("NAME")
            self.EXT = sGet("EXT")
            self.REL_PATH = sGet("REL_PATH")
            self.ABS_PATH = sGet("ABS_PATH")
            self.CWD = os.getcwd()
                
            if self.NAME == "":
                Error("xcc: ","Node have no name!")
                return False
            #@-node:ekr.20060513122450.297:Head
            #@+node:ekr.20060513122450.298:Dicts
            self.OPTS = self.sGet("Options")
            self.CPL = self.sGet("Compiler")
            self.DBG = self.sGet("Debugger")
            self.EXE = self.sGet("Executable")
            #@nonl
            #@-node:ekr.20060513122450.298:Dicts
            #@+node:ekr.20060513122450.299:File Creation
            # global CREATE_FILES,SRC_EXT
            self.CREATE_FILES = self.OPTS.get("Create files")
            
            if self.CREATE_FILES == "True":
            
                if self.REL_PATH != "" and os.access(self.REL_PATH,os.F_OK) != 1:
                    os.makedirs(self.REL_PATH)
                    
                if self.EXT == "h": self.SRC_EXT = EXT
                
                if self.EXT == "exe": self.SRC_EXT = "cpp"
                
                if self.EXT == "cpp" or self.EXT == "c":
                    self.SRC_EXT = self.EXT
                        
                if self.EXT == "dll": self.SRC_EXT = "cpp"
            #@nonl
            #@-node:ekr.20060513122450.299:File Creation
            #@+node:ekr.20060513122450.300:Compilation
            self.COMPILE = self.OPTS.get("Compile")
            
            if self.COMPILE == "True":
                self.COMPILER = self.CPL.get("Compiler")
                if not self.COMPILER:
                    Error("xcc: ","Compiler is undefined!")
                    return False
            #@nonl
            #@-node:ekr.20060513122450.300:Compilation
            #@+node:ekr.20060513122450.301:Execution
            self.EXECUTE = self.OPTS.get("Execute")
            #@nonl
            #@-node:ekr.20060513122450.301:Execution
            #@+node:ekr.20060513122450.302:Debugging
            self.DEBUG = OPTS.get("Debug")
            
            if self.DEBUG == "TRUE":
                self.DEBUGGER = self.DBG.get("Debugger")
                if not self.DEBUGGER:
                    Error("xcc: ","Debugger is undefined!")
                    return False
                    
                if self.OPTS.get("Seek breapoints")== "True":
                    if self.DBG.get("Breaks start index") == "":
                        Warning("xcc: ","Breaks start index is undefined, using 0")
                        self.DBG["Breaks start index"] = "0"
            #@nonl
            #@-node:ekr.20060513122450.302:Debugging
            #@-others
        
            self.VERBOSE = self.OPTS.get("Xcc verbose")
            self.FILTER_OUTPUT = self.OPTS.get("Filter output")
            return True
    
        return False
    #@nonl
    #@-node:ekr.20060513122450.296:sGatherInfo
    #@+node:ekr.20060513122450.303:sExtractHeadInfo
    def sExtractHeadInfo (self):
    
        w = self.SELECTED_NODE.headString() [5:]
        if w:
            path, name = os.path.split(w)
            name, ext = os.path.splitext(name)
            ext = ext.lower().replace(".","") or 'exe'
        else:
            path, name, ext = '', '', ''
    
        self.sSet("REL_PATH",path)
        self.sSet("NAME",name)
        self.sSet("EXT",ext)
        theDir = g.choose(path,self.CWD+"\\"+path,self.CWD)
        self.sSet("ABS_PATH",theDir)
    #@nonl
    #@-node:ekr.20060513122450.303:sExtractHeadInfo
    #@+node:ekr.20060513122450.304:sGetBrowseInfo
    def sGetBrowseInfo(self):
          
        w = self.SELECTED_NODE.headString()[5:]
        if w:		
            self.REL_PATH,self.NAME = os.path.split(w)
            self.NAME,EXT = os.path.splitext(self.NAME)		
            self.EXT = EXT.lower().replace(".","") or 'exe'
        else:
            self.REL_PATH = ""
            self.NAME = ""
            self.EXT = "exe"
        
        self.CWD = os.getcwd()
        
        if self.REL_PATH != "":		
            self.ABS_PATH = self.CWD+"\\"+self.REL_PATH
        else:
            self.ABS_PATH = self.CWD
            
        if EXT == "h":
            self.SRC_EXT = self.EXT	
        if EXT == "exe":
            self.SRC_EXT = "cpp"	
        if EXT == "cpp" or self.EXT == "c":
            self.SRC_EXT = self.EXT			
        if EXT == "dll":
            self.SRC_EXT = "cpp"
            
        self.PTS = self.sGet("Options",{})
        
        
    #@nonl
    #@-node:ekr.20060513122450.304:sGetBrowseInfo
    #@+node:ekr.20060513122450.305:sGetWriteInfo
    def sGetWriteInfo():
        
        if self.NAME == "":
            Error("xcc: ","Node have no name!")
            return False
        
        if self.REL_PATH != "" and os.access(self.REL_PATH,os.F_OK) != 1:
            os.makedirs(self.REL_PATH)
        
        self.COD = self.sGet("Code")	
        #FILE_HDR = COD["File header"]
        #FILE_FTR = COD["File footer"]
        #CLASS_HDR = COD["Class header"]
        #CLASS_FTR = COD["Class footer"]
        #CLASS_OPN = COD["Class opening"]
        #CLASS_END = COD["Class closing"]
        if not self.CLASS_OPN: self.CLASS_OPN = "{\n"	
        if not self.CLASS_END: self.CLASS_END = "};\n"
        #FUNC_HDR = COD["Function header"]
        #FUNC_FTR = COD["Function footer"]
        #FUNC_OPN = COD["Function opening"]
        #FUNC_END = COD["Function closing"]
        if not self.FUNC_OPN: self.FUNC_OPN = "{\n"	
        if not self.FUNC_END: self.FUNC_END = "}\n"
        return True
    #@nonl
    #@-node:ekr.20060513122450.305:sGetWriteInfo
    #@+node:ekr.20060513122450.306:sGetCompileInfo
    def sGetCompileInfo():
    
        self.CPL = self.sGet("Compiler")
    
        if not self.CPL.get("Compiler"):
            Error("xcc: ","No compiler defined!")
            return False
            
        self.VERBOSE = self.OPTS.get("Xcc verbose")
            
        return True
    
    #@-node:ekr.20060513122450.306:sGetCompileInfo
    #@+node:ekr.20060513122450.307:sGetDebugInfo
    def sGetDebugInfo():
       
        self.DBG = self.sGet("Debugger")
        if not self.DBG["Debugger"] == "":
            Error("xcc: ","No debugger defined!")
            return False
        
        self.VERBOSE = self.OPTS.get("Xcc verbose")
        
        return True
    #@nonl
    #@-node:ekr.20060513122450.307:sGetDebugInfo
    #@+node:ekr.20060513122450.308:sGetExecInfo
    def sGetExecInfo():
    
        self.EXE = self.sGet("Executable")		
        return True
    #@nonl
    #@-node:ekr.20060513122450.308:sGetExecInfo
    #@+node:ekr.20060513122450.309:sGoToError
    def sGoToError(self,e=None):
        
        mask = [" ",":","(",")"]
        if e == None:
            row,col = self.LeoBodyText.index("insert").split(".")
            row = int(row)
            col = int(col)
            lines = self.SELECTED_NODE.bodyString().splitlines()
            e = lines[row-1]
            e=e.replace("/","\\")
            
        edexp = self.CPL["Error detection"]
        m = re.search(edexp,e,re.IGNORECASE)
        if m != None:
            try:
                file = m.group("FILE")
                line = m.group("LINE")
                id = m.group("ID")
                edef = m.group("DEF")
                path,name = os.path.split(CPL["Compiler"])
                Error(name+" : ","Error: "+id+" in "+file+" line "+line+" : "+edef)
        
            except Exception:
                Warning("xcc: ","Unable to process error detection!")
                return
            
            name,ext = os.path.splitext(file)
            if name == self.NAME:
                SeekErrorClass(self,int(line),ext.replace(".",""),color=ErrorColor)
    #@nonl
    #@-node:ekr.20060513122450.309:sGoToError
    #@+node:ekr.20060513122450.310:sGo
    def sGo(self):	#this is where the selected node also become the active node
      
        if self.NAME == "":
            Error("xcc: ","Node have no name!")
            return False
        self.sSetText("@language c++\n")
        
        if self.CreateFiles() == False:
            return False
        if self.Compile() == False:
            return False
        if self.OPTS.get("Execute") == "True" and self.OPTS.get("Debug") == "False":
            if self.Execute() == False:
                return False
        if self.OPTS.get("Debug") == "True":
            if self.Debug() == False:
                return False
        return True
    #@nonl
    #@-node:ekr.20060513122450.310:sGo
    #@+node:ekr.20060513122450.311:sSet
    def sSet (self,name,value):
    
        self.SELECTED_DICT [name] = value
    #@-node:ekr.20060513122450.311:sSet
    #@+node:ekr.20060513122450.312:sGet
    def sGet(self,name,init=""):
        
        if name not in self.SELECTED_DICT:
            self.sSet(name,init)	
        return self.SELECTED_DICT[name]
    #@nonl
    #@-node:ekr.20060513122450.312:sGet
    #@+node:ekr.20060513122450.313:sIsDict
    def sIsDict(self):
    
        if not self.SELECTED_NODE:
            return False
        
        v = self.SELECTED_NODE.v	
        
        return hasattr(v,"unknownAttributes") and "xcc_cfg" in v.unknownAttributes
    #@nonl
    #@-node:ekr.20060513122450.313:sIsDict
    #@+node:ekr.20060513122450.314:sGetDict
    def sGetDict(self): # Get xcc parent dict alias "xcc_cfg" in ua
    
        if not self.SELECTED_NODE:
            return None
        
        v = self.SELECTED_NODE.v
    
        if not hasattr(v,"unknownAttributes"):
            v.unknownAttributes = {}
        
        if "xcc_cfg" in v.unknownAttributes:
            return v.unknownAttributes["xcc_cfg"]
        else:
            v.unknownAttributes["xcc_cfg"] = d = {}
            return d
    #@nonl
    #@-node:ekr.20060513122450.314:sGetDict
    #@+node:ekr.20060513122450.315:sInitDict
    def sInitDict(self):
        
        Warning("xcc: ","Writing blank configuration!")
        self.sSetText("@language c++")
        self.Config.ClearConfig()
        self.Config.SaveToNode()
        self.sSet("INITED","True")
    
    
    
    #@-node:ekr.20060513122450.315:sInitDict
    #@+node:ekr.20060513122450.316:sSelect
    def sSelect(self,node=None):
        
        c = self.c
        if node:
            if self.SELECTED_NODE:
                self.Config.Hide()
                if self.SELECTED_NODE:
                    self.SELECTED_NODE = node		
            else:
                self.SELECTED_NODE = node
            
            self.SELECTED_DICT = self.sGetDict()
            
            if self.SELECTED_NODE != self.ACTIVE_NODE and self.SELECTED_NODE.isMarked():
                self.SELECTED_NODE.clearMarked()
                c.redraw()
            
            self.sGetBrowseInfo()
            self.sShow()
        elif self.SELECTED_NODE:
            self.Config.Hide()
            self.sHide()
            self.SELECTED_NODE = None
            self.SELECTED_DICT = self.sGetDict()
    #@nonl
    #@-node:ekr.20060513122450.316:sSelect
    #@+node:ekr.20060513122450.317:sSync
    def sSync(self):
        
        self.SELECTED_DICT = self.sGetDict()
        if self.SELECTED_DICT:
            self.sExtractHeadInfo()
        
        self.CHILD_DICT = self.cGetDict()
    #@nonl
    #@-node:ekr.20060513122450.317:sSync
    #@+node:ekr.20060513122450.318:sShow
    def sShow(self):
        
        self.LeoBodyText.pack_forget()
        self.LeoYBodyBar.pack_forget()
        
        self.ToolBar.Show()
        self.LeoXBodyBar.pack(side="bottom",fill="x")
        self.LeoYBodyBar.pack(side="right",fill="y")
        self.LeoBodyText.pack(fill="both",expand=1)
        self.LeoBodyText["wrap"] = 'none'
        
        self.ToolBar.Spacer["state"] = 'normal'
        self.ToolBar.Spacer.delete('1.0','end')
        self.ToolBar.Spacer.insert("insert","."+self.EXT)
        self.ToolBar.Spacer["state"] = 'disabled'
        
        self.ToolBar.Display["state"] = 'normal'
        self.ToolBar.Display.delete('1.0','end')
        self.ToolBar.Display["state"] = 'disabled'
    
        self.Watcher.Sync()
    #@nonl
    #@-node:ekr.20060513122450.318:sShow
    #@+node:ekr.20060513122450.319:sHide
    def sHide(self):
    
        self.LeoXBodyBar.pack_forget()
        self.ToolBar.Hide()
        self.LeoBodyText["wrap"]=self.LeoWrap
    #@nonl
    #@-node:ekr.20060513122450.319:sHide
    #@+node:ekr.20060513122450.320:sSetText
    def sSetText(self,text=""):
        
        self.SELECTED_NODE.setBodyTextOrPane(text)
    #@-node:ekr.20060513122450.320:sSetText
    #@+node:ekr.20060513122450.321:sAddText
    def sAddText(self,text):
        
        self.SELECTED_NODE.setBodyTextOrPane(self.SELECTED_NODE.bodyString()+text)
    
        if self.CHILD_NODE == None:
            l,c = self.LeoBodyText.index("end").split(".")
            self.LeoBodyText.see(l+".0")
    #@nonl
    #@-node:ekr.20060513122450.321:sAddText
    #@-node:ekr.20060513122450.295:Selected Node Funcs
    #@+node:ekr.20060513122450.281:Active Node Funcs
    #@+node:ekr.20060513122450.282:aSet
    def aSet(self,name,value):
        
        self.ACTIVE_DICT[name] = value
    #@-node:ekr.20060513122450.282:aSet
    #@+node:ekr.20060513122450.283:aGet
    def aGet(self,name,init=""):
        
        if name not in self.ACTIVE_DICT:
            self.aSet(name,init)
    
        return self.ACTIVE_DICT[name]
    #@-node:ekr.20060513122450.283:aGet
    #@+node:ekr.20060513122450.284:aGetDict
    def aGetDict(self): # Get xcc parent dict alias "xcc_cfg" in ua
    
        if not self.ACTIVE_NODE:
            return None
        
        v = self.ACTIVE_NODE.v	
        if hasattr(v,"unknownAttributes") != True:
            v.unknownAttributes = {}
        
        if "xcc_cfg" in v.unknownAttributes:
            return v.unknownAttributes["xcc_cfg"]
        else:
            v.unknownAttributes["xcc_cfg"] = d = {}
            return d
    #@-node:ekr.20060513122450.284:aGetDict
    #@+node:ekr.20060513122450.285:aGo
    def aGo(self):
        
        if self.ACTIVE_NODE and self.DBG["Continue"]:
            self.aWrite(DBG["Continue"])
            self.LeoBodyText.tag_delete("xcc_error")
            self.ToolBar.DisableStep()
    #@nonl
    #@-node:ekr.20060513122450.285:aGo
    #@+node:ekr.20060513122450.286:aStop
    def aStop(self):
       
        if not self.ACTIVE_NODE or not self.ACTIVE_PROCESS:
            return Error("xcc: ","Current xcc node is not active!")
    
        if self.ACTIVE_NODE == self.SELECTED_NODE and self.TARGET_PID:
            stop = self.DBG["Stop"]
            if self.DBG_PROMPT != True:
                self.pause(self.TARGET_PID)
                if stop: self.DBG_TASK.append(DBGTASK(self,stop))					
            else:
                if stop: self.aWrite(stop)
            self.LeoBodyText.tag_delete("xcc_error")
            if self.WATCH_TASK: self.WATCH_TASK.Cancel()
    #@nonl
    #@-node:ekr.20060513122450.286:aStop
    #@+node:ekr.20060513122450.287:aStepIn
    def aStepIn(self):
       
        if (
            self.ACTIVE_NODE and self.ACTIVE_PROCESS and
            self.ACTIVE_NODE == self.SELECTED_NODE and
            self.DBG["Step in"] != "" and self.DBG_PROMPT
        ):
            self.DBG_STEPPING = True
            self.aWrite(DBG["Step in"])
            self.ToolBar.DisableStep()
            self.LeoBodyText.tag_delete("xcc_error")
            self.DBG_TASK.append(QUERYGOTASK(self))
    #@nonl
    #@-node:ekr.20060513122450.287:aStepIn
    #@+node:ekr.20060513122450.288:aStepOver
    def aStepOver(self):
        
        if (
            self.ACTIVE_NODE and self.ACTIVE_PROCESS and
            self.ACTIVE_NODE == self.SELECTED_NODE and
            self.DBG["Step in"] != "" and self.DBG_PROMPT
        ):
            self.DBG_STEPPING = True			
            self.aWrite(DBG["Step over"])
            self.ToolBar.DisableStep()
            self.LeoBodyText.tag_delete("xcc_error")
            self.DBG_TASK.append(QUERYGOTASK(self))
    #@-node:ekr.20060513122450.288:aStepOver
    #@+node:ekr.20060513122450.289:aStepOut
    def aStepOut(self):
    
        if (
            self.ACTIVE_NODE and self.ACTIVE_PROCESS and
            self.ACTIVE_NODE == self.SELECTED_NODE and
            self.DBG["Step in"] != "" and self.DBG_PROMPT
        ):
            self.DBG_STEPPING = True
            self.aWrite(DBG["Step out"])
            self.ToolBar.DisableStep()
            self.LeoBodyText.tag_delete("xcc_error")
            self.DBG_TASK.append(QUERYGOTASK(self))
    #@nonl
    #@-node:ekr.20060513122450.289:aStepOut
    #@+node:ekr.20060513122450.290:aPause
    def aPause(self):
        
        if not self.ACTIVE_NODE or not self.ACTIVE_PROCESS:
            Error("xcc: ","Current xcc node is not active!")
    
        elif self.ACTIVE_NODE == self.SELECTED_NODE and self.TARGET_PID:
            self.pause(self.TARGET_PID)
    #@nonl
    #@-node:ekr.20060513122450.290:aPause
    #@+node:ekr.20060513122450.291:aWrite
    def aWrite(self,text):
    
        if self.FILTER_OUTPUT == "False":
            self.aAddText(text+"\n")
            
        eol = "" ; code = "eol = \""+DBG["Pipe eol"]+"\""
        try:
            exec code
        except:
            TraceBack()
        if eol == "": eol = "\n"
        
        self.ACTIVE_PROCESS.In.write(text+eol)
        self.ACTIVE_PROCESS.In.flush()
        self.DBG_PROMPT = False
        self.ToolBar.PauseButton["state"] = 'normal'
        self.ToolBar.HideInput()
    #@nonl
    #@-node:ekr.20060513122450.291:aWrite
    #@+node:ekr.20060513122450.292:aSelect
    def aSelect(self,node=None):
    
        self.ACTIVE_NODE = node
        self.ACTIVE_DICT = self.aGetDict()
    #@nonl
    #@-node:ekr.20060513122450.292:aSelect
    #@+node:ekr.20060513122450.293:aSetText
    def aSetText(self,text=""):
        
        if self.ACTIVE_NODE:
            self.ACTIVE_NODE.setBodyTextOrPane(text)
    #@nonl
    #@-node:ekr.20060513122450.293:aSetText
    #@+node:ekr.20060513122450.294:aAddText
    def aAddText(self,text):
        
        if self.ACTIVE_NOD:
            self.ACTIVE_NODE.setBodyTextOrPane(self.ACTIVE_NODE.bodyString()+text)
            if self.SELECTED_NODE == self.ACTIVE_NODE and self.CHILD_NODE:
                l,c = LeoBodyText.index("end").split(".")
                self.LeoBodyText.see(l+".0")
    #@nonl
    #@-node:ekr.20060513122450.294:aAddText
    #@-node:ekr.20060513122450.281:Active Node Funcs
    #@+node:ekr.20060513122450.328:Action Funcs
    #@+node:ekr.20060513122450.329:CreateFiles
    def CreateFiles(self):
        
        if self.OPTS.get("Create files") == "True":
            return self.sGetWriteInfo() and WriterClass(self).Result
        else:
            return None
    #@nonl
    #@-node:ekr.20060513122450.329:CreateFiles
    #@+node:ekr.20060513122450.330:Compile
    def Compile(self):
       
        if not self.OPTS.get("Compile"):
            return None
        if not sGetCompileInfo():
            return False
        if len(ProcessList) > 1:
            Error("xcc: ","already running!")
            return False
            
        process = self.ProcessClass(
            self,
            self.SELECTED_NODE,
            self.CPL["Compiler"],
            self.CplCmd(),
            start=self.CplStart,out=self.CplOut,err=self.CplErr,end=self.CplEnd)
            
        ok = process.Open()
        if ok: self.ProcessList.append(process)
        return ok
    #@nonl
    #@-node:ekr.20060513122450.330:Compile
    #@+node:ekr.20060513122450.331:CplCmd
    def CplCmd(self):
        
        cwd = os.getcwd()
    
        if self.OPTS.get("Debug"):
            cmd = self.CPL["Debug arguments"]
        else:
            cmd = self.CPL["Arguments"]
        
        cmd = self.ReplaceVars(cmd.replace("\n"," ").strip())
        
        #@    @+others
        #@+node:ekr.20060513122450.332:_INCPATHS_
        if CPL["Include path"] != "":
            sym = CPL["Include path"]
            paths = CPL["Include search paths"].splitlines()
            INCPATHS = ""
            for p in paths:
                if p != "":
                    INCPATHS += " "+sym+"\""+p+"\""
            cmd = cmd.replace("_INCPATHS_",INCPATHS.strip())
        #@nonl
        #@-node:ekr.20060513122450.332:_INCPATHS_
        #@+node:ekr.20060513122450.333:_LIBPATHS_
        if CPL["Library path"] != "":
            sym = CPL["Library path"]
            paths = CPL["Library search paths"].splitlines()
            LIBPATHS = ""
            for p in paths:
                if p != "":
                    LIBPATHS += " "+sym+"\""+p+"\""
            cmd = cmd.replace("_LIBPATHS_",LIBPATHS.strip())
        #@nonl
        #@-node:ekr.20060513122450.333:_LIBPATHS_
        #@+node:ekr.20060513122450.334:_LIBRARIES_
        if CPL["Use library"] != "":
            sym = CPL["Use library"]
            libs = CPL["Used libraries"].split()
            LIBRARIES = ""
            for l in libs:
                if l != "":
                    LIBRARIES += " "+sym+"\""+l+"\""
            cmd = cmd.replace("_LIBRARIES_",LIBRARIES.strip())
        #@nonl
        #@-node:ekr.20060513122450.334:_LIBRARIES_
        #@+node:ekr.20060513122450.335:_BUILD_
        if EXT == "exe":
            if CPL["Build exe"] != "":
                cmd = cmd.replace("_BUILD_",CPL["Build exe"])
        
        if EXT == "dll":
            if CPL["Build dll"] != "":
                cmd = cmd.replace("_BUILD_",CPL["Build dll"])
            else:
                Warning("xcc: ","Build dll requested but compiler build dll symbol is undefined!")
        #@nonl
        #@-node:ekr.20060513122450.335:_BUILD_
        #@-others
        
        return cmd
    
    
    #@-node:ekr.20060513122450.331:CplCmd
    #@+node:ekr.20060513122450.336:Debug
    def Debug(self):
    
        if GetDebugInfo() and self.EXT == "exe":
            p = ProcessClass(self,
                self.SELECTED_NODE,
                self.DBG["Debugger"],
                self.DbgCmd(),
                start=self.DbgStart,
                out=self.DbgOut,
                err=self.DbgErr,
                end=self.DbgEnd)
            self.ProcessList.append(p)
    #@nonl
    #@-node:ekr.20060513122450.336:Debug
    #@+node:ekr.20060513122450.337:DbgCmd
    def DbgCmd(self):
        
        cmd = self.DBG["Arguments"].replace("\n"," ").strip()
        cmd = self.ReplaceVars(cmd)		
        return cmd
    #@nonl
    #@-node:ekr.20060513122450.337:DbgCmd
    #@+node:ekr.20060513122450.338:Execute
    def Execute(self):
        
        self.sGetExecInfo()
        cmd = ABS_PATH+"\\"+NAME+"."+EXT
        args = self.EXE["Execution arguments"]
            
        if self.OPTS.get("Connect to pipe"):
            process = ProcessClass(self,
                self.SELECTED_NODE,cmd,args,
                start=self.ProgStart,out=self.ProgOut,
                err=self.ProgErr,end=self.ProgEnd)
        else:
            process = ProcessClass(self,self.SELECTED_NODE,cmd,args,spawn=True)
    
        self.ProcessList.append(process)
    #@-node:ekr.20060513122450.338:Execute
    #@-node:ekr.20060513122450.328:Action Funcs
    #@+node:ekr.20060513122450.339:Compiler Events
    #@+node:ekr.20060513122450.340:CplStart
    def CplStart(self):
    
        self.OutBuff = ""
        self.ErrBuff = ""
        self.FIRST_ERROR = False
        self.aSelect(self.SELECTED_NODE)
        process = self.VProcessList[0]
        
        text = ""	
        if self.VERBOSE == "True":
            text += "\" Starting "+process.FileName+"...\n"
            text += "\" using arguments: "+process.Arguments+"\n"		
        text += "\""+("="*60)+"\n"
        
        self.aAddText(text)
    
    #@-node:ekr.20060513122450.340:CplStart
    #@+node:ekr.20060513122450.341:CplOut
    def CplOut(self,text):
        
        self.OutBuff += text
        lines = self.OutBuff.splitlines(True)
        if lines[-1][-1] != "\n":
            self.OutBuff = lines.pop()
        else:
            self.OutBuff = ""
        
        text = ""	
        for l in lines:
            if l != "":
                if l.lower().find("error") > -1:
                    text += "// "+l
                    if self.OPTS.get("Seek first error") and self.FIRST_ERROR == False:
                        self.FIRST_ERROR = True
                        self.sGoToError(l)
                else:
                    if self.FILTER_OUTPUT == False:
                        text += "# "+l
                
        self.aAddText(text)
    
    #@-node:ekr.20060513122450.341:CplOut
    #@+node:ekr.20060513122450.342:CplErr
    def CplErr(self,text):
        
        self.ErrBuff += text
        lines = self.ErrBuff.splitlines(True)
        if lines[-1][-1] != "\n":
            self.ErrBuff = lines.pop()
        else:
            self.ErrBuff = ""
        
        text = ""	
        for l in lines:
            text += "// "+l+"\n"
                        
        self.aAddText(text)
    #@nonl
    #@-node:ekr.20060513122450.342:CplErr
    #@+node:ekr.20060513122450.343:CplEnd
    def CplEnd(self,exitcode):
        
        text = "\""+("="*60)+"\n"
        if exitcode == None:
            text += "\" Build process successful!\n"
        else:
            text += "// Build process aborted!\n"		
        text += "\""+("-"*60)+"\n"
    
        self.aAddText(text)
        self.aSelect()
    #@nonl
    #@-node:ekr.20060513122450.343:CplEnd
    #@-node:ekr.20060513122450.339:Compiler Events
    #@+node:ekr.20060513122450.344:Debugger Events
    #@+node:ekr.20060513122450.379:DbgStart
    def DbgStart(self):
    
        g.trace()
        self.OutBuff = ""
        self.ErrBuff = ""
        self.ACTIVE_PROCESS=self.ProcessList[0]
        self.PROMPT_RD = []
        self.DBG_STEPPING = False
        self.DBG_PROMPT = False
        self.TARGET_PID = ""
        self.aSelect(self.SELECTED_NODE)
        # set buttons
        self.ToolBar.PauseButton["state"] = 'normal'
        self.ToolBar.StopButton["state"] = 'normal'
        # startup banner
        text = ""	
        if self.VERBOSE == "True":
            text += "\" Starting "+self.ACTIVE_PROCESS.FileName+"...\n"
            text += "\" using arguments: "+self.ACTIVE_PROCESS.Arguments+"\n"
        text += "\""+("="*60)+"\n"
        self.aAddText(text)
        self.DBG_TASK = []
        self.DBG_SD = []
        self.DBG_RD = []
        OUTPUTTASK(self)
        st = ReplaceVars(DBG["Startup task"]).splitlines()
        for t in st:
            DBGTASK(t)
        TARGETPIDTASK(self)
        REGEXPTASK(self)
        
        BREAKTASK(self)
        DBGTASK(self,DBG["Continue"])
    #@nonl
    #@-node:ekr.20060513122450.379:DbgStart
    #@+node:ekr.20060513122450.380:DbgOut
    def DbgOut(text):
        
        g.trace(repr(text))
       
        #Extract output lines and prompt
        if text != "":
            OutBuff += text
            lines = OutBuff.splitlines(True)
            if lines[-1][-1] != "\n":
                OutBuff = lines.pop()
            else:
                OutBuff = ""
        
        
            # sending output to SENT tasks
            for l in lines:
                for r in DBG_RD:
                    r(l)		
        
        # detect the prompt
        if OutBuff != "" and re.search(DBG["Prompt pattern"],OutBuff) != None:
            ToolBar.PauseButton["state"] = 'disabled'
            for prd in PROMPT_RD:
                prd()
            DBG_PROMPT = True
            if DBG_STEPPING == True:
                DBG_STEPPING = False
                ToolBar.EnableStep()
            if FILTER_OUTPUT == "False":
                aAddText("# "+OutBuff)
            OutBuff = ""
            
            
        # send task to the debugger
        while DBG_PROMPT == True and len(DBG_SD) > 0:
            DBG_SD[0]()
        
        if DBG_PROMPT == True:
            ToolBar.ShowInput()
    #@nonl
    #@-node:ekr.20060513122450.380:DbgOut
    #@+node:ekr.20060513122450.381:DbgErr
    def DbgErr(text):
        global ErrBuff
        
        ErrBuff += text
        lines = ErrBuff.splitlines(True)
        if lines[-1][-1] != "\n":
            ErrBuff = lines.pop()
        else:
            ErrBuff = ""
        
        text = ""	
        for l in lines:
            text += "//err: "+l
                        
        aAddText(text)
    #@-node:ekr.20060513122450.381:DbgErr
    #@+node:ekr.20060513122450.382:DbgEnd
    def DbgEnd(self,exitcode):
        # global ACTIVE_PROCESS,DBG_TASK,TARGET_PID
        text = "\""+("="*60)+"\n"
        if exitcode == None:
            text += "\" Debug session ended successfully!\n"
        else:
            text += "// Debug session aborted!\n"
        
        text += "\""+("-"*60)+"\n"
        self.aAddText(text)
        
        self.ToolBar.PauseButton["state"] = 'disabled'
        self.ToolBar.StopButton["state"] = 'disabled'
        
        self.ACTIVE_PROCESS = None
        self.DBG_TASK = []
        
        self.ToolBar.DisableStep()
        self.LeoBodyText.tag_delete("xcc_error")	
        self.TARGET_PID = ""
        
        self.aSelect()
    #@-node:ekr.20060513122450.382:DbgEnd
    #@-node:ekr.20060513122450.344:Debugger Events
    #@+node:ekr.20060513122450.383:Program Events
    #@+node:ekr.20060513122450.384:ProgStart
    def ProgStart(self):
        
        g.trace()
    
        self.OutBuff = ""
        self.ErrBuff = ""
        self.aSelect(self.SELECTED_NODE)
        self.ACTIVE_PROCESS=self.ProcessList[0]
    
        text = ""	
        if self.VERBOSE:
            text += "\" Starting "+self.ACTIVE_PROCESS.FileName+"...\n"
            text += "\" using arguments: "+self.ACTIVE_PROCESS.Arguments+"\n"		
        text += "\""+("="*60)+"\n"
        self.aAddText(text)
    #@nonl
    #@-node:ekr.20060513122450.384:ProgStart
    #@+node:ekr.20060513122450.385:ProgOut
    def ProgOut(self,text):
        
        g.trace(repr(text))
        
        self.OutBuff += text
        lines,self.OutBuff = ExtractLines(OutBuff)
        
        text = ""	
        for l in lines:
            if l != "":
                text += "# "+l+"\n"			
        
        text += "# "+self.OutBuff
        self.OutBuff = ""
        self.aAddText(text)
    #@nonl
    #@-node:ekr.20060513122450.385:ProgOut
    #@+node:ekr.20060513122450.386:ProgErr
    def ProgErr(self,text):
        
        g.trace(repr(text))
        
        self.ErrBuff += text
        lines,self.ErrBuff = ExtractLines(ErrBuff)
        
        text = ""	
        for l in lines:
            text += "// "+l+"\n"
        text += "# "+self.ErrBuff
        self.ErrBuff = ""
        self.aAddText(text)
    #@nonl
    #@-node:ekr.20060513122450.386:ProgErr
    #@+node:ekr.20060513122450.387:ProgEnd
    def ProgEnd(self,exitcode):
        
        g.trace(exitcode)
        
        text = "\n\""+("="*60)+"\n"
        if exitcode == None:
            text += "\" Program exited normally!\n"
        else:
            text += "// Program exited with code: "+str(exitcode)+"\n"		
        text += "\""+("-"*60)+"\n"
    
        self.aAddText(text)
        self.ACTIVE_PROCESS = None
        self.aSelect()
    #@nonl
    #@-node:ekr.20060513122450.387:ProgEnd
    #@-node:ekr.20060513122450.383:Program Events
    #@-others
#@nonl
#@-node:ekr.20060513141418:class controllerClass
#@+node:ekr.20060513122450.345:Debugger task classes
#@+node:ekr.20060513122450.346:DBGTASK
class DBGTASK:
    #@    @+others
    #@+node:ekr.20060513122450.347:__init__
    def __init__(self,cmd,index=None):
        self.Command = cmd
        
        if index != None:
            DBG_SD.insert(index,self.Send)
        else:
            DBG_SD.append(self.Send)
    #@nonl
    #@-node:ekr.20060513122450.347:__init__
    #@+node:ekr.20060513122450.348:Send
    def Send(self):
        if self.Command != None:
            aWrite(self.Command)
        DBG_SD.remove(self.Send)
    #@nonl
    #@-node:ekr.20060513122450.348:Send
    #@-others
#@nonl
#@-node:ekr.20060513122450.346:DBGTASK
#@+node:ekr.20060513122450.349:OUTPUTTASK
class OUTPUTTASK(DBGTASK):
    #@    @+others
    #@+node:ekr.20060513122450.350:__init__
    def __init__(self,controller):
    
        self.controller = controller
        controller.DBG_RD.append(self.Receive)
    #@nonl
    #@-node:ekr.20060513122450.350:__init__
    #@+node:ekr.20060513122450.351:Send
    def Send(self):
        pass	#we just receive
    #@-node:ekr.20060513122450.351:Send
    #@+node:ekr.20060513122450.352:Receive
    def Receive(self,line):
        
        controller = self.controller
        
        if controller.DBG_PROMPT == False and line != "":
            lower = line.lower()
            if lower.find("error") > -1 or lower.find("warning") > -1:
                aAddText("//"+line)
            else:
                if controller.OPTS["Filter output"] == "False":
                    controller.aAddText("# "+line)
    #@nonl
    #@-node:ekr.20060513122450.352:Receive
    #@-others
    
#@nonl
#@-node:ekr.20060513122450.349:OUTPUTTASK
#@+node:ekr.20060513122450.353:TARGETPIDTASK
class TARGETPIDTASK(DBGTASK):
    #@    @+others
    #@+node:ekr.20060513122450.354:__init__
    def __init__(self,controller):
        
        self.controller = controller
        controller.DBG_SD.append(self.Send)
        
        self.PidTask = ReplaceVars(controller.DBG["Target pid task"])
        self.FindPid = ReplaceVars(controller.DBG["Find pid"])
    #@nonl
    #@-node:ekr.20060513122450.354:__init__
    #@+node:ekr.20060513122450.355:Send
    def Send(self):
        if self.PidTask != "":		
            aWrite(ReplaceVars(self.PidTask))
            DBG_SD.remove(self.Send)
            DBG_RD.append(self.Receive)
        else:
            DBG_SD.remove(self.Send)
            Warning("xcc: ","Target pid task is undefined!")
    
    
    #@-node:ekr.20060513122450.355:Send
    #@+node:ekr.20060513122450.356:Receive
    def Receive(self,line):
        global TARGET_PID
        if self.FindPid != "":
            if DBG_PROMPT == False:
                if line != "":
                    m = re.search(self.FindPid,line)
                    if m != None:
                        TARGET_PID = int(m.group("PID"))		
                        if VERBOSE == "True":					
                            aAddText("\" Target pid is: "+str(TARGET_PID)+" \n")
                        DBG_RD.remove(self.Receive)
                    
        else:
            DBG_RD.remove(self.Receive)
    #@nonl
    #@-node:ekr.20060513122450.356:Receive
    #@-others
    
#@nonl
#@-node:ekr.20060513122450.353:TARGETPIDTASK
#@+node:ekr.20060513122450.357:BREAKTASK
class BREAKTASK(DBGTASK):
    #@    @+others
    #@+node:ekr.20060513122450.358:__init__
    def __init__(self):
        
        #gathering breaks
        bf = BREAKFINDER()
        self.Breaks = aGet("Breakpoints").copy()
        if len(self.Breaks) != 0:
            self.bpsym = DBG["Set break"]
            if self.bpsym == "":
                Waning("xcc: ","Set break symbol is undefined!")
            else:
                self.bpsym = ReplaceVars(self.bpsym)
                DBG_SD.append(self.Send)
        
        regexp = DBG["Break detection"]
        if regexp != "":		
            regexp = regexp.splitlines()
            self.RegExp = []
            for e in regexp:
                self.RegExp.append(re.compile(e))		
        else:
            Warning("xcc: ","No break detection expression defined!")
    #@nonl
    #@-node:ekr.20060513122450.358:__init__
    #@+node:ekr.20060513122450.359:Send
    def Send(self):
        if len(self.Breaks) > 0:
            extl,s = self.Breaks.popitem()
            ext,l = extl.split(":")
            bpat = self.bpsym
            bpat = bpat.replace("_FILE_",NAME+"."+ext).replace("_LINE_",l)
            aWrite(bpat)
        else:
            DBG_SD.remove(self.Send)
            DBG_RD.append(self.Receive)
    
    #@-node:ekr.20060513122450.359:Send
    #@+node:ekr.20060513122450.360:Receive
    def Receive(self,line):
        for r in self.RegExp:
            if r.search(line) != None:
                if OPTS["Seek breakpoints"] == "True":
                    QUERYGOTASK(0)
                if VERBOSE == "True":
                    aAddText("\" Break detected!\n")
                
                if Watcher.visible == True and ACTIVE_PROCESS != None:
                    if SELECTED_NODE == ACTIVE_NODE:
                        WATCHTASK()
                        if DBG_PROMPT == True:
                            DbgOut("")
                            
                            
                ToolBar.EnableStep()						
                return
    #@-node:ekr.20060513122450.360:Receive
    #@-others
    
#@nonl
#@-node:ekr.20060513122450.357:BREAKTASK
#@+node:ekr.20060513122450.361:REGEXPTASK
class REGEXPTASK(DBGTASK):
    #@    @+others
    #@+node:ekr.20060513122450.362:__init__
    def __init__(self):
        DBG_RD.append(self.Receive)
        
        self.Exps = ReplaceVars(DBG["Regular expression"]).splitlines()
        self.Task = ReplaceVars(DBG["Task"]).splitlines()
        self.on = False	
    #@-node:ekr.20060513122450.362:__init__
    #@+node:ekr.20060513122450.363:Send
    def Send(self):
        pass	#receive only
    
    
    
    #@-node:ekr.20060513122450.363:Send
    #@+node:ekr.20060513122450.364:Receive
    def Receive(self,line):
        try:
            if self.on == False:
                self.on = True
                return
            i=1
            for e in self.Exps:
                if e != "" and re.search(e,line) != None:
                    if len(self.Task) >= i:
                        t = self.Task[i-1]
                    else:
                        t = ""
                    DBGTASK(t,0)
                    self.on = False
                i += 1
                            
        except Exception:
            TraceBack()
    
    #@-node:ekr.20060513122450.364:Receive
    #@-others
    
#@nonl
#@-node:ekr.20060513122450.361:REGEXPTASK
#@+node:ekr.20060513122450.365:WATCHTASK
class WATCHTASK(DBGTASK):
    #@    @+others
    #@+node:ekr.20060513122450.366:__init__
    def __init__(self,index=0):
        global WATCH_TASK
        self.Index = index
        WATCH_TASK = self
        self.Buffer = ""
        self.Count = 0
        
        Watcher.OutBox.tag_delete("changed")
        self.Lines = Watcher.InBox.get(1.0,'end').strip().splitlines()	
        
        if len(self.Lines) != 0:
            d=DBG_SD.append(self.Send)
        
        for l in self.Lines:
            if l == "":
                del l
                
        #Watcher.OutBox["state"] = 'normal'
        #Watcher.OutBox.delete(1.0,'end')
        #Watcher.OutBox["state"] = 'disabled'
        
        self.nl = ""
        self.Inited = False
    #@-node:ekr.20060513122450.366:__init__
    #@+node:ekr.20060513122450.367:Cancel
    def Cancel(self):
        global WATCH_TASK
        if self.Send in DBG_SD:
            DBG_SD.remove(self.Send)
        if self.Receive in DBG_RD:
            DBG_RD.remove(self.Receive)
        if self.OnPrompt in PROMPT_RD:
            PROMPT_RD.remove(self.OnPrompt)
            
        Watcher.wastching = False
        WATCH_TASK = None
    
    #@-node:ekr.20060513122450.367:Cancel
    #@+node:ekr.20060513122450.368:Send
    def Send(self):
        if len(self.Lines) > 0:
            Watcher.Watching = True
            vari = self.Lines.pop(0)
            aWrite(DBG["Evaluate"]+vari)
            DBG_SD.remove(self.Send)
            DBG_RD.append(self.Receive)
            PROMPT_RD.append(self.OnPrompt)
            self.Buffer = ""
            self.Count += 1
    #@nonl
    #@-node:ekr.20060513122450.368:Send
    #@+node:ekr.20060513122450.369:Receive
    def Receive(self,line):
        if DBG_PROMPT == False:		
            self.Buffer += line
    #@nonl
    #@-node:ekr.20060513122450.369:Receive
    #@+node:ekr.20060513122450.370:OnPrompt
    def OnPrompt(self):
        global WATCH_TASK
        
        Watcher.OutBox["state"] = 'normal'
        s = str(self.Count)+".0"
        e = str(self.Count)+".end"
        
        self.Buffer = self.Buffer.replace("\n"," ")
        
        if self.Buffer != Watcher.OutBox.get(s,e):
            changed = True
        else:
            changed = False
        
        Watcher.OutBox.delete(s,e+"+1c")
        Watcher.OutBox.insert(s,self.Buffer+"\n")	
        
        if changed == True:
            Watcher.OutBox.tag_add("changed",s,e)
            Watcher.OutBox.tag_config("changed",foreground ="red")
        
        Watcher.OutBox["state"] = 'disabled'
            
        if len(self.Lines) != 0:
            DBG_SD.append(self.Send)		
        else:
            Watcher.Watching = False
            WATCH_TASK = None
        
        PROMPT_RD.remove(self.OnPrompt)	
        DBG_RD.remove(self.Receive)
    
    #@-node:ekr.20060513122450.370:OnPrompt
    #@-others
    
#@nonl
#@-node:ekr.20060513122450.365:WATCHTASK
#@+node:ekr.20060513122450.371:QUERYGOTASK
class QUERYGOTASK(DBGTASK):

    #@    @+others
    #@+node:ekr.20060513122450.372:__init__
    def __init__(self,controller,index=None):
        
        self.controller = controller
        self.Query = DBG["Query location"]
        self.Find = controller.ReplaceVars(DBG["Find location"])
        if self.Query == "":
            controller.DBG_TASK.remove(self)
            Warning("xcc: ","Query location task is undefined!")
        elif index != None:
            controller.DBG_SD.insert(index,self.Send)
        else:
            controller.DBG_SD.append(self.Send)
    #@nonl
    #@-node:ekr.20060513122450.372:__init__
    #@+node:ekr.20060513122450.373:Send
    def Send(self):
        
        controller = self.controller
        controller.aWrite(self.Query)
        controller.DBG_SD.remove(self.Send)
        controller.DBG_RD.append(self.Receive)
    #@nonl
    #@-node:ekr.20060513122450.373:Send
    #@+node:ekr.20060513122450.374:Receive
    def Receive(self,line):
    
        controller = self.controller
        if controller.DBG_PROMPT == False:
            if line != "":
                m = re.search(self.Find,line,re.IGNORECASE)
                if m != None:
                    bline = m.group("LINE")
                    bext = m.group("EXT")
                        
                    if bline != None and bext != None:
                        if controller.VERBOSE == "True":					
                            controller.aAddText("\" Current location is: "+bline+" in "+bext+" file!\n")
                        bline = int(bline)	
                        SeekErrorClass(self.controller,bline,bext,color=BreakColor)
                    controller.DBG_RD.remove(self.Receive)
                    
                    if Watcher.visible and controller.ACTIVE_PROCESS:
                        if controller.SELECTED_NODE == controller.ACTIVE_NODE:
                            WATCHTASK(controller)
                        if controller.DBG_PROMPT:
                            controller.DbgOut("")
        else:
            controller.DBG_RD.remove(self.Receive)
                
    #@nonl
    #@-node:ekr.20060513122450.374:Receive
    #@-others
    
#@nonl
#@-node:ekr.20060513122450.371:QUERYGOTASK
#@+node:ekr.20060513122450.375:BREAKIDTASK
class BREAKIDTASK(DBGTASK):
    #@    @+others
    #@+node:ekr.20060513122450.376:__init__
    def __init__(self,b,index=0):
        
        if len(b) >0:
            self.Break = b
            self.ListBreaks = DBG["List breaks"]
            self.IdentifyBreak = ReplaceVars(DBG["Identify break"])
            
            if self.ListBreaks != "" and self.IdentifyBreak != "":
                if index != None:
                    DBG_SD.insert(index,self.Send)
                else:
                    DBG_SD.append(self.Send)
            else:
                Warning("xcc: ","Break Identification task is undefined!")
    #@nonl
    #@-node:ekr.20060513122450.376:__init__
    #@+node:ekr.20060513122450.377:Send
    def Send(self):
        aWrite(self.ListBreaks)
        DBG_SD.remove(self.Send)
        DBG_RD.append(self.Receive)
    
    #@-node:ekr.20060513122450.377:Send
    #@+node:ekr.20060513122450.378:Receive
    def Receive(self,line):
        global TARGET_PID
        if DBG_PROMPT == False:
            if line != "":
                idb = ReplaceVars(self.IdentifyBreak)
                            
                idb = idb.replace("_FILE_",self.Break[0]).replace("_LINE_",self.Break[1])
                m = re.search(idb,line,re.IGNORECASE)
                if m != None:
                    bid = m.group("ID")					
                    if bid != None:
                        if VERBOSE == "True":					
                            aAddText("\" Break id at line "+self.Break[1]+" in "+self.Break[0]+" is "+bid+"\n")
                        DBGTASK(ReplaceVars(DBG["Clear break"]).replace("_ID_",bid))
                        
        else:
            DBG_RD.remove(self.Receive)
                
    #@nonl
    #@-node:ekr.20060513122450.378:Receive
    #@-others
    
#@nonl
#@-node:ekr.20060513122450.375:BREAKIDTASK
#@-node:ekr.20060513122450.345:Debugger task classes
#@+node:ekr.20060513122450.43:class ProcessClass
class ProcessClass:

    #@    @+others
    #@+node:ekr.20060513122450.44:class READINGTHREAD
    class READINGTHREAD(threading.Thread):
        #@    @+others
        #@+node:ekr.20060513122450.45:__init__
        def __init__(self):
            threading.Thread.__init__(self)
            self.File = None
            self.Lock = thread.allocate_lock()
            self.Buffer = ""
        
            
        #@nonl
        #@-node:ekr.20060513122450.45:__init__
        #@+node:ekr.20060513122450.46:run
        def run(self):
            global Encoding
            try:
                s=self.File.read(1)	
                while s:
                    self.Lock.acquire()			
                    self.Buffer = self.Buffer + unicode(s,Encoding)
                    self.Lock.release()
                    s=self.File.read(1)
                    
            except IOError, ioerr:
                self.Buffer = self.Buffer +"\n"+ "[@run] ioerror :"+str(ioerr)
        
        #@-node:ekr.20060513122450.46:run
        #@+node:ekr.20060513122450.47:Update
        def Update(self,func):
            ret = True	
            if self.Lock.acquire(0) == 1:
                if self.Buffer and func != None:
                    func(self.Buffer)
                    self.Buffer=""
                else:
                    ret = self.isAlive()	
                self.Lock.release()	
            return ret
        
        
        
        
        #@-node:ekr.20060513122450.47:Update
        #@-others
    #@-node:ekr.20060513122450.44:class READINGTHREAD
    #@+node:ekr.20060513122450.48:__init__
    def __init__(self,controller,node,filename,args,start=None,out=None,err=None,end=None,spawn=False):
    
        self.controller = controller
        self.Node = node	
        self.Spawn = spawn	
        self.FileName = filename
        self.Arguments = args
        
        self.In = None
        self.OutThread = None
        self.ErrThread = None	
        
        self.OnStart = start
        self.Output = out
        self.Error = err
        self.OnEnd = end
        
        self.Kill = False
    #@-node:ekr.20060513122450.48:__init__
    #@+node:ekr.20060513122450.49:Open
    def Open(self):
        #getting file path and name
        try:
            if self.Spawn == True:
                os.spawnl(os.P_NOWAIT,self.FileName,self.Arguments)
                ProcessList.remove(self)
                return True
            
            
            path,fname = os.path.split(self.FileName)
        
            #check file validity
            if fname == "" or os.access(self.FileName,os.F_OK) != 1:		
                Error("xcc: ","PROCESS: "+self.FileName+" is invalid!")
                return	False
        
            #set the working directory
            oldwdir=os.getcwd()
            os.chdir(path)	
        
            #create the threads and open the pipe
            self.OutThread = self.READINGTHREAD()
            self.ErrThread = self.READINGTHREAD()
            self.In,self.OutThread.File,self.ErrThread.File	= os.popen3(fname+" "+self.Arguments)
            
            #reset the working dir
            os.chdir(oldwdir)
            
            if self.In == None or self.OutThread.File == None or self.ErrThread.File == None:
                Error("xcc: ","PROCESS: Can't open file!")
                return	False		
                                    
            #starting the thread
            self.OutThread.start()
            self.ErrThread.start()	
            
            #set the node marked and selected	
            self.Node.setMarked()	
        
            #self.Node.c.selectVnode(self.Node)
            LeoTop.redraw()
            
            return True
            
        except Exception:
            TraceBack()
    
    
    
    
    #@-node:ekr.20060513122450.49:Open
    #@+node:ekr.20060513122450.50:Close
    def Close(self):
        
        # close file and get error code
        if self.In != None:
            self.In.close()	
        
        if self.OutThread.File != None:
            self.OutThread.File.close()
            
        if self.ErrThread.File != None:
            exitcode = self.ErrThread.File.close()
        else:
            exitcode = None
        
        # set the node unmarked
        self.Node.clearMarked()
        self.Node = None	
            
        #process exit code with OnEnd
        if self.OnEnd != None:
            self.OnEnd(exitcode)	
        
        # redraw the stuff
        LeoTop.redraw()
        
        return exitcode
    
    
    #@-node:ekr.20060513122450.50:Close
    #@+node:ekr.20060513122450.51:Update
    def Update(self):
    
        if self.OutThread == None or self.ErrThread == None:
            return False
            
        #writing intro to console
        if self.OnStart != None:
            self.OnStart()
            self.OnStart = None
        
        if self.OutThread.Update(self.Output) != True and self.ErrThread.Update(self.Error) != True:
            return False
            
        return True
    #@-node:ekr.20060513122450.51:Update
    #@-others

#@-node:ekr.20060513122450.43:class ProcessClass
#@+node:ekr.20060513122450.52:widget classes
#@+node:ekr.20060513122450.53:class ConfigClass
class ConfigClass:
    #@    @+others
    #@+node:ekr.20060513122450.54:class PAGE
    class PAGE(Tk.Canvas):
        #@    @+others
        #@+node:ekr.20060513122450.55:class CHECK
        class CHECK:
            #@    @+others
            #@+node:ekr.20060513122450.56:__init__
            def __init__(self,master,n,x=0,y=0):
            
                self.Check = Tk.StringVar()
                self.Name = n
                c = Tk.Checkbutton(master,text=n,onvalue="True",offvalue="False",variable=self.Check)
                master.create_window(x,y,anchor='nw',window=c)
            #@nonl
            #@-node:ekr.20060513122450.56:__init__
            #@+node:ekr.20060513122450.57:Get
            def Get(self):
                return self.Check.get()
            #@-node:ekr.20060513122450.57:Get
            #@+node:ekr.20060513122450.58:Set
            def Set(self,value):
                self.Check.set(value)
            #@-node:ekr.20060513122450.58:Set
            #@-others
        #@-node:ekr.20060513122450.55:class CHECK
        #@+node:ekr.20060513122450.59:class ENTRY
        class ENTRY:
            #@    @+others
            #@+node:ekr.20060513122450.60:__init__
            def __init__(self,c,n,w=175,h=22,e=1,a='nw',x=0,y=0,re=False,vs=False):
                self.Name = n
                
                if re != False: fg = RegExpFgColor
                else: fg = "black"
                    
                if vs != False: bg = VarSupBgColor
                else: bg = "white"
                
                self.MasterFrame = mf = Tk.Frame(c,relief='groove',height=h,width=w)
                self.ID = c.create_window(x,y,anchor=a,window=mf,height=h,width=w)	
                
                self.Entry = Tk.Entry(mf,width=1,bg=bg)
                self.Entry.pack(side="right",fill="x",expand=e)
                l = Tk.Label(mf,text=n+":",fg=fg).pack(side="right")
            #@-node:ekr.20060513122450.60:__init__
            #@+node:ekr.20060513122450.61:Get
            def Get(self):
                return self.Entry.get()
            #@-node:ekr.20060513122450.61:Get
            #@+node:ekr.20060513122450.62:Set
            def Set(self,text):
                self.Entry.delete(0,'end')
                self.Entry.insert('end',text)
            #@-node:ekr.20060513122450.62:Set
            #@-others
        #@-node:ekr.20060513122450.59:class ENTRY
        #@+node:ekr.20060513122450.63:class TEXT
        class TEXT:
            #@    @+others
            #@+node:ekr.20060513122450.64:__init__
            def __init__(self,c,n,w=350,h=80,a='nw',x=0,y=0,re=False,vs=False):#text are 3 column wide
                
                self.Name = n
                
                if re != False: fg = RegExpFgColor
                else: fg = "black"
                    
                if vs != False: bg = VarSupBgColor
                else: bg = "white"
                
                self.MasterFrame = mf = Tk.Frame(c,relief='groove')
                self.ID = c.create_window(x,y+1,anchor=a,window=mf,width=w,height=h)
                
                lf = Tk.Frame(mf,relief='flat')
                lf.pack(side="top",fill="x",expand=1)			
                Tk.Label(lf,text=n+":",fg=fg).pack(side="left")
                
                self.Text = Tk.Text(mf,bg=bg)
                self.Text.pack(side="top",fill="x",expand=1)
            #@-node:ekr.20060513122450.64:__init__
            #@+node:ekr.20060513122450.65:Get
            def Get(self):
                s = self.Text.get(1.0,'end')
                lines = s.splitlines()
                res = ""
                for l in lines:
                    if l != "":
                        res += l+"\n"
                return res
            #@-node:ekr.20060513122450.65:Get
            #@+node:ekr.20060513122450.66:Set
            def Set(self,text):
                self.Text.delete(1.0,'end')
                self.Text.insert('end',text)
            #@-node:ekr.20060513122450.66:Set
            #@-others
        #@-node:ekr.20060513122450.63:class TEXT
        #@+node:ekr.20060513122450.67:class LABEL
        class LABEL:
            #@    @+others
            #@+node:ekr.20060513122450.68:__init__
            def __init__(self,c,text,w=175,h=22,e=1,a='nw',x=0,y=0,color="#%02x%02x%02x" % (150,150,150)):
                
                self.MasterFrame = mf = Tk.Frame(c,relief='groove',height=h,width=w)
                self.ID = c.create_window(x,y,anchor=a,window=mf,height=h,width=w)	
                
                self.Label = Tk.Label(c,text=text,justify='left',fg=color)
                self.ID = c.create_window(x,y,anchor=a,window=self.Label)
                
            #@nonl
            #@-node:ekr.20060513122450.68:__init__
            #@-others
        #@-node:ekr.20060513122450.67:class LABEL
        #@+node:ekr.20060513122450.69:class HELP
        class HELP(Tk.Button):
            #@    @+others
            #@+node:ekr.20060513122450.70:__init__
            def __init__(self,c,buttontext="<?",boxtitle="Help",msg="!",x=5,y=0):
                
                self.Title = boxtitle
                self.Message = msg
                Tk.Button.__init__(self,c,text=buttontext,command=self.Help)
                self.ID = c.create_window(x,y,anchor='nw',window=self)
            #@nonl
            #@-node:ekr.20060513122450.70:__init__
            #@+node:ekr.20060513122450.71:Help
            def Help(self):
                tkMessageBox.showinfo(self.Title,self.Message)
            #@nonl
            #@-node:ekr.20060513122450.71:Help
            #@-others
        #@nonl
        #@-node:ekr.20060513122450.69:class HELP
        #@+node:ekr.20060513122450.72:__init__
        def __init__(self,controller,name):
            
            self.controller = controller
            self.name = name
            self.Objects = []
            Tk.Canvas.__init__(self,controller.LeoFrame.split1Pane2)
            self.X=self.Y=self.W=self.H = 0
            self.CreateObjects(self)
        #@nonl
        #@-node:ekr.20060513122450.72:__init__
        #@+node:ekr.20060513122450.73:AddObject
        def AddObject(self,o):
            if o != None:
                self.Objects.append(o)
                self.X,self.Y,self.W,self.H = self.bbox('all')
        #@-node:ekr.20060513122450.73:AddObject
        #@+node:ekr.20060513122450.74:BBox
        def BBox(self):
            self.X,self.Y,self.W,self.H = self.bbox('all')
        #@-node:ekr.20060513122450.74:BBox
        #@+node:ekr.20060513122450.75:AddSep
        def AddSep(self,length=380,color="black"):
            if length != None:
                l = length
            else:
                l = self.W
            self.create_line(5,self.H+4,l+5,self.H+4,fill=color)
            self.H += 10
        #@-node:ekr.20060513122450.75:AddSep
        #@+node:ekr.20060513122450.76:CreateObjects
        def CreateObjects(self,master):#must overide
            pass
        #@-node:ekr.20060513122450.76:CreateObjects
        #@+node:ekr.20060513122450.77:SaveObjects
        def SaveObjects(self,pd=None):
            
            controller = self.controller
        
            if pd == None:
                pd = controller.sGet(self.name,init={})
            
            for o in self.Objects:
                pd[o.Name] = o.Get()
        #@-node:ekr.20060513122450.77:SaveObjects
        #@+node:ekr.20060513122450.78:LoadObjects
        def LoadObjects(self,pd=None):	
            if pd == None:
                pd = sGet(self.name,{})
            
            for o in self.Objects:
                if o.Name not in pd:				
                    pd[o.Name] = o.Get()
                else:
                    o.Set(pd[o.Name])
        #@nonl
        #@-node:ekr.20060513122450.78:LoadObjects
        #@+node:ekr.20060513122450.79:ClearObjects
        def ClearObjects(self,value=""):
            for o in self.Objects:
                o.Set(value)
        #@nonl
        #@-node:ekr.20060513122450.79:ClearObjects
        #@+node:ekr.20060513122450.80:Hide
        def Hide(self):
            
            controller = self.controller
            self.pack_forget()
            
            b = controller.Config.GetButton(self.name)
            b.config(relief='groove',fg="black")
            
            controller.LeoYBodyBar.config(command=controller.LeoBodyText.yview)
            controller.LeoBodyText.config(yscrollcommand=controller.LeoYBodyBar.set)
        #@nonl
        #@-node:ekr.20060513122450.80:Hide
        #@+node:ekr.20060513122450.81:Show
        def Show(self):
            
            if Config.ActivePage != None:
                Config.ActivePage.Hide()
                
            Config.ActivePage = self
            b = Config.GetButton(self.name)
            b.config(relief='sunken',fg="blue")	
            
            self.config(scrollregion=self.bbox('all'))
            self.config(yscrollcommand=LeoYBodyBar.set)
            
            LeoYBodyBar.config(command=self.yview)
            LeoYBodyBar.pack(side="right",fill="y")
            
            self.pack(expand=1,fill="both")
            
        #@-node:ekr.20060513122450.81:Show
        #@-others
    #@-node:ekr.20060513122450.54:class PAGE
    #@+node:ekr.20060513122450.82:__init__
    def __init__(self,controller):
        
        self.controller = controller
        self.Pages = []
        self.Buttons = []
        self.ActivePage = None
    
        #switch frame
        self.SwitchFrame = Tk.Frame(
            controller.LeoFrame.split1Pane2,relief='groove',bd=2,height=40,width=100)
        
        #title
        self.Title = Tk.Entry(self.SwitchFrame,justify='center')
        self.Title.pack(side="top",fill="x",expand=1)	
        
        self.AddPages()	
        #add pages switches
        for p in self.Pages:
            if p:
                b = Tk.Button(self.SwitchFrame,text=p.name,width=10,command=p.Show,relief='groove')
                self.Buttons.append(b)
                b.pack(side="left")
                if self.ActivePage == None:
                    self.ActivePage = p
            
        #Cancel button
        b = Tk.Button(self.SwitchFrame,text="Cancel",command=lambda: self.Hide(False))
        b.pack(side="right")
                
        #Load button
        b = Tk.Button(self.SwitchFrame,text="Load...",command=self.LoadFromFile)
        b.pack(side="right")
        
        #Save button
        b = Tk.Button(self.SwitchFrame,text="Save...",command=self.SaveToFile)
        b.pack(side="right")	
        
        self.BreakTags = {}
        self.visible = False
    #@nonl
    #@-node:ekr.20060513122450.82:__init__
    #@+node:ekr.20060513122450.83:GetPage
    def GetPage(self,name):
        for p in self.Pages:
            if p != None and p.name == name:
                return p
    #@nonl
    #@-node:ekr.20060513122450.83:GetPage
    #@+node:ekr.20060513122450.84:GetButton
    def GetButton(self,name):
        for b in self.Buttons:
            if b != None and b["text"] == name:
                return b
    #@-node:ekr.20060513122450.84:GetButton
    #@+node:ekr.20060513122450.85:Hide
    def Hide(self,save=True):
        
        controller = self.controller
        
        if self.visible == True:
            self.ActivePage.Hide()	
            self.SwitchFrame.pack_forget()
            controller.LeoYBodyBar.config(command=controller.LeoBodyText.yview)
            controller.LeoBodyText.config(yscrollcommand=controller.LeoYBodyBar.set)
            controller.LeoXBodyBar.pack(side = "bottom",fill="x")
            if controller.CHILD_NODE != None:
                controller.BreakBar.Show()
            controller.LeoBodyText.pack(expand=1, fill="both")
            
            if save == True:
                self.SaveToNode()
            controller.ToolBar.ConfigButton.config(command=self.Show,relief=RAISED)
            controller.ToolBar.DisplayFrame.pack(side="top",fill="x",expand=1)
            self.visible = False
    #@nonl
    #@-node:ekr.20060513122450.85:Hide
    #@+node:ekr.20060513122450.86:Show
    def Show(self):
        
        controller = self.controller
        if controller.Watcher.visible:
            controller.Watcher.Hide()			
        if controller.BreakBar.visible:
            controller.BreakBar.Hide()
        controller.ToolBar.DisplayFrame.pack_forget()
        controller.LeoBodyText.pack_forget()
        controller.LeoXBodyBar.pack_forget()
        controller.LeoYBodyBar.pack_forget()
        
        self.SwitchFrame.pack(side="top", fill="x")
        self.LoadFromNode()
        self.ActivePage.Show()
        controller.ToolBar.ConfigButton.config(command=self.Hide,relief='sunken')
        self.visible = True
        controller.c.redraw()
    #@nonl
    #@-node:ekr.20060513122450.86:Show
    #@+node:ekr.20060513122450.87:ClearConfig
    def ClearConfig(self):
        for p in self.Pages:
            if p.name == "Options":
                p.ClearObjects("False")
            else:
                p.ClearObjects()
    #@-node:ekr.20060513122450.87:ClearConfig
    #@+node:ekr.20060513122450.88:LoadFromNode
    def LoadFromNode(self):
    
        self.Title.delete(0,'end')
        self.Title.insert('end',sGet("Title"))
            
        for p in self.Pages:
            if p != None:
                p.LoadObjects()
    #@-node:ekr.20060513122450.88:LoadFromNode
    #@+node:ekr.20060513122450.89:SaveToNode
    def SaveToNode(self):
        
        controller = self.controller
        
        controller.sSet("Title",self.Title.get())
        
        for p in self.Pages:
            p and p.SaveObjects()
    #@nonl
    #@-node:ekr.20060513122450.89:SaveToNode
    #@+node:ekr.20060513122450.90:LoadFromFile
    def LoadFromFile(self):
        try:
            ft = ('XCC Config files', '.xcc'),
            s = tkFileDialog.askopenfilename(filetypes=ft,title="Open xcc connfiguration file...")
        
            if s == "":
                Error("xcc: ","Load action canceled by user!")
                return
            
            #read file and compose code
            f = file(s,"r")
            td = None
            code = "td ="+f.readline()
            f.close()
            
            # load in temp dict
            try:
                exec code
            except Exception:
                TraceBack()
                Error("xcc: ","File content is invalid!")
                return
            
            #	load each pages
            for p in self.Pages:
                if p.name in td:
                    p.LoadObjects(td[p.name])
                    
            #set title to file name
            name,ext = os.path.splitext(s)
            path,name = os.path.split(name)		
            self.Title.delete(0,'end')
            self.Title.insert('end',name)		
            
            #save to node to ensure integrity
            self.SaveToNode()
            
        except Exception:
            TraceBack()
    
    
    
    
    #@-node:ekr.20060513122450.90:LoadFromFile
    #@+node:ekr.20060513122450.91:SaveToFile
    def SaveToFile(self):
        try:
            
        
            ft = ('XCC Config files', '.xcc'),
            s = tkFileDialog.asksaveasfilename(
            filetypes=ft,
            title="Save xcc connfiguration file...",
            initialfile = self.Title.get()
            )
            
            if s == "":
                Error("xcc: ","Save action canceled by user!")
                return		
            
            name,ext = os.path.splitext(s)
                    
            td = {}
            
            # save each pages
            for p in self.Pages:
                td[p.name] = {}
                p.SaveObjects(td[p.name])	
            
            #write the dict to file
            f = file(name+".xcc","w+")
            Message("xcc: ","Writing config in "+name+".xcc")
            f.write(str(td))
            f.close()
            
            # reset title to file name
            path,name = os.path.split(name)		
            self.Title.delete(0,'end')
            self.Title.insert('end',name)
            
            # save to node
            self.SaveToNode()
        except Exception:
            TraceBack()
    
    
    
    
    
    
    
    #@-node:ekr.20060513122450.91:SaveToFile
    #@+node:ekr.20060513122450.92:Apply
    def Apply(self):
        self.SaveToNode()
        self.Hide()
    #@-node:ekr.20060513122450.92:Apply
    #@+node:ekr.20060513122450.93:AddPages
    def AddPages(self):
        
        controller = self.controller
        self.Pages.append(self.OPTPAGE(controller))
        self.Pages.append(self.CPLPAGE(controller))
        self.Pages.append(self.DBGPAGE(controller))
        self.Pages.append(self.EXEPAGE(controller))
        #self.Pages.append(self.CODPAGE(controller))
    #@nonl
    #@-node:ekr.20060513122450.93:AddPages
    #@+node:ekr.20060513122450.94:class OPTPAGE
    class OPTPAGE(PAGE):
        #@    @+others
        #@+node:ekr.20060513122450.95:__init__
        def __init__(self,controller):
            
            self.controller = controller
            ConfigClass.PAGE.__init__(self,controller,"Options")
        #@-node:ekr.20060513122450.95:__init__
        #@+node:ekr.20060513122450.96:CreateObjects
        def CreateObjects(self,master): # must overide
        
            #@    @+others
            #@+node:ekr.20060513122450.97:Actions Switches
            s1 = self.CHECK(master,"Create files",x=5,y=5)
            s2 = self.CHECK(master,"Auto include header",x=100,y=5)
            self.AddObject(s1)
            self.AddObject(s2)
            
            self.AddSep(length=self.W)
            s1 = self.CHECK(master,"Compile",x=5,y=self.H)
            s2 = self.CHECK(master,"Seek first error",x=100,y=self.H)
            self.AddObject(s1)
            self.AddObject(s2)
            
            self.AddSep(length=self.W)
            s1 = self.CHECK(master,"Execute",x=5,y=self.H)
            s2 = self.CHECK(master,"Connect to pipe",x=100,y=self.H)
            self.AddObject(s1)
            self.AddObject(s2)
            
            self.AddSep(length=self.W)
            s1 = self.CHECK(master,"Debug",x=5,y=self.H)
            s2 = self.CHECK(master,"Seek breakpoints",x=100,y=self.H)
            self.AddObject(s1)
            self.AddObject(s2)
            
            #-------------------------------------------------------------
            self.AddSep(self.W)
            self.AddObject(self.CHECK(master,"Xcc verbose",x=5,y=self.H))
            self.AddObject(self.CHECK(master,"Filter output",x=5,y=self.H))
            #@nonl
            #@-node:ekr.20060513122450.97:Actions Switches
            #@+node:ekr.20060513122450.98:Import
            #self.AddSep(self.W)
            #b = Tk.Button(master,text="Import...",width=10,default='disabled',command = ImportFiles)
            #master.create_window(self.X+5,self.H,width=60,height=20,anchor='nw',window=b)
            #c1 = self.CHECK(master,"Merge",x=80,y=self.H)
            #c2 = self.CHECK(master,"Use corresponding source/header",x=150,y=self.H)
            #self.AddObject(c1)
            #self.AddObject(c2)
            #@nonl
            #@-node:ekr.20060513122450.98:Import
            #@-others
        
            self.AddSep(length=self.W)
        #@nonl
        #@-node:ekr.20060513122450.96:CreateObjects
        #@-others
    #@-node:ekr.20060513122450.94:class OPTPAGE
    #@+node:ekr.20060513122450.99:class CPLPAGE
    class CPLPAGE(PAGE):
        #@    @+others
        #@+node:ekr.20060513122450.100:__init__
        def __init__(self,controller):
            
            self.controller = controller
            ConfigClass.PAGE.__init__(self,controller,"Compiler")
        #@nonl
        #@-node:ekr.20060513122450.100:__init__
        #@+node:ekr.20060513122450.101:Browse
        def Browse(self):
            e = None
            
            for o in self.Objects:
                if o != None and o.Name == "Compiler":
                    e=o
                    break
            
            if e != None:
                ft = ('Executables', '.exe;.bin'),
                s = tkFileDialog.askopenfilename(filetypes=ft,title="Locate Compiler...")
                
                if s == None:
                    Error("xcc: ","Action canceled by user!")
                    return
            
                if s == "":
                    Error("xcc: ","Empty path returned!")
                    return
            
                s = os.path.normpath(s)
                e.Set(s)
        #@-node:ekr.20060513122450.101:Browse
        #@+node:ekr.20060513122450.102:AddPath
        def AddPath(self,name):
            d = tkFileDialog.askdirectory()
            if d != "":
                d = d.replace("/","\\")
                for o in self.Objects:
                    if o.Name == name:
                        opaths = o.Get().splitlines()
                        npaths = []
                        
                        for p in opaths:
                            p = p.strip()
                            if p != "":
                                npaths.append(p)
                                
                        npaths.append(d)
                        
                        o.Set(string.join(npaths,"\n"))
        #@nonl
        #@-node:ekr.20060513122450.102:AddPath
        #@+node:ekr.20060513122450.103:CreateObjects
        def CreateObjects(self,master):#must overide
            #@    @+others
            #@+node:ekr.20060513122450.104:Executable
            x=10
            y=10
            text_w = 350
            text_h = 80
            
            # compiler entry -
            self.AddObject(self.ENTRY(master,"Compiler",x=5,y=5,w=350,h=20))
            b = Tk.Button(master,text=" ...",command=self.Browse)
            master.create_window(360,self.Y-2,anchor='nw',window=b)
            #@nonl
            #@-node:ekr.20060513122450.104:Executable
            #@+node:ekr.20060513122450.105:Arguments
            self.AddSep()
            #-------------------------------------------------
            
            
            t1 = self.TEXT(master,"Arguments",x=5,y=self.H,vs=True)
            self.HELP(master,boxtitle="Arguments info",msg=CplArgumentsHelp,x=360,y=self.H+20)
            self.AddObject(t1)
            
            #------------------------------------------
            t1 = self.TEXT(master,"Debug arguments",x=5,y=self.H,vs=True)
            self.HELP(master,boxtitle="Debug arguments info",msg=CplDebugArgumentsHelp,x=360,y=self.H+20)
            self.AddObject(t1)
            #@nonl
            #@-node:ekr.20060513122450.105:Arguments
            #@+node:ekr.20060513122450.106:Paths
            self.AddSep()
            #-------------------------------------------------------------
            b = Tk.Button(master,text="+..",command=lambda:self.AddPath("Include search paths"))
            master.create_window(360,self.H+58,anchor='nw',window=b)
            t1 = self.TEXT(master,"Include search paths",x=5,y=self.H)
            self.HELP(master,boxtitle="Include search paths info",msg=IncludeSearchPathsHelp,x=360,y=self.H+20)
            self.AddObject(t1)
            
            #-------------------------------------------------------------
            b = Tk.Button(master,text="+..",command=lambda:self.AddPath("Library search paths"))
            master.create_window(360,self.H+58,anchor='nw',window=b)
            t1 = self.TEXT(master,"Library search paths",x=5,y=self.H)
            self.HELP(master,boxtitle="Library search paths info",msg=LibrarySearchPathsHelp,x=360,y=self.H+20)
            self.AddObject(t1)
            
            #-------------------------------------------------------------
            t1 = self.TEXT(master,"Used libraries",x=5,y=self.H)
            self.HELP(master,boxtitle="Used libraries info",msg=UsedLibrariesHelp,x=360,y=self.H+20)
            self.AddObject(t1)
            
            #@-node:ekr.20060513122450.106:Paths
            #@+node:ekr.20060513122450.107:Symbols
            ww =19
            self.AddSep()
            #------------------------------------------------------
            lf = Tk.Frame(master,relief='flat',bd=2)
            master.create_window(self.X,self.H+2,width=text_w,height=20,anchor='nw',window=lf)
            Tk.Label(lf,text="Compiler symbols:").pack(side="left")
            self.H += 22
            
            self.HELP(master,boxtitle="Include path and Library path info",msg=IncludePathAndLibraryPathHelp,x=360,y=self.H)
            #Include path
            e1 = self.ENTRY(master,"Include path",x=5,y=self.H)
            #Library path
            e2 = self.ENTRY(master,"Library path",x=180,y=self.H)
            self.AddObject(e1)
            self.AddObject(e2)
            
            self.HELP(master,boxtitle="Use library and Check syntaxe info",msg=UseLibraryAndCheckSyntaxeHelp,x=360,y=self.H)
            #Use library
            e1 = self.ENTRY(master,"Use library",x=5,y=self.H)
            #Check syntaxe
            e2 = self.ENTRY(master,"Check syntaxe",x=180,y=self.H)
            self.AddObject(e1)
            self.AddObject(e2)
            
            self.HELP(master,boxtitle="Build exe and Build dll info",msg=BuildExeAndBuildDllHelp,x=360,y=self.H)
            #Build exe
            e1 = self.ENTRY(master,"Build exe",x=5,y=self.H)
            #Build dll
            e2 = self.ENTRY(master,"Build dll",x=180,y=self.H)
            self.AddObject(e1)
            self.AddObject(e2)
            
            self.HELP(master,boxtitle="Compile pch and Use pch info",msg=CompilePchAndUsePchHelp,x=360,y=self.H)
            #Compile pch
            e1 = self.ENTRY(master,"Compile pch",x=5,y=self.H)
            #Use pch
            e2 = self.ENTRY(master,"Use pch",x=180,y=self.H)
            self.AddObject(e1)
            self.AddObject(e2)
            #@nonl
            #@-node:ekr.20060513122450.107:Symbols
            #@+node:ekr.20060513122450.108:Error Detection
            # ------------------
            self.AddSep()
            e = self.ENTRY(master,"Error detection",x=5,y=self.H,w=350,re=True)
            self.HELP(master,boxtitle="Error detection info",msg=CplArgumentsHelp,x=360,y=self.H)
            self.AddObject(e)
            #@nonl
            #@-node:ekr.20060513122450.108:Error Detection
            #@-others
        
        
        
        #@-node:ekr.20060513122450.103:CreateObjects
        #@-others
    #@-node:ekr.20060513122450.99:class CPLPAGE
    #@+node:ekr.20060513122450.109:class DBGPAGE
    class DBGPAGE(PAGE):
        #@    @+others
        #@+node:ekr.20060513122450.110:__init__
        def __init__(self,controller):
            
            self.controller = controller
            ConfigClass.PAGE.__init__(self,controller,"Debugger")
        #@-node:ekr.20060513122450.110:__init__
        #@+node:ekr.20060513122450.111:Browse
        def Browse(self):
            e = None
            for o in self.Objects:
                if o != None and o.Name == "Debugger":
                    e=o
                    break
            if e != None:
                ft = ('Executables', '.exe;.bin'),
                s = tkFileDialog.askopenfilename(filetypes=ft,title="Locate Debugger...")
                
                if s == None:
                    Error("xcc: ","Action canceled by user!")
                    return
            
                if s == "":
                    Error("xcc: ","Empty path returned!")
                    return
            
                s = os.path.normpath(s)
                #s = s.replace("\\","\\\\")
                e.Set(s)
        #@-node:ekr.20060513122450.111:Browse
        #@+node:ekr.20060513122450.112:CreateObjects
        def CreateObjects(self,master):#must overide
            #@    @+others
            #@+node:ekr.20060513122450.113:Executable
            x=10
            y=10
            text_w = 350
            text_h = 80
                
            # compiler entry
            self.AddObject(self.ENTRY(master,"Debugger",x=5,y=5,w=350,h=20))
            b = Tk.Button(master,text=" ...",command=self.Browse)
            master.create_window(360,self.Y-2,anchor='nw',window=b)	
            #@-node:ekr.20060513122450.113:Executable
            #@+node:ekr.20060513122450.114:Arguments
            self.AddSep()
            t1 = self.TEXT(master,"Arguments",x=5,y=self.H,vs=True)
            self.HELP(master,boxtitle="Arguments info",msg=DbgArgumentsHelp,x=360,y=self.H+20)
            self.AddObject(t1)
            #@nonl
            #@-node:ekr.20060513122450.114:Arguments
            #@+node:ekr.20060513122450.115:Piping
            self.AddSep()
            e1 = self.ENTRY(master,"Prompt pattern",x=5,y=self.H,re=True) 
            e2 = self.ENTRY(master,"Pipe eol",x=180,y=self.H)
            
            self.HELP(master,boxtitle="Prompt pattern and Pipe eol info",msg=DbgPipingHelp,x=360,y=self.H)
            self.AddObject(e1)
            self.AddObject(e2)
            #@nonl
            #@-node:ekr.20060513122450.115:Piping
            #@+node:ekr.20060513122450.116:Symbols
            ww =19
                
            self.AddSep()
                
            lf = Tk.Frame(master,relief='flat',bd=2)
            master.create_window(5,self.H+2,width=text_w,height=20,anchor='nw',window=lf)
            Tk.Label(lf,text="Debugger commands symbols:").pack(side="left")
            self.H += 22
                
            # ------------------
            e1 = self.ENTRY(master,"Go",x=5,y=self.H)
            e2 = self.ENTRY(master,"Step in",x=180,y=self.H)
            self.AddObject(e1)
            self.AddObject(e2)
            
            # ------------------
            e1 = self.ENTRY(master,"Continue",x=5,y=self.H)
            e2 = self.ENTRY(master,"Step over",x=180,y=self.H)
            self.AddObject(e1)
            self.AddObject(e2)
                
            # ------------------
            e1 = self.ENTRY(master,"Stop",x=5,y=self.H)
            e2 = self.ENTRY(master,"Step out",x=180,y=self.H)
            self.AddObject(e1)
            self.AddObject(e2)
                
            # ------------------
            e1 = self.ENTRY(master,"Evaluate",x=5,y=self.H)
            self.AddObject(e1)
            #@nonl
            #@-node:ekr.20060513122450.116:Symbols
            #@+node:ekr.20060513122450.117:Startup Task
            #------------------------------------------------------
            self.AddSep()
            t1 = self.TEXT(master,"Startup task",x=5,y=self.H,vs=True)
            
            self.HELP(master,boxtitle="Startup task info",msg=DbgStartupTaskHelp,x=360,y=self.H+20)
            
            self.AddObject(t1)
            #@nonl
            #@-node:ekr.20060513122450.117:Startup Task
            #@+node:ekr.20060513122450.118:Target PID
            # ------------------
            self.AddSep()
            e = self.ENTRY(master,"Target pid task",x=5,y=self.H,w=350,vs=True)
            
            self.HELP(master,boxtitle="Target pid task and Find pid info",msg=DbgTargetPidHelp,x=360,y=self.H)
            self.AddObject(e)
            
            e = self.ENTRY(master,"Find pid",x=5,y=self.H,w=350,re=True,vs=True)
            self.AddObject(e)
            #@nonl
            #@-node:ekr.20060513122450.118:Target PID
            #@+node:ekr.20060513122450.119:Break info
            #------------------------------------------------------
            self.AddSep()
            self.HELP(master,boxtitle="Break detection info",msg=DbgBreakDetectionHelp,x=360,y=self.H+20)
            self.AddObject(self.TEXT(master,"Break detection",x=5,y=self.H,w=text_w,h=text_h,re=True))
            
            self.AddSep()
            e1 = self.ENTRY(master,"Set break",x=5,y=self.H,vs=True)
            e2 = self.ENTRY(master,"Clear break",x=180,y=self.H,vs=True)
            self.HELP(master,boxtitle="Set break and Clear break info",msg=DbgSetClearBreakHelp,x=360,y=self.H)
            self.AddObject(e1)
            self.AddObject(e2)
            
            self.AddSep()
            self.HELP(master,boxtitle="List breaks and Identify break info",msg=DbgBreakIdHelp,x=360,y=self.H)
            self.AddObject(self.ENTRY(master,"List breaks",x=5,y=self.H,w=350))
            e = self.ENTRY(master,"Identify break",x=5,y=self.H,w=350,re=True)
            self.AddObject(e)
            
            # ------------------
            self.AddSep()
            self.HELP(master,boxtitle="Query location and Find location info",msg=DbgLocationHelp,x=360,y=self.H)
            self.AddObject(self.ENTRY(master,"Query location",x=5,y=self.H,w=350))
            e = self.ENTRY(master,"Find location",x=5,y=self.H,w=350,re=True,vs=True)
            self.AddObject(e)
            #@nonl
            #@-node:ekr.20060513122450.119:Break info
            #@+node:ekr.20060513122450.120:Misc RE
            #-------------------------------------------------------------
            self.AddSep()
            t1 = self.TEXT(master,"Regular expression",x=4,y=self.H,w=173,re=True,vs=True)
            t2 = self.TEXT(master,"Task",x=180,y=self.H,w=173,vs=True)
            self.HELP(master,boxtitle="Regular expression and Task info",msg=DbgMiscExpHelp,x=360,y=self.H+20)
            self.AddObject(t1)
            self.AddObject(t2)
            #@nonl
            #@-node:ekr.20060513122450.120:Misc RE
            #@-others
        #@-node:ekr.20060513122450.112:CreateObjects
        #@-others
    #@-node:ekr.20060513122450.109:class DBGPAGE
    #@+node:ekr.20060513122450.121:class EXEPAGE
    class EXEPAGE(PAGE):
        #@    @+others
        #@+node:ekr.20060513122450.122:__init__
        def __init__(self,controller):
            
            self.controller = controller
            ConfigClass.PAGE.__init__(self,controller,"Executable")
        #@-node:ekr.20060513122450.122:__init__
        #@+node:ekr.20060513122450.123:CreateObjects
        def CreateObjects(self,master):#must overide
            bd=self["background"]
            x=10
            y=10
            text_w = 350
            text_h = 80
            #@    @+others
            #@+node:ekr.20060513122450.124:Args
            self.AddObject(self.TEXT(master,"Execution arguments",x=5,y=5))
            #@-node:ekr.20060513122450.124:Args
            #@+node:ekr.20060513122450.125:Dll Caller
            self.AddSep()
            e1 = self.ENTRY(master,"Dll caller",x=5,y=self.H,w=280,h=20)
            b = Tk.Button(master,text="Browse...",width=10,default='disabled')
            master.create_window(self.X+285,self.H,width=60,height=20,anchor='nw',window=b)
            self.AddObject(e1)
            #@nonl
            #@-node:ekr.20060513122450.125:Dll Caller
            #@-others
            self.create_line(0,self.H+5,self.W+1,self.H+5)
        #@nonl
        #@-node:ekr.20060513122450.123:CreateObjects
        #@-others
    #@-node:ekr.20060513122450.121:class EXEPAGE
    #@+node:ekr.20060513122450.126:class CODPAGE
    class CODPAGE(PAGE):
        #@    @+others
        #@+node:ekr.20060513122450.127:__init__
        def __init__(self):
        
            ConfigClass.PAGE.__init__(self,"Code")
        #@-node:ekr.20060513122450.127:__init__
        #@+node:ekr.20060513122450.128:CreateObjects
        def CreateObjects(self,master):#must overide
            bd=self["background"]
            x=10
            y=10
            text_w = 350
            text_h = 80
            #@    @+others
            #@+node:ekr.20060513122450.129:Entries
            self.AddObject(self.TEXT(master,"File header",x=5,y=5,w=350,h=80))
            self.AddSep()
            self.AddObject(self.ENTRY(master,"Class opening",x=5,y=self.H,w=350,h=20))
            self.AddObject(self.ENTRY(master,"Class closing",x=5,y=self.H,w=350,h=20))
            self.AddObject(self.ENTRY(master,"Class header",x=5,y=self.H,w=350,h=20))
            self.AddObject(self.ENTRY(master,"Class footer",x=5,y=self.H,w=350,h=20))
            self.AddSep()
            self.AddObject(self.ENTRY(master,"Function header",x=5,y=self.H,w=350,h=20))
            self.AddObject(self.ENTRY(master,"Function footer",x=5,y=self.H,w=350,h=20))
            self.AddObject(self.ENTRY(master,"Function opening",x=5,y=self.H,w=350,h=20))
            self.AddObject(self.ENTRY(master,"Function closing",x=5,y=self.H,w=350,h=20))
            self.AddSep()
            self.AddObject(self.TEXT(master,"File footer",x=5,y=self.H,w=350,h=80))
            #@nonl
            #@-node:ekr.20060513122450.129:Entries
            #@-others
            self.AddSep()
        #@nonl
        #@-node:ekr.20060513122450.128:CreateObjects
        #@-others
    #@-node:ekr.20060513122450.126:class CODPAGE
    #@-others
#@nonl
#@-node:ekr.20060513122450.53:class ConfigClass
#@+node:ekr.20060513122450.130:class DBGHELP
#@+node:ekr.20060513122450.131:DbgArgumentsHelp
DbgArgumentsHelp = """
Command line passed to to the debugger.
Each lines are concatenated using space.

The following variables are supported:
        
    _ABSPATH_
    _RELPATH_
    _NAME_
    _EXT_
    _SRCEXT_"""
#@nonl
#@-node:ekr.20060513122450.131:DbgArgumentsHelp
#@+node:ekr.20060513122450.132:DbgPipingHelp
DbgPipingHelp = """
Prompt pattern:
    Regular expression used to detect the debugger prompt.
    
Pipe eol:
    End of line character used when sending command to the debugger."""
#@nonl
#@-node:ekr.20060513122450.132:DbgPipingHelp
#@+node:ekr.20060513122450.133:DbgStartupTaskHelp
DbgStartupTaskHelp = """
Commands sent to the debugger at startup.
These commands must leave the debugger breaked
in the entry point of the target.

The following variables are supported:
    
    _ABSPATH_
    _RELPATH_
    _NAME_
    _EXT_
    _SRCEXT_"""
#@nonl
#@-node:ekr.20060513122450.133:DbgStartupTaskHelp
#@+node:ekr.20060513122450.134:DbgTargetPidHelp
DbgTargetPidHelp = """
Target pid task:
    Command used to retreive the target process identifier.
    The target pid is used to break into the debugger.

    The following variables are supported:
        _ABSPATH_
        _RELPATH_
        _NAME_
        _EXT_
        _SRCEXT_
    
Find pid:
    Regular expression used to retreive the target pid when
    the "Target pid task" is sent to the debugger.

    The following variables are supported:
        
        _ABSPATH_
        _RELPATH_
        _NAME_
        _EXT_
        _SRCEXT_
        
    The following groups must be returned by the regular expression:
        
        PID"""
#@nonl
#@-node:ekr.20060513122450.134:DbgTargetPidHelp
#@+node:ekr.20060513122450.135:DbgBreakDetectionHelp
DbgBreakDetectionHelp = """
Regular expression used to detect a break in target code execution.

When an output line match one of the expressions, an attempt is 
made to find the current location in the target code using the
"Query location" and "Find location" fields.

Each line is a different regular expression."""
#@nonl
#@-node:ekr.20060513122450.135:DbgBreakDetectionHelp
#@+node:ekr.20060513122450.136:DbgSetClearBreakHelp
DbgSetClearBreakHelp = """
Set break:
    Command used to set a breakpoint.
    
    The following variables are supported:
        
        _ABSPATH_
        _RELPATH_
        _NAME_
        _EXT_
        _SRCEXT_
        _FILE_
        _LINE_

Clear break:
    Command used to clear/delete a breakpoint.
    
    The following variables are supported:
        
        _ABSPATH_
        _RELPATH_
        _NAME_
        _EXT_
        _SRCEXT_
        _FILE_
        _LINE_
        _ID_*
        
    *If _ID_ is used, attempt to find it using the
    "List breaks" and "Identify break" fields."""
#@-node:ekr.20060513122450.136:DbgSetClearBreakHelp
#@+node:ekr.20060513122450.137:DbgBreakIdHelp
DbgBreakIdHelp = """
List breaks:
    Command used to list the debugger's break table.
    
    This field is ignored if the "Clear break" field
    make no use of the _ID_ variable.
    
Identify break:
    Regular expresion used to find the id of a breakpoint
    when the "List breaks" command is sent to the debugger.
    
    This field is ignored if the "Clear break" field
    make no use of the _ID_ variable.
    
    The following variables are supported:
        
        _ABSPATH_
        _RELPATH_
        _NAME_
        _EXT_
        _SRCEXT_
        _FILE_
        _LINE_
        
    The following groups must be returned by the regular expression:
        
        ID"""
#@-node:ekr.20060513122450.137:DbgBreakIdHelp
#@+node:ekr.20060513122450.138:DbgLocationHelp
DbgLocationHelp = """
Query location:
    Command used to retreive the file and line where
    the debugger is currently breaked.
    
Find location:
    Regular expression used to retreiv the current 
    file and line when the "Query location" command
    is sent to the debugger.
    
    The following variables are supported:
        
        _ABSPATH_
        _RELPATH_
        _NAME_
        _EXT_
        _SRCEXT_
        
    The following groups must be returned by the regular expression:
        
        EXT
        LINE

"""
#@-node:ekr.20060513122450.138:DbgLocationHelp
#@+node:ekr.20060513122450.139:DbgMiscExpHelp
DbgMiscExpHelp = """
Regular expression:
    Each line is a separate regular expression.
    
    If an output line is matched by one of the expression,
    the corresponding "Task" line is sent to the debugger.
        
    The following variables are supported:
        
        _ABSPATH_
        _RELPATH_
        _NAME_
        _EXT_
        _SRCEXT_
        
Task:
    Each line is a separate task trigered by the corresponding
    "Regular expression" line.
    
    The following variables are supported:
        
        _ABSPATH_
        _RELPATH_
        _NAME_
        _EXT_
        _SRCEXT_"""
#@nonl
#@-node:ekr.20060513122450.139:DbgMiscExpHelp
#@-node:ekr.20060513122450.130:class DBGHELP
#@+node:ekr.20060513122450.140:class CPLHELP
#@+node:ekr.20060513122450.141:CplArgumentsHelp
CplArgumentsHelp = """
Command line passed to to the compiler.
Each lines are concatenated using space.

The following variables are supported:
        
    _ABSPATH_
    _RELPATH_
    _NAME_
    _EXT_
    _SRCEXT_
    _BUILD_
    _INCPATHS_
    _LIBPATHS_
    _LIBRARIES_"""
#@nonl
#@-node:ekr.20060513122450.141:CplArgumentsHelp
#@+node:ekr.20060513122450.142:CplDebugArgumentsHelp
CplDebugArgumentsHelp = """
Command line passed to to the compiler 
when debugging is requested.
Each lines are concatenated using space.

The following variables are supported:
        
    _ABSPATH_
    _RELPATH_
    _NAME_
    _EXT_
    _SRCEXT_
    _BUILD_
    _INCPATHS_
    _LIBPATHS_
    _LIBRARIES_"""
#@nonl
#@-node:ekr.20060513122450.142:CplDebugArgumentsHelp
#@+node:ekr.20060513122450.143:IncludeSearchPathsHelp
IncludeSearchPathsHelp = """
Each lines is a path to be searched for include files.

These paths are assembled unsing the "Include path"
symbol to create the _INCPATHS_ variable."""
#@nonl
#@-node:ekr.20060513122450.143:IncludeSearchPathsHelp
#@+node:ekr.20060513122450.144:LibrarySearchPathsHelp
LibrarySearchPathsHelp = """
Each lines is a path to be searched for library files.

These paths are assembled unsing the "Library path"
symbol to create the _LIBPATHS_ variable."""
#@nonl
#@-node:ekr.20060513122450.144:LibrarySearchPathsHelp
#@+node:ekr.20060513122450.145:UsedLibrariesHelp
UsedLibrariesHelp = """
Each whitespace delimited word is a libary to be 
used while building the project.

These libraries are assembled unsing the "Use library"
symbol to create the _LIBRARIES_ variable."""
#@nonl
#@-node:ekr.20060513122450.145:UsedLibrariesHelp
#@+node:ekr.20060513122450.146:IncludePathAndLibraryPathHelp
IncludePathAndLibraryPathHelp = """
Include path:	
    Symbol used with "Include search path" field
    to create the _INCPATHS_ variable.
    
Library path:	
    Symbol used with "Library search path" field
    to create the _LIBPATHS_ variable."""
#@-node:ekr.20060513122450.146:IncludePathAndLibraryPathHelp
#@+node:ekr.20060513122450.147:UseLibraryAndCheckSyntaxeHelp
UseLibraryAndCheckSyntaxeHelp = """
Use library:	
    Symbol used with "Used libraries" field
    to create the _LIBRARIES_ variable.
    
Check syntaxe:	
    Symbol used when the project is a single
    header (.h extension). Header alone cant be 
    built but some compiler offer a syntaxe check."""
#@nonl
#@-node:ekr.20060513122450.147:UseLibraryAndCheckSyntaxeHelp
#@+node:ekr.20060513122450.148:BuildExeAndBuildDllHelp
BuildExeAndBuildDllHelp = """
One of these symbols will be used to replace
the _BUILD_ variable in the "Arguments" and 
"Debug arguments" fields.

The correct one is choosed according to the
project extension.

These generally determine if the output is 
single or multi-threaded.

Build exe:	
    Symbol used to build an executable.
    
Build dll:	
    Symbol used to build a dll."""
#@nonl
#@-node:ekr.20060513122450.148:BuildExeAndBuildDllHelp
#@+node:ekr.20060513122450.149:CompilePchAndUsePchHelp
CompilePchAndUsePchHelp = """
TODO: Support precompiled header auto creation/inclusion."""
#@nonl
#@-node:ekr.20060513122450.149:CompilePchAndUsePchHelp
#@+node:ekr.20060513122450.150:ErrorDetectionHelp
ErrorDetectionHelp = """
Regular expression used to detect error 
from the compiler output.

The following groups must be defined by
the regular expression:
    
    FILE
    LINE
    ID *
    DEF *
    
    * = Facultative groups"""
#@-node:ekr.20060513122450.150:ErrorDetectionHelp
#@-node:ekr.20060513122450.140:class CPLHELP
#@+node:ekr.20060513122450.151:class ToolbarClass
class ToolbarClass(Tk.Frame):
    
    #@    @+others
    #@+node:ekr.20060513122450.152:__init__
    def __init__(self,controller):
        
        self.controller = controller
            
        Tk.Frame.__init__(self,controller.LeoFrame.split1Pane2)
        f = Tk.Frame(self)
        f.pack(side="top",fill="x",expand=1)
        
        self.Go_e=Tk.PhotoImage(data=DecompressIcon(Go_e))
        self.GoButton = Tk.Button(f,command=self.Go,image=self.Go_e)
        self.GoButton.pack(side="left")
        
        self.Pause_e=Tk.PhotoImage(data=DecompressIcon(Pause_e))
        self.PauseButton = Tk.Button(f,image=self.Pause_e,command=controller.aPause,state='disabled')
        self.PauseButton.pack(side="left")
        
        self.Stop_e=Tk.PhotoImage(data=DecompressIcon(Stop_e))
        self.StopButton = Tk.Button(f,image=self.Stop_e,command=controller.aStop,state='disabled')
        self.StopButton.pack(side="left")
        
        self.StepIn_e=Tk.PhotoImage(data=DecompressIcon(StepIn_e))
        self.StepButton = Tk.Button(f,image=self.StepIn_e,state='disabled',command=controller.aStepIn)
        self.StepButton.pack(side="left")
        
        self.StepOver_e=Tk.PhotoImage(data=DecompressIcon(StepOver_e))
        self.StepInButton = Tk.Button(f,image=self.StepOver_e,state='disabled',command=controller.aStepOver)
        self.StepInButton.pack(side="left")
        
        self.StepOut_e=Tk.PhotoImage(data=DecompressIcon(StepOut_e))
        self.StepOutButton = Tk.Button(f,image=self.StepOut_e,state='disabled',command=controller.aStepOut)
        self.StepOutButton.pack(side="left")	
        
        self.Prompt_e=Tk.PhotoImage(data=DecompressIcon(Prompt_e))
        self.PromptButton = Tk.Button(f,image=self.Prompt_e,command=self.Refresh)
        
        s="<<"
        e=">>"
        # command entry
        self.DbgEntry = Tk.Entry(f)
        self.DbgEntry.bind("<Key>",self.OnKey)
        #self.DbgEntry.pack(side="left",fill="x",expand=1)
        
        #---------------------------------------------------
        self.ConfigGif=Tk.PhotoImage(data=DecompressIcon(ConfigData))
        self.ConfigButton = Tk.Button(f,image=self.ConfigGif,command=controller.Config.Show)
        self.ConfigButton.pack(side="right")
        
        self.WatchGif=Tk.PhotoImage(data=DecompressIcon(WatchData))
        self.WatchButton = Tk.Button(f,image=self.WatchGif,command=controller.Watcher.Show)
        self.WatchButton.pack(side="right")
        
        self.DisplayFrame = Tk.Frame(self)
        self.DisplayFrame.pack(side="top",fill="x",expand=1)
        
        fgcolor = "#808080"#BreakBar.fgcolor
        self.Spacer = Tk.Text(
            self.DisplayFrame,height=1,fg=fgcolor,relief='flat',
            font=controller.LeoFont,width=4,state='disabled')
        self.Spacer.pack(side="left")
        
        self.Display = Tk.Text(
            self.DisplayFrame,height=1,relief='flat',fg=fgcolor,bg=controller.BreakBar["bg"],
            font=controller.LeoFont,state='disabled')
        self.Display.pack(side="left",fill="x",expand=1)
    #@-node:ekr.20060513122450.152:__init__
    #@+node:ekr.20060513122450.153:Go
    def Go(self):
        
        controller = self.controller
      
        if not controller.ACTIVE_NODE:
            controller.sGo()
        elif controllerACTIVE_NODE == controllerSELECTED_NODE:
            controller.aGo()
        else:
            Error("xcc: ",str(controller.ACTIVE_NODE)+" is already active!")
    #@nonl
    #@-node:ekr.20060513122450.153:Go
    #@+node:ekr.20060513122450.154:Hide
    def Hide (self):
    
        controller = self.controller
        self.pack_forget()
        controller.LeoBodyText.config(wrap=controller.LeoWrap)
        if controller.Watcher.visible:
            controller.Watcher.Hide()
    #@nonl
    #@-node:ekr.20060513122450.154:Hide
    #@+node:ekr.20060513122450.155:Show
    def Show (self):
    
        controller = self.controller
        self.pack(side="top",fill="x")
        controller.LeoBodyText.config(wrap='none')
    
        if controller.Watcher.visible:
            controller.Watcher.Show()
    #@nonl
    #@-node:ekr.20060513122450.155:Show
    #@+node:ekr.20060513122450.156:OnKey
    def OnKey(self,event=None):
        
        if ACTIVE_NODE != None:
            if len(event.char)==1 and ord(event.char) == 13:
                aWrite(self.DbgEntry.get().replace("\n",""))
                self.DbgEntry.delete(0,'end')
    #@nonl
    #@-node:ekr.20060513122450.156:OnKey
    #@+node:ekr.20060513122450.157:EnableStep
    def EnableStep(self):
    
        self.StepButton["state"] = 'normal'
        self.StepInButton["state"] = 'normal'
        self.StepOutButton["state"] = 'normal'
    #@nonl
    #@-node:ekr.20060513122450.157:EnableStep
    #@+node:ekr.20060513122450.158:DisableStep
    def DisableStep(self):
    
        self.StepButton["state"] = 'disabled'
        #self.StepButton["image"] = self.Step_d
        
        self.StepInButton["state"] = 'disabled'
        #self.StepInButton["image"] = self.StepIn_d
        
        self.StepOutButton["state"] = 'disabled'
        #self.StepOutButton["image"] = self.StepOut_d
    #@nonl
    #@-node:ekr.20060513122450.158:DisableStep
    #@+node:ekr.20060513122450.159:SyncDisplayToChild
    def SyncDisplayToChild(self,loc):
        
        self.Display["cursor"] = ""
        self.Display.unbind("<Button-1>")
        self.Spacer["state"] = 'normal'
        self.Spacer.pack(side="left")
        if BreakBar.visible:
            self.Spacer["width"] = int(BreakBar["width"])+1
        else:
            self.Spacer["width"] = 4
        
        self.Spacer.delete(1.0,'end')
        self.Spacer.insert(INSERT,"."+loc.FOUND_FILE_EXT)
        self.Spacer["state"] = 'disabled'
        
        disp = ":: " ; as = ""
        for c in loc.CLASS_LIST:
            as += c+" :: "
        disp += as	
        off = 0
        if loc.CURRENT_RULE != None and loc.CURRENT_RULE != "class":
            off = len(disp)
            disp += CHILD_NODE.headString()	
        
        self.Display["state"] = 'normal'
        self.Display.delete(1.0,'end')
        self.Display.tag_delete("marking")
        self.Display.insert("insert",disp)
        
        if loc.CURRENT_RULE == "func":
            spec,ret,name,params,pure,dest,ctors = loc.CURRENT_MATCH_OBJECT
            
            v,s,e = spec
            if v != "":
                self.Display.tag_add("marking","1."+str(s+off),"1."+str(e+off))
            
            v,s,e = ret
            if s != -1 and e != -1:
                self.Display.tag_add("marking","1."+str(s+off),"1."+str(e+off))		
            
            params,s,e = params
            if params != "()":
                s += 1
                params = params.split(",")
                for p in params:
                    pmo = re.search("[( ]*(?P<TYPE>.+) +(?P<NAME>[^) ]+)[ )]*",p)
                    if pmo != None:
                        s2,e2 = pmo.span("TYPE")
                        self.Display.tag_add("marking","1."+str(s+off+s2-1),"1."+str(s+off+(e2-s2)))
                        off += len(p)+1
    
        self.Display.tag_config("marking",foreground="#7575e5")
        self.Display["state"] = 'disabled'
    #@-node:ekr.20060513122450.159:SyncDisplayToChild
    #@+node:ekr.20060513122450.160:SyncDisplayToError
    def SyncDisplayToError(self):
        self.Spacer["state"] = 'normal'
            
        if BreakBar.visible == True:
            self.Spacer["width"] = int(BreakBar["width"])+1
        else:
            self.Spacer["width"] = 4
        
        self.Spacer.delete(1.0,'end')
        self.Spacer.insert(INSERT,"ERR")
        self.Spacer["state"] = 'disabled'
        
        self.Display["state"] = 'normal'
        self.Display.delete(1.0,'end')
        self.Display.tag_delete("marking")
        
        self.Display.insert("insert",PARSE_ERROR)
        self.Display.tag_add("marking","1.0",'end')
        self.Display.tag_config("marking",foreground="red")
        self.Display["state"] = 'disabled'
        
        self.Display["cursor"] = "hand2"
        self.Display.bind("<Button-1>",self.OnErrorLeftClick)
    
    #@-node:ekr.20060513122450.160:SyncDisplayToError
    #@+node:ekr.20060513122450.161:SetError
    def SetError(self,err,node=None):
        global PARSE_ERROR,PARSE_ERROR_NODE
        
        PARSE_ERROR = err
        PARSE_ERROR_NODE = node
    #@nonl
    #@-node:ekr.20060513122450.161:SetError
    #@+node:ekr.20060513122450.162:OnErrorLeftClick
    def OnErrorLeftClick(self,event):
        
        self.controller.GoToNode(PARSE_ERROR_NODE)
    #@nonl
    #@-node:ekr.20060513122450.162:OnErrorLeftClick
    #@+node:ekr.20060513122450.163:HideInput
    def HideInput(self):
        self.PromptButton.pack_forget()
        self.DbgEntry.pack_forget()
    #@-node:ekr.20060513122450.163:HideInput
    #@+node:ekr.20060513122450.164:ShowInput
    def ShowInput(self):
        
        self.ConfigButton.pack_forget()
        self.WatchButton.pack_forget()
        
        self.PromptButton.pack(side="left")
        self.DbgEntry.pack(side="left",fill="x",expand=1)
    
        self.ConfigButton.pack(side="right")
        self.WatchButton.pack(side="right")
    #@nonl
    #@-node:ekr.20060513122450.164:ShowInput
    #@+node:ekr.20060513122450.165:Refresh
    def Refresh(self):
        
        controller = self.controller
    
        if (
            controller.ACTIVE_NODE and controller.DBG_PROMPT and
            controller.ACTIVE_NODE != controller.SELECTED_NODE
        ):
            controller.GoToNode(ACTIVE_NODE)
            QUERYGOTASK(controller)
            controller.DbgOut("")
    #@nonl
    #@-node:ekr.20060513122450.165:Refresh
    #@-others

#@-node:ekr.20060513122450.151:class ToolbarClass
#@+node:ekr.20060513122450.166:class WatcherClass
class WatcherClass(Tk.Frame):
    #@    @+others
    #@+node:ekr.20060513122450.167:__init__
    def __init__(self,controller):
       
        self.conroller = controller
        self.Watching = False
        self.visible = False
        
        Tk.Frame.__init__(self,controller.LeoFrame.split1Pane2,relief='groove')
        
        self.EditFrame = Tk.Frame(self,relief='groove')
        self.VarEntry = Tk.Entry(self.EditFrame)
        self.VarEntry.bind("<Key>",self.OnEditKey)
        self.VarEntry.pack(side="left",fill="x",expand=1)
        self.EditFrame.pack(side="top",fill="x")
        
        self.BoxFrame = Tk.Frame(self,relief='groove')
        self.BoxBar = Tk.Scrollbar(self.BoxFrame,command=self.yview)
        self.InBox = Tk.Text(
            self.BoxFrame,
                yscrollcommand=self.BoxBar.set,font=controller.LeoFont,
                state='disabled',width=20,wrap='none',height=10,
                selectbackground="white",selectforeground="black")
        self.InBox.pack(side="left",fill="both",expand=1)
        self.BoxBar.pack(side="left",fill="y")
        
        self.OutBox = Tk.Text(
            self.BoxFrame,yscrollcommand=self.BoxBar.set,
            font=controller.LeoFont,state='disabled',width=20,wrap='none',height=10,
            selectbackground="white",selectforeground="black")
        self.OutBox.pack(side="left",fill="both",expand=1)
    
        self.BoxFrame.pack(fill="both",expand=1)
        self.InBox.bind("<Delete>",self.OnDelete)
        self.OutBox.bind("<Delete>",self.OnDelete)
        self.InBox.bind("<Button-1>",self.OnLeftClick)
        self.OutBox.bind("<Button-1>",self.OnLeftClick)
    #@nonl
    #@-node:ekr.20060513122450.167:__init__
    #@+node:ekr.20060513122450.168:OnEditKey
    def OnEditKey(self,event):
        try:
            if self.Watching == False and len(event.char)==1 and ord(event.char) == 13:
                self.InBox.config(state='normal')
                self.OutBox.config(state='normal')
                
                var = self.VarEntry.get()
                sGet("Watch",[]).append(var)
                
                self.InBox.mark_set("insert",'end')			
                self.InBox.insert("insert",var+"\n")
                
                self.OutBox.mark_set("insert",'end')
                self.OutBox.insert("insert","- ?? -\n")
                
                self.InBox.config(state='disabled')
                self.OutBox.config(state='disabled')
                self.VarEntry.delete(0, 'end')
                
                if ACTIVE_PROCESS != None and DBG_PROMPT == True:
                    if SELECTED_NODE == ACTIVE_NODE:
                        WATCHTASK()
                        DbgOut("")
                #TODO: send a WATCHTASK if breaked
                
        except Exception:
            TraceBack()
    #@-node:ekr.20060513122450.168:OnEditKey
    #@+node:ekr.20060513122450.169:OnLeftClick
    def OnLeftClick(self,event):
        try:
            if self.InBox.get(1.0,'end').replace("\n","") != "":
                w = event.widget
                w.mark_set("insert","@0,"+str(event.y))
                l,c = w.index("insert").split(".")
            
                self.InBox.tag_delete("current")
                self.InBox.tag_add("current",l+".0",l+".end")
                self.InBox.tag_config("current",background=BreakColor)
            
                self.OutBox.tag_delete("current")
                self.OutBox.tag_add("current",l+".0",l+".end")
                self.OutBox.tag_config("current",background=BreakColor)
        except Exception:
            TraceBack()
    
    #@-node:ekr.20060513122450.169:OnLeftClick
    #@+node:ekr.20060513122450.170:OnDelete
    def OnDelete(self,event):
        if "current" in self.InBox.tag_names():
            ib = self.InBox
            ob = self.OutBox
            
            ib.config(state='normal')
            ob.config(state='normal')
            
            s,e = ib.tag_nextrange("current","1.0")
            
            var = ib.get(s,e)	
            watchs = sGet("Watch",[])
            if var in watchs:
                watchs.remove(var)		
            
            ib.delete(s,e+"+1c")
            ib.tag_delete("current")
                
            s,e = ob.tag_nextrange("current","1.0")
            ob.delete(s,e+"+1c")
            ob.tag_delete("current")
            
            ib.config(state='disabled')
            ob.config(state='disabled')
            
    
    #@-node:ekr.20060513122450.170:OnDelete
    #@+node:ekr.20060513122450.171:yview
    def yview(self, *args):
        apply(self.InBox.yview,args)
        apply(self.OutBox.yview,args)
    #@-node:ekr.20060513122450.171:yview
    #@+node:ekr.20060513122450.172:Hide
    def Hide(self):
        self.pack_forget()
        self.visible = False
        ToolBar.WatchButton.config(command=self.Show,relief=RAISED)
    #@-node:ekr.20060513122450.172:Hide
    #@+node:ekr.20060513122450.173:Show
    def Show(self):
        
        controller = self.controller
       
        if controller.Config.visible == True:
            controller.Config.Hide()
        controller.LeoBodyText.pack_forget()
        controller.LeoXBodyBar.pack_forget()
        controller.LeoYBodyBar.pack_forget()
        self.pack(side = "bottom",fill="x")
        controller.LeoXBodyBar.pack(side = "bottom",fill="x")
        controller.LeoYBodyBar.pack(side="right",fill="y")
        if controller.BreakBar.visible == True:
            controller.BreakBar.Hide()
            controller.BreakBar.Show()
        controller.LeoBodyText.pack(fill="both",expand=1)
        controller.ToolBar.WatchButton.config(command=self.Hide,relief='sunken')
        self.visible = True
        self.Sync()
                
        if (
            controller.ACTIVE_PROCESS and controller.DBG_PROMPT and
            controller.SELECTED_NODE == controller.ACTIVE_NODE
        ):
            WATCHTASK(conroller)
            controller.DbgOut("")
    #@nonl
    #@-node:ekr.20060513122450.173:Show
    #@+node:ekr.20060513122450.174:Sync
    def Sync(self):
        if self.visible == True:
            self.InBox.config(state='normal')
            self.OutBox.config(state='normal')
            
            self.InBox.delete(1.0,'end')
            self.OutBox.delete(1.0,'end')
            
            for v in sGet("Watch",[]):
                self.InBox.mark_set("insert",'end')			
                self.InBox.insert("insert",v+"\n")
                
                self.OutBox.mark_set("insert",'end')
                self.OutBox.insert("insert","- ?? -\n")	
        
            self.InBox.config(state='disabled')
            self.OutBox.config(state='disabled')
    
    #@-node:ekr.20060513122450.174:Sync
    #@-others
#@-node:ekr.20060513122450.166:class WatcherClass
#@+node:ekr.20060513122450.175:class BreakbarClass
class BreakbarClass(Tk.Text):

    #@    @+others
    #@+node:ekr.20060513122450.176:__init__
    def __init__(self,controller):
        
        self.controller = controller
        self.bodychanged = False	
        self.visible = False
        coffset = 10
        c = controller.LeoBodyText.winfo_rgb(controller.LeoBodyText["bg"])	
        red, green, blue = c[0]/256, c[1]/256, c[2]/256
        red -= coffset ; green -= coffset ; blue -= coffset	
        self.bgcolor = "#%02x%02x%02x" % (red,green,blue)
        red -= coffset*6 ; green -= coffset*6 ; blue -= coffset*6
        self.fgcolor = "#%02x%02x%02x" % (red,green,blue)
        
        Tk.Text.__init__(self,
            controller.LeoFrame.split1Pane2,
            name='sidebar',
            width=2,
            bd=controller.LeoBodyText["bd"],
            bg = self.bgcolor,
            relief='flat',
            setgrid=0,
            selectbackground = self.bgcolor,
            selectforeground = self.fgcolor,
            foreground = self.fgcolor,
            font=controller.LeoFont,
            pady=controller.LeoBodyText["pady"],
            cursor="hand2",
            wrap='none'
        )
        
        self.leowrap = controller.LeoBodyText["wrap"]
        self.bind("<Button-1>",self.OnLeftClick)
        self.bind("<Button-3>",self.OnRightClick)
        self["state"]='disabled'
        controller.LeoBodyText.pack_forget()
        controller.LeoXBodyBar.pack(side="bottom", fill="x")
        controller.LeoBodyText.pack(expand=1, fill="both")
    #@nonl
    #@-node:ekr.20060513122450.176:__init__
    #@+node:ekr.20060513122450.177:Scrollbar funcs
    #@+node:ekr.20060513122450.178:yview
    def yview(self,cmd=None,arg1=None,arg2=None):
        
        controller = self.controller
        w = controller.LeoBodyText
      
        if cmd:
            if arg1 != None:
                if arg2 != None:
                    w.yview(cmd,arg1,arg2)
                    Tk.Text.yview(self,cmd,arg1,arg2)
                else:
                    w.yview(cmd,arg1)
                    Tk.Text.yview(self,cmd,arg1)
        else:
            return w.yview()
    #@-node:ekr.20060513122450.178:yview
    #@+node:ekr.20060513122450.179:setForBody
    def setForBody(self,lo, hi):
        
        controller = self.controller
       
        Tk.Text.yview(self,'moveto',lo)	
        controller.LeoYBodyBar.set(lo,hi)	
    #@nonl
    #@-node:ekr.20060513122450.179:setForBody
    #@+node:ekr.20060513122450.180:setForBar
    def setForBar(self,lo, hi):
        
        controller = self.controller
        controller.LeoBodyText.yview('moveto',lo)	
        controller.LeoYBodyBar.set(lo,hi)
    #@nonl
    #@-node:ekr.20060513122450.180:setForBar
    #@+node:ekr.20060513122450.181:Plug
    def Plug(self):
        
        controller = self.controller
        
        controller.LeoBodyText.bind(g.angleBrackets("Cut"),self.OnCut)
        controller.LeoBodyText.bind(g.angleBrackets("Paste"),self.OnPaste)
        controller.LeoYBodyBar.config(command=self.yview)
        controller.LeoBodyText["yscrollcommand"] = self.setForBody
        self["yscrollcommand"] = self.setForBar
    #@nonl
    #@-node:ekr.20060513122450.181:Plug
    #@+node:ekr.20060513122450.182:UnPlug
    def UnPlug(self):
        
        controller = self.controller
        
        controller.LeoBodyText.bind(g.angleBrackets("Cut"),LeoFrame.OnCut)
        controller.LeoBodyText.bind(g.angleBrackets("Paste"),LeoFrame.OnPaste)
        controller.LeoYBodyBar.config(command=controller.LeoBodyText.yview)
        controller.LeoBodyText["yscrollcommand"] = controller.LeoYBodyBar.set
        self["yscrollcommand"] = None
    #@nonl
    #@-node:ekr.20060513122450.182:UnPlug
    #@-node:ekr.20060513122450.177:Scrollbar funcs
    #@+node:ekr.20060513122450.183:Events
    #@+node:ekr.20060513122450.184:OnCut
    def OnCut(self,event=None):
        LeoFrame.OnCut(event)#do normal stuff
        self.bodychanged = True
    #@-node:ekr.20060513122450.184:OnCut
    #@+node:ekr.20060513122450.185:OnPaste
    def OnPaste(self,event=None):
        LeoFrame.OnPaste(event)#do normal stuff
        self.bodychanged = True
    #@-node:ekr.20060513122450.185:OnPaste
    #@+node:ekr.20060513122450.186:OnRightClick
    def OnRightClick(self,event):
        try:
            m = Menu(self)
            m.add_command(label="Delete Node Breaks", command=self.DeleteNodeBreaks)
            m.add_command(label="Delete Project Breaks", command=self.DeleteProjectBreaks)
            m.add_separator()
            m.add_command(label="Cancel",command=lambda :self.Cancel(m))
            
            m.post(event.x_root,event.y_root)
        except Exception:
            TraceBack()
    #@-node:ekr.20060513122450.186:OnRightClick
    #@+node:ekr.20060513122450.187:OnLeftClick
    def OnLeftClick(self,event):
        
        controller = self.controller
        self["state"] = 'normal'	
        self.mark_set("insert","@0,"+str(event.y))
        self["state"] = 'disabled'
        l,c = self.index("insert").split(".")
        breaks = cGet("BreakPoints")
        
        loc = LOCATOR(CHILD_NODE,l)
        if loc.FOUND_FILE_LINE == None:
            return
        
        filext = loc.FOUND_FILE_EXT.replace(".","")
        
        if l in breaks:
            self.DeleteBreak(filext,loc.FOUND_FILE_LINE,l)
        else:
            t = controller.LeoBodyText.get(str(l)+".0",str(l)+".end")
            if t != "\n" and t != "" and t.strip() != "@others":
                self.AddBreak(filext,loc.FOUND_FILE_LINE,l)
        
        self.tag_delete(SEL)
    #@nonl
    #@-node:ekr.20060513122450.187:OnLeftClick
    #@-node:ekr.20060513122450.183:Events
    #@+node:ekr.20060513122450.188:Node breaks
    #@+node:ekr.20060513122450.189:AddNodeBreak
    def AddNodeBreak(self,l,s="Enabled"):
        cGet("BreakPoints")[l] = s
    #@-node:ekr.20060513122450.189:AddNodeBreak
    #@+node:ekr.20060513122450.190:DeleteNodeBreak
    def DeleteNodeBreak(self,l):
        breaks = cGet("BreakPoints")
        if l in breaks:
            del breaks[l]
    #@-node:ekr.20060513122450.190:DeleteNodeBreak
    #@+node:ekr.20060513122450.191:ClearNodeBreaks
    def ClearNodeBreaks(self):
        cSet("BreakPoints",{})
    #@-node:ekr.20060513122450.191:ClearNodeBreaks
    #@+node:ekr.20060513122450.192:BreaksFromNode
    def BreaksFromNode(self):
        
        self.ClearBreakTags()
        self.Sync()
        
        breaks = cGet("BreakPoints",{})
        for l,s in breaks.iteritems():
            self.AddBarBreak(l,s)
            self.AddBreakTag(l)
    #@-node:ekr.20060513122450.192:BreaksFromNode
    #@-node:ekr.20060513122450.188:Node breaks
    #@+node:ekr.20060513122450.193:Bar Breaks
    #@+node:ekr.20060513122450.194:AddBarBreak
    def AddBarBreak(self,l,s="Enabled"):
        self["state"] = 'normal'
        #----------------------------------------
            
        fl = self.get(l+".0",l+".end")
        self.insert(l+".end",(int(self["width"])-len(str(fl))-1)*" "+">")
        self.tag_add(l,l+".0",l+".end")
        
        if s == "Enabled":
            self.tag_config(l,foreground="blue")
        else:
            self.tag_config(l,foreground="gray")
        #-----------------------------------------
        self["state"] = 'disabled'
    
    #@-node:ekr.20060513122450.194:AddBarBreak
    #@+node:ekr.20060513122450.195:DeleteBarBreak
    def DeleteBarBreak(self,l):
        self["state"] = 'normal'
        #----------------------------------------
        #self.insert(l+".end -2c","  ")
        self.delete(l+".end -1c",l+".end")
        self.tag_delete(l)	
        
        
        #-----------------------------------------
        self["state"] = 'disabled'
        self.update_idletasks()
    
    
    #@-node:ekr.20060513122450.195:DeleteBarBreak
    #@+node:ekr.20060513122450.196:ClearBarBreaks
    def ClearBarBreaks(self):
        self["state"] = 'normal'
        self.delete(1.0,'end')	
        #----------------------------------------
        if CHILD_LINE != None and CHILD_LINE != -1:
            fl = CHILD_LINE
            lines = CHILD_NODE.bodyString().splitlines()
            
            while len(lines) > 0:
                l = lines.pop(0)
                if l.strip() != "@others":
                    self.insert("end",str(fl)+"\n")
                    fl += 1
                else:
                    break
        
            if len(lines) > 0 and l.strip() == "@others":
                self.insert("end","\n")
                
                loc = LOCATOR(CHILD_NODE,fl-CHILD_LINE+2)
                fl = loc.FOUND_FILE_LINE
                
                if fl != None:
                    while len(lines) > 0:
                        l = lines.pop(0)
                        self.insert("end",str(fl)+"\n")
                        fl += 1
            
            self.config(width = len(str(fl))+1)
        #-----------------------------------------
        self["state"] = 'disabled'
    #@-node:ekr.20060513122450.196:ClearBarBreaks
    #@-node:ekr.20060513122450.193:Bar Breaks
    #@+node:ekr.20060513122450.197:tag breaks
    #@+node:ekr.20060513122450.198:AddBreakTag
    def AddBreakTag(self,l):
        
        w = self.controller.LeoBodyText
        
        w.tag_add("xcc_break",l+".0",l+".end")
    #@nonl
    #@-node:ekr.20060513122450.198:AddBreakTag
    #@+node:ekr.20060513122450.199:DeleteBreakTag
    def DeleteBreakTag(self,s,e=None):
        
        w = self.controller.LeoBodyText
        
        if e == None:
            w.tag_remove("xcc_break",s+".0",s+".end")
        else:
            w.tag_remove("xcc_break",s,e)
    #@nonl
    #@-node:ekr.20060513122450.199:DeleteBreakTag
    #@+node:ekr.20060513122450.200:ClearBreakTags
    def ClearBreakTags(self):
        
        w = self.controller.LeoBodyText
        w.tag_delete("xcc_break")
        w.tag_config("xcc_break",background=self.bgcolor)
    #@nonl
    #@-node:ekr.20060513122450.200:ClearBreakTags
    #@+node:ekr.20060513122450.201:BreaksFromTags
    def BreaksFromTags(self):
        
        w = self.controller.LeoBodyText
        self.ClearNodeBreaks()
        self.ClearBarBreaks()
        range = w.tag_nextrange("xcc_break","1.0")
        while len(range) > 0:
            s,e = range
            el,ec = e.split(".")
            self.DeleteBreakTag(s,e)
            self.AddBreak(CHILD_EXT,CHILD_LINE,el)
            range = w.tag_nextrange("xcc_break",el+".end")
    #@nonl
    #@-node:ekr.20060513122450.201:BreaksFromTags
    #@-node:ekr.20060513122450.197:tag breaks
    #@+node:ekr.20060513122450.202:AddBreak
    def AddBreak(self,filext,fileline,bodyline,state="Enabled"):
        breaks = sGet("BreakPoints",{})
        
        breaks[filext+":"+str(fileline)] = state
        self.AddNodeBreak(bodyline,state)
        self.AddBarBreak(bodyline,state)
        self.AddBreakTag(bodyline)
        
        if ACTIVE_PROCESS != None:
            bpat = DBG["Set break"]
            bpat = bpat.replace("_FILE_",NAME+"."+filext).replace("_LINE_",str(fileline))
            DBGTASK(bpat)
            if DBG_PROMPT == True:
                DbgOut("")
    
    #@-node:ekr.20060513122450.202:AddBreak
    #@+node:ekr.20060513122450.203:DeleteBreak
    def DeleteBreak(self,filext,fileline,bodyline):
        breaks = sGet("BreakPoints",{})
        
        if filext+":"+str(fileline) in breaks:
            del breaks[filext+":"+str(fileline)]	
        
        self.DeleteNodeBreak(bodyline)
        self.DeleteBarBreak(bodyline)
        self.DeleteBreakTag(bodyline)
        
        if ACTIVE_PROCESS != None:
            if DBG["Clear break"].find("_ID_") != -1:
                BREAKIDTASK([filext,str(fileline)])
            else:
                DBGTASK(ReplaceVars(DBG["Clear break"]).replace("_FILE_",filext).replace("_LINE_",str(fileline)))
            
            if DBG_PROMPT == True:
                DbgOut("")
    #@nonl
    #@-node:ekr.20060513122450.203:DeleteBreak
    #@+node:ekr.20060513122450.204:DeleteNodeBreaks
    def DeleteNodeBreaks(self):
        try:
            breaks = cGet("BreakPoints",{})
            
            if CHILD_LINE != None and CHILD_EXT != None and ACTIVE_PROCESS != None:
                for bp in breaks.keys():				
                    self.DeleteBreak(CHILD_EXT,CHILD_LINE+int(bp),int(bp))
                    if ACTIVE_PROCESS != None:
                        
                        
                        self.DeleteDbgBreaks()
            
            cSelect(CHILD_NODE)
        except Exception:
            TraceBack()
    
    #@-node:ekr.20060513122450.204:DeleteNodeBreaks
    #@+node:ekr.20060513122450.205:DeleteProjectBreaks
    def DeleteProjectBreaks(self):
        try:		
            if SELECTED_NODE != None:
                for c in SELECTED_NODE.subtree_iter():
                    ua = GetUnknownAttributes(c.v)
                    if ua != None and "xcc_child_cfg" in ua.keys():
                        if "BreakPoints" in ua["xcc_child_cfg"].keys():
                            ua["xcc_child_cfg"]["BreakPoints"] = {}
            
                cSelect(CHILD_NODE)
        except Exception:
            TraceBack()
    #@nonl
    #@-node:ekr.20060513122450.205:DeleteProjectBreaks
    #@+node:ekr.20060513122450.206:Hide
    def Hide(self,erase = False):
        
        w = self.controller.LeoBodyText
        self.UnPlug()
        self.pack_forget()
        w.pack(expand=1, fill="both")
        w.tag_delete("xcc_break")
        self.visible = False
    #@nonl
    #@-node:ekr.20060513122450.206:Hide
    #@+node:ekr.20060513122450.207:Show
    def Show(self):
        
        controller = self.controller
    
        self.Plug()
        w.pack_forget()
        if self.leowrap != 'none':
            controller.LeoXBodyBar.pack(side="bottom", fill="x")
        border = controller.LeoBodyText["bd"]
        self.config(pady=LeoBodyText["pady"],bd=border)
        self.pack(side='left', fill="y")
        LeoBodyText.pack(expand=1, fill="both")
        self.BreaksFromNode()
        self.visible = True
    #@nonl
    #@-node:ekr.20060513122450.207:Show
    #@+node:ekr.20060513122450.208:Sync
    def Sync(self):
        self["state"] = 'normal'
        self.delete(1.0,'end')	
        #----------------------------------------
        w=4
        if CHILD_LINE != None and CHILD_LINE != -1:
            fl = CHILD_LINE
            lines = CHILD_NODE.bodyString().splitlines()
            
            while len(lines) > 0:
                l = lines.pop(0)
                if l.strip() != "@others":
                    self.insert("end",str(fl)+"\n")
                    fl += 1
                else:
                    break
        
            if len(lines) > 0 and l.strip() == "@others":
                self.insert("end","\n")
                
                loc = LOCATOR(CHILD_NODE,fl-CHILD_LINE+2)
                fl = loc.FOUND_FILE_LINE
                
                if fl != None:
                    while len(lines) > 0:
                        l = lines.pop(0)
                        self.insert("end",str(fl)+"\n")
                        fl += 1
            if len(str(fl))+1 < w:
                pass
            else:
                w = len(str(fl))+1
        self.config(width = w)
        #-----------------------------------------
        self["state"] = 'disabled'
    #@-node:ekr.20060513122450.208:Sync
    #@+node:ekr.20060513122450.209:IdleUpdate
    def IdleUpdate(self):
        if self.bodychanged == True:
            self.Sync()
            self.bodychanged = False
    #@nonl
    #@-node:ekr.20060513122450.209:IdleUpdate
    #@+node:ekr.20060513122450.210:Cancel
    def Cancel(self,menu):
        menu.unpost()
        
    #@-node:ekr.20060513122450.210:Cancel
    #@-others
#@-node:ekr.20060513122450.175:class BreakbarClass
#@-node:ekr.20060513122450.52:widget classes
#@+node:ekr.20060513122450.211:class Parsing
#@+node:ekr.20060513122450.212:CPPPARSER
class CPPPARSER:
    #@    @+others
    #@+node:ekr.20060513122450.213:Rules
    #@+node:ekr.20060513122450.214:LoadCppRules
    def LoadCppRules(self):
        self.OUTFUNC_RULES = [
        self.DOCRULE(),
        self.COMMENTRULE(),	#placed fisrt to allow functions and class to be commented out
        self.FUNCRULE(),
        self.CLASSRULE(),	#must be after CppFuncRule or it will catch template funcs
        self.DEFAULTRULE()	#must be the last rule cos it always proceed
        ]
        
        self.RULES = self.OUTFUNC_RULES
        
        self.INFUNC_RULES = [
        self.DOCRULE(),
        self.FUNCCOMMENTRULE(),	#placed fisrt to allow functions and class to be commented out
        self.FUNCDEFAULTRULE()	#must be the last rule cos it always proceed
        ]
    #@nonl
    #@-node:ekr.20060513122450.214:LoadCppRules
    #@+node:ekr.20060513122450.215:ATRULE
    class DOCRULE:
        #@    @+others
        #@+node:ekr.20060513122450.216:Match
        def Match(self,head):
            if head.startswith("@"):
                return head
            else:
                return None
        #@-node:ekr.20060513122450.216:Match
        #@+node:ekr.20060513122450.217:OnMatch
        def OnMatch(self,mo,node):
            Parser.SetRealBodyDestination()	
            return True
        #@-node:ekr.20060513122450.217:OnMatch
        #@-others
    #@nonl
    #@-node:ekr.20060513122450.215:ATRULE
    #@+node:ekr.20060513122450.218:COMMENTRULE
    class COMMENTRULE:
        #@    @+others
        #@+node:ekr.20060513122450.219:Match
        def Match(self,head):
            if head.startswith("//"):
                if head.endswith(";"):
                    return True
                else:
                    return False
            else:
                return None
        
        #@-node:ekr.20060513122450.219:Match
        #@+node:ekr.20060513122450.220:OnMatch
        def OnMatch(self,mo,node):
            
            if Parser.CLASS_WRITER != None:
                w = Parser.CLASS_WRITER
            else:	
                if mo == True:
                    w = Parser.Define
                else:
                    w = Parser.Declare
            
            Parser.SetRealBodyDestination(w)
            Parser.CURRENT_LOCATION = "head"
            w(Parser.TAB_STRING+"/*"+node.headString()[2:]+"\n")
            Parser.Tab()
            
            if Parser.WriteOthers(node,w) == False:
                return False
            
            Parser.CURRENT_LOCATION = "tail"
            Parser.UnTab()
            w(Parser.TAB_STRING+"*/\n")
        
            return True
        #@-node:ekr.20060513122450.220:OnMatch
        #@-others
    #@nonl
    #@-node:ekr.20060513122450.218:COMMENTRULE
    #@+node:ekr.20060513122450.221:FUNCRULE
    class FUNCRULE:
        #@    @+others
        #@+node:ekr.20060513122450.222:Match
        def Match(self,head):	
            params_e = head.rfind(")")
            if params_e > -1:
                
                tctors = head.split(":")
                head = tctors.pop(0)
                
                ctors = ""
                for c in tctors:
                    ctors += ":"+c		
                
                head = head.split()
                head = string.join(head)
                params_e = head.rfind(")")
                params_s = head.rfind("(",0,params_e)
                
                if params_s > -1:
                    # pure & dest ----------------------
                    pure_s = head.find("=0",params_e)
                    if pure_s > -1:				
                        pure = (head[pure_s:pure_s+2],pure_s,pure_s+2)
                        dest = (head[pure_s+2:],pure_s+2,len(head))
                    else:
                        pure = ("",-1,-1)
                        dest = (head[params_e+1:],params_e+1,len(head))
                    
                    # params ------------------------			
                    params = (head[params_s:params_e+1],params_s,params_e+1)			
                    
                    # name ---------------------------
                    name_s = head.find("operator")
                    if name_s == -1:
                        name_s = head.rfind(" ",0,params_s)
                        if name_s > -1:
                            name_s += 1
                    
                    if name_s > 0:
                        name = (head[name_s:params_s],name_s,params_s)
                        
                        ret_s = head.rfind(" ",0,name_s-1)
                        
                        if ret_s > -1:
                            ret = (head[ret_s+1:name_s-1],ret_s+1,name_s-1)
                            spec = (head[:ret_s],0,ret_s)
                        else:
                            ret = (head[:name_s],0,name_s)
                            spec = ("",-1,-1)
                    else:
                        name = (head[:params_s],0,params_s)
                        ret = ("",-1,-1)
                        spec = ("",-1,-1)
                    
                    r = (spec,ret,name,params,pure,dest,ctors)
                    return r
                        
                    
                    
                    
            return None
            
        #@-node:ekr.20060513122450.222:Match
        #@+node:ekr.20060513122450.223:OnMatch
        def OnMatch(self,mo,node):
            Parser.CURRENT_RULE = "func"
            
            spec,ret,name,params,pure,dest,ctors = self.Groups = mo	
                
            if Parser.CLASS_WRITER != None:
                wf = Parser.CLASS_WRITER
            else:	
                if dest[0] == "":
                    wf = Parser.Declare#in hdr if EXT != cpp or EXT != c
                else:
                    wf = Parser.Define#in src if EXT != h	
            
            if pure[0] == "":#define the func, possibly splitted
                
                if dest[0] == "":#func is not splitted
                    return self.DefineFunc(wf,node,full=True)
                
                else:#func may be splitted
                    if Parser.Declare != Parser.Define and dest[0] != "":#func may be splitted
                        if Parser.CLASS_WRITER == None:#func may be splitted
                            if "!" not in dest[0]:
                                if self.DeclareFunc(Parser.Declare) == False:
                                    return False
                                return self.DefineFunc(Parser.Define,node)
                            else:
                                return self.DefineFunc(Parser.Define,node,full=True)
                        
                        else:	#func may be splitted					
                            if Parser.CLASS_WRITER == Parser.Declare:#func is split
                                if self.DeclareFunc(Parser.Declare) == False:
                                    return False
                                return self.DefineFunc(Parser.Define,node,push=True)
                            
                            else:#func is not splitted, written with the class	
                                return self.DefineFunc(Parser.CLASS_WRITER,node)
                    
                    else:#func is not splitted
                        return self.DefineFunc(wf,node,full=True)
                
            else:#only declare the func, real destination depend upon DEST group and EXT
                return self.DeclareFunc(wf)
                
            
        #@nonl
        #@-node:ekr.20060513122450.223:OnMatch
        #@+node:ekr.20060513122450.224:DeclareFunc
        def DeclareFunc(self,wf):
            global LOCATE_CHILD,PARSE_ERROR
            spec,ret,name,params,pure,dest,ctors = self.Groups
            
            if name[0] == "":
                ToolBar.SetError("No function name in : "+GetNodePath(Parser.CURRENT_NODE),Parser.CURRENT_NODE)
                return False
            
            proto = spec[0] +" "+ ret[0] +" "+ name[0] + params[0] + pure[0] +";"
                    
            Parser.SetRealBodyDestination()
            Parser.CURRENT_LOCATION = "head"
            Parser.CURRENT_FUNC = proto
            #wf(Parser.TAB_STRING+Parser.CODE_SPLITER)
            wf(Parser.TAB_STRING+proto.strip()+"\n")	
                
            return True
        #@nonl
        #@-node:ekr.20060513122450.224:DeclareFunc
        #@+node:ekr.20060513122450.225:DefineFunc
        def DefineFunc(self,wf,node,full=False,push=False):
            global LOCATE_CHILD,PARSE_ERROR
            spec,ret,name,params,pure,dest,ctors = self.Groups
            if name[0] == "":
                ToolBar.SetError("No function name in : "+GetNodePath(Parser.CURRENT_NODE),Parser.CURRENT_NODE)
                return False
            
            Parser.FUNC_WRITER = wf
            proto = ""
            as = "" #access specifier
            
            if full == True:
                proto = spec[0]+" "
                params = params[0].strip("()")
            else:
                for n in Parser.CLASS_LIST:#if full == True, declared and defined at once, so no access specifier
                    if n != None:
                        as = n+"::"+as
                
                #if this is not a full definition, must remove default parameter assignement
                params = params[0].strip("()")
                paramslist = params.split(",")
                params = ""
                for p in paramslist:
                    pa = p.split("=")
                    if params != "":
                        params += ","+pa[0]
                    else:
                        params += pa[0]
                
            proto += ret[0]+" "+as+name[0]+"("+params+")"+ctors
            proto = proto.strip()
            
            if push == True:
                Parser.PushTab()
            
            
            Parser.SetRealBodyDestination(wf)
            Parser.CURRENT_LOCATION = "head"
            Parser.CURRENT_FUNC = proto
            if FUNC_HDR != "":
                wf(Parser.TAB_STRING+FUNC_HDR)
            wf(Parser.TAB_STRING+proto+FUNC_OPN)
            Parser.Tab()
            
            Parser.RULES = Parser.INFUNC_RULES	
            if Parser.WriteOthers(node,wf) == False:
                return False	
            Parser.RULES = Parser.OUTFUNC_RULES
            
            Parser.CURRENT_FUNC = ""
            Parser.UnTab()
            Parser.CURRENT_LOCATION = "tail"	
            wf(Parser.TAB_STRING+"}\n")
            if FUNC_FTR != "":
                wf(Parser.TAB_STRING+FUNC_FTR)
            
            if push == True:
                Parser.PopTab()
                
            return True
        
        #@-node:ekr.20060513122450.225:DefineFunc
        #@-others
    #@nonl
    #@-node:ekr.20060513122450.221:FUNCRULE
    #@+node:ekr.20060513122450.226:CLASSRULE
    class CLASSRULE:
        #@    @+others
        #@+node:ekr.20060513122450.227:Match
        #"^(?P<SPEC>.*) *class +(?P<NAME>[^;:!]+)* *(?P<BASE>:[^;!]+)* *(?P<INST>![^;]+)* *(?P<DEST>;$)*"
        #spec class name base inst dest
        def Match(self,head):
            #return self.Matcher.search(head)
            class_s = head.find("class ")
            if class_s > -1:
                head = head.split()
                head = string.join(head)
                class_s = head.rfind("class ")
                
                spec = (head[:class_s],0,class_s)
                name_s = class_s+6		
                dest_s = head.find(";",name_s)
                inst_s = head.find("!",name_s)
                base_s = head.find(":",name_s)
                
                #dest -----------------------
                if dest_s > -1:
                    name_e = dest_s
                    dest = (head[dest_s:dest_s+1],dest_s,dest_s+1)
                    inst_e = dest_s
                    base_e = dest_s
                else:
                    dest = ("",-1,-1)
                    name_e = inst_e = base_e = len(head)
                
                #inst --------------------------
                if inst_s > -1:
                    name_e = inst_s
                    base_e = inst_s
                    inst = (head[inst_s:inst_e],inst_s,inst_e)
                else:
                    inst = ("",-1,-1)
                
                #base ---------------------------------		
                if base_s > -1:
                    name_e = base_s
                    base = (head[base_s:base_e],base_s,base_e)
                else:
                    base = ("",-1,-1)
                
                name = (head[name_s:name_e],name_s,name_e)
                        
                return (spec,name,base,inst,dest)
                    
            return None	
        #@-node:ekr.20060513122450.227:Match
        #@+node:ekr.20060513122450.228:OnMatch
        def OnMatch(self,mo,node):
            global LOCATE_CHILD
            
            Parser.CURRENT_RULE = "class"
            
            spec,name,base,inst,dest = mo
            
            #determine where to write
            if len(Parser.CLASS_LIST) == 0:#redirect only for the root class
                if dest[0] != "":#directed toward source
                    cw = Parser.CLASS_WRITER = Parser.Define
                else:
                    cw = Parser.CLASS_WRITER = Parser.Declare
            else:
                cw = Parser.CLASS_WRITER
            
            if Parser.CLASS_WRITER == Parser.Define and Parser.Declare != Parser.Define:
                push = True
            else:
                push = False
            
            cdec = ""
            
            if spec[0] != "":
                cdec += spec[0]+" "
            
            if name[0] == "":
                ToolBar.SetError("No name in class definition :"+GetNodePath(Parser.CURRENT_NODE),Parser.CURRENT_NODE)
                return False
            
            cdec += "class "+name[0]
            
            if base[0] != "":
                cdec += base[0]
                
            if push == True:
                Parser.PushTab()
                
            Parser.CLASS_LIST.append(name[0])
            Parser.CURRENT_LOCATION = "head"
            Parser.SetRealBodyDestination(cw)
            if CLASS_HDR != "":
                cw(Parser.TAB_STRING+CLASS_HDR)
            cw(Parser.TAB_STRING+cdec+FUNC_OPN)
            Parser.Tab()
            if Parser.WriteOthers(node,cw) == False:
                return False
            Parser.UnTab()
            Parser.CURRENT_LOCATION = "tail"
            cw(Parser.TAB_STRING+"}"+inst[0][1:]+";\n")
            if CLASS_FTR != "":
                cw(Parser.TAB_STRING+CLASS_FTR)	
            Parser.CLASS_LIST.pop()
            
            if push == True:
                Parser.PopTab()
            
            if len(Parser.CLASS_LIST) == 0:
                Parser.CLASS_WRITER = None		
            
            return True
        #@-node:ekr.20060513122450.228:OnMatch
        #@-others
    #@nonl
    #@-node:ekr.20060513122450.226:CLASSRULE
    #@+node:ekr.20060513122450.229:DEFAULTRULE
    class DEFAULTRULE:
        #@    @+others
        #@+node:ekr.20060513122450.230:__init__
        def __init__(self):	
            self.Matcher = re.compile("(?P<HEAD>[^;]*)(?P<DEST>;$)*")
            
        #@nonl
        #@-node:ekr.20060513122450.230:__init__
        #@+node:ekr.20060513122450.231:Match
        def Match(self,head):
            if head.endswith(";"):
                return True
            return False
        #@-node:ekr.20060513122450.231:Match
        #@+node:ekr.20060513122450.232:OnMatch
        def OnMatch(self,mo,node):
            if Parser.CLASS_WRITER != None:
                w = Parser.CLASS_WRITER
            else:
                if mo == True:
                    w = Parser.Define			
                else:
                    w = Parser.Declare
                                
            if mo == True:
                head = node.headString()[:-1]
            else:
                head = node.headString()
            
            Parser.SetRealBodyDestination(w)
            Parser.CURRENT_LOCATION = "head"
            w(Parser.TAB_STRING+"//"+head+"\n")
            Parser.Tab()
            
            if Parser.WriteOthers(node,w) == False:
                return False
            
            Parser.UnTab()	
            Parser.CURRENT_LOCATION = "tail"	
            w("\n")
            return True
        #@-node:ekr.20060513122450.232:OnMatch
        #@-others
    #@nonl
    #@-node:ekr.20060513122450.229:DEFAULTRULE
    #@+node:ekr.20060513122450.233:FUNCCOMMENTRULE
    class FUNCCOMMENTRULE:
        #@    @+others
        #@+node:ekr.20060513122450.234:__init__
        def __init__(self):	
            self.Matcher = re.compile("^//(?P<HEAD>.*)")
            
        #@nonl
        #@-node:ekr.20060513122450.234:__init__
        #@+node:ekr.20060513122450.235:Match
        def Match(self,head):
            return self.Matcher.search(head)
        #@-node:ekr.20060513122450.235:Match
        #@+node:ekr.20060513122450.236:OnMatch
        def OnMatch(self,mo,node):	
            w = Parser.FUNC_WRITER
            groups = mo.groupdict()
            
            head = groups["HEAD"]
            if head == None:
                head = ""
                
            Parser.CURRENT_LOCATION = "head"
            w(Parser.TAB_STRING+head+"\n")
            Parser.Tab()
            
            if Parser.WriteOthers(node,w) == False:
                return False
            
            Parser.CURRENT_LOCATION = "tail"
            Parser.UnTab()
            w(Parser.TAB_STRING+"*/\n")
        
            return True
        #@-node:ekr.20060513122450.236:OnMatch
        #@-others
    #@nonl
    #@-node:ekr.20060513122450.233:FUNCCOMMENTRULE
    #@+node:ekr.20060513122450.237:FUNCDEFAULTRULE
    class FUNCDEFAULTRULE:
        #@    @+others
        #@+node:ekr.20060513122450.238:__init__
        def __init__(self):	
            self.Matcher = re.compile("(?P<HEAD>.*)")
            
        #@nonl
        #@-node:ekr.20060513122450.238:__init__
        #@+node:ekr.20060513122450.239:Match
        def Match(self,head):
            return self.Matcher.search(head)
        #@-node:ekr.20060513122450.239:Match
        #@+node:ekr.20060513122450.240:OnMatch
        def OnMatch(self,mo,node):
            
            w = Parser.FUNC_WRITER
            groups = mo.groupdict()
            
            head = groups["HEAD"]
            if head == None:
                head = ""
            
            Parser.CURRENT_LOCATION = "head"
            w(Parser.TAB_STRING+"//"+head+"\n")
            Parser.Tab()
            
            if Parser.WriteOthers(node,w) == False:
                return False
            
            Parser.UnTab()	
            Parser.CURRENT_LOCATION = "tail"	
            w("\n")
            return True
        #@-node:ekr.20060513122450.240:OnMatch
        #@-others
    #@nonl
    #@-node:ekr.20060513122450.237:FUNCDEFAULTRULE
    #@-node:ekr.20060513122450.213:Rules
    #@+node:ekr.20060513122450.241:__init__
    def __init__(self):
        global Parser
        Parser = self
        self.InitData()
    #@-node:ekr.20060513122450.241:__init__
    #@+node:ekr.20060513122450.242:Declare
    def Declare(self,text):
        if self.CURRENT_LOCATION == "body":
            self.CURRENT_BODY_LINE += 1		
        else:
            self.CURRENT_BODY_LINE = 0
    
        if self.DECLARE_IN_HEADER == False:
            self.CURRENT_SRC_LINE += 1								
        else:
            self.CURRENT_HDR_LINE += 1
            
        for d in self.DEC_PROC_LIST:
            d(text)
    #@-node:ekr.20060513122450.242:Declare
    #@+node:ekr.20060513122450.243:Define
    def Define(self,text):
        if self.CURRENT_LOCATION == "body":
            self.CURRENT_BODY_LINE += 1		
        else:
            self.CURRENT_BODY_LINE = 0
    
        if self.DEFINE_IN_SOURCE == False:
            self.CURRENT_HDR_LINE += 1
        else:
            self.CURRENT_SRC_LINE += 1
            
        for d in self.DEF_PROC_LIST:
            d(text)
    #@-node:ekr.20060513122450.243:Define
    #@+node:ekr.20060513122450.244:Docum
    def Docum(self,text):
        if self.CURRENT_LOCATION == "body":
            self.CURRENT_BODY_LINE += 1		
        else:
            self.CURRENT_BODY_LINE = 0
    
        self.CURRENT_DOC_LINE += 1
            
        for d in self.DOC_PROC_LIST:
            d(text)
    #@nonl
    #@-node:ekr.20060513122450.244:Docum
    #@+node:ekr.20060513122450.245:PushBodyLine
    def PushBodyLine(self):
        self.BODY_LINE_STACK.insert(0,self.CURRENT_BODY_LINE)
    #@-node:ekr.20060513122450.245:PushBodyLine
    #@+node:ekr.20060513122450.246:PopBodyLine
    def PopBodyLine(self):
        self.CURRENT_BODY_LINE = self.BODY_LINE_STACK.pop(0)
        
        
    #@-node:ekr.20060513122450.246:PopBodyLine
    #@+node:ekr.20060513122450.247:SetRealBodyDestination
    def SetRealBodyDestination(self,func=None):
        if func == None:
            self.CURRENT_BODY_DEST = "VOID"
            return self.CURRENT_BODY_DEST
        
        if func == Parser.Docum:
            self.CURRENT_BODY_DEST = "DOCUM"
            
        if self.Define == self.Declare:#only one probable file
            if EXT == "h":#this is a header so..
                self.CURRENT_BODY_DEST = "HEADER"
            else:#this is not a header so..
                self.CURRENT_BODY_DEST = "SOURCE"
            
        else:#two probable file, must use func pointer
            if func == self.Declare:
                self.CURRENT_BODY_DEST = "HEADER"
            if func == self.Define:
                self.CURRENT_BODY_DEST = "SOURCE"
                
        return self.CURRENT_BODY_DEST
    
    #@-node:ekr.20060513122450.247:SetRealBodyDestination
    #@+node:ekr.20060513122450.248:Tabing
    #@+node:ekr.20060513122450.249:Tab
    def Tab(self):
        self.TAB_STRING += "\t"
    #@nonl
    #@-node:ekr.20060513122450.249:Tab
    #@+node:ekr.20060513122450.250:UnTab
    def UnTab(self):
        if len(self.TAB_STRING) > 0:
            self.TAB_STRING = self.TAB_STRING[:-1] 
    #@-node:ekr.20060513122450.250:UnTab
    #@+node:ekr.20060513122450.251:PushTab
    def PushTab(self):
        self.TAB_LIST.append(self.TAB_STRING)
        self.TAB_STRING = ""
    #@nonl
    #@-node:ekr.20060513122450.251:PushTab
    #@+node:ekr.20060513122450.252:PopTab
    def PopTab(self):
        self.TAB_STRING = self.TAB_LIST.pop(-1)
    #@nonl
    #@-node:ekr.20060513122450.252:PopTab
    #@+node:ekr.20060513122450.253:TabWrite
    def TabWrite(self,text,outfunc):
        lines = text.splitlines(True)
        for l in lines:
            outfunc(self.TAB_STRING+l)
    #@-node:ekr.20060513122450.253:TabWrite
    #@-node:ekr.20060513122450.248:Tabing
    #@+node:ekr.20060513122450.254:WriteOthers
    def WriteOthers(self,node,w):
        b = node.bodyString()
        o = b.find("@others")
        if o != -1:
            #--------------------
            lb = b[:o]
            pnl = lb.rfind("\n")
            if pnl > -1:
                lb = lb[:pnl]
            
            tb = b[o+7:]
            pnl = tb.find("\n")		
            if pnl > -1:
                tb = tb[pnl+1:]		
            
            self.CURRENT_LOCATION = "body"
            
            if lb != "":
                self.TabWrite(lb+"\n",w)
            self.PushBodyLine()
            if self.ParseNode(node) == False:
                return False
            self.PopBodyLine()
            self.CURRENT_LOCATION = "body"	
            self.TabWrite(b[o+7:]+"\n",w)
        else:
            self.CURRENT_LOCATION = "body"	
            self.TabWrite(b+"\n",w)	
            if self.ParseNode(node) == False:
                return False
        
        return True
    #@-node:ekr.20060513122450.254:WriteOthers
    #@+node:ekr.20060513122450.255:CppParse
    def CppParse(self,node,ext):
        self.LoadCppRules()	
            
        #----------------------------------------------
        if ext in self.NO_HEADER_EXT:
            self.DECLARE_IN_HDR = False
        else:
            self.DECLARE_IN_HDR = True
        
        if ext in self.NO_SOURCE_EXT:
            self.DEFINE_IN_SRC = False
        else:
            self.DEFINE_IN_SRC = True
        
        #-----------------------------------------------------
        self.CURRENT_VNODE = node.v
        self.CURRENT_NODE = node	
        
        #-----------------------------------------------------
        if self.NOW_PARSING == True:
            Error("xcc: ","AutoParse was already parsing!")
            return False
        else:
            self.NOW_PARSING = True	
        
        #------------------------------------------------------
        if self.OnStart != None:
            if self.OnStart() == False:
                return False
        time.clock()
        start = time.clock()
        
        if self.DEFINE_IN_SRC == True and self.DECLARE_IN_HDR == True:
            if OPTS.get("Auto include header") == "True":
                self.Define("#include \""+NAME+".h\"\n")
                
        #------------------------------------------------------		
        res = self.ParseNode(node,reset=True)	
        #------------------------------------------------------	
        self.PARSE_TIME = time.clock()-start
        if self.OnEnd != None:
            self.OnEnd()	
        
        return res
    #@-node:ekr.20060513122450.255:CppParse
    #@+node:ekr.20060513122450.256:OnParseNode
    def OnParseNode(self,node,back=False):
        self.CURRENT_VNODE = node.v
        self.CURRENT_NODE = node.copy()	
        
        for opn in self.OPN_PROC_LIST:
            opn(node,back)
    #@-node:ekr.20060513122450.256:OnParseNode
    #@+node:ekr.20060513122450.257:ParseNode
    def ParseNode(self,node,reset=False):
        
        if self.DO_PARSE == False:
            return False
            
        for cn in node.children_iter():
            self.OnParseNode(cn)		
            ch = cn.headString()		
            
            self.CURRENT_RULE = None
            for r in self.RULES:
                result = r.Match(ch)
                if result != None:
                    self.CURRENT_MATCH_OBJECT = result
                    if r.OnMatch(result,cn) == False or self.DO_PARSE == False:
                        return False
                    break
                
                    
        if node != SELECTED_NODE:
            self.OnParseNode(node,True)
        
        return True	
    
    #@-node:ekr.20060513122450.257:ParseNode
    #@+node:ekr.20060513122450.258:InitData
    def InitData(self):
        self.DO_PARSE = True	
        self.NOW_PARSING = False
        
        self.RULES = []	
        self.OnStart = None
        self.OnEnd = None	
        
        
        self.DEC_PROC_LIST = []
        self.DEF_PROC_LIST = []
        self.DOC_PROC_LIST = []
        self.OPN_PROC_LIST = []
        
        self.BODY_LINE_STACK = []
        
        self.CURRENT_SRC_LINE = 0
        self.CURRENT_HDR_LINE = 0
        
        self.CURRENT_BODY_LINE = 0
        self.CURRENT_BODY_DEST = None
        self.CURRENT_VNODE = None
        self.CURRENT_NODE = None
        self.CURRENT_LOCATION = "head"
        
        self.CURRENT_RULE = ""
        self.CURRENT_MO = None
        
        self.DECLARE_IN_HEADER = True
        self.DEFINE_IN_SOURCE = True	
        
        self.CLASS_LIST = []
        self.CLASS_WRITER = None	
        
        
        self.NO_HEADER_EXT = ["cpp","c"]
        self.NO_SOURCE_EXT = ["h"]
        
        self.TAB_STRING = ""
        self.TAB_LIST = []
        
        self.PARSE_TIME = 0.0
    #@nonl
    #@-node:ekr.20060513122450.258:InitData
    #@-others
#@-node:ekr.20060513122450.212:CPPPARSER
#@+node:ekr.20060513122450.259:WRITER
class WriterClass(CPPPARSER):
    #@    @+others
    #@+node:ekr.20060513122450.260:__init__
    def __init__(self,controller):
        
        self.controller = controller
        self.Result = False
        
        CPPPARSER.__init__(self)
        self.OnStart = self.OnWriteStart
        self.OnEnd = self.OnWriteEnd
        
        self.Result = self.CppParse(controller.SELECTED_NODE,controller.EXT)
    #@-node:ekr.20060513122450.260:__init__
    #@+node:ekr.20060513122450.261:OnWriteStart
    def OnWriteStart(self):
        global SRC_EXT
            
        self.HDR_FILE = None
        self.SRC_FILE = None
        
        if REL_PATH != "":
            name = REL_PATH+"\\"+NAME
        else:
            name = NAME
        
        #create a header and verify syntaxe	
        if EXT == "h":
            sAddText("\" writing "+name+".h...\n")
            self.HDR_FILE = file(name+".h","w+")
            
        #create exe using .h and .cpp files
        if EXT == "exe":
            sAddText("\" writing "+name+".h and "+name+".cpp...\n")
            self.HDR_FILE = file(name+".h","w+")
            self.SRC_FILE = file(name+".cpp","w+")
            
        #create exe using .cpp or .c file
        if EXT == "cpp" or EXT == "c":
            sAddText("\" writing "+name+"."+EXT+"...\n")
            self.SRC_FILE = file(name+"."+EXT,"w+")
                    
        #create a static .lib or dynamic .dll using .h and .cpp file	
        if EXT == "dll":
            sAddText("\" writing "+name+".h and "+name+".cpp...\n")
            self.HDR_FILE = file(name+".h","w+")
            self.SRC_FILE = file(name+".cpp","w+")
                    
        if self.HDR_FILE == None and self.SRC_FILE == None:
            Error("xcc: ","Unable to open output file(s)!")
            return False	
        
        #------------------------------------------
        if self.DECLARE_IN_HDR == True:
            self.DEC_PROC_LIST.append(self.HDR_FILE.write)
        else:
            self.DEC_PROC_LIST.append(self.SRC_FILE.write)
            
        if self.DEFINE_IN_SRC == True:
            self.DEF_PROC_LIST.append(self.SRC_FILE.write)
        else:
            self.DEF_PROC_LIST.append(self.HDR_FILE.write)
            
        
        return True
    #@-node:ekr.20060513122450.261:OnWriteStart
    #@+node:ekr.20060513122450.262:OnWriteEnd
    def OnWriteEnd(self):
        
        if self.HDR_FILE != None:
            self.HDR_FILE.write("\n")
            self.HDR_FILE.close()
            self.HDR_FILE = None
            
        if self.SRC_FILE != None:
            self.SRC_FILE.write("\n")
            self.SRC_FILE.close()
            self.SRC_FILE = None
    
    
    #@-node:ekr.20060513122450.262:OnWriteEnd
    #@-others
#@-node:ekr.20060513122450.259:WRITER
#@+node:ekr.20060513122450.263:BREAKFINDER
class BREAKFINDER(CPPPARSER):
    #@    @+others
    #@+node:ekr.20060513122450.264:__init__
    def __init__(self):
        self.Result = False
        
        CPPPARSER.__init__(self)
        self.OnStart = self.OnFindStart
        self.OnEnd = self.OnFindEnd
        
        self.Result = self.CppParse(SELECTED_NODE,EXT)
    #@-node:ekr.20060513122450.264:__init__
    #@+node:ekr.20060513122450.265:OnFindStart
    def OnFindStart(self):
        # loading event funcs
        if self.DECLARE_IN_HDR == True:
            self.DEC_PROC_LIST.append(self.BreakDec)		
        else:
            self.DEC_PROC_LIST.append(self.BreakDef)
            
        if self.DEFINE_IN_SRC == True:
            self.DEF_PROC_LIST.append(self.BreakDef)
        else:
            self.DEF_PROC_LIST.append(self.BreakDec)		
            
        self.OPN_PROC_LIST.append(self.BreakOPN)
        
        sSet("Breakpoints",{})
        self.GLOBAL_BREAKS = sGet("Breakpoints")
        
        self.CURRENT_BREAKS = None
    
    #@-node:ekr.20060513122450.265:OnFindStart
    #@+node:ekr.20060513122450.266:OnFindEnd
    def OnFindEnd(self):
        sSet("Breakpoints",self.GLOBAL_BREAKS)
    
    #@-node:ekr.20060513122450.266:OnFindEnd
    #@+node:ekr.20060513122450.267:BreakDec
    def BreakDec(self,text):
        
        cbl = self.CURRENT_BODY_LINE
        cb = self.CURRENT_BREAKS	
        
        #cGetDict(self.CURRENT_NODE)["BodyDestination"] = "HEADER"
        if cb != None and str(cbl) in cb:
            self.GLOBAL_BREAKS["h:"+str(self.CURRENT_HDR_LINE)] = cb[str(cbl)]
    #@-node:ekr.20060513122450.267:BreakDec
    #@+node:ekr.20060513122450.268:BreakDef
    def BreakDef(self,text):
        
        cbl = self.CURRENT_BODY_LINE
        cb = self.CURRENT_BREAKS
        
        #cGetDict(self.CURRENT_NODE)["BodyDestination"] = "Source"
        if cb != None and str(cbl) in cb:
            self.GLOBAL_BREAKS[SRC_EXT+":"+str(self.CURRENT_SRC_LINE)] = cb[str(cbl)]
    #@-node:ekr.20060513122450.268:BreakDef
    #@+node:ekr.20060513122450.269:BreakOPN
    def BreakOPN(self,node,back=False):
        
        txcd = cGetDict(node)
        if txcd != None:
            if "BreakPoints" in txcd:
                self.CURRENT_BREAKS = txcd["BreakPoints"]
            else:
                self.CURRENT_BREAKS = None
        else:
            self.CURRENT_BREAKS = None
    #@-node:ekr.20060513122450.269:BreakOPN
    #@-others
#@-node:ekr.20060513122450.263:BREAKFINDER
#@+node:ekr.20060513122450.270:SeekErrorClass
class SeekErrorClass(CPPPARSER):
    #@    @+others
    #@+node:ekr.20060513122450.271:__init__
    def __init__(self,controller,line,ext,col="0",color="red"):
        
        self.controller = controller
        CPPPARSER.__init__(self)		
            
        self.SEEK_LINE = line
        self.SEEK_COL = col
        self.SEEK_EXT = ext
        self.FOUND_NODE = None
        self.FOUND_INDEX = "1."+col
        self.OnStart = self.OnStartSeek
        
        if self.CppParse(controller.SELECTED_NODE,controller.EXT) == False and self.FOUND_NODE:
            controller.GoToNode(self.FOUND_NODE,self.FOUND_INDEX,tagcolor=color)
        else:
            Error("xcc: ","Unable to find line: "+str(line))
    #@nonl
    #@-node:ekr.20060513122450.271:__init__
    #@+node:ekr.20060513122450.272:OnStartSeek
    def OnStartSeek(self):
        if self.DECLARE_IN_HEADER == True:
            self.DEC_PROC_LIST.append(self.SeekDec)
        else:
            self.DEC_PROC_LIST.append(self.SeekDef)
        
        
        if self.DEFINE_IN_SOURCE == True:
            self.DEF_PROC_LIST.append(self.SeekDef)
        else:
            self.DEF_PROC_LIST.append(self.SeekDec)
    #@-node:ekr.20060513122450.272:OnStartSeek
    #@+node:ekr.20060513122450.273:SeekDec
    def SeekDec(self,text):
        if self.DO_PARSE == True:
            index = None
            cbl = self.CURRENT_BODY_LINE
            
            if self.CURRENT_HDR_LINE == self.SEEK_LINE and self.SEEK_EXT == "h":			
                
                if self.CURRENT_LOCATION == "head":
                    index = "1.0"
                if self.CURRENT_LOCATION == "body":
                    index = str(cbl)+"."+self.SEEK_COL
                if self.CURRENT_LOCATION == "tail":
                    index = "1000.0"
                    
                
                self.DO_PARSE = False
                self.FOUND_NODE = self.CURRENT_NODE.copy()
                self.FOUND_INDEX = index
    #@nonl
    #@-node:ekr.20060513122450.273:SeekDec
    #@+node:ekr.20060513122450.274:SeekDef
    def SeekDef(self,text):
        if self.DO_PARSE == True:
            index = None
            cbl = self.CURRENT_BODY_LINE
        
            if self.CURRENT_SRC_LINE == self.SEEK_LINE and self.SEEK_EXT == "cpp":
                
                if self.CURRENT_LOCATION == "head":
                    index = "1."+self.SEEK_COL
                if self.CURRENT_LOCATION == "body":
                    index = str(cbl)+"."+self.SEEK_COL
                if self.CURRENT_LOCATION == "tail":
                    index = "1000."+self.SEEK_COL
                
                self.DO_PARSE = False
                self.FOUND_NODE = self.CURRENT_NODE.copy()
                self.FOUND_INDEX = index
    #@-node:ekr.20060513122450.274:SeekDef
    #@-others
#@nonl
#@-node:ekr.20060513122450.270:SeekErrorClass
#@+node:ekr.20060513122450.275:LOCATOR
class LOCATOR(CPPPARSER):
    #@    @+others
    #@+node:ekr.20060513122450.276:__init__
    def __init__(self,node,line):
        
        CPPPARSER.__init__(self)		
            
        self.LOCATE_NODE = node
        self.LOCATE_BODY_LINE = int(line)
        
        self.FOUND_FILE_LINE = None
        self.FOUND_FILE_EXT = None
        
        self.OnStart = self.OnStartLocate
        
        if self.CppParse(SELECTED_NODE,EXT) == False and self.FOUND_FILE_LINE != None:
            pass
        else:
            #Error("xcc: ","Unable to locate line "+str(line)+" in "+str(node))
            pass
        
        
    #@nonl
    #@-node:ekr.20060513122450.276:__init__
    #@+node:ekr.20060513122450.277:OnStartLocate
    def OnStartLocate(self):
        if self.DECLARE_IN_HEADER == True:
            self.DEC_PROC_LIST.append(self.LocateDec)
        else:
            self.DEC_PROC_LIST.append(self.LocateDef)
        
        
        if self.DEFINE_IN_SOURCE == True:
            self.DEF_PROC_LIST.append(self.LocateDef)
        else:
            self.DEF_PROC_LIST.append(self.LocateDec)
            
        self.NODE_REACHED = False
    #@-node:ekr.20060513122450.277:OnStartLocate
    #@+node:ekr.20060513122450.278:LocateDec
    def LocateDec(self,text):
        if self.DO_PARSE == True:
            if self.CURRENT_NODE == self.LOCATE_NODE:
                if self.CURRENT_RULE == "func" and self.CURRENT_MATCH_OBJECT[4][0]!= "":
                    self.FOUND_FILE_LINE = -1
                    self.FOUND_FILE_EXT = "h"
                    self.DO_PARSE = False
                    return
                if self.CURRENT_BODY_LINE == self.LOCATE_BODY_LINE:
                    self.FOUND_FILE_LINE = self.CURRENT_HDR_LINE
                    self.FOUND_FILE_EXT = "h"
                    self.DO_PARSE = False
    #@nonl
    #@-node:ekr.20060513122450.278:LocateDec
    #@+node:ekr.20060513122450.279:LocateDef
    def LocateDef(self,text):
        if self.DO_PARSE == True:
            if self.CURRENT_NODE == self.LOCATE_NODE:
                if self.CURRENT_BODY_LINE == self.LOCATE_BODY_LINE:
                    self.FOUND_FILE_LINE = self.CURRENT_SRC_LINE
                    self.FOUND_FILE_EXT = SRC_EXT
                    self.DO_PARSE = False
    #@nonl
    #@-node:ekr.20060513122450.279:LocateDef
    #@-others
#@-node:ekr.20060513122450.275:LOCATOR
#@-node:ekr.20060513122450.211:class Parsing
#@-node:ekr.20060513122450.42:Classes
#@-others

#@-node:ekr.20060513122450:@thin xcc_nodes.py
#@-leo
