import numpy as np
import pandas as pd


def predict_dropout(df, threshold=0.5):
    return (df['progress'] < threshold).astype(int)


def accuracy(df, threshold=0.5):
    pred = predict_dropout(df, threshold)
    return float((pred == df['is_dropout']).sum()) / len(df)


if __name__ == "__main__":
    df = pd.read_csv('../../datasets/lesson_progress.csv')
    print("acc@0.5:", accuracy(df, 0.5))
    print("acc@0.3:", accuracy(df, 0.3))
