# Leo colorizer control file for idl mode.

# Properties for idl mode.
properties = {
	"boxComment": "*",
	"commentEnd": "*/",
	"commentStart": "/*",
	"indentCloseBrackets": "}",
	"indentOpenBrackets": "{",
	"lineComment": "//",
	"lineUpClosingBracket": "true",
}

# Keywords dict for idl_main ruleset.
idl_main_keywords_dict = {
	"		": "keywords",
	"			": "keywords",
	"
": "keywords",
	"FALSE": "literal2",
	"Object": "keyword3",
	"TRUE": "literal2",
	"any": "keyword3",
	"attribute": "keyword1",
	"boolean": "keyword3",
	"case": "keyword1",
	"char": "keyword3",
	"const": "keyword1",
	"context": "keyword1",
	"default": "keyword1",
	"double": "keyword3",
	"enum": "keyword3",
	"exception": "keyword1",
	"fixed": "keyword1",
	"float": "keyword3",
	"in": "keyword1",
	"inout": "keyword1",
	"interface": "keyword1",
	"long": "keyword3",
	"module": "keyword1",
	"octet": "keyword3",
	"oneway": "keyword1",
	"out": "keyword1",
	"raises": "keyword1",
	"readonly": "keyword1",
	"sequence": "keyword3",
	"short": "keyword3",
	"string": "keyword3",
	"struct": "keyword3",
	"switch": "keyword1",
	"typedef": "keyword3",
	"union": "keyword3",
	"unsigned": "keyword3",
	"void": "keyword3",
	"wchar": "keyword3",
	"wstring": "keyword3",
}

# Dictionary of keywords dictionaries for idl mode.
keywordsDictDict = {
	"idl_main": idl_main_keywords_dict,
}

# Rules for idl_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

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
    return colorer.match_eol_span(s, i, kind="comment2", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule8(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"\"": [rule1,],
	"'": [rule2,],
	"(": [rule7,],
	"/": [rule0,rule3,],
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
	":": [rule6,],
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
	"_": [rule8,],
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
	"{": [rule5,],
	"}": [rule4,],
}

# x.rulesDictDict for idl mode.
rulesDictDict = {
	"idl_main": rulesDict1,
}

# Import dict for idl mode.
importDict = {}

