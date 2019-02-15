import get_requests, parser
import sys
import argparse

parser = argparse.ArgumentParser(description='Check if selected website is based on wordpress or not.')
parser.add_argument('integers', metavar='URL', type=str, nargs='+',
                   help='Check if selected website is based on wordpress or not')
parser.add_argument()


args = parser.parse_args()
print(args.accumulate(args.integers))


#def app_run():
    #url = get_requests.get_page_requests(sys.argv[1])
    #print (parser.parse_data(url))
