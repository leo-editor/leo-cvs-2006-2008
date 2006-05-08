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

# Rules list for uscript_main ruleset.
uscript_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
	rule20, rule21, rule22, rule23, rule24, rule25, rule26, ]

# Rules dict for uscript mode.
rulesDict = {
	"uscript_main": uscript_main_rules,
}

# Import dict for uscript mode.
importDict = {}

