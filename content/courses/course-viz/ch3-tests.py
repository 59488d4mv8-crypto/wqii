import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def test_heatmap_returns_fig_ax():
    data = np.random.rand(4, 5)
    fig, ax = heatmap(data)
    assert isinstance(fig, Figure)


def test_heatmap_shape_preserved():
    data = np.random.rand(3, 4)
    fig, ax = heatmap(data)
    # imshow 的图像应存在
    assert len(ax.images) >= 1


def test_correlation_heatmap():
    df = pd.DataFrame({
        "a": [1,2,3,4,5],
        "b": [2,4,5,4,6],
        "c": [5,4,3,2,1]
    })
    fig, ax, corr = correlation_heatmap(df)
    assert corr.shape == (3, 3)
    assert isinstance(fig, Figure)


def test_simple_sankey():
    flows = [100, -40, -60]
    labels = ["In", "A", "B"]
    fig, ax = simple_sankey(flows, labels)
    assert isinstance(fig, Figure)


def test_sankey_shape():
    flows = [100, -30, -70]
    labels = ["Total", "A", "B"]
    fig, ax = simple_sankey(flows, labels)
    assert fig is not None


if __name__ == "__main__":
    test_heatmap_returns_fig_ax()
    test_heatmap_shape_preserved()
    test_correlation_heatmap()
    test_simple_sankey()
    test_sankey_shape()
    print("All tests passed!")
