import numpy as np
import pandas as pd


def pause_groups(df, threshold=5):
    low = df[df['pause_count'] <= threshold]['quiz_score'].tolist()
    high = df[df['pause_count'] > threshold]['quiz_score'].tolist()
    return {"low_pause": low, "high_pause": high}


def group_stats(df, threshold=5):
    g = pause_groups(df, threshold)
    return {
        "low_mean": float(np.mean(g["low_pause"])) if g["low_pause"] else 0.0,
        "high_mean": float(np.mean(g["high_pause"])) if g["high_pause"] else 0.0,
        "low_n": len(g["low_pause"]),
        "high_n": len(g["high_pause"])
    }


if __name__ == "__main__":
    df = pd.read_csv('../../datasets/study_behavior.csv')
    print(group_stats(df, 5))
