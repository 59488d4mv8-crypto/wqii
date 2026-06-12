import sys, os
sys.path.insert(0, os.path.dirname(__file__))
exec(open(os.path.join(os.path.dirname(__file__), "exam-template.py")).read()

r = solve()
assert isinstance(r, dict), "solve() 必须返回 dict"
required = ["total_sales", "avg_amount", "top_region", "top_product", "num_orders"]
for k in required:
    assert k in r, f"缺少键 {k}"

assert r["num_orders"] == 20, f"行数应为 20，实际 {r['num_orders']}"
assert r["total_sales"] > 0
assert abs(r["avg_amount"] - r["total_sales"] / 20) < 1.0
assert r["top_region"] == "华东", f"top_region 应为 华东，实际 {r['top_region']}"
assert r["top_product"] == "产品A", f"top_product 应为 产品A，实际 {r['top_product']}"
print("✅ exam 通过")
