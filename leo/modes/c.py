# Leo colorizer control file for c mode.

# Properties for c mode.
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

# Keywords dict for c_main ruleset.
c_main_keywords_dict = {
	"NULL": "literal2",
	"asm": "keyword2",
	"asmlinkage": "keyword2",
	"auto": "keyword1",
	"break": "keyword1",
	"case": "keyword1",
	"char": "keyword3",
	"const": "keyword1",
	"continue": "keyword1",
	"default": "keyword1",
	"do": "keyword1",
	"double": "keyword3",
	"else": "keyword1",
	"enum": "keyword3",
	"extern": "keyword1",
	"false": "literal2",
	"far": "keyword2",
	"float": "keyword3",
	"for": "keyword1",
	"goto": "keyword1",
	"huge": "keyword2",
	"if": "keyword1",
	"inline": "keyword2",
	"int": "keyword3",
	"long": "keyword3",
	"near": "keyword2",
	"pascal": "keyword2",
	"register": "keyword1",
	"return": "keyword1",
	"short": "keyword3",
	"signed": "keyword3",
	"sizeof": "keyword1",
	"static": "keyword1",
	"struct": "keyword3",
	"switch": "keyword1",
	"true": "literal2",
	"typedef": "keyword3",
	"union": "keyword3",
	"unsigned": "keyword3",
	"void": "keyword3",
	"volatile": "keyword1",
	"while": "keyword1",
}

# Keywords dict for c_cpp ruleset.
c_cpp_keywords_dict = {
	"assert": "markup",
	"define": "markup",
	"elif": "markup",
	"else": "markup",
	"endif": "markup",
	"error": "markup",
	"ident": "markup",
	"if": "markup",
	"ifdef": "markup",
	"ifndef": "markup",
	"import": "markup",
	"include": "markup",
	"include_next": "markup",
	"line": "markup",
	"pragma": "markup",
	"sccs": "markup",
	"unassert": "markup",
	"undef": "markup",
	"warning": "markup",
}

# Keywords dict for c_include ruleset.
c_include_keywords_dict = {}

# Dictionary of keywords dictionaries for c mode.
keywordsDictDict = {
	"c_cpp": c_cpp_keywords_dict,
	"c_include": c_include_keywords_dict,
	"c_main": c_main_keywords_dict,
}

# Rules for c_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment3", begin="/**", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="doxygen::DOXYGEN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment3", begin="/*!", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="doxygen::DOXYGEN",exclude_match=False,
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
    return colorer.match_seq(s, i, kind="keyword2", seq="##",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="keyword2", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="CPP", exclude_match=False)

def rule7(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=False, at_whitespace_end=True, at_word_start=False, exclude_match=True)

def rule26(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule27(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for c_main ruleset.
c_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
	rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, ]

# Rules for c_cpp ruleset.

def rule28(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule29(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="markup", seq="include",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="INCLUDE", exclude_match=False)

def rule30(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for c_cpp ruleset.
c_cpp_rules = [
	rule28, rule29, rule30, ]

# Rules for c_include ruleset.

# Rules list for c_include ruleset.
c_include_rules = []

# Rules dict for c mode.
rulesDict = {
	"c_cpp": c_cpp_rules,
	"c_include": c_include_rules,
	"c_main": c_main_rules,
}

# Import dict for c mode.
importDict = {}

