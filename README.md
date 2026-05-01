# Budget Analyzer

![CI](https://github.com/YOUR_USERNAME/budget-analyzer/workflows/CI/badge.svg)

A simple command-line tool for analyzing personal spending data from CSV files. This tool reads budget/expense data and generates comprehensive analysis reports including total spending, category breakdowns, and spending statistics.

> **Note:** Replace `YOUR_USERNAME` in the CI badge URL above with your actual GitHub username after creating the repository.

## Features

- 📊 Read and parse CSV-formatted budget data
- 🔍 Automatically skip and report invalid data rows
- 💰 Calculate total spending across all transactions
- 📈 Break down spending by category
- 🎯 Identify the highest spending category
- 📉 Calculate average spending per transaction
- 📊 (Optional) Generate visual bar charts of category spending
- ✅ Comprehensive test coverage with pytest
- 🔄 Continuous Integration with GitHub Actions

## Project Structure

```
budget-analyzer/
├── README.md
├── requirements.txt
├── src/
│   └── budget_analyzer.py    # Main application code
├── tests/
│   └── test_budget_analyzer.py  # Unit tests
├── data/
│   └── sample_budget.csv     # Sample data file
├── output/                   # Generated charts (created at runtime)
└── .github/
    └── workflows/
        └── ci.yml            # GitHub Actions CI configuration
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone or download this repository:
   ```bash
   git clone <repository-url>
   cd budget-analyzer
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Analyzer

Basic usage:
```bash
python src/budget_analyzer.py data/sample_budget.csv
```

With your own CSV file:
```bash
python src/budget_analyzer.py path/to/your/budget.csv
```

### CSV File Format

Your CSV file should have the following columns:
- `date`: Transaction date (e.g., 2026-04-01)
- `category`: Spending category (e.g., Food, Transportation)
- `description`: Transaction description
- `amount`: Amount spent (numeric value)

Example:
```csv
date,category,description,amount
2026-04-01,Food,Lunch,12.50
2026-04-02,Transportation,Bus ticket,2.75
2026-04-03,School,Notebook,5.99
```

### Sample Output

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
Transportation       $   56.25  ( 18.3%)
Entertainment        $   69.50  ( 22.6%)
School               $   50.49  ( 16.4%)

------------------------------------------------------------
HIGHEST SPENDING CATEGORY: Food ($131.65)
============================================================

Chart saved to: output/category_spending.png
```

## Running Tests

Run all tests with pytest:
```bash
pytest
```

Run tests with verbose output:
```bash
pytest -v
```

Run tests with coverage report:
```bash
pytest --cov=src tests/
```

### Test Coverage

The test suite covers:
- ✅ Reading valid CSV files
- ✅ Handling and skipping invalid data rows
- ✅ Calculating total spending
- ✅ Calculating category-wise spending
- ✅ Finding the top spending category
- ✅ Calculating average spending
- ✅ Edge cases (empty data, missing files, whitespace handling)

## Continuous Integration

This project uses GitHub Actions for automated testing. The CI pipeline:

1. Runs on every `push` and `pull_request`
2. Tests against Python 3.8, 3.9, 3.10, and 3.11
3. Automatically installs dependencies
4. Runs the full pytest test suite
5. Reports test results

See `.github/workflows/ci.yml` for the complete configuration.

## AI Collaboration

This project was developed with AI assistance. Here's how AI contributed:

### AI Contributions
- 🤖 Generated initial project structure and boilerplate code
- 🧪 Wrote comprehensive unit tests covering core functionality
- ⚙️ Created GitHub Actions CI/CD configuration
- 📝 Assisted with documentation and code comments
- 🎨 Suggested matplotlib integration for visualization

### Human Contributions
- 👨‍💻 Reviewed and validated all logic and algorithms
- 🔍 Tested the tool with real-world data scenarios
- 🚫 Rejected AI's suggestion to add database integration (kept it simple)
- ✨ Refined error handling and edge case management
- 📋 Made final decisions on feature scope and requirements

### Collaboration Approach
This project demonstrates effective human-AI collaboration:
- AI provided rapid prototyping and boilerplate generation
- Human maintained control over architecture decisions
- Together, achieved a balance between functionality and simplicity
- AI helped maintain code quality standards (type hints, docstrings)
- Human ensured the tool remained lightweight and dependency-minimal

## Design Decisions

- **No database**: Kept simple with CSV input/output for easy portability
- **Minimal dependencies**: Only pytest (testing) and matplotlib (optional charts)
- **Type hints**: Used throughout for better code documentation
- **Error tolerance**: Invalid data rows are skipped with warnings, not failures
- **Standalone**: Can run in any Python 3 environment without configuration

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes with tests
4. Ensure all tests pass (`pytest`)
5. Submit a pull request

## License

This project is provided as-is for educational purposes.

## Future Enhancements

Potential features for future versions:
- Support for multiple input file formats (JSON, Excel)
- Date range filtering
- Monthly/weekly spending trends
- Budget limit warnings
- Export reports to PDF or HTML
- Interactive web interface

---

**Note**: This is a learning project demonstrating Python development best practices including testing, CI/CD, and human-AI collaboration.
