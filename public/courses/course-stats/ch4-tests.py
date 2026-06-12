import numpy as np

# chi_square(table) -> (chi2, df, expected)
# cramers_v(table) -> float
# ab_test_significant(control_conv, control_total, test_conv, test_total) -> (chi2, p_approx, bool)


def test_chi2_shape():
    table = [[45, 955], [60, 940]]
    chi2, df, expected = chi_square(table)
    assert df == 1
    assert expected.shape == (2, 2)


def test_expected_sum():
    table = [[45, 955], [60, 940]]
    chi2, df, expected = chi_square(table)
    assert abs(expected.sum() - 2000) < 1e-3


def test_chi2_positive():
    table = [[45, 955], [60, 940]]
    chi2, df, expected = chi_square(table)
    assert chi2 > 0


def test_cramers_v_range():
    table = [[45, 955], [60, 940]]
    v = cramers_v(table)
    assert 0 <= v <= 1


def test_ab_test_detection():
    # 大差异应显著
    chi2, p, sig = ab_test_significant(50, 1000, 100, 1000)
    assert sig is True


if __name__ == "__main__":
    test_chi2_shape()
    test_expected_sum()
    test_chi2_positive()
    test_cramers_v_range()
    test_ab_test_detection()
    print("All tests passed!")
