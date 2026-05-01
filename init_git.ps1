# 快速部署脚本
# 运行此脚本初始化 Git 并准备推送到 GitHub

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Budget Analyzer - Git 初始化脚本" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# 检查是否在正确的目录
$currentDir = Get-Location
if ($currentDir.Path -ne "C:\Users\tongz\budget-analyzer") {
    Write-Host "错误：请先切换到项目目录" -ForegroundColor Red
    Write-Host "运行：cd C:\Users\tongz\budget-analyzer" -ForegroundColor Yellow
    exit 1
}

# 步骤 1: 初始化 Git
Write-Host "[1/6] 初始化 Git 仓库..." -ForegroundColor Green
if (Test-Path .git) {
    Write-Host "Git 仓库已存在，跳过初始化" -ForegroundColor Yellow
} else {
    git init
    Write-Host "✓ Git 仓库初始化完成" -ForegroundColor Green
}

# 步骤 2: 添加所有文件
Write-Host "`n[2/6] 添加所有文件到 Git..." -ForegroundColor Green
git add .
Write-Host "✓ 文件添加完成" -ForegroundColor Green

# 显示将要提交的文件
Write-Host "`n将要提交的文件：" -ForegroundColor Cyan
git status --short

# 步骤 3: 创建初始提交
Write-Host "`n[3/6] 创建初始提交..." -ForegroundColor Green
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

Write-Host "✓ 初始提交完成" -ForegroundColor Green

# 步骤 4: 设置主分支
Write-Host "`n[4/6] 设置主分支名称为 'main'..." -ForegroundColor Green
git branch -M main
Write-Host "✓ 分支设置完成" -ForegroundColor Green

# 步骤 5: 显示 Git 日志
Write-Host "`n[5/6] Git 提交历史：" -ForegroundColor Cyan
git log --oneline --graph --all

# 步骤 6: 准备推送到 GitHub
Write-Host "`n[6/6] 准备推送到 GitHub" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Cyan

Write-Host "下一步操作：" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. 在 GitHub 创建新仓库：" -ForegroundColor White
Write-Host "   访问：https://github.com/new" -ForegroundColor Cyan
Write-Host "   仓库名：budget-analyzer" -ForegroundColor Cyan
Write-Host "   设为 Public" -ForegroundColor Cyan
Write-Host "   不要勾选 'Initialize with README'" -ForegroundColor Cyan
Write-Host ""
Write-Host "2. 创建后，运行以下命令（替换 YOUR_USERNAME）：" -ForegroundColor White
Write-Host ""
Write-Host "   git remote add origin https://github.com/YOUR_USERNAME/budget-analyzer.git" -ForegroundColor Green
Write-Host "   git push -u origin main" -ForegroundColor Green
Write-Host ""
Write-Host "3. 验证 CI/CD：" -ForegroundColor White
Write-Host "   访问：https://github.com/YOUR_USERNAME/budget-analyzer/actions" -ForegroundColor Cyan
Write-Host "   确保 CI 显示绿色 ✓" -ForegroundColor Cyan
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "所有本地准备工作完成！ ✓" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
