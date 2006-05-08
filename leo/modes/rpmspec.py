# Leo colorizer control file for rpmspec mode.

# Properties for rpmspec mode.
properties = {
	"lineComment": "#",
}

# Keywords dict for rpmspec_main ruleset.
rpmspec_main_keywords_dict = {
	"%build": "label",
	"%clean": "label",
	"%config": "markup",
	"%description": "label",
	"%dir": "markup",
	"%doc": "markup",
	"%docdir": "markup",
	"%else": "function",
	"%endif": "function",
	"%files": "label",
	"%ifarch": "function",
	"%ifnarch": "function",
	"%ifnos": "function",
	"%ifos": "function",
	"%install": "label",
	"%package": "markup",
	"%post": "label",
	"%postun": "label",
	"%pre": "label",
	"%prep": "label",
	"%preun": "label",
	"%setup": "function",
	"%verifyscript": "label",
	"AutoReqProv:": "keyword1",
	"BuildArch:": "keyword1",
	"BuildRoot:": "keyword1",
	"Conflicts:": "keyword1",
	"Copyright:": "keyword1",
	"Distribution:": "keyword1",
	"ExcludeArch:": "keyword1",
	"ExclusiveArch:": "keyword1",
	"ExclusiveOS:": "keyword1",
	"Group:": "keyword1",
	"Icon:": "keyword1",
	"Name:": "keyword1",
	"NoPatch:": "keyword1",
	"NoSource:": "keyword1",
	"Packager:": "keyword1",
	"Prefix:": "keyword1",
	"Provides:": "keyword1",
	"Release:": "keyword1",
	"Requires:": "keyword1",
	"Serial:": "keyword1",
	"Summary:": "keyword1",
	"URL:": "keyword1",
	"Vendor:": "keyword1",
	"Version:": "keyword1",
}

# Keywords dict for rpmspec_attr ruleset.
rpmspec_attr_keywords_dict = {}

# Keywords dict for rpmspec_verify ruleset.
rpmspec_verify_keywords_dict = {
	"group": "keyword2",
	"maj": "keyword2",
	"md5": "keyword2",
	"min": "keyword2",
	"mode": "keyword2",
	"mtime": "keyword2",
	"not": "operator",
	"owner": "keyword2",
	"size": "keyword2",
	"symlink": "keyword2",
}

# Dictionary of keywords dictionaries for rpmspec mode.
keywordsDictDict = {
	"rpmspec_attr": rpmspec_attr_keywords_dict,
	"rpmspec_main": rpmspec_main_keywords_dict,
	"rpmspec_verify": rpmspec_verify_keywords_dict,
}

# Rules for rpmspec_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="%attr(", end=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ATTR",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="%verify(", end=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="VERIFY",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword1", pattern="Source"
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule7(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword1", pattern="Patch"
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule8(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="function", pattern="%patch"
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule9(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="${", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule10(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword3", begin="%{", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule11(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$#"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule12(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$?"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule13(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$*"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule14(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$<"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule15(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule16(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"#": [rule0,],
	"$": [rule9,rule11,rule12,rule13,rule14,rule15,],
	"%": [rule4,rule5,rule8,rule10,],
	"0": [rule16,],
	"1": [rule16,],
	"2": [rule16,],
	"3": [rule16,],
	"4": [rule16,],
	"5": [rule16,],
	"6": [rule16,],
	"7": [rule16,],
	"8": [rule16,],
	"9": [rule16,],
	"<": [rule1,],
	"=": [rule3,],
	">": [rule2,],
	"@": [rule16,],
	"A": [rule16,],
	"B": [rule16,],
	"C": [rule16,],
	"D": [rule16,],
	"E": [rule16,],
	"F": [rule16,],
	"G": [rule16,],
	"H": [rule16,],
	"I": [rule16,],
	"J": [rule16,],
	"K": [rule16,],
	"L": [rule16,],
	"M": [rule16,],
	"N": [rule16,],
	"O": [rule16,],
	"P": [rule7,rule16,],
	"Q": [rule16,],
	"R": [rule16,],
	"S": [rule6,rule16,],
	"T": [rule16,],
	"U": [rule16,],
	"V": [rule16,],
	"W": [rule16,],
	"X": [rule16,],
	"Y": [rule16,],
	"Z": [rule16,],
	"_": [rule16,],
	"a": [rule16,],
	"b": [rule16,],
	"c": [rule16,],
	"d": [rule16,],
	"e": [rule16,],
	"f": [rule16,],
	"g": [rule16,],
	"h": [rule16,],
	"i": [rule16,],
	"j": [rule16,],
	"k": [rule16,],
	"l": [rule16,],
	"m": [rule16,],
	"n": [rule16,],
	"o": [rule16,],
	"p": [rule16,],
	"q": [rule16,],
	"r": [rule16,],
	"s": [rule16,],
	"t": [rule16,],
	"u": [rule16,],
	"v": [rule16,],
	"w": [rule16,],
	"x": [rule16,],
	"y": [rule16,],
	"z": [rule16,],
}

# Rules for rpmspec_attr ruleset.

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

# Rules dict for attr ruleset.
rulesDict1 = {
	",": [rule17,],
	"-": [rule18,],
}

# Rules for rpmspec_verify ruleset.

def rule19(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for verify ruleset.
rulesDict1 = {
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

# x.rulesDictDict for rpmspec mode.
rulesDictDict = {
	"rpmspec_attr": rulesDict1,
	"rpmspec_main": rulesDict1,
	"rpmspec_verify": rulesDict1,
}

# Import dict for rpmspec mode.
importDict = {}

