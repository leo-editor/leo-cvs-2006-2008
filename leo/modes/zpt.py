# Leo colorizer control file for zpt mode.

# Properties for zpt mode.
properties = {
	"commentEnd": "-->",
	"commentStart": "<!--",
}

# Keywords dict for zpt_main ruleset.
zpt_main_keywords_dict = {}

# Keywords dict for zpt_tags ruleset.
zpt_tags_keywords_dict = {
	"attributes": "keyword3",
	"condition": "keyword3",
	"content": "keyword3",
	"define": "keyword3",
	"define-macro": "keyword3",
	"define-slot": "keyword3",
	"fill-slot": "keyword3",
	"metal": "keyword1",
	"omit-tag": "keyword3",
	"on-error": "keyword3",
	"repeat": "keyword3",
	"replace": "keyword3",
	"tal": "keyword1",
	"use-macro": "keyword3",
}

# Keywords dict for zpt_attribute ruleset.
zpt_attribute_keywords_dict = {
	"CONTEXTS": "literal3",
	"Letter": "literal3",
	"Roman": "literal3",
	"attrs": "literal3",
	"container": "literal3",
	"default": "literal3",
	"end": "literal3",
	"even": "literal3",
	"exists": "keyword4",
	"first": "literal3",
	"here": "literal3",
	"index": "literal3",
	"last": "literal3",
	"length": "literal3",
	"letter": "literal3",
	"modules": "literal3",
	"nocall": "keyword4",
	"not": "keyword4",
	"nothing": "literal3",
	"number": "literal3",
	"odd": "literal3",
	"options": "literal3",
	"path": "keyword4",
	"python": "keyword4",
	"repeat": "literal3",
	"request": "literal3",
	"roman": "literal3",
	"root": "literal3",
	"start": "literal3",
	"string": "keyword4",
	"template": "literal3",
	"user": "literal3",
}

# Keywords dict for zpt_javascript ruleset.
zpt_javascript_keywords_dict = {}

# Keywords dict for zpt_back_to_html ruleset.
zpt_back_to_html_keywords_dict = {}

# Keywords dict for zpt_css ruleset.
zpt_css_keywords_dict = {}

# Dictionary of keywords dictionaries for zpt mode.
keywordsDictDict = {
	"zpt_attribute": zpt_attribute_keywords_dict,
	"zpt_back_to_html": zpt_back_to_html_keywords_dict,
	"zpt_css": zpt_css_keywords_dict,
	"zpt_javascript": zpt_javascript_keywords_dict,
	"zpt_main": zpt_main_keywords_dict,
	"zpt_tags": zpt_tags_keywords_dict,
}

# Rules for zpt_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<SCRIPT", end="</SCRIPT>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="JAVASCRIPT",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<STYLE", end="</STYLE>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="CSS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="<!", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="xml::DTD-TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="&", end=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=True)

# Rules list for zpt_main ruleset.
zpt_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, ]

# Rules for zpt_tags ruleset.

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ATTRIBUTE",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule7(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ATTRIBUTE",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for zpt_tags ruleset.
zpt_tags_rules = [
	rule6, rule7, rule8, rule9, ]

# Rules for zpt_attribute ruleset.

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="?",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal2", seq="$$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="${", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule16(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule17(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for zpt_attribute ruleset.
zpt_attribute_rules = [
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, ]

# Rules for zpt_javascript ruleset.

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="javascript::MAIN")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq="SRC=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="BACK_TO_HTML")

# Rules list for zpt_javascript ruleset.
zpt_javascript_rules = [
	rule18, rule19, ]

# Rules for zpt_back_to_html ruleset.

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="zpt::MAIN")

# Rules list for zpt_back_to_html ruleset.
zpt_back_to_html_rules = [
	rule20, ]

# Rules for zpt_css ruleset.

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="css::MAIN")

# Rules list for zpt_css ruleset.
zpt_css_rules = [
	rule21, ]

# Rules dict for zpt mode.
rulesDict = {
	"zpt_attribute": zpt_attribute_rules,
	"zpt_back_to_html": zpt_back_to_html_rules,
	"zpt_css": zpt_css_rules,
	"zpt_javascript": zpt_javascript_rules,
	"zpt_main": zpt_main_rules,
	"zpt_tags": zpt_tags_rules,
}

# Import dict for zpt mode.
importDict = {}

