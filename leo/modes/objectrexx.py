# Leo colorizer control file for objectrexx mode.

# Properties for objectrexx mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"indentNextLines": "\s*(if|loop|do|else|select|otherwise|catch|finally|class|method|properties)(.*)",
	"lineComment": "--",
	"wordBreakChars": ",+-=<>/?^&*",
}

# Keywords dict for objectrexx_main ruleset.
objectrexx_main_keywords_dict = {
	"Abbrev": "keyword2",
	"Abs": "keyword2",
	"Address": "keyword2",
	"Arg": "keyword2",
	"B2X": "keyword2",
	"Beep": "keyword2",
	"BitAnd": "keyword2",
	"BitOr": "keyword2",
	"BitXor": "keyword2",
	"C2D": "keyword2",
	"C2X": "keyword2",
	"Call": "keyword1",
	"Center": "keyword2",
	"ChangeStr": "keyword2",
	"CharIn": "keyword2",
	"CharOut": "keyword2",
	"Chars": "keyword2",
	"Class": "keyword1",
	"Compare": "keyword2",
	"Consition": "keyword2",
	"Copies": "keyword2",
	"CountStr": "keyword2",
	"D2C": "keyword2",
	"D2X": "keyword2",
	"DataType": "keyword2",
	"Date": "keyword2",
	"DelStr": "keyword2",
	"DelWord": "keyword2",
	"Digits": "keyword2",
	"Directory": "keyword2",
	"Do": "keyword1",
	"Drop": "keyword1",
	"ErrorText": "keyword2",
	"Exit": "keyword1",
	"Expose": "keyword1",
	"FileSpec": "keyword2",
	"Form": "keyword2",
	"Format": "keyword2",
	"Forward": "keyword1",
	"Fuzz": "keyword2",
	"Guard": "keyword1",
	"If": "keyword1",
	"Insert": "keyword2",
	"Interpret": "keyword1",
	"Iterate": "keyword1",
	"LastPos": "keyword2",
	"Leave": "keyword1",
	"Left": "keyword2",
	"Length": "keyword2",
	"LineIn": "keyword2",
	"LineOut": "keyword2",
	"Lines": "keyword2",
	"Max": "keyword2",
	"Method": "keyword1",
	"Min": "keyword2",
	"Nop": "keyword1",
	"Numeric": "keyword1",
	"Overlay": "keyword2",
	"Parse": "keyword1",
	"Pos": "keyword2",
	"Procedure": "keyword1",
	"Push": "keyword1",
	"Queue": "keyword1",
	"Queued": "keyword2",
	"RC": "keyword1",
	"Raise": "keyword1",
	"Random": "keyword2",
	"Requires": "keyword1",
	"Result": "keyword1",
	"Return": "keyword1",
	"Reverse": "keyword2",
	"Right": "keyword2",
	"Routine": "keyword1",
	"RxFuncAdd": "keyword2",
	"RxFuncDrop": "keyword2",
	"RxFuncQuery": "keyword2",
	"RxMessageBox": "keyword2",
	"RxWinExec": "keyword2",
	"Say": "keyword1",
	"Seleect": "keyword1",
	"Self": "keyword1",
	"Sigl": "keyword1",
	"Sign": "keyword2",
	"Signal": "keyword1",
	"SourceLine": "keyword2",
	"Space": "keyword2",
	"Stream": "keyword2",
	"Strip": "keyword2",
	"SubStr": "keyword2",
	"SubWord": "keyword2",
	"Super": "keyword1",
	"Symbol": "keyword2",
	"SysAddRexxMacro": "keyword2",
	"SysBootDrive": "keyword2",
	"SysClearRexxMacroSpace": "keyword2",
	"SysCloseEventSem": "keyword2",
	"SysCloseMutexSem": "keyword2",
	"SysCls": "keyword2",
	"SysCreateEventSem": "keyword2",
	"SysCreateMutexSem": "keyword2",
	"SysCurPos": "keyword2",
	"SysCurState": "keyword2",
	"SysDriveInfo": "keyword2",
	"SysDriveMap": "keyword2",
	"SysDropFuncs": "keyword2",
	"SysDropRexxMacro": "keyword2",
	"SysDumpVariables": "keyword2",
	"SysFileDelete": "keyword2",
	"SysFileSearch": "keyword2",
	"SysFileSystemType": "keyword2",
	"SysFileTree": "keyword2",
	"SysFromUnicode": "keyword2",
	"SysGetErrortext": "keyword2",
	"SysGetFileDateTime": "keyword2",
	"SysGetKey": "keyword2",
	"SysIni": "keyword2",
	"SysLoadFuncs": "keyword2",
	"SysLoadRexxMacroSpace": "keyword2",
	"SysMkDir": "keyword2",
	"SysOpenEventSem": "keyword2",
	"SysOpenMutexSem": "keyword2",
	"SysPostEventSem": "keyword2",
	"SysPulseEventSem": "keyword2",
	"SysQueryProcess": "keyword2",
	"SysQueryRexxMacro": "keyword2",
	"SysReleaseMutexSem": "keyword2",
	"SysReorderRexxMacro": "keyword2",
	"SysRequestMutexSem": "keyword2",
	"SysResetEventSem": "keyword2",
	"SysRmDir": "keyword2",
	"SysSaveRexxMacroSpace": "keyword2",
	"SysSearchPath": "keyword2",
	"SysSetFileDateTime": "keyword2",
	"SysSetPriority": "keyword2",
	"SysSleep": "keyword2",
	"SysStemCopy": "keyword2",
	"SysStemDelete": "keyword2",
	"SysStemInsert": "keyword2",
	"SysStemSort": "keyword2",
	"SysSwitchSession": "keyword2",
	"SysSystemDirectory": "keyword2",
	"SysTempFileName": "keyword2",
	"SysTextScreenRead": "keyword2",
	"SysTextScreenSize": "keyword2",
	"SysToUnicode": "keyword2",
	"SysUtilVersion": "keyword2",
	"SysVersion": "keyword2",
	"SysVolumeLabel": "keyword2",
	"SysWaitEventSem": "keyword2",
	"SysWaitNamedPipe": "keyword2",
	"SysWinDecryptFile": "keyword2",
	"SysWinEncryptFile": "keyword2",
	"SysWinVer": "keyword2",
	"Time": "keyword2",
	"Trace": "keyword2",
	"Translate": "keyword2",
	"Trunc": "keyword2",
	"Value": "keyword2",
	"Var": "keyword2",
	"Verify": "keyword2",
	"Word": "keyword2",
	"WordIndex": "keyword2",
	"WordLength": "keyword2",
	"WordPos": "keyword2",
	"Words": "keyword2",
	"X2B": "keyword2",
	"X2C": "keyword2",
	"X2D": "keyword2",
	"XRange": "keyword2",
	"pull": "keyword1",
	"reply": "keyword1",
	"use": "keyword1",
}

