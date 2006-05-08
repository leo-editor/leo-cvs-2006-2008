# Leo colorizer control file for assembly-parrot mode.

# Properties for assembly-parrot mode.
properties = {
	"lineComment": "#",
}

# Keywords dict for assembly_parrot_main ruleset.
assembly_parrot_main_keywords_dict = {
	"abs": "keyword1",
	"acos": "keyword1",
	"add": "keyword1",
	"and": "keyword1",
	"asec": "keyword1",
	"asin": "keyword1",
	"atan": "keyword1",
	"bounds": "keyword1",
	"branch": "keyword1",
	"bsr": "keyword1",
	"chopm": "keyword1",
	"cleari": "keyword1",
	"clearn": "keyword1",
	"clearp": "keyword1",
	"clears": "keyword1",
	"clone": "keyword1",
	"close": "keyword1",
	"cmod": "keyword1",
	"concat": "keyword1",
	"cos": "keyword1",
	"cosh": "keyword1",
	"debug": "keyword1",
	"dec": "keyword1",
	"div": "keyword1",
	"end": "keyword1",
	"entrytype": "keyword1",
	"eq": "keyword1",
	"err": "keyword1",
	"exp": "keyword1",
	"find_global": "keyword1",
	"find_type": "keyword1",
	"ge": "keyword1",
	"getfile": "keyword1",
	"getline": "keyword1",
	"getpackage": "keyword1",
	"gt": "keyword1",
	"if": "keyword1",
	"inc": "keyword1",
	"index": "keyword1",
	"jsr": "keyword1",
	"jump": "keyword1",
	"le": "keyword1",
	"length": "keyword1",
	"ln": "keyword1",
	"log10": "keyword1",
	"log2": "keyword1",
	"lt": "keyword1",
	"mod": "keyword1",
	"mul": "keyword1",
	"ne": "keyword1",
	"new": "keyword1",
	"newinterp": "keyword1",
	"noop": "keyword1",
	"not": "keyword1",
	"open": "keyword1",
	"or": "keyword1",
	"ord": "keyword1",
	"pack": "keyword1",
	"pop": "keyword1",
	"popi": "keyword1",
	"popn": "keyword1",
	"popp": "keyword1",
	"pops": "keyword1",
	"pow": "keyword1",
	"print": "keyword1",
	"profile": "keyword1",
	"push": "keyword1",
	"pushi": "keyword1",
	"pushn": "keyword1",
	"pushp": "keyword1",
	"pushs": "keyword1",
	"read": "keyword1",
	"readline": "keyword1",
	"repeat": "keyword1",
	"restore": "keyword1",
	"ret": "keyword1",
	"rotate_up": "keyword1",
	"runinterp": "keyword1",
	"save": "keyword1",
	"sec": "keyword1",
	"sech": "keyword1",
	"set": "keyword1",
	"set_keyed": "keyword1",
	"setfile": "keyword1",
	"setline": "keyword1",
	"setpackage": "keyword1",
	"shl": "keyword1",
	"shr": "keyword1",
	"sin": "keyword1",
	"sinh": "keyword1",
	"sleep": "keyword1",
	"sub": "keyword1",
	"substr": "keyword1",
	"tan": "keyword1",
	"tanh": "keyword1",
	"time": "keyword1",
	"trace": "keyword1",
	"typeof": "keyword1",
	"unless": "keyword1",
	"warningsoff": "keyword1",
	"warningson": "keyword1",
	"write": "keyword1",
	"xor": "keyword1",
}

# Dictionary of keywords dictionaries for assembly_parrot mode.
keywordsDictDict = {
	"assembly_parrot_main": assembly_parrot_main_keywords_dict,
}

# Rules for assembly_parrot_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal2", seq="I\d{1,2}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal2", seq="S\d{1,2}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal2", seq="N\d{1,2}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="literal2", seq="P\d{1,2}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for assembly_parrot_main ruleset.
assembly_parrot_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, ]

# Rules dict for assembly_parrot mode.
rulesDict = {
	"assembly_parrot_main": assembly_parrot_main_rules,
}

# Import dict for assembly_parrot mode.
importDict = {}

