# Leo colorizer control file for rhtml mode.
# This file is in the public domain.

# Properties for rhtml mode.
properties = {
	"commentEnd": "%>",
	"commentStart": "<%#",
}

# Keywords dict for rhtml_main ruleset.
rhtml_main_keywords_dict = {}

# Keywords dict for rhtml_tags ruleset.
rhtml_tags_keywords_dict = {}

# Keywords dict for rhtml_tags_literal ruleset.
rhtml_tags_literal_keywords_dict = {}

# Dictionary of keywords dictionaries for rhtml mode.
keywordsDictDict = {
	"rhtml_main": rhtml_main_keywords_dict,
	"rhtml_tags": rhtml_tags_keywords_dict,
	"rhtml_tags_literal": rhtml_tags_literal_keywords_dict,
}

# Rules for rhtml_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<%#", end="%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<%=", end="%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ruby::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<%", end="%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ruby::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<SCRIPT", end="</SCRIPT>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="html::JAVASCRIPT",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<STYLE", end="</STYLE>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="html::CSS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="<!", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="xml::DTD-TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule7(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule8(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="&", end=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=True)

# Rules dict for main ruleset.
rulesDict1 = {
	"&": [rule8,],
	"<": [rule0,rule1,rule2,rule3,rule4,rule5,rule6,rule7,],
}

# Rules for rhtml_tags ruleset.

def rule9(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule10(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<%#", end="%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule11(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="TAGS_LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule12(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="TAGS_LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

# Rules dict for tags ruleset.
rulesDict2 = {
	"\"": [rule11,],
	"'": [rule12,],
	"<": [rule9,rule10,],
	"=": [rule13,],
}

# Rules for rhtml_tags_literal ruleset.

def rule14(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<%", end="%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule15(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<%=", end="%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules dict for tags_literal ruleset.
rulesDict3 = {
	"<": [rule14,rule15,],
}

# x.rulesDictDict for rhtml mode.
rulesDictDict = {
	"rhtml_main": rulesDict1,
	"rhtml_tags": rulesDict2,
	"rhtml_tags_literal": rulesDict3,
}

# Import dict for rhtml mode.
importDict = {}

