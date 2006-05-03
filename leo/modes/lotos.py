# Leo colorizer control file for lotos mode.

# Properties for lotos mode.
properties = {
	"commentEnd": "*)",
	"commentStart": "(*",
	"indentNextLines": "\s*(let|library|process|specification|type|>>).*|\s*(\(|\[\]|\[>|\|\||\|\|\||\|\[.*\]\||\[.*\]\s*->)\s*",
}

# Keywords dict for lotos_main ruleset.
lotos_main_keywords_dict = {
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

# Rules for lotos_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment1"', begin="(*", end="*)",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">>",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule2(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[>",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|||",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="||",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|[",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="]|",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[]",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for lotos_main ruleset.
lotos_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, ]

# Rules dict for lotos mode.
rulesDict = {
	"lotos_main": lotos_main_rules,
}

# Import dict for lotos mode.
importDict = {}

