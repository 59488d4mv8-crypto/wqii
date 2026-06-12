import numpy as np
import matplotlib.pyplot as plt


def simulate_binomial(n, p, trials):
    # TODO: 使用 np.random.binomial 生成 trials 个样本，返回 (samples, mean, std)
    pass


def simulate_normal(mu, sigma, trials):
    # TODO: 生成 trials 个 N(mu, sigma^2) 样本，返回 (samples, mean, std)
    pass


def compute_z_scores(xs):
    # TODO: 对 xs 做 z-score 标准化，返回标准化后的数组
    pass


def plot_binom(n, p, trials):
    # TODO: 绘制二项分布直方图，并返回 fig 对象
    pass


def plot_normal(mu, sigma, trials):
    # TODO: 绘制正态分布直方图，并返回 fig 对象
    pass


if __name__ == "__main__":
    s_bin, m_bin, std_bin = simulate_binomial(10, 0.5, 1000)
    print("binom mean:", m_bin, "std:", std_bin)
    s_norm, m_norm, std_norm = simulate_normal(0, 1, 1000)
    print("normal mean:", m_norm, "std:", std_norm)
    print("z-score demo:", compute_z_scores([10, 20, 30, 40, 50]))
