#@+leo-ver=4-thin
#@+node:EKR.20040517080250.1:@thin mod_http.py
#@<< docstring >>
#@+node:ekr.20050111111238:<< docstring >>
'''A minimal http plugin for LEO, based on AsyncHttpServer.py.

Use this plugin is as follows:

1. Start Leo with the plugin enabled.  You will see a purple message that says something like:

"http serving enabled on port 8080, version 0.91"

2. Start a web browser, and enter the following url: http://localhost:8080/

You will see a a "top" level page containing one link for every open .leo file.  Start clicking :-)

You can use the browser's refresh button to update the top-level view in the browser after you have opened or closed files.

To enable this plugin:
    put this into your file
    @settings
        @page http plugin
        @bool http_active = True
        @int  port = 8080
        @string rst_http_attributename = 'rst_http_attribute'
'''
#@nonl
#@-node:ekr.20050111111238:<< docstring >>
#@nl

#@@language python
#@@tabwidth -4

# Adapted and extended from the Python Cookbook:
# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/259148

__version__ = "0.93"

#@<< imports >>
#@+node:EKR.20040517080250.3:<< imports >>
import leoGlobals as g
import leoPlugins

import asynchat
import asyncore
import cgi
import ConfigParser
import cStringIO
import exceptions
from StringIO import StringIO
import os
import posixpath
import select
import shutil
import SimpleHTTPServer
import socket
import sys
import time
import urllib
import urlparse
#@nonl
#@-node:EKR.20040517080250.3:<< imports >>
#@nl
#@<< version history >>
#@+node:ekr.20050328104558:<< version history >>
#@@killcolor

#@+at
# 
# 0.93 EKR:
#     - Added 'version history' section.
#     - Removed vestigial sections.
#     - Changed docstring to mention
#         @string rst_http_attributename = 'rst_http_attribute'
#       (Not sure if this is correct.)
#@-at
#@nonl
#@-node:ekr.20050328104558:<< version history >>
#@nl

sockets_to_close = []

#@<< config >>
#@+node:bwmulder.20050326191345:<< config >>
class config:
    http_active = False
    http_timeout = 0
    http_port = 8080
    rst2_http_attributename = 'rst_http_attribute'
#@-node:bwmulder.20050326191345:<< config >>
#@nl
#@+others
#@+node:bwmulder.20050326191345.1:onFileOpen
def onFileOpen(tag, keywords):
    c = keywords.get("new_c")

    wasactive = config.http_active
    applyConfiguration(c)

    if config.http_active and not wasactive: # Ok for unit testing:
    
        s=Server('',config.http_port,RequestHandler)
        asyncore.read = a_read
        leoPlugins.registerHandler("idle", plugin_wrapper)
        
        g.es("http serving enabled on port %s, version %s" % (config.http_port, __version__), color="purple")
#@-node:bwmulder.20050326191345.1:onFileOpen
#@+node:bwmulder.20050322132919:rst_related
#@+node:bwmulder.20050322134325:reconstruct_html_from_attrs
def reconstruct_html_from_attrs(attrs, how_much_to_ignore=0):
    """
    Given an attribute, reconstruct the html for this node.
    """
    result = []
    stack = attrs
    while stack:
        result.append(stack[0])
        stack = stack[2]
    result.reverse()
    result = result[how_much_to_ignore:]
    result.extend(attrs[3:])
    stack = attrs
    for i in range(how_much_to_ignore):
        stack = stack[2]
    while stack:
        result.append(stack[1])
        stack = stack[2]
    return result
#@nonl
#@-node:bwmulder.20050322134325:reconstruct_html_from_attrs
#@+node:bwmulder.20050322132919.2:get_http_attribute
def get_http_attribute(p):
    vnode = p.v
    if hasattr(vnode, 'unknownAttributes'):
        return vnode.unknownAttributes.get(config.rst2_http_attributename, None)
    return None

