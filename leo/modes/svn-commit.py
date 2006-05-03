# Leo colorizer control file for svn-commit mode.

# Properties for svn-commit mode.
properties = {}

# Keywords dict for svn_commit_main ruleset.
svn_commit_main_keywords_dict = {}

# Keywords dict for svn_commit_changed ruleset.
svn_commit_changed_keywords_dict = {}

# Rules for svn_commit_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment1", seq="--This line, and those below, will be ignored--",
        at_line_start=True, at_line_end=False, at_word_start=False, delegate="CHANGED")

# Rules list for svn_commit_main ruleset.
svn_commit_main_rules = [
	rule0, ]

# Rules for svn_commit_changed ruleset.

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment2"', seq="A",
        at_line_start=True, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment2"', seq="D",
        at_line_start=True, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment2"', seq="M",
        at_line_start=True, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment2"', seq="_",
        at_line_start=True, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

# Rules list for svn_commit_changed ruleset.
svn_commit_changed_rules = [
	rule1, rule2, rule3, rule4, ]

# Rules dict for svn_commit mode.
rulesDict = {
	"svn_commit_changed": svn_commit_changed_rules,
	"svn_commit_main": svn_commit_main_rules,
}

# Import dict for svn_commit mode.
importDict = {}

