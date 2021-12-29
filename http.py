def add_protocol_to_url(url : str) -> str:
    if url.lower().find("http://") == -1: return "http://" + url
    else: return url
def is_there_protocol(url : str) -> bool:
    if url.lower().find("http://") == -1: return False
    else: return True
def get_file_you_want_to_see_from_url(url : str) -> str:
    # First case : http://www.python.org
    # Remove the protocol and see if there is a /
    url = url.replace("http://", "")
    if url.find('/') == -1: return "index.html"
    
    # Second case : http://www.python.org/
    # Remove the protocol and see if the last one is /
    url = list(url)
    if url[len(url) - 1] == '/': return "index.html"
    else: url = "".join(url)
    
    # Third case : http://www.python.org/tes/tes/tes/t/d/file.html
    # Remove http:// and then delete the domain server with the first /
    file = url.split('/')
    del file[0]
    file = '/'.join(file)
    return file
def get_domain(url : str) -> str:
    # Remove http://
    domain = url.replace("http://", "")
    
    # First case : www.domain.org/file/i/want/to/see/file.html
    # Just get the domain server before the first /
    if domain.find('/') != -1: return domain.split("/")[0]
    
    # Else we've got the domain name
    return domain