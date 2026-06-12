import numpy as np
import pandas as pd
import sys
sys.path.insert(0, '.')
from lesson2_template import load_data, summarize


def test_sample_size():
    reg, dau = load_data('../../datasets/user_registrations.csv',
                         '../../datasets/daily_active.csv')
    s = summarize(reg, dau)
    assert s["sample_size"] > 100


def test_num_channels():
    reg, dau = load_data('../../datasets/user_registrations.csv',
                         '../../datasets/daily_active.csv')
    s = summarize(reg, dau)
    assert s["num_channels"] >= 3


def test_date_range():
    reg, dau = load_data('../../datasets/user_registrations.csv',
                         '../../datasets/daily_active.csv')
    s = summarize(reg, dau)
    assert s["date_min"] < s["date_max"]


def test_dau_positive():
    reg, dau = load_data('../../datasets/user_registrations.csv',
                         '../../datasets/daily_active.csv')
    assert dau["dau"].mean() > 0


if __name__ == "__main__":
    test_sample_size()
    test_num_channels()
    test_date_range()
    test_dau_positive()
    print("lesson2 tests passed")
