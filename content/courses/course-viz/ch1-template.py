import numpy as np
import matplotlib.pyplot as plt


def create_subplots(nrows, ncols, figsize=(10, 6)):
    # TODO: 创建 nrows x ncols 的子图，返回 (fig, axes)
    pass


def set_title_and_labels(ax, title, xlabel, ylabel):
    # TODO: 在给定 ax 上设置 title / xlabel / ylabel，返回 ax
    pass


def add_line_plot(ax, x, y, color="#4C72B0", label="line"):
    # TODO: 在 ax 上画折线，并加 label，返回 ax
    pass


def add_bar_chart(ax, categories, values, colors=None):
    # TODO: 在 ax 上画柱状图，返回 ax
    pass


def add_legend(ax):
    # TODO: 给 ax 添加图例，返回 ax
    pass


if __name__ == "__main__":
    fig, axes = create_subplots(1, 2)
    add_line_plot(axes[0], [1,2,3,4], [1,4,9,16], label="quadratic")
    set_title_and_labels(axes[0], "Line Plot", "x", "y")
    add_legend(axes[0])
    add_bar_chart(axes[1], ["A","B","C","D"], [3,7,5,8])
    set_title_and_labels(axes[1], "Bar Chart", "category", "value")
    plt.tight_layout()
    plt.show()
