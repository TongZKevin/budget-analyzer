# GitHub 部署指南

## 步骤 1：初始化 Git 仓库

在项目目录运行：

```powershell
cd C:\Users\tongz\budget-analyzer

# 初始化 Git
git init

# 添加所有文件
git add .

# 查看将要提交的文件
git status

# 第一次提交（使用 Conventional Commits 格式）
git commit -m "feat: initial commit - budget analyzer CLI tool

- Implement CSV-based budget analysis tool
- Add comprehensive test suite with pytest
- Configure GitHub Actions CI/CD pipeline
- Include AI collaboration documentation
- Add presentation materials and reflection

Core features:
- Read and parse CSV budget data
- Calculate total and category spending
- Identify top spending categories
- Generate formatted terminal reports
- Handle invalid data gracefully

Testing:
- 14 unit tests covering main functionality
- Edge case handling (empty data, invalid amounts)
- CI pipeline on Python 3.8, 3.9, 3.10, 3.11

Documentation:
- Comprehensive README with examples
- AI collaboration narrative with prompts
- Presentation script (10 minutes)
- Project reflection (1800+ words)

BREAKING CHANGE: Initial release"
```

## 步骤 2：在 GitHub 创建仓库

1. 访问 https://github.com/new
2. **Repository name:** `budget-analyzer`
3. **Description:** "A simple CLI tool for analyzing personal spending from CSV files. Built with AI collaboration for SYSEN 5493."
4. **Visibility:** Public （这样教授可以查看）
5. **不要** 勾选 "Initialize this repository with a README" （我们已经有了）
6. 点击 **Create repository**

## 步骤 3：连接本地仓库到 GitHub

GitHub 会显示命令，但这里是完整步骤：

```powershell
# 添加远程仓库（替换 YOUR_USERNAME）
git remote add origin https://github.com/YOUR_USERNAME/budget-analyzer.git

# 设置主分支名称
git branch -M main

# 推送到 GitHub
git push -u origin main
```

## 步骤 4：验证 CI/CD 运行

1. 访问你的 GitHub 仓库页面
2. 点击 **Actions** 标签
3. 你应该看到 CI 工作流正在运行
4. 等待它变成绿色 ✅

## 步骤 5：添加 CI 徽章到 README

编辑 README.md，在顶部添加：

```markdown
# Budget Analyzer

![CI](https://github.com/YOUR_USERNAME/budget-analyzer/workflows/CI/badge.svg)

[其余内容保持不变]
```

提交更新：

```powershell
git add README.md
git commit -m "docs: add CI badge to README"
git push
```

## 步骤 6：创建演示视频（可选但推荐）

### 选项 A：录屏工具
- **Windows:** 使用内置的 Xbox Game Bar (Win + G)
- **OBS Studio:** 免费专业录屏工具
- **Loom:** 在线录屏，自动上传

### 录制内容（2-3分钟）
1. **开场** (10秒)
   - "Hi, this is my budget analyzer demo"
   
2. **显示 CSV 文件** (20秒)
   ```powershell
   cat data/sample_budget.csv
   ```
   
3. **运行程序** (30秒)
   ```powershell
   python src/budget_analyzer.py data/sample_budget.csv
   ```
   解释输出
   
4. **演示错误处理** (30秒)
   创建错误数据并展示工具如何处理
   
5. **运行测试** (30秒)
   ```powershell
   pytest -v
   ```
   
6. **结尾** (10秒)
   - "All tests pass, CI is green, code is on GitHub"

### 上传视频
- YouTube (unlisted link)
- Google Drive
- 或直接提交 MP4 文件

## 步骤 7：准备最终提交材料

### 在 Canvas 提交时包含：

1. **GitHub 仓库链接**
   ```
   https://github.com/YOUR_USERNAME/budget-analyzer
   ```

2. **演示视频链接** （如果录制了）
   ```
   https://youtu.be/YOUR_VIDEO_ID
   或
   https://drive.google.com/file/d/YOUR_FILE_ID
   ```

3. **关键文档清单**
   - ✅ README.md - 项目说明
   - ✅ AI_COLLABORATION.md - AI 协作文档
   - ✅ PRESENTATION_SCRIPT.md - 演示稿
   - ✅ REFLECTION.md - 反思文档
   - ✅ .github/workflows/ci.yml - CI 配置
   - ✅ src/budget_analyzer.py - 核心代码
   - ✅ tests/test_budget_analyzer.py - 测试代码

## 检查清单

提交前确保：

- [ ] 所有代码已推送到 GitHub
- [ ] CI pipeline 显示绿色 ✅
- [ ] README 包含 CI 徽章
- [ ] AI_COLLABORATION.md 完整记录了 prompts 和决策
- [ ] REFLECTION.md 回答了全部 4 个问题（150+ 字）
- [ ] PRESENTATION_SCRIPT.md 准备好了 10 分钟演讲稿
- [ ] 测试通过：`pytest` 显示 14 passed
- [ ] 程序能运行：`python src/budget_analyzer.py data/sample_budget.csv`
- [ ] Git commit 历史干净（使用 Conventional Commits）
- [ ] 仓库是 Public 的（教授可访问）
- [ ] （可选）演示视频已录制并上传

## 常见问题

### Q: Git 显示中文文件名乱码？
```powershell
git config --global core.quotepath false
```

### Q: 推送时需要用户名密码？
使用 Personal Access Token（不是密码）：
1. GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. 勾选 `repo` 权限
4. 复制 token
5. 推送时输入 token 作为密码

### Q: CI 失败怎么办？
1. 点击失败的工作流查看错误
2. 通常是测试失败或依赖问题
3. 修复后重新推送会自动重跑

### Q: 如何更新已推送的代码？
```powershell
# 修改代码
# ...

# 提交
git add .
git commit -m "fix: correct calculation error in average spending"
git push
```

## 演示建议

### 如果现场演示：
1. 提前测试所有命令
2. 准备备用视频
3. 增大终端字体（18-20pt）
4. 使用清晰的示例数据

### 如果录制演示：
1. 使用高清分辨率（1920x1080）
2. 清晰的音频
3. 剪辑掉长时间等待
4. 添加字幕（可选但推荐）

## 时间规划

- **现在 - 提交前：** 
  - 30 分钟：推送到 GitHub，验证 CI
  - 1 小时：录制演示视频（如果需要）
  - 30 分钟：准备演讲稿

- **演示日：**
  - 提前 10 分钟到达
  - 测试演示环境
  - 深呼吸 😊

## 最终提交格式（Canvas）

```
SYSEN 5493 Final Project Submission

Student Name: [Your Name]
Project: Budget Analyzer

GitHub Repository: https://github.com/YOUR_USERNAME/budget-analyzer
Demo Video: [link if recorded]

Key Deliverables:
✅ Working code with 14 passing tests
✅ GitHub Actions CI/CD pipeline (green badge)
✅ AI collaboration documentation
✅ Reflection (1847 words)
✅ Presentation materials

Conventional Commits: Yes
Clone-and-run ready: Yes
Tests pass locally: Yes
CI passes on GitHub: Yes

Thank you!
```

---

**你现在准备好了！🎉**

下一步：
1. 在 GitHub 创建仓库
2. 运行上面的 git 命令
3. 验证 CI 通过
4. （可选）录制演示视频
5. 在 Canvas 提交

有问题随时问我！
