from . import get_requests, parser
import sys
import argparse
import re
def run():
    argparser = argparse.ArgumentParser(description='Check if selected website is based on wordpress or not.It also show the wordpress version.')
    argparser.add_argument("url", help='URL to check the website.')
    args = argparser.parse_args()
    website = get_requests.get_page_requests(args.url)
    if parser.parse_data(website) == None:
        return "It's now wordpress or cannot identified"
    if (re.findall('^WordPress.*', parser.parse_data(website))):
        return parser.parse_data(website)
