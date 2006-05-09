# Leo colorizer control file for vhdl mode.
# This file is in the public domain.

# Properties for vhdl mode.
properties = {
	"label": "VHDL",
	"lineComment": "--",
}

# Keywords dict for vhdl_main ruleset.
vhdl_main_keywords_dict = {
	"ACTIVE": "keyword3",
	"ASCENDING": "keyword3",
	"BASE": "keyword3",
	"DELAYED": "keyword3",
	"DRIVING": "keyword3",
	"EVENT": "keyword3",
	"HIGH": "keyword3",
	"IMAGE": "keyword3",
	"INSTANCE": "keyword3",
	"LAST": "keyword3",
	"LEFT": "keyword3",
	"LEFTOF": "keyword3",
	"LENGTH": "keyword3",
	"LOW": "keyword3",
	"PATH": "keyword3",
	"POS": "keyword3",
	"PRED": "keyword3",
	"QUIET": "keyword3",
	"RANGE": "keyword3",
	"REVERSE": "keyword3",
	"RIGHT": "keyword3",
	"RIGHTOF": "keyword3",
	"SIMPLE": "keyword3",
	"STABLE": "keyword3",
	"SUCC": "keyword3",
	"TRANSACTION": "keyword3",
	"VAL": "keyword3",
	"VALUE": "keyword3",
	"abs": "operator",
	"alias": "keyword1",
	"all": "keyword1",
	"and": "operator",
	"architecture": "keyword1",
	"array": "keyword1",
	"assert": "keyword1",
	"begin": "keyword1",
	"bit": "keyword2",
	"bit_vector": "keyword2",
	"break": "keyword1",
	"case": "keyword1",
	"catch": "keyword1",
	"component": "keyword1",
	"constant": "keyword1",
	"continue": "keyword1",
	"default": "keyword1",
	"do": "keyword1",
	"downto": "keyword1",
	"else": "keyword1",
	"elsif": "keyword1",
	"end": "keyword1",
	"entity": "keyword1",
	"extends": "keyword1",
	"false": "literal2",
	"for": "keyword1",
	"function": "keyword1",
	"generic": "keyword1",
	"if": "keyword1",
	"implements": "keyword1",
	"import": "keyword2",
	"in": "keyword1",
	"inout": "keyword1",
	"instanceof": "keyword1",
	"integer": "keyword2",
	"is": "keyword1",
	"library": "keyword1",
	"loop": "keyword1",
	"mod": "operator",
	"nand": "operator",
	"natural": "keyword2",
	"nor": "operator",
	"not": "operator",
	"of": "keyword1",
	"or": "operator",
	"others": "keyword1",
	"out": "keyword1",
	"package": "keyword2",
	"port": "keyword1",
	"process": "keyword1",
	"range": "keyword1",
	"record": "keyword1",
	"rem": "operator",
	"resize": "function",
	"return": "keyword1",
	"rising_edge": "function",
	"rol": "operator",
	"ror": "operator",
	"rotate_left": "function",
	"rotate_right": "function",
	"shift_left": "function",
	"shift_right": "function",
	"signal": "keyword1",
	"signed": "function",
	"sla": "operator",
	"sll": "operator",
	"sra": "operator",
	"srl": "operator",
	"static": "keyword1",
	"std_logic": "keyword2",
	"std_logic_vector": "keyword2",
	"std_match": "function",
	"std_ulogic": "keyword2",
	"std_ulogic_vector": "keyword2",
	"switch": "keyword1",
	"then": "keyword1",
	"to": "keyword1",
	"to_bit": "function",
	"to_bitvector": "function",
	"to_integer": "function",
	"to_signed": "function",
	"to_stdlogicvector": "function",
	"to_stdulogic": "function",
	"to_stdulogicvector": "function",
	"to_unsigned": "function",
	"true": "literal2",
	"type": "keyword1",
	"unsigned": "function",
	"upto": "keyword1",
	"use": "keyword1",
	"variable": "keyword1",
	"wait": "keyword1",
	"when": "keyword1",
	"while": "keyword1",
	"xnor": "operator",
}

# Dictionary of keywords dictionaries for vhdl mode.
keywordsDictDict = {
	"vhdl_main": vhdl_main_keywords_dict,
}

# Rules for vhdl_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq="'event",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="--",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
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
    return colorer.match_seq(s, i, kind="operator", seq="**",
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
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule23(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule6,],
	"\"": [rule0,],
	"%": [rule17,],
	"&": [rule18,],
	"'": [rule1,rule2,],
	"*": [rule15,rule16,],
	"+": [rule12,],
	"-": [rule3,rule13,],
	"/": [rule5,rule14,],
	"0": [rule23,],
	"1": [rule23,],
	"2": [rule23,],
	"3": [rule23,],
	"4": [rule23,],
	"5": [rule23,],
	"6": [rule23,],
	"7": [rule23,],
	"8": [rule23,],
	"9": [rule23,],
	":": [rule7,rule22,],
	"<": [rule10,rule11,],
	"=": [rule4,],
	">": [rule8,rule9,],
	"@": [rule23,],
	"A": [rule23,],
	"B": [rule23,],
	"C": [rule23,],
	"D": [rule23,],
	"E": [rule23,],
	"F": [rule23,],
	"G": [rule23,],
	"H": [rule23,],
	"I": [rule23,],
	"J": [rule23,],
	"K": [rule23,],
	"L": [rule23,],
	"M": [rule23,],
	"N": [rule23,],
	"O": [rule23,],
	"P": [rule23,],
	"Q": [rule23,],
	"R": [rule23,],
	"S": [rule23,],
	"T": [rule23,],
	"U": [rule23,],
	"V": [rule23,],
	"W": [rule23,],
	"X": [rule23,],
	"Y": [rule23,],
	"Z": [rule23,],
	"^": [rule20,],
	"_": [rule23,],
	"a": [rule23,],
	"b": [rule23,],
	"c": [rule23,],
	"d": [rule23,],
	"e": [rule23,],
	"f": [rule23,],
	"g": [rule23,],
	"h": [rule23,],
	"i": [rule23,],
	"j": [rule23,],
	"k": [rule23,],
	"l": [rule23,],
	"m": [rule23,],
	"n": [rule23,],
	"o": [rule23,],
	"p": [rule23,],
	"q": [rule23,],
	"r": [rule23,],
	"s": [rule23,],
	"t": [rule23,],
	"u": [rule23,],
	"v": [rule23,],
	"w": [rule23,],
	"x": [rule23,],
	"y": [rule23,],
	"z": [rule23,],
	"|": [rule19,],
	"~": [rule21,],
}

# x.rulesDictDict for vhdl mode.
rulesDictDict = {
	"vhdl_main": rulesDict1,
}

# Import dict for vhdl mode.
importDict = {}

