import sys, os
sys.path.insert(0, os.path.dirname(__file__))
exec(open(os.path.join(os.path.dirname(__file__), "l4-2-template.py")).read()

r = solve()
assert isinstance(r, tuple)
assert r[0] == 5
assert abs(r[1] - 20.5) < 0.1
# 85+60+90+60+88 = 383, /5 = 76.6
assert abs(r[2] - 76.6) < 0.1
print("✅ l4-2 通过")
