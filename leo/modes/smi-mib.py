# Leo colorizer control file for smi-mib mode.
# This file is in the public domain.

# Properties for smi-mib mode.
properties = {
	"indentCloseBrackets": "}",
	"indentNextLines": ".*(::=|AGENT-CAPABILITIES|DESCRIPTION|IMPORTS|MODULE-COMPLIANCE|MODULE-IDENTITY|NOTIFICATION-GROUP|NOTIFICATION-TYPE|OBJECT-GROUP|OBJECT-IDENTITY|OBJECT-TYPE|TEXTUAL-CONVENTION)\\s*$",
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

# Rules dict for main ruleset.
rulesDict1 = {
	"\"": [rule1,],
	"-": [rule0,],
	"0": [rule8,],
	"1": [rule8,],
	"2": [rule8,],
	"3": [rule8,],
	"4": [rule8,],
	"5": [rule8,],
	"6": [rule8,],
	"7": [rule8,],
	"8": [rule8,],
	"9": [rule8,],
	":": [rule2,],
	"@": [rule8,],
	"A": [rule8,],
	"B": [rule8,],
	"C": [rule8,],
	"D": [rule8,],
	"E": [rule8,],
	"F": [rule8,],
	"G": [rule8,],
	"H": [rule8,],
	"I": [rule8,],
	"J": [rule8,],
	"K": [rule8,],
	"L": [rule8,],
	"M": [rule8,],
	"N": [rule8,],
	"O": [rule5,rule7,rule8,],
	"P": [rule8,],
	"Q": [rule8,],
	"R": [rule8,],
	"S": [rule6,rule8,],
	"T": [rule8,],
	"U": [rule8,],
	"V": [rule8,],
	"W": [rule8,],
	"X": [rule8,],
	"Y": [rule8,],
	"Z": [rule8,],
	"_": [rule8,],
	"a": [rule8,],
	"b": [rule8,],
	"c": [rule8,],
	"d": [rule8,],
	"e": [rule8,],
	"f": [rule8,],
	"g": [rule8,],
	"h": [rule8,],
	"i": [rule8,],
	"j": [rule8,],
	"k": [rule8,],
	"l": [rule8,],
	"m": [rule8,],
	"n": [rule8,],
	"o": [rule8,],
	"p": [rule8,],
	"q": [rule8,],
	"r": [rule8,],
	"s": [rule8,],
	"t": [rule8,],
	"u": [rule8,],
	"v": [rule8,],
	"w": [rule8,],
	"x": [rule8,],
	"y": [rule8,],
	"z": [rule8,],
	"{": [rule4,],
	"}": [rule3,],
}

# x.rulesDictDict for smi_mib mode.
rulesDictDict = {
	"smi_mib_main": rulesDict1,
}

# Import dict for smi_mib mode.
importDict = {}

