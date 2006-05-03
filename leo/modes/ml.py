# Leo colorizer control file for ml mode.

# Properties for ml mode.
properties = {
	"commentEnd": "*)",
	"commentStart": "(*",
}

# Keywords dict for ml_main ruleset.
ml_main_keywords_dict = {
	"ANTIQUOTE": "literal2",
	"Bind": "keyword2",
	"Chr": "keyword2",
	"Div": "keyword2",
	"Domain": "keyword2",
	"EQUAL": "literal2",
	"Fail": "keyword2",
	"GREATER": "literal2",
	"Graphic": "keyword2",
	"Interrupt": "keyword2",
	"Io": "keyword2",
	"LESS": "literal2",
	"Match": "keyword2",
	"NONE": "literal2",
	"Option": "keyword2",
	"Ord": "keyword2",
	"Overflow": "keyword2",
	"QUOTE": "literal2",
	"SOME": "literal2",
	"Size": "keyword2",
	"Subscript": "keyword2",
	"SysErr": "keyword2",
	"abstype": "keyword1",
	"and": "keyword1",
	"andalso": "keyword1",
	"array": "keyword3",
	"as": "keyword1",
	"before": "operator",
	"bool": "keyword3",
	"case": "keyword1",
	"char": "keyword3",
	"datatype": "keyword1",
	"div": "operator",
	"do": "keyword1",
	"else": "keyword1",
	"end": "keyword1",
	"eqtype": "keyword1",
	"exception": "keyword1",
	"exn": "keyword3",
	"false": "literal2",
	"fn": "keyword1",
	"frag": "keyword3",
	"fun": "keyword1",
	"functor": "keyword1",
	"handle": "keyword1",
	"if": "keyword1",
	"in": "keyword1",
	"include": "keyword1",
	"infix": "keyword1",
	"infixr": "keyword1",
	"int": "keyword3",
	"let": "keyword1",
	"list": "keyword3",
	"local": "keyword1",
	"mod": "operator",
	"nil": "literal2",
	"nonfix": "keyword1",
	"o": "operator",
	"of": "keyword1",
	"op": "keyword1",
	"open": "keyword1",
	"option": "keyword3",
	"order": "keyword3",
	"orelse": "keyword1",
	"raise": "keyword1",
	"real": "keyword3",
	"rec": "keyword1",
	"ref": "keyword3",
	"sharing": "keyword1",
	"sig": "keyword1",
	"signature": "keyword1",
	"string": "keyword3",
	"struct": "keyword1",
	"structure": "keyword1",
	"substring": "keyword3",
	"then": "keyword1",
	"true": "literal2",
	"type": "keyword1",
	"unit": "keyword3",
	"val": "keyword1",
	"vector": "keyword3",
	"where": "keyword1",
	"while": "keyword1",
	"with": "keyword1",
	"withtype": "keyword1",
	"word": "keyword3",
	"word8": "keyword3",
}

# Rules for ml_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment1"', begin="(*", end="*)",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="#\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="::",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<>",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for ml_main ruleset.
ml_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, ]

# Rules dict for ml mode.
rulesDict = {
	"ml_main": ml_main_rules,
}

# Import dict for ml mode.
importDict = {}

