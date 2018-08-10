#!/usr/bin/python3
# vim: set fileencoding=utf-8

# Original (slightly buggy) code:
# see https://gist.github.com/bradmontgomery/2219997


import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = ""
hostPort = 8000


class SimpleServer(BaseHTTPRequestHandler):

    def print_uri(self):
        print("URI: {uri}".format(uri=self.path))

    def send_headers(self):
        # priprava hlavicky odpovedi
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def print_request_content(self):
        # precteni tela HTTP pozadavku
        print(self.headers)
        if "Content-Length" in self.headers:
            content_length = int(self.headers['Content-Length'])
            print("content length: {len}".format(len=content_length))

            content = self.rfile.read(content_length)
            print("content value:  {content}".format(content=content))

    def do_GET(self):
        self.print_uri()
        self.print_request_content()

        # odpoved serveru klientovi
        self.send_headers()
        self.wfile.write("*** get ***".encode("utf-8"))

    def do_POST(self):
        self.print_uri()
        self.print_request_content()

        # odpoved serveru klientovi
        self.send_headers()
        self.wfile.write("*** post ***".encode("utf-8"))


simpleServer = HTTPServer((hostName, hostPort), SimpleServer)

try:
    simpleServer.serve_forever()
except KeyboardInterrupt:
    pass

simpleServer.server_close()
