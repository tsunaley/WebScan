import requests
from urllib.parse import urljoin
import sys
from lib.writeErrorLog import WriteLog


def check_mingan(url):
    try:
        headers = {
            'user-agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/80.0.3987.162 Safari/537.36',
            'Connection': 'close'
        }
        s = list()
        for line in open("data/mingan.txt"):
            url1 = urljoin(url, line)
            status = requests.get(url1, headers=headers).status_code
            if status != 404:
                res = url1.strip() + '*' + str(status)
                s.append(res)
        return s
    except:
        info = sys.exc_info()
        WriteLog(info[0], info[1], info[2])

if __name__ == '__main__':
    s = check_mingan('https://www.baidu.com')
    print(s)