import sqlite3
import pandas as pd
import os

# STRATEGY: Database Automation (ETL)
# "Take this CSV dump and load it into our database."
# This is a fundamental Data Engineering task.
# Concepts: SQL Connectivity, Cursor, Transactions, Pandas Interaction.

DB_NAME = "corporate_data.db"
CSV_FILE = "employees.csv"

def generate_csv():
    # Create dummy data
    data = {
        'id': [101, 102, 103, 104, 105],
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
        'salary': [60000, 80000, 75000, 82000, 62000]
    }
    df = pd.DataFrame(data)
    df.to_csv(CSV_FILE, index=False)
    print(f"Created {CSV_FILE}")

def load_csv_to_sql():
    print("Loading CSV into SQLite...")
    
    # 1. Connect to DB (Creates it if not exists)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # 2. Create Table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        salary INTEGER
    );
    """
    cursor.execute(create_table_query)
    
    # 3. Read CSV
    if not os.path.exists(CSV_FILE):
        generate_csv()
    
    df = pd.read_csv(CSV_FILE)
    
    # 4. Insert Data (Pandas makes this easy)
    # if_exists='replace' drops table if exists, 'append' adds to it
    df.to_sql('employees', conn, if_exists='replace', index=False)
    
    print(f"Successfully loaded {len(df)} rows into table 'employees'.")
    
    # 5. Verify
    print("\n--- Verifying Data from DB ---")
    cursor.execute("SELECT * FROM employees WHERE department='IT'")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        
    conn.close()

if __name__ == "__main__":
    # Requirement: pip install pandas
    load_csv_to_sql()
