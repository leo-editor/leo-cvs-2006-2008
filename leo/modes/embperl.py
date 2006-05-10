# Leo colorizer control file for embperl mode.
# This file is in the public domain.

# Properties for embperl mode.
properties = {
	"commentEnd": "-->",
	"commentStart": "<!--",
}

# Attributes dict for embperl_main ruleset.
embperl_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "false",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for embperl mode.
attributesDictDict = {
	"embperl_main": embperl_main_attributes_dict,
}

# Keywords dict for embperl_main ruleset.
embperl_main_keywords_dict = {}

# Dictionary of keywords dictionaries for embperl mode.
keywordsDictDict = {
	"embperl_main": embperl_main_keywords_dict,
}

# Rules for embperl_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment2", begin="[#", end="#]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal3", begin="[+", end="+]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="perl::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal3", begin="[-", end="-]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="perl::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="literal3", begin="[$", end="$]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="perl::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="literal3", begin="[!", end="!]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="perl::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)


# Rules dict for main ruleset.
rulesDict1 = {
	"[": [rule0,rule1,rule2,rule3,rule4,],
}

# x.rulesDictDict for embperl mode.
rulesDictDict = {
	"embperl_main": rulesDict1,
}

# Import dict for embperl mode.
importDict = {
	"embperl_main": ["html_main",],
}

