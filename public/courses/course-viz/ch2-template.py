import matplotlib.pyplot as plt


def funnel_chart(stages, values, title="销售漏斗", colors=None):
    # TODO: 用横向 bar 画漏斗图，反转 y 轴，并在柱子末端标注"数量 (百分比)"
    # 返回 (fig, ax)
    pass


def compute_conversion_rates(values):
    # TODO: 返回每个环节相对第一个环节的转化率（0~1 之间的列表）
    pass


def compute_step_rates(values):
    # TODO: 返回每个环节相对前一环节的转化率（第一个为 1）
    pass


if __name__ == "__main__":
    stages = ["访问", "注册", "下单", "支付"]
    values = [10000, 5000, 2000, 800]
    print("整体转化率:", compute_conversion_rates(values))
    print("逐环节转化率:", compute_step_rates(values))
    fig, ax = funnel_chart(stages, values)
    plt.show()