#@-node:bwmulder.20050322132919.2:get_http_attribute
#@+node:bwmulder.20050322133050:set_http_attribute
def set_http_attribute(p, value):
    vnode = p.v
    if hasattr(vnode, 'unknownAttributes'):
        vnode.unknownAttributes[config.rst2_http_attributename] = value
    else:
        vnode.unknownAttributes = {config.rst2_http_attributename: value}

#@-node:bwmulder.20050322133050:set_http_attribute
#@+node:bwmulder.20050322135114:node_reference
def node_reference(vnode):
    """
    Use by the rst2 plugin.
    """
    return leo_interface().node_reference(vnode)
#@nonl
#@-node:bwmulder.20050322135114:node_reference
#@-node:bwmulder.20050322132919:rst_related
#@+node:EKR.20040517080250.4:class delayedSocketStream
class delayedSocketStream(asyncore.dispatcher_with_send):
    #@    @+others
    #@+node:EKR.20040517080250.5:__init__
    def __init__(self,sock):
        self._map = asyncore.socket_map
        self.socket=sock
        self.socket.setblocking(0)
        self.closed=1   # compatibility with SocketServer
        self.buffer = []
    #@-node:EKR.20040517080250.5:__init__
    #@+node:EKR.20040517080250.6:write
    def write(self,data):
        self.buffer.append(data)
    #@-node:EKR.20040517080250.6:write
    #@+node:EKR.20040517080250.7:initiate_sending
    def initiate_sending(self):
        self.out_buffer = ''.join(self.buffer)
        del self.buffer
        self.set_socket(self.socket, None)
        self.socket.setblocking(0)
        self.connected = 1
        try:
            self.addr = self.socket.getpeername()
        except socket.error:
            # The addr isn't crucial
            pass
    #@-node:EKR.20040517080250.7:initiate_sending
    #@+node:EKR.20040517080250.8:handle_read
    def handle_read(self):
        pass
    #@nonl
    #@-node:EKR.20040517080250.8:handle_read
    #@+node:EKR.20040517080250.9:writable
    def writable(self):
        result = (not self.connected) or len(self.out_buffer)
        if not result:
            sockets_to_close.append(self)
        return result
    #@-node:EKR.20040517080250.9:writable
    #@-others
#@-node:EKR.20040517080250.4:class delayedSocketStream
#@+node:EKR.20040517080250.10:class nodeNotFound
class nodeNotFound(Exception):
    pass
#@nonl
#@-node:EKR.20040517080250.10:class nodeNotFound
#@+node:EKR.20040517080250.11:class escaped_StringIO
class escaped_StringIO(StringIO):
    #@    @+others
    #@+node:EKR.20040517080250.12:write_escaped
    def write_escaped(self, s):
        s = s.replace('&', "&amp;")
        s = s.replace('<', "&lt;")
        s = s.replace('>', "&gt;")
        
        # is there a more elegant way to do this?
        # Replaces blanks with &nbsp; id they are in
        # the beginning of the line.
        lines = s.split('\n')
        result = []
        blank = chr(32)
        for line in lines:
            if line.startswith(blank):
                resultchars = []
                startline = True
                for char in line:
                    if char == blank:
                        if startline:
                            resultchars.append('&nbsp;')
                        else:
                            resultchars.append(' ')
                    else:
                        startline = False
                        resultchars.append(char)
                result.append(''.join(resultchars))
            else:
                result.append(line)
        s = '\n'.join(result)
    
        s = s.replace('\n', '<br>')
        s = s.replace(chr(9), '&nbsp;&nbsp;&nbsp;&nbsp;')
        StringIO.write(self, s)
        
    #@nonl
    #@-node:EKR.20040517080250.12:write_escaped
    #@-others
