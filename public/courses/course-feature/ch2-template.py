import numpy as np
import pandas as pd


def iqr_bounds(xs):
    # TODO: 返回 (lower, upper) 使用 Q1 - 1.5*IQR, Q3 + 1.5*IQR
    pass


def iqr_outliers(xs):
    # TODO: 返回 xs 中的异常值组成的数组
    pass


def zscore_outliers(xs, threshold=2):
    # TODO: 返回超出 |z| > threshold 的异常值数组
    pass


def cap_outliers(xs):
    # TODO: 将 xs 中超出 IQR 上下界的值盖帽，返回 Series 或数组
    pass


if __name__ == "__main__":
    xs = pd.Series([10, 12, 14, 15, 16, 18, 20, 22, 24, 1000])
    print("bounds:", iqr_bounds(xs))
    print("outliers (iqr):", iqr_outliers(xs))
    print("outliers (zscore):", zscore_outliers(xs))
    print("capped:", cap_outliers(xs))
