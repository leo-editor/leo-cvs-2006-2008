# Leo colorizer control file for netrexx mode.
# This file is in the public domain.

# Properties for netrexx mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"indentNextLines": "\\s*(if|loop|do|else|select|otherwise|catch|finally|class|method|properties)(.*)",
	"lineComment": "--",
	"wordBreakChars": ",+-=<>/?^&*",
}

# Attributes dict for netrexx_main ruleset.
netrexx_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for netrexx mode.
attributesDictDict = {
	"netrexx_main": netrexx_main_attributes_dict,
}

# Keywords dict for netrexx_main ruleset.
netrexx_main_keywords_dict = {
	"ArithmeticException": "markup",
	"ArrayIndexOutOfBoundsException": "markup",
	"ArrayList": "label",
	"ArrayStoreException": "markup",
	"BadArgumentException": "markup",
	"BadColumnException": "markup",
	"BadNumericException": "markup",
	"BigDecimal": "label",
	"BigInteger": "label",
	"Boolean": "label",
	"BufferedInputStream": "label",
	"BufferedOutputStream": "label",
	"BufferedReader": "label",
	"BufferedWriter": "label",
	"Byte": "label",
	"ByteArrayInputStream": "label",
	"ByteArrayOutputStream": "label",
	"Calendar": "label",
	"CharArrayReader": "label",
	"CharArrayWriter": "label",
	"CharConversionException": "markup",
	"Character": "label",
	"ClassCastException": "markup",
	"ClassNotFoundException": "markup",
	"CloneNotSupportedException": "markup",
	"ConcurrentModificationException": "label",
	"DataInputStream": "label",
	"DataOutputStream": "label",
	"Date": "label",
	"DivideException": "markup",
	"Double": "label",
	"EOFException": "markup",
	"Exception": "markup",
	"ExponentOverflowException": "markup",
	"File": "label",
	"FileDescriptor": "label",
	"FileInputStream": "label",
	"FileNotFoundException": "markup",
	"FileOutputStream": "label",
	"FilePermission": "label",
	"FileReader": "label",
	"FileWriter": "label",
	"FilterInputStream": "label",
	"FilterOutputStream": "label",
	"FilterReader": "label",
	"FilterWriter": "label",
	"Float": "label",
	"HashMap": "label",
	"HashSet": "label",
	"Hashtable": "label",
	"IOException": "markup",
	"IllegalAccessException": "markup",
	"IllegalArgumentException": "markup",
	"IllegalMonitorStateException": "markup",
	"IllegalStateException": "markup",
	"IllegalThreadStateException": "markup",
	"IndexOutOfBoundsException": "markup",
	"InputStream": "label",
	"InputStreamReader": "label",
	"InstantiationException": "markup",
	"Integer": "label",
	"InterruptedException": "markup",
	"InterruptedIOException": "markup",
	"InvalidClassException": "markup",
	"InvalidObjectException": "markup",
	"LineNumberInputStream": "label",
	"LineNumberReader": "label",
	"LinkedHashMap": "label",
	"LinkedHashSet": "label",
	"Long": "label",
	"NegativeArraySizeException": "markup",
	"NoOtherwiseException": "markup",
	"NoSuchFieldException": "markup",
	"NoSuchMethodException": "markup",
	"NotActiveException": "markup",
	"NotCharacterException": "markup",
	"NotLogicException": "markup",
	"NotSerializableException": "markup",
	"NullPointerException": "markup",
	"Number": "label",
	"NumberFormatException": "markup",
	"Object": "label",
	"ObjectInputStream": "label",
	"ObjectOutputStream": "label",
	"ObjectStreamException": "markup",
	"OptionalDataException": "markup",
	"OutputStream": "label",
	"OutputStreamWriter": "label",
	"PipedInputStream": "label",
	"PipedOutputStream": "label",
	"PipedReader": "label",
	"PipedWriter": "label",
	"PrintStream": "label",
	"PrintWriter": "label",
	"PushbackInputStream": "label",
	"PushbackReader": "label",
	"RandomAccessFile": "label",
	"Reader": "label",
	"RemoteException": "markup",
	"Rexx": "label",
	"RuntimeException": "markup",
	"SecurityException": "markup",
	"SequenceInputStream": "label",
	"Short": "label",
	"StreamCorruptedException": "markup",
	"StreamTokenizer": "label",
	"String": "label",
	"StringBuffer": "label",
	"StringBufferInputStream": "label",
	"StringIndexOutOfBoundsException": "markup",
	"StringReader": "label",
	"StringWriter": "label",
	"SyncFailedException": "markup",
	"TreeMap": "label",
	"TreeSet": "label",
	"UTFDataFormatException": "markup",
	"UnsupportedEncodingException": "markup",
	"UnsupportedOperationException": "markup",
	"Vector": "label",
	"WriteAbortedException": "markup",
	"Writer": "label",
	"abbrev": "function",
	"abs": "function",
	"abstract": "keyword1",
	"adapter": "keyword1",
	"all": "keyword3",
	"ask": "keyword3",
	"b2x": "function",
	"binary": "literal2",
	"boolean": "label",
	"by": "keyword2",
	"byte": "label",
	"c2d": "function",
	"c2x": "function",
	"case": "keyword2",
	"catch": "keyword2",
	"center": "function",
	"centre": "function",
	"changestr": "function",
	"char": "label",
	"charAt": "function",
	"class": "keyword1",
	"comments": "literal2",
	"compact": "literal2",
	"compare": "function",
	"console": "literal2",
	"constant": "keyword1",
	"copies": "function",
	"copyIndexed": "function",
	"countstr": "function",
	"crossref": "literal2",
	"d2X": "function",
	"d2c": "function",
	"datatype": "function",
	"decimal": "literal2",
	"delstr": "function",
	"delword": "function",
	"dependent": "keyword1",
	"deprecated": "keyword1",
	"diag": "literal2",
	"digits": "keyword3",
	"do": "keyword2",
	"double": "label",
	"else": "keyword2",
	"end": "keyword2",
	"engineering": "keyword3",
	"equals": "function",
	"exists": "function",
	"exit": "keyword2",
	"explicit": "literal2",
	"extends": "keyword1",
	"final": "keyword1",
	"finally": "keyword2",
	"float": "label",
	"for": "keyword2",
	"forever": "keyword2",
	"form": "keyword3",
	"format": "literal2",
	"hashCode": "function",
	"if": "keyword2",
	"implements": "keyword1",
	"import": "keyword3",
	"indirect": "keyword1",
	"inheritable": "keyword1",
	"insert": "function",
	"int": "label",
	"interface": "keyword1",
	"iterate": "keyword2",
	"java": "literal2",
	"keep": "literal2",
	"label": "keyword2",
	"lastpos": "function",
	"leave": "keyword2",
	"left": "function",
	"length": "function",
	"logo": "literal2",
	"long": "label",
	"loop": "keyword2",
	"lower": "function",
	"max": "function",
	"method": "keyword1",
	"methods": "keyword3",
	"min": "function",
	"native": "keyword1",
	"nobinary": "literal2",
	"nocomments": "literal2",
	"nocompact": "literal2",
	"noconsole": "literal2",
	"nocrossref": "literal2",
	"nodecimal": "literal2",
	"nodiag": "literal2",
	"noexplicit": "literal2",
	"noformat": "literal2",
	"nojava": "literal2",
	"nokeep": "literal2",
	"nologo": "literal2",
	"nop": "function",
	"noreplace": "literal2",
	"nosavelog": "literal2",
	"nosourcedir": "literal2",
	"nostrictargs": "literal2",
	"nostrictassign": "literal2",
	"nostrictcase": "literal2",
	"nostrictimport": "literal2",
	"nostrictprops": "literal2",
	"nostrictsignal": "literal2",
	"nosymbols": "literal2",
	"notrace": "literal2",
	"noutf8": "literal2",
	"noverbose": "literal2",
	"null": "keyword3",
	"numeric": "keyword3",
	"off": "keyword3",
	"options": "literal2",
	"otherwise": "keyword2",
	"over": "keyword2",
	"overlay": "function",
	"package": "keyword3",
	"parent": "keyword3",
	"parse": "function",
	"pos": "function",
	"private": "keyword1",
	"properties": "keyword1",
	"protect": "keyword2",
	"public": "keyword1",
	"replace": "literal2",
	"results": "keyword3",
	"return": "keyword2",
	"returns": "keyword1",
	"reverse": "function",
	"right": "function",
	"savelog": "literal2",
	"say": "function",
	"scientific": "keyword3",
	"select": "keyword2",
	"sequence": "function",
	"short": "label",
	"sign": "function",
	"signal": "keyword2",
	"signals": "keyword1",
	"source": "keyword3",
	"sourcedir": "literal2",
	"sourceline": "keyword3",
	"space": "function",
	"static": "keyword1",
	"strictargs": "literal2",
	"strictassign": "literal2",
	"strictcase": "literal2",
	"strictimport": "literal2",
	"strictprops": "literal2",
	"strictsignal": "literal2",
	"strip": "function",
	"substr": "function",
	"subword": "function",
	"super": "keyword3",
	"symbols": "literal2",
	"then": "keyword2",
	"this": "keyword3",
	"to": "keyword2",
	"toCharArray": "function",
	"toString": "function",
	"toboolean": "function",
	"tobyte": "function",
	"tochar": "function",
	"todouble": "function",
	"tofloat": "function",
	"toint": "function",
	"tolong": "function",
	"toshort": "function",
	"trace": "keyword3",
	"transient": "keyword1",
	"translate": "function",
	"trunc": "function",
	"until": "keyword2",
	"unused": "keyword1",
	"upper": "function",
	"uses": "keyword1",
	"utf8": "literal2",
	"var": "keyword3",
	"verbose": "literal2",
	"verbose0": "literal2",
	"verbose1": "literal2",
	"verbose2": "literal2",
	"verbose3": "literal2",
	"verbose4": "literal2",
	"verbose5": "literal2",
	"verify": "function",
	"version": "keyword3",
	"volatile": "keyword1",
	"when": "keyword2",
	"while": "keyword2",
	"word": "function",
	"wordindex": "function",
	"wordlength": "function",
	"wordpos": "function",
	"words": "function",
	"x2b": "function",
	"x2c": "function",
	"x2d": "function",
}

