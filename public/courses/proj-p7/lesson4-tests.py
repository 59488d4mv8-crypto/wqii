import sys
sys.path.insert(0, '.')
from lesson4_template import load_data, build_baskets, apriori


def test_apriori_returns_dict():
    df = load_data('../../datasets/course_baskets.csv')
    baskets = build_baskets(df)
    freq = apriori(baskets, min_support=0.1, max_k=4)
    assert isinstance(freq, dict)
    assert 1 in freq


def test_apriori_itemsets_have_support_in_01():
    df = load_data('../../datasets/course_baskets.csv')
    baskets = build_baskets(df)
    freq = apriori(baskets, min_support=0.1, max_k=4)
    for k, itemsets in freq.items():
        for itemset, support in itemsets.items():
            assert 0 < support <= 1


def test_apriori_k_is_valid():
    df = load_data('../../datasets/course_baskets.csv')
    baskets = build_baskets(df)
    freq = apriori(baskets, min_support=0.1, max_k=4)
    for k, itemsets in freq.items():
        for itemset in itemsets.keys():
            assert len(itemset) == k


if __name__ == "__main__":
    test_apriori_returns_dict()
    test_apriori_itemsets_have_support_in_01()
    test_apriori_k_is_valid()
    print("lesson4 tests passed")
