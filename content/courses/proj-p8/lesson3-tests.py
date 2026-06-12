import sys
sys.path.insert(0, '.')
from lesson3_template import load_data, rolling_mean


def test_rolling_mean_length():
    df = load_data('../../datasets/daily_traffic.csv')
    rm = rolling_mean(df['pv'], window=7)
    assert len(rm) == len(df)


def test_rolling_mean_positive():
    df = load_data('../../datasets/daily_traffic.csv')
    rm = rolling_mean(df['pv'], window=7)
    for v in rm:
        assert v > 0


def test_rolling_mean_window_1_equals_original():
    df = load_data('../../datasets/daily_traffic.csv')
    rm = rolling_mean(df['pv'], window=1)
    for a, b in zip(rm, df['pv']):
        assert abs(a - b) < 1e-9


if __name__ == "__main__":
    test_rolling_mean_length()
    test_rolling_mean_positive()
    test_rolling_mean_window_1_equals_original()
    print("lesson3 tests passed")
