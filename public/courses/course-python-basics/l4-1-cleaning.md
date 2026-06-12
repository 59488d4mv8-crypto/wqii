# 缺失值、重复值与异常值

真实业务数据常常不干净。本章学习如何识别并处理这些问题。

## 识别缺失值

```python
import pandas as pd
import numpy as np

data = {
    "name": ["小明", "小红", None, "小丽"],
    "age": [20, np.nan, 22, 19],
    "score": [85, 90, None, 88]
}
df = pd.DataFrame(data)

print(df.isna())          # 逐元素 True/False
print(df.isna().sum())    # 每列缺失数
print(df.isna().sum() / len(df) * 100)  # 缺失百分比
```

## 处理缺失值

**删除**：适用于缺失占比很小的行或列。

```python
df_dropped = df.dropna()            # 删除任何含缺失值的行
df_col_dropped = df.dropna(axis=1)  # 删除任何含缺失值的列
```

**填充**：用均值、中位数或前/后值填充。

```python
df_filled = df.fillna({"age": df["age"].mean(), "score": df["score"].median()})
df_ffill = df.fillna(method="ffill")  # 前向填充
df_bfill = df.fillna(method="bfill")  # 后向填充
```

## 重复值

```python
dupes = df.duplicated()       # 每行是否与之前重复
print(dupes.sum())            # 重复行数
df_unique = df.drop_duplicates()
```

## 异常值（IQR 方法）

```python
data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 100])
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
clean = data[(data >= lower) & (data <= upper)]
print(f"正常值范围: [{lower:.1f}, {upper:.1f}]")
print("异常值:", data[(data < lower) | (data > upper)].values)
```

## Z-Score 方法

```python
mean = data.mean()
std = data.std()
z = (data - mean) / std
print("|Z| > 3 的异常值:", data[z.abs() > 3].values)
```
