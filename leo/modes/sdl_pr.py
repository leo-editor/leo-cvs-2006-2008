# Leo colorizer control file for sdl_pr mode.

# Properties for sdl_pr mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"indentNextLines": "\\s*(block|channel|connection|decision|generator|input|macro|newtype|operator|package|procedure|process|refinement|service|start|state|substructure|syntype|system).*|\\s*(signal)\\s*",
}

# Keywords dict for sdl_pr_main ruleset.
sdl_pr_main_keywords_dict = {
	"Array": "keyword3",
	"Boolean": "keyword2",
	"Character": "keyword2",
	"Charstring": "keyword2",
	"Duration": "keyword2",
	"Integer": "keyword2",
	"Natural": "keyword2",
	"PId": "keyword2",
	"Powerset": "keyword3",
	"Real": "keyword2",
	"String": "keyword3",
	"Time": "keyword2",
	"active": "keyword1",
	"adding": "keyword1",
	"all": "keyword1",
	"alternative": "keyword1",
	"any": "keyword1",
	"as": "keyword1",
	"atleast": "keyword1",
	"axioms": "keyword1",
	"block": "keyword1",
	"call": "keyword1",
	"channel": "keyword1",
	"comment": "keyword1",
	"connect": "keyword1",
	"connection": "keyword1",
	"constant": "keyword1",
	"constants": "keyword1",
	"create": "keyword1",
	"dcl": "keyword1",
	"decision": "keyword1",
	"default": "keyword1",
	"else": "keyword1",
	"end": "keyword1",
	"endalternative": "keyword1",
	"endblock": "keyword1",
	"endchannel": "keyword1",
	"endconnection": "keyword1",
	"enddecision": "keyword1",
	"endgenerator": "keyword1",
	"endmacro": "keyword1",
	"endnewtype": "keyword1",
	"endoperator": "keyword1",
	"endpackage": "keyword1",
	"endprocedure": "keyword1",
	"endprocess": "keyword1",
	"endrefinement": "keyword1",
	"endselect": "keyword1",
	"endservice": "keyword1",
	"endstate": "keyword1",
	"endsubstructure": "keyword1",
	"endsyntype": "keyword1",
	"endsystem": "keyword1",
	"env": "keyword1",
	"error": "keyword1",
	"export": "keyword1",
	"exported": "keyword1",
	"external": "keyword1",
	"false": "literal1",
	"fi": "keyword1",
	"finalized": "keyword1",
	"for": "keyword1",
	"fpar": "keyword1",
	"from": "keyword1",
	"gate": "keyword1",
	"generator": "keyword1",
	"if": "keyword1",
	"import": "keyword1",
	"imported": "keyword1",
	"in": "keyword1",
	"inherits": "keyword1",
	"input": "keyword1",
	"interface": "keyword1",
	"join": "keyword1",
	"literal": "keyword1",
	"literals": "keyword1",
	"macro": "keyword1",
	"macrodefinition": "keyword1",
	"macroid": "keyword1",
	"map": "keyword1",
	"nameclass": "keyword1",
	"newtype": "keyword1",
	"nextstate": "keyword1",
	"nodelay": "keyword1",
	"noequality": "keyword1",
	"none": "keyword1",
	"now": "keyword1",
	"null": "literal1",
	"offspring": "keyword1",
	"operator": "keyword1",
	"operators": "keyword1",
	"ordering": "keyword1",
	"out": "keyword1",
	"output": "keyword1",
	"package": "keyword1",
	"parent": "keyword1",
	"priority": "keyword1",
	"procedure": "keyword1",
	"process": "keyword1",
	"provided": "keyword1",
	"redefined": "keyword1",
	"referenced": "keyword1",
	"refinement": "keyword1",
	"remote": "keyword1",
	"reset": "keyword1",
	"return": "keyword1",
	"returns": "keyword1",
	"revealed": "keyword1",
	"reverse": "keyword1",
	"route": "keyword1",
	"save": "keyword1",
	"select": "keyword1",
	"self": "keyword1",
	"sender": "keyword1",
	"service": "keyword1",
	"set": "keyword1",
	"signal": "keyword1",
	"signallist": "keyword1",
	"signalroute": "keyword1",
	"signalset": "keyword1",
	"spelling": "keyword1",
	"start": "keyword1",
	"state": "keyword1",
	"stop": "keyword1",
	"struct": "keyword1",
	"substructure": "keyword1",
	"synonym": "keyword1",
	"syntype": "keyword1",
	"system": "keyword1",
	"task": "keyword1",
	"then": "keyword1",
	"this": "keyword1",
	"timer": "keyword1",
	"to": "keyword1",
	"true": "literal1",
	"type": "keyword1",
	"use": "keyword1",
	"via": "keyword1",
	"view": "keyword1",
	"viewed": "keyword1",
	"virtual": "keyword1",
	"with": "keyword1",
}

# Dictionary of keywords dictionaries for sdl_pr mode.
keywordsDictDict = {
	"sdl_pr_main": sdl_pr_main_keywords_dict,
}

# Rules for sdl_pr_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment2", begin="/*#SDTREF", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="==",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="and",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="mod",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="not",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="or",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="rem",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="xor",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule17,],
	"\"": [rule3,],
	"'": [rule2,],
	"*": [rule6,],
	"+": [rule4,],
	"-": [rule5,],
	".": [rule16,],
	"/": [rule0,rule1,rule7,rule9,rule18,],
	"0": [rule25,],
	"1": [rule25,],
	"2": [rule25,],
	"3": [rule25,],
	"4": [rule25,],
	"5": [rule25,],
	"6": [rule25,],
	"7": [rule25,],
	"8": [rule25,],
	"9": [rule25,],
	":": [rule10,],
	"<": [rule12,rule13,],
	"=": [rule8,rule11,],
	">": [rule14,rule15,],
	"@": [rule25,],
	"A": [rule25,],
	"B": [rule25,],
	"C": [rule25,],
	"D": [rule25,],
	"E": [rule25,],
	"F": [rule25,],
	"G": [rule25,],
	"H": [rule25,],
	"I": [rule25,],
	"J": [rule25,],
	"K": [rule25,],
	"L": [rule25,],
	"M": [rule25,],
	"N": [rule25,],
	"O": [rule25,],
	"P": [rule25,],
	"Q": [rule25,],
	"R": [rule25,],
	"S": [rule25,],
	"T": [rule25,],
	"U": [rule25,],
	"V": [rule25,],
	"W": [rule25,],
	"X": [rule25,],
	"Y": [rule25,],
	"Z": [rule25,],
	"_": [rule25,],
	"a": [rule19,rule25,],
	"b": [rule25,],
	"c": [rule25,],
	"d": [rule25,],
	"e": [rule25,],
	"f": [rule25,],
	"g": [rule25,],
	"h": [rule25,],
	"i": [rule25,],
	"j": [rule25,],
	"k": [rule25,],
	"l": [rule25,],
	"m": [rule20,rule25,],
	"n": [rule21,rule25,],
	"o": [rule22,rule25,],
	"p": [rule25,],
	"q": [rule25,],
	"r": [rule23,rule25,],
	"s": [rule25,],
	"t": [rule25,],
	"u": [rule25,],
	"v": [rule25,],
	"w": [rule25,],
	"x": [rule24,rule25,],
	"y": [rule25,],
	"z": [rule25,],
}

# x.rulesDictDict for sdl_pr mode.
rulesDictDict = {
	"sdl_pr_main": rulesDict1,
}

# Import dict for sdl_pr mode.
importDict = {}

