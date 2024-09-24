import datetime
import os

def get_greeting():
    now = datetime.datetime.now()
    hour = now.hour

    if 5 <= hour < 12:
        return "Hey, Good morning !"
    elif 12 <= hour < 17:
        return "Hello, Good afternoon !"
    else:
        return "Hi, Good evening !"

# Path to your Python script (adjust as needed)
script_path = "greeting.py"

# Execute the script
os.system(f"python {script_path}")