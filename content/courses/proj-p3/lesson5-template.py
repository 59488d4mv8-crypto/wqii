import numpy as np
import pandas as pd


def segment_pie_data(df):
    d = df.copy()
    labels = [5, 4, 3, 2, 1]
    d['R'] = pd.qcut(d['last_learn_days'], 5, labels=labels, duplicates='drop').astype(int)
    d['F'] = pd.qcut(d['sessions'], 5, labels=[1, 2, 3, 4, 5], duplicates='drop').astype(int)
    d['M'] = pd.qcut(d['total_learn_minutes'], 5, labels=[1, 2, 3, 4, 5], duplicates='drop').astype(int)

    def row_seg(row):
        r_high = row['R'] >= 3
        f_high = row['F'] >= 3
        m_high = row['M'] >= 3
        prefix = "重要" if r_high else "一般"
        if f_high and m_high:
            return prefix + "价值"
        elif not f_high and m_high:
            return prefix + "保持"
        elif f_high and not m_high:
            return prefix + "发展"
        else:
            return prefix + "挽留"
    d['segment'] = d.apply(row_seg, axis=1)
    return d['segment'].value_counts().to_dict()


if __name__ == "__main__":
    df = pd.read_csv('../../datasets/rfm_data.csv')
    print(segment_pie_data(df))
