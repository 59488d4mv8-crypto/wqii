import sys, os
sys.path.insert(0, os.path.dirname(__file__))
exec(open(os.path.join(os.path.dirname(__file__), "l2-2-template.py")).read()

r = solve()
assert isinstance(r, tuple)
assert r[0] == 66
assert abs(r[1] - 5.5) < 0.01
assert r[2] == 11
assert list(r[3]) == [1, 5, 9]
print("✅ l2-2 通过")
