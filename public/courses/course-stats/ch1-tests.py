import numpy as np
import pandas as pd

# 学生提交的代码应当定义以下函数：
# mean(xs), median(xs), sample_variance(xs), percentile(xs, p), summary(data)


def test_basic():
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    assert abs(mean(data) - 55.0) < 1e-6


def test_median():
    data = [3, 1, 2, 5, 4]
    assert median(data) == 3.0


def test_variance():
    data = [10, 20, 30, 40, 50]
    assert abs(sample_variance(data) - 250.0) < 1e-3


def test_percentile():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    q50 = percentile(data, 50)
    assert 4.5 <= q50 <= 5.5


def test_summary():
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    s = summary(data)
    assert isinstance(s, dict)
    assert "mean" in s and "median" in s and "q50" in s
    assert abs(s["mean"] - 55.0) < 1e-3


if __name__ == "__main__":
    test_basic()
    test_median()
    test_variance()
    test_percentile()
    test_summary()
    print("All tests passed!")
