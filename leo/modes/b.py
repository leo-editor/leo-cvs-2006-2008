# Leo colorizer control file for b mode.

# Properties for b mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"indentNextLine": "\s*(((ANY|ASSERT|CASE|CHOICE|IF|LET|PRE|SELECT|VAR|WHILE|WHEN)\s*\(|ELSE|ELSEIF|EITHER|OR|VARIANT|INVARIANT)[^;]*|for\s*\(.*)",
	"lineComment": "//",
}

# Keywords dict for b_main ruleset.
b_main_keywords_dict = {
	"ABSTRACT_CONSTANTS": "keyword2",
	"ABSTRACT_VARIABLES": "keyword2",
	"ANY": "keyword2",
	"ASSERT": "keyword2",
	"ASSERTIONS": "keyword2",
	"BE": "keyword2",
	"BEGIN": "keyword2",
	"CASE": "keyword2",
	"CHOICE": "keyword2",
	"CONCRETE_CONSTANTS": "keyword2",
	"CONCRETE_VARIABLES": "keyword2",
	"CONSTANTS": "keyword2",
	"CONSTRAINTS": "keyword2",
	"DEFINITIONS": "keyword2",
	"DO": "keyword2",
	"EITHER": "keyword2",
	"ELSE": "keyword2",
	"ELSIF": "keyword2",
	"END": "keyword2",
	"EXTENDS": "keyword2",
	"FIN": "keyword3",
	"FIN1": "keyword3",
	"IF": "keyword2",
	"IMPLEMENTATION": "keyword2",
	"IMPORTS": "keyword2",
	"IN": "keyword2",
	"INCLUDES": "keyword2",
	"INITIALISATION": "keyword2",
	"INT": "keyword3",
	"INTEGER": "keyword3",
	"INTER": "keyword3",
	"INVARIANT": "keyword2",
	"LET": "keyword2",
	"LOCAL_OPERATIONS": "keyword2",
	"MACHINE": "keyword2",
	"MAXINT": "keyword3",
	"MININT": "keyword3",
	"NAT": "keyword3",
	"NAT1": "keyword3",
	"NATURAL": "keyword3",
	"NATURAL1": "keyword3",
	"OF": "keyword2",
	"OPERATIONS": "keyword2",
	"OR": "keyword2",
	"PI": "keyword3",
	"POW": "keyword3",
	"POW1": "keyword3",
	"PRE": "keyword2",
	"PROMOTES": "keyword2",
	"PROPERTIES": "keyword2",
	"REFINEMENT": "keyword2",
	"REFINES": "keyword2",
	"SEES": "keyword2",
	"SELECT": "keyword2",
	"SETS": "keyword2",
	"SIGMA": "keyword3",
	"THEN": "keyword2",
	"UNION": "keyword3",
	"USES": "keyword2",
	"VALUES": "keyword2",
	"VAR": "keyword2",
	"VARIABLES": "keyword2",
	"VARIANT": "keyword2",
	"WHEN": "keyword2",
	"WHERE": "keyword2",
	"WHILE": "keyword2",
	"arity": "function",
	"bin": "function",
	"bool": "function",
	"btree": "function",
	"card": "function",
	"closure": "function",
	"closure1": "function",
	"conc": "function",
	"const": "function",
	"dom": "function",
	"father": "function",
	"first": "function",
	"fnc": "function",
	"front": "function",
	"id": "function",
	"infix": "function",
	"inter": "function",
	"iseq": "function",
	"iseq1": "function",
	"iterate": "function",
	"last": "function",
	"left": "function",
	"max": "function",
	"min": "function",
	"mirror": "function",
	"mod": "function",
	"not": "function",
	"or": "function",
	"perm": "function",
	"postfix": "function",
	"pred": "function",
	"prefix": "function",
	"prj1": "function",
	"prj2": "function",
	"ran": "function",
	"rank": "function",
	"rec": "function",
	"rel": "function",
	"rev": "function",
	"right": "function",
	"r~": "function",
	"seq": "function",
	"seq1": "function",
	"size": "function",
	"sizet": "function",
	"skip": "function",
	"son": "function",
	"sons": "function",
	"struct": "function",
	"subtree": "function",
	"succ": "function",
	"tail": "function",
	"top": "function",
	"tree": "function",
	"union": "function",
}

# Dictionary of keywords dictionaries for b mode.
keywordsDictDict = {
	"b_main": b_main_keywords_dict,
}

# Rules for b_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment3", begin="/*?", end="?*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="$0",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule31(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for b_main ruleset.
b_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
	rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29,
	rule30, rule31, ]

# Rules dict for b mode.
rulesDict = {
	"b_main": b_main_rules,
}

# Import dict for b mode.
importDict = {}

