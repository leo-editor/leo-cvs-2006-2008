# Leo colorizer control file for mail mode.
# This file is in the public domain.

# Properties for mail mode.
properties = {
	"lineComment": ">",
	"noWordSep": "-_",
}

# Attributes dict for mail_main ruleset.
mail_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "false",
	"ignore_case": "true",
	"no_word_sep": "-_:)",
}

# Attributes dict for mail_signature ruleset.
mail_signature_attributes_dict = {
	"default": "COMMENT2",
	"digit_re": "",
	"highlight_digits": "false",
	"ignore_case": "true",
	"no_word_sep": "-_:)",
}

# Attributes dict for mail_header ruleset.
mail_header_attributes_dict = {
	"default": "MARKUP",
	"digit_re": "",
	"highlight_digits": "false",
	"ignore_case": "true",
	"no_word_sep": "-_:)",
}

# Dictionary of attributes dictionaries for mail mode.
attributesDictDict = {
	"mail_header": mail_header_attributes_dict,
	"mail_main": mail_main_attributes_dict,
	"mail_signature": mail_signature_attributes_dict,
}

# Keywords dict for mail_main ruleset.
mail_main_keywords_dict = {}

# Keywords dict for mail_signature ruleset.
mail_signature_keywords_dict = {}

# Keywords dict for mail_header ruleset.
mail_header_keywords_dict = {}

# Dictionary of keywords dictionaries for mail mode.
keywordsDictDict = {
	"mail_header": mail_header_keywords_dict,
	"mail_main": mail_main_keywords_dict,
	"mail_signature": mail_signature_keywords_dict,
}

# Rules for mail_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment3", seq=">>>",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq=">>",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq=">",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="|",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq=":",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment2", seq="--",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, delegate="SIGNATURE")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq=":-)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq=":-(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq=":)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq=":(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq=";-)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq=";-(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq=";)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq=";(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=False)

# Rules dict for main ruleset.
rulesDict1 = {
	"-": [rule5,],
	":": [rule4,rule6,rule7,rule8,rule9,rule14,],
	";": [rule10,rule11,rule12,rule13,],
	">": [rule0,rule1,rule2,],
	"|": [rule3,],
}

# Rules for mail_signature ruleset.

# Rules dict for signature ruleset.
rulesDict2 = {}

# Rules for mail_header ruleset.

def rule15(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="<", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

# Rules dict for header ruleset.
rulesDict3 = {
	"<": [rule15,],
}

# x.rulesDictDict for mail mode.
rulesDictDict = {
	"mail_header": rulesDict3,
	"mail_main": rulesDict1,
	"mail_signature": rulesDict2,
}

# Import dict for mail mode.
importDict = {}

