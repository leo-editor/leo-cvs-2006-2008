# Leo colorizer control file for sqr mode.
# This file is in the public domain.

# Properties for sqr mode.
properties = {
	"lineComment": "!",
}

# Keywords dict for sqr_main ruleset.
sqr_main_keywords_dict = {
	"add": "keyword2",
	"and": "keyword3",
	"array-add": "keyword2",
	"array-divide": "keyword2",
	"array-multiply": "keyword2",
	"array-subtract": "keyword2",
	"ask": "keyword2",
	"begin-footing": "function",
	"begin-heading": "function",
	"begin-procedure": "function",
	"begin-program": "function",
	"begin-report": "function",
	"begin-select": "keyword1",
	"begin-setup": "function",
	"begin-sql": "keyword1",
	"between": "keyword3",
	"break": "keyword2",
	"call": "keyword2",
	"clear-array": "keyword2",
	"close": "keyword2",
	"columns": "keyword2",
	"commit": "keyword2",
	"concat": "keyword2",
	"connect": "keyword2",
	"create-array": "keyword2",
	"date-time": "keyword2",
	"display": "keyword2",
	"divide": "keyword2",
	"do": "keyword2",
	"dollar-symbol": "keyword2",
	"else": "keyword2",
	"encode": "keyword2",
	"end-evaluate": "keyword2",
	"end-footing": "function",
	"end-heading": "function",
	"end-if": "keyword2",
	"end-procedure": "function",
	"end-program": "function",
	"end-report": "function",
	"end-select": "keyword1",
	"end-setup": "function",
	"end-sql": "keyword1",
	"end-while": "keyword2",
	"evaluate": "keyword2",
	"execute": "keyword2",
	"extract": "keyword2",
	"find": "keyword2",
	"font": "keyword2",
	"from": "keyword3",
	"get": "keyword2",
	"goto": "keyword2",
	"graphic": "keyword2",
	"if": "keyword2",
	"in": "keyword3",
	"last-page": "keyword2",
	"let": "keyword2",
	"lookup": "keyword2",
	"lowercase": "keyword2",
	"money-symbol": "keyword2",
	"move": "keyword2",
	"multiply": "keyword2",
	"new-page": "keyword2",
	"new-report": "keyword2",
	"next-column": "keyword2",
	"next-listing": "keyword2",
	"no-formfeed": "keyword2",
	"open": "keyword2",
	"or": "keyword3",
	"page-number": "keyword2",
	"page-size": "keyword2",
	"position": "keyword2",
	"print": "keyword2",
	"print-bar-code": "keyword2",
	"print-chart": "keyword2",
	"print-direct": "keyword2",
	"print-image": "keyword2",
	"printer-deinit": "keyword2",
	"printer-init": "keyword2",
	"put": "keyword2",
	"read": "keyword2",
	"rollback": "keyword2",
	"show": "keyword2",
	"stop": "keyword2",
	"string": "keyword2",
	"subtract": "keyword2",
	"to": "keyword2",
	"unstring": "keyword2",
	"uppercase": "keyword2",
	"use": "keyword2",
	"use-column": "keyword2",
	"use-printer-type": "keyword2",
	"use-procedure": "keyword2",
	"use-report": "keyword2",
	"where": "keyword3",
	"while": "keyword2",
	"write": "keyword2",
}

# Dictionary of keywords dictionaries for sqr mode.
keywordsDictDict = {
	"sqr_main": sqr_main_keywords_dict,
}

# Rules for sqr_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="[", end="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="literal1", pattern="$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule16(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="literal2", pattern="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule17(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="markup", pattern="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule18(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule0,],
	"#": [rule16,],
	"$": [rule15,],
	"&": [rule17,],
	"'": [rule1,],
	"*": [rule14,],
	"+": [rule12,],
	"/": [rule13,],
	"0": [rule18,],
	"1": [rule18,],
	"2": [rule18,],
	"3": [rule18,],
	"4": [rule18,],
	"5": [rule18,],
	"6": [rule18,],
	"7": [rule18,],
	"8": [rule18,],
	"9": [rule18,],
	":": [rule5,],
	"<": [rule7,rule9,rule11,],
	"=": [rule6,],
	">": [rule8,rule10,],
	"@": [rule4,rule18,],
	"A": [rule18,],
	"B": [rule18,],
	"C": [rule18,],
	"D": [rule18,],
	"E": [rule18,],
	"F": [rule18,],
	"G": [rule18,],
	"H": [rule18,],
	"I": [rule18,],
	"J": [rule18,],
	"K": [rule18,],
	"L": [rule18,],
	"M": [rule18,],
	"N": [rule18,],
	"O": [rule18,],
	"P": [rule18,],
	"Q": [rule18,],
	"R": [rule18,],
	"S": [rule18,],
	"T": [rule18,],
	"U": [rule18,],
	"V": [rule18,],
	"W": [rule18,],
	"X": [rule18,],
	"Y": [rule18,],
	"Z": [rule18,],
	"[": [rule2,],
	"^": [rule3,],
	"_": [rule18,],
	"a": [rule18,],
	"b": [rule18,],
	"c": [rule18,],
	"d": [rule18,],
	"e": [rule18,],
	"f": [rule18,],
	"g": [rule18,],
	"h": [rule18,],
	"i": [rule18,],
	"j": [rule18,],
	"k": [rule18,],
	"l": [rule18,],
	"m": [rule18,],
	"n": [rule18,],
	"o": [rule18,],
	"p": [rule18,],
	"q": [rule18,],
	"r": [rule18,],
	"s": [rule18,],
	"t": [rule18,],
	"u": [rule18,],
	"v": [rule18,],
	"w": [rule18,],
	"x": [rule18,],
	"y": [rule18,],
	"z": [rule18,],
}

# x.rulesDictDict for sqr mode.
rulesDictDict = {
	"sqr_main": rulesDict1,
}

# Import dict for sqr mode.
importDict = {}

