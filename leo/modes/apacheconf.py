# Leo colorizer control file for apacheconf mode.
# This file is in the public domain.

# Properties for apacheconf mode.
properties = {
	"lineComment": "#",
}

# Attributes dict for apacheconf_main ruleset.
apacheconf_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"highlight_digits": "false",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for apacheconf_directive ruleset.
apacheconf_directive_attributes_dict = {
	"default": "NULL",
	"digit_re": "",
	"highlight_digits": "false",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Attributes dict for apacheconf_vhost ruleset.
apacheconf_vhost_attributes_dict = {
	"default": "NULL",
	"digit_re": "",
	"highlight_digits": "false",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for apacheconf mode.
attributesDictDict = {
	"apacheconf_directive": apacheconf_directive_attributes_dict,
	"apacheconf_main": apacheconf_main_attributes_dict,
	"apacheconf_vhost": apacheconf_vhost_attributes_dict,
}

# Keywords dict for apacheconf_main ruleset.
apacheconf_main_keywords_dict = {
	"acceptmutex": "keyword1",
	"acceptpathinfo": "keyword1",
	"accessfilename": "keyword1",
	"action": "keyword1",
	"addalt": "keyword1",
	"addaltbyencoding": "keyword1",
	"addaltbytype": "keyword1",
	"addcharset": "keyword1",
	"adddefaultcharset": "keyword1",
	"adddescription": "keyword1",
	"addencoding": "keyword1",
	"addhandler": "keyword1",
	"addicon": "keyword1",
	"addiconbyencoding": "keyword1",
	"addiconbytype": "keyword1",
	"addinputfilter": "keyword1",
	"addlanguage": "keyword1",
	"addmodule": "keyword4",
	"addmoduleinfo": "keyword1",
	"addoutputfilter": "keyword1",
	"addoutputfilterbytype": "keyword1",
	"addtype": "keyword1",
	"alias": "keyword1",
	"aliasmatch": "keyword1",
	"allowconnect": "keyword1",
	"allowencodedslashes": "keyword1",
	"authdigestnccheck": "keyword1",
	"authdigestshmemsize": "keyword1",
	"authldapcharsetconfig": "keyword1",
	"browsermatch": "keyword1",
	"browsermatchnocase": "keyword1",
	"bs2000account": "keyword1",
	"cachedefaultexpire": "keyword1",
	"cachedirlength": "keyword1",
	"cachedirlevels": "keyword1",
	"cachedisable": "keyword1",
	"cacheenable": "keyword1",
	"cacheexpirycheck": "keyword1",
	"cachefile": "keyword1",
	"cacheforcecompletion": "keyword1",
	"cachegcclean": "keyword1",
	"cachegcdaily": "keyword1",
	"cachegcinterval": "keyword1",
	"cachegcmemusage": "keyword1",
	"cachegcunused": "keyword1",
	"cacheignorecachecontrol": "keyword1",
	"cacheignorenolastmod": "keyword1",
	"cachelastmodifiedfactor": "keyword1",
	"cachemaxexpire": "keyword1",
	"cachemaxfilesize": "keyword1",
	"cacheminfilesize": "keyword1",
	"cachenegotiateddocs": "keyword1",
	"cacheroot": "keyword1",
	"cachesize": "keyword1",
	"cachetimemargin": "keyword1",
	"charsetdefault": "keyword1",
	"charsetoptions": "keyword1",
	"charsetsourceenc": "keyword1",
	"checkspelling": "keyword1",
	"childperuserid": "keyword1",
	"clearmodulelist": "keyword4",
	"contentdigest": "keyword1",
	"cookiedomain": "keyword1",
	"cookieexpires": "keyword1",
	"cookielog": "keyword1",
	"cookiename": "keyword1",
	"cookiestyle": "keyword1",
	"cookietracking": "keyword1",
	"coredumpdirectory": "keyword1",
	"customlog": "keyword1",
	"davdepthinfinity": "keyword1",
	"davlockdb": "keyword1",
	"davmintimeout": "keyword1",
	"defaulticon": "keyword1",
	"defaultlanguage": "keyword1",
	"defaulttype": "keyword1",
	"deflatebuffersize": "keyword1",
	"deflatecompressionlevel": "keyword1",
	"deflatefilternote": "keyword1",
	"deflatememlevel": "keyword1",
	"deflatewindowsize": "keyword1",
	"directoryindex": "keyword1",
	"documentroot": "keyword1",
	"enablemmap": "keyword1",
	"enablesendfile": "keyword1",
	"errordocument": "keyword1",
	"errorlog": "keyword1",
	"example": "keyword1",
	"expiresactive": "keyword1",
	"expiresbytype": "keyword1",
	"expiresdefault": "keyword1",
	"extendedstatus": "keyword1",
	"extfilterdefine": "keyword1",
	"fileetag": "keyword1",
	"forcelanguagepriority": "keyword1",
	"group": "keyword1",
	"header": "keyword1",
	"headername": "keyword1",
	"hostnamelookups": "keyword1",
	"identitycheck": "keyword1",
	"imapbase": "keyword1",
	"imapdefault": "keyword1",
	"imapmenu": "keyword1",
	"include": "keyword1",
	"indexignore": "keyword1",
	"indexoptions": "keyword1",
	"indexorderdefault": "keyword1",
	"isapiappendlogtoerrors": "keyword1",
	"isapiappendlogtoquery": "keyword1",
	"isapicachefile": "keyword1",
	"isapifakeasync": "keyword1",
	"isapilognotsupported": "keyword1",
	"isapireadaheadbuffer": "keyword1",
	"keepalive": "keyword1",
	"keepalivetimeout": "keyword1",
	"languagepriority": "keyword1",
	"ldapcacheentries": "keyword1",
	"ldapcachettl": "keyword1",
	"ldapopcacheentries": "keyword1",
	"ldapopcachettl": "keyword1",
	"ldapsharedcachesize": "keyword1",
	"ldaptrustedca": "keyword1",
	"ldaptrustedcatype": "keyword1",
	"limitinternalrecursion": "keyword1",
	"limitrequestbody": "keyword1",
	"limitrequestfields": "keyword1",
	"limitrequestfieldsize": "keyword1",
	"limitrequestline": "keyword1",
	"limitxmlrequestbody": "keyword1",
	"listen": "keyword1",
	"listenbacklog": "keyword1",
	"loadfile": "keyword1",
	"loadmodule": "keyword1",
	"lockfile": "keyword1",
	"logformat": "keyword1",
	"loglevel": "keyword1",
	"maxclients": "keyword1",
	"maxkeepaliverequests": "keyword1",
	"maxmemfree": "keyword1",
	"maxrequestsperchild": "keyword1",
	"maxrequestsperthread": "keyword1",
	"maxspareservers": "keyword1",
	"maxsparethreads": "keyword1",
	"maxthreads": "keyword1",
	"maxthreadsperchild": "keyword1",
	"mcachemaxobjectcount": "keyword1",
	"mcachemaxobjectsize": "keyword1",
	"mcachemaxstreamingbuffer": "keyword1",
	"mcacheminobjectsize": "keyword1",
	"mcacheremovalalgorithm": "keyword1",
	"mcachesize": "keyword1",
	"metadir": "keyword1",
	"metafiles": "keyword1",
	"metasuffix": "keyword1",
	"mimemagicfile": "keyword1",
	"minspareservers": "keyword1",
	"minsparethreads": "keyword1",
	"mmapfile": "keyword1",
	"multiviewsmatch": "keyword1",
	"namevirtualhost": "keyword1",
	"noproxy": "keyword1",
	"numservers": "keyword1",
	"nwssltrustedcerts": "keyword1",
	"options": "keyword1",
	"passenv": "keyword1",
	"pidfile": "keyword1",
	"port": "keyword4",
	"protocolecho": "keyword1",
	"proxybadheader": "keyword1",
	"proxyblock": "keyword1",
	"proxydomain": "keyword1",
	"proxyerroroverride": "keyword1",
	"proxyiobuffersize": "keyword1",
	"proxymaxforwards": "keyword1",
	"proxypass": "keyword1",
	"proxypassreverse": "keyword1",
	"proxypreservehost": "keyword1",
	"proxyreceivebuffersize": "keyword1",
	"proxyremote": "keyword1",
	"proxyremotematch": "keyword1",
	"proxyrequests": "keyword1",
	"proxytimeout": "keyword1",
	"proxyvia": "keyword1",
	"readmename": "keyword1",
	"redirect": "keyword1",
	"redirectmatch": "keyword1",
	"redirectpermanent": "keyword1",
	"redirecttemp": "keyword1",
	"requestheader": "keyword1",
	"rewritecond": "keyword1",
	"rewriteengine": "keyword1",
	"rewritelock": "keyword1",
	"rewritelog": "keyword1",
	"rewriteloglevel": "keyword1",
	"rewritemap": "keyword1",
	"rewriteoptions": "keyword1",
	"rewriterule": "keyword1",
	"rlimitcpu": "keyword1",
	"rlimitmem": "keyword1",
	"rlimitnproc": "keyword1",
	"scoreboardfile": "keyword1",
	"script": "keyword1",
	"scriptalias": "keyword1",
	"scriptaliasmatch": "keyword1",
	"scriptinterpretersource": "keyword1",
	"scriptlog": "keyword1",
	"scriptlogbuffer": "keyword1",
	"scriptloglength": "keyword1",
	"scriptsock": "keyword1",
	"securelisten": "keyword1",
	"sendbuffersize": "keyword1",
	"serveradmin": "keyword1",
	"serverlimit": "keyword1",
	"servername": "keyword1",
	"serverroot": "keyword1",
	"serversignature": "keyword1",
	"servertokens": "keyword1",
	"servertype": "keyword4",
	"setenv": "keyword1",
	"setenvif": "keyword1",
	"setenvifnocase": "keyword1",
	"sethandler": "keyword1",
	"setinputfilter": "keyword1",
	"setoutputfilter": "keyword1",
	"ssiendtag": "keyword1",
	"ssierrormsg": "keyword1",
	"ssistarttag": "keyword1",
	"ssitimeformat": "keyword1",
	"ssiundefinedecho": "keyword1",
	"sslcacertificatefile": "keyword1",
	"sslcacertificatepath": "keyword1",
	"sslcarevocationfile": "keyword1",
	"sslcarevocationpath": "keyword1",
	"sslcertificatechainfile": "keyword1",
	"sslcertificatefile": "keyword1",
	"sslcertificatekeyfile": "keyword1",
	"sslciphersuite": "keyword1",
	"sslengine": "keyword1",
	"sslmutex": "keyword1",
	"ssloptions": "keyword1",
	"sslpassphrasedialog": "keyword1",
	"sslprotocol": "keyword1",
	"sslproxycacertificatefile": "keyword1",
	"sslproxycacertificatepath": "keyword1",
	"sslproxycarevocationfile": "keyword1",
	"sslproxycarevocationpath": "keyword1",
	"sslproxyciphersuite": "keyword1",
	"sslproxyengine": "keyword1",
	"sslproxymachinecertificatefile": "keyword1",
	"sslproxymachinecertificatepath": "keyword1",
	"sslproxyprotocol": "keyword1",
	"sslproxyverify": "keyword1",
	"sslproxyverifydepth": "keyword1",
	"sslrandomseed": "keyword1",
	"sslsessioncache": "keyword1",
	"sslsessioncachetimeout": "keyword1",
	"sslverifyclient": "keyword1",
	"sslverifydepth": "keyword1",
	"startservers": "keyword1",
	"startthreads": "keyword1",
	"suexecusergroup": "keyword1",
	"threadlimit": "keyword1",
	"threadsperchild": "keyword1",
	"threadstacksize": "keyword1",
	"timeout": "keyword1",
	"transferlog": "keyword1",
	"typesconfig": "keyword1",
	"unsetenv": "keyword1",
	"usecanonicalname": "keyword1",
	"user": "keyword1",
	"userdir": "keyword1",
	"virtualdocumentroot": "keyword1",
	"virtualdocumentrootip": "keyword1",
	"virtualscriptalias": "keyword1",
	"virtualscriptaliasip": "keyword1",
	"xbithack": "keyword1",
}

# Keywords dict for apacheconf_directive ruleset.
apacheconf_directive_keywords_dict = {
	"acceptmutex": "keyword2",
	"acceptpathinfo": "keyword2",
	"accessfilename": "keyword2",
	"action": "keyword2",
	"addalt": "keyword2",
	"addaltbyencoding": "keyword2",
	"addaltbytype": "keyword2",
	"addcharset": "keyword2",
	"adddefaultcharset": "keyword2",
	"adddescription": "keyword2",
	"addencoding": "keyword2",
	"addhandler": "keyword2",
	"addicon": "keyword2",
	"addiconbyencoding": "keyword2",
	"addiconbytype": "keyword2",
	"addinputfilter": "keyword2",
	"addlanguage": "keyword2",
	"addmodule": "keyword4",
	"addmoduleinfo": "keyword2",
	"addoutputfilter": "keyword2",
	"addoutputfilterbytype": "keyword2",
	"addtype": "keyword2",
	"alias": "keyword2",
	"aliasmatch": "keyword2",
	"allow": "keyword2",
	"allowconnect": "keyword2",
	"allowencodedslashes": "keyword2",
	"allowoverride": "keyword2",
	"anonymous": "keyword2",
	"anonymous_authoritative": "keyword2",
	"anonymous_logemail": "keyword2",
	"anonymous_mustgiveemail": "keyword2",
	"anonymous_nouserid": "keyword2",
	"anonymous_verifyemail": "keyword2",
	"authauthoritative": "keyword2",
	"authdbmauthoritative": "keyword2",
	"authdbmgroupfile": "keyword2",
	"authdbmtype": "keyword2",
	"authdbmuserfile": "keyword2",
	"authdigestalgorithm": "keyword2",
	"authdigestdomain": "keyword2",
	"authdigestfile": "keyword2",
	"authdigestgroupfile": "keyword2",
	"authdigestnccheck": "keyword2",
	"authdigestnonceformat": "keyword2",
	"authdigestnoncelifetime": "keyword2",
	"authdigestqop": "keyword2",
	"authdigestshmemsize": "keyword2",
	"authgroupfile": "keyword2",
	"authldapauthoritative": "keyword2",
	"authldapbinddn": "keyword2",
	"authldapbindpassword": "keyword2",
	"authldapcharsetconfig": "keyword2",
	"authldapcomparednonserver": "keyword2",
	"authldapdereferencealiases": "keyword2",
	"authldapenabled": "keyword2",
	"authldapfrontpagehack": "keyword2",
	"authldapgroupattribute": "keyword2",
	"authldapgroupattributeisdn": "keyword2",
	"authldapremoteuserisdn": "keyword2",
	"authldapurl": "keyword2",
	"authname": "keyword2",
	"authtype": "keyword2",
	"authuserfile": "keyword2",
	"browsermatch": "keyword2",
	"browsermatchnocase": "keyword2",
	"bs2000account": "keyword2",
	"cachedefaultexpire": "keyword2",
	"cachedirlength": "keyword2",
	"cachedirlevels": "keyword2",
	"cachedisable": "keyword2",
	"cacheenable": "keyword2",
	"cacheexpirycheck": "keyword2",
	"cachefile": "keyword2",
	"cacheforcecompletion": "keyword2",
	"cachegcclean": "keyword2",
	"cachegcdaily": "keyword2",
	"cachegcinterval": "keyword2",
	"cachegcmemusage": "keyword2",
	"cachegcunused": "keyword2",
	"cacheignorecachecontrol": "keyword2",
	"cacheignorenolastmod": "keyword2",
	"cachelastmodifiedfactor": "keyword2",
	"cachemaxexpire": "keyword2",
	"cachemaxfilesize": "keyword2",
	"cacheminfilesize": "keyword2",
	"cachenegotiateddocs": "keyword2",
	"cacheroot": "keyword2",
	"cachesize": "keyword2",
	"cachetimemargin": "keyword2",
	"cgimapextension": "keyword2",
	"charsetdefault": "keyword2",
	"charsetoptions": "keyword2",
	"charsetsourceenc": "keyword2",
	"checkspelling": "keyword2",
	"childperuserid": "keyword2",
	"clearmodulelist": "keyword4",
	"contentdigest": "keyword2",
	"cookiedomain": "keyword2",
	"cookieexpires": "keyword2",
	"cookielog": "keyword2",
	"cookiename": "keyword2",
	"cookiestyle": "keyword2",
	"cookietracking": "keyword2",
	"coredumpdirectory": "keyword2",
	"customlog": "keyword2",
	"dav": "keyword2",
	"davdepthinfinity": "keyword2",
	"davlockdb": "keyword2",
	"davmintimeout": "keyword2",
	"defaulticon": "keyword2",
	"defaultlanguage": "keyword2",
	"defaulttype": "keyword2",
	"deflatebuffersize": "keyword2",
	"deflatecompressionlevel": "keyword2",
	"deflatefilternote": "keyword2",
	"deflatememlevel": "keyword2",
	"deflatewindowsize": "keyword2",
	"deny": "keyword2",
	"directoryindex": "keyword2",
	"documentroot": "keyword2",
	"enablemmap": "keyword2",
	"enablesendfile": "keyword2",
	"errordocument": "keyword2",
	"errorlog": "keyword2",
	"example": "keyword2",
	"expiresactive": "keyword2",
	"expiresbytype": "keyword2",
	"expiresdefault": "keyword2",
	"extendedstatus": "keyword2",
	"extfilterdefine": "keyword2",
	"extfilteroptions": "keyword2",
	"fileetag": "keyword2",
	"forcelanguagepriority": "keyword2",
	"forcetype": "keyword2",
	"group": "keyword2",
	"header": "keyword2",
	"headername": "keyword2",
	"hostnamelookups": "keyword2",
	"identitycheck": "keyword2",
	"imapbase": "keyword2",
	"imapdefault": "keyword2",
	"imapmenu": "keyword2",
	"include": "keyword2",
	"indexignore": "keyword2",
	"indexoptions": "keyword2",
	"indexorderdefault": "keyword2",
	"isapiappendlogtoerrors": "keyword2",
	"isapiappendlogtoquery": "keyword2",
	"isapicachefile": "keyword2",
	"isapifakeasync": "keyword2",
	"isapilognotsupported": "keyword2",
	"isapireadaheadbuffer": "keyword2",
	"keepalive": "keyword2",
	"keepalivetimeout": "keyword2",
	"languagepriority": "keyword2",
	"ldapcacheentries": "keyword2",
	"ldapcachettl": "keyword2",
	"ldapopcacheentries": "keyword2",
	"ldapopcachettl": "keyword2",
	"ldapsharedcachesize": "keyword2",
	"ldaptrustedca": "keyword2",
	"ldaptrustedcatype": "keyword2",
	"limitinternalrecursion": "keyword2",
	"limitrequestbody": "keyword2",
	"limitrequestfields": "keyword2",
	"limitrequestfieldsize": "keyword2",
	"limitrequestline": "keyword2",
	"limitxmlrequestbody": "keyword2",
	"listen": "keyword2",
	"listenbacklog": "keyword2",
	"loadfile": "keyword2",
	"loadmodule": "keyword2",
	"lockfile": "keyword2",
	"logformat": "keyword2",
	"loglevel": "keyword2",
	"maxclients": "keyword2",
	"maxkeepaliverequests": "keyword2",
	"maxmemfree": "keyword2",
	"maxrequestsperchild": "keyword2",
	"maxrequestsperthread": "keyword2",
	"maxspareservers": "keyword2",
	"maxsparethreads": "keyword2",
	"maxthreads": "keyword2",
	"maxthreadsperchild": "keyword2",
	"mcachemaxobjectcount": "keyword2",
	"mcachemaxobjectsize": "keyword2",
	"mcachemaxstreamingbuffer": "keyword2",
	"mcacheminobjectsize": "keyword2",
	"mcacheremovalalgorithm": "keyword2",
	"mcachesize": "keyword2",
	"metadir": "keyword2",
	"metafiles": "keyword2",
	"metasuffix": "keyword2",
	"mimemagicfile": "keyword2",
	"minspareservers": "keyword2",
	"minsparethreads": "keyword2",
	"mmapfile": "keyword2",
	"modmimeusepathinfo": "keyword2",
	"multiviewsmatch": "keyword2",
	"namevirtualhost": "keyword2",
	"noproxy": "keyword2",
	"numservers": "keyword2",
	"nwssltrustedcerts": "keyword2",
	"options": "keyword2",
	"order": "keyword2",
	"passenv": "keyword2",
	"pidfile": "keyword2",
	"protocolecho": "keyword2",
	"proxybadheader": "keyword2",
	"proxyblock": "keyword2",
	"proxydomain": "keyword2",
	"proxyerroroverride": "keyword2",
	"proxyiobuffersize": "keyword2",
	"proxymaxforwards": "keyword2",
	"proxypass": "keyword2",
	"proxypassreverse": "keyword2",
	"proxypreservehost": "keyword2",
	"proxyreceivebuffersize": "keyword2",
	"proxyremote": "keyword2",
	"proxyremotematch": "keyword2",
	"proxyrequests": "keyword2",
	"proxytimeout": "keyword2",
	"proxyvia": "keyword2",
	"pythondebug": "keyword3",
	"pythonhandler": "keyword3",
	"readmename": "keyword2",
	"redirect": "keyword2",
	"redirectmatch": "keyword2",
	"redirectpermanent": "keyword2",
	"redirecttemp": "keyword2",
	"removecharset": "keyword2",
	"removeencoding": "keyword2",
	"removehandler": "keyword2",
	"removeinputfilter": "keyword2",
	"removelanguage": "keyword2",
	"removeoutputfilter": "keyword2",
	"removetype": "keyword2",
	"requestheader": "keyword2",
	"require": "keyword2",
	"rewritebase": "keyword2",
	"rewritecond": "keyword2",
	"rewriteengine": "keyword2",
	"rewritelock": "keyword2",
	"rewritelog": "keyword2",
	"rewriteloglevel": "keyword2",
	"rewritemap": "keyword2",
	"rewriteoptions": "keyword2",
	"rewriterule": "keyword2",
	"rlimitcpu": "keyword2",
	"rlimitmem": "keyword2",
	"rlimitnproc": "keyword2",
	"satisfy": "keyword2",
	"scoreboardfile": "keyword2",
	"script": "keyword2",
	"scriptalias": "keyword2",
	"scriptaliasmatch": "keyword2",
	"scriptinterpretersource": "keyword2",
	"scriptlog": "keyword2",
	"scriptlogbuffer": "keyword2",
	"scriptloglength": "keyword2",
	"scriptsock": "keyword2",
	"securelisten": "keyword2",
	"sendbuffersize": "keyword2",
	"serveradmin": "keyword2",
	"serverlimit": "keyword2",
	"servername": "keyword2",
	"serverroot": "keyword2",
	"serversignature": "keyword2",
	"servertokens": "keyword2",
	"setenv": "keyword2",
	"setenvif": "keyword2",
	"setenvifnocase": "keyword2",
	"sethandler": "keyword2",
	"setinputfilter": "keyword2",
	"setoutputfilter": "keyword2",
	"ssiendtag": "keyword2",
	"ssierrormsg": "keyword2",
	"ssistarttag": "keyword2",
	"ssitimeformat": "keyword2",
	"ssiundefinedecho": "keyword2",
	"sslcacertificatefile": "keyword2",
	"sslcacertificatepath": "keyword2",
	"sslcarevocationfile": "keyword2",
	"sslcarevocationpath": "keyword2",
	"sslcertificatechainfile": "keyword2",
	"sslcertificatefile": "keyword2",
	"sslcertificatekeyfile": "keyword2",
	"sslciphersuite": "keyword2",
	"sslengine": "keyword2",
	"sslmutex": "keyword2",
	"ssloptions": "keyword2",
	"sslpassphrasedialog": "keyword2",
	"sslprotocol": "keyword2",
	"sslproxycacertificatefile": "keyword2",
	"sslproxycacertificatepath": "keyword2",
	"sslproxycarevocationfile": "keyword2",
	"sslproxycarevocationpath": "keyword2",
	"sslproxyciphersuite": "keyword2",
	"sslproxyengine": "keyword2",
	"sslproxymachinecertificatefile": "keyword2",
	"sslproxymachinecertificatepath": "keyword2",
	"sslproxyprotocol": "keyword2",
	"sslproxyverify": "keyword2",
	"sslproxyverifydepth": "keyword2",
	"sslrandomseed": "keyword2",
	"sslrequire": "keyword2",
	"sslrequiressl": "keyword2",
	"sslsessioncache": "keyword2",
	"sslsessioncachetimeout": "keyword2",
	"sslverifyclient": "keyword2",
	"sslverifydepth": "keyword2",
	"startservers": "keyword2",
	"startthreads": "keyword2",
	"suexecusergroup": "keyword2",
	"svnindexxslt": "keyword3",
	"svnparentpath": "keyword3",
	"svnpath": "keyword3",
	"threadlimit": "keyword2",
	"threadsperchild": "keyword2",
	"threadstacksize": "keyword2",
	"timeout": "keyword2",
	"transferlog": "keyword2",
	"typesconfig": "keyword2",
	"unsetenv": "keyword2",
	"usecanonicalname": "keyword2",
	"user": "keyword2",
	"userdir": "keyword2",
	"virtualdocumentroot": "keyword2",
	"virtualdocumentrootip": "keyword2",
	"virtualscriptalias": "keyword2",
	"virtualscriptaliasip": "keyword2",
	"xbithack": "keyword2",
}

# Keywords dict for apacheconf_vhost ruleset.
apacheconf_vhost_keywords_dict = {
	"acceptmutex": "keyword2",
	"acceptpathinfo": "keyword2",
	"accessfilename": "keyword2",
	"action": "keyword2",
	"addalt": "keyword2",
	"addaltbyencoding": "keyword2",
	"addaltbytype": "keyword2",
	"addcharset": "keyword2",
	"adddefaultcharset": "keyword2",
	"adddescription": "keyword2",
	"addencoding": "keyword2",
	"addhandler": "keyword2",
	"addicon": "keyword2",
	"addiconbyencoding": "keyword2",
	"addiconbytype": "keyword2",
	"addinputfilter": "keyword2",
	"addlanguage": "keyword2",
	"addmoduleinfo": "keyword2",
	"addoutputfilter": "keyword2",
	"addoutputfilterbytype": "keyword2",
	"addtype": "keyword2",
	"alias": "keyword2",
	"aliasmatch": "keyword2",
	"allowconnect": "keyword2",
	"allowencodedslashes": "keyword2",
	"assignuserid": "keyword2",
	"authdigestnccheck": "keyword2",
	"authdigestshmemsize": "keyword2",
	"authldapcharsetconfig": "keyword2",
	"browsermatch": "keyword2",
	"browsermatchnocase": "keyword2",
	"bs2000account": "keyword2",
	"cachedefaultexpire": "keyword2",
	"cachedirlength": "keyword2",
	"cachedirlevels": "keyword2",
	"cachedisable": "keyword2",
	"cacheenable": "keyword2",
	"cacheexpirycheck": "keyword2",
	"cachefile": "keyword2",
	"cacheforcecompletion": "keyword2",
	"cachegcclean": "keyword2",
	"cachegcdaily": "keyword2",
	"cachegcinterval": "keyword2",
	"cachegcmemusage": "keyword2",
	"cachegcunused": "keyword2",
	"cacheignorecachecontrol": "keyword2",
	"cacheignorenolastmod": "keyword2",
	"cachelastmodifiedfactor": "keyword2",
	"cachemaxexpire": "keyword2",
	"cachemaxfilesize": "keyword2",
	"cacheminfilesize": "keyword2",
	"cachenegotiateddocs": "keyword2",
	"cacheroot": "keyword2",
	"cachesize": "keyword2",
	"cachetimemargin": "keyword2",
	"charsetdefault": "keyword2",
	"charsetoptions": "keyword2",
	"charsetsourceenc": "keyword2",
	"checkspelling": "keyword2",
	"childperuserid": "keyword2",
	"contentdigest": "keyword2",
	"cookiedomain": "keyword2",
	"cookieexpires": "keyword2",
	"cookielog": "keyword2",
	"cookiename": "keyword2",
	"cookiestyle": "keyword2",
	"cookietracking": "keyword2",
	"coredumpdirectory": "keyword2",
	"customlog": "keyword2",
	"davdepthinfinity": "keyword2",
	"davlockdb": "keyword2",
	"davmintimeout": "keyword2",
	"defaulticon": "keyword2",
	"defaultlanguage": "keyword2",
	"defaulttype": "keyword2",
	"deflatebuffersize": "keyword2",
	"deflatecompressionlevel": "keyword2",
	"deflatefilternote": "keyword2",
	"deflatememlevel": "keyword2",
	"deflatewindowsize": "keyword2",
	"directoryindex": "keyword2",
	"documentroot": "keyword2",
	"enablemmap": "keyword2",
	"enablesendfile": "keyword2",
	"errordocument": "keyword2",
	"errorlog": "keyword2",
	"example": "keyword2",
	"expiresactive": "keyword2",
	"expiresbytype": "keyword2",
	"expiresdefault": "keyword2",
	"extendedstatus": "keyword2",
	"extfilterdefine": "keyword2",
	"fileetag": "keyword2",
	"forcelanguagepriority": "keyword2",
	"group": "keyword2",
	"header": "keyword2",
	"headername": "keyword2",
	"hostnamelookups": "keyword2",
	"identitycheck": "keyword2",
	"imapbase": "keyword2",
	"imapdefault": "keyword2",
	"imapmenu": "keyword2",
	"include": "keyword2",
	"indexignore": "keyword2",
	"indexoptions": "keyword2",
	"indexorderdefault": "keyword2",
	"isapiappendlogtoerrors": "keyword2",
	"isapiappendlogtoquery": "keyword2",
	"isapicachefile": "keyword2",
	"isapifakeasync": "keyword2",
	"isapilognotsupported": "keyword2",
	"isapireadaheadbuffer": "keyword2",
	"keepalive": "keyword2",
	"keepalivetimeout": "keyword2",
	"languagepriority": "keyword2",
	"ldapcacheentries": "keyword2",
	"ldapcachettl": "keyword2",
	"ldapopcacheentries": "keyword2",
	"ldapopcachettl": "keyword2",
	"ldapsharedcachesize": "keyword2",
	"ldaptrustedca": "keyword2",
	"ldaptrustedcatype": "keyword2",
	"limitinternalrecursion": "keyword2",
	"limitrequestbody": "keyword2",
	"limitrequestfields": "keyword2",
	"limitrequestfieldsize": "keyword2",
	"limitrequestline": "keyword2",
	"limitxmlrequestbody": "keyword2",
	"listen": "keyword2",
	"listenbacklog": "keyword2",
	"loadfile": "keyword2",
	"loadmodule": "keyword2",
	"lockfile": "keyword2",
	"logformat": "keyword2",
	"loglevel": "keyword2",
	"maxclients": "keyword2",
	"maxkeepaliverequests": "keyword2",
	"maxmemfree": "keyword2",
	"maxrequestsperchild": "keyword2",
	"maxrequestsperthread": "keyword2",
	"maxspareservers": "keyword2",
	"maxsparethreads": "keyword2",
	"maxthreads": "keyword2",
	"maxthreadsperchild": "keyword2",
	"mcachemaxobjectcount": "keyword2",
	"mcachemaxobjectsize": "keyword2",
	"mcachemaxstreamingbuffer": "keyword2",
	"mcacheminobjectsize": "keyword2",
	"mcacheremovalalgorithm": "keyword2",
	"mcachesize": "keyword2",
	"metadir": "keyword2",
	"metafiles": "keyword2",
	"metasuffix": "keyword2",
	"mimemagicfile": "keyword2",
	"minspareservers": "keyword2",
	"minsparethreads": "keyword2",
	"mmapfile": "keyword2",
	"multiviewsmatch": "keyword2",
	"namevirtualhost": "keyword2",
	"noproxy": "keyword2",
	"numservers": "keyword2",
	"nwssltrustedcerts": "keyword2",
	"options": "keyword2",
	"passenv": "keyword2",
	"pidfile": "keyword2",
	"protocolecho": "keyword2",
	"proxybadheader": "keyword2",
	"proxyblock": "keyword2",
	"proxydomain": "keyword2",
	"proxyerroroverride": "keyword2",
	"proxyiobuffersize": "keyword2",
	"proxymaxforwards": "keyword2",
	"proxypass": "keyword2",
	"proxypassreverse": "keyword2",
	"proxypreservehost": "keyword2",
	"proxyreceivebuffersize": "keyword2",
	"proxyremote": "keyword2",
	"proxyremotematch": "keyword2",
	"proxyrequests": "keyword2",
	"proxytimeout": "keyword2",
	"proxyvia": "keyword2",
	"readmename": "keyword2",
	"redirect": "keyword2",
	"redirectmatch": "keyword2",
	"redirectpermanent": "keyword2",
	"redirecttemp": "keyword2",
	"removecharset": "keyword2",
	"removeencoding": "keyword2",
	"removehandler": "keyword2",
	"removeinputfilter": "keyword2",
	"removelanguage": "keyword2",
	"removeoutputfilter": "keyword2",
	"removetype": "keyword2",
	"requestheader": "keyword2",
	"rewritecond": "keyword2",
	"rewriteengine": "keyword2",
	"rewritelock": "keyword2",
	"rewritelog": "keyword2",
	"rewriteloglevel": "keyword2",
	"rewritemap": "keyword2",
	"rewriteoptions": "keyword2",
	"rewriterule": "keyword2",
	"rlimitcpu": "keyword2",
	"rlimitmem": "keyword2",
	"rlimitnproc": "keyword2",
	"scoreboardfile": "keyword2",
	"script": "keyword2",
	"scriptalias": "keyword2",
	"scriptaliasmatch": "keyword2",
	"scriptinterpretersource": "keyword2",
	"scriptlog": "keyword2",
	"scriptlogbuffer": "keyword2",
	"scriptloglength": "keyword2",
	"scriptsock": "keyword2",
	"securelisten": "keyword2",
	"sendbuffersize": "keyword2",
	"serveradmin": "keyword2",
	"serveralias": "keyword2",
	"serverlimit": "keyword2",
	"servername": "keyword2",
	"serverpath": "keyword2",
	"serverroot": "keyword2",
	"serversignature": "keyword2",
	"servertokens": "keyword2",
	"setenv": "keyword2",
	"setenvif": "keyword2",
	"setenvifnocase": "keyword2",
	"sethandler": "keyword2",
	"setinputfilter": "keyword2",
	"setoutputfilter": "keyword2",
	"ssiendtag": "keyword2",
	"ssierrormsg": "keyword2",
	"ssistarttag": "keyword2",
	"ssitimeformat": "keyword2",
	"ssiundefinedecho": "keyword2",
	"sslcacertificatefile": "keyword2",
	"sslcacertificatepath": "keyword2",
	"sslcarevocationfile": "keyword2",
	"sslcarevocationpath": "keyword2",
	"sslcertificatechainfile": "keyword2",
	"sslcertificatefile": "keyword2",
	"sslcertificatekeyfile": "keyword2",
	"sslciphersuite": "keyword2",
	"sslengine": "keyword2",
	"sslmutex": "keyword2",
	"ssloptions": "keyword2",
	"sslpassphrasedialog": "keyword2",
	"sslprotocol": "keyword2",
	"sslproxycacertificatefile": "keyword2",
	"sslproxycacertificatepath": "keyword2",
	"sslproxycarevocationfile": "keyword2",
	"sslproxycarevocationpath": "keyword2",
	"sslproxyciphersuite": "keyword2",
	"sslproxyengine": "keyword2",
	"sslproxymachinecertificatefile": "keyword2",
	"sslproxymachinecertificatepath": "keyword2",
	"sslproxyprotocol": "keyword2",
	"sslproxyverify": "keyword2",
	"sslproxyverifydepth": "keyword2",
	"sslrandomseed": "keyword2",
	"sslsessioncache": "keyword2",
	"sslsessioncachetimeout": "keyword2",
	"sslverifyclient": "keyword2",
	"sslverifydepth": "keyword2",
	"startservers": "keyword2",
	"startthreads": "keyword2",
	"suexecusergroup": "keyword2",
	"threadlimit": "keyword2",
	"threadsperchild": "keyword2",
	"threadstacksize": "keyword2",
	"timeout": "keyword2",
	"transferlog": "keyword2",
	"typesconfig": "keyword2",
	"unsetenv": "keyword2",
	"usecanonicalname": "keyword2",
	"user": "keyword2",
	"userdir": "keyword2",
	"virtualdocumentroot": "keyword2",
	"virtualdocumentrootip": "keyword2",
	"virtualscriptalias": "keyword2",
	"virtualscriptaliasip": "keyword2",
	"xbithack": "keyword2",
}

# Dictionary of keywords dictionaries for apacheconf mode.
keywordsDictDict = {
	"apacheconf_directive": apacheconf_directive_keywords_dict,
	"apacheconf_main": apacheconf_main_keywords_dict,
	"apacheconf_vhost": apacheconf_vhost_keywords_dict,
}

# Rules for apacheconf_main ruleset.

def apacheconf_rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def apacheconf_rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def apacheconf_rule2(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="markup", begin="<(VirtualHost)[^>]*>", end="</$1>", hash_char="< ",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="VHOST",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def apacheconf_rule3(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="markup", begin="<(\\w+)[^>]*>", end="</$1>", hash_char="< ",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="DIRECTIVE",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def apacheconf_rule4(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for apacheconf_main ruleset.
rulesDict1 = {
	"\"": [apacheconf_rule1,],
	"#": [apacheconf_rule0,],
	"0": [apacheconf_rule4,],
	"1": [apacheconf_rule4,],
	"2": [apacheconf_rule4,],
	"3": [apacheconf_rule4,],
	"4": [apacheconf_rule4,],
	"5": [apacheconf_rule4,],
	"6": [apacheconf_rule4,],
	"7": [apacheconf_rule4,],
	"8": [apacheconf_rule4,],
	"9": [apacheconf_rule4,],
	"<": [apacheconf_rule2,apacheconf_rule3,],
	"@": [apacheconf_rule4,],
	"A": [apacheconf_rule4,],
	"B": [apacheconf_rule4,],
	"C": [apacheconf_rule4,],
	"D": [apacheconf_rule4,],
	"E": [apacheconf_rule4,],
	"F": [apacheconf_rule4,],
	"G": [apacheconf_rule4,],
	"H": [apacheconf_rule4,],
	"I": [apacheconf_rule4,],
	"J": [apacheconf_rule4,],
	"K": [apacheconf_rule4,],
	"L": [apacheconf_rule4,],
	"M": [apacheconf_rule4,],
	"N": [apacheconf_rule4,],
	"O": [apacheconf_rule4,],
	"P": [apacheconf_rule4,],
	"Q": [apacheconf_rule4,],
	"R": [apacheconf_rule4,],
	"S": [apacheconf_rule4,],
	"T": [apacheconf_rule4,],
	"U": [apacheconf_rule4,],
	"V": [apacheconf_rule4,],
	"W": [apacheconf_rule4,],
	"X": [apacheconf_rule4,],
	"Y": [apacheconf_rule4,],
	"Z": [apacheconf_rule4,],
	"_": [apacheconf_rule4,],
	"a": [apacheconf_rule4,],
	"b": [apacheconf_rule4,],
	"c": [apacheconf_rule4,],
	"d": [apacheconf_rule4,],
	"e": [apacheconf_rule4,],
	"f": [apacheconf_rule4,],
	"g": [apacheconf_rule4,],
	"h": [apacheconf_rule4,],
	"i": [apacheconf_rule4,],
	"j": [apacheconf_rule4,],
	"k": [apacheconf_rule4,],
	"l": [apacheconf_rule4,],
	"m": [apacheconf_rule4,],
	"n": [apacheconf_rule4,],
	"o": [apacheconf_rule4,],
	"p": [apacheconf_rule4,],
	"q": [apacheconf_rule4,],
	"r": [apacheconf_rule4,],
	"s": [apacheconf_rule4,],
	"t": [apacheconf_rule4,],
	"u": [apacheconf_rule4,],
	"v": [apacheconf_rule4,],
	"w": [apacheconf_rule4,],
	"x": [apacheconf_rule4,],
	"y": [apacheconf_rule4,],
	"z": [apacheconf_rule4,],
}

# Rules for apacheconf_directive ruleset.

def apacheconf_rule5(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def apacheconf_rule6(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def apacheconf_rule7(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="markup", begin="<(VirtualHost)[^>]*>", end="</$1>", hash_char="< ",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="VHOST",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def apacheconf_rule8(colorer, s, i):
    return colorer.match_span_regexp(s, i, kind="markup", begin="<(\\w+)[^>]*>", end="</$1>", hash_char="< ",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="DIRECTIVE",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def apacheconf_rule9(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for apacheconf_directive ruleset.
rulesDict2 = {
	"\"": [apacheconf_rule6,],
	"#": [apacheconf_rule5,],
	"0": [apacheconf_rule9,],
	"1": [apacheconf_rule9,],
	"2": [apacheconf_rule9,],
	"3": [apacheconf_rule9,],
	"4": [apacheconf_rule9,],
	"5": [apacheconf_rule9,],
	"6": [apacheconf_rule9,],
	"7": [apacheconf_rule9,],
	"8": [apacheconf_rule9,],
	"9": [apacheconf_rule9,],
	"<": [apacheconf_rule7,apacheconf_rule8,],
	"@": [apacheconf_rule9,],
	"A": [apacheconf_rule9,],
	"B": [apacheconf_rule9,],
	"C": [apacheconf_rule9,],
	"D": [apacheconf_rule9,],
	"E": [apacheconf_rule9,],
	"F": [apacheconf_rule9,],
	"G": [apacheconf_rule9,],
	"H": [apacheconf_rule9,],
	"I": [apacheconf_rule9,],
	"J": [apacheconf_rule9,],
	"K": [apacheconf_rule9,],
	"L": [apacheconf_rule9,],
	"M": [apacheconf_rule9,],
	"N": [apacheconf_rule9,],
	"O": [apacheconf_rule9,],
	"P": [apacheconf_rule9,],
	"Q": [apacheconf_rule9,],
	"R": [apacheconf_rule9,],
	"S": [apacheconf_rule9,],
	"T": [apacheconf_rule9,],
	"U": [apacheconf_rule9,],
	"V": [apacheconf_rule9,],
	"W": [apacheconf_rule9,],
	"X": [apacheconf_rule9,],
	"Y": [apacheconf_rule9,],
	"Z": [apacheconf_rule9,],
	"_": [apacheconf_rule9,],
	"a": [apacheconf_rule9,],
	"b": [apacheconf_rule9,],
	"c": [apacheconf_rule9,],
	"d": [apacheconf_rule9,],
	"e": [apacheconf_rule9,],
	"f": [apacheconf_rule9,],
	"g": [apacheconf_rule9,],
	"h": [apacheconf_rule9,],
	"i": [apacheconf_rule9,],
	"j": [apacheconf_rule9,],
	"k": [apacheconf_rule9,],
	"l": [apacheconf_rule9,],
	"m": [apacheconf_rule9,],
	"n": [apacheconf_rule9,],
	"o": [apacheconf_rule9,],
	"p": [apacheconf_rule9,],
	"q": [apacheconf_rule9,],
	"r": [apacheconf_rule9,],
	"s": [apacheconf_rule9,],
	"t": [apacheconf_rule9,],
	"u": [apacheconf_rule9,],
	"v": [apacheconf_rule9,],
	"w": [apacheconf_rule9,],
	"x": [apacheconf_rule9,],
	"y": [apacheconf_rule9,],
	"z": [apacheconf_rule9,],
}

# Rules for apacheconf_vhost ruleset.

def apacheconf_rule10(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def apacheconf_rule11(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def apacheconf_rule12(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for apacheconf_vhost ruleset.
rulesDict3 = {
	"\"": [apacheconf_rule11,],
	"#": [apacheconf_rule10,],
	"0": [apacheconf_rule12,],
	"1": [apacheconf_rule12,],
	"2": [apacheconf_rule12,],
	"3": [apacheconf_rule12,],
	"4": [apacheconf_rule12,],
	"5": [apacheconf_rule12,],
	"6": [apacheconf_rule12,],
	"7": [apacheconf_rule12,],
	"8": [apacheconf_rule12,],
	"9": [apacheconf_rule12,],
	"@": [apacheconf_rule12,],
	"A": [apacheconf_rule12,],
	"B": [apacheconf_rule12,],
	"C": [apacheconf_rule12,],
	"D": [apacheconf_rule12,],
	"E": [apacheconf_rule12,],
	"F": [apacheconf_rule12,],
	"G": [apacheconf_rule12,],
	"H": [apacheconf_rule12,],
	"I": [apacheconf_rule12,],
	"J": [apacheconf_rule12,],
	"K": [apacheconf_rule12,],
	"L": [apacheconf_rule12,],
	"M": [apacheconf_rule12,],
	"N": [apacheconf_rule12,],
	"O": [apacheconf_rule12,],
	"P": [apacheconf_rule12,],
	"Q": [apacheconf_rule12,],
	"R": [apacheconf_rule12,],
	"S": [apacheconf_rule12,],
	"T": [apacheconf_rule12,],
	"U": [apacheconf_rule12,],
	"V": [apacheconf_rule12,],
	"W": [apacheconf_rule12,],
	"X": [apacheconf_rule12,],
	"Y": [apacheconf_rule12,],
	"Z": [apacheconf_rule12,],
	"_": [apacheconf_rule12,],
	"a": [apacheconf_rule12,],
	"b": [apacheconf_rule12,],
	"c": [apacheconf_rule12,],
	"d": [apacheconf_rule12,],
	"e": [apacheconf_rule12,],
	"f": [apacheconf_rule12,],
	"g": [apacheconf_rule12,],
	"h": [apacheconf_rule12,],
	"i": [apacheconf_rule12,],
	"j": [apacheconf_rule12,],
	"k": [apacheconf_rule12,],
	"l": [apacheconf_rule12,],
	"m": [apacheconf_rule12,],
	"n": [apacheconf_rule12,],
	"o": [apacheconf_rule12,],
	"p": [apacheconf_rule12,],
	"q": [apacheconf_rule12,],
	"r": [apacheconf_rule12,],
	"s": [apacheconf_rule12,],
	"t": [apacheconf_rule12,],
	"u": [apacheconf_rule12,],
	"v": [apacheconf_rule12,],
	"w": [apacheconf_rule12,],
	"x": [apacheconf_rule12,],
	"y": [apacheconf_rule12,],
	"z": [apacheconf_rule12,],
}

# x.rulesDictDict for apacheconf mode.
rulesDictDict = {
	"apacheconf_directive": rulesDict2,
	"apacheconf_main": rulesDict1,
	"apacheconf_vhost": rulesDict3,
}

# Import dict for apacheconf mode.
importDict = {}

