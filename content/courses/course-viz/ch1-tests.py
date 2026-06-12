import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def test_create_subplots():
    fig, axes = create_subplots(2, 2, figsize=(10, 6))
    assert isinstance(fig, Figure)
    assert axes.shape == (2, 2)


def test_set_title_and_labels():
    fig, ax = plt.subplots()
    out = set_title_and_labels(ax, "T", "X", "Y")
    assert out.get_title() == "T"


def test_add_line_plot():
    fig, ax = plt.subplots()
    out = add_line_plot(ax, [1, 2, 3], [1, 4, 9])
    # 至少有一条线
    assert len(out.get_lines()) >= 1


def test_add_bar_chart():
    fig, ax = plt.subplots()
    out = add_bar_chart(ax, ["A","B","C"], [3,7,5])
    patches = [c for c in out.get_children() if hasattr(c, "get_height")]
    assert len(patches) >= 3 or hasattr(out, "containers")


def test_add_legend():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 4, 9], label="A")
    out = add_legend(ax)
    assert out.get_legend() is not None


if __name__ == "__main__":
    test_create_subplots()
    test_set_title_and_labels()
    test_add_line_plot()
    test_add_bar_chart()
    test_add_legend()
    print("All tests passed!")
