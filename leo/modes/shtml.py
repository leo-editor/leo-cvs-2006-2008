# Leo colorizer control file for shtml mode.

# Properties for shtml mode.
properties = {
	"commentEnd": "-->",
	"commentStart": "<!--",
}

# Keywords dict for shtml_main ruleset.
shtml_main_keywords_dict = {}

# Keywords dict for shtml_tags ruleset.
shtml_tags_keywords_dict = {}

# Keywords dict for shtml_ssi ruleset.
shtml_ssi_keywords_dict = {
	"cgi": "keyword2",
	"cmd": "keyword2",
	"config": "keyword1",
	"echo": "keyword1",
	"errmsg": "keyword2",
	"exec": "keyword1",
	"file": "keyword2",
	"flastmod": "keyword1",
	"fsize": "keyword1",
	"include": "keyword1",
	"sizefmt": "keyword2",
	"timefmt": "keyword2",
	"var": "keyword2",
}

# Keywords dict for shtml_ssi_expression ruleset.
shtml_ssi_expression_keywords_dict = {}

# Rules for shtml_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword3"', begin="<!--#", end="-->",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="SSI",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment1"', begin="<!--", end="-->",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind='"markup"', begin="<SCRIPT", end="</SCRIPT>",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="html::JAVASCRIPT",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind='"markup"', begin="<STYLE", end="</STYLE>",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="html::CSS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword2"', begin="<!", end=">",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="xml::DTD-TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind='"markup"', begin="<", end=">",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal2"', begin="&", end=";",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=True)

# Rules list for shtml_main ruleset.
shtml_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, ]

# Rules for shtml_tags ruleset.

def rule7(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule8(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="'", end="'",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

# Rules list for shtml_tags ruleset.
shtml_tags_rules = [
	rule7, rule8, rule9, ]

# Rules for shtml_ssi ruleset.

def rule10(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="SSI-EXPRESSION",exclude_match=True,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for shtml_ssi ruleset.
shtml_ssi_rules = [
	rule10, rule11, rule12, ]

# Rules for shtml_ssi_expression ruleset.

def rule13(colorer, s, i):
    return colorer.match_mark_following(s, i, kind='"keyword2"', 
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=False)

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&&",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="||",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

# Rules list for shtml_ssi_expression ruleset.
shtml_ssi_expression_rules = [
	rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, ]

# Rules dict for shtml mode.
rulesDict = {
	"shtml_main": shtml_main_rules,
	"shtml_ssi": shtml_ssi_rules,
	"shtml_ssi_expression": shtml_ssi_expression_rules,
	"shtml_tags": shtml_tags_rules,
}

# Import dict for shtml mode.
importDict = {}

