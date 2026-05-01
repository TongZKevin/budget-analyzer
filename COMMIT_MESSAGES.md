# Git Commit Messages (遵循 Conventional Commits 规范)

## 推荐的 Commit 序列

### 1. 初始项目结构
```
feat: initialize budget-analyzer project structure

- Add project directory layout
- Create src/, tests/, data/, output/ directories
- Add .gitignore for Python projects
- Add output directory placeholder
```

### 2. 核心功能实现
```
feat: implement budget analysis core functionality

- Add CSV reading with error handling
- Implement total spending calculation
- Add category-based spending breakdown
- Implement top category identification
- Add average spending calculation
- Include type hints and comprehensive docstrings
```

### 3. 测试代码
```
test: add comprehensive unit tests

- Add pytest test suite for budget analyzer
- Test CSV reading with valid and invalid data
- Test all calculation functions
- Add edge case tests (empty data, missing files)
- Achieve high test coverage
```

### 4. 示例数据
```
docs: add sample budget data

- Create sample_budget.csv with 15 transactions
- Include multiple categories (Food, Transportation, School, Entertainment)
- Provide realistic spending scenarios for testing
```

### 5. CI/CD 配置
```
ci: add GitHub Actions workflow

- Set up automated testing on push and PR
- Test against Python 3.8, 3.9, 3.10, 3.11
- Add pytest execution step
- Include CLI execution test
```

### 6. 文档
```
docs: create comprehensive README

- Add project overview and features
- Document installation and usage instructions
- Include CSV format specification
- Add testing guidelines
- Document AI collaboration approach
```

### 7. 依赖管理
```
build: add project dependencies

- Add requirements.txt with pytest
- Include optional matplotlib for charts
- Keep dependencies minimal for portability
```

## 或者使用单个 Commit（初始提交）

```
feat: initial commit - budget analyzer CLI tool

- Implement CSV-based budget analysis tool
- Add comprehensive test suite with pytest
- Configure GitHub Actions CI/CD
- Include sample data and documentation
- Document AI collaboration process

Core features:
- Read and parse CSV budget data
- Calculate total and category spending
- Identify top spending categories
- Generate optional visualization charts
- Handle invalid data gracefully

BREAKING CHANGE: Initial release
```

## Commit Message 类型说明

- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `test`: 测试相关
- `ci`: CI/CD 配置
- `build`: 构建系统或依赖更新
- `refactor`: 代码重构
- `perf`: 性能优化
- `style`: 代码格式调整
- `chore`: 其他杂项更新
