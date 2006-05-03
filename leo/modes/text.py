# Leo colorizer control file for text mode.

# Properties for text mode.
properties = {}

# Keywords dict for text_main ruleset.
text_main_keywords_dict = {}

# Rules for text_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_terminate(s, i, kind='""', at_char=0)

# Rules list for text_main ruleset.
text_main_rules = [
	rule0, ]

# Rules dict for text mode.
rulesDict = {
	"text_main": text_main_rules,
}

# Import dict for text mode.
importDict = {}

