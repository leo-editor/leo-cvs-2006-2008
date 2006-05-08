# Leo colorizer control file for dsssl mode.

# Properties for dsssl mode.
properties = {
	"commentEnd": "-->",
	"commentStart": "<!--",
	"lineComment": ";",
}

# Keywords dict for dsssl_main ruleset.
dsssl_main_keywords_dict = {
	"and": "keyword1",
	"append": "keyword1",
	"attribute-string": "function",
	"attributes:": "label",
	"car": "keyword2",
	"cdr": "keyword2",
	"children": "keyword1",
	"cond": "keyword1",
	"cons": "keyword2",
	"current-node": "function",
	"default": "function",
	"define": "keyword1",
	"element": "function",
	"else": "keyword1",
	"empty-sosofo": "function",
	"eq?": "keyword3",
	"equal?": "keyword3",
	"external-procedure": "function",
	"gi": "function",
	"gi:": "label",
	"if": "keyword1",
	"lambda": "keyword1",
	"let": "keyword1",
	"let*": "keyword1",
	"list": "keyword1",
	"literal": "function",
	"loop": "keyword1",
	"make": "function",
	"mode": "function",
	"node": "function",
	"node-list-empty?": "keyword3",
	"node-list-first": "keyword2",
	"node-list-rest": "keyword2",
	"normalize": "keyword1",
	"not": "keyword1",
	"null?": "keyword3",
	"or": "keyword1",
	"pair?": "keyword3",
	"process-children": "function",
	"process-node-list": "function",
	"quote": "keyword1",
	"root": "function",
	"select-elements": "function",
	"sequence": "function",
	"sosofo-append": "function",
	"with-mode": "function",
	"zero?": "keyword3",
}

# Dictionary of keywords dictionaries for dsssl mode.
keywordsDictDict = {
	"dsssl_main": dsssl_main_keywords_dict,
}

# Rules for dsssl_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq="'(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule3(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="literal1", pattern="'"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="$", end="$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="%", end="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule7(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="literal2", pattern="#"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule8(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="<!ENTITY", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="xml::ENTITY-TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule9(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="<![CDATA[", end="]]>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="xml::CDATA",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule10(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="<!", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="xml::DTD-TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="</style-specification", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="xml::TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule13(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="</style-sheet", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="xml::TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule14(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<style-specification", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="xml::TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule15(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<external-specification", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="xml::TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule16(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<style-sheet", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="xml::TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule17(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="&", end=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=True)

def rule18(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for dsssl_main ruleset.
dsssl_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, ]

# Rules dict for dsssl mode.
rulesDict = {
	"dsssl_main": dsssl_main_rules,
}

# Import dict for dsssl mode.
importDict = {}

