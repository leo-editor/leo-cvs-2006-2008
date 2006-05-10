# Leo colorizer control file for assembly-x86 mode.
# This file is in the public domain.

# Properties for assembly-x86 mode.
properties = {
	"lineComment": ";",
}

# Attributes dict for assembly_x86_main ruleset.
assembly_x86_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for assembly_x86 mode.
attributesDictDict = {
	"assembly_x86_main": assembly_x86_main_attributes_dict,
}

# Keywords dict for assembly_x86_main ruleset.
assembly_x86_main_keywords_dict = {
	".186": "keyword1",
	".286": "keyword1",
	".286P": "keyword1",
	".287": "keyword1",
	".386": "keyword1",
	".386P": "keyword1",
	".387": "keyword1",
	".486": "keyword1",
	".486P": "keyword1",
	".586": "keyword1",
	".586P": "keyword1",
	".686": "keyword1",
	".686P": "keyword1",
	".8086": "keyword1",
	".8087": "keyword1",
	".ALPHA": "keyword1",
	".BREAK": "keyword1",
	".BSS": "keyword1",
	".CODE": "keyword1",
	".CONST": "keyword1",
	".CONTINUE": "keyword1",
	".CREF": "keyword1",
	".DATA": "keyword1",
	".DATA?": "keyword1",
	".DOSSEG": "keyword1",
	".ELSE": "keyword1",
	".ELSEIF": "keyword1",
	".ENDIF": "keyword1",
	".ENDW": "keyword1",
	".ERR": "keyword1",
	".ERR1": "keyword1",
	".ERR2": "keyword1",
	".ERRB": "keyword1",
	".ERRDEF": "keyword1",
	".ERRDIF": "keyword1",
	".ERRDIFI": "keyword1",
	".ERRE": "keyword1",
	".ERRIDN": "keyword1",
	".ERRIDNI": "keyword1",
	".ERRNB": "keyword1",
	".ERRNDEF": "keyword1",
	".ERRNZ": "keyword1",
	".EXIT": "keyword1",
	".FARDATA": "keyword1",
	".FARDATA?": "keyword1",
	".IF": "keyword1",
	".K3D": "keyword1",
	".LALL": "keyword1",
	".LFCOND": "keyword1",
	".LIST": "keyword1",
	".LISTALL": "keyword1",
	".LISTIF": "keyword1",
	".LISTMACRO": "keyword1",
	".LISTMACROALL": "keyword1",
	".MMX": "keyword1",
	".MODEL": "keyword1",
	".MSFLOAT": "keyword1",
	".NO87": "keyword1",
	".NOCREF": "keyword1",
	".NOLIST": "keyword1",
	".NOLISTIF": "keyword1",
	".NOLISTMACRO": "keyword1",
	".RADIX": "keyword1",
	".REPEAT": "keyword1",
	".SALL": "keyword1",
	".SEQ": "keyword1",
	".SFCOND": "keyword1",
	".STACK": "keyword1",
	".STARTUP": "keyword1",
	".TEXT": "keyword1",
	".TFCOND": "keyword1",
	".UNTIL": "keyword1",
	".UNTILCXZ": "keyword1",
	".WHILE": "keyword1",
	".XALL": "keyword1",
	".XCREF": "keyword1",
	".XLIST": "keyword1",
	".XMM": "keyword1",
	"A16": "keyword1",
	"A32": "keyword1",
	"AAA": "function",
	"AAD": "function",
	"AAM": "function",
	"AAS": "function",
	"ADC": "function",
	"ADD": "function",
	"ADDPS": "function",
	"ADDR": "keyword1",
	"ADDSS": "function",
	"AH": "keyword3",
	"AL": "keyword3",
	"ALIGN": "keyword1",
	"ALIGNB": "keyword1",
	"AND": "function",
	"ANDNPS": "function",
	"ANDPS": "function",
	"ARPL": "function",
	"ASSUME": "keyword1",
	"AX": "keyword3",
	"BH": "keyword3",
	"BITS": "keyword1",
	"BL": "keyword3",
	"BOUND": "function",
	"BP": "keyword3",
	"BSF": "function",
	"BSR": "function",
	"BSWAP": "function",
	"BT": "function",
	"BTC": "function",
	"BTR": "function",
	"BTS": "function",
	"BX": "keyword3",
	"BYTE": "keyword2",
	"CALL": "function",
	"CARRY?": "keyword1",
	"CATSTR": "keyword1",
	"CBW": "function",
	"CDQ": "function",
	"CH": "keyword3",
	"CL": "keyword3",
	"CLC": "function",
	"CLD": "function",
	"CLI": "function",
	"CLTS": "function",
	"CMC": "function",
	"CMOVA": "function",
	"CMOVAE": "function",
	"CMOVB": "function",
	"CMOVBE": "function",
	"CMOVC": "function",
	"CMOVE": "function",
	"CMOVG": "function",
	"CMOVGE": "function",
	"CMOVL": "function",
	"CMOVLE": "function",
	"CMOVNA": "function",
	"CMOVNAE": "function",
	"CMOVNB": "function",
	"CMOVNBE": "function",
	"CMOVNC": "function",
	"CMOVNE": "function",
	"CMOVNG": "function",
	"CMOVNGE": "function",
	"CMOVNL": "function",
	"CMOVNLE": "function",
	"CMOVNO": "function",
	"CMOVNP": "function",
	"CMOVNS": "function",
	"CMOVNZ": "function",
	"CMOVO": "function",
	"CMOVP": "function",
	"CMOVPE": "function",
	"CMOVPO": "function",
	"CMOVS": "function",
	"CMOVZ": "function",
	"CMP": "function",
	"CMPPS": "function",
	"CMPS": "function",
	"CMPSB": "function",
	"CMPSD": "function",
	"CMPSS": "function",
	"CMPSW": "function",
	"CMPXCHG": "function",
	"CMPXCHGB": "function",
	"CODESEG": "keyword1",
	"COMISS": "function",
	"COMM": "keyword1",
	"COMMENT": "keyword1",
	"COMMON": "keyword1",
	"CPUID": "function",
	"CR0": "keyword3",
	"CR2": "keyword3",
	"CR3": "keyword3",
	"CR4": "keyword3",
	"CS": "keyword3",
	"CVTPI2PS": "function",
	"CVTPS2PI": "function",
	"CVTSI2SS": "function",
	"CVTSS2SI": "function",
	"CVTTPS2PI": "function",
	"CVTTSS2SI": "function",
	"CWD": "function",
	"CWDE": "function",
	"CX": "keyword3",
	"DAA": "function",
	"DAS": "function",
	"DATASEG": "keyword1",
	"DB": "keyword2",
	"DD": "keyword2",
	"DEC": "function",
	"DF": "keyword2",
	"DH": "keyword3",
	"DI": "keyword3",
	"DIV": "function",
	"DIVPS": "function",
	"DIVSS": "function",
	"DL": "keyword3",
	"DOSSEG": "keyword1",
	"DQ": "keyword2",
	"DR0": "keyword3",
	"DR1": "keyword3",
	"DR2": "keyword3",
	"DR3": "keyword3",
	"DR4": "keyword3",
	"DR5": "keyword3",
	"DR6": "keyword3",
	"DR7": "keyword3",
	"DS": "keyword3",
	"DT": "keyword2",
	"DUP": "keyword2",
	"DW": "keyword2",
	"DWORD": "keyword2",
	"DX": "keyword3",
	"EAX": "keyword3",
	"EBP": "keyword3",
	"EBX": "keyword3",
	"ECHO": "keyword1",
	"ECX": "keyword3",
	"EDI": "keyword3",
	"EDX": "keyword3",
	"ELSE": "keyword1",
	"ELSEIF": "keyword1",
	"ELSEIF1": "keyword1",
	"ELSEIF2": "keyword1",
	"ELSEIFB": "keyword1",
	"ELSEIFDEF": "keyword1",
	"ELSEIFE": "keyword1",
	"ELSEIFIDN": "keyword1",
	"ELSEIFNB": "keyword1",
	"ELSEIFNDEF": "keyword1",
	"EMMS": "function",
	"END": "keyword1",
	"ENDIF": "keyword1",
	"ENDM": "keyword1",
	"ENDP": "keyword1",
	"ENDS": "keyword1",
	"ENDSTRUC": "keyword1",
	"ENTER": "function",
	"EQU": "keyword2",
	"ES": "keyword3",
	"ESI": "keyword3",
	"ESP": "keyword3",
	"EVEN": "keyword1",
	"EXITM": "keyword1",
	"EXPORT": "keyword1",
	"EXTERN": "keyword1",
	"EXTERNDEF": "keyword1",
	"EXTRN": "keyword1",
	"F2XM1": "function",
	"FABS": "function",
	"FADD": "function",
	"FADDP": "function",
	"FAR": "keyword1",
	"FBLD": "function",
	"FBSTP": "function",
	"FCHS": "function",
	"FCLEX": "function",
	"FCMOVB": "function",
	"FCMOVBE": "function",
	"FCMOVE": "function",
	"FCMOVNB": "function",
	"FCMOVNBE": "function",
	"FCMOVNE": "function",
	"FCMOVNU": "function",
	"FCMOVU": "function",
	"FCOM": "function",
	"FCOMI": "function",
	"FCOMIP": "function",
	"FCOMP": "function",
	"FCOMPP": "function",
	"FCOS": "function",
	"FDECSTP": "function",
	"FDIV": "function",
	"FDIVP": "function",
	"FDIVR": "function",
	"FDIVRP": "function",
	"FEMMS": "function",
	"FFREE": "function",
	"FIADD": "function",
	"FICOM": "function",
	"FICOMP": "function",
	"FIDIV": "function",
	"FIDIVR": "function",
	"FILD": "function",
	"FIMUL": "function",
	"FINCSTP": "function",
	"FINIT": "function",
	"FIST": "function",
	"FISTP": "function",
	"FISUB": "function",
	"FISUBR": "function",
	"FLD1": "function",
	"FLDCW": "function",
	"FLDENV": "function",
	"FLDL2E": "function",
	"FLDL2T": "function",
	"FLDLG2": "function",
	"FLDLN2": "function",
	"FLDPI": "function",
	"FLDZ": "function",
	"FMUL": "function",
	"FMULP": "function",
	"FNCLEX": "function",
	"FNINIT": "function",
	"FNOP": "function",
	"FNSAVE": "function",
	"FNSTCW": "function",
	"FNSTENV": "function",
	"FNSTSW": "function",
	"FOR": "keyword1",
	"FORC": "keyword1",
	"FPATAN": "function",
	"FPREM": "function",
	"FPREMI": "function",
	"FPTAN": "function",
	"FRNDINT": "function",
	"FRSTOR": "function",
	"FS": "keyword3",
	"FSAVE": "function",
	"FSCALE": "function",
	"FSIN": "function",
	"FSINCOS": "function",
	"FSQRT": "function",
	"FST": "function",
	"FSTCW": "function",
	"FSTENV": "function",
	"FSTP": "function",
	"FSTSW": "function",
	"FSUB": "function",
	"FSUBP": "function",
	"FSUBR": "function",
	"FSUBRP": "function",
	"FTST": "function",
	"FUCOM": "function",
	"FUCOMI": "function",
	"FUCOMIP": "function",
	"FUCOMP": "function",
	"FUCOMPP": "function",
	"FWAIT": "function",
	"FWORD": "keyword2",
	"FXAM": "function",
	"FXCH": "function",
	"FXRSTOR": "function",
	"FXSAVE": "function",
	"FXTRACT": "function",
	"FYL2X": "function",
	"FYL2XP1": "function",
	"GLOBAL": "keyword1",
	"GOTO": "keyword1",
	"GROUP": "keyword1",
	"GS": "keyword3",
	"HIGH": "keyword1",
	"HIGHWORD": "keyword1",
	"HLT": "function",
	"IDIV": "function",
	"IEND": "keyword1",
	"IF": "keyword1",
	"IF1": "keyword1",
	"IF2": "keyword1",
	"IFB": "keyword1",
	"IFDEF": "keyword1",
	"IFDIF": "keyword1",
	"IFDIFI": "keyword1",
	"IFE": "keyword1",
	"IFIDN": "keyword1",
	"IFIDNI": "keyword1",
	"IFNB": "keyword1",
	"IFNDEF": "keyword1",
	"IMPORT": "keyword1",
	"IMUL": "function",
	"IN": "function",
	"INC": "function",
	"INCBIN": "keyword1",
	"INCLUDE": "keyword1",
	"INCLUDELIB": "keyword1",
	"INS": "function",
	"INSB": "function",
	"INSD": "function",
	"INSTR": "keyword1",
	"INSW": "function",
	"INT": "function",
	"INTO": "function",
	"INVD": "function",
	"INVLPG": "function",
	"INVOKE": "keyword1",
	"IRET": "function",
	"IRP": "keyword1",
	"IRPC": "keyword1",
	"ISTRUC": "keyword1",
	"JA": "function",
	"JAE": "function",
	"JB": "function",
	"JBE": "function",
	"JC": "function",
	"JCXZ": "function",
	"JE": "function",
	"JECXZ": "function",
	"JG": "function",
	"JGE": "function",
	"JL": "function",
	"JLE": "function",
	"JMP": "function",
	"JNA": "function",
	"JNAE": "function",
	"JNB": "function",
	"JNBE": "function",
	"JNC": "function",
	"JNE": "function",
	"JNG": "function",
	"JNGE": "function",
	"JNL": "function",
	"JNLE": "function",
	"JNO": "function",
	"JNP": "function",
	"JNS": "function",
	"JNZ": "function",
	"JO": "function",
	"JP": "function",
	"JPE": "function",
	"JPO": "function",
	"JS": "function",
	"JZ": "function",
	"LABEL": "keyword1",
	"LAHF": "function",
	"LAR": "function",
	"LDMXCSR": "function",
	"LDS": "function",
	"LEA": "function",
	"LEAVE": "function",
	"LENGTH": "keyword1",
	"LENGTHOF": "keyword1",
	"LES": "function",
	"LFS": "function",
	"LGDT": "function",
	"LGS": "function",
	"LIDT": "function",
	"LLDT": "function",
	"LMSW": "function",
	"LOCAL": "keyword1",
	"LOCK": "function",
	"LODS": "function",
	"LODSB": "function",
	"LODSD": "function",
	"LODSW": "function",
	"LOOP": "function",
	"LOOPE": "function",
	"LOOPNE": "function",
	"LOOPNZ": "function",
	"LOOPZ": "function",
	"LOW": "keyword1",
	"LOWWORD": "keyword1",
	"LROFFSET": "keyword1",
	"LSL": "function",
	"LSS": "function",
	"LTR": "function",
	"MACRO": "keyword1",
	"MASKMOVQ": "function",
	"MAXPS": "function",
	"MAXSS": "function",
	"MINPS": "function",
	"MINSS": "function",
	"MM0": "keyword3",
	"MM1": "keyword3",
	"MM2": "keyword3",
	"MM3": "keyword3",
	"MM4": "keyword3",
	"MM5": "keyword3",
	"MM6": "keyword3",
	"MM7": "keyword3",
	"MOV": "function",
	"MOVAPS": "function",
	"MOVD": "function",
	"MOVHLPS": "function",
	"MOVHPS": "function",
	"MOVLHPS": "function",
	"MOVLPS": "function",
	"MOVMSKPS": "function",
	"MOVNTPS": "function",
	"MOVNTQ": "function",
	"MOVQ": "function",
	"MOVS": "function",
	"MOVSB": "function",
	"MOVSD": "function",
	"MOVSS": "function",
	"MOVSW": "function",
	"MOVSX": "function",
	"MOVUPS": "function",
	"MOVZX": "function",
	"MUL": "function",
	"MULPS": "function",
	"MULSS": "function",
	"NAME": "keyword1",
	"NEAR": "keyword1",
	"NEG": "function",
	"NOP": "function",
	"NOSPLIT": "keyword1",
	"NOT": "function",
	"O16": "keyword1",
	"O32": "keyword1",
	"OFFSET": "keyword1",
	"OPATTR": "keyword1",
	"OPTION": "keyword1",
	"OR": "function",
	"ORG": "keyword1",
	"ORPS": "function",
	"OUT": "function",
	"OUTS": "function",
	"OUTSB": "function",
	"OUTSD": "function",
	"OUTSW": "function",
	"OVERFLOW?": "keyword1",
	"PACKSSDW": "function",
	"PACKSSWB": "function",
	"PACKUSWB": "function",
	"PADDB": "function",
	"PADDD": "function",
	"PADDSB": "function",
	"PADDSW": "function",
	"PADDUSB": "function",
	"PADDUSW": "function",
	"PADDW": "function",
	"PAGE": "keyword1",
	"PAND": "function",
	"PANDN": "function",
	"PARITY?": "keyword1",
	"PAVGB": "function",
	"PAVGUSB": "function",
	"PAVGW": "function",
	"PCMPEQB": "function",
	"PCMPEQD": "function",
	"PCMPEQW": "function",
	"PCMPGTB": "function",
	"PCMPGTD": "function",
	"PCMPGTW": "function",
	"PEXTRW": "function",
	"PF2ID": "function",
	"PF2IW": "function",
	"PFACC": "function",
	"PFADD": "function",
	"PFCMPEQ": "function",
	"PFCMPGE": "function",
	"PFCMPGT": "function",
	"PFMAX": "function",
	"PFMIN": "function",
	"PFMUL": "function",
	"PFNACC": "function",
	"PFPNACC": "function",
	"PFRCP": "function",
	"PFRCPIT1": "function",
	"PFRCPIT2": "function",
	"PFRSQIT1": "function",
	"PFRSQRT": "function",
	"PFSUB": "function",
	"PFSUBR": "function",
	"PI2FD": "function",
	"PI2FW": "function",
	"PINSRW": "function",
	"PMADDWD": "function",
	"PMAXSW": "function",
	"PMAXUB": "function",
	"PMINSW": "function",
	"PMINUB": "function",
	"PMOVMSKB": "function",
	"PMULHRW": "function",
	"PMULHUW": "function",
	"PMULHW": "function",
	"PMULLW": "function",
	"POP": "function",
	"POPA": "function",
	"POPAD": "function",
	"POPAW": "function",
	"POPCONTEXT": "keyword1",
	"POPF": "function",
	"POPFD": "function",
	"POPFW": "function",
	"POR": "function",
	"PREFETCH": "function",
	"PREFETCHNTA": "function",
	"PREFETCHT0": "function",
	"PREFETCHT1": "function",
	"PREFETCHT2": "function",
	"PREFETCHW": "function",
	"PRIVATE": "keyword1",
	"PROC": "keyword1",
	"PROTO": "keyword1",
	"PSADBW": "function",
	"PSHUFW": "function",
	"PSLLD": "function",
	"PSLLQ": "function",
	"PSLLW": "function",
	"PSRAD": "function",
	"PSRAW": "function",
	"PSRLD": "function",
	"PSRLQ": "function",
	"PSRLW": "function",
	"PSUBB": "function",
	"PSUBD": "function",
	"PSUBSB": "function",
	"PSUBSW": "function",
	"PSUBUSB": "function",
	"PSUBUSW": "function",
	"PSUBW": "function",
	"PSWAPD": "function",
	"PTR": "keyword1",
	"PUBLIC": "keyword1",
	"PUNPCKHBW": "function",
	"PUNPCKHDQ": "function",
	"PUNPCKHWD": "function",
	"PUNPCKLBW": "function",
	"PUNPCKLDQ": "function",
	"PUNPCKLWD": "function",
	"PURGE": "keyword1",
	"PUSH": "function",
	"PUSHA": "function",
	"PUSHAD": "function",
	"PUSHAW": "function",
	"PUSHCONTEXT": "keyword1",
	"PUSHF": "function",
	"PUSHFD": "function",
	"PUSHFW": "function",
	"PXOR": "function",
	"QWORD": "keyword2",
	"RCL": "function",
	"RCR": "function",
	"RDMSR": "function",
	"RDPMC": "function",
	"RDTSC": "function",
	"REAL10": "keyword2",
	"REAL4": "keyword2",
	"REAL8": "keyword2",
	"RECORD": "keyword1",
	"REP": "function",
	"REPE": "function",
	"REPEAT": "keyword1",
	"REPNE": "function",
	"REPNZ": "function",
	"REPT": "keyword1",
	"REPZ": "function",
	"RESB": "keyword2",
	"RESD": "keyword2",
	"RESQ": "keyword2",
	"REST": "keyword2",
	"RESW": "keyword2",
	"RET": "function",
	"RETF": "function",
	"RETN": "function",
	"ROL": "function",
	"ROR": "function",
	"RSM": "function",
	"SAHF": "function",
	"SAL": "function",
	"SAR": "function",
	"SBB": "function",
	"SBYTE": "keyword2",
	"SCAS": "function",
	"SCASB": "function",
	"SCASD": "function",
	"SCASW": "function",
	"SDWORD": "keyword2",
	"SECTION": "keyword1",
	"SEG": "keyword1",
	"SEGMENT": "keyword1",
	"SETA": "function",
	"SETAE": "function",
	"SETB": "function",
	"SETBE": "function",
	"SETC": "function",
	"SETE": "function",
	"SETG": "function",
	"SETGE": "function",
	"SETL": "function",
	"SETLE": "function",
	"SETNA": "function",
	"SETNAE": "function",
	"SETNB": "function",
	"SETNBE": "function",
	"SETNC": "function",
	"SETNE": "function",
	"SETNG": "function",
	"SETNGE": "function",
	"SETNL": "function",
	"SETNLE": "function",
	"SETNO": "function",
	"SETNP": "function",
	"SETNS": "function",
	"SETNZ": "function",
	"SETO": "function",
	"SETP": "function",
	"SETPE": "function",
	"SETPO": "function",
	"SETS": "function",
	"SETZ": "function",
	"SFENCE": "function",
	"SGDT": "function",
	"SHL": "function",
	"SHLD": "function",
	"SHORT": "keyword1",
	"SHR": "function",
	"SHRD": "function",
	"SHUFPS": "function",
	"SI": "keyword3",
	"SIDT": "function",
	"SIGN?": "keyword1",
	"SIZE": "keyword1",
	"SIZEOF": "keyword1",
	"SIZESTR": "keyword1",
	"SLDT": "function",
	"SMSW": "function",
	"SP": "keyword3",
	"SQRTPS": "function",
	"SQRTSS": "function",
	"SS": "keyword3",
	"ST": "keyword3",
	"ST0": "keyword3",
	"ST1": "keyword3",
	"ST2": "keyword3",
	"ST3": "keyword3",
	"ST4": "keyword3",
	"ST5": "keyword3",
	"ST6": "keyword3",
	"ST7": "keyword3",
	"STACK": "keyword1",
	"STC": "function",
	"STD": "function",
	"STI": "function",
	"STMXCSR": "function",
	"STOS": "function",
	"STOSB": "function",
	"STOSD": "function",
	"STOSW": "function",
	"STR": "function",
	"STRUC": "keyword1",
	"STRUCT": "keyword1",
	"SUB": "function",
	"SUBPS": "function",
	"SUBSS": "function",
	"SUBSTR": "keyword1",
	"SUBTITLE": "keyword1",
	"SUBTTL": "keyword1",
	"SWORD": "keyword2",
	"SYSENTER": "function",
	"SYSEXIT": "function",
	"TBYTE": "keyword2",
	"TEST": "function",
	"TEXTEQU": "keyword2",
	"THIS": "keyword1",
	"TIMES": "keyword2",
	"TITLE": "keyword1",
	"TR3": "keyword3",
	"TR4": "keyword3",
	"TR5": "keyword3",
	"TR6": "keyword3",
	"TR7": "keyword3",
	"TWORD": "keyword2",
	"TYPE": "keyword1",
	"TYPEDEF": "keyword1",
	"UB2": "function",
	"UCOMISS": "function",
	"UNION": "keyword1",
	"UNPCKHPS": "function",
	"UNPCKLPS": "function",
	"USE16": "keyword1",
	"USE32": "keyword1",
	"USES": "keyword1",
	"VERR": "function",
	"VERW": "function",
	"WAIT": "function",
	"WBINVD": "function",
	"WHILE": "keyword1",
	"WORD": "keyword2",
	"WRMSR": "function",
	"WRT": "keyword1",
	"XADD": "function",
	"XCHG": "function",
	"XLAT": "function",
	"XLATB": "function",
	"XMM0": "keyword3",
	"XMM1": "keyword3",
	"XMM2": "keyword3",
	"XMM3": "keyword3",
	"XMM4": "keyword3",
	"XMM5": "keyword3",
	"XMM6": "keyword3",
	"XMM7": "keyword3",
	"XOR": "function",
	"XORPS": "function",
	"ZERO?": "keyword1",
	"__FILE__": "keyword1",
	"__LINE__": "keyword1",
}

