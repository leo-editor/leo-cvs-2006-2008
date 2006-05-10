# Leo colorizer control file for pyrex mode.
# This file is in the public domain.

# Properties for pyrex mode.
properties = {
	"indentNextLines": "\\s*[^#]{3,}:\\s*(#.*)?",
	"lineComment": "#",
}

# Keywords dict for pyrex_main ruleset.
pyrex_main_keywords_dict = {
	"NULL": "literal3",
	"cdef": "keyword4",
	"char": "keyword4",
	"cinclude": "keyword4",
	"ctypedef": "keyword4",
	"double": "keyword4",
	"enum": "keyword4",
	"extern": "keyword4",
	"float": "keyword4",
	"include": "keyword4",
	"private": "keyword4",
	"public": "keyword4",
	"short": "keyword4",
	"signed": "keyword4",
	"sizeof": "keyword4",
	"struct": "keyword4",
	"union": "keyword4",
	"unsigned": "keyword4",
	"void": "keyword4",
}

# Dictionary of keywords dictionaries for pyrex mode.
keywordsDictDict = {
	"pyrex_main": pyrex_main_keywords_dict,
}

# Rules for pyrex_main ruleset.


def rule0(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"0": [rule0,],
	"1": [rule0,],
	"2": [rule0,],
	"3": [rule0,],
	"4": [rule0,],
	"5": [rule0,],
	"6": [rule0,],
	"7": [rule0,],
	"8": [rule0,],
	"9": [rule0,],
	"@": [rule0,],
	"A": [rule0,],
	"B": [rule0,],
	"C": [rule0,],
	"D": [rule0,],
	"E": [rule0,],
	"F": [rule0,],
	"G": [rule0,],
	"H": [rule0,],
	"I": [rule0,],
	"J": [rule0,],
	"K": [rule0,],
	"L": [rule0,],
	"M": [rule0,],
	"N": [rule0,],
	"O": [rule0,],
	"P": [rule0,],
	"Q": [rule0,],
	"R": [rule0,],
	"S": [rule0,],
	"T": [rule0,],
	"U": [rule0,],
	"V": [rule0,],
	"W": [rule0,],
	"X": [rule0,],
	"Y": [rule0,],
	"Z": [rule0,],
	"_": [rule0,],
	"a": [rule0,],
	"b": [rule0,],
	"c": [rule0,],
	"d": [rule0,],
	"e": [rule0,],
	"f": [rule0,],
	"g": [rule0,],
	"h": [rule0,],
	"i": [rule0,],
	"j": [rule0,],
	"k": [rule0,],
	"l": [rule0,],
	"m": [rule0,],
	"n": [rule0,],
	"o": [rule0,],
	"p": [rule0,],
	"q": [rule0,],
	"r": [rule0,],
	"s": [rule0,],
	"t": [rule0,],
	"u": [rule0,],
	"v": [rule0,],
	"w": [rule0,],
	"x": [rule0,],
	"y": [rule0,],
	"z": [rule0,],
}

# x.rulesDictDict for pyrex mode.
rulesDictDict = {
	"pyrex_main": rulesDict1,
}

# Import dict for pyrex mode.
importDict = {
	"pyrex_main": ["python_main",],
}

