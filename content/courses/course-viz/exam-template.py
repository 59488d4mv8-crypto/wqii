import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def build_sales_dashboard(csv_path):
    # TODO: 读取 sales_sample.csv（region, product, qty, amount, date），
    # 创建一个 2x2 的子图网格，绘制 4 个子图：
    #   1. 左上：按 region 汇总的 amount 柱状图
    #   2. 右上：按 product 汇总的 qty 折线图
    #   3. 左下：各 region 的 qty 占比饼图
    #   4. 右下：按 product × region 的热力图（用 pivot_table + imshow）
    # 返回包含 4 个子图的 fig 对象（matplotlib Figure）
    df = pd.read_csv(csv_path)
    # 你的实现写在这里
    pass


if __name__ == "__main__":
    fig = build_sales_dashboard("../../datasets/sales_sample.csv")
    if fig is not None:
        plt.tight_layout()
        plt.show()
