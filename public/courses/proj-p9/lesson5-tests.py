import sys
sys.path.insert(0, '.')
from lesson5_template import load_data, prepare_radar


def test_prepare_radar_top_n():
    df = load_data('../../datasets/teacher_metrics.csv')
    top, cols = prepare_radar(df, top_n=5)
    assert len(top) == 5


def test_radar_cols_present():
    df = load_data('../../datasets/teacher_metrics.csv')
    top, cols = prepare_radar(df, top_n=5)
    for c in cols:
        assert c in top.columns


def test_radar_values_in_range():
    df = load_data('../../datasets/teacher_metrics.csv')
    top, cols = prepare_radar(df, top_n=5)
    for c in cols:
        for v in top[c]:
            assert 0 <= v <= 1


if __name__ == "__main__":
    test_prepare_radar_top_n()
    test_radar_cols_present()
    test_radar_values_in_range()
    print("lesson5 tests passed")
