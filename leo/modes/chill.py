# Leo colorizer control file for chill mode.
# This file is in the public domain.

# Properties for chill mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
}

# Attributes dict for chill_main ruleset.
chill_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for chill mode.
attributesDictDict = {
	"chill_main": chill_main_attributes_dict,
}

# Keywords dict for chill_main ruleset.
chill_main_keywords_dict = {
	"and": "keyword1",
	"array": "keyword2",
	"begin": "keyword1",
	"bin": "keyword3",
	"bool": "keyword3",
	"case": "keyword1",
	"char": "keyword3",
	"dcl": "keyword2",
	"div": "keyword1",
	"do": "keyword1",
	"eject": "label",
	"else": "keyword1",
	"elsif": "keyword1",
	"end": "keyword1",
	"esac": "keyword1",
	"exit": "keyword1",
	"false": "literal2",
	"fi": "keyword1",
	"for": "keyword1",
	"goto": "keyword1",
	"grant": "keyword2",
	"if": "keyword1",
	"in": "keyword1",
	"int": "keyword3",
	"label": "keyword2",
	"lio_infos": "label",
	"mod": "keyword1",
	"module": "keyword2",
	"module_description_header": "label",
	"msg_xref": "label",
	"newmode": "keyword2",
	"not": "keyword1",
	"null": "literal2",
	"od": "keyword1",
	"of": "keyword1",
	"on": "keyword1",
	"or": "keyword1",
	"out": "keyword1",
	"pack": "keyword2",
	"patch_infos": "label",
	"powerset": "keyword2",
	"proc": "keyword2",
	"ptr": "keyword3",
	"range": "keyword3",
	"ref": "keyword3",
	"result": "keyword1",
	"return": "keyword1",
	"seize": "keyword2",
	"set": "keyword2",
	"struct": "keyword2",
	"swsg_infos": "label",
	"syn": "keyword2",
	"synmode": "keyword2",
	"then": "keyword1",
	"to": "keyword1",
	"true": "literal2",
	"type": "keyword2",
	"until": "keyword1",
	"uses": "keyword1",
	"while": "keyword1",
	"with": "keyword1",
	"xor": "keyword1",
}

# Dictionary of keywords dictionaries for chill mode.
keywordsDictDict = {
	"chill_main": chill_main_keywords_dict,
}

# Rules for chill_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment2", begin="<>", end="<>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="H'", end=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"'": [rule2,],
	"(": [rule5,],
	")": [rule4,],
	"*": [rule11,],
	"+": [rule8,],
	",": [rule13,],
	"-": [rule9,],
	".": [rule12,],
	"/": [rule1,rule10,rule20,],
	"0": [rule25,],
	"1": [rule25,],
	"2": [rule25,],
	"3": [rule25,],
	"4": [rule25,],
	"5": [rule25,],
	"6": [rule25,],
	"7": [rule25,],
	"8": [rule25,],
	"9": [rule25,],
	":": [rule17,rule18,],
	";": [rule14,],
	"<": [rule0,rule22,rule24,],
	"=": [rule19,],
	">": [rule21,rule23,],
	"@": [rule16,rule25,],
	"A": [rule25,],
	"B": [rule25,],
	"C": [rule25,],
	"D": [rule25,],
	"E": [rule25,],
	"F": [rule25,],
	"G": [rule25,],
	"H": [rule3,rule25,],
	"I": [rule25,],
	"J": [rule25,],
	"K": [rule25,],
	"L": [rule25,],
	"M": [rule25,],
	"N": [rule25,],
	"O": [rule25,],
	"P": [rule25,],
	"Q": [rule25,],
	"R": [rule25,],
	"S": [rule25,],
	"T": [rule25,],
	"U": [rule25,],
	"V": [rule25,],
	"W": [rule25,],
	"X": [rule25,],
	"Y": [rule25,],
	"Z": [rule25,],
	"[": [rule7,],
	"]": [rule6,],
	"^": [rule15,],
	"_": [rule25,],
	"a": [rule25,],
	"b": [rule25,],
	"c": [rule25,],
	"d": [rule25,],
	"e": [rule25,],
	"f": [rule25,],
	"g": [rule25,],
	"h": [rule25,],
	"i": [rule25,],
	"j": [rule25,],
	"k": [rule25,],
	"l": [rule25,],
	"m": [rule25,],
	"n": [rule25,],
	"o": [rule25,],
	"p": [rule25,],
	"q": [rule25,],
	"r": [rule25,],
	"s": [rule25,],
	"t": [rule25,],
	"u": [rule25,],
	"v": [rule25,],
	"w": [rule25,],
	"x": [rule25,],
	"y": [rule25,],
	"z": [rule25,],
}

# x.rulesDictDict for chill mode.
rulesDictDict = {
	"chill_main": rulesDict1,
}

# Import dict for chill mode.
importDict = {}

