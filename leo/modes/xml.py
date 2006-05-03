# Leo colorizer control file for xml mode.

# Properties for xml mode.
properties = {
	"commentEnd": "-->",
	"commentStart": "<!--",
}

# Keywords dict for xml_main ruleset.
xml_main_keywords_dict = {}

# Keywords dict for xml_tags ruleset.
xml_tags_keywords_dict = {}

# Keywords dict for xml_dtd_tags ruleset.
xml_dtd_tags_keywords_dict = {
	"#IMPLIED": "keyword1",
	"#PCDATA": "keyword1",
	"#REQUIRED": "keyword1",
	"CDATA": "keyword1",
	"EMPTY": "keyword1",
	"IGNORE": "keyword1",
	"INCLUDE": "keyword1",
	"NDATA": "keyword1",
}

# Keywords dict for xml_entity_tags ruleset.
xml_entity_tags_keywords_dict = {
	"SYSTEM": "keyword1",
}

# Keywords dict for xml_cdata ruleset.
xml_cdata_keywords_dict = {}

# Rules for xml_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment1"', begin="<!--", end="-->",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword2"', begin="<!ENTITY", end=">",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="ENTITY-TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword2"', begin="<![CDATA[", end="]]>",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="CDATA",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword2"', begin="<!", end=">",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="DTD-TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword3"', begin="<?", end=">",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind='"markup"', begin="<", end=">",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal2"', begin="&", end=";",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=True)

# Rules list for xml_main ruleset.
xml_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, ]

# Rules for xml_tags ruleset.

def rule7(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment1"', begin="<!--", end="-->",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule8(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule9(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="'", end="'",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq="/",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind='"label"',
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=True)

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

# Rules list for xml_tags ruleset.
xml_tags_rules = [
	rule7, rule8, rule9, rule10, rule11, rule12, ]

# Rules for xml_dtd_tags ruleset.

def rule13(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment1"', begin="<!--", end="-->",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule14(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment1"', begin="--", end="--",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule15(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal2"', begin="%", end=";",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=True)

def rule16(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule17(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="'", end="'",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule18(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword2"', begin="[", end="]",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="(",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=")",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="?",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for xml_dtd_tags ruleset.
xml_dtd_tags_rules = [
	rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22,
	rule23, rule24, rule25, rule26, ]

# Rules for xml_entity_tags ruleset.

def rule27(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment1"', begin="<!--", end="-->",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule28(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment1"', begin="--", end="--",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule29(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule30(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="'", end="'",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule31(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule32(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule33(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for xml_entity_tags ruleset.
xml_entity_tags_rules = [
	rule27, rule28, rule29, rule30, rule31, rule32, rule33, ]

# Rules for xml_cdata ruleset.

# Rules list for xml_cdata ruleset.
xml_cdata_rules = []

# Rules dict for xml mode.
rulesDict = {
	"xml_cdata": xml_cdata_rules,
	"xml_dtd_tags": xml_dtd_tags_rules,
	"xml_entity_tags": xml_entity_tags_rules,
	"xml_main": xml_main_rules,
	"xml_tags": xml_tags_rules,
}

# Import dict for xml mode.
importDict = {}

