import sys
import socket
import http
import https
import log
import protocol
from protocol import NONE, HTTP, HTTPS

class NAVIGATOR(object):
    global NONE, HTTP, HTTPS
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.url = ""
        self.protocol = NONE
    def run(self, url : str) -> None:
        if http.is_there_protocol(url):
            log.info("Running for http request...")
            self.protocol = HTTP
        elif https.is_there_protocol(url):
            log.info("Running for https request...")
            self.protocol = HTTPS
        else:
            _protocol = protocol.find_other_protocole(url)
            if _protocol == "None":
                log.info("No protocol found!")
                log.info("Trying https request...")
                url = https.add_protocol_to_url(url)
                self.protocol = HTTPS
            else:
                log.error(_protocol + " is not supported!")
                sys.exit(1)
        file_on_server = https.get_file_you_want_to_see_from_url(url)
        log.info("File you want to see on the server : " + file_on_server + "...")
navigator = NAVIGATOR()
navigator.run("https://www.python.org/my/file/on/this/server.html")