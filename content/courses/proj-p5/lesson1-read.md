# 变量与相关性概念

## 一、变量类型

- **数值变量**：duration_min、pause_count、seek_count、quiz_score
- **分类变量**：chapter_id（ch1-ch4）

## 二、相关性是什么？

**Pearson 相关系数**衡量两个数值变量之间的线性关系强度，取值范围 [-1, 1]：

- 接近 **+1**：强正相关（一个变大时另一个也变大）
- 接近 **-1**：强负相关（一个变大时另一个变小）
- 接近 **0**：几乎无线性相关

## 三、数据结构

| 字段 | 含义 |
| ---- | ---- |
| user_id | 用户 ID |
| chapter_id | 章节 |
| duration_min | 学习时长（分钟） |
| pause_count | 暂停次数 |
| seek_count | 跳转次数 |
| quiz_score | 测验成绩（0-100） |

## 四、分析流程

1. 读取并概览数据（describe）
2. 计算相关矩阵（`.corr()`）
3. 绘制散点图（duration vs quiz_score）
4. 使用 `numpy.polyfit` 做简单线性回归
5. 用箱线图对比 pause_count 高低两组的成绩分布

## 五、线性回归公式

```
score = slope * duration_min + intercept
```

`slope > 0` 表示"学得越久，分数越高"。
