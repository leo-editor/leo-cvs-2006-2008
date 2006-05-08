# Leo colorizer control file for smalltalk mode.

# Properties for smalltalk mode.
properties = {
	"commentEnd": "\"",
	"commentStart": "\"",
	"indentCloseBrackets": "]",
	"indentOpenBrackets": "[",
	"lineUpClosingBracket": "true",
}

# Keywords dict for smalltalk_main ruleset.
smalltalk_main_keywords_dict = {
	"Array": "literal2",
	"Boolean": "literal2",
	"Character": "literal2",
	"Date": "literal2",
	"False": "literal2",
	"Integer": "literal2",
	"Object": "literal2",
	"Smalltalk": "literal2",
	"String": "literal2",
	"Symbol": "literal2",
	"Time": "literal2",
	"Transcript": "literal2",
	"True": "literal2",
	"false": "keyword1",
	"isNil": "keyword3",
	"nil": "keyword1",
	"not": "keyword3",
	"self": "keyword2",
	"super": "keyword2",
	"true": "keyword1",
}

# Dictionary of keywords dictionaries for smalltalk mode.
keywordsDictDict = {
	"smalltalk_main": smalltalk_main_keywords_dict,
}

# Rules for smalltalk_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="_",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="==",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="keyword3", pattern=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule15(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="label", pattern="#"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule16(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="literal1", pattern="$"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule17(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for smalltalk_main ruleset.
smalltalk_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, ]

# Rules dict for smalltalk mode.
rulesDict = {
	"smalltalk_main": smalltalk_main_rules,
}

# Import dict for smalltalk mode.
importDict = {}

