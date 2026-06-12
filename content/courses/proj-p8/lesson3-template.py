import pandas as pd


def load_data(path):
    df = pd.read_csv(path)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date').reset_index(drop=True)
    return df


def rolling_mean(series, window=7):
    values = list(series)
    result = []
    for i in range(len(values)):
        start = max(0, i - window + 1)
        sub = values[start:i + 1]
        result.append(sum(sub) / len(sub))
    return result


if __name__ == "__main__":
    df = load_data('../../datasets/daily_traffic.csv')
    df['pv_ma7'] = rolling_mean(df['pv'], window=7)
    print(df[['date', 'pv', 'pv_ma7']].tail(10))
