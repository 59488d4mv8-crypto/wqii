import numpy as np
import pandas as pd


def load_rfm(path):
    return pd.read_csv(path)


def stats(df):
    return {
        "n_users": int(len(df)),
        "avg_recency": float(df['last_learn_days'].mean()),
        "avg_frequency": float(df['sessions'].mean()),
        "avg_monetary": float(df['total_learn_minutes'].mean())
    }


if __name__ == "__main__":
    df = load_rfm('../../datasets/rfm_data.csv')
    print(stats(df))
