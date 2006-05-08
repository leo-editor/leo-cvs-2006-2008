# Leo colorizer control file for embperl mode.

# Properties for embperl mode.
properties = {
	"commentEnd": "-->",
	"commentStart": "<!--",
}

# Keywords dict for embperl_main ruleset.
embperl_main_keywords_dict = {}

# Dictionary of keywords dictionaries for embperl mode.
keywordsDictDict = {
	"embperl_main": embperl_main_keywords_dict,
}

# Rules for embperl_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment2", begin="[#", end="#]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal3", begin="[+", end="+]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="perl::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal3", begin="[-", end="-]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="perl::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="literal3", begin="[$", end="$]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="perl::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="literal3", begin="[!", end="!]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="perl::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)


# Rules list for embperl_main ruleset.
embperl_main_rules = [
	rule0, rule1, rule2, rule3, rule4, ]

# Rules dict for embperl mode.
rulesDict = {
	"embperl_main": embperl_main_rules,
}

# Import dict for embperl mode.
importDict = {
	"embperl_main": "html_main",
}

