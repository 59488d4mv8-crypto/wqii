import pandas as pd


def solve(path):
    df = pd.read_csv(path)
    stage_order = ['view', 'trial', 'add_cart', 'purchase', 'complete']
    pivot = df.pivot(index='stage', columns='channel', values='user_count').reindex(stage_order)

    result = {}
    for ch in pivot.columns:
        paid_rate = round(pivot.loc['purchase', ch] / pivot.loc['view', ch], 4)
        rates = {}
        for i in range(1, len(stage_order)):
            prev = pivot.iloc[i - 1][ch]
            cur = pivot.iloc[i][ch]
            rates[f"{stage_order[i - 1]}_to_{stage_order[i]}"] = round(cur / prev, 4)
        bottleneck = min(rates, key=lambda k: rates[k])
        result[ch] = {
            'paid_conversion_rate': paid_rate,
            'bottleneck': bottleneck
        }
    return result


if __name__ == "__main__":
    print(solve('../../datasets/conversion_funnel.csv'))
