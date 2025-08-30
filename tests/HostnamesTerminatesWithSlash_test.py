import requests

def test_ok_1():
    s = requests.Session()
    s.mount('https://github.com/', None)

def test_violation_1():
    s = requests.Session()
    s.mount('https://github.com', None)