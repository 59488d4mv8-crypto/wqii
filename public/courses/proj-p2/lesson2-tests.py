import numpy as np
import pandas as pd
import sys
sys.path.insert(0, '.')
from lesson2_template import chapter_funnel, completion_rate


def test_funnel_length():
    df = pd.read_csv('../../datasets/lesson_progress.csv')
    f = chapter_funnel(df)
    assert len(f) >= 3


def test_funnel_sum():
    df = pd.read_csv('../../datasets/lesson_progress.csv')
    f = chapter_funnel(df)
    assert f.sum() == len(df)


def test_completion_in_range():
    df = pd.read_csv('../../datasets/lesson_progress.csv')
    r = completion_rate(df)
    for v in r.values:
        assert 0 <= v <= 1


def test_completion_is_float():
    df = pd.read_csv('../../datasets/lesson_progress.csv')
    r = completion_rate(df)
    assert r.dtype == float or str(r.dtype).startswith('float')


if __name__ == "__main__":
    test_funnel_length()
    test_funnel_sum()
    test_completion_in_range()
    test_completion_is_float()
    print("lesson2 tests passed")
