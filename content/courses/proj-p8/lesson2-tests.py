import sys
sys.path.insert(0, '.')
from lesson2_template import load_data, summary


def test_summary_has_n_days():
    df = load_data('../../datasets/daily_traffic.csv')
    s = summary(df)
    assert s['n_days'] >= 100


def test_summary_means_positive():
    df = load_data('../../datasets/daily_traffic.csv')
    s = summary(df)
    assert s['pv_mean'] > 0
    assert s['uv_mean'] > 0
    assert s['orders_mean'] > 0


def test_dates_ordered():
    df = load_data('../../datasets/daily_traffic.csv')
    assert df['date'].is_monotonic_increasing


if __name__ == "__main__":
    test_summary_has_n_days()
    test_summary_means_positive()
    test_dates_ordered()
    print("lesson2 tests passed")
