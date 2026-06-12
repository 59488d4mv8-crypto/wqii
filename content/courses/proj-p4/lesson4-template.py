import pandas as pd
import sys
sys.path.insert(0, '.')
from lesson3_template import top_words


def word_frequency_data(df, topn=10):
    words = top_words(df, topn=topn)
    return {w: int(c) for w, c in words}


if __name__ == "__main__":
    df = pd.read_csv('../../datasets/course_reviews.csv')
    print(word_frequency_data(df, 10))
