# Leo colorizer control file for latex mode.

# Properties for latex mode.
properties = {
	"lineComment": "%",
	"noWordSep": "\",
}

# Keywords dict for latex_main ruleset.
latex_main_keywords_dict = {}

# Keywords dict for latex_mathmode ruleset.
latex_mathmode_keywords_dict = {}

# Keywords dict for latex_arraymode ruleset.
latex_arraymode_keywords_dict = {}

# Keywords dict for latex_tabularmode ruleset.
latex_tabularmode_keywords_dict = {}

# Keywords dict for latex_tabbingmode ruleset.
latex_tabbingmode_keywords_dict = {}

# Keywords dict for latex_picturemode ruleset.
latex_picturemode_keywords_dict = {}

# Dictionary of keywords dictionaries for latex mode.
keywordsDictDict = {
	"latex_arraymode": latex_arraymode_keywords_dict,
	"latex_main": latex_main_keywords_dict,
	"latex_mathmode": latex_mathmode_keywords_dict,
	"latex_picturemode": latex_picturemode_keywords_dict,
	"latex_tabbingmode": latex_tabbingmode_keywords_dict,
	"latex_tabularmode": latex_tabularmode_keywords_dict,
}

# Rules for latex_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_seq(s, i, kind="label", seq="__NormalMode__",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal4", begin="``", end="''",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="literal3", begin="`", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="`",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="function", seq="#1",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="function", seq="#2",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="function", seq="#3",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="function", seq="#4",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="function", seq="#5",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="function", seq="#6",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="function", seq="#7",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="function", seq="#8",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="function", seq="#9",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\tabs",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\tabset",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\tabsdone",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\cleartabs",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\settabs",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\tabalign",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\pageno",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\headline",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\footline",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\normalbottom",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\folio",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\nopagenumbers",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\advancepageno",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\pagebody",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule31(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\plainoutput",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule32(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\pagecontents",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule33(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\makeheadline",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule34(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\makefootline",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule35(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\dosupereject",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule36(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\footstrut",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule37(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\vfootnote",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule38(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\topins",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule39(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\topinsert",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule40(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\midinsert",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule41(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\pageinsert",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule42(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\endinsert",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule43(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\fivei",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule44(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\fiverm",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule45(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\fivesy",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule46(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\fivebf",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule47(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\seveni",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule48(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\sevenbf",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule49(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\sevensy",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule50(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\teni",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule51(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\oldstyle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule52(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\eqalign",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule53(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\eqalignno",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule54(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\leqalignno",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule55(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="$$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule56(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\beginsection",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule57(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\bye",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule58(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\magnification",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule59(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule60(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule61(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="_",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule62(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule63(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="$", end="$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="MathMode",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule64(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="\(", end="\)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="MathMode",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule65(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="\[", end="\]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="MathMode",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule66(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="\begin{math}", end="\end{math}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="MathMode",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule67(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="\begin{displaymath}", end="\end{displaymath}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="MathMode",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule68(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="\begin{equation}", end="\end{equation}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="MathMode",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule69(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="\ensuremath{", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="MathMode",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule70(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="\begin{eqnarray}", end="\end{eqnarray}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ArrayMode",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule71(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="\begin{eqnarray*}", end="\end{eqnarray*}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ArrayMode",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule72(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="\begin{tabular}", end="\end{tabular}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="TabularMode",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule73(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="\begin{tabular*}", end="\end{tabular*}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="TabularMode",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule74(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="\begin{tabbing}", end="\end{tabbing}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="TabbingMode",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule75(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="\begin{picture}", end="\end{picture}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="PictureMode",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule76(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule77(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule78(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule79(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="totalnumber",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule80(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="topnumber",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule81(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="tocdepth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule82(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="secnumdepth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule83(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="dbltopnumber",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule84(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule85(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\~{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule86(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule87(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule88(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule89(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule90(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\width",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule91(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\whiledo{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule92(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\v{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule93(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\vspace{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule94(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\vspace*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule95(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\vfill",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule96(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\verb*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule97(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\verb",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule98(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\value{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule99(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\v",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule100(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\u{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule101(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\usepackage{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule102(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\usepackage[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule103(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\usecounter{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule104(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\usebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule105(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\upshape",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule106(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\unboldmath{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule107(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\u",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule108(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\t{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule109(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\typeout{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule110(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\typein{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule111(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\typein[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule112(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\twocolumn[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule113(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\twocolumn",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule114(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ttfamily",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule115(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\totalheight",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule116(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\topsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule117(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\topfraction",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule118(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\today",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule119(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\title{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule120(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\tiny",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule121(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\thispagestyle{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule122(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\thinlines",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule123(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\thicklines",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule124(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\thanks{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule125(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\textwidth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule126(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textup{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule127(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\texttt{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule128(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textsl{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule129(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textsf{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule130(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textsc{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule131(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textrm{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule132(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textnormal{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule133(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textmd{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule134(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textit{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule135(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\textfraction",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule136(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\textfloatsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule137(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textcolor{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule138(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textbf{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule139(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\tableofcontents",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule140(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\tabcolsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule141(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\tabbingsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule142(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\t",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule143(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\symbol{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule144(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\suppressfloats[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule145(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\suppressfloats",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule146(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subsubsection{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule147(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subsubsection[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule148(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subsubsection*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule149(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subsection{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule150(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subsection[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule151(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subsection*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule152(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subparagraph{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule153(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subparagraph[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule154(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subparagraph*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule155(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\stretch{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule156(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\stepcounter{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule157(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\smallskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule158(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\small",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule159(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\slshape",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule160(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sloppy",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule161(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sffamily",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule162(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\settowidth{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule163(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\settoheight{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule164(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\settodepth{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule165(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\setlength{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule166(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\setcounter{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule167(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\section{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule168(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\section[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule169(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\section*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule170(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\scshape",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule171(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\scriptsize",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule172(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\scalebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule173(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\sbox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule174(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\savebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule175(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\rule{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule176(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\rule[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule177(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\rp,am{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule178(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\rotatebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule179(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rmfamily",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule180(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\rightmargin",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule181(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\reversemarginpar",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule182(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\resizebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule183(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\resizebox*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule184(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\renewenvironment{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule185(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\renewcommand{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule186(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\ref{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule187(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\refstepcounter",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule188(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\raisebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule189(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\raggedright",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule190(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\raggedleft",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule191(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\qbeziermax",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule192(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\providecommand{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule193(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\protect",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule194(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\printindex",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule195(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\pounds",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule196(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\part{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule197(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\partopsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule198(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\part[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule199(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\part*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule200(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\parskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule201(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\parsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule202(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\parindent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule203(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\parbox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule204(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\parbox[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule205(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\paragraph{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule206(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\paragraph[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule207(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\paragraph*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule208(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\par",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule209(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\pagestyle{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule210(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\pageref{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule211(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\pagenumbering{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule212(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\pagecolor{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule213(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\pagebreak[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule214(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\pagebreak",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule215(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\onecolumn",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule216(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\normalsize",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule217(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\normalmarginpar",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule218(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\normalfont",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule219(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\nopagebreak[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule220(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nopagebreak",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule221(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nonfrenchspacing",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule222(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\nolinebreak[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule223(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nolinebreak",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule224(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\noindent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule225(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\nocite{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule226(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\newtheorem{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule227(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\newsavebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule228(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\newpage",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule229(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\newlength{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule230(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\newenvironment{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule231(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\newcounter{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule232(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\newcommand{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule233(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\medskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule234(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\mdseries",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule235(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\mbox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule236(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\mbox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule237(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\mathindent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule238(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\mathindent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule239(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\markright{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule240(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\markboth{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule241(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\marginpar{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule242(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\marginparwidth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule243(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\marginparsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule244(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\marginparpush",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule245(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\marginpar[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule246(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\maketitle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule247(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\makelabel",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule248(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\makeindex",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule249(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\makeglossary",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule250(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\makebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule251(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\makebox[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule252(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\listparindent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule253(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\listoftables",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule254(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\listoffigures",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule255(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\listfiles",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule256(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\linewidth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule257(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\linethickness{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule258(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\linebreak[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule259(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\linebreak",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule260(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\lengthtest{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule261(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\leftmarginvi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule262(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\leftmarginv",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule263(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\leftmarginiv",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule264(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\leftmarginiii",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule265(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\leftmarginii",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule266(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\leftmargini",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule267(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\leftmargin",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule268(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\large",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule269(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\label{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule270(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\labelwidth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule271(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\labelsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule272(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\jot",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule273(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\itshape",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule274(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\itemsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule275(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\itemindent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule276(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\item[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule277(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\item",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule278(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\isodd{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule279(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\intextsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule280(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\input{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule281(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\index{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule282(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\indent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule283(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\include{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule284(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\includeonly{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule285(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\includegraphics{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule286(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\includegraphics[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule287(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\includegraphics*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule288(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\includegraphics*[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule289(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\ifthenelse{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule290(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\hyphenation{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule291(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\huge",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule292(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\hspace{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule293(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\hspace*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule294(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\hfill",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule295(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\height",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule296(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\glossary{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule297(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\fussy",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule298(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\frenchspacing",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule299(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\framebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule300(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\framebox[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule301(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\fragile",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule302(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\footnote{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule303(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\footnotetext{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule304(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\footnotetext[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule305(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\footnotesize",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule306(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\footnotesep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule307(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\footnoterule",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule308(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\footnotemark[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule309(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\footnotemark",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule310(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\footnote[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule311(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\fnsymbol{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule312(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\floatsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule313(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\floatpagefraction",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule314(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\fill",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule315(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\fcolorbox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule316(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\fbox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule317(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\fboxsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule318(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\fboxrule",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule319(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\equal{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule320(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\ensuremath{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule321(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\enlargethispage{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule322(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\enlargethispage*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule323(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\end{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule324(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\emph{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule325(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\d{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule326(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\doublerulesep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule327(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\documentclass{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule328(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\documentclass[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule329(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\depth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule330(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\definecolor{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule331(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ddag",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule332(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\dbltopfraction",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule333(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\dbltextfloatsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule334(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\dblfloatsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule335(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\dblfloatpagefraction",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule336(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\date{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule337(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\dag",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule338(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\d",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule339(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\c{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule340(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\copyright",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule341(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\columnwidth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule342(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\columnseprule",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule343(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\columnsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule344(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\color{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule345(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\colorbox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule346(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\clearpage",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule347(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\cleardoublepage",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule348(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\cite{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule349(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\cite[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule350(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\chapter{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule351(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\chapter[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule352(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\chapter*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule353(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\centering",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule354(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\caption{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule355(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\caption[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule356(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\c",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule357(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\b{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule358(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\bottomnumber",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule359(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\bottomfraction",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule360(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\boolean{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule361(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\boldmath{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule362(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule363(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\bibliography{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule364(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\bibliographystyle{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule365(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\bibindent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule366(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bfseries",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule367(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\belowdisplayskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule368(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\belowdisplayshortskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule369(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\begin{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule370(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\baselinestretch",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule371(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\baselineskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule372(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\b",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule373(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\author{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule374(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\arraystgretch",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule375(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\arrayrulewidth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule376(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\arraycolsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule377(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\arabic{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule378(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\appendix",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule379(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\alph{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule380(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\addvspace{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule381(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\addtolength{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule382(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\addtocounter{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule383(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\addtocontents{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule384(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\addcontentsline{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule385(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\abovedisplayskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule386(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\abovedisplayshortskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule387(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\`{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule388(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\`",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule389(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\_",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule390(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\^{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule391(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule392(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\\[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule393(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\\*[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule394(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\\*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule395(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\\",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule396(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\TeX",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule397(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\S",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule398(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\Roman{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule399(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\P",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule400(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Large",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule401(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\LaTeX",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule402(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\LARGE",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule403(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\H{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule404(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Huge",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule405(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\H",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule406(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\Alph{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule407(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule408(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\={",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule409(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule410(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\.{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule411(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\.",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule412(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule413(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\,",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule414(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\'{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule415(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule416(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule417(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule418(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule419(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule420(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\\"{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule421(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule422(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule423(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule424(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="---",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule425(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="--",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule426(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule427(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword4", pattern="\"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

