import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

def solve():
    """
    综合项目：销售数据分析
    1. 读取 datasets/sales_sample.csv
    2. 计算总销售额、平均单笔金额
    3. 找出销售额最高的 region
    4. 找出销售额最高的产品（按 product 聚合）
    5. 绘制 region 分组柱状图并保存
    6. 返回字典 {"total_sales": X, "avg_amount": Y, "top_region": Z, "top_product": W, "num_orders": N}
    """
    data_dir = os.path.join(os.path.dirname(__file__), "..", "..", "datasets")
    df = pd.read_csv(os.path.join(data_dir, "sales_sample.csv"))

    total_sales = float(df["amount"].sum())
    avg_amount = float(df["amount"].mean())
    num_orders = int(df.shape[0])

    by_region = df.groupby("region")["amount"].sum()
    top_region = by_region.idxmax()

    by_product = df.groupby("product")["amount"].sum()
    top_product = by_product.idxmax()

    plt.figure(figsize=(8, 4))
    by_region.sort_values(ascending=False).plot(kind="bar", color="#1f77b4")
    plt.title("各区域销售额")
    plt.ylabel("金额（元）")
    plt.tight_layout()
    plt.savefig(os.path.join(os.path.dirname(__file__), "exam-output.png"))
    plt.close()

    return {
        "total_sales": total_sales,
        "avg_amount": avg_amount,
        "top_region": top_region,
        "top_product": top_product,
        "num_orders": num_orders
    }


if __name__ == "__main__":
    result = solve()
    for k, v in result.items():
        print(f"{k}: {v}")
