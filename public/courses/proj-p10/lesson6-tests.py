import sys
sys.path.insert(0, '.')
from lesson6_template import solve, strategy_matrix


def test_solve_returns_dict():
    r = solve('../../datasets/user_profile.csv')
    assert isinstance(r, dict)


def test_solve_has_counts_and_strategies():
    r = solve('../../datasets/user_profile.csv')
    assert 'counts' in r
    assert 'strategies' in r


def test_strategy_matrix_has_three_keys():
    s = strategy_matrix()
    assert '白天学习者' in s
    assert '夜猫子' in s
    assert '周末集中学习者' in s
    for k, v in s.items():
        assert isinstance(v, list)
        assert len(v) > 0


if __name__ == "__main__":
    test_solve_returns_dict()
    test_solve_has_counts_and_strategies()
    test_strategy_matrix_has_three_keys()
    print("lesson6 tests passed")
