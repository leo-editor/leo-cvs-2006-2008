# Leo colorizer control file for makefile mode.

# Properties for makefile mode.
properties = {
	"lineComment": "#",
}

# Keywords dict for makefile_main ruleset.
makefile_main_keywords_dict = {
	"		": "keywords",
	"			": "keywords",
	"
": "keywords",
	"addprefix": "keyword1",
	"addsuffix": "keyword1",
	"basename": "keyword1",
	"dir": "keyword1",
	"filter": "keyword1",
	"filter-out": "keyword1",
	"findstring": "keyword1",
	"firstword": "keyword1",
	"foreach": "keyword1",
	"join": "keyword1",
	"notdir": "keyword1",
	"origin": "keyword1",
	"patsubst": "keyword1",
	"shell": "keyword1",
	"sort": "keyword1",
	"strip": "keyword1",
	"subst": "keyword1",
	"suffix": "keyword1",
	"wildcard": "keyword1",
	"word": "keyword1",
	"words": "keyword1",
}

# Keywords dict for makefile_variable ruleset.
makefile_variable_keywords_dict = {}

# Dictionary of keywords dictionaries for makefile mode.
keywordsDictDict = {
	"makefile_main": makefile_main_keywords_dict,
	"makefile_variable": makefile_variable_keywords_dict,
}

# Rules for makefile_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="$(", end=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="VARIABLE",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="${", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="VARIABLE",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="`", end="`",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule7(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule8(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"\"": [rule4,],
	"#": [rule0,],
	"$": [rule1,rule2,rule3,],
	"'": [rule5,],
	"0": [rule8,],
	"1": [rule8,],
	"2": [rule8,],
	"3": [rule8,],
	"4": [rule8,],
	"5": [rule8,],
	"6": [rule8,],
	"7": [rule8,],
	"8": [rule8,],
	"9": [rule8,],
	":": [rule7,],
	"@": [rule8,],
	"A": [rule8,],
	"B": [rule8,],
	"C": [rule8,],
	"D": [rule8,],
	"E": [rule8,],
	"F": [rule8,],
	"G": [rule8,],
	"H": [rule8,],
	"I": [rule8,],
	"J": [rule8,],
	"K": [rule8,],
	"L": [rule8,],
	"M": [rule8,],
	"N": [rule8,],
	"O": [rule8,],
	"P": [rule8,],
	"Q": [rule8,],
	"R": [rule8,],
	"S": [rule8,],
	"T": [rule8,],
	"U": [rule8,],
	"V": [rule8,],
	"W": [rule8,],
	"X": [rule8,],
	"Y": [rule8,],
	"Z": [rule8,],
	"_": [rule8,],
	"`": [rule6,],
	"a": [rule8,],
	"b": [rule8,],
	"c": [rule8,],
	"d": [rule8,],
	"e": [rule8,],
	"f": [rule8,],
	"g": [rule8,],
	"h": [rule8,],
	"i": [rule8,],
	"j": [rule8,],
	"k": [rule8,],
	"l": [rule8,],
	"m": [rule8,],
	"n": [rule8,],
	"o": [rule8,],
	"p": [rule8,],
	"q": [rule8,],
	"r": [rule8,],
	"s": [rule8,],
	"t": [rule8,],
	"u": [rule8,],
	"v": [rule8,],
	"w": [rule8,],
	"x": [rule8,],
	"y": [rule8,],
	"z": [rule8,],
}

# Rules for makefile_variable ruleset.

def rule9(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule10(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="$(", end=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="VARIABLE",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule11(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="${", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="VARIABLE",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

# Rules dict for variable ruleset.
rulesDict1 = {
	"#": [rule9,],
	"$": [rule10,rule11,],
}

# x.rulesDictDict for makefile mode.
rulesDictDict = {
	"makefile_main": rulesDict1,
	"makefile_variable": rulesDict1,
}

# Import dict for makefile mode.
importDict = {}

