import sys, os
sys.path.insert(0, os.path.dirname(__file__))
exec(open(os.path.join(os.path.dirname(__file__), "l3-2-template.py")).read()

r = solve()
assert isinstance(r, tuple)
assert r[0] == 20  # 20 行数据
assert r[1] == 5   # 5 列
# 不硬编码总和，只检查正数
assert r[2] > 0
assert isinstance(r[3], str)
print("✅ l3-2 通过")
