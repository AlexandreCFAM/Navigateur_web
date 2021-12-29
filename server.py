def generate_basic_header(domain : str, file_on_server : str) -> str:
    header = "GET " + file_on_server + " HTTP/1.1\r\n"
    header += "Host: " + domain + "\r\n"
    header += "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0\r\n" # from firefox
    header += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\n"
    header += "Accept-Language: en-US,en;q=0.5\r\n"
    header += "Accept-Encoding: gzip, deflate\r\n"
    header += "Connection: keep-alive\r\n"
    header += "Upgrade-Insecure-Requests: 1\r\n"
    header += "Cache-Control: max-age=0\r\n"
    header += "\r\n"
    return header