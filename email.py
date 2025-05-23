import requests

HIBP_API_KEY = ""  # Put your HaveIBeenPwned API key here if you have one

def check_email_breaches(email):
    if not HIBP_API_KEY:
        return []
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {"hibp-api-key": HIBP_API_KEY, "User-Agent": "OSINT-Tool"}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.json()
    return []