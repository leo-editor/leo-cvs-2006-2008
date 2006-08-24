# Leo colorizer control file for fortran mode.
# This file is in the public domain.

# Properties for fortran mode.
properties = {
	"blockComment": "C",
	"indentNextLine": "\\s*((if\\s*\\(.*\\)\\s*then|else\\s*|do\\s*)*)",
	"wordBreakChars": ",+-=<>/?^&*",
}

# Attributes dict for fortran_main ruleset.
fortran_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "false",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for fortran mode.
attributesDictDict = {
	"fortran_main": fortran_main_attributes_dict,
}

# Keywords dict for fortran_main ruleset.
fortran_main_keywords_dict = {
	".false.": "keyword1",
	".true.": "keyword1",
	"abs": "keyword1",
	"acos": "keyword1",
	"aimag": "keyword1",
	"aint": "keyword1",
	"allocatable": "keyword1",
	"allocate": "keyword1",
	"allocated": "keyword1",
	"alog": "keyword1",
	"alog10": "keyword1",
	"amax0": "keyword1",
	"amax1": "keyword1",
	"amin0": "keyword1",
	"amin1": "keyword1",
	"amod": "keyword1",
	"anint": "keyword1",
	"asin": "keyword1",
	"atan": "keyword1",
	"atan2": "keyword1",
	"backspace": "keyword1",
	"cabs": "keyword1",
	"call": "keyword1",
	"case": "keyword1",
	"ccos": "keyword1",
	"ceiling": "keyword1",
	"char": "keyword1",
	"character": "keyword1",
	"clog": "keyword1",
	"close": "keyword1",
	"cmplx": "keyword1",
	"complex": "keyword1",
	"conjg": "keyword1",
	"contains": "keyword1",
	"continue": "keyword1",
	"cos": "keyword1",
	"cosh": "keyword1",
	"csin": "keyword1",
	"csqrt": "keyword1",
	"cycle": "keyword1",
	"dabs": "keyword1",
	"dacos": "keyword1",
	"dasin": "keyword1",
	"data": "keyword1",
	"datan": "keyword1",
	"datan2": "keyword1",
	"dble": "keyword1",
	"dcmplx": "keyword1",
	"dcos": "keyword1",
	"dcosh": "keyword1",
	"ddim": "keyword1",
	"deallocate": "keyword1",
	"default": "keyword1",
	"dexp": "keyword1",
	"dfloat": "keyword1",
	"dim": "keyword1",
	"dimension": "keyword1",
	"dint": "keyword1",
	"dlog": "keyword1",
	"dlog10": "keyword1",
	"dmax1": "keyword1",
	"dmin1": "keyword1",
	"dmod": "keyword1",
	"dnint": "keyword1",
	"do": "keyword1",
	"double": "keyword1",
	"dprod": "keyword1",
	"dreal": "keyword1",
	"dsign": "keyword1",
	"dsin": "keyword1",
	"dsinh": "keyword1",
	"dsqrt": "keyword1",
	"dtan": "keyword1",
	"dtanh": "keyword1",
	"else": "keyword1",
	"elseif": "keyword1",
	"elsewhere": "keyword1",
	"end": "keyword1",
	"enddo": "keyword1",
	"endfile": "keyword1",
	"endif": "keyword1",
	"exit": "keyword1",
	"exp": "keyword1",
	"explicit": "keyword1",
	"float": "keyword1",
	"floor": "keyword1",
	"forall": "keyword1",
	"format": "keyword1",
	"function": "keyword1",
	"goto": "keyword1",
	"iabs": "keyword1",
	"ichar": "keyword1",
	"idim": "keyword1",
	"idint": "keyword1",
	"idnint": "keyword1",
	"if": "keyword1",
	"ifix": "keyword1",
	"imag": "keyword1",
	"implicit": "keyword1",
	"include": "keyword1",
	"index": "keyword1",
	"inquire": "keyword1",
	"int": "keyword1",
	"integer": "keyword1",
	"isign": "keyword1",
	"kind": "keyword1",
	"len": "keyword1",
	"lge": "keyword1",
	"lgt": "keyword1",
	"lle": "keyword1",
	"llt": "keyword1",
	"log": "keyword1",
	"log10": "keyword1",
	"logical": "keyword1",
	"max": "keyword1",
	"max0": "keyword1",
	"max1": "keyword1",
	"min": "keyword1",
	"min0": "keyword1",
	"min1": "keyword1",
	"mod": "keyword1",
	"module": "keyword1",
	"modulo": "keyword1",
	"nint": "keyword1",
	"none": "keyword1",
	"open": "keyword1",
	"parameter": "keyword1",
	"pause": "keyword1",
	"precision": "keyword1",
	"print": "keyword1",
	"program": "keyword1",
	"read": "keyword1",
	"real": "keyword1",
	"return": "keyword1",
	"rewind": "keyword1",
	"select": "keyword1",
	"sign": "keyword1",
	"sin": "keyword1",
	"sinh": "keyword1",
	"sngl": "keyword1",
	"sqrt": "keyword1",
	"stop": "keyword1",
	"subroutine": "keyword1",
	"tan": "keyword1",
	"tanh": "keyword1",
	"then": "keyword1",
	"transfer": "keyword1",
	"use": "keyword1",
	"where": "keyword1",
	"while": "keyword1",
	"write": "keyword1",
	"zext": "keyword1",
}

