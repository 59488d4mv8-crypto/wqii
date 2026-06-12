import pandas as pd


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


def cross_analysis(df, row_col='age_group', col_col='prefer_subject'):
    crosstab = pd.crosstab(df[row_col], df[col_col])
    result = {}
    for r in crosstab.index:
        result[str(r)] = {str(c): int(crosstab.loc[r, c]) for c in crosstab.columns}
    return result


if __name__ == "__main__":
    df = load_data('../../datasets/user_profile.csv')
    df = age_bins(df)
    cross = cross_analysis(df)
    for k, v in cross.items():
        print(k, v)
