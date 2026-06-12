import numpy as np
import pandas as pd


def dau_stats(dau):
    total = dau.groupby('date')['dau'].sum()
    return {
        "mean": float(total.mean()),
        "max": int(total.max())
    }


def wau(dau):
    daily = dau.groupby('date')['dau'].sum()
    return int(daily.rolling(7).sum().mean())


def mau(dau):
    daily = dau.groupby('date')['dau'].sum()
    return int(daily.rolling(30).sum().mean())


if __name__ == "__main__":
    dau = pd.read_csv('../../datasets/daily_active.csv')
    print("DAU stats:", dau_stats(dau))
    print("WAU approx:", wau(dau))
    print("MAU approx:", mau(dau))
