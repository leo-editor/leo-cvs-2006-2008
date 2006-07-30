# Leo colorizer control file for mqsc mode.
# This file is in the public domain.

# Properties for mqsc mode.
properties = {
	"lineComment": "*",
}

# Attributes dict for mqsc_main ruleset.
mqsc_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for mqsc mode.
attributesDictDict = {
	"mqsc_main": mqsc_main_attributes_dict,
}

# Keywords dict for mqsc_main ruleset.
mqsc_main_keywords_dict = {
	"all": "keyword1",
	"alt": "keyword1",
	"altdate": "markup",
	"alter": "keyword1",
	"alttime": "markup",
	"applicid": "markup",
	"appltype": "markup",
	"authorev": "markup",
	"batches": "markup",
	"batchint": "markup",
	"batchsz": "markup",
	"boqname": "markup",
	"bothresh": "markup",
	"bufsrcvd": "markup",
	"bufssent": "markup",
	"bytsrcvd": "markup",
	"bytssent": "markup",
	"ccsid": "markup",
	"chad": "markup",
	"chadev": "markup",
	"chadexit": "markup",
	"channel": "markup",
	"chl": "keyword2",
	"chltype": "markup",
	"chst": "keyword2",
	"chstada": "markup",
	"chstati": "markup",
	"chstatus": "keyword2",
	"clear": "keyword1",
	"clusdate": "markup",
	"clusinfo": "markup",
	"clusnl": "markup",
	"clusqmgr": "markup",
	"clusqt": "markup",
	"cluster": "markup",
	"clustime": "markup",
	"clwldata": "markup",
	"clwlexit": "markup",
	"clwlwen": "markup",
	"cmdlevel": "markup",
	"commandq": "markup",
	"conname": "markup",
	"convert": "markup",
	"crdate": "markup",
	"crtime": "markup",
	"curdepth": "markup",
	"curluwid": "markup",
	"curmsgs": "markup",
	"curseqno": "markup",
	"deadq": "markup",
	"def": "keyword1",
	"defbind": "markup",
	"define": "keyword1",
	"defprty": "markup",
	"defpsist": "markup",
	"defsopt": "markup",
	"deftype": "markup",
	"defxmitq": "markup",
	"delete": "keyword1",
	"descr": "markup",
	"dis": "keyword1",
	"discint": "markup",
	"display": "keyword1",
	"distl": "markup",
	"end": "keyword1",
	"envrdata": "markup",
	"get": "markup",
	"hardenbo": "markup",
	"hbint": "markup",
	"indoubt": "markup",
	"inhibtev": "markup",
	"initq": "markup",
	"ipprocs": "markup",
	"jobname": "markup",
	"like": "keyword1",
	"localev": "markup",
	"longrts": "markup",
	"longrty": "markup",
	"longtmr": "markup",
	"lstluwid": "markup",
	"lstmsgda": "markup",
	"lstmsgti": "markup",
	"lstseqno": "markup",
	"maxdepth": "markup",
	"maxhands": "markup",
	"maxmsgl": "markup",
	"maxprty": "markup",
	"maxumsgs": "markup",
	"mcaname": "markup",
	"mcastat": "markup",
	"mcatype": "markup",
	"mcauser": "markup",
	"modename": "markup",
	"mrdata": "markup",
	"mrexit": "markup",
	"mrrty": "markup",
	"mrtmr": "markup",
	"msgdata": "markup",
	"msgdlvsq": "markup",
	"msgexit": "markup",
	"msgs": "markup",
	"namcount": "markup",
	"namelist": "keyword2",
	"names": "markup",
	"netprty": "markup",
	"nl": "keyword2",
	"npmspeed": "markup",
	"opprocs": "markup",
	"password": "markup",
	"perfmev": "markup",
	"ping": "keyword1",
	"platform": "markup",
	"proc": "keyword2",
	"process": "markup",
	"put": "markup",
	"putaut": "markup",
	"qa": "keyword2",
	"qalias": "keyword2",
	"qc": "keyword2",
	"qcluster": "keyword2",
	"qdepthhi": "markup",
	"qdepthlo": "markup",
	"qdphiev": "markup",
	"qdploev": "markup",
	"qdpmaxev": "markup",
	"ql": "keyword2",
	"qlocal": "keyword2",
	"qm": "keyword2",
	"qmgr": "keyword2",
	"qmid": "markup",
	"qmname": "markup",
	"qmodel": "keyword2",
	"qmtype": "markup",
	"qr": "keyword2",
	"qremote": "keyword2",
	"qsvciev": "markup",
	"qsvcint": "markup",
	"qtype": "markup",
	"queue": "keyword2",
	"rcvdata": "markup",
	"rcvexit": "markup",
	"ref": "keyword1",
	"refresh": "keyword1",
	"remoteev": "markup",
	"replace": "keyword1",
	"repos": "markup",
	"reposnl": "markup",
	"reset": "keyword1",
	"resolve": "keyword1",
	"resume": "keyword1",
	"retintvl": "markup",
	"rname": "markup",
	"rqmname": "markup",
	"scope": "markup",
	"scydata": "markup",
	"scyexit": "markup",
	"senddata": "markup",
	"sendexit": "markup",
	"seqwrap": "markup",
	"share": "markup",
	"shortrts": "markup",
	"shortrty": "markup",
	"shorttmr": "markup",
	"start": "keyword1",
	"status": "markup",
	"stop": "keyword1",
	"stopreq": "markup",
	"strstpev": "markup",
	"suspend": "markup",
	"syncpt": "markup",
	"targq": "markup",
	"tpname": "markup",
	"trigdata": "markup",
	"trigdpth": "markup",
	"trigger": "markup",
	"trigint": "markup",
	"trigmpri": "markup",
	"trigtype": "markup",
	"trptype": "markup",
	"type": "markup",
	"usage": "markup",
	"userdata": "markup",
	"userid": "markup",
	"xmitq": "markup",
}

