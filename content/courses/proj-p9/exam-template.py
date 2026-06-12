import pandas as pd


def load_data(path):
    return pd.read_csv(path)


def min_max_normalize(series):
    mn = series.min()
    mx = series.max()
    if mx == mn:
        return [0.0] * len(series)
    return [(v - mn) / (mx - mn) for v in series]


def solve(path, weights=None):
    if weights is None:
        weights = {'avg_rating': 0.3, 'completion_rate': 0.3, 'interaction_rate': 0.25, 'review_count': 0.15}
    df = load_data(path)
    cols = list(weights.keys())
    normalized = {col: min_max_normalize(df[col]) for col in cols}
    result = {}
    for i in range(len(df)):
        score = round(sum(normalized[col][i] * weights[col] for col in cols), 4)
        result[df.loc[i, 'teacher_id']] = score
    return result


if __name__ == "__main__":
    print(solve('../../datasets/teacher_metrics.csv'))
