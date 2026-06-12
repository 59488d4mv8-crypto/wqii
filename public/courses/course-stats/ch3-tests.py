import numpy as np

# t_test_ind(a, b) -> (t_stat, df)
# normal_approx_pvalue(t_stat) -> p_value (双尾)
# is_significant(a, b, alpha=0.05) -> (t, p, bool)


def test_t_sign():
    np.random.seed(42)
    a = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    b = np.array([6.0, 7.0, 8.0, 9.0, 10.0])
    t, df = t_test_ind(a, b)
    # a 均值 < b 均值，所以 t 应该为负
    assert t < 0


def test_df():
    a = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    b = np.array([6.0, 7.0, 8.0, 9.0, 10.0])
    t, df = t_test_ind(a, b)
    assert df == 8


def test_p_value_range():
    t = 2.0
    p = normal_approx_pvalue(t)
    assert 0 < p < 1


def test_p_value_small_for_large_t():
    p = normal_approx_pvalue(5.0)
    # z=5 时 p 应该非常小
    assert p < 0.01


def test_significant_detection():
    np.random.seed(42)
    a = np.random.normal(100, 10, 50)
    b = np.random.normal(110, 10, 50)
    t, p, sig = is_significant(a, b, 0.05)
    assert sig is True


if __name__ == "__main__":
    test_t_sign()
    test_df()
    test_p_value_range()
    test_p_value_small_for_large_t()
    test_significant_detection()
    print("All tests passed!")
