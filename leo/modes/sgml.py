# Leo colorizer control file for sgml mode.
# This file is in the public domain.

# Properties for sgml mode.
properties = {
	"commentEnd": "-->",
	"commentStart": "<!--",
}

# Attributes dict for sgml_main ruleset.
sgml_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for sgml mode.
attributesDictDict = {
	"sgml_main": sgml_main_attributes_dict,
}

# Keywords dict for sgml_main ruleset.
sgml_main_keywords_dict = {}

# Dictionary of keywords dictionaries for sgml mode.
keywordsDictDict = {
	"sgml_main": sgml_main_keywords_dict,
}

# Rules for sgml_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="<!ENTITY", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="xml::ENTITY-TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="<![CDATA[", end="]]>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="xml::CDATA",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="<!", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="xml::DTD-TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="xml::TAGS",exclude_match=False,
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

# x.rulesDictDict for sgml mode.
rulesDictDict = {
	"sgml_main": rulesDict1,
}

# Import dict for sgml mode.
importDict = {}

