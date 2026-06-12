import numpy as np
import pandas as pd


def test_equal_width_shape():
    xs = pd.Series(range(100))
    out = equal_width_bins(xs, 4)
    assert len(out) == 100
    assert out.nunique() <= 4


def test_equal_freq_bins():
    xs = pd.Series(range(100))
    out = equal_freq_bins(xs, 4)
    # 理想等频：每箱约 25 个
    counts = pd.Series(list(out)).value_counts()
    assert counts.min() >= 20


def test_bin_with_labels():
    xs = pd.Series([10, 25, 45, 70])
    out = bin_with_labels(xs, [0, 30, 60, 120], ["young", "mid", "old"])
    out = list(out)
    assert out[0] == "young"
    assert out[2] == "mid"


def test_cross_feature_length():
    a = pd.Series(["A", "B", "A", "B"])
    b = pd.Series(["X", "Y", "Y", "X"])
    out = cross_feature(a, b)
    assert len(out) == 4


def test_cross_feature_content():
    a = pd.Series(["A", "B"])
    b = pd.Series(["X", "Y"])
    out = list(cross_feature(a, b))
    assert out[0] in ("A_X", "A-X", "AX")


if __name__ == "__main__":
    test_equal_width_shape()
    test_equal_freq_bins()
    test_bin_with_labels()
    test_cross_feature_length()
    test_cross_feature_content()
    print("All tests passed!")
