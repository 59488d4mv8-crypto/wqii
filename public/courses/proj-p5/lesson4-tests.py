import pandas as pd
import sys
sys.path.insert(0, '.')
from lesson4_template import scatter_data


def test_returns_dict():
    df = pd.read_csv('../../datasets/study_behavior.csv')
    r = scatter_data(df)
    assert isinstance(r, dict)


def test_has_xy():
    df = pd.read_csv('../../datasets/study_behavior.csv')
    r = scatter_data(df)
    assert 'x' in r and 'y' in r


def test_xy_same_length():
    df = pd.read_csv('../../datasets/study_behavior.csv')
    r = scatter_data(df)
    assert len(r['x']) == len(r['y'])


def test_y_in_score_range():
    df = pd.read_csv('../../datasets/study_behavior.csv')
    r = scatter_data(df)
    for y in r['y']:
        assert 0 <= y <= 100


if __name__ == "__main__":
    test_returns_dict()
    test_has_xy()
    test_xy_same_length()
    test_y_in_score_range()
    print("lesson4 tests passed")
