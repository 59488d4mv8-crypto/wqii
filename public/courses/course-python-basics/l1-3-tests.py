# 由平台自动运行，请勿在此编辑
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
exec(open(os.path.join(os.path.dirname(__file__), "l1-3-template.py")).read())

result = solve()
assert isinstance(result, tuple), "solve() 必须返回一个 tuple"
assert result[0] == 55, f"nums 的和应为 55，实际 {result[0]}"
assert result[1] == 2, f"info 的 keys 数量应为 2，实际 {result[1]}"
assert result[2] == "Hello, World!", f"greet('World') 应为 'Hello, World!'，实际 {result[2]}"
print("✅ l1-3 通过")
