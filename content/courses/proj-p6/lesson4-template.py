import pandas as pd


def load_data(path):
    df = pd.read_csv(path)
    return df


def per_step_rates(df):
    stage_order = ['view', 'trial', 'add_cart', 'purchase', 'complete']
    counts = df.groupby('stage')['user_count'].sum().reindex(stage_order)
    rates = {}
    for i in range(1, len(stage_order)):
        prev = counts.iloc[i - 1]
        cur = counts.iloc[i]
        rates[f"{stage_order[i - 1]}_to_{stage_order[i]}"] = round(cur / prev, 4)
    return rates


def solve(df):
    rates = per_step_rates(df)
    bottleneck = min(rates, key=lambda k: rates[k])
    return bottleneck


if __name__ == "__main__":
    df = load_data('../../datasets/conversion_funnel.csv')
    print("单步转化率:", per_step_rates(df))
    print("卡点节点:", solve(df))
