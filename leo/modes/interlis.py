# Leo colorizer control file for interlis mode.

# Properties for interlis mode.
properties = {
	"blockComment": "!!",
	"commentEnd": "*/",
	"commentStart": "/*",
}

# Keywords dict for interlis_main ruleset.
interlis_main_keywords_dict = {
	"		": "keywords",
	"			": "keywords",
	"
": "keywords",
	"ABSTRACT": "keyword1",
	"ACCORDING": "keyword1",
	"AGGREGATES": "keyword1",
	"AGGREGATION": "keyword1",
	"ALL": "keyword1",
	"AND": "keyword1",
	"ANY": "keyword1",
	"ARCS": "keyword1",
	"AREA": "keyword1",
	"ASSOCIATION": "keyword1",
	"ATTRIBUTE": "keyword1",
	"ATTRIBUTES": "keyword1",
	"BAG": "keyword1",
	"BASE": "keyword1",
	"BASED": "keyword1",
	"BASKET": "keyword1",
	"BLANK": "keyword1",
	"BOOLEAN": "keyword1",
	"BY": "keyword1",
	"CIRCULAR": "keyword1",
	"CLASS": "keyword1",
	"CLOCKWISE": "keyword1",
	"CODE": "keyword1",
	"CONSTRAINT": "keyword1",
	"CONSTRAINTS": "keyword1",
	"CONTINUE": "keyword1",
	"CONTINUOUS": "keyword1",
	"CONTOUR": "keyword1",
	"CONTRACT": "keyword1",
	"COORD": "keyword1",
	"COORD2": "keyword1",
	"COORD3": "keyword1",
	"COUNTERCLOCKWISE": "keyword1",
	"DATE": "keyword1",
	"DEFAULT": "keyword1",
	"DEFINED": "keyword1",
	"DEGREES": "keyword1",
	"DEPENDS": "keyword1",
	"DERIVATIVES": "keyword1",
	"DERIVED": "keyword1",
	"DIM1": "keyword1",
	"DIM2": "keyword1",
	"DIRECTED": "keyword1",
	"DOMAIN": "keyword1",
	"END": "keyword1",
	"EQUAL": "keyword1",
	"EXISTENCE": "keyword1",
	"EXTENDS": "keyword1",
	"FIRST": "keyword1",
	"FIX": "keyword1",
	"FONT": "keyword1",
	"FORM": "keyword1",
	"FORMAT": "keyword1",
	"FREE": "keyword1",
	"FROM": "keyword1",
	"FUNCTION": "keyword1",
	"GRADS": "keyword1",
	"GRAPHIC": "keyword1",
	"HALIGNMENT": "keyword1",
	"I16": "keyword1",
	"I32": "keyword1",
	"IDENT": "keyword1",
	"IMPORTS": "keyword1",
	"IN": "keyword1",
	"INSPECTION": "keyword1",
	"INTERLIS": "keyword1",
	"ISSUED": "keyword1",
	"JOIN": "keyword1",
	"LAST": "keyword1",
	"LINE": "keyword1",
	"LINEATTR": "keyword1",
	"LINESIZE": "keyword1",
	"LIST": "keyword1",
	"LNBASE": "keyword1",
	"MANDATORY": "keyword1",
	"METAOBJECT": "keyword1",
	"MODEL": "keyword1",
	"NAME": "keyword1",
	"NO": "keyword1",
	"NOT": "keyword1",
	"NULL": "keyword1",
	"NUMERIC": "keyword1",
	"OBJECT": "keyword1",
	"OF": "keyword1",
	"ON": "keyword1",
	"OPTIONAL": "keyword1",
	"OR": "keyword1",
	"ORDERED": "keyword1",
	"OVERLAPS": "keyword1",
	"PARAMETER": "keyword1",
	"PARENT": "keyword1",
	"PATTERN": "keyword1",
	"PERIPHERY": "keyword1",
	"PI": "keyword1",
	"POLYLINE": "keyword1",
	"PREFIX": "keyword1",
	"PROJECTION": "keyword1",
	"RADIANS": "keyword1",
	"REFERENCE": "keyword1",
	"REFSYSTEM": "keyword1",
	"REQUIRED": "keyword1",
	"RESTRICTED": "keyword1",
	"ROTATION": "keyword1",
	"SELECTION": "keyword1",
	"SIGN": "keyword1",
	"STRAIGHTS": "keyword1",
	"STRUCTURE": "keyword1",
	"SURFACE": "keyword1",
	"SYMBOLOGY": "keyword1",
	"TABLE": "keyword1",
	"TEXT": "keyword1",
	"THATAREA": "keyword1",
	"THIS": "keyword1",
	"THISAREA": "keyword1",
	"TID": "keyword1",
	"TIDSIZE": "keyword1",
	"TO": "keyword1",
	"TOPIC": "keyword1",
	"TRANSFER": "keyword1",
	"TRANSLATION": "keyword1",
	"TYPE": "keyword1",
	"UNDEFINED": "keyword1",
	"UNION": "keyword1",
	"UNIQUE": "keyword1",
	"UNIT": "keyword1",
	"URI": "keyword1",
	"USES": "keyword1",
	"VALIGNMENT": "keyword1",
	"VERTEX": "keyword1",
	"VERTEXINFO": "keyword1",
	"VIEW": "keyword1",
	"WHEN": "keyword1",
	"WHERE": "keyword1",
	"WITH": "keyword1",
	"WITHOUT": "keyword1",
}

