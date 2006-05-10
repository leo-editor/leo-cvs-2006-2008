# Leo colorizer control file for pike mode.
# This file is in the public domain.

# Properties for pike mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"doubleBracketIndent": "false",
	"indentCloseBrackets": "}",
	"indentNextLine": "\\s*(((if|(for(each)?)|while|catch|gauge)\\s*\\(|(do|else)\\s*|else\\s+if\\s*\\()[^{;]*)",
	"indentOpenBrackets": "{",
	"lineComment": "//",
	"lineUpClosingBracket": "true",
	"wordBreakChars": ",+-=<>/?^&*`",
}

# Attributes dict for pike_main ruleset.
pike_main_attributes_dict = {
	"default": "null",
	"digit_re": "(0x[[:xdigit:]]+|[[:digit]]+|0[bB][01]+)[lLdDfF]?",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Attributes dict for pike_comment ruleset.
pike_comment_attributes_dict = {
	"default": "COMMENT1",
	"digit_re": "(0x[[:xdigit:]]+|[[:digit]]+|0[bB][01]+)[lLdDfF]?",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Attributes dict for pike_autodoc ruleset.
pike_autodoc_attributes_dict = {
	"default": "COMMENT1",
	"digit_re": "(0x[[:xdigit:]]+|[[:digit]]+|0[bB][01]+)[lLdDfF]?",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for pike_string_literal ruleset.
pike_string_literal_attributes_dict = {
	"default": "LITERAL1",
	"digit_re": "(0x[[:xdigit:]]+|[[:digit]]+|0[bB][01]+)[lLdDfF]?",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for pike mode.
attributesDictDict = {
	"pike_autodoc": pike_autodoc_attributes_dict,
	"pike_comment": pike_comment_attributes_dict,
	"pike_main": pike_main_attributes_dict,
	"pike_string_literal": pike_string_literal_attributes_dict,
}

# Keywords dict for pike_main ruleset.
pike_main_keywords_dict = {
	"array": "keyword3",
	"break": "keyword1",
	"case": "keyword1",
	"catch": "keyword1",
	"class": "keyword3",
	"constant": "keyword1",
	"continue": "keyword1",
	"default": "keyword1",
	"do": "keyword1",
	"else": "keyword1",
	"extern": "keyword1",
	"final": "keyword1",
	"float": "keyword3",
	"for": "keyword1",
	"foreach": "keyword1",
	"function": "keyword3",
	"gauge": "keyword1",
	"if": "keyword1",
	"import": "keyword2",
	"inherit": "keyword2",
	"inline": "keyword1",
	"int": "keyword3",
	"lambda": "keyword1",
	"local": "keyword1",
	"mapping": "keyword3",
	"mixed": "keyword3",
	"multiset": "keyword3",
	"nomask": "keyword1",
	"object": "keyword3",
	"optional": "keyword1",
	"private": "keyword1",
	"program": "keyword3",
	"protected": "keyword1",
	"public": "keyword1",
	"return": "keyword1",
	"sscanf": "keyword1",
	"static": "keyword1",
	"string": "keyword3",
	"switch": "keyword1",
	"variant": "keyword1",
	"void": "keyword3",
	"while": "keyword1",
}

# Keywords dict for pike_comment ruleset.
pike_comment_keywords_dict = {
	"FIXME": "comment2",
	"XXX": "comment2",
}

# Keywords dict for pike_autodoc ruleset.
pike_autodoc_keywords_dict = {
	"@appears": "label",
	"@array": "label",
	"@belongs": "label",
	"@bugs": "label",
	"@class": "label",
	"@constant": "label",
	"@deprecated": "label",
	"@dl": "label",
	"@elem": "label",
	"@endarray": "label",
	"@endclass": "label",
	"@enddl": "label",
	"@endignore": "label",
	"@endint": "label",
	"@endmapping": "label",
	"@endmixed": "label",
	"@endmodule": "label",
	"@endmultiset": "label",
	"@endnamespace": "label",
	"@endol": "label",
	"@endstring": "label",
	"@example": "label",
	"@fixme": "label",
	"@ignore": "label",
	"@index": "label",
	"@int": "label",
	"@item": "label",
	"@mapping": "label",
	"@member": "label",
	"@mixed": "label",
	"@module": "label",
	"@multiset": "label",
	"@namespace": "label",
	"@note": "label",
	"@ol": "label",
	"@param": "label",
	"@returns": "label",
	"@section": "label",
	"@seealso": "label",
	"@string": "label",
	"@throws": "label",
	"@type": "label",
	"@ul": "label",
	"@value": "label",
}

# Keywords dict for pike_string_literal ruleset.
pike_string_literal_keywords_dict = {}

# Dictionary of keywords dictionaries for pike mode.
keywordsDictDict = {
	"pike_autodoc": pike_autodoc_keywords_dict,
	"pike_comment": pike_comment_keywords_dict,
	"pike_main": pike_main_keywords_dict,
	"pike_string_literal": pike_string_literal_keywords_dict,
}

# Rules for pike_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="COMMENT",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="//!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="AUTODOC", exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="COMMENT", exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="STRING_LITERAL",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="#\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="STRING_LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule7(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="#.*?(?=($|/\\*|//))",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="({",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="})",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="([",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="])",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="(<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="`",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule31(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule15,],
	"\"": [rule4,],
	"#": [rule5,rule7,],
	"%": [rule22,],
	"&": [rule23,],
	"'": [rule6,],
	"(": [rule8,rule10,rule12,rule30,],
	"*": [rule1,rule19,],
	"+": [rule16,],
	"-": [rule17,],
	".": [rule29,],
	"/": [rule0,rule2,rule3,rule18,],
	"0": [rule31,],
	"1": [rule31,],
	"2": [rule31,],
	"3": [rule31,],
	"4": [rule31,],
	"5": [rule31,],
	"6": [rule31,],
	"7": [rule31,],
	"8": [rule31,],
	"9": [rule31,],
	"<": [rule21,],
	"=": [rule14,],
	">": [rule13,rule20,],
	"@": [rule27,rule31,],
	"A": [rule31,],
	"B": [rule31,],
	"C": [rule31,],
	"D": [rule31,],
	"E": [rule31,],
	"F": [rule31,],
	"G": [rule31,],
	"H": [rule31,],
	"I": [rule31,],
	"J": [rule31,],
	"K": [rule31,],
	"L": [rule31,],
	"M": [rule31,],
	"N": [rule31,],
	"O": [rule31,],
	"P": [rule31,],
	"Q": [rule31,],
	"R": [rule31,],
	"S": [rule31,],
	"T": [rule31,],
	"U": [rule31,],
	"V": [rule31,],
	"W": [rule31,],
	"X": [rule31,],
	"Y": [rule31,],
	"Z": [rule31,],
	"]": [rule11,],
	"^": [rule25,],
	"_": [rule31,],
	"`": [rule28,],
	"a": [rule31,],
	"b": [rule31,],
	"c": [rule31,],
	"d": [rule31,],
	"e": [rule31,],
	"f": [rule31,],
	"g": [rule31,],
	"h": [rule31,],
	"i": [rule31,],
	"j": [rule31,],
	"k": [rule31,],
	"l": [rule31,],
	"m": [rule31,],
	"n": [rule31,],
	"o": [rule31,],
	"p": [rule31,],
	"q": [rule31,],
	"r": [rule31,],
	"s": [rule31,],
	"t": [rule31,],
	"u": [rule31,],
	"v": [rule31,],
	"w": [rule31,],
	"x": [rule31,],
	"y": [rule31,],
	"z": [rule31,],
	"|": [rule24,],
	"}": [rule9,],
	"~": [rule26,],
}

# Rules for pike_comment ruleset.

def rule32(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for comment ruleset.
rulesDict2 = {
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
}

# Rules for pike_autodoc ruleset.

def rule33(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="null", seq="@decl",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="MAIN", exclude_match=True)

def rule34(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="@xml{", end="@}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="xml::TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule35(colorer, s, i):
    return colorer.match_span(s, i, kind="function", begin="@[", end="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule36(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="function", seq="@(b|i|u|tt|url|pre|ref|code|expr|image)?(\\{.*@\\})",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule37(colorer, s, i):
    return colorer.match_keywords(s, i)

def rule38(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="null", seq="@decl",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="MAIN", exclude_match=False)

# Rules dict for autodoc ruleset.
rulesDict3 = {
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
	"@": [rule33,rule34,rule35,rule36,rule37,rule38,],
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
}

# Rules for pike_string_literal ruleset.

def rule39(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal2", seq="%([^ a-z]*[a-z]|\\[[^\\]]*\\])",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule40(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="comment2", seq="DEBUG:",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

# Rules dict for string_literal ruleset.
rulesDict4 = {
	"%": [rule39,],
	"D": [rule40,],
}

# x.rulesDictDict for pike mode.
rulesDictDict = {
	"pike_autodoc": rulesDict3,
	"pike_comment": rulesDict2,
	"pike_main": rulesDict1,
	"pike_string_literal": rulesDict4,
}

# Import dict for pike mode.
importDict = {}

