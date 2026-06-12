import sys
sys.path.insert(0, '.')
from lesson3_template import load_data, equal_weight_score, weighted_score


def test_equal_weight_score_length():
    df = load_data('../../datasets/teacher_metrics.csv')
    scores = equal_weight_score(df)
    assert len(scores) == len(df)


def test_equal_weight_score_in_range():
    df = load_data('../../datasets/teacher_metrics.csv')
    scores = equal_weight_score(df)
    for s in scores:
        assert 0 <= s <= 1


def test_weighted_score_positive():
    df = load_data('../../datasets/teacher_metrics.csv')
    scores = weighted_score(df)
    for s in scores:
        assert 0 <= s <= 1


if __name__ == "__main__":
    test_equal_weight_score_length()
    test_equal_weight_score_in_range()
    test_weighted_score_positive()
    print("lesson3 tests passed")
