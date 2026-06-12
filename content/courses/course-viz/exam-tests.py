import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# build_sales_dashboard(csv_path) -> fig (2x2 subplots, 4 charts)


def test_returns_figure():
    fig = build_sales_dashboard("../../datasets/sales_sample.csv")
    assert isinstance(fig, Figure)


def test_has_four_axes():
    fig = build_sales_dashboard("../../datasets/sales_sample.csv")
    axes = fig.get_axes()
    assert len(axes) >= 4


def test_subplots_is_2x2():
    fig = build_sales_dashboard("../../datasets/sales_sample.csv")
    axes = fig.get_axes()
    # 判断确实在一个网格里
    assert len(axes) == 4


def test_has_at_least_one_pie():
    fig = build_sales_dashboard("../../datasets/sales_sample.csv")
    has_pie = False
    for ax in fig.get_axes():
        # 饼图会创建 Wedge 对象
        for child in ax.get_children():
            cls = type(child).__name__
            if "Wedge" in cls:
                has_pie = True
                break
        if has_pie:
            break
    assert has_pie, "四个子图中应该包含饼图"


def test_has_heatmap_like_image():
    fig = build_sales_dashboard("../../datasets/sales_sample.csv")
    has_image = False
    for ax in fig.get_axes():
        if len(ax.images) > 0:
            has_image = True
            break
    assert has_image, "四个子图中应该包含 imshow 绘制的热力图"


if __name__ == "__main__":
    test_returns_figure()
    test_has_four_axes()
    test_subplots_is_2x2()
    test_has_at_least_one_pie()
    test_has_heatmap_like_image()
    print("All exam tests passed!")
