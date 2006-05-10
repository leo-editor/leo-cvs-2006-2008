# Leo colorizer control file for postscript mode.
# This file is in the public domain.

# Properties for postscript mode.
properties = {
	"lineComment": "%",
}

# Attributes dict for postscript_main ruleset.
postscript_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Attributes dict for postscript_literal ruleset.
postscript_literal_attributes_dict = {
	"default": "LITERAL1",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for postscript mode.
attributesDictDict = {
	"postscript_literal": postscript_literal_attributes_dict,
	"postscript_main": postscript_main_attributes_dict,
}

# Keywords dict for postscript_main ruleset.
postscript_main_keywords_dict = {
	"NULL": "literal2",
	"abs": "operator",
	"add": "operator",
	"atan": "operator",
	"ceiling": "operator",
	"clear": "keyword1",
	"cleartomark": "keyword1",
	"copy": "keyword1",
	"cos": "operator",
	"count": "keyword1",
	"countexecstack": "keyword1",
	"counttomark": "keyword1",
	"div": "operator",
	"dup": "keyword1",
	"exch": "keyword1",
	"exec": "keyword1",
	"execstack": "keyword1",
	"exit": "keyword1",
	"exp": "operator",
	"false": "literal2",
	"floor": "operator",
	"for": "keyword1",
	"idiv": "operator",
	"if": "keyword1",
	"ifelse": "keyword1",
	"ln": "operator",
	"log": "operator",
	"loop": "keyword1",
	"mark": "keyword1",
	"mod": "operator",
	"mul": "operator",
	"ned": "operator",
	"pop": "keyword1",
	"quit": "keyword1",
	"rand": "operator",
	"repeat": "keyword1",
	"roll": "keyword1",
	"round": "operator",
	"rrand": "operator",
	"sin": "operator",
	"sqrt": "operator",
	"srand": "operator",
	"start": "keyword1",
	"stop": "keyword1",
	"stopped": "keyword1",
	"sub": "operator",
	"true": "literal2",
	"truncate": "operator",
}

# Keywords dict for postscript_literal ruleset.
postscript_literal_keywords_dict = {}

# Dictionary of keywords dictionaries for postscript mode.
keywordsDictDict = {
	"postscript_literal": postscript_literal_keywords_dict,
	"postscript_main": postscript_main_keywords_dict,
}

# Rules for postscript_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="%!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="%?",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="%%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="(", end=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="<", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="label", pattern="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"%": [rule0,rule1,rule2,rule3,],
	"(": [rule4,],
	"/": [rule6,],
	"0": [rule11,],
	"1": [rule11,],
	"2": [rule11,],
	"3": [rule11,],
	"4": [rule11,],
	"5": [rule11,],
	"6": [rule11,],
	"7": [rule11,],
	"8": [rule11,],
	"9": [rule11,],
	"<": [rule5,],
	"@": [rule11,],
	"A": [rule11,],
	"B": [rule11,],
	"C": [rule11,],
	"D": [rule11,],
	"E": [rule11,],
	"F": [rule11,],
	"G": [rule11,],
	"H": [rule11,],
	"I": [rule11,],
	"J": [rule11,],
	"K": [rule11,],
	"L": [rule11,],
	"M": [rule11,],
	"N": [rule11,],
	"O": [rule11,],
	"P": [rule11,],
	"Q": [rule11,],
	"R": [rule11,],
	"S": [rule11,],
	"T": [rule11,],
	"U": [rule11,],
	"V": [rule11,],
	"W": [rule11,],
	"X": [rule11,],
	"Y": [rule11,],
	"Z": [rule11,],
	"[": [rule10,],
	"]": [rule9,],
	"_": [rule11,],
	"a": [rule11,],
	"b": [rule11,],
	"c": [rule11,],
	"d": [rule11,],
	"e": [rule11,],
	"f": [rule11,],
	"g": [rule11,],
	"h": [rule11,],
	"i": [rule11,],
	"j": [rule11,],
	"k": [rule11,],
	"l": [rule11,],
	"m": [rule11,],
	"n": [rule11,],
	"o": [rule11,],
	"p": [rule11,],
	"q": [rule11,],
	"r": [rule11,],
	"s": [rule11,],
	"t": [rule11,],
	"u": [rule11,],
	"v": [rule11,],
	"w": [rule11,],
	"x": [rule11,],
	"y": [rule11,],
	"z": [rule11,],
	"{": [rule8,],
	"}": [rule7,],
}

# Rules for postscript_literal ruleset.

def rule12(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="(", end=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules dict for literal ruleset.
rulesDict2 = {
	"(": [rule12,],
}

# x.rulesDictDict for postscript mode.
rulesDictDict = {
	"postscript_literal": rulesDict2,
	"postscript_main": rulesDict1,
}

# Import dict for postscript mode.
importDict = {}

