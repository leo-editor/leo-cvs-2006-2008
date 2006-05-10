# Leo colorizer control file for c mode.
# This file is in the public domain.

# Properties for c mode.
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

# Attributes dict for c_main ruleset.
c_main_attributes_dict = {
	"default": "null",
	"digit_re": "(0x[[:xdigit:]]+[lL]?|[[:digit:]]+(e[[:digit:]]*)?[lLdDfF]?)",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Attributes dict for c_cpp ruleset.
c_cpp_attributes_dict = {
	"default": "KEYWORD2",
	"digit_re": "(0x[[:xdigit:]]+[lL]?|[[:digit:]]+(e[[:digit:]]*)?[lLdDfF]?)",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Attributes dict for c_include ruleset.
c_include_attributes_dict = {
	"default": "KEYWORD2",
	"digit_re": "(0x[[:xdigit:]]+[lL]?|[[:digit:]]+(e[[:digit:]]*)?[lLdDfF]?)",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for c mode.
attributesDictDict = {
	"c_cpp": c_cpp_attributes_dict,
	"c_include": c_include_attributes_dict,
	"c_main": c_main_attributes_dict,
}

# Keywords dict for c_main ruleset.
c_main_keywords_dict = {
	"NULL": "literal2",
	"asm": "keyword2",
	"asmlinkage": "keyword2",
	"auto": "keyword1",
	"break": "keyword1",
	"case": "keyword1",
	"char": "keyword3",
	"const": "keyword1",
	"continue": "keyword1",
	"default": "keyword1",
	"do": "keyword1",
	"double": "keyword3",
	"else": "keyword1",
	"enum": "keyword3",
	"extern": "keyword1",
	"false": "literal2",
	"far": "keyword2",
	"float": "keyword3",
	"for": "keyword1",
	"goto": "keyword1",
	"huge": "keyword2",
	"if": "keyword1",
	"inline": "keyword2",
	"int": "keyword3",
	"long": "keyword3",
	"near": "keyword2",
	"pascal": "keyword2",
	"register": "keyword1",
	"return": "keyword1",
	"short": "keyword3",
	"signed": "keyword3",
	"sizeof": "keyword1",
	"static": "keyword1",
	"struct": "keyword3",
	"switch": "keyword1",
	"true": "literal2",
	"typedef": "keyword3",
	"union": "keyword3",
	"unsigned": "keyword3",
	"void": "keyword3",
	"volatile": "keyword1",
	"while": "keyword1",
}

# Keywords dict for c_cpp ruleset.
c_cpp_keywords_dict = {
	"assert": "markup",
	"define": "markup",
	"elif": "markup",
	"else": "markup",
	"endif": "markup",
	"error": "markup",
	"ident": "markup",
	"if": "markup",
	"ifdef": "markup",
	"ifndef": "markup",
	"import": "markup",
	"include": "markup",
	"include_next": "markup",
	"line": "markup",
	"pragma": "markup",
	"sccs": "markup",
	"unassert": "markup",
	"undef": "markup",
	"warning": "markup",
}

# Keywords dict for c_include ruleset.
c_include_keywords_dict = {}

# Dictionary of keywords dictionaries for c mode.
keywordsDictDict = {
	"c_cpp": c_cpp_keywords_dict,
	"c_include": c_include_keywords_dict,
	"c_main": c_main_keywords_dict,
}

# Rules for c_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment3", begin="/**", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="doxygen::DOXYGEN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment3", begin="/*!", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="doxygen::DOXYGEN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="##",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="keyword2", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="CPP", exclude_match=False)

def rule7(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=False, at_whitespace_end=True, at_word_start=False, exclude_match=True)

def rule26(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule27(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule9,],
	"\"": [rule3,],
	"#": [rule5,rule6,],
	"%": [rule18,],
	"&": [rule19,],
	"'": [rule4,],
	"(": [rule26,],
	"*": [rule15,],
	"+": [rule12,],
	"-": [rule13,],
	"/": [rule0,rule1,rule2,rule7,rule14,],
	"0": [rule27,],
	"1": [rule27,],
	"2": [rule27,],
	"3": [rule27,],
	"4": [rule27,],
	"5": [rule27,],
	"6": [rule27,],
	"7": [rule27,],
	"8": [rule27,],
	"9": [rule27,],
	":": [rule25,],
	"<": [rule11,rule17,],
	"=": [rule8,],
	">": [rule10,rule16,],
	"@": [rule27,],
	"A": [rule27,],
	"B": [rule27,],
	"C": [rule27,],
	"D": [rule27,],
	"E": [rule27,],
	"F": [rule27,],
	"G": [rule27,],
	"H": [rule27,],
	"I": [rule27,],
	"J": [rule27,],
	"K": [rule27,],
	"L": [rule27,],
	"M": [rule27,],
	"N": [rule27,],
	"O": [rule27,],
	"P": [rule27,],
	"Q": [rule27,],
	"R": [rule27,],
	"S": [rule27,],
	"T": [rule27,],
	"U": [rule27,],
	"V": [rule27,],
	"W": [rule27,],
	"X": [rule27,],
	"Y": [rule27,],
	"Z": [rule27,],
	"^": [rule21,],
	"_": [rule27,],
	"a": [rule27,],
	"b": [rule27,],
	"c": [rule27,],
	"d": [rule27,],
	"e": [rule27,],
	"f": [rule27,],
	"g": [rule27,],
	"h": [rule27,],
	"i": [rule27,],
	"j": [rule27,],
	"k": [rule27,],
	"l": [rule27,],
	"m": [rule27,],
	"n": [rule27,],
	"o": [rule27,],
	"p": [rule27,],
	"q": [rule27,],
	"r": [rule27,],
	"s": [rule27,],
	"t": [rule27,],
	"u": [rule27,],
	"v": [rule27,],
	"w": [rule27,],
	"x": [rule27,],
	"y": [rule27,],
	"z": [rule27,],
	"{": [rule24,],
	"|": [rule20,],
	"}": [rule23,],
	"~": [rule22,],
}

# Rules for c_cpp ruleset.

def rule28(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule29(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="markup", seq="include",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="INCLUDE", exclude_match=False)

def rule30(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for cpp ruleset.
rulesDict2 = {
	"/": [rule28,],
	"0": [rule30,],
	"1": [rule30,],
	"2": [rule30,],
	"3": [rule30,],
	"4": [rule30,],
	"5": [rule30,],
	"6": [rule30,],
	"7": [rule30,],
	"8": [rule30,],
	"9": [rule30,],
	"@": [rule30,],
	"A": [rule30,],
	"B": [rule30,],
	"C": [rule30,],
	"D": [rule30,],
	"E": [rule30,],
	"F": [rule30,],
	"G": [rule30,],
	"H": [rule30,],
	"I": [rule30,],
	"J": [rule30,],
	"K": [rule30,],
	"L": [rule30,],
	"M": [rule30,],
	"N": [rule30,],
	"O": [rule30,],
	"P": [rule30,],
	"Q": [rule30,],
	"R": [rule30,],
	"S": [rule30,],
	"T": [rule30,],
	"U": [rule30,],
	"V": [rule30,],
	"W": [rule30,],
	"X": [rule30,],
	"Y": [rule30,],
	"Z": [rule30,],
	"_": [rule30,],
	"a": [rule30,],
	"b": [rule30,],
	"c": [rule30,],
	"d": [rule30,],
	"e": [rule30,],
	"f": [rule30,],
	"g": [rule30,],
	"h": [rule30,],
	"i": [rule29,rule30,],
	"j": [rule30,],
	"k": [rule30,],
	"l": [rule30,],
	"m": [rule30,],
	"n": [rule30,],
	"o": [rule30,],
	"p": [rule30,],
	"q": [rule30,],
	"r": [rule30,],
	"s": [rule30,],
	"t": [rule30,],
	"u": [rule30,],
	"v": [rule30,],
	"w": [rule30,],
	"x": [rule30,],
	"y": [rule30,],
	"z": [rule30,],
}

# Rules for c_include ruleset.

# Rules dict for include ruleset.
rulesDict3 = {}

# x.rulesDictDict for c mode.
rulesDictDict = {
	"c_cpp": rulesDict2,
	"c_include": rulesDict3,
	"c_main": rulesDict1,
}

# Import dict for c mode.
importDict = {}

