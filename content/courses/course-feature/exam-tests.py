import numpy as np
import pandas as pd

# clean_feature_csv(csv_path) -> DataFrame (已清洗、做分箱与 one-hot)


def test_returns_dataframe():
    result = clean_feature_csv("../../datasets/feature_sample.csv")
    assert isinstance(result, pd.DataFrame)


def test_shape_enlarged():
    result = clean_feature_csv("../../datasets/feature_sample.csv")
    # 原始 5 列，新增分箱和 one-hot 后应超过 5 列
    assert result.shape[1] > 5


def test_no_nan_in_numeric():
    result = clean_feature_csv("../../datasets/feature_sample.csv")
    for col in ["age", "income"]:
        if col in result.columns:
            assert result[col].isna().sum() == 0, col + " 还存在 NaN"


def test_has_age_bin_column():
    result = clean_feature_csv("../../datasets/feature_sample.csv")
    cols = list(result.columns)
    found = any("age" in c.lower() and ("bin" in c.lower() or "bucket" in c.lower() or "cut" in c.lower()) for c in cols)
    assert found, "未发现 age 分箱相关列: " + str(cols)


def test_has_income_binned_column():
    result = clean_feature_csv("../../datasets/feature_sample.csv")
    cols = list(result.columns)
    found = any("income" in c.lower() and ("bin" in c.lower() or "bucket" in c.lower() or "q" in c.lower()) for c in cols)
    assert found, "未发现 income 分箱相关列: " + str(cols)


def test_has_one_hot_columns():
    result = clean_feature_csv("../../datasets/feature_sample.csv")
    cols = list(result.columns)
    # one-hot 列名通常形如 city_xxx
    found = any("city" in c.lower() and "_" in c for c in cols)
    assert found, "未发现 city one-hot 列: " + str(cols)


if __name__ == "__main__":
    test_returns_dataframe()
    test_shape_enlarged()
    test_no_nan_in_numeric()
    test_has_age_bin_column()
    test_has_income_binned_column()
    test_has_one_hot_columns()
    print("All exam tests passed!")
