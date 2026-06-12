import sys
sys.path.insert(0, '.')
from lesson4_template import load_data, age_bins, cross_analysis


def test_cross_analysis_keys_are_age_groups():
    df = load_data('../../datasets/user_profile.csv')
    df = age_bins(df)
    cross = cross_analysis(df)
    assert len(cross) > 0


def test_cross_analysis_values_are_dicts():
    df = load_data('../../datasets/user_profile.csv')
    df = age_bins(df)
    cross = cross_analysis(df)
    for k, v in cross.items():
        assert isinstance(v, dict)
        assert len(v) > 0


def test_cross_analysis_sum_equals_total():
    df = load_data('../../datasets/user_profile.csv')
    df = age_bins(df)
    cross = cross_analysis(df)
    total = sum(sum(inner.values()) for inner in cross.values())
    assert total == len(df)


if __name__ == "__main__":
    test_cross_analysis_keys_are_age_groups()
    test_cross_analysis_values_are_dicts()
    test_cross_analysis_sum_equals_total()
    print("lesson4 tests passed")
