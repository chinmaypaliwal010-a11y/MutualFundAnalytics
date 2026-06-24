import sqlite3

conn = sqlite3.connect(
    "bluestock_mf.db"
)

print("Database Created")

conn.close()