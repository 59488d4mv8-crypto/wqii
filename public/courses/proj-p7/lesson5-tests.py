import sys
sys.path.insert(0, '.')
from lesson5_template import load_data, build_baskets, apriori, generate_rules


def test_generate_rules_is_list():
    df = load_data('../../datasets/course_baskets.csv')
    baskets = build_baskets(df)
    freq = apriori(baskets, min_support=0.1, max_k=4)
    rules = generate_rules(freq, min_confidence=0.3)
    assert isinstance(rules, list)


def test_rules_have_valid_keys():
    df = load_data('../../datasets/course_baskets.csv')
    baskets = build_baskets(df)
    freq = apriori(baskets, min_support=0.1, max_k=4)
    rules = generate_rules(freq, min_confidence=0.3)
    for r in rules:
        assert 'antecedent' in r
        assert 'consequent' in r
        assert 'support' in r
        assert 'confidence' in r
        assert 'lift' in r


def test_confidence_in_range():
    df = load_data('../../datasets/course_baskets.csv')
    baskets = build_baskets(df)
    freq = apriori(baskets, min_support=0.1, max_k=4)
    rules = generate_rules(freq, min_confidence=0.3)
    for r in rules:
        assert 0 <= r['confidence'] <= 1
        assert r['lift'] > 0


if __name__ == "__main__":
    test_generate_rules_is_list()
    test_rules_have_valid_keys()
    test_confidence_in_range()
    print("lesson5 tests passed")