# Dictionary of keywords dictionaries for mqsc mode.
keywordsDictDict = {
	"mqsc_main": mqsc_main_keywords_dict,
}

# Rules for mqsc_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="*",
        at_line_start=True, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="('", end="')",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=True,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="(", end=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=True,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"(": [rule1,rule2,],
	"*": [rule0,],
	"+": [rule3,],
	"0": [rule4,],
	"1": [rule4,],
	"2": [rule4,],
	"3": [rule4,],
	"4": [rule4,],
	"5": [rule4,],
	"6": [rule4,],
	"7": [rule4,],
	"8": [rule4,],
	"9": [rule4,],
	"@": [rule4,],
	"A": [rule4,],
	"B": [rule4,],
	"C": [rule4,],
	"D": [rule4,],
	"E": [rule4,],
	"F": [rule4,],
	"G": [rule4,],
	"H": [rule4,],
	"I": [rule4,],
	"J": [rule4,],
	"K": [rule4,],
	"L": [rule4,],
	"M": [rule4,],
	"N": [rule4,],
	"O": [rule4,],
	"P": [rule4,],
	"Q": [rule4,],
	"R": [rule4,],
	"S": [rule4,],
	"T": [rule4,],
	"U": [rule4,],
	"V": [rule4,],
	"W": [rule4,],
	"X": [rule4,],
	"Y": [rule4,],
	"Z": [rule4,],
	"a": [rule4,],
	"b": [rule4,],
	"c": [rule4,],
	"d": [rule4,],
	"e": [rule4,],
	"f": [rule4,],
	"g": [rule4,],
	"h": [rule4,],
	"i": [rule4,],
	"j": [rule4,],
	"k": [rule4,],
	"l": [rule4,],
	"m": [rule4,],
	"n": [rule4,],
	"o": [rule4,],
	"p": [rule4,],
	"q": [rule4,],
	"r": [rule4,],
	"s": [rule4,],
	"t": [rule4,],
	"u": [rule4,],
	"v": [rule4,],
	"w": [rule4,],
	"x": [rule4,],
	"y": [rule4,],
	"z": [rule4,],
}

# x.rulesDictDict for mqsc mode.
rulesDictDict = {
	"mqsc_main": rulesDict1,
}

# Import dict for mqsc mode.
importDict = {}

