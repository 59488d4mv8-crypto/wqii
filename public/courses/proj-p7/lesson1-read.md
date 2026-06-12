# 关联规则概念：支持度 / 置信度 / 提升度

## 一、业务背景

在线教育平台上，用户往往会同时学习多门课程。通过挖掘"学了 A 的用户常也学 B"的规律，可以用于课程推荐。

## 二、核心概念

- **事务（Transaction）**：一位用户学习过的课程集合
- **项集（Itemset）**：若干课程组成的集合
- **关联规则**：形式为 `A → B`，意为"学过 A 的用户，也学 B"

## 三、三个关键指标

| 指标 | 定义 | 含义 |
| --- | --- |
| **支持度 Support(A)** | 同时包含 A 和 B 的事务数 ÷ 总事务数 | 规则的出现频率 |
| **置信度 Confidence(A→B)** | Support(A∪B) ÷ Support(A) | 学 A 的人学 B 的比例 |
| **提升度 Lift(A→B)** | Confidence(A→B) ÷ Support(B) | 学 A 的人学 B 的倍数 |

- 提升度 > 1 表示规则有效；= 1 表示独立；< 1 表示负相关。

## 四、Apriori 原理

**频繁项集的任一子集也是频繁项集。因此可以"自底向上"：

1. 扫描数据扫描：计算 1-itemset 支持度，过滤低于 min_support 的项
2. 连接（join）：k-频繁项集两两连接生成 k+1 候选项集
3. 剪枝（prune）：若候选项集任一 k 项子集不在 k-频繁项集中，则剪掉
4. 扫描：计算候选项支持度，过滤低于 min_support
5. 回到第 2 步，直到无法再扩展
6. 从所有频繁项集生成规则

## 五、本项目数据

`course_baskets.csv`：两列 `user_id, course_id。同一 user_id 多行记录表示一个事务。

## 六、示例读取：

```python
import pandas as pd
df = pd.read_csv('../../datasets/course_baskets.csv')
baskets = df.groupby('user_id')['course_id'].apply(set).tolist()
print(baskets[:5]
```
