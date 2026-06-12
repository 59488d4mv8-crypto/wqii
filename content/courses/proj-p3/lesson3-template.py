import numpy as np
import pandas as pd


def rfm_score(df):
    d = df.copy()
    d['R'] = pd.qcut(d['last_learn_days'], 5, labels=[5, 4, 3, 2, 1], duplicates='drop').astype(int)
    d['F'] = pd.qcut(d['sessions'], 5, labels=[1, 2, 3, 4, 5], duplicates='drop').astype(int)
    d['M'] = pd.qcut(d['total_learn_minutes'], 5, labels=[1, 2, 3, 4, 5], duplicates='drop').astype(int)
    return d


def avg_scores(df):
    d = rfm_score(df)
    return {
        "avg_R": float(d['R'].mean()),
        "avg_F": float(d['F'].mean()),
        "avg_M": float(d['M'].mean())
    }


if __name__ == "__main__":
    df = pd.read_csv('../../datasets/rfm_data.csv')
    s = rfm_score(df)
    print(s.head())
    print(avg_scores(df))
