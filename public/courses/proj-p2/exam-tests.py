import numpy as np
import pandas as pd
import sys
sys.path.insert(0, '.')
from exam_template import top3_dropout_chapters


def test_returns_list():
    r = top3_dropout_chapters('../../datasets/lesson_progress.csv')
    assert isinstance(r, list)


def test_has_3_items():
    r = top3_dropout_chapters('../../datasets/lesson_progress.csv')
    assert len(r) == 3


def test_all_strings():
    r = top3_dropout_chapters('../../datasets/lesson_progress.csv')
    for v in r:
        assert isinstance(v, str)


def test_in_df():
    r = top3_dropout_chapters('../../datasets/lesson_progress.csv')
    df = pd.read_csv('../../datasets/lesson_progress.csv')
    for v in r:
        assert v in df['chapter_id'].values


if __name__ == "__main__":
    test_returns_list()
    test_has_3_items()
    test_all_strings()
    test_in_df()
    print("exam-p2 passed")
