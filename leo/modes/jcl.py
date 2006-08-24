# Leo colorizer control file for jcl mode.
# This file is in the public domain.

# Properties for jcl mode.
properties = {
	"wordBreakChars": ",+-=<>/?^&*",
}

# Attributes dict for jcl_main ruleset.
jcl_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "false",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for jcl mode.
attributesDictDict = {
	"jcl_main": jcl_main_attributes_dict,
}

# Keywords dict for jcl_main ruleset.
jcl_main_keywords_dict = {
	"cntl": "keyword2",
	"command": "keyword2",
	"dd": "keyword2",
	"else": "keyword2",
	"encntl": "keyword2",
	"endif": "keyword2",
	"exec": "keyword2",
	"if": "keyword2",
	"include": "keyword2",
	"jclib": "keyword2",
	"job": "keyword2",
	"msg": "keyword2",
	"output": "keyword2",
	"pend": "keyword2",
	"proc": "keyword2",
	"set": "keyword2",
	"then": "keyword2",
	"xmit": "keyword2",
}

# Dictionary of keywords dictionaries for jcl mode.
keywordsDictDict = {
	"jcl_main": jcl_main_keywords_dict,
}

# Rules for jcl_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="//*",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"&": [rule5,],
	"'": [rule1,],
	",": [rule7,],
	"/": [rule0,],
	"0": [rule8,],
	"1": [rule8,],
	"2": [rule8,],
	"3": [rule8,],
	"4": [rule8,],
	"5": [rule8,],
	"6": [rule8,],
	"7": [rule8,],
	"8": [rule8,],
	"9": [rule8,],
	"<": [rule3,],
	"=": [rule2,],
	">": [rule4,],
	"@": [rule8,],
	"A": [rule8,],
	"B": [rule8,],
	"C": [rule8,],
	"D": [rule8,],
	"E": [rule8,],
	"F": [rule8,],
	"G": [rule8,],
	"H": [rule8,],
	"I": [rule8,],
	"J": [rule8,],
	"K": [rule8,],
	"L": [rule8,],
	"M": [rule8,],
	"N": [rule8,],
	"O": [rule8,],
	"P": [rule8,],
	"Q": [rule8,],
	"R": [rule8,],
	"S": [rule8,],
	"T": [rule8,],
	"U": [rule8,],
	"V": [rule8,],
	"W": [rule8,],
	"X": [rule8,],
	"Y": [rule8,],
	"Z": [rule8,],
	"a": [rule8,],
	"b": [rule8,],
	"c": [rule8,],
	"d": [rule8,],
	"e": [rule8,],
	"f": [rule8,],
	"g": [rule8,],
	"h": [rule8,],
	"i": [rule8,],
	"j": [rule8,],
	"k": [rule8,],
	"l": [rule8,],
	"m": [rule8,],
	"n": [rule8,],
	"o": [rule8,],
	"p": [rule8,],
	"q": [rule8,],
	"r": [rule8,],
	"s": [rule8,],
	"t": [rule8,],
	"u": [rule8,],
	"v": [rule8,],
	"w": [rule8,],
	"x": [rule8,],
	"y": [rule8,],
	"z": [rule8,],
	"|": [rule6,],
}

# x.rulesDictDict for jcl mode.
rulesDictDict = {
	"jcl_main": rulesDict1,
}

# Import dict for jcl mode.
importDict = {}

