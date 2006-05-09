# Leo colorizer control file for zpt mode.
# This file is in the public domain.

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

# Rules dict for main ruleset.
rulesDict1 = {
	"&": [rule5,],
	"<": [rule0,rule1,rule2,rule3,rule4,],
}

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

# Rules dict for tags ruleset.
rulesDict2 = {
	"\"": [rule6,],
	"'": [rule7,],
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
	"=": [rule8,],
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
	"_": [rule9,],
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
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule17(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for attribute ruleset.
rulesDict3 = {
	"$": [rule14,rule15,rule16,],
	"0": [rule17,],
	"1": [rule17,],
	"2": [rule17,],
	"3": [rule17,],
	"4": [rule17,],
	"5": [rule17,],
	"6": [rule17,],
	"7": [rule17,],
	"8": [rule17,],
	"9": [rule17,],
	":": [rule10,],
	";": [rule11,],
	"?": [rule12,],
	"@": [rule17,],
	"A": [rule17,],
	"B": [rule17,],
	"C": [rule17,],
	"D": [rule17,],
	"E": [rule17,],
	"F": [rule17,],
	"G": [rule17,],
	"H": [rule17,],
	"I": [rule17,],
	"J": [rule17,],
	"K": [rule17,],
	"L": [rule17,],
	"M": [rule17,],
	"N": [rule17,],
	"O": [rule17,],
	"P": [rule17,],
	"Q": [rule17,],
	"R": [rule17,],
	"S": [rule17,],
	"T": [rule17,],
	"U": [rule17,],
	"V": [rule17,],
	"W": [rule17,],
	"X": [rule17,],
	"Y": [rule17,],
	"Z": [rule17,],
	"_": [rule17,],
	"a": [rule17,],
	"b": [rule17,],
	"c": [rule17,],
	"d": [rule17,],
	"e": [rule17,],
	"f": [rule17,],
	"g": [rule17,],
	"h": [rule17,],
	"i": [rule17,],
	"j": [rule17,],
	"k": [rule17,],
	"l": [rule17,],
	"m": [rule17,],
	"n": [rule17,],
	"o": [rule17,],
	"p": [rule17,],
	"q": [rule17,],
	"r": [rule17,],
	"s": [rule17,],
	"t": [rule17,],
	"u": [rule17,],
	"v": [rule17,],
	"w": [rule17,],
	"x": [rule17,],
	"y": [rule17,],
	"z": [rule17,],
	"|": [rule13,],
}

# Rules for zpt_javascript ruleset.

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="javascript::MAIN")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq="SRC=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="BACK_TO_HTML")

# Rules dict for javascript ruleset.
rulesDict4 = {
	">": [rule18,],
	"S": [rule19,],
}

# Rules for zpt_back_to_html ruleset.

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="zpt::MAIN")

# Rules dict for back_to_html ruleset.
rulesDict5 = {
	">": [rule20,],
}

# Rules for zpt_css ruleset.

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="css::MAIN")

# Rules dict for css ruleset.
rulesDict6 = {
	">": [rule21,],
}

# x.rulesDictDict for zpt mode.
rulesDictDict = {
	"zpt_attribute": rulesDict3,
	"zpt_back_to_html": rulesDict5,
	"zpt_css": rulesDict6,
	"zpt_javascript": rulesDict4,
	"zpt_main": rulesDict1,
	"zpt_tags": rulesDict2,
}

# Import dict for zpt mode.
importDict = {}

