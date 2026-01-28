import pandas as pd
import numpy as np
import os

# STRATEGY: Data Transformation (ETL) & Reporting
# This script simulates an "Extract, Transform, Load" process.
# We generate raw data (Extract), process it with Pandas (Transform), and save an Excel report (Load).
# Concepts: DataFrames, Pivot Tables, Excel Automation.

def generate_dummy_data():
    """Generates a random CSV file to simulate raw business data."""
    print("Generating raw data...")
    data = {
        'Date': pd.date_range(start='2024-01-01', periods=100),
        'Product': np.random.choice(['Laptop', 'Mouse', 'Monitor', 'Keyboard'], 100),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], 100),
        'Sales': np.random.randint(100, 5000, 100)
    }
    df = pd.DataFrame(data)
    df.to_csv('raw_sales_data.csv', index=False)
    print("Created 'raw_sales_data.csv'")

def automate_report():
    print("Processing report...")
    if not os.path.exists('raw_sales_data.csv'):
        generate_dummy_data()
        
    df = pd.read_csv('raw_sales_data.csv')
    
    # TRANSFORMATION 1: Calculate Total Revenue per Region
    region_pivot = df.pivot_table(index='Region', columns='Product', values='Sales', aggfunc='sum')
    
    # TRANSFORMATION 2: Calculate Average Sales
    avg_sales = df.groupby('Product')['Sales'].mean()
    
    # OUTPUT: Writing to a Multi-sheet Excel file
    # This is a common automation task in finance/admin roles.
    output_file = 'Executive_Sales_Report.xlsx'
    
    with pd.ExcelWriter(output_file) as writer:
        df.to_excel(writer, sheet_name='Raw Data', index=False)
        region_pivot.to_excel(writer, sheet_name='Regional Summary')
        avg_sales.to_excel(writer, sheet_name='Product Perf.')
    
    print(f"Report generated successfully: {output_file}")
    print("Check the 'Regional Summary' sheet in the Excel file.")

if __name__ == "__main__":
    # Requirement: pip install pandas openpyxl
    automate_report()
