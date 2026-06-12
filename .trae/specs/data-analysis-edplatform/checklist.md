# 商务数据分析在线教育平台 - 验证清单 (checklist.md)

以下检查点按"功能域"分组。每个任务完成后，请执行者/评审者对应勾选。

## 项目结构与内容扩展性
- [ ] Checkpoint 1: 项目根目录存在 `public/`、`src/`、`content/courses/`、`content/datasets/` 四个子目录
- [ ] Checkpoint 2: `scripts/validate_content.py` 对示例课程包能成功执行，退出码为 0
- [ ] Checkpoint 3: 在 `content/courses/` 下新增一个最小课程包（1 章节 1 课时）后，首页能自动显示该课程，无需修改核心代码

## 首页与导航
- [ ] Checkpoint 4: 首页按"入门 / 进阶 / 实战"三个阶段展示至少 3 门课程
- [ ] Checkpoint 5: 点击课程卡片可进入课程详情页，URL 中能看到可识别的课程标识（query 或 hash）
- [ ] Checkpoint 6: 右上角显示当前用户的 XP / 等级 / 连续学习天数迷你条
- [ ] Checkpoint 7: "继续学习"按钮可跳转到上次停留的课时

## 课时阅读与 Markdown 渲染
- [ ] Checkpoint 8: 课时正文能正确渲染标题、段落、列表、表格
- [ ] Checkpoint 9: Python 代码块有语法高亮
- [ ] Checkpoint 10: 长内容在移动端可纵向滚动，横向不溢出

## 浏览器内 Python 执行
- [ ] Checkpoint 11: 首次打开互动课时，会出现"Pyodide 加载中"友好提示；完成后可执行代码
- [ ] Checkpoint 12: 运行 `print("hello")` 可在输出区看到 "hello"
- [ ] Checkpoint 13: 运行包含 `pd.DataFrame(...)` 的示例，输出区能渲染 HTML 表格
- [ ] Checkpoint 14: 运行包含 matplotlib 的示例，输出区能看到生成的图片（PNG 或 SVG）
- [ ] Checkpoint 15: 代码执行出错（比如语法错误）时，输出区显示错误信息而非整页崩溃

## 代码练习与判题
- [ ] Checkpoint 16: 存在"提交"按钮，可运行判题脚本
- [ ] Checkpoint 17: 正确答案提交后显示"✓ 正确"并增加对应 XP
- [ ] Checkpoint 18: 错误答案提交后显示"✗ 错误"与提示语，不扣减已有 XP
- [ ] Checkpoint 19: "重置为模板"可将编辑区恢复为 lesson 中的初始代码

## 客观题测验
- [ ] Checkpoint 20: 单选题选中后可提交，对错有即时反馈
- [ ] Checkpoint 21: 多选题必须全部选中才判对；漏选/错选判错
- [ ] Checkpoint 22: 判断题 True/False 交互正常
- [ ] Checkpoint 23: 填空题支持大小写不敏感或规则可配置，并正确判分
- [ ] Checkpoint 24: 提交后按正确比例计算得分（百分制），并写入学习档案

## 综合测评与徽章
- [ ] Checkpoint 25: 课程末尾存在综合测评入口
- [ ] Checkpoint 26: 综合测评得分 = 客观题 × 60% + 代码题 × 40%
- [ ] Checkpoint 27: 得分 ≥ 60 时获得课程结业徽章；< 60 时不获得
- [ ] Checkpoint 28: "我的成就"页能看到新获得的徽章

## 成就激励系统
- [ ] Checkpoint 29: 每完成一个课时 XP 增加；每满 100 XP 升一级
- [ ] Checkpoint 30: 首次完成任意课时后获得"迈出第一步"徽章
- [ ] Checkpoint 31: 连续两天完成学习，连续学习天数 +1
- [ ] Checkpoint 32: 中断一天以上重新开始，连续学习天数重置为 1，但历史最长记录保留
- [ ] Checkpoint 33: 学习热力图正确显示近 365 天活跃情况

## 本地存储与导入/导出
- [ ] Checkpoint 34: 刷新浏览器后，XP、等级、徽章、课程进度保持不变
- [ ] Checkpoint 35: 导出按钮可下载 JSON 文件
- [ ] Checkpoint 36: 导入合法 JSON 可恢复进度；导入后再刷新，数据仍保留
- [ ] Checkpoint 37: 导入非法 JSON 不会崩溃，显示友好错误
- [ ] Checkpoint 38: 提供"重置所有进度"按钮，点击后清空学习档案

## 主题与响应式
- [ ] Checkpoint 39: 浅色/深色主题可切换，且刷新后记忆
- [ ] Checkpoint 40: 手机/平板/桌面三端均无横向滚动，布局合理
- [ ] Checkpoint 41: 主要操作可通过键盘 Tab/Enter/Esc 完成

## Cloudflare Pages 部署
- [ ] Checkpoint 42: `public/`（或根目录）作为 Pages 输出目录可成功构建
- [ ] Checkpoint 43: 构建日志无错误；部署后 `*.pages.dev` 可正常访问首页
- [ ] Checkpoint 44: 部署后互动课时可正常加载 Pyodide 并运行代码
- [ ] Checkpoint 45: 静态资源总大小 ≤ 200MB（符合 Free 计划的常识约束）

## 内容完整性
- [ ] Checkpoint 46: 阶段一基础课 `course-python-basics` 含 6 个章节，每章含图文讲解 + 代码练习 + 测验
- [ ] Checkpoint 47: 阶段二 3 门方法课（商务统计、特征工程、可视化进阶）内容齐备
- [ ] Checkpoint 48: 阶段三 10 个实战项目全部上线，每门含业务背景 + 数据集 + 代码实践 + 综合测评
- [ ] Checkpoint 49: 每门课程末有综合测评，满分 ≥ 60 可结业并获得徽章
- [ ] Checkpoint 50: 所有数据集 CSV 文件在 `content/datasets/` 目录下，代码练习中 `pd.read_csv()` 可正常读取
- [ ] Checkpoint 51: 项目 4（NLP 情感分析）使用纯 Python 分词与规则情感，不依赖 jieba/snownlp，可在 Pyodide 内运行
- [ ] Checkpoint 52: 项目 7（关联规则）手写 Apriori 算法，不依赖 mlxtend，在玩具数据集上有预期输出

## 浏览器端冒烟测试
- [ ] Checkpoint 53: `tests/smoke.test.mjs` 在本地通过
- [ ] Checkpoint 54: 测试覆盖"打开首页 → 进入基础课 → 完成练习 → 进入实战项目 → XP 增加"主流程
