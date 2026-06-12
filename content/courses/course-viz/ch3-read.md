# 第 3 章 桑基图 / 热力图

桑基图（Sankey）用于展示流量从一个节点到另一个节点的迁移；热力图（Heatmap）用于展示二维矩阵的强弱分布。

## 一、桑基图（matplotlib.sankey）

```python
import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey

fig = plt.figure(figsize=(8, 4))
sankey = Sankey(ax=None, scale=1.0, unit=None)
# 流入/流出
sankey.add(flows=[100, -30, -70],
           labels=["总流量", "渠道 A", "渠道 B"],
           orientations=[0, 0, -1])
diagrams = sankey.finish()
plt.title("Sankey 示例")
plt.show()
```

## 二、热力图（matplotlib imshow）

```python
import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(5, 5)
fig, ax = plt.subplots(figsize=(6, 5))
im = ax.imshow(data, cmap="Blues")
plt.colorbar(im, ax=ax)
ax.set_title("imshow 热力图")
plt.show()
```

## 三、seaborn heatmap（若可用），否则退回到 imshow：

```python
import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(5, 5)
fig, ax = plt.subplots(figsize=(6, 5))
im = ax.imshow(data, cmap="Blues")
plt.colorbar(im, ax=ax)
ax.set_title("Heatmap")
plt.show()
```

## 四、完整示例：渠道 × 产品销售矩阵

```python
import numpy as np
import matplotlib.pyplot as plt

regions = ["华北", "华东", "华南"]
products = ["产品A", "产品B", "产品C", "产品D"]
sales = np.array([
    [120, 80, 95, 70],
    [150, 90, 110, 85],
    [130, 75, 100, 90]
])

fig, ax = plt.subplots(figsize=(7, 4))
im = ax.imshow(sales, cmap="Reds")
ax.set_xticks(range(len(products)))
ax.set_xticklabels(products)
ax.set_yticks(range(len(regions)))
ax.set_yticklabels(regions)
plt.colorbar(im, ax=ax)

# 标注数值
for i in range(sales.shape[0]):
    for j in range(sales.shape[1]):
        ax.text(j, i, sales[i, j], ha="center", va="center", color="black")

ax.set_title("区域 × 产品 销售热力图")
plt.tight_layout()
plt.show()
```

## 五、小结

- **桑基图**展示流分析；**热力图**展示二维矩阵关系。
- matplotlib 的 **imshow + colorbar** 是绘制热力图最通用方法，配合 cmap 参数控制配色。
