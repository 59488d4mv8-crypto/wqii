import numpy as np
import pandas as pd


def load_data(reg_path, dau_path):
    reg = pd.read_csv(reg_path)
    dau = pd.read_csv(dau_path)
    return reg, dau


def summarize(reg, dau):
    sample_size = len(reg)
    num_channels = reg['channel'].nunique()
    date_min = reg['date'].min()
    date_max = reg['date'].max()
    return {
        "sample_size": sample_size,
        "num_channels": num_channels,
        "date_min": date_min,
        "date_max": date_max
    }


if __name__ == "__main__":
    reg, dau = load_data('../../datasets/user_registrations.csv',
                         '../../datasets/daily_active.csv')
    s = summarize(reg, dau)
    print(s)
