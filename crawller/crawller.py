#!/usr/bin/env python3
import requests
import optparse
import sys
def request(url):
    try:
       return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass
def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-u", "--url", dest="url", help="Target url for getting subdomain")
    (options, arguments) = parser.parse_args()
    if not options.url:
        print("[-]Please enetr a url or use '-h' or '--h' for info")
        sys.exit()
    return options
def link(url):
    print("[+]please wait searching subdomains[+]")    
    with open("wordlist/Subdomain.txt", "r") as file:
        sub_domains = file.readlines()
        for line in sub_domains:
            word = line.strip()
            test_url = str(word)+str(".")+str(url)
            responce = request(test_url)
            if responce:
                print("[+]Find a subdomain ---->" + test_url)
options = get_argument()
link(options.url)

