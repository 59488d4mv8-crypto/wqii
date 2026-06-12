import numpy as np
import pandas as pd


def corr_matrix(df):
    cols = ['duration_min', 'pause_count', 'seek_count', 'quiz_score']
    return df[cols].corr()


def score_corr(df):
    m = corr_matrix(df)
    return {
        "duration_vs_score": float(m.loc['duration_min', 'quiz_score']),
        "pause_vs_score": float(m.loc['pause_count', 'quiz_score']),
        "seek_vs_score": float(m.loc['seek_count', 'quiz_score'])
    }


if __name__ == "__main__":
    df = pd.read_csv('../../datasets/study_behavior.csv')
    print(corr_matrix(df))
    print(score_corr(df))
