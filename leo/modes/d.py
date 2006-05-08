# Leo colorizer control file for d mode.

# Properties for d mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"doubleBracketIndent": "false",
	"indentCloseBrackets": "}",
	"indentNextLine": "\s*(((if|while)\s*\(|else\s*|else\s+if\s*\(|for\s*\(.*\))[^{;]*)",
	"indentOpenBrackets": "{",
	"lineComment": "//",
	"lineUpClosingBracket": "true",
	"wordBreakChars": ",+-=<>/?^&*",
}

# Keywords dict for d_main ruleset.
d_main_keywords_dict = {
	"
": "keywords",
	"        ": "keywords",
	"            ": "keywords",
	"abstract": "keyword1",
	"alias": "keyword3",
	"align": "keyword4",
	"asm": "keyword2",
	"assert": "keyword2",
	"auto": "keyword3",
	"bit": "keyword3",
	"body": "keyword4",
	"break": "keyword1",
	"byte": "keyword3",
	"case>": "keyword1",
	"cast": "keyword3",
	"catch": "keyword1",
	"cdouble": "keyword3",
	"cent": "keyword3",
	"cfloat": "keyword3",
	"char": "keyword3",
	"class": "keyword3",
	"const": "invalid",
	"continue": "keyword1",
	"creal": "keyword3",
	"dchar": "keyword3",
	"debug": "keyword2",
	"default": "keyword1",
	"delegate": "keyword4",
	"delete": "keyword1",
	"deprecated": "keyword2",
	"do": "keyword1",
	"double": "keyword3",
	"else": "keyword1",
	"enum": "keyword3",
	"export": "keyword2",
	"extern": "keyword2",
	"false": "literal2",
	"final": "keyword1",
	"finally": "keyword1",
	"float": "keyword3",
	"for": "keyword1",
	"foreach": "keyword1",
	"function": "keyword4",
	"goto": "invalid",
	"idouble": "keyword3",
	"if": "keyword1",
	"ifloat": "keyword3",
	"import": "keyword2",
	"in": "invalid",
	"inout": "invalid",
	"int": "keyword3",
	"interface": "keyword2",
	"invariant": "keyword2",
	"ireal": "keyword3",
	"is": "operator",
	"long": "keyword3",
	"module": "keyword4",
	"new": "keyword1",
	"null": "literal2",
	"out": "invalid",
	"override": "keyword4",
	"package": "keyword2",
	"pragma": "keyword2",
	"private": "keyword1",
	"protected": "keyword1",
	"public": "keyword1",
	"real": "keyword3",
	"return": "keyword1",
	"short": "keyword3",
	"static": "keyword1",
	"struct": "keyword3",
	"super": "literal2",
	"switch": "keyword1",
	"synchronized": "keyword1",
	"template": "keyword3",
	"this": "literal2",
	"throw": "keyword1",
	"true": "literal2",
	"try": "keyword1",
	"typedef": "keyword3",
	"typeof": "keyword1",
	"ubyte": "keyword3",
	"ucent": "keyword3",
	"uint": "keyword3",
	"ulong": "keyword3",
	"union": "keyword3",
	"unittest": "keyword2",
	"ushort": "keyword3",
	"version": "keyword2",
	"void": "keyword3",
	"volatile": "keyword1",
	"wchar": "keyword3",
	"while": "keyword1",
	"with": "keyword2",
}

# Dictionary of keywords dictionaries for d mode.
keywordsDictDict = {
	"d_main": d_main_keywords_dict,
}

# Rules for d_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment1", seq="/**/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment3", begin="/**", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="doxygen::DOXYGEN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="comment3", begin="/*!", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="doxygen::DOXYGEN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
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
    return colorer.match_mark_following(s, i, kind="keyword4", pattern="@"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule27(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule8,],
	"\"": [rule4,],
	"%": [rule17,],
	"&": [rule18,],
	"'": [rule5,],
	"(": [rule25,],
	"*": [rule14,],
	"+": [rule11,],
	"-": [rule12,],
	"/": [rule0,rule1,rule2,rule3,rule6,rule13,],
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
	":": [rule24,],
	"<": [rule10,rule16,],
	"=": [rule7,],
	">": [rule9,rule15,],
	"@": [rule26,rule27,],
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
	"^": [rule20,],
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
	"{": [rule23,],
	"|": [rule19,],
	"}": [rule22,],
	"~": [rule21,],
}

# x.rulesDictDict for d mode.
rulesDictDict = {
	"d_main": rulesDict1,
}

# Import dict for d mode.
importDict = {}

