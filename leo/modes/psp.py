# Leo colorizer control file for psp mode.

# Properties for psp mode.
properties = {
	"commentEnd": "-->",
	"commentStart": "<!--",
}

# Keywords dict for psp_main ruleset.
psp_main_keywords_dict = {}

# Keywords dict for psp_tags ruleset.
psp_tags_keywords_dict = {}

# Keywords dict for psp_directive ruleset.
psp_directive_keywords_dict = {
	"file": "keyword4",
	"include": "keyword4",
}

# Rules for psp_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal4"', begin="<%@", end="%>",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="DIRECTIVE",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment2"', begin="<%--", end="--%>",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal3"', begin="<%", end="%>",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="python::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind='"markup"', begin="<script language=\"jscript\">", end="</script>",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="javascript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind='"markup"', begin="<script language=\"javascript\">", end="</script>",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="javascript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind='"markup"', begin="<script>", end="</script>",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="javascript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind='"markup"', begin="<!--#", end="-->",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule7(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment1"', begin="<!--", end="-->",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule8(colorer, s, i):
    return colorer.match_span(s, i, kind='"markup"', begin="<STYLE>", end="</STYLE>",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="css::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule9(colorer, s, i):
    return colorer.match_span(s, i, kind='"markup"', begin="<", end=">",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule10(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal2"', begin="&", end=";",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=True)

# Rules list for psp_main ruleset.
psp_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, ]

# Rules for psp_tags ruleset.

def rule11(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule12(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="'", end="'",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment2"', begin="<%--", end="--%>",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule15(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal3"', begin="<%", end="%>",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="python::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules list for psp_tags ruleset.
psp_tags_rules = [
	rule11, rule12, rule13, rule14, rule15, ]

# Rules for psp_directive ruleset.

def rule16(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule17(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="'", end="'",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for psp_directive ruleset.
psp_directive_rules = [
	rule16, rule17, rule18, rule19, ]

# Rules dict for psp mode.
rulesDict = {
	"psp_directive": psp_directive_rules,
	"psp_main": psp_main_rules,
	"psp_tags": psp_tags_rules,
}

# Import dict for psp mode.
importDict = {}