# Dictionary of keywords dictionaries for netrexx mode.
keywordsDictDict = {
	"netrexx_main": netrexx_main_keywords_dict,
}

# Rules for netrexx_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment2", begin="/**", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="java::JAVADOC",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

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
    return colorer.match_seq(s, i, kind="null", seq=".*",
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
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule6,],
	"\"": [rule2,],
	"%": [rule16,],
	"&": [rule17,],
	"'": [rule3,],
	"*": [rule13,],
	"+": [rule9,],
	"-": [rule4,rule10,],
	".": [rule12,],
	"/": [rule0,rule1,rule11,],
	"0": [rule23,],
	"1": [rule23,],
	"2": [rule23,],
	"3": [rule23,],
	"4": [rule23,],
	"5": [rule23,],
	"6": [rule23,],
	"7": [rule23,],
	"8": [rule23,],
	"9": [rule23,],
	"<": [rule8,rule15,],
	"=": [rule5,],
	">": [rule7,rule14,],
	"@": [rule23,],
	"A": [rule23,],
	"B": [rule23,],
	"C": [rule23,],
	"D": [rule23,],
	"E": [rule23,],
	"F": [rule23,],
	"G": [rule23,],
	"H": [rule23,],
	"I": [rule23,],
	"J": [rule23,],
	"K": [rule23,],
	"L": [rule23,],
	"M": [rule23,],
	"N": [rule23,],
	"O": [rule23,],
	"P": [rule23,],
	"Q": [rule23,],
	"R": [rule23,],
	"S": [rule23,],
	"T": [rule23,],
	"U": [rule23,],
	"V": [rule23,],
	"W": [rule23,],
	"X": [rule23,],
	"Y": [rule23,],
	"Z": [rule23,],
	"^": [rule19,],
	"_": [rule23,],
	"a": [rule23,],
	"b": [rule23,],
	"c": [rule23,],
	"d": [rule23,],
	"e": [rule23,],
	"f": [rule23,],
	"g": [rule23,],
	"h": [rule23,],
	"i": [rule23,],
	"j": [rule23,],
	"k": [rule23,],
	"l": [rule23,],
	"m": [rule23,],
	"n": [rule23,],
	"o": [rule23,],
	"p": [rule23,],
	"q": [rule23,],
	"r": [rule23,],
	"s": [rule23,],
	"t": [rule23,],
	"u": [rule23,],
	"v": [rule23,],
	"w": [rule23,],
	"x": [rule23,],
	"y": [rule23,],
	"z": [rule23,],
	"{": [rule22,],
	"|": [rule18,],
	"}": [rule21,],
	"~": [rule20,],
}

# x.rulesDictDict for netrexx mode.
rulesDictDict = {
	"netrexx_main": rulesDict1,
}

# Import dict for netrexx mode.
importDict = {}

