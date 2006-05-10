# Leo colorizer control file for javascript mode.
# This file is in the public domain.

# Properties for javascript mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"doubleBracketIndent": "false",
	"indentCloseBrackets": "}",
	"indentNextLine": "\\s*(((if|while)\\s*\\(|else\\s*|else\\s+if\\s*\\(|for\\s*\\(.*\\))[^{;]*)",
	"indentOpenBrackets": "{",
	"lineComment": "//",
	"lineUpClosingBracket": "true",
	"wordBreakChars": ",+-=<>/?^&*",
}

# Attributes dict for javascript_main ruleset.
javascript_main_attributes_dict = {
	"default": "null",
	"digit_re": "(0x[[:xdigit:]]+[lL]?|[[:digit:]]+(e[[:digit:]]*)?[lLdDfF]?)",
	"highlight_digits": "true",
	"ignore_case": "false",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for javascript mode.
attributesDictDict = {
	"javascript_main": javascript_main_attributes_dict,
}

# Keywords dict for javascript_main ruleset.
javascript_main_keywords_dict = {
	"Array": "keyword3",
	"Boolean": "keyword3",
	"Date": "keyword3",
	"Function": "keyword3",
	"Global": "keyword3",
	"Infinity": "literal2",
	"Math": "keyword3",
	"NaN": "literal2",
	"Number": "keyword3",
	"Object": "keyword3",
	"RegExp": "keyword3",
	"String": "keyword3",
	"abstract": "keyword1",
	"adAsyncExecute": "literal2",
	"adAsyncFetch": "literal2",
	"adAsyncFetchNonBlocking": "literal2",
	"adBSTR": "literal2",
	"adBigInt": "literal2",
	"adBinary": "literal2",
	"adBoolean": "literal2",
	"adChapter": "literal2",
	"adChar": "literal2",
	"adCmdFile": "literal2",
	"adCmdStoredProc": "literal2",
	"adCmdTable": "literal2",
	"adCmdTableDirect": "literal2",
	"adCmdText": "literal2",
	"adCmdUnknown": "literal2",
	"adCurrency": "literal2",
	"adDBDate": "literal2",
	"adDBFileTime": "literal2",
	"adDBTime": "literal2",
	"adDBTimeStamp": "literal2",
	"adDate": "literal2",
	"adDecimal": "literal2",
	"adDouble": "literal2",
	"adEmpty": "literal2",
	"adError": "literal2",
	"adExecuteNoRecords": "literal2",
	"adFileTime": "literal2",
	"adGUID": "literal2",
	"adIDispatch": "literal2",
	"adIUnknown": "literal2",
	"adInteger": "literal2",
	"adLockBatchOptimistic": "literal2",
	"adLockOptimistic": "literal2",
	"adLockPessimistic": "literal2",
	"adLockReadOnly": "literal2",
	"adLongVarBinary": "literal2",
	"adLongVarChar": "literal2",
	"adLongVarWChar": "literal2",
	"adNumeric": "literal2",
	"adOpenDynamic": "literal2",
	"adOpenForwardOnly": "literal2",
	"adOpenKeyset": "literal2",
	"adOpenStatic": "literal2",
	"adParamInput": "literal2",
	"adParamInputOutput": "literal2",
	"adParamLong": "literal2",
	"adParamNullable": "literal2",
	"adParamOutput": "literal2",
	"adParamReturnValue": "literal2",
	"adParamSigned": "literal2",
	"adParamUnknown": "literal2",
	"adPersistADTG": "literal2",
	"adPersistXML": "literal2",
	"adPropVariant": "literal2",
	"adRunAsync": "literal2",
	"adSingle": "literal2",
	"adSmallInt": "literal2",
	"adStateClosed": "literal2",
	"adStateConnecting": "literal2",
	"adStateExecuting": "literal2",
	"adStateFetching": "literal2",
	"adStateOpen": "literal2",
	"adTinyInt": "literal2",
	"adUnsignedBigInt": "literal2",
	"adUnsignedInt": "literal2",
	"adUnsignedSmallInt": "literal2",
	"adUnsignedTinyInt": "literal2",
	"adUseClient": "literal2",
	"adUseServer": "literal2",
	"adUserDefined": "literal2",
	"adVarBinary": "literal2",
	"adVarChar": "literal2",
	"adVarNumeric": "literal2",
	"adVarWChar": "literal2",
	"adVariant": "literal2",
	"adWChar": "literal2",
	"boolean": "keyword3",
	"break": "keyword1",
	"byte": "keyword3",
	"case": "keyword1",
	"catch": "keyword1",
	"char": "keyword3",
	"class": "keyword1",
	"const": "keyword1",
	"continue": "keyword1",
	"debugger": "keyword1",
	"default": "keyword1",
	"delete": "keyword1",
	"do": "keyword1",
	"double": "keyword3",
	"else": "keyword1",
	"enum": "keyword1",
	"escape": "literal2",
	"eval": "literal2",
	"export": "keyword2",
	"extends": "keyword1",
	"false": "literal2",
	"final": "keyword1",
	"finally": "keyword1",
	"float": "keyword3",
	"for": "keyword1",
	"function": "keyword1",
	"goto": "keyword1",
	"if": "keyword1",
	"implements": "keyword1",
	"import": "keyword2",
	"in": "keyword1",
	"instanceof": "keyword1",
	"int": "keyword3",
	"interface": "keyword1",
	"isFinite": "literal2",
	"isNaN": "literal2",
	"long": "keyword3",
	"native": "keyword1",
	"new": "keyword1",
	"null": "literal2",
	"package": "keyword2",
	"parseFloat": "literal2",
	"parseInt": "literal2",
	"private": "keyword1",
	"protected": "keyword1",
	"public": "keyword1",
	"return": "keyword1",
	"short": "keyword3",
	"static": "keyword1",
	"super": "literal2",
	"switch": "keyword1",
	"synchronized": "keyword1",
	"this": "literal2",
	"throw": "keyword1",
	"throws": "keyword1",
	"transient": "keyword1",
	"true": "literal2",
	"try": "keyword1",
	"typeof": "keyword1",
	"unescape": "literal2",
	"var": "keyword1",
	"void": "keyword3",
	"volatile": "keyword1",
	"while": "keyword1",
	"with": "keyword1",
}

# Dictionary of keywords dictionaries for javascript mode.
keywordsDictDict = {
	"javascript_main": javascript_main_keywords_dict,
}

# Rules for javascript_main ruleset.

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
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule4(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment1", seq="<!--",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="?",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=False, at_whitespace_end=True, at_word_start=False, exclude_match=True)

def rule30(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule31(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule7,],
	"\"": [rule1,],
	"%": [rule16,],
	"&": [rule17,],
	"'": [rule2,],
	"(": [rule3,],
	"*": [rule13,],
	"+": [rule10,],
	",": [rule24,],
	"-": [rule11,],
	".": [rule21,],
	"/": [rule0,rule4,rule12,],
	"0": [rule31,],
	"1": [rule31,],
	"2": [rule31,],
	"3": [rule31,],
	"4": [rule31,],
	"5": [rule31,],
	"6": [rule31,],
	"7": [rule31,],
	"8": [rule31,],
	"9": [rule31,],
	":": [rule29,rule30,],
	";": [rule25,],
	"<": [rule5,rule9,rule15,],
	"=": [rule6,],
	">": [rule8,rule14,],
	"?": [rule28,],
	"@": [rule31,],
	"A": [rule31,],
	"B": [rule31,],
	"C": [rule31,],
	"D": [rule31,],
	"E": [rule31,],
	"F": [rule31,],
	"G": [rule31,],
	"H": [rule31,],
	"I": [rule31,],
	"J": [rule31,],
	"K": [rule31,],
	"L": [rule31,],
	"M": [rule31,],
	"N": [rule31,],
	"O": [rule31,],
	"P": [rule31,],
	"Q": [rule31,],
	"R": [rule31,],
	"S": [rule31,],
	"T": [rule31,],
	"U": [rule31,],
	"V": [rule31,],
	"W": [rule31,],
	"X": [rule31,],
	"Y": [rule31,],
	"Z": [rule31,],
	"[": [rule27,],
	"]": [rule26,],
	"^": [rule19,],
	"_": [rule31,],
	"a": [rule31,],
	"b": [rule31,],
	"c": [rule31,],
	"d": [rule31,],
	"e": [rule31,],
	"f": [rule31,],
	"g": [rule31,],
	"h": [rule31,],
	"i": [rule31,],
	"j": [rule31,],
	"k": [rule31,],
	"l": [rule31,],
	"m": [rule31,],
	"n": [rule31,],
	"o": [rule31,],
	"p": [rule31,],
	"q": [rule31,],
	"r": [rule31,],
	"s": [rule31,],
	"t": [rule31,],
	"u": [rule31,],
	"v": [rule31,],
	"w": [rule31,],
	"x": [rule31,],
	"y": [rule31,],
	"z": [rule31,],
	"{": [rule23,],
	"|": [rule18,],
	"}": [rule22,],
	"~": [rule20,],
}

# x.rulesDictDict for javascript mode.
rulesDictDict = {
	"javascript_main": rulesDict1,
}

# Import dict for javascript mode.
importDict = {}

