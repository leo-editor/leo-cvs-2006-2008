# Leo colorizer control file for pl1 mode.
# This file is in the public domain.

# Properties for pl1 mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"wordBreakChars": ",+-=<>/?^&*",
}

# Attributes dict for pl1_main ruleset.
pl1_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "false",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for pl1 mode.
attributesDictDict = {
	"pl1_main": pl1_main_attributes_dict,
}

# Keywords dict for pl1_main ruleset.
pl1_main_keywords_dict = {
	"%include": "keyword1",
	"A": "keyword2",
	"C": "keyword2",
	"E": "keyword2",
	"F": "keyword2",
	"L": "keyword2",
	"P": "keyword2",
	"R": "keyword2",
	"abnormal": "keyword2",
	"abs": "keyword3",
	"acos": "keyword3",
	"acosf": "keyword3",
	"add": "keyword3",
	"addr": "keyword3",
	"addrdata": "keyword3",
	"address": "keyword3",
	"alias": "keyword1",
	"aligned": "keyword2",
	"all": "keyword3",
	"alloc": "keyword1",
	"allocate": "keyword1",
	"allocation": "keyword3",
	"allocn": "keyword3",
	"allocsize": "keyword3",
	"any": "keyword3",
	"anycond": "keyword2",
	"anycondition": "keyword2",
	"area": "keyword2",
	"asgn": "keyword2",
	"asin": "keyword3",
	"asinf": "keyword3",
	"asm": "keyword2",
	"assembler": "keyword2",
	"assignable": "keyword2",
	"atan": "keyword3",
	"atand": "keyword3",
	"atanf": "keyword3",
	"atanh": "keyword3",
	"attach": "keyword1",
	"attention": "keyword2",
	"attn": "keyword2",
	"auto": "keyword2",
	"automatic": "keyword2",
	"availablearea": "keyword3",
	"b": "keyword2",
	"b3": "keyword2",
	"b4": "keyword2",
	"based": "keyword2",
	"begin": "keyword1",
	"bigendian": "keyword2",
	"bin": "keyword2",
	"binary": "keyword2",
	"binaryvalue": "keyword3",
	"bind": "keyword3",
	"binvalue": "keyword3",
	"bit": "keyword2",
	"bitloc": "keyword3",
	"bitlocation": "keyword3",
	"bool": "keyword3",
	"buf": "keyword2",
	"buffered": "keyword2",
	"builtin": "keyword2",
	"bx": "keyword2",
	"by": "keyword1",
	"byaddr": "keyword2",
	"byname": "keyword1",
	"byte": "keyword3",
	"byvalue": "keyword2",
	"call": "keyword1",
	"cast": "keyword3",
	"cdecl": "keyword2",
	"cds": "keyword3",
	"ceil": "keyword3",
	"cell": "keyword2",
	"center": "keyword3",
	"centerright": "keyword3",
	"centre": "keyword3",
	"centreleft": "keyword3",
	"centreright": "keyword3",
	"char": "keyword2",
	"character": "keyword2",
	"charg": "keyword3",
	"chargraphic": "keyword3",
	"chargval": "keyword3",
	"checkstg": "keyword3",
	"close": "keyword1",
	"cobol": "keyword2",
	"collate": "keyword3",
	"column": "keyword2",
	"compare": "keyword3",
	"complex": "keyword2",
	"cond": "keyword2",
	"condition": "keyword2",
	"conjg": "keyword3",
	"conn": "keyword2",
	"connected": "keyword2",
	"controlled": "keyword2",
	"conv": "keyword2",
	"conversion": "keyword2",
	"copy": "keyword1",
	"cos": "keyword3",
	"cosd": "keyword3",
	"cosf": "keyword3",
	"cosh": "keyword3",
	"count": "keyword3",
	"cplx": "keyword2",
	"cs": "keyword3",
	"cstg": "keyword3",
	"ctl": "keyword2",
	"currentsize": "keyword3",
	"currentstorage": "keyword3",
	"data": "keyword2",
	"datafield": "keyword3",
	"date": "keyword3",
	"datetime": "keyword3",
	"days": "keyword3",
	"daystodate": "keyword3",
	"daystosecs": "keyword3",
	"dcl": "keyword1",
	"dec": "keyword2",
	"decimal": "keyword2",
	"declare": "keyword1",
	"def": "keyword2",
	"default": "keyword1",
	"define": "keyword1",
	"defined": "keyword2",
	"delay": "keyword1",
	"delete": "keyword1",
	"descriptor": "keyword2",
	"descriptors": "keyword2",
	"detach": "keyword1",
	"dft": "keyword1",
	"dim": "keyword2",
	"dimension": "keyword2",
	"direct": "keyword2",
	"display": "keyword1",
	"divide": "keyword3",
	"do": "keyword1",
	"downthru": "keyword1",
	"edit": "keyword2",
	"else": "keyword1",
	"empty": "keyword3",
	"end": "keyword1",
	"endfile": "keyword2",
	"endpage": "keyword2",
	"entry": "keyword1",
	"entryaddr": "keyword3",
	"env": "keyword2",
	"environment": "keyword2",
	"epsilon": "keyword3",
	"erfc": "keyword3",
	"error": "keyword2",
	"exclusive": "keyword2",
	"exit": "keyword1",
	"exp": "keyword3",
	"expf": "keyword3",
	"exponent": "keyword3",
	"exports": "keyword2",
	"ext": "keyword2",
	"external": "keyword2",
	"fetch": "keyword1",
	"fetchable": "keyword2",
	"file": "keyword2",
	"fileddint": "keyword3",
	"fileddtest": "keyword3",
	"fileddword": "keyword3",
	"fileid": "keyword3",
	"fileopen": "keyword3",
	"fileread": "keyword3",
	"fileseek": "keyword3",
	"filetell": "keyword3",
	"filewrite": "keyword3",
	"finish": "keyword2",
	"first": "keyword3",
	"fixed": "keyword2",
	"fixedoverflow": "keyword2",
	"float": "keyword2",
	"floor": "keyword3",
	"flush": "keyword1",
	"fofl": "keyword2",
	"format": "keyword2",
	"fortran": "keyword2",
	"free": "keyword1",
	"from": "keyword1",
	"fromalien": "keyword2",
	"g": "keyword2",
	"gamma": "keyword3",
	"generic": "keyword2",
	"get": "keyword1",
	"getenv": "keyword3",
	"go": "keyword1",
	"goto": "keyword1",
	"graphic": "keyword2",
	"gx": "keyword2",
	"handle": "keyword2",
	"hbound": "keyword3",
	"hex": "keyword3",
	"hexadec": "keyword2",
	"heximage": "keyword3",
	"high": "keyword3",
	"huge": "keyword3",
	"iand": "keyword3",
	"ieee": "keyword2",
	"ieor": "keyword3",
	"if": "keyword1",
	"ignore": "keyword1",
	"imag": "keyword3",
	"imported": "keyword2",
	"index": "keyword3",
	"init": "keyword2",
	"initial": "keyword2",
	"inline": "keyword2",
	"inot": "keyword3",
	"input": "keyword2",
	"inter": "keyword2",
	"internal": "keyword2",
	"into": "keyword1",
	"invalidop": "keyword2",
	"ior": "keyword3",
	"irred": "keyword2",
	"irreducible": "keyword2",
	"isigned": "keyword3",
	"isll": "keyword3",
	"ismain": "keyword3",
	"isrl": "keyword3",
	"iterate": "keyword1",
	"iunsigned": "keyword3",
	"key": "keyword1",
	"keyed": "keyword2",
	"keyfrom": "keyword1",
	"keyto": "keyword1",
	"label": "keyword2",
	"last": "keyword3",
	"lbound": "keyword3",
	"leave": "keyword1",
	"left": "keyword3",
	"length": "keyword3",
	"like": "keyword2",
	"limited": "keyword2",
	"line": "keyword1",
	"lineno": "keyword3",
	"linesize": "keyword2",
	"linkage": "keyword2",
	"list": "keyword2",
	"littleendian": "keyword2",
	"loc": "keyword3",
	"locate": "keyword1",
	"location": "keyword3",
	"log": "keyword3",
	"log10": "keyword3",
	"log10f": "keyword3",
	"log2": "keyword3",
	"logf": "keyword3",
	"loggamma": "keyword3",
	"loop": "keyword1",
	"low": "keyword3",
	"lower2": "keyword3",
	"lowercase": "keyword3",
	"m": "keyword2",
	"main": "keyword2",
	"max": "keyword3",
	"maxexp": "keyword3",
	"maxlength": "keyword3",
	"min": "keyword3",
	"minexp": "keyword3",
	"mod": "keyword3",
	"mpstr": "keyword3",
	"multiply": "keyword3",
	"name": "keyword1",
	"native": "keyword2",
	"new": "keyword3",
	"nocharg": "keyword2",
	"nochargraphic": "keyword2",
	"nodescriptor": "keyword2",
	"noexecops": "keyword2",
	"nomap": "keyword2",
	"nomapin": "keyword2",
	"nomapout": "keyword2",
	"nonasgn": "keyword2",
	"nonassignable": "keyword2",
	"nonconn": "keyword2",
	"nonconnected": "keyword2",
	"nonnative": "keyword2",
	"nonvar": "keyword2",
	"nonvarying": "keyword2",
	"normal": "keyword2",
	"null": "keyword3",
	"offestadd": "keyword3",
	"offestdiff": "keyword3",
	"offestsubtract": "keyword3",
	"offestvalue": "keyword3",
	"offset": "keyword2",
	"ofl": "keyword2",
	"omitted": "keyword3",
	"on": "keyword1",
	"onchar": "keyword3",
	"oncode": "keyword3",
	"oncondid": "keyword3",
	"oncondond": "keyword3",
	"oncount": "keyword3",
	"onfile": "keyword3",
	"ongsource": "keyword3",
	"onkey": "keyword3",
	"onloc": "keyword3",
	"onsource": "keyword3",
	"onsubcode": "keyword3",
	"onwchar": "keyword3",
	"onwsource": "keyword3",
	"open": "keyword1",
	"optional": "keyword2",
	"options": "keyword2",
	"optlink": "keyword2",
	"order": "keyword2",
	"ordinal": "keyword1",
	"ordinalname": "keyword3",
	"ordinalpred": "keyword3",
	"ordinalsucc": "keyword3",
	"other": "keyword1",
	"otherwise": "keyword1",
	"output": "keyword2",
	"overflow": "keyword2",
	"package": "keyword1",
	"packagename": "keyword3",
	"page": "keyword1",
	"pageno": "keyword3",
	"pagesize": "keyword2",
	"parameter": "keyword2",
	"pic": "keyword2",
	"picture": "keyword2",
	"places": "keyword3",
	"plianc": "keyword3",
	"pliascii": "keyword3",
	"plickpt": "keyword3",
	"plidelete": "keyword3",
	"plidump": "keyword3",
	"pliebcdic": "keyword3",
	"plifill": "keyword3",
	"plifree": "keyword3",
	"plimove": "keyword3",
	"pliover": "keyword3",
	"plirest": "keyword3",
	"pliretc": "keyword3",
	"pliretv": "keyword3",
	"plisaxa": "keyword3",
	"plisaxb": "keyword3",
	"plisrta": "keyword3",
	"plisrtb": "keyword3",
	"plisrtc": "keyword3",
	"plisrtd": "keyword3",
	"pointer": "keyword2",
	"pointeradd": "keyword3",
	"pointerdiff": "keyword3",
	"pointersubtract": "keyword3",
	"pointervalue": "keyword3",
	"poly": "keyword3",
	"pos": "keyword2",
	"position": "keyword2",
	"prec": "keyword2",
	"precision": "keyword2",
	"pred": "keyword3",
	"present": "keyword3",
	"print": "keyword2",
	"proc": "keyword1",
	"procedure": "keyword1",
	"procedurename": "keyword3",
	"procname": "keyword3",
	"prod": "keyword3",
	"ptr": "keyword2",
	"ptradd": "keyword3",
	"ptrdiff": "keyword3",
	"ptrsubtract": "keyword3",
	"ptrvalue": "keyword3",
	"put": "keyword1",
	"putenv": "keyword3",
	"radix": "keyword3",
	"raise": "keyword3",
	"random": "keyword3",
	"range": "keyword2",
	"rank": "keyword3",
	"read": "keyword1",
	"real": "keyword2",
	"record": "keyword2",
	"recursive": "keyword2",
	"red": "keyword2",
	"reducible": "keyword2",
	"reentrant": "keyword2",
	"refer": "keyword2",
	"release": "keyword1",
	"rem": "keyword3",
	"reorder": "keyword2",
	"repattern": "keyword3",
	"repeat": "keyword1",
	"reply": "keyword1",
	"reserved": "keyword2",
	"reserves": "keyword2",
	"resignal": "keyword1",
	"respec": "keyword3",
	"retcode": "keyword2",
	"return": "keyword1",
	"returns": "keyword2",
	"reverse": "keyword3",
	"revert": "keyword1",
	"rewrite": "keyword1",
	"right": "keyword3",
	"round": "keyword3",
	"samekey": "keyword3",
	"scale": "keyword3",
	"search": "keyword3",
	"searchr": "keyword3",
	"secs": "keyword3",
	"secstodate": "keyword3",
	"secstodays": "keyword3",
	"select": "keyword1",
	"seql": "keyword2",
	"sequential": "keyword2",
	"set": "keyword1",
	"sign": "keyword3",
	"signal": "keyword1",
	"signed": "keyword3",
	"sin": "keyword3",
	"sind": "keyword3",
	"sinf": "keyword3",
	"sinh": "keyword3",
	"size": "keyword3",
	"skip": "keyword1",
	"snap": "keyword1",
	"sourcefile": "keyword3",
	"sourceline": "keyword3",
	"sqrt": "keyword3",
	"sqrtf": "keyword3",
	"static": "keyword2",
	"stdcall": "keyword2",
	"stg": "keyword3",
	"stop": "keyword1",
	"storage": "keyword3",
	"stream": "keyword2",
	"strg": "keyword2",
	"string": "keyword3",
	"stringrange": "keyword2",
	"stringsize": "keyword2",
	"structure": "keyword1",
	"strz": "keyword2",
	"subrg": "keyword2",
	"subscriptrange": "keyword2",
	"substr": "keyword3",
	"subtract": "keyword3",
	"succ": "keyword3",
	"sum": "keyword3",
	"sysnull": "keyword3",
	"system": "keyword2",
	"tally": "keyword3",
	"tan": "keyword3",
	"tand": "keyword3",
	"tanf": "keyword3",
	"tanh": "keyword3",
	"task": "keyword2",
	"then": "keyword1",
	"thread": "keyword1",
	"threadid": "keyword3",
	"time": "keyword3",
	"tiny": "keyword3",
	"title": "keyword2",
	"to": "keyword1",
	"translate": "keyword3",
	"transmit": "keyword2",
	"trim": "keyword3",
	"trunc": "keyword3",
	"tstack": "keyword1",
	"type": "keyword3",
	"ufl": "keyword2",
	"unal": "keyword2",
	"unaligned": "keyword2",
	"unallocated": "keyword3",
	"unbuf": "keyword2",
	"unbuffered": "keyword2",
	"undefinedfile": "keyword2",
	"underflow": "keyword2",
	"undf": "keyword2",
	"union": "keyword2",
	"unlock": "keyword1",
	"unsigned": "keyword2",
	"unspec": "keyword3",
	"until": "keyword1",
	"update": "keyword2",
	"uppercase": "keyword3",
	"upthru": "keyword1",
	"valid": "keyword3",
	"validdate": "keyword3",
	"value": "keyword2",
	"var": "keyword2",
	"varglist": "keyword3",
	"vargsizer": "keyword3",
	"variable": "keyword2",
	"varying": "keyword2",
	"varyingz": "keyword2",
	"varz": "keyword2",
	"verify": "keyword3",
	"verifyr": "keyword3",
	"wait": "keyword1",
	"wchar": "keyword2",
	"wcharval": "keyword3",
	"weekday": "keyword3",
	"when": "keyword1",
	"whigh": "keyword3",
	"while": "keyword1",
	"widechar": "keyword2",
	"winmain": "keyword2",
	"wlow": "keyword3",
	"write": "keyword1",
	"wx": "keyword2",
	"x": "keyword2",
	"xn": "keyword2",
	"xu": "keyword2",
	"y4date": "keyword3",
	"y4julian": "keyword3",
	"y4year": "keyword3",
	"zdiv": "keyword2",
	"zerodivide": "keyword2",
}