# Dictionary of keywords dictionaries for assembly_x86 mode.
keywordsDictDict = {
	"assembly_x86_main": assembly_x86_main_keywords_dict,
}

# Rules for assembly_x86_main ruleset.

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
    return colorer.match_mark_following(s, i, kind="label", pattern="%%",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule4(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="%",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule5(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule15,],
	"\"": [rule2,],
	"%": [rule3,rule4,rule10,],
	"&": [rule13,],
	"'": [rule1,],
	"*": [rule9,],
	"+": [rule6,],
	"-": [rule7,],
	"/": [rule8,],
	"0": [rule19,],
	"1": [rule19,],
	"2": [rule19,],
	"3": [rule19,],
	"4": [rule19,],
	"5": [rule19,],
	"6": [rule19,],
	"7": [rule19,],
	"8": [rule19,],
	"9": [rule19,],
	":": [rule5,],
	";": [rule0,],
	"<": [rule17,],
	"=": [rule16,],
	">": [rule18,],
	"@": [rule19,],
	"A": [rule19,],
	"B": [rule19,],
	"C": [rule19,],
	"D": [rule19,],
	"E": [rule19,],
	"F": [rule19,],
	"G": [rule19,],
	"H": [rule19,],
	"I": [rule19,],
	"J": [rule19,],
	"K": [rule19,],
	"L": [rule19,],
	"M": [rule19,],
	"N": [rule19,],
	"O": [rule19,],
	"P": [rule19,],
	"Q": [rule19,],
	"R": [rule19,],
	"S": [rule19,],
	"T": [rule19,],
	"U": [rule19,],
	"V": [rule19,],
	"W": [rule19,],
	"X": [rule19,],
	"Y": [rule19,],
	"Z": [rule19,],
	"^": [rule12,],
	"_": [rule19,],
	"a": [rule19,],
	"b": [rule19,],
	"c": [rule19,],
	"d": [rule19,],
	"e": [rule19,],
	"f": [rule19,],
	"g": [rule19,],
	"h": [rule19,],
	"i": [rule19,],
	"j": [rule19,],
	"k": [rule19,],
	"l": [rule19,],
	"m": [rule19,],
	"n": [rule19,],
	"o": [rule19,],
	"p": [rule19,],
	"q": [rule19,],
	"r": [rule19,],
	"s": [rule19,],
	"t": [rule19,],
	"u": [rule19,],
	"v": [rule19,],
	"w": [rule19,],
	"x": [rule19,],
	"y": [rule19,],
	"z": [rule19,],
	"|": [rule11,],
	"~": [rule14,],
}

# x.rulesDictDict for assembly_x86 mode.
rulesDictDict = {
	"assembly_x86_main": rulesDict1,
}

# Import dict for assembly_x86 mode.
importDict = {}

