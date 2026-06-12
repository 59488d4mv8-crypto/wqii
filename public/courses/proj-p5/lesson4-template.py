import numpy as np
import pandas as pd


def scatter_data(df):
    return {
        "x": df['duration_min'].tolist(),
        "y": df['quiz_score'].tolist()
    }


if __name__ == "__main__":
    df = pd.read_csv('../../datasets/study_behavior.csv')
    d = scatter_data(df)
    print("points:", len(d['x']))
