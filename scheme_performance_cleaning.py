import pandas as pd

# Load CSV
df = pd.read_csv(
    "Data/raw/07_scheme_performance.csv"
)

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Numeric columns
numeric_cols = [
    'return_1yr_pct',
    'return_3yr_pct',
    'return_5yr_pct',
    'benchmark_3yr_pct',
    'alpha',
    'beta',
    'sharpe_ratio',
    'sortino_ratio',
    'std_dev_ann_pct',
    'max_drawdown_pct',
    'aum_crore',
    'expense_ratio_pct',
    'morningstar_rating'
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors='coerce'
    )

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Expense Ratio Validation
expense_anomalies = df[
    (df['expense_ratio_pct'] < 0.1) |
    (df['expense_ratio_pct'] > 2.5)
]

print(
    "\nExpense Ratio Anomalies:",
    len(expense_anomalies)
)

# Keep valid expense ratios only
df = df[
    (df['expense_ratio_pct'] >= 0.1) &
    (df['expense_ratio_pct'] <= 2.5)
]

# Remove rows where return values missing
df = df.dropna(
    subset=[
        'return_1yr_pct',
        'return_3yr_pct',
        'return_5yr_pct'
    ]
)

# Save cleaned CSV
df.to_csv(
    "Data/processed/07_scheme_performance.csv",
    index=False
)

print("\nCleaned Shape:", df.shape)
print("\nScheme Performance Cleaning Completed")