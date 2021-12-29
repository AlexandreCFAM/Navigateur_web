import http 
import https
import log

NONE = 0
HTTP = 1
HTTPS = 2

def find_other_protocole(url : str) -> str:
    # We suppose that http and https have been already checked
    url = url.split("://")
    if len(url) == 1: return "None"
    else: return url[0] + "://"

def detect_protocol(url : str) -> int:
    global NONE, HTTP, HTTPS
    if http.is_there_protocol(url):
        log.info("Running for http request...")
        return (url, HTTP)
    elif https.is_there_protocol(url):
        log.info("Running for https request...")
        return (url, HTTPS)
    else:
        _protocol = find_other_protocole(url)
        if _protocol == "None":
            log.info("No protocol found!")
            log.info("Trying https request...")
            url = https.add_protocol_to_url(url)
            return (url, HTTPS)
        else:
            log.error(_protocol + " is not supported!")
            sys.exit(1)