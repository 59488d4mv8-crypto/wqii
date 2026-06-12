import pandas as pd
import sys
sys.path.insert(0, '.')
from exam_template import top_corr_with_score


def test_returns_list():
    r = top_corr_with_score('../../datasets/study_behavior.csv', 3)
    assert isinstance(r, list)


def test_has_topn():
    r = top_corr_with_score('../../datasets/study_behavior.csv', 3)
    assert len(r) == 3


def test_items_are_strings():
    r = top_corr_with_score('../../datasets/study_behavior.csv', 3)
    for item in r:
        assert isinstance(item, str)


def test_first_abs_highest():
    df = pd.read_csv('../../datasets/study_behavior.csv')
    r = top_corr_with_score('../../datasets/study_behavior.csv', 3)
    abs_values = {c: abs(float(df[c].corr(df['quiz_score']))) for c in r}
    # r[0] 的 abs 应 >= r[1] >= r[2]
    assert abs_values[r[0]] >= abs_values[r[1]] >= abs_values[r[2]]


if __name__ == "__main__":
    test_returns_list()
    test_has_topn()
    test_items_are_strings()
    test_first_abs_highest()
    print("exam-p5 passed")
