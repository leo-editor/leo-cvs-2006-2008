# Leo colorizer control file for assembly-mcs51 mode.

# Properties for assembly-mcs51 mode.
properties = {
	"lineComment": ";",
}

# Keywords dict for assembly_mcs51_main ruleset.
assembly_mcs51_main_keywords_dict = {
	"$CASE": "keyword2",
	"$ELSE": "keyword2",
	"$ELSEIF": "keyword2",
	"$ENDIF": "keyword2",
	"$IF": "keyword2",
	"$INCLUDE": "keyword2",
	"$MOD167": "keyword2",
	"$SEGMENTED": "keyword2",
	"A": "keyword3",
	"AB": "keyword3",
	"ACALL": "keyword1",
	"ADD": "keyword1",
	"ADDC": "keyword1",
	"ADDM": "keyword1",
	"AJMP": "keyword1",
	"AND": "keyword1",
	"ANL": "keyword1",
	"AT": "keyword1",
	"BIT": "keyword2",
	"BITADDRESSABLE": "keyword1",
	"BSEG": "keyword1",
	"C": "keyword3",
	"CALL": "keyword1",
	"CJNE": "keyword1",
	"CLR": "keyword1",
	"CODE": "keyword2",
	"CPL": "keyword1",
	"CSEG": "keyword1",
	"DA": "keyword1",
	"DATA": "keyword2",
	"DB": "keyword1",
	"DBIT": "keyword1",
	"DEC": "keyword1",
	"DEFINE": "keyword1",
	"DIV": "keyword1",
	"DJNZ": "keyword1",
	"DPTN": "keyword1",
	"DPTR": "keyword1",
	"DPTR16": "keyword1",
	"DPTR8": "keyword1",
	"DPTX": "keyword1",
	"DR0": "keyword1",
	"DR4": "keyword1",
	"DS": "keyword1",
	"DSEG": "keyword1",
	"DW": "keyword1",
	"DWR": "keyword1",
	"ELSE": "keyword1",
	"ELSEIF": "keyword1",
	"END": "keyword1",
	"ENDIF": "keyword1",
	"ENDM": "keyword1",
	"EQ": "keyword1",
	"EQS": "keyword1",
	"EQU": "keyword1",
	"EXITM": "keyword1",
	"EXTRN": "keyword1",
	"FI": "keyword1",
	"GE": "keyword1",
	"GT": "keyword1",
	"HIGH": "keyword1",
	"IDATA": "keyword2",
	"IF": "keyword1",
	"INBLOCK": "keyword1",
	"INC": "keyword1",
	"INPAGE": "keyword1",
	"IRP": "keyword1",
	"IRPC": "keyword1",
	"ISEG": "keyword1",
	"JB": "keyword1",
	"JBC": "keyword1",
	"JC": "keyword1",
	"JMP": "keyword1",
	"JMPI": "keyword1",
	"JNB": "keyword1",
	"JNC": "keyword1",
	"JNZ": "keyword1",
	"JZ": "keyword1",
	"LCALL": "keyword1",
	"LE": "keyword1",
	"LEN": "keyword1",
	"LJMP": "keyword1",
	"LOCAL": "keyword1",
	"LOW": "keyword1",
	"LT": "keyword1",
	"MACRO": "keyword1",
	"MOD": "keyword1",
	"MOV": "keyword1",
	"MOVB": "keyword1",
	"MOVC": "keyword1",
	"MOVX": "keyword1",
	"MUL": "keyword1",
	"NAME": "keyword1",
	"NE": "keyword1",
	"NOP": "keyword1",
	"NOT": "keyword1",
	"NUL": "keyword1",
	"NUMBER": "keyword1",
	"OR": "keyword1",
	"ORG": "keyword1",
	"ORL": "keyword1",
	"OVERLAYABLE": "keyword1",
	"PAGE": "keyword1",
	"PC": "keyword1",
	"POP": "keyword1",
	"POPA": "keyword1",
	"PUBLIC": "keyword1",
	"PUSH": "keyword1",
	"PUSHA": "keyword1",
	"R0": "keyword3",
	"R1": "keyword3",
	"R2": "keyword3",
	"R3": "keyword3",
	"R4": "keyword3",
	"R5": "keyword3",
	"R6": "keyword3",
	"R7": "keyword3",
	"REPT": "keyword1",
	"RET": "keyword1",
	"RETI": "keyword1",
	"RJC": "keyword1",
	"RJNC": "keyword1",
	"RJNZ": "keyword1",
	"RJZ": "keyword1",
	"RL": "keyword1",
	"RLC": "keyword1",
	"RR": "keyword1",
	"RRC": "keyword1",
	"RSEG": "keyword1",
	"SBIT": "keyword1",
	"SEGMENT": "keyword1",
	"SET": "keyword1",
	"SETB": "keyword1",
	"SFR": "keyword1",
	"SFR16": "keyword1",
	"SHL": "keyword1",
	"SHR": "keyword1",
	"SJMP": "keyword1",
	"SLEEP": "keyword1",
	"SP": "keyword3",
	"STACKLEN": "keyword1",
	"SUB": "keyword1",
	"SUBB": "keyword1",
	"SUBM": "keyword1",
	"SUBSTR": "keyword1",
	"SWAP": "keyword1",
	"SYNC": "keyword1",
	"THEN": "keyword1",
	"UNIT": "keyword1",
	"USING": "keyword1",
	"WR0": "keyword1",
	"WR2": "keyword1",
	"WR4": "keyword1",
	"WR6": "keyword1",
	"XCH": "keyword1",
	"XCHD": "keyword1",
	"XDATA": "keyword2",
	"XOR": "keyword1",
	"XRL": "keyword1",
	"XSEG": "keyword1",
	"__ERROR__": "keyword1",
}

# Dictionary of keywords dictionaries for assembly_mcs51 mode.
keywordsDictDict = {
	"assembly_mcs51_main": assembly_mcs51_main_keywords_dict,
}

# Rules for assembly_mcs51_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="label", pattern="%%",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule4(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule5(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq="[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq="$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule22,],
	"\"": [rule2,],
	"$": [rule4,rule12,],
	"%": [rule3,rule17,],
	"&": [rule20,],
	"'": [rule1,],
	"(": [rule8,],
	")": [rule9,],
	"*": [rule16,],
	"+": [rule13,],
	",": [rule6,],
	"-": [rule14,],
	"/": [rule15,],
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
	":": [rule5,rule7,],
	";": [rule0,],
	"<": [rule24,],
	"=": [rule23,],
	">": [rule25,],
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
	"[": [rule11,],
	"]": [rule10,],
	"^": [rule19,],
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
	"|": [rule18,],
	"~": [rule21,],
}

# x.rulesDictDict for assembly_mcs51 mode.
rulesDictDict = {
	"assembly_mcs51_main": rulesDict1,
}

# Import dict for assembly_mcs51 mode.
importDict = {}

