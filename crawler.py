import re,requests,subprocess,argparse,time,requesocks
from datetime import datetime

def banner():
    time.sleep(1)
    print '\033[32m''''
                                                  ,,                    
  .g8"""bgd                                     `7MM                    
.dP'     `M                                       MM                    
dM'       ` `7Mb,od8  ,6"Yb.  `7M'    ,A    `MF'  MM   .gP"Ya  `7Mb,od8 
MM            MM' "' 8)   MM    VA   ,VAA   ,V    MM  ,M'   Yb   MM' "' 
MM.           MM      ,pm9MM     VA ,V  VA ,V     MM  8M""""""   MM     
`Mb.     ,'   MM     8M   MM      VVV    VVV      MM  YM.    ,   MM     
  `"bmmmd'  .JMML.   `Moo9^Yo.     W      W     .JMML. `Mbmmd' .JMML.   ''''\033[0;0m\n'

req = requesocks.session()
req.proxies = {'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'}

def request_tor(url):
    page = req.get(url, headers=header)
    text = page.text
    return text

def while_tor():
    while True:

        url = site_crawled[0]

        try:
            request_tor(url)

        except:
            site_crawled.remove(url)
            crawled.add(url)
            continue

        html = request_tor(url)

        links = re.findall(r'<a href="?\'?(https?:\/\/[^"\'>]*)', html)
        print '\033[32m' + hour() + "[INFO] Listening pages:" + url + '\033[0;0m'

        site_crawled.remove(url)

        crawled.add(url)

        for link in links:
            if link not in crawled and link not in site_crawled:
                site_crawled.append(link)

def while_true():
    while True:

        url = site_crawled[0]

        try:
            req = requests.get(url, headers=header)

        except:
            site_crawled.remove(url)
            crawled.add(url)
            continue

        html = req.text

        links = re.findall(r'<a href="?\'?(https?:\/\/[^"\'>]*)', html)
        print '\033[32m'+ hour() + "[INFO] Listening pages:" + url + '\033[0;0m'
        time.sleep(0.2)

        site_crawled.remove(url)

        crawled.add(url)

        for link in links:
            if link not in crawled and link not in site_crawled:
                site_crawled.append(link)

def clear():
    subprocess.call('clear', shell=True)

def hour():
    now = datetime.now()
    return "["+str(now.hour) + ":" + str(now.minute)+"]"

parser = argparse.ArgumentParser()
parser.add_argument('-u', dest="url", help="Link to site Crawling", nargs=1)
parser.add_argument('-tor', dest='tor', help="Use the tool inside the TOR network (yes/no)", default='no')
args = parser.parse_args()

site = args.url[0]

if not 'http://' in site:
    url_correct = 'http://'+site
elif not 'https://' in site:
    url_correct = 'https://'+site

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
    if args.tor == 'yes':
        banner()
        time.sleep(2)
        print '\033[32m' + hour() + "[INFO] The tool is starting in network Tor"'\033[0;0'
        time.sleep(1)
        print '\033[32m' + hour() + "[INFO] Process The Crawler Start:\n"'\033[0;0'

        while_tor()

except KeyboardInterrupt:
    print "\n\033[31m" + hour() + "[INFO] User Finished Process""\033[0;0m"
    exit()

try:
    banner()
    time.sleep(2)
    print '\033[32m'+ hour() + "[INFO] The tool is starting"'\033[0;0'
    time.sleep(1)
    print '\033[32m'+ hour() + "[INFO] Process The Crawler Start:\n"'\033[0;0m'

    while_true()

except KeyboardInterrupt:
    print "\n\033[31m" + hour() + "[INFO] User Finished Process""\033[0;0m"
    exit()
