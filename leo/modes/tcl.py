# Leo colorizer control file for tcl mode.
# This file is in the public domain.

# Properties for tcl mode.
properties = {
	"indentCloseBrackets": "}",
	"indentOpenBrackets": "{",
	"lineComment": "#",
	"lineUpClosingBracket": "true",
}

# Attributes dict for tcl_main ruleset.
tcl_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for tcl mode.
attributesDictDict = {
	"tcl_main": tcl_main_attributes_dict,
}

# Keywords dict for tcl_main ruleset.
tcl_main_keywords_dict = {
	"$argc": "keyword3",
	"$argv": "keyword3",
	"$argv0": "keyword3",
	"$tk_library": "keyword3",
	"$tk_strictMotif": "keyword3",
	"$tk_version": "keyword3",
	"Activate": "keyword3",
	"Alt": "keyword3",
	"Any": "keyword3",
	"B1": "keyword3",
	"B2": "keyword3",
	"B3": "keyword3",
	"Button": "keyword3",
	"Button1": "keyword3",
	"Button2": "keyword3",
	"Button3": "keyword3",
	"ButtonPress": "keyword3",
	"ButtonRelease": "keyword3",
	"Circulate": "keyword3",
	"Colormap": "keyword3",
	"Configure": "keyword3",
	"Control": "keyword3",
	"Deactivate": "keyword3",
	"Destroy": "keyword3",
	"Double": "keyword3",
	"Enter": "keyword3",
	"Escape": "keyword3",
	"Expose": "keyword3",
	"FocusIn": "keyword3",
	"FocusOut": "keyword3",
	"Gravity": "keyword3",
	"Key": "keyword3",
	"KeyPress": "keyword3",
	"KeyRelease": "keyword3",
	"Leave": "keyword3",
	"Lock": "keyword3",
	"MenuSelect": "keyword3",
	"Meta": "keyword3",
	"Motion": "keyword3",
	"Property": "keyword3",
	"Reparent": "keyword3",
	"Shift": "keyword3",
	"Triple": "keyword3",
	"Unmap": "keyword3",
	"Visibility": "keyword3",
	"\\": "keyword3",
	"\\a": "keyword3",
	"\\b": "keyword3",
	"\\f": "keyword3",
	"\\n": "keyword3",
	"\\r": "keyword3",
	"\\t": "keyword3",
	"\\v": "keyword3",
	"\\x": "keyword3",
	"abortretryignore": "keyword3",
	"abs": "keyword1",
	"accelerator": "keyword3",
	"acos": "keyword1",
	"active": "keyword3",
	"activebackground": "keyword3",
	"activeforeground": "keyword3",
	"add": "keyword3",
	"after": "keyword1",
	"all": "keyword3",
	"anchor": "keyword3",
	"anymore": "keyword3",
	"append": "keyword1",
	"arc": "keyword3",
	"args": "keyword3",
	"array": "keyword1",
	"asin": "keyword1",
	"aspect": "keyword3",
	"atan": "keyword1",
	"atan2": "keyword1",
	"atime": "keyword3",
	"auto_mkindex": "keyword1",
	"background": "keyword3",
	"bd": "keyword3",
	"before": "keyword3",
	"bg": "keyword3",
	"bind": "keyword2",
	"bitmap": "keyword3",
	"body": "keyword3",
	"borderwidth": "keyword3",
	"bottom": "keyword3",
	"break": "keyword1",
	"button": "keyword2",
	"canvas": "keyword2",
	"cascade": "keyword3",
	"catch": "keyword1",
	"cd": "keyword1",
	"ceil": "keyword1",
	"center": "keyword3",
	"cget": "keyword3",
	"checkbutton": "keyword2",
	"children": "keyword3",
	"class": "keyword3",
	"clear": "keyword3",
	"client": "keyword3",
	"close": "keyword1",
	"cmdcount": "keyword3",
	"code": "keyword3",
	"colormodel": "keyword3",
	"command": "keyword3",
	"commands": "keyword3",
	"compare": "keyword3",
	"concat": "keyword1",
	"configure": "keyword3",
	"console": "keyword1",
	"continue": "keyword1",
	"cos": "keyword1",
	"cosh": "keyword1",
	"create": "keyword3",
	"ctime": "keyword3",
	"current": "keyword3",
	"cursor": "keyword3",
	"default": "keyword3",
	"deiconify": "keyword3",
	"delete": "keyword3",
	"destroy": "keyword2",
	"dev": "keyword3",
	"dirname": "keyword3",
	"disabled": "keyword3",
	"donesearch": "keyword3",
	"double": "keyword1",
	"else": "keyword1",
	"elseif": "keyword1",
	"entry": "keyword2",
	"eof": "keyword1",
	"error": "keyword1",
	"errorcode": "keyword3",
	"errorinfo": "keyword3",
	"eval": "keyword1",
	"exact": "keyword3",
	"exec": "keyword1",
	"executable": "keyword3",
	"exists": "keyword3",
	"exit": "keyword1",
	"expand": "keyword3",
	"expr": "keyword1",
	"extension": "keyword3",
	"family": "keyword3",
	"fg": "keyword3",
	"file": "keyword1",
	"fill": "keyword3",
	"first": "keyword3",
	"flash": "keyword3",
	"flat": "keyword3",
	"floor": "keyword1",
	"flush": "keyword1",
	"fmod": "keyword1",
	"focus": "keyword2",
	"focusmodel": "keyword3",
	"font": "keyword3",
	"for": "keyword1",
	"force": "keyword3",
	"foreach": "keyword1",
	"foreground": "keyword3",
	"forget": "keyword3",
	"format": "keyword1",
	"frame": "keyword2",
	"from": "keyword3",
	"geometry": "keyword3",
	"get": "keyword3",
	"gets": "keyword1",
	"gid": "keyword3",
	"glob": "keyword1",
	"global": "keyword1",
	"globals": "keyword3",
	"grab": "keyword2",
	"groove": "keyword3",
	"group": "keyword3",
	"handle": "keyword3",
	"height": "keyword3",
	"history": "keyword1",
	"horizontal": "keyword3",
	"hypot": "keyword1",
	"icon": "keyword3",
	"iconbitmap": "keyword3",
	"iconify": "keyword3",
	"iconmask": "keyword3",
	"iconname": "keyword3",
	"iconposition": "keyword3",
	"iconwindow": "keyword3",
	"idletasks": "keyword3",
	"if": "keyword1",
	"image": "keyword2",
	"in": "keyword3",
	"incr": "keyword1",
	"index": "keyword3",
	"indices": "keyword3",
	"info": "keyword1",
	"ino": "keyword3",
	"insert": "keyword3",
	"int": "keyword1",
	"interps": "keyword3",
	"invoke": "keyword3",
	"ipadx": "keyword3",
	"ipady": "keyword3",
	"isdirectory": "keyword3",
	"isfile": "keyword3",
	"itemconfigure": "keyword3",
	"join": "keyword1",
	"justify": "keyword3",
	"keep": "keyword3",
	"label": "keyword2",
	"lappend": "keyword1",
	"last": "keyword3",
	"left": "keyword3",
	"length": "keyword3",
	"level": "keyword3",
	"library": "keyword3",
	"lindex": "keyword1",
	"line": "keyword3",
	"linsert": "keyword1",
	"list": "keyword1",
	"listbox": "keyword2",
	"llength": "keyword1",
	"locals": "keyword3",
	"log": "keyword1",
	"log10": "keyword1",
	"lower": "keyword2",
	"lrange": "keyword1",
	"lreplace": "keyword1",
	"lsearch": "keyword1",
	"lsort": "keyword1",
	"lstat": "keyword3",
	"mark": "keyword3",
	"match": "keyword3",
	"maxsize": "keyword3",
	"menu": "keyword2",
	"menubutton": "keyword2",
	"message": "keyword2",
	"minsize": "keyword3",
	"mode": "keyword3",
	"move": "keyword3",
	"mtime": "keyword3",
	"name": "keyword3",
	"names": "keyword3",
	"nextelement": "keyword3",
	"nextid": "keyword3",
	"nlink": "keyword3",
	"nocase": "keyword3",
	"nocomplain": "keyword3",
	"none": "keyword3",
	"nonewline": "keyword3",
	"normal": "keyword3",
	"offvalue": "keyword3",
	"ok": "keyword3",
	"okcancel": "keyword3",
	"onvalue": "keyword3",
	"open": "keyword1",
	"option": "keyword2",
	"orient": "keyword3",
	"outline": "keyword3",
	"oval": "keyword3",
	"overrideredirect": "keyword3",
	"oversrike": "keyword3",
	"own": "keyword3",
	"owned": "keyword3",
	"pack": "keyword2",
	"padx": "keyword3",
	"pady": "keyword3",
	"photo": "keyword3",
	"pid": "keyword1",
	"placer": "keyword2",
	"polygon": "keyword3",
	"positionfrom": "keyword3",
	"pow": "keyword1",
	"proc": "keyword1",
	"procs": "keyword3",
	"propagate": "keyword3",
	"protocol": "keyword3",
	"puts": "keyword1",
	"pwd": "keyword1",
	"question": "keyword3",
	"radiobutton": "keyword2",
	"raise": "keyword2",
	"raised": "keyword3",
	"range": "keyword3",
	"ranges": "keyword3",
	"read": "keyword1",
	"readable": "keyword3",
	"readlink": "keyword3",
	"rectangle": "keyword3",
	"redo": "keyword3",
	"regexp": "keyword1",
	"regsub": "keyword1",
	"release": "keyword3",
	"relief": "keyword3",
	"remove": "keyword3",
	"rename": "keyword1",
	"resizable": "keyword3",
	"retrycancel": "keyword3",
	"return": "keyword1",
	"ridge": "keyword3",
	"right": "keyword3",
	"rootname": "keyword3",
	"round": "keyword1",
	"scale": "keyword2",
	"scan": "keyword1",
	"screen": "keyword3",
	"script": "keyword3",
	"scrollbar": "keyword2",
	"seek": "keyword1",
	"selectbackground": "keyword3",
	"selectforeground": "keyword3",
	"selection": "keyword2",
	"send": "keyword2",
	"separator": "keyword3",
	"set": "keyword1",
	"setgrid": "keyword3",
	"show": "keyword3",
	"side": "keyword3",
	"sin": "keyword1",
	"sinh": "keyword1",
	"size": "keyword3",
	"sizefrom": "keyword3",
	"slant": "keyword3",
	"slaves": "keyword3",
	"solid": "keyword3",
	"source": "keyword1",
	"spacing1": "keyword3",
	"spacing2": "keyword3",
	"spacing3": "keyword3",
	"split": "keyword1",
	"sqrt": "keyword1",
	"startsearch": "keyword3",
	"stat": "keyword3",
	"state": "keyword3",
	"status": "keyword3",
	"stipple": "keyword3",
	"string": "keyword1",
	"substitute": "keyword3",
	"sunken": "keyword3",
	"switch": "keyword1",
	"tag": "keyword3",
	"tail": "keyword3",
	"takefocus": "keyword3",
	"tan": "keyword1",
	"tanh": "keyword1",
	"tclversion": "keyword3",
	"tearoff": "keyword3",
	"tell": "keyword1",
	"text": "keyword2",
	"textvariable": "keyword3",
	"time": "keyword1",
	"title": "keyword3",
	"tk": "keyword2",
	"tkerror": "keyword2",
	"tkwait": "keyword2",
	"to": "keyword3",
	"tolower": "keyword3",
	"top": "keyword3",
	"toplevel": "keyword2",
	"toupper": "keyword3",
	"trace": "keyword1",
	"transient": "keyword3",
	"trim": "keyword3",
	"trimleft": "keyword3",
	"trimright": "keyword3",
	"type": "keyword3",
	"uid": "keyword3",
	"underline": "keyword3",
	"unkown": "keyword1",
	"unset": "keyword1",
	"update": "keyword2",
	"uplevel": "keyword1",
	"upvar": "keyword1",
	"value": "keyword3",
	"variable": "keyword3",
	"vars": "keyword3",
	"vdelete": "keyword3",
	"vertical": "keyword3",
	"vinfo": "keyword3",
	"visibility": "keyword3",
	"warning": "keyword3",
	"weight": "keyword3",
	"while": "keyword1",
	"width": "keyword3",
	"window": "keyword3",
	"winfo": "keyword2",
	"withdraw": "keyword3",
	"wm": "keyword2",
	"writable": "keyword3",
	"xscrollcommand": "keyword3",
	"xview": "keyword3",
	"yesno": "keyword3",
	"yesnocancel": "keyword3",
	"yscrollcommand": "keyword3",
	"yview": "keyword3",
}

