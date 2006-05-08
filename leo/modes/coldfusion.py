# Leo colorizer control file for coldfusion mode.

# Properties for coldfusion mode.
properties = {
	"commentEnd": "-->",
	"commentStart": "<!--",
}

# Keywords dict for coldfusion_main ruleset.
coldfusion_main_keywords_dict = {}

# Keywords dict for coldfusion_tags ruleset.
coldfusion_tags_keywords_dict = {}

# Keywords dict for coldfusion_cfscript ruleset.
coldfusion_cfscript_keywords_dict = {
	"		": "keywords",
	"			": "keywords",
	"
": "keywords",
	"Abs": "function",
	"ArrayAppend": "function",
	"ArrayAvg": "function",
	"ArrayClear": "function",
	"ArrayDeleteAt": "function",
	"ArrayInsertAt": "function",
	"ArrayIsEmpty": "function",
	"ArrayLen": "function",
	"ArrayMax": "function",
	"ArrayMin": "function",
	"ArrayNew": "function",
	"ArrayPrepend": "function",
	"ArrayResize": "function",
	"ArraySet": "function",
	"ArraySort": "function",
	"ArraySum": "function",
	"ArraySwap": "function",
	"ArrayToList": "function",
	"Asc": "function",
	"Atn": "function",
	"BitAnd": "function",
	"BitMaskClear": "function",
	"BitMaskRead": "function",
	"BitMaskSet": "function",
	"BitNot": "function",
	"BitOr": "function",
	"BitSHLN": "function",
	"BitSHRN": "function",
	"BitXor": "function",
	"CJustify": "function",
	"Ceiling": "function",
	"Chr": "function",
	"Compare": "function",
	"CompareNoCase": "function",
	"Cos": "function",
	"CreateDate": "function",
	"CreateDateTime": "function",
	"CreateODBCDate": "function",
	"CreateODBCDateTime": "function",
	"CreateODBCTime": "function",
	"CreateTime": "function",
	"CreateTimeSpan": "function",
	"DE": "function",
	"DateAdd": "function",
	"DateCompare": "function",
	"DateDiff": "function",
	"DateFormat": "function",
	"DatePart": "function",
	"Day": "function",
	"DayOfWeek": "function",
	"DayOfWeekAsString": "function",
	"DayOfYear": "function",
	"DaysInMonth": "function",
	"DaysInYear": "function",
	"DecimalFormat": "function",
	"DecrementValue": "function",
	"Decrypt": "function",
	"DeleteClientVariable": "function",
	"DirectoryExists": "function",
	"DollarFormat": "function",
	"Encrypt": "function",
	"Evaluate": "function",
	"Exp": "function",
	"ExpandPath": "function",
	"FileExists": "function",
	"Find": "function",
	"FindNoCase": "function",
	"FindOneOf": "function",
	"FirstDayOfMonth": "function",
	"Fix": "function",
	"FormatBaseN": "function",
	"GetBaseTagData": "function",
	"GetBaseTagList": "function",
	"GetClientVariablesList": "function",
	"GetDirectoryFromPath": "function",
	"GetFileFromPath": "function",
	"GetLocale": "function",
	"GetTempDirectory": "function",
	"GetTempFile": "function",
	"GetTemplatePath": "function",
	"GetTickCount": "function",
	"GetToken": "function",
	"HTMLCodeFormat": "function",
	"HTMLEditFormat": "function",
	"Hour": "function",
	"IIf": "function",
	"IncrementValue": "function",
	"InputBaseN": "function",
	"Insert": "function",
	"Int": "function",
	"IsArray": "function",
	"IsAuthenticated": "function",
	"IsAuthorized": "function",
	"IsBoolean": "function",
	"IsDate": "function",
	"IsDebugMode": "function",
	"IsDefined": "function",
	"IsLeapYear": "function",
	"IsNumeric": "function",
	"IsNumericDate": "function",
	"IsQuery": "function",
	"IsSimpleValue": "function",
	"IsStruct": "function",
	"LCase": "function",
	"LJustify": "function",
	"LSCurrencyFormat": "function",
	"LSDateFormat": "function",
	"LSIsCurrency": "function",
	"LSIsDate": "function",
	"LSIsNumeric": "function",
	"LSNumberFormat": "function",
	"LSParseCurrency": "function",
	"LSParseDateTime": "function",
	"LSParseNumber": "function",
	"LSTimeFormat": "function",
	"LTrim": "function",
	"Left": "function",
	"Len": "function",
	"ListAppend": "function",
	"ListChangeDelims": "function",
	"ListContains": "function",
	"ListContainsNoCase": "function",
	"ListDeleteAt": "function",
	"ListFind": "function",
	"ListFindNoCase": "function",
	"ListFirst": "function",
	"ListGetAt": "function",
	"ListInsertAt": "function",
	"ListLast": "function",
	"ListLen": "function",
	"ListPrepend": "function",
	"ListRest": "function",
	"ListSetAt": "function",
	"ListToArray": "function",
	"Log": "function",
	"Log10": "function",
	"Max": "function",
	"Mid": "function",
	"Min": "function",
	"Minute": "function",
	"Month": "function",
	"MonthAsString": "function",
	"Now": "function",
	"NumberFormat": "function",
	"ParagraphFormat": "function",
	"ParameterExists": "function",
	"ParseDateTime": "function",
	"Pi": "function",
	"PreserveSingleQuotes": "function",
	"Quarter": "function",
	"QueryAddRow": "function",
	"QueryNew": "function",
	"QuerySetCell": "function",
	"QuotedValueList": "function",
	"REFind": "function",
	"REFindNoCase": "function",
	"REReplace": "function",
	"REReplaceNoCase": "function",
	"RJustify": "function",
	"RTrim": "function",
	"Rand": "function",
	"RandRange": "function",
	"Randomize": "function",
	"RemoveChars": "function",
	"RepeatString": "function",
	"Replace": "function",
	"ReplaceList": "function",
	"ReplaceNoCase": "function",
	"Reverse": "function",
	"Right": "function",
	"Round": "function",
	"Second": "function",
	"SetLocale": "function",
	"SetVariable": "function",
	"Sgn": "function",
	"Sin": "function",
	"SpanExcluding": "function",
	"SpanIncluding": "function",
	"Sqr": "function",
	"StripCR": "function",
	"StructClear": "function",
	"StructCopy": "function",
	"StructCount": "function",
	"StructDelete": "function",
	"StructFind": "function",
	"StructInsert": "function",
	"StructIsEmpty": "function",
	"StructKeyExists": "function",
	"StructNew": "function",
	"StructUpdate": "function",
	"Tan": "function",
	"TimeFormat": "function",
	"Trim": "function",
	"UCase": "function",
	"URLEncodedFormat": "function",
	"Val": "function",
	"ValueList": "function",
	"Week": "function",
	"WriteOutput": "function",
	"Year": "function",
	"YesNoFormat": "function",
	"break": "function",
	"else": "function",
	"for": "function",
	"if": "function",
	"if(": "function",
	"while": "function",
	"{": "function",
	"}": "function",
	"}else": "function",
	"}else{": "function",
}

