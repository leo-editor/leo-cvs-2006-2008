# Leo colorizer control file for powerdynamo mode.

# Properties for powerdynamo mode.
properties = {
	"commentEnd": "-->",
	"commentStart": "<!--",
	"indentCloseBrackets": "}",
	"indentOpenBrackets": "{",
	"lineComment": "//",
	"lineUpClosingBracket": "true",
	"wordBreakChars": " @ %^*()+=|\{}[]:;,.?$&",
}

# Keywords dict for powerdynamo_main ruleset.
powerdynamo_main_keywords_dict = {}

# Keywords dict for powerdynamo_tags ruleset.
powerdynamo_tags_keywords_dict = {}

# Keywords dict for powerdynamo_tags_literal ruleset.
powerdynamo_tags_literal_keywords_dict = {}

# Keywords dict for powerdynamo_powerdynamo_script ruleset.
powerdynamo_powerdynamo_script_keywords_dict = {
	"AskQuestion": "keyword3",
	"Close": "keyword3",
	"Commit": "keyword3",
	"Connect": "keyword3",
	"CreateConnection": "keyword3",
	"CreateDocument": "keyword3",
	"CreatePropertySheet": "keyword3",
	"CreateQuery": "keyword3",
	"CreateWizard": "keyword3",
	"DeleteConnection": "keyword3",
	"DeleteDocument": "keyword3",
	"Disconnect": "keyword3",
	"Exec": "keyword3",
	"Execute": "keyword3",
	"ExportTo": "keyword3",
	"GetCWD": "keyword3",
	"GetColumnCount": "keyword3",
	"GetColumnIndex": "keyword3",
	"GetColumnLabel": "keyword3",
	"GetConnection": "keyword3",
	"GetConnectionIdList": "keyword3",
	"GetConnectionNameList": "keyword3",
	"GetDirectory": "keyword3",
	"GetDocument": "keyword3",
	"GetEmpty": "keyword3",
	"GetEnv": "keyword3",
	"GetErrorCode": "keyword3",
	"GetErrorInfo": "keyword3",
	"GetEventList": "keyword3",
	"GetFilePtr": "keyword3",
	"GetGenerated": "keyword3",
	"GetRootDocument": "keyword3",
	"GetRowCount": "keyword3",
	"GetServerVariable": "keyword3",
	"GetState": "keyword3",
	"GetSupportedMoves": "keyword3",
	"GetValue": "keyword3",
	"ImportFrom": "keyword3",
	"Include": "keyword3",
	"Move": "keyword3",
	"MoveFirst": "keyword3",
	"MoveLast": "keyword3",
	"MoveNext": "keyword3",
	"MovePrevious": "keyword3",
	"MoveRelative": "keyword3",
	"OnEvent": "keyword3",
	"Open": "keyword3",
	"Opened": "keyword3",
	"ReadChar": "keyword3",
	"ReadLine": "keyword3",
	"Refresh": "keyword3",
	"Rollback": "keyword3",
	"Seek": "keyword3",
	"SetEnv": "keyword3",
	"SetSQL": "keyword3",
	"ShowMessage": "keyword3",
	"Write": "keyword3",
	"WriteLine": "keyword3",
	"abstract": "keyword1",
	"autoCommit": "keyword3",
	"boolean": "keyword1",
	"break": "keyword1",
	"byte": "keyword1",
	"cachedOutputTimeOut": "keyword3",
	"case": "keyword1",
	"catch": "keyword1",
	"char": "keyword1",
	"charAt": "keyword3",
	"class": "keyword1",
	"connectParameters": "keyword3",
	"connected": "keyword3",
	"connection": "keyword3",
	"connectionId": "keyword3",
	"connectionName": "keyword3",
	"connectionType": "keyword3",
	"contentType": "keyword3",
	"continue": "keyword1",
	"dataSource": "keyword3",
	"dataSourceList": "keyword3",
	"database": "keyword3",
	"default": "keyword1",
	"description": "keyword3",
	"do": "keyword1",
	"document": "keyword2",
	"double": "keyword1",
	"else": "keyword1",
	"eof": "keyword3",
	"errorNumber": "keyword3",
	"errorString": "keyword3",
	"exists": "keyword1",
	"extends": "keyword1",
	"false": "keyword1",
	"file": "keyword2",
	"final": "keyword1",
	"finally": "keyword1",
	"float": "keyword1",
	"for": "keyword1",
	"function": "keyword1",
	"id": "keyword3",
	"if": "keyword1",
	"implements": "keyword1",
	"import": "keyword1",
	"indexOf": "keyword3",
	"instanceof": "keyword1",
	"int": "keyword1",
	"interface": "keyword1",
	"lastIndexOf": "keyword3",
	"lastModified": "keyword3",
	"length": "keyword3",
	"location": "keyword3",
	"long": "keyword1",
	"mode": "keyword3",
	"name": "keyword3",
	"native": "keyword1",
	"new": "keyword1",
	"null": "keyword1",
	"package": "keyword1",
	"parent": "keyword3",
	"password": "keyword3",
	"private": "keyword1",
	"protected": "keyword1",
	"public": "keyword1",
	"query": "keyword2",
	"redirect": "keyword3",
	"return": "keyword1",
	"server": "keyword3",
	"session": "keyword2",
	"short": "keyword1",
	"simulateCursors": "keyword3",
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
	"timeOut": "keyword3",
	"toLowerCase": "keyword3",
	"toUpperCase": "keyword3",
	"transient": "keyword1",
	"true": "keyword1",
	"try": "keyword1",
	"type": "keyword3",
	"typeof": "keyword2",
	"userId": "keyword3",
	"value": "keyword3",
	"var": "keyword1",
	"void": "keyword1",
	"while": "keyword1",
	"write": "keyword3",
	"writeln": "keyword3",
}

