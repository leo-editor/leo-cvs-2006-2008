# Leo colorizer control file for velocity mode.
# This file is in the public domain.

# Properties for velocity mode.
properties = {
	"commentEnd": "*#",
	"commentStart": "#*",
	"lineComment": "##",
}

# Keywords dict for velocity_main ruleset.
velocity_main_keywords_dict = {}

# Keywords dict for velocity_velocity ruleset.
velocity_velocity_keywords_dict = {
	"#else": "keyword1",
	"#elseif": "keyword1",
	"#end": "keyword1",
	"#foreach": "keyword1",
	"#if": "keyword1",
	"#include": "keyword1",
	"#macro": "keyword1",
	"#parse": "keyword1",
	"#set": "keyword1",
	"#stop": "keyword1",
}

# Keywords dict for velocity_javascript ruleset.
velocity_javascript_keywords_dict = {}

# Keywords dict for velocity_javascript2 ruleset.
velocity_javascript2_keywords_dict = {}

# Keywords dict for velocity_back_to_html ruleset.
velocity_back_to_html_keywords_dict = {}

# Keywords dict for velocity_css ruleset.
velocity_css_keywords_dict = {}

# Keywords dict for velocity_css2 ruleset.
velocity_css2_keywords_dict = {}

# Dictionary of keywords dictionaries for velocity mode.
keywordsDictDict = {
	"velocity_back_to_html": velocity_back_to_html_keywords_dict,
	"velocity_css": velocity_css_keywords_dict,
	"velocity_css2": velocity_css2_keywords_dict,
	"velocity_javascript": velocity_javascript_keywords_dict,
	"velocity_javascript2": velocity_javascript2_keywords_dict,
	"velocity_main": velocity_main_keywords_dict,
	"velocity_velocity": velocity_velocity_keywords_dict,
}

# Rules for velocity_main ruleset.

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
        delegate="html::TAGS",exclude_match=False,
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

# Rules for velocity_velocity ruleset.

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind="comment2", begin="#*", end="*#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule7(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment3", seq="##",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule8(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword3", begin="${", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule9(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword3", pattern="$!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule10(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword3", pattern="$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule11(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for velocity ruleset.
rulesDict2 = {
	"#": [rule6,rule7,],
	"$": [rule8,rule9,rule10,],
	"0": [rule11,],
	"1": [rule11,],
	"2": [rule11,],
	"3": [rule11,],
	"4": [rule11,],
	"5": [rule11,],
	"6": [rule11,],
	"7": [rule11,],
	"8": [rule11,],
	"9": [rule11,],
	"@": [rule11,],
	"A": [rule11,],
	"B": [rule11,],
	"C": [rule11,],
	"D": [rule11,],
	"E": [rule11,],
	"F": [rule11,],
	"G": [rule11,],
	"H": [rule11,],
	"I": [rule11,],
	"J": [rule11,],
	"K": [rule11,],
	"L": [rule11,],
	"M": [rule11,],
	"N": [rule11,],
	"O": [rule11,],
	"P": [rule11,],
	"Q": [rule11,],
	"R": [rule11,],
	"S": [rule11,],
	"T": [rule11,],
	"U": [rule11,],
	"V": [rule11,],
	"W": [rule11,],
	"X": [rule11,],
	"Y": [rule11,],
	"Z": [rule11,],
	"_": [rule11,],
	"a": [rule11,],
	"b": [rule11,],
	"c": [rule11,],
	"d": [rule11,],
	"e": [rule11,],
	"f": [rule11,],
	"g": [rule11,],
	"h": [rule11,],
	"i": [rule11,],
	"j": [rule11,],
	"k": [rule11,],
	"l": [rule11,],
	"m": [rule11,],
	"n": [rule11,],
	"o": [rule11,],
	"p": [rule11,],
	"q": [rule11,],
	"r": [rule11,],
	"s": [rule11,],
	"t": [rule11,],
	"u": [rule11,],
	"v": [rule11,],
	"w": [rule11,],
	"x": [rule11,],
	"y": [rule11,],
	"z": [rule11,],
}

# Rules for velocity_javascript ruleset.

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="JAVASCRIPT2")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq="SRC=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="BACK_TO_HTML")

# Rules dict for javascript ruleset.
rulesDict3 = {
	">": [rule12,],
	"S": [rule13,],
}

# Rules for velocity_javascript2 ruleset.



# Rules dict for javascript2 ruleset.
rulesDict4 = {}

# Rules for velocity_back_to_html ruleset.

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="MAIN")

# Rules dict for back_to_html ruleset.
rulesDict5 = {
	">": [rule14,],
}

# Rules for velocity_css ruleset.

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="CSS2")

# Rules dict for css ruleset.
rulesDict6 = {
	">": [rule15,],
}

# Rules for velocity_css2 ruleset.



# Rules dict for css2 ruleset.
rulesDict7 = {}

# x.rulesDictDict for velocity mode.
rulesDictDict = {
	"velocity_back_to_html": rulesDict5,
	"velocity_css": rulesDict6,
	"velocity_css2": rulesDict7,
	"velocity_javascript": rulesDict3,
	"velocity_javascript2": rulesDict4,
	"velocity_main": rulesDict1,
	"velocity_velocity": rulesDict2,
}

# Import dict for velocity mode.
importDict = {
	"velocity_css2": "velocity_css2_velocitycss_main",
	"velocity_javascript2": "velocity_javascript2_velocityjavascript_main",
	"velocity_main": "velocity_main_velocity",
}

