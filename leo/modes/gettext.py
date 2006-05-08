# Leo colorizer control file for gettext mode.

# Properties for gettext mode.
properties = {
	"lineComment": "# ",
}

# Keywords dict for gettext_main ruleset.
gettext_main_keywords_dict = {
	"c-format": "keyword2",
	"fuzzy": "keyword2",
	"msgid": "keyword1",
	"msgid_plural": "keyword1",
	"msgstr": "keyword1",
	"no-c-format": "keyword2",
}

# Keywords dict for gettext_quoted ruleset.
gettext_quoted_keywords_dict = {}

# Dictionary of keywords dictionaries for gettext mode.
keywordsDictDict = {
	"gettext_main": gettext_main_keywords_dict,
	"gettext_quoted": gettext_quoted_keywords_dict,
}

# Rules for gettext_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="#:",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="#.",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="#~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="comment2", pattern="#,"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule5(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword3", pattern="%"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule6(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword3", pattern="$"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule7(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword3", pattern="@"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule8(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="QUOTED",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule9(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for gettext_main ruleset.
gettext_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
]

# Rules for gettext_quoted ruleset.

def rule10(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="\\"", end="\\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule11(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword3", pattern="%"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule12(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword3", pattern="$"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule13(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword3", pattern="@"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

# Rules list for gettext_quoted ruleset.
gettext_quoted_rules = [
	rule10, rule11, rule12, rule13, ]

# Rules dict for gettext mode.
rulesDict = {
	"gettext_main": gettext_main_rules,
	"gettext_quoted": gettext_quoted_rules,
}

# Import dict for gettext mode.
importDict = {}

