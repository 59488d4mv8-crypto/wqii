import re

STOPWORDS = {"的", "了", "是", "在", "和", "也", "就", "都", "我", "你", "他", "她",
             "它", "这", "那", "个", "有", "还", "会", "能", "要", "不", "没", "吗",
             "呢", "啊", "吧", "很", "非常", "特别", "真的", "的话", "但是", "而且"}


def tokenize(text, stopwords=None):
    if stopwords is None:
        stopwords = STOPWORDS
    tokens = re.split(r'[，。！？!?,.\s]+', text)
    tokens = [t for t in tokens if t and t not in stopwords]
    return tokens


def tokenize_all(texts):
    out = []
    for t in texts:
        out.extend(tokenize(t))
    return out


if __name__ == "__main__":
    print(tokenize("课程非常好，讲解清晰易懂！"))
