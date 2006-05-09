# Leo colorizer control file for jmk mode.
# This file is in the public domain.

# Properties for jmk mode.
properties = {
	"indentCloseBrackets": "}",
	"indentOpenBrackets": "{",
	"lineComment": "#",
	"lineUpClosingBracket": "true",
}

# Keywords dict for jmk_main ruleset.
jmk_main_keywords_dict = {
	"%": "keyword2",
	"<": "keyword2",
	"?": "keyword2",
	"@": "keyword2",
	"cat": "keyword1",
	"copy": "keyword1",
	"create": "keyword1",
	"delall": "keyword1",
	"delete": "keyword1",
	"dirs": "keyword1",
	"else": "keyword1",
	"end": "keyword1",
	"equal": "keyword1",
	"exec": "keyword1",
	"first": "keyword1",
	"forname": "keyword1",
	"function": "keyword1",
	"getprop": "keyword1",
	"glob": "keyword1",
	"if": "keyword1",
	"include": "keyword3",
	"join": "keyword1",
	"load": "keyword1",
	"mkdir": "keyword1",
	"mkdirs": "keyword1",
	"note": "keyword1",
	"patsubst": "keyword1",
	"rename": "keyword1",
	"rest": "keyword1",
	"subst": "keyword1",
	"then": "keyword1",
}

# Dictionary of keywords dictionaries for jmk mode.
keywordsDictDict = {
	"jmk_main": jmk_main_keywords_dict,
}

# Rules for jmk_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"\"": [rule1,],
	"#": [rule0,],
	"'": [rule2,],
	"(": [rule5,],
	")": [rule6,],
	"-": [rule7,],
	"0": [rule9,],
	"1": [rule9,],
	"2": [rule9,],
	"3": [rule9,],
	"4": [rule9,],
	"5": [rule9,],
	"6": [rule9,],
	"7": [rule9,],
	"8": [rule9,],
	"9": [rule9,],
	"=": [rule8,],
	"@": [rule9,],
	"A": [rule9,],
	"B": [rule9,],
	"C": [rule9,],
	"D": [rule9,],
	"E": [rule9,],
	"F": [rule9,],
	"G": [rule9,],
	"H": [rule9,],
	"I": [rule9,],
	"J": [rule9,],
	"K": [rule9,],
	"L": [rule9,],
	"M": [rule9,],
	"N": [rule9,],
	"O": [rule9,],
	"P": [rule9,],
	"Q": [rule9,],
	"R": [rule9,],
	"S": [rule9,],
	"T": [rule9,],
	"U": [rule9,],
	"V": [rule9,],
	"W": [rule9,],
	"X": [rule9,],
	"Y": [rule9,],
	"Z": [rule9,],
	"_": [rule9,],
	"a": [rule9,],
	"b": [rule9,],
	"c": [rule9,],
	"d": [rule9,],
	"e": [rule9,],
	"f": [rule9,],
	"g": [rule9,],
	"h": [rule9,],
	"i": [rule9,],
	"j": [rule9,],
	"k": [rule9,],
	"l": [rule9,],
	"m": [rule9,],
	"n": [rule9,],
	"o": [rule9,],
	"p": [rule9,],
	"q": [rule9,],
	"r": [rule9,],
	"s": [rule9,],
	"t": [rule9,],
	"u": [rule9,],
	"v": [rule9,],
	"w": [rule9,],
	"x": [rule9,],
	"y": [rule9,],
	"z": [rule9,],
	"{": [rule3,],
	"}": [rule4,],
}

# x.rulesDictDict for jmk mode.
rulesDictDict = {
	"jmk_main": rulesDict1,
}

# Import dict for jmk mode.
importDict = {}

