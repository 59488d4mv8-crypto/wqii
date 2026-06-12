from itertools import combinations


def build_toy_baskets():
    return [
        {'A', 'B', 'C'},
        {'A', 'B', 'D'},
        {'A', 'B', 'C', 'D'},
        {'B', 'C', 'D'},
        {'A', 'C', 'D'},
        {'A', 'B'},
        {'B', 'C'},
        {'C', 'D'},
        {'A', 'D'},
        {'A', 'B', 'C'}
    ]


def get_support(itemset, baskets):
    count = sum(1 for b in baskets if itemset.issubset(b))
    return count / len(baskets)


def apriori(baskets, min_support=0.2, max_k=4):
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
        itemsets_list = list(frequent[k - 1].keys())
        candidates = set()
        for i in range(len(itemsets_list)):
            for j in range(i + 1, len(itemsets_list)):
                union = itemsets_list[i] | itemsets_list[j]
                if len(union) == k:
                    candidates.add(frozenset(union))
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


def generate_rules(frequent, min_confidence=0.3):
    rules = []
    for k, itemsets in frequent.items():
        if k < 2:
            continue
        for itemset, sup_itemset in itemsets.items():
            items = list(itemset)
            for r in range(1, len(items)):
                for comb in combinations(items, r):
                    antecedent = frozenset(comb)
                    consequent = itemset - antecedent
                    if len(antecedent) in frequent and antecedent in frequent[len(antecedent)]:
                        sup_antecedent = frequent[len(antecedent)][antecedent]
                    else:
                        continue
                    conf = sup_itemset / sup_antecedent
                    if conf < min_confidence:
                        continue
                    if len(consequent) in frequent and consequent in frequent[len(consequent)]:
                        sup_consequent = frequent[len(consequent)][consequent]
                    else:
                        continue
                    if sup_consequent == 0:
                        continue
                    lift = conf / sup_consequent
                    rules.append({
                        'antecedent': set(antecedent),
                        'consequent': set(consequent),
                        'support': sup_itemset,
                        'confidence': conf,
                        'lift': lift
                    })
    return rules


def solve(min_support=0.2, min_confidence=0.3, top_n=5):
    baskets = build_toy_baskets()
    freq = apriori(baskets, min_support=min_support, max_k=4)
    rules = generate_rules(freq, min_confidence=min_confidence)
    rules_sorted = sorted(rules, key=lambda r: r['lift'], reverse=True)
    return rules_sorted[:top_n]


if __name__ == "__main__":
    print(solve())
