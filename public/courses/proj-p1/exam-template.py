import numpy as np
import pandas as pd


def top3_channel_dau_mean(dau_path):
    dau = pd.read_csv(dau_path)
    channel_mean = dau.groupby('channel')['dau'].mean()
    top3 = channel_mean.sort_values(ascending=False).head(3)
    return {str(k): float(round(v, 2)) for k, v in top3.items()}


if __name__ == "__main__":
    result = top3_channel_dau_mean('../../datasets/daily_active.csv')
    print(result)
