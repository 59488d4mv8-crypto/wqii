import numpy as np
import pandas as pd


def channel_counts(reg):
    return reg.groupby('channel')['user_id'].count().sort_values(ascending=False)


def top_channel(reg):
    counts = channel_counts(reg)
    return counts.index[0], counts.iloc[0]


if __name__ == "__main__":
    reg = pd.read_csv('../../datasets/user_registrations.csv')
    print(channel_counts(reg))
    print("top:", top_channel(reg))
