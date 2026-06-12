# 商务数据分析在线教育平台 - 实施计划 (tasks.md)

## [ ] Task 1: 项目脚手架与目录结构
- **Priority**: P0
- **Depends On**: None
- **Description**:
  - 创建项目根目录结构：`public/`（静态资源与数据集）、`src/`（前端代码）、`content/courses/`（课程 Markdown）、`content/datasets/`（CSV/Excel 数据集）
  - 引入基础依赖：Pyodide（CDN）、`marked`（Markdown 渲染）、`highlight.js`（代码高亮），选择"原生 ES Modules + 无构建"方案以最小化 Cloudflare Pages 构建压力
  - 定义课程包 schema：每门课程对应一个 `course.json` + 若干 `lesson-*.md`；lesson 类型包含 `read`/`code`/`quiz`/`exam`
- **Acceptance Criteria Addressed**: AC-1, AC-2, NFR-6
- **Test Requirements**:
  - `programmatic` TR-1.1: `python scripts/validate_content.py` 对所有课程 JSON 与 Markdown 做 schema 校验，退出码为 0
  - `human-judgement` TR-1.2: 本地启动静态服务器（`python -m http.server`）后可浏览首页骨架
- **Notes**: 选择"零构建"静态方案可避免 Pages 构建时长超限；所有依赖通过 CDN（jsDelivr / unpkg）加载

## [ ] Task 2: 首页与课程路线图
- **Priority**: P0
- **Depends On**: Task 1
- **Description**:
  - 实现首页：Hero、课程路线图（阶段：入门 / 进阶 / 实战）、课程卡片网格、"我的成就"迷你条（XP、等级、连续学习天数）、"继续学习"入口
  - 从 `content/courses/*.json` 动态加载课程元数据
- **Acceptance Criteria Addressed**: AC-1, AC-8
- **Test Requirements**:
  - `programmatic` TR-2.1: 打开首页后，`window.__APP__.courses` 长度 ≥ 3
  - `human-judgement` TR-2.2: 手机 360px / 平板 768px / 桌面 1280px 三个尺寸下无横向滚动

## [ ] Task 3: 课程详情与章节/课时导航
- **Priority**: P0
- **Depends On**: Task 2
- **Description**:
  - 实现课程详情页：课程简介、章节列表、每个课时的"已完成/未完成"状态、学习进度百分比
  - 实现课时页 URL hash 路由或 History API；点击课时进入对应内容页
- **Acceptance Criteria Addressed**: AC-1, AC-2, AC-8
- **Test Requirements**:
  - `programmatic` TR-3.1: 进入课时页后，URL 包含 `course`、`chapter`、`lesson` 参数/片段
  - `human-judgement` TR-3.2: 章节折叠/展开交互清晰，已完成课时有明显的 ✓ 标记

## [ ] Task 4: 课时内容渲染（图文讲解）
- **Priority**: P0
- **Depends On**: Task 3
- **Description**:
  - 解析 lesson Markdown 文件，使用 `marked` 渲染正文、`highlight.js` 做代码高亮
  - 支持自定义组件语法：`@@exercise`（代码练习块）、`@@quiz`（客观题块）、`@@dataset(xxx.csv)`（数据集插入）
- **Acceptance Criteria Addressed**: AC-2
- **Test Requirements**:
  - `programmatic` TR-4.1: 预置示例课时渲染后 DOM 中至少有 1 个 `<pre><code class="language-python">` 元素
  - `human-judgement` TR-4.2: 标题层级、表格、列表可读性良好

## [ ] Task 5: 封装 Pyodide 运行时模块
- **Priority**: P0
- **Depends On**: Task 1
- **Description**:
  - 封装 `src/pyodide.js`：`ensurePyodide()`、`runPython(code)`、`runPythonAsync(code)`、`readDataset(path)`
  - 约定 stdout/stderr 被捕获；支持捕获 `matplotlib` 的 Figure 为 SVG；支持捕获 pandas `DataFrame` 最后表达式为 HTML 表格
  - 全局单例 + 加载进度提示
- **Acceptance Criteria Addressed**: AC-3, NFR-2
- **Test Requirements**:
  - `programmatic` TR-5.1: 执行 `print("hello")` 返回 stdout 包含 "hello"
  - `programmatic` TR-5.2: 执行 `import pandas as pd; pd.DataFrame({"a":[1,2]})` 的返回结果能渲染为 `<table>`
  - `programmatic` TR-5.3: 执行 `import matplotlib; ...; plt.show()` 返回 `<img>` 或 SVG

