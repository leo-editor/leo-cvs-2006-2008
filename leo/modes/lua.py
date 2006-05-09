# Leo colorizer control file for lua mode.

# Properties for lua mode.
properties = {
	"commentEnd": "]]",
	"commentStart": "--[[",
	"doubleBracketIndent": "true",
	"indentCloseBrackets": "}",
	"indentOpenBrackets": "{",
	"lineComment": "--",
	"lineUpClosingBracket": "true",
	"wordBreakChars": ",+-=<>/?^&*",
}

# Keywords dict for lua_main ruleset.
lua_main_keywords_dict = {
	"...": "keyword2",
	"LUA_PATH": "keyword2",
	"_ALERT": "keyword2",
	"_ERRORMESSAGE": "keyword2",
	"_G": "keyword2",
	"_LOADED": "keyword2",
	"_PROMPT": "keyword2",
	"_REQUIREDNAME": "keyword2",
	"_VERSION": "keyword2",
	"__add": "keyword2",
	"__call": "keyword2",
	"__concat": "keyword2",
	"__div": "keyword2",
	"__eq": "keyword2",
	"__fenv": "keyword2",
	"__index": "keyword2",
	"__le": "keyword2",
	"__lt": "keyword2",
	"__metatable": "keyword2",
	"__mode": "keyword2",
	"__mul": "keyword2",
	"__newindex": "keyword2",
	"__pow": "keyword2",
	"__sub": "keyword2",
	"__tostring": "keyword2",
	"__unm": "keyword2",
	"and": "keyword1",
	"arg": "keyword2",
	"assert": "keyword2",
	"break": "keyword1",
	"collectgarbage": "keyword2",
	"coroutine.create": "keyword2",
	"coroutine.resume": "keyword2",
	"coroutine.status": "keyword2",
	"coroutine.wrap": "keyword2",
	"coroutine.yield": "keyword2",
	"debug.debug": "keyword2",
	"debug.gethook": "keyword2",
	"debug.getinfo": "keyword2",
	"debug.getlocal": "keyword2",
	"debug.getupvalue": "keyword2",
	"debug.sethook": "keyword2",
	"debug.setlocal": "keyword2",
	"debug.setupvalue": "keyword2",
	"debug.traceback": "keyword2",
	"do": "keyword1",
	"dofile": "keyword2",
	"else": "keyword1",
	"elseif": "keyword1",
	"end": "keyword1",
	"error": "keyword2",
	"false": "keyword3",
	"for": "keyword1",
	"function": "keyword1",
	"gcinfo": "keyword2",
	"getfenv": "keyword2",
	"getmetatable": "keyword2",
	"if": "keyword1",
	"in": "keyword1",
	"io.close": "keyword2",
	"io.flush": "keyword2",
	"io.input": "keyword2",
	"io.lines": "keyword2",
	"io.open": "keyword2",
	"io.read": "keyword2",
	"io.stderr": "keyword2",
	"io.stdin": "keyword2",
	"io.stdout": "keyword2",
	"io.tmpfile": "keyword2",
	"io.type": "keyword2",
	"io.write": "keyword2",
	"ipairs": "keyword2",
	"loadfile": "keyword2",
	"loadlib": "keyword2",
	"loadstring": "keyword2",
	"local": "keyword1",
	"math.abs": "keyword2",
	"math.acos": "keyword2",
	"math.asin": "keyword2",
	"math.atan": "keyword2",
	"math.atan2": "keyword2",
	"math.ceil": "keyword2",
	"math.cos": "keyword2",
	"math.deg": "keyword2",
	"math.exp": "keyword2",
	"math.floor": "keyword2",
	"math.frexp": "keyword2",
	"math.ldexp": "keyword2",
	"math.log": "keyword2",
	"math.log10": "keyword2",
	"math.max": "keyword2",
	"math.min": "keyword2",
	"math.mod": "keyword2",
	"math.pi": "keyword2",
	"math.pow": "keyword2",
	"math.rad": "keyword2",
	"math.random": "keyword2",
	"math.randomseed": "keyword2",
	"math.sin": "keyword2",
	"math.sqrt": "keyword2",
	"math.tan": "keyword2",
	"next": "keyword2",
	"nil": "keyword3",
	"not": "keyword1",
	"or": "keyword1",
	"os.clock": "keyword2",
	"os.date": "keyword2",
	"os.difftime": "keyword2",
	"os.execute": "keyword2",
	"os.exit": "keyword2",
	"os.getenv": "keyword2",
	"os.remove": "keyword2",
	"os.rename": "keyword2",
	"os.setlocale": "keyword2",
	"os.time": "keyword2",
	"os.tmpname": "keyword2",
	"pairs": "keyword2",
	"pcall": "keyword2",
	"print": "keyword2",
	"rawequal": "keyword2",
	"rawget": "keyword2",
	"rawset": "keyword2",
	"repeat": "keyword1",
	"require": "keyword2",
	"return": "keyword1",
	"setfenv": "keyword2",
	"setmetatable": "keyword2",
	"string.byte": "keyword2",
	"string.char": "keyword2",
	"string.dump": "keyword2",
	"string.find": "keyword2",
	"string.format": "keyword2",
	"string.gfind": "keyword2",
	"string.gsub": "keyword2",
	"string.len": "keyword2",
	"string.lower": "keyword2",
	"string.rep": "keyword2",
	"string.sub": "keyword2",
	"string.upper": "keyword2",
	"table.concat": "keyword2",
	"table.foreach": "keyword2",
	"table.foreachi": "keyword2",
	"table.getn": "keyword2",
	"table.insert": "keyword2",
	"table.remove": "keyword2",
	"table.setn": "keyword2",
	"table.sort": "keyword2",
	"then": "keyword1",
	"tonumber": "keyword2",
	"tostring": "keyword2",
	"true": "keyword3",
	"type": "keyword2",
	"unpack": "keyword2",
	"until": "keyword1",
	"while": "keyword1",
	"xpcall": "keyword2",
}

