import requests

# 1. 'r =' ko requests.get ke sath ek hi line mein likhein
# 2. URL ko 'api.mfai.in' se badalkar 'api.mfapi.in' karein
url = "https://api.mfapi.in/mf/119551"

r = requests.get(url)

print("Status Code:", r.status_code)
print("Response Status:", r.json()["status"])