# Keywords dict for coldfusion_cftags ruleset.
coldfusion_cftags_keywords_dict = {
	"		": "keywords",
	"			": "keywords",
	"
": "keywords",
	"AND": "operator",
	"Abs": "keyword2",
	"ArrayAppend": "keyword2",
	"ArrayAvg": "keyword2",
	"ArrayClear": "keyword2",
	"ArrayDeleteAt": "keyword2",
	"ArrayInsertAt": "keyword2",
	"ArrayIsEmpty": "keyword2",
	"ArrayLen": "keyword2",
	"ArrayMax": "keyword2",
	"ArrayMin": "keyword2",
	"ArrayNew": "keyword2",
	"ArrayPrepend": "keyword2",
	"ArrayResize": "keyword2",
	"ArraySet": "keyword2",
	"ArraySort": "keyword2",
	"ArraySum": "keyword2",
	"ArraySwap": "keyword2",
	"ArrayToList": "keyword2",
	"Asc": "keyword2",
	"Atn": "keyword2",
	"BitAnd": "keyword2",
	"BitMaskClear": "keyword2",
	"BitMaskRead": "keyword2",
	"BitMaskSet": "keyword2",
	"BitNot": "keyword2",
	"BitOr": "keyword2",
	"BitSHLN": "keyword2",
	"BitSHRN": "keyword2",
	"BitXor": "keyword2",
	"CJustify": "keyword2",
	"Ceiling": "keyword2",
	"Chr": "keyword2",
	"Compare": "keyword2",
	"CompareNoCase": "keyword2",
	"Cos": "keyword2",
	"CreateDate": "keyword2",
	"CreateDateTime": "keyword2",
	"CreateODBCDate": "keyword2",
	"CreateODBCDateTime": "keyword2",
	"CreateODBCTime": "keyword2",
	"CreateTime": "keyword2",
	"CreateTimeSpan": "keyword2",
	"DE": "keyword2",
	"DateAdd": "keyword2",
	"DateCompare": "keyword2",
	"DateDiff": "keyword2",
	"DateFormat": "keyword2",
	"DatePart": "keyword2",
	"Day": "keyword2",
	"DayOfWeek": "keyword2",
	"DayOfWeekAsString": "keyword2",
	"DayOfYear": "keyword2",
	"DaysInMonth": "keyword2",
	"DaysInYear": "keyword2",
	"DecimalFormat": "keyword2",
	"DecrementValue": "keyword2",
	"Decrypt": "keyword2",
	"DeleteClientVariable": "keyword2",
	"DirectoryExists": "keyword2",
	"DollarFormat": "keyword2",
	"EQ": "operator",
	"Encrypt": "keyword2",
	"Evaluate": "keyword2",
	"Exp": "keyword2",
	"ExpandPath": "keyword2",
	"FileExists": "keyword2",
	"Find": "keyword2",
	"FindNoCase": "keyword2",
	"FindOneOf": "keyword2",
	"FirstDayOfMonth": "keyword2",
	"Fix": "keyword2",
	"FormatBaseN": "keyword2",
	"GREATER": "operator",
	"GT": "operator",
	"GTE": "operator",
	"GetBaseTagData": "keyword2",
	"GetBaseTagList": "keyword2",
	"GetClientVariablesList": "keyword2",
	"GetDirectoryFromPath": "keyword2",
	"GetFileFromPath": "keyword2",
	"GetLocale": "keyword2",
	"GetTempDirectory": "keyword2",
	"GetTempFile": "keyword2",
	"GetTemplatePath": "keyword2",
	"GetTickCount": "keyword2",
	"GetToken": "keyword2",
	"HTMLCodeFormat": "keyword2",
	"HTMLEditFormat": "keyword2",
	"Hour": "keyword2",
	"IIf": "keyword2",
	"IS": "operator",
	"IncrementValue": "keyword2",
	"InputBaseN": "keyword2",
	"Insert": "keyword2",
	"Int": "keyword2",
	"IsArray": "keyword2",
	"IsAuthenticated": "keyword2",
	"IsAuthorized": "keyword2",
	"IsBoolean": "keyword2",
	"IsDate": "keyword2",
	"IsDebugMode": "keyword2",
	"IsDefined": "keyword2",
	"IsLeapYear": "keyword2",
	"IsNumeric": "keyword2",
	"IsNumericDate": "keyword2",
	"IsQuery": "keyword2",
	"IsSimpleValue": "keyword2",
	"IsStruct": "keyword2",
	"LCase": "keyword2",
	"LESS": "operator",
	"LJustify": "keyword2",
	"LSCurrencyFormat": "keyword2",
	"LSDateFormat": "keyword2",
	"LSIsCurrency": "keyword2",
	"LSIsDate": "keyword2",
	"LSIsNumeric": "keyword2",
	"LSNumberFormat": "keyword2",
	"LSParseCurrency": "keyword2",
	"LSParseDateTime": "keyword2",
	"LSParseNumber": "keyword2",
	"LSTimeFormat": "keyword2",
	"LT": "operator",
	"LTE": "operator",
	"LTrim": "keyword2",
	"Left": "keyword2",
	"Len": "keyword2",
	"ListAppend": "keyword2",
	"ListChangeDelims": "keyword2",
	"ListContains": "keyword2",
	"ListContainsNoCase": "keyword2",
	"ListDeleteAt": "keyword2",
	"ListFind": "keyword2",
	"ListFindNoCase": "keyword2",
	"ListFirst": "keyword2",
	"ListGetAt": "keyword2",
	"ListInsertAt": "keyword2",
	"ListLast": "keyword2",
	"ListLen": "keyword2",
	"ListPrepend": "keyword2",
	"ListRest": "keyword2",
	"ListSetAt": "keyword2",
	"ListToArray": "keyword2",
	"Log": "keyword2",
	"Log10": "keyword2",
	"Max": "keyword2",
	"Mid": "keyword2",
	"Min": "keyword2",
	"Minute": "keyword2",
	"Month": "keyword2",
	"MonthAsString": "keyword2",
	"NEQ": "operator",
	"NOT": "operator",
	"Now": "keyword2",
	"NumberFormat": "keyword2",
	"OR": "operator",
	"ParagraphFormat": "keyword2",
	"ParameterExists": "keyword2",
	"ParseDateTime": "keyword2",
	"Pi": "keyword2",
	"PreserveSingleQuotes": "keyword2",
	"Quarter": "keyword2",
	"QueryAddRow": "keyword2",
	"QueryNew": "keyword2",
	"QuerySetCell": "keyword2",
	"QuotedValueList": "keyword2",
	"REFind": "keyword2",
	"REFindNoCase": "keyword2",
	"REReplace": "keyword2",
	"REReplaceNoCase": "keyword2",
	"RJustify": "keyword2",
	"RTrim": "keyword2",
	"Rand": "keyword2",
	"RandRange": "keyword2",
	"Randomize": "keyword2",
	"RemoveChars": "keyword2",
	"RepeatString": "keyword2",
	"Replace": "keyword2",
	"ReplaceList": "keyword2",
	"ReplaceNoCase": "keyword2",
	"Reverse": "keyword2",
	"Right": "keyword2",
	"Round": "keyword2",
	"Second": "keyword2",
	"SetLocale": "keyword2",
	"SetVariable": "keyword2",
	"Sgn": "keyword2",
	"Sin": "keyword2",
	"SpanExcluding": "keyword2",
	"SpanIncluding": "keyword2",
	"Sqr": "keyword2",
	"StripCR": "keyword2",
	"StructClear": "keyword2",
	"StructCopy": "keyword2",
	"StructCount": "keyword2",
	"StructDelete": "keyword2",
	"StructFind": "keyword2",
	"StructInsert": "keyword2",
	"StructIsEmpty": "keyword2",
	"StructKeyExists": "keyword2",
	"StructNew": "keyword2",
	"StructUpdate": "keyword2",
	"THAN": "operator",
	"Tan": "keyword2",
	"TimeFormat": "keyword2",
	"Trim": "keyword2",
	"UCase": "keyword2",
	"URLEncodedFormat": "keyword2",
	"Val": "keyword2",
	"ValueList": "keyword2",
	"Week": "keyword2",
	"WriteOutput": "keyword2",
	"XOR": "operator",
	"Year": "keyword2",
	"YesNoFormat": "keyword2",
}

