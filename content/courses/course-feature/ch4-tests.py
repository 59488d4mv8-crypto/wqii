import numpy as np
import pandas as pd


def test_label_encode():
    s = pd.Series(["S", "M", "L", "XL"])
    out = label_encode(s, {"S": 0, "M": 1, "L": 2, "XL": 3})
    assert list(out) == [0, 1, 2, 3]


def test_one_hot_shape():
    s = pd.Series(["BJ", "SH", "GZ", "BJ"])
    out = one_hot_encode(s, "city")
    assert out.shape == (4, 3)


def test_one_hot_columns():
    s = pd.Series(["X", "Y", "X", "Z"])
    out = one_hot_encode(s, "type")
    # 至少包含 type_X, type_Y, type_Z 列名
    names = list(out.columns)
    assert any("X" in n for n in names)


def test_freq_encode_range():
    s = pd.Series(["A", "A", "B", "C"])
    out = freq_encode(s)
    vals = list(out)
    for v in vals:
        assert 0 < v <= 1


def test_encode_dataframe():
    df = pd.DataFrame({
        "size": ["S", "M", "L", "XL", "M"],
        "city": ["BJ", "SH", "BJ", "GZ", "SH"]
    })
    out = encode_dataframe(df.copy(), "size", "city", {"S":0,"M":1,"L":2,"XL":3})
    assert "size_label" in out.columns or "size" in out.columns
    # one-hot 至少新增了一列
    assert out.shape[1] > 2


if __name__ == "__main__":
    test_label_encode()
    test_one_hot_shape()
    test_one_hot_columns()
    test_freq_encode_range()
    test_encode_dataframe()
    print("All tests passed!")
