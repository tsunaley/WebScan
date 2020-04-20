import requests
import socket
from urllib.request import urlparse
from bs4 import BeautifulSoup
import time
import os
import json
import whois
import sys
from lib.download import Downloader
from lib.writeErrorLog import WriteLog


# 查ip
def IpCheck(dname):
    ip = socket.gethostbyname(dname)
    return {'ip': ip}


# 查whois
def WhoisCheck(url):
    try:
        return whois.whois(url)
    except:
        info = sys.exc_info()
        WriteLog(info[0], info[1], info[2])
        return None

# 子域名收集
def SubdomainCheck(dname):
    # sdomainlist = []
    # for i in range(1, 40, 10):
    #     url = "https://cn.bing.com/search?q=" + dname + " & first = {}".format(str(i))
    #     heads = {
    #         'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.16 (KHTML, like Geko) Chrome/10.0.648.133 Safari/534.16'
    #     }
    #     try:
    #         html = requests.get(url, headers=heads)
    #         soup = BeautifulSoup(html.content, 'html.parser')
    #         tags = soup.find_all('h2')
    #         for tag in tags:
    #             # time.sleep(4)
    #             tag_a = tag.find_all('a')
    #             for a in tag_a:
    #                 href = a.attrs['href']
    #                 sdomainlist.append(href)
    #     except:
    #         continue

    # sdomainlist = []
    # for i in range(1, 80):
    #     url = "https://cn.bing.com/search?q=domain:" + dname + " & first = {}".format(str(i))
    #     i *= 10
    #     heads = {
    #         'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.16 (KHTML, like Geko) Chrome/10.0.648.133 Safari/534.16'
    #     }
    #     try:
    #         html = requests.get(url, headers=heads)
    #         soup = BeautifulSoup(html.content, 'html.parser')
    #         tags = soup.find_all('div', attrs={'class': 'b-attribution'})
    #         r = re.compile(r'<cite>(.*?)</cite>')
    #         for tag in tags:
    #             time.sleep(1)
    #
    #             subdomain = re.findall(r, tag.text)[0]
    #             sdomainlist.append(subdomain)
    #     except:
    #         continue
    #
    # sdomainlist_ = list(set(sdomainlist))
    # print("Subdomains are below:\n")
    # for line in sdomainlist_:
    #     print(line)

    sdomainlist = []
    for i in range(1, 80):
        url = "https://cn.bing.com/search?q=domain:" + dname + " & first = {}".format(str(i))
        i *= 10
        heads = {
            'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.16 (KHTML, like Geko) Chrome/10.0.648.133 Safari/534.16'
        }
        try:
            html = requests.get(url, headers=heads)
            soup = BeautifulSoup(html.content, 'html.parser')
            tags = soup.find_all('cite')
            for tag in tags:
                time.sleep(1)
                subdomain = tag.string
                sdomainlist.append(subdomain)
        except:
            continue

    sdomainlist_ = list(set(sdomainlist))
    print("Subdomains are below:\n")
    for line in sdomainlist_:
        print(line)

    sdomainlist_ = list(set(sdomainlist))
    print("Subdomains are below:\n")
    for line in sdomainlist_:
        print(line)


# 端口状态收集
def PortScan(dname):
    openPort = []
    ip = socket.gethostbyname(dname)
    portlist = [5, 21, 22, 23, 25, 69, 80, 102, 109, 110, 119, 135, 137, 138, 139, 161, 177, 389, 443, 445, 1080, 1158,
                1433, 1434, 1521, 2100, 3128, 3306, 3389, 7001, 8080, 8081, 9080, 9090]
    for port in portlist:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            s.connect((ip, port))
            openPort.append(port)
        except:
            continue
        finally:
            s.close()
    return {"open_port": openPort}


# cms查看
def CmsCheck(url):
    j = 0
    download = Downloader()
    filename = os.path.join(sys.path[0], "data", "CMSdata.json")
    if os.path.exists(filename):
        js = open(filename, 'r', encoding='UTF-8')
        lr = json.load(js)
    else:
        return None
    for i in lr:
        j += 1
        print(j)
        text = download.get(url)
        if text == None:
            pass
        else:
            if i["re"]:
                if text.find(i["re"]) != -1:
                    # print("The CMS of {} is {}, and the whole url is {}".format(url, i["name"], url_))
                    return {'CMS': i["name"]}


def InfoCollection(url):
    msg = []
    # url = 'https://www.wpdaxue.com/'
    try:
        dname = urlparse(url).netloc
        msg.append(IpCheck(dname))
        msg.append(WhoisCheck(url))
        # SubdomainCheck(dname)
        msg.append(PortScan(dname))
        msg.append(CmsCheck(url))
        return msg
    except:
        info = sys.exc_info()
        WriteLog(info[0], info[1], info[2])
        return False