## [ ] Task 6: 交互式代码编辑器与运行面板
- **Priority**: P0
- **Depends On**: Task 5
- **Description**:
  - 在课时页内提供代码编辑区（`<textarea>` 或 CodeMirror 5 精简版）、运行按钮、停止按钮、输出区
  - 支持"重置为模板""复制代码""下载代码"
- **Acceptance Criteria Addressed**: AC-3
- **Test Requirements**:
  - `programmatic` TR-6.1: 点击"运行"后 15 秒内（允许 Pyodide 冷启动）输出区出现文本
  - `human-judgement` TR-6.2: 编辑区语法高亮可读，Tab/Shift+Tab 缩进体验顺畅

## [ ] Task 7: 代码练习 + 断言判题
- **Priority**: P0
- **Depends On**: Task 6
- **Description**:
  - 在 lesson Markdown 中通过 `@@exercise` 定义：模板代码、判题代码（以 `assert` 为主）、提示语、XP 奖励
  - 前端执行"先执行用户 solve() → 再执行判题脚本"；捕获断言错误并给出错误提示；通过则增加 XP
- **Acceptance Criteria Addressed**: AC-4, AC-6
- **Test Requirements**:
  - `programmatic` TR-7.1: 内置一道"答案唯一"的样题（如 `solve(): return 42`），运行正确判题返回 `{ok:true}`，错误返回 `{ok:false, hint:"..."}`
  - `programmatic` TR-7.2: 通过后用户 XP 增加对应值（localStorage 中 `profile.xp` 有增长）

## [ ] Task 8: 客观题测验引擎（单选/多选/判断/填空）
- **Priority**: P0
- **Depends On**: Task 4
- **Description**:
  - 在 Markdown 中 `@@quiz` 块定义若干题，支持题型 `single`、`multi`、`bool`、`fill`
  - 计分规则：客观题按题均分；提交后显示对错与正确答案；得分记录到学习档案
- **Acceptance Criteria Addressed**: AC-5
- **Test Requirements**:
  - `programmatic` TR-8.1: 提交全部正确时得分为 100
  - `programmatic` TR-8.2: 提交部分正确时得分按比例计算（保留到整数）

## [ ] Task 9: 综合测评（综合客观题 + 综合代码题）
- **Priority**: P1
- **Depends On**: Task 7, Task 8
- **Description**:
  - 每门课程末尾设一个综合测评 lesson：15–20 道客观题 + 1 道代码综合题（代码题同样使用 Task 7 的判题机制）
  - 代码综合题分数占比 40%，客观题 60%；总分 ≥ 60 视为通过，颁发"结业徽章"
- **Acceptance Criteria Addressed**: AC-6
- **Test Requirements**:
  - `programmatic` TR-9.1: 总分 ≥ 60 时 `profile.badges` 中出现该课程结业徽章 id
  - `programmatic` TR-9.2: 总分 < 60 时不颁发徽章

## [ ] Task 10: 学习档案与本地存储
- **Priority**: P0
- **Depends On**: Task 1
- **Description**:
  - 定义 `profile` schema：`{xp, level, nickname, streaks, badges:{id, earnedAt}, courses:{courseId:{completed, score, lastLessonId, completedLessons:[...]}}}`
  - 提供 `src/storage.js`：`loadProfile()`, `saveProfile(profile)`, `resetProfile()`
  - 使用 `localStorage` 为默认存储；预留 IndexedDB 升级接口（暂不实现）
- **Acceptance Criteria Addressed**: AC-8
- **Test Requirements**:
  - `programmatic` TR-10.1: 刷新后 `loadProfile()` 返回的数据与刷新前一致
  - `programmatic` TR-10.2: 调用 `resetProfile()` 后 profile 恢复默认值

## [ ] Task 11: 成就激励系统（XP / 等级 / 徽章 / 连续天数 / 热力图）
- **Priority**: P0
- **Depends On**: Task 10
- **Description**:
  - XP 规则：完成一个 read 课时 +5，code 练习通过 +20，quiz 测验按"得分 × 0.3"取整；每满 100 XP 升一级
  - 徽章：至少 10 枚基础徽章 + 14 枚课程结业徽章
    - 基础徽章："迈出第一步"（完成首个课时）、"代码小能手"（通过 10 道代码题）、"测试达人"（3 次测验 ≥ 80 分）、"连续学习 7 天"、"连续学习 30 天"、"图表收藏家"（生成 20 张图表）、"数据侦探"（完成任意实战项目）、"实战先锋"（完成 5 个实战项目）、"全能分析师"（完成全部 10 个实战项目）、"教师之友"（完成教师综合评分项目）
    - 课程结业徽章：4 门基础/方法课 + 10 门实战项目课 → 每门通过后自动获得对应徽章
  - 连续学习天数：记录 `lastActiveDate`，每次完成任务时更新；如果是当天首次则 `streak+1`；若 gap > 1 天则 `streak=1`；保留 `maxStreak`
  - 学习热力图：基于 `activeDates` 记录（Set<yyyy-mm-dd>），渲染近 365 天 GitHub 风格热力图
