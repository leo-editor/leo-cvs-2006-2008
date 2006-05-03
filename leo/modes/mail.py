# Leo colorizer control file for mail mode.

# Properties for mail mode.
properties = {
	"lineComment": ">",
	"noWordSep": "-_",
}

# Keywords dict for mail_main ruleset.
mail_main_keywords_dict = {}

# Keywords dict for mail_signature ruleset.
mail_signature_keywords_dict = {}

# Keywords dict for mail_header ruleset.
mail_header_keywords_dict = {}

# Rules for mail_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment3"', seq=">>>",
        at_line_start=True, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment2"', seq=">>",
        at_line_start=True, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment1"', seq=">",
        at_line_start=True, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment1"', seq="|",
        at_line_start=True, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment1"', seq=":",
        at_line_start=True, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="comment2", seq="--",
        at_line_start=True, at_line_end=False, at_word_start=False, delegate="SIGNATURE")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq=":-)",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq=":-(",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq=":)",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq=":(",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq=";-)",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq=";-(",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq=";)",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword1", seq=";(",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind='"label"',
        at_line_start=True, at_line_end=False, at_word_start=False, exclude_match=False)

# Rules list for mail_main ruleset.
mail_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, ]

# Rules for mail_signature ruleset.

# Rules list for mail_signature ruleset.
mail_signature_rules = []

# Rules for mail_header ruleset.

def rule15(colorer, s, i):
    return colorer.match_span(s, i, kind='"keyword2"', begin="<", end=">",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

# Rules list for mail_header ruleset.
mail_header_rules = [
	rule15, ]

# Rules dict for mail mode.
rulesDict = {
	"mail_header": mail_header_rules,
	"mail_main": mail_main_rules,
	"mail_signature": mail_signature_rules,
}

# Import dict for mail mode.
importDict = {}