# Dictionary of keywords dictionaries for objectrexx mode.
keywordsDictDict = {
	"objectrexx_main": objectrexx_main_keywords_dict,
}

# Rules for objectrexx_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

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
    return colorer.match_eol_span(s, i, kind="keyword2", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="--",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="::",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule23(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=False, at_whitespace_end=True, at_word_start=False, exclude_match=True)

def rule24(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule25(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule6,],
	"\"": [rule1,],
	"#": [rule3,],
	"%": [rule15,],
	"&": [rule16,],
	"'": [rule2,],
	"(": [rule24,],
	"*": [rule12,],
	"+": [rule9,],
	"-": [rule4,rule10,],
	"/": [rule0,rule11,],
	"0": [rule25,],
	"1": [rule25,],
	"2": [rule25,],
	"3": [rule25,],
	"4": [rule25,],
	"5": [rule25,],
	"6": [rule25,],
	"7": [rule25,],
	"8": [rule25,],
	"9": [rule25,],
	":": [rule22,rule23,],
	"<": [rule8,rule14,],
	"=": [rule5,],
	">": [rule7,rule13,],
	"@": [rule25,],
	"A": [rule25,],
	"B": [rule25,],
	"C": [rule25,],
	"D": [rule25,],
	"E": [rule25,],
	"F": [rule25,],
	"G": [rule25,],
	"H": [rule25,],
	"I": [rule25,],
	"J": [rule25,],
	"K": [rule25,],
	"L": [rule25,],
	"M": [rule25,],
	"N": [rule25,],
	"O": [rule25,],
	"P": [rule25,],
	"Q": [rule25,],
	"R": [rule25,],
	"S": [rule25,],
	"T": [rule25,],
	"U": [rule25,],
	"V": [rule25,],
	"W": [rule25,],
	"X": [rule25,],
	"Y": [rule25,],
	"Z": [rule25,],
	"^": [rule18,],
	"_": [rule25,],
	"a": [rule25,],
	"b": [rule25,],
	"c": [rule25,],
	"d": [rule25,],
	"e": [rule25,],
	"f": [rule25,],
	"g": [rule25,],
	"h": [rule25,],
	"i": [rule25,],
	"j": [rule25,],
	"k": [rule25,],
	"l": [rule25,],
	"m": [rule25,],
	"n": [rule25,],
	"o": [rule25,],
	"p": [rule25,],
	"q": [rule25,],
	"r": [rule25,],
	"s": [rule25,],
	"t": [rule25,],
	"u": [rule25,],
	"v": [rule25,],
	"w": [rule25,],
	"x": [rule25,],
	"y": [rule25,],
	"z": [rule25,],
	"{": [rule21,],
	"|": [rule17,],
	"}": [rule20,],
	"~": [rule19,],
}

# x.rulesDictDict for objectrexx mode.
rulesDictDict = {
	"objectrexx_main": rulesDict1,
}

# Import dict for objectrexx mode.
importDict = {}

