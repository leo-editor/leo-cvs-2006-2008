# Leo colorizer control file for vhdl mode.

# Properties for vhdl mode.
properties = {
	"label": "VHDL",
	"lineComment": "--",
}

# Keywords dict for vhdl_main ruleset.
vhdl_main_keywords_dict = {
	"ACTIVE": "keyword3",
	"ASCENDING": "keyword3",
	"BASE": "keyword3",
	"DELAYED": "keyword3",
	"DRIVING": "keyword3",
	"EVENT": "keyword3",
	"HIGH": "keyword3",
	"IMAGE": "keyword3",
	"INSTANCE": "keyword3",
	"LAST": "keyword3",
	"LEFT": "keyword3",
	"LEFTOF": "keyword3",
	"LENGTH": "keyword3",
	"LOW": "keyword3",
	"PATH": "keyword3",
	"POS": "keyword3",
	"PRED": "keyword3",
	"QUIET": "keyword3",
	"RANGE": "keyword3",
	"REVERSE": "keyword3",
	"RIGHT": "keyword3",
	"RIGHTOF": "keyword3",
	"SIMPLE": "keyword3",
	"STABLE": "keyword3",
	"SUCC": "keyword3",
	"TRANSACTION": "keyword3",
	"VAL": "keyword3",
	"VALUE": "keyword3",
	"abs": "operator",
	"alias": "keyword1",
	"all": "keyword1",
	"and": "operator",
	"architecture": "keyword1",
	"array": "keyword1",
	"assert": "keyword1",
	"begin": "keyword1",
	"bit": "keyword2",
	"bit_vector": "keyword2",
	"break": "keyword1",
	"case": "keyword1",
	"catch": "keyword1",
	"component": "keyword1",
	"constant": "keyword1",
	"continue": "keyword1",
	"default": "keyword1",
	"do": "keyword1",
	"downto": "keyword1",
	"else": "keyword1",
	"elsif": "keyword1",
	"end": "keyword1",
	"entity": "keyword1",
	"extends": "keyword1",
	"false": "literal2",
	"for": "keyword1",
	"function": "keyword1",
	"generic": "keyword1",
	"if": "keyword1",
	"implements": "keyword1",
	"import": "keyword2",
	"in": "keyword1",
	"inout": "keyword1",
	"instanceof": "keyword1",
	"integer": "keyword2",
	"is": "keyword1",
	"library": "keyword1",
	"loop": "keyword1",
	"mod": "operator",
	"nand": "operator",
	"natural": "keyword2",
	"nor": "operator",
	"not": "operator",
	"of": "keyword1",
	"or": "operator",
	"others": "keyword1",
	"out": "keyword1",
	"package": "keyword2",
	"port": "keyword1",
	"process": "keyword1",
	"range": "keyword1",
	"record": "keyword1",
	"rem": "operator",
	"resize": "function",
	"return": "keyword1",
	"rising_edge": "function",
	"rol": "operator",
	"ror": "operator",
	"rotate_left": "function",
	"rotate_right": "function",
	"shift_left": "function",
	"shift_right": "function",
	"signal": "keyword1",
	"signed": "function",
	"sla": "operator",
	"sll": "operator",
	"sra": "operator",
	"srl": "operator",
	"static": "keyword1",
	"std_logic": "keyword2",
	"std_logic_vector": "keyword2",
	"std_match": "function",
	"std_ulogic": "keyword2",
	"std_ulogic_vector": "keyword2",
	"switch": "keyword1",
	"then": "keyword1",
	"to": "keyword1",
	"to_bit": "function",
	"to_bitvector": "function",
	"to_integer": "function",
	"to_signed": "function",
	"to_stdlogicvector": "function",
	"to_stdulogic": "function",
	"to_stdulogicvector": "function",
	"to_unsigned": "function",
	"true": "literal2",
	"type": "keyword1",
	"unsigned": "function",
	"upto": "keyword1",
	"use": "keyword1",
	"variable": "keyword1",
	"wait": "keyword1",
	"when": "keyword1",
	"while": "keyword1",
	"xnor": "operator",
}

# Rules for vhdl_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq="'event",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="'", end="'",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment1"', seq="--",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="**",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind='"label"',
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=True)

def rule23(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for vhdl_main ruleset.
vhdl_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
	rule20, rule21, rule22, rule23, ]

# Rules dict for vhdl mode.
rulesDict = {
	"vhdl_main": vhdl_main_rules,
}

# Import dict for vhdl mode.
importDict = {}

