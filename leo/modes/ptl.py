# Leo colorizer control file for ptl mode.

# Properties for ptl mode.
properties = {
	"indentNextLines": "\s*[^#]{3,}:\s*(#.*)?",
	"lineComment": "#",
}

# Keywords dict for ptl_main ruleset.
ptl_main_keywords_dict = {
	"		": "keywords",
	"			": "keywords",
	"
": "keywords",
	"_q_access": "literal4",
	"_q_exception_handler": "literal4",
	"_q_exports": "literal4",
	"_q_index": "literal4",
	"_q_lookup": "literal4",
	"_q_resolve": "literal4",
}

# Dictionary of keywords dictionaries for ptl mode.
keywordsDictDict = {
	"ptl_main": ptl_main_keywords_dict,
}

# Rules for ptl_main ruleset.


def rule0(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword4", seq="[html]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword4", seq="[plain]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"0": [rule2,],
	"1": [rule2,],
	"2": [rule2,],
	"3": [rule2,],
	"4": [rule2,],
	"5": [rule2,],
	"6": [rule2,],
	"7": [rule2,],
	"8": [rule2,],
	"9": [rule2,],
	"@": [rule2,],
	"A": [rule2,],
	"B": [rule2,],
	"C": [rule2,],
	"D": [rule2,],
	"E": [rule2,],
	"F": [rule2,],
	"G": [rule2,],
	"H": [rule2,],
	"I": [rule2,],
	"J": [rule2,],
	"K": [rule2,],
	"L": [rule2,],
	"M": [rule2,],
	"N": [rule2,],
	"O": [rule2,],
	"P": [rule2,],
	"Q": [rule2,],
	"R": [rule2,],
	"S": [rule2,],
	"T": [rule2,],
	"U": [rule2,],
	"V": [rule2,],
	"W": [rule2,],
	"X": [rule2,],
	"Y": [rule2,],
	"Z": [rule2,],
	"[": [rule0,rule1,],
	"_": [rule2,],
	"a": [rule2,],
	"b": [rule2,],
	"c": [rule2,],
	"d": [rule2,],
	"e": [rule2,],
	"f": [rule2,],
	"g": [rule2,],
	"h": [rule2,],
	"i": [rule2,],
	"j": [rule2,],
	"k": [rule2,],
	"l": [rule2,],
	"m": [rule2,],
	"n": [rule2,],
	"o": [rule2,],
	"p": [rule2,],
	"q": [rule2,],
	"r": [rule2,],
	"s": [rule2,],
	"t": [rule2,],
	"u": [rule2,],
	"v": [rule2,],
	"w": [rule2,],
	"x": [rule2,],
	"y": [rule2,],
	"z": [rule2,],
}

# x.rulesDictDict for ptl mode.
rulesDictDict = {
	"ptl_main": rulesDict1,
}

# Import dict for ptl mode.
importDict = {
	"ptl_main": "python_main",
}

