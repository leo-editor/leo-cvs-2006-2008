# Leo colorizer control file for shell mode.

# Properties for shell mode.
properties = {
	"indentCloseBrackets": "}",
	"indentOpenBrackets": "{",
	"lineComment": "#",
	"lineUpClosingBracket": "true",
}

# Keywords dict for shell_main ruleset.
shell_main_keywords_dict = {
	";;": "operator",
	"case": "keyword1",
	"continue": "keyword1",
	"do": "keyword1",
	"done": "keyword1",
	"elif": "keyword1",
	"else": "keyword1",
	"esac": "keyword1",
	"fi": "keyword1",
	"for": "keyword1",
	"if": "keyword1",
	"in": "keyword1",
	"local": "keyword1",
	"return": "keyword1",
	"then": "keyword1",
	"while": "keyword1",
}

# Keywords dict for shell_literal ruleset.
shell_literal_keywords_dict = {}

# Keywords dict for shell_exec ruleset.
shell_exec_keywords_dict = {}

# Dictionary of keywords dictionaries for shell mode.
keywordsDictDict = {
	"shell_exec": shell_exec_keywords_dict,
	"shell_literal": shell_literal_keywords_dict,
	"shell_main": shell_main_keywords_dict,
}

# Rules for shell_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="#!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="${", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$?",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule5(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule6(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule7(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule8(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule9(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule10(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="keyword2", pattern="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule11(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword3", begin="$((", end="))",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="EXEC",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule12(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword3", begin="$(", end=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="EXEC",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule13(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword3", begin="$[", end="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="EXEC",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule14(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword3", begin="`", end="`",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="EXEC",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule15(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule16(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule17(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="literal1", begin="<<[[:space:]'\"]*([[:alnum:]_]+)[[:space:]'\"]*", end="$1",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule24(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule25(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule20,],
	"\"": [rule15,],
	"#": [rule0,rule1,],
	"$": [rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule11,rule12,rule13,],
	"%": [rule23,],
	"&": [rule19,],
	"'": [rule16,],
	"(": [rule24,],
	"0": [rule25,],
	"1": [rule25,],
	"2": [rule25,],
	"3": [rule25,],
	"4": [rule25,],
	"5": [rule25,],
	"6": [rule25,],
	"7": [rule25,],
	"8": [rule25,],
	"9": [rule25,],
	"<": [rule17,rule22,],
	"=": [rule10,],
	">": [rule21,],
	"@": [rule25,],
	"A": [rule25,],
	"B": [rule25,],
	"C": [rule25,],
	"D": [rule25,],
	"E": [rule25,],
	"F": [rule25,],
	"G": [rule25,],
	"H": [rule25,],
	"I": [rule25,],
	"J": [rule25,],
	"K": [rule25,],
	"L": [rule25,],
	"M": [rule25,],
	"N": [rule25,],
	"O": [rule25,],
	"P": [rule25,],
	"Q": [rule25,],
	"R": [rule25,],
	"S": [rule25,],
	"T": [rule25,],
	"U": [rule25,],
	"V": [rule25,],
	"W": [rule25,],
	"X": [rule25,],
	"Y": [rule25,],
	"Z": [rule25,],
	"_": [rule25,],
	"`": [rule14,],
	"a": [rule25,],
	"b": [rule25,],
	"c": [rule25,],
	"d": [rule25,],
	"e": [rule25,],
	"f": [rule25,],
	"g": [rule25,],
	"h": [rule25,],
	"i": [rule25,],
	"j": [rule25,],
	"k": [rule25,],
	"l": [rule25,],
	"m": [rule25,],
	"n": [rule25,],
	"o": [rule25,],
	"p": [rule25,],
	"q": [rule25,],
	"r": [rule25,],
	"s": [rule25,],
	"t": [rule25,],
	"u": [rule25,],
	"v": [rule25,],
	"w": [rule25,],
	"x": [rule25,],
	"y": [rule25,],
	"z": [rule25,],
	"|": [rule18,],
}

# Rules for shell_literal ruleset.

def rule26(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="${", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule27(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

# Rules dict for literal ruleset.
rulesDict2 = {
	"$": [rule26,rule27,],
}

# Rules for shell_exec ruleset.

def rule28(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="${", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule29(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword3", begin="$((", end="))",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule30(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword3", begin="$(", end=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule31(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword3", begin="$[", end="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule32(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule33(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule34(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule35(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule36(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule37(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

# Rules dict for exec ruleset.
rulesDict3 = {
	"!": [rule35,],
	"$": [rule28,rule29,rule30,rule31,rule32,],
	"&": [rule34,],
	"<": [rule37,],
	">": [rule36,],
	"|": [rule33,],
}

# x.rulesDictDict for shell mode.
rulesDictDict = {
	"shell_exec": rulesDict3,
	"shell_literal": rulesDict2,
	"shell_main": rulesDict1,
}

# Import dict for shell mode.
importDict = {}

