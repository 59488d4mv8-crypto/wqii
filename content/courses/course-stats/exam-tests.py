import numpy as np

# analyze_ab_test(csv_path) -> dict with keys:
#   control_rate, test_rate, lift, chi2, p, significant


def test_result_is_dict():
    result = analyze_ab_test("../../datasets/ab_test.csv")
    assert isinstance(result, dict)


def test_has_required_keys():
    result = analyze_ab_test("../../datasets/ab_test.csv")
    for key in ["control_rate", "test_rate", "lift", "chi2", "p", "significant"]:
        assert key in result, "缺少 key: " + key


def test_rates_valid():
    result = analyze_ab_test("../../datasets/ab_test.csv")
    assert 0 <= result["control_rate"] <= 1
    assert 0 <= result["test_rate"] <= 1


def test_lift_positive():
    result = analyze_ab_test("../../datasets/ab_test.csv")
    # 数据集设定：实验组转化率更高
    assert result["lift"] > 0


def test_chi2_positive():
    result = analyze_ab_test("../../datasets/ab_test.csv")
    assert result["chi2"] > 0


def test_p_in_range():
    result = analyze_ab_test("../../datasets/ab_test.csv")
    assert 0 <= result["p"] <= 1


def test_significant_is_bool():
    result = analyze_ab_test("../../datasets/ab_test.csv")
    assert isinstance(result["significant"], bool)


if __name__ == "__main__":
    test_result_is_dict()
    test_has_required_keys()
    test_rates_valid()
    test_lift_positive()
    test_chi2_positive()
    test_p_in_range()
    test_significant_is_bool()
    print("All exam tests passed!")
