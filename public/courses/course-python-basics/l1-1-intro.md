# Python 快速入门

Python 是一门简洁优雅的动态语言，在数据分析、人工智能、Web 开发等领域应用广泛。学习数据分析的第一步，就是掌握 Python 的基本语法和常用工具。本章我们将介绍变量、数据类型、控制结构以及 Jupyter Notebook 的使用方法。

## 变量与基本数据类型

在 Python 中，变量不需要显式声明类型。常见的数据类型包括整数 `int`、浮点数 `float`、字符串 `str` 和布尔值 `bool`。使用 `type()` 函数可以查看变量类型。

```python
name = "数据分析"
year = 2024
pi = 3.14159
is_ok = True

print(name, year, pi, is_ok)
print(type(year), type(pi), type(name))
```

## 控制结构

Python 使用缩进表示代码块，这让代码更具可读性。`if-elif-else` 用于条件判断，`for` 和 `while` 用于循环。列表推导式（list comprehension）是 Python 特有的简洁写法，可以用一行代码生成过滤或变换后的列表。

```python
scores = [85, 92, 78, 65, 88, 95]

for s in scores:
    if s >= 90:
        print(s, "优秀")
    elif s >= 75:
        print(s, "良好")
    else:
        print(s, "加油")

evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)
```

## Jupyter Notebook 使用技巧

Jupyter Notebook 是数据分析的标准工作台。它以单元格（cell）为单位，分为 Markdown 单元格（写文字）和 Code 单元格（写代码）。按 `Shift + Enter` 可以执行当前单元格并跳到下一格；按 `Ctrl + Enter` 只执行不跳转。在单元格中可以使用 `?` 查询函数文档，也能通过 `%timeit` 这样的魔法命令测量代码运行时间。熟练掌握这些快捷键，能极大提升数据分析的效率。

```python
import math
# 计算前 10 个自然数的平方根
roots = [math.sqrt(i) for i in range(1, 11)]
print(roots)
```

## 小结

掌握变量、控制结构与列表推导式，再结合 Jupyter 的交互工作流，你已经具备了编写数据分析脚本的基本能力。后续章节将在此基础上介绍如何使用 NumPy、Pandas 等库处理真实数据。
