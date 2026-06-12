import numpy as np


def chi_square(table):
    # TODO: 计算卡方统计量、自由度 df、期望频数 expected
    # 返回 (chi2, df, expected)
    pass


def cramers_v(table):
    # TODO: 计算 Cramer's V 效应量
    # 公式: V = sqrt(chi2 / (total * min(r-1, c-1)))
    pass


def ab_test_significant(control_conv, control_total,
                        test_conv, test_total):
    # TODO: 给定两组转化数据，构造列联表并判断是否显著
    # 返回 (chi2, p_approx, significant_bool)
    # p_approx 可用 chi2 查表近似：chi2 > 3.84 (df=1) 视为显著 (p<0.05)
    pass


if __name__ == "__main__":
    table = [[45, 955], [60, 940]]
    chi2, df, expected = chi_square(table)
    print("chi2 =", chi2, "df =", df)
    print("expected:\n", expected)
    print("Cramer's V =", cramers_v(table))
    print(ab_test_significant(45, 1000, 60, 1000))
