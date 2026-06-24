import pandas as pd

# Read CSV
df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Sort data
df = df.sort_values(['amfi_code', 'date'])

# Fill missing NAV values
df['nav'] = df.groupby('amfi_code')['nav'].ffill()

# Remove duplicates
df = df.drop_duplicates()

# Keep only valid NAV values
df = df[df['nav'] > 0]

# Save cleaned CSV
df.to_csv(
    "data/processed/nav_history.csv",
    index=False
)

print("nav_history.csv cleaned successfully!")
