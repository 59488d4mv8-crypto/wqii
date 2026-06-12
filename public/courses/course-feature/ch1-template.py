import numpy as np
import pandas as pd


def count_missing(df, col):
    # TODO: 返回指定列中 NaN 的数量
    pass


def fill_numeric_with_median(df, col):
    # TODO: 用 col 的中位数填充该列 NaN，返回修改后的 DataFrame
    pass


def fill_categorical_with_mode(df, col):
    # TODO: 用 col 的众数填充该列 NaN，返回修改后的 DataFrame
    pass


def flag_missing(df, col):
    # TODO: 在 df 中新增 col + "_is_null" 列（0/1）并返回 df
    pass


def dropna_rows(df):
    # TODO: 删掉所有含 NaN 的行，返回结果
    pass


if __name__ == "__main__":
    df = pd.DataFrame({
        "age": [22, 25, np.nan, 35, np.nan, 45, 28],
        "city": ["BJ", np.nan, "SH", "BJ", np.nan, "GZ", "BJ"]
    })
    print(count_missing(df, "age"))
    print(fill_numeric_with_median(df.copy(), "age"))
    print(fill_categorical_with_mode(df.copy(), "city"))
    print(flag_missing(df.copy(), "age"))
    print(dropna_rows(df.copy()))
