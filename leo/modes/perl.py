# Leo colorizer control file for perl mode.
# This file is in the public domain.

# Properties for perl mode.
properties = {
	"indentCloseBrackets": "}",
	"indentOpenBrackets": "{",
	"lineComment": "#",
	"lineUpClosingBracket": "true",
}

# Keywords dict for perl_main ruleset.
perl_main_keywords_dict = {
	"BEGIN": "keyword1",
	"END": "keyword1",
	"abs": "keyword3",
	"accept": "keyword3",
	"alarm": "keyword3",
	"and": "operator",
	"atan2": "keyword3",
	"bind": "keyword3",
	"binmode": "keyword3",
	"bless": "keyword3",
	"caller": "keyword1",
	"chdir": "keyword3",
	"chmod": "keyword3",
	"chomp": "keyword3",
	"chop": "keyword3",
	"chown": "keyword3",
	"chr": "keyword3",
	"chroot": "keyword3",
	"close": "keyword3",
	"closedir": "keyword3",
	"cmp": "operator",
	"connect": "keyword3",
	"continue": "keyword1",
	"cos": "keyword3",
	"crypt": "keyword3",
	"dbmclose": "keyword3",
	"dbmopen": "keyword3",
	"defined": "keyword3",
	"delete": "keyword3",
	"die": "keyword1",
	"do": "keyword1",
	"dump": "keyword1",
	"each": "keyword3",
	"else": "keyword1",
	"elsif": "keyword1",
	"endgrent": "keyword3",
	"endhostent": "keyword3",
	"endnetent": "keyword3",
	"endprotoent": "keyword3",
	"endpwent": "keyword3",
	"endservent": "keyword3",
	"eof": "keyword3",
	"eq": "operator",
	"eval": "keyword1",
	"exec": "keyword3",
	"exists": "keyword3",
	"exit": "keyword1",
	"exp": "keyword3",
	"fcntl": "keyword3",
	"fileno": "keyword3",
	"flock": "keyword3",
	"for": "keyword1",
	"foreach": "keyword1",
	"fork": "keyword3",
	"format": "keyword3",
	"formline": "keyword3",
	"ge": "operator",
	"getc": "keyword3",
	"getgrent": "keyword3",
	"getgrgid": "keyword3",
	"getgrnam": "keyword3",
	"gethostbyaddr": "keyword3",
	"gethostbyname": "keyword3",
	"gethostent": "keyword3",
	"getlogin": "keyword3",
	"getnetbyaddr": "keyword3",
	"getnetbyname": "keyword3",
	"getnetent": "keyword3",
	"getpeername": "keyword3",
	"getpgrp": "keyword3",
	"getppid": "keyword3",
	"getpriority": "keyword3",
	"getprotobyname": "keyword3",
	"getprotobynumber": "keyword3",
	"getprotoent": "keyword3",
	"getpwent": "keyword3",
	"getpwnam": "keyword3",
	"getpwuid": "keyword3",
	"getservbyname": "keyword3",
	"getservbyport": "keyword3",
	"getservent": "keyword3",
	"getsockname": "keyword3",
	"getsockopt": "keyword3",
	"glob": "keyword3",
	"gmtime": "keyword3",
	"goto": "keyword1",
	"grep": "keyword3",
	"hex": "keyword3",
	"if": "keyword1",
	"import": "keyword1",
	"index": "keyword3",
	"int": "keyword3",
	"ioctl": "keyword3",
	"join": "keyword3",
	"keys": "keyword3",
	"kill": "keyword3",
	"last": "keyword1",
	"lc": "keyword3",
	"lcfirst": "keyword3",
	"le": "operator",
	"length": "keyword3",
	"link": "keyword3",
	"listen": "keyword3",
	"local": "keyword1",
	"localtime": "keyword3",
	"log": "keyword3",
	"lstat": "keyword3",
	"map": "keyword3",
	"mkdir": "keyword3",
	"msgctl": "keyword3",
	"msgget": "keyword3",
	"msgrcv": "keyword3",
	"msgsnd": "keyword3",
	"my": "keyword1",
	"ne": "operator",
	"new": "keyword1",
	"next": "keyword1",
	"no": "keyword1",
	"not": "operator",
	"oct": "keyword3",
	"open": "keyword3",
	"opendir": "keyword3",
	"or": "operator",
	"ord": "keyword3",
	"our": "keyword1",
	"pack": "keyword3",
	"package": "keyword1",
	"pipe": "keyword3",
	"pop": "keyword3",
	"pos": "keyword3",
	"print": "keyword3",
	"printf": "keyword3",
	"push": "keyword3",
	"quotemeta": "keyword3",
	"rand": "keyword3",
	"read": "keyword3",
	"readdir": "keyword3",
	"readlink": "keyword3",
	"recv": "keyword3",
	"redo": "keyword1",
	"ref": "keyword3",
	"rename": "keyword3",
	"require": "keyword1",
	"reset": "keyword3",
	"return": "keyword1",
	"reverse": "keyword3",
	"rewinddir": "keyword3",
	"rindex": "keyword3",
	"rmdir": "keyword3",
	"scalar": "keyword3",
	"seek": "keyword3",
	"seekdir": "keyword3",
	"select": "keyword3",
	"semctl": "keyword3",
	"semget": "keyword3",
	"semop": "keyword3",
	"send": "keyword3",
	"setgrent": "keyword3",
	"sethostent": "keyword3",
	"setnetent": "keyword3",
	"setpgrp": "keyword3",
	"setpriority": "keyword3",
	"setprotoent": "keyword3",
	"setpwent": "keyword3",
	"setservent": "keyword3",
	"setsockopt": "keyword3",
	"shift": "keyword3",
	"shmctl": "keyword3",
	"shmget": "keyword3",
	"shmread": "keyword3",
	"shmwrite": "keyword3",
	"shutdown": "keyword3",
	"sin": "keyword3",
	"sleep": "keyword3",
	"socket": "keyword3",
	"socketpair": "keyword3",
	"sort": "keyword3",
	"splice": "keyword3",
	"split": "keyword3",
	"sprintf": "keyword3",
	"sqrt": "keyword3",
	"srand": "keyword3",
	"stat": "keyword3",
	"study": "keyword3",
	"sub": "keyword1",
	"substr": "keyword3",
	"symlink": "keyword3",
	"syscall": "keyword3",
	"sysread": "keyword3",
	"sysseek": "keyword3",
	"system": "keyword3",
	"syswrite": "keyword3",
	"tell": "keyword3",
	"telldir": "keyword3",
	"tie": "keyword3",
	"tied": "keyword3",
	"time": "keyword3",
	"times": "keyword3",
	"truncate": "keyword3",
	"uc": "keyword3",
	"ucfirst": "keyword3",
	"umask": "keyword3",
	"undef": "keyword3",
	"unless": "keyword1",
	"unlink": "keyword3",
	"unpack": "keyword3",
	"unshift": "keyword3",
	"untie": "keyword3",
	"until": "keyword1",
	"use": "keyword1",
	"utime": "keyword3",
	"values": "keyword3",
	"vec": "keyword3",
	"wait": "keyword3",
	"waitpid": "keyword3",
	"wantarray": "keyword1",
	"warn": "keyword3",
	"while": "keyword1",
	"write": "keyword3",
	"x": "operator",
	"xor": "operator",
}

