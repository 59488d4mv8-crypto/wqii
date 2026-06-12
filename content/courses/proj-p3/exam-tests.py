import numpy as np
import pandas as pd
import sys
sys.path.insert(0, '.')
from exam_template import segment_user_counts


def test_returns_dict():
    r = segment_user_counts('../../datasets/rfm_data.csv')
    assert isinstance(r, dict)


def test_counts_sum():
    r = segment_user_counts('../../datasets/rfm_data.csv')
    df = pd.read_csv('../../datasets/rfm_data.csv')
    assert sum(r.values()) == len(df)


def test_values_int():
    r = segment_user_counts('../../datasets/rfm_data.csv')
    for v in r.values():
        assert isinstance(v, (int, np.integer))


def test_at_least_2_segments():
    r = segment_user_counts('../../datasets/rfm_data.csv')
    assert len(r) >= 2


if __name__ == "__main__":
    test_returns_dict()
    test_counts_sum()
    test_values_int()
    test_at_least_2_segments()
    print("exam-p3 passed")
