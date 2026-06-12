import pandas as pd


def load_data(path):
    return pd.read_csv(path)


def min_max_normalize(series):
    mn = series.min()
    mx = series.max()
    if mx == mn:
        return [0.0] * len(series)
    return [round((v - mn) / (mx - mn), 4) for v in series]


def z_score_normalize(series):
    mean = sum(series) / len(series)
    variance = sum((v - mean) ** 2 for v in series) / len(series)
    std = variance ** 0.5
    if std == 0:
        return [0.0] * len(series)
    return [round((v - mean) / std, 4) for v in series]


if __name__ == "__main__":
    df = load_data('../../datasets/teacher_metrics.csv')
    print("Min-Max avg_rating:", min_max_normalize(df['avg_rating']))
    print("Z-Score avg_rating:", z_score_normalize(df['avg_rating']))
