# Leo colorizer control file for antlr mode.
# This file is in the public domain.

# Properties for antlr mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"lineComment": "//",
	"wordBreakChars": "",
}

# Attributes dict for antlr_main ruleset.
antlr_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for antlr mode.
attributesDictDict = {
	"antlr_main": antlr_main_attributes_dict,
}

# Keywords dict for antlr_main ruleset.
antlr_main_keywords_dict = {
	"abstract": "keyword1",
	"assert": "function",
	"boolean": "keyword2",
	"break": "keyword1",
	"byte": "keyword2",
	"case": "keyword1",
	"catch": "keyword1",
	"char": "keyword2",
	"class": "keyword2",
	"const": "invalid",
	"continue": "keyword1",
	"default": "keyword1",
	"do": "keyword1",
	"double": "keyword2",
	"else": "keyword1",
	"extends": "keyword1",
	"false": "literal2",
	"final": "keyword1",
	"finally": "keyword1",
	"float": "keyword2",
	"for": "keyword1",
	"goto": "invalid",
	"header": "keyword3",
	"if": "keyword1",
	"implements": "keyword1",
	"import": "keyword1",
	"instanceof": "keyword1",
	"int": "keyword2",
	"interface": "keyword2",
	"long": "keyword2",
	"native": "keyword1",
	"new": "keyword1",
	"null": "literal2",
	"options": "keyword3",
	"package": "keyword1",
	"private": "keyword1",
	"protected": "keyword1",
	"public": "keyword1",
	"return": "keyword1",
	"short": "keyword2",
	"static": "keyword1",
	"strictfp": "keyword1",
	"super": "literal2",
	"switch": "keyword1",
	"synchronized": "keyword1",
	"this": "literal2",
	"throw": "keyword1",
	"throws": "keyword1",
	"tokens": "keyword3",
	"transient": "keyword1",
	"true": "literal2",
	"try": "keyword1",
	"void": "keyword2",
	"volatile": "keyword1",
	"while": "keyword1",
}

# Dictionary of keywords dictionaries for antlr mode.
keywordsDictDict = {
	"antlr_main": antlr_main_keywords_dict,
}

# Rules for antlr_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment2", begin="/**", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="java::JAVADOC",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"\"": [rule3,],
	"/": [rule0,rule1,rule2,],
	"0": [rule6,],
	"1": [rule6,],
	"2": [rule6,],
	"3": [rule6,],
	"4": [rule6,],
	"5": [rule6,],
	"6": [rule6,],
	"7": [rule6,],
	"8": [rule6,],
	"9": [rule6,],
	":": [rule5,],
	"@": [rule6,],
	"A": [rule6,],
	"B": [rule6,],
	"C": [rule6,],
	"D": [rule6,],
	"E": [rule6,],
	"F": [rule6,],
	"G": [rule6,],
	"H": [rule6,],
	"I": [rule6,],
	"J": [rule6,],
	"K": [rule6,],
	"L": [rule6,],
	"M": [rule6,],
	"N": [rule6,],
	"O": [rule6,],
	"P": [rule6,],
	"Q": [rule6,],
	"R": [rule6,],
	"S": [rule6,],
	"T": [rule6,],
	"U": [rule6,],
	"V": [rule6,],
	"W": [rule6,],
	"X": [rule6,],
	"Y": [rule6,],
	"Z": [rule6,],
	"a": [rule6,],
	"b": [rule6,],
	"c": [rule6,],
	"d": [rule6,],
	"e": [rule6,],
	"f": [rule6,],
	"g": [rule6,],
	"h": [rule6,],
	"i": [rule6,],
	"j": [rule6,],
	"k": [rule6,],
	"l": [rule6,],
	"m": [rule6,],
	"n": [rule6,],
	"o": [rule6,],
	"p": [rule6,],
	"q": [rule6,],
	"r": [rule6,],
	"s": [rule6,],
	"t": [rule6,],
	"u": [rule6,],
	"v": [rule6,],
	"w": [rule6,],
	"x": [rule6,],
	"y": [rule6,],
	"z": [rule6,],
	"|": [rule4,],
}

# x.rulesDictDict for antlr mode.
rulesDictDict = {
	"antlr_main": rulesDict1,
}

# Import dict for antlr mode.
importDict = {}

