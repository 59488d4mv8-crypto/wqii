# 第 3 章 分箱与交叉特征

分箱（binning）是将连续数值切分到多个区间（箱）的过程，能提高模型稳定性，也能让业务分析更直观。

## 一、等距分箱 (pd.cut)

```python
import pandas as pd

ages = pd.Series([18, 22, 30, 45, 55, 60, 70])
bins = [0, 25, 40, 60, 120]
labels = ["青年", "中年", "中老年", "老年"]
age_binned = pd.cut(ages, bins=bins, labels=labels)
print(age_binned)
```

## 二、等频分箱 (pd.qcut)

按分位数切分，保证每个箱子样本量相同：

```python
pd.qcut(ages, q=3, labels=["低", "中", "高")
```

## 三、交叉特征 (Cross Features)

两个分箱后的变量可以与其他类别变量做 **交叉** 成新变量：

```python
df = pd.DataFrame({
    "age_bin": ["青年", "中年", "青年", "老年", "中年"],
    "city":    ["BJ", "SH", "BJ", "GZ", "SH"]
})

df["age_x_city"] = df["age_bin"] + "_" + df["city"]
print(df)
```

## 四、完整示例

```python
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    "income": np.random.randint(1000, 50000, 200),
    "spend":  np.random.randint(50, 3000, 200)
})

df["income_bin"] = pd.qcut(df["income"], 4, labels=["Q1","Q2","Q3","Q4"])
df["spend_bin"]  = pd.cut(df["spend"], 3, labels=["低","中","高"])
df["cross"] = df["income_bin"].astype(str) + "_" + df["spend_bin"].astype(str)
print(df["cross"].value_counts())
```

## 五、小结

- **pd.cut**：按固定区间分箱，适合阈值驱动的业务场景；**pd.qcut**：按分位数分箱，适合保证等频。
- **交叉特征**能捕捉变量的组合效应。
