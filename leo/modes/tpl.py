# Leo colorizer control file for tpl mode.
# This file is in the public domain.

# Properties for tpl mode.
properties = {
	"commentEnd": "-->",
	"commentStart": "<!--",
}

# Attributes dict for tpl_main ruleset.
tpl_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for tpl_tpl ruleset.
tpl_tpl_attributes_dict = {
	"default": "KEYWORD1",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for tpl_tags ruleset.
tpl_tags_attributes_dict = {
	"default": "MARKUP",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for tpl mode.
attributesDictDict = {
	"tpl_main": tpl_main_attributes_dict,
	"tpl_tags": tpl_tags_attributes_dict,
	"tpl_tpl": tpl_tpl_attributes_dict,
}

# Keywords dict for tpl_main ruleset.
tpl_main_keywords_dict = {}

# Keywords dict for tpl_tpl ruleset.
tpl_tpl_keywords_dict = {
	"=": "operator",
	"end": "keyword2",
	"include": "keyword1",
	"start": "keyword2",
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

# Rules dict for main ruleset.
rulesDict1 = {
	"&": [rule4,],
	"<": [rule0,rule1,rule2,rule3,],
	"{": [rule5,],
}

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

# Rules dict for tpl ruleset.
rulesDict2 = {
	"\"": [rule6,],
	"'": [rule7,],
	"*": [rule8,],
	"0": [rule9,],
	"1": [rule9,],
	"2": [rule9,],
	"3": [rule9,],
	"4": [rule9,],
	"5": [rule9,],
	"6": [rule9,],
	"7": [rule9,],
	"8": [rule9,],
	"9": [rule9,],
	"=": [rule9,],
	"@": [rule9,],
	"A": [rule9,],
	"B": [rule9,],
	"C": [rule9,],
	"D": [rule9,],
	"E": [rule9,],
	"F": [rule9,],
	"G": [rule9,],
	"H": [rule9,],
	"I": [rule9,],
	"J": [rule9,],
	"K": [rule9,],
	"L": [rule9,],
	"M": [rule9,],
	"N": [rule9,],
	"O": [rule9,],
	"P": [rule9,],
	"Q": [rule9,],
	"R": [rule9,],
	"S": [rule9,],
	"T": [rule9,],
	"U": [rule9,],
	"V": [rule9,],
	"W": [rule9,],
	"X": [rule9,],
	"Y": [rule9,],
	"Z": [rule9,],
	"a": [rule9,],
	"b": [rule9,],
	"c": [rule9,],
	"d": [rule9,],
	"e": [rule9,],
	"f": [rule9,],
	"g": [rule9,],
	"h": [rule9,],
	"i": [rule9,],
	"j": [rule9,],
	"k": [rule9,],
	"l": [rule9,],
	"m": [rule9,],
	"n": [rule9,],
	"o": [rule9,],
	"p": [rule9,],
	"q": [rule9,],
	"r": [rule9,],
	"s": [rule9,],
	"t": [rule9,],
	"u": [rule9,],
	"v": [rule9,],
	"w": [rule9,],
	"x": [rule9,],
	"y": [rule9,],
	"z": [rule9,],
}

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

# Rules dict for tags ruleset.
rulesDict3 = {
	"\"": [rule10,],
	"'": [rule11,],
	"=": [rule12,],
}

# x.rulesDictDict for tpl mode.
rulesDictDict = {
	"tpl_main": rulesDict1,
	"tpl_tags": rulesDict3,
	"tpl_tpl": rulesDict2,
}

# Import dict for tpl mode.
importDict = {}

