# Leo colorizer control file for swig mode.
# This file is in the public domain.

# Properties for swig mode.
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

# Keywords dict for swig_main ruleset.
swig_main_keywords_dict = {}

# Dictionary of keywords dictionaries for swig mode.
keywordsDictDict = {
	"swig_main": swig_main_keywords_dict,
}

# Rules for swig_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="literal3", begin="%{", end="%}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword4", pattern="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)


# Rules dict for main ruleset.
rulesDict1 = {
	"%": [rule0,rule1,],
}

# x.rulesDictDict for swig mode.
rulesDictDict = {
	"swig_main": rulesDict1,
}

# Import dict for swig mode.
importDict = {
	"swig_main": ["c_main",],
}

