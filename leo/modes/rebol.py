# Leo colorizer control file for rebol mode.
# This file is in the public domain.

# Properties for rebol mode.
properties = {
	"commentEnd": "}",
	"commentStart": "comment {",
	"indentCloseBrackets": "}])",
	"indentOpenBrackets": "{[(",
	"lineComment": ";",
	"lineUpClosingBracket": "true",
	"noWordSep": "_-",
	"wordBreakChars": ",+-=<>/?^&*",
}

# Attributes dict for rebol_main ruleset.
rebol_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "false",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for rebol mode.
attributesDictDict = {
	"rebol_main": rebol_main_attributes_dict,
}

# Keywords dict for rebol_main ruleset.
rebol_main_keywords_dict = {
	"?": "keyword2",
	"??": "keyword2",
	"Usage": "keyword1",
	"about": "keyword1",
	"abs": "keyword1",
	"absolute": "keyword1",
	"across": "keyword1",
	"action!": "keyword3",
	"action?": "keyword2",
	"add": "keyword1",
	"alert": "keyword1",
	"alias": "keyword1",
	"all": "keyword1",
	"alter": "keyword1",
	"and~": "keyword1",
	"any": "keyword1",
	"any-block!": "keyword3",
	"any-block?": "keyword2",
	"any-function!": "keyword3",
	"any-function?": "keyword2",
	"any-string!": "keyword3",
	"any-string?": "keyword2",
	"any-type!": "keyword3",
	"any-type?": "keyword2",
	"any-word!": "keyword3",
	"any-word?": "keyword2",
	"append": "keyword1",
	"arccosine": "keyword1",
	"arcsine": "keyword1",
	"arctangent": "keyword1",
	"array": "keyword1",
	"ask": "keyword1",
	"at": "keyword1",
	"back": "keyword1",
	"backcolor": "keyword1",
	"basic-syntax-header": "keyword1",
	"below": "keyword1",
	"binary!": "keyword3",
	"binary?": "keyword2",
	"bind": "keyword1",
	"bitset!": "keyword3",
	"bitset?": "keyword2",
	"block!": "keyword3",
	"block?": "keyword2",
	"boot-prefs": "keyword1",
	"break": "keyword1",
	"browse": "keyword1",
	"build-tag": "keyword1",
	"call": "keyword1",
	"caret-to-offset": "keyword1",
	"catch": "keyword1",
	"center-face": "keyword1",
	"change": "keyword1",
	"change-dir": "keyword1",
	"char!": "keyword3",
	"char?": "keyword2",
	"charset": "keyword1",
	"checksum": "keyword1",
	"choose": "keyword1",
	"clean-path": "keyword1",
	"clear": "keyword1",
	"clear-fields": "keyword1",
	"close": "keyword1",
	"comment": "keyword1",
	"complement": "keyword1",
	"compose": "keyword1",
	"compress": "keyword1",
	"confine": "keyword1",
	"confirm": "keyword1",
	"connected?": "keyword2",
	"context": "keyword1",
	"copy": "keyword1",
	"cosine": "keyword1",
	"cp": "keyword1",
	"crlf": "keyword1",
	"crypt-strength?": "keyword2",
	"cvs-date": "keyword1",
	"cvs-version": "keyword1",
	"datatype!": "keyword3",
	"datatype?": "keyword2",
	"date!": "keyword3",
	"date?": "keyword2",
	"debase": "keyword1",
	"decimal!": "keyword3",
	"decimal?": "keyword2",
	"decode-cgi": "keyword1",
	"decode-url": "keyword1",
	"decompress": "keyword1",
	"deflag-face": "keyword1",
	"dehex": "keyword1",
	"delete": "keyword1",
	"demo": "keyword1",
	"desktop": "keyword1",
	"detab": "keyword1",
	"dh-compute-key": "keyword1",
	"dh-generate-key": "keyword1",
	"dh-make-key": "keyword1",
	"difference": "keyword1",
	"dir?": "keyword2",
	"dirize": "keyword1",
	"disarm": "keyword1",
	"dispatch": "keyword1",
	"divide": "keyword1",
	"do": "keyword1",
	"do-boot": "keyword1",
	"do-events": "keyword1",
	"do-face": "keyword1",
	"do-face-alt": "keyword1",
	"does": "keyword1",
	"dsa-generate-key": "keyword1",
	"dsa-make-key": "keyword1",
	"dsa-make-signature": "keyword1",
	"dsa-verify-signature": "keyword1",
	"dump-face": "keyword1",
	"dump-pane": "keyword1",
	"echo": "keyword1",
	"editor": "keyword1",
	"either": "keyword1",
	"else": "keyword1",
	"email!": "keyword3",
	"email?": "keyword2",
	"emailer": "keyword1",
	"emit": "keyword1",
	"empty?": "keyword2",
	"enbase": "keyword1",
	"entab": "keyword1",
	"equal?": "keyword2",
	"error!": "keyword3",
	"error?": "keyword2",
	"even?": "keyword2",
	"event!": "keyword3",
	"event?": "keyword2",
	"exclude": "keyword1",
	"exists-key?": "keyword2",
	"exists-thru?": "keyword2",
	"exists?": "keyword2",
	"exit": "keyword1",
	"exp": "keyword1",
	"extract": "keyword1",
	"false": "literal2",
	"fifth": "keyword1",
	"file!": "keyword3",
	"file?": "keyword2",
	"find": "keyword1",
	"find-by-type": "keyword1",
	"find-key-face": "keyword1",
	"find-window": "keyword1",
	"first": "keyword1",
	"flag-face": "keyword1",
	"flag-face?": "keyword2",
	"flash": "keyword1",
	"focus": "keyword1",
	"font-fixed": "keyword1",
	"font-sans-serif": "keyword1",
	"font-serif": "keyword1",
	"for": "keyword1",
	"forall": "keyword1",
	"foreach": "keyword1",
	"forever": "keyword1",
	"form": "keyword1",
	"forskip": "keyword1",
	"found?": "keyword2",
	"fourth": "keyword1",
	"free": "keyword1",
	"func": "keyword1",
	"function": "keyword1",
	"function!": "keyword3",
	"function?": "keyword2",
	"get": "keyword1",
	"get-modes": "keyword1",
	"get-net-info": "keyword1",
	"get-style": "keyword1",
	"get-word!": "keyword3",
	"get-word?": "keyword2",
	"greater-or-equal?": "keyword2",
	"greater?": "keyword2",
	"guide": "keyword1",
	"halt": "keyword1",
	"has": "keyword1",
	"hash!": "keyword3",
	"hash?": "keyword2",
	"head": "keyword1",
	"head?": "keyword2",
	"help": "keyword1",
	"hide": "keyword1",
	"hide-popup": "keyword1",
	"if": "keyword1",
	"image!": "keyword3",
	"image?": "keyword2",
	"import-email": "keyword1",
	"in": "keyword1",
	"in-window?": "keyword2",
	"indent": "keyword1",
	"index?": "keyword2",
	"info?": "keyword2",
	"inform": "keyword1",
	"input": "keyword1",
	"input?": "keyword2",
	"insert": "keyword1",
	"insert-event-func": "keyword1",
	"inside?": "keyword2",
	"integer!": "keyword3",
	"integer?": "keyword2",
	"intersect": "keyword1",
	"issue!": "keyword3",
	"issue?": "keyword2",
	"join": "keyword1",
	"last": "keyword1",
	"launch": "keyword1",
	"launch-thru": "keyword1",
	"layout": "keyword1",
	"length?": "keyword2",
	"lesser-or-equal?": "keyword2",
	"lesser?": "keyword2",
	"library!": "keyword3",
	"library?": "keyword2",
	"license": "keyword1",
	"link-app?": "keyword2",
	"link?": "keyword2",
	"list!": "keyword3",
	"list-dir": "keyword1",
	"list-words": "keyword1",
	"list?": "keyword2",
	"lit-path!": "keyword3",
	"lit-path?": "keyword2",
	"lit-word!": "keyword3",
	"lit-word?": "keyword2",
	"load": "keyword1",
	"load-image": "keyword1",
	"load-prefs": "keyword1",
	"load-thru": "keyword1",
	"log-10": "keyword1",
	"log-2": "keyword1",
	"log-e": "keyword1",
	"logic!": "keyword3",
	"logic?": "keyword2",
	"loop": "keyword1",
	"lowercase": "keyword1",
	"make": "keyword1",
	"make-dir": "keyword1",
	"make-face": "keyword1",
	"max": "keyword1",
	"maximum": "keyword1",
	"maximum-of": "keyword1",
	"min": "keyword1",
	"minimum": "keyword1",
	"minimum-of": "keyword1",
	"modified?": "keyword2",
	"mold": "keyword1",
	"money!": "keyword3",
	"money?": "keyword2",
	"multiply": "keyword1",
	"native!": "keyword3",
	"native?": "keyword2",
	"negate": "keyword1",
	"negative?": "keyword2",
	"net-error": "keyword1",
	"next": "keyword1",
	"none": "keyword1",
	"none!": "keyword3",
	"none?": "keyword2",
	"not": "keyword1",
	"not-equal?": "keyword2",
	"now": "keyword1",
	"number!": "keyword3",
	"number?": "keyword2",
	"object!": "keyword3",
	"object?": "keyword2",
	"odd?": "keyword2",
	"offset-to-caret": "keyword1",
	"offset?": "keyword2",
	"op!": "keyword3",
	"op?": "keyword2",
	"open": "keyword1",
	"open-events": "keyword1",
	"origin": "keyword1",
	"or~": "keyword1",
	"outside?": "keyword2",
	"outstr": "keyword1",
	"pad": "keyword1",
	"pair!": "keyword3",
	"pair?": "keyword2",
	"paren!": "keyword3",
	"paren?": "keyword2",
	"parse": "keyword1",
	"parse-email-addrs": "keyword1",
	"parse-header": "keyword1",
	"parse-header-date": "keyword1",
	"parse-xml": "keyword1",
	"path!": "keyword3",
	"path-thru": "keyword1",
	"path?": "keyword2",
	"pick": "keyword1",
	"poke": "keyword1",
	"port!": "keyword3",
	"port?": "keyword2",
	"positive?": "keyword2",
	"power": "keyword1",
	"prin": "keyword1",
	"print": "keyword1",
	"probe": "keyword1",
	"protect": "keyword1",
	"protect-system": "keyword1",
	"q": "keyword1",
	"query": "keyword1",
	"quit": "keyword1",
	"random": "keyword1",
	"read": "keyword1",
	"read-io": "keyword1",
	"read-net": "keyword1",
	"read-thru": "keyword1",
	"reboot": "keyword1",
	"recycle": "keyword1",
	"reduce": "keyword1",
	"refinement!": "keyword3",
	"refinement?": "keyword2",
	"reform": "keyword1",
	"rejoin": "keyword1",
	"remainder": "keyword1",
	"remold": "keyword1",
	"remove": "keyword1",
	"remove-event-func": "keyword1",
	"rename": "keyword1",
	"repeat": "keyword1",
	"repend": "keyword1",
	"replace": "keyword1",
	"request": "keyword1",
	"request-color": "keyword1",
	"request-date": "keyword1",
	"request-download": "keyword1",
	"request-file": "keyword1",
	"request-list": "keyword1",
	"request-pass": "keyword1",
	"request-text": "keyword1",
	"resend": "keyword1",
	"return": "keyword1",
	"reverse": "keyword1",
	"routine!": "keyword3",
	"routine?": "keyword2",
	"rsa-encrypt": "keyword1",
	"rsa-generate-key": "keyword1",
	"rsa-make-key": "keyword1",
	"same?": "keyword2",
	"save": "keyword1",
	"save-prefs": "keyword1",
	"save-user": "keyword1",
	"screen-offset?": "keyword2",
	"script?": "keyword2",
	"scroll-para": "keyword1",
	"second": "keyword1",
	"secure": "keyword1",
	"select": "keyword1",
	"self": "literal2",
	"send": "keyword1",
	"sense": "keyword1",
	"series!": "keyword3",
	"series?": "keyword2",
	"set": "keyword1",
	"set-font": "keyword1",
	"set-modes": "keyword1",
	"set-net": "keyword1",
	"set-para": "keyword1",
	"set-path!": "keyword3",
	"set-path?": "keyword2",
	"set-style": "keyword1",
	"set-user": "keyword1",
	"set-user-name": "keyword1",
	"set-word!": "keyword3",
	"set-word?": "keyword2",
	"show": "keyword1",
	"show-popup": "keyword1",
	"sine": "keyword1",
	"size": "keyword1",
	"size-text": "keyword1",
	"size?": "keyword2",
	"skip": "keyword1",
	"sort": "keyword1",
	"source": "keyword1",
	"space": "keyword1",
	"span?": "keyword2",
	"split-path": "keyword1",
	"square-root": "keyword1",
	"strict-equal?": "keyword2",
	"strict-not-equal?": "keyword2",
	"string!": "keyword3",
	"string?": "keyword2",
	"struct!": "keyword3",
	"struct?": "keyword2",
	"style": "keyword1",
	"styles": "keyword1",
	"stylize": "keyword1",
	"subtract": "keyword1",
	"switch": "keyword1",
	"symbol!": "keyword3",
	"tabs": "keyword1",
	"tag!": "keyword3",
	"tag?": "keyword2",
	"tail": "keyword1",
	"tail?": "keyword2",
	"tangent": "keyword1",
	"textinfo": "keyword1",
	"third": "keyword1",
	"throw": "keyword1",
	"throw-on-error": "keyword1",
	"time!": "keyword3",
	"time?": "keyword2",
	"to": "keyword1",
	"to-binary": "keyword1",
	"to-bitset": "keyword1",
	"to-block": "keyword1",
	"to-char": "keyword1",
	"to-date": "keyword1",
	"to-decimal": "keyword1",
	"to-email": "keyword1",
	"to-event": "keyword1",
	"to-file": "keyword1",
	"to-get-word": "keyword1",
	"to-hash": "keyword1",
	"to-hex": "keyword1",
	"to-idate": "keyword1",
	"to-image": "keyword1",
	"to-integer": "keyword1",
	"to-issue": "keyword1",
	"to-list": "keyword1",
	"to-lit-path": "keyword1",
	"to-lit-word": "keyword1",
	"to-local-file": "keyword1",
	"to-logic": "keyword1",
	"to-money": "keyword1",
	"to-none": "keyword1",
	"to-pair": "keyword1",
	"to-paren": "keyword1",
	"to-path": "keyword1",
	"to-rebol-file": "keyword1",
	"to-refinement": "keyword1",
	"to-set-path": "keyword1",
	"to-set-word": "keyword1",
	"to-string": "keyword1",
	"to-tag": "keyword1",
	"to-time": "keyword1",
	"to-tuple": "keyword1",
	"to-url": "keyword1",
	"to-word": "keyword1",
	"trace": "keyword1",
	"trim": "keyword1",
	"true": "literal2",
	"try": "keyword1",
	"tuple!": "keyword3",
	"tuple?": "keyword2",
	"type?": "keyword2",
	"unfocus": "keyword1",
	"uninstall": "keyword1",
	"union": "keyword1",
	"unique": "keyword1",
	"unprotect": "keyword1",
	"unset": "keyword1",
	"unset!": "keyword3",
	"unset?": "keyword2",
	"until": "keyword1",
	"unview": "keyword1",
	"update": "keyword1",
	"upgrade": "keyword1",
	"uppercase": "keyword1",
	"url!": "keyword3",
	"url?": "keyword2",
	"use": "keyword1",
	"val": "keyword1",
	"value": "keyword1",
	"value?": "keyword2",
	"vbug": "keyword1",
	"view": "keyword1",
	"view-install": "keyword1",
	"view-prefs": "keyword1",
	"view?": "keyword2",
	"viewed?": "keyword2",
	"wait": "keyword1",
	"what": "keyword1",
	"what-dir": "keyword1",
	"while": "keyword1",
	"win-offset?": "keyword2",
	"within?": "keyword2",
	"word!": "keyword3",
	"word?": "keyword2",
	"write": "keyword1",
	"write-io": "keyword1",
	"write-user": "keyword1",
	"xor~": "keyword1",
	"zero?": "keyword2",
}

