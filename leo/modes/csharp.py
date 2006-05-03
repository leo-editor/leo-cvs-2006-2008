# Leo colorizer control file for csharp mode.

# Properties for csharp mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"doubleBracketIndent": "false",
	"indentCloseBrackets": "}",
	"indentNextLine": "\s*(((if|while)\s*\(|else\s*|else\s+if\s*\(|for\s*\(.*\))[^{;]*)",
	"indentOpenBrackets": "{",
	"lineComment": "//",
	"lineUpClosingBracket": "true",
}

# Keywords dict for csharp_main ruleset.
csharp_main_keywords_dict = {
	"abstract": "keyword1",
	"as": "keyword1",
	"base": "keyword1",
	"bool": "keyword3",
	"break": "keyword1",
	"byte": "keyword3",
	"case": "keyword1",
	"catch": "keyword1",
	"char": "keyword3",
	"checked": "keyword1",
	"class": "keyword3",
	"const": "keyword1",
	"continue": "keyword1",
	"decimal": "keyword1",
	"default": "keyword1",
	"delegate": "keyword1",
	"do": "keyword1",
	"double": "keyword3",
	"else": "keyword1",
	"enum": "keyword3",
	"event": "keyword3",
	"explicit": "keyword1",
	"extern": "keyword1",
	"false": "literal2",
	"finally": "keyword1",
	"fixed": "keyword1",
	"float": "keyword3",
	"for": "keyword1",
	"foreach": "keyword1",
	"goto": "keyword1",
	"if": "keyword1",
	"implicit": "keyword1",
	"in": "keyword1",
	"int": "keyword3",
	"interface": "keyword3",
	"internal": "keyword1",
	"is": "keyword1",
	"lock": "keyword1",
	"long": "keyword3",
	"namespace": "keyword2",
	"new": "keyword1",
	"null": "literal2",
	"object": "keyword3",
	"operator": "keyword1",
	"out": "keyword1",
	"override": "keyword1",
	"params": "keyword1",
	"private": "keyword1",
	"protected": "keyword1",
	"public": "keyword1",
	"readonly": "keyword1",
	"ref": "keyword1",
	"return": "keyword1",
	"sbyte": "keyword3",
	"sealed": "keyword1",
	"short": "keyword3",
	"sizeof": "keyword1",
	"stackalloc": "keyword1",
	"static": "keyword1",
	"string": "keyword3",
	"struct": "keyword3",
	"switch": "keyword1",
	"this": "literal2",
	"throw": "keyword1",
	"true": "literal2",
	"try": "keyword1",
	"typeof": "keyword1",
	"uint": "keyword3",
	"ulong": "keyword3",
	"unchecked": "keyword1",
	"unsafe": "keyword1",
	"ushort": "keyword3",
	"using": "keyword2",
	"virtual": "keyword1",
	"void": "keyword3",
	"while": "keyword1",
}

# Keywords dict for csharp_doc_comment ruleset.
csharp_doc_comment_keywords_dict = {}

# Rules for csharp_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment1"', begin="/*", end="*/",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment3"', seq="///",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="DOC_COMMENT", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment2"', seq="//",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal3"', begin="@\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=True, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="'", end="'",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"keyword2"', seq="#if",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule7(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"keyword2"', seq="#else",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule8(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"keyword2"', seq="#elif",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule9(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"keyword2"', seq="#endif",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule10(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"keyword2"', seq="#define",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule11(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"keyword2"', seq="#undef",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule12(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"keyword2"', seq="#warning",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule13(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"keyword2"', seq="#error",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule14(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"keyword2"', seq="#line",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule15(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"keyword2"', seq="#region",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule16(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"keyword2"', seq="#endregion",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=";",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="]",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule31(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule32(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule33(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule34(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule35(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule36(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule37(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule38(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule39(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule40(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="?",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule41(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind='"function"',
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=True)

def rule42(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for csharp_main ruleset.
csharp_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
	rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29,
	rule30, rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39,
	rule40, rule41, rule42, ]

# Rules for csharp_doc_comment ruleset.

def rule43(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment1"', begin="<--", end="-->",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule44(colorer, s, i):
    return colorer.match_span(s, i, kind='"markup"', begin="<", end=">",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="xml::TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules list for csharp_doc_comment ruleset.
csharp_doc_comment_rules = [
	rule43, rule44, ]

# Rules dict for csharp mode.
rulesDict = {
	"csharp_doc_comment": csharp_doc_comment_rules,
	"csharp_main": csharp_main_rules,
}

# Import dict for csharp mode.
importDict = {}

