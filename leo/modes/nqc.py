# Leo colorizer control file for nqc mode.

# Properties for nqc mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"doubleBracketIndent": "false",
	"indentCloseBrackets": "}",
	"indentNextLine": "\s*(((if|while)\s*\(|else\s*|else\s+if\s*\(|for\s*\(.*\))[^{;]*)",
	"indentOpenBrackets": "{",
	"lineComment": "//",
	"lineUpClosingBracket": "true",
	"wordBreakChars": ",+-=<>/?^&*",
}

# Keywords dict for nqc_main ruleset.
nqc_main_keywords_dict = {
	"ACQUIRE_OUT_A": "literal2",
	"ACQUIRE_OUT_B": "literal2",
	"ACQUIRE_OUT_C": "literal2",
	"ACQUIRE_SOUND": "literal2",
	"ACQUIRE_USER_1": "literal2",
	"ACQUIRE_USER_2": "literal2",
	"ACQUIRE_USER_3": "literal2",
	"ACQUIRE_USER_4": "literal2",
	"DISPLAY_OUT_A": "literal2",
	"DISPLAY_OUT_B": "literal2",
	"DISPLAY_OUT_C": "literal2",
	"DISPLAY_SENSOR_1": "literal2",
	"DISPLAY_SENSOR_2": "literal2",
	"DISPLAY_SENSOR_3": "literal2",
	"DISPLAY_WATCH": "literal2",
	"EVENT_1_PRESSED": "literal2",
	"EVENT_1_RELEASED": "literal2",
	"EVENT_2_PRESSED": "literal2",
	"EVENT_2_RELEASED": "literal2",
	"EVENT_COUNTER_0": "literal2",
	"EVENT_COUNTER_1": "literal2",
	"EVENT_LIGHT_CLICK": "literal2",
	"EVENT_LIGHT_DOUBLECLICK": "literal2",
	"EVENT_LIGHT_HIGH": "literal2",
	"EVENT_LIGHT_LOW": "literal2",
	"EVENT_LIGHT_NORMAL": "literal2",
	"EVENT_MESSAGE": "literal2",
	"EVENT_TIMER_0": "literal2",
	"EVENT_TIMER_1": "literal2",
	"EVENT_TIMER_2": "literal2",
	"EVENT_TYPE_CLICK": "literal2",
	"EVENT_TYPE_DOUBLECLICK": "literal2",
	"EVENT_TYPE_EDGE": "literal2",
	"EVENT_TYPE_FASTCHANGE": "literal2",
	"EVENT_TYPE_HIGH": "literal2",
	"EVENT_TYPE_LOW": "literal2",
	"EVENT_TYPE_MESSAGE": "literal2",
	"EVENT_TYPE_NORMAL": "literal2",
	"EVENT_TYPE_PRESSED": "literal2",
	"EVENT_TYPE_PULSE": "literal2",
	"EVENT_TYPE_RELEASED": "literal2",
	"NULL": "literal2",
	"OUT_A": "literal2",
	"OUT_B": "literal2",
	"OUT_C": "literal2",
	"OUT_FLOAT": "literal2",
	"OUT_FULL": "literal2",
	"OUT_FWD": "literal2",
	"OUT_HALF": "literal2",
	"OUT_LOW": "literal2",
	"OUT_OFF": "literal2",
	"OUT_ON": "literal2",
	"OUT_REV": "literal2",
	"OUT_TOOGLE": "literal2",
	"SENSOR_1": "literal2",
	"SENSOR_2": "literal2",
	"SENSOR_3": "literal2",
	"SENSOR_CELSIUS": "literal2",
	"SENSOR_EDGE": "literal2",
	"SENSOR_FAHRENHEIT": "literal2",
	"SENSOR_LIGHT": "literal2",
	"SENSOR_MODE_BOOL": "literal2",
	"SENSOR_MODE_CELSIUS": "literal2",
	"SENSOR_MODE_EDGE": "literal2",
	"SENSOR_MODE_FAHRENHEIT": "literal2",
	"SENSOR_MODE_PERCENT": "literal2",
	"SENSOR_MODE_PULSE": "literal2",
	"SENSOR_MODE_RAW": "literal2",
	"SENSOR_MODE_ROTATION": "literal2",
	"SENSOR_PULSE": "literal2",
	"SENSOR_ROTATION": "literal2",
	"SENSOR_TOUCH": "literal2",
	"SENSOR_TYPE_LIGHT": "literal2",
	"SENSOR_TYPE_NONE": "literal2",
	"SENSOR_TYPE_ROTATION": "literal2",
	"SENSOR_TYPE_TEMPERATURE": "literal2",
	"SENSOR_TYPE_TOUCH": "literal2",
	"SERIAL_COMM_4800": "literal2",
	"SERIAL_COMM_76KHZ": "literal2",
	"SERIAL_COMM_DEFAULT": "literal2",
	"SERIAL_COMM_DUTY25": "literal2",
	"SERIAL_PACKET_": "literal2",
	"SERIAL_PACKET_CHECKSUM": "literal2",
	"SERIAL_PACKET_DEFAULT": "literal2",
	"SERIAL_PACKET_NEGATED": "literal2",
	"SERIAL_PACKET_PREAMBLE": "literal2",
	"SERIAL_PACKET_RCX": "literal2",
	"SOUND_CLICK": "literal2",
	"SOUND_DOUBLE_BEEP": "literal2",
	"SOUND_DOWN": "literal2",
	"SOUND_FAST_UP": "literal2",
	"SOUND_LOW_BEEP": "literal2",
	"SOUND_UP": "literal2",
	"TX_POWER_HI": "literal2",
	"TX_POWER_LO": "literal2",
	"__event_src": "keyword1",
	"__sensor": "keyword1",
	"__type": "keyword1",
	"abs": "keyword1",
	"aquire": "keyword1",
	"asm": "keyword2",
	"break": "keyword1",
	"case": "keyword1",
	"catch": "keyword1",
	"const": "keyword1",
	"continue": "keyword1",
	"default": "keyword1",
	"do": "keyword1",
	"else": "keyword1",
	"false": "literal2",
	"for": "keyword1",
	"if": "keyword1",
	"inline": "keyword2",
	"int": "keyword3",
	"monitor": "keyword1",
	"repeat": "keyword1",
	"return": "keyword1",
	"sign": "keyword1",
	"start": "keyword1",
	"stop": "keyword1",
	"sub": "keyword1",
	"switch": "keyword1",
	"task": "keyword1",
	"true": "literal2",
	"void": "keyword3",
	"while": "keyword1",
}

