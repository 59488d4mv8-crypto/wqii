# 商务数据分析在线教育平台 - 产品需求文档 (PRD)

## Overview
- **Summary**: 一个基于 Python 的商务数据分析与应用专业在线教育平台，面向高校/高职该专业学生，提供完整的课程体系、交互式学习、练习与测评以及成就激励系统。平台前端部署于 Cloudflare Pages（免费计划），数据与学习进度持久化于浏览器本地存储，Python 数据分析代码通过 Pyodide 在浏览器端运行，避免后端服务器依赖。
- **Purpose**: 解决商务数据分析专业学生"课堂理论为主、动手实践不足、学习动力难以持续"的痛点，构建一个轻量、可零成本部署、易于教师二次扩展课程内容的在线学习平台。
- **Target Users**:
  - 高职/本科商务数据分析与应用专业学生（核心用户）
  - 商务数据分析课程教师（内容维护者/使用者）
  - 对数据分析有兴趣的自学者

## Goals
- 提供覆盖商务数据分析核心知识域的完整课程体系
- 通过浏览器内 Python 环境（Pyodide）实现"学—练—测"一体化的互动体验
- 通过成就系统（经验值、徽章、排行榜、连续学习天数）维持长期学习动机
- 在 Cloudflare Pages Free 计划下稳定部署，无额外运营成本
- 课程内容以 Markdown/YAML 数据驱动，便于教师二次扩展

## Non-Goals (Out of Scope)
- 不做视频点播/直播课（以图文 + 互动代码为主）
- 不做付费订阅/会员系统（全部内容免费）
- 不做多人实时协作编程
- 不做复杂的用户体系（如邮箱注册、短信验证），仅使用浏览器本地 + 可选的本地"学生昵称"
- 不做后端持久化数据库服务端（免费方案下不引入 R2/KV 的付费超限风险）；学习数据默认保存在用户本地浏览器

