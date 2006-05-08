# Leo colorizer control file for fortran mode.

# Properties for fortran mode.
properties = {
	"blockComment": "C",
	"indentNextLine": "\s*((if\s*\(.*\)\s*then|else\s*|do\s*)*)",
	"wordBreakChars": ",+-=<>/?^&*",
}

# Keywords dict for fortran_main ruleset.
fortran_main_keywords_dict = {
	".false.": "keyword1",
	".true.": "keyword1",
	"ABS": "keyword1",
	"ACOS": "keyword1",
	"AIMAG": "keyword1",
	"AINT": "keyword1",
	"ALLOCATABLE": "keyword1",
	"ALLOCATE": "keyword1",
	"ALLOCATED": "keyword1",
	"ALOG": "keyword1",
	"ALOG10": "keyword1",
	"AMAX0": "keyword1",
	"AMAX1": "keyword1",
	"AMIN0": "keyword1",
	"AMIN1": "keyword1",
	"AMOD": "keyword1",
	"ANINT": "keyword1",
	"ASIN": "keyword1",
	"ATAN": "keyword1",
	"ATAN2": "keyword1",
	"BACKSPACE": "keyword1",
	"CABS": "keyword1",
	"CALL": "keyword1",
	"CASE": "keyword1",
	"CCOS": "keyword1",
	"CEILING": "keyword1",
	"CHAR": "keyword1",
	"CHARACTER": "keyword1",
	"CLOG": "keyword1",
	"CLOSE": "keyword1",
	"CMPLX": "keyword1",
	"COMPLEX": "keyword1",
	"CONJG": "keyword1",
	"CONTAINS": "keyword1",
	"CONTINUE": "keyword1",
	"COS": "keyword1",
	"COSH": "keyword1",
	"CSIN": "keyword1",
	"CSQRT": "keyword1",
	"CYCLE": "keyword1",
	"DABS": "keyword1",
	"DACOS": "keyword1",
	"DASIN": "keyword1",
	"DATA": "keyword1",
	"DATAN": "keyword1",
	"DATAN2": "keyword1",
	"DBLE": "keyword1",
	"DCMPLX": "keyword1",
	"DCOS": "keyword1",
	"DCOSH": "keyword1",
	"DDIM": "keyword1",
	"DEALLOCATE": "keyword1",
	"DEFAULT": "keyword1",
	"DEXP": "keyword1",
	"DFLOAT": "keyword1",
	"DIM": "keyword1",
	"DIMENSION": "keyword1",
	"DINT": "keyword1",
	"DLOG": "keyword1",
	"DLOG10": "keyword1",
	"DMAX1": "keyword1",
	"DMIN1": "keyword1",
	"DMOD": "keyword1",
	"DNINT": "keyword1",
	"DO": "keyword1",
	"DOUBLE": "keyword1",
	"DPROD": "keyword1",
	"DREAL": "keyword1",
	"DSIGN": "keyword1",
	"DSIN": "keyword1",
	"DSINH": "keyword1",
	"DSQRT": "keyword1",
	"DTAN": "keyword1",
	"DTANH": "keyword1",
	"ELSE": "keyword1",
	"ELSEIF": "keyword1",
	"ELSEWHERE": "keyword1",
	"END": "keyword1",
	"ENDDO": "keyword1",
	"ENDFILE": "keyword1",
	"ENDIF": "keyword1",
	"EXIT": "keyword1",
	"EXP": "keyword1",
	"EXPLICIT": "keyword1",
	"FLOAT": "keyword1",
	"FLOOR": "keyword1",
	"FORALL": "keyword1",
	"FORMAT": "keyword1",
	"FUNCTION": "keyword1",
	"GOTO": "keyword1",
	"IABS": "keyword1",
	"ICHAR": "keyword1",
	"IDIM": "keyword1",
	"IDINT": "keyword1",
	"IDNINT": "keyword1",
	"IF": "keyword1",
	"IFIX": "keyword1",
	"IMAG": "keyword1",
	"IMPLICIT": "keyword1",
	"INCLUDE": "keyword1",
	"INDEX": "keyword1",
	"INQUIRE": "keyword1",
	"INT": "keyword1",
	"INTEGER": "keyword1",
	"ISIGN": "keyword1",
	"KIND": "keyword1",
	"LEN": "keyword1",
	"LGE": "keyword1",
	"LGT": "keyword1",
	"LLE": "keyword1",
	"LLT": "keyword1",
	"LOG": "keyword1",
	"LOG10": "keyword1",
	"LOGICAL": "keyword1",
	"MAX": "keyword1",
	"MAX0": "keyword1",
	"MAX1": "keyword1",
	"MIN": "keyword1",
	"MIN0": "keyword1",
	"MIN1": "keyword1",
	"MOD": "keyword1",
	"MODULE": "keyword1",
	"MODULO": "keyword1",
	"NINT": "keyword1",
	"NONE": "keyword1",
	"OPEN": "keyword1",
	"PARAMETER": "keyword1",
	"PAUSE": "keyword1",
	"PRECISION": "keyword1",
	"PRINT": "keyword1",
	"PROGRAM": "keyword1",
	"READ": "keyword1",
	"REAL": "keyword1",
	"RETURN": "keyword1",
	"REWIND": "keyword1",
	"SELECT": "keyword1",
	"SIGN": "keyword1",
	"SIN": "keyword1",
	"SINH": "keyword1",
	"SNGL": "keyword1",
	"SQRT": "keyword1",
	"STOP": "keyword1",
	"SUBROUTINE": "keyword1",
	"TAN": "keyword1",
	"TANH": "keyword1",
	"THEN": "keyword1",
	"TRANSFER": "keyword1",
	"USE": "keyword1",
	"WHERE": "keyword1",
	"WHILE": "keyword1",
	"WRITE": "keyword1",
	"ZEXT": "keyword1",
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

# Rules list for fortran_main ruleset.
fortran_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
	rule20, rule21, rule22, ]

# Rules dict for fortran mode.
rulesDict = {
	"fortran_main": fortran_main_rules,
}

# Import dict for fortran mode.
importDict = {}