- **Acceptance Criteria Addressed**: AC-5, AC-6, AC-7
- **Test Requirements**:
  - `programmatic` TR-11.1: 首次完成任意课时后获得"迈出第一步"徽章
  - `programmatic` TR-11.2: 模拟昨天学习 + 今日学习 → streak 从 N → N+1；模拟 gap 3 天 → streak = 1
  - `human-judgement` TR-11.3: "我的成就"页的等级、XP 进度条、徽章墙、热力图视觉清晰

## [ ] Task 12: 学习档案导入/导出
- **Priority**: P1
- **Depends On**: Task 10
- **Description**:
  - 在"我的成就"页提供"导出 JSON"与"导入 JSON"按钮；导入前提示会覆盖当前进度；导入失败（格式错误）给出友好提示
- **Acceptance Criteria Addressed**: AC-9
- **Test Requirements**:
  - `programmatic` TR-12.1: 导出的 JSON 再次导入后，`profile.xp` 值与导出前一致
  - `programmatic` TR-12.2: 导入非法 JSON 不抛异常，仅显示提示

## [ ] Task 13: 主题切换与响应式样式
- **Priority**: P1
- **Depends On**: Task 2
- **Description**:
  - 使用 CSS 变量实现浅色/深色主题；跟随系统主题，并允许手动切换；记忆到 localStorage
  - 移动端优先的响应式布局；导航在手机端变为汉堡菜单
- **Acceptance Criteria Addressed**: FR-8, NFR-4, NFR-5
- **Test Requirements**:
  - `programmatic` TR-13.1: 切换主题后 `document.documentElement.dataset.theme` 从 `light` 变为 `dark`
  - `human-judgement` TR-13.2: 手机端点击菜单按钮后导航出现/隐藏动画流畅

## [ ] Task 14: 阶段一 · 基础工具课程（Python 数据分析基础）
- **Priority**: P0
- **Depends On**: Task 4, Task 7, Task 8
- **Description**:
  - 课程代号 `course-python-basics`，章节：① Python 与 Jupyter 基础 ② NumPy 数值计算 ③ Pandas 数据结构与读写 ④ Pandas 数据清洗（缺失值、重复值、异常值）⑤ 分组聚合与透视表 ⑥ Matplotlib 基础可视化
  - 每章至少 2 个课时（含图文讲解 + 1 个代码练习），章末 5 题客观测验，课程末 1 个综合代码题
  - 数据集：`datasets/sales_sample.csv`、`datasets/students.csv` 等小型样本
- **Acceptance Criteria Addressed**: AC-1, AC-3, AC-6
- **Test Requirements**:
  - `programmatic` TR-14.1: `scripts/validate_content.py` 校验该课程通过
  - `human-judgement` TR-14.2: 代码练习可在 Pyodide 中运行并被判题脚本通过

## [ ] Task 14B: 阶段二 · 方法工具课程（3 门）
- **Priority**: P0
- **Depends On**: Task 14
- **Description**:
  - `course-stats` 商务统计与假设检验：描述性统计、概率分布、t 检验、卡方检验、A/B 测试思维
  - `course-feature` 数据清洗与特征工程：缺失值处理、异常值、分箱、交叉特征、编码
  - `course-viz` 数据可视化进阶：Seaborn 高级图、漏斗图、桑基图、热力图
  - 每门课程结构与 Task 14 相同
- **Acceptance Criteria Addressed**: AC-1, AC-6
- **Test Requirements**:
  - `programmatic` TR-14B.1: `scripts/validate_content.py` 全部通过
  - `human-judgement` TR-14B.2: 三门课程在首页阶段二栏目可见且可完成

## [ ] Task 14P1: 实战项目 1 · 用户注册与活跃行为分析
- **Priority**: P1
- **Depends On**: Task 14
- **Description**:
  - 模拟数据集 `datasets/user_registrations.csv`、`datasets/daily_active.csv`（含注册渠道、注册时间、登录时间）
  - 课时：业务背景 → 数据概览 → 注册渠道对比 → 注册时段热力图 → DAU/WAU/MAU 计算 → N 日留存率曲线 → 结论与业务建议 → 综合代码练习题
