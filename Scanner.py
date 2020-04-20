from bs4 import BeautifulSoup
import re
from lib.download import Downloader
from urllib.parse import urljoin

class Scanner(object):
    def __init__(self, url, limit=100):
        self.__url = url
        self.__limit = limit
        self.__urlList = list()
        self.__urlList.append(url)
        self.__keywords = url.split('.')[1]

    def scan(self, target, flag=0):
        download = Downloader(flag=flag)
        data = download.get(target)
        soup = BeautifulSoup(data, 'html.parser')
        links = soup.find_all('a')

        for item in links:
            if len(self.__urlList) >= 100:
                break
            url = item.get('href')
            if url == '':
                continue
            url = url + '/' if url[-1] != '/' else url              # 末尾有/的加上/
            url = urljoin(target, url)
            url = url.split('#', 1)[0] if '#' in url else url           # 有#的删除#后面
            if self.__keywords in url:
                url = url.replace('//', 'http://', 1) if url[0:2] == '//' else url           # //开头的加上http:
                url = url.replace('https', 'http', 1)      # 把https换成http避免重复
                if 'http' not in url:
                    continue
                if url in self.__urlList:
                    continue
                self.__urlList.append(url)

    def init(self):
        i = 0
        try:
            while len(self.__urlList) < self.__limit:
                self.scan(self.__urlList[i])
                i += 1
        except:
            pass
        finally:
            return self.__urlList


if __name__ == '__main__':
    url = 'https://www.baidu.com/'
    k = Scanner(url, 100)
    print(k.init())