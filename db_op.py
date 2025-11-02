import sqlite3
conn = sqlite3.connect("sales.db")
cur = conn.cursor()
cur.execute("DELETE FROM sales")
conn.commit()
conn.close()
