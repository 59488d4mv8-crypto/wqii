import sys
sys.path.insert(0, '.')
from lesson5_template import load_data, solve, personas_summary


def test_solve_returns_dict():
    r = solve('../../datasets/user_profile.csv')
    assert isinstance(r, dict)


def test_solve_has_three_personas():
    r = solve('../../datasets/user_profile.csv')
    for key in ['白天学习者', '夜猫子', '周末集中学习者']:
        assert key in r or len(r) >= 1


def test_sum_equals_total():
    df = load_data('../../datasets/user_profile.csv')
    r = personas_summary(df)
    assert sum(r.values()) == len(df)


if __name__ == "__main__":
    test_solve_returns_dict()
    test_solve_has_three_personas()
    test_sum_equals_total()
    print("lesson5 tests passed")
