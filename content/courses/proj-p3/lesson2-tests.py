import numpy as np
import pandas as pd
import sys
sys.path.insert(0, '.')
from lesson2_template import load_rfm, stats


def test_n_users():
    df = load_rfm('../../datasets/rfm_data.csv')
    s = stats(df)
    assert s["n_users"] >= 100


def test_avg_recency_positive():
    df = load_rfm('../../datasets/rfm_data.csv')
    s = stats(df)
    assert s["avg_recency"] > 0


def test_avg_frequency_positive():
    df = load_rfm('../../datasets/rfm_data.csv')
    s = stats(df)
    assert s["avg_frequency"] > 0


def test_avg_monetary_positive():
    df = load_rfm('../../datasets/rfm_data.csv')
    s = stats(df)
    assert s["avg_monetary"] > 0


if __name__ == "__main__":
    test_n_users()
    test_avg_recency_positive()
    test_avg_frequency_positive()
    test_avg_monetary_positive()
    print("lesson2 tests passed")
