# Leo colorizer control file for texinfo mode.

# Properties for texinfo mode.
properties = {
	"lineComment": "@c",
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
    return colorer.match_mark_following(s, i, kind="keyword1", pattern="@"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

# Rules list for texinfo_main ruleset.
texinfo_main_rules = [
	rule0, rule1, rule2, rule3, rule4, ]

# Rules dict for texinfo mode.
rulesDict = {
	"texinfo_main": texinfo_main_rules,
}

# Import dict for texinfo mode.
importDict = {}

