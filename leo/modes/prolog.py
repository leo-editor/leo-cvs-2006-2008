# Leo colorizer control file for prolog mode.

# Properties for prolog mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"lineComment": "%",
}

# Keywords dict for prolog_main ruleset.
prolog_main_keywords_dict = {
	"!": "keyword1",
	"_": "keyword3",
	"abolish": "function",
	"arg": "function",
	"asserta": "function",
	"assertz": "function",
	"at_end_of_stream": "function",
	"atan": "function",
	"atom": "function",
	"atom_chars": "function",
	"atom_codes": "function",
	"atom_concat": "function",
	"atom_length": "function",
	"atomic": "function",
	"bagof": "function",
	"call": "function",
	"catch": "function",
	"char_code": "function",
	"char_conversion": "function",
	"clause": "function",
	"close": "function",
	"compound": "function",
	"copy_term": "function",
	"cos": "function",
	"current_char_conversion": "function",
	"current_input": "function",
	"current_op": "function",
	"current_output": "function",
	"current_predicate": "function",
	"current_prolog_flag": "function",
	"exp": "function",
	"fail": "keyword1",
	"findall": "function",
	"float": "function",
	"functor": "function",
	"get_byte": "function",
	"get_char": "function",
	"get_code": "function",
	"halt": "function",
	"integer": "function",
	"is": "keyword2",
	"log": "function",
	"mod": "keyword2",
	"nl": "function",
	"nonvar": "function",
	"number": "function",
	"number_chars": "function",
	"number_codes": "function",
	"once": "function",
	"op": "function",
	"open": "function",
	"peek_byte": "function",
	"peek_char": "function",
	"peek_code": "function",
	"put_byte": "function",
	"put_char": "function",
	"put_code": "function",
	"read": "function",
	"read_term": "function",
	"rem": "keyword2",
	"repeat": "keyword1",
	"retract": "function",
	"set_input": "function",
	"set_output": "function",
	"set_prolog_flag": "function",
	"set_stream_position": "function",
	"setof": "function",
	"sin": "function",
	"sqrt": "function",
	"stream_property": "function",
	"sub_atom": "function",
	"throw": "function",
	"true": "keyword1",
	"unify_with_occurs_check": "function",
	"var": "function",
	"write": "function",
	"write_canonical": "function",
	"write_term": "function",
	"writeq": "function",
}

# Keywords dict for prolog_list ruleset.
prolog_list_keywords_dict = {}

# Rules for prolog_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment1"', seq="%",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment1"', begin="/*", end="*/",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="'", end="'",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal2"', begin="[", end="]",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="LIST",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-->",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":-",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="?-",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=";",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="->",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\+",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="==",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\==",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@<",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@=<",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@>=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@>",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=..",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=:=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=\=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=<",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/\",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\/",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="//",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<<",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule31(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">>",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule32(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule33(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="**",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule34(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule35(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule36(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule37(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule38(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule39(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule40(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq="(",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule41(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq=")",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule42(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq="{",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule43(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq="}",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule44(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for prolog_main ruleset.
prolog_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
	rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29,
	rule30, rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39,
	rule40, rule41, rule42, rule43, rule44, ]

# Rules for prolog_list ruleset.

def rule45(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal2"', begin="[", end="]",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="LIST",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

# Rules list for prolog_list ruleset.
prolog_list_rules = [
	rule45, ]

# Rules dict for prolog mode.
rulesDict = {
	"prolog_list": prolog_list_rules,
	"prolog_main": prolog_main_rules,
}

# Import dict for prolog mode.
importDict = {}

