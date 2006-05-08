# Leo colorizer control file for smi-mib mode.

# Properties for smi-mib mode.
properties = {
	"indentCloseBrackets": "}",
	"indentNextLines": ".*(::=|AGENT-CAPABILITIES|DESCRIPTION|IMPORTS|MODULE-COMPLIANCE|MODULE-IDENTITY|NOTIFICATION-GROUP|NOTIFICATION-TYPE|OBJECT-GROUP|OBJECT-IDENTITY|OBJECT-TYPE|TEXTUAL-CONVENTION)\s*$",
	"indentOpenBrackets": "{",
	"lineComment": "--",
	"lineUpClosingBracket": "true",
	"noWordSep": "-",
}

# Keywords dict for smi_mib_main ruleset.
smi_mib_main_keywords_dict = {
	"ACCESS": "keyword1",
	"AGENT-CAPABILITIES": "function",
	"AUGMENTS": "keyword1",
	"AutonomousType": "keyword2",
	"BEGIN": "function",
	"BITS": "keyword2",
	"CONTACT-INFO": "keyword1",
	"CREATION-REQUIRES": "keyword1",
	"Counter32": "keyword2",
	"Counter64": "keyword2",
	"DEFINITIONS": "keyword1",
	"DEFVAL": "keyword1",
	"DESCRIPTION": "keyword1",
	"DISPLAY-HINT": "keyword1",
	"DateAndTime": "keyword2",
	"DisplayString": "keyword2",
	"END": "function",
	"FROM": "function",
	"GROUP": "keyword1",
	"Gauge32": "keyword2",
	"IMPORTS": "function",
	"INCLUDES": "keyword1",
	"INDEX": "keyword1",
	"INTEGER": "keyword2",
	"InstancePointer": "keyword2",
	"Integer32": "keyword2",
	"IpAddress": "keyword2",
	"LAST-UPDATED": "keyword1",
	"MANDATORY-GROUPS": "keyword1",
	"MAX-ACCESS": "keyword1",
	"MIN-ACCESS": "keyword1",
	"MODULE": "keyword1",
	"MODULE-COMPLIANCE": "function",
	"MODULE-IDENTITY": "function",
	"MacAddress": "keyword2",
	"NOTIFICATION-GROUP": "function",
	"NOTIFICATION-TYPE": "function",
	"NOTIFICATIONS": "keyword1",
	"OBJECT": "keyword1",
	"OBJECT-GROUP": "function",
	"OBJECT-IDENTITY": "function",
	"OBJECT-TYPE": "function",
	"OBJECTS": "keyword1",
	"ORGANIZATION": "keyword1",
	"Opaque": "keyword2",
	"PRODUCT-RELEASE": "keyword1",
	"PhysAddress": "keyword2",
	"REFERENCE": "keyword1",
	"REVISION": "keyword1",
	"RowPointer": "keyword2",
	"RowStatus": "keyword2",
	"SEQUENCE": "keyword2",
	"SIZE": "keyword3",
	"STATUS": "keyword1",
	"SUPPORTS": "keyword1",
	"SYNTAX": "keyword1",
	"StorageType": "keyword2",
	"TAddress": "keyword2",
	"TDomain": "keyword2",
	"TEXTUAL-CONVENTION": "function",
	"TestAndIncr": "keyword2",
	"TimeInterval": "keyword2",
	"TimeStamp": "keyword2",
	"TimeTicks": "keyword2",
	"TruthValue": "keyword2",
	"UNITS": "keyword1",
	"Unsigned32": "keyword2",
	"VARIATION": "keyword1",
	"VariablePointer": "keyword2",
	"WRITE-SYNTAX": "keyword1",
	"accessible-for-notify": "keyword3",
	"current": "keyword3",
	"deprecated": "keyword3",
	"not-accessible": "keyword3",
	"obsolete": "keyword3",
	"read-create": "keyword3",
	"read-only": "keyword3",
	"read-write": "keyword3",
}

# Dictionary of keywords dictionaries for smi_mib mode.
keywordsDictDict = {
	"smi_mib_main": smi_mib_main_keywords_dict,
}

# Rules for smi_mib_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="--",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="::=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="OBJECT IDENTIFIER",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="SEQUENCE OF",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="OCTET STRING",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for smi_mib_main ruleset.
smi_mib_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, ]

# Rules dict for smi_mib mode.
rulesDict = {
	"smi_mib_main": smi_mib_main_rules,
}

# Import dict for smi_mib mode.
importDict = {}

