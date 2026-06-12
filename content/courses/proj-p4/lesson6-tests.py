import pandas as pd
import sys
sys.path.insert(0, '.')
from lesson6_template import positive_negative_keywords


def test_returns_dict():
    df = pd.read_csv('../../datasets/course_reviews.csv')
    r = positive_negative_keywords(df, 10)
    assert isinstance(r, dict)


def test_has_keys():
    df = pd.read_csv('../../datasets/course_reviews.csv')
    r = positive_negative_keywords(df, 10)
    assert "positive" in r and "negative" in r


def test_values_lists():
    df = pd.read_csv('../../datasets/course_reviews.csv')
    r = positive_negative_keywords(df, 10)
    assert isinstance(r["positive"], list)
    assert isinstance(r["negative"], list)


def test_topn_length():
    df = pd.read_csv('../../datasets/course_reviews.csv')
    r = positive_negative_keywords(df, 5)
    assert len(r["positive"]) <= 5


if __name__ == "__main__":
    test_returns_dict()
    test_has_keys()
    test_values_lists()
    test_topn_length()
    print("lesson6 tests passed")
