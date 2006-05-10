# Leo colorizer control file for texinfo mode.
# This file is in the public domain.

# Properties for texinfo mode.
properties = {
	"lineComment": "@c",
}

# Attributes dict for texinfo_main ruleset.
texinfo_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for texinfo mode.
attributesDictDict = {
	"texinfo_main": texinfo_main_attributes_dict,
}

# Keywords dict for texinfo_main ruleset.
texinfo_main_keywords_dict = {}

# Dictionary of keywords dictionaries for texinfo mode.
keywordsDictDict = {
	"texinfo_main": texinfo_main_keywords_dict,
}

# Rules for texinfo_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="@c",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="@comment",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword1", pattern="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

# Rules dict for main ruleset.
rulesDict1 = {
	"@": [rule0,rule1,rule2,],
	"{": [rule3,],
	"}": [rule4,],
}

# x.rulesDictDict for texinfo mode.
rulesDictDict = {
	"texinfo_main": rulesDict1,
}

# Import dict for texinfo mode.
importDict = {}

