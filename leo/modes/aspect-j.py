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

def rule0(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment1", seq="/**/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment3", begin="/**", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="java::JAVADOC",exclude_match=False,
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
    return colorer.match_eol_span(s, i, kind="comment2", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq=".*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=False, at_whitespace_end=True, at_word_start=False, exclude_match=True)

def rule25(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule26(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule7,],
	"\"": [rule3,],
	"%": [rule17,],
	"&": [rule18,],
	"'": [rule4,],
	"(": [rule25,],
	"*": [rule14,],
	"+": [rule10,],
	"-": [rule11,],
	".": [rule13,],
	"/": [rule0,rule1,rule2,rule5,rule12,],
	"0": [rule26,],
	"1": [rule26,],
	"2": [rule26,],
	"3": [rule26,],
	"4": [rule26,],
	"5": [rule26,],
	"6": [rule26,],
	"7": [rule26,],
	"8": [rule26,],
	"9": [rule26,],
	":": [rule24,],
	"<": [rule9,rule16,],
	"=": [rule6,],
	">": [rule8,rule15,],
	"@": [rule26,],
	"A": [rule26,],
	"B": [rule26,],
	"C": [rule26,],
	"D": [rule26,],
	"E": [rule26,],
	"F": [rule26,],
	"G": [rule26,],
	"H": [rule26,],
	"I": [rule26,],
	"J": [rule26,],
	"K": [rule26,],
	"L": [rule26,],
	"M": [rule26,],
	"N": [rule26,],
	"O": [rule26,],
	"P": [rule26,],
	"Q": [rule26,],
	"R": [rule26,],
	"S": [rule26,],
	"T": [rule26,],
	"U": [rule26,],
	"V": [rule26,],
	"W": [rule26,],
	"X": [rule26,],
	"Y": [rule26,],
	"Z": [rule26,],
	"^": [rule20,],
	"_": [rule26,],
	"a": [rule26,],
	"b": [rule26,],
	"c": [rule26,],
	"d": [rule26,],
	"e": [rule26,],
	"f": [rule26,],
	"g": [rule26,],
	"h": [rule26,],
	"i": [rule26,],
	"j": [rule26,],
	"k": [rule26,],
	"l": [rule26,],
	"m": [rule26,],
	"n": [rule26,],
	"o": [rule26,],
	"p": [rule26,],
	"q": [rule26,],
	"r": [rule26,],
	"s": [rule26,],
	"t": [rule26,],
	"u": [rule26,],
	"v": [rule26,],
	"w": [rule26,],
	"x": [rule26,],
	"y": [rule26,],
	"z": [rule26,],
	"{": [rule23,],
	"|": [rule19,],
	"}": [rule22,],
	"~": [rule21,],
}

# x.rulesDictDict for aspect_j mode.
rulesDictDict = {
	"aspect_j_main": rulesDict1,
}

# Import dict for aspect_j mode.
importDict = {}

