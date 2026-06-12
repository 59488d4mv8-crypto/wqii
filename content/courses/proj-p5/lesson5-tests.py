import pandas as pd
import sys
sys.path.insert(0, '.')
from lesson5_template import linear_fit, fit_score_by_duration


def test_linear_fit_slope_intercept():
    # y = 2x + 1
    x = [1, 2, 3, 4, 5]
    y = [3, 5, 7, 9, 11]
    s, i = linear_fit(x, y, 1)
    assert abs(s - 2.0) < 1e-6
    assert abs(i - 1.0) < 1e-6


def test_fit_score_returns_dict():
    df = pd.read_csv('../../datasets/study_behavior.csv')
    r = fit_score_by_duration(df)
    assert isinstance(r, dict)


def test_fit_has_keys():
    df = pd.read_csv('../../datasets/study_behavior.csv')
    r = fit_score_by_duration(df)
    assert 'slope' in r and 'intercept' in r


def test_slope_is_float():
    df = pd.read_csv('../../datasets/study_behavior.csv')
    r = fit_score_by_duration(df)
    assert isinstance(r['slope'], float)


if __name__ == "__main__":
    test_linear_fit_slope_intercept()
    test_fit_score_returns_dict()
    test_fit_has_keys()
    test_slope_is_float()
    print("lesson5 tests passed")
