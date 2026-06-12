# TODO：请实现以下函数

def solve():
    """
    完成基础语法练习：
    1. 创建一个列表 nums，包含数字 1 到 10
    2. 创建一个字典 info，键为 "name", "age"，值自定
    3. 编写一个函数 greet(name)，返回 "Hello, {name}!"
    4. 返回 (nums 的和, info 的 keys 数量, greet("World"))
    """
    nums = list(range(1, 11))
    info = {"name": "student", "age": 20}

    def greet(name):
        return f"Hello, {name}!"

    return (sum(nums), len(info.keys()), greet("World"))


if __name__ == "__main__":
    print(solve())
