import pandas as pd
import sys
sys.path.insert(0, '.')
from lesson2_template import tokenize
from lesson5_template import POS, NEG


def analyze_reviews(path):
    df = pd.read_csv(path)
    scores = []
    pos_count = 0
    neg_count = 0
    for text in df['text'].fillna(''):
        tokens = tokenize(str(text))
        if not tokens:
            scores.append(0.0)
            continue
        p = sum(1 for t in tokens if any(x in t for x in POS))
        n = sum(1 for t in tokens if any(x in t for x in NEG))
        s = float(p - n) / len(tokens)
        scores.append(s)
        if s > 0:
            pos_count += 1
        elif s < 0:
            neg_count += 1
    avg = float(sum(scores)) / len(scores) if scores else 0.0
    return {"avg_sentiment": avg, "positive_reviews": int(pos_count), "negative_reviews": int(neg_count)}


if __name__ == "__main__":
    print(analyze_reviews('../../datasets/course_reviews.csv'))
