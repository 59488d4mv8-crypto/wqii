import numpy as np
import pandas as pd
import sys
sys.path.insert(0, '.')
from lesson4_template import hour_distribution, peak_hour


def test_hour_shape():
    reg = pd.read_csv('../../datasets/user_registrations.csv')
    d = hour_distribution(reg)
    assert len(d) >= 1


def test_hour_sum():
    reg = pd.read_csv('../../datasets/user_registrations.csv')
    d = hour_distribution(reg)
    assert d.sum() == len(reg)


def test_peak_hour_in_range():
    reg = pd.read_csv('../../datasets/user_registrations.csv')
    h = peak_hour(reg)
    assert 0 <= h <= 23


def test_peak_hour_is_max():
    reg = pd.read_csv('../../datasets/user_registrations.csv')
    d = hour_distribution(reg)
    h = peak_hour(reg)
    assert d[h] == d.max()


if __name__ == "__main__":
    test_hour_shape()
    test_hour_sum()
    test_peak_hour_in_range()
    test_peak_hour_is_max()
    print("lesson4 tests passed")
