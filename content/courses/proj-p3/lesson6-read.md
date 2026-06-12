# 运营策略建议

## 一、典型策略

| 分层 | 策略 |
| ---- | ---- |
| 重要价值 | VIP 专属服务，个性化推荐高阶课程 |
| 重要发展 | 增加学习激励，设置打卡奖励 |
| 重要保持 | 发送优惠活动和新课提醒，维持学习习惯 |
| 重要挽留 | 主动联系、设置回归奖励 |
| 一般价值 / 发展 / 保持 / 挽留 | 通过大众化推送、低价课程试探兴趣 |

## 二、运营执行建议

1. **对高价值用户做主动关怀**（运营 1v1）
2. **对流失风险用户做自动化推送**（Push / 邮件 / 短消息）
3. **对低频用户做限时打卡奖励**

## 三、饼图可视化示例

```python
import matplotlib.pyplot as plt
from lesson5_template import segment_pie_data
import pandas as pd

df = pd.read_csv('../../datasets/rfm_data.csv')
d = segment_pie_data(df)

plt.figure(figsize=(8, 8))
plt.pie(list(d.values()), labels=list(d.keys()), autopct='%1.1f%%')
plt.title('RFM 用户分层占比')
plt.show()
```
