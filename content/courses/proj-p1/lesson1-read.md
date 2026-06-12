# 业务背景：在线教育平台如何度量获客与活跃？

## 一、项目背景

假设你所在的数据团队负责为一家在线教育平台做用户增长分析。运营同学最近推出了几个获客渠道（自然搜索、付费广告、社交媒体、推荐、直访），他们想了解：

1. **哪个渠道获客最多？**
2. **用户主要在什么时段注册？**
3. **平台的日活跃用户（DAU）是否稳定？**
4. **用户注册后是否能持续留下？**

我们将通过两份数据（`user_registrations.csv` 和 `daily_active.csv`）来回答这些问题。

## 二、关键指标

| 指标 | 含义 |
| ---- | ---- |
| **注册量** | 新注册用户数，反映获客能力 |
| **DAU** | 日活跃用户数，反映平台健康度 |
| **WAU** | 周活跃用户数（7 天去重） |
| **MAU** | 月活跃用户数（30 天去重） |
| **留存率** | 注册后第 N 天仍活跃的比例 |

## 三、数据结构

**user_registrations.csv**（用户注册表）

| 字段 | 含义 |
| ---- | ---- |
| date | 注册日期 |
| channel | 注册渠道 |
| user_id | 用户 ID |
| hour | 注册小时（0-23） |
| session_count | 学习次数 |
| active_days | 活跃天数 |

**daily_active.csv**（每日活跃）

| 字段 | 含义 |
| ---- | ---- |
| date | 日期 |
| channel | 渠道 |
| dau | 当日活跃用户数 |

## 四、读取数据示例

```python
import pandas as pd

reg = pd.read_csv('../../datasets/user_registrations.csv')
dau = pd.read_csv('../../datasets/daily_active.csv')

print("注册样本量:", len(reg))
print("渠道:", reg['channel'].unique())
print("日期范围:", reg['date'].min(), "~", reg['date'].max())
```

## 五、分析思路

1. **概览**：看样本量、渠道数、时间跨度
2. **渠道对比**：按渠道统计注册量，绘制柱状图
3. **时段分布**：按 hour 统计注册量，绘制分布图
4. **活跃指标**：计算 DAU、WAU、MAU
5. **留存曲线**：根据 active_days 推断 30 日留存率
6. **输出业务建议**
