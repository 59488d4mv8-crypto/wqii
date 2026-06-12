import numpy as np

# simulate_binomial(n, p, trials) 应返回 (samples, mean, std)
# simulate_normal(mu, sigma, trials) 应返回 (samples, mean, std)
# compute_z_scores(xs) 应返回标准化后的数组
# plot_binom / plot_normal 应返回 matplotlib figure 对象


def test_binomial_size():
    np.random.seed(42)
    samples, m, s = simulate_binomial(10, 0.5, 1000)
    assert len(samples) == 1000


def test_binomial_mean():
    np.random.seed(42)
    samples, m, s = simulate_binomial(10, 0.5, 5000)
    # E[X] = n*p = 5
    assert 4.5 <= m <= 5.5


def test_normal_simple_normal_mean_std():
    np.random.seed(42)
    samples, m, s = simulate_normal(0, 1, 5000)
    assert -0.2 <= m <= 0.2
    assert 0.8 <= s <= 1.2


def test_z_scores():
    z = compute_z_scores([10, 20, 30, 40, 50])
    assert abs(z[0] - (-1.4142) < 0.01
    assert abs(z[-1] - 1.4142) < 0.01


def test_figures():
    fig1 = plot_binom(10, 0.5, 500)
    fig2 = plot_normal(0, 1, 500)
    assert fig1 is not None
    assert fig2 is not None


if __name__ == "__main__":
    test_binomial_size()
    test_binomial_mean()
    test_normal_mean_std()
    test_z_scores()
    test_figures()
    print("All tests passed!")
