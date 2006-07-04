# Leo colorizer control file for moin mode.
# This file is in the public domain.

# Properties for moin mode.
properties = {
	"lineComment": "##",
	"wrap": "soft",
}

# Attributes dict for moin_main ruleset.
moin_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "false",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for moin mode.
attributesDictDict = {
	"moin_main": moin_main_attributes_dict,
}

# Keywords dict for moin_main ruleset.
moin_main_keywords_dict = {}

# Dictionary of keywords dictionaries for moin mode.
keywordsDictDict = {
	"moin_main": moin_main_keywords_dict,
}

# Rules for moin_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="##",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="keyword2", seq="#pragma",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword4", begin="[[", end="]]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="label", regexp="\\s+\\w[[:alnum:][:blank:]]+::", hash_char=" ",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="{{{", end="}}}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="`", end="`",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal1", regexp="('{2,5})[^']+\\1[^']", hash_char="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal4", regexp="-{4,}", hash_char="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword1", begin="(={1,5})", end="$1", hash_char="=",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule9(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="A[a-z]+[A-Z][a-zA-Z]+", hash_char="A",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="B[a-z]+[A-Z][a-zA-Z]+", hash_char="B",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="C[a-z]+[A-Z][a-zA-Z]+", hash_char="C",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="D[a-z]+[A-Z][a-zA-Z]+", hash_char="D",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="E[a-z]+[A-Z][a-zA-Z]+", hash_char="E",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="F[a-z]+[A-Z][a-zA-Z]+", hash_char="F",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="G[a-z]+[A-Z][a-zA-Z]+", hash_char="G",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="H[a-z]+[A-Z][a-zA-Z]+", hash_char="H",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="I[a-z]+[A-Z][a-zA-Z]+", hash_char="I",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="J[a-z]+[A-Z][a-zA-Z]+", hash_char="J",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="K[a-z]+[A-Z][a-zA-Z]+", hash_char="K",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="L[a-z]+[A-Z][a-zA-Z]+", hash_char="L",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="M[a-z]+[A-Z][a-zA-Z]+", hash_char="M",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="N[a-z]+[A-Z][a-zA-Z]+", hash_char="N",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="O[a-z]+[A-Z][a-zA-Z]+", hash_char="O",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="P[a-z]+[A-Z][a-zA-Z]+", hash_char="P",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="Q[a-z]+[A-Z][a-zA-Z]+", hash_char="Q",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="R[a-z]+[A-Z][a-zA-Z]+", hash_char="R",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="S[a-z]+[A-Z][a-zA-Z]+", hash_char="S",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="T[a-z]+[A-Z][a-zA-Z]+", hash_char="T",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="U[a-z]+[A-Z][a-zA-Z]+", hash_char="U",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="V[a-z]+[A-Z][a-zA-Z]+", hash_char="V",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule31(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="W[a-z]+[A-Z][a-zA-Z]+", hash_char="W",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule32(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="X[a-z]+[A-Z][a-zA-Z]+", hash_char="X",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule33(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="Y[a-z]+[A-Z][a-zA-Z]+", hash_char="Y",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule34(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", regexp="Z[a-z]+[A-Z][a-zA-Z]+", hash_char="Z",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule35(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="[\"", end="\"]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule36(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword3", begin="[", end="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules dict for main ruleset.
rulesDict1 = {
	"#": [rule0,rule1,],
	"(": [rule6,rule8,],
	"-": [rule7,],
	"A": [rule9,],
	"B": [rule10,],
	"C": [rule11,],
	"D": [rule12,],
	"E": [rule13,],
	"F": [rule14,],
	"G": [rule15,],
	"H": [rule16,],
	"I": [rule17,],
	"J": [rule18,],
	"K": [rule19,],
	"L": [rule20,],
	"M": [rule21,],
	"N": [rule22,],
	"O": [rule23,],
	"P": [rule24,],
	"Q": [rule25,],
	"R": [rule26,],
	"S": [rule27,],
	"T": [rule28,],
	"U": [rule29,],
	"V": [rule30,],
	"W": [rule31,],
	"X": [rule32,],
	"Y": [rule33,],
	"Z": [rule34,],
	"[": [rule2,rule35,rule36,],
	"\\": [rule3,],
	"`": [rule5,],
	"{": [rule4,],
}

# x.rulesDictDict for moin mode.
rulesDictDict = {
	"moin_main": rulesDict1,
}

# Import dict for moin mode.
importDict = {}

