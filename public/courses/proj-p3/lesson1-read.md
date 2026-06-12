# RFM 概念与应用场景

## 一、RFM 是什么？

RFM 模型最初用于电商用户价值分群，在在线教育场景可以改造为：

| 字母 | 教育场景含义 |
| ---- | ---- |
| R (Recency) | 最近一次学习距今天数，越小越近 |
| F (Frequency) | 学习频次（sessions） |
| M (Monetary) | 总学习时长（minutes） |

## 二、为什么做 RFM？

- 找出 **高价值用户**，进行 VIP 运营
- 识别 **沉睡用户**，进行召回
- 指导 **新用户引导** 与 **学习激励**

## 三、数据结构

| 字段 | 含义 |
| ---- | ---- |
| user_id | 用户 ID |
| last_learn_days | 距上次学习天数 |
| sessions | 学习次数 |
| total_learn_minutes | 总学习分钟数 |

## 四、分箱打分思路

1. 每个指标按分位数分为 5 档（1-5）
2. R：越小越好，因此 last_learn_days 越小打分越高
3. F/M：越大越好，直接升序打分

```python
import pandas as pd
df = pd.read_csv('../../datasets/rfm_data.csv')
df['R_score'] = pd.qcut(df['last_learn_days'], 5, labels=[5,4,3,2,1])
df['F_score'] = pd.qcut(df['sessions'], 5, labels=[1,2,3,4,5])
df['M_score'] = pd.qcut(df['total_learn_minutes'], 5, labels=[1,2,3,4,5])
```

## 五、8 类分层（简化版）

以 **R >= 3** 为「重要」（近期活跃），再按 F/M 高低：

- 重要价值（F≥3 且 M≥3）
- 重要保持（F<3 且 M≥3）
- 重要发展（F≥3 且 M<3）
- 重要挽留（F<3 且 M<3）
- 一般价值 / 一般保持 / 一般发展 / 一般挽留（R<3 时对应的四类）
