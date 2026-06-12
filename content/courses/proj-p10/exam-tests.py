import sys
sys.path.insert(0, '.')
from exam_template import solve


def test_returns_dict():
    r = solve('../../datasets/user_profile.csv')
    assert isinstance(r, dict)


def test_has_persona_counts_and_strategies():
    r = solve('../../datasets/user_profile.csv')
    assert 'persona_counts' in r
    assert 'recommended_strategies' in r


def test_counts_sum_to_total():
    r = solve('../../datasets/user_profile.csv')
    assert sum(r['persona_counts'].values()) > 0


def test_strategies_are_lists():
    r = solve('../../datasets/user_profile.csv')
    for k, v in r['recommended_strategies'].items():
        assert isinstance(v, list)
        assert len(v) > 0


if __name__ == "__main__":
    test_returns_dict()
    test_has_persona_counts_and_strategies()
    test_counts_sum_to_total()
    test_strategies_are_lists()
    print("exam-p10 passed")
