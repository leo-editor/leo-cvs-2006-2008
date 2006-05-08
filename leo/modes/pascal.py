# Leo colorizer control file for pascal mode.

# Properties for pascal mode.
properties = {
	"commentEnd": "}",
	"commentStart": "{",
	"lineComment": "//",
}

# Keywords dict for pascal_main ruleset.
pascal_main_keywords_dict = {
	"absolute": "keyword2",
	"abstract": "keyword2",
	"and": "keyword1",
	"array": "keyword1",
	"as": "keyword1",
	"asm": "keyword1",
	"assembler": "keyword2",
	"at": "keyword1",
	"automated": "keyword2",
	"begin": "keyword1",
	"boolean": "keyword3",
	"byte": "keyword3",
	"bytebool": "keyword3",
	"cardinal": "keyword3",
	"case": "keyword1",
	"cdecl": "keyword2",
	"char": "keyword3",
	"class": "keyword1",
	"comp": "keyword3",
	"const": "keyword1",
	"constructor": "keyword1",
	"contains": "keyword2",
	"currency": "keyword3",
	"default": "keyword2",
	"deprecated": "keyword2",
	"destructor": "keyword1",
	"dispid": "keyword2",
	"dispinterface": "keyword1",
	"div": "keyword1",
	"do": "keyword1",
	"double": "keyword3",
	"downto": "keyword1",
	"dynamic": "keyword2",
	"else": "keyword1",
	"end": "keyword1",
	"except": "keyword1",
	"export": "keyword2",
	"exports": "keyword1",
	"extended": "keyword3",
	"external": "keyword2",
	"false": "literal2",
	"far": "keyword2",
	"file": "keyword1",
	"final": "keyword1",
	"finalization": "keyword1",
	"finally": "keyword1",
	"for": "keyword1",
	"forward": "keyword2",
	"function": "keyword1",
	"goto": "keyword1",
	"if": "keyword1",
	"implementation": "keyword1",
	"implements": "keyword2",
	"in": "keyword1",
	"index": "keyword2",
	"inherited": "keyword1",
	"initialization": "keyword1",
	"inline": "keyword1",
	"integer": "keyword3",
	"interface": "keyword1",
	"is": "keyword1",
	"label": "keyword1",
	"library": "keyword2",
	"local": "keyword2",
	"longbool": "keyword3",
	"longint": "keyword3",
	"message": "keyword2",
	"mod": "keyword1",
	"name": "keyword2",
	"namespaces": "keyword2",
	"near": "keyword2",
	"nil": "literal2",
	"nodefault": "keyword2",
	"not": "keyword1",
	"object": "keyword1",
	"of": "keyword1",
	"on": "keyword1",
	"or": "keyword1",
	"out": "keyword1",
	"overload": "keyword2",
	"override": "keyword2",
	"package": "keyword2",
	"packed": "keyword1",
	"pascal": "keyword2",
	"platform": "keyword2",
	"pointer": "keyword3",
	"private": "keyword2",
	"procedure": "keyword1",
	"program": "keyword1",
	"property": "keyword1",
	"protected": "keyword2",
	"public": "keyword2",
	"published": "keyword2",
	"raise": "keyword1",
	"read": "keyword2",
	"readonly": "keyword2",
	"real": "keyword3",
	"record": "keyword1",
	"register": "keyword2",
	"reintroduce": "keyword2",
	"repeat": "keyword1",
	"requires": "keyword2",
	"resident": "keyword2",
	"resourcestring": "keyword1",
	"safecall": "keyword2",
	"sealed": "keyword1",
	"self": "literal2",
	"set": "keyword1",
	"shl": "keyword1",
	"shortint": "keyword3",
	"shr": "keyword1",
	"single": "keyword3",
	"smallint": "keyword3",
	"static": "keyword1",
	"stdcall": "keyword2",
	"stored": "keyword2",
	"string": "keyword1",
	"then": "keyword1",
	"threadvar": "keyword1",
	"to": "keyword1",
	"true": "literal2",
	"try": "keyword1",
	"type": "keyword1",
	"unit": "keyword1",
	"unsafe": "keyword1",
	"until": "keyword1",
	"uses": "keyword1",
	"var": "keyword1",
	"varargs": "keyword2",
	"virtual": "keyword2",
	"while": "keyword1",
	"with": "keyword1",
	"word": "keyword3",
	"wordbool": "keyword3",
	"write": "keyword2",
	"writeonly": "keyword2",
	"xor": "keyword1",
}

# Dictionary of keywords dictionaries for pascal mode.
keywordsDictDict = {
	"pascal_main": pascal_main_keywords_dict,
}

# Rules for pascal_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment3", begin="{$", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="comment3", begin="(*$", end="*)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="{", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="(*", end="*)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for pascal_main ruleset.
pascal_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
	rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, ]

# Rules dict for pascal mode.
rulesDict = {
	"pascal_main": pascal_main_rules,
}

# Import dict for pascal mode.
importDict = {}

