# Leo colorizer control file for rest mode.

# Properties for rest mode.
properties = {
	"indentNextLines": ".+::$",
	"lineComment": "..",
}

# Keywords dict for rest_main ruleset.
rest_main_keywords_dict = {}

# Dictionary of keywords dictionaries for rest mode.
keywordsDictDict = {
	"rest_main": rest_main_keywords_dict,
}

# Rules for rest_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="keyword3", seq="__",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="keyword3", seq=".. _",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="label", seq="={3,}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule3(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="label", seq="-{3,}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="label", seq="~{3,}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="label", seq="`{3,}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="label", seq="#{3,}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="label", seq="\"{3,}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="label", seq="\^{3,}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="label", seq="\+{3,}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="label", seq="\*{3,}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal3", seq="\.\.\s\|[^|]+\|",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal4", seq="\|[^|]+\|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal2", seq="\.\.\s[A-z][A-z0-9-_]+::",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="\*\*[^*]+\*\*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword4", seq="\*[^\s*][^*]*\*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="..",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule17(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="label", seq="`[A-z0-9]+[^`]+`_{1,2}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="label", seq="\[[0-9]+\]_",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="label", seq="\[#[A-z0-9_]*\]_",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="label", seq="\[*\]_",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="label", seq="\[[A-z][A-z0-9_-]*\]_",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="``", end="``",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule23(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword1", seq="`[^`]+`",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword1", seq=":[A-z][A-z0-9 	=\s\t_]*:",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="label", seq="\+-[+-]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="label", seq="\+=[+=]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

# Rules list for rest_main ruleset.
rest_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
	rule20, rule21, rule22, rule23, rule24, rule25, rule26, ]

# Rules dict for rest mode.
rulesDict = {
	"rest_main": rest_main_rules,
}

# Import dict for rest mode.
importDict = {}

