# Leo colorizer control file for ada95 mode.

# Properties for ada95 mode.
properties = {
	"lineComment": "--",
}

# Keywords dict for ada95_main ruleset.
ada95_main_keywords_dict = {
	"abort": "keyword2",
	"abs": "keyword2",
	"abstract": "keyword2",
	"accept": "keyword2",
	"access": "keyword2",
	"address": "literal2",
	"aliased": "keyword2",
	"all": "keyword2",
	"and": "keyword2",
	"array": "keyword2",
	"at": "keyword2",
	"begin": "keyword2",
	"body": "keyword2",
	"boolean": "literal2",
	"case": "keyword2",
	"character": "literal2",
	"constant": "keyword2",
	"declare": "keyword2",
	"delay": "keyword2",
	"delta": "keyword2",
	"digits": "keyword2",
	"do": "keyword2",
	"duration": "literal2",
	"else": "keyword2",
	"elsif": "keyword2",
	"end": "keyword2",
	"entry": "keyword1",
	"exception": "keyword2",
	"exit": "keyword2",
	"false": "literal1",
	"float": "literal2",
	"for": "keyword2",
	"function": "keyword1",
	"goto": "keyword2",
	"if": "keyword2",
	"in": "keyword2",
	"integer": "literal2",
	"is": "keyword2",
	"latin_1": "literal2",
	"limited": "keyword2",
	"loop": "keyword2",
	"mod": "keyword2",
	"natural": "literal2",
	"new": "keyword2",
	"not": "keyword2",
	"null": "literal1",
	"or": "keyword2",
	"others": "keyword2",
	"out": "keyword2",
	"package": "keyword2",
	"positive": "literal2",
	"pragma": "keyword2",
	"private": "keyword2",
	"procedure": "keyword1",
	"protected": "keyword2",
	"raise": "keyword2",
	"range": "keyword2",
	"record": "keyword2",
	"rem": "keyword2",
	"renames": "keyword2",
	"requeue": "keyword2",
	"return": "keyword2",
	"select": "keyword2",
	"separate": "keyword2",
	"string": "literal2",
	"subtype": "keyword2",
	"tagged": "keyword2",
	"task": "keyword2",
	"terminate": "keyword2",
	"then": "keyword2",
	"time": "literal2",
	"true": "literal1",
	"type": "keyword2",
	"until": "keyword2",
	"use": "keyword2",
	"when": "keyword2",
	"while": "keyword2",
	"with": "keyword2",
	"xor": "keyword2",
}

# Dictionary of keywords dictionaries for ada95 mode.
keywordsDictDict = {
	"ada95_main": ada95_main_keywords_dict,
}

# Rules for ada95_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="--",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="..",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".all",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq="<>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="label", seq="<<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="label", seq=">>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="**",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'access",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'address",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'adjacent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'aft",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'alignment",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'base",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'bit_order",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'body_version",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule31(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'callable",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule32(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'caller",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule33(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'ceiling",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule34(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'class",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule35(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'component_size",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule36(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'composed",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule37(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'constrained",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule38(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'copy_size",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule39(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'count",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule40(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'definite",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule41(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'delta",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule42(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'denorm",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule43(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'digits",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule44(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'exponent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule45(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'external_tag",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule46(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'first",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule47(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'first_bit",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule48(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'floor",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule49(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'fore",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule50(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'fraction",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule51(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'genetic",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule52(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'identity",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule53(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'image",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule54(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'input",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule55(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'last",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule56(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'last_bit",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule57(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'leading_part",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule58(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'length",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule59(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'machine",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule60(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'machine_emax",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule61(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'machine_emin",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule62(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'machine_mantissa",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule63(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'machine_overflows",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule64(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'machine_radix",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule65(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'machine_rounds",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule66(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'max",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule67(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'max_size_in_storage_elements",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule68(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'min",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule69(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'model",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule70(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'model_emin",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule71(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'model_epsilon",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule72(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'model_mantissa",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule73(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'model_small",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule74(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'modulus",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule75(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'output",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule76(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'partition_id",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule77(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'pos",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule78(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'position",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule79(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'pred",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule80(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'range",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule81(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'read",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule82(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'remainder",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule83(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'round",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule84(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'rounding",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule85(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'safe_first",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule86(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'safe_last",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule87(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'scale",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule88(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'scaling",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule89(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'signed_zeros",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule90(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'size",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule91(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'small",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule92(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'storage_pool",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule93(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'storage_size",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule94(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'succ",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule95(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'tag",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule96(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'terminated",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule97(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'truncation",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule98(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'unbiased_rounding",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule99(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'unchecked_access",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule100(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'val",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule101(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'valid",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule102(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'value",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule103(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'version",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule104(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'wide_image",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule105(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'wide_value",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule106(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'wide_width",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule107(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'width",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule108(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="'write",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule109(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule110(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for ada95_main ruleset.
ada95_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
	rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29,
	rule30, rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39,
	rule40, rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49,
	rule50, rule51, rule52, rule53, rule54, rule55, rule56, rule57, rule58, rule59,
	rule60, rule61, rule62, rule63, rule64, rule65, rule66, rule67, rule68, rule69,
	rule70, rule71, rule72, rule73, rule74, rule75, rule76, rule77, rule78, rule79,
	rule80, rule81, rule82, rule83, rule84, rule85, rule86, rule87, rule88, rule89,
	rule90, rule91, rule92, rule93, rule94, rule95, rule96, rule97, rule98, rule99,
	rule100, rule101, rule102, rule103, rule104, rule105, rule106, rule107, rule108, rule109,
	rule110, ]

# Rules dict for ada95 mode.
rulesDict = {
	"ada95_main": ada95_main_rules,
}

# Import dict for ada95 mode.
importDict = {}

