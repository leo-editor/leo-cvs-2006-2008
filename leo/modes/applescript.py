# Leo colorizer control file for applescript mode.
# This file is in the public domain.

# Properties for applescript mode.
properties = {
	"commentEnd": "*)",
	"commentStart": "(*",
	"doubleBracketIndent": "false",
	"lineComment": "--",
	"wordBreakChars": ",+-=<>/?^&*",
}

# Attributes dict for applescript_main ruleset.
applescript_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for applescript mode.
attributesDictDict = {
	"applescript_main": applescript_main_attributes_dict,
}

# Keywords dict for applescript_main ruleset.
applescript_main_keywords_dict = {
	"after": "keyword2",
	"and": "operator",
	"anything": "literal2",
	"apr": "literal2",
	"april": "literal2",
	"as": "operator",
	"ask": "literal2",
	"aug": "literal2",
	"august": "literal2",
	"back": "keyword2",
	"before": "keyword2",
	"beginning": "keyword2",
	"bold": "literal2",
	"case": "literal2",
	"close": "keyword3",
	"condensed": "literal2",
	"considering": "keyword1",
	"contains": "operator",
	"continue": "keyword1",
	"copy": "keyword3",
	"count": "keyword3",
	"days": "literal2",
	"dec": "literal2",
	"december": "literal2",
	"delete": "keyword3",
	"diacriticals": "literal2",
	"div": "operator",
	"duplicate": "keyword3",
	"each": "keyword2",
	"eighth": "keyword2",
	"else": "keyword1",
	"end": "keyword1",
	"equal": "operator",
	"equals": "operator",
	"error": "keyword1",
	"every": "keyword2",
	"exists": "keyword3",
	"exit": "keyword1",
	"expanded": "literal2",
	"expansion": "literal2",
	"false": "literal2",
	"feb": "literal2",
	"february": "literal2",
	"fifth": "keyword2",
	"first": "keyword2",
	"fourth": "keyword2",
	"fri": "literal2",
	"friday": "literal2",
	"from": "keyword1",
	"front": "keyword2",
	"get": "keyword1",
	"given": "keyword1",
	"global": "keyword1",
	"hidden": "literal2",
	"hours": "literal2",
	"hyphens": "literal2",
	"id": "keyword2",
	"if": "keyword1",
	"ignoring": "keyword1",
	"in": "keyword1",
	"index": "keyword2",
	"into": "keyword1",
	"is": "keyword1",
	"isn't": "operator",
	"it": "literal2",
	"italic": "literal2",
	"jan": "literal2",
	"january": "literal2",
	"jul": "literal2",
	"july": "literal2",
	"jun": "literal2",
	"june": "literal2",
	"last": "keyword2",
	"launch": "keyword3",
	"local": "keyword1",
	"make": "keyword3",
	"mar": "literal2",
	"march": "literal2",
	"may": "literal2",
	"me": "literal2",
	"middle": "keyword2",
	"minutes": "literal2",
	"mod": "operator",
	"mon": "literal2",
	"monday": "literal2",
	"month": "literal2",
	"move": "keyword3",
	"my": "keyword1",
	"named": "keyword2",
	"nd": "keyword2",
	"ninth": "keyword2",
	"no": "literal2",
	"not": "operator",
	"nov": "literal2",
	"november": "literal2",
	"oct": "literal2",
	"october": "literal2",
	"of": "keyword1",
	"on": "keyword1",
	"open": "keyword3",
	"or": "operator",
	"outline": "literal2",
	"pi": "literal2",
	"plain": "literal2",
	"print": "keyword3",
	"prop": "keyword1",
	"property": "keyword1",
	"punctuation": "literal2",
	"put": "keyword1",
	"quit": "keyword3",
	"rd": "keyword2",
	"reopen": "keyword3",
	"repeat": "keyword1",
	"result": "literal2",
	"return": "keyword1",
	"run": "keyword3",
	"sat": "literal2",
	"saturday": "literal2",
	"save": "keyword3",
	"saving": "keyword3",
	"script": "keyword1",
	"second": "keyword2",
	"sep": "literal2",
	"september": "literal2",
	"set": "keyword1",
	"seventh": "keyword2",
	"shadow": "literal2",
	"sixth": "keyword2",
	"some": "keyword2",
	"space": "literal2",
	"st": "keyword2",
	"strikethrough": "literal2",
	"subscript": "literal2",
	"sun": "literal2",
	"sunday": "literal2",
	"superscript": "literal2",
	"tab": "literal2",
	"tell": "keyword1",
	"tenth": "keyword2",
	"th": "keyword2",
	"the": "keyword2",
	"then": "keyword1",
	"third": "keyword2",
	"through": "keyword2",
	"thru": "keyword2",
	"thu": "literal2",
	"thursday": "literal2",
	"timeout": "keyword1",
	"times": "keyword1",
	"to": "keyword1",
	"transaction": "keyword1",
	"true": "literal2",
	"try": "keyword1",
	"tue": "literal2",
	"tuesday": "literal2",
	"underline": "literal2",
	"until": "keyword1",
	"version": "literal2",
	"wed": "literal2",
	"wednesday": "literal2",
	"weekday": "literal2",
	"weeks": "literal2",
	"where": "keyword2",
	"while": "keyword1",
	"whose": "keyword2",
	"with": "keyword1",
	"without": "keyword1",
	"yes": "literal2",
}

