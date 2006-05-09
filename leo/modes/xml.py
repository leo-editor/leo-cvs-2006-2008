# Leo colorizer control file for xml mode.
# This file is in the public domain.

# Properties for xml mode.
properties = {
	"commentEnd": "-->",
	"commentStart": "<!--",
}

# Keywords dict for xml_main ruleset.
xml_main_keywords_dict = {}

# Keywords dict for xml_tags ruleset.
xml_tags_keywords_dict = {}

# Keywords dict for xml_dtd_tags ruleset.
xml_dtd_tags_keywords_dict = {
	"#IMPLIED": "keyword1",
	"#PCDATA": "keyword1",
	"#REQUIRED": "keyword1",
	"CDATA": "keyword1",
	"EMPTY": "keyword1",
	"IGNORE": "keyword1",
	"INCLUDE": "keyword1",
	"NDATA": "keyword1",
}

# Keywords dict for xml_entity_tags ruleset.
xml_entity_tags_keywords_dict = {
	"SYSTEM": "keyword1",
}

# Keywords dict for xml_cdata ruleset.
xml_cdata_keywords_dict = {}

# Dictionary of keywords dictionaries for xml mode.
keywordsDictDict = {
	"xml_cdata": xml_cdata_keywords_dict,
	"xml_dtd_tags": xml_dtd_tags_keywords_dict,
	"xml_entity_tags": xml_entity_tags_keywords_dict,
	"xml_main": xml_main_keywords_dict,
	"xml_tags": xml_tags_keywords_dict,
}

# Rules for xml_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="<!ENTITY", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ENTITY-TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="<![CDATA[", end="]]>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="CDATA",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="<!", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="DTD-TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword3", begin="<?", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
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

# Rules for xml_tags ruleset.

def rule7(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule8(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule9(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

# Rules dict for tags ruleset.
rulesDict2 = {
	"\"": [rule8,],
	"'": [rule9,],
	"/": [rule10,],
	":": [rule11,rule12,],
	"<": [rule7,],
}

# Rules for xml_dtd_tags ruleset.

def rule13(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule14(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="--", end="--",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule15(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="%", end=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=True)

def rule16(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule17(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule18(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="[", end="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="?",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for dtd_tags ruleset.
rulesDict3 = {
	"\"": [rule16,],
	"%": [rule15,],
	"'": [rule17,],
	"(": [rule19,],
	")": [rule20,],
	"*": [rule23,],
	"+": [rule24,],
	",": [rule25,],
	"-": [rule14,],
	"0": [rule26,],
	"1": [rule26,],
	"2": [rule26,],
	"3": [rule26,],
	"4": [rule26,],
	"5": [rule26,],
	"6": [rule26,],
	"7": [rule26,],
	"8": [rule26,],
	"9": [rule26,],
	"<": [rule13,],
	"?": [rule22,],
	"@": [rule26,],
	"A": [rule26,],
	"B": [rule26,],
	"C": [rule26,],
	"D": [rule26,],
	"E": [rule26,],
	"F": [rule26,],
	"G": [rule26,],
	"H": [rule26,],
	"I": [rule26,],
	"J": [rule26,],
	"K": [rule26,],
	"L": [rule26,],
	"M": [rule26,],
	"N": [rule26,],
	"O": [rule26,],
	"P": [rule26,],
	"Q": [rule26,],
	"R": [rule26,],
	"S": [rule26,],
	"T": [rule26,],
	"U": [rule26,],
	"V": [rule26,],
	"W": [rule26,],
	"X": [rule26,],
	"Y": [rule26,],
	"Z": [rule26,],
	"[": [rule18,],
	"_": [rule26,],
	"a": [rule26,],
	"b": [rule26,],
	"c": [rule26,],
	"d": [rule26,],
	"e": [rule26,],
	"f": [rule26,],
	"g": [rule26,],
	"h": [rule26,],
	"i": [rule26,],
	"j": [rule26,],
	"k": [rule26,],
	"l": [rule26,],
	"m": [rule26,],
	"n": [rule26,],
	"o": [rule26,],
	"p": [rule26,],
	"q": [rule26,],
	"r": [rule26,],
	"s": [rule26,],
	"t": [rule26,],
	"u": [rule26,],
	"v": [rule26,],
	"w": [rule26,],
	"x": [rule26,],
	"y": [rule26,],
	"z": [rule26,],
	"|": [rule21,],
}

# Rules for xml_entity_tags ruleset.

def rule27(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule28(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="--", end="--",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule29(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule30(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule31(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule32(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule33(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for entity_tags ruleset.
rulesDict4 = {
	"\"": [rule29,],
	"%": [rule32,],
	"'": [rule30,],
	"-": [rule28,],
	"0": [rule33,],
	"1": [rule33,],
	"2": [rule33,],
	"3": [rule33,],
	"4": [rule33,],
	"5": [rule33,],
	"6": [rule33,],
	"7": [rule33,],
	"8": [rule33,],
	"9": [rule33,],
	"<": [rule27,],
	"=": [rule31,],
	"@": [rule33,],
	"A": [rule33,],
	"B": [rule33,],
	"C": [rule33,],
	"D": [rule33,],
	"E": [rule33,],
	"F": [rule33,],
	"G": [rule33,],
	"H": [rule33,],
	"I": [rule33,],
	"J": [rule33,],
	"K": [rule33,],
	"L": [rule33,],
	"M": [rule33,],
	"N": [rule33,],
	"O": [rule33,],
	"P": [rule33,],
	"Q": [rule33,],
	"R": [rule33,],
	"S": [rule33,],
	"T": [rule33,],
	"U": [rule33,],
	"V": [rule33,],
	"W": [rule33,],
	"X": [rule33,],
	"Y": [rule33,],
	"Z": [rule33,],
	"_": [rule33,],
	"a": [rule33,],
	"b": [rule33,],
	"c": [rule33,],
	"d": [rule33,],
	"e": [rule33,],
	"f": [rule33,],
	"g": [rule33,],
	"h": [rule33,],
	"i": [rule33,],
	"j": [rule33,],
	"k": [rule33,],
	"l": [rule33,],
	"m": [rule33,],
	"n": [rule33,],
	"o": [rule33,],
	"p": [rule33,],
	"q": [rule33,],
	"r": [rule33,],
	"s": [rule33,],
	"t": [rule33,],
	"u": [rule33,],
	"v": [rule33,],
	"w": [rule33,],
	"x": [rule33,],
	"y": [rule33,],
	"z": [rule33,],
}

# Rules for xml_cdata ruleset.

# Rules dict for cdata ruleset.
rulesDict5 = {}

# x.rulesDictDict for xml mode.
rulesDictDict = {
	"xml_cdata": rulesDict5,
	"xml_dtd_tags": rulesDict3,
	"xml_entity_tags": rulesDict4,
	"xml_main": rulesDict1,
	"xml_tags": rulesDict2,
}

# Import dict for xml mode.
importDict = {}

