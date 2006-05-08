# Leo colorizer control file for shtml mode.

# Properties for shtml mode.
properties = {
	"commentEnd": "-->",
	"commentStart": "<!--",
}

# Keywords dict for shtml_main ruleset.
shtml_main_keywords_dict = {}

# Keywords dict for shtml_tags ruleset.
shtml_tags_keywords_dict = {}

# Keywords dict for shtml_ssi ruleset.
shtml_ssi_keywords_dict = {
	"cgi": "keyword2",
	"cmd": "keyword2",
	"config": "keyword1",
	"echo": "keyword1",
	"errmsg": "keyword2",
	"exec": "keyword1",
	"file": "keyword2",
	"flastmod": "keyword1",
	"fsize": "keyword1",
	"include": "keyword1",
	"sizefmt": "keyword2",
	"timefmt": "keyword2",
	"var": "keyword2",
}

# Keywords dict for shtml_ssi_expression ruleset.
shtml_ssi_expression_keywords_dict = {}

# Dictionary of keywords dictionaries for shtml mode.
keywordsDictDict = {
	"shtml_main": shtml_main_keywords_dict,
	"shtml_ssi": shtml_ssi_keywords_dict,
	"shtml_ssi_expression": shtml_ssi_expression_keywords_dict,
	"shtml_tags": shtml_tags_keywords_dict,
}

# Rules for shtml_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword3", begin="<!--#", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="SSI",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<SCRIPT", end="</SCRIPT>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="html::JAVASCRIPT",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<STYLE", end="</STYLE>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="html::CSS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="<!", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="xml::DTD-TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="&", end=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=True)

# Rules dict for main ruleset.
rulesDict1 = {
	"&": [rule6,],
	"<": [rule0,rule1,rule2,rule3,rule4,rule5,],
}

# Rules for shtml_tags ruleset.

def rule7(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule8(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

# Rules dict for tags ruleset.
rulesDict1 = {
	"\"": [rule7,],
	"'": [rule8,],
	"=": [rule9,],
}

# Rules for shtml_ssi ruleset.

def rule10(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="SSI-EXPRESSION",exclude_match=True,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for ssi ruleset.
rulesDict1 = {
	"\"": [rule10,],
	"0": [rule12,],
	"1": [rule12,],
	"2": [rule12,],
	"3": [rule12,],
	"4": [rule12,],
	"5": [rule12,],
	"6": [rule12,],
	"7": [rule12,],
	"8": [rule12,],
	"9": [rule12,],
	"=": [rule11,],
	"@": [rule12,],
	"A": [rule12,],
	"B": [rule12,],
	"C": [rule12,],
	"D": [rule12,],
	"E": [rule12,],
	"F": [rule12,],
	"G": [rule12,],
	"H": [rule12,],
	"I": [rule12,],
	"J": [rule12,],
	"K": [rule12,],
	"L": [rule12,],
	"M": [rule12,],
	"N": [rule12,],
	"O": [rule12,],
	"P": [rule12,],
	"Q": [rule12,],
	"R": [rule12,],
	"S": [rule12,],
	"T": [rule12,],
	"U": [rule12,],
	"V": [rule12,],
	"W": [rule12,],
	"X": [rule12,],
	"Y": [rule12,],
	"Z": [rule12,],
	"_": [rule12,],
	"a": [rule12,],
	"b": [rule12,],
	"c": [rule12,],
	"d": [rule12,],
	"e": [rule12,],
	"f": [rule12,],
	"g": [rule12,],
	"h": [rule12,],
	"i": [rule12,],
	"j": [rule12,],
	"k": [rule12,],
	"l": [rule12,],
	"m": [rule12,],
	"n": [rule12,],
	"o": [rule12,],
	"p": [rule12,],
	"q": [rule12,],
	"r": [rule12,],
	"s": [rule12,],
	"t": [rule12,],
	"u": [rule12,],
	"v": [rule12,],
	"w": [rule12,],
	"x": [rule12,],
	"y": [rule12,],
	"z": [rule12,],
}

# Rules for shtml_ssi_expression ruleset.

def rule13(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="||",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

# Rules dict for ssi_expression ruleset.
rulesDict1 = {
	"!": [rule15,],
	"$": [rule13,],
	"&": [rule20,],
	"<": [rule16,rule17,],
	"=": [rule14,],
	">": [rule18,rule19,],
	"|": [rule21,],
}

# x.rulesDictDict for shtml mode.
rulesDictDict = {
	"shtml_main": rulesDict1,
	"shtml_ssi": rulesDict1,
	"shtml_ssi_expression": rulesDict1,
	"shtml_tags": rulesDict1,
}

# Import dict for shtml mode.
importDict = {}

