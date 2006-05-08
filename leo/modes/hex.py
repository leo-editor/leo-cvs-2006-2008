# Leo colorizer control file for hex mode.

# Properties for hex mode.
properties = {}

# Keywords dict for hex_main ruleset.
hex_main_keywords_dict = {}

# Dictionary of keywords dictionaries for hex mode.
keywordsDictDict = {
	"hex_main": hex_main_keywords_dict,
}

# Rules for hex_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="keyword1", pattern=":",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="keyword2", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

# Rules dict for main ruleset.
rulesDict1 = {
	":": [rule0,],
	";": [rule1,],
}

# x.rulesDictDict for hex mode.
rulesDictDict = {
	"hex_main": rulesDict1,
}

# Import dict for hex mode.
importDict = {}

