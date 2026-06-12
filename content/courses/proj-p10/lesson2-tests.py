import sys
sys.path.insert(0, '.')
from lesson2_template import load_data, count_distribution, age_bins


def test_count_distribution_gender():
    df = load_data('../../datasets/user_profile.csv')
    d = count_distribution(df, 'gender')
    assert 'M' in d or 'F' in d
    assert sum(d.values()) == len(df)


def test_count_distribution_city():
    df = load_data('../../datasets/user_profile.csv')
    d = count_distribution(df, 'city')
    assert len(d) > 0
    assert sum(d.values()) == len(df)


def test_age_bins_creates_age_group():
    df = load_data('../../datasets/user_profile.csv')
    df = age_bins(df)
    assert 'age_group' in df.columns


if __name__ == "__main__":
    test_count_distribution_gender()
    test_count_distribution_city()
    test_age_bins_creates_age_group()
    print("lesson2 tests passed")
