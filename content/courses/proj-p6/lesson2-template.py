import pandas as pd


def load_data(path):
    df = pd.read_csv(path)
    return df


def funnel_counts(df):
    stage_order = ['view', 'trial', 'add_cart', 'purchase', 'complete']
    counts = df.groupby('stage')['user_count'].sum().reindex(stage_order)
    return counts


def per_step_rates(counts):
    rates = {}
    stage_order = counts.index.tolist()
    for i in range(1, len(stage_order)):
        prev = counts.iloc[i - 1]
        cur = counts.iloc[i]
        rates[f"{stage_order[i - 1]}_to_{stage_order[i]}"] = round(cur / prev, 4)
    return rates


def overall_conversion(counts):
    return round(counts.iloc[-1] / counts.iloc[0], 4)


if __name__ == "__main__":
    df = load_data('../../datasets/conversion_funnel.csv')
    counts = funnel_counts(df)
    print("漏斗节点计数:\n", counts)
    print("单步转化率:\n", per_step_rates(counts))
    print("总转化率:", overall_conversion(counts))
