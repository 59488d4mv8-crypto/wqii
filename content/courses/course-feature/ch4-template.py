import numpy as np
import pandas as pd


def label_encode(s, mapping):
    # TODO: 按 mapping 字典对 Series s 做 label encoding，返回编码后的 Series
    pass


def one_hot_encode(s, prefix):
    # TODO: 对 s 做 one-hot encoding，列名使用 prefix_类别，返回 DataFrame
    pass


def freq_encode(s):
    # TODO: 对 s 做频次编码，返回每个值被替换为其出现频率的 Series
    pass


def encode_dataframe(df, label_col, one_hot_col, label_map):
    # TODO: 对 df 的 label_col 做 label，对 one_hot_col 做 one-hot，
    # 返回处理后的 df
    pass


if __name__ == "__main__":
    df = pd.DataFrame({
        "size": ["S", "M", "L", "XL", "M"],
        "city": ["BJ", "SH", "BJ", "GZ", "SH"]
    })
    print(label_encode(df["size"], {"S":0,"M":1,"L":2,"XL":3}))
    print(one_hot_encode(df["city"], "city"))
    print(freq_encode(df["city"]))
    print(encode_dataframe(df, "size", "city", {"S":0,"M":1,"L":2,"XL":3}))
