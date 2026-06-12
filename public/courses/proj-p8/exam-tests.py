import sys
sys.path.insert(0, '.')
from exam_template import solve


def test_returns_dict():
    r = solve('../../datasets/daily_traffic.csv', target_col='pv')
    assert isinstance(r, dict)


def test_has_daily_mean_and_next7():
    r = solve('../../datasets/daily_traffic.csv', target_col='pv')
    assert 'daily_mean' in r
    assert 'next_7_days' in r


def test_daily_mean_positive():
    r = solve('../../datasets/daily_traffic.csv', target_col='pv')
    assert r['daily_mean'] > 0


def test_next7_has_7_values():
    r = solve('../../datasets/daily_traffic.csv', target_col='pv')
    assert len(r['next_7_days']) == 7
    for p in r['next_7_days']:
        assert p > 0


if __name__ == "__main__":
    test_returns_dict()
    test_has_daily_mean_and_next7()
    test_daily_mean_positive()
    test_next7_has_7_values()
    print("exam-p8 passed")
