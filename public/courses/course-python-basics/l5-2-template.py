import pandas as pd
import os

def solve():
    """
    分组聚合练习：读取 sales_sample.csv
    1. 按 region 分组，计算每个 region 的 amount 总和、均值、行数
    2. 返回 (top_region, top_sum, 全局均值)
    """
    data_dir = os.path.join(os.path.dirname(__file__), "..", "..", "datasets")
    df = pd.read_csv(os.path.join(data_dir, "sales_sample.csv"))

    agg = df.groupby("region")["amount"].agg(["sum", "mean", "count"])
    top_region = agg["sum"].idxmax()
    top_sum = float(agg["sum"].max())
    global_mean = float(df["amount"].mean())

    return (top_region, top_sum, global_mean)


if __name__ == "__main__":
    print(solve())
