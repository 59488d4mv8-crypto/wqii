import numpy as np
import pandas as pd
import sys
sys.path.insert(0, '.')
from exam_template import top3_channel_dau_mean


def test_returns_dict():
    r = top3_channel_dau_mean('../../datasets/daily_active.csv')
    assert isinstance(r, dict)


def test_has_3_keys():
    r = top3_channel_dau_mean('../../datasets/daily_active.csv')
    assert len(r) == 3


def test_values_positive():
    r = top3_channel_dau_mean('../../datasets/daily_active.csv')
    for v in r.values():
        assert v > 0


def test_sorted_desc():
    r = top3_channel_dau_mean('../../datasets/daily_active.csv')
    vals = list(r.values())
    assert vals[0] >= vals[1] >= vals[2]


if __name__ == "__main__":
    test_returns_dict()
    test_has_3_keys()
    test_values_positive()
    test_sorted_desc()
    print("exam-p1 passed")
