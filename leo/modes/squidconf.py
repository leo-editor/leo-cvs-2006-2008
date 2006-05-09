# Leo colorizer control file for squidconf mode.
# This file is in the public domain.

# Properties for squidconf mode.
properties = {
	"lineComment": "#",
}

# Keywords dict for squidconf_main ruleset.
squidconf_main_keywords_dict = {
	"acl": "keyword1",
	"allow": "literal2",
	"always_direct": "keyword1",
	"announce_file": "keyword1",
	"announce_host": "keyword1",
	"announce_period": "keyword1",
	"announce_port": "keyword1",
	"append_domain": "keyword1",
	"as_whois_server": "keyword1",
	"auth_param": "keyword1",
	"authenticate_cache_garbage_interval": "keyword1",
	"authenticate_ip_ttl": "keyword1",
	"authenticate_ttl": "keyword1",
	"broken_posts": "keyword1",
	"buffered_logs": "keyword1",
	"cache_access_log": "keyword1",
	"cache_dir": "keyword1",
	"cache_dns_program": "keyword1",
	"cache_effective_group": "keyword1",
	"cache_effective_user": "keyword1",
	"cache_log": "keyword1",
	"cache_mem": "keyword1",
	"cache_mgr": "keyword1",
	"cache_peer": "keyword1",
	"cache_peer_access": "keyword1",
	"cache_peer_domain": "keyword1",
	"cache_replacement_policy": "keyword1",
	"cache_store_log": "keyword1",
	"cache_swap_high": "keyword1",
	"cache_swap_log": "keyword1",
	"cache_swap_low": "keyword1",
	"cachemgr_passwd": "keyword1",
	"chroot": "keyword1",
	"client_db": "keyword1",
	"client_lifetime": "keyword1",
	"client_netmask": "keyword1",
	"client_persistent_connections": "keyword1",
	"connect_timeout": "keyword1",
	"coredump_dir": "keyword1",
	"dead_peer_timeout": "keyword1",
	"debug_options": "keyword1",
	"delay_access": "keyword1",
	"delay_class": "keyword1",
	"delay_initial_bucket_level": "keyword1",
	"delay_parameters": "keyword1",
	"delay_pools": "keyword1",
	"deny": "literal2",
	"deny_info": "keyword1",
	"digest_bits_per_entry": "keyword1",
	"digest_generation": "keyword1",
	"digest_rebuild_chunk_percentage": "keyword1",
	"digest_rebuild_period": "keyword1",
	"digest_rewrite_period": "keyword1",
	"digest_swapout_chunk_size": "keyword1",
	"diskd_program": "keyword1",
	"dns_children": "keyword1",
	"dns_defnames": "keyword1",
	"dns_nameservers": "keyword1",
	"dns_retransmit_interval": "keyword1",
	"dns_testnames": "keyword1",
	"dns_timeout": "keyword1",
	"dst": "keyword2",
	"emulate_httpd_log": "keyword1",
	"err_html_text": "keyword1",
	"error_directory": "keyword1",
	"extension_methods": "keyword1",
	"external_acl_type": "keyword1",
	"forward_log": "keyword1",
	"forwarded_for": "keyword1",
	"fqdncache_size": "keyword1",
	"ftp_list_width": "keyword1",
	"ftp_passive": "keyword1",
	"ftp_sanitycheck": "keyword1",
	"ftp_user": "keyword1",
	"half_closed_clients": "keyword1",
	"header_access": "keyword1",
	"header_replace": "keyword1",
	"hierarchy_stoplist": "keyword1",
	"high_memory_warning": "keyword1",
	"high_page_fault_warning": "keyword1",
	"high_response_time_warning": "keyword1",
	"hostname_aliases": "keyword1",
	"hosts_file": "keyword1",
	"htcp_port": "keyword1",
	"http_access": "keyword1",
	"http_port": "keyword1",
	"http_reply_access": "keyword1",
	"httpd_accel_host": "keyword1",
	"httpd_accel_port": "keyword1",
	"httpd_accel_single_host": "keyword1",
	"httpd_accel_uses_host_header": "keyword1",
	"httpd_accel_with_proxy": "keyword1",
	"https_port": "keyword1",
	"icon_directory": "keyword1",
	"icp_access": "keyword1",
	"icp_hit_stale": "keyword1",
	"icp_port": "keyword1",
	"icp_query_timeout": "keyword1",
	"ident_lookup_access": "keyword1",
	"ident_timeout": "keyword1",
	"ie_refresh": "keyword1",
	"ignore_unknown_nameservers": "keyword1",
	"incoming_dns_average": "keyword1",
	"incoming_http_average": "keyword1",
	"incoming_icp_average": "keyword1",
	"ipcache_high": "keyword1",
	"ipcache_low": "keyword1",
	"ipcache_size": "keyword1",
	"log_fqdn": "keyword1",
	"log_icp_queries": "keyword1",
	"log_ip_on_direct": "keyword1",
	"log_mime_hdrs": "keyword1",
	"logfile_rotate": "keyword1",
	"max_open_disk_fds": "keyword1",
	"maximum_icp_query_timeout": "keyword1",
	"maximum_object_size": "keyword1",
	"maximum_object_size_in_memory": "keyword1",
	"maximum_single_addr_tries": "keyword1",
	"mcast_groups": "keyword1",
	"mcast_icp_query_timeout": "keyword1",
	"mcast_miss_addr": "keyword1",
	"mcast_miss_encode_key": "keyword1",
	"mcast_miss_port": "keyword1",
	"mcast_miss_ttl": "keyword1",
	"memory_pools": "keyword1",
	"memory_pools_limit": "keyword1",
	"memory_replacement_policy": "keyword1",
	"method": "keyword2",
	"mime_table": "keyword1",
	"min_dns_poll_cnt": "keyword1",
	"min_http_poll_cnt": "keyword1",
	"min_icp_poll_cnt": "keyword1",
	"minimum_direct_hops": "keyword1",
	"minimum_direct_rtt": "keyword1",
	"minimum_object_size": "keyword1",
	"miss_access": "keyword1",
	"negative_dns_ttl": "keyword1",
	"negative_ttl": "keyword1",
	"neighbor_type_domain": "keyword1",
	"netdb_high": "keyword1",
	"netdb_low": "keyword1",
	"netdb_ping_period": "keyword1",
	"never_direct": "keyword1",
	"no_cache": "keyword1",
	"nonhierarchical_direct": "keyword1",
	"off": "literal2",
	"offline_mode": "keyword1",
	"on": "literal2",
	"pconn_timeout": "keyword1",
	"peer_connect_timeout": "keyword1",
	"persistent_request_timeout": "keyword1",
	"pid_filename": "keyword1",
	"pinger_program": "keyword1",
	"pipeline_prefetch": "keyword1",
	"port": "keyword2",
	"positive_dns_ttl": "keyword1",
	"prefer_direct": "keyword1",
	"proxy_auth": "keyword2",
	"query_icmp": "keyword1",
	"quick_abort_max": "keyword1",
	"quick_abort_min": "keyword1",
	"quick_abort_pct": "keyword1",
	"range_offset_limit": "keyword1",
	"read_timeout": "keyword1",
	"redirect_children": "keyword1",
	"redirect_program": "keyword1",
	"redirect_rewrites_host_header": "keyword1",
	"redirector_access": "keyword1",
	"redirector_bypass": "keyword1",
	"referer_log": "keyword1",
	"refresh_pattern": "keyword1",
	"reload_into_ims": "keyword1",
	"reply_body_max_size": "keyword1",
	"request_body_max_size": "keyword1",
	"request_entities": "keyword1",
	"request_header_max_size": "keyword1",
	"request_timeout": "keyword1",
	"server_persistent_connections": "keyword1",
	"shutdown_lifetime": "keyword1",
	"sleep_after_fork": "keyword1",
	"snmp_access": "keyword1",
	"snmp_incoming_address": "keyword1",
	"snmp_outgoing_address": "keyword1",
	"snmp_port": "keyword1",
	"src": "keyword2",
	"ssl_unclean_shutdown": "keyword1",
	"store_avg_object_size": "keyword1",
	"store_dir_select_algorithm": "keyword1",
	"store_objects_per_bucket": "keyword1",
	"strip_query_terms": "keyword1",
	"tcp_outgoing_address": "keyword1",
	"tcp_outgoing_tos": "keyword1",
	"tcp_recv_bufsize": "keyword1",
	"test_reachability": "keyword1",
	"udp_incoming_address": "keyword1",
	"udp_outgoing_address": "keyword1",
	"unique_hostname": "keyword1",
	"unlinkd_program": "keyword1",
	"uri_whitespace": "keyword1",
	"useragent_log": "keyword1",
	"vary_ignore_expire": "keyword1",
	"visible_hostname": "keyword1",
	"wais_relay_host": "keyword1",
	"wais_relay_port": "keyword1",
	"wccp_incoming_address": "keyword1",
	"wccp_outgoing_address": "keyword1",
	"wccp_router": "keyword1",
	"wccp_version": "keyword1",
}

