import numpy as np

def solve():
    """
    NumPy 练习：
    1. 创建一个 shape=(3, 4) 的数组，值为 0 到 11
    2. 计算数组的总和、均值、最大值
    3. 取第二列（index=1）所有元素
    4. 返回 (sum, mean, max_val, second_col)
    """
    arr = np.arange(12).reshape(3, 4)
    total = int(arr.sum())
    mean_val = float(arr.mean())
    max_val = int(arr.max())
    second_col = arr[:, 1].tolist()
    return (total, mean_val, max_val, second_col)


if __name__ == "__main__":
    print(solve())