# Dictionary of keywords dictionaries for rebol mode.
keywordsDictDict = {
	"rebol_main": rebol_main_keywords_dict,
}

# Rules for rebol_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="comment {", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="comment{", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="{", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="literal2", pattern="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule15(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"\"": [rule2,],
	"'": [rule14,],
	"*": [rule11,],
	"+": [rule9,],
	"/": [rule10,],
	"0": [rule15,],
	"1": [rule15,],
	"2": [rule15,],
	"3": [rule15,],
	"4": [rule15,],
	"5": [rule15,],
	"6": [rule15,],
	"7": [rule15,],
	"8": [rule15,],
	"9": [rule15,],
	";": [rule4,],
	"<": [rule7,rule8,rule13,],
	"=": [rule5,],
	">": [rule6,rule12,],
	"@": [rule15,],
	"A": [rule15,],
	"B": [rule15,],
	"C": [rule15,],
	"D": [rule15,],
	"E": [rule15,],
	"F": [rule15,],
	"G": [rule15,],
	"H": [rule15,],
	"I": [rule15,],
	"J": [rule15,],
	"K": [rule15,],
	"L": [rule15,],
	"M": [rule15,],
	"N": [rule15,],
	"O": [rule15,],
	"P": [rule15,],
	"Q": [rule15,],
	"R": [rule15,],
	"S": [rule15,],
	"T": [rule15,],
	"U": [rule15,],
	"V": [rule15,],
	"W": [rule15,],
	"X": [rule15,],
	"Y": [rule15,],
	"Z": [rule15,],
	"_": [rule15,],
	"a": [rule15,],
	"b": [rule15,],
	"c": [rule0,rule1,rule15,],
	"d": [rule15,],
	"e": [rule15,],
	"f": [rule15,],
	"g": [rule15,],
	"h": [rule15,],
	"i": [rule15,],
	"j": [rule15,],
	"k": [rule15,],
	"l": [rule15,],
	"m": [rule15,],
	"n": [rule15,],
	"o": [rule15,],
	"p": [rule15,],
	"q": [rule15,],
	"r": [rule15,],
	"s": [rule15,],
	"t": [rule15,],
	"u": [rule15,],
	"v": [rule15,],
	"w": [rule15,],
	"x": [rule15,],
	"y": [rule15,],
	"z": [rule15,],
	"{": [rule3,],
}

# x.rulesDictDict for rebol mode.
rulesDictDict = {
	"rebol_main": rulesDict1,
}

# Import dict for rebol mode.
importDict = {}

