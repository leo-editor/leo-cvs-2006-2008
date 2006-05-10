# Leo colorizer control file for icon mode.
# This file is in the public domain.

# Properties for icon mode.
properties = {
	"indentCloseBrackets": "}",
	"indentOpenBrackets": "{",
	"lineComment": "#",
	"lineUpClosingBracket": "true",
	"wordBreakChars": "|.\\\\:,+-*/=?^!@%<>&",
}

# Attributes dict for icon_main ruleset.
icon_main_attributes_dict = {
	"default": "null",
	"digit_re": "(0x[[:xdigit:]]+[lL]?|[[:digit:]]+(e[[:digit:]]*)?[lLdDfF]?)",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for icon mode.
attributesDictDict = {
	"icon_main": icon_main_attributes_dict,
}

# Keywords dict for icon_main ruleset.
icon_main_keywords_dict = {
	"$define": "keyword3",
	"$else": "keyword3",
	"$endif": "keyword3",
	"$error": "keyword3",
	"$ifdef": "keyword3",
	"$ifndef": "keyword3",
	"$include": "keyword3",
	"$line": "keyword3",
	"$undef": "keyword3",
	"&": "keyword3",
	"_MACINTOSH": "keyword3",
	"_MSDOS": "keyword3",
	"_MSDOS_386": "keyword3",
	"_MS_WINDOWS": "keyword3",
	"_MS_WINDOWS_NT": "keyword3",
	"_OS2": "keyword3",
	"_PIPES": "keyword3",
	"_PRESENTATION_MGR": "keyword3",
	"_SYSTEM_FUNCTION": "keyword3",
	"_UNIX": "keyword3",
	"_VMS": "keyword3",
	"_WINDOW_FUNCTIONS": "keyword3",
	"_X_WINDOW_SYSTEM": "keyword3",
	"allocated": "keyword3",
	"ascii": "keyword3",
	"break": "keyword2",
	"by": "keyword1",
	"case": "keyword1",
	"clock": "keyword3",
	"co-expression": "keyword4",
	"collections": "keyword3",
	"create": "keyword1",
	"cset": "keyword4",
	"current": "keyword3",
	"date": "keyword3",
	"dateline": "keyword3",
	"default": "keyword1",
	"digits": "keyword3",
	"do": "keyword1",
	"dump": "keyword3",
	"e": "keyword3",
	"else": "keyword1",
	"end": "keyword2",
	"error": "keyword3",
	"errornumber": "keyword3",
	"errortext": "keyword3",
	"errorvalue": "keyword3",
	"errout": "keyword3",
	"every": "keyword1",
	"fail": "keyword3",
	"features": "keyword3",
	"file": "keyword4",
	"global": "keyword2",
	"host": "keyword3",
	"if": "keyword1",
	"initial": "keyword1",
	"input": "keyword3",
	"integer": "keyword4",
	"invocable": "keyword2",
	"lcase": "keyword3",
	"letters": "keyword3",
	"level": "keyword3",
	"line": "keyword3",
	"link": "keyword2",
	"list": "keyword4",
	"local": "keyword2",
	"main": "keyword3",
	"next": "keyword1",
	"null": "keyword4",
	"of": "keyword1",
	"output": "keyword3",
	"phi": "keyword3",
	"pi": "keyword3",
	"pos": "keyword3",
	"procedure": "keyword2",
	"progname": "keyword3",
	"random": "keyword3",
	"real": "keyword4",
	"record": "keyword2",
	"regions": "keyword3",
	"repeat": "keyword1",
	"return": "keyword2",
	"set": "keyword4",
	"source": "keyword3",
	"static": "keyword2",
	"storage": "keyword3",
	"string": "keyword4",
	"subject": "keyword3",
	"suspend": "keyword2",
	"table": "keyword4",
	"then": "keyword1",
	"time": "keyword3",
	"to": "keyword1",
	"trace": "keyword3",
	"ucase": "keyword3",
	"until": "keyword1",
	"version": "keyword3",
	"while": "keyword1",
	"window": "keyword4",
}

# Dictionary of keywords dictionaries for icon mode.
keywordsDictDict = {
	"icon_main": icon_main_keywords_dict,
}

# Rules for icon_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~===",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="===",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|||",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">>=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~==",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="==",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="||",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="++",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="**",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="--",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="op:=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":=:",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-:",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+:",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule31(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule32(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule33(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="not",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule34(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule35(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="?",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule36(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule37(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule38(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule39(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule40(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule41(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule42(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule43(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule44(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule30,],
	"\"": [rule1,],
	"#": [rule0,],
	"%": [rule38,],
	"&": [rule32,],
	"'": [rule2,],
	"(": [rule43,],
	"*": [rule14,rule34,],
	"+": [rule13,rule27,rule40,],
	"-": [rule15,rule26,rule39,],
	"/": [rule42,],
	"0": [rule44,],
	"1": [rule44,],
	"2": [rule44,],
	"3": [rule44,],
	"4": [rule44,],
	"5": [rule44,],
	"6": [rule44,],
	"7": [rule44,],
	"8": [rule44,],
	"9": [rule44,],
	":": [rule24,rule25,rule29,],
	"<": [rule8,rule9,rule16,rule17,rule19,rule20,],
	"=": [rule4,rule11,rule41,],
	">": [rule6,rule7,rule21,rule22,],
	"?": [rule35,],
	"@": [rule36,rule44,],
	"A": [rule44,],
	"B": [rule44,],
	"C": [rule44,],
	"D": [rule44,],
	"E": [rule44,],
	"F": [rule44,],
	"G": [rule44,],
	"H": [rule44,],
	"I": [rule44,],
	"J": [rule44,],
	"K": [rule44,],
	"L": [rule44,],
	"M": [rule44,],
	"N": [rule44,],
	"O": [rule44,],
	"P": [rule44,],
	"Q": [rule44,],
	"R": [rule44,],
	"S": [rule44,],
	"T": [rule44,],
	"U": [rule44,],
	"V": [rule44,],
	"W": [rule44,],
	"X": [rule44,],
	"Y": [rule44,],
	"Z": [rule44,],
	"^": [rule37,],
	"_": [rule44,],
	"a": [rule44,],
	"b": [rule44,],
	"c": [rule44,],
	"d": [rule44,],
	"e": [rule44,],
	"f": [rule44,],
	"g": [rule44,],
	"h": [rule44,],
	"i": [rule44,],
	"j": [rule44,],
	"k": [rule44,],
	"l": [rule44,],
	"m": [rule44,],
	"n": [rule33,rule44,],
	"o": [rule18,rule44,],
	"p": [rule44,],
	"q": [rule44,],
	"r": [rule44,],
	"s": [rule44,],
	"t": [rule44,],
	"u": [rule44,],
	"v": [rule44,],
	"w": [rule44,],
	"x": [rule44,],
	"y": [rule44,],
	"z": [rule44,],
	"|": [rule5,rule12,rule31,],
	"~": [rule3,rule10,rule23,rule28,],
}

# x.rulesDictDict for icon mode.
rulesDictDict = {
	"icon_main": rulesDict1,
}

# Import dict for icon mode.
importDict = {}

