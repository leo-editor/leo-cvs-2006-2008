# Leo colorizer control file for jhtml mode.
# This file is in the public domain.

# Properties for jhtml mode.
properties = {
	"commentEnd": "-->",
	"commentStart": "<!--",
	"indentNextLines": "\\s*(<\\s*(droplet|oparam))\\s+.*",
}

# Attributes dict for jhtml_main ruleset.
jhtml_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for jhtml_jhtml ruleset.
jhtml_jhtml_attributes_dict = {
	"default": "MARKUP",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for jhtml_attrvalue ruleset.
jhtml_attrvalue_attributes_dict = {
	"default": "LITERAL1",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for jhtml mode.
attributesDictDict = {
	"jhtml_attrvalue": jhtml_attrvalue_attributes_dict,
	"jhtml_jhtml": jhtml_jhtml_attributes_dict,
	"jhtml_main": jhtml_main_attributes_dict,
}

# Keywords dict for jhtml_main ruleset.
jhtml_main_keywords_dict = {}

# Keywords dict for jhtml_jhtml ruleset.
jhtml_jhtml_keywords_dict = {
	"bean": "keyword2",
	"converter": "keyword2",
	"currency": "keyword2",
	"currencyconversion": "keyword2",
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

# Dictionary of keywords dictionaries for jhtml mode.
keywordsDictDict = {
	"jhtml_attrvalue": jhtml_attrvalue_keywords_dict,
	"jhtml_jhtml": jhtml_jhtml_keywords_dict,
	"jhtml_main": jhtml_main_keywords_dict,
}

# Rules for jhtml_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="null", begin="<!--#", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="`", end="`",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="java::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<java>", end="</java>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="java::MAIN",exclude_match=False,
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
        delegate="JHTML",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule8(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="&", end=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=True)

# Rules dict for main ruleset.
rulesDict1 = {
	"&": [rule8,],
	"<": [rule0,rule1,rule3,rule4,rule5,rule6,rule7,],
	"`": [rule2,],
}

# Rules for jhtml_jhtml ruleset.

def rule9(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule10(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ATTRVALUE",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule11(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ATTRVALUE",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for jhtml ruleset.
rulesDict2 = {
	"\"": [rule10,],
	"'": [rule11,],
	"/": [rule12,],
	"0": [rule13,],
	"1": [rule13,],
	"2": [rule13,],
	"3": [rule13,],
	"4": [rule13,],
	"5": [rule13,],
	"6": [rule13,],
	"7": [rule13,],
	"8": [rule13,],
	"9": [rule13,],
	"<": [rule9,],
	"@": [rule13,],
	"A": [rule13,],
	"B": [rule13,],
	"C": [rule13,],
	"D": [rule13,],
	"E": [rule13,],
	"F": [rule13,],
	"G": [rule13,],
	"H": [rule13,],
	"I": [rule13,],
	"J": [rule13,],
	"K": [rule13,],
	"L": [rule13,],
	"M": [rule13,],
	"N": [rule13,],
	"O": [rule13,],
	"P": [rule13,],
	"Q": [rule13,],
	"R": [rule13,],
	"S": [rule13,],
	"T": [rule13,],
	"U": [rule13,],
	"V": [rule13,],
	"W": [rule13,],
	"X": [rule13,],
	"Y": [rule13,],
	"Z": [rule13,],
	"a": [rule13,],
	"b": [rule13,],
	"c": [rule13,],
	"d": [rule13,],
	"e": [rule13,],
	"f": [rule13,],
	"g": [rule13,],
	"h": [rule13,],
	"i": [rule13,],
	"j": [rule13,],
	"k": [rule13,],
	"l": [rule13,],
	"m": [rule13,],
	"n": [rule13,],
	"o": [rule13,],
	"p": [rule13,],
	"q": [rule13,],
	"r": [rule13,],
	"s": [rule13,],
	"t": [rule13,],
	"u": [rule13,],
	"v": [rule13,],
	"w": [rule13,],
	"x": [rule13,],
	"y": [rule13,],
	"z": [rule13,],
}

# Rules for jhtml_attrvalue ruleset.

def rule14(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="`", end="`",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="java::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="label", seq="param:",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="label", seq="bean:",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

# Rules dict for attrvalue ruleset.
rulesDict3 = {
	"`": [rule14,],
	"b": [rule16,],
	"p": [rule15,],
}

# x.rulesDictDict for jhtml mode.
rulesDictDict = {
	"jhtml_attrvalue": rulesDict3,
	"jhtml_jhtml": rulesDict2,
	"jhtml_main": rulesDict1,
}

# Import dict for jhtml mode.
importDict = {}

