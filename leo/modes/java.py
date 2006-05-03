# Leo colorizer control file for java mode.

# Properties for java mode.
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

# Rules for java_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment1", seq="/**/",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment3"', begin="/**", end="*/",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="JAVADOC",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment1"', begin="/*", end="*/",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="'", end="'",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment2"', seq="//",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq=".*",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind='"label"',
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=True)

def rule25(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind='"function"',
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=True)

def rule26(colorer, s, i):
    return colorer.match_mark_following(s, i, kind='"keyword4"', 
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=False)

def rule27(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for java_main ruleset.
java_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
	rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, ]

# Rules for java_javadoc ruleset.

def rule28(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment3", seq="{",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment3", seq="*",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment1"', begin="<!--", end="-->",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule31(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment3", seq="<<",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule32(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment3", seq="<=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule33(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment3", seq="<",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule34(colorer, s, i):
    return colorer.match_span(s, i, kind='"markup"', begin="<", end=">",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="xml::TAGS",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule35(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for java_javadoc ruleset.
java_javadoc_rules = [
	rule28, rule29, rule30, rule31, rule32, rule33, rule34, rule35, ]

# Rules dict for java mode.
rulesDict = {
	"java_javadoc": java_javadoc_rules,
	"java_main": java_main_rules,
}

# Import dict for java mode.
importDict = {}

