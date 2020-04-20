# sql注入检测通过一些payload使payload使页面报错，判断原始网页，正确网页，错误网页即可检测出是否存在sql注入漏洞
# 通过匹配出sql报错出来的信息，可以正则判断出所用的数据库
# 扫描器目前是通过一个爬虫扫描来进行漏洞检测，以后会从各个方面进行检测


import re
from lib.download import Downloader, Url
from lib.writeErrorLog import WriteLog
import sys

DBMS_ERRORS = {            # 用一个字典存储数据库特征
    "MySQL": (r"SQL syntax.*MySQL", r"Warning.*mysql_.*", r"valid MySQL result", r"MySqlClient\."),
    "PostgreSQL": (r"PostgreSQL.*ERROR", r"Warning.*\Wpg_.*", r"valid PostgreSQL result", r"Npgsql\."),
    "Microsoft SQL Server": (r"Driver.* SQL[\-\_\ ]*Server", r"OLE DB.* SQL Server", r"(\W|\A)SQL Server.*Driver", r"Warning.*mssql_.*", r"(\W|\A)SQL Server.*[0-9a-fA-F]{8}", r"(?s)Exception.*\WSystem\.Data\.SqlClient\.", r"(?s)Exception.*\WRoadhouse\.Cms\."),
    "Microsoft Access": (r"Microsoft Access Driver", r"JET Database Engine", r"Access Database Engine"),
    "Oracle": (r"\bORA-[0-9][0-9][0-9][0-9]", r"Oracle error", r"Oracle.*Driver", r"Warning.*\Woci_.*", r"Warning.*\Wora_.*"),
    "IBM DB2": (r"CLI Driver.*DB2", r"DB2 SQL error", r"\bdb2_\w+\("),
    "SQLite": (r"SQLite/JDBCDriver", r"SQLite.Exception", r"System.Data.SQLite.SQLiteException", r"Warning.*sqlite_.*", r"Warning.*SQLite3::", r"\[SQLITE_ERROR\]"),
    "Sybase": (r"(?i)Warning.*sybase.*", r"Sybase message", r"Sybase.*Server message.*"),
}
# BOOLEAN_TESTS = (" AND {}={}", " OR NOT ({}={})")   # 测试语句payload
BOOLEAN_TESTS = ("' AND 1=1#", "' AND 1=2#")


def sqlcheck(url, flag=0, loginUrl='', loginData=''):
    try:
        domain, pararms = Url.urlCheck(url)
        if domain is not None:
            pass
        download = Downloader(flag=flag, loginUrl=loginUrl, loginData=loginData)
        urls = Url.paylodJoint(domain, pararms, ")(\" '")

        for _url in urls:
            _content = download.get(_url)
            for (dbms, regex) in ((dbms, regex) for dbms in DBMS_ERRORS for regex in DBMS_ERRORS[dbms]):   # 通过正则判断是哪个数据库
                if re.search(regex, _content):
                    return url

        content = {}
        content["origin"] = download.get(_url)
        pararm1 = Url.paylodJoint(domain, pararms, BOOLEAN_TESTS[0])
        pararm2 = Url.paylodJoint(domain, pararms, BOOLEAN_TESTS[1])

        for url1, url2 in zip(pararm1, pararm2):
            # RANDINT = 1
            content["true"] = download.get(url1)
            content["false"] = download.get(url2)
            # a = content["origin"] == content["true"]
            # b = content["true"] != content["false"]
            if content["origin"] == content["true"] != content["false"]:
                return url
        return False
    except:
        info = sys.exc_info()
        WriteLog(info[0], info[1], info[2])
        return False


if __name__ == '__main__':
    print(sqlcheck('http://192.168.220.132/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit#', 1))