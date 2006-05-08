# Leo colorizer control file for ptl mode.

# Properties for ptl mode.
properties = {
	"indentNextLines": "\s*[^#]{3,}:\s*(#.*)?",
	"lineComment": "#",
}

# Keywords dict for ptl_main ruleset.
ptl_main_keywords_dict = {
	"_q_access": "literal4",
	"_q_exception_handler": "literal4",
	"_q_exports": "literal4",
	"_q_index": "literal4",
	"_q_lookup": "literal4",
	"_q_resolve": "literal4",
}

# Dictionary of keywords dictionaries for ptl mode.
keywordsDictDict = {
	"ptl_main": ptl_main_keywords_dict,
}

# Rules for ptl_main ruleset.


def rule0(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword4", seq="[html]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword4", seq="[plain]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for ptl_main ruleset.
ptl_main_rules = [
	rule0, rule1, rule2, ]

# Rules dict for ptl mode.
rulesDict = {
	"ptl_main": ptl_main_rules,
}

# Import dict for ptl mode.
importDict = {
	"ptl_main": "python_main",
}

