import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

def solve():
    """
    Matplotlib 练习：
    1. 绘制 sales_sample.csv 的按 region 分组的 amount 柱状图
    2. 返回 (top_region, 第二高的 region, 总销售额)
    """
    data_dir = os.path.join(os.path.dirname(__file__), "..", "..", "datasets")
    df = pd.read_csv(os.path.join(data_dir, "sales_sample.csv"))

    by_region = df.groupby("region")["amount"].sum().sort_values(ascending=False)
    regions = by_region.index.tolist()
    amounts = by_region.values.tolist()

    plt.figure(figsize=(8, 4))
    plt.bar(regions, amounts, color="#1f77b4")
    plt.title("各区域销售总额")
    plt.ylabel("金额（元）")
    plt.tight_layout()
    plt.savefig(os.path.join(os.path.dirname(__file__), "l6-2-output.png"))
    plt.close()

    total = float(sum(amounts))
    top_region = regions[0]
    second_region = regions[1] if len(regions) > 1 else None
    return (top_region, second_region, total)


if __name__ == "__main__":
    print(solve())
