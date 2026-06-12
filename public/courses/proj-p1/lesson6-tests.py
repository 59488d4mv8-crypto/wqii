import numpy as np
import pandas as pd
import sys
sys.path.insert(0, '.')
from lesson6_template import retention_curve


def test_curve_length():
    reg = pd.read_csv('../../datasets/user_registrations.csv')
    c = retention_curve(reg, days=30)
    assert len(c) == 30


def test_curve_decreasing():
    reg = pd.read_csv('../../datasets/user_registrations.csv')
    c = retention_curve(reg, days=30)
    for i in range(1, len(c)):
        assert c[i] <= c[i-1] + 1e-9


def test_curve_in_range():
    reg = pd.read_csv('../../datasets/user_registrations.csv')
    c = retention_curve(reg, days=30)
    for v in c:
        assert 0 <= v <= 1


def test_first_is_largest():
    reg = pd.read_csv('../../datasets/user_registrations.csv')
    c = retention_curve(reg, days=30)
    assert c[0] >= c[-1]


if __name__ == "__main__":
    test_curve_length()
    test_curve_decreasing()
    test_curve_in_range()
    test_first_is_largest()
    print("lesson6 tests passed")