# Keywords dict for powerdynamo_powerdynamo_tag_general ruleset.
powerdynamo_powerdynamo_tag_general_keywords_dict = {
	"NAME": "keyword2",
}

# Keywords dict for powerdynamo_powerdynamo_tag_data ruleset.
powerdynamo_powerdynamo_tag_data_keywords_dict = {
	"NAME": "keyword2",
	"QUERY": "keyword2",
}

# Keywords dict for powerdynamo_powerdynamo_tag_document ruleset.
powerdynamo_powerdynamo_tag_document_keywords_dict = {
	"CACHED_OUTPUT_TIMEOUT": "keyword2",
	"CONTENT_TYPE": "keyword2",
	"REDIRECT": "keyword2",
	"STATUS": "keyword2",
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

# Rules list for powerdynamo_main ruleset.
powerdynamo_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
	rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
	rule20, rule21, rule22, rule23, rule24, rule25, rule26, ]

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

# Rules list for powerdynamo_tags ruleset.
powerdynamo_tags_rules = [
	rule27, rule28, rule29, rule30, ]

# Rules for powerdynamo_tags_literal ruleset.

def rule31(colorer, s, i):
    return colorer.match_span(s, i, kind="label", begin="<!--script", end="?-->",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="powerdynamo-script",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

# Rules list for powerdynamo_tags_literal ruleset.
powerdynamo_tags_literal_rules = [
	rule31, ]

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

# Rules list for powerdynamo_powerdynamo_script ruleset.
powerdynamo_powerdynamo_script_rules = [
	rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40, rule41,
	rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49, rule50, rule51,
	rule52, rule53, rule54, rule55, rule56, rule57, rule58, rule59, rule60, rule61,
	rule62, rule63, ]

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

# Rules list for powerdynamo_powerdynamo_tag_general ruleset.
powerdynamo_powerdynamo_tag_general_rules = [
	rule64, rule65, rule66, ]

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

# Rules list for powerdynamo_powerdynamo_tag_data ruleset.
powerdynamo_powerdynamo_tag_data_rules = [
	rule67, rule68, rule69, ]

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

# Rules list for powerdynamo_powerdynamo_tag_document ruleset.
powerdynamo_powerdynamo_tag_document_rules = [
	rule70, rule71, rule72, ]

# Rules dict for powerdynamo mode.
rulesDict = {
	"powerdynamo_main": powerdynamo_main_rules,
	"powerdynamo_powerdynamo_script": powerdynamo_powerdynamo_script_rules,
	"powerdynamo_powerdynamo_tag_data": powerdynamo_powerdynamo_tag_data_rules,
	"powerdynamo_powerdynamo_tag_document": powerdynamo_powerdynamo_tag_document_rules,
	"powerdynamo_powerdynamo_tag_general": powerdynamo_powerdynamo_tag_general_rules,
	"powerdynamo_tags": powerdynamo_tags_rules,
	"powerdynamo_tags_literal": powerdynamo_tags_literal_rules,
}

# Import dict for powerdynamo mode.
importDict = {}