# Keywords dict for perl_pod ruleset.
perl_pod_keywords_dict = {}

# Keywords dict for perl_literal ruleset.
perl_literal_keywords_dict = {}

# Keywords dict for perl_exec ruleset.
perl_exec_keywords_dict = {}

# Keywords dict for perl_variable ruleset.
perl_variable_keywords_dict = {}

# Keywords dict for perl_regexp ruleset.
perl_regexp_keywords_dict = {}

# Dictionary of keywords dictionaries for perl mode.
keywordsDictDict = {
	"perl_exec": perl_exec_keywords_dict,
	"perl_literal": perl_literal_keywords_dict,
	"perl_main": perl_main_keywords_dict,
	"perl_pod": perl_pod_keywords_dict,
	"perl_regexp": perl_regexp_keywords_dict,
	"perl_variable": perl_variable_keywords_dict,
}

# Rules for perl_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="=head1", end="=cut",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="POD",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="=head2", end="=cut",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="POD",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="=head3", end="=cut",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="POD",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="=head4", end="=cut",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="POD",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="=item", end="=cut",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="POD",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="=over", end="=cut",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="POD",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule7(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="=back", end="=cut",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="POD",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule8(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="=pod", end="=cut",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="POD",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule9(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="=for", end="=cut",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="POD",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule10(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="=begin", end="=cut",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="POD",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule11(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="=end", end="=cut",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="POD",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="$`",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="$'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="keyword2", seq="$\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="${", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="VARIABLE",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule16(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="\\$(?:#|\\w)+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="@(?:#|\\w)+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="keyword2", seq="%(?:#|\\w)+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="@{", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="VARIABLE",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule20(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="%{", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="VARIABLE",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule21(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule22(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule23(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword3", begin="`", end="`",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="EXEC",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule24(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="literal2", begin="<<[:space:]*(['\"])([[:space:][:alnum:]_]*)\\1;?\\s*", end="$2",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule25(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="literal2", begin="<<([[:alpha:]_][[:alnum:]_]*);?\\s*", end="$1",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule26(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="markup", seq="/[^[:blank:]]*?[^\\\\]/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule27(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="markup", seq="q(?:|[qrx])\\{(?:.*?[^\\\\])*?\\}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule28(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="markup", seq="tr([[:punct:]])(?:.*?[^\\\\])*?\\1(?:.*?[^\\\\])*?\\1",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule29(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="markup", seq="y([[:punct:]])(?:.*?[^\\\\])*?\\1(?:.*?[^\\\\])*?\\1",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule30(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="markup", seq="m\\{(?:.*?[^\\\\])*?\\}[sgiexom]*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule31(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="markup", seq="m([[:punct:]])(?:.*?[^\\\\])*?\\1[sgiexom]*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule32(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="markup", seq="s\\s*\\{(?:.*?[^\\\\])*?\\}\\s*\\{(?:.*?[^\\\\])*?\\}[sgiexom]*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule33(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="markup", seq="s([[:punct:]])(?:.*?[^\\\\])*?\\1(?:.*?[^\\\\])*?\\1[sgiexom]*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule34(colorer, s, i):
    return colorer.match_seq_regexp(s, i, kind="markup", seq="/[^[:blank:]]*?/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule35(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule36(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule37(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule38(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule39(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule40(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule41(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule42(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule43(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule44(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule45(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule46(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule47(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule48(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule49(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule50(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule51(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule52(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="?",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule53(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule54(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule37,rule43,],
	"\"": [rule21,],
	"#": [rule0,],
	"$": [rule12,rule13,rule14,rule15,],
	"%": [rule18,rule20,],
	"&": [rule36,],
	"'": [rule22,],
	"*": [rule47,],
	"+": [rule44,],
	"-": [rule45,],
	"/": [rule26,rule34,rule46,],
	"0": [rule54,],
	"1": [rule54,],
	"2": [rule54,],
	"3": [rule54,],
	"4": [rule54,],
	"5": [rule54,],
	"6": [rule54,],
	"7": [rule54,],
	"8": [rule54,],
	"9": [rule54,],
	":": [rule53,],
	"<": [rule24,rule25,rule39,rule41,],
	"=": [rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule42,],
	">": [rule38,rule40,],
	"?": [rule52,],
	"@": [rule17,rule19,rule54,],
	"A": [rule54,],
	"B": [rule54,],
	"C": [rule54,],
	"D": [rule54,],
	"E": [rule54,],
	"F": [rule54,],
	"G": [rule54,],
	"H": [rule54,],
	"I": [rule54,],
	"J": [rule54,],
	"K": [rule54,],
	"L": [rule54,],
	"M": [rule54,],
	"N": [rule54,],
	"O": [rule54,],
	"P": [rule54,],
	"Q": [rule54,],
	"R": [rule54,],
	"S": [rule54,],
	"T": [rule54,],
	"U": [rule54,],
	"V": [rule54,],
	"W": [rule54,],
	"X": [rule54,],
	"Y": [rule54,],
	"Z": [rule54,],
	"\\": [rule16,],
	"^": [rule48,],
	"_": [rule54,],
	"`": [rule23,],
	"a": [rule54,],
	"b": [rule54,],
	"c": [rule54,],
	"d": [rule54,],
	"e": [rule54,],
	"f": [rule54,],
	"g": [rule54,],
	"h": [rule54,],
	"i": [rule54,],
	"j": [rule54,],
	"k": [rule54,],
	"l": [rule54,],
	"m": [rule30,rule31,rule54,],
	"n": [rule54,],
	"o": [rule54,],
	"p": [rule54,],
	"q": [rule27,rule54,],
	"r": [rule54,],
	"s": [rule32,rule33,rule54,],
	"t": [rule28,rule54,],
	"u": [rule54,],
	"v": [rule54,],
	"w": [rule54,],
	"x": [rule54,],
	"y": [rule29,rule54,],
	"z": [rule54,],
	"{": [rule51,],
	"|": [rule35,],
	"}": [rule50,],
	"~": [rule49,],
}

