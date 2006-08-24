# Leo colorizer control file for powerdynamo mode.
# This file is in the public domain.

# Properties for powerdynamo mode.
properties = {
	"commentEnd": "-->",
	"commentStart": "<!--",
	"indentCloseBrackets": "}",
	"indentOpenBrackets": "{",
	"lineComment": "//",
	"lineUpClosingBracket": "true",
	"wordBreakChars": " @ %^*()+=|\\{}[]:;,.?$&",
}

# Attributes dict for powerdynamo_main ruleset.
powerdynamo_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for powerdynamo_tags ruleset.
powerdynamo_tags_attributes_dict = {
	"default": "MARKUP",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for powerdynamo_tags_literal ruleset.
powerdynamo_tags_literal_attributes_dict = {
	"default": "LITERAL1",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for powerdynamo_powerdynamo_script ruleset.
powerdynamo_powerdynamo_script_attributes_dict = {
	"default": "LITERAL1",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for powerdynamo_powerdynamo_tag_general ruleset.
powerdynamo_powerdynamo_tag_general_attributes_dict = {
	"default": "LITERAL1",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for powerdynamo_powerdynamo_tag_data ruleset.
powerdynamo_powerdynamo_tag_data_attributes_dict = {
	"default": "LITERAL1",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for powerdynamo_powerdynamo_tag_document ruleset.
powerdynamo_powerdynamo_tag_document_attributes_dict = {
	"default": "LITERAL1",
	"digit_re": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for powerdynamo mode.
attributesDictDict = {
	"powerdynamo_main": powerdynamo_main_attributes_dict,
	"powerdynamo_powerdynamo_script": powerdynamo_powerdynamo_script_attributes_dict,
	"powerdynamo_powerdynamo_tag_data": powerdynamo_powerdynamo_tag_data_attributes_dict,
	"powerdynamo_powerdynamo_tag_document": powerdynamo_powerdynamo_tag_document_attributes_dict,
	"powerdynamo_powerdynamo_tag_general": powerdynamo_powerdynamo_tag_general_attributes_dict,
	"powerdynamo_tags": powerdynamo_tags_attributes_dict,
	"powerdynamo_tags_literal": powerdynamo_tags_literal_attributes_dict,
}

# Keywords dict for powerdynamo_main ruleset.
powerdynamo_main_keywords_dict = {}

# Keywords dict for powerdynamo_tags ruleset.
powerdynamo_tags_keywords_dict = {}

# Keywords dict for powerdynamo_tags_literal ruleset.
powerdynamo_tags_literal_keywords_dict = {}

# Keywords dict for powerdynamo_powerdynamo_script ruleset.
powerdynamo_powerdynamo_script_keywords_dict = {
	"abstract": "keyword1",
	"askquestion": "keyword3",
	"autocommit": "keyword3",
	"boolean": "keyword1",
	"break": "keyword1",
	"byte": "keyword1",
	"cachedoutputtimeout": "keyword3",
	"case": "keyword1",
	"catch": "keyword1",
	"char": "keyword1",
	"charat": "keyword3",
	"class": "keyword1",
	"close": "keyword3",
	"commit": "keyword3",
	"connect": "keyword3",
	"connected": "keyword3",
	"connection": "keyword3",
	"connectionid": "keyword3",
	"connectionname": "keyword3",
	"connectiontype": "keyword3",
	"connectparameters": "keyword3",
	"contenttype": "keyword3",
	"continue": "keyword1",
	"createconnection": "keyword3",
	"createdocument": "keyword3",
	"createpropertysheet": "keyword3",
	"createquery": "keyword3",
	"createwizard": "keyword3",
	"database": "keyword3",
	"datasource": "keyword3",
	"datasourcelist": "keyword3",
	"default": "keyword1",
	"deleteconnection": "keyword3",
	"deletedocument": "keyword3",
	"description": "keyword3",
	"disconnect": "keyword3",
	"do": "keyword1",
	"document": "keyword2",
	"double": "keyword1",
	"else": "keyword1",
	"eof": "keyword3",
	"errornumber": "keyword3",
	"errorstring": "keyword3",
	"exec": "keyword3",
	"execute": "keyword3",
	"exists": "keyword1",
	"exportto": "keyword3",
	"extends": "keyword1",
	"false": "keyword1",
	"file": "keyword2",
	"final": "keyword1",
	"finally": "keyword1",
	"float": "keyword1",
	"for": "keyword1",
	"function": "keyword1",
	"getcolumncount": "keyword3",
	"getcolumnindex": "keyword3",
	"getcolumnlabel": "keyword3",
	"getconnection": "keyword3",
	"getconnectionidlist": "keyword3",
	"getconnectionnamelist": "keyword3",
	"getcwd": "keyword3",
	"getdirectory": "keyword3",
	"getdocument": "keyword3",
	"getempty": "keyword3",
	"getenv": "keyword3",
	"geterrorcode": "keyword3",
	"geterrorinfo": "keyword3",
	"geteventlist": "keyword3",
	"getfileptr": "keyword3",
	"getgenerated": "keyword3",
	"getrootdocument": "keyword3",
	"getrowcount": "keyword3",
	"getservervariable": "keyword3",
	"getstate": "keyword3",
	"getsupportedmoves": "keyword3",
	"getvalue": "keyword3",
	"id": "keyword3",
	"if": "keyword1",
	"implements": "keyword1",
	"import": "keyword1",
	"importfrom": "keyword3",
	"include": "keyword3",
	"indexof": "keyword3",
	"instanceof": "keyword1",
	"int": "keyword1",
	"interface": "keyword1",
	"lastindexof": "keyword3",
	"lastmodified": "keyword3",
	"length": "keyword3",
	"location": "keyword3",
	"long": "keyword1",
	"mode": "keyword3",
	"move": "keyword3",
	"movefirst": "keyword3",
	"movelast": "keyword3",
	"movenext": "keyword3",
	"moveprevious": "keyword3",
	"moverelative": "keyword3",
	"name": "keyword3",
	"native": "keyword1",
	"new": "keyword1",
	"null": "keyword1",
	"onevent": "keyword3",
	"open": "keyword3",
	"opened": "keyword3",
	"package": "keyword1",
	"parent": "keyword3",
	"password": "keyword3",
	"private": "keyword1",
	"protected": "keyword1",
	"public": "keyword1",
	"query": "keyword2",
	"readchar": "keyword3",
	"readline": "keyword3",
	"redirect": "keyword3",
	"refresh": "keyword3",
	"return": "keyword1",
	"rollback": "keyword3",
	"seek": "keyword3",
	"server": "keyword3",
	"session": "keyword2",
	"setenv": "keyword3",
	"setsql": "keyword3",
	"short": "keyword1",
	"showmessage": "keyword3",
	"simulatecursors": "keyword3",
	"site": "keyword2",
	"size": "keyword3",
	"source": "keyword3",
	"static": "keyword1",
	"status": "keyword3",
	"substring": "keyword3",
	"super": "keyword1",
	"switch": "keyword1",
	"synchronized": "keyword1",
	"system": "keyword2",
	"this": "keyword1",
	"threadsafe": "keyword1",
	"throw": "keyword1",
	"throws": "keyword1",
	"timeout": "keyword3",
	"tolowercase": "keyword3",
	"touppercase": "keyword3",
	"transient": "keyword1",
	"true": "keyword1",
	"try": "keyword1",
	"type": "keyword3",
	"typeof": "keyword2",
	"userid": "keyword3",
	"value": "keyword3",
	"var": "keyword1",
	"void": "keyword1",
	"while": "keyword1",
	"write": "keyword3",
	"writeline": "keyword3",
	"writeln": "keyword3",
}

# Keywords dict for powerdynamo_powerdynamo_tag_general ruleset.
powerdynamo_powerdynamo_tag_general_keywords_dict = {
	"name": "keyword2",
}

# Keywords dict for powerdynamo_powerdynamo_tag_data ruleset.
powerdynamo_powerdynamo_tag_data_keywords_dict = {
	"name": "keyword2",
	"query": "keyword2",
}

# Keywords dict for powerdynamo_powerdynamo_tag_document ruleset.
powerdynamo_powerdynamo_tag_document_keywords_dict = {
	"cached_output_timeout": "keyword2",
	"content_type": "keyword2",
	"redirect": "keyword2",
	"status": "keyword2",
}

# Dictionary of keywords dictionaries for powerdynamo mode.
keywordsDictDict = {
	"powerdynamo_main": powerdynamo_main_keywords_dict,
	"powerdynamo_powerdynamo_script": powerdynamo_powerdynamo_script_keywords_dict,
	"powerdynamo_powerdynamo_tag_data": powerdynamo_powerdynamo_tag_data_keywords_dict,
	"powerdynamo_powerdynamo_tag_document": powerdynamo_powerdynamo_tag_document_keywords_dict,
	"powerdynamo_powerdynamo_tag_general": powerdynamo_powerdynamo_tag_general_keywords_dict,
	"powerdynamo_tags": powerdynamo_tags_keywords_dict,
	"powerdynamo_tags_literal": powerdynamo_tags_literal_keywords_dict,
}

# Rules for powerdynamo_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="<!--script", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo-script",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="<!--data", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo-tag-data",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="<!--document", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo-tag-document",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="<!--evaluate", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo-script",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="<!--execute", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo-script",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule5(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="<!--formatting", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo-tag-general",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="<!--/formatting", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo-tag-general",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule7(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="<!--include", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo-tag-general",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule8(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="<!--label", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo-tag-general",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule9(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="<!--sql", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="transact-sql::MAIN",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule10(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="<!--sql_error_code", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo-tag-general",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule11(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="<!--sql_error_info", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo-tag-general",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule12(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="<!--sql_state", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo-tag-general",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule13(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="<!--sql_on_no_error", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo-tag-general",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule14(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="<!--/sql_on_no_error", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo-tag-general",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule15(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="<!--sql_on_error", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo-tag-general",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule16(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="<!--/sql_on_error", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo-tag-general",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule17(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="<!--sql_on_no_rows", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo-tag-general",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule18(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="<!--/sql_on_no_rows", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo-tag-general",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule19(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="<!--sql_on_rows", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo-tag-general",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule20(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="<!--/sql_on_rows", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo-tag-general",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule21(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="<!--", end="-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule22(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<SCRIPT", end="</SCRIPT>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="html::JAVASCRIPT",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule23(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<STYLE", end="</STYLE>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="html::CSS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule24(colorer, s, i):
    return colorer.match_span(s, i, kind="keyword2", begin="<!", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="xml::DTD-TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule25(colorer, s, i):
    return colorer.match_span(s, i, kind="markup", begin="<", end=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="TAGS",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule26(colorer, s, i):
    return colorer.match_span(s, i, kind="literal2", begin="&", end=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=True)

# Rules dict for main ruleset.
rulesDict1 = {
	"&": [rule26,],
	"<": [rule0,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,],
}

# Rules for powerdynamo_tags ruleset.

def rule27(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="<!--script", end="--?>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo-script",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule28(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="TAGS_LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule29(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="TAGS_LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule30(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

# Rules dict for tags ruleset.
rulesDict2 = {
	"\"": [rule28,],
	"'": [rule29,],
	"<": [rule27,],
	"=": [rule30,],
}

# Rules for powerdynamo_tags_literal ruleset.

def rule31(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="<!--script", end="?-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo-script",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules dict for tags_literal ruleset.
rulesDict3 = {
	"<": [rule31,],
}

# Rules for powerdynamo_powerdynamo_script ruleset.

def rule32(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule33(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo_LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule34(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo_LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule35(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule36(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
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
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule41(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule42(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule43(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule44(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule45(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule46(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule47(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule48(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule49(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule50(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule51(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule52(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule53(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule54(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule55(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule56(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule57(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule58(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule59(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="?",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule60(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule61(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule62(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule63(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for powerdynamo_script ruleset.
rulesDict4 = {
	"!": [rule37,],
	"\"": [rule33,],
	"%": [rule47,],
	"&": [rule48,],
	"'": [rule34,],
	"(": [rule62,],
	"*": [rule44,],
	"+": [rule41,],
	",": [rule55,],
	"-": [rule42,],
	".": [rule52,],
	"/": [rule32,rule35,rule43,],
	"0": [rule63,],
	"1": [rule63,],
	"2": [rule63,],
	"3": [rule63,],
	"4": [rule63,],
	"5": [rule63,],
	"6": [rule63,],
	"7": [rule63,],
	"8": [rule63,],
	"9": [rule63,],
	":": [rule61,],
	";": [rule56,],
	"<": [rule39,rule46,],
	"=": [rule36,rule40,],
	">": [rule38,rule45,],
	"?": [rule59,],
	"@": [rule60,rule63,],
	"A": [rule63,],
	"B": [rule63,],
	"C": [rule63,],
	"D": [rule63,],
	"E": [rule63,],
	"F": [rule63,],
	"G": [rule63,],
	"H": [rule63,],
	"I": [rule63,],
	"J": [rule63,],
	"K": [rule63,],
	"L": [rule63,],
	"M": [rule63,],
	"N": [rule63,],
	"O": [rule63,],
	"P": [rule63,],
	"Q": [rule63,],
	"R": [rule63,],
	"S": [rule63,],
	"T": [rule63,],
	"U": [rule63,],
	"V": [rule63,],
	"W": [rule63,],
	"X": [rule63,],
	"Y": [rule63,],
	"Z": [rule63,],
	"[": [rule58,],
	"]": [rule57,],
	"^": [rule50,],
	"_": [rule63,],
	"a": [rule63,],
	"b": [rule63,],
	"c": [rule63,],
	"d": [rule63,],
	"e": [rule63,],
	"f": [rule63,],
	"g": [rule63,],
	"h": [rule63,],
	"i": [rule63,],
	"j": [rule63,],
	"k": [rule63,],
	"l": [rule63,],
	"m": [rule63,],
	"n": [rule63,],
	"o": [rule63,],
	"p": [rule63,],
	"q": [rule63,],
	"r": [rule63,],
	"s": [rule63,],
	"t": [rule63,],
	"u": [rule63,],
	"v": [rule63,],
	"w": [rule63,],
	"x": [rule63,],
	"y": [rule63,],
	"z": [rule63,],
	"{": [rule54,],
	"|": [rule49,],
	"}": [rule53,],
	"~": [rule51,],
}

# Rules for powerdynamo_powerdynamo_tag_general ruleset.

def rule64(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo_LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule65(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo_LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule66(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for powerdynamo_tag_general ruleset.
rulesDict5 = {
	"\"": [rule64,],
	"'": [rule65,],
	"0": [rule66,],
	"1": [rule66,],
	"2": [rule66,],
	"3": [rule66,],
	"4": [rule66,],
	"5": [rule66,],
	"6": [rule66,],
	"7": [rule66,],
	"8": [rule66,],
	"9": [rule66,],
	"@": [rule66,],
	"A": [rule66,],
	"B": [rule66,],
	"C": [rule66,],
	"D": [rule66,],
	"E": [rule66,],
	"F": [rule66,],
	"G": [rule66,],
	"H": [rule66,],
	"I": [rule66,],
	"J": [rule66,],
	"K": [rule66,],
	"L": [rule66,],
	"M": [rule66,],
	"N": [rule66,],
	"O": [rule66,],
	"P": [rule66,],
	"Q": [rule66,],
	"R": [rule66,],
	"S": [rule66,],
	"T": [rule66,],
	"U": [rule66,],
	"V": [rule66,],
	"W": [rule66,],
	"X": [rule66,],
	"Y": [rule66,],
	"Z": [rule66,],
	"_": [rule66,],
	"a": [rule66,],
	"b": [rule66,],
	"c": [rule66,],
	"d": [rule66,],
	"e": [rule66,],
	"f": [rule66,],
	"g": [rule66,],
	"h": [rule66,],
	"i": [rule66,],
	"j": [rule66,],
	"k": [rule66,],
	"l": [rule66,],
	"m": [rule66,],
	"n": [rule66,],
	"o": [rule66,],
	"p": [rule66,],
	"q": [rule66,],
	"r": [rule66,],
	"s": [rule66,],
	"t": [rule66,],
	"u": [rule66,],
	"v": [rule66,],
	"w": [rule66,],
	"x": [rule66,],
	"y": [rule66,],
	"z": [rule66,],
}

# Rules for powerdynamo_powerdynamo_tag_data ruleset.

def rule67(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo_LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule68(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo_LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule69(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for powerdynamo_tag_data ruleset.
rulesDict6 = {
	"\"": [rule67,],
	"'": [rule68,],
	"0": [rule69,],
	"1": [rule69,],
	"2": [rule69,],
	"3": [rule69,],
	"4": [rule69,],
	"5": [rule69,],
	"6": [rule69,],
	"7": [rule69,],
	"8": [rule69,],
	"9": [rule69,],
	"@": [rule69,],
	"A": [rule69,],
	"B": [rule69,],
	"C": [rule69,],
	"D": [rule69,],
	"E": [rule69,],
	"F": [rule69,],
	"G": [rule69,],
	"H": [rule69,],
	"I": [rule69,],
	"J": [rule69,],
	"K": [rule69,],
	"L": [rule69,],
	"M": [rule69,],
	"N": [rule69,],
	"O": [rule69,],
	"P": [rule69,],
	"Q": [rule69,],
	"R": [rule69,],
	"S": [rule69,],
	"T": [rule69,],
	"U": [rule69,],
	"V": [rule69,],
	"W": [rule69,],
	"X": [rule69,],
	"Y": [rule69,],
	"Z": [rule69,],
	"_": [rule69,],
	"a": [rule69,],
	"b": [rule69,],
	"c": [rule69,],
	"d": [rule69,],
	"e": [rule69,],
	"f": [rule69,],
	"g": [rule69,],
	"h": [rule69,],
	"i": [rule69,],
	"j": [rule69,],
	"k": [rule69,],
	"l": [rule69,],
	"m": [rule69,],
	"n": [rule69,],
	"o": [rule69,],
	"p": [rule69,],
	"q": [rule69,],
	"r": [rule69,],
	"s": [rule69,],
	"t": [rule69,],
	"u": [rule69,],
	"v": [rule69,],
	"w": [rule69,],
	"x": [rule69,],
	"y": [rule69,],
	"z": [rule69,],
}

# Rules for powerdynamo_powerdynamo_tag_document ruleset.

def rule70(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo_LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule71(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo_LITERAL",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule72(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for powerdynamo_tag_document ruleset.
rulesDict7 = {
	"\"": [rule70,],
	"'": [rule71,],
	"0": [rule72,],
	"1": [rule72,],
	"2": [rule72,],
	"3": [rule72,],
	"4": [rule72,],
	"5": [rule72,],
	"6": [rule72,],
	"7": [rule72,],
	"8": [rule72,],
	"9": [rule72,],
	"@": [rule72,],
	"A": [rule72,],
	"B": [rule72,],
	"C": [rule72,],
	"D": [rule72,],
	"E": [rule72,],
	"F": [rule72,],
	"G": [rule72,],
	"H": [rule72,],
	"I": [rule72,],
	"J": [rule72,],
	"K": [rule72,],
	"L": [rule72,],
	"M": [rule72,],
	"N": [rule72,],
	"O": [rule72,],
	"P": [rule72,],
	"Q": [rule72,],
	"R": [rule72,],
	"S": [rule72,],
	"T": [rule72,],
	"U": [rule72,],
	"V": [rule72,],
	"W": [rule72,],
	"X": [rule72,],
	"Y": [rule72,],
	"Z": [rule72,],
	"_": [rule72,],
	"a": [rule72,],
	"b": [rule72,],
	"c": [rule72,],
	"d": [rule72,],
	"e": [rule72,],
	"f": [rule72,],
	"g": [rule72,],
	"h": [rule72,],
	"i": [rule72,],
	"j": [rule72,],
	"k": [rule72,],
	"l": [rule72,],
	"m": [rule72,],
	"n": [rule72,],
	"o": [rule72,],
	"p": [rule72,],
	"q": [rule72,],
	"r": [rule72,],
	"s": [rule72,],
	"t": [rule72,],
	"u": [rule72,],
	"v": [rule72,],
	"w": [rule72,],
	"x": [rule72,],
	"y": [rule72,],
	"z": [rule72,],
}

# x.rulesDictDict for powerdynamo mode.
rulesDictDict = {
	"powerdynamo_main": rulesDict1,
	"powerdynamo_powerdynamo_script": rulesDict4,
	"powerdynamo_powerdynamo_tag_data": rulesDict6,
	"powerdynamo_powerdynamo_tag_document": rulesDict7,
	"powerdynamo_powerdynamo_tag_general": rulesDict5,
	"powerdynamo_tags": rulesDict2,
	"powerdynamo_tags_literal": rulesDict3,
}

# Import dict for powerdynamo mode.
importDict = {}

