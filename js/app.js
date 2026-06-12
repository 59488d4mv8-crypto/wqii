/* ================================================================
   DA-Learn · 前端核心模块
   功能：1) 本地存储（学习档案） 2) 成就系统（XP/等级/徽章/连续天数）
         3) 课程内容加载（Markdown + JSON） 4) 主题切换
         5) 首页 / 课程页 / 课时页 / 成就页 的渲染
   ================================================================ */
(function () {
  'use strict';

  // ------------------------------------------------------------
  // 1) 存储层：profile 读 / 写
  // ------------------------------------------------------------
  const STORAGE_KEY = 'dalearn.profile.v1';

  function defaultProfile() {
    return {
      nickname: '同学',
      xp: 0,
      level: 1,
      streaks: { current: 0, max: 0, lastActiveDate: null },
      activeDates: {},           // { "YYYY-MM-DD": n }
      badges: {},                 // { badgeId: { earnedAt } }
      courses: {}                 // { courseId: { completedLessons: [...], quizScores: {...}, completed: bool } }
    };
  }

  function loadProfile() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return defaultProfile();
      const p = JSON.parse(raw);
      // 兼容老字段
      if (!p.nickname) p.nickname = '同学';
      if (!p.streaks) p.streaks = { current: 0, max: 0, lastActiveDate: null };
      if (!p.activeDates) p.activeDates = {};
      if (!p.badges) p.badges = {};
      if (!p.courses) p.courses = {};
      return p;
    } catch (e) {
      console.warn('profile 读取失败，使用默认', e);
      return defaultProfile();
    }
  }

  function saveProfile(p) {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(p)); }
    catch (e) { console.warn('保存失败', e); }
  }

  function resetProfile() {
    localStorage.removeItem(STORAGE_KEY);
    return loadProfile();
  }

  // ------------------------------------------------------------
  // 2) 成就系统
  // ------------------------------------------------------------
  // 等级阈值：每 100 XP 升一级
  function xpToLevel(xp) {
    return Math.floor(xp / 100) + 1;
  }
  function xpThisLevel(xp) { return xp % 100; }

  function todayKey() {
    const d = new Date();
    const y = d.getFullYear();
    const m = String(d.getMonth() + 1).padStart(2, '0');
    const day = String(d.getDate()).padStart(2, '0');
    return `${y}-${m}-${day}`;
  }

  function yesterdayKey() {
    const d = new Date(); d.setDate(d.getDate() - 1);
    const y = d.getFullYear();
    const m = String(d.getMonth() + 1).padStart(2, '0');
    const day = String(d.getDate()).padStart(2, '0');
    return `${y}-${m}-${day}`;
  }

  // 记录一次活跃（完成课时 / 练习 / 测验）
  function recordActive(profile) {
    const tk = todayKey();
    if (!profile.activeDates[tk]) profile.activeDates[tk] = 0;
    profile.activeDates[tk] += 1;

    if (profile.streaks.lastActiveDate !== tk) {
      if (profile.streaks.lastActiveDate === yesterdayKey()) {
        profile.streaks.current += 1;
      } else {
        profile.streaks.current = 1;
      }
      profile.streaks.lastActiveDate = tk;
      if (profile.streaks.current > profile.streaks.max) {
        profile.streaks.max = profile.streaks.current;
      }
    }
  }

  function addXp(profile, amount, reason) {
    if (!amount) return;
    profile.xp += amount;
    const newLv = xpToLevel(profile.xp);
    if (newLv !== profile.level) {
      profile.level = newLv;
    }
    if (reason) console.log(`[成就] +${amount} XP (${reason})`);
  }

  // 判定徽章（每次完成动作后调用）
  function checkBadges(profile) {
    const badges = profile.badges;
    const grant = (id) => {
      if (!badges[id]) {
        badges[id] = { earnedAt: Date.now() };
        console.log(`[徽章] 获得：${id}`);
        return true;
      }
      return false;
    };
    if (Object.keys(profile.activeDates).length >= 1) grant('first-lesson');
    if (profile.streaks.current >= 7) grant('streak-7');
    if (profile.streaks.max >= 30) grant('streak-30');
    return badges;
  }

  // ------------------------------------------------------------
  // 3) 工具：请求 Markdown / JSON / CSV 文本
  // ------------------------------------------------------------
  async function fetchText(url) {
    const r = await fetch(url);
    if (!r.ok) throw new Error(`无法加载 ${url}`);
    return await r.text();
  }
  async function fetchJSON(url) {
    const r = await fetch(url);
    if (!r.ok) throw new Error(`无法加载 JSON ${url}`);
    return await r.json();
  }

  // 根据构建/未构建环境动态选择资源基础路径
  function baseUrl() {
    // 若 URL 指向 public/ 下的页面或本地直接访问 root html 均返回 ./
    return '.';
  }

  // ------------------------------------------------------------
  // 4) 主题
  // ------------------------------------------------------------
  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('dalearn.theme', theme);
  }
  function initThemeToggle() {
    const saved = localStorage.getItem('dalearn.theme');
    const initial = saved || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    applyTheme(initial);
    const btn = document.getElementById('themeToggle');
    if (btn) btn.addEventListener('click', () => {
      const cur = document.documentElement.getAttribute('data-theme');
      applyTheme(cur === 'dark' ? 'light' : 'dark');
    });
  }

  // ------------------------------------------------------------
  // 5) 顶部用户 chip 更新
  // ------------------------------------------------------------
  function renderUserChip() {
    const p = loadProfile();
    const nameEl = document.getElementById('chipName');
    const xpEl = document.getElementById('chipXp');
    if (nameEl) nameEl.textContent = p.nickname || '同学';
    if (xpEl) xpEl.textContent = String(p.xp);
  }

  // ------------------------------------------------------------
  // 6) 首页渲染：加载课程索引 + 三个阶段
  // ------------------------------------------------------------
  async function initHome() {
    initThemeToggle();
    renderUserChip();
    try {
      const index = await fetchJSON(`${baseUrl()}/courses/index.json`);
      const courses = index.courses || [];
      const p = loadProfile();
      // 按 stage 分组
      const groups = { 1: [], 2: [], 3: [] };
      let totalLessons = 0;
      for (const c of courses) {
        groups[c.stage] = groups[c.stage] || [];
        groups[c.stage].push(c);
        totalLessons += (c.chapters || []).reduce((s, ch) => s + (ch.lessons || []).length, 0);
      }
      const grid1 = document.getElementById('courseGrid-1');
      const grid2 = document.getElementById('courseGrid-2');
      const grid3 = document.getElementById('courseGrid-3');
      if (grid1) grid1.innerHTML = groups[1].map(c => courseCardHtml(c, p)).join('');
      if (grid2) grid2.innerHTML = groups[2].map(c => courseCardHtml(c, p)).join('');
      if (grid3) grid3.innerHTML = groups[3].map(c => courseCardHtml(c, p)).join('');
      document.querySelectorAll('.course-card').forEach(el => {
        el.addEventListener('click', () => {
          const id = el.dataset.courseId;
          window.location.href = `course.html?id=${id}`;
        });
      });
      const statLessons = document.getElementById('statLessons');
      if (statLessons) statLessons.textContent = String(totalLessons);
    } catch (err) {
      console.error(err);
      document.body.insertAdjacentHTML('beforeend',
        `<div style="padding:30px;color:#ef4444;text-align:center">⚠ 课程索引加载失败（请先运行 <code>npm run build</code> 生成 public/）：${err.message}</div>`);
    }
  }

  function courseCardHtml(c, profile) {
    const prog = courseProgress(c, profile);
    const xpEst = estimateCourseXp(c);
    const typeMap = { 1: '基础课', 2: '方法课', 3: '实战项目' };
    const iconMap = {
      'course-python-basics': '🐍', 'course-stats': '📊', 'course-feature': '🧹',
      'course-viz': '🎨',
      'proj-p1': '📈', 'proj-p2': '⚠️', 'proj-p3': '🎯', 'proj-p4': '💬',
      'proj-p5': '🔗', 'proj-p6': '⏳', 'proj-p7': '🧠', 'proj-p8': '📡',
      'proj-p9': '⭐', 'proj-p10': '🧑‍🎓'
    };
    const icon = iconMap[c.id] || '📚';
    const pct = Math.round(prog.pct);
    return `
    <div class="course-card ${prog.done ? 'completed' : ''}" data-course-id="${c.id}">
      <div class="cc-head">
        <span class="cc-icon">${icon}</span>
        <span class="cc-badge">${typeMap[c.stage] || '课程'}</span>
      </div>
      <h3>${escapeHtml(c.title)}</h3>
      <p>${escapeHtml(c.description || '')}</p>
      <div class="cc-progress"><div class="cc-progress-fill" style="width:${pct}%"></div></div>
      <div class="cc-meta">
        <span>${prog.doneLessons}/${prog.totalLessons} 课时</span>
        <span>🪙 ${xpEst} XP</span>
      </div>
    </div>`;
  }

  function estimateCourseXp(c) {
    let total = 0;
    (c.chapters || []).forEach(ch => (ch.lessons || []).forEach(l => {
      if (l.type === 'read') total += 5;
      else if (l.type === 'code') total += (l.xp || 20);
      else if (l.type === 'quiz') total += 30;
      else if (l.type === 'exam') total += 80;
    }));
    return total;
  }

  function courseProgress(course, profile) {
    let total = 0, done = 0;
    const rec = profile.courses[course.id] || { completedLessons: [] };
    const lessonSet = new Set(rec.completedLessons);
    (course.chapters || []).forEach(ch => (ch.lessons || []).forEach(l => {
      total += 1;
      if (lessonSet.has(l.id)) done += 1;
    }));
    return { totalLessons: total, doneLessons: done, pct: total ? done / total * 100 : 0, done: total > 0 && done === total };
  }

  function escapeHtml(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, ch => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
    }[ch]));
  }

  // ------------------------------------------------------------
  // 7) 课程页渲染
  // ------------------------------------------------------------
  async function initCourse() {
    initThemeToggle();
    renderUserChip();
    const params = new URLSearchParams(location.search);
    const id = params.get('id');
    if (!id) { document.getElementById('courseLoading').textContent = '未指定课程 ID'; return; }

    try {
      const meta = await fetchJSON(`${baseUrl()}/courses/${id}/course.json`);
      document.getElementById('courseTitle').textContent = meta.title;
      document.getElementById('courseDesc').textContent = meta.description;
      document.getElementById('courseStage').textContent = ['', '阶段一 · 基础', '阶段二 · 方法', '阶段三 · 实战项目'][meta.stage] || '课程';
      const total = (meta.chapters || []).reduce((s, ch) => s + (ch.lessons || []).length, 0);
      document.getElementById('chapterCount').textContent = String((meta.chapters || []).length);
      document.getElementById('lessonCount').textContent = String(total);
      document.getElementById('courseXp').textContent = String(estimateCourseXp(meta));
      document.getElementById('backToCourse').href = `course.html?id=${id}`;

      const profile = loadProfile();
      const prog = courseProgress(meta, profile);
      document.getElementById('courseProgressPct').textContent = String(Math.round(prog.pct));
      document.getElementById('courseProgressBar').style.width = prog.pct + '%';

      const wrap = document.getElementById('chaptersWrap');
      wrap.innerHTML = (meta.chapters || []).map((ch, i) => chapterCardHtml(id, ch, i, profile)).join('');
      wrap.querySelectorAll('.chapter-head').forEach(el => {
        el.addEventListener('click', () => el.parentElement.classList.toggle('open'));
      });
      // 默认展开第一章
      const first = wrap.querySelector('.chapter-card');
      if (first) first.classList.add('open');

      document.getElementById('courseLoading').hidden = true;
      document.getElementById('courseWrap').hidden = false;
    } catch (err) {
      console.error(err);
      document.getElementById('courseLoading').textContent = '加载失败：' + err.message;
    }
  }

  function chapterCardHtml(courseId, ch, idx, profile) {
    const rec = profile.courses[courseId] || { completedLessons: [] };
    const set = new Set(rec.completedLessons);
    const typeIcons = { read: '📖', code: '💻', quiz: '✅', exam: '🏆' };
    const lessons = (ch.lessons || []).map(l => {
      const done = set.has(l.id);
      return `<li><a class="ll-left" href="lesson.html?course=${courseId}&ch=${idx}&lesson=${l.id}">
        <span class="ll-icon ${done ? 'll-done' : ''}">${done ? '✓' : typeIcons[l.type] || '•'}</span>
        <span>${escapeHtml(l.title)}</span>
        <span class="ll-type">${l.type}</span>
      </a><span class="ll-xp">${l.type === 'read' ? '+5' : '+' + (l.xp || (l.type === 'quiz' ? 30 : 20))} XP</span></li>`;
    }).join('');
    return `<div class="chapter-card">
      <div class="chapter-head"><h3>第 ${idx + 1} 章 · ${escapeHtml(ch.title)}</h3>
      <span class="ch-meta">${(ch.lessons || []).length} 课时</span></div>
      <div class="chapter-body"><ul class="lesson-list">${lessons}</ul></div>
    </div>`;
  }

  // ------------------------------------------------------------
  // 8) 课时页渲染
  // ------------------------------------------------------------
  async function initLesson() {
    initThemeToggle();
    renderUserChip();
    const params = new URLSearchParams(location.search);
    const courseId = params.get('course');
    const lessonId = params.get('lesson');
    const chIdx = Number(params.get('ch') || 0);
    if (!courseId || !lessonId) { document.getElementById('lessonLoading').textContent = '参数缺失'; return; }

    try {
      const meta = await fetchJSON(`${baseUrl()}/courses/${courseId}/course.json`);
      const chapters = meta.chapters || [];
      // 找课时
      let lesson = null, chapter = null, lessonIdx = -1;
      for (let ci = 0; ci < chapters.length; ci++) {
        const ls = chapters[ci].lessons || [];
        const idx = ls.findIndex(x => x.id === lessonId);
        if (idx >= 0) { chapter = chapters[ci]; lesson = ls[idx]; lessonIdx = idx; break; }
      }
      if (!lesson) { document.getElementById('lessonLoading').textContent = '未找到该课时'; return; }

      document.title = `${lesson.title} | DA-Learn`;
      document.getElementById('lessonBadge').textContent = `${meta.title} · ${chapter.title}`;
      document.getElementById('lessonTitle').textContent = lesson.title;
      document.getElementById('lessonMeta').textContent = `${lesson.type.toUpperCase()} · 最多 +${lesson.type === 'read' ? 5 : (lesson.xp || (lesson.type === 'quiz' ? 30 : 20))} XP`;
      document.getElementById('backToCourse').href = `course.html?id=${courseId}`;

      // 上一 / 下一课时（章节内 + 跨章节）
      const flat = [];
      chapters.forEach((ch, ci) => (ch.lessons || []).forEach((l, li) => flat.push({ courseId, ci, li, id: l.id })));
      const curPos = flat.findIndex(x => x.id === lessonId);
      const prev = curPos > 0 ? flat[curPos - 1] : null;
      const next = curPos < flat.length - 1 ? flat[curPos + 1] : null;
      document.getElementById('prevBtn').disabled = !prev;
      document.getElementById('prevBtn').onclick = () => { if (prev) location.href = `lesson.html?course=${courseId}&ch=${prev.ci}&lesson=${prev.id}`; };
      document.getElementById('nextBtn').disabled = !next;
      document.getElementById('nextBtn').onclick = () => { if (next) location.href = `lesson.html?course=${courseId}&ch=${next.ci}&lesson=${next.id}`; };

      // 内容
      const content = lesson.content ? await fetchText(`${baseUrl()}/courses/${courseId}/${lesson.content}`) : '';
      const contentEl = document.getElementById('lessonContent');
      if (window.marked) {
        contentEl.innerHTML = window.marked.parse(content || '_该课时暂无正文_');
      } else {
        contentEl.innerHTML = `<pre>${escapeHtml(content)}</pre>`;
      }
      if (window.hljs && contentEl.querySelectorAll) {
        contentEl.querySelectorAll('pre code').forEach(block => window.hljs.highlightElement(block));
      }

      // 代码练习 or 测验
      if (lesson.type === 'code') {
        document.getElementById('codeSection').hidden = false;
        setupCodeEditor(courseId, lesson);
      } else if (lesson.type === 'quiz' || lesson.type === 'exam') {
        document.getElementById('quizSection').hidden = false;
        setupQuiz(courseId, lesson);
      }

      document.getElementById('btnMarkDone').addEventListener('click', () => {
        markLessonDone(courseId, lessonId, lesson.type === 'read' ? 5 : 0, lesson.type === 'read' ? '阅读完成' : null);
        document.getElementById('btnMarkDone').textContent = '✓ 已完成（可关闭）';
        document.getElementById('btnMarkDone').disabled = true;
      });

      document.getElementById('lessonLoading').hidden = true;
      document.getElementById('lessonWrap').hidden = false;
    } catch (err) {
      console.error(err);
      document.getElementById('lessonLoading').textContent = '加载失败：' + err.message;
    }
  }

  // --- 代码编辑器 & Pyodide 封装 ---
  function setupCodeEditor(courseId, lesson) {
    const editor = document.getElementById('codeEditor');
    const output = document.getElementById('codeOutput').querySelector('code');
    const status = document.getElementById('pyodideStatus');
    const judgeEl = document.getElementById('judgeResult');

    // 加载模板
    fetchText(`${baseUrl()}/courses/${courseId}/${lesson.template || 'template.py'}`).then(t => { editor.value = t; }).catch(() => { editor.value = '# 在此编写 Python 代码\nprint("Hello, DA-Learn!")'; });
    const originalTemplate = () => fetchText(`${baseUrl()}/courses/${courseId}/${lesson.template || 'template.py'}`).catch(() => '');

    document.getElementById('btnReset').onclick = async () => {
      editor.value = await originalTemplate() || '# 在此编写 Python 代码';
      output.textContent = '';
      judgeEl.hidden = true;
    };

    // 运行
    document.getElementById('btnRun').onclick = async () => {
      output.textContent = '▶ 正在运行...';
      try {
        const result = await window.DAL_PY.runCode(editor.value);
        output.textContent = result.stdout + (result.error ? ('\n---ERROR---\n' + result.error) : '');
        // 若有 DataFrame / 图，插入 HTML
        if (result.html) { output.innerHTML = output.textContent + '\n' + result.html; }
        status.textContent = 'Pyodide 就绪 ✓';
      } catch (err) {
        output.textContent = '运行异常：' + err.message;
      }
    };

    // 提交判题
    document.getElementById('btnSubmit').onclick = async () => {
      output.textContent = '▶ 正在运行并判题...';
      let judgeScript = '';
      try { judgeScript = await fetchText(`${baseUrl()}/courses/${courseId}/${lesson.tests || 'tests.py'}`); }
      catch (e) { judgeScript = ''; }
      try {
        const result = await window.DAL_PY.judge(editor.value, judgeScript, lesson.judgeMode || 'solution');
        output.textContent = result.stdout + (result.error ? ('\n---ERROR---\n' + result.error) : '');
        judgeEl.hidden = false;
        if (result.passed) {
          judgeEl.className = 'judge-result ok';
          judgeEl.innerHTML = `✅ 判题通过！获得 +${lesson.xp || 20} XP <span class="small muted">（${new Date().toLocaleTimeString()}）</span>`;
          markLessonDone(courseId, lesson.id, lesson.xp || 20, '代码练习通过');
        } else {
          judgeEl.className = 'judge-result fail';
          judgeEl.innerHTML = `❌ 未通过：${escapeHtml(result.message || '断言失败，请检查你的解法。')}`;
        }
      } catch (err) {
        judgeEl.hidden = false;
        judgeEl.className = 'judge-result fail';
        judgeEl.textContent = '❌ 判题出错：' + err.message;
      }
    };
  }

  // --- 测验 ---
  function setupQuiz(courseId, lesson) {
    // 加载题目
    fetchJSON(`${baseUrl()}/courses/${courseId}/${lesson.questions || 'questions.json'}`).then(questions => {
      const wrap = document.getElementById('quizQuestions');
      wrap.innerHTML = questions.map((q, i) => renderQuestion(q, i)).join('');
      document.getElementById('btnQuizSubmit').onclick = () => {
        let correct = 0, total = questions.length;
        questions.forEach((q, i) => {
          const res = gradeQuestion(q, i);
          if (res.ok) correct += 1;
        });
        const score = Math.round(correct / total * 100);
        const resEl = document.getElementById('quizResult');
        resEl.hidden = false;
        resEl.className = 'quiz-result-box';
        const earned = score >= 60 ? (lesson.xp || (lesson.type === 'exam' ? 80 : 30)) : 0;
        resEl.innerHTML = `得分 ${score} / 100 · 答对 ${correct}/${total} 题${score >= 60 ? ` · 🪙 +${earned} XP` : ' · 未通过（<60 分）'}`;
        if (score >= 60) {
          markLessonDone(courseId, lesson.id, earned, '测验通过');
        } else {
          // 仍然记录一次活跃
          const p = loadProfile(); recordActive(p); saveProfile(p); renderUserChip();
        }
        document.getElementById('btnQuizSubmit').disabled = true;
      };
    }).catch(err => {
      document.getElementById('quizQuestions').innerHTML = `<p class="muted">题目加载失败：${escapeHtml(err.message)}</p>`;
    });
  }

  function renderQuestion(q, i) {
    const id = `q${i}`;
    if (q.type === 'single' || q.type === 'multi') {
      const opts = q.options.map((o, k) => `<label class="q-option"><input type="${q.type === 'multi' ? 'checkbox' : 'radio'}" name="${id}" value="${k}"/> ${escapeHtml(o)}</label>`).join('');
      return `<div class="q-question"><h4>Q${i + 1}. ${escapeHtml(q.question)}</h4>${opts}</div>`;
    }
    if (q.type === 'bool') {
      return `<div class="q-question"><h4>Q${i + 1}. ${escapeHtml(q.question)}</h4>
        <label class="q-option"><input type="radio" name="${id}" value="true"/> True</label>
        <label class="q-option"><input type="radio" name="${id}" value="false"/> False</label></div>`;
    }
    if (q.type === 'fill') {
      return `<div class="q-question"><h4>Q${i + 1}. ${escapeHtml(q.question)}</h4>
        <input class="q-fill-input" type="text" data-qidx="${i}" placeholder="输入答案..."/></div>`;
    }
    return '';
  }

  function gradeQuestion(q, i) {
    const id = `q${i}`;
    const wrap = document.getElementById('quizQuestions');
    let ok = false, userAnswer;
    if (q.type === 'single' || q.type === 'bool') {
      const sel = wrap.querySelector(`input[name="${id}"]:checked`);
      userAnswer = sel ? (q.type === 'bool' ? sel.value === 'true' : Number(sel.value)) : null;
      ok = userAnswer === q.answer;
    } else if (q.type === 'multi') {
      const sels = Array.from(wrap.querySelectorAll(`input[name="${id}"]:checked`)).map(x => Number(x.value));
      const ans = (Array.isArray(q.answer) ? q.answer : [q.answer]).sort();
      userAnswer = sels.slice().sort();
      ok = userAnswer.length === ans.length && userAnswer.every((v, k) => v === ans[k]);
    } else if (q.type === 'fill') {
      const input = wrap.querySelector(`input[data-qidx="${i}"]`);
      userAnswer = (input.value || '').trim();
      const expected = String(q.answer).trim();
      ok = userAnswer.toLowerCase() === expected.toLowerCase();
    }
    // 标记正确/错误（仅单选/多选/判断）
    if (q.type !== 'fill') {
      const opts = wrap.querySelectorAll(`input[name="${id}"]`);
      opts.forEach(o => {
        const val = q.type === 'bool' ? (o.value === 'true') : Number(o.value);
        const isAns = Array.isArray(q.answer) ? q.answer.includes(val) : val === q.answer;
        if (isAns) o.parentElement.classList.add('correct');
        if (o.checked && !isAns) o.parentElement.classList.add('wrong');
      });
    } else {
      const input = wrap.querySelector(`input[data-qidx="${i}"]`);
      input.style.borderColor = ok ? 'var(--success)' : 'var(--danger)';
    }
    return { ok };
  }

  // ------------------------------------------------------------
  // 9) 统一的"完成某课时"逻辑
  // ------------------------------------------------------------
  function markLessonDone(courseId, lessonId, xp, reason) {
    const p = loadProfile();
    if (!p.courses[courseId]) p.courses[courseId] = { completedLessons: [] };
    if (!p.courses[courseId].completedLessons.includes(lessonId)) {
      p.courses[courseId].completedLessons.push(lessonId);
    }
    recordActive(p);
    if (xp) addXp(p, xp, reason);
    checkBadges(p);
    saveProfile(p);
    renderUserChip();
  }

  // ------------------------------------------------------------
  // 10) 成就页渲染
  // ------------------------------------------------------------
  async function initAchievement() {
    initThemeToggle();
    let badges = [];
    try { badges = await fetchJSON(`${baseUrl()}/meta/badges.json`); }
    catch (e) { badges = []; }
    const p = loadProfile();

    // 昵称输入
    const nick = document.getElementById('nickname');
    if (nick) { nick.value = p.nickname; nick.addEventListener('input', () => { p.nickname = nick.value || '同学'; saveProfile(p); }); }
    document.getElementById('heroUser').textContent = p.nickname + '，你好！';
    document.getElementById('heroXp').textContent = String(p.xp);
    document.getElementById('heroLv').textContent = String(p.level);
    document.getElementById('heroBadges').textContent = String(Object.keys(p.badges).length);
    document.getElementById('heroStreak').textContent = String(p.streaks.current);
    document.getElementById('heroMaxStreak').textContent = String(p.streaks.max);

    // 等级环
    const ring = document.getElementById('levelRing');
    if (ring) {
      ring.textContent = 'Lv ' + p.level;
      const pct = xpThisLevel(p.xp);
      ring.style.background = `conic-gradient(var(--primary) ${pct}%, var(--border-soft) 0)`;
    }

    // 徽章墙
    const bg = document.getElementById('badgeGrid');
    if (bg) {
      bg.innerHTML = badges.map(b => {
        const earned = !!p.badges[b.id];
        return `<div class="badge-card ${earned ? '' : 'locked'}" title="${escapeHtml(b.desc)}">
          <div class="bc-icon">${b.icon}</div>
          <h4>${escapeHtml(b.name)}</h4>
          <p>${escapeHtml(b.desc)}</p>
          <span class="bc-xp">+${b.xp} XP</span>
        </div>`;
      }).join('');
    }

    // 热力图
    const heatmap = document.getElementById('heatmap');
    if (heatmap) {
      const cells = [];
      const today = new Date(); today.setHours(0, 0, 0, 0);
      for (let i = 179; i >= 0; i--) {
        const d = new Date(today); d.setDate(d.getDate() - i);
        const key = `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
        const n = p.activeDates[key] || 0;
        const lv = n === 0 ? '' : n === 1 ? 'l1' : n <= 3 ? 'l2' : n <= 6 ? 'l3' : 'l4';
        cells.push(`<div class="cell ${lv}" title="${key}: ${n} 次"></div>`);
      }
      heatmap.innerHTML = cells.join('');
    }

    // 课程进度
    const cp = document.getElementById('courseProgressList');
    if (cp) {
      try {
        const index = await fetchJSON(`${baseUrl()}/courses/index.json`);
        const rows = (index.courses || []).map(c => {
          const pr = courseProgress(c, p);
          const pct = Math.round(pr.pct);
          return `<div class="cp-row"><span class="cc-icon" style="font-size:22px">${(c.id && c.id.startsWith('proj')) ? '🎯' : '📘'}</span>
            <strong>${escapeHtml(c.title)}</strong>
            <div class="cp-bar"><div class="cp-fill" style="width:${pct}%"></div></div>
            <span class="cp-pct">${pct}%</span></div>`;
        }).join('');
        cp.innerHTML = rows || '<p class="muted">暂无课程数据</p>';
      } catch (e) {
        cp.innerHTML = '<p class="muted">课程索引未加载，请先运行 build 生成 public/</p>';
      }
    }

    // 导出 / 导入 / 清空
    document.getElementById('btnExport').onclick = () => {
      const data = JSON.stringify(loadProfile(), null, 2);
      const blob = new Blob([data], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url; a.download = `dalearn-profile-${todayKey()}.json`; a.click();
      URL.revokeObjectURL(url);
    };
    const fileInput = document.getElementById('importFile');
    if (fileInput) fileInput.addEventListener('change', async (e) => {
      const f = e.target.files[0]; if (!f) return;
      try {
        const text = await f.text();
        const data = JSON.parse(text);
        saveProfile(data);
        alert('导入成功，页面将刷新');
        location.reload();
      } catch (err) {
        alert('导入失败：' + err.message);
      }
    });
    document.getElementById('btnReset').onclick = () => {
      if (confirm('确认清空所有学习进度、XP、徽章？此操作不可恢复。')) {
        resetProfile(); location.reload();
      }
    };
  }

  // ------------------------------------------------------------
  // 暴露到 window.DAL
  // ------------------------------------------------------------
  window.DAL = {
    initHome, initCourse, initLesson, initAchievement,
    loadProfile, saveProfile, resetProfile,
    addXp, recordActive, checkBadges,
    markLessonDone,
  };
})();
