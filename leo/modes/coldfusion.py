# Leo colorizer control file for coldfusion mode.
# This file is in the public domain.

# Properties for coldfusion mode.
properties = {
	"commentEnd": "-->",
	"commentStart": "<!--",
}

# Attributes dict for coldfusion_main ruleset.
coldfusion_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for coldfusion_tags ruleset.
coldfusion_tags_attributes_dict = {
	"default": "MARKUP",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for coldfusion_cfscript ruleset.
coldfusion_cfscript_attributes_dict = {
	"default": "KEYWORD1",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for coldfusion_cftags ruleset.
coldfusion_cftags_attributes_dict = {
	"default": "KEYWORD3",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for coldfusion mode.
attributesDictDict = {
	"coldfusion_cfscript": coldfusion_cfscript_attributes_dict,
	"coldfusion_cftags": coldfusion_cftags_attributes_dict,
	"coldfusion_main": coldfusion_main_attributes_dict,
	"coldfusion_tags": coldfusion_tags_attributes_dict,
}

# Keywords dict for coldfusion_main ruleset.
coldfusion_main_keywords_dict = {}

# Keywords dict for coldfusion_tags ruleset.
coldfusion_tags_keywords_dict = {}

# Keywords dict for coldfusion_cfscript ruleset.
coldfusion_cfscript_keywords_dict = {
	"abs": "function",
	"arrayappend": "function",
	"arrayavg": "function",
	"arrayclear": "function",
	"arraydeleteat": "function",
	"arrayinsertat": "function",
	"arrayisempty": "function",
	"arraylen": "function",
	"arraymax": "function",
	"arraymin": "function",
	"arraynew": "function",
	"arrayprepend": "function",
	"arrayresize": "function",
	"arrayset": "function",
	"arraysort": "function",
	"arraysum": "function",
	"arrayswap": "function",
	"arraytolist": "function",
	"asc": "function",
	"atn": "function",
	"bitand": "function",
	"bitmaskclear": "function",
	"bitmaskread": "function",
	"bitmaskset": "function",
	"bitnot": "function",
	"bitor": "function",
	"bitshln": "function",
	"bitshrn": "function",
	"bitxor": "function",
	"break": "function",
	"ceiling": "function",
	"chr": "function",
	"cjustify": "function",
	"compare": "function",
	"comparenocase": "function",
	"cos": "function",
	"createdate": "function",
	"createdatetime": "function",
	"createodbcdate": "function",
	"createodbcdatetime": "function",
	"createodbctime": "function",
	"createtime": "function",
	"createtimespan": "function",
	"dateadd": "function",
	"datecompare": "function",
	"datediff": "function",
	"dateformat": "function",
	"datepart": "function",
	"day": "function",
	"dayofweek": "function",
	"dayofweekasstring": "function",
	"dayofyear": "function",
	"daysinmonth": "function",
	"daysinyear": "function",
	"de": "function",
	"decimalformat": "function",
	"decrementvalue": "function",
	"decrypt": "function",
	"deleteclientvariable": "function",
	"directoryexists": "function",
	"dollarformat": "function",
	"else": "function",
	"encrypt": "function",
	"evaluate": "function",
	"exp": "function",
	"expandpath": "function",
	"fileexists": "function",
	"find": "function",
	"findnocase": "function",
	"findoneof": "function",
	"firstdayofmonth": "function",
	"fix": "function",
	"for": "function",
	"formatbasen": "function",
	"getbasetagdata": "function",
	"getbasetaglist": "function",
	"getclientvariableslist": "function",
	"getdirectoryfrompath": "function",
	"getfilefrompath": "function",
	"getlocale": "function",
	"gettempdirectory": "function",
	"gettempfile": "function",
	"gettemplatepath": "function",
	"gettickcount": "function",
	"gettoken": "function",
	"hour": "function",
	"htmlcodeformat": "function",
	"htmleditformat": "function",
	"if": "function",
	"if(": "function",
	"iif": "function",
	"incrementvalue": "function",
	"inputbasen": "function",
	"insert": "function",
	"int": "function",
	"isarray": "function",
	"isauthenticated": "function",
	"isauthorized": "function",
	"isboolean": "function",
	"isdate": "function",
	"isdebugmode": "function",
	"isdefined": "function",
	"isleapyear": "function",
	"isnumeric": "function",
	"isnumericdate": "function",
	"isquery": "function",
	"issimplevalue": "function",
	"isstruct": "function",
	"lcase": "function",
	"left": "function",
	"len": "function",
	"listappend": "function",
	"listchangedelims": "function",
	"listcontains": "function",
	"listcontainsnocase": "function",
	"listdeleteat": "function",
	"listfind": "function",
	"listfindnocase": "function",
	"listfirst": "function",
	"listgetat": "function",
	"listinsertat": "function",
	"listlast": "function",
	"listlen": "function",
	"listprepend": "function",
	"listrest": "function",
	"listsetat": "function",
	"listtoarray": "function",
	"ljustify": "function",
	"log": "function",
	"log10": "function",
	"lscurrencyformat": "function",
	"lsdateformat": "function",
	"lsiscurrency": "function",
	"lsisdate": "function",
	"lsisnumeric": "function",
	"lsnumberformat": "function",
	"lsparsecurrency": "function",
	"lsparsedatetime": "function",
	"lsparsenumber": "function",
	"lstimeformat": "function",
	"ltrim": "function",
	"max": "function",
	"mid": "function",
	"min": "function",
	"minute": "function",
	"month": "function",
	"monthasstring": "function",
	"now": "function",
	"numberformat": "function",
	"paragraphformat": "function",
	"parameterexists": "function",
	"parsedatetime": "function",
	"pi": "function",
	"preservesinglequotes": "function",
	"quarter": "function",
	"queryaddrow": "function",
	"querynew": "function",
	"querysetcell": "function",
	"quotedvaluelist": "function",
	"rand": "function",
	"randomize": "function",
	"randrange": "function",
	"refind": "function",
	"refindnocase": "function",
	"removechars": "function",
	"repeatstring": "function",
	"replace": "function",
	"replacelist": "function",
	"replacenocase": "function",
	"rereplace": "function",
	"rereplacenocase": "function",
	"reverse": "function",
	"right": "function",
	"rjustify": "function",
	"round": "function",
	"rtrim": "function",
	"second": "function",
	"setlocale": "function",
	"setvariable": "function",
	"sgn": "function",
	"sin": "function",
	"spanexcluding": "function",
	"spanincluding": "function",
	"sqr": "function",
	"stripcr": "function",
	"structclear": "function",
	"structcopy": "function",
	"structcount": "function",
	"structdelete": "function",
	"structfind": "function",
	"structinsert": "function",
	"structisempty": "function",
	"structkeyexists": "function",
	"structnew": "function",
	"structupdate": "function",
	"tan": "function",
	"timeformat": "function",
	"trim": "function",
	"ucase": "function",
	"urlencodedformat": "function",
	"val": "function",
	"valuelist": "function",
	"week": "function",
	"while": "function",
	"writeoutput": "function",
	"year": "function",
	"yesnoformat": "function",
	"{": "function",
	"}": "function",
	"}else": "function",
	"}else{": "function",
}

# Keywords dict for coldfusion_cftags ruleset.
coldfusion_cftags_keywords_dict = {
	"abs": "keyword2",
	"and": "operator",
	"arrayappend": "keyword2",
	"arrayavg": "keyword2",
	"arrayclear": "keyword2",
	"arraydeleteat": "keyword2",
	"arrayinsertat": "keyword2",
	"arrayisempty": "keyword2",
	"arraylen": "keyword2",
	"arraymax": "keyword2",
	"arraymin": "keyword2",
	"arraynew": "keyword2",
	"arrayprepend": "keyword2",
	"arrayresize": "keyword2",
	"arrayset": "keyword2",
	"arraysort": "keyword2",
	"arraysum": "keyword2",
	"arrayswap": "keyword2",
	"arraytolist": "keyword2",
	"asc": "keyword2",
	"atn": "keyword2",
	"bitand": "keyword2",
	"bitmaskclear": "keyword2",
	"bitmaskread": "keyword2",
	"bitmaskset": "keyword2",
	"bitnot": "keyword2",
	"bitor": "keyword2",
	"bitshln": "keyword2",
	"bitshrn": "keyword2",
	"bitxor": "keyword2",
	"ceiling": "keyword2",
	"chr": "keyword2",
	"cjustify": "keyword2",
	"compare": "keyword2",
	"comparenocase": "keyword2",
	"cos": "keyword2",
	"createdate": "keyword2",
	"createdatetime": "keyword2",
	"createodbcdate": "keyword2",
	"createodbcdatetime": "keyword2",
	"createodbctime": "keyword2",
	"createtime": "keyword2",
	"createtimespan": "keyword2",
	"dateadd": "keyword2",
	"datecompare": "keyword2",
	"datediff": "keyword2",
	"dateformat": "keyword2",
	"datepart": "keyword2",
	"day": "keyword2",
	"dayofweek": "keyword2",
	"dayofweekasstring": "keyword2",
	"dayofyear": "keyword2",
	"daysinmonth": "keyword2",
	"daysinyear": "keyword2",
	"de": "keyword2",
	"decimalformat": "keyword2",
	"decrementvalue": "keyword2",
	"decrypt": "keyword2",
	"deleteclientvariable": "keyword2",
	"directoryexists": "keyword2",
	"dollarformat": "keyword2",
	"encrypt": "keyword2",
	"eq": "operator",
	"evaluate": "keyword2",
	"exp": "keyword2",
	"expandpath": "keyword2",
	"fileexists": "keyword2",
	"find": "keyword2",
	"findnocase": "keyword2",
	"findoneof": "keyword2",
	"firstdayofmonth": "keyword2",
	"fix": "keyword2",
	"formatbasen": "keyword2",
	"getbasetagdata": "keyword2",
	"getbasetaglist": "keyword2",
	"getclientvariableslist": "keyword2",
	"getdirectoryfrompath": "keyword2",
	"getfilefrompath": "keyword2",
	"getlocale": "keyword2",
	"gettempdirectory": "keyword2",
	"gettempfile": "keyword2",
	"gettemplatepath": "keyword2",
	"gettickcount": "keyword2",
	"gettoken": "keyword2",
	"greater": "operator",
	"gt": "operator",
	"gte": "operator",
	"hour": "keyword2",
	"htmlcodeformat": "keyword2",
	"htmleditformat": "keyword2",
	"iif": "keyword2",
	"incrementvalue": "keyword2",
	"inputbasen": "keyword2",
	"insert": "keyword2",
	"int": "keyword2",
	"is": "operator",
	"isarray": "keyword2",
	"isauthenticated": "keyword2",
	"isauthorized": "keyword2",
	"isboolean": "keyword2",
	"isdate": "keyword2",
	"isdebugmode": "keyword2",
	"isdefined": "keyword2",
	"isleapyear": "keyword2",
	"isnumeric": "keyword2",
	"isnumericdate": "keyword2",
	"isquery": "keyword2",
	"issimplevalue": "keyword2",
	"isstruct": "keyword2",
	"lcase": "keyword2",
	"left": "keyword2",
	"len": "keyword2",
	"less": "operator",
	"listappend": "keyword2",
	"listchangedelims": "keyword2",
	"listcontains": "keyword2",
	"listcontainsnocase": "keyword2",
	"listdeleteat": "keyword2",
	"listfind": "keyword2",
	"listfindnocase": "keyword2",
	"listfirst": "keyword2",
	"listgetat": "keyword2",
	"listinsertat": "keyword2",
	"listlast": "keyword2",
	"listlen": "keyword2",
	"listprepend": "keyword2",
	"listrest": "keyword2",
	"listsetat": "keyword2",
	"listtoarray": "keyword2",
	"ljustify": "keyword2",
	"log": "keyword2",
	"log10": "keyword2",
	"lscurrencyformat": "keyword2",
	"lsdateformat": "keyword2",
	"lsiscurrency": "keyword2",
	"lsisdate": "keyword2",
	"lsisnumeric": "keyword2",
	"lsnumberformat": "keyword2",
	"lsparsecurrency": "keyword2",
	"lsparsedatetime": "keyword2",
	"lsparsenumber": "keyword2",
	"lstimeformat": "keyword2",
	"lt": "operator",
	"lte": "operator",
	"ltrim": "keyword2",
	"max": "keyword2",
	"mid": "keyword2",
	"min": "keyword2",
	"minute": "keyword2",
	"month": "keyword2",
	"monthasstring": "keyword2",
	"neq": "operator",
	"not": "operator",
	"now": "keyword2",
	"numberformat": "keyword2",
	"or": "operator",
	"paragraphformat": "keyword2",
	"parameterexists": "keyword2",
	"parsedatetime": "keyword2",
	"pi": "keyword2",
	"preservesinglequotes": "keyword2",
	"quarter": "keyword2",
	"queryaddrow": "keyword2",
	"querynew": "keyword2",
	"querysetcell": "keyword2",
	"quotedvaluelist": "keyword2",
	"rand": "keyword2",
	"randomize": "keyword2",
	"randrange": "keyword2",
	"refind": "keyword2",
	"refindnocase": "keyword2",
	"removechars": "keyword2",
	"repeatstring": "keyword2",
	"replace": "keyword2",
	"replacelist": "keyword2",
	"replacenocase": "keyword2",
	"rereplace": "keyword2",
	"rereplacenocase": "keyword2",
	"reverse": "keyword2",
	"right": "keyword2",
	"rjustify": "keyword2",
	"round": "keyword2",
	"rtrim": "keyword2",
	"second": "keyword2",
	"setlocale": "keyword2",
	"setvariable": "keyword2",
	"sgn": "keyword2",
	"sin": "keyword2",
	"spanexcluding": "keyword2",
	"spanincluding": "keyword2",
	"sqr": "keyword2",
	"stripcr": "keyword2",
	"structclear": "keyword2",
	"structcopy": "keyword2",
	"structcount": "keyword2",
	"structdelete": "keyword2",
	"structfind": "keyword2",
	"structinsert": "keyword2",
	"structisempty": "keyword2",
	"structkeyexists": "keyword2",
	"structnew": "keyword2",
	"structupdate": "keyword2",
	"tan": "keyword2",
	"than": "operator",
	"timeformat": "keyword2",
	"trim": "keyword2",
	"ucase": "keyword2",
	"urlencodedformat": "keyword2",
	"val": "keyword2",
	"valuelist": "keyword2",
	"week": "keyword2",
	"writeoutput": "keyword2",
	"xor": "operator",
	"year": "keyword2",
	"yesnoformat": "keyword2",
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
rulesDict2 = {
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
rulesDict3 = {
	"!": [rule31,],
	"\"": [rule19,],
	"&": [rule32,],
	"'": [rule20,],
	"(": [rule21,rule33,],
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
	"{": [rule33,],
	"}": [rule33,],
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
rulesDict4 = {
	"\"": [rule34,],
	"#": [rule37,rule38,],
	"'": [rule35,],
	"(": [rule39,],
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
	"{": [rule39,],
	"}": [rule39,],
}

# x.rulesDictDict for coldfusion mode.
rulesDictDict = {
	"coldfusion_cfscript": rulesDict3,
	"coldfusion_cftags": rulesDict4,
	"coldfusion_main": rulesDict1,
	"coldfusion_tags": rulesDict2,
}

# Import dict for coldfusion mode.
importDict = {}

