import sys
sys.path.insert(0, '.')
from lesson4_template import load_data, weekday_agg


def test_weekday_agg_has_7_keys():
    df = load_data('../../datasets/daily_traffic.csv')
    agg = weekday_agg(df)
    assert len(agg) == 7


def test_agg_values_are_positive():
    df = load_data('../../datasets/daily_traffic.csv')
    agg = weekday_agg(df)
    for k, v in agg.items():
        assert v['pv'] > 0
        assert v['uv'] > 0
        assert v['orders'] > 0


if __name__ == "__main__":
    test_weekday_agg_has_7_keys()
    test_agg_values_are_positive()
    print("lesson4 tests passed")
