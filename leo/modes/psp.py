# Leo colorizer control file for psp mode.

# Properties for psp mode.
properties = {
	"commentEnd": "-->",
	"commentStart": "<!--",
}

# Keywords dict for psp_main ruleset.
psp_main_keywords_dict = {}

# Keywords dict for psp_tags ruleset.
psp_tags_keywords_dict = {}

# Keywords dict for psp_directive ruleset.
psp_directive_keywords_dict = {
	"		": "keywords",
	"			": "keywords",
	"
": "keywords",
	"file": "keyword4",
	"include": "keyword4",
}

# Dictionary of keywords dictionaries for psp mode.
keywordsDictDict = {
	"psp_directive": psp_directive_keywords_dict,
	"psp_main": psp_main_keywords_dict,
	"psp_tags": psp_tags_keywords_dict,
}

# Rules for psp_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="literal4", begin="<%@", end="%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="DIRECTIVE",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment2", begin="<%--", end="--%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal3", begin="<%", end="%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="python::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"jscript\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="javascript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"javascript\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="javascript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script>", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="javascript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<!--#", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule7(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule8(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<STYLE>", end="</STYLE>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="css::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule9(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule10(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="&", end=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=True)

# Rules dict for main ruleset.
rulesDict1 = {
	"&": [rule10,],
	"<": [rule0,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,],
}

# Rules for psp_tags ruleset.

def rule11(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule12(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_span(s, i, kind="comment2", begin="<%--", end="--%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule15(colorer, s, i):
    return colorer.match_span(s, i, kind="literal3", begin="<%", end="%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="python::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules dict for tags ruleset.
rulesDict1 = {
	"\"": [rule11,],
	"'": [rule12,],
	"<": [rule14,rule15,],
	"=": [rule13,],
}

# Rules for psp_directive ruleset.

def rule16(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule17(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for directive ruleset.
rulesDict1 = {
	"\"": [rule16,],
	"'": [rule17,],
	"0": [rule19,],
	"1": [rule19,],
	"2": [rule19,],
	"3": [rule19,],
	"4": [rule19,],
	"5": [rule19,],
	"6": [rule19,],
	"7": [rule19,],
	"8": [rule19,],
	"9": [rule19,],
	"=": [rule18,],
	"@": [rule19,],
	"A": [rule19,],
	"B": [rule19,],
	"C": [rule19,],
	"D": [rule19,],
	"E": [rule19,],
	"F": [rule19,],
	"G": [rule19,],
	"H": [rule19,],
	"I": [rule19,],
	"J": [rule19,],
	"K": [rule19,],
	"L": [rule19,],
	"M": [rule19,],
	"N": [rule19,],
	"O": [rule19,],
	"P": [rule19,],
	"Q": [rule19,],
	"R": [rule19,],
	"S": [rule19,],
	"T": [rule19,],
	"U": [rule19,],
	"V": [rule19,],
	"W": [rule19,],
	"X": [rule19,],
	"Y": [rule19,],
	"Z": [rule19,],
	"_": [rule19,],
	"a": [rule19,],
	"b": [rule19,],
	"c": [rule19,],
	"d": [rule19,],
	"e": [rule19,],
	"f": [rule19,],
	"g": [rule19,],
	"h": [rule19,],
	"i": [rule19,],
	"j": [rule19,],
	"k": [rule19,],
	"l": [rule19,],
	"m": [rule19,],
	"n": [rule19,],
	"o": [rule19,],
	"p": [rule19,],
	"q": [rule19,],
	"r": [rule19,],
	"s": [rule19,],
	"t": [rule19,],
	"u": [rule19,],
	"v": [rule19,],
	"w": [rule19,],
	"x": [rule19,],
	"y": [rule19,],
	"z": [rule19,],
}

# x.rulesDictDict for psp mode.
rulesDictDict = {
	"psp_directive": rulesDict1,
	"psp_main": rulesDict1,
	"psp_tags": rulesDict1,
}

# Import dict for psp mode.
importDict = {}

