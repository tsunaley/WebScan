import Collection
import Scanner
import json
import datetime
import mingan
import beifen
import sql_check
import xss_check
import web_shell
from lib.tool import DateEncoder
from lib.Exception import ExceptHookHandler
import sys, os


def main(url, flag=0, loginUrl='', loginData=''):
    logFile = os.path.join(sys.path[0], "log", "log.txt")
    ExceptHookHandler(logFile)

    scan = Scanner.Scanner(url, 100)
    url_list = scan.init()

    result = dict()

    msg = Collection.InfoCollection(url)

    min = mingan.check_mingan(url)

    bei = beifen.check_beifen(url)

    sql = []
    xss = []
    shell = []

    for u in url_list:
        sql_url = sql_check.sqlcheck(u, flag, loginUrl, loginData)
        if sql_url:
            sql.append(sql_url)
        xss_url = xss_check.run(u, flag, loginUrl, loginData)
        if xss_url:
            xss.append(xss_url)
        shell_url = web_shell.run(u, flag, loginUrl, loginData)
        if shell_url:
            shell.append(shell_url)

    result['msg'] = msg
    result['敏感目录'] = min
    result['备份文件'] = bei
    result['sql注入漏洞'] = sql
    result['xss漏洞'] = xss
    result['webshell'] = shell

    results = json.dumps(result, cls=DateEncoder, ensure_ascii=False)
    with open('F:\比赛\作品赛\project\\result\\result.json'.format(datetime.datetime.now()), 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, separators=(',', ': '))


if __name__ == '__main__':
    url = ''
    main(url)