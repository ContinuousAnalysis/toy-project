def test_ok_1():
    l = list(range(8))
    l.append("test")

def test_ok_2():
    l = list(range(8))
    l.extend(["test"])

def test_ok_3():
    l = list(range(8))
    l.insert(0, "test")

def test_violation_1():
    l = list(range(20))
    l.append("test")

def test_violation_2():
    l = list(range(20))
    l = l.extend(["test"])

def test_violation_3():
    l = list(range(20))
    l = l.insert(0, "test")

# Currently not supported
def test_violation_4():
    l = list(range(20))
    l += ["test"]

# Currently not supported
def test_violation_5():
    l = list(range(20))
    l = l + ["test"]
