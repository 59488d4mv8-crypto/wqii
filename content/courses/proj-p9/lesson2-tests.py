import sys
sys.path.insert(0, '.')
from lesson2_template import load_data, min_max_normalize, z_score_normalize


def test_min_max_in_range():
    df = load_data('../../datasets/teacher_metrics.csv')
    norm = min_max_normalize(df['avg_rating'])
    for v in norm:
        assert 0 <= v <= 1


def test_z_score_mean_near_zero():
    df = load_data('../../datasets/teacher_metrics.csv')
    norm = z_score_normalize(df['avg_rating'])
    assert -1 <= sum(norm) / len(norm) <= 1


def test_min_max_length():
    df = load_data('../../datasets/teacher_metrics.csv')
    norm = min_max_normalize(df['avg_rating'])
    assert len(norm) == len(df)


if __name__ == "__main__":
    test_min_max_in_range()
    test_z_score_mean_near_zero()
    test_min_max_length()
    print("lesson2 tests passed")
