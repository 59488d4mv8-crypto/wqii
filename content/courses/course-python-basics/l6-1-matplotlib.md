# 常用图表类型

Matplotlib 是 Python 最经典的绘图库。本节介绍 5 种最常用的商务图表。

```python
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
```

## 折线图（趋势）

```python
months = ["1月", "2月", "3月", "4月", "5月", "6月"]
sales = [120, 135, 128, 150, 170, 160]

plt.figure(figsize=(8, 4))
plt.plot(months, sales, marker="o", linewidth=2, color="#1f77b4")
plt.title("月度销售趋势")
plt.xlabel("月份")
plt.ylabel("销售额（万元）")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

## 柱状图（对比）

```python
regions = ["华东", "华北", "华南", "西南"]
amounts = [45000, 36000, 33000, 28000]

plt.figure(figsize=(7, 4))
plt.bar(regions, amounts, color="#2ca02c")
plt.title("各区域销售额对比")
plt.ylabel("金额（元）")
for i, v in enumerate(amounts):
    plt.text(i, v + 500, str(v), ha="center")
plt.tight_layout()
plt.show()
```

## 散点图（相关性）

```python
np.random.seed(42)
study_hours = np.random.normal(5, 1.5, 50)
scores = 60 + study_hours * 4 + np.random.normal(0, 5, 50)

plt.figure(figsize=(7, 4))
plt.scatter(study_hours, scores, alpha=0.6, color="#ff7f0e")
plt.xlabel("学习时长（小时）")
plt.ylabel("分数")
plt.title("学习时长与成绩相关性")
plt.tight_layout()
plt.show()
```

## 直方图（分布）

```python
np.random.seed(42)
data = np.random.normal(70, 10, 1000)

plt.figure(figsize=(7, 4))
plt.hist(data, bins=30, color="#9467bd", edgecolor="black", alpha=0.7)
plt.title("分数分布直方图")
plt.xlabel("分数")
plt.ylabel("频数")
plt.tight_layout()
plt.show()
```

## 饼图（占比）

```python
labels = ["华东", "华北", "华南", "西南"]
sizes = [35, 25, 22, 18]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors,
        shadow=True, startangle=90)
plt.title("区域销售占比")
plt.axis("equal")
plt.tight_layout()
plt.show()
```

## 多图布局

```python
fig, axes = plt.subplots(2, 2, figsize=(10, 7))
axes[0, 0].plot([1, 2, 3], [1, 4, 9])
axes[0, 0].set_title("折线图")
axes[0, 1].bar(["A", "B", "C"], [3, 7, 5])
axes[0, 1].set_title("柱状图")
axes[1, 0].hist(np.random.randn(100), bins=20)
axes[1, 0].set_title("直方图")
axes[1, 1].pie([30, 40, 30], labels=["x", "y", "z"])
axes[1, 1].set_title("饼图")
plt.tight_layout()
plt.show()
```
