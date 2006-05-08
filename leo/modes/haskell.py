# Leo colorizer control file for haskell mode.

# Properties for haskell mode.
properties = {
	"commentEnd": "-}",
	"commentStart": "{-",
	"indentSize": "8",
	"lineComment": "--",
	"tabSize": "8",
}

# Keywords dict for haskell_main ruleset.
haskell_main_keywords_dict = {
	"		": "keywords",
	"			": "keywords",
	"
": "keywords",
	":": "literal2",
	"Addr": "keyword3",
	"Bool": "keyword3",
	"Bounded": "keyword3",
	"Char": "keyword3",
	"Double": "keyword3",
	"EQ": "literal2",
	"Either": "keyword3",
	"Enum": "keyword3",
	"Eq": "keyword3",
	"False": "literal2",
	"FilePath": "keyword3",
	"Float": "keyword3",
	"Floating": "keyword3",
	"Fractional": "keyword3",
	"Functor": "keyword3",
	"GT": "literal2",
	"IO": "keyword3",
	"IOError": "keyword3",
	"IOResult": "keyword3",
	"Int": "keyword3",
	"Integer": "keyword3",
	"Integral": "keyword3",
	"Ix": "keyword3",
	"Just": "literal2",
	"LT": "literal2",
	"Left": "literal2",
	"Maybe": "keyword3",
	"Monad": "keyword3",
	"Nothing": "literal2",
	"Num": "keyword3",
	"Ord": "keyword3",
	"Ordering": "keyword3",
	"Ratio": "keyword3",
	"Rational": "keyword3",
	"Read": "keyword3",
	"ReadS": "keyword3",
	"Real": "keyword3",
	"RealFloat": "keyword3",
	"RealFrac": "keyword3",
	"Right": "literal2",
	"Show": "keyword3",
	"ShowS": "keyword3",
	"String": "keyword3",
	"True": "literal2",
	"_": "keyword1",
	"as": "keyword1",
	"case": "keyword1",
	"class": "keyword1",
	"data": "keyword1",
	"default": "keyword1",
	"deriving": "keyword1",
	"div": "operator",
	"do": "keyword1",
	"elem": "operator",
	"else": "keyword1",
	"hiding": "keyword1",
	"if": "keyword1",
	"import": "keyword1",
	"in": "keyword1",
	"infix": "keyword1",
	"infixl": "keyword1",
	"infixr": "keyword1",
	"instance": "keyword1",
	"let": "keyword1",
	"mod": "operator",
	"module": "keyword1",
	"newtype": "keyword1",
	"notElem": "operator",
	"of": "keyword1",
	"qualified": "keyword1",
	"quot": "operator",
	"rem": "operator",
	"seq": "operator",
	"then": "keyword1",
	"type": "keyword1",
	"where": "keyword1",
}

# Dictionary of keywords dictionaries for haskell mode.
keywordsDictDict = {
	"haskell_main": haskell_main_keywords_dict,
}

# Rules for haskell_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment2", begin="{-#", end="#-}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="{-", end="-}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="--",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="' '",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="'!'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="'\"'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="'$'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="'%'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="'/'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="'('",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="')'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="'['",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="']'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="'+'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="'-'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="'*'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="'='",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="'/'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="'^'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="'.'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="','",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="':'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="';'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="'<'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="'>'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="'|'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="'@'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=True)

def rule29(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="..",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule31(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="::",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule32(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule33(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule34(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule35(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule36(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule37(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule38(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule39(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule40(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule41(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule42(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule43(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule44(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule45(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule46(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule44,],
	"\"": [rule3,],
	"$": [rule45,],
	"%": [rule38,],
	"&": [rule30,],
	"'": [rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27,rule28,],
	"*": [rule36,],
	"+": [rule34,],
	"-": [rule2,rule35,],
	".": [rule29,],
	"/": [rule37,],
	"0": [rule46,],
	"1": [rule46,],
	"2": [rule46,],
	"3": [rule46,],
	"4": [rule46,],
	"5": [rule46,],
	"6": [rule46,],
	"7": [rule46,],
	"8": [rule46,],
	"9": [rule46,],
	":": [rule31,],
	"<": [rule32,],
	"=": [rule40,],
	">": [rule33,],
	"@": [rule42,rule46,],
	"A": [rule46,],
	"B": [rule46,],
	"C": [rule46,],
	"D": [rule46,],
	"E": [rule46,],
	"F": [rule46,],
	"G": [rule46,],
	"H": [rule46,],
	"I": [rule46,],
	"J": [rule46,],
	"K": [rule46,],
	"L": [rule46,],
	"M": [rule46,],
	"N": [rule46,],
	"O": [rule46,],
	"P": [rule46,],
	"Q": [rule46,],
	"R": [rule46,],
	"S": [rule46,],
	"T": [rule46,],
	"U": [rule46,],
	"V": [rule46,],
	"W": [rule46,],
	"X": [rule46,],
	"Y": [rule46,],
	"Z": [rule46,],
	"^": [rule39,],
	"_": [rule46,],
	"a": [rule46,],
	"b": [rule46,],
	"c": [rule46,],
	"d": [rule46,],
	"e": [rule46,],
	"f": [rule46,],
	"g": [rule46,],
	"h": [rule46,],
	"i": [rule46,],
	"j": [rule46,],
	"k": [rule46,],
	"l": [rule46,],
	"m": [rule46,],
	"n": [rule46,],
	"o": [rule46,],
	"p": [rule46,],
	"q": [rule46,],
	"r": [rule46,],
	"s": [rule46,],
	"t": [rule46,],
	"u": [rule46,],
	"v": [rule46,],
	"w": [rule46,],
	"x": [rule46,],
	"y": [rule46,],
	"z": [rule46,],
	"{": [rule0,rule1,],
	"|": [rule41,],
	"~": [rule43,],
}

# x.rulesDictDict for haskell mode.
rulesDictDict = {
	"haskell_main": rulesDict1,
}

# Import dict for haskell mode.
importDict = {}

