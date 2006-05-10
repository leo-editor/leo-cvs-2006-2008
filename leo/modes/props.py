# Leo colorizer control file for props mode.
# This file is in the public domain.

# Properties for props mode.
properties = {
	"lineComment": "#",
}

# Attributes dict for props_main ruleset.
props_main_attributes_dict = {
	"default": "KEYWORD1",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for props_prop_value ruleset.
props_prop_value_attributes_dict = {
	"default": "KEYWORD1",
	"digit_re": "([[:digit:]]+|#[[:xdigit:]]+)",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "#",
}

# Dictionary of attributes dictionaries for props mode.
attributesDictDict = {
	"props_main": props_main_attributes_dict,
	"props_prop_value": props_prop_value_attributes_dict,
}

# Keywords dict for props_main ruleset.
props_main_keywords_dict = {}

# Keywords dict for props_prop_value ruleset.
props_prop_value_keywords_dict = {}

# Dictionary of keywords dictionaries for props mode.
keywordsDictDict = {
	"props_main": props_main_keywords_dict,
	"props_prop_value": props_prop_value_keywords_dict,
}

# Rules for props_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="null", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="PROP_VALUE", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="null", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="PROP_VALUE", exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="null", seq=" ",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="PROP_VALUE", exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="null", seq="\t",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="PROP_VALUE", exclude_match=False)

# Rules dict for main ruleset.
rulesDict1 = {
	"\t": [rule4,],
	" ": [rule3,],
	"#": [rule0,],
	":": [rule2,],
	"=": [rule1,],
}

# Rules for props_prop_value ruleset.

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword3", begin="{", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="digit", pattern="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

# Rules dict for prop_value ruleset.
rulesDict2 = {
	"#": [rule6,],
	"{": [rule5,],
}

# x.rulesDictDict for props mode.
rulesDictDict = {
	"props_main": rulesDict1,
	"props_prop_value": rulesDict2,
}

# Import dict for props mode.
importDict = {}

