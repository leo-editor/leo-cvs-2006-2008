# Leo colorizer control file for tex mode.

# Properties for tex mode.
properties = {
	"lineComment": "%",
}

# Keywords dict for tex_main ruleset.
tex_main_keywords_dict = {}

# Keywords dict for tex_math ruleset.
tex_math_keywords_dict = {}

# Keywords dict for tex_verbatim ruleset.
tex_verbatim_keywords_dict = {}

# Dictionary of keywords dictionaries for tex mode.
keywordsDictDict = {
	"tex_main": tex_main_keywords_dict,
	"tex_math": tex_math_keywords_dict,
	"tex_verbatim": tex_verbatim_keywords_dict,
}

# Rules for tex_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="$$", end="$$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="MATH",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="$", end="$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="MATH",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="\[", end="\]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="MATH",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\\",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="\iffalse", end="\fi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule7(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword1", begin="\begin{verbatim}", end="\end{verbatim}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="VERBATIM",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule8(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword1", begin="\verb|", end="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="VERBATIM",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule9(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword1", pattern="\"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule10(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

# Rules dict for main ruleset.
rulesDict1 = {
	"$": [rule0,rule1,],
	"%": [rule10,],
	"[": [rule13,],
	"\": [rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,],
	"]": [rule14,],
	"{": [rule11,],
	"}": [rule12,],
}

# Rules for tex_math ruleset.

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\\",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword3", pattern="\"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule31(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule32(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule33(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule34(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule35(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule36(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule37(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq=".",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule38(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule39(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule40(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="?",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule41(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule42(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule43(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule44(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="`",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule45(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

# Rules dict for math ruleset.
rulesDict1 = {
	"!": [rule26,],
	"\"": [rule43,],
	"%": [rule45,],
	"&": [rule33,],
	"'": [rule42,],
	"(": [rule20,],
	")": [rule19,],
	"*": [rule30,],
	"+": [rule27,],
	",": [rule38,],
	"-": [rule28,],
	".": [rule37,],
	"/": [rule29,],
	":": [rule41,],
	";": [rule39,],
	"<": [rule32,],
	"=": [rule25,],
	">": [rule31,],
	"?": [rule40,],
	"[": [rule23,],
	"\": [rule15,rule16,rule17,rule18,],
	"]": [rule24,],
	"^": [rule35,],
	"`": [rule44,],
	"{": [rule21,],
	"|": [rule34,],
	"}": [rule22,],
	"~": [rule36,],
}

# Rules for tex_verbatim ruleset.

# Rules dict for verbatim ruleset.
rulesDict1 = {}

# x.rulesDictDict for tex mode.
rulesDictDict = {
	"tex_main": rulesDict1,
	"tex_math": rulesDict1,
	"tex_verbatim": rulesDict1,
}

# Import dict for tex mode.
importDict = {}

