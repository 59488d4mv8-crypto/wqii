import numpy as np
import matplotlib.pyplot as plt


def heatmap(data, row_labels=None, col_labels=None, title="Heatmap", cmap="Blues"):
    # TODO: 用 matplotlib imshow 绘制 data 的热力图，标注数值；
    # row_labels/col_labels 为可选轴标签；返回 (fig, ax)
    pass


def correlation_heatmap(df):
    # TODO: 计算 DataFrame 的相关系数矩阵，返回 (fig, ax, corr_matrix)
    pass


def simple_sankey(flows, labels, title="Sankey"):
    # TODO: 用 matplotlib.sankey.Sankey 绘制简单桑基图（若无 sankey 则退化为 bar 图）
    # 返回 (fig, ax)
    pass


if __name__ == "__main__":
    data = np.random.rand(5, 5)
    fig, ax = heatmap(data, title="Demo Heatmap")
    plt.show()
