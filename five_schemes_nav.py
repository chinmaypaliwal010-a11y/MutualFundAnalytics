import requests
import pandas as pd

schemes = {
    "SBI Bluechip": 119551,
    "ICICI Bluechip": 120503,
    "Nippon Large Cap": 118632,
    "Axis Bluechip": 119092,
    "Kotak Bluechip": 120823
}
data = []

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"
    response = requests.get(url)

    if response.status_code ==200:
        result = response.json()

        data.append({
            "scheme": name,
            "AMFI_code": code,
            "latest_NAV": result ["data"][0]["nav"],
            "date": result["data"][0]["date"]
        })

        df = pd.DataFrame(data)
        print(df)
        df.to_csv("Data/Raw/five_schemes_nav.csv", index=False)
        print("saved successfully")



        