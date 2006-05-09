# Leo colorizer control file for html mode.
# This file is in the public domain.

# Properties for html mode.
properties = {
	"commentEnd": "-->",
	"commentStart": "<!--",
}

# Keywords dict for html_main ruleset.
html_main_keywords_dict = {}

# Keywords dict for html_tags ruleset.
html_tags_keywords_dict = {}

# Keywords dict for html_javascript ruleset.
html_javascript_keywords_dict = {}

# Keywords dict for html_back_to_html ruleset.
html_back_to_html_keywords_dict = {}

# Keywords dict for html_css ruleset.
html_css_keywords_dict = {}

# Dictionary of keywords dictionaries for html mode.
keywordsDictDict = {
	"html_back_to_html": html_back_to_html_keywords_dict,
	"html_css": html_css_keywords_dict,
	"html_javascript": html_javascript_keywords_dict,
	"html_main": html_main_keywords_dict,
	"html_tags": html_tags_keywords_dict,
}

# Rules for html_main ruleset.

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

# Rules dict for main ruleset.
rulesDict1 = {
	"&": [rule5,],
	"<": [rule0,rule1,rule2,rule3,rule4,],
}

# Rules for html_tags ruleset.

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule7(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

# Rules dict for tags ruleset.
rulesDict2 = {
	"\"": [rule6,],
	"'": [rule7,],
	"=": [rule8,],
}

# Rules for html_javascript ruleset.

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="javascript::MAIN")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq="SRC=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="BACK_TO_HTML")

# Rules dict for javascript ruleset.
rulesDict3 = {
	">": [rule9,],
	"S": [rule10,],
}

# Rules for html_back_to_html ruleset.

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="html::MAIN")

# Rules dict for back_to_html ruleset.
rulesDict4 = {
	">": [rule11,],
}

# Rules for html_css ruleset.

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="css::MAIN")

# Rules dict for css ruleset.
rulesDict5 = {
	">": [rule12,],
}

# x.rulesDictDict for html mode.
rulesDictDict = {
	"html_back_to_html": rulesDict4,
	"html_css": rulesDict5,
	"html_javascript": rulesDict3,
	"html_main": rulesDict1,
	"html_tags": rulesDict2,
}

# Import dict for html mode.
importDict = {}

