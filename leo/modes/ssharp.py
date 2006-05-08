# Leo colorizer control file for ssharp mode.

# Properties for ssharp mode.
properties = {
	"commentEnd": "\"",
	"commentStart": "\"",
	"indentCloseBrackets": "]",
	"indentOpenBrackets": "[",
	"lineComment": "#",
	"lineUpClosingBracket": "true",
}

# Keywords dict for ssharp_main ruleset.
ssharp_main_keywords_dict = {
	"		": "keywords",
	"			": "keywords",
	"	  ": "keywords",
	"
": "keywords",
	" ": "keyword2",
	"            ": "keywords",
	"            			": "keywords",
	"?": "keyword2",
	"Application": "literal3",
	"Array": "literal2",
	"Boolean": "literal2",
	"Category": "literal3",
	"Character": "literal2",
	"Class": "literal3",
	"Compiler": "literal3",
	"Date": "literal2",
	"EntryPoint": "literal3",
	"Enum": "literal3",
	"Eval": "literal3",
	"Exception": "literal3",
	"False": "literal2",
	"Function": "literal3",
	"IconResource": "literal3",
	"Integer": "literal2",
	"Interface": "literal3",
	"Literal": "literal3",
	"Method": "literal3",
	"Mixin": "literal3",
	"Module": "literal3",
	"Namespace": "literal3",
	"Object": "literal2",
	"Project": "literal3",
	"Reference": "literal3",
	"Require": "literal3",
	"Resource": "literal3",
	"Signal": "literal3",
	"Smalltalk": "literal2",
	"Specifications": "literal3",
	"String": "literal2",
	"Struct": "literal3",
	"Subsystem": "literal3",
	"Symbol": "literal2",
	"Time": "literal2",
	"Transcript": "literal2",
	"True": "literal2",
	"Warning": "literal3",
	"blockSelf": "keyword2",
	"disable": "keyword1",
	"enable": "keyword1",
	"false": "keyword2",
	"isNil": "keyword4",
	"nil": "keyword2",
	"no": "keyword1",
	"not": "keyword4",
	"off": "keyword1",
	"on": "keyword1",
	"scheduler": "keyword2",
	"self": "keyword2",
	"sender": "keyword2",
	"senderMethod": "keyword2",
	"super": "keyword2",
	"thread": "keyword2",
	"true": "keyword2",
	"yes": "keyword1",
}

# Dictionary of keywords dictionaries for ssharp mode.
keywordsDictDict = {
	"ssharp_main": ssharp_main_keywords_dict,
}

# Rules for ssharp_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment3", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="\"\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="? ", end="? ",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="_",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="==",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
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
    return colorer.match_seq(s, i, kind="operator", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\\",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="**",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule31(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="||",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule32(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule33(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule34(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule35(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!==",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule36(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule37(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="keyword3", pattern=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule38(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="label", pattern="#"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule39(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="literal1", pattern="$"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule40(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule33,rule35,],
	"\"": [rule2,rule3,],
	"#": [rule1,rule24,rule38,],
	"$": [rule39,],
	"&": [rule30,],
	"'": [rule0,],
	"(": [rule5,],
	")": [rule6,],
	"*": [rule22,rule23,],
	"+": [rule17,],
	"-": [rule18,rule29,],
	".": [rule28,],
	"/": [rule19,rule20,],
	"0": [rule40,],
	"1": [rule40,],
	"2": [rule40,],
	"3": [rule40,],
	"4": [rule40,],
	"5": [rule40,],
	"6": [rule40,],
	"7": [rule40,],
	"8": [rule40,],
	"9": [rule40,],
	":": [rule9,rule37,],
	";": [rule27,],
	"<": [rule14,rule16,],
	"=": [rule11,rule12,],
	">": [rule13,rule15,],
	"?": [rule4,],
	"@": [rule40,],
	"A": [rule40,],
	"B": [rule40,],
	"C": [rule40,],
	"D": [rule40,],
	"E": [rule40,],
	"F": [rule40,],
	"G": [rule40,],
	"H": [rule40,],
	"I": [rule40,],
	"J": [rule40,],
	"K": [rule40,],
	"L": [rule40,],
	"M": [rule40,],
	"N": [rule40,],
	"O": [rule40,],
	"P": [rule40,],
	"Q": [rule40,],
	"R": [rule40,],
	"S": [rule40,],
	"T": [rule40,],
	"U": [rule40,],
	"V": [rule40,],
	"W": [rule40,],
	"X": [rule40,],
	"Y": [rule40,],
	"Z": [rule40,],
	"\": [rule21,],
	"^": [rule25,rule26,rule32,],
	"_": [rule10,rule40,],
	"a": [rule40,],
	"b": [rule40,],
	"c": [rule40,],
	"d": [rule40,],
	"e": [rule40,],
	"f": [rule40,],
	"g": [rule40,],
	"h": [rule40,],
	"i": [rule40,],
	"j": [rule40,],
	"k": [rule40,],
	"l": [rule40,],
	"m": [rule40,],
	"n": [rule40,],
	"o": [rule40,],
	"p": [rule40,],
	"q": [rule40,],
	"r": [rule40,],
	"s": [rule40,],
	"t": [rule40,],
	"u": [rule40,],
	"v": [rule40,],
	"w": [rule40,],
	"x": [rule40,],
	"y": [rule40,],
	"z": [rule40,],
	"{": [rule7,],
	"|": [rule31,],
	"}": [rule8,],
	"~": [rule34,rule36,],
}

# x.rulesDictDict for ssharp mode.
rulesDictDict = {
	"ssharp_main": rulesDict1,
}

# Import dict for ssharp mode.
importDict = {}

