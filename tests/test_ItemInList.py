import sys
import pytest

def test_violation_1():
    x = []
    for i in range(600):
        x.append(i)

    if 1 in x:
        print("1 is in x")
    else:
        print("1 is not in x")