## Background & Context
- Cloudflare Pages Free 计划约束：静态站点、构建次数/带宽有限；Pages Functions（Workers）可用但需注意免费额度
- Python 在浏览器端运行的成熟方案：[Pyodide](https://pyodide.org/)（基于 WebAssembly，支持 numpy / pandas / matplotlib / scikit-learn 等核心数据分析库）
- 国内高校商务数据分析专业的典型课程模块：Excel 数据分析、Python 数据分析、商务统计、数据可视化、市场/销售/财务数据分析、商业智能与报告
- 本平台阶段三"十大实战项目"统一围绕"在线教育平台"业务主题，按业务分析流程递进：用户注册活跃分析 → 完课率与流失预测 → RFM 用户价值 → NLP 评论情感 → 学习时长与成绩相关性 → 付费转化漏斗 → 关联规则推荐 → 时间序列预测 → 教师综合评分 → 用户画像与运营策略

## Functional Requirements
- **FR-1 课程体系展示**: 首页按"三阶段"呈现课程路线图，每门课程包含多个章节与课时；课时支持"图文讲解 + 代码练习 + 测验"三种混合内容。三阶段如下：
  - **阶段一 · 基础工具**：Python 数据分析基础（NumPy / Pandas / Matplotlib 基础）
  - **阶段二 · 方法工具**：商务统计与假设检验、数据清洗与特征工程、数据可视化进阶
  - **阶段三 · 十大实战项目**：围绕"在线教育平台"业务场景，10 个端到端分析项目（详见下文列表）
- **FR-2 交互式 Python 学习环境**: 在课时页嵌入可编辑、可运行的 Python 代码编辑器，支持以下能力：执行代码、查看 stdout/stderr、展示 pandas DataFrame 表格、渲染 matplotlib/seaborn 图表、预设数据集（CSV）。
- **FR-3 练习题与即时反馈**: 每个代码练习包含"题目描述 + 预设代码模板 + 自动判题"；判题通过在 Pyodide 沙箱内运行断言脚本实现，支持"正确/错误 + 提示语"反馈。
- **FR-4 单元测验与综合测评**: 每章结束有 5–10 题客观题（单选/多选/判断/填空）；课程结束有综合测评（15–20 题 + 1 道综合代码题）；成绩 ≥60 记为通过。
- **FR-5 成就激励系统**: 用户获得经验值（XP）、等级（Level）、徽章（Badge）、连续学习天数（Streak）、学习日历热力图；在"我的成就"页可视化展示。
- **FR-6 学习进度记录**: 自动记录已完成课时、最近学习位置、各章节得分；支持"继续学习"一键跳回上次停留的课时。
- **FR-7 本地数据管理**: 学习记录存储于 `localStorage`/`IndexedDB`；支持"导出学习档案 JSON"与"导入学习档案 JSON"，方便跨设备迁移。
- **FR-8 响应式 UI**: 支持桌面浏览器与移动浏览器基本浏览；深色/浅色主题切换。

## Non-Functional Requirements
- **NFR-1 首屏加载时间**: 非首次访问 ≤ 2s（中国国内网络环境需允许 Pyodide 首次加载约 5–10s，需做友好的加载提示）
- **NFR-2 代码执行安全**: Pyodide 代码运行在浏览器沙箱，不能访问本机文件系统；平台不收集任何代码内容到服务器
- **NFR-3 可扩展性**: 新增一门课程只需新增一个 Markdown/YAML 课程包，无需修改核心代码
- **NFR-4 可访问性**: 所有按钮/输入控件可键盘操作；主要文字颜色对比度满足 WCAG AA
- **NFR-5 浏览器兼容**: Chrome/Edge/Firefox/Safari 最新两个主版本
- **NFR-6 Cloudflare Free 兼容性**: 站点打包后静态资源总大小 ≤ 200MB；Pages Functions 不被用于代码执行（代码执行完全在浏览器）

## Constraints
- **Technical**: 静态站点部署于 Cloudflare Pages；Python 执行基于 Pyodide（WASM）；前端使用原生 HTML/CSS/JS 或轻量框架（建议：Vite + Vue 3 或直接原生 JS 以减小体积）
- **Business**: 零运营成本；不收集个人信息（符合最小化原则与免费工具的隐私要求）
- **Dependencies**: Pyodide CDN、Markdown 渲染库（如 `marked`）、图表渲染沿用 matplotlib 在 Pyodide 中生成 PNG/SVG

## Assumptions
- 用户使用较新的浏览器并支持 WebAssembly
- 教师会通过 Git 提交新的课程内容 Markdown 文件
- 代码执行所需数据集（CSV/Excel）随课程内容一同打包进静态站点
- Cloudflare Pages Free 的构建与带宽配额在常规使用下不会被突破

## Acceptance Criteria

### AC-1: 课程路线图可见
- **Given**: 用户首次进入首页
- **When**: 页面加载完成
- **Then**: 能看到按阶段组织的课程卡片（至少 3 门课、每门课包含 ≥ 2 个章节），点击卡片可进入课程详情
- **Verification**: `programmatic` + `human-judgment`

### AC-2: 课时浏览支持图文讲解
- **Given**: 用户进入某一课时
- **When**: 该课时是讲解型内容
- **Then**: 能够看到 Markdown 渲染的正文、代码高亮示例、必要图片/表格
- **Verification**: `human-judgment`

### AC-3: 浏览器内可运行 Python 代码并看到输出
- **Given**: 用户处于互动课时
- **When**: 点击"运行代码"按钮
- **Then**: 在输出区看到 stdout 文本输出；若代码产生 DataFrame，以 HTML 表格呈现；若代码产生 matplotlib 图，在输出区看到图片
- **Verification**: `programmatic`（运行预置样例并断言有输出）

### AC-4: 练习代码判题能给出正确/错误反馈
- **Given**: 用户处于一个带判题的练习课时，题目答案函数 `solve()` 存在断言检查
- **When**: 用户点击"提交"
- **Then**: 若答案通过断言，显示"✓ 正确"并给 XP；否则显示"✗ 错误"及提示语，不扣分
- **Verification**: `programmatic`

### AC-5: 单元测验计分与通过判定
- **Given**: 用户在章节末尾开始单元测验
- **When**: 作答并提交
- **Then**: 系统计算得分（百分制），≥60 标记为通过，并写入学习档案
- **Verification**: `programmatic`

### AC-6: 综合测评通过后获得课程结业徽章
- **Given**: 用户完成某门课程的综合测评且得分 ≥ 60
- **When**: 提交测评成功
- **Then**: 获得对应课程的"结业"徽章，并在"我的成就"页可见
- **Verification**: `programmatic`

### AC-7: 连续学习天数可累计并中断清零
- **Given**: 用户昨日已登录并完成任意课时
- **When**: 用户今日完成至少一个课时
- **Then**: 连续学习天数 +1；若超过 24 小时未学习则连续天数回到 0（但历史最长记录保留）
- **Verification**: `programmatic`

### AC-8: 学习进度跨刷新保留
- **Given**: 用户已完成若干课时并获得 XP
- **When**: 关闭并重新打开浏览器
- **Then**: 首页依然显示"继续学习"按钮，并展示累计 XP、等级、徽章
- **Verification**: `programmatic`

### AC-9: 支持学习档案的导出/导入
- **Given**: 用户点击"导出学习档案"
- **When**: 选择导出后再在另一浏览器/设备点击"导入学习档案"并选择该 JSON
- **Then**: 导入后该设备的进度/XP/徽章与原设备一致
- **Verification**: `programmatic`

### AC-10: 站点成功部署到 Cloudflare Pages
- **Given**: 项目代码已推送到 Git 仓库并关联 Cloudflare Pages
- **When**: Pages 构建完成
- **Then**: 通过 `*.pages.dev` 子域可访问，首屏无 404/白屏；Pyodide 样例代码可执行
- **Verification**: `human-judgment`

## Open Questions
- [ ] 是否需要一个"教师控制台"用于可视化新建课程？当前方案采用 Git + Markdown 数据驱动。
- [ ] 是否需要在学校场景下做一个简单的班级/学号字段？当前方案不引入身份体系。
- [ ] 课程内容由哪一方提供？（本次平台交付时将同时内置 2–3 门示例课程，方便教师参考。）
- [ ] 是否需要 PWA 离线缓存？当前可作为后续增强。
