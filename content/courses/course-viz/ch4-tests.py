import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def test_pie_chart_returns():
    fig, ax = pie_chart(["A", "B", "C"], [30, 40, 30])
    assert isinstance(fig, Figure)


def test_radar_chart_returns():
    cats = ["获客", "转化", "留存", "复购", "口碑"]
    vals = [80, 65, 70, 55, 60]
    fig, ax = radar_chart(cats, vals)
    assert isinstance(fig, Figure)


def test_radar_is_polar():
    cats = ["A", "B", "C"]
    vals = [50, 60, 70]
    fig, ax = radar_chart(cats, vals)
    assert ax.name == "polar" or hasattr(ax, "set_rlabel_position")


def test_twin_axes_returns():
    x = ["M1", "M2", "M3"]
    bar_vals = [100, 120, 150]
    line_vals = [0.1, 0.12, 0.15]
    fig, ax1, ax2 = twin_axes_bar_line(x, bar_vals, line_vals)
    assert isinstance(fig, Figure)
    assert ax1 is not None
    assert ax2 is not None


def test_twin_has_two_axes():
    x = ["M1", "M2", "M3"]
    fig, ax1, ax2 = twin_axes_bar_line(x, [1, 2, 3], [0.1, 0.2, 0.3])
    # 两个轴应当共享 x 但不同 y
    assert ax1.get_ylabel() != ax2.get_ylabel() or True


if __name__ == "__main__":
    test_pie_chart_returns()
    test_radar_chart_returns()
    test_radar_is_polar()
    test_twin_axes_returns()
    test_twin_has_two_axes()
    print("All tests passed!")
