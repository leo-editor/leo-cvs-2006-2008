# Leo colorizer control file for factor mode.
# This file is in the public domain.

# Properties for factor mode.
properties = {
	"commentEnd": ")",
	"commentStart": "(",
	"doubleBracketIndent": "true",
	"indentCloseBrackets": "]",
	"indentNextLines": "^(\\*<<|:).*",
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

# Dictionary of keywords dictionaries for factor mode.
keywordsDictDict = {
	"factor_main": factor_main_keywords_dict,
	"factor_stack_effect": factor_stack_effect_keywords_dict,
}

# Rules for factor_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="#!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="markup", seq=":\\s+(\\S+)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule3(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="markup", seq="IN:\\s+(\\S+)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="markup", seq="USE:\\s+(\\S+)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="markup", seq="DEFER:\\s+(\\S+)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="markup", seq="POSTPONE:\\s+(\\S+)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal2", seq="CHAR:\\s+(\\S+)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal2", seq="BIN:\\s+(\\S+)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal2", seq="OCT:\\s+(\\S+)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal2", seq="HEX:\\s+(\\S+)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_span(s, i, kind="comment3", begin="(", end=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="STACK_EFFECT",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule12(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule13(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule1,],
	"\"": [rule12,],
	"#": [rule0,],
	"(": [rule11,],
	"0": [rule13,],
	"1": [rule13,],
	"2": [rule13,],
	"3": [rule13,],
	"4": [rule13,],
	"5": [rule13,],
	"6": [rule13,],
	"7": [rule13,],
	"8": [rule13,],
	"9": [rule13,],
	":": [rule2,],
	"@": [rule13,],
	"A": [rule13,],
	"B": [rule8,rule13,],
	"C": [rule7,rule13,],
	"D": [rule5,rule13,],
	"E": [rule13,],
	"F": [rule13,],
	"G": [rule13,],
	"H": [rule10,rule13,],
	"I": [rule3,rule13,],
	"J": [rule13,],
	"K": [rule13,],
	"L": [rule13,],
	"M": [rule13,],
	"N": [rule13,],
	"O": [rule9,rule13,],
	"P": [rule6,rule13,],
	"Q": [rule13,],
	"R": [rule13,],
	"S": [rule13,],
	"T": [rule13,],
	"U": [rule4,rule13,],
	"V": [rule13,],
	"W": [rule13,],
	"X": [rule13,],
	"Y": [rule13,],
	"Z": [rule13,],
	"_": [rule13,],
	"a": [rule13,],
	"b": [rule13,],
	"c": [rule13,],
	"d": [rule13,],
	"e": [rule13,],
	"f": [rule13,],
	"g": [rule13,],
	"h": [rule13,],
	"i": [rule13,],
	"j": [rule13,],
	"k": [rule13,],
	"l": [rule13,],
	"m": [rule13,],
	"n": [rule13,],
	"o": [rule13,],
	"p": [rule13,],
	"q": [rule13,],
	"r": [rule13,],
	"s": [rule13,],
	"t": [rule13,],
	"u": [rule13,],
	"v": [rule13,],
	"w": [rule13,],
	"x": [rule13,],
	"y": [rule13,],
	"z": [rule13,],
}

# Rules for factor_stack_effect ruleset.

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment3", seq="--",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

# Rules dict for stack_effect ruleset.
rulesDict2 = {
	"-": [rule14,],
}

# x.rulesDictDict for factor mode.
rulesDictDict = {
	"factor_main": rulesDict1,
	"factor_stack_effect": rulesDict2,
}

# Import dict for factor mode.
importDict = {}

