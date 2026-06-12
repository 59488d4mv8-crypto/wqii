import pandas as pd
import matplotlib.pyplot as plt


def load_data(path):
    df = pd.read_csv(path)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date').reset_index(drop=True)
    return df


def summary(df):
    return {
        'n_days': len(df),
        'date_min': df['date'].min().strftime('%Y-%m-%d'),
        'date_max': df['date'].max().strftime('%Y-%m-%d'),
        'pv_mean': round(float(df['pv'].mean()), 2),
        'uv_mean': round(float(df['uv'].mean()), 2),
        'orders_mean': round(float(df['orders'].mean()), 2)
    }


def plot_trend(df):
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df['date'], df['pv'], label='PV')
    ax.plot(df['date'], df['uv'], label='UV')
    ax.plot(df['date'], df['orders'], label='Orders')
    ax.legend()
    ax.set_title('时间序列趋势图')
    return fig


if __name__ == "__main__":
    df = load_data('../../datasets/daily_traffic.csv')
    print(summary(df))
