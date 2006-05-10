# Leo colorizer control file for xsl mode.
# This file is in the public domain.

# Properties for xsl mode.
properties = {
	"commentEnd": "-->",
	"commentStart": "<!--",
}

# Attributes dict for xsl_main ruleset.
xsl_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "false",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Attributes dict for xsl_tasks ruleset.
xsl_tasks_attributes_dict = {
	"default": "COMMENT1",
	"digit_re": "",
	"highlight_digits": "false",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Attributes dict for xsl_tags ruleset.
xsl_tags_attributes_dict = {
	"default": "MARKUP",
	"digit_re": "",
	"highlight_digits": "false",
	"ignore_case": "false",
	"no_word_sep": ".-_:",
}

# Attributes dict for xsl_avt ruleset.
xsl_avt_attributes_dict = {
	"default": "KEYWORD3",
	"digit_re": "",
	"highlight_digits": "false",
	"ignore_case": "false",
	"no_word_sep": ".-_:",
}

# Attributes dict for xsl_xsltags ruleset.
xsl_xsltags_attributes_dict = {
	"default": "KEYWORD2",
	"digit_re": "",
	"highlight_digits": "false",
	"ignore_case": "false",
	"no_word_sep": ".-_:",
}

# Attributes dict for xsl_xpath ruleset.
xsl_xpath_attributes_dict = {
	"default": "KEYWORD3",
	"digit_re": "[[:digit:]]+([[:punct:]][[:digit:]]+)?",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": ".-_",
}

# Attributes dict for xsl_xpathcomment2 ruleset.
xsl_xpathcomment2_attributes_dict = {
	"default": "COMMENT2",
	"digit_re": "[[:digit:]]+([[:punct:]][[:digit:]]+)?",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": ".-_",
}

# Attributes dict for xsl_xpathcomment3 ruleset.
xsl_xpathcomment3_attributes_dict = {
	"default": "COMMENT3",
	"digit_re": "[[:digit:]]+([[:punct:]][[:digit:]]+)?",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": ".-_",
}

# Dictionary of attributes dictionaries for xsl mode.
attributesDictDict = {
	"xsl_avt": xsl_avt_attributes_dict,
	"xsl_main": xsl_main_attributes_dict,
	"xsl_tags": xsl_tags_attributes_dict,
	"xsl_tasks": xsl_tasks_attributes_dict,
	"xsl_xpath": xsl_xpath_attributes_dict,
	"xsl_xpathcomment2": xsl_xpathcomment2_attributes_dict,
	"xsl_xpathcomment3": xsl_xpathcomment3_attributes_dict,
	"xsl_xsltags": xsl_xsltags_attributes_dict,
}

# Keywords dict for xsl_main ruleset.
xsl_main_keywords_dict = {}

# Keywords dict for xsl_tasks ruleset.
xsl_tasks_keywords_dict = {
	"???": "comment4",
	"DEBUG:": "comment4",
	"DONE:": "comment4",
	"FIXME:": "comment4",
	"IDEA:": "comment4",
	"NOTE:": "comment4",
	"QUESTION:": "comment4",
	"TODO:": "comment4",
	"XXX": "comment4",
}

# Keywords dict for xsl_tags ruleset.
xsl_tags_keywords_dict = {}

# Keywords dict for xsl_avt ruleset.
xsl_avt_keywords_dict = {}

# Keywords dict for xsl_xsltags ruleset.
xsl_xsltags_keywords_dict = {
	"analyze-string": "keyword1",
	"apply-imports": "keyword1",
	"apply-templates": "keyword1",
	"attribute": "keyword1",
	"attribute-set": "keyword1",
	"call-template": "keyword1",
	"character-map": "keyword1",
	"choose": "keyword1",
	"comment": "keyword1",
	"copy": "keyword1",
	"copy-of": "keyword1",
	"date-format": "keyword1",
	"decimal-format": "keyword1",
	"element": "keyword1",
	"fallback": "keyword1",
	"for-each": "keyword1",
	"for-each-group": "keyword1",
	"function": "keyword1",
	"if": "keyword1",
	"import": "keyword1",
	"import-schema": "keyword1",
	"include": "keyword1",
	"key": "keyword1",
	"matching-substring": "keyword1",
	"message": "keyword1",
	"namespace": "keyword1",
	"namespace-alias": "keyword1",
	"next-match": "keyword1",
	"non-matching-substring": "keyword1",
	"number": "keyword1",
	"otherwise": "keyword1",
	"output": "keyword1",
	"output-character": "keyword1",
	"param": "keyword1",
	"preserve-space": "keyword1",
	"processing-instruction": "keyword1",
	"result-document": "keyword1",
	"sequence": "keyword1",
	"sort": "keyword1",
	"sort-key": "keyword1",
	"strip-space": "keyword1",
	"stylesheet": "keyword1",
	"template": "keyword1",
	"text": "keyword1",
	"transform": "keyword1",
	"value-of": "keyword1",
	"variable": "keyword1",
	"when": "keyword1",
	"with-param": "keyword1",
}

# Keywords dict for xsl_xpath ruleset.
xsl_xpath_keywords_dict = {
	"-": "operator",
	"and": "operator",
	"as": "operator",
	"castable": "operator",
	"div": "operator",
	"else": "operator",
	"eq": "operator",
	"every": "operator",
	"except": "operator",
	"for": "operator",
	"ge": "operator",
	"gt": "operator",
	"idiv": "operator",
	"if": "operator",
	"in": "operator",
	"instance": "operator",
	"intersect": "operator",
	"is": "operator",
	"isnot": "operator",
	"le": "operator",
	"lt": "operator",
	"mod": "operator",
	"ne": "operator",
	"nillable": "operator",
	"of": "operator",
	"or": "operator",
	"return": "operator",
	"satisfies": "operator",
	"some": "operator",
	"then": "operator",
	"to": "operator",
	"treat": "operator",
	"union": "operator",
}

# Keywords dict for xsl_xpathcomment2 ruleset.
xsl_xpathcomment2_keywords_dict = {}

# Keywords dict for xsl_xpathcomment3 ruleset.
xsl_xpathcomment3_keywords_dict = {}

# Dictionary of keywords dictionaries for xsl mode.
keywordsDictDict = {
	"xsl_avt": xsl_avt_keywords_dict,
	"xsl_main": xsl_main_keywords_dict,
	"xsl_tags": xsl_tags_keywords_dict,
	"xsl_tasks": xsl_tasks_keywords_dict,
	"xsl_xpath": xsl_xpath_keywords_dict,
	"xsl_xpathcomment2": xsl_xpathcomment2_keywords_dict,
	"xsl_xpathcomment3": xsl_xpathcomment3_keywords_dict,
	"xsl_xsltags": xsl_xsltags_keywords_dict,
}

# Rules for xsl_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="TASKS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword2", begin="<(?=xsl:)", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XSLTAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword2", begin="<(?=/xsl:)", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XSLTAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="<![CDATA[", end="]]>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="xml::CDATA",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="<!", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="xml::DTD-TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="literal3", begin="&", end=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=True)

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind="literal3", begin="<?", end="?>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule7(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules dict for main ruleset.
rulesDict1 = {
	"&": [rule5,],
	"<": [rule0,rule1,rule2,rule3,rule4,rule6,rule7,],
}

# Rules for xsl_tasks ruleset.

def rule8(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for tasks ruleset.
rulesDict2 = {
	"0": [rule8,],
	"1": [rule8,],
	"2": [rule8,],
	"3": [rule8,],
	"4": [rule8,],
	"5": [rule8,],
	"6": [rule8,],
	"7": [rule8,],
	"8": [rule8,],
	"9": [rule8,],
	"@": [rule8,],
	"A": [rule8,],
	"B": [rule8,],
	"C": [rule8,],
	"D": [rule8,],
	"E": [rule8,],
	"F": [rule8,],
	"G": [rule8,],
	"H": [rule8,],
	"I": [rule8,],
	"J": [rule8,],
	"K": [rule8,],
	"L": [rule8,],
	"M": [rule8,],
	"N": [rule8,],
	"O": [rule8,],
	"P": [rule8,],
	"Q": [rule8,],
	"R": [rule8,],
	"S": [rule8,],
	"T": [rule8,],
	"U": [rule8,],
	"V": [rule8,],
	"W": [rule8,],
	"X": [rule8,],
	"Y": [rule8,],
	"Z": [rule8,],
	"_": [rule8,],
	"a": [rule8,],
	"b": [rule8,],
	"c": [rule8,],
	"d": [rule8,],
	"e": [rule8,],
	"f": [rule8,],
	"g": [rule8,],
	"h": [rule8,],
	"i": [rule8,],
	"j": [rule8,],
	"k": [rule8,],
	"l": [rule8,],
	"m": [rule8,],
	"n": [rule8,],
	"o": [rule8,],
	"p": [rule8,],
	"q": [rule8,],
	"r": [rule8,],
	"s": [rule8,],
	"t": [rule8,],
	"u": [rule8,],
	"v": [rule8,],
	"w": [rule8,],
	"x": [rule8,],
	"y": [rule8,],
	"z": [rule8,],
}

# Rules for xsl_tags ruleset.

def rule9(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="AVT",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule10(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="AVT",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="xmlns:",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="xmlns",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

# Rules dict for tags ruleset.
rulesDict3 = {
	"\"": [rule9,],
	"'": [rule10,],
	":": [rule13,],
	"x": [rule11,rule12,],
}

# Rules for xsl_avt ruleset.

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="", seq="{{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="", seq="}}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_span(s, i, kind="operator", begin="{", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATH",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule17(colorer, s, i):
    return colorer.match_span(s, i, kind="literal3", begin="&", end=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=True)

# Rules dict for avt ruleset.
rulesDict4 = {
	"&": [rule17,],
	"{": [rule14,rule16,],
	"}": [rule15,],
}

# Rules for xsl_xsltags ruleset.

def rule18(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="AVT",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule19(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="AVT",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule20(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword2", begin="count[[:space:]]*=[[:space:]]*\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATH",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule21(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword2", begin="count[[:space:]]*=[[:space:]]*'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATH",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule22(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword2", begin="from[[:space:]]*=[[:space:]]*\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATH",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule23(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword2", begin="from[[:space:]]*=[[:space:]]*'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATH",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule24(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword2", begin="group-adjacent[[:space:]]*=[[:space:]]*\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATH",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule25(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword2", begin="group-adjacent[[:space:]]*=[[:space:]]*'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATH",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule26(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword2", begin="group-by[[:space:]]*=[[:space:]]*\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATH",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule27(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword2", begin="group-by[[:space:]]*=[[:space:]]*'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATH",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule28(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword2", begin="group-ending-with[[:space:]]*=[[:space:]]*\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATH",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule29(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword2", begin="group-ending-with[[:space:]]*=[[:space:]]*'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATH",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule30(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword2", begin="group-starting-with[[:space:]]*=[[:space:]]*\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATH",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule31(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword2", begin="group-starting-with[[:space:]]*=[[:space:]]*'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATH",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule32(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword2", begin="match[[:space:]]*=[[:space:]]*\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATH",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule33(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword2", begin="match[[:space:]]*=[[:space:]]*'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATH",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule34(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword2", begin="select[[:space:]]*=[[:space:]]*\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATH",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule35(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword2", begin="select[[:space:]]*=[[:space:]]*'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATH",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule36(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword2", begin="test[[:space:]]*=[[:space:]]*\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATH",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule37(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword2", begin="test[[:space:]]*=[[:space:]]*'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATH",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule38(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword2", begin="use[[:space:]]*=[[:space:]]*\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATH",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule39(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword2", begin="use[[:space:]]*=[[:space:]]*'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATH",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule40(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="xmlns:",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule41(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="xmlns",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule42(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule43(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for xsltags ruleset.
rulesDict5 = {
	"\"": [rule18,],
	"'": [rule19,],
	"0": [rule43,],
	"1": [rule43,],
	"2": [rule43,],
	"3": [rule43,],
	"4": [rule43,],
	"5": [rule43,],
	"6": [rule43,],
	"7": [rule43,],
	"8": [rule43,],
	"9": [rule43,],
	":": [rule42,],
	"@": [rule43,],
	"A": [rule43,],
	"B": [rule43,],
	"C": [rule43,],
	"D": [rule43,],
	"E": [rule43,],
	"F": [rule43,],
	"G": [rule43,],
	"H": [rule43,],
	"I": [rule43,],
	"J": [rule43,],
	"K": [rule43,],
	"L": [rule43,],
	"M": [rule43,],
	"N": [rule43,],
	"O": [rule43,],
	"P": [rule43,],
	"Q": [rule43,],
	"R": [rule43,],
	"S": [rule43,],
	"T": [rule43,],
	"U": [rule43,],
	"V": [rule43,],
	"W": [rule43,],
	"X": [rule43,],
	"Y": [rule43,],
	"Z": [rule43,],
	"_": [rule43,],
	"a": [rule43,],
	"b": [rule43,],
	"c": [rule20,rule21,rule43,],
	"d": [rule43,],
	"e": [rule43,],
	"f": [rule22,rule23,rule43,],
	"g": [rule24,rule25,rule26,rule27,rule28,rule29,rule30,rule31,rule43,],
	"h": [rule43,],
	"i": [rule43,],
	"j": [rule43,],
	"k": [rule43,],
	"l": [rule43,],
	"m": [rule32,rule33,rule43,],
	"n": [rule43,],
	"o": [rule43,],
	"p": [rule43,],
	"q": [rule43,],
	"r": [rule43,],
	"s": [rule34,rule35,rule43,],
	"t": [rule36,rule37,rule43,],
	"u": [rule38,rule39,rule43,],
	"v": [rule43,],
	"w": [rule43,],
	"x": [rule40,rule41,rule43,],
	"y": [rule43,],
	"z": [rule43,],
}

# Rules for xsl_xpath ruleset.

def rule44(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule45(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule46(colorer, s, i):
    return colorer.match_span(s, i, kind="comment2", begin="(:", end=":)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATHCOMMENT2",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule47(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="keyword4", pattern="::",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule48(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword4", seq="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule49(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule50(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule51(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule52(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&gt;",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule53(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&lt;",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule54(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="?",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule55(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule56(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule57(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule58(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule59(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule60(colorer, s, i):
    return colorer.match_span(s, i, kind="operator", begin="[", end="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATH",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule61(colorer, s, i):
    return colorer.match_span(s, i, kind="literal3", begin="&", end=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=True)

def rule62(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule63(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule64(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="literal2", pattern="$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule65(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for xpath ruleset.
rulesDict6 = {
	"!": [rule50,],
	"\"": [rule44,],
	"$": [rule64,],
	"&": [rule52,rule53,rule61,],
	"'": [rule45,],
	"(": [rule46,rule63,],
	"*": [rule56,],
	"+": [rule55,],
	",": [rule59,],
	"/": [rule57,],
	"0": [rule65,],
	"1": [rule65,],
	"2": [rule65,],
	"3": [rule65,],
	"4": [rule65,],
	"5": [rule65,],
	"6": [rule65,],
	"7": [rule65,],
	"8": [rule65,],
	"9": [rule65,],
	":": [rule47,rule62,],
	"=": [rule49,],
	">": [rule51,],
	"?": [rule54,],
	"@": [rule48,rule65,],
	"A": [rule65,],
	"B": [rule65,],
	"C": [rule65,],
	"D": [rule65,],
	"E": [rule65,],
	"F": [rule65,],
	"G": [rule65,],
	"H": [rule65,],
	"I": [rule65,],
	"J": [rule65,],
	"K": [rule65,],
	"L": [rule65,],
	"M": [rule65,],
	"N": [rule65,],
	"O": [rule65,],
	"P": [rule65,],
	"Q": [rule65,],
	"R": [rule65,],
	"S": [rule65,],
	"T": [rule65,],
	"U": [rule65,],
	"V": [rule65,],
	"W": [rule65,],
	"X": [rule65,],
	"Y": [rule65,],
	"Z": [rule65,],
	"[": [rule60,],
	"_": [rule65,],
	"a": [rule65,],
	"b": [rule65,],
	"c": [rule65,],
	"d": [rule65,],
	"e": [rule65,],
	"f": [rule65,],
	"g": [rule65,],
	"h": [rule65,],
	"i": [rule65,],
	"j": [rule65,],
	"k": [rule65,],
	"l": [rule65,],
	"m": [rule65,],
	"n": [rule65,],
	"o": [rule65,],
	"p": [rule65,],
	"q": [rule65,],
	"r": [rule65,],
	"s": [rule65,],
	"t": [rule65,],
	"u": [rule65,],
	"v": [rule65,],
	"w": [rule65,],
	"x": [rule65,],
	"y": [rule65,],
	"z": [rule65,],
	"|": [rule58,],
}

# Rules for xsl_xpathcomment2 ruleset.

def rule66(colorer, s, i):
    return colorer.match_span(s, i, kind="comment3", begin="(:", end=":)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATHCOMMENT3",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules dict for xpathcomment2 ruleset.
rulesDict7 = {
	"(": [rule66,],
}

# Rules for xsl_xpathcomment3 ruleset.

def rule67(colorer, s, i):
    return colorer.match_span(s, i, kind="comment2", begin="(:", end=":)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATHCOMMENT2",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules dict for xpathcomment3 ruleset.
rulesDict8 = {
	"(": [rule67,],
}

# x.rulesDictDict for xsl mode.
rulesDictDict = {
	"xsl_avt": rulesDict4,
	"xsl_main": rulesDict1,
	"xsl_tags": rulesDict3,
	"xsl_tasks": rulesDict2,
	"xsl_xpath": rulesDict6,
	"xsl_xpathcomment2": rulesDict7,
	"xsl_xpathcomment3": rulesDict8,
	"xsl_xsltags": rulesDict5,
}

# Import dict for xsl mode.
importDict = {}

