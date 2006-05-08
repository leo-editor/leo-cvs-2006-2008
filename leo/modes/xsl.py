# Leo colorizer control file for xsl mode.

# Properties for xsl mode.
properties = {
	"commentEnd": "-->",
	"commentStart": "<!--",
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

# Rules list for xsl_main ruleset.
xsl_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, ]

# Rules for xsl_tasks ruleset.

def rule8(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for xsl_tasks ruleset.
xsl_tasks_rules = [
	rule8, ]

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

# Rules list for xsl_tags ruleset.
xsl_tags_rules = [
	rule9, rule10, rule11, rule12, rule13, ]

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

# Rules list for xsl_avt ruleset.
xsl_avt_rules = [
	rule14, rule15, rule16, rule17, ]

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

# Rules list for xsl_xsltags ruleset.
xsl_xsltags_rules = [
	rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27,
	rule28, rule29, rule30, rule31, rule32, rule33, rule34, rule35, rule36, rule37,
	rule38, rule39, rule40, rule41, rule42, rule43, ]

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
    return colorer.match_mark_following(s, i, kind="literal2", pattern="$"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule65(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for xsl_xpath ruleset.
xsl_xpath_rules = [
	rule44, rule45, rule46, rule47, rule48, rule49, rule50, rule51, rule52, rule53,
	rule54, rule55, rule56, rule57, rule58, rule59, rule60, rule61, rule62, rule63,
	rule64, rule65, ]

# Rules for xsl_xpathcomment2 ruleset.

def rule66(colorer, s, i):
    return colorer.match_span(s, i, kind="comment3", begin="(:", end=":)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATHCOMMENT3",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules list for xsl_xpathcomment2 ruleset.
xsl_xpathcomment2_rules = [
	rule66, ]

# Rules for xsl_xpathcomment3 ruleset.

def rule67(colorer, s, i):
    return colorer.match_span(s, i, kind="comment2", begin="(:", end=":)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="XPATHCOMMENT2",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules list for xsl_xpathcomment3 ruleset.
xsl_xpathcomment3_rules = [
	rule67, ]

# Rules dict for xsl mode.
rulesDict = {
	"xsl_avt": xsl_avt_rules,
	"xsl_main": xsl_main_rules,
	"xsl_tags": xsl_tags_rules,
	"xsl_tasks": xsl_tasks_rules,
	"xsl_xpath": xsl_xpath_rules,
	"xsl_xpathcomment2": xsl_xpathcomment2_rules,
	"xsl_xpathcomment3": xsl_xpathcomment3_rules,
	"xsl_xsltags": xsl_xsltags_rules,
}

# Import dict for xsl mode.
importDict = {}

