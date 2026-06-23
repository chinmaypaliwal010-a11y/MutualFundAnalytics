import requests
import pandas as pd

scheme_codes = [
    119551,
    120503,
    118632,
    119092,
    120841
]

all_data = []

for code in scheme_codes:
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        df = pd.DataFrame(data["data"])

        df["scheme_code"] = code
        df["scheme_name"] = data["meta"]["scheme_name"]

        all_data.append(df)

combined_df = pd.concat(all_data, ignore_index=True)

combined_df.to_csv(
    "Data/Raw/live_nav.csv",
    index=False
)

print("CSV Saved Successfully")