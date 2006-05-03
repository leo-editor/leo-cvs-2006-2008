# Leo colorizer control file for shellscript mode.

# Properties for shellscript mode.
properties = {
	"indentCloseBrackets": "}",
	"indentOpenBrackets": "{",
	"lineComment": "#",
	"lineUpClosingBracket": "true",
}

# Keywords dict for shellscript_main ruleset.
shellscript_main_keywords_dict = {
	";;": "operator",
	"case": "keyword1",
	"continue": "keyword1",
	"do": "keyword1",
	"done": "keyword1",
	"elif": "keyword1",
	"else": "keyword1",
	"esac": "keyword1",
	"fi": "keyword1",
	"for": "keyword1",
	"if": "keyword1",
	"in": "keyword1",
	"local": "keyword1",
	"return": "keyword1",
	"then": "keyword1",
	"while": "keyword1",
}

# Keywords dict for shellscript_literal ruleset.
shellscript_literal_keywords_dict = {}

# Keywords dict for shellscript_exec ruleset.
shellscript_exec_keywords_dict = {}

# Rules for shellscript_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment2"', seq="#!",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment1"', seq="#",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword2"', begin="${", end="}",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_mark_following(s, i, kind='"keyword2"', 
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_mark_following(s, i, kind='"keyword2"', 
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=False)

def rule5(colorer, s, i):
    return colorer.match_mark_following(s, i, kind='"keyword2"', 
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=False)

def rule6(colorer, s, i):
    return colorer.match_mark_following(s, i, kind='"keyword2"', 
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=False)

def rule7(colorer, s, i):
    return colorer.match_mark_following(s, i, kind='"keyword2"', 
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=False)

def rule8(colorer, s, i):
    return colorer.match_mark_following(s, i, kind='"keyword2"', 
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=False)

def rule9(colorer, s, i):
    return colorer.match_mark_following(s, i, kind='"keyword2"', 
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=False)

def rule10(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind='"keyword2"',
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=True)

def rule11(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword3"', begin="$((", end="))",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="EXEC",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule12(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword3"', begin="$(", end=")",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="EXEC",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule13(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword3"', begin="$[", end="]",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="EXEC",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule14(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword3"', begin="`", end="`",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="EXEC",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule15(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule16(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="'", end="'",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule17(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind='"literal1"', begin="<<[[:space:]'\"]*([[:alnum:]_]+)[[:space:]'\"]*", end="$1",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_mark_following(s, i, kind='"keyword2"', 
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=False)

def rule24(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind='"function"',
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=True)

def rule25(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for shellscript_main ruleset.
shellscript_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
	rule20, rule21, rule22, rule23, rule24, rule25, ]

# Rules for shellscript_literal ruleset.

def rule26(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword2"', begin="${", end="}",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule27(colorer, s, i):
    return colorer.match_mark_following(s, i, kind='"keyword2"', 
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=False)

# Rules list for shellscript_literal ruleset.
shellscript_literal_rules = [
	rule26, rule27, ]

# Rules for shellscript_exec ruleset.

def rule28(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword2"', begin="${", end="}",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule29(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword3"', begin="$((", end="))",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule30(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword3"', begin="$(", end=")",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule31(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword3"', begin="$[", end="]",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule32(colorer, s, i):
    return colorer.match_mark_following(s, i, kind='"keyword2"', 
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=False)

def rule33(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule34(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule35(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule36(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule37(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

# Rules list for shellscript_exec ruleset.
shellscript_exec_rules = [
	rule28, rule29, rule30, rule31, rule32, rule33, rule34, rule35, rule36, rule37,
]

# Rules dict for shellscript mode.
rulesDict = {
	"shellscript_exec": shellscript_exec_rules,
	"shellscript_literal": shellscript_literal_rules,
	"shellscript_main": shellscript_main_rules,
}

# Import dict for shellscript mode.
importDict = {}

