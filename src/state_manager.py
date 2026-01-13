import json
import os

STATE_FILE = "processed_ids.json"


def load_processed_ids():
    if not os.path.exists(STATE_FILE):
        return set()

    with open(STATE_FILE, "r") as f:
        return set(json.load(f))


def save_processed_ids(processed_ids):
    with open(STATE_FILE, "w") as f:
        json.dump(list(processed_ids), f, indent=2)
