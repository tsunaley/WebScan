import requests
from lib.writeErrorLog import WriteLog
import sys

def check_beifen(url):
    headers = {
        'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/80.0.3987.162 Safari/537.36',
        'Connection': 'close'
    }
    s = set()
    for line1 in open("data/beifen.txt"):
        try:
            url1 = url + line1.strip()
            status1 = requests.get(url1, headers=headers).status_code
            if status1 == 200:
                s.add(url1)
            for line2 in open("data/shuju.txt"):
                url2 = url+line2.strip()+line1.strip()
                status2 = requests.get(url2, headers=headers).status_code
                if status2 == 200:
                    s.add(url2)
        except:
            info = sys.exc_info()
            WriteLog(info[0], info[1], info[2])
    return s


if __name__ == '__main__':
    s = check_beifen('https://www.baidu.com')
    print(s)