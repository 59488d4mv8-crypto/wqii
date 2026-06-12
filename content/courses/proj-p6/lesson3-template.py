import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load_data(path):
    df = pd.read_csv(path)
    return df


def channel_funnel(df):
    stage_order = ['view', 'trial', 'add_cart', 'purchase', 'complete']
    pivot = df.pivot(index='stage', columns='channel', values='user_count').reindex(stage_order)
    return pivot


def channel_conversion_rate(df):
    stage_order = ['view', 'trial', 'add_cart', 'purchase', 'complete']
    pivot = df.pivot(index='stage', columns='channel', values='user_count').reindex(stage_order)
    rate = {}
    for ch in pivot.columns:
        rate[ch] = round(pivot.loc['purchase', ch] / pivot.loc['view', ch], 4)
    return rate


def plot_funnel(pivot):
    stages = pivot.index.tolist()
    channels = pivot.columns.tolist()
    x = np.arange(len(stages))
    width = 0.15
    fig, ax = plt.subplots(figsize=(10, 6))
    for i, ch in enumerate(channels):
        ax.bar(x + (i - 2) * width, pivot[ch].values, width, label=ch)
    ax.set_xticks(x)
    ax.set_xticklabels(stages)
    ax.legend()
    ax.set_title('渠道漏斗对比')
    return fig


if __name__ == "__main__":
    df = load_data('../../datasets/conversion_funnel.csv')
    pivot = channel_funnel(df)
    print("各渠道节点计数:\n", pivot)
    print("各渠道付费转化率:\n", channel_conversion_rate(df))
