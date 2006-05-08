# Leo colorizer control file for moin mode.

# Properties for moin mode.
properties = {
	"lineComment": "##",
	"wrap": "soft",
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
    return colorer.match_seq_regexp(s, i, kind="label", seq="\s+\w[[:alnum:][:blank:]]+::",
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
    return colorer.match_seq_regexp(s, i, kind="literal1", seq="('{2,5})[^']+\1[^']",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal4", seq="-{4,}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="keyword1", begin="(={1,5})", end="$1",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule9(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="A[a-z]+[A-Z][a-zA-Z]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="B[a-z]+[A-Z][a-zA-Z]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="C[a-z]+[A-Z][a-zA-Z]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="D[a-z]+[A-Z][a-zA-Z]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="E[a-z]+[A-Z][a-zA-Z]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="F[a-z]+[A-Z][a-zA-Z]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="G[a-z]+[A-Z][a-zA-Z]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="H[a-z]+[A-Z][a-zA-Z]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="I[a-z]+[A-Z][a-zA-Z]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="J[a-z]+[A-Z][a-zA-Z]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="K[a-z]+[A-Z][a-zA-Z]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="L[a-z]+[A-Z][a-zA-Z]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="M[a-z]+[A-Z][a-zA-Z]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="N[a-z]+[A-Z][a-zA-Z]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="O[a-z]+[A-Z][a-zA-Z]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="P[a-z]+[A-Z][a-zA-Z]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="Q[a-z]+[A-Z][a-zA-Z]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="R[a-z]+[A-Z][a-zA-Z]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="S[a-z]+[A-Z][a-zA-Z]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="T[a-z]+[A-Z][a-zA-Z]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="U[a-z]+[A-Z][a-zA-Z]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="V[a-z]+[A-Z][a-zA-Z]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule31(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="W[a-z]+[A-Z][a-zA-Z]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule32(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="X[a-z]+[A-Z][a-zA-Z]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule33(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="Y[a-z]+[A-Z][a-zA-Z]+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule34(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="Z[a-z]+[A-Z][a-zA-Z]+",
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
	"\": [rule3,],
	"`": [rule5,],
	"{": [rule4,],
}

# x.rulesDictDict for moin mode.
rulesDictDict = {
	"moin_main": rulesDict1,
}

# Import dict for moin mode.
importDict = {}

