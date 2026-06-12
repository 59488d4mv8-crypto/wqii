import numpy as np
import pandas as pd
import sys
sys.path.insert(0, '.')
from lesson4_template import segment, segment_counts


def test_segment_column():
    df = pd.read_csv('../../datasets/rfm_data.csv')
    d = segment(df)
    assert 'segment' in d.columns


def test_segment_values():
    df = pd.read_csv('../../datasets/rfm_data.csv')
    d = segment(df)
    segs = set(d['segment'].unique())
    expected = {"重要价值", "重要保持", "重要发展", "重要挽留",
                "一般价值", "一般保持", "一般发展", "一般挽留"}
    assert segs.issubset(expected)


def test_counts_dict():
    df = pd.read_csv('../../datasets/rfm_data.csv')
    c = segment_counts(df)
    assert isinstance(c, dict)


def test_counts_sum():
    df = pd.read_csv('../../datasets/rfm_data.csv')
    c = segment_counts(df)
    assert sum(c.values()) == len(df)


if __name__ == "__main__":
    test_segment_column()
    test_segment_values()
    test_counts_dict()
    test_counts_sum()
    print("lesson4 tests passed")
