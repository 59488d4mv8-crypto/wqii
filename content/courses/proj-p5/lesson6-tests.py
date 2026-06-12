import pandas as pd
import sys
sys.path.insert(0, '.')
from lesson6_template import pause_groups, group_stats


def test_returns_dict():
    df = pd.read_csv('../../datasets/study_behavior.csv')
    r = pause_groups(df, 5)
    assert isinstance(r, dict)


def test_has_two_groups():
    df = pd.read_csv('../../datasets/study_behavior.csv')
    r = pause_groups(df, 5)
    assert 'low_pause' in r and 'high_pause' in r


def test_group_sum_matches():
    df = pd.read_csv('../../datasets/study_behavior.csv')
    r = pause_groups(df, 5)
    assert len(r['low_pause']) + len(r['high_pause']) == len(df)


def test_group_stats_valid():
    df = pd.read_csv('../../datasets/study_behavior.csv')
    s = group_stats(df, 5)
    assert 0 <= s["low_mean"] <= 100
    assert 0 <= s["high_mean"] <= 100


if __name__ == "__main__":
    test_returns_dict()
    test_has_two_groups()
    test_group_sum_matches()
    test_group_stats_valid()
    print("lesson6 tests passed")
