# Leo colorizer control file for objective-c mode.
# This file is in the public domain.

# Properties for objective-c mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"doubleBracketIndent": "false",
	"indentCloseBrackets": "}",
	"indentNextLine": "\\s*(((if|while)\\s*\\(|else\\s*|else\\s+if\\s*\\(|for\\s*\\(.*\\))[^{;]*)",
	"indentOpenBrackets": "{",
	"lineComment": "//",
	"lineUpClosingBracket": "true",
	"wordBreakChars": ",+-=<>/?^&*",
}

# Attributes dict for objective_c_main ruleset.
objective_c_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for objective_c mode.
attributesDictDict = {
	"objective_c_main": objective_c_main_attributes_dict,
}

# Keywords dict for objective_c_main ruleset.
objective_c_main_keywords_dict = {
	"@class": "keyword1",
	"@defs": "keyword1",
	"@end": "keyword1",
	"@endcode": "keyword1",
	"@implementation": "keyword1",
	"@interface": "keyword1",
	"@private": "keyword1",
	"@protected": "keyword1",
	"@protocol": "keyword1",
	"@public": "keyword1",
	"@selector": "keyword1",
	"BOOL": "keyword3",
	"Class": "keyword3",
	"FALSE": "literal2",
	"IMP": "keyword3",
	"NIl": "literal2",
	"NO": "literal2",
	"NULL": "literal2",
	"SEL": "keyword3",
	"TRUE": "literal2",
	"YES": "literal2",
	"asm": "keyword1",
	"auto": "keyword1",
	"break": "keyword1",
	"bycopy": "keyword1",
	"byref": "keyword1",
	"case": "keyword1",
	"char": "keyword3",
	"const": "keyword3",
	"continue": "keyword1",
	"default": "keyword1",
	"do": "keyword1",
	"double": "keyword3",
	"else": "keyword1",
	"enum": "keyword3",
	"extern": "keyword1",
	"false": "literal2",
	"float": "keyword3",
	"for": "keyword1",
	"goto": "keyword1",
	"id": "keyword3",
	"if": "keyword1",
	"in": "keyword1",
	"inline": "keyword1",
	"inout": "keyword1",
	"int": "keyword3",
	"long": "keyword3",
	"nil": "literal2",
	"oneway": "keyword1",
	"out": "keyword1",
	"register": "keyword1",
	"return": "keyword1",
	"self": "keyword1",
	"short": "keyword3",
	"signed": "keyword3",
	"sizeof": "keyword1",
	"static": "keyword1",
	"struct": "keyword3",
	"super": "keyword1",
	"switch": "keyword1",
	"true": "literal2",
	"typedef": "keyword3",
	"union": "keyword3",
	"unsigned": "keyword3",
	"void": "keyword3",
	"volatile": "keyword1",
	"while": "keyword1",
}

# Dictionary of keywords dictionaries for objective_c mode.
keywordsDictDict = {
	"objective_c_main": objective_c_main_keywords_dict,
}

# Rules for objective_c_main ruleset.

def objective-c_rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment3", begin="/**", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="doxygen::DOXYGEN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def objective-c_rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment3", begin="/*!", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="doxygen::DOXYGEN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def objective-c_rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def objective-c_rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def objective-c_rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def objective-c_rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="literal3", begin="@\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def objective-c_rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="##",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def objective-c_rule7(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="keyword2", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="c::CPP", exclude_match=False)

def objective-c_rule8(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def objective-c_rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def objective-c_rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def objective-c_rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def objective-c_rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def objective-c_rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def objective-c_rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def objective-c_rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def objective-c_rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def objective-c_rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def objective-c_rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def objective-c_rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def objective-c_rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def objective-c_rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def objective-c_rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def objective-c_rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def objective-c_rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def objective-c_rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def objective-c_rule26(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=False, at_whitespace_end=True, at_word_start=False, exclude_match=True)

def objective-c_rule27(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def objective-c_rule28(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [objective-c_rule10,],
	"\"": [objective-c_rule3,],
	"#": [objective-c_rule6,objective-c_rule7,],
	"%": [objective-c_rule19,],
	"&": [objective-c_rule20,],
	"'": [objective-c_rule4,],
	"(": [objective-c_rule27,],
	"*": [objective-c_rule16,],
	"+": [objective-c_rule13,],
	"-": [objective-c_rule14,],
	"/": [objective-c_rule0,objective-c_rule1,objective-c_rule2,objective-c_rule8,objective-c_rule15,],
	"0": [objective-c_rule28,],
	"1": [objective-c_rule28,],
	"2": [objective-c_rule28,],
	"3": [objective-c_rule28,],
	"4": [objective-c_rule28,],
	"5": [objective-c_rule28,],
	"6": [objective-c_rule28,],
	"7": [objective-c_rule28,],
	"8": [objective-c_rule28,],
	"9": [objective-c_rule28,],
	":": [objective-c_rule26,],
	"<": [objective-c_rule12,objective-c_rule18,],
	"=": [objective-c_rule9,],
	">": [objective-c_rule11,objective-c_rule17,],
	"@": [objective-c_rule5,objective-c_rule28,],
	"A": [objective-c_rule28,],
	"B": [objective-c_rule28,],
	"C": [objective-c_rule28,],
	"D": [objective-c_rule28,],
	"E": [objective-c_rule28,],
	"F": [objective-c_rule28,],
	"G": [objective-c_rule28,],
	"H": [objective-c_rule28,],
	"I": [objective-c_rule28,],
	"J": [objective-c_rule28,],
	"K": [objective-c_rule28,],
	"L": [objective-c_rule28,],
	"M": [objective-c_rule28,],
	"N": [objective-c_rule28,],
	"O": [objective-c_rule28,],
	"P": [objective-c_rule28,],
	"Q": [objective-c_rule28,],
	"R": [objective-c_rule28,],
	"S": [objective-c_rule28,],
	"T": [objective-c_rule28,],
	"U": [objective-c_rule28,],
	"V": [objective-c_rule28,],
	"W": [objective-c_rule28,],
	"X": [objective-c_rule28,],
	"Y": [objective-c_rule28,],
	"Z": [objective-c_rule28,],
	"^": [objective-c_rule22,],
	"a": [objective-c_rule28,],
	"b": [objective-c_rule28,],
	"c": [objective-c_rule28,],
	"d": [objective-c_rule28,],
	"e": [objective-c_rule28,],
	"f": [objective-c_rule28,],
	"g": [objective-c_rule28,],
	"h": [objective-c_rule28,],
	"i": [objective-c_rule28,],
	"j": [objective-c_rule28,],
	"k": [objective-c_rule28,],
	"l": [objective-c_rule28,],
	"m": [objective-c_rule28,],
	"n": [objective-c_rule28,],
	"o": [objective-c_rule28,],
	"p": [objective-c_rule28,],
	"q": [objective-c_rule28,],
	"r": [objective-c_rule28,],
	"s": [objective-c_rule28,],
	"t": [objective-c_rule28,],
	"u": [objective-c_rule28,],
	"v": [objective-c_rule28,],
	"w": [objective-c_rule28,],
	"x": [objective-c_rule28,],
	"y": [objective-c_rule28,],
	"z": [objective-c_rule28,],
	"{": [objective-c_rule25,],
	"|": [objective-c_rule21,],
	"}": [objective-c_rule24,],
	"~": [objective-c_rule23,],
}

# x.rulesDictDict for objective_c mode.
rulesDictDict = {
	"objective_c_main": rulesDict1,
}

# Import dict for objective_c mode.
importDict = {}

