# 列表、字典与函数

Python 中最常用的三种数据结构：**列表（list）**、**字典（dict）**、**函数（function）**。

## 列表（List）

有序、可变的元素集合。

```python
fruits = ["apple", "banana", "cherry", 1, 3.14, True]
print(fruits[0])     # apple
print(fruits[1:3])   # ['banana', 'cherry']
fruits.append("orange")  # 末尾添加
print(len(fruits))   # 长度
```

常用列表方法：`.append()`, `.extend()`, `.insert()`, `.remove()`, `.pop()`, `.index()`, `.sort()`。

## 字典（Dictionary）

键值对结构，通过 key 快速查找 value。

```python
student = {"name": "小明", "age": 20, "courses": ["数学", "英语"]}
print(student["name"])          # 小明
student["age"] = 21             # 修改
student["city"] = "北京"        # 新增
for k, v in student.items():
    print(k, "->", v)
```

## 函数（Function）

封装可重用的代码块。

```python
def add(a, b):
    """返回 a 与 b 的和"""
    return a + b

print(add(3, 5))  # 8

# 匿名函数（lambda）
square = lambda x: x * x
print(square(5))  # 25
```

## 组合练习

```python
def analyze_scores(scores):
    """返回最高分、最低分、平均分"""
    return {
        "max": max(scores),
        "min": min(scores),
        "avg": sum(scores) / len(scores)
    }

result = analyze_scores([80, 90, 75, 88, 92])
print(result)  # {'max': 92, 'min': 75, 'avg': 85.0}
```
