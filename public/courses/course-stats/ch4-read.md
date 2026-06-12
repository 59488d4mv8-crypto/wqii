# 第 4 章 卡方检验与 A/B 测试思维

**卡方检验 (Chi-square test)** 用于比较两个分类变量之间是否存在关联。在 A/B 测试中，常见应用场景是："不同版本的转化率是否显著不同？"

## 一、列联表 (Contingency Table)

假设我们做了一个 A/B 测试，得到如下数据：

| | 转化 | 未转化 | 合计 |
|---|---|---|---|
| 对照组 A | 45 | 955 | 1000 |
| 实验组 B | 60 | 940 | 1000 |

这就是一张 **2×2 列联表**。

## 二、卡方检验的思想

H0：版本与转化率独立（两组没有差异）。

**期望频数 E** 表示"若 H0 成立，每个格子应该有的数量"：

```
E_ij = (行合计 × 列合计) / 总样本
```

卡方统计量：

```
χ² = Σ (O - E)² / E
```

## 三、手写卡方检验函数

```python
import numpy as np

def chi_square(table):
    table = np.asarray(table, dtype=float)
    row_tot = table.sum(axis=1, keepdims=True)
    col_tot = table.sum(axis=0, keepdims=True)
    total = table.sum()
    expected = row_tot @ col_tot / total
    chi2 = ((table - expected) ** 2 / expected).sum()
    df = (table.shape[0] - 1) * (table.shape[1] - 1)
    return chi2, df, expected
```

## 四、A/B 测试思维

A/B 测试的完整流程：

1. 明确指标（如转化率、客单价）
2. 确定样本量（避免"早期停止"偏差）
3. 随机分流（保证两组同质）
4. 运行实验、收集数据
5. 用假设检验（t 检验 / 卡方检验）判断显著性

## 五、完整示例

```python
import numpy as np

table = [[45, 955],
         [60, 940]]

chi2, df, expected = chi_square(table)
print("卡方值:", round(chi2, 3))
print("自由度:", df)
print("期望频数:\n", expected)
```

## 六、小结

- **卡方检验** 是分类变量关联分析的基础工具。
- **A/B 测试** = 随机分流 + 假设检验。
- 切勿在实验未达到预设样本量时"偷看"并停止，会造成 p 值膨胀。
