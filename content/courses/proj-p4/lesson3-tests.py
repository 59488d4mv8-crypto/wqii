import pandas as pd
import sys
sys.path.insert(0, '.')
from lesson3_template import top_words


def test_returns_list():
    df = pd.read_csv('../../datasets/course_reviews.csv')
    r = top_words(df, 10)
    assert isinstance(r, list)


def test_returns_tuples():
    df = pd.read_csv('../../datasets/course_reviews.csv')
    r = top_words(df, 10)
    for item in r:
        assert isinstance(item, tuple) and len(item) == 2


def test_topn_respected():
    df = pd.read_csv('../../datasets/course_reviews.csv')
    r = top_words(df, 5)
    assert len(r) == 5


def test_counts_positive():
    df = pd.read_csv('../../datasets/course_reviews.csv')
    r = top_words(df, 10)
    for _, c in r:
        assert c > 0


if __name__ == "__main__":
    test_returns_list()
    test_returns_tuples()
    test_topn_respected()
    test_counts_positive()
    print("lesson3 tests passed")
