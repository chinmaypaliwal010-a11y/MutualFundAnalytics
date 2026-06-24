import pandas as pd
import os
import sqlite3
from sqlalchemy import create_engine

# SQLite Database Connection
engine = create_engine("sqlite:///bluestock_mf.db")

# Processed Folder Path
folder = "Data/processed"

print("Loading CSV files into SQLite...\n")

# Load all CSVs into SQLite
for file in os.listdir(folder):

    if file.endswith(".csv"):

        file_path = os.path.join(folder, file)

        table_name = file.replace(".csv", "")

        df = pd.read_csv(file_path)

        csv_rows = len(df)

        # Load into SQLite
        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(f"Loaded: {table_name} ({csv_rows} rows)")

print("\nAll datasets loaded successfully!")


# Verify Row Counts


print("\nVerifying row counts...\n")

conn = sqlite3.connect("bluestock_mf.db")

for file in os.listdir(folder):

    if file.endswith(".csv"):

        table_name = file.replace(".csv", "")

        file_path = os.path.join(folder, file)

        csv_rows = len(pd.read_csv(file_path))

        query = f"SELECT COUNT(*) as cnt FROM '{table_name}'"

        db_rows = pd.read_sql(query, conn).iloc[0, 0]

        status = "PASS" if csv_rows == db_rows else "FAIL"

        print(
            f"{table_name}: "
            f"CSV={csv_rows}, "
            f"DB={db_rows} --> {status}"
        )

conn.close()

print("\nVerification Completed!")