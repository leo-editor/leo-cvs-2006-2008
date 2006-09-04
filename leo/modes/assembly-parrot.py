# Leo colorizer control file for assembly-parrot mode.
# This file is in the public domain.

# Properties for assembly-parrot mode.
properties = {
	"lineComment": "#",
}

# Attributes dict for assembly_parrot_main ruleset.
assembly_parrot_main_attributes_dict = {
	"default": "null",
	"digit_re": "(0x[[:xdigit:]]+|[[:digit:]]+)",
	"escape": "",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for assembly_parrot mode.
attributesDictDict = {
	"assembly_parrot_main": assembly_parrot_main_attributes_dict,
}

# Keywords dict for assembly_parrot_main ruleset.
assembly_parrot_main_keywords_dict = {
	"abs": "keyword1",
	"acos": "keyword1",
	"add": "keyword1",
	"and": "keyword1",
	"asec": "keyword1",
	"asin": "keyword1",
	"atan": "keyword1",
	"bounds": "keyword1",
	"branch": "keyword1",
	"bsr": "keyword1",
	"chopm": "keyword1",
	"cleari": "keyword1",
	"clearn": "keyword1",
	"clearp": "keyword1",
	"clears": "keyword1",
	"clone": "keyword1",
	"close": "keyword1",
	"cmod": "keyword1",
	"concat": "keyword1",
	"cos": "keyword1",
	"cosh": "keyword1",
	"debug": "keyword1",
	"dec": "keyword1",
	"div": "keyword1",
	"end": "keyword1",
	"entrytype": "keyword1",
	"eq": "keyword1",
	"err": "keyword1",
	"exp": "keyword1",
	"find_global": "keyword1",
	"find_type": "keyword1",
	"ge": "keyword1",
	"getfile": "keyword1",
	"getline": "keyword1",
	"getpackage": "keyword1",
	"gt": "keyword1",
	"if": "keyword1",
	"inc": "keyword1",
	"index": "keyword1",
	"jsr": "keyword1",
	"jump": "keyword1",
	"le": "keyword1",
	"length": "keyword1",
	"ln": "keyword1",
	"log10": "keyword1",
	"log2": "keyword1",
	"lt": "keyword1",
	"mod": "keyword1",
	"mul": "keyword1",
	"ne": "keyword1",
	"new": "keyword1",
	"newinterp": "keyword1",
	"noop": "keyword1",
	"not": "keyword1",
	"open": "keyword1",
	"or": "keyword1",
	"ord": "keyword1",
	"pack": "keyword1",
	"pop": "keyword1",
	"popi": "keyword1",
	"popn": "keyword1",
	"popp": "keyword1",
	"pops": "keyword1",
	"pow": "keyword1",
	"print": "keyword1",
	"profile": "keyword1",
	"push": "keyword1",
	"pushi": "keyword1",
	"pushn": "keyword1",
	"pushp": "keyword1",
	"pushs": "keyword1",
	"read": "keyword1",
	"readline": "keyword1",
	"repeat": "keyword1",
	"restore": "keyword1",
	"ret": "keyword1",
	"rotate_up": "keyword1",
	"runinterp": "keyword1",
	"save": "keyword1",
	"sec": "keyword1",
	"sech": "keyword1",
	"set": "keyword1",
	"set_keyed": "keyword1",
	"setfile": "keyword1",
	"setline": "keyword1",
	"setpackage": "keyword1",
	"shl": "keyword1",
	"shr": "keyword1",
	"sin": "keyword1",
	"sinh": "keyword1",
	"sleep": "keyword1",
	"sub": "keyword1",
	"substr": "keyword1",
	"tan": "keyword1",
	"tanh": "keyword1",
	"time": "keyword1",
	"trace": "keyword1",
	"typeof": "keyword1",
	"unless": "keyword1",
	"warningsoff": "keyword1",
	"warningson": "keyword1",
	"write": "keyword1",
	"xor": "keyword1",
}

# Dictionary of keywords dictionaries for assembly_parrot mode.
keywordsDictDict = {
	"assembly_parrot_main": assembly_parrot_main_keywords_dict,
}

# Rules for assembly_parrot_main ruleset.

def assembly-parrot_rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def assembly-parrot_rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def assembly-parrot_rule2(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def assembly-parrot_rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly-parrot_rule4(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal2", regexp="I\\d{1,2}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly-parrot_rule5(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal2", regexp="S\\d{1,2}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly-parrot_rule6(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal2", regexp="N\\d{1,2}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly-parrot_rule7(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal2", regexp="P\\d{1,2}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly-parrot_rule8(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for assembly_parrot_main ruleset.
rulesDict1 = {
	"\"": [assembly-parrot_rule0,],
	"#": [assembly-parrot_rule1,],
	",": [assembly-parrot_rule3,],
	"0": [assembly-parrot_rule8,],
	"1": [assembly-parrot_rule8,],
	"2": [assembly-parrot_rule8,],
	"3": [assembly-parrot_rule8,],
	"4": [assembly-parrot_rule8,],
	"5": [assembly-parrot_rule8,],
	"6": [assembly-parrot_rule8,],
	"7": [assembly-parrot_rule8,],
	"8": [assembly-parrot_rule8,],
	"9": [assembly-parrot_rule8,],
	":": [assembly-parrot_rule2,],
	"@": [assembly-parrot_rule8,],
	"A": [assembly-parrot_rule8,],
	"B": [assembly-parrot_rule8,],
	"C": [assembly-parrot_rule8,],
	"D": [assembly-parrot_rule8,],
	"E": [assembly-parrot_rule8,],
	"F": [assembly-parrot_rule8,],
	"G": [assembly-parrot_rule8,],
	"H": [assembly-parrot_rule8,],
	"I": [assembly-parrot_rule4,assembly-parrot_rule8,],
	"J": [assembly-parrot_rule8,],
	"K": [assembly-parrot_rule8,],
	"L": [assembly-parrot_rule8,],
	"M": [assembly-parrot_rule8,],
	"N": [assembly-parrot_rule6,assembly-parrot_rule8,],
	"O": [assembly-parrot_rule8,],
	"P": [assembly-parrot_rule7,assembly-parrot_rule8,],
	"Q": [assembly-parrot_rule8,],
	"R": [assembly-parrot_rule8,],
	"S": [assembly-parrot_rule5,assembly-parrot_rule8,],
	"T": [assembly-parrot_rule8,],
	"U": [assembly-parrot_rule8,],
	"V": [assembly-parrot_rule8,],
	"W": [assembly-parrot_rule8,],
	"X": [assembly-parrot_rule8,],
	"Y": [assembly-parrot_rule8,],
	"Z": [assembly-parrot_rule8,],
	"_": [assembly-parrot_rule8,],
	"a": [assembly-parrot_rule8,],
	"b": [assembly-parrot_rule8,],
	"c": [assembly-parrot_rule8,],
	"d": [assembly-parrot_rule8,],
	"e": [assembly-parrot_rule8,],
	"f": [assembly-parrot_rule8,],
	"g": [assembly-parrot_rule8,],
	"h": [assembly-parrot_rule8,],
	"i": [assembly-parrot_rule8,],
	"j": [assembly-parrot_rule8,],
	"k": [assembly-parrot_rule8,],
	"l": [assembly-parrot_rule8,],
	"m": [assembly-parrot_rule8,],
	"n": [assembly-parrot_rule8,],
	"o": [assembly-parrot_rule8,],
	"p": [assembly-parrot_rule8,],
	"q": [assembly-parrot_rule8,],
	"r": [assembly-parrot_rule8,],
	"s": [assembly-parrot_rule8,],
	"t": [assembly-parrot_rule8,],
	"u": [assembly-parrot_rule8,],
	"v": [assembly-parrot_rule8,],
	"w": [assembly-parrot_rule8,],
	"x": [assembly-parrot_rule8,],
	"y": [assembly-parrot_rule8,],
	"z": [assembly-parrot_rule8,],
}

# x.rulesDictDict for assembly_parrot mode.
rulesDictDict = {
	"assembly_parrot_main": rulesDict1,
}

# Import dict for assembly_parrot mode.
importDict = {}