# Dictionary of keywords dictionaries for tcl mode.
keywordsDictDict = {
	"tcl_main": tcl_main_keywords_dict,
}

# Rules for tcl_main ruleset.

def tcl_rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def tcl_rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def tcl_rule2(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tcl_rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tcl_rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tcl_rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tcl_rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tcl_rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tcl_rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tcl_rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tcl_rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tcl_rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tcl_rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tcl_rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tcl_rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tcl_rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tcl_rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tcl_rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tcl_rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tcl_rule19(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for tcl_main ruleset.
rulesDict1 = {
	"!": [tcl_rule3,],
	"\"": [tcl_rule0,],
	"#": [tcl_rule1,],
	"$": [tcl_rule19,],
	"%": [tcl_rule12,],
	"&": [tcl_rule13,],
	"*": [tcl_rule9,],
	"+": [tcl_rule6,],
	"-": [tcl_rule7,],
	"/": [tcl_rule8,],
	"0": [tcl_rule19,],
	"1": [tcl_rule19,],
	"2": [tcl_rule19,],
	"3": [tcl_rule19,],
	"4": [tcl_rule19,],
	"5": [tcl_rule19,],
	"6": [tcl_rule19,],
	"7": [tcl_rule19,],
	"8": [tcl_rule19,],
	"9": [tcl_rule19,],
	"<": [tcl_rule5,tcl_rule11,],
	"=": [tcl_rule2,],
	">": [tcl_rule4,tcl_rule10,],
	"@": [tcl_rule19,],
	"A": [tcl_rule19,],
	"B": [tcl_rule19,],
	"C": [tcl_rule19,],
	"D": [tcl_rule19,],
	"E": [tcl_rule19,],
	"F": [tcl_rule19,],
	"G": [tcl_rule19,],
	"H": [tcl_rule19,],
	"I": [tcl_rule19,],
	"J": [tcl_rule19,],
	"K": [tcl_rule19,],
	"L": [tcl_rule19,],
	"M": [tcl_rule19,],
	"N": [tcl_rule19,],
	"O": [tcl_rule19,],
	"P": [tcl_rule19,],
	"Q": [tcl_rule19,],
	"R": [tcl_rule19,],
	"S": [tcl_rule19,],
	"T": [tcl_rule19,],
	"U": [tcl_rule19,],
	"V": [tcl_rule19,],
	"W": [tcl_rule19,],
	"X": [tcl_rule19,],
	"Y": [tcl_rule19,],
	"Z": [tcl_rule19,],
	"\\": [tcl_rule19,],
	"^": [tcl_rule15,],
	"_": [tcl_rule19,],
	"a": [tcl_rule19,],
	"b": [tcl_rule19,],
	"c": [tcl_rule19,],
	"d": [tcl_rule19,],
	"e": [tcl_rule19,],
	"f": [tcl_rule19,],
	"g": [tcl_rule19,],
	"h": [tcl_rule19,],
	"i": [tcl_rule19,],
	"j": [tcl_rule19,],
	"k": [tcl_rule19,],
	"l": [tcl_rule19,],
	"m": [tcl_rule19,],
	"n": [tcl_rule19,],
	"o": [tcl_rule19,],
	"p": [tcl_rule19,],
	"q": [tcl_rule19,],
	"r": [tcl_rule19,],
	"s": [tcl_rule19,],
	"t": [tcl_rule19,],
	"u": [tcl_rule19,],
	"v": [tcl_rule19,],
	"w": [tcl_rule19,],
	"x": [tcl_rule19,],
	"y": [tcl_rule19,],
	"z": [tcl_rule19,],
	"{": [tcl_rule18,],
	"|": [tcl_rule14,],
	"}": [tcl_rule17,],
	"~": [tcl_rule16,],
}

# x.rulesDictDict for tcl mode.
rulesDictDict = {
	"tcl_main": rulesDict1,
}

# Import dict for tcl mode.
importDict = {}

