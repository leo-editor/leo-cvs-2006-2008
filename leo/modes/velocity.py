# Leo colorizer control file for velocity mode.

# Properties for velocity mode.
properties = {
	"commentEnd": "*#",
	"commentStart": "#*",
	"lineComment": "##",
}

# Keywords dict for velocity_main ruleset.
velocity_main_keywords_dict = {}

# Keywords dict for velocity_velocity ruleset.
velocity_velocity_keywords_dict = {
	"#else": "keyword1",
	"#elseif": "keyword1",
	"#end": "keyword1",
	"#foreach": "keyword1",
	"#if": "keyword1",
	"#include": "keyword1",
	"#macro": "keyword1",
	"#parse": "keyword1",
	"#set": "keyword1",
	"#stop": "keyword1",
}

# Keywords dict for velocity_javascript ruleset.
velocity_javascript_keywords_dict = {}

# Keywords dict for velocity_javascript2 ruleset.
velocity_javascript2_keywords_dict = {}

# Keywords dict for velocity_back_to_html ruleset.
velocity_back_to_html_keywords_dict = {}

# Keywords dict for velocity_css ruleset.
velocity_css_keywords_dict = {}

# Keywords dict for velocity_css2 ruleset.
velocity_css2_keywords_dict = {}

# Rules for velocity_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment1"', begin="<!--", end="-->",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind='"markup"', begin="<SCRIPT", end="</SCRIPT>",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="JAVASCRIPT",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind='"markup"', begin="<STYLE", end="</STYLE>",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="CSS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword2"', begin="<!", end=">",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="xml::DTD-TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind='"markup"', begin="<", end=">",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="html::TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal2"', begin="&", end=";",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=True)


# Rules list for velocity_main ruleset.
velocity_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, ]

# Rules for velocity_velocity ruleset.

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind='"comment2"', begin="#*", end="*#",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule7(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment3"', seq="##",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule8(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword3"', begin="${", end="}",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule9(colorer, s, i):
    return colorer.match_mark_following(s, i, kind='"keyword3"', 
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=False)

def rule10(colorer, s, i):
    return colorer.match_mark_following(s, i, kind='"keyword3"', 
        at_line_start=False, at_line_end=False, at_word_start=False, exclude_match=False)

def rule11(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for velocity_velocity ruleset.
velocity_velocity_rules = [
	rule6, rule7, rule8, rule9, rule10, rule11, ]

# Rules for velocity_javascript ruleset.

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq=">",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="JAVASCRIPT2")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq="SRC=",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="BACK_TO_HTML")

# Rules list for velocity_javascript ruleset.
velocity_javascript_rules = [
	rule12, rule13, ]

# Rules for velocity_javascript2 ruleset.



# Rules list for velocity_javascript2 ruleset.
velocity_javascript2_rules = []

# Rules for velocity_back_to_html ruleset.

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq=">",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="MAIN")

# Rules list for velocity_back_to_html ruleset.
velocity_back_to_html_rules = [
	rule14, ]

# Rules for velocity_css ruleset.

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq=">",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="CSS2")

# Rules list for velocity_css ruleset.
velocity_css_rules = [
	rule15, ]

# Rules for velocity_css2 ruleset.



# Rules list for velocity_css2 ruleset.
velocity_css2_rules = []

# Rules dict for velocity mode.
rulesDict = {
	"velocity_back_to_html": velocity_back_to_html_rules,
	"velocity_css": velocity_css_rules,
	"velocity_css2": velocity_css2_rules,
	"velocity_javascript": velocity_javascript_rules,
	"velocity_javascript2": velocity_javascript2_rules,
	"velocity_main": velocity_main_rules,
	"velocity_velocity": velocity_velocity_rules,
}

# Import dict for velocity mode.
importDict = {
	"velocity_css2": "velocity_css2_velocitycss_main",
	"velocity_javascript2": "velocity_javascript2_velocityjavascript_main",
	"velocity_main": "velocity_main_velocity",
}

