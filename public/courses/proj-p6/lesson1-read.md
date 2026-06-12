# 漏斗概念：浏览 → 试学 → 加购 → 付费 → 完课

## 一、什么是漏斗

漏斗分析是将用户旅程拆解为若干关键步骤，每一步用户数量都比上一步少，形成"漏斗"形状。通过对比各步骤的流失率，找到最需要优化的环节。

## 二、本项目漏斗的 5 个节点

| 节点 | 含义 |
| --- | --- |
| view（浏览） | 用户访问课程详情页 |
| trial（试学） | 点击免费试学/试听 |
| add_cart（加购） | 将课程加入购物车 |
| purchase（付费） | 完成支付购买 |
| complete（完课） | 学完全部课程章节 |

## 三、关键指标

- **节点计数**：每个节点的独立用户数
- **单步转化率** = 当前节点用户数 ÷ 上一节点用户数
- **总转化率** = 最终节点用户数 ÷ 起始节点用户数
- **收入** = 付费节点 × 平均客单价

## 四、数据结构

数据文件 `conversion_funnel.csv`：5 个节点 × 5 个渠道（organic/paid/social/ref/direct）= 25 行，字段为 `stage, channel, user_count, revenue`。

## 五、读取示例

```python
import pandas as pd

df = pd.read_csv('../../datasets/conversion_funnel.csv')
print(df.head())
print(df.groupby('stage')['user_count'].sum())
```

## 六、分析思路

1. 计算全网漏斗各节点总数
2. 逐节点计算单步转化率
3. 按渠道绘制漏斗对比图
4. 识别最低转化率的"卡点节点"
5. 输出业务建议
