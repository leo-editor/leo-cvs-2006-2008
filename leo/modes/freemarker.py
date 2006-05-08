# Leo colorizer control file for freemarker mode.

# Properties for freemarker mode.
properties = {}

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
    return colorer.match_span_regexp(s, i, kind="keyword1", begin="<#ftl\>", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="EXPRESSION",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule11(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword1", begin="<#?(if|elseif|switch|foreach|list|case|assign|local|global|setting|include|import|stop|escape|macro|function|transform|call|visit|recurse)(\s|/|$)", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="EXPRESSION",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule12(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword1", begin="</#?(assign|local|global|if|switch|foreach|list|escape|macro|function|transform|compress|noescape)\>", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="INVALID",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule13(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword1", begin="<#?(else|compress|noescape|default|break|flush|nested|t|rt|lt|return|recurse)\>", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="INVALID",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule14(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword1", begin="</@(([_@[:alpha:]][_@[:alnum:]]*)(\.[_@[:alpha:]][_@[:alnum:]]*)*)?", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="INVALID",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule15(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword1", begin="<@([_@[:alpha:]][_@[:alnum:]]*)(\.[_@[:alpha:]][_@[:alnum:]]*)*", end=">",
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

# Rules list for freemarker_main ruleset.
freemarker_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
	rule20, rule21, ]

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
    return colorer.match_mark_following(s, i, kind="function", pattern="?"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule47(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for freemarker_expression ruleset.
freemarker_expression_rules = [
	rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30, rule31,
	rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40, rule41,
	rule42, rule43, rule44, rule45, rule46, rule47, ]

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

# Rules list for freemarker_tags ruleset.
freemarker_tags_rules = [
	rule48, rule49, rule50, ]

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

# Rules list for freemarker_inquote ruleset.
freemarker_inquote_rules = [
	rule51, rule52, ]

# Rules for freemarker_invalid ruleset.

# Rules list for freemarker_invalid ruleset.
freemarker_invalid_rules = []

# Rules dict for freemarker mode.
rulesDict = {
	"freemarker_expression": freemarker_expression_rules,
	"freemarker_inquote": freemarker_inquote_rules,
	"freemarker_invalid": freemarker_invalid_rules,
	"freemarker_main": freemarker_main_rules,
	"freemarker_tags": freemarker_tags_rules,
}

# Import dict for freemarker mode.
importDict = {}

