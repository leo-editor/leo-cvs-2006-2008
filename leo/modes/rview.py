# Leo colorizer control file for rview mode.

# Properties for rview mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"indentCloseBrackets": "}",
	"indentOpenBrackets": "{",
	"lineComment": "//",
	"lineUpClosingBracket": "true",
}

# Keywords dict for rview_main ruleset.
rview_main_keywords_dict = {
	"BIGINT": "keyword3",
	"BINARY": "keyword3",
	"BIT": "keyword3",
	"CHAR": "keyword3",
	"DATE": "keyword3",
	"DECIMAL": "keyword3",
	"DOUBLE": "keyword3",
	"FLOAT": "keyword3",
	"INTEGER": "keyword3",
	"LONGVARBINARY": "keyword3",
	"LONGVARCHAR": "keyword3",
	"NUMERIC": "keyword3",
	"REAL": "keyword3",
	"SMALLINT": "keyword3",
	"TIME": "keyword3",
	"TIMESTAMP": "keyword3",
	"TINYINT": "keyword3",
	"VARBINARY": "keyword3",
	"VARCHAR": "keyword3",
	"allow": "keyword1",
	"boolean": "keyword3",
	"byte": "keyword3",
	"case": "keyword1",
	"char": "keyword3",
	"class": "keyword1",
	"constraints": "keyword1",
	"delete": "keyword1",
	"distinct": "keyword1",
	"double": "keyword3",
	"float": "keyword3",
	"function": "keyword1",
	"insert": "keyword1",
	"int": "keyword3",
	"join": "keyword1",
	"jointype": "keyword1",
	"leftouter": "keyword1",
	"long": "keyword3",
	"orderby": "keyword1",
	"query": "keyword1",
	"relationalview": "keyword1",
	"return": "keyword1",
	"rightouter": "keyword1",
	"rowmap": "keyword1",
	"select": "keyword1",
	"short": "keyword3",
	"sql": "keyword1",
	"subview": "keyword1",
	"switch": "keyword1",
	"table": "keyword1",
	"unique": "keyword1",
	"update": "keyword1",
	"useCallableStatement": "keyword1",
	"where": "keyword1",
}

# Keywords dict for rview_rviewstmt ruleset.
rview_rviewstmt_keywords_dict = {
	"AND": "keyword1",
	"BETWEEN": "keyword1",
	"BIGINT": "keyword3",
	"BINARY": "keyword3",
	"BIT": "keyword3",
	"CHAR": "keyword3",
	"DATE": "keyword3",
	"DECIMAL": "keyword3",
	"DOUBLE": "keyword3",
	"FLOAT": "keyword3",
	"FROM": "keyword1",
	"IN": "keyword1",
	"INTEGER": "keyword3",
	"LONGVARBINARY": "keyword3",
	"LONGVARCHAR": "keyword3",
	"NOT": "keyword1",
	"NUMERIC": "keyword3",
	"REAL": "keyword3",
	"SELECT": "keyword1",
	"SET": "keyword1",
	"SMALLINT": "keyword3",
	"TIME": "keyword3",
	"TIMESTAMP": "keyword3",
	"TINYINT": "keyword3",
	"UPDATE": "keyword1",
	"VARBINARY": "keyword3",
	"VARCHAR": "keyword3",
	"WHERE": "keyword1",
	"call": "keyword1",
	"desc": "keyword1",
}

# Rules for rview_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment1", seq="/**/",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment2"', begin="/**", end="*/",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="JAVADOC",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment1"', begin="/*", end="*/",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="RVIEWSTMT",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind='"function"',
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=True)

def rule8(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment2"', seq="//",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule9(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for rview_main ruleset.
rview_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
]

# Rules for rview_rviewstmt ruleset.

def rule10(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="'", end="'",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq="::",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_mark_following(s, i, kind='"label"', 
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=False)

def rule24(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind='"function"',
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=True)

def rule25(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for rview_rviewstmt ruleset.
rview_rviewstmt_rules = [
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
	rule20, rule21, rule22, rule23, rule24, rule25, ]

# Rules dict for rview mode.
rulesDict = {
	"rview_main": rview_main_rules,
	"rview_rviewstmt": rview_rviewstmt_rules,
}

# Import dict for rview mode.
importDict = {}