# Dictionary of keywords dictionaries for coldfusion mode.
keywordsDictDict = {
	"coldfusion_cfscript": coldfusion_cfscript_keywords_dict,
	"coldfusion_cftags": coldfusion_cftags_keywords_dict,
	"coldfusion_main": coldfusion_main_keywords_dict,
	"coldfusion_tags": coldfusion_tags_keywords_dict,
}

# Rules for coldfusion_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment4", begin="<!---", end="--->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="comment3", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword3", begin="<CFSCRIPT", end="</CFSCRIPT>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="CFSCRIPT",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword3", begin="<CF", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="CFTAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword3", begin="</CF", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="CFTAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule7(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<SCRIPT", end="</SCRIPT>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="html::JAVASCRIPT",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule8(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<STYLE", end="</STYLE>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="html::CSS",exclude_match=False,
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
	"/": [rule1,rule2,],
	"<": [rule0,rule3,rule4,rule5,rule6,rule7,rule8,rule9,],
}

# Rules for coldfusion_tags ruleset.

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
    return colorer.match_span(s, i, kind="keyword3", begin="<CF", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="CFTAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule15(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword3", begin="</CF", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="CFTAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule16(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword3", begin="<CFSCRIPT", end="</CFSCRIPT>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="CFSCRIPT",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules dict for tags ruleset.
rulesDict1 = {
	"\"": [rule11,],
	"'": [rule12,],
	"<": [rule14,rule15,rule16,],
	"=": [rule13,],
}

# Rules for coldfusion_cfscript ruleset.

def rule17(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule18(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule19(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule20(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal2", seq="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal2", seq=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="><",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule31(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule32(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule33(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for cfscript ruleset.
rulesDict1 = {
	"!": [rule31,],
	"\"": [rule19,],
	"&": [rule32,],
	"'": [rule20,],
	"(": [rule21,],
	")": [rule22,],
	"*": [rule30,],
	"+": [rule24,],
	"-": [rule25,],
	"/": [rule17,rule18,rule26,],
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
	"<": [rule28,],
	"=": [rule23,],
	">": [rule27,rule29,],
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

# Rules for coldfusion_cftags ruleset.

def rule34(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule35(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule36(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule37(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="##",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule38(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="#", end="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule39(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for cftags ruleset.
rulesDict1 = {
	"\"": [rule34,],
	"#": [rule37,rule38,],
	"'": [rule35,],
	"0": [rule39,],
	"1": [rule39,],
	"2": [rule39,],
	"3": [rule39,],
	"4": [rule39,],
	"5": [rule39,],
	"6": [rule39,],
	"7": [rule39,],
	"8": [rule39,],
	"9": [rule39,],
	"=": [rule36,],
	"@": [rule39,],
	"A": [rule39,],
	"B": [rule39,],
	"C": [rule39,],
	"D": [rule39,],
	"E": [rule39,],
	"F": [rule39,],
	"G": [rule39,],
	"H": [rule39,],
	"I": [rule39,],
	"J": [rule39,],
	"K": [rule39,],
	"L": [rule39,],
	"M": [rule39,],
	"N": [rule39,],
	"O": [rule39,],
	"P": [rule39,],
	"Q": [rule39,],
	"R": [rule39,],
	"S": [rule39,],
	"T": [rule39,],
	"U": [rule39,],
	"V": [rule39,],
	"W": [rule39,],
	"X": [rule39,],
	"Y": [rule39,],
	"Z": [rule39,],
	"_": [rule39,],
	"a": [rule39,],
	"b": [rule39,],
	"c": [rule39,],
	"d": [rule39,],
	"e": [rule39,],
	"f": [rule39,],
	"g": [rule39,],
	"h": [rule39,],
	"i": [rule39,],
	"j": [rule39,],
	"k": [rule39,],
	"l": [rule39,],
	"m": [rule39,],
	"n": [rule39,],
	"o": [rule39,],
	"p": [rule39,],
	"q": [rule39,],
	"r": [rule39,],
	"s": [rule39,],
	"t": [rule39,],
	"u": [rule39,],
	"v": [rule39,],
	"w": [rule39,],
	"x": [rule39,],
	"y": [rule39,],
	"z": [rule39,],
}

# x.rulesDictDict for coldfusion mode.
rulesDictDict = {
	"coldfusion_cfscript": rulesDict1,
	"coldfusion_cftags": rulesDict1,
	"coldfusion_main": rulesDict1,
	"coldfusion_tags": rulesDict1,
}

# Import dict for coldfusion mode.
importDict = {}

