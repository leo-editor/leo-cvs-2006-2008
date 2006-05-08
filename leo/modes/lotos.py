# Leo colorizer control file for lotos mode.

# Properties for lotos mode.
properties = {
	"commentEnd": "*)",
	"commentStart": "(*",
	"indentNextLines": "\s*(let|library|process|specification|type|>>).*|\s*(\(|\[\]|\[>|\|\||\|\|\||\|\[.*\]\||\[.*\]\s*->)\s*",
}

# Keywords dict for lotos_main ruleset.
lotos_main_keywords_dict = {
	"
": "keywords",
	"    ": "keywords",
	"      ": "keywords",
	"BasicNaturalNumber": "keyword2",
	"BasicNonEmptyString": "keyword2",
	"Bit": "keyword2",
	"BitNatRepr": "keyword2",
	"BitString": "keyword2",
	"Bool": "keyword2",
	"Boolean": "keyword2",
	"DecDigit": "keyword2",
	"DecNatRepr": "keyword2",
	"DecString": "keyword2",
	"Element": "keyword2",
	"FBool": "keyword2",
	"FBoolean": "keyword2",
	"HexDigit": "keyword2",
	"HexNatRepr": "keyword2",
	"HexString": "keyword2",
	"Nat": "keyword2",
	"NatRepresentations": "keyword2",
	"NaturalNumber": "keyword2",
	"NonEmptyString": "keyword2",
	"OctDigit": "keyword2",
	"OctNatRepr": "keyword2",
	"OctString": "keyword2",
	"Octet": "keyword2",
	"OctetString": "keyword2",
	"RicherNonEmptyString": "keyword2",
	"Set": "keyword2",
	"String": "keyword2",
	"String0": "keyword2",
	"String1": "keyword2",
	"accept": "keyword1",
	"actualizedby": "keyword1",
	"any": "keyword1",
	"behavior": "keyword1",
	"behaviour": "keyword1",
	"choice": "keyword1",
	"endlib": "keyword1",
	"endproc": "keyword1",
	"endspec": "keyword1",
	"endtype": "keyword1",
	"eqns": "keyword1",
	"exit": "keyword1",
	"false": "literal1",
	"for": "keyword1",
	"forall": "keyword1",
	"formaleqns": "keyword1",
	"formalopns": "keyword1",
	"formalsorts": "keyword1",
	"hide": "keyword1",
	"i": "keyword1",
	"in": "keyword1",
	"is": "keyword1",
	"let": "keyword1",
	"library": "keyword1",
	"noexit": "keyword1",
	"of": "keyword1",
	"ofsort": "keyword1",
	"opnnames": "keyword1",
	"opns": "keyword1",
	"par": "keyword1",
	"process": "keyword1",
	"renamedby": "keyword1",
	"sortnames": "keyword1",
	"sorts": "keyword1",
	"specification": "keyword1",
	"stop": "keyword1",
	"true": "literal1",
	"type": "keyword1",
	"using": "keyword1",
	"where": "keyword1",
}

# Dictionary of keywords dictionaries for lotos mode.
keywordsDictDict = {
	"lotos_main": lotos_main_keywords_dict,
}

# Rules for lotos_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="(*", end="*)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|||",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="||",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="]|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"(": [rule0,],
	"0": [rule8,],
	"1": [rule8,],
	"2": [rule8,],
	"3": [rule8,],
	"4": [rule8,],
	"5": [rule8,],
	"6": [rule8,],
	"7": [rule8,],
	"8": [rule8,],
	"9": [rule8,],
	">": [rule1,],
	"@": [rule8,],
	"A": [rule8,],
	"B": [rule8,],
	"C": [rule8,],
	"D": [rule8,],
	"E": [rule8,],
	"F": [rule8,],
	"G": [rule8,],
	"H": [rule8,],
	"I": [rule8,],
	"J": [rule8,],
	"K": [rule8,],
	"L": [rule8,],
	"M": [rule8,],
	"N": [rule8,],
	"O": [rule8,],
	"P": [rule8,],
	"Q": [rule8,],
	"R": [rule8,],
	"S": [rule8,],
	"T": [rule8,],
	"U": [rule8,],
	"V": [rule8,],
	"W": [rule8,],
	"X": [rule8,],
	"Y": [rule8,],
	"Z": [rule8,],
	"[": [rule2,rule7,],
	"]": [rule6,],
	"_": [rule8,],
	"a": [rule8,],
	"b": [rule8,],
	"c": [rule8,],
	"d": [rule8,],
	"e": [rule8,],
	"f": [rule8,],
	"g": [rule8,],
	"h": [rule8,],
	"i": [rule8,],
	"j": [rule8,],
	"k": [rule8,],
	"l": [rule8,],
	"m": [rule8,],
	"n": [rule8,],
	"o": [rule8,],
	"p": [rule8,],
	"q": [rule8,],
	"r": [rule8,],
	"s": [rule8,],
	"t": [rule8,],
	"u": [rule8,],
	"v": [rule8,],
	"w": [rule8,],
	"x": [rule8,],
	"y": [rule8,],
	"z": [rule8,],
	"|": [rule3,rule4,rule5,],
}

# x.rulesDictDict for lotos mode.
rulesDictDict = {
	"lotos_main": rulesDict1,
}

# Import dict for lotos mode.
importDict = {}

