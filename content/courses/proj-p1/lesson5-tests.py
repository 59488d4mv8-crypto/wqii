import numpy as np
import pandas as pd
import sys
sys.path.insert(0, '.')
from lesson5_template import dau_stats, wau, mau


def test_dau_mean_positive():
    dau = pd.read_csv('../../datasets/daily_active.csv')
    s = dau_stats(dau)
    assert s["mean"] > 0


def test_dau_max_greater_mean():
    dau = pd.read_csv('../../datasets/daily_active.csv')
    s = dau_stats(dau)
    assert s["max"] >= s["mean"]


def test_wau_positive():
    dau = pd.read_csv('../../datasets/daily_active.csv')
    assert wau(dau) > 0


def test_mau_positive():
    dau = pd.read_csv('../../datasets/daily_active.csv')
    assert mau(dau) > 0


if __name__ == "__main__":
    test_dau_mean_positive()
    test_dau_max_greater_mean()
    test_wau_positive()
    test_mau_positive()
    print("lesson5 tests passed")
