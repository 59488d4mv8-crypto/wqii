import pandas as pd


def load_data(path):
    df = pd.read_csv(path)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date').reset_index(drop=True)
    df['weekday'] = df['date'].dt.dayofweek
    return df


def weekday_agg(df):
    return df.groupby('weekday')[['pv', 'uv', 'orders']].mean().to_dict(orient='index')


if __name__ == "__main__":
    df = load_data('../../datasets/daily_traffic.csv')
    agg = weekday_agg(df)
    for k, v in agg.items():
        print(f"weekday={k}: {v}")
