import pandas as pd
import matplotlib.pyplot as plt


def load_data(path):
    return pd.read_csv(path)


def age_bins(df, bins=None):
    if bins is None:
        bins = [0, 20, 30, 40, 50, 100]
        labels = ['<20', '20-29', '30-39', '40-49', '50+']
    else:
        labels = [f'{bins[i]}-{bins[i + 1] - 1}' for i in range(len(bins) - 1)]
    df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)
    return df


def plot_pie(df, col):
    counts = df[col].value_counts()
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(counts.values, labels=counts.index, autopct='%1.1f%%')
    ax.set_title(f'{col} 分布')
    return fig


def plot_bar(df, col):
    counts = df[col].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(counts.index.astype(str), counts.values)
    ax.set_title(f'{col} 分布')
    return fig


if __name__ == "__main__":
    df = load_data('../../datasets/user_profile.csv')
    df = age_bins(df)
    print("gender counts:", df['gender'].value_counts().to_dict())
    print("age_group counts:", df['age_group'].value_counts().sort_index().to_dict())
