import numpy as np
import pandas as pd


def analyze_ab_test(csv_path):
    # TODO: 读取 csv_path 下的 ab_test.csv 文件（列：group, converted, spend）
    # 返回字典：
    #   - control_rate: 对照组转化率
    #   - test_rate:    实验组转化率
    #   - lift:         (test_rate - control_rate) / control_rate
    #   - chi2:         卡方统计量（基于转化/未转化 2x2 列联表）
    #   - p:            基于正态近似的双尾 p 值（使用 chi2 开方后做 z）
    #   - significant:  若 p < 0.05 则为 True，否则 False
    df = pd.read_csv(csv_path)
    # 你的实现写在这里
    pass


if __name__ == "__main__":
    result = analyze_ab_test("../../datasets/ab_test.csv")
    print(result)
