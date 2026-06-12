import sys
sys.path.insert(0, '.')
from exam_template import solve


def test_returns_dict():
    r = solve('../../datasets/teacher_metrics.csv')
    assert isinstance(r, dict)


def test_keys_are_teacher_ids():
    r = solve('../../datasets/teacher_metrics.csv')
    assert len(r) == 20


def test_scores_in_range():
    r = solve('../../datasets/teacher_metrics.csv')
    for k, v in r.items():
        assert 0 <= v <= 1


if __name__ == "__main__":
    test_returns_dict()
    test_keys_are_teacher_ids()
    test_scores_in_range()
    print("exam-p9 passed")
