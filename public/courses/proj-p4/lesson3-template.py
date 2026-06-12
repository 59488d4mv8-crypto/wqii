import pandas as pd
from collections import Counter
import sys
sys.path.insert(0, '.')
from lesson2_template import tokenize


def top_words(df, topn=10):
    tokens = []
    for text in df['text'].fillna(''):
        tokens.extend(tokenize(str(text)))
    cnt = Counter(tokens)
    return cnt.most_common(topn)


if __name__ == "__main__":
    df = pd.read_csv('../../datasets/course_reviews.csv')
    print(top_words(df, 10))
