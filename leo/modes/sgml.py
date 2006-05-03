# Leo colorizer control file for sgml mode.

# Properties for sgml mode.
properties = {
	"commentEnd": "-->",
	"commentStart": "<!--",
}

# Keywords dict for sgml_main ruleset.
sgml_main_keywords_dict = {}

# Rules for sgml_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment1"', begin="<!--", end="-->",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword2"', begin="<!ENTITY", end=">",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="xml::ENTITY-TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword2"', begin="<![CDATA[", end="]]>",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="xml::CDATA",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword2"', begin="<!", end=">",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="xml::DTD-TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind='"markup"', begin="<", end=">",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="xml::TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal2"', begin="&", end=";",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=True)

# Rules list for sgml_main ruleset.
sgml_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, ]

# Rules dict for sgml mode.
rulesDict = {
	"sgml_main": sgml_main_rules,
}

# Import dict for sgml mode.
importDict = {}

