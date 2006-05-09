# Leo colorizer control file for cvs-commit mode.
# This file is in the public domain.

# Properties for cvs-commit mode.
properties = {}

# Keywords dict for cvs_commit_main ruleset.
cvs_commit_main_keywords_dict = {}

# Keywords dict for cvs_commit_changed ruleset.
cvs_commit_changed_keywords_dict = {}

# Dictionary of keywords dictionaries for cvs_commit mode.
keywordsDictDict = {
	"cvs_commit_changed": cvs_commit_changed_keywords_dict,
	"cvs_commit_main": cvs_commit_main_keywords_dict,
}

# Rules for cvs_commit_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="CVS:",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="CHANGED", exclude_match=False)

# Rules dict for main ruleset.
rulesDict1 = {
	"C": [rule0,],
}

# Rules for cvs_commit_changed ruleset.

def rule1(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment1", seq="CVS:",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="Committing in",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="Added Files:",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="Modified Files:",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="Removed Files:",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

# Rules dict for changed ruleset.
rulesDict2 = {
	"A": [rule3,],
	"C": [rule1,rule2,],
	"M": [rule4,],
	"R": [rule5,],
}

# x.rulesDictDict for cvs_commit mode.
rulesDictDict = {
	"cvs_commit_changed": rulesDict2,
	"cvs_commit_main": rulesDict1,
}

# Import dict for cvs_commit mode.
importDict = {}

