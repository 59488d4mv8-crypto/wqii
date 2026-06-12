import numpy as np
import pandas as pd


def linear_fit(xs, ys, degree=1):
    coef = np.polyfit(xs, ys, degree)
    return float(coef[0]), float(coef[1])


def fit_score_by_duration(df):
    x = df['duration_min'].values.astype(float)
    y = df['quiz_score'].values.astype(float)
    slope, intercept = linear_fit(x, y, 1)
    return {"slope": slope, "intercept": intercept}


if __name__ == "__main__":
    df = pd.read_csv('../../datasets/study_behavior.csv')
    print(fit_score_by_duration(df))
