# Leo colorizer control file for aspect-j mode.
# This file is in the public domain.

# Properties for aspect-j mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"doubleBracketIndent": "false",
	"indentCloseBrackets": "}",
	"indentOpenBrackets": "{",
	"indentPrevLine": "\\s*(((if|while)\\s*\\(|else\\s*|else\\s+if\\s*\\(|for\\s*\\(.*\\))[^{;]*)",
	"lineComment": "//",
	"wordBreakChars": ",+-=<>/?^&*",
}

# Attributes dict for aspect_j_main ruleset.
aspect_j_main_attributes_dict = {
	"default": "null",
	"digit_re": "(0x)?[[:xdigit:]]+[lLdDfF]?",
	"escape": "\\",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for aspect_j mode.
attributesDictDict = {
	"aspect_j_main": aspect_j_main_attributes_dict,
}

# Keywords dict for aspect_j_main ruleset.
aspect_j_main_keywords_dict = {
	"..": "keyword4",
	"abstract": "keyword1",
	"adviceexecution": "keyword4",
	"after": "keyword4",
	"args": "keyword4",
	"around": "keyword4",
	"aspect": "keyword4",
	"assert": "function",
	"before": "keyword4",
	"boolean": "keyword3",
	"break": "keyword1",
	"byte": "keyword3",
	"call": "keyword4",
	"case": "keyword1",
	"catch": "keyword1",
	"cflow": "keyword4",
	"cflowbelow": "keyword4",
	"char": "keyword3",
	"class": "keyword3",
	"const": "invalid",
	"continue": "keyword1",
	"declare": "keyword4",
	"default": "keyword1",
	"do": "keyword1",
	"double": "keyword3",
	"else": "keyword1",
	"execution": "keyword4",
	"extends": "keyword1",
	"false": "literal2",
	"final": "keyword1",
	"finally": "keyword1",
	"float": "keyword3",
	"for": "keyword1",
	"get": "keyword4",
	"goto": "invalid",
	"handler": "keyword4",
	"if": "keyword1",
	"implements": "keyword1",
	"import": "keyword2",
	"initialization": "keyword4",
	"instanceof": "keyword1",
	"int": "keyword3",
	"interface": "keyword3",
	"issingleton": "keyword4",
	"long": "keyword3",
	"native": "keyword1",
	"new": "keyword1",
	"null": "literal2",
	"package": "keyword2",
	"percflow": "keyword4",
	"pertarget": "keyword4",
	"perthis": "keyword4",
	"pointcut": "keyword4",
	"precedence": "keyword4",
	"preinitialization": "keyword4",
	"private": "keyword1",
	"privileged": "keyword4",
	"proceed": "keyword4",
	"protected": "keyword1",
	"public": "keyword1",
	"return": "keyword1",
	"set": "keyword4",
	"short": "keyword3",
	"static": "keyword1",
	"staticinitialization": "keyword4",
	"strictfp": "keyword1",
	"super": "literal2",
	"switch": "keyword1",
	"synchronized": "keyword1",
	"target": "keyword4",
	"this": "literal2",
	"throw": "keyword1",
	"throws": "keyword1",
	"transient": "keyword1",
	"true": "literal2",
	"try": "keyword1",
	"void": "keyword3",
	"volatile": "keyword1",
	"while": "keyword1",
	"within": "keyword4",
	"withincode": "keyword4",
}

# Dictionary of keywords dictionaries for aspect_j mode.
keywordsDictDict = {
	"aspect_j_main": aspect_j_main_keywords_dict,
}

# Rules for aspect_j_main ruleset.

def aspect-j_rule0(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment1", seq="/**/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def aspect-j_rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment3", begin="/**", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="java::javadoc",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def aspect-j_rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def aspect-j_rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def aspect-j_rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def aspect-j_rule5(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def aspect-j_rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def aspect-j_rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def aspect-j_rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def aspect-j_rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def aspect-j_rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def aspect-j_rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def aspect-j_rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def aspect-j_rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq=".*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def aspect-j_rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def aspect-j_rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def aspect-j_rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def aspect-j_rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def aspect-j_rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def aspect-j_rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def aspect-j_rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def aspect-j_rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def aspect-j_rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def aspect-j_rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def aspect-j_rule24(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=False, at_whitespace_end=True, at_word_start=False, exclude_match=True)

def aspect-j_rule25(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def aspect-j_rule26(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for aspect_j_main ruleset.
rulesDict1 = {
	"!": [aspect-j_rule7,],
	"\"": [aspect-j_rule3,],
	"%": [aspect-j_rule17,],
	"&": [aspect-j_rule18,],
	"'": [aspect-j_rule4,],
	"(": [aspect-j_rule25,],
	"*": [aspect-j_rule14,],
	"+": [aspect-j_rule10,],
	"-": [aspect-j_rule11,],
	".": [aspect-j_rule13,aspect-j_rule26,],
	"/": [aspect-j_rule0,aspect-j_rule1,aspect-j_rule2,aspect-j_rule5,aspect-j_rule12,],
	"0": [aspect-j_rule26,],
	"1": [aspect-j_rule26,],
	"2": [aspect-j_rule26,],
	"3": [aspect-j_rule26,],
	"4": [aspect-j_rule26,],
	"5": [aspect-j_rule26,],
	"6": [aspect-j_rule26,],
	"7": [aspect-j_rule26,],
	"8": [aspect-j_rule26,],
	"9": [aspect-j_rule26,],
	":": [aspect-j_rule24,],
	"<": [aspect-j_rule9,aspect-j_rule16,],
	"=": [aspect-j_rule6,],
	">": [aspect-j_rule8,aspect-j_rule15,],
	"@": [aspect-j_rule26,],
	"A": [aspect-j_rule26,],
	"B": [aspect-j_rule26,],
	"C": [aspect-j_rule26,],
	"D": [aspect-j_rule26,],
	"E": [aspect-j_rule26,],
	"F": [aspect-j_rule26,],
	"G": [aspect-j_rule26,],
	"H": [aspect-j_rule26,],
	"I": [aspect-j_rule26,],
	"J": [aspect-j_rule26,],
	"K": [aspect-j_rule26,],
	"L": [aspect-j_rule26,],
	"M": [aspect-j_rule26,],
	"N": [aspect-j_rule26,],
	"O": [aspect-j_rule26,],
	"P": [aspect-j_rule26,],
	"Q": [aspect-j_rule26,],
	"R": [aspect-j_rule26,],
	"S": [aspect-j_rule26,],
	"T": [aspect-j_rule26,],
	"U": [aspect-j_rule26,],
	"V": [aspect-j_rule26,],
	"W": [aspect-j_rule26,],
	"X": [aspect-j_rule26,],
	"Y": [aspect-j_rule26,],
	"Z": [aspect-j_rule26,],
	"^": [aspect-j_rule20,],
	"a": [aspect-j_rule26,],
	"b": [aspect-j_rule26,],
	"c": [aspect-j_rule26,],
	"d": [aspect-j_rule26,],
	"e": [aspect-j_rule26,],
	"f": [aspect-j_rule26,],
	"g": [aspect-j_rule26,],
	"h": [aspect-j_rule26,],
	"i": [aspect-j_rule26,],
	"j": [aspect-j_rule26,],
	"k": [aspect-j_rule26,],
	"l": [aspect-j_rule26,],
	"m": [aspect-j_rule26,],
	"n": [aspect-j_rule26,],
	"o": [aspect-j_rule26,],
	"p": [aspect-j_rule26,],
	"q": [aspect-j_rule26,],
	"r": [aspect-j_rule26,],
	"s": [aspect-j_rule26,],
	"t": [aspect-j_rule26,],
	"u": [aspect-j_rule26,],
	"v": [aspect-j_rule26,],
	"w": [aspect-j_rule26,],
	"x": [aspect-j_rule26,],
	"y": [aspect-j_rule26,],
	"z": [aspect-j_rule26,],
	"{": [aspect-j_rule23,],
	"|": [aspect-j_rule19,],
	"}": [aspect-j_rule22,],
	"~": [aspect-j_rule21,],
}

# x.rulesDictDict for aspect_j mode.
rulesDictDict = {
	"aspect_j_main": rulesDict1,
}

# Import dict for aspect_j mode.
importDict = {}

