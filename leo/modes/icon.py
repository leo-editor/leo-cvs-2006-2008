# Leo colorizer control file for icon mode.

# Properties for icon mode.
properties = {
	"indentCloseBrackets": "}",
	"indentOpenBrackets": "{",
	"lineComment": "#",
	"lineUpClosingBracket": "true",
	"wordBreakChars": "|.\\:,+-*/=?^!@%<>&",
}

# Keywords dict for icon_main ruleset.
icon_main_keywords_dict = {
	"$define": "keyword3",
	"$else": "keyword3",
	"$endif": "keyword3",
	"$error": "keyword3",
	"$ifdef": "keyword3",
	"$ifndef": "keyword3",
	"$include": "keyword3",
	"$line": "keyword3",
	"$undef": "keyword3",
	"&": "keyword3",
	"_MACINTOSH": "keyword3",
	"_MSDOS": "keyword3",
	"_MSDOS_386": "keyword3",
	"_MS_WINDOWS": "keyword3",
	"_MS_WINDOWS_NT": "keyword3",
	"_OS2": "keyword3",
	"_PIPES": "keyword3",
	"_PRESENTATION_MGR": "keyword3",
	"_SYSTEM_FUNCTION": "keyword3",
	"_UNIX": "keyword3",
	"_VMS": "keyword3",
	"_WINDOW_FUNCTIONS": "keyword3",
	"_X_WINDOW_SYSTEM": "keyword3",
	"allocated": "keyword3",
	"ascii": "keyword3",
	"break": "keyword2",
	"by": "keyword1",
	"case": "keyword1",
	"clock": "keyword3",
	"co-expression": "keyword4",
	"collections": "keyword3",
	"create": "keyword1",
	"cset": "keyword4",
	"current": "keyword3",
	"date": "keyword3",
	"dateline": "keyword3",
	"default": "keyword1",
	"digits": "keyword3",
	"do": "keyword1",
	"dump": "keyword3",
	"e": "keyword3",
	"else": "keyword1",
	"end": "keyword2",
	"error": "keyword3",
	"errornumber": "keyword3",
	"errortext": "keyword3",
	"errorvalue": "keyword3",
	"errout": "keyword3",
	"every": "keyword1",
	"fail": "keyword3",
	"features": "keyword3",
	"file": "keyword4",
	"global": "keyword2",
	"host": "keyword3",
	"if": "keyword1",
	"initial": "keyword1",
	"input": "keyword3",
	"integer": "keyword4",
	"invocable": "keyword2",
	"lcase": "keyword3",
	"letters": "keyword3",
	"level": "keyword3",
	"line": "keyword3",
	"link": "keyword2",
	"list": "keyword4",
	"local": "keyword2",
	"main": "keyword3",
	"next": "keyword1",
	"null": "keyword4",
	"of": "keyword1",
	"output": "keyword3",
	"phi": "keyword3",
	"pi": "keyword3",
	"pos": "keyword3",
	"procedure": "keyword2",
	"progname": "keyword3",
	"random": "keyword3",
	"real": "keyword4",
	"record": "keyword2",
	"regions": "keyword3",
	"repeat": "keyword1",
	"return": "keyword2",
	"set": "keyword4",
	"source": "keyword3",
	"static": "keyword2",
	"storage": "keyword3",
	"string": "keyword4",
	"subject": "keyword3",
	"suspend": "keyword2",
	"table": "keyword4",
	"then": "keyword1",
	"time": "keyword3",
	"to": "keyword1",
	"trace": "keyword3",
	"ucase": "keyword3",
	"until": "keyword1",
	"version": "keyword3",
	"while": "keyword1",
	"window": "keyword4",
}

# Rules for icon_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment1"', seq="#",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal2"', begin="'", end="'",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~===",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="===",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|||",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">>=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">>",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<<=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<<",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~==",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="==",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="||",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="++",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="**",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="--",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<->",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<-",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="op:=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":=:",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-:",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+:",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule31(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule32(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule33(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="not",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule34(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule35(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="?",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule36(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule37(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule38(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule39(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule40(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule41(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule42(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule43(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind='"function"',
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=True)

def rule44(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for icon_main ruleset.
icon_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
	rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29,
	rule30, rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39,
	rule40, rule41, rule42, rule43, rule44, ]

# Rules dict for icon mode.
rulesDict = {
	"icon_main": icon_main_rules,
}

# Import dict for icon mode.
importDict = {}

