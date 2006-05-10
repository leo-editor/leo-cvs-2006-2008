# Leo colorizer control file for ruby mode.
# This file is in the public domain.

# Properties for ruby mode.
properties = {
	"commentEnd": "=end",
	"commentStart": "=begin",
	"indentCloseBrackets": "}",
	"indentOpenBrackets": "{",
	"lineComment": "#",
	"lineUpClosingBracket": "true",
}

# Attributes dict for ruby_main ruleset.
ruby_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Attributes dict for ruby_doublequoteliteral ruleset.
ruby_doublequoteliteral_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for ruby mode.
attributesDictDict = {
	"ruby_doublequoteliteral": ruby_doublequoteliteral_attributes_dict,
	"ruby_main": ruby_main_attributes_dict,
}

# Keywords dict for ruby_main ruleset.
ruby_main_keywords_dict = {
	"BEGIN": "keyword1",
	"END": "keyword1",
	"__FILE__": "literal2",
	"__LINE__": "literal2",
	"alias": "keyword1",
	"and": "keyword1",
	"begin": "keyword1",
	"break": "keyword1",
	"case": "keyword1",
	"class": "keyword1",
	"def": "keyword1",
	"defined": "keyword1",
	"do": "keyword1",
	"else": "keyword1",
	"elsif": "keyword1",
	"end": "keyword1",
	"ensure": "keyword1",
	"false": "literal2",
	"for": "keyword1",
	"if": "keyword1",
	"in": "keyword1",
	"include": "keyword2",
	"module": "keyword1",
	"next": "keyword1",
	"nil": "keyword1",
	"not": "operator",
	"or": "keyword1",
	"redo": "keyword1",
	"require": "keyword2",
	"rescue": "keyword1",
	"retry": "keyword1",
	"return": "keyword1",
	"self": "literal2",
	"super": "literal2",
	"then": "keyword1",
	"true": "literal2",
	"undef": "keyword1",
	"unless": "keyword1",
	"until": "keyword1",
	"when": "keyword1",
	"while": "keyword1",
	"yield": "keyword1",
}

# Keywords dict for ruby_doublequoteliteral ruleset.
ruby_doublequoteliteral_keywords_dict = {}

# Dictionary of keywords dictionaries for ruby mode.
keywordsDictDict = {
	"ruby_doublequoteliteral": ruby_doublequoteliteral_keywords_dict,
	"ruby_main": ruby_main_keywords_dict,
}

# Rules for ruby_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment2", begin="=begin", end="=end",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="#{", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=True,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="doubleQuoteLiteral",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="::",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="===",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="**",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="...",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="..",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule31(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule32(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="?",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule33(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=False, at_whitespace_end=True, at_word_start=False, exclude_match=True)

def rule34(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule35(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule23,],
	"\"": [rule2,],
	"#": [rule1,rule4,],
	"%": [rule20,],
	"&": [rule21,],
	"'": [rule3,],
	"(": [rule7,],
	")": [rule8,],
	"*": [rule18,rule19,],
	"+": [rule15,],
	"-": [rule16,],
	".": [rule28,rule29,],
	"/": [rule17,],
	"0": [rule35,],
	"1": [rule35,],
	"2": [rule35,],
	"3": [rule35,],
	"4": [rule35,],
	"5": [rule35,],
	"6": [rule35,],
	"7": [rule35,],
	"8": [rule35,],
	"9": [rule35,],
	":": [rule9,rule33,rule34,],
	"<": [rule13,rule14,rule25,],
	"=": [rule0,rule10,rule11,],
	">": [rule12,rule24,],
	"?": [rule32,],
	"@": [rule35,],
	"A": [rule35,],
	"B": [rule35,],
	"C": [rule35,],
	"D": [rule35,],
	"E": [rule35,],
	"F": [rule35,],
	"G": [rule35,],
	"H": [rule35,],
	"I": [rule35,],
	"J": [rule35,],
	"K": [rule35,],
	"L": [rule35,],
	"M": [rule35,],
	"N": [rule35,],
	"O": [rule35,],
	"P": [rule35,],
	"Q": [rule35,],
	"R": [rule35,],
	"S": [rule35,],
	"T": [rule35,],
	"U": [rule35,],
	"V": [rule35,],
	"W": [rule35,],
	"X": [rule35,],
	"Y": [rule35,],
	"Z": [rule35,],
	"[": [rule31,],
	"]": [rule30,],
	"^": [rule26,],
	"_": [rule35,],
	"a": [rule35,],
	"b": [rule35,],
	"c": [rule35,],
	"d": [rule35,],
	"e": [rule35,],
	"f": [rule35,],
	"g": [rule35,],
	"h": [rule35,],
	"i": [rule35,],
	"j": [rule35,],
	"k": [rule35,],
	"l": [rule35,],
	"m": [rule35,],
	"n": [rule35,],
	"o": [rule35,],
	"p": [rule35,],
	"q": [rule35,],
	"r": [rule35,],
	"s": [rule35,],
	"t": [rule35,],
	"u": [rule35,],
	"v": [rule35,],
	"w": [rule35,],
	"x": [rule35,],
	"y": [rule35,],
	"z": [rule35,],
	"{": [rule5,],
	"|": [rule22,],
	"}": [rule6,],
	"~": [rule27,],
}

# Rules for ruby_doublequoteliteral ruleset.

def rule36(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="#{", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=True,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules dict for doublequoteliteral ruleset.
rulesDict2 = {
	"#": [rule36,],
}

# x.rulesDictDict for ruby mode.
rulesDictDict = {
	"ruby_doublequoteliteral": rulesDict2,
	"ruby_main": rulesDict1,
}

# Import dict for ruby mode.
importDict = {}

