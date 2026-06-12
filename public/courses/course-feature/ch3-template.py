import numpy as np
import pandas as pd


def equal_width_bins(xs, n_bins):
    # TODO: 使用 pd.cut 把 xs 分成 n_bins 个等宽箱，返回分箱结果（Series or Categorical）
    pass


def equal_freq_bins(xs, n_bins):
    # TODO: 使用 pd.qcut 把 xs 分成 n_bins 个等频箱
    pass


def bin_with_labels(xs, bins, labels):
    # TODO: 用给定 bins 和 labels 分箱
    pass


def cross_feature(a, b):
    # TODO: 对两个列做交叉特征（字符串拼接），返回 Series
    pass


if __name__ == "__main__":
    xs = pd.Series([18, 22, 30, 45, 55, 60, 70, 80, 90, 100])
    print(equal_width_bins(xs, 3))
    print(equal_freq_bins(xs, 3))
    print(bin_with_labels(xs, [0, 30, 60, 120], ["young", "mid", "old"]))
    print(cross_feature(pd.Series(["A","B","A","B"]), pd.Series(["X","Y","Y","X"])))
