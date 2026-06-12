import numpy as np
import pandas as pd


def test_iqr_bounds_range():
    xs = pd.Series([10, 12, 14, 15, 16, 18, 20, 22, 24, 1000])
    lower, upper = iqr_bounds(xs)
    assert lower < upper


def test_iqr_outliers_contains_big_value():
    xs = pd.Series([10, 12, 14, 15, 16, 18, 20, 22, 24, 1000])
    outs = iqr_outliers(xs)
    assert 1000 in list(outs)


def test_zscore_outliers_contains_big_value():
    xs = pd.Series([10, 12, 14, 15, 16, 18, 20, 22, 24, 1000])
    outs = zscore_outliers(xs, threshold=2)
    assert 1000 in list(outs)


def test_cap_outliers_no_extreme():
    xs = pd.Series([10, 12, 14, 15, 16, 18, 20, 22, 24, 1000])
    capped = cap_outliers(xs)
    # 盖帽后最大值不能超过原来 upper 上界
    _, upper = iqr_bounds(xs)
    assert max(capped) <= upper + 1e-6


def test_cap_length_preserved():
    xs = pd.Series([10, 12, 14, 15, 16, 18, 20, 22, 24, 1000])
    capped = cap_outliers(xs)
    assert len(capped) == 10


if __name__ == "__main__":
    test_iqr_bounds_range()
    test_iqr_outliers_contains_big_value()
    test_zscore_outliers_contains_big_value()
    test_cap_outliers_no_extreme()
    test_cap_length_preserved()
    print("All tests passed!")
