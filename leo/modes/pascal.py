# Leo colorizer control file for pascal mode.
# This file is in the public domain.

# Properties for pascal mode.
properties = {
	"commentEnd": "}",
	"commentStart": "{",
	"lineComment": "//",
}

# Attributes dict for pascal_main ruleset.
pascal_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for pascal mode.
attributesDictDict = {
	"pascal_main": pascal_main_attributes_dict,
}

# Keywords dict for pascal_main ruleset.
pascal_main_keywords_dict = {
	"absolute": "keyword2",
	"abstract": "keyword2",
	"and": "keyword1",
	"array": "keyword1",
	"as": "keyword1",
	"asm": "keyword1",
	"assembler": "keyword2",
	"at": "keyword1",
	"automated": "keyword2",
	"begin": "keyword1",
	"boolean": "keyword3",
	"byte": "keyword3",
	"bytebool": "keyword3",
	"cardinal": "keyword3",
	"case": "keyword1",
	"cdecl": "keyword2",
	"char": "keyword3",
	"class": "keyword1",
	"comp": "keyword3",
	"const": "keyword1",
	"constructor": "keyword1",
	"contains": "keyword2",
	"currency": "keyword3",
	"default": "keyword2",
	"deprecated": "keyword2",
	"destructor": "keyword1",
	"dispid": "keyword2",
	"dispinterface": "keyword1",
	"div": "keyword1",
	"do": "keyword1",
	"double": "keyword3",
	"downto": "keyword1",
	"dynamic": "keyword2",
	"else": "keyword1",
	"end": "keyword1",
	"except": "keyword1",
	"export": "keyword2",
	"exports": "keyword1",
	"extended": "keyword3",
	"external": "keyword2",
	"false": "literal2",
	"far": "keyword2",
	"file": "keyword1",
	"final": "keyword1",
	"finalization": "keyword1",
	"finally": "keyword1",
	"for": "keyword1",
	"forward": "keyword2",
	"function": "keyword1",
	"goto": "keyword1",
	"if": "keyword1",
	"implementation": "keyword1",
	"implements": "keyword2",
	"in": "keyword1",
	"index": "keyword2",
	"inherited": "keyword1",
	"initialization": "keyword1",
	"inline": "keyword1",
	"integer": "keyword3",
	"interface": "keyword1",
	"is": "keyword1",
	"label": "keyword1",
	"library": "keyword2",
	"local": "keyword2",
	"longbool": "keyword3",
	"longint": "keyword3",
	"message": "keyword2",
	"mod": "keyword1",
	"name": "keyword2",
	"namespaces": "keyword2",
	"near": "keyword2",
	"nil": "literal2",
	"nodefault": "keyword2",
	"not": "keyword1",
	"object": "keyword1",
	"of": "keyword1",
	"on": "keyword1",
	"or": "keyword1",
	"out": "keyword1",
	"overload": "keyword2",
	"override": "keyword2",
	"package": "keyword2",
	"packed": "keyword1",
	"pascal": "keyword2",
	"platform": "keyword2",
	"pointer": "keyword3",
	"private": "keyword2",
	"procedure": "keyword1",
	"program": "keyword1",
	"property": "keyword1",
	"protected": "keyword2",
	"public": "keyword2",
	"published": "keyword2",
	"raise": "keyword1",
	"read": "keyword2",
	"readonly": "keyword2",
	"real": "keyword3",
	"record": "keyword1",
	"register": "keyword2",
	"reintroduce": "keyword2",
	"repeat": "keyword1",
	"requires": "keyword2",
	"resident": "keyword2",
	"resourcestring": "keyword1",
	"safecall": "keyword2",
	"sealed": "keyword1",
	"self": "literal2",
	"set": "keyword1",
	"shl": "keyword1",
	"shortint": "keyword3",
	"shr": "keyword1",
	"single": "keyword3",
	"smallint": "keyword3",
	"static": "keyword1",
	"stdcall": "keyword2",
	"stored": "keyword2",
	"string": "keyword1",
	"then": "keyword1",
	"threadvar": "keyword1",
	"to": "keyword1",
	"true": "literal2",
	"try": "keyword1",
	"type": "keyword1",
	"unit": "keyword1",
	"unsafe": "keyword1",
	"until": "keyword1",
	"uses": "keyword1",
	"var": "keyword1",
	"varargs": "keyword2",
	"virtual": "keyword2",
	"while": "keyword1",
	"with": "keyword1",
	"word": "keyword3",
	"wordbool": "keyword3",
	"write": "keyword2",
	"writeonly": "keyword2",
	"xor": "keyword1",
}

# Dictionary of keywords dictionaries for pascal mode.
keywordsDictDict = {
	"pascal_main": pascal_main_keywords_dict,
}

# Rules for pascal_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment3", begin="{$", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment3", begin="(*$", end="*)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="{", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="(*", end="*)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"'": [rule5,],
	"(": [rule1,rule3,rule7,],
	")": [rule6,],
	"*": [rule26,],
	"+": [rule23,],
	",": [rule11,],
	"-": [rule24,],
	".": [rule10,],
	"/": [rule4,rule25,],
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
	":": [rule15,rule16,],
	";": [rule12,],
	"<": [rule18,rule20,rule22,],
	"=": [rule17,],
	">": [rule19,rule21,],
	"@": [rule14,rule27,],
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
	"[": [rule9,],
	"]": [rule8,],
	"^": [rule13,],
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
	"{": [rule0,rule2,],
}

# x.rulesDictDict for pascal mode.
rulesDictDict = {
	"pascal_main": rulesDict1,
}

# Import dict for pascal mode.
importDict = {}

