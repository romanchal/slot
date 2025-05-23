import subprocess
import json

def run_socialscan(username):
    try:
        result = subprocess.run(["socialscan", username, "--json", "socialscan_output.json"], capture_output=True, text=True)
        if result.returncode == 0:
            with open("socialscan_output.json") as f:
                return json.load(f)
    except Exception:
        pass
    return None