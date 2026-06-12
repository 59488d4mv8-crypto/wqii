import pandas as pd


def load_data(path):
    return pd.read_csv(path)


def count_distribution(df, col):
    counts = df[col].value_counts().sort_index()
    return {str(k): int(v) for k, v in counts.items()}


def age_bins(df, bins=None):
    if bins is None:
        bins = [0, 20, 30, 40, 50, 100]
        labels = ['<20', '20-29', '30-39', '40-49', '50+']
    else:
        labels = [f'{bins[i]}-{bins[i + 1] - 1}' for i in range(len(bins) - 1)]
    df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)
    return df


if __name__ == "__main__":
    df = load_data('../../datasets/user_profile.csv')
    df = age_bins(df)
    print("性别分布:", count_distribution(df, 'gender'))
    print("城市分布:", count_distribution(df, 'city'))
    print("偏好学科分布:", count_distribution(df, 'prefer_subject'))
    print("年龄分组:", count_distribution(df, 'age_group'))
