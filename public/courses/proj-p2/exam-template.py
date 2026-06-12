import numpy as np
import pandas as pd


def top3_dropout_chapters(df_path):
    df = pd.read_csv(df_path)
    rates = df.groupby('chapter_id')['is_dropout'].mean().sort_values(ascending=False)
    return list(rates.head(3).index)


if __name__ == "__main__":
    print(top3_dropout_chapters('../../datasets/lesson_progress.csv'))
