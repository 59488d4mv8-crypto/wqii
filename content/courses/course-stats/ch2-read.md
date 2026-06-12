# 第 2 章 概率分布

在商务场景中，我们经常需要"想象"数据背后的生成规律，比如：
- 投放 100 个广告，点击的用户数服从什么分布？
- 某个页面停留时长服从什么分布？

本章学习两种最常见的分布：**二项分布** 与 **正态分布**。

## 一、二项分布 (Binomial Distribution)

场景：重复 n 次独立试验，每次成功概率为 p，求成功次数的分布。

```python
import numpy as np

np.random.seed(42)

# 掷 10 次硬币，重复做 1000 次实验
n, p = 10, 0.5
samples = np.random.binomial(n, p, size=1000)
print("均值:", samples.mean())  # 接近 5
```

用 matplotlib 画出分布直方图：

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 4))
plt.hist(samples, bins=range(0, n + 2), align="left", rwidth=0.8, color="#4C72B0")
plt.title("Binomial Distribution (n=10, p=0.5)")
plt.xlabel("Success count")
plt.ylabel("Frequency")
plt.show()
```

## 二、正态分布 (Normal Distribution)

很多自然现象与商务数据（身高、测量误差、考试成绩等近似服从正态分布。

```python
np.random.seed(42)

mu, sigma = 170, 8
heights = np.random.normal(mu, sigma, size=1000)
print("均值:", heights.mean())
print("标准差:", heights.std())
```

画图：

```python
plt.figure(figsize=(8, 4))
plt.hist(heights, bins=30, density=True, color="#DD8452", alpha=0.8)
plt.title("Normal Distribution (mu=170, sigma=8)
plt.xlabel("Height (cm)")
plt.ylabel("Density")
plt.show()
```

## 三、中心极限定理（CLT）

**中心极限定理**告诉我们：无论原始分布是什么，大量独立同分布样本的均值将接近正态分布。这是假设检验的理论基础。

```python
np.random.seed(42)

means = []
for _ in range(200):
    sample = np.random.uniform(0, 1, 100)
    means.append(sample.mean())

plt.figure(figsize=(8, 4))
plt.hist(means, bins=25, density=True, color="#55A868", alpha=0.8)
plt.title("Sampling distribution of sample means")
plt.show()
```

## 四、z-score 标准化

将数据做标准化变换：`z = (x - mean) / std，使之变为均值 0、方差 1 的标准正态分布。

```python
x = np.array([10, 20, 30, 40, 50])
z = (x - x.mean()) / x.std()
print("z-scores:", z)
```

## 五、完整示例：模拟 AB 测试中的二项分布

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# 模拟两个版本的转化率
p_control = np.random.binomial(n=1000, p=0.10, size=10000)
p_test = np.random.binomial(n=1000, p=0.12, size=10000)

plt.figure(figsize=(8, 4))
plt.hist(p_control / 1000, bins=30, alpha=0.6, label="control", color="#4C72B0")
plt.hist(p_test / 1000, bins=30, alpha=0.6, label="test", color="#DD8452")
plt.title("Conversion Rate Distribution")
plt.xlabel("rate")
plt.ylabel("Frequency")
plt.legend()
plt.show()
```

## 六、小结

- **二项分布** 适用于"成功/失败的计数问题。
- **正态分布** 是商务数据最常见的连续分布。
- **中心极限定理** 让我们可以用样本均值做推断——这是下一章假设检验的核心理论支撑。
