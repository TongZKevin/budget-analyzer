#!/usr/bin/env python3
"""
Budget Analyzer - A simple command-line tool for analyzing spending data.

This tool reads CSV files containing budget/spending data and generates
analysis reports including total spending, category breakdowns, and statistics.
"""

import csv
import sys
from pathlib import Path
from typing import List, Dict, Tuple
from collections import defaultdict


def read_budget_csv(file_path: str) -> List[Dict[str, str]]:
    """
    Read and parse CSV file containing budget data.
    
    Args:
        file_path: Path to the CSV file
        
    Returns:
        List of dictionaries containing valid budget records
        
    Raises:
        FileNotFoundError: If the CSV file doesn't exist
    """
    if not Path(file_path).exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    valid_records = []
    
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for line_num, row in enumerate(reader, start=2):  # start=2 because line 1 is header
            try:
                # Strip whitespace from all fields
                row = {k.strip(): v.strip() for k, v in row.items()}
                
                # Validate required fields exist
                if not all(k in row for k in ['date', 'category', 'description', 'amount']):
                    print(f"Warning: Line {line_num} missing required fields, skipping")
                    continue
                
                # Validate amount is a valid number
                try:
                    float(row['amount'])
                except ValueError:
                    print(f"Warning: Line {line_num} has invalid amount '{row['amount']}', skipping")
                    continue
                
                valid_records.append(row)
                
            except Exception as e:
                print(f"Warning: Error processing line {line_num}: {e}, skipping")
                continue
    
    return valid_records


def calculate_total_spending(records: List[Dict[str, str]]) -> float:
    """
    Calculate total spending from all records.
    
    Args:
        records: List of budget records
        
    Returns:
        Total amount spent
    """
    return sum(float(record['amount']) for record in records)


def calculate_category_spending(records: List[Dict[str, str]]) -> Dict[str, float]:
    """
    Calculate spending by category.
    
    Args:
        records: List of budget records
        
    Returns:
        Dictionary mapping category names to total spending
    """
    category_totals = defaultdict(float)
    
    for record in records:
        category = record['category']
        amount = float(record['amount'])
        category_totals[category] += amount
    
    return dict(category_totals)


def find_top_category(category_spending: Dict[str, float]) -> Tuple[str, float]:
    """
    Find the category with the highest spending.
    
    Args:
        category_spending: Dictionary of category totals
        
    Returns:
        Tuple of (category_name, amount)
        
    Raises:
        ValueError: If no categories exist
    """
    if not category_spending:
        raise ValueError("No spending data available")
    
    top_category = max(category_spending.items(), key=lambda x: x[1])
    return top_category


def calculate_average_spending(records: List[Dict[str, str]]) -> float:
    """
    Calculate average spending per transaction.
    
    Args:
        records: List of budget records
        
    Returns:
        Average amount per transaction
    """
    if not records:
        return 0.0
    
    total = calculate_total_spending(records)
    return total / len(records)


def print_report(records: List[Dict[str, str]]) -> None:
    """
    Print a formatted analysis report to the console.
    
    Args:
        records: List of budget records
    """
    if not records:
        print("\n" + "=" * 60)
        print("BUDGET ANALYSIS REPORT")
        print("=" * 60)
        print("\nNo valid data to analyze.")
        print("=" * 60)
        return
    
    # Calculate all statistics
    total_spending = calculate_total_spending(records)
    category_spending = calculate_category_spending(records)
    top_category, top_amount = find_top_category(category_spending)
    average_spending = calculate_average_spending(records)
    
    # Print header
    print("\n" + "=" * 60)
    print("BUDGET ANALYSIS REPORT")
    print("=" * 60)
    
    # Print summary statistics
    print(f"\nTotal Transactions: {len(records)}")
    print(f"Total Spending: ${total_spending:.2f}")
    print(f"Average per Transaction: ${average_spending:.2f}")
    
    # Print category breakdown
    print("\n" + "-" * 60)
    print("SPENDING BY CATEGORY")
    print("-" * 60)
    
    # Sort categories by amount (descending)
    sorted_categories = sorted(category_spending.items(), key=lambda x: x[1], reverse=True)
    
    for category, amount in sorted_categories:
        percentage = (amount / total_spending) * 100
        print(f"{category:20s} ${amount:>10.2f}  ({percentage:>5.1f}%)")
    
    # Print top category
    print("\n" + "-" * 60)
    print(f"HIGHEST SPENDING CATEGORY: {top_category} (${top_amount:.2f})")
    print("=" * 60 + "\n")


def generate_chart(category_spending: Dict[str, float], output_path: str = "output/category_spending.png") -> None:
    """
    Generate a bar chart of category spending (optional feature).
    
    Args:
        category_spending: Dictionary of category totals
        output_path: Path where to save the chart
    """
    try:
        import matplotlib.pyplot as plt
        
        # Create output directory if it doesn't exist
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        
        # Sort categories by spending
        sorted_data = sorted(category_spending.items(), key=lambda x: x[1], reverse=True)
        categories = [item[0] for item in sorted_data]
        amounts = [item[1] for item in sorted_data]
        
        # Create bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(categories, amounts, color='steelblue')
        plt.xlabel('Category')
        plt.ylabel('Amount ($)')
        plt.title('Spending by Category')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        # Save chart
        plt.savefig(output_path)
        print(f"Chart saved to: {output_path}")
        
    except ImportError:
        print("\nNote: matplotlib not installed. Skipping chart generation.")
        print("Install with: pip install matplotlib")


def main() -> int:
    """
    Main entry point for the budget analyzer.
    
    Returns:
        Exit code (0 for success, 1 for error)
    """
    # Check command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python budget_analyzer.py <path_to_csv_file>")
        print("Example: python budget_analyzer.py data/sample_budget.csv")
        return 1
    
    csv_file_path = sys.argv[1]
    
    try:
        # Read and parse CSV data
        print(f"Reading budget data from: {csv_file_path}")
        records = read_budget_csv(csv_file_path)
        
        print(f"Successfully loaded {len(records)} valid records")
        
        # Print analysis report
        print_report(records)
        
        # Optionally generate chart if matplotlib is available
        if records:
            category_spending = calculate_category_spending(records)
            generate_chart(category_spending)
        
        return 0
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