# Dictionary of keywords dictionaries for lua mode.
keywordsDictDict = {
	"lua_main": lua_main_keywords_dict,
}

# Rules for lua_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="--[[", end="]]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="--",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="#!",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="[[", end="]]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="..",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="==",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule20(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule21(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule22(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule23(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"\"": [rule3,rule21,],
	"#": [rule2,],
	"'": [rule4,rule22,],
	"(": [rule19,],
	"*": [rule8,],
	"+": [rule6,],
	"-": [rule0,rule1,rule7,],
	".": [rule11,],
	"/": [rule9,],
	"0": [rule23,],
	"1": [rule23,],
	"2": [rule23,],
	"3": [rule23,],
	"4": [rule23,],
	"5": [rule23,],
	"6": [rule23,],
	"7": [rule23,],
	"8": [rule23,],
	"9": [rule23,],
	"<": [rule12,rule13,],
	"=": [rule16,rule18,],
	">": [rule14,rule15,],
	"@": [rule23,],
	"A": [rule23,],
	"B": [rule23,],
	"C": [rule23,],
	"D": [rule23,],
	"E": [rule23,],
	"F": [rule23,],
	"G": [rule23,],
	"H": [rule23,],
	"I": [rule23,],
	"J": [rule23,],
	"K": [rule23,],
	"L": [rule23,],
	"M": [rule23,],
	"N": [rule23,],
	"O": [rule23,],
	"P": [rule23,],
	"Q": [rule23,],
	"R": [rule23,],
	"S": [rule23,],
	"T": [rule23,],
	"U": [rule23,],
	"V": [rule23,],
	"W": [rule23,],
	"X": [rule23,],
	"Y": [rule23,],
	"Z": [rule23,],
	"[": [rule5,],
	"^": [rule10,],
	"_": [rule23,],
	"a": [rule23,],
	"b": [rule23,],
	"c": [rule23,],
	"d": [rule23,],
	"e": [rule23,],
	"f": [rule23,],
	"g": [rule23,],
	"h": [rule23,],
	"i": [rule23,],
	"j": [rule23,],
	"k": [rule23,],
	"l": [rule23,],
	"m": [rule23,],
	"n": [rule23,],
	"o": [rule23,],
	"p": [rule23,],
	"q": [rule23,],
	"r": [rule23,],
	"s": [rule23,],
	"t": [rule23,],
	"u": [rule23,],
	"v": [rule23,],
	"w": [rule23,],
	"x": [rule23,],
	"y": [rule23,],
	"z": [rule23,],
	"{": [rule20,],
	"~": [rule17,],
}

# x.rulesDictDict for lua mode.
rulesDictDict = {
	"lua_main": rulesDict1,
}

# Import dict for lua mode.
importDict = {}

