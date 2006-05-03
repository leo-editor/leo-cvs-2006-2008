# Leo colorizer control file for props mode.

# Properties for props mode.
properties = {
	"lineComment": "#",
}

# Keywords dict for props_main ruleset.
props_main_keywords_dict = {}

# Keywords dict for props_prop_value ruleset.
props_prop_value_keywords_dict = {}

# Rules for props_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment1"', seq="#",
        at_line_start=True, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"null"', seq="=",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="PROP_VALUE", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"null"', seq=":",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="PROP_VALUE", exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"null"', seq="",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="PROP_VALUE", exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"null"', seq="",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="PROP_VALUE", exclude_match=False)

# Rules list for props_main ruleset.
props_main_rules = [
	rule0, rule1, rule2, rule3, rule4, ]

# Rules for props_prop_value ruleset.

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword3"', begin="{", end="}",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_mark_following(s, i, kind='"digit"', 
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=False)

# Rules list for props_prop_value ruleset.
props_prop_value_rules = [
	rule5, rule6, ]

# Rules dict for props mode.
rulesDict = {
	"props_main": props_main_rules,
	"props_prop_value": props_prop_value_rules,
}

# Import dict for props mode.
importDict = {}

