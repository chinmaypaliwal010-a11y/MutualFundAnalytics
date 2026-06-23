import pandas as pd
fund_master = pd.read_csv("Data/Raw/01_fund_master.csv")
nav_history = pd.read_csv("Data/Raw/02_nav_history.csv")

missing_codes = set (fund_master["amfi_code"]) - set (nav_history["amfi_code"])

print("Missing codes :")
print(missing_codes)

print("total missing :", len(missing_codes))
