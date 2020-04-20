from lib.download import Downloader, Url
from lib.writeErrorLog import WriteLog
import sys, os

payloads = []    # 读取xss.txt文件
filename = os.path.join(sys.path[0], "data", "xss.txt")    # os.path.join(path1,path2)把文件或目录合并成一个路径
f = open(filename)
for i in f:
    payloads.append(i.strip())  # 对每行用strip()过滤下\n 空格等的特殊符号


 # 获取url，拆分url，对每个url拆分参数进入注入分析，成功就返回出来。
def run(url, flag=0, loginUrl='', loginData=''):
    try:
        download = Downloader(flag=flag, loginUrl=loginUrl, loginData=loginData)
        domain, pararms = Url.urlCheck(url)
        1/0
        if domain is not None:
            pass
        for payload in payloads:
            urls = Url.paylodJoint(domain, pararms, payload)
            for _url in urls:
                str = download.get(_url)
                if str is None:
                    return False
                if str.find(payload) != -1:
                    return "xss found: {}".format(url)
    except:
        info = sys.exc_info()
        WriteLog(info[0], info[1], info[2])
        return False


if __name__ == '__main__':
    print(run('http://192.168.220.132/dvwa/vulnerabilities/xss_r/?name=1#', 1))