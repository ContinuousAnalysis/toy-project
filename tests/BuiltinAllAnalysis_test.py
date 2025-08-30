def test_ok_1():
    all([True, True, True])

def test_ok_2():
    all([True, True, False])

def test_ok_3():
    all([[]])  # returns False

def test_ok_4():
    all([[[True]]])
    all([[[], True]])
    all([[[]], True])

def test_ok_5():
    any([[[True]]])
    any([[[], True]])
    any([[[]], True])

def test_violation_1():
    all([])  # returns True # DyLin warn

def test_violation_2():
    all([[[]]])  # returns True # DyLin warn

def test_violation_3():
    all([[[[]]]])  # returns True # DyLin warn

def test_violation_4():
    any([[[]]])  # DyLin warn