# Leo colorizer control file for jmk mode.

# Properties for jmk mode.
properties = {
	"indentCloseBrackets": "}",
	"indentOpenBrackets": "{",
	"lineComment": "#",
	"lineUpClosingBracket": "true",
}

# Keywords dict for jmk_main ruleset.
jmk_main_keywords_dict = {
	"%": "keyword2",
	"<": "keyword2",
	"?": "keyword2",
	"@": "keyword2",
	"cat": "keyword1",
	"copy": "keyword1",
	"create": "keyword1",
	"delall": "keyword1",
	"delete": "keyword1",
	"dirs": "keyword1",
	"else": "keyword1",
	"end": "keyword1",
	"equal": "keyword1",
	"exec": "keyword1",
	"first": "keyword1",
	"forname": "keyword1",
	"function": "keyword1",
	"getprop": "keyword1",
	"glob": "keyword1",
	"if": "keyword1",
	"include": "keyword3",
	"join": "keyword1",
	"load": "keyword1",
	"mkdir": "keyword1",
	"mkdirs": "keyword1",
	"note": "keyword1",
	"patsubst": "keyword1",
	"rename": "keyword1",
	"rest": "keyword1",
	"subst": "keyword1",
	"then": "keyword1",
}

# Rules for jmk_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment1"', seq="#",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="'", end="'",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="(",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=")",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for jmk_main ruleset.
jmk_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
]

# Rules dict for jmk mode.
rulesDict = {
	"jmk_main": jmk_main_rules,
}

# Import dict for jmk mode.
importDict = {}

