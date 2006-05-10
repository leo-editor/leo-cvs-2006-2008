# Leo colorizer control file for inform mode.
# This file is in the public domain.

# Properties for inform mode.
properties = {
	"doubleBracketIndent": "false",
	"filenameGlob": "*.(inf|h)",
	"indentCloseBrackets": "}]",
	"indentNextLine": "\\s*(((if|while)\\s*\\(|else\\s*|else\\s+if\\s*\\(|for\\s*\\(.*\\))[^{;]*)",
	"indentOpenBrackets": "{[",
	"lineComment": "!",
	"lineUpClosingBracket": "true",
	"wordBreakChars": ",+-=<>/?^&*",
}

# Attributes dict for inform_main ruleset.
inform_main_attributes_dict = {
	"default": "null",
	"digit_re": "(\\$[[:xdigit:]]|[[:digit:]])",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Attributes dict for inform_informinnertext ruleset.
inform_informinnertext_attributes_dict = {
	"default": "LITERAL1",
	"digit_re": "(\\$[[:xdigit:]]|[[:digit:]])",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for inform mode.
attributesDictDict = {
	"inform_informinnertext": inform_informinnertext_attributes_dict,
	"inform_main": inform_main_attributes_dict,
}

# Keywords dict for inform_main ruleset.
inform_main_keywords_dict = {
	"Abbreviate": "keyword3",
	"Array": "keyword3",
	"Attribute": "keyword3",
	"Class": "keyword3",
	"Constant": "keyword3",
	"Default": "keyword3",
	"End": "keyword3",
	"Endif": "keyword3",
	"Extend": "keyword3",
	"Global": "keyword3",
	"Ifdef": "keyword3",
	"Iffalse": "keyword3",
	"Ifndef": "keyword3",
	"Ifnot": "keyword3",
	"Iftrue": "keyword3",
	"Import": "keyword3",
	"Include": "keyword3",
	"Link": "keyword3",
	"Lowstring": "keyword3",
	"Message": "keyword3",
	"Object": "keyword3",
	"Property": "keyword3",
	"Replace": "keyword3",
	"Serial": "keyword3",
	"Statusline": "keyword3",
	"Switches": "keyword3",
	"System_file": "keyword3",
	"The": "literal2",
	"Verb": "keyword3",
	"a": "literal2",
	"address": "literal2",
	"an": "literal2",
	"bold": "keyword2",
	"box": "function",
	"break": "keyword1",
	"char": "literal2",
	"continue": "keyword1",
	"do": "keyword1",
	"else": "keyword1",
	"false": "literal2",
	"fixed": "keyword2",
	"font": "function",
	"for": "keyword1",
	"give": "keyword1",
	"has": "keyword1",
	"hasnt": "keyword1",
	"if": "keyword1",
	"in": "keyword1",
	"inversion": "keyword1",
	"jump": "keyword1",
	"move": "keyword1",
	"name": "literal2",
	"new_line": "function",
	"notin": "keyword1",
	"null": "literal2",
	"object": "literal2",
	"objectloop": "keyword1",
	"ofclass": "keyword1",
	"off": "keyword2",
	"on": "keyword2",
	"or": "keyword1",
	"print": "function",
	"print_ret": "function",
	"private": "keyword3",
	"property": "literal2",
	"provides": "keyword1",
	"quit": "function",
	"read": "function",
	"remove": "keyword1",
	"restore": "function",
	"return": "keyword1",
	"reverse": "keyword2",
	"rfalse": "keyword1",
	"roman": "keyword2",
	"rtrue": "keyword1",
	"save": "function",
	"score": "function",
	"self": "literal2",
	"spaces": "function",
	"string": "keyword1",
	"style": "function",
	"super": "literal2",
	"switch": "keyword1",
	"the": "literal2",
	"this": "invalid",
	"time": "function",
	"to": "keyword2",
	"true": "literal2",
	"underline": "keyword2",
	"until": "keyword1",
	"while": "keyword1",
	"with": "keyword1",
}

# Keywords dict for inform_informinnertext ruleset.
inform_informinnertext_keywords_dict = {}

# Dictionary of keywords dictionaries for inform mode.
keywordsDictDict = {
	"inform_informinnertext": inform_informinnertext_keywords_dict,
	"inform_main": inform_main_keywords_dict,
}

# Rules for inform_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="InformInnerText",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="keyword2", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="==",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule30(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="::",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule31(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule32(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule0,rule4,],
	"\"": [rule1,],
	"#": [rule3,],
	"$": [rule12,],
	"%": [rule17,],
	"&": [rule18,],
	"'": [rule2,],
	"(": [rule29,],
	"*": [rule14,],
	"+": [rule10,],
	"-": [rule11,rule28,],
	".": [rule26,rule27,],
	"/": [rule13,],
	"0": [rule32,],
	"1": [rule32,],
	"2": [rule32,],
	"3": [rule32,],
	"4": [rule32,],
	"5": [rule32,],
	"6": [rule32,],
	"7": [rule32,],
	"8": [rule32,],
	"9": [rule32,],
	":": [rule30,rule31,],
	"<": [rule8,rule16,],
	"=": [rule5,rule6,],
	">": [rule7,rule15,],
	"@": [rule32,],
	"A": [rule32,],
	"B": [rule32,],
	"C": [rule32,],
	"D": [rule32,],
	"E": [rule32,],
	"F": [rule32,],
	"G": [rule32,],
	"H": [rule32,],
	"I": [rule32,],
	"J": [rule32,],
	"K": [rule32,],
	"L": [rule32,],
	"M": [rule32,],
	"N": [rule32,],
	"O": [rule32,],
	"P": [rule32,],
	"Q": [rule32,],
	"R": [rule32,],
	"S": [rule32,],
	"T": [rule32,],
	"U": [rule32,],
	"V": [rule32,],
	"W": [rule32,],
	"X": [rule32,],
	"Y": [rule32,],
	"Z": [rule32,],
	"[": [rule25,],
	"]": [rule24,],
	"^": [rule20,],
	"_": [rule32,],
	"a": [rule32,],
	"b": [rule32,],
	"c": [rule32,],
	"d": [rule32,],
	"e": [rule32,],
	"f": [rule32,],
	"g": [rule32,],
	"h": [rule32,],
	"i": [rule32,],
	"j": [rule32,],
	"k": [rule32,],
	"l": [rule32,],
	"m": [rule32,],
	"n": [rule32,],
	"o": [rule32,],
	"p": [rule32,],
	"q": [rule32,],
	"r": [rule32,],
	"s": [rule32,],
	"t": [rule32,],
	"u": [rule32,],
	"v": [rule32,],
	"w": [rule32,],
	"x": [rule32,],
	"y": [rule32,],
	"z": [rule32,],
	"{": [rule23,],
	"|": [rule19,],
	"}": [rule22,],
	"~": [rule9,rule21,],
}

# Rules for inform_informinnertext ruleset.

def rule33(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule34(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule35(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule36(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\\",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule37(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal2", seq="@@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

# Rules dict for informinnertext ruleset.
rulesDict2 = {
	"@": [rule35,rule37,],
	"\\": [rule36,],
	"^": [rule33,],
	"~": [rule34,],
}

# x.rulesDictDict for inform mode.
rulesDictDict = {
	"inform_informinnertext": rulesDict2,
	"inform_main": rulesDict1,
}

# Import dict for inform mode.
importDict = {}

