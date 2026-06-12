import sys
sys.path.insert(0, '.')
from exam_template import solve


def test_returns_dict():
    r = solve('../../datasets/conversion_funnel.csv')
    assert isinstance(r, dict)


def test_has_5_channels():
    r = solve('../../datasets/conversion_funnel.csv')
    assert len(r) == 5


def test_each_channel_has_paid_rate():
    r = solve('../../datasets/conversion_funnel.csv')
    for k, v in r.items():
        assert 'paid_conversion_rate' in v
        assert 0 < v['paid_conversion_rate'] <= 1


def test_each_channel_has_bottleneck():
    r = solve('../../datasets/conversion_funnel.csv')
    for k, v in r.items():
        assert 'bottleneck' in v
        assert '_to_' in v['bottleneck']


if __name__ == "__main__":
    test_returns_dict()
    test_has_5_channels()
    test_each_channel_has_paid_rate()
    test_each_channel_has_bottleneck()
    print("exam-p6 passed")
