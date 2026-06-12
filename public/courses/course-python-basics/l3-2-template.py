import pandas as pd
import os

def solve():
    """
    Pandas 练习：
    1. 读取 datasets/sales_sample.csv
    2. 返回 (行数, 列数, amount 列的总和, amount 列最高的那一行的 region)
    """
    data_dir = os.path.join(os.path.dirname(__file__), "..", "..", "datasets")
    csv_path = os.path.join(data_dir, "sales_sample.csv")
    df = pd.read_csv(csv_path)
    rows, cols = df.shape
    total = float(df["amount"].sum())
    top_row = df.loc[df["amount"].idxmax()]
    top_region = top_row["region"]
    return (rows, cols, total, top_region)


if __name__ == "__main__":
    print(solve())
