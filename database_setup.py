import sqlite3
import pandas as pd

# Connect to SQLite database (or create one)
conn = sqlite3.connect('retail_sales.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    product TEXT,
    category TEXT,
    region TEXT,
    quantity INTEGER,
    revenue REAL
)''')

# Load sample CSV
data = pd.read_csv('sales_data.csv')
data.to_sql('sales', conn, if_exists='replace', index=False)

print("Database setup complete! Data inserted successfully.")
conn.close()
