# 第 2 章 异常值检测

异常值（outlier）是显著偏离整体分布的数据点，可能来自录入错误、测量误差，也可能是罕见但真实的事件（如 VIP 大客户）。

## 一、IQR 法（箱线图法）

**IQR = Q3 - Q1**，表示中间 50% 数据的跨度。常用判定：

```
下界 = Q1 - 1.5 * IQR
上界 = Q3 + 1.5 * IQR
```

```python
import numpy as np
import pandas as pd

xs = pd.Series([10, 12, 14, 15, 16, 18, 20, 22, 24, 1000])

q1 = xs.quantile(0.25)
q3 = xs.quantile(0.75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = xs[(xs < lower) | (xs > upper)]
print("IQR 异常值:", outliers.values)
```

## 二、Z-score 法

对每个数据点计算 `z = (x - μ) / σ`，若 `|z| > 3` 视为异常值。

```python
z = (xs - xs.mean()) / xs.std()
outliers_z = xs[z.abs() > 2]
print("Z-score 异常值 (|z|>2):", outliers_z.values)
```

## 三、异常值的处理策略

1. **直接剔除**：确认是错误录入时
2. **盖帽（capping / winsorize）**：将超出上界的数值替换为上界
3. **分箱**：归到"≥x"箱
4. **保留并建模**：当异常值本身就是关注对象（如欺诈识别）

```python
# 盖帽示例
xs_cap = xs.clip(lower=lower, upper=upper)
print(xs_cap.values)
```

## 四、完整示例

```python
import numpy as np
import pandas as pd

np.random.seed(42)
income = np.concatenate([np.random.normal(50000, 10000, 200), [1_000_000, 2_000_000]])
df = pd.DataFrame({"income": income})

q1 = df["income"].quantile(0.25)
q3 = df["income"].quantile(0.75)
iqr = q3 - q1
upper = q3 + 1.5 * iqr

print(f"上界: {upper:.0f}")
print("异常值:", df[df["income"] > upper]["income"].values)

df["income_capped"] = df["income"].clip(upper=upper)
print("盖帽后 max:", df["income_capped"].max())
```

## 五、小结

- **IQR 法**对非正态分布更稳健，常用于商务数据。
- **Z-score**适合近似正态分布的数据。
- 发现异常值后不要盲目删除——先理解其**业务含义**再决定处理方式。
