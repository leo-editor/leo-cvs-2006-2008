# Leo colorizer control file for chill mode.

# Properties for chill mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
}

# Keywords dict for chill_main ruleset.
chill_main_keywords_dict = {
	"AND": "keyword1",
	"ARRAY": "keyword2",
	"BEGIN": "keyword1",
	"BIN": "keyword3",
	"BOOL": "keyword3",
	"CASE": "keyword1",
	"CHAR": "keyword3",
	"DCL": "keyword2",
	"DIV": "keyword1",
	"DO": "keyword1",
	"EJECT": "label",
	"ELSE": "keyword1",
	"ELSIF": "keyword1",
	"END": "keyword1",
	"ESAC": "keyword1",
	"EXIT": "keyword1",
	"FALSE": "literal2",
	"FI": "keyword1",
	"FOR": "keyword1",
	"GOTO": "keyword1",
	"GRANT": "keyword2",
	"IF": "keyword1",
	"IN": "keyword1",
	"INT": "keyword3",
	"LABEL": "keyword2",
	"LIO_INFOS": "label",
	"MOD": "keyword1",
	"MODULE": "keyword2",
	"MODULE_DESCRIPTION_HEADER": "label",
	"MSG_XREF": "label",
	"NEWMODE": "keyword2",
	"NOT": "keyword1",
	"NULL": "literal2",
	"OD": "keyword1",
	"OF": "keyword1",
	"ON": "keyword1",
	"OR": "keyword1",
	"OUT": "keyword1",
	"PACK": "keyword2",
	"PATCH_INFOS": "label",
	"POWERSET": "keyword2",
	"PROC": "keyword2",
	"PTR": "keyword3",
	"RANGE": "keyword3",
	"REF": "keyword3",
	"RESULT": "keyword1",
	"RETURN": "keyword1",
	"SEIZE": "keyword2",
	"SET": "keyword2",
	"STRUCT": "keyword2",
	"SWSG_INFOS": "label",
	"SYN": "keyword2",
	"SYNMODE": "keyword2",
	"THEN": "keyword1",
	"TO": "keyword1",
	"TRUE": "literal2",
	"TYPE": "keyword2",
	"UNTIL": "keyword1",
	"USES": "keyword1",
	"WHILE": "keyword1",
	"WITH": "keyword1",
	"XOR": "keyword1",
}

# Rules for chill_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment2"', begin="<>", end="<>",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment1"', begin="/*", end="*/",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="'", end="'",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="H'", end=";",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=")",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="(",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="]",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=";",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for chill_main ruleset.
chill_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
	rule20, rule21, rule22, rule23, rule24, rule25, ]

# Rules dict for chill mode.
rulesDict = {
	"chill_main": chill_main_rules,
}

# Import dict for chill mode.
importDict = {}