# Rules dict for main ruleset.
rulesDict1 = {
	"\"": [rule4,rule5,],
	"#": [rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule59,],
	"$": [rule55,rule63,],
	"%": [rule1,],
	"&": [rule60,],
	"-": [rule424,rule425,rule426,],
	"[": [rule423,],
	"\": [rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27,rule28,rule29,rule30,rule31,rule32,rule33,rule34,rule35,rule36,rule37,rule38,rule39,rule40,rule41,rule42,rule43,rule44,rule45,rule46,rule47,rule48,rule49,rule50,rule51,rule52,rule53,rule54,rule56,rule57,rule58,rule62,rule64,rule65,rule66,rule67,rule68,rule69,rule70,rule71,rule72,rule73,rule74,rule75,rule85,rule86,rule87,rule88,rule89,rule90,rule91,rule92,rule93,rule94,rule95,rule96,rule97,rule98,rule99,rule100,rule101,rule102,rule103,rule104,rule105,rule106,rule107,rule108,rule109,rule110,rule111,rule112,rule113,rule114,rule115,rule116,rule117,rule118,rule119,rule120,rule121,rule122,rule123,rule124,rule125,rule126,rule127,rule128,rule129,rule130,rule131,rule132,rule133,rule134,rule135,rule136,rule137,rule138,rule139,rule140,rule141,rule142,rule143,rule144,rule145,rule146,rule147,rule148,rule149,rule150,rule151,rule152,rule153,rule154,rule155,rule156,rule157,rule158,rule159,rule160,rule161,rule162,rule163,rule164,rule165,rule166,rule167,rule168,rule169,rule170,rule171,rule172,rule173,rule174,rule175,rule176,rule177,rule178,rule179,rule180,rule181,rule182,rule183,rule184,rule185,rule186,rule187,rule188,rule189,rule190,rule191,rule192,rule193,rule194,rule195,rule196,rule197,rule198,rule199,rule200,rule201,rule202,rule203,rule204,rule205,rule206,rule207,rule208,rule209,rule210,rule211,rule212,rule213,rule214,rule215,rule216,rule217,rule218,rule219,rule220,rule221,rule222,rule223,rule224,rule225,rule226,rule227,rule228,rule229,rule230,rule231,rule232,rule233,rule234,rule235,rule236,rule237,rule238,rule239,rule240,rule241,rule242,rule243,rule244,rule245,rule246,rule247,rule248,rule249,rule250,rule251,rule252,rule253,rule254,rule255,rule256,rule257,rule258,rule259,rule260,rule261,rule262,rule263,rule264,rule265,rule266,rule267,rule268,rule269,rule270,rule271,rule272,rule273,rule274,rule275,rule276,rule277,rule278,rule279,rule280,rule281,rule282,rule283,rule284,rule285,rule286,rule287,rule288,rule289,rule290,rule291,rule292,rule293,rule294,rule295,rule296,rule297,rule298,rule299,rule300,rule301,rule302,rule303,rule304,rule305,rule306,rule307,rule308,rule309,rule310,rule311,rule312,rule313,rule314,rule315,rule316,rule317,rule318,rule319,rule320,rule321,rule322,rule323,rule324,rule325,rule326,rule327,rule328,rule329,rule330,rule331,rule332,rule333,rule334,rule335,rule336,rule337,rule338,rule339,rule340,rule341,rule342,rule343,rule344,rule345,rule346,rule347,rule348,rule349,rule350,rule351,rule352,rule353,rule354,rule355,rule356,rule357,rule358,rule359,rule360,rule361,rule362,rule363,rule364,rule365,rule366,rule367,rule368,rule369,rule370,rule371,rule372,rule373,rule374,rule375,rule376,rule377,rule378,rule379,rule380,rule381,rule382,rule383,rule384,rule385,rule386,rule387,rule388,rule389,rule390,rule391,rule392,rule393,rule394,rule395,rule396,rule397,rule398,rule399,rule400,rule401,rule402,rule403,rule404,rule405,rule406,rule407,rule408,rule409,rule410,rule411,rule412,rule413,rule414,rule415,rule416,rule417,rule418,rule419,rule420,rule421,rule422,rule427,],
	"]": [rule84,],
	"_": [rule0,rule61,],
	"`": [rule2,rule3,rule6,],
	"d": [rule83,],
	"s": [rule82,],
	"t": [rule79,rule80,rule81,],
	"{": [rule78,],
	"}": [rule77,],
	"~": [rule76,],
}

# Rules for latex_mathmode ruleset.

