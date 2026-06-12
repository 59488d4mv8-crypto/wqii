import numpy as np
import pandas as pd


def mean(xs):
    # TODO: 计算列表 xs 的均值并返回
    pass


def median(xs):
    # TODO: 计算列表 xs 的中位数并返回
    pass


def sample_variance(xs):
    # TODO: 计算列表 xs 的样本方差（除以 n-1）并返回
    pass


def percentile(xs, p):
    # TODO: 计算列表 xs 的第 p 百分位数（p 取值 0~100）并返回
    pass


def summary(data):
    # TODO: 返回一个字典，键为 mean/median/std/q25/q50/q75
    pass


if __name__ == "__main__":
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print("mean:", mean(data))
    print("median:", median(data))
    print("var:", sample_variance(data))
    print("p25:", percentile(data, 25))
    print("summary:", summary(data))