# Dictionary of keywords dictionaries for interlis mode.
keywordsDictDict = {
	"interlis_main": interlis_main_keywords_dict,
}

# Rules for interlis_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="!!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="comment2", begin="//", end="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="..",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="--",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-<#>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-<>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="..",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule31(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule32(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule33(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule34(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule35(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule36(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule37(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule38(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule39(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="==",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule40(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule41(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule42(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule43(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule44(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule45(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule46(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule47(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule48(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule1,rule18,],
	"\"": [rule2,],
	"#": [rule19,],
	"%": [rule20,],
	"(": [rule15,rule21,],
	")": [rule16,rule22,],
	"*": [rule12,rule23,],
	",": [rule8,rule24,],
	"-": [rule4,rule25,rule26,rule27,rule28,],
	".": [rule6,rule7,rule29,rule30,],
	"/": [rule0,rule3,rule31,],
	"0": [rule48,],
	"1": [rule48,],
	"2": [rule48,],
	"3": [rule48,],
	"4": [rule48,],
	"5": [rule48,],
	"6": [rule48,],
	"7": [rule48,],
	"8": [rule48,],
	"9": [rule48,],
	":": [rule11,rule32,rule33,],
	";": [rule10,rule34,],
	"<": [rule5,rule35,rule36,rule37,],
	"=": [rule9,rule38,rule39,],
	">": [rule17,rule40,rule41,],
	"@": [rule48,],
	"A": [rule48,],
	"B": [rule48,],
	"C": [rule48,],
	"D": [rule48,],
	"E": [rule48,],
	"F": [rule48,],
	"G": [rule48,],
	"H": [rule48,],
	"I": [rule48,],
	"J": [rule48,],
	"K": [rule48,],
	"L": [rule48,],
	"M": [rule48,],
	"N": [rule48,],
	"O": [rule48,],
	"P": [rule48,],
	"Q": [rule48,],
	"R": [rule48,],
	"S": [rule48,],
	"T": [rule48,],
	"U": [rule48,],
	"V": [rule48,],
	"W": [rule48,],
	"X": [rule48,],
	"Y": [rule48,],
	"Z": [rule48,],
	"[": [rule13,rule42,],
	"\": [rule43,],
	"]": [rule14,rule44,],
	"_": [rule48,],
	"a": [rule48,],
	"b": [rule48,],
	"c": [rule48,],
	"d": [rule48,],
	"e": [rule48,],
	"f": [rule48,],
	"g": [rule48,],
	"h": [rule48,],
	"i": [rule48,],
	"j": [rule48,],
	"k": [rule48,],
	"l": [rule48,],
	"m": [rule48,],
	"n": [rule48,],
	"o": [rule48,],
	"p": [rule48,],
	"q": [rule48,],
	"r": [rule48,],
	"s": [rule48,],
	"t": [rule48,],
	"u": [rule48,],
	"v": [rule48,],
	"w": [rule48,],
	"x": [rule48,],
	"y": [rule48,],
	"z": [rule48,],
	"{": [rule45,],
	"}": [rule46,],
	"~": [rule47,],
}

# x.rulesDictDict for interlis mode.
rulesDictDict = {
	"interlis_main": rulesDict1,
}

# Import dict for interlis mode.
importDict = {}

