# Leo colorizer control file for assembly-macro32 mode.

# Properties for assembly-macro32 mode.
properties = {
	"lineComment": ";",
}

# Keywords dict for assembly_macro32_main ruleset.
assembly_macro32_main_keywords_dict = {
	".ADDRESS": "keyword1",
	".ALIGN": "keyword1",
	".ASCIC": "keyword1",
	".ASCID": "keyword1",
	".ASCII": "keyword1",
	".ASCIZ": "keyword1",
	".BLKA": "keyword1",
	".BLKB": "keyword1",
	".BLKD": "keyword1",
	".BLKF": "keyword1",
	".BLKG": "keyword1",
	".BLKH": "keyword1",
	".BLKL": "keyword1",
	".BLKO": "keyword1",
	".BLKQ": "keyword1",
	".BLKW": "keyword1",
	".BYTE": "keyword1",
	".CROSS": "keyword1",
	".DEBUG": "keyword1",
	".DEFAULT": "keyword1",
	".DISABLE": "keyword1",
	".DOUBLE": "keyword1",
	".DSABL": "keyword1",
	".D_FLOATING": "keyword1",
	".ENABL": "keyword1",
	".ENABLE": "keyword1",
	".END": "keyword1",
	".ENDC": "keyword1",
	".ENDM": "keyword1",
	".ENDR": "keyword1",
	".ENTRY": "keyword1",
	".ERROR": "keyword1",
	".EVEN": "keyword1",
	".EXTERNAL": "keyword1",
	".EXTRN": "keyword1",
	".FLOAT": "keyword1",
	".F_FLOATING": "keyword1",
	".GLOBAL": "keyword1",
	".GLOBL": "keyword1",
	".G_FLOATING": "keyword1",
	".H_FLOATING": "keyword1",
	".IDENT": "keyword1",
	".IF": "keyword1",
	".IFF": "keyword1",
	".IFT": "keyword1",
	".IFTF": "keyword1",
	".IF_FALSE": "keyword1",
	".IF_TRUE": "keyword1",
	".IF_TRUE_FALSE": "keyword1",
	".IIF": "keyword1",
	".IRP": "keyword1",
	".IRPC": "keyword1",
	".LIBRARY": "keyword1",
	".LINK": "keyword1",
	".LIST": "keyword1",
	".LONG": "keyword1",
	".MACRO": "keyword1",
	".MASK": "keyword1",
	".MCALL": "keyword1",
	".MDELETE": "keyword1",
	".MEXIT": "keyword1",
	".NARG": "keyword1",
	".NCHR": "keyword1",
	".NLIST": "keyword1",
	".NOCROSS": "keyword1",
	".NOSHOW": "keyword1",
	".NTYPE": "keyword1",
	".OCTA": "keyword1",
	".ODD": "keyword1",
	".OPDEF": "keyword1",
	".PACKED": "keyword1",
	".PAGE": "keyword1",
	".PRINT": "keyword1",
	".PSECT": "keyword1",
	".QUAD": "keyword1",
	".REF1": "keyword1",
	".REF16": "keyword1",
	".REF2": "keyword1",
	".REF4": "keyword1",
	".REF8": "keyword1",
	".REPEAT": "keyword1",
	".REPT": "keyword1",
	".RESTORE": "keyword1",
	".RESTORE_PSECT": "keyword1",
	".SAVE": "keyword1",
	".SAVE_PSECT": "keyword1",
	".SBTTL": "keyword1",
	".SHOW": "keyword1",
	".SIGNED_BYTE": "keyword1",
	".SIGNED_WORD": "keyword1",
	".SUBTITLE": "keyword1",
	".TITLE": "keyword1",
	".TRANSFER": "keyword1",
	".WARN": "keyword1",
	".WEAK": "keyword1",
	".WORD": "keyword1",
	"ACBB": "function",
	"ACBD": "function",
	"ACBF": "function",
	"ACBG": "function",
	"ACBH": "function",
	"ACBL": "function",
	"ACBW": "function",
	"ADAWI": "function",
	"ADDB2": "function",
	"ADDB3": "function",
	"ADDD2": "function",
	"ADDD3": "function",
	"ADDF2": "function",
	"ADDF3": "function",
	"ADDG2": "function",
	"ADDG3": "function",
	"ADDH2": "function",
	"ADDH3": "function",
	"ADDL2": "function",
	"ADDL3": "function",
	"ADDP4": "function",
	"ADDP6": "function",
	"ADDW2": "function",
	"ADDW3": "function",
	"ADWC": "function",
	"AOBLEQ": "function",
	"AOBLSS": "function",
	"AP": "keyword3",
	"ASHL": "function",
	"ASHP": "function",
	"ASHQ": "function",
	"BBC": "function",
	"BBCC": "function",
	"BBCCI": "function",
	"BBCS": "function",
	"BBS": "function",
	"BBSC": "function",
	"BBSS": "function",
	"BBSSI": "function",
	"BCC": "function",
	"BCS": "function",
	"BEQL": "function",
	"BEQLU": "function",
	"BGEQ": "function",
	"BGEQU": "function",
	"BGTR": "function",
	"BGTRU": "function",
	"BICB2": "function",
	"BICB3": "function",
	"BICL2": "function",
	"BICL3": "function",
	"BICPSW": "function",
	"BICW2": "function",
	"BICW3": "function",
	"BISB2": "function",
	"BISB3": "function",
	"BISL2": "function",
	"BISL3": "function",
	"BISPSW": "function",
	"BISW2": "function",
	"BISW3": "function",
	"BITB": "function",
	"BITL": "function",
	"BITW": "function",
	"BLBC": "function",
	"BLBS": "function",
	"BLEQ": "function",
	"BLEQU": "function",
	"BLSS": "function",
	"BLSSU": "function",
	"BNEQ": "function",
	"BNEQU": "function",
	"BPT": "function",
	"BRB": "function",
	"BRW": "function",
	"BSBB": "function",
	"BSBW": "function",
	"BVC": "function",
	"BVS": "function",
	"CALLG": "function",
	"CALLS": "function",
	"CASEB": "function",
	"CASEL": "function",
	"CASEW": "function",
	"CHME": "function",
	"CHMK": "function",
	"CHMS": "function",
	"CHMU": "function",
	"CLRB": "function",
	"CLRD": "function",
	"CLRF": "function",
	"CLRG": "function",
	"CLRH": "function",
	"CLRL": "function",
	"CLRO": "function",
	"CLRQ": "function",
	"CLRW": "function",
	"CMPB": "function",
	"CMPC3": "function",
	"CMPC5": "function",
	"CMPD": "function",
	"CMPF": "function",
	"CMPG": "function",
	"CMPH": "function",
	"CMPL": "function",
	"CMPP3": "function",
	"CMPP4": "function",
	"CMPV": "function",
	"CMPW": "function",
	"CMPZV": "function",
	"CRC": "function",
	"CVTBD": "function",
	"CVTBF": "function",
	"CVTBG": "function",
	"CVTBH": "function",
	"CVTBL": "function",
	"CVTBW": "function",
	"CVTDB": "function",
	"CVTDF": "function",
	"CVTDH": "function",
	"CVTDL": "function",
	"CVTDW": "function",
	"CVTFB": "function",
	"CVTFD": "function",
	"CVTFG": "function",
	"CVTFH": "function",
	"CVTFL": "function",
	"CVTFW": "function",
	"CVTGB": "function",
	"CVTGF": "function",
	"CVTGH": "function",
	"CVTGL": "function",
	"CVTGW": "function",
	"CVTHB": "function",
	"CVTHD": "function",
	"CVTHF": "function",
	"CVTHG": "function",
	"CVTHL": "function",
	"CVTHW": "function",
	"CVTLB": "function",
	"CVTLD": "function",
	"CVTLF": "function",
	"CVTLG": "function",
	"CVTLH": "function",
	"CVTLP": "function",
	"CVTLW": "function",
	"CVTPL": "function",
	"CVTPS": "function",
	"CVTPT": "function",
	"CVTRDL": "function",
	"CVTRFL": "function",
	"CVTRGL": "function",
	"CVTRHL": "function",
	"CVTSP": "function",
	"CVTTP": "function",
	"CVTWB": "function",
	"CVTWD": "function",
	"CVTWF": "function",
	"CVTWG": "function",
	"CVTWH": "function",
	"CVTWL": "function",
	"DECB": "function",
	"DECL": "function",
	"DECW": "function",
	"DIVB2": "function",
	"DIVB3": "function",
	"DIVD2": "function",
	"DIVD3": "function",
	"DIVF2": "function",
	"DIVF3": "function",
	"DIVG2": "function",
	"DIVG3": "function",
	"DIVH2": "function",
	"DIVH3": "function",
	"DIVL2": "function",
	"DIVL3": "function",
	"DIVP": "function",
	"DIVW2": "function",
	"DIVW3": "function",
	"EDITPC": "function",
	"EDIV": "function",
	"EMODD": "function",
	"EMODF": "function",
	"EMODG": "function",
	"EMODH": "function",
	"EMUL": "function",
	"EXTV": "function",
	"EXTZV": "function",
	"FFC": "function",
	"FFS": "function",
	"FP": "keyword3",
	"HALT": "function",
	"INCB": "function",
	"INCL": "function",
	"INCW": "function",
	"INDEX": "function",
	"INSQHI": "function",
	"INSQTI": "function",
	"INSQUE": "function",
	"INSV": "function",
	"IOTA": "function",
	"JMP": "function",
	"JSB": "function",
	"LDPCTX": "function",
	"LOCC": "function",
	"MATCHC": "function",
	"MCOMB": "function",
	"MCOML": "function",
	"MCOMW": "function",
	"MFPR": "function",
	"MFVP": "function",
	"MNEGB": "function",
	"MNEGD": "function",
	"MNEGF": "function",
	"MNEGG": "function",
	"MNEGH": "function",
	"MNEGL": "function",
	"MNEGW": "function",
	"MOVAB": "function",
	"MOVAD": "function",
	"MOVAF": "function",
	"MOVAG": "function",
	"MOVAH": "function",
	"MOVAL": "function",
	"MOVAO": "function",
	"MOVAQ": "function",
	"MOVAW": "function",
	"MOVB": "function",
	"MOVC3": "function",
	"MOVC5": "function",
	"MOVD": "function",
	"MOVF": "function",
	"MOVG": "function",
	"MOVH": "function",
	"MOVL": "function",
	"MOVO": "function",
	"MOVP": "function",
	"MOVPSL": "function",
	"MOVQ": "function",
	"MOVTC": "function",
	"MOVTUC": "function",
	"MOVW": "function",
	"MOVZBL": "function",
	"MOVZBW": "function",
	"MOVZWL": "function",
	"MTPR": "function",
	"MTVP": "function",
	"MULB2": "function",
	"MULB3": "function",
	"MULD2": "function",
	"MULD3": "function",
	"MULF2": "function",
	"MULF3": "function",
	"MULG2": "function",
	"MULG3": "function",
	"MULH2": "function",
	"MULH3": "function",
	"MULL2": "function",
	"MULL3": "function",
	"MULP": "function",
	"MULW2": "function",
	"MULW3": "function",
	"NOP": "function",
	"PC": "keyword3",
	"POLYD": "function",
	"POLYF": "function",
	"POLYG": "function",
	"POLYH": "function",
	"POPR": "function",
	"PROBER": "function",
	"PROBEW": "function",
	"PUSHAB": "function",
	"PUSHABL": "function",
	"PUSHAD": "function",
	"PUSHAF": "function",
	"PUSHAG": "function",
	"PUSHAH": "function",
	"PUSHAL": "function",
	"PUSHAO": "function",
	"PUSHAQ": "function",
	"PUSHAW": "function",
	"PUSHL": "function",
	"PUSHR": "function",
	"R0": "keyword3",
	"R1": "keyword3",
	"R10": "keyword3",
	"R11": "keyword3",
	"R12": "keyword3",
	"R2": "keyword3",
	"R3": "keyword3",
	"R4": "keyword3",
	"R5": "keyword3",
	"R6": "keyword3",
	"R7": "keyword3",
	"R8": "keyword3",
	"R9": "keyword3",
	"REI": "function",
	"REMQHI": "function",
	"REMQTI": "function",
	"REMQUE": "function",
	"RET": "function",
	"ROTL": "function",
	"RSB": "function",
	"SBWC": "function",
	"SCANC": "function",
	"SKPC": "function",
	"SOBGEQ": "function",
	"SOBGTR": "function",
	"SP": "keyword3",
	"SPANC": "function",
	"SUBB2": "function",
	"SUBB3": "function",
	"SUBD2": "function",
	"SUBD3": "function",
	"SUBF2": "function",
	"SUBF3": "function",
	"SUBG2": "function",
	"SUBG3": "function",
	"SUBH2": "function",
	"SUBH3": "function",
	"SUBL2": "function",
	"SUBL3": "function",
	"SUBP4": "function",
	"SUBP6": "function",
	"SUBW2": "function",
	"SUBW3": "function",
	"SVPCTX": "function",
	"TSTB": "function",
	"TSTD": "function",
	"TSTF": "function",
	"TSTG": "function",
	"TSTH": "function",
	"TSTL": "function",
	"TSTW": "function",
	"VGATHL": "function",
	"VGATHQ": "function",
	"VLDL": "function",
	"VLDQ": "function",
	"VSADDD": "function",
	"VSADDF": "function",
	"VSADDG": "function",
	"VSADDL": "function",
	"VSBICL": "function",
	"VSBISL": "function",
	"VSCATL": "function",
	"VSCATQ": "function",
	"VSCMPD": "function",
	"VSCMPF": "function",
	"VSCMPG": "function",
	"VSCMPL": "function",
	"VSDIVD": "function",
	"VSDIVF": "function",
	"VSDIVG": "function",
	"VSMERGE": "function",
	"VSMULD": "function",
	"VSMULF": "function",
	"VSMULG": "function",
	"VSMULL": "function",
	"VSSLLL": "function",
	"VSSRLL": "function",
	"VSSUBD": "function",
	"VSSUBF": "function",
	"VSSUBG": "function",
	"VSSUBL": "function",
	"VSTL": "function",
	"VSTQ": "function",
	"VSXORL": "function",
	"VSYNC": "function",
	"VVADDD": "function",
	"VVADDF": "function",
	"VVADDG": "function",
	"VVADDL": "function",
	"VVBICL": "function",
	"VVBISL": "function",
	"VVCMPD": "function",
	"VVCMPF": "function",
	"VVCMPG": "function",
	"VVCMPL": "function",
	"VVCVT": "function",
	"VVDIVD": "function",
	"VVDIVF": "function",
	"VVDIVG": "function",
	"VVMERGE": "function",
	"VVMULD": "function",
	"VVMULF": "function",
	"VVMULG": "function",
	"VVMULL": "function",
	"VVSLLL": "function",
	"VVSRLL": "function",
	"VVSUBD": "function",
	"VVSUBF": "function",
	"VVSUBG": "function",
	"VVSUBL": "function",
	"VVXORL": "function",
	"XFC": "function",
	"XORB2": "function",
	"XORB3": "function",
	"XORL2": "function",
	"XORL3": "function",
	"XORW2": "function",
	"XORW3": "function",
}

# Dictionary of keywords dictionaries for assembly_macro32 mode.
keywordsDictDict = {
	"assembly_macro32_main": assembly_macro32_main_keywords_dict,
}

# Rules for assembly_macro32_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="label", pattern="%%"
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule4(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="%"
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule5(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="B^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="D^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="O^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="X^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="A^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="M^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="F^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="C^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="L^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="G^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="\",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule26(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for assembly_macro32_main ruleset.
assembly_macro32_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
	rule20, rule21, rule22, rule23, rule24, rule25, rule26, ]

# Rules dict for assembly_macro32 mode.
rulesDict = {
	"assembly_macro32_main": assembly_macro32_main_rules,
}

# Import dict for assembly_macro32 mode.
importDict = {}

