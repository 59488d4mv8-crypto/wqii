import pandas as pd


def load_data(path):
    df = pd.read_csv(path)
    return df


def build_baskets(df):
    return df.groupby('user_id')['course_id'].apply(set).tolist()


def count_1_itemsets(baskets):
    counts = {}
    for b in baskets:
        for item in b:
            counts[frozenset([item])] = counts.get(frozenset([item]), 0) + 1
    return counts


def frequent_1_itemsets(baskets, min_support=0.1):
    counts = count_1_itemsets(baskets)
    total = len(baskets)
    return {itemset: c / total for itemset, c in counts.items() if c / total >= min_support}


if __name__ == "__main__":
    df = load_data('../../datasets/course_baskets.csv')
    baskets = build_baskets(df)
    freq1 = frequent_1_itemsets(baskets, min_support=0.1)
    print("1-itemsets 频繁项集:", len(freq1))
    for itemset, support in list(freq1.items())[:5]:
        print(set(itemset), round(support, 3))