#@nonl
#@-node:EKR.20040517080250.11:class escaped_StringIO
#@+node:EKR.20040517080250.20:class leo_interface
class leo_interface(object):
    #@    @+others
    #@+node:EKR.20040517080250.21:add_leo_links
    def add_leo_links(self, window, node, f):
        """
        Given a node 'node', add links to:
            The next sibling, if any.
            the next node.
            the parent.
            The children, if any.
        """
    
        # Collecting the navigational links.
        if node:
            nodename = node.headString()
            threadNext = node.threadNext()
            sibling = node.next()
            parent = node.parent()
    
            children = []
            firstChild = node.firstChild()
            if firstChild:
                child = firstChild
                while child:
                    children.append(child)
                    child = child.next()
    
            if threadNext is not None:
                self.create_leo_reference(window, threadNext,  "next", f)
            f.write("<br>")
            if sibling is not None:
                self.create_leo_reference(window, sibling, "next Sibling", f)
            f.write("<br>")
            if parent is None:
                self.create_href("/", "Top level", f)
            else:
                self.create_leo_reference(window, parent, "Up", f)
            f.write("<br>")
        else:
            # top level
            child = window.c.rootVnode()
            children = [child]
            next = child.next()
            while next:
                child = next
                children.append(child)
                next = child.next()
            nodename = window.shortFileName()
        if children:
            f.write("<h2>")
            f.write("Children of ")
            f.write_escaped(nodename)
            f.write("</h2>\n")
            f.write("<ol>\n")
            for child in children:
                f.write("<li>\n")
                self.create_leo_reference(window, child, child.headString(), f)
            f.write("</ol>\n")
    #@nonl
    #@-node:EKR.20040517080250.21:add_leo_links
    #@+node:EKR.20040517080250.22:create_href
    def create_href(self, href, text, f):
        f.write('<a href="%s">' % href)
        f.write_escaped(text)
        f.write("</a>\n")
    
    #@-node:EKR.20040517080250.22:create_href
    #@+node:bwmulder.20050319134815:create_leo_h_reference
    def create_leo_h_reference(self, window, node):
        parts = [window.shortFileName()] + self.get_leo_nameparts(node)
        href = '/' + '/'.join(parts)
        return href
    #@-node:bwmulder.20050319134815:create_leo_h_reference
    #@+node:EKR.20040517080250.23:create_leo_reference
    def create_leo_reference(self, window, node, text, f):
        """
        Create a reference to 'node' in 'window', displaying 'text'
        """
        href = self.create_leo_h_reference(window, node)
        self.create_href(href, text, f)
    #@-node:EKR.20040517080250.23:create_leo_reference
    #@+node:EKR.20040517080250.24:format_leo_node
    def format_leo_node(self, window, node):
        """
        Given a node 'node', return the contents of that node as html text.
        
        Include some navigational references too
        """
    
        if node:
            headString = node.headString()
            bodyString = node.bodyString()
            format_info = get_http_attribute(node)
        else:
            headString, bodyString = "Top level", ""
            format_info = None
        f = escaped_StringIO()
        write, write_escaped = f.write, f.write_escaped
        write("<title>")
        write_escaped(window.shortFileName() + ":" + headString)
        write("</title>\n")
        # write navigation
        self.add_leo_links(window, node, f)
        # write path
        self.write_path(node, f)
        write("<hr>\n") # horizontal rule
        # f.write('<span style="font-family: monospace;">')
        if format_info:
            html_lines = reconstruct_html_from_attrs(format_info, 3)
            for line in html_lines:
                write(line) 
        else:
            write_escaped(bodyString)
        # f.write("</span>\n")
        return f
    #@nonl
    #@-node:EKR.20040517080250.24:format_leo_node
    #@+node:EKR.20040517080250.25:get_leo_nameparts
    def get_leo_nameparts(self, node):
        """
        Given a 'node', construct a list of sibling numbers to get to that node.
        """
        result = []
        if node:
            cnode = node
            parent = cnode.parent()
            while parent:
                i = 0
                child = parent.firstChild()
                while child != cnode:
                    child = child.next()
                    i += 1
                result.append(str(i))
                cnode = parent
                parent = cnode.parent()
            i = 0
            previous = cnode.back()
            while previous:
                i += 1
                previous = previous.back()
            result.append(str(i))
            result.reverse()
        return result
    #@nonl
    #@-node:EKR.20040517080250.25:get_leo_nameparts
    #@+node:EKR.20040517080250.26:get_leo_node
    def get_leo_node(self, path):
        """
        given a path of the form:
            [<short filename>,<number1>,<number2>...<numbern>]
            identify the leo node which is in that file, and,
            from top to bottom, is the <number1> child of the topmost
            node, the <number2> child of that node, and so on.
            
            Return None if that node can not be identified that way.
        """
        # Identify the window
        for w in g.app.windowList:
            if w.shortFileName() == path[0]:
                break
        else:
            return None, None
            
        node = w.c.rootVnode()
        
        if len(path) >= 2:
            for i in range(int(path[1])):
                node = node.next()
                if node is None:
                    raise nodeNotFound
            # go to the i'th child for each path element.
            for i in path[2:]:
                node = node.nthChild(int(i))
                if node is None:
                    raise nodeNotFound
        else:
            node = None
        return w, node
    #@nonl
    #@-node:EKR.20040517080250.26:get_leo_node
    #@+node:EKR.20040517080250.27:get_leo_windowlist
    def get_leo_windowlist(self):
        """
     
        """
        f = escaped_StringIO()
        write, write_escaped = f.write, f.write_escaped
        write("<title>ROOT for LEO HTTP plugin</title>\n")
        write("<h2>Windowlist</h2>\n")
        write("<hr>\n") # horizontal rule
        write("<ul>\n")
        a = g.app # get the singleton application instance.
        windows = a.windowList # get the list of all open frames.
        for w in windows:
            write("<li>")
            shortfilename = w.shortFileName()
            write('<a href="%s">' % shortfilename)
            write("file name: %s" % shortfilename)
            write("</a>\n")
        write("</ul>\n")
        write("<hr>\n")
        return f
    #@-node:EKR.20040517080250.27:get_leo_windowlist
    #@+node:bwmulder.20050319135316:node_reference
    def node_reference(self, vnode):
        """
        Given a position p, return the name of the node.
        """
        # 1. Find the root
        root = vnode
        parent = root.parent()
        while parent:
            root = parent
            parent = root.parent()
        
        while root.v._back:
            root.moveToBack()
        
        # 2. Return the window
        window = [w for w in g.app.windowList if w.c.rootVnode().v == root.v][0]
        
        result = self.create_leo_h_reference(window, vnode)
        return result
    #@-node:bwmulder.20050319135316:node_reference
    #@+node:bwmulder.20050322224921:send_head
    def send_head(self):
        """Common code for GET and HEAD commands.
    
         This sends the response code and MIME headers.
    
         Return value is either a file object (which has to be copied
         to the outputfile by the caller unless the command was HEAD,
         and must be closed by the caller under all circumstances), or
         None, in which case the caller has nothing further to do.
    
         """
        try:
            path = self.split_leo_path(self.path)
            if path == '/':
                 f = self.get_leo_windowlist()
            else:
                try:
                    window, node = self.get_leo_node(path)
                    if window is None:
                        self.send_error(404, "File not found")
                        return None
                    f = self.format_leo_node(window, node)
                except nodeNotFound:
                    self.send_error(404, "Node not found")
                    return None
            length = f.tell()
            f.seek(0)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.send_header("Content-Length", str(length))
            self.end_headers()
            return f
        except:
            import traceback
            traceback.print_exc()
            raise
    
    #@-node:bwmulder.20050322224921:send_head
    #@+node:EKR.20040517080250.30:split_leo_path
    def split_leo_path(self, path):
        """
        A leo node is represented by a string of the form:
            <number1>_<number2>...<numbern>,
        where <number> is the number of sibling of the node.
        """
        if path == '/':
            return '/'
        if path.startswith("/"):
            path = path[1:]
        return path.split('/')
    #@nonl
    #@-node:EKR.20040517080250.30:split_leo_path
    #@+node:EKR.20040517080250.28:write_path
    def write_path(self, node, f):
        result = []
        while node:
            result.append(node.headString())
            node = node.parent()
        result.reverse()
        if result:
            result2 = result[:-1]
            if result2:
                result2 = ' / '.join(result2)
                f.write("<br>\n")
                f.write_escaped(result2)
                f.write("<br>\n")
            f.write("<h2>")
            f.write_escaped(result[-1])
            f.write("</h2>\n")
    #@nonl
    #@-node:EKR.20040517080250.28:write_path
    #@-others
