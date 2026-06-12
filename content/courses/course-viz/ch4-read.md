# 第 4 章 商务常见图形

本章介绍三种在商务报告中高频出现的图形：**饼图**、**雷达图**、**双轴图**。

## 一、饼图（Pie Chart）

适合展示单一维度的占比。

```python
import matplotlib.pyplot as plt

labels = ["华北", "华东", "华南", "西部"]
sizes = [25, 35, 25, 15]

fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(sizes, labels=labels, autopct="%1.1f%%",
       colors=["#4C72B0", "#DD8452", "#55A868", "#C44E52"],
       startangle=90)
ax.set_title("区域销售占比")
plt.show()
```

## 二、雷达图（Radar Chart）

适合展示多维指标的综合对比，常用于能力模型或 KPI 评估。

```python
import numpy as np
import matplotlib.pyplot as plt

categories = ["获客", "转化", "留存", "复购", "口碑"]
values = [80, 65, 70, 55, 60]
# 闭合
values += values[:1]
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False)
angles = np.concatenate((angles, [angles[0]]))

fig, ax = plt.subplots(subplot_kw=dict(polar=True), figsize=(6, 6))
ax.plot(angles, values, "o-", color="#4C72B0", linewidth=2)
ax.fill(angles, values, color="#4C72B0", alpha=0.25)
ax.set_thetagrids(angles[:-1] * 180 / np.pi, categories)
ax.set_title("综合能力雷达图")
plt.show()
```

## 三、双轴图（Twin Axes）

用于对比量纲不同的两个指标（例如销售额 vs 利润率）。

```python
import matplotlib.pyplot as plt

months = ["1月","2月","3月","4月","5月","6月"]
sales = [100, 130, 150, 170, 160, 200]
rate = [0.10, 0.12, 0.11, 0.14, 0.13, 0.15]

fig, ax1 = plt.subplots(figsize=(8, 4))
ax1.bar(months, sales, color="#4C72B0", alpha=0.8, label="销售额")
ax1.set_ylabel("销售额（万）")

ax2 = ax1.twinx()
ax2.plot(months, [r*100 for r in rate], color="#DD8452", marker="o", linewidth=2, label="利润率%")
ax2.set_ylabel("利润率（%）")

fig.suptitle("销售与利润率双轴图")
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))
plt.show()
```

## 四、小结

- **饼图**展示占比；**雷达图**展示多维综合；**双轴图**展示不同量纲的对比。
- 绘制这些图的关键是正确调用 `pie` / `polar=True` / `twinx`。
