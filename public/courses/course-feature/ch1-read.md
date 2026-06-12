# 第 1 章 缺失值处理

真实业务数据几乎不可能没有缺失。处理缺失值的策略主要有三种：**删除**、**填充**、**保留（标记）**。

## 一、检测缺失值

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "age":     [20, 25, np.nan, 35, 40],
    "income":  [np.nan, 50000, 60000, np.nan, 80000],
    "city":    ["Beijing", np.nan, "Shanghai", "Beijing", "Guangzhou"]
})

print(df.isna().sum())        # 每列缺失数量
print(df.isna().mean())       # 每列缺失率
```

## 二、直接删除

仅在缺失占比极低（<5%）且随机时使用：

```python
# 删掉任何含有 NaN 的行
df_drop = df.dropna(axis=0)

# 删掉所有列都是 NaN 的行
df_drop2 = df.dropna(how="all")
```

## 三、填充缺失值

- 数值列：**均值 / 中位数 / 0**
- 类别列：**众数 / "Unknown"**

```python
df["age"].fillna(df["age"].mean(), inplace=False)
df["income"].fillna(df["income"].median(), inplace=False)
df["city"].fillna("Unknown", inplace=False)
```

## 四、ffill / bfill

时间序列数据常用前向后向填充：

```python
ts = pd.Series([1, np.nan, np.nan, 4, 5])
print(ts.ffill())   # [1, 1, 1, 4, 5]
print(ts.bfill())   # [1, 4, 4, 4, 5]
```

## 五、标记缺失列

保留缺失信息，新建 `xxx_is_null` 列，对模型更友好：

```python
df["income_is_null"] = df["income"].isna().astype(int)
df["income"].fillna(df["income"].median(), inplace=False)
```

## 六、完整示例

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "age": [22, 25, np.nan, 35, np.nan, 45, 28],
    "income": [30000, np.nan, 50000, np.nan, 70000, 80000, 55000]
})

# 统计并填充
print("缺失数:\n", df.isna().sum())
df["age"] = df["age"].fillna(df["age"].mean())
df["income_is_null"] = df["income"].isna().astype(int)
df["income"] = df["income"].fillna(df["income"].median())
print(df)
```

## 七、小结

- **isna()** 用于检测；**fillna()** 用于填充；**dropna()** 用于删除。
- 填充数值列优先用 **中位数**（对异常值更稳健），类别列用 **众数或"Unknown"**。
- 重要变量的缺失本身可能就是一种信号，务必加上"缺失标记"。
