import numpy as np
import pandas as pd
import sys
sys.path.insert(0, '.')
from lesson5_template import predict_dropout, accuracy


def test_predict_length():
    df = pd.read_csv('../../datasets/lesson_progress.csv')
    p = predict_dropout(df)
    assert len(p) == len(df)


def test_predict_binary():
    df = pd.read_csv('../../datasets/lesson_progress.csv')
    p = predict_dropout(df)
    assert set(p.unique()).issubset({0, 1})


def test_accuracy_in_range():
    df = pd.read_csv('../../datasets/lesson_progress.csv')
    a = accuracy(df)
    assert 0 <= a <= 1


def test_accuracy_positive():
    df = pd.read_csv('../../datasets/lesson_progress.csv')
    a = accuracy(df)
    assert a > 0


if __name__ == "__main__":
    test_predict_length()
    test_predict_binary()
    test_accuracy_in_range()
    test_accuracy_positive()
    print("lesson5 tests passed")
