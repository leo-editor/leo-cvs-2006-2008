# Leo colorizer control file for prolog mode.
# This file is in the public domain.

# Properties for prolog mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"lineComment": "%",
}

# Attributes dict for prolog_main ruleset.
prolog_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Attributes dict for prolog_list ruleset.
prolog_list_attributes_dict = {
	"default": "LITERAL2",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for prolog mode.
attributesDictDict = {
	"prolog_list": prolog_list_attributes_dict,
	"prolog_main": prolog_main_attributes_dict,
}

# Keywords dict for prolog_main ruleset.
prolog_main_keywords_dict = {
	"!": "keyword1",
	"_": "keyword3",
	"abolish": "function",
	"arg": "function",
	"asserta": "function",
	"assertz": "function",
	"at_end_of_stream": "function",
	"atan": "function",
	"atom": "function",
	"atom_chars": "function",
	"atom_codes": "function",
	"atom_concat": "function",
	"atom_length": "function",
	"atomic": "function",
	"bagof": "function",
	"call": "function",
	"catch": "function",
	"char_code": "function",
	"char_conversion": "function",
	"clause": "function",
	"close": "function",
	"compound": "function",
	"copy_term": "function",
	"cos": "function",
	"current_char_conversion": "function",
	"current_input": "function",
	"current_op": "function",
	"current_output": "function",
	"current_predicate": "function",
	"current_prolog_flag": "function",
	"exp": "function",
	"fail": "keyword1",
	"findall": "function",
	"float": "function",
	"functor": "function",
	"get_byte": "function",
	"get_char": "function",
	"get_code": "function",
	"halt": "function",
	"integer": "function",
	"is": "keyword2",
	"log": "function",
	"mod": "keyword2",
	"nl": "function",
	"nonvar": "function",
	"number": "function",
	"number_chars": "function",
	"number_codes": "function",
	"once": "function",
	"op": "function",
	"open": "function",
	"peek_byte": "function",
	"peek_char": "function",
	"peek_code": "function",
	"put_byte": "function",
	"put_char": "function",
	"put_code": "function",
	"read": "function",
	"read_term": "function",
	"rem": "keyword2",
	"repeat": "keyword1",
	"retract": "function",
	"set_input": "function",
	"set_output": "function",
	"set_prolog_flag": "function",
	"set_stream_position": "function",
	"setof": "function",
	"sin": "function",
	"sqrt": "function",
	"stream_property": "function",
	"sub_atom": "function",
	"throw": "function",
	"true": "keyword1",
	"unify_with_occurs_check": "function",
	"var": "function",
	"write": "function",
	"write_canonical": "function",
	"write_term": "function",
	"writeq": "function",
}

# Keywords dict for prolog_list ruleset.
prolog_list_keywords_dict = {}

# Dictionary of keywords dictionaries for prolog mode.
keywordsDictDict = {
	"prolog_list": prolog_list_keywords_dict,
	"prolog_main": prolog_main_keywords_dict,
}

# Rules for prolog_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

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
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="[", end="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="LIST",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="?-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\\+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="==",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\\==",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\\=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@=<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@>=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=..",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=:=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=\\=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/\\",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\\/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule31(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule32(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule33(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="**",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule34(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule35(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\\",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule36(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule37(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule38(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule39(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule40(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule41(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule42(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule43(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule44(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule44,],
	"\"": [rule3,],
	"%": [rule0,],
	"'": [rule2,],
	"(": [rule40,],
	")": [rule41,],
	"*": [rule33,rule38,],
	"+": [rule24,],
	",": [rule10,],
	"-": [rule5,rule9,rule25,],
	".": [rule39,],
	"/": [rule1,rule26,rule28,rule36,],
	"0": [rule44,],
	"1": [rule44,],
	"2": [rule44,],
	"3": [rule44,],
	"4": [rule44,],
	"5": [rule44,],
	"6": [rule44,],
	"7": [rule44,],
	"8": [rule44,],
	"9": [rule44,],
	":": [rule6,],
	";": [rule8,],
	"<": [rule29,rule30,],
	"=": [rule12,rule19,rule20,rule21,rule22,rule37,],
	">": [rule23,rule31,rule32,],
	"?": [rule7,],
	"@": [rule15,rule16,rule17,rule18,rule44,],
	"A": [rule44,],
	"B": [rule44,],
	"C": [rule44,],
	"D": [rule44,],
	"E": [rule44,],
	"F": [rule44,],
	"G": [rule44,],
	"H": [rule44,],
	"I": [rule44,],
	"J": [rule44,],
	"K": [rule44,],
	"L": [rule44,],
	"M": [rule44,],
	"N": [rule44,],
	"O": [rule44,],
	"P": [rule44,],
	"Q": [rule44,],
	"R": [rule44,],
	"S": [rule44,],
	"T": [rule44,],
	"U": [rule44,],
	"V": [rule44,],
	"W": [rule44,],
	"X": [rule44,],
	"Y": [rule44,],
	"Z": [rule44,],
	"[": [rule4,],
	"\\": [rule11,rule13,rule14,rule27,rule35,],
	"^": [rule34,],
	"_": [rule44,],
	"a": [rule44,],
	"b": [rule44,],
	"c": [rule44,],
	"d": [rule44,],
	"e": [rule44,],
	"f": [rule44,],
	"g": [rule44,],
	"h": [rule44,],
	"i": [rule44,],
	"j": [rule44,],
	"k": [rule44,],
	"l": [rule44,],
	"m": [rule44,],
	"n": [rule44,],
	"o": [rule44,],
	"p": [rule44,],
	"q": [rule44,],
	"r": [rule44,],
	"s": [rule44,],
	"t": [rule44,],
	"u": [rule44,],
	"v": [rule44,],
	"w": [rule44,],
	"x": [rule44,],
	"y": [rule44,],
	"z": [rule44,],
	"{": [rule42,],
	"}": [rule43,],
}

# Rules for prolog_list ruleset.

def rule45(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="[", end="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="LIST",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

# Rules dict for list ruleset.
rulesDict2 = {
	"[": [rule45,],
}

# x.rulesDictDict for prolog mode.
rulesDictDict = {
	"prolog_list": rulesDict2,
	"prolog_main": rulesDict1,
}

# Import dict for prolog mode.
importDict = {}

