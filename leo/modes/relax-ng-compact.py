# Leo colorizer control file for relax-ng-compact mode.

# Properties for relax-ng-compact mode.
properties = {
	"doubleBracketIndent": "false",
	"indentCloseBrackets": "}",
	"indentOpenBrackets": "{",
	"lineComment": "#",
	"wordBreakChars": ",+-=<>/?^&*",
}

# Keywords dict for relax_ng_compact_main ruleset.
relax_ng_compact_main_keywords_dict = {
	"
": "keywords",
	"        ": "keywords",
	"            ": "keywords",
	"attribute": "keyword1",
	"datatypes": "keyword1",
	"default": "keyword1",
	"div": "keyword1",
	"element": "keyword1",
	"empty": "keyword1",
	"external": "keyword1",
	"grammar": "keyword1",
	"include": "keyword1",
	"inherit": "keyword1",
	"list": "keyword1",
	"mixed": "keyword1",
	"namespace": "keyword1",
	"notAllowed": "keyword1",
	"parent": "keyword1",
	"start": "keyword1",
	"string": "keyword2",
	"text": "keyword1",
	"token": "keyword2",
}

# Dictionary of keywords dictionaries for relax_ng_compact mode.
keywordsDictDict = {
	"relax_ng_compact_main": relax_ng_compact_main_keywords_dict,
}

# Rules for relax_ng_compact_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="\"\"\"", end="\"\"\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="'''", end="'''",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="?",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="null", pattern="\"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule15(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"\"": [rule1,rule3,],
	"#": [rule0,],
	"&": [rule8,rule9,],
	"'": [rule2,rule4,],
	"*": [rule6,],
	"+": [rule5,],
	"-": [rule13,],
	"0": [rule15,],
	"1": [rule15,],
	"2": [rule15,],
	"3": [rule15,],
	"4": [rule15,],
	"5": [rule15,],
	"6": [rule15,],
	"7": [rule15,],
	"8": [rule15,],
	"9": [rule15,],
	"=": [rule12,],
	"?": [rule7,],
	"@": [rule15,],
	"A": [rule15,],
	"B": [rule15,],
	"C": [rule15,],
	"D": [rule15,],
	"E": [rule15,],
	"F": [rule15,],
	"G": [rule15,],
	"H": [rule15,],
	"I": [rule15,],
	"J": [rule15,],
	"K": [rule15,],
	"L": [rule15,],
	"M": [rule15,],
	"N": [rule15,],
	"O": [rule15,],
	"P": [rule15,],
	"Q": [rule15,],
	"R": [rule15,],
	"S": [rule15,],
	"T": [rule15,],
	"U": [rule15,],
	"V": [rule15,],
	"W": [rule15,],
	"X": [rule15,],
	"Y": [rule15,],
	"Z": [rule15,],
	"\": [rule14,],
	"_": [rule15,],
	"a": [rule15,],
	"b": [rule15,],
	"c": [rule15,],
	"d": [rule15,],
	"e": [rule15,],
	"f": [rule15,],
	"g": [rule15,],
	"h": [rule15,],
	"i": [rule15,],
	"j": [rule15,],
	"k": [rule15,],
	"l": [rule15,],
	"m": [rule15,],
	"n": [rule15,],
	"o": [rule15,],
	"p": [rule15,],
	"q": [rule15,],
	"r": [rule15,],
	"s": [rule15,],
	"t": [rule15,],
	"u": [rule15,],
	"v": [rule15,],
	"w": [rule15,],
	"x": [rule15,],
	"y": [rule15,],
	"z": [rule15,],
	"|": [rule10,rule11,],
}

# x.rulesDictDict for relax_ng_compact mode.
rulesDictDict = {
	"relax_ng_compact_main": rulesDict1,
}

# Import dict for relax_ng_compact mode.
importDict = {}

