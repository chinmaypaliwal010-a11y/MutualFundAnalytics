import sqlite3

conn = sqlite3.connect(
    "bluestock_mf.db"
)

cursor = conn.cursor()

with open(
    "SQL/schema.sql",
    "r"
) as file:

    sql_script = file.read()

cursor.executescript(
    sql_script
)

conn.commit()

print("Tables Created")

conn.close()