#@nonl
#@-node:EKR.20040517080250.20:class leo_interface
#@+node:EKR.20040517080250.13:class RequestHandler
class RequestHandler(
    leo_interface
    ,asynchat.async_chat,
    SimpleHTTPServer.SimpleHTTPRequestHandler
    ):
    #@    @+others
    #@+node:EKR.20040517080250.14:__init__
    def __init__(self,conn,addr,server):
        asynchat.async_chat.__init__(self,conn)
        self.client_address=addr
        self.connection=conn
        self.server=server
        self.wfile = delayedSocketStream(self.socket)
        # sets the terminator : when it is received, this means that the
        # http request is complete ; control will be passed to
        # self.found_terminator
        self.set_terminator ('\r\n\r\n')
        self.buffer=cStringIO.StringIO()
        self.found_terminator=self.handle_request_line
    #@-node:EKR.20040517080250.14:__init__
    #@+node:EKR.20040517080250.15:copyfile
    def copyfile(self, source, outputfile):
        """Copy all data between two file objects.
    
        The SOURCE argument is a file object open for reading
        (or anything with a read() method) and the DESTINATION
        argument is a file object open for writing (or
        anything with a write() method).
    
        The only reason for overriding this would be to change
        the block size or perhaps to replace newlines by CRLF
        -- note however that this the default server uses this
        to copy binary data as well.
         """
        shutil.copyfileobj(source, outputfile, length=255)
    #@-node:EKR.20040517080250.15:copyfile
    #@+node:EKR.20040517080250.16:log_message
    def log_message(self, format, *args):
        """Log an arbitrary message.
    
         This is used by all other logging functions.  Override
         it if you have specific logging wishes.
    
         The first argument, FORMAT, is a format string for the
         message to be logged.  If the format string contains
         any % escapes requiring parameters, they should be
         specified as subsequent arguments (it's just like
         printf!).
    
         The client host and current date/time are prefixed to
         every message.
    
         """
        message = "%s - - [%s] %s\n" % (
            self.address_string(),
            self.log_date_time_string(),
            format%args)
        g.es(message)
    #@-node:EKR.20040517080250.16:log_message
    #@+node:EKR.20040517080250.17:collect_incoming_data
    def collect_incoming_data(self,data):
        """Collects the data arriving on the connexion"""
        self.buffer.write(data)
    #@-node:EKR.20040517080250.17:collect_incoming_data
    #@+node:EKR.20040517080250.18:prepare_POST
    def prepare_POST(self):
        """Prepare to read the request body"""
        bytesToRead = int(self.headers.getheader('content-length'))
        # set terminator to length (will read bytesToRead bytes)
        self.set_terminator(bytesToRead)
        self.buffer=cStringIO.StringIO()
        # control will be passed to a new found_terminator
        self.found_terminator=self.handle_post_data
    #@-node:EKR.20040517080250.18:prepare_POST
    #@+node:EKR.20040517080250.19:handle_post_data
    def handle_post_data(self):
        """Called when a POST request body has been read"""
        self.rfile=cStringIO.StringIO(self.buffer.getvalue())
        self.do_POST()
        self.finish()
    #@-node:EKR.20040517080250.19:handle_post_data
    #@+node:EKR.20040517080250.31:do_GET
    def do_GET(self):
        """Begins serving a GET request"""
        # nothing more to do before handle_data()
        self.handle_data()
    #@-node:EKR.20040517080250.31:do_GET
    #@+node:EKR.20040517080250.32:do_POST
    def do_POST(self):
        """Begins serving a POST request. The request data must be readable
         on a file-like object called self.rfile"""
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        length = int(self.headers.getheader('content-length'))
        if ctype == 'multipart/form-data':
            query=cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            qs=self.rfile.read(length)
            query=cgi.parse_qs(qs, keep_blank_values=1)
        else:
            query = ''                   # Unknown content-type
        # some browsers send 2 more bytes...
        [ready_to_read,x,y]=select.select([self.connection],[],[],0)
        if ready_to_read:
            self.rfile.read(2)
    
        self.QUERY.update(self.query(query))
        self.handle_data()
    #@-node:EKR.20040517080250.32:do_POST
    #@+node:EKR.20040517080250.33:query
    def query(self,parsedQuery):
        """Returns the QUERY dictionary, similar to the result of cgi.parse_qs
         except that :
         - if the key ends with [], returns the value (a Python list)
         - if not, returns a string, empty if the list is empty, or with the
         first value in the list"""
        res={}
        for item in parsedQuery.keys():
            value=parsedQuery[item] # a Python list
            if item.endswith("[]"):
                    res[item[:-2]]=value
            else:
                    if len(value)==0:
                        res[item]=''
                    else:
                        res[item]=value[0]
        return res
    #@-node:EKR.20040517080250.33:query
    #@+node:EKR.20040517080250.34:handle_data
    def handle_data(self):
        """Class to override"""
        f = self.send_head()
        if f:
            self.copyfile(f, self.wfile)
    #@-node:EKR.20040517080250.34:handle_data
    #@+node:EKR.20040517080250.35:handle_request_line
    def handle_request_line(self):
        """Called when the http request line and headers have been received"""
    
        # prepare attributes needed in parse_request()
        self.rfile=cStringIO.StringIO(self.buffer.getvalue())
        self.raw_requestline=self.rfile.readline()
        self.parse_request()
    
        # if there is a Query String, decodes it in a QUERY dictionary
        self.path_without_qs,self.qs=self.path,''
        if self.path.find('?')>=0:
            self.qs=self.path[self.path.find('?')+1:]
            self.path_without_qs=self.path[:self.path.find('?')]
        self.QUERY=self.query(cgi.parse_qs(self.qs,1))
    
        if self.command in ['GET','HEAD']:
            # if method is GET or HEAD, call do_GET or do_HEAD and finish
            method="do_"+self.command
            if hasattr(self,method):
                    getattr(self,method)()
                    self.finish()
        elif self.command=="POST":
            # if method is POST, call prepare_POST, don't finish before
            self.prepare_POST()
        else:
            self.send_error(501, "Unsupported method (%s)" %self.command)
    #@-node:EKR.20040517080250.35:handle_request_line
    #@+node:EKR.20040517080250.36:finish
    def finish(self):
        """Reset terminator (required after POST method), then close"""
        self.set_terminator ('\r\n\r\n')
        self.wfile.initiate_sending()
        # self.close()
    #@nonl
    #@-node:EKR.20040517080250.36:finish
    #@-others
