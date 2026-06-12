import pandas as pd


def load_data(path):
    return pd.read_csv(path)


def min_max_normalize(series):
    mn = series.min()
    mx = series.max()
    if mx == mn:
        return [0.0] * len(series)
    return [(v - mn) / (mx - mn) for v in series]


def weighted_score(df, weights=None):
    if weights is None:
        weights = {'avg_rating': 0.3, 'completion_rate': 0.3, 'interaction_rate': 0.25, 'review_count': 0.15}
    cols = list(weights.keys())
    normalized = {col: min_max_normalize(df[col]) for col in cols}
    scores = []
    for i in range(len(df)):
        scores.append(sum(normalized[col][i] * weights[col] for col in cols))
    return scores


def solve(path, top_n=5):
    df = load_data(path)
    scores = weighted_score(df)
    df['score'] = scores
    ranked = df.sort_values('score', ascending=False).reset_index(drop=True)
    return [ranked.loc[i, 'teacher_id'] for i in range(min(top_n, len(ranked)))]


if __name__ == "__main__":
    print("Top 5 教师:", solve('../../datasets/teacher_metrics.csv'))
