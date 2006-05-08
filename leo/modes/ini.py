# Leo colorizer control file for ini mode.

# Properties for ini mode.
properties = {
	"lineComment": ";",
}

# Keywords dict for ini_main ruleset.
ini_main_keywords_dict = {}

# Dictionary of keywords dictionaries for ini mode.
keywordsDictDict = {
	"ini_main": ini_main_keywords_dict,
}

# Rules for ini_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="[", end="]",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq=";",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="keyword1", pattern="=",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=True)

# Rules list for ini_main ruleset.
ini_main_rules = [
	rule0, rule1, rule2, rule3, ]

# Rules dict for ini mode.
rulesDict = {
	"ini_main": ini_main_rules,
}

# Import dict for ini mode.
importDict = {}

