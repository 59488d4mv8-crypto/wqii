# 第 1 章 多图布局与样式

好的可视化不仅要对，还要**好看、易读**。本章学习 matplotlib 最核心的布局与样式。

## 一、创建画布与多图

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(10, 6))
# axes 是一个 2x2 的 numpy 数组
axes[0, 0].plot([1, 2, 3], [1, 4, 9])
axes[0, 1].bar(["A", "B", "C"], [3, 7, 5])
axes[1, 0].scatter(range(10), range(10))
axes[1, 1].hist([1, 2, 2, 3, 3, 3, 4])
plt.tight_layout()
plt.show()
```

## 二、标题与子标题

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot([1, 2, 3], [1, 4, 9])
ax.set_title("My Plot", fontsize=14, fontweight="bold")
ax.set_xlabel("X")
ax.set_ylabel("Y")
fig.suptitle("Global Title", y=1.02, fontsize=16)
plt.show()
```

## 三、图例 legend

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot([1, 2, 3], [1, 4, 9], label="Series A", color="#4C72B0")
ax.plot([1, 2, 3], [2, 3, 8], label="Series B", color="#DD8452")
ax.legend(loc="upper left", frameon=True)
plt.show()
```

## 四、颜色与样式

```python
import matplotlib.pyplot as plt

colors = ["#4C72B0", "#DD8452", "#55A868", "#C44E52"]
fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(["A", "B", "C", "D"], [3, 7, 5, 8], color=colors, edgecolor="black")
ax.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()
```

## 五、完整示例

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.arange(20)
y1 = np.random.randint(10, 30, 20)
y2 = np.random.randint(5, 25, 20)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(x, y1, color="#4C72B0", linewidth=2, label="y1")
axes[0].set_title("Line Chart")
axes[0].legend()
axes[1].bar(x, y2, color="#DD8452", label="y2")
axes[1].set_title("Bar Chart")
axes[1].legend()
fig.suptitle("Subplots Demo", fontsize=14)
plt.tight_layout()
plt.show()
```

## 六、小结

- **plt.subplots(nrows, ncols, figsize=(w, h))** 创建多图网格。
- **set_title / set_xlabel / set_ylabel** 控制文字。
- **legend** 配合 label 参数显示图例。
- **color** 支持 16 进制颜色代码，便于统一品牌色。
