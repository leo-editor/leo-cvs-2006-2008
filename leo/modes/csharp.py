# Leo colorizer control file for csharp mode.
# This file is in the public domain.

# Properties for csharp mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"doubleBracketIndent": "false",
	"indentCloseBrackets": "}",
	"indentNextLine": "\\s*(((if|while)\\s*\\(|else\\s*|else\\s+if\\s*\\(|for\\s*\\(.*\\))[^{;]*)",
	"indentOpenBrackets": "{",
	"lineComment": "//",
	"lineUpClosingBracket": "true",
}

# Attributes dict for csharp_main ruleset.
csharp_main_attributes_dict = {
	"default": "null",
	"digit_re": "(0x[[:xdigit:]]+[lL]?|[[:digit:]]+(e[[:digit:]]*)?[lLdDfF]?)",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Attributes dict for csharp_doc_comment ruleset.
csharp_doc_comment_attributes_dict = {
	"default": "COMMENT3",
	"digit_re": "(0x[[:xdigit:]]+[lL]?|[[:digit:]]+(e[[:digit:]]*)?[lLdDfF]?)",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for csharp mode.
attributesDictDict = {
	"csharp_doc_comment": csharp_doc_comment_attributes_dict,
	"csharp_main": csharp_main_attributes_dict,
}

# Keywords dict for csharp_main ruleset.
csharp_main_keywords_dict = {
	"abstract": "keyword1",
	"as": "keyword1",
	"base": "keyword1",
	"bool": "keyword3",
	"break": "keyword1",
	"byte": "keyword3",
	"case": "keyword1",
	"catch": "keyword1",
	"char": "keyword3",
	"checked": "keyword1",
	"class": "keyword3",
	"const": "keyword1",
	"continue": "keyword1",
	"decimal": "keyword1",
	"default": "keyword1",
	"delegate": "keyword1",
	"do": "keyword1",
	"double": "keyword3",
	"else": "keyword1",
	"enum": "keyword3",
	"event": "keyword3",
	"explicit": "keyword1",
	"extern": "keyword1",
	"false": "literal2",
	"finally": "keyword1",
	"fixed": "keyword1",
	"float": "keyword3",
	"for": "keyword1",
	"foreach": "keyword1",
	"goto": "keyword1",
	"if": "keyword1",
	"implicit": "keyword1",
	"in": "keyword1",
	"int": "keyword3",
	"interface": "keyword3",
	"internal": "keyword1",
	"is": "keyword1",
	"lock": "keyword1",
	"long": "keyword3",
	"namespace": "keyword2",
	"new": "keyword1",
	"null": "literal2",
	"object": "keyword3",
	"operator": "keyword1",
	"out": "keyword1",
	"override": "keyword1",
	"params": "keyword1",
	"private": "keyword1",
	"protected": "keyword1",
	"public": "keyword1",
	"readonly": "keyword1",
	"ref": "keyword1",
	"return": "keyword1",
	"sbyte": "keyword3",
	"sealed": "keyword1",
	"short": "keyword3",
	"sizeof": "keyword1",
	"stackalloc": "keyword1",
	"static": "keyword1",
	"string": "keyword3",
	"struct": "keyword3",
	"switch": "keyword1",
	"this": "literal2",
	"throw": "keyword1",
	"true": "literal2",
	"try": "keyword1",
	"typeof": "keyword1",
	"uint": "keyword3",
	"ulong": "keyword3",
	"unchecked": "keyword1",
	"unsafe": "keyword1",
	"ushort": "keyword3",
	"using": "keyword2",
	"virtual": "keyword1",
	"void": "keyword3",
	"while": "keyword1",
}

# Keywords dict for csharp_doc_comment ruleset.
csharp_doc_comment_keywords_dict = {}

# Dictionary of keywords dictionaries for csharp mode.
keywordsDictDict = {
	"csharp_doc_comment": csharp_doc_comment_keywords_dict,
	"csharp_main": csharp_main_keywords_dict,
}

# Rules for csharp_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment3", seq="///",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="DOC_COMMENT", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="literal3", begin="@\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=True, no_line_break=False, no_word_break=False)

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
    return colorer.match_eol_span(s, i, kind="keyword2", seq="#if",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule7(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="keyword2", seq="#else",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule8(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="keyword2", seq="#elif",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule9(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="keyword2", seq="#endif",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule10(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="keyword2", seq="#define",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule11(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="keyword2", seq="#undef",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule12(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="keyword2", seq="#warning",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule13(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="keyword2", seq="#error",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule14(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="keyword2", seq="#line",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule15(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="keyword2", seq="#region",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule16(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="keyword2", seq="#endregion",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule31(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule32(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule33(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule34(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule35(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\\",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule36(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule37(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule38(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule39(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule40(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="?",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule41(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule42(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule18,rule25,],
	"\"": [rule4,],
	"#": [rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,],
	"%": [rule39,],
	"&": [rule38,],
	"'": [rule5,],
	"(": [rule41,],
	"*": [rule33,],
	"+": [rule28,],
	",": [rule23,],
	"-": [rule29,],
	".": [rule24,],
	"/": [rule0,rule1,rule2,rule34,],
	"0": [rule42,],
	"1": [rule42,],
	"2": [rule42,],
	"3": [rule42,],
	"4": [rule42,],
	"5": [rule42,],
	"6": [rule42,],
	"7": [rule42,],
	"8": [rule42,],
	"9": [rule42,],
	":": [rule19,],
	";": [rule20,],
	"<": [rule31,],
	"=": [rule32,],
	">": [rule30,],
	"?": [rule40,],
	"@": [rule3,rule42,],
	"A": [rule42,],
	"B": [rule42,],
	"C": [rule42,],
	"D": [rule42,],
	"E": [rule42,],
	"F": [rule42,],
	"G": [rule42,],
	"H": [rule42,],
	"I": [rule42,],
	"J": [rule42,],
	"K": [rule42,],
	"L": [rule42,],
	"M": [rule42,],
	"N": [rule42,],
	"O": [rule42,],
	"P": [rule42,],
	"Q": [rule42,],
	"R": [rule42,],
	"S": [rule42,],
	"T": [rule42,],
	"U": [rule42,],
	"V": [rule42,],
	"W": [rule42,],
	"X": [rule42,],
	"Y": [rule42,],
	"Z": [rule42,],
	"[": [rule26,],
	"\\": [rule35,],
	"]": [rule27,],
	"^": [rule36,],
	"_": [rule42,],
	"a": [rule42,],
	"b": [rule42,],
	"c": [rule42,],
	"d": [rule42,],
	"e": [rule42,],
	"f": [rule42,],
	"g": [rule42,],
	"h": [rule42,],
	"i": [rule42,],
	"j": [rule42,],
	"k": [rule42,],
	"l": [rule42,],
	"m": [rule42,],
	"n": [rule42,],
	"o": [rule42,],
	"p": [rule42,],
	"q": [rule42,],
	"r": [rule42,],
	"s": [rule42,],
	"t": [rule42,],
	"u": [rule42,],
	"v": [rule42,],
	"w": [rule42,],
	"x": [rule42,],
	"y": [rule42,],
	"z": [rule42,],
	"{": [rule21,],
	"|": [rule37,],
	"}": [rule22,],
	"~": [rule17,],
}

# Rules for csharp_doc_comment ruleset.

def rule43(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule44(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="xml::TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules dict for doc_comment ruleset.
rulesDict2 = {
	"<": [rule43,rule44,],
}

# x.rulesDictDict for csharp mode.
rulesDictDict = {
	"csharp_doc_comment": rulesDict2,
	"csharp_main": rulesDict1,
}

# Import dict for csharp mode.
importDict = {}