# Dictionary of keywords dictionaries for nqc mode.
keywordsDictDict = {
	"nqc_main": nqc_main_keywords_dict,
}

# Rules for nqc_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="keyword2", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule4(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=False, at_whitespace_end=True, at_word_start=False, exclude_match=True)

def rule23(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule24(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule6,],
	"\"": [rule1,],
	"#": [rule3,],
	"%": [rule15,],
	"&": [rule16,],
	"'": [rule2,],
	"(": [rule23,],
	"*": [rule12,],
	"+": [rule9,],
	"-": [rule10,],
	"/": [rule0,rule4,rule11,],
	"0": [rule24,],
	"1": [rule24,],
	"2": [rule24,],
	"3": [rule24,],
	"4": [rule24,],
	"5": [rule24,],
	"6": [rule24,],
	"7": [rule24,],
	"8": [rule24,],
	"9": [rule24,],
	":": [rule22,],
	"<": [rule8,rule14,],
	"=": [rule5,],
	">": [rule7,rule13,],
	"@": [rule24,],
	"A": [rule24,],
	"B": [rule24,],
	"C": [rule24,],
	"D": [rule24,],
	"E": [rule24,],
	"F": [rule24,],
	"G": [rule24,],
	"H": [rule24,],
	"I": [rule24,],
	"J": [rule24,],
	"K": [rule24,],
	"L": [rule24,],
	"M": [rule24,],
	"N": [rule24,],
	"O": [rule24,],
	"P": [rule24,],
	"Q": [rule24,],
	"R": [rule24,],
	"S": [rule24,],
	"T": [rule24,],
	"U": [rule24,],
	"V": [rule24,],
	"W": [rule24,],
	"X": [rule24,],
	"Y": [rule24,],
	"Z": [rule24,],
	"^": [rule18,],
	"_": [rule24,],
	"a": [rule24,],
	"b": [rule24,],
	"c": [rule24,],
	"d": [rule24,],
	"e": [rule24,],
	"f": [rule24,],
	"g": [rule24,],
	"h": [rule24,],
	"i": [rule24,],
	"j": [rule24,],
	"k": [rule24,],
	"l": [rule24,],
	"m": [rule24,],
	"n": [rule24,],
	"o": [rule24,],
	"p": [rule24,],
	"q": [rule24,],
	"r": [rule24,],
	"s": [rule24,],
	"t": [rule24,],
	"u": [rule24,],
	"v": [rule24,],
	"w": [rule24,],
	"x": [rule24,],
	"y": [rule24,],
	"z": [rule24,],
	"{": [rule21,],
	"|": [rule17,],
	"}": [rule20,],
	"~": [rule19,],
}

# x.rulesDictDict for nqc mode.
rulesDictDict = {
	"nqc_main": rulesDict1,
}

# Import dict for nqc mode.
importDict = {}

