import sys
sys.path.insert(0, '.')
from lesson2_template import load_data, funnel_counts, per_step_rates, overall_conversion


def test_funnel_counts():
    df = load_data('../../datasets/conversion_funnel.csv')
    counts = funnel_counts(df)
    assert counts['view'] > counts['trial']
    assert counts['trial'] > counts['add_cart']
    assert counts['add_cart'] > counts['purchase']
    assert counts['purchase'] > counts['complete']


def test_per_step_rates_between_0_and_1():
    df = load_data('../../datasets/conversion_funnel.csv')
    counts = funnel_counts(df)
    rates = per_step_rates(counts)
    for k, v in rates.items():
        assert 0 < v <= 1


def test_overall_conversion():
    df = load_data('../../datasets/conversion_funnel.csv')
    counts = funnel_counts(df)
    overall = overall_conversion(counts)
    assert 0 < overall < 1


def test_5_stages():
    df = load_data('../../datasets/conversion_funnel.csv')
    counts = funnel_counts(df)
    assert len(counts) == 5


if __name__ == "__main__":
    test_funnel_counts()
    test_per_step_rates_between_0_and_1()
    test_overall_conversion()
    test_5_stages()
    print("lesson2 tests passed")
