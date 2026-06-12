import numpy as np
import pandas as pd


def retention_curve(reg, days=30):
    total = len(reg)
    curve = []
    for d in range(1, days + 1):
        cnt = (reg['active_days'] >= d).sum()
        curve.append(round(float(cnt) / total, 4))
    return curve


if __name__ == "__main__":
    reg = pd.read_csv('../../datasets/user_registrations.csv')
    print(retention_curve(reg)[:10])
