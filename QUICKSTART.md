# 快速开始指南

## 5 分钟快速上手

### 1️⃣ 进入项目目录
```bash
cd C:\Users\tongz\budget-analyzer
```

### 2️⃣ 安装依赖
```bash
pip install -r requirements.txt
```

### 3️⃣ 运行示例
```bash
python src/budget_analyzer.py data/sample_budget.csv
```

### 4️⃣ 运行测试
```bash
pytest
```

## 使用自己的数据

### 创建你的 CSV 文件

创建一个新文件 `my_budget.csv`：

```csv
date,category,description,amount
2026-04-01,Food,Lunch,12.50
2026-04-02,Transportation,Bus,2.75
2026-04-03,Shopping,Clothes,45.00
```

### 运行分析

```bash
python src/budget_analyzer.py my_budget.csv
```

## 可选：生成图表

安装 matplotlib：
```bash
pip install matplotlib
```

再次运行分析，会自动生成图表到 `output/category_spending.png`

## 下一步

- 查看 [README.md](README.md) 了解完整功能
- 查看 [SAMPLE_OUTPUT.md](SAMPLE_OUTPUT.md) 查看示例输出
- 查看 [COMMIT_MESSAGES.md](COMMIT_MESSAGES.md) 了解推荐的 git 提交信息

## 常见问题

**Q: 如何创建虚拟环境？**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

**Q: CSV 文件格式错误怎么办？**
程序会自动跳过格式错误的行，并在控制台显示警告信息。

**Q: 如何贡献代码？**
1. 修改代码
2. 运行测试确保通过：`pytest`
3. 提交代码

**Q: 如何部署到 GitHub？**
```bash
git init
git add .
git commit -m "feat: initial commit - budget analyzer CLI tool"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

## 项目特点

✅ 零配置 - 开箱即用  
✅ 轻量级 - 最小依赖  
✅ 容错性强 - 自动跳过错误数据  
✅ 完整测试 - 14 个单元测试  
✅ CI/CD - GitHub Actions 自动化测试  
