import pandas as pd


def load_data(path):
    df = pd.read_csv(path)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date').reset_index(drop=True)
    return df


def detect_outliers(series, threshold=3.0):
    values = list(series)
    mean = sum(values) / len(values)
    variance = sum((v - mean) ** 2 for v in values) / len(values)
    std = variance ** 0.5
    if std == 0:
        return []
    outliers = []
    for i, v in enumerate(values):
        if abs(v - mean) / std > threshold:
            outliers.append((i, v))
    return outliers


def iqr_outliers(series, k=1.5):
    values = sorted(list(series))
    n = len(values)
    q1 = values[int(n * 0.25)]
    q3 = values[int(n * 0.75)]
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    outliers = []
    for i, v in enumerate(series):
        if v < lower or v > upper:
            outliers.append((i, v))
    return outliers


if __name__ == "__main__":
    df = load_data('../../datasets/daily_traffic.csv')
    print("3-sigma 异常点 (pv):", detect_outliers(df['pv'], threshold=3.0)[:10])
    print("IQR 异常点 (pv):", iqr_outliers(df['pv'])[:10])
