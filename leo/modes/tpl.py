# Leo colorizer control file for tpl mode.

# Properties for tpl mode.
properties = {
	"commentEnd": "-->",
	"commentStart": "<!--",
}

# Keywords dict for tpl_main ruleset.
tpl_main_keywords_dict = {}

# Keywords dict for tpl_tpl ruleset.
tpl_tpl_keywords_dict = {
	"=": "operator",
	"END": "keyword2",
	"START": "keyword2",
	"include": "keyword1",
}

# Keywords dict for tpl_tags ruleset.
tpl_tags_keywords_dict = {}

# Dictionary of keywords dictionaries for tpl mode.
keywordsDictDict = {
	"tpl_main": tpl_main_keywords_dict,
	"tpl_tags": tpl_tags_keywords_dict,
	"tpl_tpl": tpl_tpl_keywords_dict,
}

# Rules for tpl_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment3", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<SCRIPT", end="</SCRIPT>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="html::JAVASCRIPT",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<STYLE", end="</STYLE>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="html::CSS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="&", end=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=True)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword3", begin="{", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="TPL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules list for tpl_main ruleset.
tpl_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, ]

# Rules for tpl_tpl ruleset.

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule7(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for tpl_tpl ruleset.
tpl_tpl_rules = [
	rule6, rule7, rule8, rule9, ]

# Rules for tpl_tags ruleset.

def rule10(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule11(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

# Rules list for tpl_tags ruleset.
tpl_tags_rules = [
	rule10, rule11, rule12, ]

# Rules dict for tpl mode.
rulesDict = {
	"tpl_main": tpl_main_rules,
	"tpl_tags": tpl_tags_rules,
	"tpl_tpl": tpl_tpl_rules,
}

# Import dict for tpl mode.
importDict = {}

