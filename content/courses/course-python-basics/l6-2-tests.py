import sys, os
sys.path.insert(0, os.path.dirname(__file__))
exec(open(os.path.join(os.path.dirname(__file__), "l6-2-template.py")).read()

r = solve()
assert isinstance(r, tuple)
assert isinstance(r[0], str)
assert r[2] > 0  # 总销售额 > 0
print("✅ l6-2 通过")
