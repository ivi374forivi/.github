import json
from datetime import datetime

SUBSCRIPTIONS_FILE = ".github/subscriptions.json"

def direct_fix():
    """Forcefully resets the Jules_Agent quota to today."""
    try:
        with open(SUBSCRIPTIONS_FILE, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error: Could not read subscriptions file.")
        return

    found = False
    for sub in data.get("subscriptions", []):
        if sub.get("name") == "Jules_Agent":
            today_str = datetime.now().strftime("%Y-%m-%d")
            sub["last_reset"] = today_str
            sub["usage"] = 0
            found = True
            break

    if found:
        with open(SUBSCRIPTIONS_FILE, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Successfully reset Jules_Agent quota. Last reset date is now {today_str}.")
    else:
        print("Error: Jules_Agent subscription not found.")

if __name__ == "__main__":
    direct_fix()