# groupby 与 pivot_table

分组聚合是数据分析中最常用的操作之一。Pandas 提供了强大的 `groupby` 和 `pivot_table` 工具。

## groupby 基础

```python
import pandas as pd
import numpy as np

df = pd.read_csv("../../datasets/sales_sample.csv")

# 按 region 分组，对 amount 求和
by_region = df.groupby("region")["amount"].sum()
print(by_region)

# 多列聚合
by_region_stats = df.groupby("region")["amount"].agg(["sum", "mean", "count"])
print(by_region_stats)

# 多列分组
by_region_product = df.groupby(["region", "product"])["amount"].sum()
print(by_region_product)
```

## 应用自定义聚合函数

```python
def range_func(x):
    return x.max() - x.min()

df.groupby("region")["amount"].apply(range_func)
```

## 透视表 pivot_table

类似 Excel 的数据透视表。

```python
import pandas as pd

df = pd.read_csv("../../datasets/sales_sample.csv")

# 基本透视表：按 region 行，按 product 列，值为 amount 总和
pivot = pd.pivot_table(
    df,
    values="amount",
    index="region",
    columns="product",
    aggfunc="sum",
    fill_value=0
)
print(pivot)

# 多重聚合
pivot2 = pd.pivot_table(
    df,
    values=["qty", "amount"],
    index="region",
    aggfunc={"qty": "sum", "amount": ["sum", "mean"]}
)
print(pivot2)
```

## 常用聚合函数一览

- `sum()`：求和
- `mean()`：均值
- `count()`：计数
- `max() / min()`：最大/最小
- `std() / var()`：标准差 / 方差
- `first() / last()`：第一个 / 最后一个
- `median()`：中位数
