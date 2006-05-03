# Leo colorizer control file for jhtml mode.

# Properties for jhtml mode.
properties = {
	"commentEnd": "-->",
	"commentStart": "<!--",
	"indentNextLines": "\s*(<\s*(droplet|oparam))\s+.*",
}

# Keywords dict for jhtml_main ruleset.
jhtml_main_keywords_dict = {}

# Keywords dict for jhtml_jhtml ruleset.
jhtml_jhtml_keywords_dict = {
	"bean": "keyword2",
	"converter": "keyword2",
	"currency": "keyword2",
	"currencyConversion": "keyword2",
	"date": "keyword2",
	"declareparam": "keyword2",
	"droplet": "keyword1",
	"euro": "keyword2",
	"importbean": "keyword1",
	"locale": "keyword2",
	"nullable": "keyword2",
	"number": "keyword2",
	"oparam": "keyword1",
	"param": "keyword1",
	"priority": "keyword2",
	"required": "keyword2",
	"servlet": "keyword1",
	"setvalue": "keyword1",
	"submitvalue": "keyword2",
	"symbol": "keyword2",
	"synchronized": "keyword2",
	"valueof": "keyword1",
}

# Keywords dict for jhtml_attrvalue ruleset.
jhtml_attrvalue_keywords_dict = {}

# Rules for jhtml_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind='"null"', begin="<!--#", end="-->",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment1"', begin="<!--", end="-->",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind='"markup"', begin="`", end="`",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="java::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind='"markup"', begin="<java>", end="</java>",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="java::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind='"markup"', begin="<SCRIPT", end="</SCRIPT>",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="html::JAVASCRIPT",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind='"markup"', begin="<STYLE", end="</STYLE>",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="html::CSS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword2"', begin="<!", end=">",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="xml::DTD-TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule7(colorer, s, i):
    return colorer.match_span(s, i, kind='"markup"', begin="<", end=">",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="JHTML",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule8(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal2"', begin="&", end=";",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=True)

# Rules list for jhtml_main ruleset.
jhtml_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, ]

# Rules for jhtml_jhtml ruleset.

def rule9(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment1"', begin="<!--", end="-->",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule10(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="ATTRVALUE",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule11(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="'", end="'",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="ATTRVALUE",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq="/",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for jhtml_jhtml ruleset.
jhtml_jhtml_rules = [
	rule9, rule10, rule11, rule12, rule13, ]

# Rules for jhtml_attrvalue ruleset.

def rule14(colorer, s, i):
    return colorer.match_span(s, i, kind='"markup"', begin="`", end="`",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="java::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="label", seq="param:",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="label", seq="bean:",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

# Rules list for jhtml_attrvalue ruleset.
jhtml_attrvalue_rules = [
	rule14, rule15, rule16, ]

# Rules dict for jhtml mode.
rulesDict = {
	"jhtml_attrvalue": jhtml_attrvalue_rules,
	"jhtml_jhtml": jhtml_jhtml_rules,
	"jhtml_main": jhtml_main_rules,
}

# Import dict for jhtml mode.
importDict = {}

