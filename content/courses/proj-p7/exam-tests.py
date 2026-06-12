import sys
sys.path.insert(0, '.')
from exam_template import solve


def test_returns_list():
    r = solve()
    assert isinstance(r, list)


def test_top5_at_most_5():
    r = solve()
    assert len(r) <= 5


def test_each_rule_has_lift():
    r = solve()
    for rule in r:
        assert 'lift' in rule
        assert rule['lift'] > 0


def test_rules_sorted_by_lift_desc():
    r = solve()
    if len(r) >= 2:
        for i in range(1, len(r)):
            assert r[i - 1]['lift'] >= r[i]['lift']


if __name__ == "__main__":
    test_returns_list()
    test_top5_at_most_5()
    test_each_rule_has_lift()
    test_rules_sorted_by_lift_desc()
    print("exam-p7 passed")
