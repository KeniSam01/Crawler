# -*- coding: UTF-8 -*-

import re
import requests
import subprocess
import argparse
import time
import requesocks

from datetime import datetime


def banner():
    time.sleep(1)
    print '''
                                                  ,,                    
  .g8"""bgd                                     `7MM                    
.dP'     `M                                       MM                    
dM'       ` `7Mb,od8  ,6"Yb.  `7M'    ,A    `MF'  MM   .gP"Ya  `7Mb,od8 
MM            MM' "' 8)   MM    VA   ,VAA   ,V    MM  ,M'   Yb   MM' "' 
MM.           MM      ,pm9MM     VA ,V  VA ,V     MM  8M""""""   MM     
`Mb.     ,'   MM     8M   MM      VVV    VVV      MM  YM.    ,   MM     
  `"bmmmd'  .JMML.   `Moo9^Yo.     W      W     .JMML. `Mbmmd' .JMML.   '''"\n"


def while_true():
    while True:
        url = site_crawled[0]

        try:
            req = requests.get(url, headers=header)
            if args.tor == "yes":
                req = requesocks.session()
                req.proxies = {'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'}
                req = req.get(url, headers=header)

        except:
            site_crawled.remove(url)
            crawled.add(url)
            continue

        html = req.text

        links = re.findall(r'<a href="?\'?(https?:\/\/[^"\'>]*)', html)
        print hour(), "[INFO] Listening pages:", url
        time.sleep(0.2)

        site_crawled.remove(url)

        crawled.add(url)

        for link in links:
            if link not in crawled and link not in site_crawled:
                site_crawled.append(link)


def clear():
    subprocess.call("clear", shell=True)


def hour():
    now = datetime.now()
    return "["+str(now.hour) + ":" + str(now.minute)+"]"


parser = argparse.ArgumentParser()
parser.add_argument("-u", dest="url", help="Link to site Crawling", nargs=1)
parser.add_argument("--tor", dest="tor", help="Use the tool inside the TOR network (yes/no)", default="no")
args = parser.parse_args()

site = args.url[0]

if not "http://" in site:
    url_correct = "http://"+site
elif not "https://" in site:
    url_correct = "https://"+site


site_crawled = [url_correct]
crawled = set()
header = {
    'user-agent': 'Googlebot'
                  'Mozilla/5.0 (Windows NT 6.1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/56.0.2924.87 '
                  'Safari/537.36'
         }

clear()

try:
    banner()
    if args.tor == "yes":
        time.sleep(2)
        print hour(), "[INFO] The tool is starting on network the Tor"
    else:
        time.sleep(2)
        print hour(), "[INFO] The tool is starting"
    time.sleep(1)
    print hour(), "[INFO] Process The Crawler Start:\n"

    while_true()

except KeyboardInterrupt:
    print "\n", hour(), "[INFO] User Finished Process"
    exit()
