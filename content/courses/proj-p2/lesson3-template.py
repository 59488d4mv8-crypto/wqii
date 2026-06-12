import numpy as np
import pandas as pd


def chapter_dropout_rate(df):
    return df.groupby('chapter_id')['is_dropout'].mean()


def lowest_completion_chapter(df):
    r = chapter_dropout_rate(df)
    return r.idxmax(), float(r.max())


if __name__ == "__main__":
    df = pd.read_csv('../../datasets/lesson_progress.csv')
    print(chapter_dropout_rate(df))
    print(lowest_completion_chapter(df))
