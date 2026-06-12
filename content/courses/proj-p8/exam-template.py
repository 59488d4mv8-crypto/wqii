import pandas as pd


def load_data(path):
    df = pd.read_csv(path)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date').reset_index(drop=True)
    return df


def solve(path, target_col='pv', next_days=7, window=7):
    df = load_data(path)
    daily_mean = round(float(df[target_col].mean()), 2)
    values = list(df[target_col])
    predictions = []
    current = list(values)
    for i in range(next_days):
        recent = current[-window:]
        pred = sum(recent) / len(recent)
        predictions.append(round(pred, 2))
        current.append(pred)
    return {
        'daily_mean': daily_mean,
        'next_7_days': predictions
    }


if __name__ == "__main__":
    print(solve('../../datasets/daily_traffic.csv', target_col='pv'))
