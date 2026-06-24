import pandas as pd

# Load CSV
df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

print("Original Shape:", df.shape)

# 1. Fix Date Format

df['transaction_date'] = pd.to_datetime(
    df['transaction_date'],
    errors='coerce'
)

# 2. Standardize Transaction Type

df['transaction_type'] = (
    df['transaction_type']
    .astype(str)
    .str.strip()
    .str.upper()
)


# 3. Validate Amount > 0

df = df[df['amount_inr'] > 0]

# 4. Standardize KYC Status

df['kyc_status'] = (
    df['kyc_status']
    .astype(str)
    .str.strip()
    .str.upper()
)

# Allowed values
valid_kyc = [
    'VERIFIED',
    'PENDING',
    'REJECTED'
]

df = df[
    df['kyc_status'].isin(valid_kyc)
]


# 5. Remove Duplicates

df = df.drop_duplicates()

# 6. Check Missing Values

print("\nMissing Values:")
print(df.isnull().sum())

# 7. Save Clean File

df.to_csv(
    "data/processed/08_investor_transactions.csv",
    index=False
)

print("\nCleaned Shape:", df.shape)
print("\nInvestor Transactions Cleaning Completed")

print(df['transaction_type'].unique())
print(df['kyc_status'].unique())