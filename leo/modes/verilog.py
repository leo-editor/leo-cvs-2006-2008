# Leo colorizer control file for verilog mode.

# Properties for verilog mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"indentNextLines": "(.*:\s*)|(\s*(begin|fork|task|table|specify|primitive|module|generate|function|case[xz]?)\>.*)|(\s*(always|if|else|for|forever|initial|repeat|while)\>[^;]*)",
	"lineComment": "//",
	"noWordSep": "_'",
	"wordBreakChars": ",+-=<>/?^&*",
}

# Keywords dict for verilog_main ruleset.
verilog_main_keywords_dict = {
	"$cleartrace": "function",
	"$finish": "function",
	"$monitoroff": "function",
	"$monitoron": "function",
	"$printtimescale": "function",
	"$random": "function",
	"$realtime": "function",
	"$settrace": "function",
	"$showscopes": "function",
	"$showvars": "function",
	"$stime": "function",
	"$stop": "function",
	"$time": "function",
	"$timeformat": "function",
	"`autoexpand_vectornets": "keyword2",
	"`celldefine": "keyword2",
	"`default_nettype": "keyword2",
	"`define": "keyword2",
	"`else": "keyword2",
	"`endcelldefine": "keyword2",
	"`endif": "keyword2",
	"`endprotect": "keyword2",
	"`endprotected": "keyword2",
	"`expand_vectornets": "keyword2",
	"`ifdef": "keyword2",
	"`ifndef": "keyword2",
	"`include": "keyword2",
	"`noexpand_vectornets": "keyword2",
	"`noremove_gatename": "keyword2",
	"`noremove_netname": "keyword2",
	"`nounconnected_drive": "keyword2",
	"`protect": "keyword2",
	"`protected": "keyword2",
	"`remove_gatename": "keyword2",
	"`remove_netname": "keyword2",
	"`resetall": "keyword2",
	"`signed": "keyword2",
	"`timescale": "keyword2",
	"`unconnected_drive": "keyword2",
	"`undef": "keyword2",
	"`unsigned": "keyword2",
	"always": "keyword1",
	"and": "function",
	"assign": "keyword1",
	"begin": "keyword1",
	"buf": "function",
	"bufif0": "function",
	"bufif1": "function",
	"case": "keyword1",
	"casex": "keyword1",
	"casez": "keyword1",
	"cmos": "function",
	"deassign": "keyword1",
	"default": "keyword1",
	"defparam": "keyword3",
	"disable": "keyword1",
	"else": "keyword1",
	"end": "keyword1",
	"endcase": "keyword1",
	"endfunction": "keyword1",
	"endgenerate": "keyword1",
	"endmodule": "keyword1",
	"endprimitive": "keyword1",
	"endspecify": "keyword1",
	"endtable": "keyword1",
	"endtask": "keyword1",
	"event": "keyword3",
	"for": "keyword1",
	"force": "keyword1",
	"forever": "keyword1",
	"fork": "keyword1",
	"function": "keyword1",
	"generate": "keyword1",
	"highz0": "keyword3",
	"highz1": "keyword3",
	"if": "keyword1",
	"initial": "keyword1",
	"inout": "keyword3",
	"input": "keyword3",
	"integer": "keyword3",
	"join": "keyword1",
	"large": "keyword3",
	"macromodule": "keyword1",
	"medium": "keyword3",
	"module": "keyword1",
	"nand": "function",
	"negedge": "keyword1",
	"nmos": "function",
	"nor": "function",
	"not": "function",
	"notif0": "function",
	"notif1": "function",
	"or": "function",
	"output": "keyword3",
	"parameter": "keyword3",
	"pmos": "function",
	"posedge": "keyword1",
	"primitive": "keyword1",
	"pull0": "keyword3",
	"pull1": "keyword3",
	"pulldown": "function",
	"pullup": "function",
	"rcmos": "function",
	"realtime": "keyword3",
	"reg": "keyword3",
	"release": "keyword1",
	"repeat": "keyword1",
	"rnmos": "function",
	"rpmos": "function",
	"rtran": "function",
	"rtranif0": "function",
	"rtranif1": "function",
	"scalared": "keyword3",
	"small": "keyword3",
	"specify": "keyword1",
	"strong0": "keyword3",
	"strong1": "keyword3",
	"supply0": "keyword3",
	"supply1": "keyword3",
	"table": "keyword1",
	"task": "keyword1",
	"time": "keyword3",
	"tran": "function",
	"tranif0": "function",
	"tranif1": "function",
	"tri": "keyword3",
	"tri0": "keyword3",
	"tri1": "keyword3",
	"triand": "keyword3",
	"trior": "keyword3",
	"trireg": "keyword3",
	"vectored": "keyword3",
	"wait": "keyword1",
	"wand": "keyword3",
	"weak0": "keyword3",
	"weak1": "keyword3",
	"while": "keyword1",
	"wire": "keyword3",
	"wor": "keyword3",
	"xnor": "function",
	"xor": "function",
}

# Rules for verilog_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment1"', begin="/*", end="*/",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment2"', seq="//",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="digit", seq="'d",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="digit", seq="'h",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="digit", seq="'b",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="digit", seq="'o",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind='"function"',
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=True)

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for verilog_main ruleset.
verilog_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
	rule20, rule21, rule22, rule23, ]

# Rules dict for verilog mode.
rulesDict = {
	"verilog_main": verilog_main_rules,
}

# Import dict for verilog mode.
importDict = {}

