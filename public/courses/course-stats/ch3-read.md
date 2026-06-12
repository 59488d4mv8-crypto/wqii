# 第 3 章 假设检验

假设检验是统计学的核心思想之一：通过样本数据来判断某个"假设"是否成立。典型场景：
- 新药是否比旧药有效？
- 新的广告文案是否带来更高转化率？

## 一、原假设 H0 与备择假设 H1

- **H0 (null hypothesis)**："现状没有变化""两组没有差异"，我们要反驳的假设。
- **H1 (alternative hypothesis)**：我们想要支持的假设。

决策规则：计算出 **p 值**，若 p < 0.05，则拒绝 H0，认为差异显著。

## 二、t 检验：比较两组均值

当样本量较小或方差未知时，使用 t 检验。

### 独立双样本 t 检验公式

```
t = (x̄1 - x̄2) / sqrt( s1²/n1 + s2²/n2 )
```

其中 s² 为样本方差。

## 三、手写 t 检验函数

```python
import numpy as np

def t_test_ind(a, b):
    n1, n2 = len(a), len(b)
    m1, m2 = np.mean(a), np.mean(b)
    v1 = np.var(a, ddof=1)
    v2 = np.var(b, ddof=1)
    se = np.sqrt(v1 / n1 + v2 / n2)
    t = (m1 - m2) / se
    df = n1 + n2 - 2
    return t, df
```

## 四、p 值的含义

p 值表示"**在 H0 成立的前提下，出现当前或更极端数据的概率**"。越小越倾向于拒绝 H0。

对于对称分布，p 值 ≈ 2 × Φ(-|t|)。

```python
def normal_approx_pvalue(t_stat):
    # 当 df 较大时，用正态分布近似
    from math import erf, sqrt
    z = abs(t_stat)
    p = 1 - erf(z / sqrt(2))
    return p
```

## 五、完整示例

```python
import numpy as np

np.random.seed(42)

group_a = np.random.normal(100, 15, 30)
group_b = np.random.normal(105, 15, 30)

t, df = t_test_ind(group_a, group_b)
p = normal_approx_pvalue(t)
print("t =", round(t, 3), "df =", df, "p ≈", round(p, 4))
if p < 0.05:
    print("差异显著")
else:
    print("差异不显著")
```

## 六、小结

- 假设检验用 **t 值** 量化差异，用 **p 值** 判断是否显著。
- p 值越小，越有信心拒绝 H0。
- α=0.05 是业界最常用的显著性阈值。