- **Test Requirements**:
  - `programmatic` TR-P1.1: 所有代码练习在 Pyodide 内可运行且可被判题通过
  - `human-judgement` TR-P1.2: 课程末综合测评结果输出至少 3 张图表 + 文字结论

## [ ] Task 14P2: 实战项目 2 · 课程学习完课率与流失预测
- **Priority**: P1
- **Depends On**: Task 14
- **Description**:
  - 模拟数据集 `datasets/lesson_progress.csv`（user_id, course_id, chapter_id, progress, is_dropout, timestamp）
  - 课时：漏斗分析 → 各章节退出节点 → 流失特征热力图 → 简单流失预测（逻辑回归或阈值规则）→ 业务建议
- **Test Requirements**:
  - `programmatic` TR-P2.1: 漏斗图代码可运行并输出图像
  - `human-judgement` TR-P2.2: 学生可输出"最容易流失的 Top-3 章节"列表

## [ ] Task 14P3: 实战项目 3 · 在线教育用户 RFM 价值分层
- **Priority**: P1
- **Depends On**: Task 14
- **Description**:
  - 数据集：`datasets/rfm_data.csv`（user_id, last_learn_days, sessions, total_learn_minutes）
  - 课时：R/F/M 定义 → 分箱与打分 → 8 类用户分层（重要价值/重要保持/重要发展/重要挽留/一般价值/一般保持/一般发展/一般挽留）→ 可视化分组 → 运营策略输出
- **Test Requirements**:
  - `programmatic` TR-P3.1: RFM 分箱函数 `rfm_segment()` 单元测试通过
  - `human-judgement` TR-P3.2: 可输出针对每个分层的运营建议文本

## [ ] Task 14P4: 实战项目 4 · 课程评价 NLP 情感分析
- **Priority**: P1
- **Depends On**: Task 14
- **Description**:
  - 数据集：`datasets/course_reviews.csv`（review_id, course_id, text, rating）
  - 课时：中文分词（纯 Python 简易分词器 + 停用词表，避免 Pyodide 装 jieba）→ 词频统计 → WordCloud 词云（使用纯 Python 生成词频表，由 matplotlib 展示大小气泡代替 WordCloud 图形）→ 基于规则的情感打分（正向词/负向词词典）→ 好评/差评关键词 Top-10
- **Notes**: 为避免 Pyodide 第三方库安装限制，NLP 部分使用纯 Python 实现（不含 jieba / snownlp）。
- **Test Requirements**:
  - `programmatic` TR-P4.1: 分词函数可运行，词频表输出正确
  - `human-judgement` TR-P4.2: 输出每门课程的 3 条代表性好评词与 3 条差评词

## [ ] Task 14P5: 实战项目 5 · 学习时长与成绩相关性分析
- **Priority**: P1
- **Depends On**: Task 14
- **Description**:
  - 数据集：`datasets/study_behavior.csv`（user_id, chapter_id, duration, pause_count, seek_count, quiz_score）
  - 课时：变量描述 → Pearson 相关系数矩阵热力图 → 时长 vs 成绩散点图 → 简单线性回归（numpy.polyfit）→ 箱线图按"是否暂停过多"分组对比
- **Test Requirements**:
  - `programmatic` TR-P5.1: 相关系数矩阵输出 shape 正确
  - `human-judgement` TR-P5.2: 输出"对成绩影响最大的 3 个行为特征"文本

## [ ] Task 14P6: 实战项目 6 · 付费转化漏斗分析
- **Priority**: P1
- **Depends On**: Task 14
- **Description**:
  - 数据集：`datasets/conversion_funnel.csv`（stage, user_count, channel）
  - 课时：漏斗定义 → 各节点转化率计算 → 渠道对比漏斗图 → 转化卡点识别 → 提升建议
- **Test Requirements**:
  - `programmatic` TR-P6.1: 漏斗函数 `calc_funnel(df)` 返回各 stage 转化率
  - `human-judgement` TR-P6.2: 至少 2 个渠道的漏斗图横向对比

## [ ] Task 14P7: 实战项目 7 · 课程推荐关联规则（Apriori）
- **Priority**: P1
- **Depends On**: Task 14
- **Description**:
  - 数据集：`datasets/course_baskets.csv`（user_id, course_id）
  - 课时：事务数据格式 → 手写 Apriori 简化实现（1-itemsets → join → prune → 规则生成）→ 最小支持度/置信度/提升度 → "学了 A 还会学 B"推荐表 → 网络关系图
