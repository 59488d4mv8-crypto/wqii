import sys
sys.path.insert(0, '.')
from lesson6_template import solve


def test_solve_returns_list():
    r = solve('../../datasets/course_baskets.csv', min_support=0.1, min_confidence=0.3, top_n=5)
    assert isinstance(r, list)


def test_solve_rules_valid():
    r = solve('../../datasets/course_baskets.csv', min_support=0.1, min_confidence=0.3, top_n=5)
    for rule in r:
        assert 'antecedent' in rule
        assert 'consequent' in rule


def test_solve_at_most_top_n():
    r = solve('../../datasets/course_baskets.csv', min_support=0.1, min_confidence=0.3, top_n=5)
    assert len(r) <= 5


if __name__ == "__main__":
    test_solve_returns_list()
    test_solve_rules_valid()
    test_solve_at_most_top_n()
    print("lesson6 tests passed")
