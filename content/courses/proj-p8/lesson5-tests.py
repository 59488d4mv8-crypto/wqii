import sys
sys.path.insert(0, '.')
from lesson5_template import solve


def test_solve_returns_list():
    r = solve('../../datasets/daily_traffic.csv', target_col='pv')
    assert isinstance(r, list)


def test_solve_length_7():
    r = solve('../../datasets/daily_traffic.csv', target_col='pv')
    assert len(r) == 7


def test_predictions_positive():
    r = solve('../../datasets/daily_traffic.csv', target_col='pv')
    for p in r:
        assert p > 0


if __name__ == "__main__":
    test_solve_returns_list()
    test_solve_length_7()
    test_predictions_positive()
    print("lesson5 tests passed")
