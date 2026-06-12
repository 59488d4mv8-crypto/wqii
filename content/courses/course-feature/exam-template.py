import numpy as np
import pandas as pd


def clean_feature_csv(csv_path):
    # TODO: 读取 csv_path 下的 feature_sample.csv（列：age, gender, income, city, purchase）
    # 做完整清洗：
    #   1. 数值列缺失值用中位数填充（age, income）
    #   2. 类别列缺失值用众数或 "Unknown" 填充（gender, city）
    #   3. age 分箱为 ["青年","中年","老年"]（使用边界 [0,35,55,200]）
    #   4. income 做等频分箱，分 4 个箱
    #   5. 对 city 做 one-hot 编码
    # 返回：最终清洗后的 DataFrame（应包含所有新列）
    df = pd.read_csv(csv_path)
    # 你的实现写在这里
    pass


if __name__ == "__main__":
    result = clean_feature_csv("../../datasets/feature_sample.csv")
    print("shape:", result.shape)
    print(result.head())
