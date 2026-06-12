import sys
sys.path.insert(0, '.')
from lesson2_template import load_data, build_baskets


def test_baskets_is_list():
    df = load_data('../../datasets/course_baskets.csv')
    baskets = build_baskets(df)
    assert isinstance(baskets, list)


def test_baskets_elements_are_sets():
    df = load_data('../../datasets/course_baskets.csv')
    baskets = build_baskets(df)
    for b in baskets:
        assert isinstance(b, set)
        assert len(b) >= 1


def test_baskets_count():
    df = load_data('../../datasets/course_baskets.csv')
    baskets = build_baskets(df)
    assert len(baskets) > 50


if __name__ == "__main__":
    test_baskets_is_list()
    test_baskets_elements_are_sets()
    test_baskets_count()
    print("lesson2 tests passed")
