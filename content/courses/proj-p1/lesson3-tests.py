import numpy as np
import pandas as pd
import sys
sys.path.insert(0, '.')
from lesson3_template import channel_counts, top_channel


def test_counts_shape():
    reg = pd.read_csv('../../datasets/user_registrations.csv')
    c = channel_counts(reg)
    assert len(c) == reg['channel'].nunique()


def test_counts_sum():
    reg = pd.read_csv('../../datasets/user_registrations.csv')
    c = channel_counts(reg)
    assert c.sum() == len(reg)


def test_top_channel_name():
    reg = pd.read_csv('../../datasets/user_registrations.csv')
    name, cnt = top_channel(reg)
    assert isinstance(name, str) and len(name) > 0


def test_top_channel_max():
    reg = pd.read_csv('../../datasets/user_registrations.csv')
    c = channel_counts(reg)
    _, cnt = top_channel(reg)
    assert cnt == c.max()


if __name__ == "__main__":
    test_counts_shape()
    test_counts_sum()
    test_top_channel_name()
    test_top_channel_max()
    print("lesson3 tests passed")
