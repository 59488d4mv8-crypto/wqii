import numpy as np
import pandas as pd
import sys
sys.path.insert(0, '.')
from lesson4_template import feature_corr, progress_dropout_corr


def test_corr_shape():
    df = pd.read_csv('../../datasets/lesson_progress.csv')
    c = feature_corr(df)
    assert c.shape[0] == c.shape[1]


def test_corr_diagonal():
    df = pd.read_csv('../../datasets/lesson_progress.csv')
    c = feature_corr(df)
    assert abs(c.iloc[0, 0] - 1.0) < 1e-6


def test_progress_corr_range():
    df = pd.read_csv('../../datasets/lesson_progress.csv')
    v = progress_dropout_corr(df)
    assert -1.0 <= v <= 1.0


def test_progress_corr_negative():
    # progress 越高，流失应该越低 -> 负相关
    df = pd.read_csv('../../datasets/lesson_progress.csv')
    v = progress_dropout_corr(df)
    assert v < 0


if __name__ == "__main__":
    test_corr_shape()
    test_corr_diagonal()
    test_progress_corr_range()
    test_progress_corr_negative()
    print("lesson4 tests passed")
