#@+leo-ver=4
#@+node:@file server.py
import SocketServer
#import SimpleHTTPServer
import CGIHTTPServer
import urllib

#import os
#path = g.os_path_abspath(g.os_path_normpath(g.os_path_join(g.app.loadDir,'..','test','cgi-bin')))
# os.chdir(path)

port = 8080
Handler = CGIHTTPServer.CGIHTTPRequestHandler
s = SocketServer.TCPServer(("", port), Handler)
s.server_name = '127.0.0.1'
s.server_port = 8080

print "server.py: serving at port", port
s.serve_forever()
#@nonl
#@-node:@file server.py
#@-leo
