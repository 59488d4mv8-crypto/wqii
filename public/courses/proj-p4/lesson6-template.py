import pandas as pd
from collections import Counter
import sys
sys.path.insert(0, '.')
from lesson2_template import tokenize


def positive_negative_keywords(df, topn=10):
    good = df[df['rating'] >= 4]['text'].fillna('')
    bad = df[df['rating'] <= 2]['text'].fillna('')

    good_tokens = []
    for t in good:
        good_tokens.extend(tokenize(str(t)))
    bad_tokens = []
    for t in bad:
        bad_tokens.extend(tokenize(str(t)))

    good_top = [w for w, _ in Counter(good_tokens).most_common(topn)]
    bad_top = [w for w, _ in Counter(bad_tokens).most_common(topn)]
    return {"positive": good_top, "negative": bad_top}


if __name__ == "__main__":
    df = pd.read_csv('../../datasets/course_reviews.csv')
    print(positive_negative_keywords(df, 10))
