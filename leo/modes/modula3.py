# Leo colorizer control file for modula3 mode.
# This file is in the public domain.

# Properties for modula3 mode.
properties = {
	"commentEnd": "*)",
	"commentStart": "(*",
}

# Attributes dict for modula3_main ruleset.
modula3_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for modula3 mode.
attributesDictDict = {
	"modula3_main": modula3_main_attributes_dict,
}

# Keywords dict for modula3_main ruleset.
modula3_main_keywords_dict = {
	"abs": "literal2",
	"address": "literal2",
	"adr": "literal2",
	"adrsize": "literal2",
	"and": "keyword1",
	"any": "keyword1",
	"array": "keyword1",
	"as": "keyword1",
	"begin": "keyword1",
	"bits": "keyword1",
	"bitsize": "literal2",
	"boolean": "literal2",
	"branded": "keyword1",
	"by": "keyword1",
	"bytesize": "literal2",
	"cardinal": "literal2",
	"case": "keyword1",
	"ceiling": "literal2",
	"char": "literal2",
	"const": "keyword1",
	"dec": "literal2",
	"dispose": "literal2",
	"div": "keyword1",
	"do": "keyword1",
	"else": "keyword1",
	"elsif": "keyword1",
	"end": "keyword1",
	"eval": "keyword1",
	"except": "keyword1",
	"exception": "keyword1",
	"exit": "keyword1",
	"exports": "keyword1",
	"extended": "literal2",
	"extendedfloat": "keyword2",
	"extendedreal": "keyword2",
	"false": "literal2",
	"finally": "keyword1",
	"first": "literal2",
	"float": "literal2",
	"floatmode": "keyword2",
	"floor": "literal2",
	"fmt": "keyword3",
	"for": "keyword1",
	"from": "keyword1",
	"generic": "keyword1",
	"if": "keyword1",
	"import": "keyword1",
	"in": "keyword1",
	"inc": "literal2",
	"integer": "literal2",
	"interface": "keyword1",
	"istype": "literal2",
	"last": "literal2",
	"lex": "keyword3",
	"lock": "keyword1",
	"longfloat": "keyword2",
	"longreal": "literal2",
	"loop": "keyword1",
	"loophole": "literal2",
	"max": "literal2",
	"methods": "keyword1",
	"min": "literal2",
	"mod": "keyword1",
	"module": "keyword1",
	"mutex": "literal2",
	"narrow": "literal2",
	"new": "literal2",
	"nil": "literal2",
	"not": "keyword1",
	"null": "literal2",
	"number": "literal2",
	"object": "keyword1",
	"of": "keyword1",
	"or": "keyword1",
	"ord": "literal2",
	"overrides": "keyword1",
	"pickle": "keyword3",
	"procedure": "keyword1",
	"raise": "keyword1",
	"raises": "keyword1",
	"readonly": "keyword1",
	"real": "keyword2",
	"realfloat": "keyword2",
	"record": "keyword1",
	"ref": "keyword1",
	"refany": "literal2",
	"repeat": "keyword1",
	"return": "keyword1",
	"reveal": "keyword1",
	"root": "keyword1",
	"round": "literal2",
	"set": "keyword1",
	"subarray": "literal2",
	"table": "keyword3",
	"text": "keyword2",
	"then": "keyword1",
	"thread": "keyword2",
	"to": "keyword1",
	"true": "literal2",
	"trunc": "literal2",
	"try": "keyword1",
	"type": "keyword1",
	"typecase": "keyword1",
	"typecode": "literal2",
	"unsafe": "keyword1",
	"until": "keyword1",
	"untraced": "keyword1",
	"val": "literal2",
	"value": "keyword1",
	"var": "keyword1",
	"while": "keyword1",
	"with": "keyword1",
	"word": "keyword2",
}

# Dictionary of keywords dictionaries for modula3 mode.
keywordsDictDict = {
	"modula3_main": modula3_main_keywords_dict,
}

# Rules for modula3_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment2", begin="<*", end="*>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="(*", end="*)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"\"": [rule2,],
	"'": [rule3,],
	"(": [rule1,],
	"*": [rule16,],
	"+": [rule13,],
	"-": [rule14,],
	"/": [rule15,],
	"0": [rule17,],
	"1": [rule17,],
	"2": [rule17,],
	"3": [rule17,],
	"4": [rule17,],
	"5": [rule17,],
	"6": [rule17,],
	"7": [rule17,],
	"8": [rule17,],
	"9": [rule17,],
	":": [rule6,],
	"<": [rule0,rule8,rule10,rule12,],
	"=": [rule7,],
	">": [rule9,rule11,],
	"@": [rule5,rule17,],
	"A": [rule17,],
	"B": [rule17,],
	"C": [rule17,],
	"D": [rule17,],
	"E": [rule17,],
	"F": [rule17,],
	"G": [rule17,],
	"H": [rule17,],
	"I": [rule17,],
	"J": [rule17,],
	"K": [rule17,],
	"L": [rule17,],
	"M": [rule17,],
	"N": [rule17,],
	"O": [rule17,],
	"P": [rule17,],
	"Q": [rule17,],
	"R": [rule17,],
	"S": [rule17,],
	"T": [rule17,],
	"U": [rule17,],
	"V": [rule17,],
	"W": [rule17,],
	"X": [rule17,],
	"Y": [rule17,],
	"Z": [rule17,],
	"^": [rule4,],
	"a": [rule17,],
	"b": [rule17,],
	"c": [rule17,],
	"d": [rule17,],
	"e": [rule17,],
	"f": [rule17,],
	"g": [rule17,],
	"h": [rule17,],
	"i": [rule17,],
	"j": [rule17,],
	"k": [rule17,],
	"l": [rule17,],
	"m": [rule17,],
	"n": [rule17,],
	"o": [rule17,],
	"p": [rule17,],
	"q": [rule17,],
	"r": [rule17,],
	"s": [rule17,],
	"t": [rule17,],
	"u": [rule17,],
	"v": [rule17,],
	"w": [rule17,],
	"x": [rule17,],
	"y": [rule17,],
	"z": [rule17,],
}

# x.rulesDictDict for modula3 mode.
rulesDictDict = {
	"modula3_main": rulesDict1,
}

# Import dict for modula3 mode.
importDict = {}

