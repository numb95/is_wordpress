import requests
def get_page_requests(url):
    if (url.startswith('http')):
        pass
    else:
        url = 'http://'+url
    page_code = requests.get(url)
    return page_code.text