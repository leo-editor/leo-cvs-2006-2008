# Leo colorizer control file for rpmspec mode.

# Properties for rpmspec mode.
properties = {
	"lineComment": "#",
}

# Keywords dict for rpmspec_main ruleset.
rpmspec_main_keywords_dict = {
	"%build": "label",
	"%clean": "label",
	"%config": "markup",
	"%description": "label",
	"%dir": "markup",
	"%doc": "markup",
	"%docdir": "markup",
	"%else": "function",
	"%endif": "function",
	"%files": "label",
	"%ifarch": "function",
	"%ifnarch": "function",
	"%ifnos": "function",
	"%ifos": "function",
	"%install": "label",
	"%package": "markup",
	"%post": "label",
	"%postun": "label",
	"%pre": "label",
	"%prep": "label",
	"%preun": "label",
	"%setup": "function",
	"%verifyscript": "label",
	"AutoReqProv:": "keyword1",
	"BuildArch:": "keyword1",
	"BuildRoot:": "keyword1",
	"Conflicts:": "keyword1",
	"Copyright:": "keyword1",
	"Distribution:": "keyword1",
	"ExcludeArch:": "keyword1",
	"ExclusiveArch:": "keyword1",
	"ExclusiveOS:": "keyword1",
	"Group:": "keyword1",
	"Icon:": "keyword1",
	"Name:": "keyword1",
	"NoPatch:": "keyword1",
	"NoSource:": "keyword1",
	"Packager:": "keyword1",
	"Prefix:": "keyword1",
	"Provides:": "keyword1",
	"Release:": "keyword1",
	"Requires:": "keyword1",
	"Serial:": "keyword1",
	"Summary:": "keyword1",
	"URL:": "keyword1",
	"Vendor:": "keyword1",
	"Version:": "keyword1",
}

# Keywords dict for rpmspec_attr ruleset.
rpmspec_attr_keywords_dict = {}

# Keywords dict for rpmspec_verify ruleset.
rpmspec_verify_keywords_dict = {
	"group": "keyword2",
	"maj": "keyword2",
	"md5": "keyword2",
	"min": "keyword2",
	"mode": "keyword2",
	"mtime": "keyword2",
	"not": "operator",
	"owner": "keyword2",
	"size": "keyword2",
	"symlink": "keyword2",
}

# Dictionary of keywords dictionaries for rpmspec mode.
keywordsDictDict = {
	"rpmspec_attr": rpmspec_attr_keywords_dict,
	"rpmspec_main": rpmspec_main_keywords_dict,
	"rpmspec_verify": rpmspec_verify_keywords_dict,
}

# Rules for rpmspec_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule2(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="%attr(", end=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="ATTR",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="%verify(", end=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="VERIFY",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword1", pattern="Source"
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule7(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword1", pattern="Patch"
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule8(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="function", pattern="%patch"
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule9(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="${", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule10(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword3", begin="%{", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule11(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$#"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule12(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$?"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule13(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$*"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule14(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$<"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule15(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$"
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule16(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for rpmspec_main ruleset.
rpmspec_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, ]

# Rules for rpmspec_attr ruleset.

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

# Rules list for rpmspec_attr ruleset.
rpmspec_attr_rules = [
	rule17, rule18, ]

# Rules for rpmspec_verify ruleset.

def rule19(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for rpmspec_verify ruleset.
rpmspec_verify_rules = [
	rule19, ]

# Rules dict for rpmspec mode.
rulesDict = {
	"rpmspec_attr": rpmspec_attr_rules,
	"rpmspec_main": rpmspec_main_rules,
	"rpmspec_verify": rpmspec_verify_rules,
}

# Import dict for rpmspec mode.
importDict = {}

