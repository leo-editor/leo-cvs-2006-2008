# Leo colorizer control file for awk mode.
# This file is in the public domain.

# Properties for awk mode.
properties = {
	"indentCloseBrackets": "}",
	"indentOpenBrackets": "{",
	"lineComment": "#",
	"lineUpClosingBracket": "true",
	"wordBreakChars": ",+-=<>/?^&*",
}

# Keywords dict for awk_main ruleset.
awk_main_keywords_dict = {
	"$0": "keyword3",
	"ARGC": "keyword3",
	"ARGIND": "keyword3",
	"ARGV": "keyword3",
	"BEGIN": "keyword3",
	"CONVFMT": "keyword3",
	"END": "keyword3",
	"ENVIRON": "keyword3",
	"ERRNO": "keyword3",
	"FIELDSWIDTH": "keyword3",
	"FILENAME": "keyword3",
	"FNR": "keyword3",
	"FS": "keyword3",
	"IGNORECASE": "keyword3",
	"NF": "keyword3",
	"NR": "keyword3",
	"OFMT": "keyword3",
	"OFS": "keyword3",
	"ORS": "keyword3",
	"RLENGTH": "keyword3",
	"RS": "keyword3",
	"RSTART": "keyword3",
	"RT": "keyword3",
	"SUBSEP": "keyword3",
	"atan2": "keyword2",
	"break": "keyword1",
	"close": "keyword1",
	"continue": "keyword1",
	"cos": "keyword2",
	"delete": "keyword1",
	"do": "keyword1",
	"else": "keyword1",
	"exit": "keyword1",
	"exp": "keyword2",
	"fflush": "keyword1",
	"for": "keyword1",
	"function": "keyword1",
	"gensub": "keyword2",
	"getline": "keyword2",
	"gsub": "keyword2",
	"huge": "keyword1",
	"if": "keyword1",
	"in": "keyword1",
	"index": "keyword2",
	"int": "keyword2",
	"length": "keyword2",
	"log": "keyword2",
	"match": "keyword2",
	"next": "keyword1",
	"nextfile": "keyword1",
	"print": "keyword1",
	"printf": "keyword1",
	"rand": "keyword2",
	"return": "keyword1",
	"sin": "keyword2",
	"split": "keyword2",
	"sprintf": "keyword2",
	"sqrt": "keyword2",
	"srand": "keyword2",
	"sub": "keyword2",
	"substr": "keyword2",
	"system": "keyword2",
	"tolower": "keyword2",
	"toupper": "keyword2",
	"while": "keyword1",
}

# Dictionary of keywords dictionaries for awk mode.
keywordsDictDict = {
	"awk_main": awk_main_keywords_dict,
}

# Rules for awk_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=False, at_whitespace_end=True, at_word_start=False, exclude_match=True)

def rule21(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule4,],
	"\"": [rule0,],
	"#": [rule2,],
	"%": [rule13,],
	"&": [rule14,],
	"'": [rule1,],
	"*": [rule10,],
	"+": [rule7,],
	"-": [rule8,],
	"/": [rule9,],
	"0": [rule21,],
	"1": [rule21,],
	"2": [rule21,],
	"3": [rule21,],
	"4": [rule21,],
	"5": [rule21,],
	"6": [rule21,],
	"7": [rule21,],
	"8": [rule21,],
	"9": [rule21,],
	":": [rule20,],
	"<": [rule6,rule12,],
	"=": [rule3,],
	">": [rule5,rule11,],
	"@": [rule21,],
	"A": [rule21,],
	"B": [rule21,],
	"C": [rule21,],
	"D": [rule21,],
	"E": [rule21,],
	"F": [rule21,],
	"G": [rule21,],
	"H": [rule21,],
	"I": [rule21,],
	"J": [rule21,],
	"K": [rule21,],
	"L": [rule21,],
	"M": [rule21,],
	"N": [rule21,],
	"O": [rule21,],
	"P": [rule21,],
	"Q": [rule21,],
	"R": [rule21,],
	"S": [rule21,],
	"T": [rule21,],
	"U": [rule21,],
	"V": [rule21,],
	"W": [rule21,],
	"X": [rule21,],
	"Y": [rule21,],
	"Z": [rule21,],
	"^": [rule16,],
	"_": [rule21,],
	"a": [rule21,],
	"b": [rule21,],
	"c": [rule21,],
	"d": [rule21,],
	"e": [rule21,],
	"f": [rule21,],
	"g": [rule21,],
	"h": [rule21,],
	"i": [rule21,],
	"j": [rule21,],
	"k": [rule21,],
	"l": [rule21,],
	"m": [rule21,],
	"n": [rule21,],
	"o": [rule21,],
	"p": [rule21,],
	"q": [rule21,],
	"r": [rule21,],
	"s": [rule21,],
	"t": [rule21,],
	"u": [rule21,],
	"v": [rule21,],
	"w": [rule21,],
	"x": [rule21,],
	"y": [rule21,],
	"z": [rule21,],
	"{": [rule19,],
	"|": [rule15,],
	"}": [rule18,],
	"~": [rule17,],
}

# x.rulesDictDict for awk mode.
rulesDictDict = {
	"awk_main": rulesDict1,
}

# Import dict for awk mode.
importDict = {}

