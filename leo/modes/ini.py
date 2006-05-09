# Leo colorizer control file for ini mode.
# This file is in the public domain.

# Properties for ini mode.
properties = {
	"lineComment": ";",
}

# Keywords dict for ini_main ruleset.
ini_main_keywords_dict = {}

# Dictionary of keywords dictionaries for ini mode.
keywordsDictDict = {
	"ini_main": ini_main_keywords_dict,
}

# Rules for ini_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="[", end="]",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq=";",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="keyword1", pattern="=",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=True)

# Rules dict for main ruleset.
rulesDict1 = {
	"#": [rule2,],
	";": [rule1,],
	"=": [rule3,],
	"[": [rule0,],
}

# x.rulesDictDict for ini mode.
rulesDictDict = {
	"ini_main": rulesDict1,
}

# Import dict for ini mode.
importDict = {}

