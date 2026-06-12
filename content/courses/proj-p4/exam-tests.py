import pandas as pd
import sys
sys.path.insert(0, '.')
from exam_template import analyze_reviews


def test_returns_dict():
    r = analyze_reviews('../../datasets/course_reviews.csv')
    assert isinstance(r, dict)


def test_has_required_keys():
    r = analyze_reviews('../../datasets/course_reviews.csv')
    for k in ["avg_sentiment", "positive_reviews", "negative_reviews"]:
        assert k in r


def test_avg_in_range():
    r = analyze_reviews('../../datasets/course_reviews.csv')
    assert -1.0 <= r["avg_sentiment"] <= 1.0


def test_counts_nonnegative():
    r = analyze_reviews('../../datasets/course_reviews.csv')
    assert r["positive_reviews"] >= 0 and r["negative_reviews"] >= 0


if __name__ == "__main__":
    test_returns_dict()
    test_has_required_keys()
    test_avg_in_range()
    test_counts_nonnegative()
    print("exam-p4 passed")
