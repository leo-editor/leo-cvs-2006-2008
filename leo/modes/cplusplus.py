# Leo colorizer control file for cplusplus mode.

# Properties for cplusplus mode.
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

# Keywords dict for cplusplus_main ruleset.
cplusplus_main_keywords_dict = {
	"NULL": "literal2",
	"and": "keyword3",
	"and_eq": "keyword3",
	"asm": "keyword2",
	"auto": "keyword1",
	"bitand": "keyword3",
	"bitor": "keyword3",
	"bool": "keyword3",
	"break": "keyword1",
	"case": "keyword1",
	"catch": "keyword1",
	"char": "keyword3",
	"class": "keyword3",
	"compl": "keyword3",
	"const": "keyword1",
	"const_cast": "keyword3",
	"continue": "keyword1",
	"default": "keyword1",
	"delete": "keyword1",
	"do": "keyword1",
	"double": "keyword3",
	"dynamic_cast": "keyword3",
	"else": "keyword1",
	"enum": "keyword3",
	"explicit": "keyword1",
	"export": "keyword2",
	"extern": "keyword2",
	"false": "literal2",
	"float": "keyword3",
	"for": "keyword1",
	"friend": "keyword1",
	"goto": "keyword1",
	"if": "keyword1",
	"inline": "keyword1",
	"int": "keyword3",
	"long": "keyword3",
	"mutable": "keyword3",
	"namespace": "keyword2",
	"new": "keyword1",
	"not": "keyword3",
	"not_eq": "keyword3",
	"operator": "keyword3",
	"or": "keyword3",
	"or_eq": "keyword3",
	"private": "keyword1",
	"protected": "keyword1",
	"public": "keyword1",
	"register": "keyword1",
	"reinterpret_cast": "keyword3",
	"return": "keyword1",
	"short": "keyword3",
	"signed": "keyword3",
	"sizeof": "keyword1",
	"static": "keyword1",
	"static_cast": "keyword3",
	"struct": "keyword3",
	"switch": "keyword1",
	"template": "keyword3",
	"this": "literal2",
	"throw": "keyword1",
	"true": "literal2",
	"try": "keyword1",
	"typedef": "keyword3",
	"typeid": "keyword3",
	"typename": "keyword3",
	"union": "keyword3",
	"unsigned": "keyword3",
	"using": "keyword2",
	"virtual": "keyword1",
	"void": "keyword1",
	"volatile": "keyword1",
	"wchar_t": "keyword3",
	"while": "keyword1",
	"xor": "keyword3",
	"xor_eq": "keyword3",
}

# Dictionary of keywords dictionaries for cplusplus mode.
keywordsDictDict = {
	"cplusplus_main": cplusplus_main_keywords_dict,
}

# Rules for cplusplus_main ruleset.

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
        delegate="c::CPP", exclude_match=False)

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
    return colorer.match_mark_previous(s, i, kind="function", pattern="::",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule26(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=False, at_whitespace_end=True, at_word_start=False, exclude_match=True)

def rule27(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule28(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule9,],
	"\"": [rule3,],
	"#": [rule5,rule6,],
	"%": [rule18,],
	"&": [rule19,],
	"'": [rule4,],
	"(": [rule27,],
	"*": [rule15,],
	"+": [rule12,],
	"-": [rule13,],
	"/": [rule0,rule1,rule2,rule7,rule14,],
	"0": [rule28,],
	"1": [rule28,],
	"2": [rule28,],
	"3": [rule28,],
	"4": [rule28,],
	"5": [rule28,],
	"6": [rule28,],
	"7": [rule28,],
	"8": [rule28,],
	"9": [rule28,],
	":": [rule25,rule26,],
	"<": [rule11,rule17,],
	"=": [rule8,],
	">": [rule10,rule16,],
	"@": [rule28,],
	"A": [rule28,],
	"B": [rule28,],
	"C": [rule28,],
	"D": [rule28,],
	"E": [rule28,],
	"F": [rule28,],
	"G": [rule28,],
	"H": [rule28,],
	"I": [rule28,],
	"J": [rule28,],
	"K": [rule28,],
	"L": [rule28,],
	"M": [rule28,],
	"N": [rule28,],
	"O": [rule28,],
	"P": [rule28,],
	"Q": [rule28,],
	"R": [rule28,],
	"S": [rule28,],
	"T": [rule28,],
	"U": [rule28,],
	"V": [rule28,],
	"W": [rule28,],
	"X": [rule28,],
	"Y": [rule28,],
	"Z": [rule28,],
	"^": [rule21,],
	"_": [rule28,],
	"a": [rule28,],
	"b": [rule28,],
	"c": [rule28,],
	"d": [rule28,],
	"e": [rule28,],
	"f": [rule28,],
	"g": [rule28,],
	"h": [rule28,],
	"i": [rule28,],
	"j": [rule28,],
	"k": [rule28,],
	"l": [rule28,],
	"m": [rule28,],
	"n": [rule28,],
	"o": [rule28,],
	"p": [rule28,],
	"q": [rule28,],
	"r": [rule28,],
	"s": [rule28,],
	"t": [rule28,],
	"u": [rule28,],
	"v": [rule28,],
	"w": [rule28,],
	"x": [rule28,],
	"y": [rule28,],
	"z": [rule28,],
	"{": [rule24,],
	"|": [rule20,],
	"}": [rule23,],
	"~": [rule22,],
}

# x.rulesDictDict for cplusplus mode.
rulesDictDict = {
	"cplusplus_main": rulesDict1,
}

# Import dict for cplusplus mode.
importDict = {}

