# 第 4 章 编码

机器学习模型只能处理数值数据，因此需要把文本/类别变量转为数值。本章学习两种最常用方式：**one-hot encoding** 和 **label encoding**。

## 一、Label encoding

把每个类别用一个整数表示：`0, 1, 2, ...`。

适用场景：类别之间**有天然顺序**的特征（如 size: S/M/L/XL）。

```python
import pandas as pd

s = pd.Series(["small", "medium", "large", "small", "large"])
mapping = {"small": 0, "medium": 1, "large": 2}
encoded = s.map(mapping)
print(encoded)
```

## 二、One-hot encoding

对每个类别新建一列，用 0/1 表示是否属于该类：

```python
df = pd.DataFrame({"city": ["BJ", "SH", "GZ", "BJ", "SH"]})
one_hot = pd.get_dummies(df["city"], prefix="city")
print(one_hot)
```

## 三、何时用哪种？

- **无序类别**（如城市）：用 **one-hot**
- **有序类别**（如评分等级）：用 **label**
- 高基变量（>20 类别）：可考虑合并小类 + 频次编码

## 四、频次编码

用类别出现的频率替代类别：

```python
city = pd.Series(["BJ","SH","BJ","GZ","SH","BJ"])
freq = city.value_counts(normalize=True).to_dict()
encoded = city.map(freq)
print(encoded)
```

## 五、完整示例

```python
import pandas as pd

df = pd.DataFrame({
    "size": ["S", "M", "L", "XL", "M", "L"],
    "city": ["BJ", "SH", "BJ", "GZ", "GZ", "SH"]
})

# label encoding for size
size_map = {"S": 0, "M": 1, "L": 2, "XL": 3}
df["size_label"] = df["size"].map(size_map)

# one-hot for city
df = pd.concat([df, pd.get_dummies(df["city"], prefix="city")], axis=1)
print(df)
```

## 六、小结

- **Label encoding** 适合有序类别；**one-hot** 适合无序类别。
- 类别过多时先做**频次过滤/合并**，再编码。
