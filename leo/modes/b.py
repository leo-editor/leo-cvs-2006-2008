# Leo colorizer control file for b mode.
# This file is in the public domain.

# Properties for b mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"indentNextLine": "\\s*(((ANY|ASSERT|CASE|CHOICE|IF|LET|PRE|SELECT|VAR|WHILE|WHEN)\\s*\\(|ELSE|ELSEIF|EITHER|OR|VARIANT|INVARIANT)[^;]*|for\\s*\\(.*)",
	"lineComment": "//",
}

# Keywords dict for b_main ruleset.
b_main_keywords_dict = {
	"ABSTRACT_CONSTANTS": "keyword2",
	"ABSTRACT_VARIABLES": "keyword2",
	"ANY": "keyword2",
	"ASSERT": "keyword2",
	"ASSERTIONS": "keyword2",
	"BE": "keyword2",
	"BEGIN": "keyword2",
	"CASE": "keyword2",
	"CHOICE": "keyword2",
	"CONCRETE_CONSTANTS": "keyword2",
	"CONCRETE_VARIABLES": "keyword2",
	"CONSTANTS": "keyword2",
	"CONSTRAINTS": "keyword2",
	"DEFINITIONS": "keyword2",
	"DO": "keyword2",
	"EITHER": "keyword2",
	"ELSE": "keyword2",
	"ELSIF": "keyword2",
	"END": "keyword2",
	"EXTENDS": "keyword2",
	"FIN": "keyword3",
	"FIN1": "keyword3",
	"IF": "keyword2",
	"IMPLEMENTATION": "keyword2",
	"IMPORTS": "keyword2",
	"IN": "keyword2",
	"INCLUDES": "keyword2",
	"INITIALISATION": "keyword2",
	"INT": "keyword3",
	"INTEGER": "keyword3",
	"INTER": "keyword3",
	"INVARIANT": "keyword2",
	"LET": "keyword2",
	"LOCAL_OPERATIONS": "keyword2",
	"MACHINE": "keyword2",
	"MAXINT": "keyword3",
	"MININT": "keyword3",
	"NAT": "keyword3",
	"NAT1": "keyword3",
	"NATURAL": "keyword3",
	"NATURAL1": "keyword3",
	"OF": "keyword2",
	"OPERATIONS": "keyword2",
	"OR": "keyword2",
	"PI": "keyword3",
	"POW": "keyword3",
	"POW1": "keyword3",
	"PRE": "keyword2",
	"PROMOTES": "keyword2",
	"PROPERTIES": "keyword2",
	"REFINEMENT": "keyword2",
	"REFINES": "keyword2",
	"SEES": "keyword2",
	"SELECT": "keyword2",
	"SETS": "keyword2",
	"SIGMA": "keyword3",
	"THEN": "keyword2",
	"UNION": "keyword3",
	"USES": "keyword2",
	"VALUES": "keyword2",
	"VAR": "keyword2",
	"VARIABLES": "keyword2",
	"VARIANT": "keyword2",
	"WHEN": "keyword2",
	"WHERE": "keyword2",
	"WHILE": "keyword2",
	"arity": "function",
	"bin": "function",
	"bool": "function",
	"btree": "function",
	"card": "function",
	"closure": "function",
	"closure1": "function",
	"conc": "function",
	"const": "function",
	"dom": "function",
	"father": "function",
	"first": "function",
	"fnc": "function",
	"front": "function",
	"id": "function",
	"infix": "function",
	"inter": "function",
	"iseq": "function",
	"iseq1": "function",
	"iterate": "function",
	"last": "function",
	"left": "function",
	"max": "function",
	"min": "function",
	"mirror": "function",
	"mod": "function",
	"not": "function",
	"or": "function",
	"perm": "function",
	"postfix": "function",
	"pred": "function",
	"prefix": "function",
	"prj1": "function",
	"prj2": "function",
	"ran": "function",
	"rank": "function",
	"rec": "function",
	"rel": "function",
	"rev": "function",
	"right": "function",
	"r~": "function",
	"seq": "function",
	"seq1": "function",
	"size": "function",
	"sizet": "function",
	"skip": "function",
	"son": "function",
	"sons": "function",
	"struct": "function",
	"subtree": "function",
	"succ": "function",
	"tail": "function",
	"top": "function",
	"tree": "function",
	"union": "function",
}

# Dictionary of keywords dictionaries for b mode.
keywordsDictDict = {
	"b_main": b_main_keywords_dict,
}

# Rules for b_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment3", begin="/*?", end="?*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
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
    return colorer.match_eol_span(s, i, kind="comment2", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="$0",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\\",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule31(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule5,],
	"\"": [rule2,],
	"#": [rule6,],
	"$": [rule7,],
	"%": [rule8,],
	"&": [rule10,],
	"'": [rule3,],
	"(": [rule25,],
	")": [rule26,],
	"*": [rule13,],
	"+": [rule14,],
	",": [rule24,],
	"-": [rule21,],
	".": [rule23,],
	"/": [rule0,rule1,rule4,rule15,],
	"0": [rule31,],
	"1": [rule31,],
	"2": [rule31,],
	"3": [rule31,],
	"4": [rule31,],
	"5": [rule31,],
	"6": [rule31,],
	"7": [rule31,],
	"8": [rule31,],
	"9": [rule31,],
	":": [rule18,],
	";": [rule19,],
	"<": [rule12,],
	"=": [rule9,],
	">": [rule11,],
	"@": [rule31,],
	"A": [rule31,],
	"B": [rule31,],
	"C": [rule31,],
	"D": [rule31,],
	"E": [rule31,],
	"F": [rule31,],
	"G": [rule31,],
	"H": [rule31,],
	"I": [rule31,],
	"J": [rule31,],
	"K": [rule31,],
	"L": [rule31,],
	"M": [rule31,],
	"N": [rule31,],
	"O": [rule31,],
	"P": [rule31,],
	"Q": [rule31,],
	"R": [rule31,],
	"S": [rule31,],
	"T": [rule31,],
	"U": [rule31,],
	"V": [rule31,],
	"W": [rule31,],
	"X": [rule31,],
	"Y": [rule31,],
	"Z": [rule31,],
	"[": [rule30,],
	"\\": [rule16,],
	"]": [rule29,],
	"^": [rule22,],
	"_": [rule31,],
	"a": [rule31,],
	"b": [rule31,],
	"c": [rule31,],
	"d": [rule31,],
	"e": [rule31,],
	"f": [rule31,],
	"g": [rule31,],
	"h": [rule31,],
	"i": [rule31,],
	"j": [rule31,],
	"k": [rule31,],
	"l": [rule31,],
	"m": [rule31,],
	"n": [rule31,],
	"o": [rule31,],
	"p": [rule31,],
	"q": [rule31,],
	"r": [rule31,],
	"s": [rule31,],
	"t": [rule31,],
	"u": [rule31,],
	"v": [rule31,],
	"w": [rule31,],
	"x": [rule31,],
	"y": [rule31,],
	"z": [rule31,],
	"{": [rule28,],
	"|": [rule20,],
	"}": [rule27,],
	"~": [rule17,],
}

# x.rulesDictDict for b mode.
rulesDictDict = {
	"b_main": rulesDict1,
}

# Import dict for b mode.
importDict = {}

