"""
data_store.py

This file's only job is saving data to a file, and loading it back.
We used a JSON file because JSON is just text that looks like Python
dictionaries and lists, so it is easy to save and read back.

We keep our outreach data file inside the "data" folder.
"""

import json
import os

# This is the path to the file where we keep all our saved data.
# os.path.join makes sure this works on Windows, Mac, and Linux.
DATA_FILE = os.path.join("data", "outreach_data.json")


def save_data(records, next_id):
    """
    Save our records and next_id into the JSON file.
    We call this every time something changes (add, update, delete).
    """
    data_to_save = {
        "records": records,
        "next_id": next_id
    }

    try:
        file = open(DATA_FILE, "w")
        json.dump(data_to_save, file, indent=2)
        file.close()
    except OSError:
        print("Sorry, something went wrong while saving the data.")


def load_data():
     """
        Try to open the JSON file and read our saved data from it.
        If the file does not exist yet, or cannot be read, we just
        start with empty lists instead of crashing the program.
     """
    try:
        file = open(DATA_FILE, "r")
        data = json.load(file)
        file.close()

        records = data["records"]
        next_id = data["next_id"]
        return records, next_id

    except FileNotFoundError:
        # This happens the very first time the program runs.
        empty_records = {"Organization": [], "Individual": []}
        return empty_records, 1

    except json.JSONDecodeError:
        # This happens if the file exists but is broken or empty.
        print("The saved data file could not be read. Starting fresh.")
        empty_records = {"Organization": [], "Individual": []}
        return empty_records, 1
