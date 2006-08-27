# Leo colorizer control file for svn-commit mode.
# This file is in the public domain.

# Properties for svn-commit mode.
properties = {}

# Attributes dict for svn_commit_main ruleset.
svn_commit_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "false",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for svn_commit_changed ruleset.
svn_commit_changed_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "false",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for svn_commit mode.
attributesDictDict = {
	"svn_commit_changed": svn_commit_changed_attributes_dict,
	"svn_commit_main": svn_commit_main_attributes_dict,
}

# Keywords dict for svn_commit_main ruleset.
svn_commit_main_keywords_dict = {}

# Keywords dict for svn_commit_changed ruleset.
svn_commit_changed_keywords_dict = {}

# Dictionary of keywords dictionaries for svn_commit mode.
keywordsDictDict = {
	"svn_commit_changed": svn_commit_changed_keywords_dict,
	"svn_commit_main": svn_commit_main_keywords_dict,
}

# Rules for svn_commit_main ruleset.

def svn-commit_rule0(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment1", seq="--This line, and those below, will be ignored--",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, delegate="svn-commit::changed")

# Rules dict for svn_commit_main ruleset.
rulesDict1 = {
	"-": [svn-commit_rule0,],
}

# Rules for svn_commit_changed ruleset.

def svn-commit_rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="A",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def svn-commit_rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="D",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def svn-commit_rule3(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="M",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def svn-commit_rule4(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="_",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

# Rules dict for svn_commit_changed ruleset.
rulesDict2 = {
	"A": [svn-commit_rule1,],
	"D": [svn-commit_rule2,],
	"M": [svn-commit_rule3,],
	"_": [svn-commit_rule4,],
}

# x.rulesDictDict for svn_commit mode.
rulesDictDict = {
	"svn_commit_changed": rulesDict2,
	"svn_commit_main": rulesDict1,
}

# Import dict for svn_commit mode.
importDict = {}

