# Leo colorizer control file for erlang mode.

# Properties for erlang mode.
properties = {
	"lineComment": "%",
}

# Keywords dict for erlang_main ruleset.
erlang_main_keywords_dict = {
	"		": "keywords",
	"			": "keywords",
	"
": "keywords",
	"-behaviour": "keyword3",
	"-compile": "keyword3",
	"-define": "keyword3",
	"-else": "keyword3",
	"-endif": "keyword3",
	"-export": "keyword3",
	"-file": "keyword3",
	"-ifdef": "keyword3",
	"-ifndef": "keyword3",
	"-import": "keyword3",
	"-include": "keyword3",
	"-include_lib": "keyword3",
	"-module": "keyword3",
	"-record": "keyword3",
	"-undef": "keyword3",
	"abs": "keyword2",
	"acos": "keyword2",
	"after": "keyword1",
	"alive": "keyword2",
	"apply": "keyword2",
	"asin": "keyword2",
	"atan": "keyword2",
	"atan2": "keyword2",
	"atom": "keyword2",
	"atom_to_list": "keyword2",
	"begin": "keyword1",
	"binary": "keyword2",
	"binary_to_list": "keyword2",
	"binary_to_term": "keyword2",
	"case": "keyword1",
	"catch": "keyword1",
	"check_process_code": "keyword2",
	"concat_binary": "keyword2",
	"cond": "keyword1",
	"constant": "keyword2",
	"cos": "keyword2",
	"cosh": "keyword2",
	"date": "keyword2",
	"delete_module": "keyword2",
	"disconnect_node": "keyword2",
	"element": "keyword2",
	"end": "keyword1",
	"erase": "keyword2",
	"exit": "keyword2",
	"exp": "keyword2",
	"float": "keyword2",
	"float_to_list": "keyword2",
	"fun": "keyword1",
	"function": "keyword2",
	"get": "keyword2",
	"get_cookie": "keyword2",
	"get_keys": "keyword2",
	"group_leader": "keyword2",
	"halt": "keyword2",
	"hash": "keyword2",
	"hd": "keyword2",
	"if": "keyword1",
	"integer": "keyword2",
	"integer_to_list": "keyword2",
	"is_alive": "keyword2",
	"length": "keyword2",
	"let": "keyword1",
	"link": "keyword2",
	"list": "keyword2",
	"list_to_atom": "keyword2",
	"list_to_binary": "keyword2",
	"list_to_float": "keyword2",
	"list_to_integer": "keyword2",
	"list_to_pid": "keyword2",
	"list_to_tuple": "keyword2",
	"load_module": "keyword2",
	"log": "keyword2",
	"log10": "keyword2",
	"make_ref": "keyword2",
	"math": "keyword2",
	"module_loaded": "keyword2",
	"monitor_node": "keyword2",
	"node": "keyword2",
	"nodes": "keyword2",
	"now": "keyword2",
	"number": "keyword2",
	"of": "keyword1",
	"open_port": "keyword2",
	"pi": "keyword2",
	"pid": "keyword2",
	"pid_to_list": "keyword2",
	"port_close": "keyword2",
	"port_info": "keyword2",
	"ports": "keyword2",
	"pow": "keyword2",
	"power": "keyword2",
	"preloaded": "keyword2",
	"process": "keyword2",
	"process_flag": "keyword2",
	"process_info": "keyword2",
	"processes": "keyword2",
	"purge_module": "keyword2",
	"put": "keyword2",
	"query": "keyword1",
	"receive": "keyword1",
	"record": "keyword2",
	"reference": "keyword2",
	"register": "keyword2",
	"registered": "keyword2",
	"round": "keyword2",
	"self": "keyword2",
	"set_cookie": "keyword2",
	"set_node": "keyword2",
	"setelement": "keyword2",
	"sin": "keyword2",
	"sinh": "keyword2",
	"size": "keyword2",
	"spawn": "keyword2",
	"spawn_link": "keyword2",
	"split_binary": "keyword2",
	"sqrt": "keyword2",
	"statistics": "keyword2",
	"tan": "keyword2",
	"tanh": "keyword2",
	"term_to_binary": "keyword2",
	"throw": "keyword2",
	"time": "keyword2",
	"tl": "keyword2",
	"trunc": "keyword2",
	"tuple_to_list": "keyword2",
	"unlink": "keyword2",
	"unregister": "keyword2",
	"when": "keyword1",
	"whereis": "keyword2",
}

