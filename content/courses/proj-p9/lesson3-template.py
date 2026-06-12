import pandas as pd


def load_data(path):
    return pd.read_csv(path)


def min_max_normalize(series):
    mn = series.min()
    mx = series.max()
    if mx == mn:
        return [0.0] * len(series)
    return [(v - mn) / (mx - mn) for v in series]


def equal_weight_score(df):
    cols = ['avg_rating', 'completion_rate', 'interaction_rate', 'review_count']
    normalized = {}
    for col in cols:
        normalized[col] = min_max_normalize(df[col])
    scores = []
    for i in range(len(df)):
        s = sum(normalized[col][i] for col in cols) / len(cols)
        scores.append(round(s, 4))
    return scores


def weighted_score(df, weights=None):
    if weights is None:
        weights = {'avg_rating': 0.3, 'completion_rate': 0.3, 'interaction_rate': 0.25, 'review_count': 0.15}
    cols = list(weights.keys())
    normalized = {}
    for col in cols:
        normalized[col] = min_max_normalize(df[col])
    scores = []
    for i in range(len(df)):
        s = sum(normalized[col][i] * weights[col] for col in cols)
        scores.append(round(s, 4))
    return scores


if __name__ == "__main__":
    df = load_data('../../datasets/teacher_metrics.csv')
    df['equal_score'] = equal_weight_score(df)
    df['weighted_score'] = weighted_score(df)
    print(df[['teacher_id', 'equal_score', 'weighted_score']].head())
