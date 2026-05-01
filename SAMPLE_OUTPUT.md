# 示例输出

## 命令行运行示例

```bash
$ python src/budget_analyzer.py data/sample_budget.csv
```

## 控制台输出

```
Reading budget data from: data/sample_budget.csv
Successfully loaded 15 valid records

============================================================
BUDGET ANALYSIS REPORT
============================================================

Total Transactions: 15
Total Spending: $307.89
Average per Transaction: $20.53

------------------------------------------------------------
SPENDING BY CATEGORY
------------------------------------------------------------
Food                 $  131.65  ( 42.8%)
Entertainment        $   69.50  ( 22.6%)
Transportation       $   56.25  ( 18.3%)
School               $   50.49  ( 16.4%)

------------------------------------------------------------
HIGHEST SPENDING CATEGORY: Food ($131.65)
============================================================

Note: matplotlib not installed. Skipping chart generation.
Install with: pip install matplotlib
```

## 如果安装了 matplotlib

```
Reading budget data from: data/sample_budget.csv
Successfully loaded 15 valid records

============================================================
BUDGET ANALYSIS REPORT
============================================================

Total Transactions: 15
Total Spending: $307.89
Average per Transaction: $20.53

------------------------------------------------------------
SPENDING BY CATEGORY
------------------------------------------------------------
Food                 $  131.65  ( 42.8%)
Entertainment        $   69.50  ( 22.6%)
Transportation       $   56.25  ( 18.3%)
School               $   50.49  ( 16.4%)

------------------------------------------------------------
HIGHEST SPENDING CATEGORY: Food ($131.65)
============================================================

Chart saved to: output/category_spending.png
```

## 处理无效数据的示例

假设 CSV 文件包含一些错误：

```csv
date,category,description,amount
2026-04-01,Food,Lunch,12.50
2026-04-02,Transportation,Bus,invalid
2026-04-03,School,Book,
2026-04-04,Food,Dinner,18.20
```

输出：
```
Reading budget data from: data/sample_budget.csv
Warning: Line 3 has invalid amount 'invalid', skipping
Warning: Line 4 has invalid amount '', skipping
Successfully loaded 2 valid records

============================================================
BUDGET ANALYSIS REPORT
============================================================

Total Transactions: 2
Total Spending: $30.70
Average per Transaction: $15.35

------------------------------------------------------------
SPENDING BY CATEGORY
------------------------------------------------------------
Food                 $   30.70  (100.0%)

------------------------------------------------------------
HIGHEST SPENDING CATEGORY: Food ($30.70)
============================================================
```

## 空数据处理示例

```
Reading budget data from: data/empty.csv
Successfully loaded 0 valid records

============================================================
BUDGET ANALYSIS REPORT
============================================================

No valid data to analyze.
============================================================
```

## pytest 测试运行示例

```bash
$ pytest -v
```

输出：
```
======================== test session starts ========================
platform win32 -- Python 3.11.0, pytest-7.4.0, pluggy-1.0.0
cachedir: .pytest_cache
rootdir: C:\Users\tongz\budget-analyzer
collected 14 items

tests/test_budget_analyzer.py::test_read_valid_csv PASSED        [  7%]
tests/test_budget_analyzer.py::test_read_csv_with_invalid_data PASSED [ 14%]
tests/test_budget_analyzer.py::test_read_csv_file_not_found PASSED [ 21%]
tests/test_budget_analyzer.py::test_read_empty_csv PASSED        [ 28%]
tests/test_budget_analyzer.py::test_calculate_total_spending PASSED [ 35%]
tests/test_budget_analyzer.py::test_calculate_total_spending_empty PASSED [ 42%]
tests/test_budget_analyzer.py::test_calculate_category_spending PASSED [ 50%]
tests/test_budget_analyzer.py::test_calculate_category_spending_empty PASSED [ 57%]
tests/test_budget_analyzer.py::test_find_top_category PASSED     [ 64%]
tests/test_budget_analyzer.py::test_find_top_category_empty PASSED [ 71%]
tests/test_budget_analyzer.py::test_calculate_average_spending PASSED [ 78%]
tests/test_budget_analyzer.py::test_calculate_average_spending_empty PASSED [ 85%]
tests/test_budget_analyzer.py::test_csv_with_whitespace PASSED   [ 92%]
tests/test_budget_analyzer.py::test_multiple_categories_same_amount PASSED [100%]

======================== 14 passed in 0.12s ========================
```

## 文件帮助信息

```bash
$ python src/budget_analyzer.py
```

输出：
```
Usage: python budget_analyzer.py <path_to_csv_file>
Example: python budget_analyzer.py data/sample_budget.csv
```
