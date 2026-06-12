import numpy as np
import pandas as pd


def top_corr_with_score(path, topn=3):
    df = pd.read_csv(path)
    numeric_cols = [c for c in df.columns if c != 'quiz_score' and pd.api.types.is_numeric_dtype(df[c])]
    corr_scores = {}
    for c in numeric_cols:
        corr_scores[c] = float(df[c].corr(df['quiz_score']))
    sorted_items = sorted(corr_scores.items(), key=lambda kv: abs(kv[1]), reverse=True)
    return [name for name, _ in sorted_items[:topn]]


if __name__ == "__main__":
    print(top_corr_with_score('../../datasets/study_behavior.csv', 3))
