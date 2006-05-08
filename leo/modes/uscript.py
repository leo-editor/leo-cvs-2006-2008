# Leo colorizer control file for uscript mode.

# Properties for uscript mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"doubleBracketIndent": "false",
	"indentCloseBrackets": "}",
	"indentNextLine": "\s*(((if|while)\s*\(|else\s*|else\s+if\s*\(|for\s*\(.*\))[^{;]*)",
	"indentOpenBrackets": "{",
	"lineComment": "//",
	"lineUpClosingBracket": "true",
	"wordBreakChars": ",+-=<>/?^&*",
}

# Keywords dict for uscript_main ruleset.
uscript_main_keywords_dict = {
	"abstract": "keyword1",
	"array": "keyword1",
	"auto": "keyword1",
	"bool": "keyword3",
	"byte": "keyword3",
	"case": "keyword1",
	"class": "keyword1",
	"coerce": "keyword1",
	"collapscategories": "keyword1",
	"config": "keyword1",
	"const": "keyword1",
	"default": "keyword2",
	"defaultproperties": "keyword1",
	"deprecated": "keyword1",
	"do": "keyword1",
	"dontcollapsecategories": "keyword1",
	"edfindable": "keyword1",
	"editconst": "keyword1",
	"editinline": "keyword1",
	"editinlinenew": "keyword1",
	"else": "keyword1",
	"enum": "keyword1",
	"event": "keyword1",
	"exec": "keyword1",
	"export": "keyword1",
	"exportstructs": "keyword1",
	"extends": "keyword1",
	"false": "keyword1",
	"final": "keyword1",
	"float": "keyword3",
	"for": "keyword1",
	"foreach": "keyword1",
	"function": "keyword1",
	"global": "keyword2",
	"globalconfig": "keyword1",
	"hidecategories": "keyword1",
	"if": "keyword1",
	"ignores": "keyword1",
	"input": "keyword1",
	"int": "keyword3",
	"iterator": "keyword1",
	"latent": "keyword1",
	"local": "keyword1",
	"localized": "keyword1",
	"name": "keyword3",
	"native": "keyword1",
	"nativereplication": "keyword1",
	"noexport": "keyword1",
	"none": "keyword2",
	"noteditinlinenew": "keyword1",
	"notplaceable": "keyword1",
	"operator": "keyword1",
	"optional": "keyword1",
	"out": "keyword1",
	"perobjectconfig": "keyword1",
	"placeable": "keyword1",
	"postoperator": "keyword1",
	"preoperator": "keyword1",
	"private": "keyword1",
	"protected": "keyword1",
	"reliable": "keyword1",
	"replication": "keyword1",
	"return": "keyword1",
	"safereplace": "keyword1",
	"self": "keyword2",
	"showcategories": "keyword1",
	"simulated": "keyword1",
	"singular": "keyword1",
	"state": "keyword1",
	"static": "keyword2",
	"string": "keyword3",
	"struct": "keyword1",
	"super": "keyword2",
	"switch": "keyword1",
	"transient": "keyword1",
	"travel": "keyword1",
	"true": "keyword1",
	"unreliable": "keyword1",
	"until": "keyword1",
	"var": "keyword1",
	"while": "keyword1",
	"within": "keyword1",
}

# Dictionary of keywords dictionaries for uscript mode.
keywordsDictDict = {
	"uscript_main": uscript_main_keywords_dict,
}

# Rules for uscript_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment1", seq="/**/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\\",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="?",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="`",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=False, at_whitespace_end=True, at_word_start=False, exclude_match=True)

def rule25(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule26(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule6,],
	"\"": [rule2,],
	"#": [rule8,],
	"$": [rule9,],
	"&": [rule11,],
	"'": [rule3,],
	"(": [rule25,],
	"*": [rule12,],
	"+": [rule15,],
	"-": [rule13,],
	"/": [rule0,rule1,rule4,rule21,],
	"0": [rule26,],
	"1": [rule26,],
	"2": [rule26,],
	"3": [rule26,],
	"4": [rule26,],
	"5": [rule26,],
	"6": [rule26,],
	"7": [rule26,],
	"8": [rule26,],
	"9": [rule26,],
	":": [rule18,rule24,],
	"<": [rule19,],
	"=": [rule14,],
	">": [rule20,],
	"?": [rule22,],
	"@": [rule7,rule26,],
	"A": [rule26,],
	"B": [rule26,],
	"C": [rule26,],
	"D": [rule26,],
	"E": [rule26,],
	"F": [rule26,],
	"G": [rule26,],
	"H": [rule26,],
	"I": [rule26,],
	"J": [rule26,],
	"K": [rule26,],
	"L": [rule26,],
	"M": [rule26,],
	"N": [rule26,],
	"O": [rule26,],
	"P": [rule26,],
	"Q": [rule26,],
	"R": [rule26,],
	"S": [rule26,],
	"T": [rule26,],
	"U": [rule26,],
	"V": [rule26,],
	"W": [rule26,],
	"X": [rule26,],
	"Y": [rule26,],
	"Z": [rule26,],
	"\": [rule17,],
	"^": [rule10,],
	"_": [rule26,],
	"`": [rule23,],
	"a": [rule26,],
	"b": [rule26,],
	"c": [rule26,],
	"d": [rule26,],
	"e": [rule26,],
	"f": [rule26,],
	"g": [rule26,],
	"h": [rule26,],
	"i": [rule26,],
	"j": [rule26,],
	"k": [rule26,],
	"l": [rule26,],
	"m": [rule26,],
	"n": [rule26,],
	"o": [rule26,],
	"p": [rule26,],
	"q": [rule26,],
	"r": [rule26,],
	"s": [rule26,],
	"t": [rule26,],
	"u": [rule26,],
	"v": [rule26,],
	"w": [rule26,],
	"x": [rule26,],
	"y": [rule26,],
	"z": [rule26,],
	"|": [rule16,],
	"~": [rule5,],
}

# x.rulesDictDict for uscript mode.
rulesDictDict = {
	"uscript_main": rulesDict1,
}

# Import dict for uscript mode.
importDict = {}

