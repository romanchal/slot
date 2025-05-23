import requests

NUMVERIFY_API_KEY = "239896282ce8701a0d89d839a1455f4e"

def get_phone_info(phone):
    url = f"http://apilayer.net/api/validate?access_key={NUMVERIFY_API_KEY}&number={phone}&format=1"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        if data.get("valid"):
            return data
    return None