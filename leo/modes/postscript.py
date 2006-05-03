# Leo colorizer control file for postscript mode.

# Properties for postscript mode.
properties = {
	"lineComment": "%",
}

# Keywords dict for postscript_main ruleset.
postscript_main_keywords_dict = {
	"NULL": "literal2",
	"abs": "operator",
	"add": "operator",
	"atan": "operator",
	"ceiling": "operator",
	"clear": "keyword1",
	"cleartomark": "keyword1",
	"copy": "keyword1",
	"cos": "operator",
	"count": "keyword1",
	"countexecstack": "keyword1",
	"counttomark": "keyword1",
	"div": "operator",
	"dup": "keyword1",
	"exch": "keyword1",
	"exec": "keyword1",
	"execstack": "keyword1",
	"exit": "keyword1",
	"exp": "operator",
	"false": "literal2",
	"floor": "operator",
	"for": "keyword1",
	"idiv": "operator",
	"if": "keyword1",
	"ifelse": "keyword1",
	"ln": "operator",
	"log": "operator",
	"loop": "keyword1",
	"mark": "keyword1",
	"mod": "operator",
	"mul": "operator",
	"ned": "operator",
	"pop": "keyword1",
	"quit": "keyword1",
	"rand": "operator",
	"repeat": "keyword1",
	"roll": "keyword1",
	"round": "operator",
	"rrand": "operator",
	"sin": "operator",
	"sqrt": "operator",
	"srand": "operator",
	"start": "keyword1",
	"stop": "keyword1",
	"stopped": "keyword1",
	"sub": "operator",
	"true": "literal2",
	"truncate": "operator",
}

# Keywords dict for postscript_literal ruleset.
postscript_literal_keywords_dict = {}

# Rules for postscript_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment2"', seq="%!",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment2"', seq="%?",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment2"', seq="%%",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment1"', seq="%",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="(", end=")",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="<", end=">",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_mark_following(s, i, kind='"label"', 
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=False)

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="]",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for postscript_main ruleset.
postscript_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, ]

# Rules for postscript_literal ruleset.

def rule12(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="(", end=")",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules list for postscript_literal ruleset.
postscript_literal_rules = [
	rule12, ]

# Rules dict for postscript mode.
rulesDict = {
	"postscript_literal": postscript_literal_rules,
	"postscript_main": postscript_main_rules,
}

# Import dict for postscript mode.
importDict = {}

