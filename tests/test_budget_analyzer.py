"""
Unit tests for budget_analyzer module.

Tests cover:
- CSV reading with valid and invalid data
- Total spending calculation
- Category spending calculation
- Top category identification
- Average spending calculation
- Edge cases (empty data, invalid formats)
"""

import pytest
import sys
import tempfile
from pathlib import Path

# Add src directory to path so we can import the module
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from budget_analyzer import (
    read_budget_csv,
    calculate_total_spending,
    calculate_category_spending,
    find_top_category,
    calculate_average_spending
)


@pytest.fixture
def sample_csv_file():
    """Create a temporary CSV file with sample budget data."""
    content = """date,category,description,amount
2026-04-01,Food,Lunch,12.50
2026-04-02,Transportation,Bus ticket,2.75
2026-04-03,School,Notebook,5.99
2026-04-04,Food,Dinner,18.20
2026-04-05,Transportation,Train ticket,15.00"""
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
        f.write(content)
        temp_path = f.name
    
    yield temp_path
    
    # Cleanup
    Path(temp_path).unlink()


@pytest.fixture
def invalid_csv_file():
    """Create a temporary CSV file with some invalid data."""
    content = """date,category,description,amount
2026-04-01,Food,Lunch,12.50
2026-04-02,Transportation,Bus ticket,invalid_amount
2026-04-03,School,Notebook,5.99
2026-04-04,Food,Dinner,
2026-04-05,Entertainment,Movie,25.00"""
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
        f.write(content)
        temp_path = f.name
    
    yield temp_path
    
    # Cleanup
    Path(temp_path).unlink()


@pytest.fixture
def empty_csv_file():
    """Create a temporary CSV file with only headers."""
    content = """date,category,description,amount"""
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
        f.write(content)
        temp_path = f.name
    
    yield temp_path
    
    # Cleanup
    Path(temp_path).unlink()


def test_read_valid_csv(sample_csv_file):
    """Test reading a valid CSV file."""
    records = read_budget_csv(sample_csv_file)
    
    assert len(records) == 5
    assert records[0]['category'] == 'Food'
    assert records[0]['amount'] == '12.50'
    assert records[2]['description'] == 'Notebook'


def test_read_csv_with_invalid_data(invalid_csv_file):
    """Test that invalid data rows are skipped."""
    records = read_budget_csv(invalid_csv_file)
    
    # Should only have 3 valid records (invalid_amount and empty amount are skipped)
    assert len(records) == 3
    assert records[0]['amount'] == '12.50'
    assert records[1]['amount'] == '5.99'
    assert records[2]['amount'] == '25.00'


def test_read_csv_file_not_found():
    """Test that FileNotFoundError is raised for non-existent files."""
    with pytest.raises(FileNotFoundError):
        read_budget_csv('nonexistent_file.csv')


def test_read_empty_csv(empty_csv_file):
    """Test reading a CSV file with no data rows."""
    records = read_budget_csv(empty_csv_file)
    
    assert len(records) == 0


def test_calculate_total_spending(sample_csv_file):
    """Test total spending calculation."""
    records = read_budget_csv(sample_csv_file)
    total = calculate_total_spending(records)
    
    # 12.50 + 2.75 + 5.99 + 18.20 + 15.00 = 54.44
    assert abs(total - 54.44) < 0.01


def test_calculate_total_spending_empty():
    """Test total spending with empty data."""
    records = []
    total = calculate_total_spending(records)
    
    assert total == 0.0


def test_calculate_category_spending(sample_csv_file):
    """Test category spending calculation."""
    records = read_budget_csv(sample_csv_file)
    category_spending = calculate_category_spending(records)
    
    assert len(category_spending) == 3
    assert abs(category_spending['Food'] - 30.70) < 0.01  # 12.50 + 18.20
    assert abs(category_spending['Transportation'] - 17.75) < 0.01  # 2.75 + 15.00
    assert abs(category_spending['School'] - 5.99) < 0.01


def test_calculate_category_spending_empty():
    """Test category spending with empty data."""
    records = []
    category_spending = calculate_category_spending(records)
    
    assert len(category_spending) == 0


def test_find_top_category(sample_csv_file):
    """Test finding the top spending category."""
    records = read_budget_csv(sample_csv_file)
    category_spending = calculate_category_spending(records)
    top_category, top_amount = find_top_category(category_spending)
    
    assert top_category == 'Food'
    assert abs(top_amount - 30.70) < 0.01


def test_find_top_category_empty():
    """Test finding top category with empty data."""
    category_spending = {}
    
    with pytest.raises(ValueError):
        find_top_category(category_spending)


def test_calculate_average_spending(sample_csv_file):
    """Test average spending calculation."""
    records = read_budget_csv(sample_csv_file)
    average = calculate_average_spending(records)
    
    # 54.44 / 5 = 10.888
    assert abs(average - 10.888) < 0.01


def test_calculate_average_spending_empty():
    """Test average spending with empty data."""
    records = []
    average = calculate_average_spending(records)
    
    assert average == 0.0


def test_csv_with_whitespace():
    """Test that CSV fields with extra whitespace are handled correctly."""
    content = """date,category,description,amount
2026-04-01,  Food  ,  Lunch  ,  12.50  
2026-04-02, Transportation , Bus ticket , 2.75 """
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
        f.write(content)
        temp_path = f.name
    
    try:
        records = read_budget_csv(temp_path)
        
        assert len(records) == 2
        assert records[0]['category'] == 'Food'  # Whitespace should be stripped
        assert records[0]['amount'] == '12.50'
    finally:
        Path(temp_path).unlink()


def test_multiple_categories_same_amount():
    """Test handling when multiple categories have the same spending."""
    content = """date,category,description,amount
2026-04-01,Food,Lunch,10.00
2026-04-02,Entertainment,Movie,10.00"""
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
        f.write(content)
        temp_path = f.name
    
    try:
        records = read_budget_csv(temp_path)
        category_spending = calculate_category_spending(records)
        top_category, top_amount = find_top_category(category_spending)
        
        # Either category could be "top" since they're equal
        assert top_category in ['Food', 'Entertainment']
        assert abs(top_amount - 10.00) < 0.01
    finally:
        Path(temp_path).unlink()
