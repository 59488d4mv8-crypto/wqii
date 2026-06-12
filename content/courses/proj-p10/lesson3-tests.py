import sys
sys.path.insert(0, '.')
from lesson3_template import load_data, age_bins


def test_age_bins_no_nan():
    df = load_data('../../datasets/user_profile.csv')
    df = age_bins(df)
    assert df['age_group'].isna().sum() == 0


def test_plot_data_exists():
    df = load_data('../../datasets/user_profile.csv')
    counts = df['gender'].value_counts()
    assert len(counts) > 0
    assert counts.sum() == len(df)


if __name__ == "__main__":
    test_age_bins_no_nan()
    test_plot_data_exists()
    print("lesson3 tests passed")
