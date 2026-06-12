# 第 2 章 漏斗图

漏斗图（Funnel Chart）用于展示业务流程各环节的转化情况，常见于电商、SaaS 等转化分析。

## 一、漏斗图结构

典型的销售漏斗：访问 → 注册 → 下单 → 支付。每一层用户数逐级递减。

## 二、使用 matplotlib 横向 bar 绘制漏斗

```python
import matplotlib.pyplot as plt

stages = ["访问", "注册", "下单", "支付"]
values = [10000, 5000, 2000, 800]

fig, ax = plt.subplots(figsize=(8, 4))
ax.barh(stages, values, color=["#4C72B0", "#55A868", "#DD8452", "#C44E52"])
ax.invert_yaxis()  # 从上到下递减
ax.set_xlabel("用户数")
ax.set_title("销售漏斗")
plt.show()
```

## 三、计算转化率

```python
rates = [v / values[0] for v in values]
for i, (s, v, r) in enumerate(zip(stages, values, rates)):
    print(f"{s}: {v} ({r:.1%})")
```

## 四、完整示例

```python
import matplotlib.pyplot as plt

stages = ["访问", "注册", "下单", "支付"]
users = [10000, 5200, 2100, 900]

fig, ax = plt.subplots(figsize=(8, 5))
colors = ["#4C72B0", "#55A868", "#DD8452", "#C44E52"]
ax.barh(stages, users, color=colors, edgecolor="black")
ax.invert_yaxis()
ax.set_xlabel("用户数")
ax.set_title("销售漏斗")

# 在柱子末端标注数量
for i, (s, v) in enumerate(zip(stages, users)):
    rate = v / users[0]
    ax.text(v + 100, i, f"{v} ({rate:.1%}", va="center")

plt.tight_layout()
plt.show()
```

## 五、小结

- 漏斗图本质就是一张**横向条形图**（`barh`），并把 y 轴反转。
- 加上数值/转化率标注，让业务一目了然。
