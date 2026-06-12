import numpy as np
import pandas as pd

# count_missing(df, col) -> int
# fill_numeric_with_median(df, col) -> DataFrame
# fill_categorical_with_mode(df, col) -> DataFrame
# flag_missing(df, col) -> DataFrame (新增 col_is_null 列)
# dropna_rows(df) -> DataFrame


def sample_df():
    return pd.DataFrame({
        "age": [22, 25, np.nan, 35, np.nan, 45, 28],
        "income": [30000, np.nan, 50000, np.nan, 70000, 80000, 55000],
        "city": ["BJ", np.nan, "SH", "BJ", np.nan, "GZ", "BJ"]
    })


def test_count_missing():
    df = sample_df()
    assert count_missing(df, "age") == 2
    assert count_missing(df, "city") == 2


def test_fill_numeric():
    df = sample_df()
    out = fill_numeric_with_median(df.copy(), "age")
    assert out["age"].isna().sum() == 0


def test_fill_categorical():
    df = sample_df()
    out = fill_categorical_with_mode(df.copy(), "city")
    assert out["city"].isna().sum() == 0


def test_flag_missing():
    df = sample_df()
    out = flag_missing(df.copy(), "age")
    assert "age_is_null" in out.columns
    assert out["age_is_null"].sum() == 2


def test_dropna():
    df = sample_df()
    out = dropna_rows(df.copy())
    assert out.isna().sum().sum() == 0


if __name__ == "__main__":
    test_count_missing()
    test_fill_numeric()
    test_fill_categorical()
    test_flag_missing()
    test_dropna()
    print("All tests passed!")
