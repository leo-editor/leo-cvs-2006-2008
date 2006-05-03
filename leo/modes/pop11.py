# Leo colorizer control file for pop11 mode.

# Properties for pop11 mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"lineComment": ";;;",
}

# Keywords dict for pop11_main ruleset.
pop11_main_keywords_dict = {
	"add": "literal2",
	"alladd": "literal2",
	"and": "keyword2",
	"biginteger": "keyword1",
	"boolean": "keyword1",
	"by": "keyword3",
	"case": "keyword3",
	"class": "keyword1",
	"complex": "keyword1",
	"cons_with": "keyword2",
	"consclosure": "literal2",
	"consstring": "keyword2",
	"copydata": "literal2",
	"copylist": "literal2",
	"copytree": "literal2",
	"database": "literal2",
	"datalength": "literal2",
	"dataword": "literal2",
	"ddecimal": "keyword1",
	"decimal": "keyword1",
	"define": "keyword1",
	"delete": "literal2",
	"device": "keyword1",
	"dlocal": "keyword1",
	"do": "keyword3",
	"else": "keyword3",
	"elseif": "keyword3",
	"enddefine": "keyword1",
	"endfor": "keyword3",
	"endforevery": "keyword3",
	"endif": "keyword3",
	"endinstance": "keyword1",
	"endrepeat": "keyword3",
	"endswitchon": "keyword3",
	"endwhile": "keyword3",
	"false": "literal2",
	"for": "keyword3",
	"forevery": "keyword3",
	"from": "keyword3",
	"goto": "keyword2",
	"hd": "literal2",
	"ident": "keyword1",
	"if": "keyword3",
	"in": "keyword3",
	"instance": "keyword1",
	"integer": "keyword1",
	"interrupt": "literal2",
	"intvec": "keyword1",
	"isboolean": "literal2",
	"isinteger": "literal2",
	"islist": "literal2",
	"isnumber": "literal2",
	"it": "literal2",
	"key": "keyword1",
	"last": "literal2",
	"length": "literal2",
	"listlength": "literal2",
	"lvars": "keyword1",
	"matches": "keyword2",
	"max": "literal2",
	"member": "literal2",
	"method": "keyword1",
	"mishap": "literal2",
	"nil": "keyword1",
	"nl": "literal2",
	"not": "literal2",
	"oneof": "literal2",
	"or": "keyword2",
	"pair": "keyword1",
	"partapply": "literal2",
	"pr": "literal2",
	"present": "literal2",
	"procedure": "keyword1",
	"process": "keyword1",
	"prologterm": "keyword1",
	"prologvar": "keyword1",
	"quitif": "literal2",
	"quitloop": "keyword2",
	"random": "literal2",
	"ratio": "keyword1",
	"readline": "literal2",
	"ref": "keyword1",
	"remove": "literal2",
	"repeat": "keyword3",
	"return": "keyword3",
	"rev": "literal2",
	"section": "keyword1",
	"shuffle": "literal2",
	"slot": "keyword1",
	"sort": "literal2",
	"step": "keyword3",
	"string": "keyword1",
	"subword": "literal2",
	"switchon": "keyword3",
	"syntax": "keyword1",
	"syssort": "literal2",
	"termin": "keyword1",
	"then": "keyword3",
	"till": "keyword3",
	"times": "keyword3",
	"tl": "literal2",
	"to": "keyword3",
	"trace": "keyword2",
	"true": "literal2",
	"undef": "literal2",
	"uses": "keyword2",
	"valof": "literal2",
	"vars": "keyword1",
	"vector": "keyword1",
	"while": "keyword3",
	"word": "keyword1",
}

# Keywords dict for pop11_list ruleset.
pop11_list_keywords_dict = {}

# Keywords dict for pop11_string ruleset.
pop11_string_keywords_dict = {}

# Keywords dict for pop11_comment ruleset.
pop11_comment_keywords_dict = {}

# Rules for pop11_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment1"', begin="/*", end="*/",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="COMMENT",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment1"', seq=";;;",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="'", end="'",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="STRING",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="STRING",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="`", end="`",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="STRING",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="[", end="]",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="LIST",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="{", end="}",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="LIST",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule7(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="![", end="]",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="LIST",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule8(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind='"function"',
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=True)

def rule9(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind='"label"',
        at_line_start=True, at_line_end=False, at_word_start=False, exclude_match=False)

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq="#_<",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq=">_#",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_mark_following(s, i, kind='"label"', 
        at_line_start=True, at_line_end=False, at_word_start=False, exclude_match=False)

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq=")",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq="(",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq=".",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq=",",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq=";",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq="^",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq="@",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq=":",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq="|",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<>",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule31(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule32(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for pop11_main ruleset.
pop11_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
	rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29,
	rule30, rule31, rule32, ]

# Rules for pop11_list ruleset.

def rule33(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="[", end="]",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="LIST",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule34(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="{", end="}",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="LIST",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule35(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="![", end="]",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="LIST",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule36(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="'", end="'",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="STRING",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule37(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="STRING",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule38(colorer, s, i):
    return colorer.match_span(s, i, kind='"null"', begin="%", end="%",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule39(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment1"', begin="/*", end="*/",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="COMMENT",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule40(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment1"', seq=";;;",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule41(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal2", seq="=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule42(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal2", seq="==",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule43(colorer, s, i):
    return colorer.match_mark_following(s, i, kind='"literal2"', 
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=False)

def rule44(colorer, s, i):
    return colorer.match_mark_following(s, i, kind='"literal2"', 
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=False)

# Rules list for pop11_list ruleset.
pop11_list_rules = [
	rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40, rule41, rule42,
	rule43, rule44, ]

# Rules for pop11_string ruleset.

# Rules list for pop11_string ruleset.
pop11_string_rules = []

# Rules for pop11_comment ruleset.

def rule45(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind='"label"',
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=False)

def rule46(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment1", seq="*",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

# Rules list for pop11_comment ruleset.
pop11_comment_rules = [
	rule45, rule46, ]

# Rules dict for pop11 mode.
rulesDict = {
	"pop11_comment": pop11_comment_rules,
	"pop11_list": pop11_list_rules,
	"pop11_main": pop11_main_rules,
	"pop11_string": pop11_string_rules,
}

# Import dict for pop11 mode.
importDict = {}

