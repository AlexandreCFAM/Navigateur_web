def add_protocol_to_url(url : str) -> str:
    if url.lower().find("https://") == -1: return "https://" + url
    else: return url
def is_there_protocol(url : str) -> bool:
    if url.lower().find("https://") == -1: return False
    else: return True
def get_file_you_want_to_see_from_url(url : str) -> str:
    # First case : https://www.python.org
    # Remove the protocol and see if there is a /
    url = url.replace("https://", "")
    if url.find('/') == -1: return "index.html"
    
    # Second case : https://www.python.org/
    # Remove the protocol and see if the last one is /
    url = list(url)
    if url[len(url) - 1] == '/': return "index.html"
    else: url = "".join(url)
    
    # Third case : https://www.python.org/tes/tes/tes/t/d/file.html
    # Remove https:// and then delete the domain server with the first /
    file = url.split('/')
    del file[0]
    file = '/'.join(file)
    return file
    