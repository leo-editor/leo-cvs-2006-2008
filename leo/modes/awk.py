# Leo colorizer control file for awk mode.

# Properties for awk mode.
properties = {
	"indentCloseBrackets": "}",
	"indentOpenBrackets": "{",
	"lineComment": "#",
	"lineUpClosingBracket": "true",
	"wordBreakChars": ",+-=<>/?^&*",
}

# Keywords dict for awk_main ruleset.
awk_main_keywords_dict = {
	"$0": "keyword3",
	"ARGC": "keyword3",
	"ARGIND": "keyword3",
	"ARGV": "keyword3",
	"BEGIN": "keyword3",
	"CONVFMT": "keyword3",
	"END": "keyword3",
	"ENVIRON": "keyword3",
	"ERRNO": "keyword3",
	"FIELDSWIDTH": "keyword3",
	"FILENAME": "keyword3",
	"FNR": "keyword3",
	"FS": "keyword3",
	"IGNORECASE": "keyword3",
	"NF": "keyword3",
	"NR": "keyword3",
	"OFMT": "keyword3",
	"OFS": "keyword3",
	"ORS": "keyword3",
	"RLENGTH": "keyword3",
	"RS": "keyword3",
	"RSTART": "keyword3",
	"RT": "keyword3",
	"SUBSEP": "keyword3",
	"atan2": "keyword2",
	"break": "keyword1",
	"close": "keyword1",
	"continue": "keyword1",
	"cos": "keyword2",
	"delete": "keyword1",
	"do": "keyword1",
	"else": "keyword1",
	"exit": "keyword1",
	"exp": "keyword2",
	"fflush": "keyword1",
	"for": "keyword1",
	"function": "keyword1",
	"gensub": "keyword2",
	"getline": "keyword2",
	"gsub": "keyword2",
	"huge": "keyword1",
	"if": "keyword1",
	"in": "keyword1",
	"index": "keyword2",
	"int": "keyword2",
	"length": "keyword2",
	"log": "keyword2",
	"match": "keyword2",
	"next": "keyword1",
	"nextfile": "keyword1",
	"print": "keyword1",
	"printf": "keyword1",
	"rand": "keyword2",
	"return": "keyword1",
	"sin": "keyword2",
	"split": "keyword2",
	"sprintf": "keyword2",
	"sqrt": "keyword2",
	"srand": "keyword2",
	"sub": "keyword2",
	"substr": "keyword2",
	"system": "keyword2",
	"tolower": "keyword2",
	"toupper": "keyword2",
	"while": "keyword1",
}

# Rules for awk_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="'", end="'",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment1"', seq="#",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind='"label"',
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=True)

def rule21(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for awk_main ruleset.
awk_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
	rule20, rule21, ]

# Rules dict for awk mode.
rulesDict = {
	"awk_main": awk_main_rules,
}

# Import dict for awk mode.
importDict = {}

