# NumPy 数组基础

NumPy（Numerical Python）是 Python 做科学计算的基础库，提供高性能的 **ndarray** 多维数组对象。

## 创建数组

```python
import numpy as np

# 从列表创建
arr1d = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

# 特殊数组
print(np.zeros(5))           # [0. 0. 0. 0. 0.]
print(np.ones((2, 3)))       # 2x3 的 1
print(np.arange(0, 10, 2))   # [0 2 4 6 8]
print(np.linspace(0, 1, 5))  # [0. 0.25 0.5 0.75 1.]
print(np.random.rand(4))     # 随机 [0,1)
```

## 形状与类型

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)   # (2, 3)
print(arr.dtype)   # int64
print(arr.size)    # 6 个元素
print(arr.ndim)    # 2 维
```

## 索引与切片

```python
a = np.array([10, 20, 30, 40, 50])
print(a[0])        # 10
print(a[-1])       # 50
print(a[1:4])      # [20 30 40]

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b[0, 2])     # 3
print(b[:, 1])     # [2 5 8]  整列
print(b[:2, :2])   # [[1 2] [4 5]]
```

## 向量化运算

NumPy 数组可直接进行元素级运算，无需 for 循环。

```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(x + y)       # [5 7 9]
print(x * 2)       # [2 4 6]
print(x ** 2)      # [1 4 9]
print(np.dot(x, y)) # 32  点积
print(np.mean(x))  # 2.0
print(np.sum(x))   # 6
print(np.max(x))   # 3
```

## 布尔索引

```python
scores = np.array([85, 72, 93, 68, 78, 90, 55])
print(scores[scores >= 80])   # [85 93 90]
print(np.where(scores >= 60, "及格", "不及格"))
```