# Dictionary of keywords dictionaries for fortran mode.
keywordsDictDict = {
	"fortran_main": fortran_main_keywords_dict,
}

# Rules for fortran_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="C",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="!",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="*",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="D",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="==",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".lt.",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".gt.",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".eq.",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".ne.",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".le.",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".ge.",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".AND.",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".OR.",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule1,rule3,],
	"\"": [rule5,],
	"&": [rule11,],
	"'": [rule6,],
	"*": [rule2,],
	".": [rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,],
	"/": [rule12,],
	"0": [rule22,],
	"1": [rule22,],
	"2": [rule22,],
	"3": [rule22,],
	"4": [rule22,],
	"5": [rule22,],
	"6": [rule22,],
	"7": [rule22,],
	"8": [rule22,],
	"9": [rule22,],
	"<": [rule7,rule10,],
	"=": [rule13,],
	">": [rule8,rule9,],
	"@": [rule22,],
	"A": [rule22,],
	"B": [rule22,],
	"C": [rule0,rule22,],
	"D": [rule4,rule22,],
	"E": [rule22,],
	"F": [rule22,],
	"G": [rule22,],
	"H": [rule22,],
	"I": [rule22,],
	"J": [rule22,],
	"K": [rule22,],
	"L": [rule22,],
	"M": [rule22,],
	"N": [rule22,],
	"O": [rule22,],
	"P": [rule22,],
	"Q": [rule22,],
	"R": [rule22,],
	"S": [rule22,],
	"T": [rule22,],
	"U": [rule22,],
	"V": [rule22,],
	"W": [rule22,],
	"X": [rule22,],
	"Y": [rule22,],
	"Z": [rule22,],
	"a": [rule22,],
	"b": [rule22,],
	"c": [rule22,],
	"d": [rule22,],
	"e": [rule22,],
	"f": [rule22,],
	"g": [rule22,],
	"h": [rule22,],
	"i": [rule22,],
	"j": [rule22,],
	"k": [rule22,],
	"l": [rule22,],
	"m": [rule22,],
	"n": [rule22,],
	"o": [rule22,],
	"p": [rule22,],
	"q": [rule22,],
	"r": [rule22,],
	"s": [rule22,],
	"t": [rule22,],
	"u": [rule22,],
	"v": [rule22,],
	"w": [rule22,],
	"x": [rule22,],
	"y": [rule22,],
	"z": [rule22,],
}

# x.rulesDictDict for fortran mode.
rulesDictDict = {
	"fortran_main": rulesDict1,
}

# Import dict for fortran mode.
importDict = {}

