import pandas as pd
import os

folder = "data/raw"

for file in os.listdir(folder):
    if file.endswith(".csv"):
        path = os.path.join(folder, file)

        df = pd.read_csv(path)

        print("\n====================")
        print("File:", file)

        print("Shape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values :")
        print(df.isnull().sum())

        print("\nDuplicate Rows :")
        print(df.duplicated().sum())

        print("\nTotal Missing Values :")
        print(df.isnull().sum().sum())

