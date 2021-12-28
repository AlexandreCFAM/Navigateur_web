def add_protocol_to_url(url : str) -> str:
    if url.lower().find("http://") == -1: return "http://" + url
    else: return url
def is_there_protocol(url : str) -> bool:
    if url.lower().find("http://") == -1: return False
    else: return True