# memory.py
import json
import time
import os
from config import ALERT_COOLDOWN_SECONDS

HISTORY_FILE = "history.json"

def _load_history():
    if not os.path.exists(HISTORY_FILE):
        return {}
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)

def _save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def should_alert(alert_type):
    history = _load_history()
    last_time = history.get(alert_type)

    if last_time is None:
        return True

    return (time.time() - last_time) > ALERT_COOLDOWN_SECONDS

def record_alert(alert_type):
    history = _load_history()
    history[alert_type] = time.time()
    _save_history(history)
