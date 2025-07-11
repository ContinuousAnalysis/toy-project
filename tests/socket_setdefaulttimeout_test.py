import socket

def test_ok_1():
    assert 1 == 1

def test_ok_2():
    socket.setdefaulttimeout(None)

def test_ok_3():
    socket.setdefaulttimeout(0)

def test_ok_4():
    socket.setdefaulttimeout(2.4)

def test_violation_1():
    try:
        socket.setdefaulttimeout(-3)
    except ValueError:
        pass

def test_violation_2():
    try:
        socket.setdefaulttimeout(-435)
    except ValueError:
        pass

def test_violation_3():
    try:
        socket.setdefaulttimeout(-3.4)
    except ValueError:
        pass