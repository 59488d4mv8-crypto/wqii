import numpy as np
import pandas as pd
import sys
sys.path.insert(0, '.')
from lesson5_template import segment_pie_data


def test_returns_dict():
    df = pd.read_csv('../../datasets/rfm_data.csv')
    r = segment_pie_data(df)
    assert isinstance(r, dict)


def test_has_segments():
    df = pd.read_csv('../../datasets/rfm_data.csv')
    r = segment_pie_data(df)
    assert len(r) >= 2


def test_sum_total():
    df = pd.read_csv('../../datasets/rfm_data.csv')
    r = segment_pie_data(df)
    assert sum(r.values()) == len(df)


def test_values_nonzero():
    df = pd.read_csv('../../datasets/rfm_data.csv')
    r = segment_pie_data(df)
    for v in r.values():
        assert v > 0


if __name__ == "__main__":
    test_returns_dict()
    test_has_segments()
    test_sum_total()
    test_values_nonzero()
    print("lesson5 tests passed")
