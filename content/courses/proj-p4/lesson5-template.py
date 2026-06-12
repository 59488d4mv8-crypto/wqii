import pandas as pd
import sys
sys.path.insert(0, '.')
from lesson2_template import tokenize

POS = {"好", "不错", "喜欢", "推荐", "清晰", "棒", "赞", "优秀", "满意", "丰富", "实用",
       "值得", "易懂", "简单", "厉害", "超出预期", "好课", "好的", "舒服", "干货"}
NEG = {"差", "烂", "失望", "过时", "枯燥", "困惑", "一般", "不够", "不满", "垃圾",
       "糟糕", "遗憾", "问题", "不懂", "简单", "混乱", "难懂", "乏味", "失望的", "不好"}


def sentiment_score(text):
    tokens = tokenize(text)
    if not tokens:
        return 0.0
    pos = sum(1 for t in tokens if any(p in t for p in POS))
    neg = sum(1 for t in tokens if any(n in t for n in NEG))
    total = len(tokens)
    return float(pos - neg) / total


def avg_sentiment(df):
    scores = [sentiment_score(str(t)) for t in df['text'].fillna('')]
    return float(sum(scores)) / len(scores) if scores else 0.0


if __name__ == "__main__":
    df = pd.read_csv('../../datasets/course_reviews.csv')
    print("avg:", avg_sentiment(df))
