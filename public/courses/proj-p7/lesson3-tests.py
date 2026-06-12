import sys
sys.path.insert(0, '.')
from lesson3_template import load_data, build_baskets, count_1_itemsets, frequent_1_itemsets


def test_count_1_itemsets_keys_are_size_1():
    df = load_data('../../datasets/course_baskets.csv')
    baskets = build_baskets(df)
    counts = count_1_itemsets(baskets)
    for k in counts.keys():
        assert len(k) == 1


def test_frequent_1_itemsets_positive_counts():
    df = load_data('../../datasets/course_baskets.csv')
    baskets = build_baskets(df)
    freq = frequent_1_itemsets(baskets, min_support=0.1)
    for itemset, support in freq.items():
        assert support > 0
        assert support <= 1


def test_frequent_1_itemsets_not_empty():
    df = load_data('../../datasets/course_baskets.csv')
    baskets = build_baskets(df)
    freq = frequent_1_itemsets(baskets, min_support=0.1)
    assert len(freq) > 0


if __name__ == "__main__":
    test_count_1_itemsets_keys_are_size_1()
    test_frequent_1_itemsets_positive_counts()
    test_frequent_1_itemsets_not_empty()
    print("lesson3 tests passed")
