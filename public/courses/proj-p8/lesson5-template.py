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


def solve(path, target_col='pv', next_days=7, window=7):
    df = load_data(path)
    values = list(df[target_col])
    predictions = []
    current = list(values)
    for _ in range(next_days):
        recent = current[-window:]
        pred = sum(recent) / len(recent)
        predictions.append(round(pred, 2))
        current.append(pred)
    return predictions


if __name__ == "__main__":
    print("下 7 天 pv 预测:", solve('../../datasets/daily_traffic.csv', target_col='pv'))
