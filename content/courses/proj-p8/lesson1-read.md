# 时间序列基础

## 一、什么是时间序列

将同一指标在不同时间点上的观测值按时间顺序排列而成的序列。常见如：日访问量、日销量、月收入。

## 二、时间序列的三大成分

| 成分 | 含义 |
| --- | --- |
| **趋势（Trend）** | 长期上升/下降/平稳的倾向 |
| **季节性（Seasonality）** | 以固定周期（如周、月、年）重复出现的模式 |
| **残差/噪声（Residual）** | 不可解释的随机波动 |

## 三、数据结构

`daily_traffic.csv`：`date, pv, uv, orders`，约 180 行。

## 四、常用分析方法

1. **折线图**：观察整体趋势
2. **滑动平均（MA）**：平滑波动，捕捉趋势
3. **按 weekday 聚合**：发现周季节性
4. **下一 N 天移动平均预测**：用最近若干天的均值作为预测值
5. **离群点检测**：用标准差或 IQR 识别异常点

## 五、示例读取

```python
import pandas as pd

df = pd.read_csv('../../datasets/daily_traffic.csv', parse_dates=['date'])
df = df.sort_values('date').reset_index(drop=True)
print(df.head())
```