- **Notes**: 在 Pyodide 中手写 Apriori，避免安装 mlxtend
- **Test Requirements**:
  - `programmatic` TR-P7.1: 手写 Apriori 在玩具数据集上输出规则与期望一致
  - `human-judgement` TR-P7.2: 输出 Top-5 提升度最高的课程推荐规则

## [ ] Task 14P8: 实战项目 8 · 访问量与销量时间序列预测
- **Priority**: P1
- **Depends On**: Task 14
- **Description**:
  - 数据集：`datasets/daily_traffic.csv`（date, pv, uv, orders）
  - 课时：趋势图 → 7 日滑动平均 → 周季节性 → 简单移动平均预测（下一 7 天）→ 节假日异常标记 → 业务排期建议
- **Test Requirements**:
  - `programmatic` TR-P8.1: 滑动平均 `rolling_mean(series, 7)` 单元测试通过
  - `human-judgement` TR-P8.2: 预测下一 7 天曲线叠加在历史曲线上可看

## [ ] Task 14P9: 实战项目 9 · 教师授课质量多维度综合评分
- **Priority**: P1
- **Depends On**: Task 14
- **Description**:
  - 数据集：`datasets/teacher_metrics.csv`（teacher_id, avg_rating, completion_rate, interaction_rate, review_count）
  - 课时：指标标准化（Min-Max / Z-Score）→ 权重设定（等权 / AHP 思路）→ 综合评分 → 教师排名 → 雷达图 → 弱势维度建议
- **Test Requirements**:
  - `programmatic` TR-P9.1: 综合评分 `teacher_score(row)` 单元测试通过
  - `human-judgement` TR-P9.2: 至少一张教师对比雷达图

## [ ] Task 14P10: 实战项目 10 · 用户画像与精准运营策略
- **Priority**: P1
- **Depends On**: Task 14P3, Task 14P5
- **Description**:
  - 数据集：`datasets/user_profile.csv`（user_id, age, region, device, prefer_subject, active_hour）
  - 课时：变量聚合与分布 → 饼图 + 柱状图 → 偏好交叉分析 → 输出三类典型用户画像（"白天学习型学生"、"夜猫子型自学者"、"周末集中学习者"）→ 运营策略矩阵
- **Test Requirements**:
  - `programmatic` TR-P10.1: 画像分组 `segment_user(row)` 单元测试通过
  - `human-judgement` TR-P10.2: 输出一张"画像 × 运营策略"表格

## [ ] Task 15: Cloudflare Pages 部署配置
- **Priority**: P0
- **Depends On**: Task 1
- **Description**:
  - 在项目根目录添加 `public/` 或根目录静态文件；`_headers` 文件用于设置安全响应头（Content-Security-Policy 允许 Pyodide CDN）
  - 添加 `_redirects`（可选）与 `robots.txt`
  - 添加 `README.md` 的 Cloudflare Pages 部署小节（连接 Git 仓库 → 选择项目 → 构建命令留空或 `python scripts/build.py` 若需要内容预处理 → 输出目录设为 `/` 或 `public/`）
- **Acceptance Criteria Addressed**: AC-10, NFR-6
- **Test Requirements**:
  - `human-judgement` TR-15.1: 在本地 `python -m http.server --directory public` 可访问并完成一次完整学习流程
  - `programmatic` TR-15.2: Cloudflare Pages 构建日志显示成功（Build successful）

## [ ] Task 16: 浏览器端端到端冒烟测试
- **Priority**: P1
- **Depends On**: Task 14, Task 14B, Task 14P1, Task 15
- **Description**:
  - 编写 `tests/smoke.test.mjs`（或使用 Playwright 轻量方案）：启动静态服务器 → 打开首页 → 进入 `course-python-basics` → 完成第一个代码练习 → 进入实战项目 1 课程 → 完成一个课时 → 检查 XP 增长
- **Acceptance Criteria Addressed**: AC-1, AC-3, AC-4, AC-8
- **Test Requirements**:
  - `programmatic` TR-16.1: 测试脚本以退出码 0 成功
  - `programmatic` TR-16.2: 测试脚本覆盖基础课与至少 1 个实战项目

## [x] 任务状态维护约定
- 每项任务完成后，执行者更新本文件中对应任务的 `[ ]` 为 `[x]`，并在 checklist.md 中勾选相关检查点。
