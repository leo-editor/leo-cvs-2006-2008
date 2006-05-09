# Leo colorizer control file for tsql mode.

# Properties for tsql mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"lineComment": "--",
}

# Keywords dict for tsql_main ruleset.
tsql_main_keywords_dict = {
	"@@CONNECTIONS": "keyword2",
	"@@CPU_BUSY": "keyword2",
	"@@CURSOR_ROWS": "keyword2",
	"@@DATEFIRST": "keyword2",
	"@@DBTS": "keyword2",
	"@@ERROR": "keyword2",
	"@@FETCH_STATUS": "keyword2",
	"@@IDENTITY": "keyword2",
	"@@IDLE": "keyword2",
	"@@IO_BUSY": "keyword2",
	"@@LANGID": "keyword2",
	"@@LANGUAGE": "keyword2",
	"@@LOCK_TIMEOUT": "keyword2",
	"@@MAX_CONNECTIONS": "keyword2",
	"@@MAX_PRECISION": "keyword2",
	"@@NESTLEVEL": "keyword2",
	"@@OPTIONS": "keyword2",
	"@@PACKET_ERRORS": "keyword2",
	"@@PACK_RECEIVED": "keyword2",
	"@@PACK_SENT": "keyword2",
	"@@PROCID": "keyword2",
	"@@REMSERVER": "keyword2",
	"@@ROWCOUNT": "keyword2",
	"@@SERVERNAME": "keyword2",
	"@@SERVICENAME": "keyword2",
	"@@SPID": "keyword2",
	"@@TEXTSIZE": "keyword2",
	"@@TIMETICKS": "keyword2",
	"@@TOTAL_ERRORS": "keyword2",
	"@@TOTAL_READ": "keyword2",
	"@@TOTAL_WRITE": "keyword2",
	"@@TRANCOUNT": "keyword2",
	"@@VERSION": "keyword2",
	"ABS": "keyword2",
	"ABSOLUTE": "keyword1",
	"ACOS": "keyword2",
	"ADD": "keyword1",
	"ALL": "keyword1",
	"ALTER": "keyword1",
	"AND": "keyword1",
	"ANSI_NULLS": "keyword1",
	"ANY": "keyword1",
	"APP_NAME": "keyword2",
	"AS": "keyword1",
	"ASC": "keyword1",
	"ASCII": "keyword2",
	"ASIN": "keyword2",
	"ATAN": "keyword2",
	"ATN2": "keyword2",
	"AUTHORIZATION": "keyword1",
	"AVG": "keyword2",
	"BACKUP": "keyword1",
	"BEGIN": "keyword1",
	"BETWEEN": "keyword1",
	"BINARY_CHECKSUM": "keyword2",
	"BREAK": "keyword1",
	"BROWSE": "keyword1",
	"BULK": "keyword1",
	"BY": "keyword1",
	"CASCADE": "keyword1",
	"CASE": "keyword2",
	"CAST": "keyword2",
	"CEILING": "keyword2",
	"CHARINDEX": "keyword2",
	"CHECK": "keyword1",
	"CHECKPOINT": "keyword1",
	"CHECKSUM": "keyword2",
	"CHECKSUM_AGG": "keyword2",
	"CLOSE": "keyword1",
	"CLUSTERED": "keyword1",
	"COALESCE": "keyword2",
	"COLLATIONPROPERTY": "keyword2",
	"COLUMN": "keyword1",
	"COLUMNPROPERTY": "keyword2",
	"COL_LENGTH": "keyword2",
	"COL_NAME": "keyword2",
	"COMMIT": "keyword1",
	"COMMITTED": "keyword1",
	"COMPUTE": "keyword1",
	"CONFIRM": "keyword1",
	"CONSTRAINT": "keyword1",
	"CONTAINS": "keyword1",
	"CONTAINSTABLE": "keyword1",
	"CONTINUE": "keyword1",
	"CONTROLROW": "keyword1",
	"CONVERT": "keyword2",
	"COS": "keyword2",
	"COT": "keyword2",
	"COUNT": "keyword2",
	"COUNT_BIG": "keyword2",
	"CREATE": "keyword1",
	"CROSS": "keyword1",
	"CURRENT": "keyword1",
	"CURRENT_DATE": "keyword2",
	"CURRENT_TIME": "keyword2",
	"CURRENT_TIMESTAMP": "keyword2",
	"CURRENT_USER": "keyword2",
	"CURSOR": "keyword1",
	"CURSOR_STATUS": "keyword2",
	"DATABASE": "keyword1",
	"DATABASEPROPERTY": "keyword2",
	"DATALENGTH": "keyword2",
	"DATEADD": "keyword2",
	"DATEDIFF": "keyword2",
	"DATENAME": "keyword2",
	"DATEPART": "keyword2",
	"DAY": "keyword2",
	"DBCC": "keyword1",
	"DB_ID": "keyword2",
	"DB_NAME": "keyword2",
	"DEALLOCATE": "keyword1",
	"DECLARE": "keyword1",
	"DEFAULT": "keyword1",
	"DEGREES": "keyword2",
	"DELETE": "keyword1",
	"DENY": "keyword1",
	"DESC": "keyword1",
	"DIFFERENCE": "keyword2",
	"DISK": "keyword1",
	"DISTINCT": "keyword1",
	"DISTRIBUTED": "keyword1",
	"DOUBLE": "keyword1",
	"DROP": "keyword1",
	"DUMMY": "keyword1",
	"DUMP": "keyword1",
	"DYNAMIC": "keyword1",
	"ELSE": "keyword1",
	"END": "keyword1",
	"ERRLVL": "keyword1",
	"ERROREXIT": "keyword1",
	"ESCAPE": "keyword1",
	"EXCEPT": "keyword1",
	"EXEC": "keyword1",
	"EXECUTE": "keyword1",
	"EXISTS": "keyword1",
	"EXIT": "keyword1",
	"EXP": "keyword2",
	"FAST_FORWARD": "keyword1",
	"FETCH": "keyword1",
	"FILE": "keyword1",
	"FILEGROUPPROPERTY": "keyword2",
	"FILEGROUP_ID": "keyword2",
	"FILEGROUP_NAME": "keyword2",
	"FILEPROPERTY": "keyword2",
	"FILE_ID": "keyword2",
	"FILE_NAME": "keyword2",
	"FILLFACTOR": "keyword1",
	"FIRST": "keyword1",
	"FLOOR": "keyword2",
	"FLOPPY": "keyword1",
	"FOR": "keyword1",
	"FOREIGN": "keyword1",
	"FORMATMESSAGE": "keyword2",
	"FORWARD_ONLY": "keyword1",
	"FREETEXT": "keyword1",
	"FREETEXTTABLE": "keyword1",
	"FROM": "keyword1",
	"FULL": "keyword1",
	"FULLTEXTCATALOGPROPERTY": "keyword2",
	"FULLTEXTSERVICEPROPERTY": "keyword2",
	"FUNCTION": "keyword1",
	"GETANSINULL": "keyword2",
	"GETDATE": "keyword2",
	"GETUTCDATE": "keyword2",
	"GLOBAL": "keyword1",
	"GOTO": "keyword1",
	"GRANT": "keyword1",
	"GROUP": "keyword1",
	"GROUPING": "keyword2",
	"HAVING": "keyword1",
	"HOLDLOCK": "keyword1",
	"HOST_ID": "keyword2",
	"HOST_NAME": "keyword2",
	"ID": "keyword1",
	"IDENTITY": "keyword2",
	"IDENTITYCOL": "keyword1",
	"IDENTITY_INSERT": "keyword2",
	"IDENT_CURRENT": "keyword2",
	"IDENT_INCR": "keyword2",
	"IDENT_SEED": "keyword2",
	"IF": "keyword1",
	"IN": "keyword1",
	"INDEX": "keyword1",
	"INDEXPROPERTY": "keyword2",
	"INDEX_COL": "keyword2",
	"INNER": "keyword1",
	"INSENSITIVE": "keyword1",
	"INSERT": "keyword1",
	"INTERSECT": "keyword1",
	"INTO": "keyword1",
	"IS": "keyword1",
	"ISDATE": "keyword2",
	"ISNULL": "keyword2",
	"ISNUMERIC": "keyword2",
	"ISOLATION": "keyword1",
	"IS_MEMBER": "keyword2",
	"IS_SRVROLEMEMBER": "keyword2",
	"JOIN": "keyword1",
	"KEY": "keyword1",
	"KEYSET": "keyword1",
	"KILL": "keyword1",
	"LAST": "keyword1",
	"LEFT": "keyword2",
	"LEN": "keyword2",
	"LEVEL": "keyword1",
	"LIKE": "keyword1",
	"LINENO": "keyword1",
	"LOAD": "keyword1",
	"LOCAL": "keyword1",
	"LOG": "keyword2",
	"LOG10": "keyword2",
	"LOWER": "keyword2",
	"LTRIM": "keyword2",
	"MAX": "keyword1",
	"MIN": "keyword1",
	"MIRROREXIT": "keyword1",
	"MONTH": "keyword2",
	"MSagent_parameters": "keyword3",
	"MSagent_profiles": "keyword3",
	"MSarticles": "keyword3",
	"MSdistpublishers": "keyword3",
	"MSdistribution_agents": "keyword3",
	"MSdistribution_history": "keyword3",
	"MSdistributiondbs": "keyword3",
	"MSdistributor": "keyword3",
	"MSlogreader_agents": "keyword3",
	"MSlogreader_history": "keyword3",
	"MSmerge_agents": "keyword3",
	"MSmerge_contents": "keyword3",
	"MSmerge_delete_conflicts": "keyword3",
	"MSmerge_genhistory": "keyword3",
	"MSmerge_history": "keyword3",
	"MSmerge_replinfo": "keyword3",
	"MSmerge_subscriptions": "keyword3",
	"MSmerge_tombstone": "keyword3",
	"MSpublication_access": "keyword3",
	"MSrepl_commands": "keyword3",
	"MSrepl_errors": "keyword3",
	"MSrepl_transactions": "keyword3",
	"MSrepl_version": "keyword3",
	"MSreplication_objects": "keyword3",
	"MSreplication_subscriptions": "keyword3",
	"MSsnapshot_agents": "keyword3",
	"MSsnapshot_history": "keyword3",
	"MSsubscriber_info": "keyword3",
	"MSsubscriber_schedule": "keyword3",
	"MSsubscription_properties": "keyword3",
	"MSsubscriptions": "keyword3",
	"Mspublications": "keyword3",
	"Mspublisher_databases": "keyword3",
	"Msrepl_originators": "keyword3",
	"NATIONAL": "keyword1",
	"NEWID": "keyword2",
	"NEXT": "keyword1",
	"NOCHECK": "keyword1",
	"NONCLUSTERED": "keyword1",
	"NOT": "keyword1",
	"NULL": "keyword1",
	"NULLIF": "keyword2",
	"OBJECTPROPERTY": "keyword2",
	"OBJECT_ID": "keyword2",
	"OBJECT_NAME": "keyword2",
	"OF": "keyword1",
	"OFF": "keyword1",
	"OFFSETS": "keyword1",
	"ON": "keyword1",
	"ONCE": "keyword1",
	"ONLY": "keyword1",
	"OPEN": "keyword1",
	"OPENDATASOURCE": "keyword1",
	"OPENQUERY": "keyword1",
	"OPENROWSET": "keyword1",
	"OPTIMISTIC": "keyword1",
	"OPTION": "keyword1",
	"OR": "keyword1",
	"ORDER": "keyword1",
	"OUTER": "keyword1",
	"OUTPUT": "keyword1",
	"OVER": "keyword1",
	"PARSENAME": "keyword2",
	"PATINDEX": "keyword2",
	"PERCENT": "keyword1",
	"PERM": "keyword1",
	"PERMANENT": "keyword1",
	"PERMISSIONS": "keyword2",
	"PI": "keyword2",
	"PIPE": "keyword1",
	"PLAN": "keyword1",
	"POWER": "keyword2",
	"PRECISION": "keyword1",
	"PREPARE": "keyword1",
	"PRIMARY": "keyword1",
	"PRINT": "keyword1",
	"PRIOR": "keyword1",
	"PRIVILEGES": "keyword1",
	"PROC": "keyword1",
	"PROCEDURE": "keyword1",
	"PROCESSEXIT": "keyword1",
	"PUBLIC": "keyword1",
	"QUOTED_IDENTIFIER": "keyword1",
	"QUOTENAME": "keyword2",
	"RADIANS": "keyword2",
	"RAISERROR": "keyword1",
	"RAND": "keyword2",
	"READ": "keyword1",
	"READTEXT": "keyword1",
	"READ_ONLY": "keyword1",
	"RECONFIGURE": "keyword1",
	"REFERENCES": "keyword1",
	"RELATIVE": "keyword1",
	"REPEATABLE": "keyword1",
	"REPLACE": "keyword2",
	"REPLICATE": "keyword2",
	"REPLICATION": "keyword1",
	"RESTORE": "keyword1",
	"RESTRICT": "keyword1",
	"RETURN": "keyword1",
	"RETURNS": "keyword1",
	"REVERSE": "keyword2",
	"REVOKE": "keyword1",
	"RIGHT": "keyword2",
	"ROLLBACK": "keyword1",
	"ROUND": "keyword2",
	"ROWCOUNT_BIG": "keyword2",
	"ROWGUIDCOL": "keyword1",
	"RTRIM": "keyword2",
	"RULE": "keyword1",
	"SAVE": "keyword1",
	"SCHEMA": "keyword1",
	"SCOPE_IDENTITY": "keyword2",
	"SCROLL": "keyword1",
	"SCROLL_LOCKS": "keyword1",
	"SELECT": "keyword1",
	"SERIALIZABLE": "keyword1",
	"SERVERPROPERTY": "keyword2",
	"SESSIONPROPERTY": "keyword2",
	"SESSION_USER": "keyword2",
	"SET": "keyword1",
	"SETUSER": "keyword1",
	"SHUTDOWN": "keyword1",
	"SIGN": "keyword2",
	"SIN": "keyword2",
	"SOME": "keyword1",
	"SOUNDEX": "keyword2",
	"SPACE": "keyword2",
	"SQRT": "keyword2",
	"SQUARE": "keyword2",
	"STATIC": "keyword1",
	"STATISTICS": "keyword1",
	"STATS_DATE": "keyword2",
	"STDEV": "keyword2",
	"STDEVP": "keyword2",
	"STR": "keyword2",
	"STUFF": "keyword2",
	"SUBSTRING": "keyword2",
	"SUM": "keyword2",
	"SUSER_ID": "keyword2",
	"SUSER_NAME": "keyword2",
	"SUSER_SID": "keyword2",
	"SUSER_SNAME": "keyword2",
	"SYSTEM_USER": "keyword2",
	"TABLE": "keyword1",
	"TAN": "keyword2",
	"TAPE": "keyword1",
	"TEMP": "keyword1",
	"TEMPORARY": "keyword1",
	"TEXTIMAGE_ON": "keyword1",
	"TEXTPTR": "keyword2",
	"TEXTVALID": "keyword2",
	"THEN": "keyword1",
	"TO": "keyword1",
	"TOP": "keyword1",
	"TRAN": "keyword1",
	"TRANSACTION": "keyword1",
	"TRIGGER": "keyword1",
	"TRUNCATE": "keyword1",
	"TSEQUAL": "keyword1",
	"TYPEPROPERTY": "keyword2",
	"UNCOMMITTED": "keyword1",
	"UNICODE": "keyword2",
	"UNION": "keyword1",
	"UNIQUE": "keyword1",
	"UPDATE": "keyword1",
	"UPDATETEXT": "keyword1",
	"UPPER": "keyword2",
	"USE": "keyword1",
	"USER": "keyword2",
	"USER_ID": "keyword2",
	"USER_NAME": "keyword2",
	"VALUES": "keyword1",
	"VAR": "keyword2",
	"VARP": "keyword2",
	"VARYING": "keyword1",
	"VIEW": "keyword1",
	"WAITFOR": "keyword1",
	"WHEN": "keyword1",
	"WHERE": "keyword1",
	"WHILE": "keyword1",
	"WITH": "keyword1",
	"WORK": "keyword1",
	"WRITETEXT": "keyword1",
	"YEAR": "keyword2",
	"backupfile": "keyword3",
	"backupmediafamily": "keyword3",
	"backupmediaset": "keyword3",
	"backupset": "keyword3",
	"binary": "keyword1",
	"bit": "keyword1",
	"char": "keyword1",
	"character": "keyword1",
	"datetime": "keyword1",
	"decimal": "keyword1",
	"float": "keyword1",
	"fn_helpcollations": "keyword3",
	"fn_servershareddrives": "keyword3",
	"fn_virtualfilestats": "keyword3",
	"image": "keyword1",
	"int": "keyword1",
	"integer": "keyword1",
	"money": "keyword1",
	"name": "keyword1",
	"nchar": "keyword1",
	"ntext": "keyword1",
	"numeric": "keyword1",
	"nvarchar": "keyword1",
	"real": "keyword1",
	"restorefile": "keyword3",
	"restorefilegroup": "keyword3",
	"restorehistory": "keyword3",
	"smalldatetime": "keyword1",
	"smallint": "keyword1",
	"smallmoney": "keyword1",
	"sp_OACreate": "keyword3",
	"sp_OADestroy": "keyword3",
	"sp_OAGetErrorInfo": "keyword3",
	"sp_OAGetProperty": "keyword3",
	"sp_OAMethod": "keyword3",
	"sp_OASetProperty": "keyword3",
	"sp_OAStop": "keyword3",
	"sp_add_agent_parameter": "keyword3",
	"sp_add_agent_profile": "keyword3",
	"sp_add_alert": "keyword3",
	"sp_add_category": "keyword3",
	"sp_add_data_file_recover_suspect_db": "keyword3",
	"sp_add_job": "keyword3",
	"sp_add_jobschedule": "keyword3",
	"sp_add_jobserver": "keyword3",
	"sp_add_jobstep": "keyword3",
	"sp_add_log_file_recover_suspect_db": "keyword3",
	"sp_add_notification": "keyword3",
	"sp_add_operator": "keyword3",
	"sp_add_targetservergroup": "keyword3",
	"sp_add_targetsvrgrp_member": "keyword3",
	"sp_addalias": "keyword3",
	"sp_addapprole": "keyword3",
	"sp_addarticle": "keyword3",
	"sp_adddistpublisher": "keyword3",
	"sp_adddistributiondb": "keyword3",
	"sp_adddistributor": "keyword3",
	"sp_addextendedproc": "keyword3",
	"sp_addgroup": "keyword3",
	"sp_addlinkedserver": "keyword3",
	"sp_addlinkedsrvlogin": "keyword3",
	"sp_addlogin": "keyword3",
	"sp_addmergearticle": "keyword3",
	"sp_addmergefilter": "keyword3",
	"sp_addmergepublication": "keyword3",
	"sp_addmergepullsubscription": "keyword3",
	"sp_addmergepullsubscription_agent": "keyword3",
	"sp_addmergesubscription": "keyword3",
	"sp_addmessage": "keyword3",
	"sp_addpublication": "keyword3",
	"sp_addpublication_snapshot": "keyword3",
	"sp_addpublisher70": "keyword3",
	"sp_addpullsubscription": "keyword3",
	"sp_addpullsubscription_agent": "keyword3",
	"sp_addremotelogin": "keyword3",
	"sp_addrole": "keyword3",
	"sp_addrolemember": "keyword3",
	"sp_addserver": "keyword3",
	"sp_addsrvrolemember": "keyword3",
	"sp_addsubscriber": "keyword3",
	"sp_addsubscriber_schedule": "keyword3",
	"sp_addsubscription": "keyword3",
	"sp_addsynctriggers": "keyword3",
	"sp_addtabletocontents": "keyword3",
	"sp_addtask": "keyword3",
	"sp_addtype": "keyword3",
	"sp_addumpdevice": "keyword3",
	"sp_adduser": "keyword3",
	"sp_altermessage": "keyword3",
	"sp_apply_job_to_targets": "keyword3",
	"sp_approlepassword": "keyword3",
	"sp_article_validation": "keyword3",
	"sp_articlecolumn": "keyword3",
	"sp_articlefilter": "keyword3",
	"sp_articlesynctranprocs": "keyword3",
	"sp_articleview": "keyword3",
	"sp_attach_db": "keyword3",
	"sp_attach_single_file_db": "keyword3",
	"sp_autostats": "keyword3",
	"sp_bindefault": "keyword3",
	"sp_bindrule": "keyword3",
	"sp_bindsession": "keyword3",
	"sp_browsereplcmds": "keyword3",
	"sp_catalogs": "keyword3",
	"sp_certify_removable": "keyword3",
	"sp_change_agent_parameter": "keyword3",
	"sp_change_agent_profile": "keyword3",
	"sp_change_subscription_properties": "keyword3",
	"sp_change_users_login": "keyword3",
	"sp_changearticle": "keyword3",
	"sp_changedbowner": "keyword3",
	"sp_changedistpublisher": "keyword3",
	"sp_changedistributiondb": "keyword3",
	"sp_changedistributor_password": "keyword3",
	"sp_changedistributor_property": "keyword3",
	"sp_changegroup": "keyword3",
	"sp_changemergearticle": "keyword3",
	"sp_changemergefilter": "keyword3",
	"sp_changemergepublication": "keyword3",
	"sp_changemergepullsubscription": "keyword3",
	"sp_changemergesubscription": "keyword3",
	"sp_changeobjectowner": "keyword3",
	"sp_changepublication": "keyword3",
	"sp_changesubscriber": "keyword3",
	"sp_changesubscriber_schedule": "keyword3",
	"sp_changesubstatus": "keyword3",
	"sp_check_for_sync_trigger": "keyword3",
	"sp_column_privileges": "keyword3",
	"sp_column_privileges_ex": "keyword3",
	"sp_columns": "keyword3",
	"sp_columns_ex": "keyword3",
	"sp_configure": "keyword3",
	"sp_create_removable": "keyword3",
	"sp_createorphan": "keyword3",
	"sp_createstats": "keyword3",
	"sp_cursor": "keyword3",
	"sp_cursor_list": "keyword3",
	"sp_cursorclose": "keyword3",
	"sp_cursorexecute": "keyword3",
	"sp_cursorfetch": "keyword3",
	"sp_cursoropen": "keyword3",
	"sp_cursoroption": "keyword3",
	"sp_cursorprepare": "keyword3",
	"sp_cursorunprepare": "keyword3",
	"sp_cycle_errorlog": "keyword3",
	"sp_databases": "keyword3",
	"sp_datatype_info": "keyword3",
	"sp_dbcmptlevel": "keyword3",
	"sp_dbfixedrolepermission": "keyword3",
	"sp_dboption": "keyword3",
	"sp_defaultdb": "keyword3",
	"sp_defaultlanguage": "keyword3",
	"sp_delete_alert": "keyword3",
	"sp_delete_backuphistory": "keyword3",
	"sp_delete_category": "keyword3",
	"sp_delete_job": "keyword3",
	"sp_delete_jobschedule": "keyword3",
	"sp_delete_jobserver": "keyword3",
	"sp_delete_jobstep": "keyword3",
	"sp_delete_notification": "keyword3",
	"sp_delete_operator": "keyword3",
	"sp_delete_targetserver": "keyword3",
	"sp_delete_targetservergroup": "keyword3",
	"sp_delete_targetsvrgrp_member": "keyword3",
	"sp_deletemergeconflictrow": "keyword3",
	"sp_denylogin": "keyword3",
	"sp_depends": "keyword3",
	"sp_describe_cursor": "keyword3",
	"sp_describe_cursor_columns": "keyword3",
	"sp_describe_cursor_tables": "keyword3",
	"sp_detach_db": "keyword3",
	"sp_drop_agent_parameter": "keyword3",
	"sp_drop_agent_profile": "keyword3",
	"sp_dropalias": "keyword3",
	"sp_dropapprole": "keyword3",
	"sp_droparticle": "keyword3",
	"sp_dropdevice": "keyword3",
	"sp_dropdistpublisher": "keyword3",
	"sp_dropdistributiondb": "keyword3",
	"sp_dropdistributor": "keyword3",
	"sp_dropextendedproc": "keyword3",
	"sp_dropgroup": "keyword3",
	"sp_droplinkedsrvlogin": "keyword3",
	"sp_droplogin": "keyword3",
	"sp_dropmergearticle": "keyword3",
	"sp_dropmergefilter": "keyword3",
	"sp_dropmergepublication": "keyword3",
	"sp_dropmergepullsubscription": "keyword3",
	"sp_dropmergesubscription": "keyword3",
	"sp_dropmessage": "keyword3",
	"sp_droporphans": "keyword3",
	"sp_droppublication": "keyword3",
	"sp_droppullsubscription": "keyword3",
	"sp_dropremotelogin": "keyword3",
	"sp_droprole": "keyword3",
	"sp_droprolemember": "keyword3",
	"sp_dropserver": "keyword3",
	"sp_dropsrvrolemember": "keyword3",
	"sp_dropsubscriber": "keyword3",
	"sp_dropsubscription": "keyword3",
	"sp_droptask": "keyword3",
	"sp_droptype": "keyword3",
	"sp_dropuser": "keyword3",
	"sp_dropwebtask": "keyword3",
	"sp_dsninfo": "keyword3",
	"sp_dumpparamcmd": "keyword3",
	"sp_enumcodepages": "keyword3",
	"sp_enumcustomresolvers": "keyword3",
	"sp_enumdsn": "keyword3",
	"sp_enumfullsubscribers": "keyword3",
	"sp_execute": "keyword3",
	"sp_executesql": "keyword3",
	"sp_expired_subscription_cleanup": "keyword3",
	"sp_fkeys": "keyword3",
	"sp_foreignkeys": "keyword3",
	"sp_fulltext_catalog": "keyword3",
	"sp_fulltext_column": "keyword3",
	"sp_fulltext_database": "keyword3",
	"sp_fulltext_service": "keyword3",
	"sp_fulltext_table": "keyword3",
	"sp_generatefilters": "keyword3",
	"sp_get_distributor": "keyword3",
	"sp_getbindtoken": "keyword3",
	"sp_getmergedeletetype": "keyword3",
	"sp_grant_publication_access": "keyword3",
	"sp_grantdbaccess": "keyword3",
	"sp_grantlogin": "keyword3",
	"sp_help": "keyword3",
	"sp_help_agent_default": "keyword3",
	"sp_help_agent_parameter": "keyword3",
	"sp_help_agent_profile": "keyword3",
	"sp_help_alert": "keyword3",
	"sp_help_category": "keyword3",
	"sp_help_downloadlist": "keyword3",
	"sp_help_fulltext_catalogs": "keyword3",
	"sp_help_fulltext_catalogs_cursor": "keyword3",
	"sp_help_fulltext_columns": "keyword3",
	"sp_help_fulltext_columns_cursor": "keyword3",
	"sp_help_fulltext_tables": "keyword3",
	"sp_help_fulltext_tables_cursor": "keyword3",
	"sp_help_job": "keyword3",
	"sp_help_jobhistory": "keyword3",
	"sp_help_jobschedule": "keyword3",
	"sp_help_jobserver": "keyword3",
	"sp_help_jobstep": "keyword3",
	"sp_help_notification": "keyword3",
	"sp_help_operator": "keyword3",
	"sp_help_publication_access": "keyword3",
	"sp_help_targetserver": "keyword3",
	"sp_help_targetservergroup": "keyword3",
	"sp_helparticle": "keyword3",
	"sp_helparticlecolumns": "keyword3",
	"sp_helpconstraint": "keyword3",
	"sp_helpdb": "keyword3",
	"sp_helpdbfixedrole": "keyword3",
	"sp_helpdevice": "keyword3",
	"sp_helpdistpublisher": "keyword3",
	"sp_helpdistributiondb": "keyword3",
	"sp_helpdistributor": "keyword3",
	"sp_helpextendedproc": "keyword3",
	"sp_helpfile": "keyword3",
	"sp_helpfilegroup": "keyword3",
	"sp_helpgroup": "keyword3",
	"sp_helphistory": "keyword3",
	"sp_helpindex": "keyword3",
	"sp_helplanguage": "keyword3",
	"sp_helplinkedsrvlogin": "keyword3",
	"sp_helplogins": "keyword3",
	"sp_helpmergearticle": "keyword3",
	"sp_helpmergearticleconflicts": "keyword3",
	"sp_helpmergeconflictrows": "keyword3",
	"sp_helpmergedeleteconflictrows": "keyword3",
	"sp_helpmergefilter": "keyword3",
	"sp_helpmergepublication": "keyword3",
	"sp_helpmergepullsubscription": "keyword3",
	"sp_helpmergesubscription": "keyword3",
	"sp_helpntgroup": "keyword3",
	"sp_helppublication": "keyword3",
	"sp_helppullsubscription": "keyword3",
	"sp_helpremotelogin": "keyword3",
	"sp_helpreplicationdboption": "keyword3",
	"sp_helprole": "keyword3",
	"sp_helprolemember": "keyword3",
	"sp_helprotect": "keyword3",
	"sp_helpserver": "keyword3",
	"sp_helpsort": "keyword3",
	"sp_helpsrvrole": "keyword3",
	"sp_helpsrvrolemember": "keyword3",
	"sp_helpsubscriberinfo": "keyword3",
	"sp_helpsubscription": "keyword3",
	"sp_helpsubscription_properties": "keyword3",
	"sp_helptask": "keyword3",
	"sp_helptext": "keyword3",
	"sp_helptrigger": "keyword3",
	"sp_helpuser": "keyword3",
	"sp_indexes": "keyword3",
	"sp_indexoption": "keyword3",
	"sp_link_publication": "keyword3",
	"sp_linkedservers": "keyword3",
	"sp_lock": "keyword3",
	"sp_makewebtask": "keyword3",
	"sp_manage_jobs_by_login": "keyword3",
	"sp_mergedummyupdate": "keyword3",
	"sp_mergesubscription_cleanup": "keyword3",
	"sp_monitor": "keyword3",
	"sp_msx_defect": "keyword3",
	"sp_msx_enlist": "keyword3",
	"sp_password": "keyword3",
	"sp_pkeys": "keyword3",
	"sp_post_msx_operation": "keyword3",
	"sp_prepare": "keyword3",
	"sp_primarykeys": "keyword3",
	"sp_processmail": "keyword3",
	"sp_procoption": "keyword3",
	"sp_publication_validation": "keyword3",
	"sp_purge_jobhistory": "keyword3",
	"sp_purgehistory": "keyword3",
	"sp_reassigntask": "keyword3",
	"sp_recompile": "keyword3",
	"sp_refreshsubscriptions": "keyword3",
	"sp_refreshview": "keyword3",
	"sp_reinitmergepullsubscription": "keyword3",
	"sp_reinitmergesubscription": "keyword3",
	"sp_reinitpullsubscription": "keyword3",
	"sp_reinitsubscription": "keyword3",
	"sp_remoteoption": "keyword3",
	"sp_remove_job_from_targets": "keyword3",
	"sp_removedbreplication": "keyword3",
	"sp_rename": "keyword3",
	"sp_renamedb": "keyword3",
	"sp_replcmds": "keyword3",
	"sp_replcounters": "keyword3",
	"sp_repldone": "keyword3",
	"sp_replflush": "keyword3",
	"sp_replication_agent_checkup": "keyword3",
	"sp_replicationdboption": "keyword3",
	"sp_replsetoriginator": "keyword3",
	"sp_replshowcmds": "keyword3",
	"sp_repltrans": "keyword3",
	"sp_reset_connection": "keyword3",
	"sp_resync_targetserver": "keyword3",
	"sp_revoke_publication_access": "keyword3",
	"sp_revokedbaccess": "keyword3",
	"sp_revokelogin": "keyword3",
	"sp_runwebtask": "keyword3",
	"sp_script_synctran_commands": "keyword3",
	"sp_scriptdelproc": "keyword3",
	"sp_scriptinsproc": "keyword3",
	"sp_scriptmappedupdproc": "keyword3",
	"sp_scriptupdproc": "keyword3",
	"sp_sdidebug": "keyword3",
	"sp_server_info": "keyword3",
	"sp_serveroption": "keyword3",
	"sp_setapprole": "keyword3",
	"sp_setnetname": "keyword3",
	"sp_spaceused": "keyword3",
	"sp_special_columns": "keyword3",
	"sp_sproc_columns": "keyword3",
	"sp_srvrolepermission": "keyword3",
	"sp_start_job": "keyword3",
	"sp_statistics": "keyword3",
	"sp_stop_job": "keyword3",
	"sp_stored_procedures": "keyword3",
	"sp_subscription_cleanup": "keyword3",
	"sp_table_privileges": "keyword3",
	"sp_table_privileges_ex": "keyword3",
	"sp_table_validation": "keyword3",
	"sp_tableoption": "keyword3",
	"sp_tables": "keyword3",
	"sp_tables_ex": "keyword3",
	"sp_unbindefault": "keyword3",
	"sp_unbindrule": "keyword3",
	"sp_unprepare": "keyword3",
	"sp_update_agent_profile": "keyword3",
	"sp_update_alert": "keyword3",
	"sp_update_category": "keyword3",
	"sp_update_job": "keyword3",
	"sp_update_jobschedule": "keyword3",
	"sp_update_jobstep": "keyword3",
	"sp_update_notification": "keyword3",
	"sp_update_operator": "keyword3",
	"sp_update_targetservergroup": "keyword3",
	"sp_updatestats": "keyword3",
	"sp_updatetask": "keyword3",
	"sp_validatelogins": "keyword3",
	"sp_validname": "keyword3",
	"sp_who": "keyword3",
	"sysalerts": "keyword3",
	"sysallocations": "keyword3",
	"sysaltfiles": "keyword3",
	"sysarticles": "keyword3",
	"sysarticleupdates": "keyword3",
	"syscacheobjects": "keyword3",
	"syscategories": "keyword3",
	"syscharsets": "keyword3",
	"syscolumns": "keyword3",
	"syscomments": "keyword3",
	"sysconfigures": "keyword3",
	"sysconstraints": "keyword3",
	"syscurconfigs": "keyword3",
	"sysdatabases": "keyword3",
	"sysdepends": "keyword3",
	"sysdevices": "keyword3",
	"sysdownloadlist": "keyword3",
	"sysfilegroups": "keyword3",
	"sysfiles": "keyword3",
	"sysforeignkeys": "keyword3",
	"sysfulltextcatalogs": "keyword3",
	"sysindexes": "keyword3",
	"sysindexkeys": "keyword3",
	"sysjobhistory": "keyword3",
	"sysjobs": "keyword3",
	"sysjobschedules": "keyword3",
	"sysjobservers": "keyword3",
	"sysjobsteps": "keyword3",
	"syslanguages": "keyword3",
	"syslockinfo": "keyword3",
	"syslogins": "keyword3",
	"sysmembers": "keyword3",
	"sysmergearticles": "keyword3",
	"sysmergepublications": "keyword3",
	"sysmergeschemachange": "keyword3",
	"sysmergesubscriptions": "keyword3",
	"sysmergesubsetfilters": "keyword3",
	"sysmessages": "keyword3",
	"sysnotifications": "keyword3",
	"sysobjects": "keyword3",
	"sysoledbusers": "keyword3",
	"sysoperators": "keyword3",
	"sysperfinfo": "keyword3",
	"syspermissions": "keyword3",
	"sysprocesses": "keyword3",
	"sysprotects": "keyword3",
	"syspublications": "keyword3",
	"sysreferences": "keyword3",
	"sysremotelogins": "keyword3",
	"sysreplicationalerts": "keyword3",
	"sysservers": "keyword3",
	"syssubscriptions": "keyword3",
	"systargetservergroupmembers": "keyword3",
	"systargetservergroups": "keyword3",
	"systargetservers": "keyword3",
	"systaskids": "keyword3",
	"systypes": "keyword3",
	"sysusers": "keyword3",
	"text": "keyword1",
	"timestamp": "keyword1",
	"tinyint": "keyword1",
	"uniqueidentifier": "keyword1",
	"varbinary": "keyword1",
	"varchar": "keyword1",
	"xp_cmdshell": "keyword3",
	"xp_deletemail": "keyword3",
	"xp_enumgroups": "keyword3",
	"xp_findnextmsg": "keyword3",
	"xp_grantlogin": "keyword3",
	"xp_logevent": "keyword3",
	"xp_loginconfig": "keyword3",
	"xp_logininfo": "keyword3",
	"xp_msver": "keyword3",
	"xp_readmail": "keyword3",
	"xp_revokelogin": "keyword3",
	"xp_sendmail": "keyword3",
	"xp_sprintf": "keyword3",
	"xp_sqlinventory": "keyword3",
	"xp_sqlmaint": "keyword3",
	"xp_sqltrace": "keyword3",
	"xp_sscanf": "keyword3",
	"xp_startmail": "keyword3",
	"xp_stopmail": "keyword3",
	"xp_trace_addnewqueue": "keyword3",
	"xp_trace_deletequeuedefinition": "keyword3",
	"xp_trace_destroyqueue": "keyword3",
	"xp_trace_enumqueuedefname": "keyword3",
	"xp_trace_enumqueuehandles": "keyword3",
	"xp_trace_eventclassrequired": "keyword3",
	"xp_trace_flushqueryhistory": "keyword3",
	"xp_trace_generate_event": "keyword3",
	"xp_trace_getappfilter": "keyword3",
	"xp_trace_getconnectionidfilter": "keyword3",
	"xp_trace_getcpufilter": "keyword3",
	"xp_trace_getdbidfilter": "keyword3",
	"xp_trace_getdurationfilter": "keyword3",
	"xp_trace_geteventfilter": "keyword3",
	"xp_trace_geteventnames": "keyword3",
	"xp_trace_getevents": "keyword3",
	"xp_trace_gethostfilter": "keyword3",
	"xp_trace_gethpidfilter": "keyword3",
	"xp_trace_getindidfilter": "keyword3",
	"xp_trace_getntdmfilter": "keyword3",
	"xp_trace_getntnmfilter": "keyword3",
	"xp_trace_getobjidfilter": "keyword3",
	"xp_trace_getqueueautostart": "keyword3",
	"xp_trace_getqueuedestination": "keyword3",
	"xp_trace_getqueueproperties": "keyword3",
	"xp_trace_getreadfilter": "keyword3",
	"xp_trace_getserverfilter": "keyword3",
	"xp_trace_getseverityfilter": "keyword3",
	"xp_trace_getspidfilter": "keyword3",
	"xp_trace_getsysobjectsfilter": "keyword3",
	"xp_trace_gettextfilter": "keyword3",
	"xp_trace_getuserfilter": "keyword3",
	"xp_trace_getwritefilter": "keyword3",
	"xp_trace_loadqueuedefinition": "keyword3",
	"xp_trace_pausequeue": "keyword3",
	"xp_trace_restartqueue": "keyword3",
	"xp_trace_savequeuedefinition": "keyword3",
	"xp_trace_setappfilter": "keyword3",
	"xp_trace_setconnectionidfilter": "keyword3",
	"xp_trace_setcpufilter": "keyword3",
	"xp_trace_setdbidfilter": "keyword3",
	"xp_trace_setdurationfilter": "keyword3",
	"xp_trace_seteventclassrequired": "keyword3",
	"xp_trace_seteventfilter": "keyword3",
	"xp_trace_sethostfilter": "keyword3",
	"xp_trace_sethpidfilter": "keyword3",
	"xp_trace_setindidfilter": "keyword3",
	"xp_trace_setntdmfilter": "keyword3",
	"xp_trace_setntnmfilter": "keyword3",
	"xp_trace_setobjidfilter": "keyword3",
	"xp_trace_setqueryhistory": "keyword3",
	"xp_trace_setqueueautostart": "keyword3",
	"xp_trace_setqueuecreateinfo": "keyword3",
	"xp_trace_setqueuedestination": "keyword3",
	"xp_trace_setreadfilter": "keyword3",
	"xp_trace_setserverfilter": "keyword3",
	"xp_trace_setseverityfilter": "keyword3",
	"xp_trace_setspidfilter": "keyword3",
	"xp_trace_setsysobjectsfilter": "keyword3",
	"xp_trace_settextfilter": "keyword3",
	"xp_trace_setuserfilter": "keyword3",
	"xp_trace_setwritefilter": "keyword3",
}

# Dictionary of keywords dictionaries for tsql mode.
keywordsDictDict = {
	"tsql_main": tsql_main_keywords_dict,
}

# Rules for tsql_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="[", end="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule4(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def rule5(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="--",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

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
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="::",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rule22(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule23(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="literal2", pattern="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def rule24(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"!": [rule18,rule19,rule20,],
	"\"": [rule1,],
	"%": [rule13,],
	"&": [rule14,],
	"'": [rule2,],
	"(": [rule4,],
	"*": [rule9,],
	"+": [rule6,],
	"-": [rule5,rule7,],
	"/": [rule0,rule8,],
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
	":": [rule21,rule22,],
	"<": [rule12,],
	"=": [rule10,],
	">": [rule11,],
	"@": [rule23,rule24,],
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
	"[": [rule3,],
	"^": [rule16,],
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
	"|": [rule15,],
	"~": [rule17,],
}

# x.rulesDictDict for tsql mode.
rulesDictDict = {
	"tsql_main": rulesDict1,
}

# Import dict for tsql mode.
importDict = {}

