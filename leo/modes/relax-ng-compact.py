# Leo colorizer control file for relax-ng-compact mode.

# Properties for relax-ng-compact mode.
properties = {
	"doubleBracketIndent": "false",
	"indentCloseBrackets": "}",
	"indentOpenBrackets": "{",
	"lineComment": "#",
	"wordBreakChars": ",+-=<>/?^&*",
}

# Keywords dict for relax_ng_compact_main ruleset.
relax_ng_compact_main_keywords_dict = {
	"attribute": "keyword1",
	"datatypes": "keyword1",
	"default": "keyword1",
	"div": "keyword1",
	"element": "keyword1",
	"empty": "keyword1",
	"external": "keyword1",
	"grammar": "keyword1",
	"include": "keyword1",
	"inherit": "keyword1",
	"list": "keyword1",
	"mixed": "keyword1",
	"namespace": "keyword1",
	"notAllowed": "keyword1",
	"parent": "keyword1",
	"start": "keyword1",
	"string": "keyword2",
	"text": "keyword1",
	"token": "keyword2",
}

# Rules for relax_ng_compact_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment1"', seq="#",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="'", end="'",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal2"', begin="\"\"\"", end="\"\"\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal2"', begin="'''", end="'''",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="?",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_mark_following(s, i, kind='"null"', 
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=False)

def rule15(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for relax_ng_compact_main ruleset.
relax_ng_compact_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, ]

# Rules dict for relax_ng_compact mode.
rulesDict = {
	"relax_ng_compact_main": relax_ng_compact_main_rules,
}

# Import dict for relax_ng_compact mode.
importDict = {}

