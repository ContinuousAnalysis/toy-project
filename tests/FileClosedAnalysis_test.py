def test_ok_1():
    t1 = open("test1.txt", "w")
    t1.close()

def test_ok_2():
    with open("test2.txt", "w") as t:
        pass

def test_violation_1():
    t3 = open("test3.txt", "w")
    t3.write("test")
