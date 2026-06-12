import numpy as np
import pandas as pd


def load_behavior(path):
    return pd.read_csv(path)


def overview(df):
    return {
        "n": int(len(df)),
        "avg_duration": float(df['duration_min'].mean()),
        "avg_pause": float(df['pause_count'].mean()),
        "avg_seek": float(df['seek_count'].mean()),
        "avg_score": float(df['quiz_score'].mean())
    }


if __name__ == "__main__":
    df = load_behavior('../../datasets/study_behavior.csv')
    print(overview(df))
