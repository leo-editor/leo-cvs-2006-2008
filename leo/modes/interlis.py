# Leo colorizer control file for interlis mode.

# Properties for interlis mode.
properties = {
	"blockComment": "!!",
	"commentEnd": "*/",
	"commentStart": "/*",
}

# Keywords dict for interlis_main ruleset.
interlis_main_keywords_dict = {
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

# Rules list for interlis_main ruleset.
interlis_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
	rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29,
	rule30, rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39,
	rule40, rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, ]

# Rules dict for interlis mode.
rulesDict = {
	"interlis_main": interlis_main_rules,
}

# Import dict for interlis mode.
importDict = {}

