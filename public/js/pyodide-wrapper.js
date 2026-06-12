/* ================================================================
   DA-Learn · Pyodide 封装
   - 单例懒加载 Pyodide
   - runCode(code): 捕获 stdout/stderr，自动识别最后一行表达式的结果
   - judge(userCode, judgeScript): 两种模式
       * solution: 用户脚本里应暴露 solve() 等函数，判题脚本里调用断言
       * output: 对 stdout 进行关键字/正则匹配（可选）
   ================================================================ */
(function () {
  'use strict';

  let _pyodide = null;
  let _initPromise = null;

  async function ensurePyodide() {
    if (_pyodide) return _pyodide;
    if (_initPromise) return _initPromise;
    if (typeof window.loadPyodide !== 'function') {
      throw new Error('Pyodide 脚本未加载，请检查 <script src=".../pyodide.js">');
    }
    const status = document.getElementById('pyodideStatus');
    if (status) status.textContent = '⏳ 首次加载 Pyodide（约 5–15 秒）...';
    _initPromise = window.loadPyodide({
      indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.26.2/full/'
    }).then(async (py) => {
      _pyodide = py;
      // 预加载常见数据分析包（同步 API 在浏览器线程中阻塞即可）
      if (status) status.textContent = '⏳ 正在安装 numpy/pandas/matplotlib...';
      await py.loadPackage(['numpy', 'pandas', 'matplotlib']);
      // 把 matplotlib 后端设置为 AGG 并启用 SVG 收集
      await py.runPythonAsync(`
import io, sys, builtins
import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
_last_figures = []
__dal_stdout = io.StringIO()
`);
      if (status) status.textContent = '✓ Pyodide 就绪';
      return py;
    });
    return _initPromise;
  }

  async function runCode(code) {
    const py = await ensurePyodide();
    const output = { stdout: '', stderr: '', html: '', error: null, value: null };
    try {
      // 捕获 stdout
      await py.runPythonAsync(`
import sys, io
__dal_stdout = io.StringIO()
sys.stdout = __dal_stdout
sys.stderr = __dal_stdout
`);
      const result = await py.runPythonAsync(code);
      // 取回 stdout
      const stdout = py.runPython('__dal_stdout.getvalue()');
      output.stdout = stdout || '';
      // 获取 DataFrame / Figure
      if (result !== undefined && result !== null) {
        try {
          // 若结果是 DataFrame，转 HTML
          py.globals.set('__dal_result', result);
          const html = py.runPython(`
try:
    import pandas as pd
    if isinstance(__dal_result, (pd.DataFrame, pd.Series)):
        _html = __dal_result.to_html(classes="pyout-table", border=0, max_rows=30, max_cols=10)
    else:
        _html = None
except Exception:
    _html = None
_html
`);
          if (html) output.html = (output.html || '') + '\n' + html;
          // matplotlib 收集
          const figs = py.runPython(`
import matplotlib
_figs = [matplotlib.pyplot.figure(n) for n in matplotlib.pyplot.get_fignums()]
_svgs = []
try:
    for _f in _figs:
        _buf = __import__("io").BytesIO()
        _f.savefig(_buf, format="svg", bbox_inches="tight")
        _svgs.append(_buf.getvalue().decode("utf-8"))
finally:
    matplotlib.pyplot.close("all")
_svgs
`);
          if (figs && figs.length) {
            output.html = (output.html || '') + '\n' + figs.join('\n');
          }
        } catch (e) { /* 忽略后处理异常 */ }
      }
    } catch (err) {
      output.error = err.message || String(err);
    } finally {
      // 恢复 stdout
      try { await py.runPythonAsync('sys.stdout = sys.__stdout__\nsys.stderr = sys.__stderr__'); } catch (_) {}
    }
    return output;
  }

  // 判题逻辑
  // mode = "solution": 在同一 globals 环境下先执行用户代码，再执行 judge 脚本
  // 如果 judge 脚本包含 `assert`，任何失败会被捕获作为 passed=false
  async function judge(userCode, judgeScript, mode) {
    const py = await ensurePyodide();
    const result = { stdout: '', error: null, message: '', passed: false };
    try {
      await py.runPythonAsync(`
import sys, io, traceback
__dal_stdout = io.StringIO()
sys.stdout = __dal_stdout
sys.stderr = __dal_stdout
`);
      // 1) 跑用户代码
      try {
        await py.runPythonAsync(userCode);
      } catch (err) {
        result.stdout = py.runPython('__dal_stdout.getvalue()') || '';
        result.error = err.message;
        result.message = '用户代码运行出错：' + (err.message || '');
        return result;
      }
      result.stdout = (py.runPython('__dal_stdout.getvalue()') || '') + '\n';
      // 2) 跑判题脚本（如有）
      if (judgeScript && judgeScript.trim()) {
        try {
          await py.runPythonAsync(judgeScript);
          result.passed = true;
          result.message = '全部断言通过 ✓';
        } catch (err) {
          result.passed = false;
          // 从 traceback 提取最后一行消息
          const msg = (err.message || '').split('\n').filter(Boolean).pop() || '断言失败';
          result.message = msg;
        }
      } else {
        // 无判题脚本：只要用户代码无异常即通过
        result.passed = true;
        result.message = '代码成功运行 ✓';
      }
    } catch (err) {
      result.error = err.message;
      result.message = '判题环境异常：' + err.message;
    } finally {
      try { await py.runPythonAsync('sys.stdout = sys.__stdout__\nsys.stderr = sys.__stderr__'); } catch (_) {}
    }
    return result;
  }

  window.DAL_PY = { ensurePyodide, runCode, judge };
})();
