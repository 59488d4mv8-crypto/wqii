# 业务建议

## 一、关键发现

1. **章节 3-5** 往往是流失最严重的节点，可能因为内容难度较高
2. **进度 < 50% 的用户流失率明显更高**，需要关注
3. progress 与 is_dropout 呈强负相关，这是我们的重要信号

## 二、具体建议

- **对流失严重的章节增加提示语**：在 ch3 之前增加学习提示和助教答疑；
- **进度监控进度监测进度监测进度监测进度告警**：当用户连续 3 天未学习则推送消息；
- **进度预警**：当用户 progress 低于 0.3 的用户增加激励机制和激励措施。

## 三、漏斗图绘制

```python
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../../datasets/lesson_progress.csv')
by = df.groupby('chapter_id')['user_id'].count().sort_index()

plt.figure(figsize=(10, 5))
plt.bar(by.index, by.values)
plt.ylabel('Users')
plt.show()
```
