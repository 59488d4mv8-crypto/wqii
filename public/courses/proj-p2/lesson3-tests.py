import numpy as np
import pandas as pd
import sys
sys.path.insert(0, '.')
from lesson3_template import chapter_dropout_rate, lowest_completion_chapter


def test_rate_length():
    df = pd.read_csv('../../datasets/lesson_progress.csv')
    r = chapter_dropout_rate(df)
    assert len(r) >= 3


def test_rate_in_range():
    df = pd.read_csv('../../datasets/lesson_progress.csv')
    r = chapter_dropout_rate(df)
    for v in r.values:
        assert 0 <= v <= 1


def test_lowest_chapter_return_type():
    df = pd.read_csv('../../datasets/lesson_progress.csv')
    ch, _ = lowest_completion_chapter(df)
    assert isinstance(ch, str) or isinstance(ch, (np.str_,))


def test_lowest_value_valid():
    df = pd.read_csv('../../datasets/lesson_progress.csv')
    _, v = lowest_completion_chapter(df)
    assert 0 <= v <= 1


if __name__ == "__main__":
    test_rate_length()
    test_rate_in_range()
    test_lowest_chapter_return_type()
    test_lowest_value_valid()
    print("lesson3 tests passed")
