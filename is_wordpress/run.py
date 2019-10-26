from . import get_requests, parser
import sys
import argparse
import re
import requests

def run():
request = requests.get(args.url)
if request.status_code == 200:
    print('Web site exists')
    argparser = argparse.ArgumentParser(description='Check if selected website is based on wordpress or not.It also show the wordpress version.')
    argparser.add_argument("url", help='URL to check the website.')
    args = argparser.parse_args()
    website = get_requests.get_page_requests(args.url)
    if parser.parse_data(website) == None:
        return "It's not wordpress or cannot identified"
    if (re.findall('^WordPress.*', parser.parse_data(website))):
        return parser.parse_data(website)
else:
    print('Web site does not exist')
