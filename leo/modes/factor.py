# Leo colorizer control file for factor mode.

# Properties for factor mode.
properties = {
	"commentEnd": ")",
	"commentStart": "(",
	"doubleBracketIndent": "true",
	"indentCloseBrackets": "]",
	"indentNextLines": "^(\*<<|:).*",
	"indentOpenBrackets": "[",
	"lineComment": "!",
	"lineUpClosingBracket": "true",
	"noWordSep": "+-*=><;.?/'",
}

# Keywords dict for factor_main ruleset.
factor_main_keywords_dict = {
	"#{": "operator",
	"--": "label",
	";": "markup",
	"<": "label",
	">": "label",
	"[": "operator",
	"]": "operator",
	"f": "literal4",
	"r": "keyword1",
	"t": "literal3",
	"{": "operator",
	"|": "operator",
	"}": "operator",
	"~": "label",
}

# Keywords dict for factor_stack_effect ruleset.
factor_stack_effect_keywords_dict = {}

# Rules for factor_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment2"', seq="#!",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment1"', seq="!",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind='"markup"', seq=":\s+(\S+)",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule3(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind='"markup"', seq="IN:\s+(\S+)",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind='"markup"', seq="USE:\s+(\S+)",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind='"markup"', seq="DEFER:\s+(\S+)",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind='"markup"', seq="POSTPONE:\s+(\S+)",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind='"literal2"', seq="CHAR:\s+(\S+)",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind='"literal2"', seq="BIN:\s+(\S+)",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind='"literal2"', seq="OCT:\s+(\S+)",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind='"literal2"', seq="HEX:\s+(\S+)",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment3"', begin="(", end=")",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="STACK_EFFECT",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule12(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule13(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for factor_main ruleset.
factor_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, ]

# Rules for factor_stack_effect ruleset.

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment3", seq="--",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

# Rules list for factor_stack_effect ruleset.
factor_stack_effect_rules = [
	rule14, ]

# Rules dict for factor mode.
rulesDict = {
	"factor_main": factor_main_rules,
	"factor_stack_effect": factor_stack_effect_rules,
}

# Import dict for factor mode.
importDict = {}