# Dictionary of keywords dictionaries for pl1 mode.
keywordsDictDict = {
	"pl1_main": pl1_main_keywords_dict,
}

# Rules for pl1_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_eol_span_regexp(s, i, kind="keyword2", regexp="\\* *process", hash_char="*",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=False, at_whitespace_end=True, at_word_start=False, exclude_match=True)

def rule20(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule21(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"\"": [rule2,],
	"&": [rule12,],
	"'": [rule1,],
	"(": [rule18,rule20,],
	")": [rule17,],
	"*": [rule7,],
	"+": [rule5,],
	",": [rule15,],
	"-": [rule6,],
	".": [rule14,],
	"/": [rule0,rule8,],
	"0": [rule21,],
	"1": [rule21,],
	"2": [rule21,],
	"3": [rule21,],
	"4": [rule21,],
	"5": [rule21,],
	"6": [rule21,],
	"7": [rule21,],
	"8": [rule21,],
	"9": [rule21,],
	":": [rule19,],
	";": [rule16,],
	"<": [rule10,],
	"=": [rule4,],
	">": [rule9,],
	"@": [rule21,],
	"A": [rule21,],
	"B": [rule21,],
	"C": [rule21,],
	"D": [rule21,],
	"E": [rule21,],
	"F": [rule21,],
	"G": [rule21,],
	"H": [rule21,],
	"I": [rule21,],
	"J": [rule21,],
	"K": [rule21,],
	"L": [rule21,],
	"M": [rule21,],
	"N": [rule21,],
	"O": [rule21,],
	"P": [rule21,],
	"Q": [rule21,],
	"R": [rule21,],
	"S": [rule21,],
	"T": [rule21,],
	"U": [rule21,],
	"V": [rule21,],
	"W": [rule21,],
	"X": [rule21,],
	"Y": [rule21,],
	"Z": [rule21,],
	"\\": [rule3,],
	"^": [rule11,],
	"_": [rule21,],
	"a": [rule21,],
	"b": [rule21,],
	"c": [rule21,],
	"d": [rule21,],
	"e": [rule21,],
	"f": [rule21,],
	"g": [rule21,],
	"h": [rule21,],
	"i": [rule21,],
	"j": [rule21,],
	"k": [rule21,],
	"l": [rule21,],
	"m": [rule21,],
	"n": [rule21,],
	"o": [rule21,],
	"p": [rule21,],
	"q": [rule21,],
	"r": [rule21,],
	"s": [rule21,],
	"t": [rule21,],
	"u": [rule21,],
	"v": [rule21,],
	"w": [rule21,],
	"x": [rule21,],
	"y": [rule21,],
	"z": [rule21,],
	"|": [rule13,],
}

# x.rulesDictDict for pl1 mode.
rulesDictDict = {
	"pl1_main": rulesDict1,
}

# Import dict for pl1 mode.
importDict = {}

