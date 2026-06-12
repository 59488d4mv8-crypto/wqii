// scripts/build.js
// Cloudflare Pages 构建脚本：将 content/ 复制到 public/ 并生成课程索引
// 本项目是零依赖的静态站，构建仅做一致性检查与目录整理
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const PUBLIC = path.join(ROOT, 'public');
const CONTENT = path.join(ROOT, 'content');

function ensureDir(dir) {
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
}

function copyRecursive(src, dst) {
  if (!fs.existsSync(src)) return;
  const stat = fs.statSync(src);
  if (stat.isDirectory()) {
    ensureDir(dst);
    for (const name of fs.readdirSync(src)) {
      copyRecursive(path.join(src, name), path.join(dst, name));
    }
  } else {
    fs.copyFileSync(src, dst);
  }
}

function buildCourseIndex() {
  // 扫描 content/courses 下的 course.json，写入 public/courses/index.json
  const coursesDir = path.join(CONTENT, 'courses');
  const indexPath = path.join(PUBLIC, 'courses', 'index.json');
  ensureDir(path.join(PUBLIC, 'courses'));

  const index = { courses: [] };
  if (!fs.existsSync(coursesDir)) {
    console.warn('[build] 未找到 content/courses 目录');
    fs.writeFileSync(indexPath, JSON.stringify(index, null, 2));
    return;
  }

  for (const id of fs.readdirSync(coursesDir)) {
    const metaPath = path.join(coursesDir, id, 'course.json');
    if (!fs.existsSync(metaPath)) continue;
    try {
      const meta = JSON.parse(fs.readFileSync(metaPath, 'utf8'));
      index.courses.push({ id, ...meta });
      // 同步复制该课程的全部内容到 public/courses/<id>
      copyRecursive(path.join(coursesDir, id), path.join(PUBLIC, 'courses', id));
    } catch (err) {
      console.error(`[build] 解析 ${metaPath} 失败:`, err.message);
    }
  }

  index.courses.sort((a, b) => (a.order || 999) - (b.order || 999));
  fs.writeFileSync(indexPath, JSON.stringify(index, null, 2));
  console.log(`[build] 已生成课程索引：${index.courses.length} 门课`);
}

function buildBadgeIndex() {
  // 生成徽章索引
  const badges = [
    { id: 'first-lesson', name: '迈出第一步', desc: '完成首个课时', icon: '🎯', xp: 10 },
    { id: 'first-quiz', name: '测验新星', desc: '完成一次单元测验', icon: '✏️', xp: 15 },
    { id: 'first-code', name: '代码小能手', desc: '通过一道代码练习', icon: '💻', xp: 20 },
    { id: 'streak-7', name: '七日连学', desc: '连续学习 7 天', icon: '🔥', xp: 50 },
    { id: 'streak-30', name: '月度学者', desc: '连续学习 30 天', icon: '🏆', xp: 200 },
    { id: 'analyst', name: '数据侦探', desc: '完成任意实战项目', icon: '🔍', xp: 80 },
    { id: 'pioneer', name: '实战先锋', desc: '完成 5 个实战项目', icon: '🚀', xp: 300 },
    { id: 'master', name: '全能分析师', desc: '完成全部 10 个实战项目', icon: '👑', xp: 800 },
    { id: 'course-basics', name: '基础工具通关', desc: '完成 Python 数据分析基础', icon: '📘', xp: 100 },
    { id: 'course-stats', name: '统计高手', desc: '完成商务统计课程', icon: '📊', xp: 120 },
    { id: 'course-feature', name: '数据清洗专家', desc: '完成特征工程课程', icon: '🧹', xp: 120 },
    { id: 'course-viz', name: '可视化达人', desc: '完成数据可视化进阶', icon: '🎨', xp: 120 },
    { id: 'proj-p1', name: '注册活跃分析师', desc: '完成项目 1', icon: '📈', xp: 80 },
    { id: 'proj-p2', name: '流失预警专家', desc: '完成项目 2', icon: '⚠️', xp: 80 },
    { id: 'proj-p3', name: 'RFM 分层达人', desc: '完成项目 3', icon: '🎯', xp: 80 },
    { id: 'proj-p4', name: '情感洞察师', desc: '完成项目 4', icon: '💬', xp: 80 },
    { id: 'proj-p5', name: '相关性分析师', desc: '完成项目 5', icon: '🔗', xp: 80 },
    { id: 'proj-p6', name: '转化漏斗专家', desc: '完成项目 6', icon: '⏳', xp: 80 },
    { id: 'proj-p7', name: '推荐规则挖掘师', desc: '完成项目 7', icon: '🧠', xp: 80 },
    { id: 'proj-p8', name: '流量预言家', desc: '完成项目 8', icon: '📡', xp: 80 },
    { id: 'proj-p9', name: '教师评分专家', desc: '完成项目 9', icon: '⭐', xp: 80 },
    { id: 'proj-p10', name: '用户画像设计师', desc: '完成项目 10', icon: '🧑‍🎓', xp: 80 }
  ];
  ensureDir(path.join(PUBLIC, 'meta'));
  fs.writeFileSync(path.join(PUBLIC, 'meta', 'badges.json'), JSON.stringify(badges, null, 2));
  console.log(`[build] 已生成徽章索引：${badges.length} 枚`);
}

function main() {
  ensureDir(PUBLIC);
  buildCourseIndex();
  buildBadgeIndex();
  // 复制 datasets
  copyRecursive(path.join(CONTENT, 'datasets'), path.join(PUBLIC, 'datasets'));
  // 复制根目录静态文件
  const staticFiles = ['index.html', 'course.html', 'lesson.html', 'achievement.html', '_headers', 'robots.txt'];
  for (const f of staticFiles) {
    const src = path.join(ROOT, f);
    if (fs.existsSync(src)) fs.copyFileSync(src, path.join(PUBLIC, f));
  }
  copyRecursive(path.join(ROOT, 'css'), path.join(PUBLIC, 'css'));
  copyRecursive(path.join(ROOT, 'js'), path.join(PUBLIC, 'js'));
  console.log('[build] 完成 ✅');
}

main();
