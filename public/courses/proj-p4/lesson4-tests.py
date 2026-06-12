import pandas as pd
import sys
sys.path.insert(0, '.')
from lesson4_template import word_frequency_data


def test_returns_dict():
    df = pd.read_csv('../../datasets/course_reviews.csv')
    r = word_frequency_data(df, 10)
    assert isinstance(r, dict)


def test_keys_are_strings():
    df = pd.read_csv('../../datasets/course_reviews.csv')
    r = word_frequency_data(df, 10)
    for k in r.keys():
        assert isinstance(k, str)


def test_values_positive_int():
    df = pd.read_csv('../../datasets/course_reviews.csv')
    r = word_frequency_data(df, 10)
    for v in r.values():
        assert isinstance(v, int) and v > 0


def test_size_topn():
    df = pd.read_csv('../../datasets/course_reviews.csv')
    r = word_frequency_data(df, 5)
    assert len(r) == 5


if __name__ == "__main__":
    test_returns_dict()
    test_keys_are_strings()
    test_values_positive_int()
    test_size_topn()
    print("lesson4 tests passed")
