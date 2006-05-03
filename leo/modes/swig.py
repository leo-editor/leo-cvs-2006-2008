# Leo colorizer control file for swig mode.

# Properties for swig mode.
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

# Keywords dict for swig_main ruleset.
swig_main_keywords_dict = {}

# Rules for swig_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal3"', begin="%{", end="%}",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_mark_following(s, i, kind='"keyword4"', 
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=False)


# Rules list for swig_main ruleset.
swig_main_rules = [
	rule0, rule1, ]

# Rules dict for swig mode.
rulesDict = {
	"swig_main": swig_main_rules,
}

# Import dict for swig mode.
importDict = {
	"swig_main": "c_main",
}

