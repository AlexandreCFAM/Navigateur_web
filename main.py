import sys
import socket
import http
import https
import log
import protocol
from protocol import NONE, HTTP, HTTPS
import server

class NAVIGATOR(object):
    global NONE, HTTP, HTTPS
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.url = ""
        self.domain = ""
        self.header = ""
        self.file = ""
        self.port = 0
        self.protocol = NONE
    def run(self, url : str) -> None:
        (self.url, self.protocol) = protocol.detect_protocol(url)
        if self.protocol == HTTPS: self.file = https.get_file_you_want_to_see_from_url(url)
        elif self.protocol == HTTP: self.file = http.get_file_you_want_to_see_from_url(url)
        else:
            log.error(self.protocol + " is not a valid protocol!")
            sys.exit(1)
        log.info("File you want to see on the server : " + self.file + "...")
        self.domain = http.get_domain(self.url)
        log.info("Generating header...")
        self.header = server.generate_basic_header(self.domain, self.file)
navigator = NAVIGATOR()
navigator.run("http://laphilosophiedevie.serveblog.net")