# Dictionary of keywords dictionaries for applescript mode.
keywordsDictDict = {
	"applescript_main": applescript_main_keywords_dict,
}

# Rules for applescript_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="(*", end="*)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="--",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

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
    return colorer.match_seq(s, i, kind="operator", seq="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal2", regexp="application[\\t\\s]+responses", hash_char="a",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal2", regexp="current[\\t\\s]+application", hash_char="c",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal2", regexp="white[\\t\\s]+space", hash_char="w",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal2", regexp="all[\\t\\s]+caps", hash_char="a",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal2", regexp="all[\\t\\s]+lowercase", hash_char="a",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal2", regexp="small[\\t\\s]+caps", hash_char="s",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword3", regexp="missing[\\t\\s]+value", hash_char="m",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"\"": [rule2,],
	"&": [rule11,],
	"'": [rule3,rule24,],
	"(": [rule0,rule4,],
	")": [rule5,],
	"*": [rule9,],
	"+": [rule6,],
	"-": [rule1,rule7,],
	"/": [rule10,],
	"0": [rule24,],
	"1": [rule24,],
	"2": [rule24,],
	"3": [rule24,],
	"4": [rule24,],
	"5": [rule24,],
	"6": [rule24,],
	"7": [rule24,],
	"8": [rule24,],
	"9": [rule24,],
	"<": [rule12,rule13,],
	"=": [rule16,],
	">": [rule14,rule15,],
	"@": [rule24,],
	"A": [rule24,],
	"B": [rule24,],
	"C": [rule24,],
	"D": [rule24,],
	"E": [rule24,],
	"F": [rule24,],
	"G": [rule24,],
	"H": [rule24,],
	"I": [rule24,],
	"J": [rule24,],
	"K": [rule24,],
	"L": [rule24,],
	"M": [rule24,],
	"N": [rule24,],
	"O": [rule24,],
	"P": [rule24,],
	"Q": [rule24,],
	"R": [rule24,],
	"S": [rule24,],
	"T": [rule24,],
	"U": [rule24,],
	"V": [rule24,],
	"W": [rule24,],
	"X": [rule24,],
	"Y": [rule24,],
	"Z": [rule24,],
	"^": [rule8,],
	"a": [rule17,rule20,rule21,rule24,],
	"b": [rule24,],
	"c": [rule18,rule24,],
	"d": [rule24,],
	"e": [rule24,],
	"f": [rule24,],
	"g": [rule24,],
	"h": [rule24,],
	"i": [rule24,],
	"j": [rule24,],
	"k": [rule24,],
	"l": [rule24,],
	"m": [rule23,rule24,],
	"n": [rule24,],
	"o": [rule24,],
	"p": [rule24,],
	"q": [rule24,],
	"r": [rule24,],
	"s": [rule22,rule24,],
	"t": [rule24,],
	"u": [rule24,],
	"v": [rule24,],
	"w": [rule19,rule24,],
	"x": [rule24,],
	"y": [rule24,],
	"z": [rule24,],
}

# x.rulesDictDict for applescript mode.
rulesDictDict = {
	"applescript_main": rulesDict1,
}

# Import dict for applescript mode.
importDict = {}

