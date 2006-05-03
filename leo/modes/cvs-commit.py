# Leo colorizer control file for cvs-commit mode.

# Properties for cvs-commit mode.
properties = {}

# Keywords dict for cvs_commit_main ruleset.
cvs_commit_main_keywords_dict = {}

# Keywords dict for cvs_commit_changed ruleset.
cvs_commit_changed_keywords_dict = {}

# Rules for cvs_commit_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment1"', seq="CVS:",
        at_line_start=True, at_line_end=False, at_word_start=False,
        delegate="CHANGED", exclude_match=False)

# Rules list for cvs_commit_main ruleset.
cvs_commit_main_rules = [
	rule0, ]

# Rules for cvs_commit_changed ruleset.

def rule1(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment1", seq="CVS:",
        at_line_start=True, at_line_end=False, at_word_start=False, delegate="")

def rule2(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="Committing in",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="Added Files:",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="Modified Files:",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="Removed Files:",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

# Rules list for cvs_commit_changed ruleset.
cvs_commit_changed_rules = [
	rule1, rule2, rule3, rule4, rule5, ]

# Rules dict for cvs_commit mode.
rulesDict = {
	"cvs_commit_changed": cvs_commit_changed_rules,
	"cvs_commit_main": cvs_commit_main_rules,
}

# Import dict for cvs_commit mode.
importDict = {}

