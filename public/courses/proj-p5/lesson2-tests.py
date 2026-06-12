import pandas as pd
import sys
sys.path.insert(0, '.')
from lesson2_template import load_behavior, overview


def test_n_positive():
    df = load_behavior('../../datasets/study_behavior.csv')
    o = overview(df)
    assert o["n"] > 100


def test_avg_positive():
    df = load_behavior('../../datasets/study_behavior.csv')
    o = overview(df)
    for k in ["avg_duration", "avg_pause", "avg_seek", "avg_score"]:
        assert o[k] >= 0


def test_avg_score_range():
    df = load_behavior('../../datasets/study_behavior.csv')
    o = overview(df)
    assert 0 <= o["avg_score"] <= 100


def test_returns_dict():
    df = load_behavior('../../datasets/study_behavior.csv')
    o = overview(df)
    assert isinstance(o, dict)


if __name__ == "__main__":
    test_n_positive()
    test_avg_positive()
    test_avg_score_range()
    test_returns_dict()
    print("lesson2 tests passed")
