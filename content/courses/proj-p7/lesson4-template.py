import pandas as pd
from itertools import combinations


def load_data(path):
    return pd.read_csv(path)


def build_baskets(df):
    return df.groupby('user_id')['course_id'].apply(set).tolist()


def get_support(itemset, baskets):
    count = sum(1 for b in baskets if itemset.issubset(b))
    return count / len(baskets)


def join_and_prune(prev_frequent, k):
    candidates = set()
    itemsets = list(prev_frequent)
    for i in range(len(itemsets)):
        for j in range(i + 1, len(itemsets)):
            a, b = itemsets[i], itemsets[j]
            union = a | b
            if len(union) == k:
                candidates.add(frozenset(union))
    return candidates


def apriori(baskets, min_support=0.1, max_k=4):
    frequent = {}
    counts1 = {}
    for b in baskets:
        for item in b:
            counts1[frozenset([item])] = counts1.get(frozenset([item]), 0) + 1
    total = len(baskets)
    freq1 = {itemset: c / total for itemset, c in counts1.items() if c / total >= min_support}
    frequent[1] = freq1

    for k in range(2, max_k + 1):
        if k - 1 not in frequent or len(frequent[k - 1]) < 2:
            break
        candidates = join_and_prune(list(frequent[k - 1].keys()), k)
        cur = {}
        for cand in candidates:
            sup = get_support(cand, baskets)
            if sup >= min_support:
                cur[cand] = sup
        if cur:
            frequent[k] = cur
        else:
            break
    return frequent


if __name__ == "__main__":
    df = load_data('../../datasets/course_baskets.csv')
    baskets = build_baskets(df)
    freq = apriori(baskets, min_support=0.1, max_k=4)
    for k, itemsets in freq.items():
        print(f"k={k}: {len(itemsets)} itemsets")
