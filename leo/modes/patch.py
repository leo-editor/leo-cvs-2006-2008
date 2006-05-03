# Leo colorizer control file for patch mode.

# Properties for patch mode.
properties = {}

# Keywords dict for patch_main ruleset.
patch_main_keywords_dict = {}

# Rules for patch_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"literal1"', seq="+++",
        at_line_start=True, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"literal2"', seq="---",
        at_line_start=True, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"keyword3"', seq="Index:",
        at_line_start=True, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"keyword1"', seq="+",
        at_line_start=True, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"keyword1"', seq=">",
        at_line_start=True, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule5(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"keyword2"', seq="-",
        at_line_start=True, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule6(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"keyword2"', seq="<",
        at_line_start=True, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule7(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"keyword3"', seq="!",
        at_line_start=True, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule8(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"keyword3"', seq="@@",
        at_line_start=True, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule9(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"keyword3"', seq="*",
        at_line_start=True, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

# Rules list for patch_main ruleset.
patch_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
]

# Rules dict for patch mode.
rulesDict = {
	"patch_main": patch_main_rules,
}

# Import dict for patch mode.
importDict = {}