# Rules for perl_pod ruleset.

def rule55(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="label", pattern="=",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=False)

# Rules dict for pod ruleset.
rulesDict2 = {
	"=": [rule55,],
}

# Rules for perl_literal ruleset.

def rule56(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="${", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="VARIABLE",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule57(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule58(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule59(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="@{", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="VARIABLE",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule60(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule61(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="%{", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="VARIABLE",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule62(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule63(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule64(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule65(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule66(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule67(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule68(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule69(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule70(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule71(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule72(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule73(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule74(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule75(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule76(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule77(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule78(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule79(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule80(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq=".",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule81(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule82(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule83(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule84(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule85(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq="?",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule86(colorer, s, i):
    return colorer.match_seq(s, i, kind="literal1", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

# Rules dict for literal ruleset.
rulesDict3 = {
	"!": [rule65,rule71,],
	"$": [rule56,rule57,rule58,],
	"%": [rule61,rule62,],
	"&": [rule64,],
	"(": [rule69,],
	")": [rule68,],
	"*": [rule75,],
	"+": [rule72,],
	",": [rule81,],
	"-": [rule73,],
	".": [rule80,],
	"/": [rule74,],
	":": [rule86,],
	";": [rule82,],
	"<": [rule67,],
	"=": [rule70,],
	">": [rule66,],
	"?": [rule85,],
	"@": [rule59,rule60,],
	"[": [rule84,],
	"]": [rule83,],
	"^": [rule76,],
	"{": [rule79,],
	"|": [rule63,],
	"}": [rule78,],
	"~": [rule77,],
}

# Rules for perl_exec ruleset.

def rule87(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule88(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="${", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule89(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule90(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="$",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule91(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="@{", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule92(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule93(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="%{", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule94(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

# Rules dict for exec ruleset.
rulesDict4 = {
	"#": [rule87,],
	"$": [rule88,rule89,rule90,],
	"%": [rule93,rule94,],
	"@": [rule91,rule92,],
}

# Rules for perl_variable ruleset.

def rule95(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="{", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="VARIABLE",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule96(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

# Rules dict for variable ruleset.
rulesDict5 = {
	"-": [rule96,],
	"{": [rule95,],
}

# Rules for perl_regexp ruleset.

def rule97(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq=")(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule98(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq=")[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule99(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq="){",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule100(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq="](",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule101(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq="][",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule102(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq="]{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule103(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq="}(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule104(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq="}[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule105(colorer, s, i):
    return colorer.match_seq(s, i, kind="markup", seq="}{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule106(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="(", end=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="REGEXP",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule107(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="[", end="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="REGEXP",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule108(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="{", end="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="REGEXP",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules dict for regexp ruleset.
rulesDict6 = {
	"(": [rule106,],
	")": [rule97,rule98,rule99,],
	"[": [rule107,],
	"]": [rule100,rule101,rule102,],
	"{": [rule108,],
	"}": [rule103,rule104,rule105,],
}

# x.rulesDictDict for perl mode.
rulesDictDict = {
	"perl_exec": rulesDict4,
	"perl_literal": rulesDict3,
	"perl_main": rulesDict1,
	"perl_pod": rulesDict2,
	"perl_regexp": rulesDict6,
	"perl_variable": rulesDict5,
}

# Import dict for perl mode.
importDict = {}

