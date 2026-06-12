import numpy as np
import pandas as pd


def feature_corr(df):
    # 将分类列数字列与 is_dropout 的相关系数
    num = df[['progress', 'is_dropout']]
    return num.corr()


def progress_dropout_corr(df):
    return float(df['progress'].corr(df['is_dropout']))


if __name__ == "__main__":
    df = pd.read_csv('../../datasets/lesson_progress.csv')
    print(feature_corr(df))
    print(progress_dropout_corr(df))