#@-node:EKR.20040517080250.13:class RequestHandler
#@+node:EKR.20040517080250.37:class Server
class Server(asyncore.dispatcher):
    """Copied from http_server in medusa"""
    #@    @+others
    #@+node:EKR.20040517080250.38:__init__
    def __init__ (self, ip, port,handler):
        self.ip = ip
        self.port = port
        self.handler=handler
        asyncore.dispatcher.__init__ (self)
        self.create_socket (socket.AF_INET, socket.SOCK_STREAM)
    
        self.set_reuse_addr()
        self.bind ((ip, port))
    
        # lower this to 5 if your OS complains
        self.listen (1024)
    #@-node:EKR.20040517080250.38:__init__
    #@+node:EKR.20040517080250.39:handle_accept
    def handle_accept (self):
        try:
            conn, addr = self.accept()
        except socket.error:
            self.log_info ('warning: server accept() threw an exception', 'warning')
            return
        except TypeError:
            self.log_info ('warning: server accept() threw EWOULDBLOCK', 'warning')
            return
        # creates an instance of the handler class to handle the request/response
        # on the incoming connexion
        self.handler(conn,addr,self)
    #@-node:EKR.20040517080250.39:handle_accept
    #@-others
#@-node:EKR.20040517080250.37:class Server
#@+node:EKR.20040517080250.40:poll
def poll(timeout=0.0):
    global sockets_to_close
    map = asyncore.socket_map
    if not map:
        return False
    while 1:
        r = []; w = []; e = []
        for fd, obj in map.items():
            if obj.readable():
                r.append(fd)
            if obj.writable():
                w.append(fd)
        if not sockets_to_close: # Set by writeable()
            break
        for s in sockets_to_close:
            s.close()
        sockets_to_close = []
    if [] == r == w == e:
        time.sleep(timeout)
    else:
        #@        << try r, w, e = select.select >>
        #@+node:EKR.20040517080250.41:<< try r, w, e = select.select >>
        try:
            r, w, e = select.select(r, w, e, timeout)
        except select.error, err:
            if err[0] != EINTR:
                raise
            else:
                return False # EKR: added return value.
        #@nonl
        #@-node:EKR.20040517080250.41:<< try r, w, e = select.select >>
        #@nl
    for fd in r:
        #@        << asyncore.read(map.get(fd)) >>
        #@+node:EKR.20040517080250.42:<< asyncore.read(map.get(fd)) >>
        obj = map.get(fd)
        if obj is not None:
            asyncore.read(obj)
        #@nonl
        #@-node:EKR.20040517080250.42:<< asyncore.read(map.get(fd)) >>
        #@nl
    for fd in w:
        #@        << asyncore.write(map.get(fd)) >>
        #@+node:EKR.20040517080250.43:<< asyncore.write(map.get(fd)) >>
         obj = map.get(fd)
         if obj is not None:
            asyncore.write(obj)
        #@-node:EKR.20040517080250.43:<< asyncore.write(map.get(fd)) >>
        #@nl
    return len(r) > 0 or len(w) > 0
