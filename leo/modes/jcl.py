# Leo colorizer control file for jcl mode.

# Properties for jcl mode.
properties = {
	"wordBreakChars": ",+-=<>/?^&*",
}

# Keywords dict for jcl_main ruleset.
jcl_main_keywords_dict = {
	"CNTL": "keyword2",
	"COMMAND": "keyword2",
	"DD": "keyword2",
	"ELSE": "keyword2",
	"ENCNTL": "keyword2",
	"ENDIF": "keyword2",
	"EXEC": "keyword2",
	"IF": "keyword2",
	"INCLUDE": "keyword2",
	"JCLIB": "keyword2",
	"JOB": "keyword2",
	"MSG": "keyword2",
	"OUTPUT": "keyword2",
	"PEND": "keyword2",
	"PROC": "keyword2",
	"SET": "keyword2",
	"THEN": "keyword2",
	"XMIT": "keyword2",
}

# Dictionary of keywords dictionaries for jcl mode.
keywordsDictDict = {
	"jcl_main": jcl_main_keywords_dict,
}

# Rules for jcl_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="//*",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for jcl_main ruleset.
jcl_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, ]

# Rules dict for jcl mode.
rulesDict = {
	"jcl_main": jcl_main_rules,
}

# Import dict for jcl mode.
importDict = {}

