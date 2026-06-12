import sys
sys.path.insert(0, '.')
from lesson6_template import load_data, detect_outliers, iqr_outliers


def test_detect_outliers_returns_list():
    df = load_data('../../datasets/daily_traffic.csv')
    r = detect_outliers(df['pv'], threshold=3.0)
    assert isinstance(r, list)


def test_iqr_outliers_returns_list():
    df = load_data('../../datasets/daily_traffic.csv')
    r = iqr_outliers(df['pv'])
    assert isinstance(r, list)


def test_outlier_values_exist_or_acceptable():
    df = load_data('../../datasets/daily_traffic.csv')
    r = detect_outliers(df['pv'], threshold=2.0)
    if len(r) > 0:
        for idx, v in r:
            assert v > 0


if __name__ == "__main__":
    test_detect_outliers_returns_list()
    test_iqr_outliers_returns_list()
    test_outlier_values_exist_or_acceptable()
    print("lesson6 tests passed")
