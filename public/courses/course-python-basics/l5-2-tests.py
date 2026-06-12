import sys, os
sys.path.insert(0, os.path.dirname(__file__))
exec(open(os.path.join(os.path.dirname(__file__), "l5-2-template.py")).read()

r = solve()
assert isinstance(r, tuple)
assert isinstance(r[0], str)  # top_region
assert r[1] > 0
assert r[2] > 0
# top_sum 应该大于等于全局均值（必然）
assert r[1] >= r[2]
print("✅ l5-2 通过")
