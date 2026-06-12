import pandas as pd
import numpy as np
import os

def solve():
    """
    数据清洗练习：
    1. 创建一个 DataFrame：
       name: ["小明", "小红", "小刚", "小丽", "小强"]
       age: [20, None, 22, 19, 21]
       score: [85, np.nan, 90, None, 88]
    2. 返回清洗后的 DataFrame：
       - 用 age 的均值填充 age 缺失值
       - 用 60 填充 score 的缺失值
       - 返回清洗后的行数
    """
    data = {
        "name": ["小明", "小红", "小刚", "小丽", "小强"],
        "age": [20, None, 22, 19, 21],
        "score": [85, np.nan, 90, None, 88]
    }
    df = pd.DataFrame(data)
    df["age"] = df["age"].fillna(df["age"].mean())
    df["score"] = df["score"].fillna(60)
    return (len(df), float(df["age"].mean()), float(df["score"].mean()))


if __name__ == "__main__":
    print(solve())
