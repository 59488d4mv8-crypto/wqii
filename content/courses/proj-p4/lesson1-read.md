# NLP 入门：分词 / 停用词 / 情感

## 一、什么是 NLP？

自然语言处理（Natural Language Processing, NLP）研究如何让计算机理解和生成人类语言。常见应用包括情感分析、聊天机器人、文本摘要、机器翻译等。

## 二、中文文本处理的三个基础步骤

1. **分词**：把句子拆成最小语义单元（词）
2. **停用词过滤**：去掉意义不大的词（如"的"、"是"、"了"）
3. **词频统计 / 情感词典**：统计词频或基于词典打分

## 三、简易分词示例

```python
def tokenize(text, stopwords=None):
    import re
    # 按非中文字符切分（纯 Python 版）
    words = re.split(r'[，。！？\s,.!?]+', text)
    if stopwords:
        words = [w for w in words if w and w not in stopwords]
    return [w for w in words if w]

text = "课程非常好，讲解清晰易懂！"
print(tokenize(text))
```

## 四、情感词典思路

- 正向词：好、清晰、推荐、不错、赞、喜欢……
- 负向词：差、烂、失望、过时、枯燥、困惑……

对一段文本：`score = (正向词数 - 负向词数) / 总词数`

## 五、数据结构

| 字段 | 含义 |
| ---- | ---- |
| review_id | 评论 ID |
| course_id | 课程 ID |
| text | 评论文本 |
| rating | 评分（1-5） |

## 六、分析目标

- 课程整体的**平均情感分**是多少？
- **好评 / 差评**各有多少条？
- 好评和差评的代表性关键词分别是什么？
