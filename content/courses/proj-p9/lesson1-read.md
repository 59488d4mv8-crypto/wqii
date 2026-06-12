# 指标体系：评分、完课率、互动率、复购率

## 一、业务背景

在线教育平台的教师质量是决定用户留存与付费转化的关键。我们通过多维指标量化教师质量，为平台提供排名与改进建议。

## 二、核心指标

| 指标 | 含义 | 取值范围 |
| --- | --- | --- |
| avg_rating | 平均评分 | 0 ~ 5 |
| completion_rate | 完课率 | 0 ~ 1 |
| interaction_rate | 互动率 | 0 ~ 1 |
| review_count | 评价数 | 整数，越大越有"人气" |

## 三、数据结构

`teacher_metrics.csv`：20 行，字段 `teacher_id, avg_rating, completion_rate, interaction_rate, review_count`。

## 四、综合评分流程

1. **指标标准化**：Min-Max 归一化到 [0,1]，或 Z-Score 标准化到均值为 0、标准差为 1
2. **权重设置**：等权法、自定义加权法
3. **综合评分**：加权求和
4. **排名**：按综合评分降序
5. **可视化**：雷达图对比 Top 教师

## 五、读取示例

```python
import pandas as pd

df = pd.read_csv('../../datasets/teacher_metrics.csv')
print(df.head())
print(df.describe())
```
