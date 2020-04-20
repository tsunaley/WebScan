import requests
from bs4 import BeautifulSoup
from maybe.iptools import header, dict2proxy


def check(ip):
    try:
        pro = dict2proxy(ip)
        url = 'https://www.ipip.net/'
        r = requests.get(url, headers=header, proxies=pro, timeout=5)
        r.raise_for_status()
    except:
        return False
    else:
        return True


ips = []
url = 'https://www.xicidaili.com/nn/'

headers = {  # 模拟浏览器请求，可以用 cookie模拟登陆状态
     'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
}
data = requests.get(url, headers=headers).text
soup = BeautifulSoup(data, 'html.parser')

trs = soup.find('table', id='ip_list').find_all('tr')

ip = '0.0.0.0'
port = '0'
hType = '0'

for tr in trs:
    tds = tr.find_all('td')
    ip = tds[1].text if tds != [] else '0.0.0.0'
    port = tds[2].text if tds != [] else '0'
    hType = tds[5].text if tds != [] else '0'
    msg = {'ip': ip, 'port': port, 'type': hType}
    if check(msg):
        ips.append(msg)


print(ips)


