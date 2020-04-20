import re

def isurl(url):
    if re.match(r'^https?:/{2}\w.+$', url):
        return True
    else:
        return False


if __name__ == '__main__':
    print(isurl("http://www.baidu.com/fdsa"))