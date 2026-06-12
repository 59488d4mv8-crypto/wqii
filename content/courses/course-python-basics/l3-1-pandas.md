# Series 与 DataFrame

Pandas 是 Python 中最流行的数据分析库，核心是两种数据结构：**Series**（一维）和 **DataFrame**（二维表格）。

## Series

带索引（label）的一维数组。

```python
import pandas as pd

s = pd.Series([80, 75, 90, 88], index=["小明", "小红", "小刚", "小丽"])
print(s)
print(s["小明"])        # 80
print(s.mean())         # 83.25
print(s[s > 80])        # 筛选 > 80 的
```

## DataFrame

类似 Excel 表格，由行索引（index）和列（columns）组成。

```python
data = {
    "name": ["小明", "小红", "小刚", "小丽"],
    "math": [80, 75, 90, 88],
    "english": [75, 82, 85, 91]
}
df = pd.DataFrame(data)
print(df)
print(df.columns)         # ['name', 'math', 'english']
print(df.shape)           # (4, 3)
print(df["math"])         # math 列
print(df.loc[0])          # 第 0 行
```

## 读写 CSV

```python
# 读取
df = pd.read_csv("../../datasets/sales_sample.csv")
print(df.head())          # 前 5 行
print(df.tail(3))         # 后 3 行
print(df.info())          # 数据信息
print(df.describe())      # 数值列统计

# 保存
df.to_csv("output.csv", index=False)
```

## 基本筛选与排序

```python
df = pd.read_csv("../../datasets/sales_sample.csv")

# 条件筛选
filtered = df[df["amount"] > 1000]

# 多条件
mask = (df["amount"] > 500) & (df["region"] == "华东")
subset = df[mask]

# 排序
sorted_df = df.sort_values("amount", ascending=False)

# 选择多列
subset = df[["region", "amount"]]
```
