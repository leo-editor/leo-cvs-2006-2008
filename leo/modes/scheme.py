# Leo colorizer control file for scheme mode.

# Properties for scheme mode.
properties = {
	"commentEnd": "|#",
	"commentStart": "#|",
	"indentCloseBrackets": ")",
	"indentOpenBrackets": "(",
	"lineComment": ";",
	"lineUpClosingBracket": "false",
	"noWordSep": "_-+?:*/!",
}

# Keywords dict for scheme_main ruleset.
scheme_main_keywords_dict = {
	"#f": "literal2",
	"#t": "literal2",
	"<": "keyword3",
	"=?": "keyword3",
	">": "keyword3",
	"?": "keyword3",
	"abs": "keyword2",
	"acos": "keyword2",
	"and": "keyword1",
	"angle": "keyword2",
	"append": "keyword2",
	"apply": "keyword2",
	"asin": "keyword2",
	"assoc": "keyword2",
	"assq": "keyword2",
	"assv": "keyword2",
	"atan": "keyword2",
	"begin": "keyword1",
	"boolean?": "keyword3",
	"caaar": "keyword2",
	"caadr": "keyword2",
	"caar": "keyword2",
	"cadar": "keyword2",
	"caddr": "keyword2",
	"cadr": "keyword2",
	"call-with-current-continuation": "keyword2",
	"call-with-input-file": "keyword2",
	"call-with-output-file": "keyword2",
	"call-with-values": "keyword2",
	"call/cc": "keyword2",
	"car": "keyword2",
	"case": "keyword1",
	"catch": "keyword2",
	"cdaar": "keyword2",
	"cdadr": "keyword2",
	"cdar": "keyword2",
	"cddar": "keyword2",
	"cdddr": "keyword2",
	"cddr": "keyword2",
	"cdr": "keyword2",
	"ceiling": "keyword2",
	"char": "keyword3",
	"char-": "keyword2",
	"char-alphabetic?": "keyword3",
	"char-ci": "keyword3",
	"char-ci=?": "keyword3",
	"char-downcase": "keyword2",
	"char-lower-case?": "keyword3",
	"char-numeric?": "keyword3",
	"char-ready?": "keyword3",
	"char-upcase": "keyword2",
	"char-upper-case?": "keyword3",
	"char-whitespace?": "keyword3",
	"char=?": "keyword3",
	"char?": "keyword3",
	"close-input-port": "keyword2",
	"close-output-port": "keyword2",
	"complex?": "keyword3",
	"cond": "keyword1",
	"cond-expand": "keyword1",
	"cons": "keyword2",
	"cos": "keyword2",
	"current-input-port": "keyword2",
	"current-output-port": "keyword2",
	"define": "keyword1",
	"define-macro": "keyword1",
	"delay": "keyword1",
	"delete-file": "keyword2",
	"display": "keyword2",
	"do": "keyword1",
	"dynamic-wind": "keyword2",
	"else": "keyword1",
	"eof-object?": "keyword3",
	"eq?": "keyword3",
	"equal?": "keyword3",
	"eqv?": "keyword3",
	"eval": "keyword2",
	"even?": "keyword3",
	"exact-": "keyword2",
	"exact?": "keyword3",
	"exit": "keyword2",
	"exp": "keyword2",
	"expt": "keyword2",
	"file-exists?": "keyword3",
	"file-or-directory-modify-seconds": "keyword2",
	"floor": "keyword2",
	"fluid-let": "keyword1",
	"for-each": "keyword2",
	"force": "keyword2",
	"gcd": "keyword2",
	"gensym": "keyword2",
	"get-output-string": "keyword2",
	"getenv": "keyword2",
	"if": "keyword1",
	"imag-part": "keyword2",
	"inexact": "keyword2",
	"inexact?": "keyword3",
	"input-port?": "keyword3",
	"integer": "keyword2",
	"integer-": "keyword2",
	"integer?": "keyword3",
	"lambda": "keyword1",
	"lcm": "keyword2",
	"length": "keyword2",
	"let": "keyword1",
	"let*": "keyword1",
	"letrec": "keyword1",
	"list": "keyword2",
	"list-": "keyword2",
	"list-ref": "keyword2",
	"list-tail": "keyword2",
	"list?": "keyword3",
	"load": "keyword2",
	"log": "keyword2",
	"magnitude": "keyword2",
	"make-polar": "keyword2",
	"make-rectangular": "keyword2",
	"make-string": "keyword2",
	"make-vector": "keyword2",
	"map": "keyword2",
	"max": "keyword2",
	"member": "keyword2",
	"memq": "keyword2",
	"memv": "keyword2",
	"min": "keyword2",
	"modulo": "keyword2",
	"negative?": "keyword3",
	"newline": "keyword2",
	"nil": "keyword2",
	"not": "keyword2",
	"null?": "keyword3",
	"number": "keyword2",
	"number-": "keyword2",
	"number?": "keyword3",
	"odd?": "keyword3",
	"open-input-file": "keyword2",
	"open-input-string": "keyword2",
	"open-output-file": "keyword2",
	"open-output-string": "keyword2",
	"or": "keyword1",
	"output-port?": "keyword3",
	"pair?": "keyword3",
	"peek-char": "keyword2",
	"port?": "keyword3",
	"positive?": "keyword3",
	"procedure?": "keyword3",
	"quasiquote": "keyword1",
	"quote": "keyword1",
	"quotient": "keyword2",
	"rational?": "keyword3",
	"read": "keyword2",
	"read-char": "keyword2",
	"read-line": "keyword2",
	"real-part": "keyword2",
	"real?": "keyword3",
	"remainder": "keyword2",
	"reverse": "keyword2",
	"reverse!": "keyword2",
	"round": "keyword2",
	"set!": "keyword1",
	"set-car!": "keyword2",
	"set-cdr!": "keyword2",
	"sin": "keyword2",
	"sqrt": "keyword2",
	"string": "keyword3",
	"string-": "keyword2",
	"string-append": "keyword2",
	"string-ci": "keyword3",
	"string-ci=?": "keyword3",
	"string-copy": "keyword2",
	"string-fill!": "keyword2",
	"string-length": "keyword2",
	"string-ref": "keyword2",
	"string-set!": "keyword2",
	"string=?": "keyword3",
	"string?": "keyword3",
	"substring": "keyword2",
	"symbol": "keyword2",
	"symbol-": "keyword2",
	"symbol?": "keyword3",
	"system": "keyword2",
	"tan": "keyword2",
	"truncate": "keyword2",
	"values": "keyword2",
	"vector": "keyword2",
	"vector-": "keyword2",
	"vector-fill!": "keyword2",
	"vector-length": "keyword2",
	"vector-ref": "keyword2",
	"vector-set!": "keyword2",
	"vector?": "keyword3",
	"with-input-from-file": "keyword2",
	"with-output-to-file": "keyword2",
	"write": "keyword2",
	"write-char": "keyword2",
	"zero?": "keyword3",
}

