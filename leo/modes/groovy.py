# Leo colorizer control file for groovy mode.

# Properties for groovy mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"indentCloseBrackets": "}",
	"indentNextLine": "\s*(((if|while)\s*\(|else\s*|else\s+if\s*\(|for\s*\(.*\))[^{;]*)",
	"indentOpenBrackets": "{",
	"lineComment": "//",
	"lineUpClosingBracket": "true",
}

# Keywords dict for groovy_main ruleset.
groovy_main_keywords_dict = {
	"abs": "keyword4",
	"abstract": "keyword1",
	"any": "keyword4",
	"append": "keyword4",
	"as": "keyword2",
	"asList": "keyword4",
	"asWritable": "keyword4",
	"assert": "keyword2",
	"boolean": "keyword3",
	"break": "keyword1",
	"byte": "keyword3",
	"call": "keyword4",
	"case": "keyword1",
	"catch": "keyword1",
	"char": "keyword3",
	"class": "keyword3",
	"collect": "keyword4",
	"compareTo": "keyword4",
	"const": "invalid",
	"continue": "keyword1",
	"count": "keyword4",
	"def": "keyword2",
	"default": "keyword1",
	"div": "keyword4",
	"do": "keyword1",
	"double": "keyword3",
	"dump": "keyword4",
	"each": "keyword4",
	"eachByte": "keyword4",
	"eachFile": "keyword4",
	"eachLine": "keyword4",
	"else": "keyword1",
	"every": "keyword4",
	"extends": "keyword1",
	"false": "literal2",
	"final": "keyword1",
	"finally": "keyword1",
	"find": "keyword4",
	"findAll": "keyword4",
	"flatten": "keyword4",
	"float": "keyword3",
	"for": "keyword1",
	"getAt": "keyword4",
	"getErr": "keyword4",
	"getIn": "keyword4",
	"getOut": "keyword4",
	"getText": "keyword4",
	"goto": "invalid",
	"grep": "keyword4",
	"if": "keyword1",
	"immutable": "keyword4",
	"implements": "keyword1",
	"import": "keyword1",
	"in": "keyword2",
	"inject": "keyword4",
	"inspect": "keyword4",
	"instanceof": "keyword1",
	"int": "keyword3",
	"interface": "keyword3",
	"intersect": "keyword4",
	"invokeMethods": "keyword4",
	"isCase": "keyword4",
	"it": "literal3",
	"join": "keyword4",
	"leftShift": "keyword4",
	"long": "keyword3",
	"minus": "keyword4",
	"mixin": "keyword2",
	"multiply": "keyword4",
	"native": "keyword1",
	"new": "keyword1",
	"newInputStream": "keyword4",
	"newOutputStream": "keyword4",
	"newPrintWriter": "keyword4",
	"newReader": "keyword4",
	"newWriter": "keyword4",
	"next": "keyword4",
	"null": "literal2",
	"package": "keyword1",
	"plus": "keyword4",
	"pop": "keyword4",
	"power": "keyword4",
	"previous": "keyword4",
	"print": "keyword4",
	"println": "keyword4",
	"private": "keyword1",
	"property": "keyword2",
	"protected": "keyword1",
	"public": "keyword1",
	"push": "keyword4",
	"putAt": "keyword4",
	"read": "keyword4",
	"readBytes": "keyword4",
	"readLines": "keyword4",
	"return": "keyword1",
	"reverse": "keyword4",
	"reverseEach": "keyword4",
	"round": "keyword4",
	"short": "keyword3",
	"size": "keyword4",
	"sort": "keyword4",
	"splitEachLine": "keyword4",
	"static": "keyword1",
	"step": "keyword4",
	"strictfp": "keyword1",
	"subMap": "keyword4",
	"super": "literal2",
	"switch": "keyword1",
	"synchronized": "keyword1",
	"test": "keyword2",
	"this": "literal2",
	"throw": "keyword1",
	"throws": "keyword1",
	"times": "keyword4",
	"toInteger": "keyword4",
	"toList": "keyword4",
	"tokenize": "keyword4",
	"transient": "keyword1",
	"true": "literal2",
	"try": "keyword1",
	"upto": "keyword4",
	"using": "keyword2",
	"void": "keyword3",
	"volatile": "keyword1",
	"waitForOrKill": "keyword4",
	"while": "keyword1",
	"withPrintWriter": "keyword4",
	"withReader": "keyword4",
	"withStream": "keyword4",
	"withWriter": "keyword4",
	"withWriterAppend": "keyword4",
	"write": "keyword4",
	"writeLine": "keyword4",
}

