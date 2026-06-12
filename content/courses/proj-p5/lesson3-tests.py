import pandas as pd
import sys
sys.path.insert(0, '.')
from lesson3_template import corr_matrix, score_corr


def test_corr_shape():
    df = pd.read_csv('../../datasets/study_behavior.csv')
    m = corr_matrix(df)
    assert m.shape == (4, 4)


def test_corr_diagonal():
    df = pd.read_csv('../../datasets/study_behavior.csv')
    m = corr_matrix(df)
    for c in m.columns:
        assert abs(m.loc[c, c] - 1.0) < 1e-6


def test_score_corr_range():
    df = pd.read_csv('../../datasets/study_behavior.csv')
    s = score_corr(df)
    for v in s.values():
        assert -1.0 <= v <= 1.0


def test_pause_corr_is_negative():
    df = pd.read_csv('../../datasets/study_behavior.csv')
    s = score_corr(df)
    assert s["pause_vs_score"] <= 0.1


if __name__ == "__main__":
    test_corr_shape()
    test_corr_diagonal()
    test_score_corr_range()
    test_pause_corr_is_negative()
    print("lesson3 tests passed")
