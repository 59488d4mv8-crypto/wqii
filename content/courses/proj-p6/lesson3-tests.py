import sys
sys.path.insert(0, '.')
from lesson3_template import load_data, channel_funnel, channel_conversion_rate


def test_channel_funnel_shape():
    df = load_data('../../datasets/conversion_funnel.csv')
    pivot = channel_funnel(df)
    assert pivot.shape == (5, 5)


def test_channel_conversion_rate_positive():
    df = load_data('../../datasets/conversion_funnel.csv')
    rates = channel_conversion_rate(df)
    for k, v in rates.items():
        assert 0 < v <= 1


def test_channel_conversion_rate_keys():
    df = load_data('../../datasets/conversion_funnel.csv')
    rates = channel_conversion_rate(df)
    assert 'organic' in rates
    assert 'paid' in rates


if __name__ == "__main__":
    test_channel_funnel_shape()
    test_channel_conversion_rate_positive()
    test_channel_conversion_rate_keys()
    print("lesson3 tests passed")
