import numpy as np
import pandas as pd


def hour_distribution(reg):
    return reg.groupby('hour')['user_id'].count().sort_index()


def peak_hour(reg):
    d = hour_distribution(reg)
    return d.index[int(np.argmax(d.values))]


if __name__ == "__main__":
    reg = pd.read_csv('../../datasets/user_registrations.csv')
    print(hour_distribution(reg))
    print("peak:", peak_hour(reg))
