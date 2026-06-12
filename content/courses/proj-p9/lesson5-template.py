import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load_data(path):
    return pd.read_csv(path)


def min_max_normalize(series):
    mn = series.min()
    mx = series.max()
    if mx == mn:
        return [0.0] * len(series)
    return [(v - mn) / (mx - mn) for v in series]


def prepare_radar(df, top_n=5):
    cols = ['avg_rating', 'completion_rate', 'interaction_rate', 'review_count']
    normalized = {col: min_max_normalize(df[col]) for col in cols}
    norm_df = pd.DataFrame(normalized)
    norm_df['teacher_id'] = df['teacher_id']
    norm_df['score'] = norm_df[cols].mean(axis=1)
    top = norm_df.sort_values('score', ascending=False).head(top_n)
    return top, cols


def plot_radar(top, cols):
    num_vars = len(cols)
    angles = [n / float(num_vars) * 2 * 3.14159 for n in range(num_vars)]
    angles += angles[:1]
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'polar': True})
    for _, row in top.iterrows():
        values = [row[c] for c in cols]
        values += values[:1]
        ax.plot(angles, values, label=row['teacher_id'])
        ax.fill(angles, values, alpha=0.1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(cols)
    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
    return fig


if __name__ == "__main__":
    df = load_data('../../datasets/teacher_metrics.csv')
    top, cols = prepare_radar(df, top_n=5)
    print(top)
