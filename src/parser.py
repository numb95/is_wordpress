from bs4 import BeautifulSoup

def parse_data(req):
    soup = BeautifulSoup(req, 'html.parser')
    for tags in soup.find_all("meta"):
        if (tags.get("name", None) == 'generator'):
            return (tags.get("content", None))