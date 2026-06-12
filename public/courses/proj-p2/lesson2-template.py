import numpy as np
import pandas as pd


def chapter_funnel(df):
    return df.groupby('chapter_id')['user_id'].count().sort_index()


def completion_rate(df):
    r = df.groupby('chapter_id').apply(
        lambda x: float((x['progress'] >= 0.8).sum()) / len(x),
        include_groups=False
    )
    return r


if __name__ == "__main__":
    df = pd.read_csv('../../datasets/lesson_progress.csv')
    print(chapter_funnel(df))
    print(completion_rate(df))
