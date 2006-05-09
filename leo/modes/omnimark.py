# Leo colorizer control file for omnimark mode.
# This file is in the public domain.

# Properties for omnimark mode.
properties = {
	"indentNextLines": "\\s*((PROCESS|MARKUP|EXTERNAL|DOCUMENT|DTD|ELEMENT|FIND|TRANSLATE)((-|\\s).*|\\s*)|(DO|ELSE|REPEAT|MATCH|CASE|USING|GROUP|DEFINE|MACRO)(\\s+.*|\\s*))",
	"lineComment": ";",
	"noWordSep": ".-_",
}

# Keywords dict for omnimark_main ruleset.
omnimark_main_keywords_dict = {
	"#!": "keyword2",
	"#additional-info": "keyword2",
	"#appinfo": "keyword2",
	"#args": "keyword2",
	"#capacity": "keyword2",
	"#charset": "keyword2",
	"#class": "keyword2",
	"#command-line-names": "keyword2",
	"#console": "keyword2",
	"#current-input": "keyword2",
	"#current-output": "keyword2",
	"#data": "keyword2",
	"#doctype": "keyword2",
	"#document": "keyword2",
	"#dtd": "keyword2",
	"#empty": "keyword2",
	"#error": "keyword2",
	"#error-code": "keyword2",
	"#external-exception": "keyword2",
	"#file-name": "keyword2",
	"#first": "keyword2",
	"#group": "keyword2",
	"#implied": "keyword2",
	"#item": "keyword2",
	"#language-version": "keyword2",
	"#last": "keyword2",
	"#libpath": "keyword2",
	"#library": "keyword2",
	"#libvalue": "keyword2",
	"#line-number": "keyword2",
	"#main-input": "keyword2",
	"#main-output": "keyword2",
	"#markup-error-count": "keyword2",
	"#markup-error-total": "keyword2",
	"#markup-parser": "keyword2",
	"#markup-warning-count": "keyword2",
	"#markup-warning-total": "keyword2",
	"#message": "keyword2",
	"#none": "keyword2",
	"#output": "keyword2",
	"#platform-info": "keyword2",
	"#process-input": "keyword2",
	"#process-output": "keyword2",
	"#program-error": "keyword2",
	"#recovery-info": "keyword2",
	"#sgml": "keyword2",
	"#sgml-error-count": "keyword2",
	"#sgml-error-total": "keyword2",
	"#sgml-warning-count": "keyword2",
	"#sgml-warning-total": "keyword2",
	"#suppress": "keyword2",
	"#syntax": "keyword2",
	"abs": "operator",
	"activate": "keyword1",
	"active": "operator",
	"after": "keyword2",
	"again": "keyword1",
	"always": "keyword1",
	"ancestor": "keyword2",
	"and": "operator",
	"another": "keyword2",
	"any": "keyword3",
	"any-text": "keyword3",
	"arg": "keyword2",
	"as": "operator",
	"assert": "keyword1",
	"attached": "keyword2",
	"attribute": "keyword2",
	"attributes": "keyword2",
	"base": "operator",
	"bcd": "keyword2",
	"before": "keyword2",
	"binary": "operator",
	"binary-input": "keyword2",
	"binary-mode": "keyword2",
	"binary-output": "keyword2",
	"blank": "keyword3",
	"break-width": "keyword2",
	"buffer": "keyword2",
	"buffered": "keyword2",
	"by": "keyword2",
	"case": "keyword1",
	"catch": "keyword1",
	"catchable": "keyword2",
	"cdata": "keyword3",
	"cdata-entity": "keyword2",
	"ceiling": "operator",
	"children": "keyword2",
	"clear": "keyword1",
	"close": "keyword1",
	"closed": "keyword2",
	"compiled-date": "operator",
	"complement": "operator",
	"conref": "keyword2",
	"content": "keyword2",
	"content-end": "keyword3",
	"content-start": "keyword3",
	"context-translate": "keyword2",
	"copy": "keyword1",
	"copy-clear": "keyword1",
	"counter": "keyword2",
	"created": "keyword2",
	"creating": "operator",
	"creator": "operator",
	"cross-translate": "keyword2",
	"current": "keyword2",
	"data-attribute": "keyword2",
	"data-attributes": "keyword2",
	"data-content": "keyword2",
	"data-letters": "keyword2",
	"date": "operator",
	"deactivate": "keyword1",
	"declare": "keyword2",
	"declared-conref": "keyword2",
	"declared-current": "keyword2",
	"declared-defaulted": "keyword2",
	"declared-fixed": "keyword2",
	"declared-implied": "keyword2",
	"declared-required": "keyword2",
	"decrement": "keyword1",
	"default-entity": "keyword2",
	"defaulted": "keyword2",
	"defaulting": "keyword2",
	"define": "keyword2",
	"delimiter": "keyword2",
	"difference": "operator",
	"digit": "keyword3",
	"directory": "keyword2",
	"discard": "keyword1",
	"divide": "operator",
	"do": "keyword1",
	"doctype": "keyword2",
	"document": "keyword2",
	"document-element": "keyword2",
	"document-end": "keyword2",
	"document-start": "keyword2",
	"domain-free": "keyword2",
	"done": "keyword1",
	"down-translate": "keyword2",
	"drop": "operator",
	"dtd": "keyword2",
	"dtd-end": "keyword2",
	"dtd-start": "keyword2",
	"dtds": "keyword2",
	"element": "keyword2",
	"elements": "keyword2",
	"else": "keyword1",
	"elsewhere": "keyword2",
	"empty": "keyword2",
	"entities": "keyword2",
	"entity": "keyword2",
	"epilog-start": "keyword2",
	"equal": "operator",
	"equals": "operator",
	"escape": "keyword2",
	"except": "keyword1",
	"exists": "operator",
	"exit": "keyword1",
	"external": "keyword2",
	"external-data-entity": "keyword2",
	"external-entity": "keyword2",
	"external-function": "keyword2",
	"external-output-function": "keyword2",
	"external-text-entity": "keyword2",
	"false": "keyword2",
	"file": "operator",
	"find": "keyword2",
	"find-end": "keyword2",
	"find-start": "keyword2",
	"floor": "operator",
	"flush": "keyword1",
	"for": "keyword1",
	"format": "keyword1",
	"function": "keyword2",
	"function-library": "keyword2",
	"general": "keyword2",
	"global": "keyword2",
	"greater-equal": "operator",
	"greater-than": "operator",
	"group": "keyword2",
	"groups": "keyword2",
	"halt": "keyword1",
	"halt-everything": "keyword1",
	"has": "operator",
	"hasnt": "operator",
	"heralded-names": "keyword2",
	"id": "keyword2",
	"id-checking": "keyword2",
	"idref": "keyword2",
	"idrefs": "keyword2",
	"ignore": "keyword2",
	"implied": "keyword2",
	"in": "keyword2",
	"in-library": "keyword2",
	"include": "keyword2",
	"include-end": "keyword2",
	"include-guard": "keyword2",
	"include-start": "keyword2",
	"inclusion": "keyword2",
	"increment": "keyword1",
	"initial": "keyword2",
	"initial-size": "keyword2",
	"input": "keyword1",
	"insertion-break": "keyword2",
	"instance": "keyword2",
	"integer": "keyword2",
	"internal": "keyword2",
	"invalid-data": "keyword2",
	"is": "operator",
	"isnt": "operator",
	"item": "operator",
	"join": "keyword1",
	"key": "operator",
	"keyed": "keyword2",
	"last": "operator",
	"lastmost": "operator",
	"lc": "keyword3",
	"length": "operator",
	"less-equal": "operator",
	"less-than": "operator",
	"letter": "keyword3",
	"letters": "keyword2",
	"library": "keyword2",
	"line-end": "keyword3",
	"line-start": "keyword3",
	"literal": "operator",
	"ln": "operator",
	"local": "keyword2",
	"log": "keyword1",
	"log10": "operator",
	"lookahead": "operator",
	"macro": "keyword2",
	"macro-end": "keyword2",
	"marked-section": "keyword2",
	"markup-comment": "keyword2",
	"markup-error": "keyword2",
	"markup-parser": "keyword2",
	"markup-wrapper": "keyword2",
	"mask": "operator",
	"match": "keyword1",
	"matches": "operator",
	"minus": "operator",
	"mixed": "keyword2",
	"modifiable": "keyword2",
	"modulo": "operator",
	"name": "operator",
	"name-letters": "keyword2",
	"namecase": "keyword2",
	"named": "keyword2",
	"names": "keyword2",
	"ndata-entity": "keyword2",
	"negate": "operator",
	"nested-referents": "keyword2",
	"new": "keyword1",
	"newline": "keyword2",
	"next": "keyword1",
	"nmtoken": "keyword2",
	"nmtokens": "keyword2",
	"no": "keyword2",
	"no-default-io": "keyword2",
	"non-cdata": "keyword3",
	"non-implied": "keyword2",
	"non-sdata": "keyword3",
	"not": "operator",
	"not-reached": "keyword1",
	"notation": "keyword2",
	"null": "keyword3",
	"number": "keyword2",
	"number-of": "operator",
	"numbers": "keyword2",
	"nutoken": "keyword2",
	"nutokens": "keyword2",
	"occurrence": "operator",
	"of": "operator",
	"opaque": "keyword2",
	"open": "keyword1",
	"optional": "keyword2",
	"or": "operator",
	"output": "keyword1",
	"output-to": "keyword1",
	"over": "keyword1",
	"parameter": "keyword2",
	"parent": "keyword2",
	"past": "keyword2",
	"pattern": "keyword2",
	"pcdata": "keyword3",
	"plus": "keyword2",
	"preparent": "keyword2",
	"previous": "keyword2",
	"process": "keyword2",
	"process-end": "keyword2",
	"process-start": "keyword2",
	"processing-instruction": "keyword2",
	"prolog-end": "keyword2",
	"prolog-in-error": "keyword2",
	"proper": "keyword2",
	"public": "keyword2",
	"put": "keyword1",
	"rcdata": "keyword3",
	"read-only": "keyword2",
	"readable": "keyword2",
	"referent": "keyword2",
	"referents": "keyword2",
	"referents-allowed": "keyword2",
	"referents-displayed": "keyword2",
	"referents-not-allowed": "keyword2",
	"remainder": "keyword2",
	"remove": "keyword1",
	"reopen": "keyword1",
	"repeat": "keyword1",
	"repeated": "keyword2",
	"replacement-break": "keyword2",
	"reset": "keyword1",
	"rethrow": "keyword1",
	"return": "keyword1",
	"reversed": "keyword2",
	"round": "operator",
	"save": "keyword1",
	"save-clear": "keyword1",
	"scan": "keyword1",
	"sdata": "keyword3",
	"sdata-entity": "keyword2",
	"select": "keyword1",
	"set": "keyword1",
	"sgml": "keyword1",
	"sgml-comment": "keyword2",
	"sgml-declaration-end": "keyword2",
	"sgml-dtd": "keyword2",
	"sgml-dtds": "keyword2",
	"sgml-error": "keyword2",
	"sgml-in": "keyword1",
	"sgml-out": "keyword1",
	"sgml-parse": "keyword1",
	"sgml-parser": "keyword1",
	"shift": "operator",
	"silent-referent": "keyword2",
	"size": "keyword2",
	"skip": "keyword1",
	"source": "keyword2",
	"space": "keyword3",
	"specified": "keyword2",
	"sqrt": "operator",
	"status": "operator",
	"stream": "keyword2",
	"subdoc-entity": "keyword2",
	"subdocument": "keyword2",
	"subdocuments": "keyword2",
	"subelement": "keyword2",
	"submit": "keyword1",
	"succeed": "keyword1",
	"suppress": "keyword1",
	"switch": "keyword2",
	"symbol": "keyword2",
	"system": "keyword2",
	"system-call": "keyword1",
	"take": "operator",
	"test-system": "keyword1",
	"text": "keyword3",
	"text-mode": "keyword2",
	"this": "operator",
	"throw": "keyword1",
	"thrown": "keyword2",
	"times": "keyword2",
	"to": "keyword1",
	"token": "keyword2",
	"translate": "keyword2",
	"true": "keyword2",
	"truncate": "operator",
	"uc": "keyword3",
	"ul": "operator",
	"unanchored": "operator",
	"unattached": "keyword2",
	"unbuffered": "keyword2",
	"union": "operator",
	"unless": "keyword1",
	"up-translate": "keyword2",
	"usemap": "operator",
	"using": "keyword1",
	"value": "keyword2",
	"value-end": "keyword3",
	"value-start": "keyword3",
	"valued": "keyword2",
	"variable": "keyword2",
	"when": "keyword1",
	"white-space": "keyword3",
	"with": "operator",
	"word-end": "keyword3",
	"word-start": "keyword3",
	"writable": "keyword2",
	"xml": "keyword2",
	"xml-dtd": "keyword2",
	"xml-dtds": "keyword2",
	"xml-parse": "keyword1",
	"yes": "keyword2",
}

# Dictionary of keywords dictionaries for omnimark mode.
keywordsDictDict = {
	"omnimark_main": omnimark_main_keywords_dict,
}

# Rules for omnimark_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="invalid", begin="\"((?!$)[^\"])*$", end="$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="invalid", begin="'((?!$)[^'])*$", end="$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="?",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule20,],
	"\"": [rule2,rule3,],
	"#": [rule0,],
	"$": [rule15,],
	"%": [rule16,],
	"&": [rule6,],
	"'": [rule4,rule5,],
	"*": [rule18,],
	"+": [rule8,],
	"/": [rule10,],
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
	";": [rule1,],
	"<": [rule11,],
	"=": [rule9,],
	">": [rule12,],
	"?": [rule19,],
	"@": [rule14,rule21,],
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
	"^": [rule17,],
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
	"|": [rule7,],
	"~": [rule13,],
}

# x.rulesDictDict for omnimark mode.
rulesDictDict = {
	"omnimark_main": rulesDict1,
}

# Import dict for omnimark mode.
importDict = {}

