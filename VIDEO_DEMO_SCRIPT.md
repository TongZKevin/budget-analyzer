# 演示视频脚本（2-3 分钟版本）

如果你要录制备用演示视频，按照这个简短脚本：

---

## 🎬 开场（10秒）

**镜头：** 你的脸 / 或直接屏幕录制

**说：**
> "Hi, this is my budget analyzer demo for SYSEN 5493. It's a command-line tool that analyzes personal spending from CSV files. Let me show you how it works."

---

## 📄 展示数据（20秒）

**镜头：** 终端，切换到项目目录

**运行：**
```powershell
cd C:\Users\tongz\budget-analyzer
Get-Content data\sample_budget.csv | Select-Object -First 5
```

**说：**
> "Here's the input - a simple CSV file with date, category, description, and amount. Anyone can create this in Excel."

**显示：**
```
date,category,description,amount
2026-04-01,Food,Lunch at cafe,12.50
2026-04-02,Transportation,Bus ticket,2.75
...
```

---

## 🚀 运行程序（30秒）

**运行：**
```powershell
python src/budget_analyzer.py data/sample_budget.csv
```

**说（当输出显示时）：**
> "The tool reads the CSV, calculates totals, groups by category, and prints a formatted report.
>
> We can see:
> - Total spending: $307.89 across 15 transactions
> - Food is the top category at $131
> - Average transaction is about $20
>
> Clear, actionable insights in seconds."

---

## ⚠️ 展示错误处理（30秒）

**创建错误文件：**
```powershell
@"
date,category,description,amount
2026-05-01,Food,Lunch,not_a_number
2026-05-01,Food,Valid,12.50
"@ | Out-File -FilePath bad_data.csv
```

**运行：**
```powershell
python src/budget_analyzer.py bad_data.csv
```

**说：**
> "Important: it handles bad data gracefully. See the warning about the invalid amount? But it doesn't crash - it skips the bad row and processes the good ones. Real-world data is messy; this tool adapts."

---

## ✅ 运行测试（30秒）

**运行：**
```powershell
pytest -v
```

**说（当测试运行时）：**
> "The project has 14 unit tests covering:
> - Valid data scenarios
> - Invalid data handling
> - Edge cases like empty files and whitespace
>
> All tests pass. This gives me confidence the code works correctly."

---

## 🤖 AI 协作简述（20秒）

**镜头：** 打开 `AI_COLLABORATION.md` 快速滚动

**说：**
> "This was built with AI assistance. The AI generated the code scaffold and tests, but I made all final decisions.
>
> I accepted: The function structure and error handling
> I rejected: Database integration and web UI - kept it simple
>
> AI wrote code fast; I ensured it matched requirements."

---

## 🎯 结尾（10秒）

**镜头：** GitHub 页面（如果已推送）或终端

**说：**
> "The code is on GitHub with passing CI tests. It's simple, portable, and works. Thanks for watching!"

**显示：**
- GitHub repo URL (如果有)
- 或者 `git log --oneline` 显示 commit

---

## 📹 录制技巧

### 准备
1. **关闭通知** - 防止干扰
2. **清理桌面** - 看起来专业
3. **增大字体** - 终端用 18pt+
4. **测试音频** - 清晰无噪音
5. **准备脚本** - 但不要照读，自然一些

### 录制设置
- **分辨率:** 1920x1080
- **帧率:** 30 fps
- **音频:** 清晰，无回音
- **时长:** 2-3 分钟（不超过 3.5 分钟）

### 录制工具

**Windows 内置：Xbox Game Bar**
```
按 Win + G
点击"录制"按钮
完成后 Win + Alt + R 停止
```

**OBS Studio（推荐）**
- 免费，专业级
- 可以添加摄像头画面
- 可以高亮鼠标
- 下载：https://obsproject.com

**Loom（最简单）**
- 浏览器扩展
- 自动上传
- 可以同时录制摄像头
- 免费版最长 5 分钟

### 后期

如果需要剪辑：
- **剪掉长时间等待**（如 pip install）
- **加快某些部分**（如测试运行）
- **添加字幕**（可选但好）
- **检查音频清晰度**

### 上传

**YouTube（推荐）**
1. 上传为 "Unlisted"（不要 Private，教授看不到）
2. 标题：`Budget Analyzer - SYSEN 5493 Final Project Demo`
3. 描述：项目描述 + GitHub 链接
4. 复制链接提交到 Canvas

**Google Drive**
1. 上传 MP4
2. 设置为"任何有链接的人都可以查看"
3. 复制分享链接

**OneDrive**
1. 上传视频
2. 创建分享链接
3. 确保权限设置正确

---

## 🎭 演示时不要做的事

❌ **不要：**
- 道歉（"这可能不工作..."）
- 解释太多技术细节
- 卡在错误上太久
- 超时（保持在 3 分钟内）
- 读屏幕上的文字

✅ **要：**
- 自信
- 简洁
- 展示，不要只说
- 预期问题，准备答案
- 保持节奏

---

## 🔧 故障排除

### 如果录制失败
- 重录！前几次总是不完美
- 可以分段录制后拼接
- 不需要完美，需要清晰

### 如果程序出错
- 提前测试 5 遍
- 准备 Plan B（展示截图）
- 坦然面对："This shows why testing matters"

### 如果时间太长
- 剪掉开场的"um"和"uh"
- 加快测试运行部分
- 只展示核心功能

---

## ✨ 专业技巧

1. **写提词器脚本** - 但要自然说话
2. **练习 3 遍** - 第 3 遍最流畅
3. **微笑** - 即使只是录屏，态度会传达
4. **慢一点** - 比你想的慢 20%
5. **暂停** - 给观众消化时间

---

## 📊 示例时间分配（3 分钟版）

- 0:00-0:10 开场
- 0:10-0:30 展示 CSV
- 0:30-1:00 运行程序
- 1:00-1:30 错误处理
- 1:30-2:00 运行测试
- 2:00-2:20 AI 协作
- 2:20-2:30 结尾

**总时长：2.5 分钟** ✓

---

**记住：** 这是备用视频。如果现场演示顺利，你可能不需要播放它。但有备无患！

**Good luck! 🎬**
