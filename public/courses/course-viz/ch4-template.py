import numpy as np
import matplotlib.pyplot as plt


def pie_chart(labels, sizes, title="Pie Chart"):
    # TODO: 绘制饼图，返回 (fig, ax)
    pass


def radar_chart(categories, values, title="Radar Chart"):
    # TODO: 绘制雷达图（polar=True），返回 (fig, ax)
    # 需要闭合 angles 和 values
    pass


def twin_axes_bar_line(x, bar_vals, line_vals, title="Twin Axes"):
    # TODO: 绘制双轴图：左轴 bar，右轴 line，返回 (fig, ax1, ax2)
    pass


if __name__ == "__main__":
    pie_chart(["A","B","C"], [30, 40, 30])
    radar_chart(["获客","转化","留存","复购","口碑"], [80, 65, 70, 55, 60])
    twin_axes_bar_line(["M1","M2","M3"], [100,120,150], [0.1,0.12,0.15])
    plt.show()
