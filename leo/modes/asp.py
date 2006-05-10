# Leo colorizer control file for asp mode.
# This file is in the public domain.

# Properties for asp mode.
properties = {
	"commentEnd": "-->",
	"commentStart": "<!--",
}

# Attributes dict for asp_main ruleset.
asp_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for asp_aspvb ruleset.
asp_aspvb_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for asp_aspjs ruleset.
asp_aspjs_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for asp_asppl ruleset.
asp_asppl_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for asp_aspvb_tags ruleset.
asp_aspvb_tags_attributes_dict = {
	"default": "MARKUP",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for asp_aspjs_tags ruleset.
asp_aspjs_tags_attributes_dict = {
	"default": "MARKUP",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for asp_asppl_tags ruleset.
asp_asppl_tags_attributes_dict = {
	"default": "MARKUP",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for asp mode.
attributesDictDict = {
	"asp_aspjs": asp_aspjs_attributes_dict,
	"asp_aspjs_tags": asp_aspjs_tags_attributes_dict,
	"asp_asppl": asp_asppl_attributes_dict,
	"asp_asppl_tags": asp_asppl_tags_attributes_dict,
	"asp_aspvb": asp_aspvb_attributes_dict,
	"asp_aspvb_tags": asp_aspvb_tags_attributes_dict,
	"asp_main": asp_main_attributes_dict,
}

# Keywords dict for asp_main ruleset.
asp_main_keywords_dict = {}

# Keywords dict for asp_aspvb ruleset.
asp_aspvb_keywords_dict = {}

# Keywords dict for asp_aspjs ruleset.
asp_aspjs_keywords_dict = {}

# Keywords dict for asp_asppl ruleset.
asp_asppl_keywords_dict = {}

# Keywords dict for asp_aspvb_tags ruleset.
asp_aspvb_tags_keywords_dict = {}

# Keywords dict for asp_aspjs_tags ruleset.
asp_aspjs_tags_keywords_dict = {}

# Keywords dict for asp_asppl_tags ruleset.
asp_asppl_tags_keywords_dict = {}

# Dictionary of keywords dictionaries for asp mode.
keywordsDictDict = {
	"asp_aspjs": asp_aspjs_keywords_dict,
	"asp_aspjs_tags": asp_aspjs_tags_keywords_dict,
	"asp_asppl": asp_asppl_keywords_dict,
	"asp_asppl_tags": asp_asppl_tags_keywords_dict,
	"asp_aspvb": asp_aspvb_keywords_dict,
	"asp_aspvb_tags": asp_aspvb_tags_keywords_dict,
	"asp_main": asp_main_keywords_dict,
}

# Rules for asp_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq="<%@LANGUAGE=\"VBSCRIPT\"%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="ASPVB")

def rule1(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq="<%@LANGUAGE=\"JSCRIPT\"%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="ASPJS")

def rule2(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq="<%@LANGUAGE=\"JAVASCRIPT\"%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="ASPJS")

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq="<%@LANGUAGE=\"PERLSCRIPT\"%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="ASPPL")

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<%", end="%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="vbscript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"vbscript\" runat=\"server\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="vbscript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"jscript\" runat=\"server\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="javascript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule7(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"javascript\" runat=\"server\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="javascript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule8(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"perlscript\" runat=\"server\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="perl::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule9(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"jscript\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="javascript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule10(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"javascript\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="javascript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule11(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script>", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="javascript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule12(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<!--#", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule13(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule14(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<STYLE>", end="</STYLE>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="css::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule15(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ASPVB_TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule16(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="&", end=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=True)

# Rules dict for main ruleset.
rulesDict1 = {
	"&": [rule16,],
	"<": [rule0,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,],
}

# Rules for asp_aspvb ruleset.

def rule17(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<%", end="%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="vbscript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule18(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"vbscript\" runat=\"server\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="vbscript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule19(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"jscript\" runat=\"server\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="javascript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule20(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"javascript\" runat=\"server\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="javascript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule21(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"perlscript\" runat=\"server\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="perl::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule22(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"jscript\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="javascript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule23(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"javascript\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="javascript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule24(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script>", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="javascript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule25(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<!--#", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule26(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule27(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<STYLE>", end="</STYLE>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="css::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule28(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="</", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ASPVB_TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule29(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ASPVB_TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule30(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="&", end=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=True)

# Rules dict for aspvb ruleset.
rulesDict2 = {
	"&": [rule30,],
	"<": [rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27,rule28,rule29,],
}

# Rules for asp_aspjs ruleset.

def rule31(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<%", end="%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="javascript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule32(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"vbscript\" runat=\"server\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="vbscript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule33(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"jscript\" runat=\"server\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="javascript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule34(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"javascript\" runat=\"server\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="javascript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule35(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"perlscript\" runat=\"server\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="perl::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule36(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"jscript\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="javascript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule37(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"javascript\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="javascript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule38(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script>", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="javascript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule39(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<!--#", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule40(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule41(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<STYLE>", end="</STYLE>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="css::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule42(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="</", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ASPJS_TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule43(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ASPJS_TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule44(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="&", end=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=True)

# Rules dict for aspjs ruleset.
rulesDict3 = {
	"&": [rule44,],
	"<": [rule31,rule32,rule33,rule34,rule35,rule36,rule37,rule38,rule39,rule40,rule41,rule42,rule43,],
}

# Rules for asp_asppl ruleset.

def rule45(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<%", end="%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="perl::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule46(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"vbscript\" runat=\"server\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="vbscript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule47(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"jscript\" runat=\"server\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="javascript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule48(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"javascript\" runat=\"server\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="javascript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule49(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"perlscript\" runat=\"server\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="perl::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule50(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"jscript\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ASPPL_CSJS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule51(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script language=\"javascript\">", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ASPPL_CSJS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule52(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<script>", end="</script>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ASPPL_CSJS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule53(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<!--#", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule54(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule55(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<STYLE>", end="</STYLE>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="css::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule56(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="</", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ASPPL_TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule57(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ASPPL_TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule58(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="&", end=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=True)

# Rules dict for asppl ruleset.
rulesDict4 = {
	"&": [rule58,],
	"<": [rule45,rule46,rule47,rule48,rule49,rule50,rule51,rule52,rule53,rule54,rule55,rule56,rule57,],
}

# Rules for asp_aspvb_tags ruleset.

def rule59(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<%", end="%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="vbscript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules dict for aspvb_tags ruleset.
rulesDict5 = {
	"<": [rule59,],
}

# Rules for asp_aspjs_tags ruleset.

def rule60(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<%", end="%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="javascript::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules dict for aspjs_tags ruleset.
rulesDict6 = {
	"<": [rule60,],
}

# Rules for asp_asppl_tags ruleset.

def rule61(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<%", end="%>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="perl::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules dict for asppl_tags ruleset.
rulesDict7 = {
	"<": [rule61,],
}

# x.rulesDictDict for asp mode.
rulesDictDict = {
	"asp_aspjs": rulesDict3,
	"asp_aspjs_tags": rulesDict6,
	"asp_asppl": rulesDict4,
	"asp_asppl_tags": rulesDict7,
	"asp_aspvb": rulesDict2,
	"asp_aspvb_tags": rulesDict5,
	"asp_main": rulesDict1,
}

# Import dict for asp mode.
importDict = {}

