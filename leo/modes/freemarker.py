# Leo colorizer control file for freemarker mode.
# This file is in the public domain.

# Properties for freemarker mode.
properties = {}

# Attributes dict for freemarker_main ruleset.
freemarker_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Attributes dict for freemarker_expression ruleset.
freemarker_expression_attributes_dict = {
	"default": "KEYWORD2",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Attributes dict for freemarker_tags ruleset.
freemarker_tags_attributes_dict = {
	"default": "MARKUP",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Attributes dict for freemarker_inquote ruleset.
freemarker_inquote_attributes_dict = {
	"default": "MARKUP",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Attributes dict for freemarker_invalid ruleset.
freemarker_invalid_attributes_dict = {
	"default": "INVALID",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for freemarker mode.
attributesDictDict = {
	"freemarker_expression": freemarker_expression_attributes_dict,
	"freemarker_inquote": freemarker_inquote_attributes_dict,
	"freemarker_invalid": freemarker_invalid_attributes_dict,
	"freemarker_main": freemarker_main_attributes_dict,
	"freemarker_tags": freemarker_tags_attributes_dict,
}

# Keywords dict for freemarker_main ruleset.
freemarker_main_keywords_dict = {}

# Keywords dict for freemarker_expression ruleset.
freemarker_expression_keywords_dict = {
	"as": "keyword1",
	"false": "keyword1",
	"gt": "operator",
	"gte": "operator",
	"in": "keyword1",
	"lt": "operator",
	"lte": "operator",
	"true": "keyword1",
	"using": "keyword1",
}

# Keywords dict for freemarker_tags ruleset.
freemarker_tags_keywords_dict = {}

# Keywords dict for freemarker_inquote ruleset.
freemarker_inquote_keywords_dict = {}

# Keywords dict for freemarker_invalid ruleset.
freemarker_invalid_keywords_dict = {}

# Dictionary of keywords dictionaries for freemarker mode.
keywordsDictDict = {
	"freemarker_expression": freemarker_expression_keywords_dict,
	"freemarker_inquote": freemarker_inquote_keywords_dict,
	"freemarker_invalid": freemarker_invalid_keywords_dict,
	"freemarker_main": freemarker_main_keywords_dict,
	"freemarker_tags": freemarker_tags_keywords_dict,
}

# Rules for freemarker_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="html::JAVASCRIPT",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<Script", end="</Script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="html::JAVASCRIPT",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<SCRIPT", end="</SCRIPT>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="html::JAVASCRIPT",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<style", end="</style>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="html::CSS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<Style", end="</Style>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="html::CSS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<STYLE", end="</STYLE>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="html::CSS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind="comment2", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="xml::DTD-TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule7(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="<!", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="xml::DTD-TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule8(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword1", begin="${", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="EXPRESSION",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule9(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword1", begin="#{", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="EXPRESSION",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule10(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword1", begin="<#ftl\\>", end=">", hash_char="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="EXPRESSION",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule11(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword1", begin="<#?(if|elseif|switch|foreach|list|case|assign|local|global|setting|include|import|stop|escape|macro|function|transform|call|visit|recurse)(\\s|/|$)", end=">", hash_char="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="EXPRESSION",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule12(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword1", begin="</#?(assign|local|global|if|switch|foreach|list|escape|macro|function|transform|compress|noescape)\\>", end=">", hash_char="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="INVALID",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule13(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword1", begin="<#?(else|compress|noescape|default|break|flush|nested|t|rt|lt|return|recurse)\\>", end=">", hash_char="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="INVALID",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule14(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword1", begin="</@(([_@[:alpha:]][_@[:alnum:]]*)(\\.[_@[:alpha:]][_@[:alnum:]]*)*)?", end=">", hash_char="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="INVALID",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule15(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword1", begin="<@([_@[:alpha:]][_@[:alnum:]]*)(\\.[_@[:alpha:]][_@[:alnum:]]*)*", end=">", hash_char="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="EXPRESSION",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule16(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<#--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="<stop>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<comment>", end="</comment>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule19(colorer, s, i):
    return colorer.match_span(s, i, kind="invalid", begin="<#", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule20(colorer, s, i):
    return colorer.match_span(s, i, kind="invalid", begin="</#", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule21(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules dict for main ruleset.
rulesDict1 = {
	"#": [rule9,],
	"$": [rule8,],
	"<": [rule0,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,],
}

# Rules for freemarker_expression ruleset.

def rule22(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<#--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule23(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule24(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule25(colorer, s, i):
    return colorer.match_span(s, i, kind="operator", begin="(", end=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="EXPRESSION",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule31(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule32(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule33(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule34(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule35(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule36(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule37(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule38(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule39(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule40(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule41(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule42(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule43(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule44(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule45(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule46(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="function", pattern="?",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule47(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for expression ruleset.
rulesDict2 = {
	"!": [rule27,],
	"\"": [rule24,],
	"%": [rule36,],
	"&": [rule29,],
	"(": [rule25,],
	"*": [rule32,],
	"+": [rule35,],
	"-": [rule34,],
	".": [rule37,rule39,rule40,],
	"/": [rule33,],
	"0": [rule47,],
	"1": [rule47,],
	"2": [rule47,],
	"3": [rule47,],
	"4": [rule47,],
	"5": [rule47,],
	"6": [rule47,],
	"7": [rule47,],
	"8": [rule47,],
	"9": [rule47,],
	":": [rule38,],
	";": [rule45,],
	"<": [rule22,rule23,rule30,],
	"=": [rule26,],
	">": [rule31,],
	"?": [rule46,],
	"@": [rule47,],
	"A": [rule47,],
	"B": [rule47,],
	"C": [rule47,],
	"D": [rule47,],
	"E": [rule47,],
	"F": [rule47,],
	"G": [rule47,],
	"H": [rule47,],
	"I": [rule47,],
	"J": [rule47,],
	"K": [rule47,],
	"L": [rule47,],
	"M": [rule47,],
	"N": [rule47,],
	"O": [rule47,],
	"P": [rule47,],
	"Q": [rule47,],
	"R": [rule47,],
	"S": [rule47,],
	"T": [rule47,],
	"U": [rule47,],
	"V": [rule47,],
	"W": [rule47,],
	"X": [rule47,],
	"Y": [rule47,],
	"Z": [rule47,],
	"[": [rule41,],
	"]": [rule42,],
	"a": [rule47,],
	"b": [rule47,],
	"c": [rule47,],
	"d": [rule47,],
	"e": [rule47,],
	"f": [rule47,],
	"g": [rule47,],
	"h": [rule47,],
	"i": [rule47,],
	"j": [rule47,],
	"k": [rule47,],
	"l": [rule47,],
	"m": [rule47,],
	"n": [rule47,],
	"o": [rule47,],
	"p": [rule47,],
	"q": [rule47,],
	"r": [rule47,],
	"s": [rule47,],
	"t": [rule47,],
	"u": [rule47,],
	"v": [rule47,],
	"w": [rule47,],
	"x": [rule47,],
	"y": [rule47,],
	"z": [rule47,],
	"{": [rule43,],
	"|": [rule28,],
	"}": [rule44,],
}

# Rules for freemarker_tags ruleset.

def rule48(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="INQUOTE",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule49(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="INQUOTE",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule50(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

# Rules dict for tags ruleset.
rulesDict3 = {
	"\"": [rule48,],
	"'": [rule49,],
	"=": [rule50,],
}

# Rules for freemarker_inquote ruleset.

def rule51(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword1", begin="${", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="EXPRESSION",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule52(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword1", begin="#{", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="EXPRESSION",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules dict for inquote ruleset.
rulesDict4 = {
	"#": [rule52,],
	"$": [rule51,],
}

# Rules for freemarker_invalid ruleset.

# Rules dict for invalid ruleset.
rulesDict5 = {}

# x.rulesDictDict for freemarker mode.
rulesDictDict = {
	"freemarker_expression": rulesDict2,
	"freemarker_inquote": rulesDict4,
	"freemarker_invalid": rulesDict5,
	"freemarker_main": rulesDict1,
	"freemarker_tags": rulesDict3,
}

# Import dict for freemarker mode.
importDict = {}

