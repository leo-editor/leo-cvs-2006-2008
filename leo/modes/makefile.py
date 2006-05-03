# Leo colorizer control file for makefile mode.

# Properties for makefile mode.
properties = {
	"lineComment": "#",
}

# Keywords dict for makefile_main ruleset.
makefile_main_keywords_dict = {
	"addprefix": "keyword1",
	"addsuffix": "keyword1",
	"basename": "keyword1",
	"dir": "keyword1",
	"filter": "keyword1",
	"filter-out": "keyword1",
	"findstring": "keyword1",
	"firstword": "keyword1",
	"foreach": "keyword1",
	"join": "keyword1",
	"notdir": "keyword1",
	"origin": "keyword1",
	"patsubst": "keyword1",
	"shell": "keyword1",
	"sort": "keyword1",
	"strip": "keyword1",
	"subst": "keyword1",
	"suffix": "keyword1",
	"wildcard": "keyword1",
	"word": "keyword1",
	"words": "keyword1",
}

# Keywords dict for makefile_variable ruleset.
makefile_variable_keywords_dict = {}

# Rules for makefile_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment1"', seq="#",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword2"', begin="$(", end=")",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="VARIABLE",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword2"', begin="${", end="}",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="VARIABLE",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_mark_following(s, i, kind='"keyword2"', 
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="'", end="'",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="`", end="`",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule7(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind='"label"',
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=False)

def rule8(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for makefile_main ruleset.
makefile_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, ]

# Rules for makefile_variable ruleset.

def rule9(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment1"', seq="#",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule10(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword2"', begin="$(", end=")",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="VARIABLE",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule11(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword2"', begin="${", end="}",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="VARIABLE",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

# Rules list for makefile_variable ruleset.
makefile_variable_rules = [
	rule9, rule10, rule11, ]

# Rules dict for makefile mode.
rulesDict = {
	"makefile_main": makefile_main_rules,
	"makefile_variable": makefile_variable_rules,
}

# Import dict for makefile mode.
importDict = {}

