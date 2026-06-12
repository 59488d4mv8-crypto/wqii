# 第 1 章 描述性统计

描述性统计是数据分析的基础。它用一组关键指标来总结数据集的整体特征，常用的有 **集中趋势**（均值、中位数、众数）、**离散程度**（方差、标准差、极差）和 **分位数**（25%、50%、75% 分位数）等。

## 一、集中趋势

**均值 (Mean)**：所有数值的平均数，对异常值敏感。

```python
import numpy as np

data = [10, 20, 30, 40, 50]
mean = np.mean(data)
print("均值:", mean)  # 30.0
```

**中位数 (Median)**：将数据排序后位于中间的数值，对异常值不敏感。

```python
median = np.median([10, 20, 30, 40, 1000])
print("中位数:", median)  # 30.0
```

## 二、离散程度

**方差 (Variance)**：描述数据与均值的偏离程度。

```python
variance = np.var(data)          # 总体方差（除以 N）
print("总体方差:", variance)
sample_var = np.var(data, ddof=1) # 样本方差（除以 N-1）
print("样本方差:", sample_var)
```

**标准差 (Standard Deviation)**：方差的平方根，单位与原始数据一致。

```python
std = np.std(data, ddof=1)
print("样本标准差:", std)
```

## 三、分位数（Quartiles / Percentiles）

分位数告诉我们数据的分布情况，在箱线图和异常值检测中很常用。

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q25 = np.percentile(arr, 25)
q50 = np.percentile(arr, 50)   # 即中位数
q75 = np.percentile(arr, 75)
print("25%:", q25, "  50%:", q50, "  75%:", q75)
```

## 四、pandas 一键汇总

`describe()` 可以一次性输出 count、mean、std、min、25%、50%、75%、max。

```python
import pandas as pd

df = pd.DataFrame({"income": [30, 40, 50, 60, 70, 80, 120]})
print(df.describe())
```

## 五、完整示例

下面我们对一份销售数据做完整的描述性统计分析：

```python
import numpy as np
import pandas as pd

sales = pd.Series([120, 150, 130, 180, 90, 210, 160, 140, 170, 200])

print("均值:", sales.mean())
print("中位数:", sales.median())
print("样本方差:", sales.var())
print("样本标准差:", sales.std())
print("四分位数:")
print(sales.describe()[["25%", "50%", "75%"]])
```

## 六、小结

- **均值** 适合对称分布数据；**中位数** 在存在极端值时更稳健。
- **方差/标准差** 衡量数据离散程度，越大表示波动越大。
- **分位数** 帮助我们理解数据的整体分布形态，是做假设检验之前的必备步骤。