# Keywords dict for groovy_literal ruleset.
groovy_literal_keywords_dict = {}

# Keywords dict for groovy_groovydoc ruleset.
groovy_groovydoc_keywords_dict = {}

# Dictionary of keywords dictionaries for groovy mode.
keywordsDictDict = {
	"groovy_groovydoc": groovy_groovydoc_keywords_dict,
	"groovy_literal": groovy_literal_keywords_dict,
	"groovy_main": groovy_main_keywords_dict,
}

# Rules for groovy_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment1", seq="/**/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment3", begin="/**", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="GROOVYDOC",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="literal1", begin="<<<([[:alpha:]_][[:alnum:]_]*)\s*", end="$1",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="?",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq=".*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule20(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule21(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule9,],
	"\"": [rule3,],
	"&": [rule17,],
	"'": [rule4,],
	"(": [rule20,],
	"+": [rule13,],
	"-": [rule14,rule15,],
	".": [rule18,],
	"/": [rule0,rule1,rule2,rule19,],
	"0": [rule21,],
	"1": [rule21,],
	"2": [rule21,],
	"3": [rule21,],
	"4": [rule21,],
	"5": [rule21,],
	"6": [rule21,],
	"7": [rule21,],
	"8": [rule21,],
	"9": [rule21,],
	"<": [rule5,rule10,rule12,],
	"=": [rule6,rule7,],
	">": [rule11,],
	"?": [rule16,],
	"@": [rule21,],
	"A": [rule21,],
	"B": [rule21,],
	"C": [rule21,],
	"D": [rule21,],
	"E": [rule21,],
	"F": [rule21,],
	"G": [rule21,],
	"H": [rule21,],
	"I": [rule21,],
	"J": [rule21,],
	"K": [rule21,],
	"L": [rule21,],
	"M": [rule21,],
	"N": [rule21,],
	"O": [rule21,],
	"P": [rule21,],
	"Q": [rule21,],
	"R": [rule21,],
	"S": [rule21,],
	"T": [rule21,],
	"U": [rule21,],
	"V": [rule21,],
	"W": [rule21,],
	"X": [rule21,],
	"Y": [rule21,],
	"Z": [rule21,],
	"_": [rule21,],
	"a": [rule21,],
	"b": [rule21,],
	"c": [rule21,],
	"d": [rule21,],
	"e": [rule21,],
	"f": [rule21,],
	"g": [rule21,],
	"h": [rule21,],
	"i": [rule21,],
	"j": [rule21,],
	"k": [rule21,],
	"l": [rule21,],
	"m": [rule21,],
	"n": [rule21,],
	"o": [rule21,],
	"p": [rule21,],
	"q": [rule21,],
	"r": [rule21,],
	"s": [rule21,],
	"t": [rule21,],
	"u": [rule21,],
	"v": [rule21,],
	"w": [rule21,],
	"x": [rule21,],
	"y": [rule21,],
	"z": [rule21,],
	"|": [rule8,],
}

# Rules for groovy_literal ruleset.

def rule22(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="${", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule23(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

# Rules dict for literal ruleset.
rulesDict1 = {
	"$": [rule22,rule23,],
}

# Rules for groovy_groovydoc ruleset.

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment3", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment3", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule27(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment3", seq="<<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment3", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment3", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="xml::TAGS",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule31(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="label", pattern="@"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

# Rules dict for groovydoc ruleset.
rulesDict1 = {
	"*": [rule25,],
	"<": [rule26,rule27,rule28,rule29,rule30,],
	"@": [rule31,],
	"{": [rule24,],
}

# x.rulesDictDict for groovy mode.
rulesDictDict = {
	"groovy_groovydoc": rulesDict1,
	"groovy_literal": rulesDict1,
	"groovy_main": rulesDict1,
}

# Import dict for groovy mode.
importDict = {}