# Dictionary of keywords dictionaries for squidconf mode.
keywordsDictDict = {
	"squidconf_main": squidconf_main_keywords_dict,
}

# Rules for squidconf_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for main ruleset.
rulesDict1 = {
	"#": [rule0,],
	"0": [rule1,],
	"1": [rule1,],
	"2": [rule1,],
	"3": [rule1,],
	"4": [rule1,],
	"5": [rule1,],
	"6": [rule1,],
	"7": [rule1,],
	"8": [rule1,],
	"9": [rule1,],
	"@": [rule1,],
	"A": [rule1,],
	"B": [rule1,],
	"C": [rule1,],
	"D": [rule1,],
	"E": [rule1,],
	"F": [rule1,],
	"G": [rule1,],
	"H": [rule1,],
	"I": [rule1,],
	"J": [rule1,],
	"K": [rule1,],
	"L": [rule1,],
	"M": [rule1,],
	"N": [rule1,],
	"O": [rule1,],
	"P": [rule1,],
	"Q": [rule1,],
	"R": [rule1,],
	"S": [rule1,],
	"T": [rule1,],
	"U": [rule1,],
	"V": [rule1,],
	"W": [rule1,],
	"X": [rule1,],
	"Y": [rule1,],
	"Z": [rule1,],
	"_": [rule1,],
	"a": [rule1,],
	"b": [rule1,],
	"c": [rule1,],
	"d": [rule1,],
	"e": [rule1,],
	"f": [rule1,],
	"g": [rule1,],
	"h": [rule1,],
	"i": [rule1,],
	"j": [rule1,],
	"k": [rule1,],
	"l": [rule1,],
	"m": [rule1,],
	"n": [rule1,],
	"o": [rule1,],
	"p": [rule1,],
	"q": [rule1,],
	"r": [rule1,],
	"s": [rule1,],
	"t": [rule1,],
	"u": [rule1,],
	"v": [rule1,],
	"w": [rule1,],
	"x": [rule1,],
	"y": [rule1,],
	"z": [rule1,],
}

# x.rulesDictDict for squidconf mode.
rulesDictDict = {
	"squidconf_main": rulesDict1,
}

# Import dict for squidconf mode.
importDict = {}

