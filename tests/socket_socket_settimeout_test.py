import socket

# create a new socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def test_ok_1():
    assert 1 == 1
    assert 2 == 2
    assert 3 == 3

def test_ok_2():
    s.settimeout(None)

def test_ok_3():
    s.settimeout(0)

def test_ok_4():
    s.settimeout(2.4)

def test_violation_1():
    try:
        s.settimeout(-3)
    except ValueError:
        pass

def test_violation_2():
    try:
        s.settimeout(-3.4)
    except ValueError:
        pass