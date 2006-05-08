# Leo colorizer control file for eiffel mode.

# Properties for eiffel mode.
properties = {
	"lineComment": "--",
}

# Keywords dict for eiffel_main ruleset.
eiffel_main_keywords_dict = {
	"alias": "keyword1",
	"all": "keyword1",
	"and": "keyword1",
	"as": "keyword1",
	"check": "keyword1",
	"class": "keyword1",
	"creation": "keyword1",
	"current": "literal2",
	"debug": "keyword1",
	"deferred": "keyword1",
	"do": "keyword1",
	"else": "keyword1",
	"elseif": "keyword1",
	"end": "keyword1",
	"ensure": "keyword1",
	"expanded": "keyword1",
	"export": "keyword1",
	"external": "keyword1",
	"false": "literal2",
	"feature": "keyword1",
	"from": "keyword1",
	"frozen": "keyword1",
	"if": "keyword1",
	"implies": "keyword1",
	"indexing": "keyword1",
	"infix": "keyword1",
	"inherit": "keyword1",
	"inspect": "keyword1",
	"invariant": "keyword1",
	"is": "keyword1",
	"like": "keyword1",
	"local": "keyword1",
	"loop": "keyword1",
	"not": "keyword1",
	"obsolete": "keyword1",
	"old": "keyword1",
	"once": "keyword1",
	"or": "keyword1",
	"precursor": "literal2",
	"prefix": "keyword1",
	"redefine": "keyword1",
	"rename": "keyword1",
	"require": "keyword1",
	"rescue": "keyword1",
	"result": "literal2",
	"retry": "keyword1",
	"select": "keyword1",
	"separate": "keyword1",
	"strip": "literal2",
	"then": "keyword1",
	"true": "literal2",
	"undefine": "keyword1",
	"unique": "literal2",
	"until": "keyword1",
	"variant": "keyword1",
	"void": "literal2",
	"when": "keyword1",
	"xor": "keyword1",
}

# Dictionary of keywords dictionaries for eiffel mode.
keywordsDictDict = {
	"eiffel_main": eiffel_main_keywords_dict,
}

# Rules for eiffel_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="--",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"\"": [rule1,],
	"'": [rule2,],
	"-": [rule0,],
	"0": [rule3,],
	"1": [rule3,],
	"2": [rule3,],
	"3": [rule3,],
	"4": [rule3,],
	"5": [rule3,],
	"6": [rule3,],
	"7": [rule3,],
	"8": [rule3,],
	"9": [rule3,],
	"@": [rule3,],
	"A": [rule3,],
	"B": [rule3,],
	"C": [rule3,],
	"D": [rule3,],
	"E": [rule3,],
	"F": [rule3,],
	"G": [rule3,],
	"H": [rule3,],
	"I": [rule3,],
	"J": [rule3,],
	"K": [rule3,],
	"L": [rule3,],
	"M": [rule3,],
	"N": [rule3,],
	"O": [rule3,],
	"P": [rule3,],
	"Q": [rule3,],
	"R": [rule3,],
	"S": [rule3,],
	"T": [rule3,],
	"U": [rule3,],
	"V": [rule3,],
	"W": [rule3,],
	"X": [rule3,],
	"Y": [rule3,],
	"Z": [rule3,],
	"_": [rule3,],
	"a": [rule3,],
	"b": [rule3,],
	"c": [rule3,],
	"d": [rule3,],
	"e": [rule3,],
	"f": [rule3,],
	"g": [rule3,],
	"h": [rule3,],
	"i": [rule3,],
	"j": [rule3,],
	"k": [rule3,],
	"l": [rule3,],
	"m": [rule3,],
	"n": [rule3,],
	"o": [rule3,],
	"p": [rule3,],
	"q": [rule3,],
	"r": [rule3,],
	"s": [rule3,],
	"t": [rule3,],
	"u": [rule3,],
	"v": [rule3,],
	"w": [rule3,],
	"x": [rule3,],
	"y": [rule3,],
	"z": [rule3,],
}

# x.rulesDictDict for eiffel mode.
rulesDictDict = {
	"eiffel_main": rulesDict1,
}

# Import dict for eiffel mode.
importDict = {}

