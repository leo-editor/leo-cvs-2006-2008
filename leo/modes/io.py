# Leo colorizer control file for io mode.

# Properties for io mode.
properties = {
	"commentStart": "*/",
	"indentCloseBrackets": ")",
	"indentOpenBrackets": "(",
	"lineComment": "//",
	"lineUpClosingBracket": "true",
}

# Keywords dict for io_main ruleset.
io_main_keywords_dict = {
	"Block": "keyword1",
	"Buffer": "keyword1",
	"CFunction": "keyword1",
	"Date": "keyword1",
	"Duration": "keyword1",
	"File": "keyword1",
	"Future": "keyword1",
	"LinkedList": "keyword1",
	"List": "keyword1",
	"Map": "keyword1",
	"Message": "keyword1",
	"Nil": "keyword1",
	"Nop": "keyword1",
	"Number": "keyword1",
	"Object": "keyword1",
	"String": "keyword1",
	"WeakLink": "keyword1",
	"block": "keyword1",
	"clone": "keyword3",
	"do": "keyword2",
	"else": "keyword2",
	"foreach": "keyword2",
	"forward": "keyword3",
	"hasSlot": "keyword3",
	"if": "keyword2",
	"method": "keyword1",
	"print": "keyword3",
	"proto": "keyword3",
	"self": "keyword3",
	"setSlot": "keyword3",
	"super": "keyword3",
	"type": "keyword3",
	"while": "keyword2",
	"write": "keyword3",
}

# Dictionary of keywords dictionaries for io mode.
keywordsDictDict = {
	"io_main": io_main_keywords_dict,
}

# Rules for io_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="\"\"\"", end="\"\"\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="`",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\\",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="?",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"\"": [rule3,rule4,],
	"#": [rule0,],
	"$": [rule9,],
	"%": [rule10,],
	"&": [rule12,],
	"*": [rule13,],
	"+": [rule15,],
	"-": [rule14,],
	"/": [rule1,rule2,rule16,],
	"0": [rule27,],
	"1": [rule27,],
	"2": [rule27,],
	"3": [rule27,],
	"4": [rule27,],
	"5": [rule27,],
	"6": [rule27,],
	"7": [rule27,],
	"8": [rule27,],
	"9": [rule27,],
	"<": [rule25,],
	"=": [rule17,],
	">": [rule24,],
	"?": [rule26,],
	"@": [rule7,rule8,rule27,],
	"A": [rule27,],
	"B": [rule27,],
	"C": [rule27,],
	"D": [rule27,],
	"E": [rule27,],
	"F": [rule27,],
	"G": [rule27,],
	"H": [rule27,],
	"I": [rule27,],
	"J": [rule27,],
	"K": [rule27,],
	"L": [rule27,],
	"M": [rule27,],
	"N": [rule27,],
	"O": [rule27,],
	"P": [rule27,],
	"Q": [rule27,],
	"R": [rule27,],
	"S": [rule27,],
	"T": [rule27,],
	"U": [rule27,],
	"V": [rule27,],
	"W": [rule27,],
	"X": [rule27,],
	"Y": [rule27,],
	"Z": [rule27,],
	"[": [rule20,],
	"\\": [rule23,],
	"]": [rule21,],
	"^": [rule11,],
	"_": [rule27,],
	"`": [rule5,],
	"a": [rule27,],
	"b": [rule27,],
	"c": [rule27,],
	"d": [rule27,],
	"e": [rule27,],
	"f": [rule27,],
	"g": [rule27,],
	"h": [rule27,],
	"i": [rule27,],
	"j": [rule27,],
	"k": [rule27,],
	"l": [rule27,],
	"m": [rule27,],
	"n": [rule27,],
	"o": [rule27,],
	"p": [rule27,],
	"q": [rule27,],
	"r": [rule27,],
	"s": [rule27,],
	"t": [rule27,],
	"u": [rule27,],
	"v": [rule27,],
	"w": [rule27,],
	"x": [rule27,],
	"y": [rule27,],
	"z": [rule27,],
	"{": [rule18,],
	"|": [rule22,],
	"}": [rule19,],
	"~": [rule6,],
}

# x.rulesDictDict for io mode.
rulesDictDict = {
	"io_main": rulesDict1,
}

# Import dict for io mode.
importDict = {}

