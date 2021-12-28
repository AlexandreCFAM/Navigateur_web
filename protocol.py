NONE = 0
HTTP = 1
HTTPS = 2

def find_other_protocole(url : str) -> str:
    # We suppose that http and https have been already checked
    url = url.split("://")
    if len(url) == 1: return "None"
    else: return url[0] + "://"