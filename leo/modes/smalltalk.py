# Leo colorizer control file for smalltalk mode.
# This file is in the public domain.

# Properties for smalltalk mode.
properties = {
	"commentEnd": "\"",
	"commentStart": "\"",
	"indentCloseBrackets": "]",
	"indentOpenBrackets": "[",
	"lineUpClosingBracket": "true",
}

# Keywords dict for smalltalk_main ruleset.
smalltalk_main_keywords_dict = {
	"Array": "literal2",
	"Boolean": "literal2",
	"Character": "literal2",
	"Date": "literal2",
	"False": "literal2",
	"Integer": "literal2",
	"Object": "literal2",
	"Smalltalk": "literal2",
	"String": "literal2",
	"Symbol": "literal2",
	"Time": "literal2",
	"Transcript": "literal2",
	"True": "literal2",
	"false": "keyword1",
	"isNil": "keyword3",
	"nil": "keyword1",
	"not": "keyword3",
	"self": "keyword2",
	"super": "keyword2",
	"true": "keyword1",
}

# Dictionary of keywords dictionaries for smalltalk mode.
keywordsDictDict = {
	"smalltalk_main": smalltalk_main_keywords_dict,
}

# Rules for smalltalk_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="_",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="==",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="keyword3", pattern=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule15(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="label", pattern="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule16(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="literal1", pattern="$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule17(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"\"": [rule1,],
	"#": [rule15,],
	"$": [rule16,],
	"'": [rule0,],
	"*": [rule13,],
	"+": [rule10,],
	"-": [rule11,],
	"/": [rule12,],
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
	":": [rule2,rule14,],
	"<": [rule7,rule9,],
	"=": [rule4,rule5,],
	">": [rule6,rule8,],
	"@": [rule17,],
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
	"_": [rule3,rule17,],
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

# x.rulesDictDict for smalltalk mode.
rulesDictDict = {
	"smalltalk_main": rulesDict1,
}

# Import dict for smalltalk mode.
importDict = {}

