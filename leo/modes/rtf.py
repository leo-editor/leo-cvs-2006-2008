# Leo colorizer control file for rtf mode.

# Properties for rtf mode.
properties = {}

# Keywords dict for rtf_main ruleset.
rtf_main_keywords_dict = {}

# Dictionary of keywords dictionaries for rtf mode.
keywordsDictDict = {
	"rtf_main": rtf_main_keywords_dict,
}

# Rules for rtf_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal2", seq="\\'\w\d",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule3(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="\*\"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword1", pattern="\"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

# Rules dict for main ruleset.
rulesDict1 = {
	"\": [rule2,rule3,rule4,],
	"{": [rule0,],
	"}": [rule1,],
}

# x.rulesDictDict for rtf mode.
rulesDictDict = {
	"rtf_main": rulesDict1,
}

# Import dict for rtf mode.
importDict = {}