# Dictionary of keywords dictionaries for erlang mode.
keywordsDictDict = {
	"erlang_main": erlang_main_keywords_dict,
}

# Rules for erlang_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule4(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="literal2", pattern=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule5(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal3", seq="\$.\w*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal3", seq="badarg",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal3", seq="nocookie",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal3", seq="false",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal3", seq="true",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="?",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="operator", seq="\bdiv\b",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="operator", seq="\brem\b",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="operator", seq="\bor\b",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule31(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="operator", seq="\bxor\b",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule32(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="operator", seq="\bbor\b",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule33(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="operator", seq="\bbxor\b",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule34(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="operator", seq="\bbsl\b",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule35(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="operator", seq="\bbsr\b",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule36(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="operator", seq="\band\b",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule37(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="operator", seq="\bband\b",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule38(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="operator", seq="\bnot\b",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule39(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="operator", seq="\bbnot\b",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule40(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule27,],
	"\"": [rule1,],
	"#": [rule17,],
	"%": [rule0,],
	"'": [rule2,],
	"(": [rule3,],
	"*": [rule19,],
	"+": [rule18,],
	",": [rule25,],
	"-": [rule10,],
	".": [rule12,],
	"/": [rule15,],
	"0": [rule40,],
	"1": [rule40,],
	"2": [rule40,],
	"3": [rule40,],
	"4": [rule40,],
	"5": [rule40,],
	"6": [rule40,],
	"7": [rule40,],
	"8": [rule40,],
	"9": [rule40,],
	":": [rule4,rule20,],
	";": [rule13,],
	"<": [rule11,],
	"=": [rule14,],
	"?": [rule26,],
	"@": [rule40,],
	"A": [rule40,],
	"B": [rule40,],
	"C": [rule40,],
	"D": [rule40,],
	"E": [rule40,],
	"F": [rule40,],
	"G": [rule40,],
	"H": [rule40,],
	"I": [rule40,],
	"J": [rule40,],
	"K": [rule40,],
	"L": [rule40,],
	"M": [rule40,],
	"N": [rule40,],
	"O": [rule40,],
	"P": [rule40,],
	"Q": [rule40,],
	"R": [rule40,],
	"S": [rule40,],
	"T": [rule40,],
	"U": [rule40,],
	"V": [rule40,],
	"W": [rule40,],
	"X": [rule40,],
	"Y": [rule40,],
	"Z": [rule40,],
	"[": [rule23,],
	"\": [rule5,rule28,rule29,rule30,rule31,rule32,rule33,rule34,rule35,rule36,rule37,rule38,rule39,],
	"]": [rule24,],
	"_": [rule40,],
	"a": [rule40,],
	"b": [rule6,rule40,],
	"c": [rule40,],
	"d": [rule40,],
	"e": [rule40,],
	"f": [rule8,rule40,],
	"g": [rule40,],
	"h": [rule40,],
	"i": [rule40,],
	"j": [rule40,],
	"k": [rule40,],
	"l": [rule40,],
	"m": [rule40,],
	"n": [rule7,rule40,],
	"o": [rule40,],
	"p": [rule40,],
	"q": [rule40,],
	"r": [rule40,],
	"s": [rule40,],
	"t": [rule9,rule40,],
	"u": [rule40,],
	"v": [rule40,],
	"w": [rule40,],
	"x": [rule40,],
	"y": [rule40,],
	"z": [rule40,],
	"{": [rule21,],
	"|": [rule16,],
	"}": [rule22,],
}

# x.rulesDictDict for erlang mode.
rulesDictDict = {
	"erlang_main": rulesDict1,
}

# Import dict for erlang mode.
importDict = {}

