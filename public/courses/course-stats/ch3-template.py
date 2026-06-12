import numpy as np
from math import erf, sqrt


def t_test_ind(a, b):
    # TODO: 计算两个独立样本的 t 统计量和自由度 df
    # 返回 (t_stat, df)
    pass


def normal_approx_pvalue(t_stat):
    # TODO: 使用正态分布近似计算双尾 p 值
    # 提示：p = 1 - erf(|t| / sqrt(2))
    pass


def is_significant(a, b, alpha=0.05):
    # TODO: 判断两组数据差异是否显著，返回 (t, p, significant_bool)
    pass


if __name__ == "__main__":
    np.random.seed(42)
    a = np.random.normal(100, 15, 30)
    b = np.random.normal(108, 15, 30)
    t, df = t_test_ind(a, b)
    p = normal_approx_pvalue(t)
    print("t =", t, "df =", df, "p =", p)
    print("significant?", is_significant(a, b))
