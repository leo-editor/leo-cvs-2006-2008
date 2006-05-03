# Leo colorizer control file for pyrex mode.

# Properties for pyrex mode.
properties = {
	"indentNextLines": "\s*[^#]{3,}:\s*(#.*)?",
	"lineComment": "#",
}

# Keywords dict for pyrex_main ruleset.
pyrex_main_keywords_dict = {
	"NULL": "literal3",
	"cdef": "keyword4",
	"char": "keyword4",
	"cinclude": "keyword4",
	"ctypedef": "keyword4",
	"double": "keyword4",
	"enum": "keyword4",
	"extern": "keyword4",
	"float": "keyword4",
	"include": "keyword4",
	"private": "keyword4",
	"public": "keyword4",
	"short": "keyword4",
	"signed": "keyword4",
	"sizeof": "keyword4",
	"struct": "keyword4",
	"union": "keyword4",
	"unsigned": "keyword4",
	"void": "keyword4",
}

# Rules for pyrex_main ruleset.


def rule0(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for pyrex_main ruleset.
pyrex_main_rules = [
	rule0, ]

# Rules dict for pyrex mode.
rulesDict = {
	"pyrex_main": pyrex_main_rules,
}

# Import dict for pyrex mode.
importDict = {
	"pyrex_main": "python_main",
}