# Dictionary of keywords dictionaries for scheme mode.
keywordsDictDict = {
	"scheme_main": scheme_main_keywords_dict,
}

# Rules for scheme_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="#|", end="|#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq="'(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="literal1", pattern="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="literal1", pattern="#\\",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="literal1", pattern="#b",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule5(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="literal1", pattern="#d",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule6(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="literal1", pattern="#o",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule7(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="literal1", pattern="#x",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule8(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule9(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule10(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"\"": [rule9,],
	"#": [rule0,rule3,rule4,rule5,rule6,rule7,],
	"'": [rule1,rule2,],
	"0": [rule10,],
	"1": [rule10,],
	"2": [rule10,],
	"3": [rule10,],
	"4": [rule10,],
	"5": [rule10,],
	"6": [rule10,],
	"7": [rule10,],
	"8": [rule10,],
	"9": [rule10,],
	";": [rule8,],
	"@": [rule10,],
	"A": [rule10,],
	"B": [rule10,],
	"C": [rule10,],
	"D": [rule10,],
	"E": [rule10,],
	"F": [rule10,],
	"G": [rule10,],
	"H": [rule10,],
	"I": [rule10,],
	"J": [rule10,],
	"K": [rule10,],
	"L": [rule10,],
	"M": [rule10,],
	"N": [rule10,],
	"O": [rule10,],
	"P": [rule10,],
	"Q": [rule10,],
	"R": [rule10,],
	"S": [rule10,],
	"T": [rule10,],
	"U": [rule10,],
	"V": [rule10,],
	"W": [rule10,],
	"X": [rule10,],
	"Y": [rule10,],
	"Z": [rule10,],
	"_": [rule10,],
	"a": [rule10,],
	"b": [rule10,],
	"c": [rule10,],
	"d": [rule10,],
	"e": [rule10,],
	"f": [rule10,],
	"g": [rule10,],
	"h": [rule10,],
	"i": [rule10,],
	"j": [rule10,],
	"k": [rule10,],
	"l": [rule10,],
	"m": [rule10,],
	"n": [rule10,],
	"o": [rule10,],
	"p": [rule10,],
	"q": [rule10,],
	"r": [rule10,],
	"s": [rule10,],
	"t": [rule10,],
	"u": [rule10,],
	"v": [rule10,],
	"w": [rule10,],
	"x": [rule10,],
	"y": [rule10,],
	"z": [rule10,],
}

# x.rulesDictDict for scheme mode.
rulesDictDict = {
	"scheme_main": rulesDict1,
}

# Import dict for scheme mode.
importDict = {}

