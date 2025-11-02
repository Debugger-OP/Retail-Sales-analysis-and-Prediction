import sqlite3
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox

# -----------------------------
# Database setup
# -----------------------------
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    month TEXT,
    revenue INTEGER,
    expenses INTEGER
)
""")
conn.commit()

# -----------------------------
# Core functions
# -----------------------------
def add_record():
    month = month_entry.get().capitalize()
    revenue = revenue_entry.get()
    expenses = expenses_entry.get()

    if not month or not revenue or not expenses:
        messagebox.showwarning("Input Error", "Please fill all fields!")
        return

    try:
        revenue = int(revenue)
        expenses = int(expenses)
        cursor.execute("INSERT INTO sales (month, revenue, expenses) VALUES (?, ?, ?)", (month, revenue, expenses))
        conn.commit()
        messagebox.showinfo("Success", f"Data for {month} added successfully!")
        month_entry.delete(0, END)
        revenue_entry.delete(0, END)
        expenses_entry.delete(0, END)
    except ValueError:
        messagebox.showerror("Invalid Input", "Revenue and Expenses must be numbers!")

def view_data():
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    if df.empty:
        messagebox.showinfo("No Data", "No records found.")
        return
    print("\n📊 Current Sales Data:\n", df)
    messagebox.showinfo("Data Loaded", f"{len(df)} records loaded. Check terminal for details.")

def predict_next_month():
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    if len(df) < 2:
        messagebox.showwarning("Not Enough Data", "Add at least 2 months of data to predict.")
        return

    df['month_num'] = range(1, len(df) + 1)
    X = df[['month_num']]
    y = df['revenue']

    model = LinearRegression()
    model.fit(X, y)

    next_month = pd.DataFrame({'month_num': [len(df) + 1]})
    predicted = model.predict(next_month)[0]

    messagebox.showinfo("Prediction Result", f"Predicted Revenue for Next Month: ₹{predicted:,.2f}")

    # Plot chart
    plt.figure(figsize=(7,4))
    plt.plot(df['month'], df['revenue'], marker='o', label='Actual Revenue')
    plt.axhline(predicted, color='red', linestyle='--', label='Predicted Next Month')
    plt.title('Revenue Trend & Prediction')
    plt.xlabel('Month')
    plt.ylabel('Revenue (₹)')
    plt.legend()
    plt.tight_layout()
    plt.show()

# -----------------------------
# Tkinter GUI setup
# -----------------------------
root = Tk()
root.title("💼 Sales Prediction System")
root.geometry("420x380")
root.resizable(False, False)
root.config(bg="#f2f2f2")

Label(root, text="📊 Sales Prediction Dashboard", font=("Arial", 16, "bold"), bg="#f2f2f2").pack(pady=10)

frame = Frame(root, bg="#f2f2f2")
frame.pack(pady=10)

Label(frame, text="Month:", font=("Arial", 12), bg="#f2f2f2").grid(row=0, column=0, sticky=W, padx=5, pady=5)
month_entry = Entry(frame, font=("Arial", 12), width=25)
month_entry.grid(row=0, column=1, padx=5, pady=5)

Label(frame, text="Revenue (₹):", font=("Arial", 12), bg="#f2f2f2").grid(row=1, column=0, sticky=W, padx=5, pady=5)
revenue_entry = Entry(frame, font=("Arial", 12), width=25)
revenue_entry.grid(row=1, column=1, padx=5, pady=5)

Label(frame, text="Expenses (₹):", font=("Arial", 12), bg="#f2f2f2").grid(row=2, column=0, sticky=W, padx=5, pady=5)
expenses_entry = Entry(frame, font=("Arial", 12), width=25)
expenses_entry.grid(row=2, column=1, padx=5, pady=5)

Button(root, text="➕ Add Record", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
       width=18, command=add_record).pack(pady=10)

Button(root, text="📋 View Data", font=("Arial", 12, "bold"), bg="#2196F3", fg="white",
       width=18, command=view_data).pack(pady=5)

Button(root, text="🔮 Predict Next Month", font=("Arial", 12, "bold"), bg="#FF9800", fg="white",
       width=18, command=predict_next_month).pack(pady=5)

Button(root, text="❌ Exit", font=("Arial", 12, "bold"), bg="#f44336", fg="white",
       width=18, command=root.quit).pack(pady=15)

Label(root, text="Data stored in sales.db (SQLite)", font=("Arial", 10), bg="#f2f2f2").pack()

root.mainloop()