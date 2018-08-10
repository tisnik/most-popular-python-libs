#!/usr/bin/python3
# vim: set fileencoding=utf-8

# Original (slightly buggy) code:
# see https://gist.github.com/bradmontgomery/2219997


import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = ""
hostPort = 8000


class SimpleServer(BaseHTTPRequestHandler):

    def do_GET(self):
        # priprava hlavicky odpovedi
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        # odpoved serveru klientovi
        self.wfile.write("*** get ***".encode("utf-8"))

    def do_POST(self):
        print("URI: {uri}".format(uri=self.path))

        # precteni tela HTTP pozadavku
        content_length = int(self.headers['Content-Length'])
        print("content length: {len}".format(len=content_length))

        content = self.rfile.read(content_length)
        print("content value:  {content}".format(content=content))

        # priprava hlavicky odpovedi
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        # odpoved serveru klientovi
        self.wfile.write("*** post ***".encode("utf-8"))


simpleServer = HTTPServer((hostName, hostPort), SimpleServer)

try:
    simpleServer.serve_forever()
except KeyboardInterrupt:
    pass

simpleServer.server_close()
