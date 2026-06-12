import pandas as pd
import sys
sys.path.insert(0, '.')
from lesson5_template import sentiment_score, avg_sentiment, POS, NEG


def test_score_range():
    s = sentiment_score("这个课程非常好，讲解清晰，推荐！")
    assert s > 0


def test_negative_text():
    s = sentiment_score("这个课程很一般，内容过时，失望")
    assert s < 0


def test_avg_in_range():
    df = pd.read_csv('../../datasets/course_reviews.csv')
    a = avg_sentiment(df)
    assert -1.0 <= a <= 1.0


def test_avg_positive_overall():
    df = pd.read_csv('../../datasets/course_reviews.csv')
    a = avg_sentiment(df)
    assert a > -1.0


if __name__ == "__main__":
    test_score_range()
    test_negative_text()
    test_avg_in_range()
    test_avg_positive_overall()
    print("lesson5 tests passed")
