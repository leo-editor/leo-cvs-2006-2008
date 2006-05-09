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

# Dictionary of keywords dictionaries for rview mode.
keywordsDictDict = {
	"rview_main": rview_main_keywords_dict,
	"rview_rviewstmt": rview_rviewstmt_keywords_dict,
}

# Rules for rview_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment1", seq="/**/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment2", begin="/**", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="JAVADOC",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="RVIEWSTMT",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule8(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule9(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"\"": [rule3,],
	"(": [rule7,],
	"/": [rule0,rule1,rule2,rule8,],
	"0": [rule9,],
	"1": [rule9,],
	"2": [rule9,],
	"3": [rule9,],
	"4": [rule9,],
	"5": [rule9,],
	"6": [rule9,],
	"7": [rule9,],
	"8": [rule9,],
	"9": [rule9,],
	"=": [rule6,],
	"@": [rule9,],
	"A": [rule9,],
	"B": [rule9,],
	"C": [rule9,],
	"D": [rule9,],
	"E": [rule9,],
	"F": [rule9,],
	"G": [rule9,],
	"H": [rule9,],
	"I": [rule9,],
	"J": [rule9,],
	"K": [rule9,],
	"L": [rule9,],
	"M": [rule9,],
	"N": [rule9,],
	"O": [rule9,],
	"P": [rule9,],
	"Q": [rule9,],
	"R": [rule9,],
	"S": [rule9,],
	"T": [rule9,],
	"U": [rule9,],
	"V": [rule9,],
	"W": [rule9,],
	"X": [rule9,],
	"Y": [rule9,],
	"Z": [rule9,],
	"_": [rule9,],
	"a": [rule9,],
	"b": [rule9,],
	"c": [rule9,],
	"d": [rule9,],
	"e": [rule9,],
	"f": [rule9,],
	"g": [rule9,],
	"h": [rule9,],
	"i": [rule9,],
	"j": [rule9,],
	"k": [rule9,],
	"l": [rule9,],
	"m": [rule9,],
	"n": [rule9,],
	"o": [rule9,],
	"p": [rule9,],
	"q": [rule9,],
	"r": [rule9,],
	"s": [rule9,],
	"t": [rule9,],
	"u": [rule9,],
	"v": [rule9,],
	"w": [rule9,],
	"x": [rule9,],
	"y": [rule9,],
	"z": [rule9,],
	"{": [rule5,],
	"}": [rule4,],
}

# Rules for rview_rviewstmt ruleset.

def rule10(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq="::",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="label", pattern=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule24(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule25(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for rviewstmt ruleset.
rulesDict2 = {
	"'": [rule10,],
	"(": [rule24,],
	"*": [rule14,],
	"+": [rule11,],
	"-": [rule12,],
	"/": [rule13,],
	"0": [rule25,],
	"1": [rule25,],
	"2": [rule25,],
	"3": [rule25,],
	"4": [rule25,],
	"5": [rule25,],
	"6": [rule25,],
	"7": [rule25,],
	"8": [rule25,],
	"9": [rule25,],
	":": [rule22,rule23,],
	"<": [rule17,rule19,],
	"=": [rule15,],
	">": [rule16,rule18,],
	"@": [rule25,],
	"A": [rule25,],
	"B": [rule25,],
	"C": [rule25,],
	"D": [rule25,],
	"E": [rule25,],
	"F": [rule25,],
	"G": [rule25,],
	"H": [rule25,],
	"I": [rule25,],
	"J": [rule25,],
	"K": [rule25,],
	"L": [rule25,],
	"M": [rule25,],
	"N": [rule25,],
	"O": [rule25,],
	"P": [rule25,],
	"Q": [rule25,],
	"R": [rule25,],
	"S": [rule25,],
	"T": [rule25,],
	"U": [rule25,],
	"V": [rule25,],
	"W": [rule25,],
	"X": [rule25,],
	"Y": [rule25,],
	"Z": [rule25,],
	"_": [rule25,],
	"a": [rule25,],
	"b": [rule25,],
	"c": [rule25,],
	"d": [rule25,],
	"e": [rule25,],
	"f": [rule25,],
	"g": [rule25,],
	"h": [rule25,],
	"i": [rule25,],
	"j": [rule25,],
	"k": [rule25,],
	"l": [rule25,],
	"m": [rule25,],
	"n": [rule25,],
	"o": [rule25,],
	"p": [rule25,],
	"q": [rule25,],
	"r": [rule25,],
	"s": [rule25,],
	"t": [rule25,],
	"u": [rule25,],
	"v": [rule25,],
	"w": [rule25,],
	"x": [rule25,],
	"y": [rule25,],
	"z": [rule25,],
	"{": [rule21,],
	"}": [rule20,],
}

# x.rulesDictDict for rview mode.
rulesDictDict = {
	"rview_main": rulesDict1,
	"rview_rviewstmt": rulesDict2,
}

# Import dict for rview mode.
importDict = {}