def rule428(colorer, s, i):
    return colorer.match_seq(s, i, kind="label", seq="__MathMode__",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule429(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule430(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="_",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule431(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule432(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\zeta",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule433(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\xi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule434(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\wr",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule435(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\wp",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule436(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\widetilde{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule437(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\widehat{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule438(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\wedge",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule439(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\veebar",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule440(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\vee",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule441(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\vec{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule442(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\vdots",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule443(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\vdash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule444(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\vartriangleright",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule445(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\vartriangleleft",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule446(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\vartriangle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule447(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\vartheta",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule448(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\varsupsetneqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule449(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\varsupsetneq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule450(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\varsubsetneqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule451(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\varsubsetneq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule452(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\varsigma",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule453(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\varrho",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule454(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\varpropto",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule455(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\varpi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule456(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\varphi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule457(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\varnothing",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule458(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\varkappa",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule459(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\varepsilon",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule460(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\vDash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule461(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\urcorner",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule462(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\upuparrows",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule463(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\upsilon",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule464(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\uplus",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule465(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\upharpoonright",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule466(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\upharpoonleft",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule467(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\updownarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule468(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\uparrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule469(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ulcorner",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule470(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\twoheadrightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule471(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\twoheadleftarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule472(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\trianglerighteq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule473(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\triangleright",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule474(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\triangleq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule475(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\trianglelefteq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule476(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\triangleleft",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule477(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\triangledown",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule478(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\triangle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule479(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\top",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule480(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\times",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule481(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\tilde{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule482(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\thicksim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule483(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\thickapprox",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule484(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\theta",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule485(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\therefore",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule486(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\text{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule487(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\textstyle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule488(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\tau",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule489(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\tanh",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule490(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\tan",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule491(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\swarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule492(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\surd",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule493(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\supsetneqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule494(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\supsetneq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule495(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\supseteqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule496(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\supseteq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule497(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\supset",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule498(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sum",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule499(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\succsim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule500(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\succnsim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule501(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\succnapprox",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule502(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\succeq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule503(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\succcurlyeq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule504(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\succapprox",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule505(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\succ",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule506(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\subsetneqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule507(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\subsetneq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule508(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\subseteqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule509(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\subseteq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule510(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\subset",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule511(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\star",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule512(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\stackrel{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule513(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\square",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule514(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sqsupseteq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule515(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sqsupset",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule516(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sqsubseteq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule517(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sqsubset",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule518(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\sqrt{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule519(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sqcup",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule520(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sqcap",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule521(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sphericalangle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule522(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\spadesuit",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule523(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\smile",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule524(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\smallsmile",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule525(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\smallsetminus",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule526(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\smallfrown",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule527(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sinh",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule528(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sin",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule529(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\simeq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule530(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule531(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sigma",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule532(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\shortparallel",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule533(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\shortmid",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule534(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sharp",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule535(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\setminus",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule536(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sec",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule537(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\searrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule538(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\scriptstyle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule539(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\scriptscriptstyle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule540(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rtimes",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule541(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\risingdotseq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule542(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule543(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rightthreetimes",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule544(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rightsquigarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule545(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rightrightarrows",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule546(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rightrightarrows",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule547(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rightleftharpoons",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule548(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rightleftharpoons",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule549(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rightleftarrows",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule550(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rightharpoonup",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule551(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rightharpoondown",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule552(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rightarrowtail",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule553(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule554(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule555(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule556(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\updownarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule557(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\uparrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule558(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\rfloor",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule559(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\rceil",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule560(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\rangle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule561(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\lfloor",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule562(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\lceil",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule563(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\langle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule564(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\downarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule565(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\backslash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule566(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\Updownarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule567(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\Uparrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule568(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\Downarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule569(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule570(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule571(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\right[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule572(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule573(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule574(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule575(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rho",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule576(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\psi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule577(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\propto",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule578(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\prod",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule579(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\prime",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule580(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\precsim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule581(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\precnsim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule582(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\precnapprox",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule583(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\preceq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule584(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\preccurlyeq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule585(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\precapprox",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule586(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\prec",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule587(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\pmod{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule588(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\pmb{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule589(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\pm",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule590(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\pitchfork",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule591(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\pi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule592(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\phi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule593(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\perp",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule594(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\partial",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule595(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\parallel",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule596(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\overline{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule597(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\otimes",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule598(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\oslash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule599(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\oplus",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule600(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ominus",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule601(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\omega",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule602(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\oint",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule603(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\odot",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule604(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nwarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule605(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nvdash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule606(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nvDash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule607(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nvDash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule608(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nu",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule609(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ntrianglerighteq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule610(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ntriangleright",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule611(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ntrianglelefteq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule612(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ntriangleleft",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule613(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nsupseteqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule614(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nsupseteq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule615(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nsucceq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule616(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nsucc",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule617(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nsubseteq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule618(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nsim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule619(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nshortparallel",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule620(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nshortmid",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule621(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nrightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule622(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\npreceq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule623(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nprec",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule624(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nparallel",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule625(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\notin",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule626(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nmid",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule627(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nless",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule628(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nleqslant",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule629(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nleqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule630(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nleq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule631(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nleftrightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule632(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nleftarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule633(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ni",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule634(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ngtr",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule635(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ngeqslant",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule636(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ngeqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule637(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ngeq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule638(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nexists",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule639(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\neq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule640(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\neg",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule641(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nearrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule642(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ncong",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule643(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\natural",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule644(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nabla",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule645(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nVDash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule646(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nRightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule647(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nLeftrightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule648(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nLeftarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule649(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\multimap",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule650(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\mu",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule651(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\mp",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule652(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\models",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule653(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\min",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule654(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\mid",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule655(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\mho",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule656(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\measuredangle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule657(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\max",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule658(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\mathtt{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule659(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\mathsf{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule660(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\mathrm{~~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule661(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\mathit{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule662(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\mathcal{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule663(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\mathbf{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule664(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\mapsto",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule665(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lvertneqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule666(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ltimes",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule667(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lrcorner",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule668(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lozenge",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule669(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\looparrowright",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule670(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\looparrowleft",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule671(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\longrightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule672(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\longmapsto",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule673(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\longleftrightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule674(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\longleftarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule675(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\log",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule676(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lnsim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule677(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lneqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule678(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lneq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule679(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lnapprox",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule680(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ln",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule681(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lll",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule682(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\llcorner",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule683(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ll",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule684(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\limsup",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule685(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\liminf",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule686(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule687(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lg",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule688(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lesssim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule689(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lessgtr",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule690(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lesseqqgtr",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule691(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lesseqgtr",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule692(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lessdot",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule693(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lessapprox",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule694(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leqslant",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule695(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule696(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule697(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule698(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leftthreetimes",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule699(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leftrightsquigarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule700(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leftrightharpoons",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule701(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leftrightarrows",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule702(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leftrightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule703(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leftleftarrows",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule704(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leftharpoonup",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule705(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leftharpoondown",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule706(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\lefteqn{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule707(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leftarrowtail",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule708(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leftarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule709(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule710(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule711(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\updownarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule712(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\uparrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule713(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\rfloor",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule714(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\rceil",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule715(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\rangle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule716(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\lfloor",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule717(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\lceil",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule718(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\langle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule719(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\downarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule720(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\backslash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule721(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\Updownarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule722(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\Uparrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule723(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\Downarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule724(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule725(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule726(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\left[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule727(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule728(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule729(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule730(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ldots",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule731(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lambda",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule732(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ker",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule733(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\kappa",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule734(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\jmath",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule735(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\jmath",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule736(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\iota",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule737(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\intercal",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule738(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\int",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule739(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\infty",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule740(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\inf",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule741(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\in",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule742(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\imath",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule743(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\imath",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule744(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\hslash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule745(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\hookrightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule746(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\hookleftarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule747(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\hom",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule748(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\heartsuit",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule749(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\hbar",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule750(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\hat{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule751(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gvertneqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule752(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gtrsim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule753(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gtrless",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule754(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gtreqqless",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule755(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gtreqless",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule756(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gtrdot",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule757(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gtrapprox",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule758(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\grave{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule759(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gnsim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule760(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gneqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule761(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gneq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule762(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gnapprox",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule763(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gnapprox",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule764(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gimel",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule765(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ggg",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule766(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gg",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule767(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\geqslant",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule768(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\geqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule769(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\geq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule770(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gcd",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule771(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gamma",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule772(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\frown",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule773(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\frak{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule774(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\frac{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule775(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\forall",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule776(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\flat",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule777(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\fallingdotseq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule778(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\exp",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule779(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\exists",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule780(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\eth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule781(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\eta",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule782(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\equiv",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule783(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\eqslantless",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule784(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\eqslantgtr",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule785(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\eqcirc",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule786(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\epsilon",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule787(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\ensuremath{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule788(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\end{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule789(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\emptyset",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule790(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ell",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule791(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\downharpoonright",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule792(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\downharpoonleft",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule793(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\downdownarrows",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule794(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\downarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule795(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\doublebarwedge",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule796(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\dot{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule797(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\dotplus",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule798(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\doteqdot",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule799(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\doteq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule800(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\divideontimes",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule801(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\div",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule802(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\displaystyle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule803(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\dim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule804(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\digamma",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule805(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\diamondsuit",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule806(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\diamond",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule807(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\diagup",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule808(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\diagdown",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule809(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\det",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule810(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\delta",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule811(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\deg",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule812(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\ddot{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule813(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ddots",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule814(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ddagger",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule815(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\dashv",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule816(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\dashrightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule817(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\dashleftarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule818(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\daleth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule819(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\dagger",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule820(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\curvearrowright",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule821(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\curvearrowleft",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule822(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\curlywedge",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule823(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\curlyvee",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule824(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\curlyeqsucc",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule825(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\curlyeqprec",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule826(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\cup",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule827(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\csc",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule828(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\coth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule829(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\cot",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule830(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\cosh",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule831(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\cos",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule832(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\coprod",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule833(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\cong",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule834(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\complement",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule835(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\clubsuit",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule836(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\circleddash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule837(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\circledcirc",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule838(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\circledast",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule839(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\circledS",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule840(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\circlearrowright",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule841(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\circlearrowleft",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule842(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\circeq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule843(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\circ",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule844(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\chi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule845(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\check{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule846(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\centerdot",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule847(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\cdots",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule848(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\cdot",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule849(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\cap",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule850(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bumpeq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule851(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bullet",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule852(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\breve{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule853(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\boxtimes",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule854(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\boxplus",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule855(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\boxminus",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule856(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\boxdot",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule857(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bowtie",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule858(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bot",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule859(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\boldsymbol{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule860(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bmod",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule861(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\blacktriangleright",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule862(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\blacktriangleleft",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule863(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\blacktriangledown",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule864(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\blacktriangle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule865(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\blacksquare",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule866(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\blacklozenge",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule867(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigwedge",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule868(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigvee",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule869(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\biguplus",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule870(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigtriangleup",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule871(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigtriangledown",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule872(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigstar",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule873(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigsqcup",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule874(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigotimes",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule875(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigoplus",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule876(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigodot",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule877(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigcup",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule878(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigcirc",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule879(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigcap",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule880(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\between",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule881(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\beth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule882(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\beta",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule883(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\begin{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule884(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\because",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule885(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\bar{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule886(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\barwedge",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule887(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\backslash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule888(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\backsimeq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule889(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\backsim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule890(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\backprime",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule891(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\asymp",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule892(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ast",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule893(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\arg",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule894(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\arctan",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule895(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\arcsin",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule896(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\arccos",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule897(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\approxeq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule898(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\approx",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule899(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\angle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule900(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\angle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule901(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\amalg",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule902(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\alpha",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule903(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\aleph",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule904(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\acute{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule905(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Xi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule906(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Vvdash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule907(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Vdash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule908(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Upsilon",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule909(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Updownarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule910(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Uparrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule911(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Theta",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule912(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Supset",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule913(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Subset",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule914(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Sigma",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule915(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Rsh",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule916(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Rightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule917(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Re",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule918(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Psi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule919(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Pr",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule920(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Pi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule921(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Phi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule922(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Omega",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule923(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Lsh",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule924(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Longrightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule925(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Longleftrightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule926(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Longleftarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule927(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Lleftarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule928(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Leftrightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule929(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Leftarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule930(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Lambda",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule931(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Im",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule932(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Gamma",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule933(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Game",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule934(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Finv",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule935(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Downarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule936(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Delta",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule937(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Cup",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule938(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Cap",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule939(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Bumpeq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule940(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\Bbb{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule941(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Bbbk",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule942(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\;",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule943(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\:",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule944(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\,",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule945(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule946(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule947(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="\begin{array}", end="\end{array}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ArrayMode",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule948(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword4", pattern="\"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

# Rules dict for mathmode ruleset.
rulesDict1 = {
	"%": [rule429,],
	"'": [rule946,],
	"\": [rule432,rule433,rule434,rule435,rule436,rule437,rule438,rule439,rule440,rule441,rule442,rule443,rule444,rule445,rule446,rule447,rule448,rule449,rule450,rule451,rule452,rule453,rule454,rule455,rule456,rule457,rule458,rule459,rule460,rule461,rule462,rule463,rule464,rule465,rule466,rule467,rule468,rule469,rule470,rule471,rule472,rule473,rule474,rule475,rule476,rule477,rule478,rule479,rule480,rule481,rule482,rule483,rule484,rule485,rule486,rule487,rule488,rule489,rule490,rule491,rule492,rule493,rule494,rule495,rule496,rule497,rule498,rule499,rule500,rule501,rule502,rule503,rule504,rule505,rule506,rule507,rule508,rule509,rule510,rule511,rule512,rule513,rule514,rule515,rule516,rule517,rule518,rule519,rule520,rule521,rule522,rule523,rule524,rule525,rule526,rule527,rule528,rule529,rule530,rule531,rule532,rule533,rule534,rule535,rule536,rule537,rule538,rule539,rule540,rule541,rule542,rule543,rule544,rule545,rule546,rule547,rule548,rule549,rule550,rule551,rule552,rule553,rule554,rule555,rule556,rule557,rule558,rule559,rule560,rule561,rule562,rule563,rule564,rule565,rule566,rule567,rule568,rule569,rule570,rule571,rule572,rule573,rule574,rule575,rule576,rule577,rule578,rule579,rule580,rule581,rule582,rule583,rule584,rule585,rule586,rule587,rule588,rule589,rule590,rule591,rule592,rule593,rule594,rule595,rule596,rule597,rule598,rule599,rule600,rule601,rule602,rule603,rule604,rule605,rule606,rule607,rule608,rule609,rule610,rule611,rule612,rule613,rule614,rule615,rule616,rule617,rule618,rule619,rule620,rule621,rule622,rule623,rule624,rule625,rule626,rule627,rule628,rule629,rule630,rule631,rule632,rule633,rule634,rule635,rule636,rule637,rule638,rule639,rule640,rule641,rule642,rule643,rule644,rule645,rule646,rule647,rule648,rule649,rule650,rule651,rule652,rule653,rule654,rule655,rule656,rule657,rule658,rule659,rule660,rule661,rule662,rule663,rule664,rule665,rule666,rule667,rule668,rule669,rule670,rule671,rule672,rule673,rule674,rule675,rule676,rule677,rule678,rule679,rule680,rule681,rule682,rule683,rule684,rule685,rule686,rule687,rule688,rule689,rule690,rule691,rule692,rule693,rule694,rule695,rule696,rule697,rule698,rule699,rule700,rule701,rule702,rule703,rule704,rule705,rule706,rule707,rule708,rule709,rule710,rule711,rule712,rule713,rule714,rule715,rule716,rule717,rule718,rule719,rule720,rule721,rule722,rule723,rule724,rule725,rule726,rule727,rule728,rule729,rule730,rule731,rule732,rule733,rule734,rule735,rule736,rule737,rule738,rule739,rule740,rule741,rule742,rule743,rule744,rule745,rule746,rule747,rule748,rule749,rule750,rule751,rule752,rule753,rule754,rule755,rule756,rule757,rule758,rule759,rule760,rule761,rule762,rule763,rule764,rule765,rule766,rule767,rule768,rule769,rule770,rule771,rule772,rule773,rule774,rule775,rule776,rule777,rule778,rule779,rule780,rule781,rule782,rule783,rule784,rule785,rule786,rule787,rule788,rule789,rule790,rule791,rule792,rule793,rule794,rule795,rule796,rule797,rule798,rule799,rule800,rule801,rule802,rule803,rule804,rule805,rule806,rule807,rule808,rule809,rule810,rule811,rule812,rule813,rule814,rule815,rule816,rule817,rule818,rule819,rule820,rule821,rule822,rule823,rule824,rule825,rule826,rule827,rule828,rule829,rule830,rule831,rule832,rule833,rule834,rule835,rule836,rule837,rule838,rule839,rule840,rule841,rule842,rule843,rule844,rule845,rule846,rule847,rule848,rule849,rule850,rule851,rule852,rule853,rule854,rule855,rule856,rule857,rule858,rule859,rule860,rule861,rule862,rule863,rule864,rule865,rule866,rule867,rule868,rule869,rule870,rule871,rule872,rule873,rule874,rule875,rule876,rule877,rule878,rule879,rule880,rule881,rule882,rule883,rule884,rule885,rule886,rule887,rule888,rule889,rule890,rule891,rule892,rule893,rule894,rule895,rule896,rule897,rule898,rule899,rule900,rule901,rule902,rule903,rule904,rule905,rule906,rule907,rule908,rule909,rule910,rule911,rule912,rule913,rule914,rule915,rule916,rule917,rule918,rule919,rule920,rule921,rule922,rule923,rule924,rule925,rule926,rule927,rule928,rule929,rule930,rule931,rule932,rule933,rule934,rule935,rule936,rule937,rule938,rule939,rule940,rule941,rule942,rule943,rule944,rule945,rule947,rule948,],
	"^": [rule431,],
	"_": [rule428,rule430,],
}

# Rules for latex_arraymode ruleset.

def rule949(colorer, s, i):
    return colorer.match_seq(s, i, kind="label", seq="__ArrayMode__",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule950(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule951(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="_",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule952(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule953(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\zeta",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule954(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\xi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule955(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\wr",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule956(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\wp",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule957(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\widetilde{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule958(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\widehat{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule959(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\wedge",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule960(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\vline",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule961(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\veebar",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule962(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\vee",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule963(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\vec{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule964(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\vdots",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule965(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\vdash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule966(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\vartriangleright",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule967(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\vartriangleleft",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule968(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\vartriangle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule969(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\vartheta",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule970(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\varsupsetneqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule971(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\varsupsetneq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule972(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\varsubsetneqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule973(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\varsubsetneq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule974(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\varsigma",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule975(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\varrho",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule976(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\varpropto",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule977(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\varpi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule978(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\varphi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule979(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\varnothing",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule980(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\varkappa",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule981(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\varepsilon",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule982(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\vDash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule983(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\urcorner",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule984(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\upuparrows",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule985(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\upsilon",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule986(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\uplus",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule987(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\upharpoonright",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule988(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\upharpoonleft",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule989(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\updownarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule990(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\uparrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule991(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ulcorner",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule992(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\twoheadrightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule993(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\twoheadleftarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule994(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\trianglerighteq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule995(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\triangleright",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule996(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\triangleq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule997(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\trianglelefteq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule998(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\triangleleft",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule999(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\triangledown",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1000(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\triangle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1001(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\top",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1002(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\times",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1003(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\tilde{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1004(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\thicksim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1005(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\thickapprox",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1006(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\theta",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1007(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\therefore",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1008(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\text{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1009(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\textstyle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1010(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\tau",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1011(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\tanh",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1012(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\tan",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1013(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\swarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1014(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\surd",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1015(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\supsetneqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1016(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\supsetneq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1017(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\supseteqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1018(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\supseteq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1019(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\supset",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1020(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sum",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1021(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\succsim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1022(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\succnsim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1023(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\succnapprox",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1024(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\succeq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1025(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\succcurlyeq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1026(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\succapprox",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1027(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\succ",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1028(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\subsetneqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1029(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\subsetneq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1030(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\subseteqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1031(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\subseteq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1032(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\subset",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1033(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\star",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1034(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\stackrel{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1035(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\square",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1036(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sqsupseteq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1037(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sqsupset",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1038(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sqsubseteq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1039(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sqsubset",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1040(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\sqrt{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1041(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sqcup",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1042(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sqcap",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1043(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sphericalangle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1044(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\spadesuit",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1045(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\smile",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1046(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\smallsmile",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1047(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\smallsetminus",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1048(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\smallfrown",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1049(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sinh",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1050(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sin",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1051(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\simeq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1052(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1053(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sigma",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1054(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\shortparallel",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1055(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\shortmid",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1056(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sharp",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1057(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\setminus",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1058(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sec",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1059(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\searrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1060(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\scriptstyle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1061(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\scriptscriptstyle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1062(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rtimes",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1063(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\risingdotseq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1064(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1065(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rightthreetimes",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1066(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rightsquigarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1067(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rightrightarrows",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1068(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rightrightarrows",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1069(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rightleftharpoons",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1070(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rightleftharpoons",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1071(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rightleftarrows",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1072(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rightharpoonup",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1073(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rightharpoondown",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1074(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rightarrowtail",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1075(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1076(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1077(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1078(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\updownarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1079(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\uparrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1080(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\rfloor",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1081(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\rceil",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1082(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\rangle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1083(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\lfloor",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1084(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\lceil",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1085(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\langle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1086(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\downarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1087(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\backslash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1088(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\Updownarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1089(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\Uparrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1090(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\Downarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1091(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1092(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right\(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1093(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\right[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1094(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1095(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1096(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\right(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1097(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rho",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1098(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\psi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1099(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\propto",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1100(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\prod",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1101(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\prime",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1102(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\precsim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1103(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\precnsim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1104(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\precnapprox",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1105(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\preceq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1106(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\preccurlyeq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1107(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\precapprox",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1108(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\prec",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1109(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\pmod{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1110(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\pmb{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1111(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\pm",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1112(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\pitchfork",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1113(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\pi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1114(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\phi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1115(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\perp",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1116(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\partial",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1117(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\parallel",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1118(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\overline{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1119(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\otimes",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1120(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\oslash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1121(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\oplus",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1122(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ominus",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1123(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\omega",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1124(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\oint",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1125(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\odot",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1126(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nwarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1127(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nvdash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1128(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nvDash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1129(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nvDash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1130(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nu",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1131(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ntrianglerighteq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1132(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ntriangleright",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1133(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ntrianglelefteq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1134(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ntriangleleft",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1135(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nsupseteqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1136(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nsupseteq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1137(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nsucceq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1138(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nsucc",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1139(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nsubseteq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1140(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nsim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1141(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nshortparallel",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1142(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nshortmid",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1143(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nrightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1144(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\npreceq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1145(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nprec",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1146(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nparallel",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1147(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\notin",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1148(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nmid",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1149(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nless",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1150(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nleqslant",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1151(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nleqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1152(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nleq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1153(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nleftrightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1154(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nleftarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1155(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ni",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1156(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ngtr",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1157(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ngeqslant",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1158(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ngeqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1159(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ngeq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1160(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nexists",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1161(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\neq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1162(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\neg",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1163(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nearrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1164(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ncong",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1165(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\natural",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1166(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nabla",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1167(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nVDash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1168(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nRightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1169(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nLeftrightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1170(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nLeftarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1171(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\multimap",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1172(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\multicolumn{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1173(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\mu",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1174(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\mp",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1175(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\models",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1176(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\min",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1177(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\mid",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1178(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\mho",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1179(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\measuredangle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1180(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\max",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1181(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\mathtt{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1182(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\mathsf{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1183(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\mathrm{~~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1184(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\mathit{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1185(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\mathcal{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1186(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\mathbf{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1187(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\mapsto",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1188(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lvertneqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1189(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ltimes",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1190(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lrcorner",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1191(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lozenge",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1192(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\looparrowright",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1193(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\looparrowleft",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1194(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\longrightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1195(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\longmapsto",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1196(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\longleftrightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1197(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\longleftarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1198(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\log",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1199(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lnsim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1200(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lneqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1201(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lneq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1202(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lnapprox",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1203(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ln",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1204(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lll",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1205(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\llcorner",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1206(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ll",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1207(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\limsup",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1208(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\liminf",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1209(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1210(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lg",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1211(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lesssim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1212(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lessgtr",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1213(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lesseqqgtr",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1214(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lesseqgtr",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1215(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lessdot",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1216(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lessapprox",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1217(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leqslant",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1218(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1219(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1220(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1221(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leftthreetimes",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1222(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leftrightsquigarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1223(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leftrightharpoons",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1224(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leftrightarrows",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1225(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leftrightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1226(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leftleftarrows",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1227(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leftharpoonup",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1228(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leftharpoondown",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1229(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\lefteqn{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1230(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leftarrowtail",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1231(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\leftarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1232(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1233(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1234(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\updownarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1235(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\uparrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1236(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\rfloor",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1237(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\rceil",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1238(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\rangle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1239(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\lfloor",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1240(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\lceil",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1241(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\langle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1242(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\downarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1243(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\backslash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1244(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\Updownarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1245(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\Uparrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1246(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\Downarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1247(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1248(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left\(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1249(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\left[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1250(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1251(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left)",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1252(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\left(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1253(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ldots",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1254(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\lambda",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1255(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ker",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1256(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\kappa",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1257(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\jmath",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1258(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\jmath",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1259(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\iota",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1260(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\intercal",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1261(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\int",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1262(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\infty",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1263(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\inf",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1264(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\in",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1265(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\imath",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1266(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\imath",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1267(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\hslash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1268(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\hookrightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1269(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\hookleftarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1270(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\hom",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1271(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\hline",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1272(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\heartsuit",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1273(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\hbar",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1274(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\hat{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1275(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gvertneqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1276(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gtrsim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1277(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gtrless",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1278(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gtreqqless",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1279(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gtreqless",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1280(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gtrdot",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1281(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gtrapprox",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1282(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\grave{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1283(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gnsim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1284(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gneqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1285(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gneq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1286(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gnapprox",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1287(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gnapprox",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1288(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gimel",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1289(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ggg",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1290(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gg",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1291(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\geqslant",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1292(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\geqq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1293(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\geq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1294(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gcd",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1295(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\gamma",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1296(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\frown",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1297(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\frak{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1298(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\frac{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1299(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\forall",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1300(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\flat",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1301(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\fallingdotseq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1302(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\exp",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1303(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\exists",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1304(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\eth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1305(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\eta",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1306(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\equiv",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1307(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\eqslantless",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1308(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\eqslantgtr",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1309(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\eqcirc",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1310(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\epsilon",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1311(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\ensuremath{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1312(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\end{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1313(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\emptyset",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1314(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ell",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1315(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\downharpoonright",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1316(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\downharpoonleft",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1317(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\downdownarrows",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1318(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\downarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1319(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\doublebarwedge",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1320(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\dot{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1321(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\dotplus",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1322(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\doteqdot",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1323(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\doteq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1324(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\divideontimes",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1325(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\div",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1326(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\displaystyle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1327(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\dim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1328(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\digamma",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1329(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\diamondsuit",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1330(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\diamond",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1331(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\diagup",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1332(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\diagdown",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1333(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\det",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1334(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\delta",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1335(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\deg",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1336(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\ddot{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1337(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ddots",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1338(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ddagger",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1339(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\dashv",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1340(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\dashrightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1341(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\dashleftarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1342(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\daleth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1343(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\dagger",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1344(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\curvearrowright",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1345(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\curvearrowleft",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1346(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\curlywedge",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1347(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\curlyvee",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1348(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\curlyeqsucc",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1349(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\curlyeqprec",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1350(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\cup",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1351(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\csc",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1352(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\coth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1353(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\cot",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1354(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\cosh",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1355(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\cos",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1356(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\coprod",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1357(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\cong",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1358(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\complement",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1359(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\clubsuit",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1360(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\cline{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1361(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\circleddash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1362(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\circledcirc",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1363(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\circledast",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1364(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\circledS",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1365(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\circlearrowright",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1366(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\circlearrowleft",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1367(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\circeq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1368(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\circ",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1369(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\chi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1370(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\check{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1371(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\centerdot",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1372(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\cdots",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1373(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\cdot",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1374(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\cap",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1375(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bumpeq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1376(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bullet",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1377(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\breve{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1378(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\boxtimes",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1379(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\boxplus",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1380(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\boxminus",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1381(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\boxdot",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1382(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bowtie",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1383(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bot",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1384(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\boldsymbol{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1385(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bmod",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1386(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\blacktriangleright",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1387(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\blacktriangleleft",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1388(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\blacktriangledown",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1389(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\blacktriangle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1390(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\blacksquare",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1391(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\blacklozenge",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1392(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigwedge",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1393(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigvee",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1394(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\biguplus",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1395(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigtriangleup",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1396(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigtriangledown",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1397(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigstar",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1398(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigsqcup",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1399(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigotimes",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1400(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigoplus",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1401(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigodot",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1402(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigcup",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1403(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigcirc",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1404(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigcap",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1405(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\between",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1406(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\beth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1407(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\beta",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1408(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\begin{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1409(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\because",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1410(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\bar{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1411(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\barwedge",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1412(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\backslash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1413(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\backsimeq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1414(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\backsim",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1415(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\backprime",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1416(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\asymp",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1417(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ast",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1418(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\arg",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1419(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\arctan",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1420(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\arcsin",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1421(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\arccos",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1422(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\approxeq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1423(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\approx",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1424(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\angle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1425(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\angle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1426(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\amalg",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1427(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\alpha",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1428(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\aleph",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1429(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\acute{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1430(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Xi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1431(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Vvdash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1432(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Vdash",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1433(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Upsilon",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1434(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Updownarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1435(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Uparrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1436(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Theta",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1437(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Supset",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1438(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Subset",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1439(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Sigma",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1440(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Rsh",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1441(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Rightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1442(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Re",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1443(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Psi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1444(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Pr",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1445(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Pi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1446(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Phi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1447(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Omega",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1448(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Lsh",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1449(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Longrightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1450(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Longleftrightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1451(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Longleftarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1452(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Lleftarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1453(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Leftrightarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1454(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Leftarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1455(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Lambda",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1456(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Im",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1457(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Gamma",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1458(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Game",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1459(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Finv",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1460(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Downarrow",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1461(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Delta",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1462(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Cup",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1463(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Cap",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1464(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Bumpeq",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1465(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\Bbb{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1466(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Bbbk",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1467(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\;",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1468(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\:",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1469(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\,",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1470(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1471(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1472(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1473(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword4", pattern="\"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

# Rules dict for arraymode ruleset.
rulesDict1 = {
	"%": [rule950,],
	"&": [rule1472,],
	"'": [rule1471,],
	"\": [rule953,rule954,rule955,rule956,rule957,rule958,rule959,rule960,rule961,rule962,rule963,rule964,rule965,rule966,rule967,rule968,rule969,rule970,rule971,rule972,rule973,rule974,rule975,rule976,rule977,rule978,rule979,rule980,rule981,rule982,rule983,rule984,rule985,rule986,rule987,rule988,rule989,rule990,rule991,rule992,rule993,rule994,rule995,rule996,rule997,rule998,rule999,rule1000,rule1001,rule1002,rule1003,rule1004,rule1005,rule1006,rule1007,rule1008,rule1009,rule1010,rule1011,rule1012,rule1013,rule1014,rule1015,rule1016,rule1017,rule1018,rule1019,rule1020,rule1021,rule1022,rule1023,rule1024,rule1025,rule1026,rule1027,rule1028,rule1029,rule1030,rule1031,rule1032,rule1033,rule1034,rule1035,rule1036,rule1037,rule1038,rule1039,rule1040,rule1041,rule1042,rule1043,rule1044,rule1045,rule1046,rule1047,rule1048,rule1049,rule1050,rule1051,rule1052,rule1053,rule1054,rule1055,rule1056,rule1057,rule1058,rule1059,rule1060,rule1061,rule1062,rule1063,rule1064,rule1065,rule1066,rule1067,rule1068,rule1069,rule1070,rule1071,rule1072,rule1073,rule1074,rule1075,rule1076,rule1077,rule1078,rule1079,rule1080,rule1081,rule1082,rule1083,rule1084,rule1085,rule1086,rule1087,rule1088,rule1089,rule1090,rule1091,rule1092,rule1093,rule1094,rule1095,rule1096,rule1097,rule1098,rule1099,rule1100,rule1101,rule1102,rule1103,rule1104,rule1105,rule1106,rule1107,rule1108,rule1109,rule1110,rule1111,rule1112,rule1113,rule1114,rule1115,rule1116,rule1117,rule1118,rule1119,rule1120,rule1121,rule1122,rule1123,rule1124,rule1125,rule1126,rule1127,rule1128,rule1129,rule1130,rule1131,rule1132,rule1133,rule1134,rule1135,rule1136,rule1137,rule1138,rule1139,rule1140,rule1141,rule1142,rule1143,rule1144,rule1145,rule1146,rule1147,rule1148,rule1149,rule1150,rule1151,rule1152,rule1153,rule1154,rule1155,rule1156,rule1157,rule1158,rule1159,rule1160,rule1161,rule1162,rule1163,rule1164,rule1165,rule1166,rule1167,rule1168,rule1169,rule1170,rule1171,rule1172,rule1173,rule1174,rule1175,rule1176,rule1177,rule1178,rule1179,rule1180,rule1181,rule1182,rule1183,rule1184,rule1185,rule1186,rule1187,rule1188,rule1189,rule1190,rule1191,rule1192,rule1193,rule1194,rule1195,rule1196,rule1197,rule1198,rule1199,rule1200,rule1201,rule1202,rule1203,rule1204,rule1205,rule1206,rule1207,rule1208,rule1209,rule1210,rule1211,rule1212,rule1213,rule1214,rule1215,rule1216,rule1217,rule1218,rule1219,rule1220,rule1221,rule1222,rule1223,rule1224,rule1225,rule1226,rule1227,rule1228,rule1229,rule1230,rule1231,rule1232,rule1233,rule1234,rule1235,rule1236,rule1237,rule1238,rule1239,rule1240,rule1241,rule1242,rule1243,rule1244,rule1245,rule1246,rule1247,rule1248,rule1249,rule1250,rule1251,rule1252,rule1253,rule1254,rule1255,rule1256,rule1257,rule1258,rule1259,rule1260,rule1261,rule1262,rule1263,rule1264,rule1265,rule1266,rule1267,rule1268,rule1269,rule1270,rule1271,rule1272,rule1273,rule1274,rule1275,rule1276,rule1277,rule1278,rule1279,rule1280,rule1281,rule1282,rule1283,rule1284,rule1285,rule1286,rule1287,rule1288,rule1289,rule1290,rule1291,rule1292,rule1293,rule1294,rule1295,rule1296,rule1297,rule1298,rule1299,rule1300,rule1301,rule1302,rule1303,rule1304,rule1305,rule1306,rule1307,rule1308,rule1309,rule1310,rule1311,rule1312,rule1313,rule1314,rule1315,rule1316,rule1317,rule1318,rule1319,rule1320,rule1321,rule1322,rule1323,rule1324,rule1325,rule1326,rule1327,rule1328,rule1329,rule1330,rule1331,rule1332,rule1333,rule1334,rule1335,rule1336,rule1337,rule1338,rule1339,rule1340,rule1341,rule1342,rule1343,rule1344,rule1345,rule1346,rule1347,rule1348,rule1349,rule1350,rule1351,rule1352,rule1353,rule1354,rule1355,rule1356,rule1357,rule1358,rule1359,rule1360,rule1361,rule1362,rule1363,rule1364,rule1365,rule1366,rule1367,rule1368,rule1369,rule1370,rule1371,rule1372,rule1373,rule1374,rule1375,rule1376,rule1377,rule1378,rule1379,rule1380,rule1381,rule1382,rule1383,rule1384,rule1385,rule1386,rule1387,rule1388,rule1389,rule1390,rule1391,rule1392,rule1393,rule1394,rule1395,rule1396,rule1397,rule1398,rule1399,rule1400,rule1401,rule1402,rule1403,rule1404,rule1405,rule1406,rule1407,rule1408,rule1409,rule1410,rule1411,rule1412,rule1413,rule1414,rule1415,rule1416,rule1417,rule1418,rule1419,rule1420,rule1421,rule1422,rule1423,rule1424,rule1425,rule1426,rule1427,rule1428,rule1429,rule1430,rule1431,rule1432,rule1433,rule1434,rule1435,rule1436,rule1437,rule1438,rule1439,rule1440,rule1441,rule1442,rule1443,rule1444,rule1445,rule1446,rule1447,rule1448,rule1449,rule1450,rule1451,rule1452,rule1453,rule1454,rule1455,rule1456,rule1457,rule1458,rule1459,rule1460,rule1461,rule1462,rule1463,rule1464,rule1465,rule1466,rule1467,rule1468,rule1469,rule1470,rule1473,],
	"^": [rule952,],
	"_": [rule949,rule951,],
}

# Rules for latex_tabularmode ruleset.

def rule1474(colorer, s, i):
    return colorer.match_seq(s, i, kind="label", seq="__TabularMode__",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1475(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1476(colorer, s, i):
    return colorer.match_span(s, i, kind="literal4", begin="``", end="''",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1477(colorer, s, i):
    return colorer.match_span(s, i, kind="literal3", begin="`", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1478(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1479(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1480(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="`",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1481(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1482(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1483(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1484(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="totalnumber",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1485(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="topnumber",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1486(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="tocdepth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1487(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="secnumdepth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1488(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="dbltopnumber",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1489(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1490(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\~{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1491(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1492(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1493(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1494(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1495(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\width",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1496(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\whiledo{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1497(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\v{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1498(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\vspace{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1499(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\vspace*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1500(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\vline",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1501(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\vfill",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1502(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\verb*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1503(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\verb",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1504(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\value{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1505(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\v",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1506(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\u{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1507(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\usepackage{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1508(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\usepackage[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1509(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\usecounter{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1510(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\usebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1511(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\upshape",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1512(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\unboldmath{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1513(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\u",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1514(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\t{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1515(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\typeout{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1516(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\typein{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1517(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\typein[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1518(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\twocolumn[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1519(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\twocolumn",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1520(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ttfamily",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1521(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\totalheight",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1522(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\topsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1523(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\topfraction",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1524(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\today",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1525(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\title{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1526(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\tiny",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1527(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\thispagestyle{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1528(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\thinlines",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1529(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\thicklines",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1530(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\thanks{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1531(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\textwidth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1532(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textup{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1533(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\texttt{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1534(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textsl{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1535(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textsf{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1536(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textsc{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1537(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textrm{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1538(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textnormal{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1539(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textmd{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1540(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textit{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1541(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\textfraction",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1542(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\textfloatsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1543(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textcolor{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1544(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textbf{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1545(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\tableofcontents",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1546(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\tabcolsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1547(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\tabbingsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1548(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\t",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1549(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\symbol{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1550(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\suppressfloats[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1551(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\suppressfloats",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1552(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subsubsection{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1553(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subsubsection[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1554(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subsubsection*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1555(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subsection{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1556(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subsection[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1557(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subsection*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1558(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subparagraph{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1559(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subparagraph[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1560(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subparagraph*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1561(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\stretch{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1562(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\stepcounter{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1563(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\smallskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1564(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\small",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1565(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\slshape",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1566(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sloppy",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1567(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sffamily",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1568(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\settowidth{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1569(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\settoheight{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1570(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\settodepth{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1571(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\setlength{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1572(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\setcounter{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1573(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\section{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1574(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\section[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1575(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\section*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1576(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\scshape",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1577(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\scriptsize",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1578(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\scalebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1579(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\sbox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1580(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\savebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1581(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\rule{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1582(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\rule[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1583(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\rp,am{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1584(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\rotatebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1585(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rmfamily",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1586(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\rightmargin",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1587(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\reversemarginpar",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1588(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\resizebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1589(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\resizebox*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1590(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\renewenvironment{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1591(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\renewcommand{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1592(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\ref{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1593(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\refstepcounter",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1594(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\raisebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1595(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\raggedright",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1596(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\raggedleft",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1597(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\qbeziermax",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1598(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\providecommand{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1599(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\protect",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1600(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\printindex",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1601(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\pounds",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1602(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\part{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1603(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\partopsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1604(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\part[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1605(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\part*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1606(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\parskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1607(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\parsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1608(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\parindent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1609(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\parbox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1610(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\parbox[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1611(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\paragraph{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1612(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\paragraph[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1613(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\paragraph*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1614(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\par",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1615(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\pagestyle{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1616(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\pageref{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1617(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\pagenumbering{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1618(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\pagecolor{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1619(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\pagebreak[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1620(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\pagebreak",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1621(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\onecolumn",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1622(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\normalsize",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1623(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\normalmarginpar",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1624(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\normalfont",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1625(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\nopagebreak[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1626(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nopagebreak",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1627(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nonfrenchspacing",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1628(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\nolinebreak[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1629(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nolinebreak",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1630(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\noindent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1631(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\nocite{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1632(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\newtheorem{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1633(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\newsavebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1634(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\newpage",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1635(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\newlength{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1636(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\newenvironment{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1637(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\newcounter{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1638(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\newcommand{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1639(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\multicolumn{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1640(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\medskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1641(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\mdseries",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1642(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\mbox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1643(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\mbox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1644(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\mathindent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1645(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\mathindent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1646(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\markright{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1647(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\markboth{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1648(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\marginpar{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1649(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\marginparwidth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1650(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\marginparsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1651(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\marginparpush",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1652(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\marginpar[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1653(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\maketitle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1654(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\makelabel",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1655(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\makeindex",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1656(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\makeglossary",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1657(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\makebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1658(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\makebox[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1659(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\listparindent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1660(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\listoftables",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1661(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\listoffigures",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1662(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\listfiles",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1663(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\linewidth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1664(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\linethickness{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1665(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\linebreak[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1666(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\linebreak",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1667(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\lengthtest{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1668(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\leftmarginvi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1669(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\leftmarginv",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1670(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\leftmarginiv",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1671(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\leftmarginiii",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1672(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\leftmarginii",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1673(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\leftmargini",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1674(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\leftmargin",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1675(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\large",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1676(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\label{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1677(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\labelwidth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1678(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\labelsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1679(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\jot",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1680(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\itshape",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1681(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\itemsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1682(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\itemindent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1683(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\item[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1684(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\item",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1685(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\isodd{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1686(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\intextsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1687(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\input{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1688(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\index{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1689(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\indent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1690(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\include{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1691(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\includeonly{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1692(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\includegraphics{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1693(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\includegraphics[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1694(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\includegraphics*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1695(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\includegraphics*[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1696(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\ifthenelse{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1697(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\hyphenation{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1698(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\huge",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1699(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\hspace{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1700(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\hspace*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1701(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\hline",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1702(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\hfill",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1703(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\height",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1704(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\glossary{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1705(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\fussy",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1706(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\frenchspacing",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1707(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\framebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1708(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\framebox[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1709(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\fragile",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1710(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\footnote{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1711(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\footnotetext{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1712(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\footnotetext[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1713(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\footnotesize",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1714(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\footnotesep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1715(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\footnoterule",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1716(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\footnotemark[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1717(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\footnotemark",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1718(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\footnote[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1719(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\fnsymbol{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1720(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\floatsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1721(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\floatpagefraction",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1722(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\fill",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1723(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\fcolorbox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1724(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\fbox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1725(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\fboxsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1726(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\fboxrule",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1727(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\equal{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1728(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\ensuremath{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1729(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\enlargethispage{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1730(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\enlargethispage*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1731(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\end{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1732(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\emph{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1733(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\d{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1734(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\doublerulesep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1735(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\documentclass{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1736(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\documentclass[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1737(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\depth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1738(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\definecolor{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1739(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ddag",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1740(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\dbltopfraction",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1741(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\dbltextfloatsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1742(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\dblfloatsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1743(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\dblfloatpagefraction",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1744(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\date{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1745(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\dag",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1746(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\d",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1747(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\c{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1748(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\copyright",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1749(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\columnwidth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1750(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\columnseprule",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1751(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\columnsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1752(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\color{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1753(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\colorbox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1754(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\cline{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1755(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\clearpage",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1756(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\cleardoublepage",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1757(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\cite{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1758(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\cite[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1759(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\chapter{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1760(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\chapter[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1761(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\chapter*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1762(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\centering",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1763(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\caption{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1764(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\caption[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1765(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\c",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1766(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\b{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1767(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\bottomnumber",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1768(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\bottomfraction",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1769(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\boolean{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1770(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\boldmath{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1771(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1772(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\bibliography{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1773(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\bibliographystyle{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1774(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\bibindent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1775(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bfseries",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1776(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\belowdisplayskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1777(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\belowdisplayshortskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1778(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\begin{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1779(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\baselinestretch",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1780(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\baselineskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1781(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\b",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1782(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\author{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1783(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\arraystgretch",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1784(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\arrayrulewidth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1785(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\arraycolsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1786(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\arabic{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1787(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\appendix",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1788(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\alph{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1789(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\addvspace{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1790(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\addtolength{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1791(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\addtocounter{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1792(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\addtocontents{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1793(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\addcontentsline{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1794(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\abovedisplayskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1795(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\abovedisplayshortskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1796(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\`{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1797(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\`",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1798(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\_",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1799(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\^{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1800(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1801(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\\[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1802(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\\*[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1803(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\\*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1804(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\\",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1805(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\TeX",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1806(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\S",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1807(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\Roman{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1808(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\P",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1809(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Large",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1810(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\LaTeX",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1811(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\LARGE",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1812(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\H{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1813(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Huge",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1814(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\H",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1815(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\Alph{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1816(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1817(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\={",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1818(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1819(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\.{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1820(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\.",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1821(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1822(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\,",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1823(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\'{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1824(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1825(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1826(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1827(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1828(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1829(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\\"{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1830(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1831(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1832(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1833(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="---",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1834(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="--",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1835(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1836(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1837(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword4", pattern="\"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

# Rules dict for tabularmode ruleset.
rulesDict1 = {
	"\"": [rule1478,rule1479,],
	"%": [rule1475,],
	"&": [rule1836,],
	"-": [rule1833,rule1834,rule1835,],
	"[": [rule1832,],
	"\": [rule1490,rule1491,rule1492,rule1493,rule1494,rule1495,rule1496,rule1497,rule1498,rule1499,rule1500,rule1501,rule1502,rule1503,rule1504,rule1505,rule1506,rule1507,rule1508,rule1509,rule1510,rule1511,rule1512,rule1513,rule1514,rule1515,rule1516,rule1517,rule1518,rule1519,rule1520,rule1521,rule1522,rule1523,rule1524,rule1525,rule1526,rule1527,rule1528,rule1529,rule1530,rule1531,rule1532,rule1533,rule1534,rule1535,rule1536,rule1537,rule1538,rule1539,rule1540,rule1541,rule1542,rule1543,rule1544,rule1545,rule1546,rule1547,rule1548,rule1549,rule1550,rule1551,rule1552,rule1553,rule1554,rule1555,rule1556,rule1557,rule1558,rule1559,rule1560,rule1561,rule1562,rule1563,rule1564,rule1565,rule1566,rule1567,rule1568,rule1569,rule1570,rule1571,rule1572,rule1573,rule1574,rule1575,rule1576,rule1577,rule1578,rule1579,rule1580,rule1581,rule1582,rule1583,rule1584,rule1585,rule1586,rule1587,rule1588,rule1589,rule1590,rule1591,rule1592,rule1593,rule1594,rule1595,rule1596,rule1597,rule1598,rule1599,rule1600,rule1601,rule1602,rule1603,rule1604,rule1605,rule1606,rule1607,rule1608,rule1609,rule1610,rule1611,rule1612,rule1613,rule1614,rule1615,rule1616,rule1617,rule1618,rule1619,rule1620,rule1621,rule1622,rule1623,rule1624,rule1625,rule1626,rule1627,rule1628,rule1629,rule1630,rule1631,rule1632,rule1633,rule1634,rule1635,rule1636,rule1637,rule1638,rule1639,rule1640,rule1641,rule1642,rule1643,rule1644,rule1645,rule1646,rule1647,rule1648,rule1649,rule1650,rule1651,rule1652,rule1653,rule1654,rule1655,rule1656,rule1657,rule1658,rule1659,rule1660,rule1661,rule1662,rule1663,rule1664,rule1665,rule1666,rule1667,rule1668,rule1669,rule1670,rule1671,rule1672,rule1673,rule1674,rule1675,rule1676,rule1677,rule1678,rule1679,rule1680,rule1681,rule1682,rule1683,rule1684,rule1685,rule1686,rule1687,rule1688,rule1689,rule1690,rule1691,rule1692,rule1693,rule1694,rule1695,rule1696,rule1697,rule1698,rule1699,rule1700,rule1701,rule1702,rule1703,rule1704,rule1705,rule1706,rule1707,rule1708,rule1709,rule1710,rule1711,rule1712,rule1713,rule1714,rule1715,rule1716,rule1717,rule1718,rule1719,rule1720,rule1721,rule1722,rule1723,rule1724,rule1725,rule1726,rule1727,rule1728,rule1729,rule1730,rule1731,rule1732,rule1733,rule1734,rule1735,rule1736,rule1737,rule1738,rule1739,rule1740,rule1741,rule1742,rule1743,rule1744,rule1745,rule1746,rule1747,rule1748,rule1749,rule1750,rule1751,rule1752,rule1753,rule1754,rule1755,rule1756,rule1757,rule1758,rule1759,rule1760,rule1761,rule1762,rule1763,rule1764,rule1765,rule1766,rule1767,rule1768,rule1769,rule1770,rule1771,rule1772,rule1773,rule1774,rule1775,rule1776,rule1777,rule1778,rule1779,rule1780,rule1781,rule1782,rule1783,rule1784,rule1785,rule1786,rule1787,rule1788,rule1789,rule1790,rule1791,rule1792,rule1793,rule1794,rule1795,rule1796,rule1797,rule1798,rule1799,rule1800,rule1801,rule1802,rule1803,rule1804,rule1805,rule1806,rule1807,rule1808,rule1809,rule1810,rule1811,rule1812,rule1813,rule1814,rule1815,rule1816,rule1817,rule1818,rule1819,rule1820,rule1821,rule1822,rule1823,rule1824,rule1825,rule1826,rule1827,rule1828,rule1829,rule1830,rule1831,rule1837,],
	"]": [rule1489,],
	"_": [rule1474,],
	"`": [rule1476,rule1477,rule1480,],
	"d": [rule1488,],
	"s": [rule1487,],
	"t": [rule1484,rule1485,rule1486,],
	"{": [rule1483,],
	"}": [rule1482,],
	"~": [rule1481,],
}

# Rules for latex_tabbingmode ruleset.

def rule1838(colorer, s, i):
    return colorer.match_seq(s, i, kind="label", seq="__TabbingMode__",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1839(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1840(colorer, s, i):
    return colorer.match_span(s, i, kind="literal4", begin="``", end="''",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1841(colorer, s, i):
    return colorer.match_span(s, i, kind="literal3", begin="`", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1842(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1843(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1844(colorer, s, i):
    return colorer.match_seq(s, i, kind="invalid", seq="`",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1845(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1846(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1847(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1848(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="totalnumber",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1849(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="topnumber",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1850(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="tocdepth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1851(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="secnumdepth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1852(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="dbltopnumber",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1853(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1854(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\~{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1855(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1856(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1857(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1858(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1859(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\width",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1860(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\whiledo{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1861(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\v{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1862(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\vspace{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1863(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\vspace*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1864(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\vfill",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1865(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\verb*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1866(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\verb",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1867(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\value{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1868(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\v",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1869(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\u{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1870(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\usepackage{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1871(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\usepackage[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1872(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\usecounter{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1873(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\usebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1874(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\upshape",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1875(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\unboldmath{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1876(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\u",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1877(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\t{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1878(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\typeout{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1879(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\typein{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1880(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\typein[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1881(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\twocolumn[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1882(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\twocolumn",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1883(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ttfamily",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1884(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\totalheight",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1885(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\topsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1886(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\topfraction",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1887(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\today",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1888(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\title{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1889(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\tiny",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1890(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\thispagestyle{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1891(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\thinlines",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1892(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\thicklines",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1893(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\thanks{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1894(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\textwidth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1895(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textup{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1896(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\texttt{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1897(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textsl{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1898(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textsf{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1899(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textsc{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1900(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textrm{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1901(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textnormal{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1902(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textmd{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1903(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textit{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1904(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\textfraction",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1905(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\textfloatsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1906(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textcolor{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1907(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\textbf{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1908(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\tableofcontents",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1909(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\tabcolsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1910(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\tabbingsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1911(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\t",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1912(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\symbol{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1913(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\suppressfloats[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1914(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\suppressfloats",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1915(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subsubsection{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1916(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subsubsection[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1917(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subsubsection*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1918(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subsection{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1919(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subsection[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1920(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subsection*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1921(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subparagraph{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1922(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subparagraph[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1923(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\subparagraph*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1924(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\stretch{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1925(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\stepcounter{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1926(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\smallskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1927(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\small",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1928(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\slshape",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1929(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sloppy",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1930(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\sffamily",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1931(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\settowidth{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1932(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\settoheight{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1933(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\settodepth{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1934(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\setlength{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1935(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\setcounter{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1936(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\section{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1937(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\section[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1938(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\section*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1939(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\scshape",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1940(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\scriptsize",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1941(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\scalebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1942(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\sbox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1943(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\savebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1944(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\rule{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1945(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\rule[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1946(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\rp,am{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1947(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\rotatebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1948(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\rmfamily",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1949(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\rightmargin",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1950(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\reversemarginpar",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1951(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\resizebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1952(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\resizebox*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1953(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\renewenvironment{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1954(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\renewcommand{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1955(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\ref{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1956(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\refstepcounter",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1957(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\raisebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1958(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\raggedright",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1959(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\raggedleft",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1960(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\qbeziermax",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1961(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\pushtabs",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1962(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\providecommand{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1963(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\protect",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1964(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\printindex",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1965(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\pounds",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1966(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\poptabs",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1967(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\part{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1968(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\partopsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1969(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\part[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1970(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\part*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1971(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\parskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1972(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\parsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1973(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\parindent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1974(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\parbox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1975(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\parbox[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1976(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\paragraph{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1977(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\paragraph[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1978(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\paragraph*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1979(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\par",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1980(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\pagestyle{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1981(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\pageref{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1982(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\pagenumbering{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1983(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\pagecolor{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1984(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\pagebreak[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1985(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\pagebreak",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1986(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\onecolumn",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1987(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\normalsize",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1988(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\normalmarginpar",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1989(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\normalfont",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1990(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\nopagebreak[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1991(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nopagebreak",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1992(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nonfrenchspacing",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1993(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\nolinebreak[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1994(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\nolinebreak",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1995(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\noindent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1996(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\nocite{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1997(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\newtheorem{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1998(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\newsavebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule1999(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\newpage",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2000(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\newlength{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2001(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\newenvironment{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2002(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\newcounter{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2003(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\newcommand{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2004(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\medskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2005(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\mdseries",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2006(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\mbox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2007(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\mbox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2008(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\mathindent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2009(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\mathindent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2010(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\markright{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2011(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\markboth{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2012(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\marginpar{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2013(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\marginparwidth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2014(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\marginparsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2015(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\marginparpush",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2016(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\marginpar[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2017(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\maketitle",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2018(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\makelabel",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2019(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\makeindex",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2020(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\makeglossary",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2021(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\makebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2022(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\makebox[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2023(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\listparindent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2024(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\listoftables",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2025(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\listoffigures",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2026(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\listfiles",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2027(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\linewidth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2028(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\linethickness{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2029(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\linebreak[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2030(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\linebreak",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2031(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\lengthtest{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2032(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\leftmarginvi",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2033(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\leftmarginv",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2034(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\leftmarginiv",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2035(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\leftmarginiii",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2036(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\leftmarginii",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2037(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\leftmargini",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2038(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\leftmargin",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2039(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\large",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2040(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\label{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2041(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\labelwidth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2042(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\labelsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2043(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\kill",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2044(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\jot",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2045(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\itshape",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2046(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\itemsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2047(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\itemindent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2048(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\item[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2049(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\item",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2050(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\isodd{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2051(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\intextsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2052(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\input{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2053(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\index{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2054(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\indent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2055(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\include{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2056(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\includeonly{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2057(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\includegraphics{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2058(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\includegraphics[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2059(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\includegraphics*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2060(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\includegraphics*[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2061(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\ifthenelse{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2062(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\hyphenation{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2063(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\huge",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2064(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\hspace{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2065(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\hspace*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2066(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\hfill",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2067(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\height",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2068(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\glossary{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2069(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\fussy",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2070(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\frenchspacing",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2071(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\framebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2072(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\framebox[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2073(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\fragile",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2074(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\footnote{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2075(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\footnotetext{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2076(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\footnotetext[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2077(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\footnotesize",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2078(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\footnotesep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2079(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\footnoterule",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2080(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\footnotemark[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2081(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\footnotemark",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2082(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\footnote[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2083(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\fnsymbol{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2084(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\floatsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2085(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\floatpagefraction",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2086(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\fill",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2087(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\fcolorbox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2088(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\fbox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2089(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\fboxsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2090(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\fboxrule",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2091(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\equal{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2092(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\ensuremath{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2093(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\enlargethispage{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2094(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\enlargethispage*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2095(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\end{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2096(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\emph{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2097(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\d{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2098(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\doublerulesep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2099(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\documentclass{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2100(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\documentclass[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2101(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\depth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2102(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\definecolor{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2103(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\ddag",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2104(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\dbltopfraction",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2105(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\dbltextfloatsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2106(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\dblfloatsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2107(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\dblfloatpagefraction",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2108(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\date{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2109(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\dag",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2110(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\d",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2111(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\c{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2112(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\copyright",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2113(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\columnwidth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2114(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\columnseprule",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2115(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\columnsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2116(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\color{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2117(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\colorbox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2118(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\clearpage",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2119(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\cleardoublepage",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2120(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\cite{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2121(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\cite[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2122(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\chapter{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2123(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\chapter[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2124(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\chapter*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2125(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\centering",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2126(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\caption{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2127(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\caption[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2128(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\c",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2129(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\b{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2130(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\bottomnumber",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2131(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\bottomfraction",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2132(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\boolean{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2133(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\boldmath{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2134(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bigskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2135(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\bibliography{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2136(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\bibliographystyle{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2137(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\bibindent",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2138(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\bfseries",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2139(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\belowdisplayskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2140(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\belowdisplayshortskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2141(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\begin{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2142(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\baselinestretch",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2143(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\baselineskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2144(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\b",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2145(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\author{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2146(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\arraystgretch",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2147(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\arrayrulewidth",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2148(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\arraycolsep",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2149(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\arabic{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2150(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\appendix",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2151(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\alph{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2152(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\addvspace{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2153(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\addtolength{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2154(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\addtocounter{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2155(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\addtocontents{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2156(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\addcontentsline{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2157(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\abovedisplayskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2158(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword3", seq="\abovedisplayshortskip",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2159(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\a`",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2160(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\a=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2161(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\a'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2162(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\`{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2163(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\`",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2164(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\`",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2165(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\_",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2166(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\^{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2167(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2168(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\\[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2169(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\\*[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2170(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\\*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2171(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\\",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2172(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\\",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2173(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\TeX",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2174(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\S",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2175(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\Roman{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2176(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\P",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2177(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Large",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2178(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\LaTeX",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2179(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\LARGE",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2180(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\H{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2181(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\Huge",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2182(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\H",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2183(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\Alph{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2184(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2185(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\={",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2186(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2187(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2188(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\.{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2189(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\.",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2190(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2191(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2192(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\,",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2193(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2194(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\'{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2195(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2196(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2197(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2198(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2199(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2200(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2201(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2202(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2203(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\\"{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2204(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2205(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2206(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2207(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="---",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2208(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="--",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2209(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2210(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword4", pattern="\"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

# Rules dict for tabbingmode ruleset.
rulesDict1 = {
	"\"": [rule1842,rule1843,],
	"%": [rule1839,],
	"-": [rule2207,rule2208,rule2209,],
	"[": [rule2206,],
	"\": [rule1854,rule1855,rule1856,rule1857,rule1858,rule1859,rule1860,rule1861,rule1862,rule1863,rule1864,rule1865,rule1866,rule1867,rule1868,rule1869,rule1870,rule1871,rule1872,rule1873,rule1874,rule1875,rule1876,rule1877,rule1878,rule1879,rule1880,rule1881,rule1882,rule1883,rule1884,rule1885,rule1886,rule1887,rule1888,rule1889,rule1890,rule1891,rule1892,rule1893,rule1894,rule1895,rule1896,rule1897,rule1898,rule1899,rule1900,rule1901,rule1902,rule1903,rule1904,rule1905,rule1906,rule1907,rule1908,rule1909,rule1910,rule1911,rule1912,rule1913,rule1914,rule1915,rule1916,rule1917,rule1918,rule1919,rule1920,rule1921,rule1922,rule1923,rule1924,rule1925,rule1926,rule1927,rule1928,rule1929,rule1930,rule1931,rule1932,rule1933,rule1934,rule1935,rule1936,rule1937,rule1938,rule1939,rule1940,rule1941,rule1942,rule1943,rule1944,rule1945,rule1946,rule1947,rule1948,rule1949,rule1950,rule1951,rule1952,rule1953,rule1954,rule1955,rule1956,rule1957,rule1958,rule1959,rule1960,rule1961,rule1962,rule1963,rule1964,rule1965,rule1966,rule1967,rule1968,rule1969,rule1970,rule1971,rule1972,rule1973,rule1974,rule1975,rule1976,rule1977,rule1978,rule1979,rule1980,rule1981,rule1982,rule1983,rule1984,rule1985,rule1986,rule1987,rule1988,rule1989,rule1990,rule1991,rule1992,rule1993,rule1994,rule1995,rule1996,rule1997,rule1998,rule1999,rule2000,rule2001,rule2002,rule2003,rule2004,rule2005,rule2006,rule2007,rule2008,rule2009,rule2010,rule2011,rule2012,rule2013,rule2014,rule2015,rule2016,rule2017,rule2018,rule2019,rule2020,rule2021,rule2022,rule2023,rule2024,rule2025,rule2026,rule2027,rule2028,rule2029,rule2030,rule2031,rule2032,rule2033,rule2034,rule2035,rule2036,rule2037,rule2038,rule2039,rule2040,rule2041,rule2042,rule2043,rule2044,rule2045,rule2046,rule2047,rule2048,rule2049,rule2050,rule2051,rule2052,rule2053,rule2054,rule2055,rule2056,rule2057,rule2058,rule2059,rule2060,rule2061,rule2062,rule2063,rule2064,rule2065,rule2066,rule2067,rule2068,rule2069,rule2070,rule2071,rule2072,rule2073,rule2074,rule2075,rule2076,rule2077,rule2078,rule2079,rule2080,rule2081,rule2082,rule2083,rule2084,rule2085,rule2086,rule2087,rule2088,rule2089,rule2090,rule2091,rule2092,rule2093,rule2094,rule2095,rule2096,rule2097,rule2098,rule2099,rule2100,rule2101,rule2102,rule2103,rule2104,rule2105,rule2106,rule2107,rule2108,rule2109,rule2110,rule2111,rule2112,rule2113,rule2114,rule2115,rule2116,rule2117,rule2118,rule2119,rule2120,rule2121,rule2122,rule2123,rule2124,rule2125,rule2126,rule2127,rule2128,rule2129,rule2130,rule2131,rule2132,rule2133,rule2134,rule2135,rule2136,rule2137,rule2138,rule2139,rule2140,rule2141,rule2142,rule2143,rule2144,rule2145,rule2146,rule2147,rule2148,rule2149,rule2150,rule2151,rule2152,rule2153,rule2154,rule2155,rule2156,rule2157,rule2158,rule2159,rule2160,rule2161,rule2162,rule2163,rule2164,rule2165,rule2166,rule2167,rule2168,rule2169,rule2170,rule2171,rule2172,rule2173,rule2174,rule2175,rule2176,rule2177,rule2178,rule2179,rule2180,rule2181,rule2182,rule2183,rule2184,rule2185,rule2186,rule2187,rule2188,rule2189,rule2190,rule2191,rule2192,rule2193,rule2194,rule2195,rule2196,rule2197,rule2198,rule2199,rule2200,rule2201,rule2202,rule2203,rule2204,rule2205,rule2210,],
	"]": [rule1853,],
	"_": [rule1838,],
	"`": [rule1840,rule1841,rule1844,],
	"d": [rule1852,],
	"s": [rule1851,],
	"t": [rule1848,rule1849,rule1850,],
	"{": [rule1847,],
	"}": [rule1846,],
	"~": [rule1845,],
}

# Rules for latex_picturemode ruleset.

def rule2211(colorer, s, i):
    return colorer.match_seq(s, i, kind="label", seq="__PictureMode__",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2212(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2213(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\vector(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2214(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\thinlines",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2215(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\thicklines",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2216(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\shortstack{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2217(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\shortstack[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2218(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\savebox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2219(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\qbezier[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2220(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\qbezier(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2221(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\put(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2222(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\oval[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2223(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\oval(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2224(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\multiput(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2225(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\makebox(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2226(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\linethickness{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2227(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\line(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2228(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\graphpaper[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2229(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\graphpaper(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2230(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\frame{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2231(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="\framebox(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2232(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\dashbox{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2233(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\circle{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2234(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq="\circle*{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2235(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword4", pattern="\"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

# Rules dict for picturemode ruleset.
rulesDict1 = {
	"%": [rule2212,],
	"\": [rule2213,rule2214,rule2215,rule2216,rule2217,rule2218,rule2219,rule2220,rule2221,rule2222,rule2223,rule2224,rule2225,rule2226,rule2227,rule2228,rule2229,rule2230,rule2231,rule2232,rule2233,rule2234,rule2235,],
	"_": [rule2211,],
}

# x.rulesDictDict for latex mode.
rulesDictDict = {
	"latex_arraymode": rulesDict1,
	"latex_main": rulesDict1,
	"latex_mathmode": rulesDict1,
	"latex_picturemode": rulesDict1,
	"latex_tabbingmode": rulesDict1,
	"latex_tabularmode": rulesDict1,
}

# Import dict for latex mode.
importDict = {}

