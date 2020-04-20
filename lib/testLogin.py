import requests


def login(url, header, data):
    # data = {'username': 'admin', 'password': 'admin'}
    # url = 'http://192.168.220.132/dvwa/login.php'
    session = requests.Session()
    session.post(url, data=data, headers=header)
    return session
