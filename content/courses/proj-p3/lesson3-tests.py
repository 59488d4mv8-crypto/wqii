import numpy as np
import pandas as pd
import sys
sys.path.insert(0, '.')
from lesson3_template import rfm_score, avg_scores


def test_rfm_shape():
    df = pd.read_csv('../../datasets/rfm_data.csv')
    s = rfm_score(df)
    for col in ['R', 'F', 'M']:
        assert col in s.columns


def test_scores_in_range():
    df = pd.read_csv('../../datasets/rfm_data.csv')
    s = rfm_score(df)
    for col in ['R', 'F', 'M']:
        assert s[col].min() >= 1 and s[col].max() <= 5


def test_avg_scores_dict():
    df = pd.read_csv('../../datasets/rfm_data.csv')
    a = avg_scores(df)
    assert isinstance(a, dict)


def test_avg_in_range():
    df = pd.read_csv('../../datasets/rfm_data.csv')
    a = avg_scores(df)
    for v in a.values():
        assert 1 <= v <= 5


if __name__ == "__main__":
    test_rfm_shape()
    test_scores_in_range()
    test_avg_scores_dict()
    test_avg_in_range()
    print("lesson3 tests passed")
