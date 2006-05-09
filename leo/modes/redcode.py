# Leo colorizer control file for redcode mode.
# This file is in the public domain.

# Properties for redcode mode.
properties = {
	"lineComment": ";",
}

# Keywords dict for redcode_main ruleset.
redcode_main_keywords_dict = {
	"ADD": "keyword1",
	"CMP": "keyword1",
	"CORESIZE": "keyword2",
	"CURLINE": "keyword2",
	"DAT": "keyword1",
	"DIV": "keyword1",
	"DJN": "keyword1",
	"END": "keyword2",
	"EQU": "keyword2",
	"FOR": "keyword2",
	"JMN": "keyword1",
	"JMP": "keyword1",
	"JMZ": "keyword1",
	"LDP": "keyword1",
	"MAXCYCLES": "keyword2",
	"MAXLENGTH": "keyword2",
	"MAXPROCESSES": "keyword2",
	"MINDISTANCE": "keyword2",
	"MOD": "keyword1",
	"MOV": "keyword1",
	"MUL": "keyword1",
	"NOP": "keyword1",
	"ORG": "keyword2",
	"PIN": "keyword2",
	"PSPACESIZE": "keyword2",
	"ROF": "keyword2",
	"ROUNDS": "keyword2",
	"SEQ": "keyword1",
	"SLT": "keyword1",
	"SNE": "keyword1",
	"SPL": "keyword1",
	"STP": "keyword1",
	"SUB": "keyword1",
	"VERSION": "keyword2",
	"WARRIORS": "keyword2",
}

# Dictionary of keywords dictionaries for redcode mode.
keywordsDictDict = {
	"redcode_main": redcode_main_keywords_dict,
}

# Rules for redcode_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq=";redcode",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq=";author",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq=";name",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq=";strategy",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq=";password",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule5(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq=".AB",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq=".BA",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq=".A",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq=".B",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq=".F",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq=".X",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq=".I",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="==",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="||",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule31(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule32(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule33(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule34(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule35(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule36(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule37(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule22,rule29,],
	"#": [rule33,],
	"$": [rule31,],
	"%": [rule20,],
	"&": [rule27,],
	"(": [rule15,],
	")": [rule16,],
	"*": [rule34,],
	"+": [rule17,],
	",": [rule13,],
	"-": [rule18,],
	".": [rule6,rule7,rule8,rule9,rule10,rule11,rule12,],
	"/": [rule19,],
	"0": [rule37,],
	"1": [rule37,],
	"2": [rule37,],
	"3": [rule37,],
	"4": [rule37,],
	"5": [rule37,],
	"6": [rule37,],
	"7": [rule37,],
	"8": [rule37,],
	"9": [rule37,],
	":": [rule14,],
	";": [rule0,rule1,rule2,rule3,rule4,rule5,],
	"<": [rule23,rule25,],
	"=": [rule21,rule30,],
	">": [rule24,rule26,],
	"@": [rule32,rule37,],
	"A": [rule37,],
	"B": [rule37,],
	"C": [rule37,],
	"D": [rule37,],
	"E": [rule37,],
	"F": [rule37,],
	"G": [rule37,],
	"H": [rule37,],
	"I": [rule37,],
	"J": [rule37,],
	"K": [rule37,],
	"L": [rule37,],
	"M": [rule37,],
	"N": [rule37,],
	"O": [rule37,],
	"P": [rule37,],
	"Q": [rule37,],
	"R": [rule37,],
	"S": [rule37,],
	"T": [rule37,],
	"U": [rule37,],
	"V": [rule37,],
	"W": [rule37,],
	"X": [rule37,],
	"Y": [rule37,],
	"Z": [rule37,],
	"_": [rule37,],
	"a": [rule37,],
	"b": [rule37,],
	"c": [rule37,],
	"d": [rule37,],
	"e": [rule37,],
	"f": [rule37,],
	"g": [rule37,],
	"h": [rule37,],
	"i": [rule37,],
	"j": [rule37,],
	"k": [rule37,],
	"l": [rule37,],
	"m": [rule37,],
	"n": [rule37,],
	"o": [rule37,],
	"p": [rule37,],
	"q": [rule37,],
	"r": [rule37,],
	"s": [rule37,],
	"t": [rule37,],
	"u": [rule37,],
	"v": [rule37,],
	"w": [rule37,],
	"x": [rule37,],
	"y": [rule37,],
	"z": [rule37,],
	"{": [rule35,],
	"|": [rule28,],
	"}": [rule36,],
}

# x.rulesDictDict for redcode mode.
rulesDictDict = {
	"redcode_main": rulesDict1,
}

# Import dict for redcode mode.
importDict = {}

