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
	"ABS": "literal2",
	"ADDRESS": "literal2",
	"ADR": "literal2",
	"ADRSIZE": "literal2",
	"AND": "keyword1",
	"ANY": "keyword1",
	"ARRAY": "keyword1",
	"AS": "keyword1",
	"BEGIN": "keyword1",
	"BITS": "keyword1",
	"BITSIZE": "literal2",
	"BOOLEAN": "literal2",
	"BRANDED": "keyword1",
	"BY": "keyword1",
	"BYTESIZE": "literal2",
	"CARDINAL": "literal2",
	"CASE": "keyword1",
	"CEILING": "literal2",
	"CHAR": "literal2",
	"CONST": "keyword1",
	"DEC": "literal2",
	"DISPOSE": "literal2",
	"DIV": "keyword1",
	"DO": "keyword1",
	"ELSE": "keyword1",
	"ELSIF": "keyword1",
	"END": "keyword1",
	"EVAL": "keyword1",
	"EXCEPT": "keyword1",
	"EXCEPTION": "keyword1",
	"EXIT": "keyword1",
	"EXPORTS": "keyword1",
	"EXTENDED": "literal2",
	"ExtendedFloat": "keyword2",
	"ExtendedReal": "keyword2",
	"FALSE": "literal2",
	"FINALLY": "keyword1",
	"FIRST": "literal2",
	"FLOAT": "literal2",
	"FLOOR": "literal2",
	"FOR": "keyword1",
	"FROM": "keyword1",
	"FloatMode": "keyword2",
	"Fmt": "keyword3",
	"GENERIC": "keyword1",
	"IF": "keyword1",
	"IMPORT": "keyword1",
	"IN": "keyword1",
	"INC": "literal2",
	"INTEGER": "literal2",
	"INTERFACE": "keyword1",
	"ISTYPE": "literal2",
	"LAST": "literal2",
	"LOCK": "keyword1",
	"LONGREAL": "literal2",
	"LOOP": "keyword1",
	"LOOPHOLE": "literal2",
	"Lex": "keyword3",
	"LongFloat": "keyword2",
	"LongReal": "keyword2",
	"MAX": "literal2",
	"METHODS": "keyword1",
	"MIN": "literal2",
	"MOD": "keyword1",
	"MODULE": "keyword1",
	"MUTEX": "literal2",
	"NARROW": "literal2",
	"NEW": "literal2",
	"NIL": "literal2",
	"NOT": "keyword1",
	"NULL": "literal2",
	"NUMBER": "literal2",
	"OBJECT": "keyword1",
	"OF": "keyword1",
	"OR": "keyword1",
	"ORD": "literal2",
	"OVERRIDES": "keyword1",
	"PROCEDURE": "keyword1",
	"Pickle": "keyword3",
	"RAISE": "keyword1",
	"RAISES": "keyword1",
	"READONLY": "keyword1",
	"REAL": "literal2",
	"RECORD": "keyword1",
	"REF": "keyword1",
	"REFANY": "literal2",
	"REPEAT": "keyword1",
	"RETURN": "keyword1",
	"REVEAL": "keyword1",
	"ROOT": "keyword1",
	"ROUND": "literal2",
	"Real": "keyword2",
	"RealFloat": "keyword2",
	"SET": "keyword1",
	"SUBARRAY": "literal2",
	"TEXT": "literal2",
	"THEN": "keyword1",
	"TO": "keyword1",
	"TRUE": "literal2",
	"TRUNC": "literal2",
	"TRY": "keyword1",
	"TYPE": "keyword1",
	"TYPECASE": "keyword1",
	"TYPECODE": "literal2",
	"Table": "keyword3",
	"Text": "keyword2",
	"Thread": "keyword2",
	"UNSAFE": "keyword1",
	"UNTIL": "keyword1",
	"UNTRACED": "keyword1",
	"VAL": "literal2",
	"VALUE": "keyword1",
	"VAR": "keyword1",
	"WHILE": "keyword1",
	"WITH": "keyword1",
	"Word": "keyword2",
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

# x.rulesDictDict for modula3 mode.
rulesDictDict = {
	"modula3_main": rulesDict1,
}

# Import dict for modula3 mode.
importDict = {}

