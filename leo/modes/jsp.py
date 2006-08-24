# Leo colorizer control file for jsp mode.
# This file is in the public domain.

# Properties for jsp mode.
properties = {
	"commentEnd": "--%>",
	"commentStart": "<%--",
}

# Attributes dict for jsp_main ruleset.
jsp_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for jsp_comment ruleset.
jsp_comment_attributes_dict = {
	"default": "COMMENT1",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for jsp_directives ruleset.
jsp_directives_attributes_dict = {
	"default": "MARKUP",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for jsp_tags ruleset.
jsp_tags_attributes_dict = {
	"default": "MARKUP",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for jsp_attrvalue ruleset.
jsp_attrvalue_attributes_dict = {
	"default": "LITERAL1",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for jsp mode.
attributesDictDict = {
	"jsp_attrvalue": jsp_attrvalue_attributes_dict,
	"jsp_comment": jsp_comment_attributes_dict,
	"jsp_directives": jsp_directives_attributes_dict,
	"jsp_main": jsp_main_attributes_dict,
	"jsp_tags": jsp_tags_attributes_dict,
}

# Keywords dict for jsp_main ruleset.
jsp_main_keywords_dict = {}

# Keywords dict for jsp_comment ruleset.
jsp_comment_keywords_dict = {}

# Keywords dict for jsp_directives ruleset.
jsp_directives_keywords_dict = {
	"autoflush": "keyword2",
	"buffer": "keyword2",
	"charset": "keyword2",
	"contenttype": "keyword2",
	"default": "keyword2",
	"errorpage": "keyword2",
	"extends": "keyword2",
	"file": "keyword2",
	"id": "keyword2",
	"import": "keyword2",
	"include": "keyword1",
	"info": "keyword2",
	"iserrorpage": "keyword2",
	"isthreadsafe": "keyword2",
	"language": "keyword2",
	"method": "keyword2",
	"name": "keyword2",
	"page": "keyword1",
	"prefix": "keyword2",
	"required": "keyword2",
	"rtexprvalue": "keyword2",
	"scope": "keyword2",
	"session": "keyword2",
	"tag": "keyword1",
	"tagattribute": "keyword1",
	"taglib": "keyword1",
	"tagvariable": "keyword1",
	"type": "keyword2",
	"uri": "keyword2",
}

# Keywords dict for jsp_tags ruleset.
jsp_tags_keywords_dict = {}

# Keywords dict for jsp_attrvalue ruleset.
jsp_attrvalue_keywords_dict = {}

# Dictionary of keywords dictionaries for jsp mode.
keywordsDictDict = {
	"jsp_attrvalue": jsp_attrvalue_keywords_dict,
	"jsp_comment": jsp_comment_keywords_dict,
	"jsp_directives": jsp_directives_keywords_dict,
	"jsp_main": jsp_main_keywords_dict,
	"jsp_tags": jsp_tags_keywords_dict,
}

# Rules for jsp_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment2", begin="<%--", end="--%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword1", begin="<%@", end="%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="DIRECTIVES",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword1", begin="<jsp:directive>", end="</jsp:directive>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="DIRECTIVES",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword1", begin="<%=", end="%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="java::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword1", begin="<jsp:expression>", end="</jsp:expression>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="java::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword1", begin="<%!", end="%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="java::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword1", begin="<jsp:declaration>", end="</jsp:declaration>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="java::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule7(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword1", begin="<%", end="%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="java::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule8(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword1", begin="<jsp:scriptlet>", end="</jsp:scriptlet>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="java::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule9(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="COMMENT",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule10(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<SCRIPT", end="</SCRIPT>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="html::JAVASCRIPT",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule11(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<STYLE", end="</STYLE>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="html::CSS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule12(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="<!", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="xml::DTD-TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule13(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule14(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="&", end=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=True)

# Rules dict for main ruleset.
rulesDict1 = {
	"&": [rule14,],
	"<": [rule0,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,],
}

# Rules for jsp_comment ruleset.

def rule15(colorer, s, i):
    return colorer.match_span(s, i, kind="comment2", begin="<%--", end="--%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule16(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword1", begin="<%=", end="%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="java::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule17(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword1", begin="<%", end="%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="java::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules dict for comment ruleset.
rulesDict2 = {
	"<": [rule15,rule16,rule17,],
}

# Rules for jsp_directives ruleset.

def rule18(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword1", begin="<%=", end="%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="java::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule19(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ATTRVALUE",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule20(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ATTRVALUE",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for directives ruleset.
rulesDict3 = {
	"\"": [rule19,],
	"'": [rule20,],
	"/": [rule21,],
	"0": [rule24,],
	"1": [rule24,],
	"2": [rule24,],
	"3": [rule24,],
	"4": [rule24,],
	"5": [rule24,],
	"6": [rule24,],
	"7": [rule24,],
	"8": [rule24,],
	"9": [rule24,],
	":": [rule22,rule23,],
	"<": [rule18,],
	"@": [rule24,],
	"A": [rule24,],
	"B": [rule24,],
	"C": [rule24,],
	"D": [rule24,],
	"E": [rule24,],
	"F": [rule24,],
	"G": [rule24,],
	"H": [rule24,],
	"I": [rule24,],
	"J": [rule24,],
	"K": [rule24,],
	"L": [rule24,],
	"M": [rule24,],
	"N": [rule24,],
	"O": [rule24,],
	"P": [rule24,],
	"Q": [rule24,],
	"R": [rule24,],
	"S": [rule24,],
	"T": [rule24,],
	"U": [rule24,],
	"V": [rule24,],
	"W": [rule24,],
	"X": [rule24,],
	"Y": [rule24,],
	"Z": [rule24,],
	"a": [rule24,],
	"b": [rule24,],
	"c": [rule24,],
	"d": [rule24,],
	"e": [rule24,],
	"f": [rule24,],
	"g": [rule24,],
	"h": [rule24,],
	"i": [rule24,],
	"j": [rule24,],
	"k": [rule24,],
	"l": [rule24,],
	"m": [rule24,],
	"n": [rule24,],
	"o": [rule24,],
	"p": [rule24,],
	"q": [rule24,],
	"r": [rule24,],
	"s": [rule24,],
	"t": [rule24,],
	"u": [rule24,],
	"v": [rule24,],
	"w": [rule24,],
	"x": [rule24,],
	"y": [rule24,],
	"z": [rule24,],
}

# Rules for jsp_tags ruleset.

def rule25(colorer, s, i):
    return colorer.match_span(s, i, kind="comment2", begin="<%--", end="--%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule26(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword1", begin="<%=", end="%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="java::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule27(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ATTRVALUE",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule28(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ATTRVALUE",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule29(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="function", pattern=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule31(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

# Rules dict for tags ruleset.
rulesDict4 = {
	"\"": [rule27,],
	"'": [rule28,],
	"/": [rule29,],
	":": [rule30,rule31,],
	"<": [rule25,rule26,],
}

# Rules for jsp_attrvalue ruleset.

def rule32(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword1", begin="<%=", end="%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="java::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules dict for attrvalue ruleset.
rulesDict5 = {
	"<": [rule32,],
}

# x.rulesDictDict for jsp mode.
rulesDictDict = {
	"jsp_attrvalue": rulesDict5,
	"jsp_comment": rulesDict2,
	"jsp_directives": rulesDict3,
	"jsp_main": rulesDict1,
	"jsp_tags": rulesDict4,
}

# Import dict for jsp mode.
importDict = {}

