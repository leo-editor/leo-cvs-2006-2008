# Leo colorizer control file for java mode.
# This file is in the public domain.

# Properties for java mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"doubleBracketIndent": "false",
	"indentCloseBrackets": "}",
	"indentNextLine": "\\s*(((if|while)\\s*\\(|else\\s*|else\\s+if\\s*\\(|for\\s*\\(.*\\))[^{;]*)",
	"indentOpenBrackets": "{",
	"lineComment": "//",
	"lineUpClosingBracket": "true",
	"wordBreakChars": ",+-=<>/?^&*",
}

# Keywords dict for java_main ruleset.
java_main_keywords_dict = {
	"abstract": "keyword1",
	"assert": "function",
	"boolean": "keyword3",
	"break": "keyword1",
	"byte": "keyword3",
	"case": "keyword1",
	"catch": "keyword1",
	"char": "keyword3",
	"class": "keyword3",
	"const": "invalid",
	"continue": "keyword1",
	"default": "keyword1",
	"do": "keyword1",
	"double": "keyword3",
	"else": "keyword1",
	"enum": "keyword3",
	"extends": "keyword1",
	"false": "literal2",
	"final": "keyword1",
	"finally": "keyword1",
	"float": "keyword3",
	"for": "keyword1",
	"goto": "invalid",
	"if": "keyword1",
	"implements": "keyword1",
	"import": "keyword2",
	"instanceof": "keyword1",
	"int": "keyword3",
	"interface": "keyword3",
	"long": "keyword3",
	"native": "keyword1",
	"new": "keyword1",
	"null": "literal2",
	"package": "keyword2",
	"private": "keyword1",
	"protected": "keyword1",
	"public": "keyword1",
	"return": "keyword1",
	"short": "keyword3",
	"static": "keyword1",
	"strictfp": "keyword1",
	"super": "literal2",
	"switch": "keyword1",
	"synchronized": "keyword1",
	"this": "literal2",
	"throw": "keyword1",
	"throws": "keyword1",
	"transient": "keyword1",
	"true": "literal2",
	"try": "keyword1",
	"void": "keyword3",
	"volatile": "keyword1",
	"while": "keyword1",
}

# Keywords dict for java_javadoc ruleset.
java_javadoc_keywords_dict = {
	"@access": "label",
	"@author": "label",
	"@beaninfo": "label",
	"@bon": "label",
	"@bug": "label",
	"@complexity": "label",
	"@deprecated": "label",
	"@design": "label",
	"@docRoot": "label",
	"@ensures": "label",
	"@equivalent": "label",
	"@example": "label",
	"@exception": "label",
	"@generates": "label",
	"@guard": "label",
	"@hides": "label",
	"@history": "label",
	"@idea": "label",
	"@invariant": "label",
	"@link": "label",
	"@modifies": "label",
	"@overrides": "label",
	"@param": "label",
	"@post": "label",
	"@pre": "label",
	"@references": "label",
	"@requires": "label",
	"@return": "label",
	"@review": "label",
	"@see": "label",
	"@serial": "label",
	"@serialData": "label",
	"@serialField": "label",
	"@since": "label",
	"@spec": "label",
	"@throws": "label",
	"@todo": "label",
	"@uses": "label",
	"@values": "label",
	"@version": "label",
}

# Dictionary of keywords dictionaries for java mode.
keywordsDictDict = {
	"java_javadoc": java_javadoc_keywords_dict,
	"java_main": java_main_keywords_dict,
}

# Rules for java_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment1", seq="/**/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment3", begin="/**", end="*/",
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
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq=".*",
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
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=False, at_whitespace_end=True, at_word_start=False, exclude_match=True)

def rule25(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule26(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword4", pattern="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule27(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule7,],
	"\"": [rule3,],
	"%": [rule17,],
	"&": [rule18,],
	"'": [rule4,],
	"(": [rule25,],
	"*": [rule14,],
	"+": [rule10,],
	"-": [rule11,],
	".": [rule13,],
	"/": [rule0,rule1,rule2,rule5,rule12,],
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
	":": [rule24,],
	"<": [rule9,rule16,],
	"=": [rule6,],
	">": [rule8,rule15,],
	"@": [rule26,rule27,],
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
	"^": [rule20,],
	"_": [rule27,],
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
	"{": [rule23,],
	"|": [rule19,],
	"}": [rule22,],
	"~": [rule21,],
}

# Rules for java_javadoc ruleset.

def rule28(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment3", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment3", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule31(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment3", seq="<<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule32(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment3", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule33(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment3", seq="< ",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule34(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="xml::TAGS",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule35(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for javadoc ruleset.
rulesDict2 = {
	"*": [rule29,],
	"0": [rule35,],
	"1": [rule35,],
	"2": [rule35,],
	"3": [rule35,],
	"4": [rule35,],
	"5": [rule35,],
	"6": [rule35,],
	"7": [rule35,],
	"8": [rule35,],
	"9": [rule35,],
	"<": [rule30,rule31,rule32,rule33,rule34,],
	"@": [rule35,],
	"A": [rule35,],
	"B": [rule35,],
	"C": [rule35,],
	"D": [rule35,],
	"E": [rule35,],
	"F": [rule35,],
	"G": [rule35,],
	"H": [rule35,],
	"I": [rule35,],
	"J": [rule35,],
	"K": [rule35,],
	"L": [rule35,],
	"M": [rule35,],
	"N": [rule35,],
	"O": [rule35,],
	"P": [rule35,],
	"Q": [rule35,],
	"R": [rule35,],
	"S": [rule35,],
	"T": [rule35,],
	"U": [rule35,],
	"V": [rule35,],
	"W": [rule35,],
	"X": [rule35,],
	"Y": [rule35,],
	"Z": [rule35,],
	"_": [rule35,],
	"a": [rule35,],
	"b": [rule35,],
	"c": [rule35,],
	"d": [rule35,],
	"e": [rule35,],
	"f": [rule35,],
	"g": [rule35,],
	"h": [rule35,],
	"i": [rule35,],
	"j": [rule35,],
	"k": [rule35,],
	"l": [rule35,],
	"m": [rule35,],
	"n": [rule35,],
	"o": [rule35,],
	"p": [rule35,],
	"q": [rule35,],
	"r": [rule35,],
	"s": [rule35,],
	"t": [rule35,],
	"u": [rule35,],
	"v": [rule35,],
	"w": [rule35,],
	"x": [rule35,],
	"y": [rule35,],
	"z": [rule35,],
	"{": [rule28,],
}

# x.rulesDictDict for java mode.
rulesDictDict = {
	"java_javadoc": rulesDict2,
	"java_main": rulesDict1,
}

# Import dict for java mode.
importDict = {}

