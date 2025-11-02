# Interactive Sales Prediction System

### A Python-based Desktop Application for Sales Analysis & Forecasting

Combining **Machine Learning**, **SQL Database**, and a **Tkinter GUI** to help users analyze, visualize, and predict future sales revenue.

---

## Overview

The **Interactive Sales Prediction System** is a standalone desktop application built with **Python** that helps businesses and individuals manage their sales data efficiently and predict future revenue trends.  
It integrates **Data Science** and **Database Management** concepts in a simple and user-friendly GUI using **Tkinter**.

This project bridges the gap between traditional sales management and modern predictive analytics by combining:

- **SQLite** for local data storage,
- **Pandas** and **NumPy** for data processing,
- **Scikit-learn** for regression-based prediction, and
- **Matplotlib** for visual representation of trends.

Users can add, view, delete, and analyze their data directly from the interface — making this a perfect educational and real-world utility tool.

---

## Tech Stack

| Component            | Technology Used                  |
| -------------------- | -------------------------------- |
| **Language**         | Python 3                         |
| **Frontend (GUI)**   | Tkinter                          |
| **Database**         | SQLite3                          |
| **Data Handling**    | Pandas, NumPy                    |
| **Machine Learning** | Scikit-learn (Linear Regression) |
| **Visualization**    | Matplotlib                       |

---

## Features

- **Data Entry & Management** – Add, delete, or view monthly revenue and expenses directly through the GUI.
- **Data Visualization** – Displays bar and line charts representing sales performance.
- **Machine Learning Prediction** – Predicts the next month’s revenue using Linear Regression.
- **Local Database Integration** – Saves all records persistently in `sales.db` (SQLite).
- **Interactive GUI** – Built using Tkinter for simple and clean user experience.
- **Auto Graph Generation** – Displays revenue trends and prediction lines dynamically.
- **Offline Functionality** – Works completely offline, with no internet dependency.

---

## Project Structure

```
Interactive-Sales-Prediction/
│
├── main.py                # Main Tkinter + ML application
├── sales.db               # SQLite database (auto-created)
├── requirements.txt        # Required dependencies
├── README.md              # Project documentation
└── report.pdf             # (Optional) Generated business report
```

---

## How to Run

### Clone the Repository

```bash
git clone https://github.com/<your-username>/Interactive-Sales-Prediction.git
cd Interactive-Sales-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

> **requirements.txt**
>
> ```
> pandas
> numpy
> matplotlib
> scikit-learn
> ```

### Run the Application

```bash
python main.py
```

---

## Usage Guide

1. **Launch the app** using `python main.py`
2. **Enter data**: Type month, revenue (₹), and expenses (₹)
3. Click **➕ Add Record** to store in the database
4. Click **📋 View Data** to display all saved entries
5. Click **🔮 Predict Next Month** to view forecast and graph
6. Click **🗑️ Delete Record** to remove a month’s data
7. Click **❌ Exit** to close the app safely

---

## Machine Learning Overview

The system uses a **Linear Regression** model to forecast future sales based on previous months’ revenue.

Mathematical Formula:

```
y = m*x + c
```

Where:

- `x` = Month number
- `y` = Predicted revenue
- `m` = Growth rate (slope)
- `c` = Base revenue

The model is trained each time new data is added, ensuring accurate and dynamic predictions.

---

## Database Schema

| Field      | Type    | Description                |
| ---------- | ------- | -------------------------- |
| `id`       | INTEGER | Auto-increment primary key |
| `month`    | TEXT    | Month name (e.g., January) |
| `revenue`  | INTEGER | Monthly revenue in ₹       |
| `expenses` | INTEGER | Monthly expenses in ₹      |

---

## Author

**Saurav Sharma**  
MCA Student – Data Science & Software Development  
saurav@example.com  
Passionate about AI, ML, and Full Stack Development

---

## License

This project is licensed under the **MIT License** — you’re free to use, modify, and distribute it with proper credit.
