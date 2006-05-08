# Leo colorizer control file for batch mode.

# Properties for batch mode.
properties = {
	"lineComment": "rem",
}

# Keywords dict for batch_main ruleset.
batch_main_keywords_dict = {
	"APPEND": "function",
	"ATTRIB": "function",
	"AUX": "keyword2",
	"CHKDSK": "function",
	"CHOICE": "function",
	"DEBUG": "function",
	"DEFRAG": "function",
	"DELTREE": "function",
	"DISKCOMP": "function",
	"DISKCOPY": "function",
	"DOSKEY": "function",
	"DRVSPACE": "function",
	"EMM386": "function",
	"EXPAND": "function",
	"FASTOPEN": "function",
	"FC": "function",
	"FDISK": "function",
	"FIND": "function",
	"FORMAT": "function",
	"GRAPHICS": "function",
	"KEYB": "function",
	"LABEL": "function",
	"LOADFIX": "function",
	"MEM": "function",
	"MODE": "function",
	"MORE": "function",
	"MOVE": "function",
	"MSCDEX": "function",
	"NLSFUNC": "function",
	"NUL": "keyword2",
	"POWER": "function",
	"PRINT": "function",
	"PRN": "keyword2",
	"RD": "function",
	"REPLACE": "function",
	"RESTORE": "function",
	"SETVER": "function",
	"SHARE": "function",
	"SORT": "function",
	"SUBST": "function",
	"SYS": "function",
	"TREE": "function",
	"UNDELETE": "function",
	"UNFORMAT": "function",
	"VSAFE": "function",
	"XCOPY": "function",
	"call": "keyword1",
	"cd": "keyword1",
	"chdir": "keyword1",
	"cls": "keyword1",
	"copy": "keyword1",
	"defined": "keyword2",
	"del": "keyword1",
	"do": "keyword2",
	"echo": "keyword1",
	"echo.": "keyword1",
	"else": "keyword2",
	"endlocal": "keyword1",
	"errorlevel": "keyword2",
	"exist": "keyword2",
	"exit": "keyword1",
	"for": "keyword1",
	"goto": "keyword3",
	"if": "keyword1",
	"in": "keyword2",
	"md": "keyword1",
	"mkdir": "keyword1",
	"move": "keyword1",
	"not": "keyword1",
	"pause": "keyword1",
	"ren": "keyword1",
	"set": "keyword1",
	"setlocal": "keyword1",
	"shift": "keyword1",
}

# Dictionary of keywords dictionaries for batch mode.
keywordsDictDict = {
	"batch_main": batch_main_keywords_dict,
}

# Rules for batch_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="label", pattern=":"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule8(colorer, s, i):
    return colorer.match_eol_span_regexp(s, i, kind="comment1", seq="REM\s",
        at_line_start=False, at_whitespace_end=True, at_word_start=False,
        delegate="", exclude_match=False)

def rule9(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="%0",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="%1",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="%2",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="%3",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="%4",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="%5",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="%6",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="%7",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="%8",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="%9",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="%%[[:alpha:]]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="%", end="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule22(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for batch_main ruleset.
batch_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
	rule20, rule21, rule22, ]

# Rules dict for batch mode.
rulesDict = {
	"batch_main": batch_main_rules,
}

# Import dict for batch mode.
importDict = {}

