import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def test_funnel_returns_fig_ax():
    stages = ["A", "B", "C"]
    values = [1000, 600, 300]
    fig, ax = funnel_chart(stages, values)
    assert isinstance(fig, Figure)


def test_conversion_rates_bounds():
    values = [10000, 5000, 2000, 800]
    rates = compute_conversion_rates(values)
    assert rates[0] == 1.0
    for r in rates:
        assert 0 <= r <= 1


def test_conversion_length():
    values = [10000, 5000, 2000, 800]
    rates = compute_conversion_rates(values)
    assert len(rates) == len(values)


def test_step_rates_first():
    values = [10000, 5000, 2000, 800]
    rates = compute_step_rates(values)
    assert rates[0] == 1.0
    assert abs(rates[1] - 0.5) < 1e-9


def test_step_rates_length():
    values = [10000, 5000, 2000, 800]
    rates = compute_step_rates(values)
    assert len(rates) == len(values)


if __name__ == "__main__":
    test_funnel_returns_fig_ax()
    test_conversion_rates_bounds()
    test_conversion_length()
    test_step_rates_first()
    test_step_rates_length()
    print("All tests passed!")
