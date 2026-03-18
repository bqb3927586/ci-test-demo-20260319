# GitHub CI 测试 Demo

这个仓库是用来测试 `ci-cd-debugger` 技能的示例项目，包含故意设计的错误，用于验证CI失败分析能力。

## 包含的错误类型：

1. **语法错误**：`app.py` 第10行 `if b == 0` 缺少冒号，会触发 `SyntaxError`
2. **Lint错误**：
   - 未使用的 `requests` 导入（F401）
   - `multiply` 函数定义逗号后缺少空格（E231）
3. **测试失败**：`test_app.py` 第10行测试 `divide(10, 0)` 未捕获异常，会导致测试失败

## 使用方法：

1. 将此仓库推送到你的GitHub账号：
```bash
git add .
git commit -m "init: 测试CI错误"
git branch -M main
git remote add origin git@github.com:<你的用户名>/ci-test-demo.git
git push -u origin main
```

2. 推送后GitHub Actions会自动运行CI，并且会失败

3. 使用 `ci-cd-debugger` 技能分析失败的CI：
```bash
python /root/.openclaw/workspace/skills/ci-cd-debugger/scripts/ci_cd_debugger.py analyze <你的Actions失败URL>
```

4. 预期技能会正确识别出以上三类错误，并给出对应的修复建议。
