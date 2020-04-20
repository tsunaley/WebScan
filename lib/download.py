import requests
from urllib import parse
from fake_useragent import UserAgent
from lib.testLogin import login


class Downloader(object):
    def __init__(self, flag=0, loginUrl='http://192.168.220.132/dvwa/login.php', loginData={'username': 'admin', 'password': 'admin', 'Login': 'Login'}):
        self.ua = UserAgent()
        self.heads = {
            'user-agent': self.ua.random,
            'Connection': 'close'
        }
        self.flag = flag
        self.loginUrl = loginUrl
        self.loginData = loginData

    def get(self, url):
        if self.flag == 1:
            session = login(self.loginUrl, self.heads, self.loginData)
            r = session.get(url, timeout=2, headers=self.heads)
        else:
            r = requests.get(url, timeout=2, headers=self.heads)
        if r.status_code != 200:
            return None
        r.encoding = r.apparent_encoding
        _str = r.text
        return _str

    def post(self, url, data):
        if self.flag == 1:
            session = login(self.loginUrl, self.heads, self.loginData)
            r = session.post(url, data, headers=self.heads)
        else:
            r = requests.post(url, data, headers=self.heads)
        r.encoding = r.apparent_encoding
        _str = r.text
        return _str

    def download(self, url, htmls):
        if url is None:
            return None
        _str = {}
        _str["url"] = url
        try:
            r = requests.get(url, timeout=10, headers=self.heads)
            if r.status_code != 200:
                return None
            r.encoding = r.apparent_encoding
            _str["html"] = r.text
        except Exception as e:
            return None
        htmls.append(_str)


class Url(object):
    @staticmethod
    def urlsplit(url):
        _url = url.split("?")[-1]
        pararm = {}      # pararm 参数
        for val in _url.split("&"):
            pararm[val.split("=")[0]] = val.split("=")[-1].replace('#', '')
        return pararm

    @staticmethod
    def paylodJoint(domain, pararms, payload):
        urls = []
        domain += '?'
        keys = list(pararms.keys())
        for i in range(len(pararms)):
            pararm = pararms.copy()
            pararm[keys[i]] += payload
            _url = domain + parse.urlencode(pararm)
            urls.append(_url)
        return urls

    @staticmethod
    def getUrl(domain, pararms):
        url = domain + parse.urlencode(pararms)
        return url

    @staticmethod
    def urlCheck(url):
        if url.find("?"):  # 通过查找？来判断url是否符s合标准
            _url = url
            domain = url.split("?")[0]
            pararms = Url.urlsplit(url)
            return domain, pararms
        else:
            return None




if __name__ == '__main__':
    pararm = Url.urlsplit('http://192.168.220.132/dvwa/vulnerabilities/sqli/?id=d&Submit=Submit#')
    print(pararm)
    print(pararm, Url.paylodJoint('http://192.168.220.132/dvwa/vulnerabilities/sqli/', pararm, ')("\''))