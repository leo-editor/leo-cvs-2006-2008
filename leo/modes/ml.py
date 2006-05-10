# Leo colorizer control file for ml mode.
# This file is in the public domain.

# Properties for ml mode.
properties = {
	"commentEnd": "*)",
	"commentStart": "(*",
}

# Attributes dict for ml_main ruleset.
ml_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for ml mode.
attributesDictDict = {
	"ml_main": ml_main_attributes_dict,
}

# Keywords dict for ml_main ruleset.
ml_main_keywords_dict = {
	"ANTIQUOTE": "literal2",
	"Bind": "keyword2",
	"Chr": "keyword2",
	"Div": "keyword2",
	"Domain": "keyword2",
	"EQUAL": "literal2",
	"Fail": "keyword2",
	"GREATER": "literal2",
	"Graphic": "keyword2",
	"Interrupt": "keyword2",
	"Io": "keyword2",
	"LESS": "literal2",
	"Match": "keyword2",
	"NONE": "literal2",
	"Option": "keyword2",
	"Ord": "keyword2",
	"Overflow": "keyword2",
	"QUOTE": "literal2",
	"SOME": "literal2",
	"Size": "keyword2",
	"Subscript": "keyword2",
	"SysErr": "keyword2",
	"abstype": "keyword1",
	"and": "keyword1",
	"andalso": "keyword1",
	"array": "keyword3",
	"as": "keyword1",
	"before": "operator",
	"bool": "keyword3",
	"case": "keyword1",
	"char": "keyword3",
	"datatype": "keyword1",
	"div": "operator",
	"do": "keyword1",
	"else": "keyword1",
	"end": "keyword1",
	"eqtype": "keyword1",
	"exception": "keyword1",
	"exn": "keyword3",
	"false": "literal2",
	"fn": "keyword1",
	"frag": "keyword3",
	"fun": "keyword1",
	"functor": "keyword1",
	"handle": "keyword1",
	"if": "keyword1",
	"in": "keyword1",
	"include": "keyword1",
	"infix": "keyword1",
	"infixr": "keyword1",
	"int": "keyword3",
	"let": "keyword1",
	"list": "keyword3",
	"local": "keyword1",
	"mod": "operator",
	"nil": "literal2",
	"nonfix": "keyword1",
	"o": "operator",
	"of": "keyword1",
	"op": "keyword1",
	"open": "keyword1",
	"option": "keyword3",
	"order": "keyword3",
	"orelse": "keyword1",
	"raise": "keyword1",
	"real": "keyword3",
	"rec": "keyword1",
	"ref": "keyword3",
	"sharing": "keyword1",
	"sig": "keyword1",
	"signature": "keyword1",
	"string": "keyword3",
	"struct": "keyword1",
	"structure": "keyword1",
	"substring": "keyword3",
	"then": "keyword1",
	"true": "literal2",
	"type": "keyword1",
	"unit": "keyword3",
	"val": "keyword1",
	"vector": "keyword3",
	"where": "keyword1",
	"while": "keyword1",
	"with": "keyword1",
	"withtype": "keyword1",
	"word": "keyword3",
	"word8": "keyword3",
}

# Dictionary of keywords dictionaries for ml mode.
keywordsDictDict = {
	"ml_main": ml_main_keywords_dict,
}

# Rules for ml_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="(*", end="*)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="#\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="::",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"\"": [rule2,],
	"#": [rule1,],
	"(": [rule0,],
	"*": [rule4,],
	"+": [rule5,],
	"-": [rule6,],
	"/": [rule3,],
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
	":": [rule8,rule16,],
	"<": [rule11,rule12,rule13,],
	"=": [rule10,],
	">": [rule14,rule15,],
	"@": [rule9,rule17,],
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
	"^": [rule7,],
	"_": [rule17,],
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

# x.rulesDictDict for ml mode.
rulesDictDict = {
	"ml_main": rulesDict1,
}

# Import dict for ml mode.
importDict = {}

