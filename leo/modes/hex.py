# Leo colorizer control file for hex mode.

# Properties for hex mode.
properties = {}

# Keywords dict for hex_main ruleset.
hex_main_keywords_dict = {}

# Rules for hex_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind='"keyword1"',
        at_line_start=True, at_line_end=False, at_word_start=False, exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"keyword2"', seq=";",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

# Rules list for hex_main ruleset.
hex_main_rules = [
	rule0, rule1, ]

# Rules dict for hex mode.
rulesDict = {
	"hex_main": hex_main_rules,
}

# Import dict for hex mode.
importDict = {}