#@-node:EKR.20040517080250.40:poll
#@+node:EKR.20040517080250.44:loop
def loop(timeout=5.0, use_poll=0, map=None):
    """
    Override the loop function of asynchore.
    We poll only until there is not read or
    write request pending.
    """
    return poll(timeout)
#@nonl
#@-node:EKR.20040517080250.44:loop
#@+node:EKR.20040517080250.45:plugin_wrapper
def plugin_wrapper(tag, keywords):
    
    if g.app.killed: return

    first = True
    while loop(config.http_timeout):
        pass
#@nonl
#@-node:EKR.20040517080250.45:plugin_wrapper
#@+node:EKR.20040517080250.46:asynchore_overrides
#@+node:EKR.20040517080250.47:a_read
def a_read(obj):
    try:
        obj.handle_read_event()
    except asyncore.ExitNow:
        raise
    except:
        obj.handle_error()


#@-node:EKR.20040517080250.47:a_read
#@-node:EKR.20040517080250.46:asynchore_overrides
#@+node:EKR.20040517080250.48:applyConfiguration
def applyConfiguration(c):

    """Called when the user opens a new file."""

    newtimeout = c.config.getInt("http_timeout")
    if newtimeout is not None:
        config.http_timeout = newtimeout  / 1000.0
    newport = c.config.getInt("http_port") 
    if newport:
        config.port = newport
    newactive = c.config.getBool("http_active")
    if newactive is not None:
        config.http_active = newactive
    new_rst2_http_attributename = c.config.getString("rst2_http_attributename")
    if new_rst2_http_attributename:
        config.rst2_http_attributename = new_rst2_http_attributename
#@nonl
#@-node:EKR.20040517080250.48:applyConfiguration
#@-others
leoPlugins.registerHandler("open2", onFileOpen)
    
#@-node:EKR.20040517080250.1:@thin mod_http.py
#@-leo
