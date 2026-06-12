# 业务背景：漏斗分析与流失节点

## 一、项目背景

某在线课程团队发现很多用户报名课程后未完成学习。为了优化课程体验，我们需要回答：

1. **用户在哪些章节流失最多？**
2. **流失用户有什么特征？**
3. **能否提前识别流失用户？**

本项目使用 `lesson_progress.csv` 数据：

| 字段 | 含义 |
| ---- | ---- |
| user_id | 用户 ID |
| course_id | 课程（A/B/C） |
| chapter_id | 章节（ch1-ch5） |
| progress | 章节完成度（0-1） |
| is_dropout | 是否流失（1=流失） |
| timestamp | 时间戳 |

## 二、漏斗分析

漏斗 (Funnel) 分析从访问 → 注册 → 学习 → 完成的每个环节统计用户数，找出流失最严重的环节。

```python
import pandas as pd

df = pd.read_csv('../../datasets/lesson_progress.csv')
by_chapter = df.groupby('chapter_id')['user_id'].count()
print(by_chapter.sort_index())
```

## 三、流失预测

流失预测可以用最简单的**规则模型**（progress < 0.5 的用户标记为高风险）。也可以通过与 `is_dropout` 的相关系数来选择强特征。

## 四、关键问题

- 哪个章节完课率最低？
- 哪些特征和流失最相关？
- 基于进度阈值的规则预测准确率是多少？
