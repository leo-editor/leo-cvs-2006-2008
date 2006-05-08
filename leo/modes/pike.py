# Leo colorizer control file for pike mode.

# Properties for pike mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"doubleBracketIndent": "false",
	"indentCloseBrackets": "}",
	"indentNextLine": "\s*(((if|(for(each)?)|while|catch|gauge)\s*\(|(do|else)\s*|else\s+if\s*\()[^{;]*)",
	"indentOpenBrackets": "{",
	"lineComment": "//",
	"lineUpClosingBracket": "true",
	"wordBreakChars": ",+-=<>/?^&*`",
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
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="#.*?(?=($|/\*|//))",
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

# Rules list for pike_main ruleset.
pike_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
	rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29,
	rule30, rule31, ]

# Rules for pike_comment ruleset.

def rule32(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for pike_comment ruleset.
pike_comment_rules = [
	rule32, ]

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
    return colorer.match_seq_regexp(s, i, kind="function", seq="@(b|i|u|tt|url|pre|ref|code|expr|image)?(\{.*@\})",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule37(colorer, s, i):
    return colorer.match_keywords(s, i)

def rule38(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="null", seq="@decl",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="MAIN", exclude_match=False)

# Rules list for pike_autodoc ruleset.
pike_autodoc_rules = [
	rule33, rule34, rule35, rule36, rule37, rule38, ]

# Rules for pike_string_literal ruleset.

def rule39(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal2", seq="%([^ a-z]*[a-z]|\[[^\]]*\])",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule40(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="comment2", seq="DEBUG:",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

# Rules list for pike_string_literal ruleset.
pike_string_literal_rules = [
	rule39, rule40, ]

# Rules dict for pike mode.
rulesDict = {
	"pike_autodoc": pike_autodoc_rules,
	"pike_comment": pike_comment_rules,
	"pike_main": pike_main_rules,
	"pike_string_literal": pike_string_literal_rules,
}

# Import dict for pike mode.
importDict = {}

