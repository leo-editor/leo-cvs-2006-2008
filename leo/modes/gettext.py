# Leo colorizer control file for gettext mode.

# Properties for gettext mode.
properties = {
	"lineComment": "# ",
}

# Keywords dict for gettext_main ruleset.
gettext_main_keywords_dict = {
	"c-format": "keyword2",
	"fuzzy": "keyword2",
	"msgid": "keyword1",
	"msgid_plural": "keyword1",
	"msgstr": "keyword1",
	"no-c-format": "keyword2",
}

# Keywords dict for gettext_quoted ruleset.
gettext_quoted_keywords_dict = {}

# Dictionary of keywords dictionaries for gettext mode.
keywordsDictDict = {
	"gettext_main": gettext_main_keywords_dict,
	"gettext_quoted": gettext_quoted_keywords_dict,
}

# Rules for gettext_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="#:",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="#.",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="#~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="comment2", pattern="#,",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule5(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword3", pattern="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule6(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword3", pattern="$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule7(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword3", pattern="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule8(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="QUOTED",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule9(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"\"": [rule8,],
	"#": [rule0,rule1,rule2,rule3,rule4,],
	"$": [rule6,],
	"%": [rule5,],
	"0": [rule9,],
	"1": [rule9,],
	"2": [rule9,],
	"3": [rule9,],
	"4": [rule9,],
	"5": [rule9,],
	"6": [rule9,],
	"7": [rule9,],
	"8": [rule9,],
	"9": [rule9,],
	"@": [rule7,rule9,],
	"A": [rule9,],
	"B": [rule9,],
	"C": [rule9,],
	"D": [rule9,],
	"E": [rule9,],
	"F": [rule9,],
	"G": [rule9,],
	"H": [rule9,],
	"I": [rule9,],
	"J": [rule9,],
	"K": [rule9,],
	"L": [rule9,],
	"M": [rule9,],
	"N": [rule9,],
	"O": [rule9,],
	"P": [rule9,],
	"Q": [rule9,],
	"R": [rule9,],
	"S": [rule9,],
	"T": [rule9,],
	"U": [rule9,],
	"V": [rule9,],
	"W": [rule9,],
	"X": [rule9,],
	"Y": [rule9,],
	"Z": [rule9,],
	"_": [rule9,],
	"a": [rule9,],
	"b": [rule9,],
	"c": [rule9,],
	"d": [rule9,],
	"e": [rule9,],
	"f": [rule9,],
	"g": [rule9,],
	"h": [rule9,],
	"i": [rule9,],
	"j": [rule9,],
	"k": [rule9,],
	"l": [rule9,],
	"m": [rule9,],
	"n": [rule9,],
	"o": [rule9,],
	"p": [rule9,],
	"q": [rule9,],
	"r": [rule9,],
	"s": [rule9,],
	"t": [rule9,],
	"u": [rule9,],
	"v": [rule9,],
	"w": [rule9,],
	"x": [rule9,],
	"y": [rule9,],
	"z": [rule9,],
}

# Rules for gettext_quoted ruleset.

def rule10(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="\\\"", end="\\\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule11(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword3", pattern="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule12(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword3", pattern="$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule13(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword3", pattern="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

# Rules dict for quoted ruleset.
rulesDict2 = {
	"$": [rule12,],
	"%": [rule11,],
	"@": [rule13,],
	"\\": [rule10,],
}

# x.rulesDictDict for gettext mode.
rulesDictDict = {
	"gettext_main": rulesDict1,
	"gettext_quoted": rulesDict2,
}

# Import dict for gettext mode.
importDict = {}

