# Leo colorizer control file for splus mode.
# This file is in the public domain.

# Properties for splus mode.
properties = {
	"doubleBracketIndent": "false",
	"indentCloseBrackets": "}",
	"indentNextLine": "\\s*(((if|while)\\s*\\(|else\\s*|else\\s+if\\s*\\(|for\\s*\\(.*\\))[^{;]*)",
	"indentOpenBrackets": "{",
	"lineComment": "#",
	"lineUpClosingBracket": "true",
	"wordBreakChars": "_,+-=<>/?^&*",
}

# Attributes dict for splus_main ruleset.
splus_main_attributes_dict = {
	"default": "null",
	"digit_re": "(0x[[:xdigit:]]+[lL]?|[[:digit:]]+(e[[:digit:]]*)?[lLdDfF]?)",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for splus mode.
attributesDictDict = {
	"splus_main": splus_main_attributes_dict,
}

# Keywords dict for splus_main ruleset.
splus_main_keywords_dict = {
	"F": "literal2",
	"T": "literal2",
	"break": "keyword1",
	"case": "keyword1",
	"continue": "keyword1",
	"default": "keyword1",
	"do": "keyword1",
	"else": "keyword1",
	"for": "keyword1",
	"function": "keyword1",
	"goto": "keyword1",
	"if": "keyword1",
	"return": "keyword1",
	"sizeof": "keyword1",
	"switch": "keyword1",
	"while": "keyword1",
}

# Dictionary of keywords dictionaries for splus mode.
keywordsDictDict = {
	"splus_main": splus_main_keywords_dict,
}

# Rules for splus_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="_",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=False, at_whitespace_end=True, at_word_start=False, exclude_match=True)

def rule23(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule24(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule4,],
	"\"": [rule0,],
	"#": [rule2,],
	"%": [rule15,],
	"&": [rule16,],
	"'": [rule1,],
	"(": [rule23,],
	"*": [rule12,],
	"+": [rule9,],
	"-": [rule10,],
	"/": [rule11,],
	"0": [rule24,],
	"1": [rule24,],
	"2": [rule24,],
	"3": [rule24,],
	"4": [rule24,],
	"5": [rule24,],
	"6": [rule24,],
	"7": [rule24,],
	"8": [rule24,],
	"9": [rule24,],
	":": [rule22,],
	"<": [rule7,rule8,rule14,],
	"=": [rule3,],
	">": [rule6,rule13,],
	"@": [rule24,],
	"A": [rule24,],
	"B": [rule24,],
	"C": [rule24,],
	"D": [rule24,],
	"E": [rule24,],
	"F": [rule24,],
	"G": [rule24,],
	"H": [rule24,],
	"I": [rule24,],
	"J": [rule24,],
	"K": [rule24,],
	"L": [rule24,],
	"M": [rule24,],
	"N": [rule24,],
	"O": [rule24,],
	"P": [rule24,],
	"Q": [rule24,],
	"R": [rule24,],
	"S": [rule24,],
	"T": [rule24,],
	"U": [rule24,],
	"V": [rule24,],
	"W": [rule24,],
	"X": [rule24,],
	"Y": [rule24,],
	"Z": [rule24,],
	"^": [rule18,],
	"_": [rule5,],
	"a": [rule24,],
	"b": [rule24,],
	"c": [rule24,],
	"d": [rule24,],
	"e": [rule24,],
	"f": [rule24,],
	"g": [rule24,],
	"h": [rule24,],
	"i": [rule24,],
	"j": [rule24,],
	"k": [rule24,],
	"l": [rule24,],
	"m": [rule24,],
	"n": [rule24,],
	"o": [rule24,],
	"p": [rule24,],
	"q": [rule24,],
	"r": [rule24,],
	"s": [rule24,],
	"t": [rule24,],
	"u": [rule24,],
	"v": [rule24,],
	"w": [rule24,],
	"x": [rule24,],
	"y": [rule24,],
	"z": [rule24,],
	"{": [rule21,],
	"|": [rule17,],
	"}": [rule20,],
	"~": [rule19,],
}

# x.rulesDictDict for splus mode.
rulesDictDict = {
	"splus_main": rulesDict1,
}

# Import dict for splus mode.
importDict = {}

